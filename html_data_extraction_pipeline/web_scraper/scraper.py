"""
HTTP Scraper module responsible strictly for downloading webpage content.

Separates network acquisition from data parsing, adhering to the Single
Responsibility Principle (SRP). Handles HTTP requests, retries, timeouts,
and rate limiting.
"""

import time
from typing import Optional
import requests
from config import (
    HEADERS,
    BOT_USER_AGENT,
    REQUEST_TIMEOUT,
    REQUEST_DELAY,
    RETRY_COUNT,
    RETRY_BACKOFF_FACTOR,
)
from logger import get_logger
from robots import is_allowed, get_crawl_delay

logger = get_logger("scraper")


def fetch_page(url: str) -> Optional[str]:
    """
    Downloads raw HTML content from the specified URL with retries and rate limiting.

    Args:
        url (str): Target HTTP/HTTPS URL to download.

    Returns:
        Optional[str]: Raw HTML string if request succeeds (HTTP 200),
                       or None if all retry attempts fail.
    """
    # robots.txt Compliance Check
    if not is_allowed(url, BOT_USER_AGENT):
        logger.error(f"Access disallowed by robots.txt compliance rules for URL: {url}")
        return None

    # Dynamic Rate Limiting: Pause before initiating request to be a polite scraper
    robots_delay = get_crawl_delay(url, BOT_USER_AGENT)
    active_delay = max(REQUEST_DELAY, robots_delay) if robots_delay is not None else REQUEST_DELAY
    if active_delay > REQUEST_DELAY:
        logger.info(f"Using robots.txt crawl-delay of {active_delay}s instead of default {REQUEST_DELAY}s")
    time.sleep(active_delay)

    for attempt in range(1, RETRY_COUNT + 1):
        try:
            logger.info(f"Fetching URL: {url} (Attempt {attempt}/{RETRY_COUNT})")
            
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=REQUEST_TIMEOUT
            )

            # Raise HTTPError if status code is 4xx or 5xx
            response.raise_for_status()

            logger.info(f"Successfully fetched {url} [Status: {response.status_code}]")
            return response.text

        except requests.Timeout:
            logger.warning(
                f"Timeout ({REQUEST_TIMEOUT}s) on attempt {attempt}/{RETRY_COUNT} for {url}"
            )
        except requests.HTTPError as http_err:
            logger.warning(
                f"HTTP Error {response.status_code} on attempt {attempt}/{RETRY_COUNT}: {http_err}"
            )
        except requests.RequestException as req_err:
            logger.warning(
                f"Network error on attempt {attempt}/{RETRY_COUNT} for {url}: {req_err}"
            )

        # Exponential backoff delay before retrying
        if attempt < RETRY_COUNT:
            backoff = REQUEST_DELAY * (RETRY_BACKOFF_FACTOR ** (attempt - 1))
            logger.info(f"Retrying in {backoff:.2f} seconds...")
            time.sleep(backoff)

    logger.error(f"Failed to fetch {url} after {RETRY_COUNT} attempts.")
    return None
