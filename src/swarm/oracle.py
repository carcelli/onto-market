"""
Social Sentiment Oracle — MiroFish/OASIS-inspired swarm consensus engine.

Spawns N heterogeneous agents across 6 archetypes, seeds their estimates
from a base probability, runs interaction dynamics on a small-world network,
then aggregates into a confidence-weighted consensus signal.

Only Analyst agents (small fraction) call the LLM; the rest use heuristic
perturbations, keeping cost proportional to SWARM_SIZE * analyst_fraction.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import numpy as np

from config import config
from src.swarm.archetypes import (
    Archetype,
    SwarmAgent,
    spawn_agents,
)
from src.swarm.dynamics import build_network, run_dynamics
from src.utils.logger import get_logger

logger = get_logger(__name__)


@dataclass
class OracleResult:
    consensus_prob: float
    confidence: float
    dissent_ratio: float
    rounds_executed: int
    swarm_size: int
    mean_estimate: float
    std_estimate: float


class SocialSentimentOracle:
    """
    OASIS-style swarm simulation for prediction market probability estimation.

    Lifecycle:
        oracle = SocialSentimentOracle(swarm_size=5000)
        result = oracle.estimate(query, base_prob=0.65, context="...")
        print(result.consensus_prob, result.confidence)
    """

    def __init__(
        self,
        swarm_size: int | None = None,
        max_rounds: int | None = None,
        convergence_threshold: float | None = None,
        analyst_fraction: float | None = None,
    ):
        self.swarm_size = swarm_size or config.SWARM_SIZE
        self.max_rounds = max_rounds or config.SWARM_ROUNDS
        self.convergence_threshold = (
            convergence_threshold or config.SWARM_CONVERGENCE_THRESHOLD
        )
        self.analyst_fraction = analyst_fraction or config.SWARM_ANALYST_FRACTION

        self.agents: list[SwarmAgent] = spawn_agents(self.swarm_size)
        self.network = build_network(self.swarm_size)

    def estimate(
        self,
        query: str,
        base_prob: float,
        context: str = "",
        llm_client=None,
    ) -> OracleResult:
        """
        Run the full swarm simulation and return consensus.

        Args:
            query: market question
            base_prob: starting probability (e.g. from probability_node)
            context: research context for LLM-calling analysts
            llm_client: optional LLMClient for analyst agents
        """
        self._seed_estimates(base_prob, query, context, llm_client)

        rounds = run_dynamics(
            self.agents,
            self.network,
            max_rounds=self.max_rounds,
            convergence_threshold=self.convergence_threshold,
        )

        return self._aggregate(rounds)

    def _seed_estimates(
        self,
        base_prob: float,
        query: str,
        context: str,
        llm_client,
    ) -> None:
        """Seed each agent's initial estimate based on archetype."""
        analyst_estimates: list[float] = []

        if llm_client:
            analyst_estimates = self._get_analyst_estimates(
                query, base_prob, context, llm_client
            )

        analyst_idx = 0
        for agent in self.agents:
            if agent.archetype == Archetype.ANALYST and analyst_idx < len(analyst_estimates):
                agent.estimate = analyst_estimates[analyst_idx]
                analyst_idx += 1
            else:
                agent.seed_estimate(base_prob)

    def _get_analyst_estimates(
        self,
        query: str,
        base_prob: float,
        context: str,
        llm_client,
    ) -> list[float]:
        """Call LLM for a batch of analyst-quality independent estimates."""
        num_analysts = sum(
            1 for a in self.agents if a.archetype == Archetype.ANALYST
        )
        if num_analysts == 0:
            return []

        try:
            messages = [
                llm_client.system(
                    "You are a superforecaster. Given a prediction market question, base "
                    "probability, and research context, produce independent probability "
                    "estimates. Respond ONLY with valid JSON:\n"
                    '{"estimates": [<float 0-1>, ...], "rationale": "<brief>"}'
                ),
                llm_client.user(
                    f"Question: {query}\n"
                    f"Base probability: {base_prob:.3f}\n"
                    f"Context: {context[:1500]}\n\n"
                    f"Produce {min(num_analysts, 5)} independent estimates."
                ),
            ]
            result = llm_client.chat_json(messages, temperature=0.4)
            estimates = [
                max(0.01, min(0.99, float(e)))
                for e in result.get("estimates", [])
            ]
            logger.info("Analyst LLM returned %d estimates", len(estimates))
            return estimates
        except Exception as exc:
            logger.warning("Analyst LLM call failed, using heuristic: %s", exc)
            return []

    def _aggregate(self, rounds_executed: int) -> OracleResult:
        """Compute confidence-weighted consensus from final agent estimates."""
        estimates = np.array([a.estimate for a in self.agents])
        weights = np.array([a.confidence_weight for a in self.agents])

        total_weight = weights.sum()
        if total_weight > 0:
            weighted_mean = float(np.dot(weights, estimates) / total_weight)
        else:
            weighted_mean = float(estimates.mean())

        # Confidence-weighted median via sorting
        sorted_indices = np.argsort(estimates)
        sorted_estimates = estimates[sorted_indices]
        sorted_weights = weights[sorted_indices]
        cumulative = np.cumsum(sorted_weights)
        median_idx = np.searchsorted(cumulative, total_weight / 2)
        consensus = float(sorted_estimates[min(median_idx, len(sorted_estimates) - 1)])

        std = float(estimates.std())
        confidence = max(0.0, min(1.0, 1.0 - std * 5))

        dissent_count = sum(
            1 for e in estimates if abs(e - consensus) > 0.2
        )
        dissent_ratio = dissent_count / len(estimates) if estimates.size > 0 else 0.0

        logger.info(
            "Oracle result: consensus=%.3f confidence=%.3f dissent=%.1f%% "
            "(mean=%.3f std=%.4f rounds=%d)",
            consensus, confidence, dissent_ratio * 100,
            weighted_mean, std, rounds_executed,
        )

        return OracleResult(
            consensus_prob=consensus,
            confidence=confidence,
            dissent_ratio=dissent_ratio,
            rounds_executed=rounds_executed,
            swarm_size=len(self.agents),
            mean_estimate=weighted_mean,
            std_estimate=std,
        )
