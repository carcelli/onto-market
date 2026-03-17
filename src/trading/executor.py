"""
LLM-powered trade executor.

Uses onto-market's LLMClient (not raw LangChain) for market filtering,
superforecasting, and trade sizing.  Adapted from the polymarket_langchain
reference executor.
"""
from __future__ import annotations

from typing import Any

from src.connectors.gamma import GammaConnector
from src.connectors.polymarket import PolymarketConnector
from src.utils.llm_client import LLMClient
from src.utils.logger import get_logger

logger = get_logger(__name__)


class TradeExecutor:
    """
    Market analysis and trade execution engine.

    Provides LLM-powered filtering, superforecasting, and order sizing.
    All actual order execution is delegated to PolymarketConnector
    (which respects SAFE_MODE).
    """

    def __init__(
        self,
        llm: LLMClient | None = None,
        gamma: GammaConnector | None = None,
        polymarket: PolymarketConnector | None = None,
    ):
        self.llm = llm or LLMClient()
        self.gamma = gamma or GammaConnector()
        self.polymarket = polymarket or PolymarketConnector()

    def filter_events(self, events: list[dict], max_keep: int = 10) -> list[dict]:
        """Use LLM to select the most tradeable events from a list."""
        if not events:
            return []

        summaries = "\n".join(
            f"{i+1}. [{e.get('id')}] {e.get('title', e.get('question', '?'))}"
            for i, e in enumerate(events[:50])
        )

        messages = [
            self.llm.system(
                "You are a Polymarket trading analyst. Given a list of prediction "
                "market events, select the ones with the highest trading potential "
                "(clear resolution criteria, sufficient liquidity signals, "
                "timely resolution). Return ONLY valid JSON:\n"
                '{"selected_ids": [<int>, ...], "rationale": "<brief>"}'
            ),
            self.llm.user(f"Select up to {max_keep} events:\n\n{summaries}"),
        ]

        try:
            result = self.llm.chat_json(messages, temperature=0.1)
            selected_ids = set(result.get("selected_ids", []))
            filtered = [e for e in events if e.get("id") in selected_ids]
            logger.info("Filtered %d -> %d events via LLM", len(events), len(filtered))
            return filtered or events[:max_keep]
        except Exception as exc:
            logger.warning("Event filtering failed, returning top %d: %s", max_keep, exc)
            return events[:max_keep]

    def superforecast(
        self,
        question: str,
        description: str,
        outcomes: list[str],
        context: str = "",
    ) -> dict:
        """
        Produce a superforecaster probability estimate for a market.

        Returns {"probability": float, "side": str, "rationale": str}
        """
        messages = [
            self.llm.system(
                "You are a world-class superforecaster trained in probabilistic "
                "reasoning.  Given a prediction market question, its description, "
                "possible outcomes, and research context, estimate the true "
                "probability of the YES outcome.\n\n"
                "Consider base rates, inside/outside view, and key uncertainties.\n\n"
                "Respond ONLY with valid JSON:\n"
                '{"probability": <float 0-1>, "side": "YES"|"NO", '
                '"rationale": "<2-3 sentences>"}'
            ),
            self.llm.user(
                f"Question: {question}\n"
                f"Description: {description[:800]}\n"
                f"Outcomes: {outcomes}\n"
                f"Research context: {context[:1200]}"
            ),
        ]

        try:
            result = self.llm.chat_json(messages, temperature=0.2)
            return {
                "probability": max(0.01, min(0.99, float(result.get("probability", 0.5)))),
                "side": result.get("side", "YES"),
                "rationale": result.get("rationale", ""),
            }
        except Exception as exc:
            logger.warning("Superforecast failed: %s", exc)
            return {"probability": 0.5, "side": "YES", "rationale": f"Error: {exc}"}

    def size_trade(
        self,
        edge: float,
        kelly_fraction: float,
        max_position_pct: float = 0.05,
    ) -> float:
        """
        Compute trade size as fraction of available balance.

        Uses half-Kelly by default for safety, capped at max_position_pct.
        """
        half_kelly = kelly_fraction / 2.0
        position_fraction = min(half_kelly, max_position_pct)

        try:
            balance = self.polymarket.get_usdc_balance()
        except Exception:
            logger.warning("Could not fetch USDC balance, using notional $100")
            balance = 100.0

        size = balance * position_fraction
        logger.info(
            "Trade sizing: edge=%.2f%% kelly=%.2f%% half_kelly=%.2f%% "
            "balance=$%.2f -> size=$%.2f",
            edge * 100, kelly_fraction * 100, half_kelly * 100,
            balance, size,
        )
        return round(size, 2)
