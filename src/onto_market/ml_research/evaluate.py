"""Evaluation metrics for probabilistic forecasters.

Primary metric: Brier score (lower is better).
All functions return plain dicts for JSON serialization.
"""
from __future__ import annotations

import math

import numpy as np


def brier_score(probs: np.ndarray, labels: np.ndarray) -> float:
    """Mean squared error between predicted probabilities and binary labels.

    ``probs`` ∈ [0, 1] — predicted P(YES).
    ``labels`` ∈ {0, 1} — 1 if YES resolved.

    Returns a float in [0, 1]; lower is better.  A naive 0.5 baseline
    scores 0.25.
    """
    probs = np.asarray(probs, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.float64)
    return float(np.mean((probs - labels) ** 2))


def log_loss(probs: np.ndarray, labels: np.ndarray, eps: float = 1e-15) -> float:
    """Binary cross-entropy / log-loss.  Lower is better."""
    probs = np.clip(np.asarray(probs, dtype=np.float64), eps, 1 - eps)
    labels = np.asarray(labels, dtype=np.float64)
    return float(-np.mean(labels * np.log(probs) + (1 - labels) * np.log(1 - probs)))


def calibration_buckets(
    probs: np.ndarray,
    labels: np.ndarray,
    n_bins: int = 10,
) -> list[dict]:
    """Reliability diagram data — bin predicted probs and compute actual frequencies.

    Returns a list of dicts with keys: ``bin_lower``, ``bin_upper``,
    ``mean_predicted``, ``mean_actual``, ``count``.
    """
    probs = np.asarray(probs, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.float64)
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    buckets: list[dict] = []

    for lo, hi in zip(bins[:-1], bins[1:]):
        if hi < 1.0:
            mask = (probs >= lo) & (probs < hi)
        else:
            mask = (probs >= lo) & (probs <= hi)
        count = int(mask.sum())
        buckets.append({
            "bin_lower": round(float(lo), 4),
            "bin_upper": round(float(hi), 4),
            "mean_predicted": round(float(probs[mask].mean()), 4) if count else None,
            "mean_actual": round(float(labels[mask].mean()), 4) if count else None,
            "count": count,
        })

    return buckets


def edge_backtest(
    model_probs: np.ndarray,
    implied_probs: np.ndarray,
    labels: np.ndarray,
) -> dict:
    """Simulate betting edge: compare model Brier to market-implied Brier.

    Returns a dict with model_brier, market_brier, brier_lift,
    and mean_abs_edge.
    """
    model_probs = np.asarray(model_probs, dtype=np.float64)
    implied_probs = np.asarray(implied_probs, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.float64)

    model_brier = brier_score(model_probs, labels)
    market_brier = brier_score(implied_probs, labels)

    return {
        "model_brier": round(model_brier, 6),
        "market_brier": round(market_brier, 6),
        "brier_lift": round(market_brier - model_brier, 6),
        "mean_abs_edge": round(float(np.mean(np.abs(model_probs - implied_probs))), 6),
        "n_samples": int(len(labels)),
    }
