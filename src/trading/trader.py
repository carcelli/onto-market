"""
Trader — orchestrates the full discover-filter-analyze-execute pipeline.

Adapted from polymarket_langchain's Trader class, using onto-market's
connectors, LLMClient, and SAFE_MODE gating.
"""
from __future__ import annotations

from src.connectors.gamma import GammaConnector
from src.connectors.polymarket import PolymarketConnector
from src.polymarket_agents.utils.analytics import score_market, calculate_edge
from src.trading.executor import TradeExecutor
from src.utils.llm_client import LLMClient
from src.utils.logger import get_logger

logger = get_logger(__name__)


class Trader:
    """
    End-to-end trading pipeline:
        1. Discover tradeable events
        2. LLM-filter to highest-potential subset
        3. Map events to markets
        4. Superforecast each market
        5. Score edge / Kelly / EV
        6. Execute best trade (dry-run unless SAFE_MODE=false)
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
        self.executor = TradeExecutor(
            llm=self.llm,
            gamma=self.gamma,
            polymarket=self.polymarket,
        )

    def one_best_trade(self) -> dict:
        """
        Full pipeline: find the single best trade opportunity and execute it.

        Returns a dict with the trade details, scorecard, and execution result.
        """
        # 1. Discover
        logger.info("Step 1: Discovering tradeable events")
        events = self.polymarket.get_tradeable_events()
        logger.info("Found %d tradeable events", len(events))
        if not events:
            return {"action": "PASS", "reason": "No tradeable events found"}

        # 2. Filter
        logger.info("Step 2: LLM-filtering events")
        filtered = self.executor.filter_events(events, max_keep=10)
        logger.info("Filtered to %d events", len(filtered))

        # 3. Map to markets
        logger.info("Step 3: Mapping events to markets")
        markets = self._events_to_markets(filtered)
        logger.info("Found %d markets from filtered events", len(markets))
        if not markets:
            return {"action": "PASS", "reason": "No markets found for filtered events"}

        # 4. Superforecast + score each market
        logger.info("Step 4: Superforecasting %d markets", len(markets))
        best_trade = None
        best_edge = -1.0

        for market in markets[:20]:
            outcomes = market.get("outcomes", ["YES", "NO"])
            if isinstance(outcomes, str):
                import ast
                try:
                    outcomes = ast.literal_eval(outcomes)
                except Exception:
                    outcomes = ["YES", "NO"]

            prices = market.get("outcome_prices", "[0.5, 0.5]")
            if isinstance(prices, str):
                import ast
                try:
                    prices = ast.literal_eval(prices)
                except Exception:
                    prices = [0.5, 0.5]

            implied_prob = float(prices[0]) if prices else 0.5
            volume = float(market.get("volume", 0) or 0)

            forecast = self.executor.superforecast(
                question=market.get("question", ""),
                description=market.get("description", ""),
                outcomes=outcomes,
            )

            scorecard = score_market(
                true_prob=forecast["probability"],
                implied_prob=implied_prob,
                volume=volume,
            )

            edge = scorecard["edge"]
            if edge > best_edge and scorecard["action"] == "BET":
                best_trade = {
                    "market": market,
                    "forecast": forecast,
                    "scorecard": scorecard,
                }
                best_edge = edge

        if not best_trade:
            logger.info("No BET-worthy trades found")
            return {"action": "PASS", "reason": "No markets met edge/volume/Kelly thresholds"}

        # 5. Size and execute
        logger.info("Step 5: Executing best trade (edge=%.2f%%)", best_edge * 100)
        market = best_trade["market"]
        scorecard = best_trade["scorecard"]

        size = self.executor.size_trade(
            edge=scorecard["edge"],
            kelly_fraction=scorecard["kelly_fraction"],
        )

        # Raw Gamma dicts use camelCase; parsed Market objects use snake_case
        token_ids = market.get("clob_token_ids") or market.get("clobTokenIds", "[]")
        if isinstance(token_ids, str):
            import ast
            try:
                token_ids = ast.literal_eval(token_ids)
            except Exception:
                token_ids = []

        side = best_trade["forecast"]["side"]
        token_id = token_ids[0] if side == "YES" and token_ids else (
            token_ids[1] if side == "NO" and len(token_ids) > 1 else None
        )

        execution_result = {"no_token": True}
        if token_id and size > 0:
            execution_result = self.polymarket.build_order(
                token_id=token_id,
                price=scorecard["implied_prob"],
                size=size,
                side="BUY",
            )

        result = {
            "action": "BET",
            "market_question": market.get("question", ""),
            "side": side,
            "edge": scorecard["edge"],
            "expected_value": scorecard["expected_value"],
            "kelly_fraction": scorecard["kelly_fraction"],
            "size_usd": size,
            "execution": execution_result,
            "forecast_rationale": best_trade["forecast"]["rationale"],
        }

        logger.info(
            "Trade result: %s %s | edge=%.1f%% | size=$%.2f | dry_run=%s",
            side, market.get("question", "")[:50],
            scorecard["edge"] * 100, size,
            execution_result.get("dry_run", "N/A"),
        )

        return result

    def _events_to_markets(self, events: list[dict]) -> list[dict]:
        """Resolve event IDs to their constituent markets."""
        markets = []
        for evt in events:
            market_ids = str(evt.get("markets", "")).split(",")
            for mid in market_ids:
                mid = mid.strip()
                if not mid:
                    continue
                try:
                    rm = self.gamma.get_market_by_id(mid)
                    if rm is not None:
                        markets.append(rm)
                except Exception as exc:
                    logger.debug("Failed to fetch market %s: %s", mid, exc)
        return markets
