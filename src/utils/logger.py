"""Structured logger with console + rotating file output (MiroFish-inspired)."""
import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

_loggers: dict[str, logging.Logger] = {}


def setup_logger(
    name: str,
    level: int = logging.INFO,
    log_file: str = "onto-market.log",
) -> logging.Logger:
    if name in _loggers:
        return _loggers[name]

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    fmt = logging.Formatter(
        "%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(fmt)
    logger.addHandler(console)

    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=5)
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)

    _loggers[name] = logger
    return logger


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    return setup_logger(name, level)
