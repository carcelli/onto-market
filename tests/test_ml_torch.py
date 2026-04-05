"""Tests for PyTorch autoresearch subsystem.

Covers: models, torch_train, artifacts (torch round-trip), inference dispatch.
All tests use synthetic fixture data — no network calls, no GPU required.
Tests are skipped if torch is not installed.
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pytest

torch = pytest.importorskip("torch")

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


# ── models tests ─────────────────────────────────────────────────────────


class TestModels:
    def test_tiny_forecaster_forward(self):
        from onto_market.ml_research.models import TinyForecaster

        model = TinyForecaster(n_features=6, hidden=32, depth=2, dropout=0.1)
        x = torch.randn(4, 6)
        out = model(x)
        assert out.shape == (4,)
        assert (out >= 0).all() and (out <= 1).all()

    def test_tiny_forecaster_clamps_params(self):
        from onto_market.ml_research.models import MAX_DEPTH, MAX_HIDDEN, TinyForecaster

        model = TinyForecaster(n_features=6, hidden=9999, depth=99, dropout=0.9)
        assert model._hidden <= MAX_HIDDEN
        assert model._depth <= MAX_DEPTH
        assert model._dropout <= 0.5

    def test_tiny_forecaster_hyperparams(self):
        from onto_market.ml_research.models import TinyForecaster

        model = TinyForecaster(n_features=10, hidden=64, depth=2, dropout=0.1)
        hp = model.hyperparams()
        assert hp["architecture"] == "MLP"
        assert hp["n_features"] == 10
        assert hp["hidden"] == 64
        assert hp["depth"] == 2

    def test_tiny_transformer_forward(self):
        from onto_market.ml_research.models import TinyTransformerForecaster

        model = TinyTransformerForecaster(
            n_features=6, d_model=16, n_heads=2, n_layers=2, dropout=0.1
        )
        x = torch.randn(4, 6)
        out = model(x)
        assert out.shape == (4,)
        assert (out >= 0).all() and (out <= 1).all()

    def test_tiny_transformer_clamps_params(self):
        from onto_market.ml_research.models import (
            MAX_DEPTH,
            MAX_HIDDEN,
            TinyTransformerForecaster,
        )

        model = TinyTransformerForecaster(
            n_features=6, d_model=9999, n_heads=99, n_layers=99
        )
        assert model._d_model <= MAX_HIDDEN
        assert model._n_layers <= MAX_DEPTH
        assert model._d_model % model._n_heads == 0

    def test_tiny_transformer_hyperparams(self):
        from onto_market.ml_research.models import TinyTransformerForecaster

        model = TinyTransformerForecaster(n_features=6, d_model=32, n_heads=2)
        hp = model.hyperparams()
        assert hp["architecture"] == "Transformer"
        assert hp["n_features"] == 6
        assert hp["d_model"] == 32

    def test_device_config_cpu(self):
        from onto_market.ml_research.models import DeviceConfig

        dev = DeviceConfig()
        assert dev.device in ("cpu", "cuda")
        assert dev.dtype == torch.float32
        assert dev.check_vram()


# ── torch_train tests ────────────────────────────────────────────────────


class TestTorchTrain:
    def test_train_smoke(self, tmp_db: str):
        from onto_market.ml_research.torch_train import train

        model, brier = train(db_path=tmp_db, max_age_days=0)
        assert model is not None
        assert 0.0 <= brier <= 1.0

    def test_train_too_few_rows(self, tmp_path: Path):
        db = str(tmp_path / "tiny.db")
        _seed_db(db, RESOLVED_ROWS[:5])

        from onto_market.ml_research.torch_train import train

        model, brier = train(db_path=db)
        assert model is None
        assert brier == pytest.approx(0.25)

    def test_train_prints_contracts(self, tmp_db: str, capsys):
        from onto_market.ml_research.torch_train import train

        train(db_path=tmp_db, max_age_days=0)
        captured = capsys.readouterr()
        assert "brier:" in captured.out
        assert "training_seconds:" in captured.out
        assert "peak_vram_mb:" in captured.out

    def test_train_model_has_metadata_attrs(self, tmp_db: str):
        from onto_market.ml_research.torch_train import train

        model, _ = train(db_path=tmp_db, max_age_days=0)
        assert model is not None
        assert hasattr(model, "_onto_market_feature_names")
        assert hasattr(model, "_onto_market_category_map")
        assert hasattr(model, "_onto_market_vocab")
        assert hasattr(model, "_onto_market_hyperparams")
        assert isinstance(model._onto_market_feature_names, list)


# ── artifacts torch round-trip ───────────────────────────────────────────


class TestArtifactsTorch:
    def _make_model(self):
        from onto_market.ml_research.models import TinyForecaster

        model = TinyForecaster(n_features=6, hidden=32, depth=2)
        model._onto_market_feature_names = [
            "implied_prob", "log_volume", "log_liquidity",
            "days_to_end", "tag_count", "category_enc",
        ]
        model._onto_market_category_map = {"crypto": 0, "politics": 1}
        model._onto_market_vocab = []
        return model

    def test_save_and_load_torch(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import get_latest, save_artifact

        model = self._make_model()
        x_in = torch.randn(2, 6)
        model.eval()
        with torch.no_grad():
            expected = model(x_in)

        v = save_artifact(
            model,
            {"brier": 0.15, "model_type": "torch"},
            artifact_dir=tmp_artifact_dir,
        )
        assert v == 1
        assert (tmp_artifact_dir / "model_v001.pt").exists()
        assert (tmp_artifact_dir / "metadata_v001.json").exists()

        result = get_latest(artifact_dir=tmp_artifact_dir)
        assert result is not None
        loaded, meta = result
        assert meta["model_type"] == "torch"
        assert meta["brier"] == 0.15
        assert meta["feature_names"] == model._onto_market_feature_names

        loaded.eval()
        with torch.no_grad():
            actual = loaded(x_in)
        assert torch.allclose(expected, actual, atol=1e-5)

    def test_save_torch_infers_model_type(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import get_metadata, save_artifact

        model = self._make_model()
        v = save_artifact(model, {"brier": 0.2}, artifact_dir=tmp_artifact_dir)
        meta = get_metadata(v, artifact_dir=tmp_artifact_dir)
        assert meta is not None
        assert meta["model_type"] == "torch"

    def test_promote_torch(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import (
            get_latest,
            promote,
            save_artifact,
        )

        m1 = self._make_model()
        m2 = self._make_model()

        save_artifact(m1, {"brier": 0.20, "model_type": "torch"}, artifact_dir=tmp_artifact_dir)
        save_artifact(m2, {"brier": 0.15, "model_type": "torch"}, artifact_dir=tmp_artifact_dir)

        promote(1, artifact_dir=tmp_artifact_dir)
        result = get_latest(artifact_dir=tmp_artifact_dir)
        assert result is not None
        _, meta = result
        assert meta["version"] == 1

        promote(2, artifact_dir=tmp_artifact_dir)
        result = get_latest(artifact_dir=tmp_artifact_dir)
        assert result is not None
        _, meta = result
        assert meta["version"] == 2

    def test_status_shows_torch(self, tmp_artifact_dir: Path):
        from onto_market.ml_research.artifacts import save_artifact, status

        model = self._make_model()
        save_artifact(model, {"brier": 0.18, "model_type": "torch"}, artifact_dir=tmp_artifact_dir)

        s = status(artifact_dir=tmp_artifact_dir)
        assert "torch" in s
        assert "0.18" in s

    def test_mixed_sklearn_and_torch(self, tmp_artifact_dir: Path):
        """Save an sklearn model, then a torch model; promoted should load correctly."""
        from onto_market.ml_research.artifacts import get_latest, promote, save_artifact

        from sklearn.linear_model import LogisticRegression
        sk_model = LogisticRegression()
        sk_model.fit(np.array([[1], [2], [3]]), np.array([0, 1, 1]))
        sk_model._onto_market_feature_names = ["f1"]
        sk_model._onto_market_category_map = {"a": 0}
        sk_model._onto_market_vocab = []

        save_artifact(sk_model, {"brier": 0.20, "model_type": "sklearn"}, artifact_dir=tmp_artifact_dir)

        torch_model = self._make_model()
        save_artifact(torch_model, {"brier": 0.15, "model_type": "torch"}, artifact_dir=tmp_artifact_dir)

        promote(2, artifact_dir=tmp_artifact_dir)
        result = get_latest(artifact_dir=tmp_artifact_dir)
        assert result is not None
        loaded, meta = result
        assert meta["model_type"] == "torch"
        assert isinstance(loaded, torch.nn.Module)

        promote(1, artifact_dir=tmp_artifact_dir)
        result = get_latest(artifact_dir=tmp_artifact_dir)
        assert result is not None
        loaded, meta = result
        assert meta["model_type"] == "sklearn"
        assert hasattr(loaded, "predict_proba")


# ── inference dispatch tests ─────────────────────────────────────────────


class TestInferenceDispatch:
    def test_predict_torch_model(self):
        from onto_market.ml_research.inference import predict_market_prior
        from onto_market.ml_research.models import TinyForecaster

        model = TinyForecaster(n_features=6, hidden=16, depth=1)
        model._onto_market_feature_names = [
            "implied_prob", "log_volume", "log_liquidity",
            "days_to_end", "tag_count", "category_enc",
        ]
        model._onto_market_category_map = {"crypto": 0}
        model._onto_market_vocab = []
        model.eval()

        metadata = {
            "model_type": "torch",
            "feature_names": model._onto_market_feature_names,
            "category_map": model._onto_market_category_map,
            "vocab": model._onto_market_vocab,
        }

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

        with patch("onto_market.ml_research.inference.get_latest", return_value=(model, metadata)):
            prob = predict_market_prior(market, artifact_dir="unused")

        assert prob is not None
        assert 0.01 <= prob <= 0.99

    def test_predict_sklearn_model_still_works(self):
        from onto_market.ml_research.inference import predict_market_prior

        class FakeSklearn:
            def predict_proba(self, X):
                return np.array([[0.3, 0.7]])

        model = FakeSklearn()
        metadata = {
            "model_type": "sklearn",
            "feature_names": ["implied_prob", "log_volume", "log_liquidity",
                              "days_to_end", "tag_count", "category_enc"],
            "category_map": {"crypto": 0},
            "vocab": [],
        }

        market = {
            "question": "Test?",
            "category": "crypto",
            "volume": 1000.0,
            "liquidity": 500.0,
            "implied_prob_at_close": 0.5,
            "tags": "[]",
            "end_date": "2025-06-10T00:00:00Z",
            "closed_time": "2025-06-05T00:00:00Z",
        }

        with patch("onto_market.ml_research.inference.get_latest", return_value=(model, metadata)):
            prob = predict_market_prior(market, artifact_dir="unused")

        assert prob == pytest.approx(0.7)

    def test_blend_uses_torch_model(self):
        from onto_market.ml_research.inference import blend_with_ml_prior

        with patch("onto_market.ml_research.inference.predict_market_prior", return_value=0.6):
            blended = blend_with_ml_prior(
                llm_prob=0.4,
                market={"question": "Test"},
                artifact_dir="unused",
                weight=0.5,
            )

        assert blended == pytest.approx(0.5)


# ── runner mode tests ────────────────────────────────────────────────────


class TestRunnerMode:
    def test_target_file_sklearn(self):
        from onto_market.ml_research.runner import _target_file

        path = _target_file("sklearn")
        assert path.name == "train.py"

    def test_target_file_torch(self):
        from onto_market.ml_research.runner import _target_file

        path = _target_file("torch")
        assert path.name == "torch_train.py"

    def test_default_timeouts(self):
        from onto_market.ml_research.runner import _DEFAULT_TIMEOUTS

        assert _DEFAULT_TIMEOUTS["sklearn"] == 300
        assert _DEFAULT_TIMEOUTS["torch"] == 300

    def test_is_oom(self):
        from onto_market.ml_research.runner import _is_oom

        assert _is_oom("RuntimeError: CUDA out of memory. Tried to allocate 2GB")
        assert _is_oom("torch.cuda.OutOfMemoryError: ...")
        assert _is_oom("CUDA error: out of memory")
        assert not _is_oom("ModuleNotFoundError: No module named 'foo'")

    def test_run_torch_train_subprocess(self, tmp_db: str):
        from onto_market.ml_research.runner import _run_train

        brier, extras = _run_train("torch", db_path=tmp_db, timeout=120)
        assert brier is not None
        assert 0.0 <= brier <= 1.0
        assert "training_seconds" in extras
        assert "peak_vram_mb" in extras
