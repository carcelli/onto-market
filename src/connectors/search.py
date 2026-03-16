"""Web search connector (Tavily)."""
import os

from src.utils.logger import get_logger
from src.utils.retry import retry_with_backoff

logger = get_logger(__name__)


class SearchConnector:
    def __init__(self):
        self.api_key = os.getenv("TAVILY_API_KEY")
        self._client = None

    def _get_client(self):
        if self._client is None:
            if not self.api_key:
                raise EnvironmentError("TAVILY_API_KEY is not set")
            from tavily import TavilyClient  # lazy import
            self._client = TavilyClient(api_key=self.api_key)
        return self._client

    @retry_with_backoff(attempts=3, min_wait=2, max_wait=20)
    def search(self, query: str, max_results: int = 5) -> list[dict]:
        client = self._get_client()
        result = client.search(query=query, max_results=max_results)
        return result.get("results", [])

    def search_text(self, query: str, max_results: int = 5) -> str:
        """Return concatenated snippets as a single string."""
        results = self.search(query, max_results)
        return "\n\n".join(r.get("content", "") for r in results if r.get("content"))
