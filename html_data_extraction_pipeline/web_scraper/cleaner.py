"""
Data Cleaner module responsible strictly for transforming and normalizing raw strings.

Converts raw text fields (e.g., '£51.77', '\\n    In stock\\n') into clean,
standardized Python data types (e.g., 51.77, 'In stock').
"""

import re
from typing import List, Dict, Any
from logger import get_logger

logger = get_logger("cleaner")


def clean_price(raw_price: str) -> float:
    """
    Strips currency symbols and converts raw price string to a float.

    Example: '£51.77' -> 51.77
    """
    if not raw_price:
        return 0.0
    
    # Extract digits and decimal point using regular expression
    match = re.search(r"(\d+\.\d+|\d+)", raw_price)
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            return 0.0
    return 0.0


def clean_string(raw_text: str) -> str:
    """
    Removes leading/trailing whitespace, newlines, and extra internal spaces.
    """
    if not raw_text:
        return ""
    return " ".join(raw_text.split())


def clean_book_record(raw_book: Dict[str, Any]) -> Dict[str, Any]:
    """
    Cleans an individual book record dictionary.
    """
    cleaned_title = clean_string(raw_book.get("title", ""))
    cleaned_price = clean_price(str(raw_book.get("price", "")))
    cleaned_availability = clean_string(raw_book.get("availability", ""))
    cleaned_rating = clean_string(raw_book.get("rating", ""))

    return {
        "title": cleaned_title,
        "price": cleaned_price,
        "availability": cleaned_availability,
        "rating": cleaned_rating
    }


def clean_books(raw_books: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Processes and cleans a list of raw book record dictionaries.

    Args:
        raw_books (List[Dict[str, Any]]): List of raw dictionaries from parser.

    Returns:
        List[Dict[str, Any]]: List of sanitized, clean dictionaries.
    """
    cleaned_list = []
    for raw_book in raw_books:
        cleaned_record = clean_book_record(raw_book)
        cleaned_list.append(cleaned_record)

    logger.info(f"Cleaned {len(cleaned_list)} book records.")
    return cleaned_list
