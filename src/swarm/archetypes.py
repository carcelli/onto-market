"""
Agent archetypes for the Social Sentiment Oracle.

Each archetype defines a persona with bias direction, social influence
susceptibility (alpha), and a method to produce an initial estimate
given a base probability.  Only the Analyst archetype calls the LLM;
others use fast heuristic perturbations to keep cost bounded.
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable


class Archetype(str, Enum):
    BULL = "bull"
    BEAR = "bear"
    ANALYST = "analyst"
    CONTRARIAN = "contrarian"
    NOISE_TRADER = "noise_trader"
    INSIDER = "insider"


@dataclass
class ArchetypeConfig:
    name: Archetype
    bias_range: tuple[float, float]
    alpha: float                       # social influence susceptibility (0=immune, 1=follows crowd)
    confidence_range: tuple[float, float]
    fraction: float                    # target share of the swarm
    description: str = ""

    def sample_bias(self) -> float:
        return random.uniform(*self.bias_range)

    def sample_confidence(self) -> float:
        return random.uniform(*self.confidence_range)


ARCHETYPE_REGISTRY: dict[Archetype, ArchetypeConfig] = {
    Archetype.BULL: ArchetypeConfig(
        name=Archetype.BULL,
        bias_range=(0.03, 0.15),
        alpha=0.3,
        confidence_range=(0.5, 0.8),
        fraction=0.25,
        description="Optimistic, overweights positive signals",
    ),
    Archetype.BEAR: ArchetypeConfig(
        name=Archetype.BEAR,
        bias_range=(-0.15, -0.03),
        alpha=0.3,
        confidence_range=(0.5, 0.8),
        fraction=0.25,
        description="Pessimistic, overweights risk and downside",
    ),
    Archetype.ANALYST: ArchetypeConfig(
        name=Archetype.ANALYST,
        bias_range=(-0.02, 0.02),
        alpha=0.1,
        confidence_range=(0.7, 0.95),
        fraction=0.03,
        description="Data-driven, anchors on base rates, calls LLM",
    ),
    Archetype.CONTRARIAN: ArchetypeConfig(
        name=Archetype.CONTRARIAN,
        bias_range=(-0.05, 0.05),
        alpha=-0.4,     # negative alpha = inverts neighbor influence
        confidence_range=(0.4, 0.7),
        fraction=0.12,
        description="Moves opposite to crowd consensus",
    ),
    Archetype.NOISE_TRADER: ArchetypeConfig(
        name=Archetype.NOISE_TRADER,
        bias_range=(-0.20, 0.20),
        alpha=0.6,
        confidence_range=(0.2, 0.5),
        fraction=0.25,
        description="Random perturbation, adds stochastic diversity",
    ),
    Archetype.INSIDER: ArchetypeConfig(
        name=Archetype.INSIDER,
        bias_range=(-0.01, 0.01),
        alpha=0.05,
        confidence_range=(0.85, 0.98),
        fraction=0.10,
        description="High-confidence, low-frequency signal anchored near base rate",
    ),
}


@dataclass
class SwarmAgent:
    id: int
    archetype: Archetype
    bias: float
    alpha: float
    confidence_weight: float
    estimate: float = 0.5
    track_record: float = 0.5

    @classmethod
    def from_config(cls, agent_id: int, cfg: ArchetypeConfig) -> SwarmAgent:
        return cls(
            id=agent_id,
            archetype=cfg.name,
            bias=cfg.sample_bias(),
            alpha=cfg.alpha + random.gauss(0, 0.05),
            confidence_weight=cfg.sample_confidence(),
        )

    def seed_estimate(self, base_prob: float) -> None:
        """Set initial estimate from base probability + archetype bias."""
        raw = base_prob + self.bias + random.gauss(0, 0.03)
        self.estimate = max(0.01, min(0.99, raw))

    def update_from_neighbors(self, neighbor_avg: float) -> None:
        """
        OASIS-style influence update.

        Positive alpha -> pull toward neighbor average.
        Negative alpha (contrarian) -> push away from neighbor average.
        """
        influence = abs(self.alpha) * (neighbor_avg - self.estimate)
        if self.alpha < 0:
            influence = -influence
        self.estimate = max(0.01, min(0.99, self.estimate + influence))


def spawn_agents(swarm_size: int) -> list[SwarmAgent]:
    """Instantiate a heterogeneous swarm from the archetype registry."""
    agents: list[SwarmAgent] = []
    agent_id = 0

    for archetype, cfg in ARCHETYPE_REGISTRY.items():
        count = max(1, int(swarm_size * cfg.fraction))
        for _ in range(count):
            agents.append(SwarmAgent.from_config(agent_id, cfg))
            agent_id += 1

    # Fill remaining slots with random archetypes
    while len(agents) < swarm_size:
        cfg = random.choice(list(ARCHETYPE_REGISTRY.values()))
        agents.append(SwarmAgent.from_config(agent_id, cfg))
        agent_id += 1

    return agents[:swarm_size]
