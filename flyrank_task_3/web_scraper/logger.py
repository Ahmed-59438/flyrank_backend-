"""
Logging module for structured, level-based log output.

Replaces standard print statements with Python's built-in logging system.
Configures dual output: streams to console (stdout) and writes to a file (scraper.log).
"""

import logging
import sys
from config import LOG_FILE_PATH


def get_logger(name: str = "web_scraper") -> logging.Logger:
    """
    Configures and returns a Logger instance with Stream and File handlers.
    
    Args:
        name (str): Name of the logger, defaults to 'web_scraper'.

    Returns:
        logging.Logger: Standard python logger configured with custom formatters.
    """
    logger = logging.getLogger(name)

    # Avoid duplicate handlers if logger is instantiated multiple times
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    # Standard log format: Timestamp | Level | Module Name | Message
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE_PATH, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
