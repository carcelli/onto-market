"""Point-in-time-safe feature extraction for resolved markets.

Every feature must be derivable *before* resolution — no leakage allowed.
"""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from typing import Any

import numpy as np


def _safe_float(v: Any, default: float = 0.0) -> float:
    try:
        f = float(v)
        return default if (math.isnan(f) or math.isinf(f)) else f
    except (TypeError, ValueError):
        return default


def _parse_json(v: Any, default: Any = None) -> Any:
    if isinstance(v, str):
        try:
            return json.loads(v)
        except (json.JSONDecodeError, ValueError):
            return default
    return v if v is not None else default


def _days_to_end(row: dict) -> float:
    """Approximate market duration in days from end_date string.

    If end_date is missing or unparseable, returns 30.0 as a neutral default.
    """
    end = row.get("end_date", "")
    closed = row.get("closed_time", "")
    if not end:
        return 30.0
    try:
        from datetime import datetime
        fmt_candidates = ["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"]
        end_dt = None
        for fmt in fmt_candidates:
            try:
                end_dt = datetime.strptime(end[:26].rstrip("Z") + "Z", fmt)
                break
            except ValueError:
                continue
        if end_dt is None:
            return 30.0

        if closed:
            close_dt = None
            for fmt in fmt_candidates:
                try:
                    close_dt = datetime.strptime(closed[:26].rstrip("Z") + "Z", fmt)
                    break
                except ValueError:
                    continue
            if close_dt:
                return max(0.0, (end_dt - close_dt).total_seconds() / 86400)

        return 30.0
    except Exception:
        return 30.0


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


# ── Public API ────────────────────────────────────────────────────────────


def build_category_map(rows: list[dict]) -> dict[str, int]:
    """Build a deterministic category → integer label map from training data."""
    cats = sorted({r.get("category", "") or "" for r in rows})
    return {c: i for i, c in enumerate(cats)}


def build_vocab(rows: list[dict], max_vocab: int = 200) -> list[str]:
    """Build a small question-text vocabulary from training data."""
    counter: Counter[str] = Counter()
    for r in rows:
        counter.update(_tokenize(r.get("question", "")))
    return [w for w, _ in counter.most_common(max_vocab)]


def extract_row(
    row: dict,
    category_map: dict[str, int] | None = None,
    vocab: list[str] | None = None,
) -> dict[str, float]:
    """Extract a feature dict from a single resolved_markets row.

    Returns plain floats suitable for numpy/sklearn consumption.
    """
    implied = _safe_float(
        row.get("implied_prob_at_close", row.get("implied_prob", 0.5)),
        0.5,
    )
    volume = _safe_float(row.get("volume"), 0.0)
    liquidity = _safe_float(row.get("liquidity"), 0.0)
    tags = _parse_json(row.get("tags"), [])
    tag_count = len(tags) if isinstance(tags, list) else 0
    days = _days_to_end(row)

    feats: dict[str, float] = {
        "implied_prob": implied,
        "log_volume": math.log1p(volume),
        "log_liquidity": math.log1p(liquidity),
        "days_to_end": days,
        "tag_count": float(tag_count),
    }

    cat = row.get("category", "") or ""
    if category_map is not None:
        feats["category_enc"] = float(category_map.get(cat, -1))
    else:
        feats["category_enc"] = 0.0

    if vocab:
        tokens = set(_tokenize(row.get("question", "")))
        for w in vocab:
            feats[f"bow_{w}"] = 1.0 if w in tokens else 0.0

    return feats


def extract_matrix(
    rows: list[dict],
    category_map: dict[str, int] | None = None,
    vocab: list[str] | None = None,
) -> tuple[np.ndarray, np.ndarray, list[str]]:
    """Extract feature matrix X and label vector y from a list of rows.

    Returns ``(X, y, feature_names)`` where X has shape ``(n, d)`` and y
    has shape ``(n,)`` with values in ``{0, 1}``.
    """
    if not rows:
        return np.empty((0, 0)), np.empty(0), []

    feat_dicts = [extract_row(r, category_map, vocab) for r in rows]
    names = list(feat_dicts[0].keys())

    X = np.array([[fd[n] for n in names] for fd in feat_dicts], dtype=np.float64)
    y = np.array([int(r.get("resolved_yes", 0)) for r in rows], dtype=np.float64)

    nan_mask = np.isnan(X)
    if nan_mask.any():
        X = np.nan_to_num(X, nan=0.0)

    return X, y, names
