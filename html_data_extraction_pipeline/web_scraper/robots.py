"""
Robots.txt compliance checker.
"""
from urllib.robotparser import RobotFileParser
from urllib.parse import urljoin, urlparse
from typing import Optional
import requests
from config import BOT_USER_AGENT
from logger import get_logger

logger = get_logger("robots")

# Cached parser instances, keyed by base url scheme + netloc (e.g. https://books.toscrape.com)
_parsers = {}

def _get_robots_url(target_url: str) -> str:
    """
    Constructs the robots.txt URL for the given target URL.
    """
    parsed = urlparse(target_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    return urljoin(base_url, "/robots.txt")

def _get_parser(target_url: str) -> RobotFileParser:
    """
    Gets or initializes the cached RobotFileParser for the target URL's domain.
    """
    parsed = urlparse(target_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    
    if base_url not in _parsers:
        rp = RobotFileParser()
        robots_url = _get_robots_url(target_url)
        logger.info(f"Loading robots.txt from {robots_url}")
        
        try:
            # Fetch using requests to override default urllib User-Agent and set timeout
            response = requests.get(
                robots_url,
                headers={"User-Agent": BOT_USER_AGENT},
                timeout=10
            )
            if response.status_code == 200:
                rp.parse(response.text.splitlines())
                logger.info(f"Successfully loaded and parsed robots.txt for {base_url}")
            elif response.status_code == 404:
                # If robots.txt doesn't exist, all paths are allowed
                logger.info(f"robots.txt not found (404) for {base_url}. Assuming all paths are allowed.")
                rp.parse([])
            else:
                logger.warning(
                    f"Unexpected status code {response.status_code} fetching robots.txt for {base_url}. "
                    "Proceeding with default permissions."
                )
                rp.parse([])
        except Exception as err:
            logger.error(f"Error fetching/parsing robots.txt for {base_url}: {err}. Defaulting to allowed.")
            rp.parse([])
            
        _parsers[base_url] = rp
        
    return _parsers[base_url]

def is_allowed(url: str, user_agent: str = BOT_USER_AGENT) -> bool:
    """
    Checks if the specified User-Agent is allowed to crawl the target URL.
    """
    try:
        rp = _get_parser(url)
        return rp.can_fetch(user_agent, url)
    except Exception as err:
        logger.error(f"Error checking robots.txt permission for {url}: {err}")
        return True

def get_crawl_delay(url: str, user_agent: str = BOT_USER_AGENT) -> Optional[float]:
    """
    Retrieves the Crawl-delay specified in robots.txt for the given User-Agent, if any.
    """
    try:
        rp = _get_parser(url)
        delay = rp.crawl_delay(user_agent)
        return float(delay) if delay is not None else None
    except Exception as err:
        logger.error(f"Error reading Crawl-delay for {url}: {err}")
        return None
