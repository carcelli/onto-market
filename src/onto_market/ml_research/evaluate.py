"""Frozen evaluator for probabilistic forecasters.

Primary metric: Brier score (lower is better).
Secondary metrics: calibration error, simulated PnL, drawdown, turnover.
All functions return plain dicts / floats for JSON serialization.

This module is part of the **frozen evaluator contract** — the autoresearch
loop must NEVER edit this file.  The researcher edits train.py / torch_train.py;
this module judges results.
"""
from __future__ import annotations

import math

import numpy as np


# ── Core probability metrics ────────────────────────────────────────────


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


# ── Calibration ─────────────────────────────────────────────────────────


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


def calibration_error(
    probs: np.ndarray,
    labels: np.ndarray,
    n_bins: int = 10,
) -> float:
    """Expected calibration error (ECE).

    Weighted average of |mean_predicted - mean_actual| across bins.
    Returns 0.0 for perfect calibration.
    """
    buckets = calibration_buckets(probs, labels, n_bins)
    n = len(probs)
    if n == 0:
        return 0.0
    ece = 0.0
    for b in buckets:
        if b["count"] > 0 and b["mean_predicted"] is not None and b["mean_actual"] is not None:
            ece += b["count"] * abs(b["mean_predicted"] - b["mean_actual"])
    return round(ece / n, 6)


# ── Edge / economic backtest ────────────────────────────────────────────


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


def simulated_pnl(
    model_probs: np.ndarray,
    implied_probs: np.ndarray,
    labels: np.ndarray,
    fee_rate: float = 0.02,
    slippage_bps: float = 50.0,
    edge_threshold: float = 0.03,
    unit_stake: float = 1.0,
) -> dict:
    """Walk-forward simulated PnL on resolved markets.

    For each market where ``|model_prob - implied_prob| > edge_threshold``:
      - BUY YES if model_prob > implied_prob, else BUY NO.
      - Payout: ``unit_stake / price`` if correct, else 0.
      - Cost: ``unit_stake + fees + slippage``.

    Returns: total_pnl, n_trades (turnover), max_drawdown, win_rate, roi.
    """
    model_probs = np.asarray(model_probs, dtype=np.float64)
    implied_probs = np.asarray(implied_probs, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.float64)

    edges = model_probs - implied_probs
    slippage_frac = slippage_bps / 10_000.0

    cumulative = 0.0
    peak = 0.0
    max_dd = 0.0
    trades = 0
    wins = 0
    pnl_series: list[float] = []

    for i in range(len(edges)):
        if abs(edges[i]) < edge_threshold:
            continue

        trades += 1
        buy_yes = edges[i] > 0
        price = float(implied_probs[i])
        price = max(0.01, min(0.99, price))

        cost = unit_stake * (1.0 + fee_rate + slippage_frac)

        if buy_yes:
            payout = (unit_stake / price) if labels[i] == 1.0 else 0.0
        else:
            no_price = 1.0 - price
            no_price = max(0.01, min(0.99, no_price))
            payout = (unit_stake / no_price) if labels[i] == 0.0 else 0.0

        trade_pnl = payout - cost
        cumulative += trade_pnl
        pnl_series.append(cumulative)

        if cumulative > peak:
            peak = cumulative
        dd = peak - cumulative
        if dd > max_dd:
            max_dd = dd

        if trade_pnl > 0:
            wins += 1

    total_cost = trades * unit_stake * (1.0 + fee_rate + slippage_frac)
    return {
        "total_pnl": round(cumulative, 4),
        "n_trades": trades,
        "win_rate": round(wins / trades, 4) if trades else 0.0,
        "max_drawdown": round(max_dd, 4),
        "roi": round(cumulative / total_cost, 4) if total_cost > 0 else 0.0,
    }


# ── Promotion gate ──────────────────────────────────────────────────────


def promotion_score(
    model_probs: np.ndarray,
    implied_probs: np.ndarray,
    labels: np.ndarray,
    *,
    min_samples: int = 20,
    max_calibration_error: float = 0.15,
    max_turnover_frac: float = 0.80,
    edge_threshold: float = 0.03,
) -> dict:
    """Compute a composite promotion score with hard risk gates.

    The autoresearch loop calls this to decide whether to promote a
    candidate model.  The score combines forecast quality (Brier, log-loss,
    calibration) with economic quality (simulated PnL, drawdown).

    Hard gates (any failure → ``promotable=False``):
      - ``n_samples >= min_samples`` — reject thin evaluations.
      - ``calibration_error <= max_calibration_error`` — reject uncalibrated.
      - ``turnover_frac <= max_turnover_frac`` — reject overtrading.

    Returns a dict with all sub-metrics plus ``promotable`` bool and
    ``composite_score`` float (higher is better, only meaningful when
    promotable).
    """
    model_probs = np.asarray(model_probs, dtype=np.float64)
    implied_probs = np.asarray(implied_probs, dtype=np.float64)
    labels = np.asarray(labels, dtype=np.float64)
    n = len(labels)

    brier = brier_score(model_probs, labels)
    ll = log_loss(model_probs, labels)
    ece = calibration_error(model_probs, labels)
    edge = edge_backtest(model_probs, implied_probs, labels)
    pnl = simulated_pnl(
        model_probs, implied_probs, labels,
        edge_threshold=edge_threshold,
    )

    turnover_frac = pnl["n_trades"] / n if n > 0 else 0.0

    # Hard gates
    gates: dict[str, bool] = {
        "sufficient_samples": n >= min_samples,
        "calibrated": ece <= max_calibration_error,
        "turnover_ok": turnover_frac <= max_turnover_frac,
    }
    promotable = all(gates.values())

    # Composite: lower Brier is better → invert; add PnL lift; penalize ECE.
    # Scale so that the naive baseline (brier=0.25, ece=0.1, pnl=0) ≈ 0.
    composite = (0.25 - brier) * 4.0 + pnl["roi"] * 0.5 - ece * 2.0

    return {
        "brier": round(brier, 6),
        "log_loss": round(ll, 6),
        "calibration_error": round(ece, 6),
        "brier_lift": edge["brier_lift"],
        "mean_abs_edge": edge["mean_abs_edge"],
        "total_pnl": pnl["total_pnl"],
        "n_trades": pnl["n_trades"],
        "win_rate": pnl["win_rate"],
        "max_drawdown": pnl["max_drawdown"],
        "roi": pnl["roi"],
        "turnover_frac": round(turnover_frac, 4),
        "n_samples": n,
        "gates": gates,
        "promotable": promotable,
        "composite_score": round(composite, 6),
    }
