"""News API connector for market sentiment context."""
import os

from onto_market.utils.logger import get_logger
from onto_market.utils.retry import retry_with_backoff

logger = get_logger(__name__)


class NewsConnector:
    def __init__(self):
        self.api_key = os.getenv("NEWSAPI_API_KEY")

    @retry_with_backoff(attempts=3, min_wait=2, max_wait=20)
    def get_headlines(self, query: str, page_size: int = 10) -> list[dict]:
        if not self.api_key:
            logger.debug("NEWSAPI_API_KEY not set; returning empty headlines")
            return []
        import requests
        resp = requests.get(
            "https://newsapi.org/v2/everything",
            params={"q": query, "pageSize": page_size, "sortBy": "publishedAt"},
            headers={"X-Api-Key": self.api_key},
            timeout=15,
        )
        resp.raise_for_status()
        return resp.json().get("articles", [])

    def headlines_text(self, query: str, page_size: int = 5) -> str:
        articles = self.get_headlines(query, page_size)
        lines = [f"- {a['title']} ({a['source']['name']})" for a in articles]
        return "\n".join(lines)
