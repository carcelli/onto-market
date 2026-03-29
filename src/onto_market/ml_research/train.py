"""Editable PyTorch training surface for the autoresearch loop.

**THIS IS THE ONLY FILE THE AUTORESEARCH LOOP MAY EDIT.**

Contract:
  - Must print exactly one line matching ``brier: <float>`` to stdout.
  - Must print ``training_seconds: <float>`` and ``peak_vram_mb: <float>``.
  - Must complete within the time budget (default 300 s / 5 min).
  - ``train()`` returns ``(model, brier)``.

Tiny MLP so gpt-oss-20b can freely edit architecture, LR, depth, etc.
Uses real resolved markets with proper temporal split (no leakage).
"""
from __future__ import annotations

import sys
import time

import numpy as np
import torch
import torch.nn as nn

from onto_market.ml_research.dataset import load_resolved, time_split
from onto_market.ml_research.evaluate import brier_score
from onto_market.ml_research.features import (
    build_category_map,
    build_vocab,
    extract_matrix,
)

# ========================= CONFIG (agent edits this) =========================
DEPTH = 2                    # number of hidden layers
HIDDEN = 64                  # size of each hidden layer
DROPOUT = 0.1                # dropout rate (0 to disable)
LR = 0.001                   # learning rate
WEIGHT_DECAY = 1e-4          # AdamW weight decay
BATCH_SIZE = 256             # safe on 3050 8 GB
MAX_EPOCHS = 200             # max training epochs
TIME_BUDGET = 300            # 5 minutes wall-clock
USE_VOCAB = False            # bag-of-words features from question text
MAX_VOCAB = 200              # vocab size if USE_VOCAB enabled
# =============================================================================


class TinyForecaster(nn.Module):
    """Small MLP — gpt-oss-20b can freely edit architecture."""

    def __init__(self, n_features: int):
        super().__init__()
        layers: list[nn.Module] = []
        prev = n_features
        for _ in range(DEPTH):
            layers.append(nn.Linear(prev, HIDDEN))
            layers.append(nn.ReLU())
            if DROPOUT > 0:
                layers.append(nn.Dropout(DROPOUT))
            prev = HIDDEN
        layers.append(nn.Linear(prev, 1))
        layers.append(nn.Sigmoid())
        self.net = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)


# ── Training entrypoint ──────────────────────────────────────────────────


def train(db_path: str | None = None, max_age_days: int | None = None) -> tuple[object | None, float]:
    """Train a tiny MLP on resolved markets and return ``(model, brier)``."""
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

    # Device setup
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if device.type == "cuda":
        torch.cuda.reset_peak_memory_stats()

    X_train_t = torch.tensor(X_train, dtype=torch.float32, device=device)
    y_train_t = torch.tensor(y_train, dtype=torch.float32, device=device)
    X_val_t = torch.tensor(X_val, dtype=torch.float32, device=device)

    n_features = X_train.shape[1]
    model = TinyForecaster(n_features).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=LR, weight_decay=WEIGHT_DECAY)
    loss_fn = nn.MSELoss()  # MSE on probabilities = Brier loss

    print(f"Model: {sum(p.numel() for p in model.parameters()):,} params on {device}")

    start = time.time()
    best_brier = float("inf")
    best_state = None

    for epoch in range(MAX_EPOCHS):
        if time.time() - start > TIME_BUDGET:
            break

        # Train one epoch with mini-batches
        model.train()
        idx = torch.randperm(len(X_train_t), device=device)
        for i in range(0, len(idx), BATCH_SIZE):
            batch_idx = idx[i : i + BATCH_SIZE]
            preds = model(X_train_t[batch_idx])
            loss = loss_fn(preds, y_train_t[batch_idx])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # Validate and track best
        model.eval()
        with torch.no_grad():
            val_preds = model(X_val_t).cpu().numpy()

        val_brier = brier_score(val_preds, y_val)
        if val_brier < best_brier:
            best_brier = val_brier
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

    total_seconds = time.time() - start
    peak_mb = (
        torch.cuda.max_memory_allocated() / (1024 * 1024)
        if device.type == "cuda"
        else 0.0
    )

    # Restore best checkpoint
    if best_state is not None:
        model.load_state_dict(best_state)
    model.cpu().eval()

    # Attach metadata for artifact storage
    model._onto_market_feature_names = list(feature_names)
    model._onto_market_category_map = dict(cat_map)
    model._onto_market_vocab = list(vocab or [])

    print(f"brier: {best_brier:.6f}", flush=True)
    print(f"training_seconds: {total_seconds:.1f}", flush=True)
    print(f"peak_vram_mb: {peak_mb:.1f}", flush=True)
    return model, best_brier


if __name__ == "__main__":
    db = sys.argv[1] if len(sys.argv) > 1 else None
    train(db_path=db)
