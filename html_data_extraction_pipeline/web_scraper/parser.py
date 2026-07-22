"""
HTML Parser module responsible ONLY for parsing HTML and extracting raw data fields.

Uses BeautifulSoup to locate book elements on the page and extract title,
price, availability, and rating.
"""

from typing import List, Dict, Any
from bs4 import BeautifulSoup
from logger import get_logger

logger = get_logger("parser")


def parse_books(html_content: str) -> List[Dict[str, Any]]:
    """
    Parses HTML content of a catalog page and extracts raw book information.

    Args:
        html_content (str): Raw HTML string downloaded from the webpage.

    Returns:
        List[Dict[str, Any]]: A list of raw dictionaries containing book details.
    """
    if not html_content:
        logger.warning("Received empty HTML content to parse.")
        return []

    soup = BeautifulSoup(html_content, "lxml")
    book_cards = soup.find_all("article", class_="product_pod")
    
    extracted_books = []

    for card in book_cards:
        try:
            # 1. Extract Title (located inside <h3> <a title="...">)
            title_tag = card.find("h3").find("a")
            title = title_tag.get("title") or title_tag.text

            # 2. Extract Price (located inside <p class="price_color">)
            price_tag = card.find("p", class_="price_color")
            price = price_tag.text if price_tag else ""

            # 3. Extract Availability (located inside <p class="instock availability">)
            availability_tag = card.find("p", class_="instock availability")
            availability = availability_tag.text if availability_tag else ""

            # 4. Extract Rating (located in class name of <p class="star-rating RatingClass">)
            rating_tag = card.find("p", class_="star-rating")
            rating = ""
            if rating_tag:
                # Class list looks like: ['star-rating', 'Three'] -> Rating is second class
                classes = rating_tag.get("class", [])
                rating_classes = [c for c in classes if c != "star-rating"]
                rating = rating_classes[0] if rating_classes else ""

            book = {
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating
            }
            extracted_books.append(book)

        except Exception as err:
            logger.warning(f"Error parsing individual book card: {err}")
            continue

    logger.info(f"Successfully extracted {len(extracted_books)} books from page HTML.")
    return extracted_books
