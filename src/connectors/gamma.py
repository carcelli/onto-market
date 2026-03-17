"""Gamma Markets API connector - market discovery and metadata."""
import json as _json

import requests

from src.polymarket_agents.utils.objects import Market
from src.utils.logger import get_logger
from src.utils.retry import retry_with_backoff

logger = get_logger(__name__)

GAMMA_BASE = "https://gamma-api.polymarket.com"
_TIMEOUT = (10, 30)  # (connect, read) seconds


def _json_field(value, default=None):
    """Gamma returns some list/dict fields as JSON-encoded strings."""
    if value is None:
        return default
    if isinstance(value, str):
        try:
            return _json.loads(value)
        except (_json.JSONDecodeError, ValueError):
            return default
    return value


class GammaConnector:
    def __init__(self):
        self.session = requests.Session()

    @retry_with_backoff(attempts=3, min_wait=2, max_wait=30)
    def get_markets(
        self,
        limit: int = 100,
        offset: int = 0,
        active: bool = True,
        closed: bool = False,
        category: str | None = None,
        order: str = "volumeNum",
        ascending: bool = False,
    ) -> list[dict]:
        params: dict = {
            "limit": limit,
            "offset": offset,
            "active": str(active).lower(),
            "closed": str(closed).lower(),
            "order": order,
            "ascending": str(ascending).lower(),
        }
        if category:
            params["tag"] = category
        resp = self.session.get(f"{GAMMA_BASE}/markets", params=params, timeout=_TIMEOUT)
        resp.raise_for_status()
        return resp.json()

    def iter_markets(self, max_markets: int = 500, **kwargs) -> list[Market]:
        """Paginate through Gamma and return Market objects."""
        markets: list[Market] = []
        offset = 0
        limit = min(100, max_markets)
        max_pages = max(3, (max_markets // limit) + 2)

        for _ in range(max_pages):
            if len(markets) >= max_markets:
                break
            batch = self.get_markets(limit=limit, offset=offset, **kwargs)
            if not batch:
                break
            parsed_count = 0
            for raw in batch:
                try:
                    markets.append(_parse_market(raw))
                    parsed_count += 1
                except Exception as exc:
                    logger.debug("Skipping malformed market %s: %s", raw.get("id"), exc)
            offset += len(batch)
            if len(batch) < limit:
                break
            if parsed_count == 0:
                logger.warning("Entire batch of %d markets failed to parse, stopping", len(batch))
                break

        logger.info("Fetched %d markets from Gamma", len(markets))
        return markets[:max_markets]

    def close(self) -> None:
        self.session.close()


def _parse_market(raw: dict) -> Market:
    prices = _json_field(raw.get("outcomePrices"), ["0.5", "0.5"])
    outcomes = _json_field(raw.get("outcomes"), ["YES", "NO"])
    clob_ids = _json_field(raw.get("clobTokenIds"), [])
    tags_raw = _json_field(raw.get("tags"), [])

    category = raw.get("category", "")
    if not category and tags_raw:
        if isinstance(tags_raw, list) and tags_raw:
            first = tags_raw[0]
            category = first.get("label", "") if isinstance(first, dict) else str(first)

    tag_labels: list[str] = []
    if isinstance(tags_raw, list):
        for t in tags_raw:
            tag_labels.append(t.get("label", str(t)) if isinstance(t, dict) else str(t))

    return Market(
        id=str(raw["id"]),
        question=raw.get("question", ""),
        description=raw.get("description", ""),
        category=category,
        outcomes=outcomes if isinstance(outcomes, list) else ["YES", "NO"],
        outcome_prices=[float(p) for p in prices],
        volume=float(raw.get("volumeNum", 0) or raw.get("volume", 0) or 0),
        liquidity=float(raw.get("liquidityNum", 0) or raw.get("liquidity", 0) or 0),
        active=bool(raw.get("active", True)),
        end_date=raw.get("endDate"),
        slug=raw.get("slug", ""),
        clob_token_ids=clob_ids if isinstance(clob_ids, list) else [],
        event_id=str(raw.get("eventId", "")),
        tags=tag_labels,
    )
