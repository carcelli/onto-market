"""
Interaction dynamics for the Social Sentiment Oracle.

Agents are placed on a Watts-Strogatz small-world network.  Each round,
agents observe their neighbors' estimates and update their own via an
archetype-specific influence rule.  The simulation runs until convergence
(std < threshold) or max rounds are exhausted.
"""
from __future__ import annotations

import numpy as np
import networkx as nx

from src.swarm.archetypes import SwarmAgent
from src.utils.logger import get_logger

logger = get_logger(__name__)


def build_network(n: int, k: int = 6, p: float = 0.1) -> nx.Graph:
    """
    Build a small-world graph for agent interaction.

    k: each node connected to k nearest neighbors (even number)
    p: rewiring probability — higher means more random long-range links
    """
    k = min(k, max(2, n - 1))
    if k % 2 != 0:
        k -= 1
    return nx.watts_strogatz_graph(n, k, p, seed=42)


def propagate_influence(
    agents: list[SwarmAgent],
    network: nx.Graph,
) -> None:
    """
    One round of OASIS-style influence propagation.

    Each agent computes a confidence-weighted average of its neighbors'
    estimates, then updates via its own alpha (susceptibility).
    """
    new_estimates: list[float] = []

    for agent in agents:
        neighbors = list(network.neighbors(agent.id))
        if not neighbors:
            new_estimates.append(agent.estimate)
            continue

        neighbor_agents = [agents[n] for n in neighbors]
        weights = np.array([a.confidence_weight for a in neighbor_agents])
        estimates = np.array([a.estimate for a in neighbor_agents])

        total_weight = weights.sum()
        if total_weight > 0:
            weighted_avg = float(np.dot(weights, estimates) / total_weight)
        else:
            weighted_avg = float(estimates.mean())

        agent.update_from_neighbors(weighted_avg)
        new_estimates.append(agent.estimate)


def check_convergence(
    agents: list[SwarmAgent],
    threshold: float = 0.02,
) -> bool:
    """Return True if the swarm's estimate spread is below threshold."""
    estimates = np.array([a.estimate for a in agents])
    return float(estimates.std()) < threshold


def run_dynamics(
    agents: list[SwarmAgent],
    network: nx.Graph,
    max_rounds: int = 5,
    convergence_threshold: float = 0.02,
) -> int:
    """
    Run interaction rounds until convergence or max_rounds.

    Returns the number of rounds actually executed.
    """
    for round_num in range(1, max_rounds + 1):
        propagate_influence(agents, network)

        std = float(np.array([a.estimate for a in agents]).std())
        logger.debug(
            "Swarm round %d/%d: std=%.4f (threshold=%.4f)",
            round_num, max_rounds, std, convergence_threshold,
        )

        if check_convergence(agents, convergence_threshold):
            logger.info("Swarm converged after %d rounds (std=%.4f)", round_num, std)
            return round_num

    logger.info("Swarm reached max rounds (%d) without convergence (std=%.4f)", max_rounds, std)
    return max_rounds
