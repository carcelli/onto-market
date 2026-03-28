"""Tests for the Social Sentiment Oracle swarm simulation."""
import pytest

from onto_market.swarm.archetypes import (
    Archetype,
    ArchetypeConfig,
    SwarmAgent,
    spawn_agents,
    ARCHETYPE_REGISTRY,
)
from onto_market.swarm.dynamics import build_network, propagate_influence, check_convergence, run_dynamics
from onto_market.swarm.oracle import SocialSentimentOracle, OracleResult


class TestArchetypes:
    def test_all_archetypes_registered(self):
        for archetype in Archetype:
            assert archetype in ARCHETYPE_REGISTRY

    def test_fractions_sum_to_one(self):
        total = sum(cfg.fraction for cfg in ARCHETYPE_REGISTRY.values())
        assert 0.95 <= total <= 1.05, f"Archetype fractions sum to {total}"

    def test_spawn_correct_count(self):
        agents = spawn_agents(100)
        assert len(agents) == 100

    def test_spawn_large_swarm(self):
        agents = spawn_agents(5000)
        assert len(agents) == 5000

    def test_unique_ids(self):
        agents = spawn_agents(200)
        ids = [a.id for a in agents]
        assert len(ids) == len(set(ids))

    def test_agent_from_config(self):
        cfg = ARCHETYPE_REGISTRY[Archetype.BULL]
        agent = SwarmAgent.from_config(0, cfg)
        assert agent.archetype == Archetype.BULL
        assert cfg.bias_range[0] <= agent.bias <= cfg.bias_range[1]

    def test_seed_estimate_clamped(self):
        cfg = ARCHETYPE_REGISTRY[Archetype.NOISE_TRADER]
        agent = SwarmAgent.from_config(0, cfg)
        agent.seed_estimate(0.99)
        assert 0.01 <= agent.estimate <= 0.99

    def test_contrarian_has_negative_alpha(self):
        cfg = ARCHETYPE_REGISTRY[Archetype.CONTRARIAN]
        assert cfg.alpha < 0

    def test_archetype_diversity(self):
        agents = spawn_agents(1000)
        archetypes_seen = {a.archetype for a in agents}
        assert len(archetypes_seen) >= 5


class TestDynamics:
    def test_build_network_correct_size(self):
        g = build_network(100)
        assert g.number_of_nodes() == 100

    def test_build_network_small(self):
        g = build_network(10)
        assert g.number_of_nodes() == 10
        assert g.number_of_edges() > 0

    def test_propagate_preserves_bounds(self):
        agents = spawn_agents(50)
        network = build_network(50)
        for a in agents:
            a.seed_estimate(0.7)

        propagate_influence(agents, network)

        for a in agents:
            assert 0.01 <= a.estimate <= 0.99

    def test_convergence_uniform_swarm(self):
        agents = spawn_agents(50)
        for a in agents:
            a.estimate = 0.6
        assert check_convergence(agents, threshold=0.01)

    def test_no_convergence_diverse(self):
        agents = spawn_agents(50)
        for i, a in enumerate(agents):
            a.estimate = 0.1 + (i / 50) * 0.8
        assert not check_convergence(agents, threshold=0.01)

    def test_run_dynamics_converges(self):
        agents = spawn_agents(100)
        network = build_network(100)
        for a in agents:
            a.seed_estimate(0.6)

        rounds = run_dynamics(agents, network, max_rounds=20, convergence_threshold=0.05)
        assert rounds <= 20

    def test_run_dynamics_zero_rounds(self):
        agents = spawn_agents(10)
        network = build_network(10)
        for a in agents:
            a.seed_estimate(0.5)
        rounds = run_dynamics(agents, network, max_rounds=0)
        assert rounds == 0


class TestOracle:
    def test_oracle_returns_result(self):
        oracle = SocialSentimentOracle(swarm_size=100, max_rounds=3)
        result = oracle.estimate(query="Will BTC hit $100k?", base_prob=0.6)
        assert isinstance(result, OracleResult)

    def test_oracle_consensus_in_range(self):
        oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)
        result = oracle.estimate(query="Test market", base_prob=0.5)
        assert 0.0 <= result.consensus_prob <= 1.0

    def test_oracle_confidence_in_range(self):
        oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)
        result = oracle.estimate(query="Test market", base_prob=0.7)
        assert 0.0 <= result.confidence <= 1.0

    def test_oracle_dissent_in_range(self):
        oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)
        result = oracle.estimate(query="Test market", base_prob=0.5)
        assert 0.0 <= result.dissent_ratio <= 1.0

    def test_oracle_swarm_size_respected(self):
        oracle = SocialSentimentOracle(swarm_size=150, max_rounds=2)
        result = oracle.estimate(query="Test", base_prob=0.5)
        assert result.swarm_size == 150

    def test_oracle_consensus_near_base(self):
        """Consensus should be in the neighborhood of the base probability."""
        oracle = SocialSentimentOracle(swarm_size=500, max_rounds=5)
        result = oracle.estimate(query="Test", base_prob=0.7)
        assert abs(result.consensus_prob - 0.7) < 0.25

    def test_oracle_high_base_prob(self):
        oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)
        result = oracle.estimate(query="Very likely event", base_prob=0.95)
        assert result.consensus_prob > 0.5

    def test_oracle_low_base_prob(self):
        oracle = SocialSentimentOracle(swarm_size=200, max_rounds=3)
        result = oracle.estimate(query="Unlikely event", base_prob=0.1)
        assert result.consensus_prob < 0.5
