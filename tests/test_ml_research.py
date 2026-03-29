"""Tests for the ml_research autoresearch subsystem.

Covers: dataset, features, evaluate, train, artifacts, runner.
All tests use synthetic fixture data — no network calls.
"""
from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

# ── Fixtures ──────────────────────────────────────────────────────────────

RESOLVED_ROWS = [
    {
        "market_id": f"m{i}",
        "question": f"Will event {i} happen?",
        "category": "crypto" if i % 2 == 0 else "politics",
        "tags": json.dumps(["tag_a", "tag_b"]),
        "volume": 10000.0 + i * 1000,
        "liquidity": 5000.0 + i * 500,
        "implied_prob_at_close": 0.3 + i * 0.03,
        "resolved_yes": 1 if i % 3 == 0 else 0,
        "end_date": f"2026-03-{min(i + 1, 28):02d}T00:00:00Z",
        "closed_time": f"2026-03-{min(i + 1, 28):02d}T00:00:00Z",
        "fetched_at": "2026-03-28T00:00:00Z",
    }
    for i in range(20)
]


def _seed_db(db_path: str, rows: list[dict] | None = None) -> None:
    """Create and populate a resolved_markets table."""
    rows = rows or RESOLVED_ROWS
    con = sqlite3.connect(db_path)
    con.execute("""
        CREATE TABLE IF NOT EXISTS resolved_markets (
            market_id   TEXT PRIMARY KEY,
            question    TEXT,
            category    TEXT,
            tags        TEXT,
            volume      REAL,
            liquidity   REAL,
            implied_prob_at_close REAL,
            resolved_yes INTEGER,
            end_date    TEXT,
            closed_time TEXT,
            fetched_at  TEXT
        )
    """)
    con.executemany(
        """INSERT OR REPLACE INTO resolved_markets
           (market_id, question, category, tags, volume, liquidity,
            implied_prob_at_close, resolved_yes, end_date, closed_time, fetched_at)
           VALUES (:market_id, :question, :category, :tags, :volume,
                   :liquidity, :implied_prob_at_close, :resolved_yes,
                   :end_date, :closed_time, :fetched_at)""",
        rows,
    )
    con.commit()
    con.close()


@pytest.fixture
def tmp_db(tmp_path: Path) -> str:
    db_path = str(tmp_path / "test.db")
    _seed_db(db_path)
    return db_path


@pytest.fixture
def tmp_artifact_dir(tmp_path: Path) -> Path:
    d = tmp_path / "artifacts"
    d.mkdir()
    return d


# ── dataset tests ─────────────────────────────────────────────────────────


class TestDataset:
    def test_load_resolved(self, tmp_db: str):
        from onto_market.ml_research.dataset import load_resolved

        rows = load_resolved(db_path=tmp_db)
        assert len(rows) == 20
        assert all("market_id" in r for r in rows)

    def test_load_resolved_sorted_by_closed_time(self, tmp_db: str):
        from onto_market.ml_research.dataset import load_resolved

        rows = load_resolved(db_path=tmp_db)
        times = [r["closed_time"] for r in rows]
        assert times == sorted(times)

    def test_time_split(self, tmp_db: str):
        from onto_market.ml_research.dataset import load_resolved, time_split

        rows = load_resolved(db_path=tmp_db)
        train, val = time_split(rows, train_frac=0.7)
        assert len(train) == 14
        assert len(val) == 6
        assert len(train) + len(val) == len(rows)

    def test_time_split_empty(self):
        from onto_market.ml_research.dataset import time_split

        train, val = time_split([])
        assert train == []
        assert val == []

    def test_is_binary_resolved(self):
        from onto_market.ml_research.dataset import _is_binary_resolved

        assert _is_binary_resolved({
            "umaResolutionStatus": "resolved",
            "outcomePrices": '["1","0"]',
        })
        assert _is_binary_resolved({
            "umaResolutionStatus": "resolved",
            "outcomePrices": '["0","1"]',
        })
        assert not _is_binary_resolved({
            "umaResolutionStatus": "proposed",
            "outcomePrices": '["1","0"]',
        })
        assert not _is_binary_resolved({
            "umaResolutionStatus": "resolved",
            "outcomePrices": '["0.5","0.5"]',
        })

    def test_extract_row(self):
        from onto_market.ml_research.dataset import _extract_row

        raw = {
            "id": 123,
            "question": "Will X?",
            "category": "crypto",
            "tags": '["tag1"]',
            "volumeNum": 50000,
            "liquidityNum": 20000,
            "outcomePrices": '["1","0"]',
            "endDate": "2025-06-01",
            "closedTime": "2025-05-31",
        }
        row = _extract_row(raw)
        assert row["market_id"] == "123"
        assert row["resolved_yes"] == 1
        assert row["volume"] == 50000.0

    def test_fetch_resolved_mocked(self, tmp_db: str):
        """Mock the Gamma API and verify rows land in the DB."""
        from onto_market.ml_research.dataset import fetch_resolved

        fake_markets = [
            {
                "id": 999,
                "question": "Mock market?",
                "category": "test",
                "tags": "[]",
                "volumeNum": 100,
                "liquidityNum": 50,
                "outcomePrices": '["1","0"]',
                "umaResolutionStatus": "resolved",
                "endDate": "2025-01-01",
                "closedTime": "2025-01-01",
            }
        ]

        with patch("onto_market.ml_research.dataset.GammaConnector") as MockGamma:
            instance = MockGamma.return_value
            instance.get_markets.return_value = fake_markets

            count = fetch_resolved(max_markets=10, db_path=tmp_db)

        assert count >= 1


# ── features tests ────────────────────────────────────────────────────────


class TestFeatures:
    def test_extract_row_basic(self):
        from onto_market.ml_research.features import extract_row

        row = RESOLVED_ROWS[0]
        feats = extract_row(row)
        assert "implied_prob" in feats
        assert "log_volume" in feats
        assert "log_liquidity" in feats
        assert "days_to_end" in feats
        assert "tag_count" in feats
        assert feats["implied_prob"] == pytest.approx(0.3, abs=0.01)
        assert feats["tag_count"] == 2.0

    def test_extract_row_with_category_map(self):
        from onto_market.ml_research.features import extract_row

        cat_map = {"crypto": 0, "politics": 1}
        feats = extract_row(RESOLVED_ROWS[0], category_map=cat_map)
        assert feats["category_enc"] == 0.0
        feats2 = extract_row(RESOLVED_ROWS[1], category_map=cat_map)
        assert feats2["category_enc"] == 1.0

    def test_extract_row_with_vocab(self):
        from onto_market.ml_research.features import extract_row

        vocab = ["will", "event", "happen"]
        feats = extract_row(RESOLVED_ROWS[0], vocab=vocab)
        assert feats["bow_will"] == 1.0
        assert feats["bow_event"] == 1.0
        assert feats["bow_happen"] == 1.0

    def test_extract_matrix(self, tmp_db: str):
        from onto_market.ml_research.dataset import load_resolved
        from onto_market.ml_research.features import (
            build_category_map,
            extract_matrix,
        )

        rows = load_resolved(db_path=tmp_db)
        cat_map = build_category_map(rows)
        X, y, names = extract_matrix(rows, cat_map)
        assert X.shape[0] == 20
        assert X.shape[1] == len(names)
        assert y.shape == (20,)
        assert set(y) <= {0.0, 1.0}
        assert not np.isnan(X).any()

    def test_extract_matrix_empty(self):
        from onto_market.ml_research.features import extract_matrix

        X, y, names = extract_matrix([])
        assert X.shape == (0, 0)
        assert y.shape == (0,)

    def test_build_vocab(self):
        from onto_market.ml_research.features import build_vocab

        vocab = build_vocab(RESOLVED_ROWS, max_vocab=5)
        assert len(vocab) <= 5
        assert "will" in vocab

    def test_build_category_map(self):
        from onto_market.ml_research.features import build_category_map

        cat_map = build_category_map(RESOLVED_ROWS)
        assert "crypto" in cat_map
        assert "politics" in cat_map
        assert isinstance(cat_map["crypto"], int)


# ── evaluate tests ────────────────────────────────────────────────────────


class TestEvaluate:
    def test_brier_perfect(self):
        from onto_market.ml_research.evaluate import brier_score

        probs = np.array([1.0, 0.0, 1.0])
        labels = np.array([1.0, 0.0, 1.0])
        assert brier_score(probs, labels) == pytest.approx(0.0)

    def test_brier_worst(self):
        from onto_market.ml_research.evaluate import brier_score

        probs = np.array([0.0, 1.0])
        labels = np.array([1.0, 0.0])
        assert brier_score(probs, labels) == pytest.approx(1.0)

    def test_brier_naive(self):
        from onto_market.ml_research.evaluate import brier_score

        probs = np.array([0.5, 0.5, 0.5, 0.5])
        labels = np.array([1.0, 0.0, 1.0, 0.0])
        assert brier_score(probs, labels) == pytest.approx(0.25)

    def test_log_loss_perfect(self):
        from onto_market.ml_research.evaluate import log_loss

        probs = np.array([0.999, 0.001])
        labels = np.array([1.0, 0.0])
        assert log_loss(probs, labels) < 0.01

    def test_log_loss_bad(self):
        from onto_market.ml_research.evaluate import log_loss

        probs = np.array([0.1, 0.9])
        labels = np.array([1.0, 0.0])
        assert log_loss(probs, labels) > 1.0

    def test_calibration_buckets(self):
        from onto_market.ml_research.evaluate import calibration_buckets

        probs = np.array([0.1, 0.2, 0.3, 0.7, 0.8, 0.9])
        labels = np.array([0.0, 0.0, 1.0, 1.0, 1.0, 1.0])
        buckets = calibration_buckets(probs, labels, n_bins=5)
        assert len(buckets) == 5
        assert all("count" in b for b in buckets)
        total = sum(b["count"] for b in buckets)
        assert total == 6

    def test_calibration_error_perfect(self):
        from onto_market.ml_research.evaluate import calibration_error

        probs = np.array([0.0, 0.0, 1.0, 1.0])
        labels = np.array([0.0, 0.0, 1.0, 1.0])
        ece = calibration_error(probs, labels, n_bins=5)
        assert ece == pytest.approx(0.0, abs=0.01)

    def test_calibration_error_bad(self):
        from onto_market.ml_research.evaluate import calibration_error

        probs = np.array([0.9, 0.9, 0.1, 0.1])
        labels = np.array([0.0, 0.0, 1.0, 1.0])
        ece = calibration_error(probs, labels, n_bins=5)
        assert ece > 0.5

    def test_calibration_error_empty(self):
        from onto_market.ml_research.evaluate import calibration_error

        ece = calibration_error(np.array([]), np.array([]))
        assert ece == 0.0

    def test_edge_backtest(self):
        from onto_market.ml_research.evaluate import edge_backtest

        model_probs = np.array([0.7, 0.3, 0.8])
        implied_probs = np.array([0.5, 0.5, 0.5])
        labels = np.array([1.0, 0.0, 1.0])
        result = edge_backtest(model_probs, implied_probs, labels)
        assert "model_brier" in result
        assert "market_brier" in result
        assert "brier_lift" in result
        assert result["brier_lift"] == pytest.approx(
            result["market_brier"] - result["model_brier"], abs=1e-6
        )
        assert result["n_samples"] == 3

    def test_simulated_pnl_no_trades(self):
        from onto_market.ml_research.evaluate import simulated_pnl

        model_probs = np.array([0.51, 0.49])
        implied_probs = np.array([0.50, 0.50])
        labels = np.array([1.0, 0.0])
        result = simulated_pnl(model_probs, implied_probs, labels, edge_threshold=0.05)
        assert result["n_trades"] == 0
        assert result["total_pnl"] == 0.0

    def test_simulated_pnl_with_trades(self):
        from onto_market.ml_research.evaluate import simulated_pnl

        model_probs = np.array([0.8, 0.2, 0.7])
        implied_probs = np.array([0.5, 0.5, 0.5])
        labels = np.array([1.0, 0.0, 1.0])
        result = simulated_pnl(model_probs, implied_probs, labels, edge_threshold=0.03)
        assert result["n_trades"] == 3
        assert "win_rate" in result
        assert "max_drawdown" in result
        assert "roi" in result

    def test_simulated_pnl_keys(self):
        from onto_market.ml_research.evaluate import simulated_pnl

        result = simulated_pnl(
            np.array([0.9]), np.array([0.5]), np.array([1.0]),
            edge_threshold=0.03,
        )
        expected_keys = {"total_pnl", "n_trades", "win_rate", "max_drawdown", "roi"}
        assert expected_keys == set(result.keys())

    def test_promotion_score_gates_pass(self):
        from onto_market.ml_research.evaluate import promotion_score

        n = 30
        np.random.seed(42)
        model_probs = np.clip(np.random.rand(n), 0.1, 0.9)
        implied_probs = np.clip(np.random.rand(n), 0.1, 0.9)
        labels = (np.random.rand(n) > 0.5).astype(float)

        result = promotion_score(
            model_probs, implied_probs, labels,
            min_samples=20,
        )
        assert "brier" in result
        assert "composite_score" in result
        assert "gates" in result
        assert "promotable" in result
        assert result["gates"]["sufficient_samples"] is True
        assert result["n_samples"] == n

    def test_promotion_score_rejects_small_sample(self):
        from onto_market.ml_research.evaluate import promotion_score

        result = promotion_score(
            np.array([0.8, 0.2]),
            np.array([0.5, 0.5]),
            np.array([1.0, 0.0]),
            min_samples=20,
        )
        assert result["promotable"] is False
        assert result["gates"]["sufficient_samples"] is False

    def test_promotion_score_rejects_uncalibrated(self):
        from onto_market.ml_research.evaluate import promotion_score

        n = 30
        model_probs = np.array([0.95] * n)
        implied_probs = np.array([0.5] * n)
        labels = np.array([0.0] * 15 + [1.0] * 15)

        result = promotion_score(
            model_probs, implied_probs, labels,
            min_samples=10,
            max_calibration_error=0.05,
        )
        assert result["promotable"] is False
        assert result["gates"]["calibrated"] is False


# ── train tests ───────────────────────────────────────────────────────────


class TestTrain:
    def test_train_smoke(self, tmp_db: str):
        """Train on fixture data, verify it returns a model and reasonable Brier."""
        from onto_market.ml_research.train import train

        model, brier = train(db_path=tmp_db, max_age_days=0)
        assert model is not None
        assert 0.0 <= brier <= 1.0

    def test_train_too_few_rows(self, tmp_path: Path):
        """With < 10 rows, train should return baseline 0.25."""
        db = str(tmp_path / "tiny.db")
        _seed_db(db, RESOLVED_ROWS[:5])

        from onto_market.ml_research.train import train

        model, brier = train(db_path=db, max_age_days=0)
        assert model is None
        assert brier == pytest.approx(0.25)

    def test_train_prints_brier(self, tmp_db: str, capsys):
        """Verify the brier: <float> stdout contract."""
        from onto_market.ml_research.train import train

        train(db_path=tmp_db, max_age_days=0)
        captured = capsys.readouterr()
        assert "brier:" in captured.out


# ── artifacts tests ───────────────────────────────────────────────────────


class TestArtifacts:
    def test_save_and_load(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import get_latest, save_artifact

        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression()
        model.fit(np.array([[1], [2], [3]]), np.array([0, 1, 1]))
        model._onto_market_feature_names = ["implied_prob"]
        model._onto_market_category_map = {"crypto": 0}
        model._onto_market_vocab = []

        v = save_artifact(model, {"brier": 0.18}, artifact_dir=tmp_artifact_dir)
        assert v == 1

        result = get_latest(artifact_dir=tmp_artifact_dir)
        assert result is not None
        loaded_model, meta = result
        assert meta["version"] == 1
        assert meta["brier"] == 0.18
        assert meta["feature_names"] == ["implied_prob"]
        assert meta["category_map"] == {"crypto": 0}
        assert meta["vocab"] == []

    def test_promote(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import (
            get_latest,
            promote,
            save_artifact,
        )

        from sklearn.linear_model import LogisticRegression
        m = LogisticRegression()
        m.fit(np.array([[1], [2]]), np.array([0, 1]))

        save_artifact(m, {"brier": 0.20}, artifact_dir=tmp_artifact_dir)
        save_artifact(m, {"brier": 0.15}, artifact_dir=tmp_artifact_dir)

        promote(1, artifact_dir=tmp_artifact_dir)
        _, meta = get_latest(artifact_dir=tmp_artifact_dir)
        assert meta["version"] == 1

        promote(2, artifact_dir=tmp_artifact_dir)
        _, meta = get_latest(artifact_dir=tmp_artifact_dir)
        assert meta["version"] == 2

    def test_promote_invalid_version(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import promote

        with pytest.raises(ValueError, match="not found"):
            promote(999, artifact_dir=tmp_artifact_dir)

    def test_list_versions(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import list_versions, save_artifact

        from sklearn.linear_model import LogisticRegression
        m = LogisticRegression()
        m.fit(np.array([[1], [2]]), np.array([0, 1]))

        save_artifact(m, {"brier": 0.2}, artifact_dir=tmp_artifact_dir)
        save_artifact(m, {"brier": 0.1}, artifact_dir=tmp_artifact_dir)

        reg = list_versions(artifact_dir=tmp_artifact_dir)
        assert reg["latest"] == 2
        assert reg["versions"] == [1, 2]

    def test_status(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import save_artifact, status

        assert "No artifacts" in status(artifact_dir=tmp_artifact_dir)

        from sklearn.linear_model import LogisticRegression
        m = LogisticRegression()
        m.fit(np.array([[1], [2]]), np.array([0, 1]))
        save_artifact(m, {"brier": 0.18}, artifact_dir=tmp_artifact_dir)

        s = status(artifact_dir=tmp_artifact_dir)
        assert "v001" in s
        assert "0.18" in s

    def test_get_latest_empty(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import get_latest

        assert get_latest(artifact_dir=tmp_artifact_dir) is None


# ── runner tests ──────────────────────────────────────────────────────────


class TestRunner:
    def test_run_train_subprocess(self, tmp_db: str):
        """Verify _run_train can execute train.py and parse the Brier score."""
        from onto_market.ml_research.runner import _run_train

        brier, extras = _run_train("sklearn", db_path=tmp_db)
        assert brier is not None
        assert 0.0 <= brier <= 1.0

    def test_run_train_handles_crash(self, tmp_path: Path):
        """If train.py doesn't exist or crashes, _run_train returns None."""
        from onto_market.ml_research.runner import _run_train

        brier, extras = _run_train("sklearn", db_path=str(tmp_path / "nonexistent.db"))
        assert brier is None or (0.0 <= brier <= 1.0)

    def test_backup_and_restore(self, tmp_path: Path):
        from onto_market.ml_research.runner import (
            _TRAIN_PY,
            _backup_train,
            _restore_train,
        )

        original = _TRAIN_PY.read_text()
        backup = _backup_train("sklearn")
        assert Path(backup).read_text() == original

        _TRAIN_PY.write_text("# corrupted")
        _restore_train(backup, "sklearn")
        assert _TRAIN_PY.read_text() == original

        Path(backup).unlink(missing_ok=True)


class RecordingModel:
    def __init__(self):
        self.seen_X = None

    def predict_proba(self, X):
        self.seen_X = X
        return np.array([[0.2, 0.8]])


class TestInference:
    def test_predict_market_prior_uses_artifact_feature_order(self):
        from onto_market.ml_research.features import extract_row
        from onto_market.ml_research.inference import predict_market_prior

        market = {
            "question": "Will Bitcoin hit $100k?",
            "category": "crypto",
            "volume": 10000.0,
            "liquidity": 5000.0,
            "implied_prob_at_close": 0.42,
            "tags": json.dumps(["btc"]),
            "end_date": "2025-06-10T00:00:00Z",
            "closed_time": "2025-06-05T00:00:00Z",
        }
        category_map = {"crypto": 3}
        vocab = ["bitcoin"]
        feats = extract_row(market, category_map=category_map, vocab=vocab)
        feature_names = ["category_enc", "implied_prob", "bow_bitcoin"]

        model = RecordingModel()
        metadata = {
            "feature_names": feature_names,
            "category_map": category_map,
            "vocab": vocab,
        }

        with patch("onto_market.ml_research.inference.get_latest", return_value=(model, metadata)):
            prob = predict_market_prior(market, artifact_dir="unused")

        assert prob == pytest.approx(0.8)
        assert model.seen_X is not None
        assert model.seen_X.shape == (1, 3)
        assert model.seen_X[0].tolist() == [feats[name] for name in feature_names]

    def test_predict_market_prior_rejects_missing_metadata(self):
        from onto_market.ml_research.inference import predict_market_prior

        model = RecordingModel()
        market = {"question": "Test?", "category": "crypto"}

        with patch("onto_market.ml_research.inference.get_latest", return_value=(model, {"brier": 0.1})):
            assert predict_market_prior(market, artifact_dir="unused") is None

    def test_blend_with_ml_prior_clamps_weight(self):
        from onto_market.ml_research.inference import blend_with_ml_prior

        with patch("onto_market.ml_research.inference.predict_market_prior", return_value=0.2):
            blended = blend_with_ml_prior(
                llm_prob=0.8,
                market={"question": "Test"},
                artifact_dir="unused",
                weight=2.0,
            )

        assert blended == pytest.approx(0.2)


# ── local provider tests ────────────────────────────────────────────────


class TestLocalProvider:
    def test_llm_client_local_factory(self):
        from onto_market.utils.llm_client import LLMClient

        client = LLMClient.local(model="test-model")
        assert client.provider == "local"
        assert client.model == "test-model"
        assert "11434" in client.base_url

    def test_llm_client_local_default_model(self):
        from onto_market.utils.llm_client import LLMClient

        client = LLMClient.local()
        assert client.provider == "local"
        assert client.model is not None

    def test_llm_client_provider_override(self):
        from onto_market.utils.llm_client import LLMClient

        client = LLMClient(provider="local", base_url="http://test:1234/v1")
        kw = client._extra_kwargs()
        assert kw["provider"] == "local"
        assert kw["base_url"] == "http://test:1234/v1"

    def test_llm_client_no_override(self):
        from onto_market.utils.llm_client import LLMClient

        client = LLMClient()
        kw = client._extra_kwargs()
        assert kw == {}

    def test_ollama_completion_called(self):
        """Verify the local provider dispatches to _ollama_completion."""
        from onto_market.core.llm_router import llm_completion

        with patch("onto_market.core.llm_router._ollama_completion", return_value="hello") as mock:
            result = llm_completion(
                [{"role": "user", "content": "test"}],
                provider="local",
            )
        assert result == "hello"
        mock.assert_called_once()

    def test_resolve_researcher_local(self):
        from onto_market.ml_research.runner import _resolve_researcher

        client = _resolve_researcher(None, "local")
        assert client.provider == "local"

    def test_resolve_researcher_local_with_model(self):
        from onto_market.ml_research.runner import _resolve_researcher

        client = _resolve_researcher(None, "local/qwen2:7b")
        assert client.provider == "local"
        assert client.model == "qwen2:7b"

    def test_resolve_researcher_default(self):
        from onto_market.ml_research.runner import _resolve_researcher

        client = _resolve_researcher(None, None)
        assert client.provider is None

    def test_resolve_researcher_explicit_llm(self):
        from onto_market.ml_research.runner import _resolve_researcher
        from onto_market.utils.llm_client import LLMClient

        explicit = LLMClient(model="custom")
        result = _resolve_researcher(explicit, "local")
        assert result is explicit
