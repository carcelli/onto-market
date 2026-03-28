"""Retry utilities with exponential backoff (MiroFish-inspired)."""
import functools
import logging
from typing import Callable, TypeVar

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

F = TypeVar("F", bound=Callable)
logger = logging.getLogger(__name__)


def retry_with_backoff(
    attempts: int = 5,
    min_wait: float = 4,
    max_wait: float = 60,
    exceptions: tuple = (Exception,),
) -> Callable[[F], F]:
    """Decorator: retry with exponential backoff on transient failures."""
    return retry(
        stop=stop_after_attempt(attempts),
        wait=wait_exponential(multiplier=1, min=min_wait, max=max_wait),
        retry=retry_if_exception_type(exceptions),
        reraise=True,
    )


class RetryableAPIClient:
    """Wrap any callable so every call is automatically retried."""

    def __init__(self, client: Callable, **retry_kwargs):
        self._client = client
        self._retry_kwargs = retry_kwargs

    def __call__(self, *args, **kwargs):
        fn = retry_with_backoff(**self._retry_kwargs)(self._client)
        return fn(*args, **kwargs)
