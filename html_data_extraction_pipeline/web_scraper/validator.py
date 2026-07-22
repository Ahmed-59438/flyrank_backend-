"""
Data Validator module responsible strictly for schema integrity and quality control.

Filters out incomplete, empty, or corrupted records before data persistence,
ensuring only clean, valid records are saved to files or databases.
"""

from typing import List, Dict, Any
from logger import get_logger

logger = get_logger("validator")


def is_valid_book(book: Dict[str, Any]) -> bool:
    """
    Validates an individual cleaned book dictionary record.

    Checks:
    - Title exists and is not empty.
    - Price is a float and is greater than 0.
    - Availability exists and is not empty.
    - Rating exists and is not empty.

    Args:
        book (Dict[str, Any]): Cleaned book record dictionary.

    Returns:
        bool: True if the record meets all validation criteria, False otherwise.
    """
    title = book.get("title")
    price = book.get("price")
    availability = book.get("availability")
    rating = book.get("rating")

    # 1. Check title
    if not title or not isinstance(title, str):
        logger.warning(f"Validation failed: Invalid or missing title -> {book}")
        return False

    # 2. Check price (must be positive numeric value)
    if price is None or not isinstance(price, (int, float)) or price <= 0:
        logger.warning(f"Validation failed: Invalid price ({price}) for '{title}'")
        return False

    # 3. Check availability
    if not availability or not isinstance(availability, str):
        logger.warning(f"Validation failed: Missing availability for '{title}'")
        return False

    # 4. Check rating
    if not rating or not isinstance(rating, str):
        logger.warning(f"Validation failed: Missing rating for '{title}'")
        return False

    return True


def validate_books(books: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filters a list of cleaned book records, keeping only valid ones.

    Args:
        books (List[Dict[str, Any]]): List of cleaned dictionaries.

    Returns:
        List[Dict[str, Any]]: List of verified valid book dictionaries.
    """
    valid_books = []
    skipped_count = 0

    for book in books:
        if is_valid_book(book):
            valid_books.append(book)
        else:
            skipped_count += 1

    logger.info(
        f"Validation complete. Valid records: {len(valid_books)}, Skipped invalid: {skipped_count}"
    )
    return valid_books
