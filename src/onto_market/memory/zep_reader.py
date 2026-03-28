"""
Zep Cloud entity reader — stub for Phase 2.
When ZEP_API_KEY is set, wire real zep-python client here.
"""
from onto_market.config import config


class ZepEntityReader:
    """Read market narratives and entity facts from Zep knowledge graph."""

    def __init__(self):
        self.enabled = bool(config.ZEP_API_KEY)
        if self.enabled:
            # Phase 2: import zep_python and initialise client
            pass

    def get_facts(self, entity: str) -> list[dict]:
        """Return known facts about a market entity (e.g., 'Bitcoin', 'Trump')."""
        if not self.enabled:
            return []
        # Phase 2: self.client.graph.search(query=entity, ...)
        return []

    def store_fact(self, entity: str, fact: str) -> None:
        if not self.enabled:
            return
        # Phase 2: self.client.graph.add(...)
