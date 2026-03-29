"""Editable PyTorch training surface for the autoresearch loop.

**THIS IS THE ONLY FILE THE AUTORESEARCH LOOP MAY EDIT (torch mode).**

Contract:
  - Must print exactly one line matching ``brier: <float>`` to stdout.
  - Must print ``training_seconds: <float>`` and ``peak_vram_mb: <float>``.
  - Must complete within the time budget (default 300 s / 5 min).
  - Returns the trained model object and the Brier score.

The runner reads stdout, parses the Brier score, and decides whether to
keep or reject the change.  Everything else (data loading, feature
extraction, evaluation) is imported from sibling modules.
"""
from __future__ import annotations

import sys
import time

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from onto_market.ml_research.dataset import load_resolved, time_split
from onto_market.ml_research.evaluate import brier_score
from onto_market.ml_research.features import (
    build_category_map,
    build_vocab,
    extract_matrix,
)
from onto_market.ml_research.models import DeviceConfig, TinyForecaster

# ── Hyperparams (autoresearch may change everything below) ───────────────

MODEL_PARAMS: dict = {
    "hidden": 64,
    "depth": 2,
    "dropout": 0.1,
}

LR = 1e-3
WEIGHT_DECAY = 1e-4
BATCH_SIZE = 256
MAX_EPOCHS = 200
TIME_BUDGET = 300  # seconds

USE_VOCAB = False
MAX_VOCAB = 200


def build_model(n_features: int) -> TinyForecaster:
    return TinyForecaster(n_features=n_features, **MODEL_PARAMS)


# ── Training entrypoint ──────────────────────────────────────────────────


def train(db_path: str | None = None, max_age_days: int | None = None) -> tuple[object | None, float]:
    """Train a PyTorch model on resolved markets and return ``(model, brier)``.

    Prints ``brier: <float>`` to stdout as required by the runner contract.
    """
    from onto_market.config import config

    kwargs: dict = {}
    if db_path:
        kwargs["db_path"] = db_path
    age = max_age_days if max_age_days is not None else config.ML_MAX_AGE_DAYS
    if age and age > 0:
        kwargs["max_age_days"] = age

    rows = load_resolved(**kwargs)
    if len(rows) < 10:
        print("brier: 0.2500", flush=True)
        print("training_seconds: 0.0", flush=True)
        print("peak_vram_mb: 0.0", flush=True)
        return None, 0.25

    train_rows, val_rows = time_split(rows)
    if not val_rows:
        print("brier: 0.2500", flush=True)
        print("training_seconds: 0.0", flush=True)
        print("peak_vram_mb: 0.0", flush=True)
        return None, 0.25

    cat_map = build_category_map(train_rows)
    vocab = build_vocab(train_rows, max_vocab=MAX_VOCAB) if USE_VOCAB else None

    X_train, y_train, feature_names = extract_matrix(train_rows, cat_map, vocab)
    X_val, y_val, _ = extract_matrix(val_rows, cat_map, vocab)

    dev = DeviceConfig()
    dev.reset_peak()
    device = torch.device(dev.device)
    dtype = dev.dtype

    X_train_t = torch.tensor(X_train, dtype=dtype, device=device)
    y_train_t = torch.tensor(y_train, dtype=dtype, device=device)
    X_val_t = torch.tensor(X_val, dtype=dtype, device=device)

    train_ds = TensorDataset(X_train_t, y_train_t)
    train_dl = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)

    n_features = X_train.shape[1]
    model = build_model(n_features)
    model = model.to(device=device, dtype=dtype)

    optimizer = torch.optim.AdamW(
        model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY
    )
    loss_fn = nn.MSELoss()  # Brier loss = MSE on probabilities

    start = time.time()
    best_val_brier = float("inf")
    best_state = None

    for epoch in range(MAX_EPOCHS):
        elapsed = time.time() - start
        if elapsed > TIME_BUDGET:
            break

        model.train()
        for xb, yb in train_dl:
            preds = model(xb)
            loss = loss_fn(preds, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_preds = model(X_val_t).cpu().numpy()

        val_brier = brier_score(val_preds, y_val)
        if val_brier < best_val_brier:
            best_val_brier = val_brier
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    total_seconds = time.time() - start
    peak_mb = dev.peak_vram_mb()

    if best_state is not None:
        model.load_state_dict(best_state)
    model.cpu().eval()

    model._onto_market_feature_names = list(feature_names)
    model._onto_market_category_map = dict(cat_map)
    model._onto_market_vocab = list(vocab or [])
    model._onto_market_hyperparams = model.hyperparams()

    print(f"brier: {best_val_brier:.6f}", flush=True)
    print(f"training_seconds: {total_seconds:.1f}", flush=True)
    print(f"peak_vram_mb: {peak_mb:.1f}", flush=True)
    return model, best_val_brier


if __name__ == "__main__":
    db = sys.argv[1] if len(sys.argv) > 1 else None
    train(db_path=db)
