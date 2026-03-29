"""Model versioning — store, promote, and retrieve trained artifacts.

Layout under ``data/ml_artifacts/``:

    model_v001.pkl          — pickled sklearn model
    metadata_v001.json      — brier, log_loss, feature_names, timestamp, …
    registry.json           — {"latest": 1, "promoted": 1, "versions": [...]}
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import joblib

from onto_market.utils.logger import get_logger

logger = get_logger(__name__)

_DEFAULT_DIR = Path("data/ml_artifacts")


def _ensure_dir(d: Path) -> Path:
    d.mkdir(parents=True, exist_ok=True)
    return d


def _registry_path(base: Path) -> Path:
    return base / "registry.json"


def _load_registry(base: Path) -> dict:
    rp = _registry_path(base)
    if rp.exists():
        return json.loads(rp.read_text())
    return {"latest": 0, "promoted": 0, "versions": []}


def _save_registry(base: Path, reg: dict) -> None:
    _registry_path(base).write_text(json.dumps(reg, indent=2) + "\n")


def _version_tag(v: int) -> str:
    return f"v{v:03d}"


def _extract_model_metadata(model: Any) -> dict[str, Any]:
    metadata: dict[str, Any] = {}
    attr_map = {
        "feature_names": "_onto_market_feature_names",
        "category_map": "_onto_market_category_map",
        "vocab": "_onto_market_vocab",
    }
    for key, attr in attr_map.items():
        value = getattr(model, attr, None)
        if value is not None:
            metadata[key] = value

    metadata["model_class"] = model.__class__.__name__
    return metadata


# ── Public API ────────────────────────────────────────────────────────────


def save_artifact(
    model: Any,
    metadata: dict,
    artifact_dir: str | Path = _DEFAULT_DIR,
) -> int:
    """Persist a trained model and its metadata.  Returns the new version number."""
    base = _ensure_dir(Path(artifact_dir))
    reg = _load_registry(base)
    version = reg["latest"] + 1
    tag = _version_tag(version)

    model_path = base / f"model_{tag}.pkl"
    meta_path = base / f"metadata_{tag}.json"

    joblib.dump(model, model_path)
    metadata = {
        **_extract_model_metadata(model),
        **metadata,
        "version": version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "model_path": str(model_path),
    }
    meta_path.write_text(json.dumps(metadata, indent=2, default=str) + "\n")

    reg["latest"] = version
    reg["versions"].append(version)
    _save_registry(base, reg)

    logger.info("artifacts: saved %s (brier=%.6f)", tag, metadata.get("brier", -1))
    return version


def promote(version: int, artifact_dir: str | Path = _DEFAULT_DIR) -> None:
    """Mark a version as the promoted (live) artifact."""
    base = Path(artifact_dir)
    reg = _load_registry(base)
    if version not in reg["versions"]:
        raise ValueError(f"Version {version} not found in registry")
    reg["promoted"] = version
    _save_registry(base, reg)
    logger.info("artifacts: promoted %s", _version_tag(version))


def get_latest(artifact_dir: str | Path = _DEFAULT_DIR) -> tuple[Any, dict] | None:
    """Load the promoted model and its metadata.

    Falls back to the most recent version if nothing is explicitly promoted.
    Returns ``None`` if no artifacts exist.
    """
    base = Path(artifact_dir)
    reg = _load_registry(base)
    version = reg.get("promoted") or reg.get("latest", 0)
    if version == 0:
        return None

    tag = _version_tag(version)
    model_path = base / f"model_{tag}.pkl"
    meta_path = base / f"metadata_{tag}.json"

    if not model_path.exists():
        logger.warning("artifacts: model file missing for %s", tag)
        return None

    model = joblib.load(model_path)
    metadata = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    return model, metadata


def get_metadata(version: int, artifact_dir: str | Path = _DEFAULT_DIR) -> dict | None:
    """Read metadata for a specific version."""
    base = Path(artifact_dir)
    tag = _version_tag(version)
    meta_path = base / f"metadata_{tag}.json"
    if not meta_path.exists():
        return None
    return json.loads(meta_path.read_text())


def list_versions(artifact_dir: str | Path = _DEFAULT_DIR) -> dict:
    """Return the full registry."""
    return _load_registry(Path(artifact_dir))


def status(artifact_dir: str | Path = _DEFAULT_DIR) -> str:
    """Human-readable summary of the artifact registry."""
    base = Path(artifact_dir)
    reg = _load_registry(base)
    if not reg["versions"]:
        return "No artifacts yet."

    lines = [f"Artifacts: {len(reg['versions'])} versions"]
    lines.append(f"  Latest:   v{reg['latest']:03d}")
    lines.append(f"  Promoted: v{reg['promoted']:03d}" if reg["promoted"] else "  Promoted: (none)")

    promoted_v = reg.get("promoted") or reg.get("latest", 0)
    meta = get_metadata(promoted_v, base)
    if meta:
        lines.append(f"  Brier:    {meta.get('brier', '?')}")
        lines.append(f"  Trained:  {meta.get('timestamp', '?')}")

    return "\n".join(lines)
