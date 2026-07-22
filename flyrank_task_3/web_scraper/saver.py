"""
Data Saver module responsible strictly for data persistence and file exporting.

Writes structured records to JSON and CSV formats. Automatically creates target
output directories if they do not already exist.
"""

import csv
import json
from pathlib import Path
from typing import List, Dict, Any
from logger import get_logger

logger = get_logger("saver")


def ensure_directory_exists(filepath: Path) -> None:
    """
    Ensures parent directories exist before writing files.
    """
    filepath.parent.mkdir(parents=True, exist_ok=True)


def save_to_json(data: List[Dict[str, Any]], filepath: Path) -> bool:
    """
    Saves a list of dictionaries to a formatted JSON file.

    Args:
        data (List[Dict[str, Any]]): List of validated book records.
        filepath (Path): Destination file path for JSON output.

    Returns:
        bool: True if save succeeded, False otherwise.
    """
    if not data:
        logger.warning(f"No data to save to JSON at {filepath}")
        return False

    try:
        ensure_directory_exists(filepath)
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

        logger.info(f"Successfully saved {len(data)} records to JSON: {filepath}")
        return True
    except Exception as err:
        logger.error(f"Failed to save JSON to {filepath}: {err}")
        return False


def save_to_csv(data: List[Dict[str, Any]], filepath: Path) -> bool:
    """
    Saves a list of dictionaries to a structured CSV file.

    Args:
        data (List[Dict[str, Any]]): List of validated book records.
        filepath (Path): Destination file path for CSV output.

    Returns:
        bool: True if save succeeded, False otherwise.
    """
    if not data:
        logger.warning(f"No data to save to CSV at {filepath}")
        return False

    try:
        ensure_directory_exists(filepath)
        headers = list(data[0].keys())

        with open(filepath, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)

        logger.info(f"Successfully saved {len(data)} records to CSV: {filepath}")
        return True
    except Exception as err:
        logger.error(f"Failed to save CSV to {filepath}: {err}")
        return False


def save_data(data: List[Dict[str, Any]], json_path: Path, csv_path: Path) -> None:
    """
    Convenience function to save dataset into both JSON and CSV formats.
    """
    logger.info("Initiating data persistence phase...")
    save_to_json(data, json_path)
    save_to_csv(data, csv_path)
    logger.info("Data persistence phase complete.")
