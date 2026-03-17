"""Core domain models."""
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Market:
    id: str
    question: str
    description: str = ""
    category: str = ""
    outcomes: list[str] = field(default_factory=lambda: ["YES", "NO"])
    outcome_prices: list[float] = field(default_factory=lambda: [0.5, 0.5])
    volume: float = 0.0
    liquidity: float = 0.0
    active: bool = True
    end_date: str | None = None
    slug: str = ""
    clob_token_ids: list[str] = field(default_factory=list)
    event_id: str = ""
    tags: list[str] = field(default_factory=list)
    last_updated: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @property
    def implied_probability(self) -> float:
        """YES price as implied probability."""
        return self.outcome_prices[0] if self.outcome_prices else 0.5

    @property
    def yes_token_id(self) -> str | None:
        return self.clob_token_ids[0] if self.clob_token_ids else None

    @property
    def no_token_id(self) -> str | None:
        return self.clob_token_ids[1] if len(self.clob_token_ids) > 1 else None


@dataclass
class ResearchNote:
    market_id: str
    content: str
    source: str = ""
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
