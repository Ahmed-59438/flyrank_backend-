"""
Configuration settings for the Web Scraping & Data Extraction Pipeline.

Centralizing configuration constants avoids hardcoded magic values across modules,
enabling easy parameter adjustments (e.g., rate limits, user-agents, paths) in one place.
"""

from pathlib import Path

# Base Directory Setup
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# Target Web Configuration
BASE_URL = "https://books.toscrape.com/catalogue/page-{page}.html"
START_URL = "https://books.toscrape.com/"

# HTTP Request Configurations
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# Network & Resilience Parameters
REQUEST_TIMEOUT = 10  # Seconds to wait for server response
REQUEST_DELAY = 1.0   # Seconds to pause between page requests (rate limiting)
RETRY_COUNT = 3       # Maximum retry attempts for failed HTTP requests
RETRY_BACKOFF_FACTOR = 1.5  # Multiplier for exponential backoff delay

# Pagination Controls
TOTAL_PAGES = 50      # Target number of catalog pages on books.toscrape.com

# Output File Targets
OUTPUT_JSON_PATH = DATA_DIR / "books.json"
OUTPUT_CSV_PATH = DATA_DIR / "books.csv"
LOG_FILE_PATH = BASE_DIR / "scraper.log"
