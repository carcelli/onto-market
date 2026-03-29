"""Editable training surface for the autoresearch loop.

**THIS IS THE ONLY FILE THE AUTORESEARCH LOOP MAY EDIT.**

Contract:
  - Must print exactly one line matching ``brier: <float>`` to stdout.
  - Must complete in under 60 seconds on the validation set.
  - Returns the trained model object and the Brier score.

The runner reads stdout, parses the Brier score, and decides whether to
keep or reject the change.  Everything else (data loading, feature
extraction, evaluation) is imported from sibling modules.
"""
from __future__ import annotations

import sys

import numpy as np
from sklearn.ensemble import HistGradientBoostingClassifier

from onto_market.ml_research.dataset import load_resolved, time_split
from onto_market.ml_research.evaluate import brier_score
from onto_market.ml_research.features import (
    build_category_map,
    build_vocab,
    extract_matrix,
)

# ── Model definition (autoresearch may change everything below) ───────────

MODEL_PARAMS: dict = {
    "max_iter": 200,
    "max_depth": 5,
    "learning_rate": 0.1,
    "min_samples_leaf": 10,
    "l2_regularization": 1.0,
    "max_bins": 128,
    "random_state": 42,
}

USE_VOCAB = False
MAX_VOCAB = 200


def build_model() -> HistGradientBoostingClassifier:
    return HistGradientBoostingClassifier(**MODEL_PARAMS)


# ── Training entrypoint ──────────────────────────────────────────────────

def train(db_path: str | None = None) -> tuple[object, float]:
    """Train a model on resolved markets and return ``(model, brier)``.

    Prints ``brier: <float>`` to stdout as required by the runner contract.
    """
    kwargs: dict = {}
    if db_path:
        kwargs["db_path"] = db_path

    rows = load_resolved(**kwargs)
    if len(rows) < 10:
        print("brier: 0.2500", flush=True)
        return None, 0.25

    train_rows, val_rows = time_split(rows)
    if not val_rows:
        print("brier: 0.2500", flush=True)
        return None, 0.25

    cat_map = build_category_map(train_rows)
    vocab = build_vocab(train_rows, max_vocab=MAX_VOCAB) if USE_VOCAB else None

    X_train, y_train, feature_names = extract_matrix(train_rows, cat_map, vocab)
    X_val, y_val, _ = extract_matrix(val_rows, cat_map, vocab)

    model = build_model()
    model.fit(X_train, y_train)
    model._onto_market_feature_names = list(feature_names)
    model._onto_market_category_map = dict(cat_map)
    model._onto_market_vocab = list(vocab or [])

    probs = model.predict_proba(X_val)[:, 1]
    score = brier_score(probs, y_val)

    print(f"brier: {score:.6f}", flush=True)
    return model, score


if __name__ == "__main__":
    db = sys.argv[1] if len(sys.argv) > 1 else None
    train(db_path=db)
