"""Runtime ML prior inference for live market scoring."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from onto_market.ml_research.artifacts import get_latest
from onto_market.ml_research.features import extract_row
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)


def _clamp_probability(value: float) -> float:
    return max(0.01, min(0.99, float(value)))


def _clamp_weight(weight: float) -> float:
    clipped = max(0.0, min(1.0, float(weight)))
    if clipped != weight:
        logger.warning(
            "ml_research.inference: clamped ML_PRIOR_WEIGHT %.3f -> %.3f",
            weight,
            clipped,
        )
    return clipped


def _validate_metadata(metadata: dict[str, Any]) -> tuple[list[str], dict[str, int], list[str]] | None:
    feature_names = metadata.get("feature_names")
    category_map = metadata.get("category_map")
    vocab = metadata.get("vocab")

    if not isinstance(feature_names, list) or not all(isinstance(name, str) for name in feature_names):
        logger.warning("ml_research.inference: artifact metadata missing feature_names")
        return None
    if not isinstance(category_map, dict):
        logger.warning("ml_research.inference: artifact metadata missing category_map")
        return None
    if not isinstance(vocab, list) or not all(isinstance(token, str) for token in vocab):
        logger.warning("ml_research.inference: artifact metadata missing vocab")
        return None

    normalized_category_map: dict[str, int] = {}
    for key, value in category_map.items():
        if not isinstance(key, str):
            logger.warning("ml_research.inference: artifact category_map has non-string key")
            return None
        try:
            normalized_category_map[key] = int(value)
        except (TypeError, ValueError):
            logger.warning("ml_research.inference: artifact category_map has non-integer value")
            return None

    return feature_names, normalized_category_map, vocab


def predict_market_prior(
    market: dict,
    artifact_dir: str | Path = "data/ml_artifacts",
) -> float | None:
    """Return a model probability for the selected market, or None on fallback."""
    result = get_latest(artifact_dir)
    if result is None:
        return None

    model, metadata = result
    validated = _validate_metadata(metadata)
    if validated is None:
        return None

    feature_names, category_map, vocab = validated
    features = extract_row(market, category_map=category_map, vocab=vocab)

    missing = [name for name in feature_names if name not in features]
    if missing:
        logger.warning(
            "ml_research.inference: artifact requires missing features: %s",
            ", ".join(missing),
        )
        return None

    if not hasattr(model, "predict_proba"):
        logger.warning("ml_research.inference: artifact model lacks predict_proba")
        return None

    X = np.array([[features[name] for name in feature_names]], dtype=np.float64)
    probs = model.predict_proba(X)
    if getattr(probs, "ndim", 0) != 2 or probs.shape[1] < 2:
        logger.warning("ml_research.inference: predict_proba returned incompatible shape")
        return None

    return _clamp_probability(float(probs[:, 1][0]))


def blend_with_ml_prior(
    llm_prob: float,
    market: dict,
    artifact_dir: str | Path = "data/ml_artifacts",
    weight: float = 0.3,
) -> float:
    """Blend LLM probability with promoted ML artifact prediction."""
    model_prob = predict_market_prior(market, artifact_dir=artifact_dir)
    if model_prob is None:
        return _clamp_probability(llm_prob)

    clipped_weight = _clamp_weight(weight)
    blended = (1 - clipped_weight) * llm_prob + clipped_weight * model_prob
    logger.info(
        "ml_research.inference: blended llm=%.3f model=%.3f weight=%.1f%% -> %.3f",
        llm_prob,
        model_prob,
        clipped_weight * 100,
        blended,
    )
    return _clamp_probability(blended)
