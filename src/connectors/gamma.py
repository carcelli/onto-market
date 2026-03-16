"""Gamma Markets API connector — market discovery and metadata."""
import httpx

from src.polymarket_agents.utils.objects import Market
from src.utils.logger import get_logger
from src.utils.retry import retry_with_backoff

logger = get_logger(__name__)

GAMMA_BASE = "https://gamma-api.polymarket.com"


class GammaConnector:
    def __init__(self, timeout: float = 30.0):
        self.client = httpx.Client(base_url=GAMMA_BASE, timeout=timeout)

    @retry_with_backoff(attempts=3, min_wait=2, max_wait=30)
    def get_markets(
        self,
        limit: int = 100,
        offset: int = 0,
        active: bool = True,
        category: str | None = None,
    ) -> list[dict]:
        params: dict = {"limit": limit, "offset": offset, "active": str(active).lower()}
        if category:
            params["tag"] = category
        resp = self.client.get("/markets", params=params)
        resp.raise_for_status()
        return resp.json()

    def iter_markets(self, max_markets: int = 500, **kwargs) -> list[Market]:
        """Paginate through Gamma and return Market objects."""
        markets: list[Market] = []
        offset = 0
        limit = min(100, max_markets)

        while len(markets) < max_markets:
            batch = self.get_markets(limit=limit, offset=offset, **kwargs)
            if not batch:
                break
            for raw in batch:
                try:
                    markets.append(_parse_market(raw))
                except Exception as exc:
                    logger.debug("Skipping malformed market %s: %s", raw.get("id"), exc)
            offset += len(batch)
            if len(batch) < limit:
                break

        logger.info("Fetched %d markets from Gamma", len(markets))
        return markets[:max_markets]

    def close(self) -> None:
        self.client.close()


def _parse_market(raw: dict) -> Market:
    prices = raw.get("outcomePrices", ["0.5", "0.5"])
    return Market(
        id=str(raw["id"]),
        question=raw.get("question", ""),
        description=raw.get("description", ""),
        category=raw.get("tags", [{}])[0].get("label", "") if raw.get("tags") else "",
        outcomes=raw.get("outcomes", ["YES", "NO"]),
        outcome_prices=[float(p) for p in prices],
        volume=float(raw.get("volume", 0) or 0),
        liquidity=float(raw.get("liquidity", 0) or 0),
        active=bool(raw.get("active", True)),
        end_date=raw.get("endDate"),
        slug=raw.get("slug", ""),
        clob_token_ids=raw.get("clobTokenIds", []),
        event_id=str(raw.get("eventId", "")),
        tags=[t.get("label", "") for t in raw.get("tags", [])],
    )
