"""
Application context for dependency injection.

Centralizes all configurable dependencies — connectors, memory, trading —
so agents and CLI commands share singletons without hardcoded imports.

Usage:
    from src.context import get_context
    ctx = get_context()
    gamma = ctx.get_gamma()
    polymarket = ctx.get_polymarket()
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class AppContext:
    db_path: str = field(
        default_factory=lambda: os.getenv("DATABASE_PATH", "data/memory.db")
    )
    gamma_api_url: str = "https://gamma-api.polymarket.com"
    clob_api_url: str = field(
        default_factory=lambda: os.getenv("CLOB_API_URL", "https://clob.polymarket.com")
    )
    safe_mode: bool = field(
        default_factory=lambda: os.getenv("SAFE_MODE", "true").lower() == "true"
    )

    _memory_manager: Optional[Any] = field(default=None, repr=False)
    _gamma: Optional[Any] = field(default=None, repr=False)
    _polymarket: Optional[Any] = field(default=None, repr=False)
    _llm: Optional[Any] = field(default=None, repr=False)

    def get_memory_manager(self):
        if self._memory_manager is None:
            from src.memory.manager import MemoryManager
            self._memory_manager = MemoryManager(self.db_path)
        return self._memory_manager

    def get_gamma(self):
        if self._gamma is None:
            from src.connectors.gamma import GammaConnector
            self._gamma = GammaConnector()
        return self._gamma

    def get_polymarket(self):
        if self._polymarket is None:
            from src.connectors.polymarket import PolymarketConnector
            self._polymarket = PolymarketConnector(safe_mode=self.safe_mode)
        return self._polymarket

    def get_llm(self):
        if self._llm is None:
            from src.utils.llm_client import LLMClient
            self._llm = LLMClient()
        return self._llm

    def reset(self):
        self._memory_manager = None
        self._gamma = None
        self._polymarket = None
        self._llm = None


_context: Optional[AppContext] = None


def get_context() -> AppContext:
    global _context
    if _context is None:
        _context = AppContext()
    return _context


def set_context(ctx: AppContext) -> None:
    global _context
    _context = ctx


def reset_context() -> None:
    global _context
    _context = None
