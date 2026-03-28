"""File parsing utilities for market research (MiroFish-inspired)."""
import logging
from pathlib import Path
from typing import Any

import pandas as pd

logger = logging.getLogger(__name__)


def parse_txt(path: Path) -> str:
    """Read a simple text file."""
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        logger.error("Failed to parse TXT %s: %s", path, exc)
        return ""


def parse_csv(path: Path) -> str:
    """Read a CSV and return a markdown table or summary."""
    try:
        df = pd.read_csv(path)
        return df.to_markdown(index=False)
    except Exception as exc:
        logger.error("Failed to parse CSV %s: %s", path, exc)
        return ""


def parse_file(file_path: str | Path) -> str:
    """Generic entry point for parsing research files."""
    path = Path(file_path)
    if not path.exists():
        return ""

    suffix = path.suffix.lower()
    if suffix in (".txt", ".md", ".log"):
        return parse_txt(path)
    if suffix == ".csv":
        return parse_csv(path)
    if suffix in (".xls", ".xlsx"):
        try:
            df = pd.read_excel(path)
            return df.to_markdown(index=False)
        except Exception as exc:
            logger.error("Failed to parse Excel %s: %s", path, exc)
            return ""

    logger.warning("No parser for extension: %s", suffix)
    return ""
