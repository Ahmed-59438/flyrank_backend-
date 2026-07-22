"""
Pipeline Controller / Main Orchestrator.

Coordinates the end-to-end execution of the web scraping pipeline:
Fetch -> Parse -> Clean -> Validate -> Save

Does not contain low-level scraping, parsing, or saving logic. Strictly orchestrates
the modular flow across catalog pagination.
"""

from config import (
    BASE_URL,
    TOTAL_PAGES,
    OUTPUT_JSON_PATH,
    OUTPUT_CSV_PATH,
)
from logger import get_logger
from scraper import fetch_page
from parser import parse_books
from cleaner import clean_books
from validator import validate_books
from saver import save_data

logger = get_logger("main")


def run_pipeline(total_pages: int = TOTAL_PAGES) -> None:
    """
    Executes the web scraping and data extraction pipeline.

    Args:
        total_pages (int): Number of catalog pages to scrape.
    """
    logger.info("==================================================")
    logger.info("Starting Web Scraping & Data Extraction Pipeline")
    logger.info("==================================================")

    all_valid_books = []

    for page_num in range(1, total_pages + 1):
        # 1. Construct target page URL
        page_url = BASE_URL.format(page=page_num)
        logger.info(f"--- Processing Page {page_num}/{total_pages} ---")

        # 2. HTTP Fetch Layer
        html_content = fetch_page(page_url)
        if not html_content:
            logger.warning(f"Skipping page {page_num} due to fetch failure.")
            continue

        # 3. HTML Parse Layer
        raw_books = parse_books(html_content)
        if not raw_books:
            logger.warning(f"No books extracted from page {page_num}.")
            continue

        # 4. Data Cleaning Layer
        cleaned_books = clean_books(raw_books)

        # 5. Data Validation Layer
        valid_books = validate_books(cleaned_books)

        # 6. Aggregate Valid Records
        all_valid_books.extend(valid_books)
        logger.info(f"Page {page_num} completed. Accumulated valid books: {len(all_valid_books)}")

    # 7. Data Persistence Layer
    if all_valid_books:
        save_data(all_valid_books, OUTPUT_JSON_PATH, OUTPUT_CSV_PATH)
        logger.info("==================================================")
        logger.info(f"Pipeline Completed Successfully! Total Books Saved: {len(all_valid_books)}")
        logger.info("==================================================")
    else:
        logger.error("Pipeline finished but no valid book records were extracted.")


if __name__ == "__main__":
    run_pipeline()
