"""Autonomous experiment loop — the autoresearch engine.

Supports two modes:
  - ``sklearn`` (default): edits ``train.py``, 120 s timeout, sklearn only.
  - ``torch``:  edits ``torch_train.py``, 300 s timeout, PyTorch allowed.

Supports split GPU/CPU operation: the **researcher LLM** (which proposes
edits) can run on CPU/RAM via a local Ollama model (e.g. gpt-oss:20b)
while the **training subprocess** keeps the GPU free for PyTorch.

Cycle:
  1. Read ``program.md`` for research instructions
  2. Load current best Brier score from the artifact registry
  3. Ask the researcher LLM to propose an edit to the target training file
  4. Apply the edit, run it, parse ``brier: <float>`` from stdout
  5. If Brier improves and passes promotion gates → save artifact, update registry
  6. If Brier regresses or gates fail → reject, restore the file
  7. Repeat
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Literal

from onto_market.ml_research.artifacts import (
    get_metadata,
    list_versions,
    promote,
    save_artifact,
)
from onto_market.utils.llm_client import LLMClient
from onto_market.utils.logger import get_logger

# Lazy import to avoid circular deps — ontology enrichment is optional
_enricher = None


def _get_enricher():
    global _enricher
    if _enricher is None:
        try:
            from onto_market.ontology import enricher as _mod
            _enricher = _mod
        except Exception:
            pass
    return _enricher

logger = get_logger(__name__)

_HERE = Path(__file__).resolve().parent
_TRAIN_PY = _HERE / "train.py"
_TORCH_TRAIN_PY = _HERE / "torch_train.py"
_PROGRAM_MD = _HERE / "program.md"
_BRIER_RE = re.compile(r"^brier:\s*([\d.]+)", re.MULTILINE)
_OOM_PATTERNS = ("CUDA out of memory", "OutOfMemoryError", "CUDA error")

TrainingMode = Literal["sklearn", "torch"]

_DEFAULT_TIMEOUTS: dict[TrainingMode, int] = {
    "sklearn": 300,  # train.py is now torch-based
    "torch": 300,
}


def _target_file(mode: TrainingMode) -> Path:
    return _TORCH_TRAIN_PY if mode == "torch" else _TRAIN_PY


def _read_program() -> str:
    if _PROGRAM_MD.exists():
        return _PROGRAM_MD.read_text()
    return "Minimize Brier score on the validation set by editing train.py."


def _read_train(mode: TrainingMode) -> str:
    return _target_file(mode).read_text()


def _backup_train(mode: TrainingMode) -> str:
    """Copy current train file to a tempfile, return the temp path."""
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, prefix="train_backup_"
    )
    tmp.write(_read_train(mode))
    tmp.close()
    return tmp.name


def _restore_train(backup_path: str, mode: TrainingMode) -> None:
    shutil.copy2(backup_path, _target_file(mode))


def _apply_edit(new_contents: str, mode: TrainingMode) -> None:
    _target_file(mode).write_text(new_contents)


def _is_oom(stderr: str) -> bool:
    return any(pat in stderr for pat in _OOM_PATTERNS)


def _run_train(
    mode: TrainingMode,
    db_path: str | None = None,
    timeout: int | None = None,
) -> tuple[float | None, dict[str, Any]]:
    """Execute the training file and parse metrics from stdout.

    Returns ``(brier_or_none, extra_metrics_dict)``.
    """
    target = _target_file(mode)
    if timeout is None:
        timeout = _DEFAULT_TIMEOUTS[mode]

    cmd = [sys.executable, str(target)]
    if db_path:
        cmd.append(db_path)

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(_HERE.parents[2]),
        )
    except subprocess.TimeoutExpired:
        logger.warning("runner: %s timed out after %ds", target.name, timeout)
        return None, {"error": "timeout"}

    stdout = result.stdout
    stderr = result.stderr

    if result.returncode != 0:
        if _is_oom(stderr):
            logger.warning("runner: OOM detected in %s", target.name)
            return None, {"error": "oom"}
        logger.warning(
            "runner: %s exited %d\nstderr: %s",
            target.name,
            result.returncode,
            stderr[:500],
        )
        return None, {"error": "crash"}

    match = _BRIER_RE.search(stdout)
    if not match:
        logger.warning(
            "runner: could not parse brier from %s stdout:\n%s",
            target.name,
            stdout[:500],
        )
        return None, {"error": "no_brier"}

    extras: dict[str, Any] = {}
    for key in ("training_seconds", "peak_vram_mb"):
        m = re.search(rf"^{key}:\s*([\d.]+)", stdout, re.MULTILINE)
        if m:
            extras[key] = float(m.group(1))

    return float(match.group(1)), extras


# ── LLM prompts ──────────────────────────────────────────────────────────

_SKLEARN_SYSTEM = (
    "You are an ML research assistant optimizing a PyTorch Polymarket forecaster.\n"
    "You will receive the current train.py and must output a COMPLETE "
    "replacement version of the file.\n\n"
    "Rules:\n"
    "- You may change the CONFIG block (DEPTH, HIDDEN, DROPOUT, LR, "
    "WEIGHT_DECAY, BATCH_SIZE, MAX_EPOCHS, TIME_BUDGET, USE_VOCAB, MAX_VOCAB).\n"
    "- You may change the TinyForecaster class architecture.\n"
    "- You may add learning-rate schedulers, gradient clipping, early stopping.\n"
    "- You must NOT change the function signature of train() or the "
    "brier:/training_seconds:/peak_vram_mb: output contracts.\n"
    "- You must NOT change imports from sibling modules.\n"
    "- Only use torch, numpy, and sklearn (no new deps).\n"
    "- Keep the model small: HIDDEN <= 128, DEPTH <= 4, BATCH_SIZE <= 512 "
    "(RTX 3050, 8 GB VRAM).\n"
    "- Respond with ONLY the Python file contents, no markdown fences."
)

_TORCH_SYSTEM = (
    "You are an ML research assistant optimizing a PyTorch Polymarket forecaster.\n"
    "You will receive the current torch_train.py and must output a COMPLETE "
    "replacement version of the file.\n\n"
    "Rules:\n"
    "- You may change MODEL_PARAMS, LR, WEIGHT_DECAY, BATCH_SIZE, MAX_EPOCHS, "
    "TIME_BUDGET, USE_VOCAB, MAX_VOCAB, build_model(), and the training logic.\n"
    "- You may swap TinyForecaster for TinyTransformerForecaster from models.py.\n"
    "- You may add learning-rate schedulers, gradient clipping, early stopping.\n"
    "- You must NOT change the function signature of train() or the "
    "brier:/training_seconds:/peak_vram_mb: output contracts.\n"
    "- You must NOT change imports from sibling modules.\n"
    "- Only use torch, numpy, and sklearn (no new deps).\n"
    "- Keep the model small: hidden <= 128, depth <= 4, batch <= 512 "
    "(RTX 3050, 4-6 GB VRAM).\n"
    "- Respond with ONLY the Python file contents, no markdown fences."
)


def _ask_llm_for_edit(
    llm: LLMClient,
    current_train: str,
    best_brier: float,
    program: str,
    history: list[dict],
    mode: TrainingMode,
) -> str:
    """Ask the LLM to propose a new version of the training file."""
    history_text = ""
    if history:
        recent = history[-5:]
        lines: list[str] = []
        for h in recent:
            brier_s = f"{h['brier']:.6f}" if h.get("brier") is not None else "N/A"
            tag = "kept" if h.get("kept") else "rejected"
            err = f" ({h['error']})" if h.get("error") else ""
            lines.append(f"  v{h.get('version', '?')}: brier={brier_s} {tag}{err}")
        history_text = "\n\nRecent experiment history:\n" + "\n".join(lines)

    system_text = _TORCH_SYSTEM if mode == "torch" else _SKLEARN_SYSTEM
    file_label = "torch_train.py" if mode == "torch" else "train.py"

    messages = [
        llm.system(f"{system_text}\n\nResearch instructions:\n{program}"),
        llm.user(
            f"Current best Brier score: {best_brier:.6f}\n"
            f"{history_text}\n\n"
            f"Current {file_label}:\n```python\n{current_train}\n```\n\n"
            "Propose an improved version. Output the complete file."
        ),
    ]

    response = llm.chat(messages, temperature=0.4)
    cleaned = llm.strip_think_tags(response)
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[-1].rsplit("```", 1)[0]
    return cleaned.strip()


# ── Main loop ────────────────────────────────────────────────────────────


def _resolve_researcher(
    llm: LLMClient | None,
    researcher: str | None,
) -> LLMClient:
    """Build the researcher LLM client.

    Priority:
      1. Explicit ``llm`` object passed by caller.
      2. ``researcher`` spec string — ``"local"`` or ``"local/<model>"``.
      3. Default ``LLMClient()`` (uses global LLM_PROVIDER).
    """
    if llm is not None:
        return llm
    if researcher:
        parts = researcher.split("/", 1)
        provider = parts[0]
        model = parts[1] if len(parts) > 1 else None
        if provider == "local":
            return LLMClient.local(model=model)
        return LLMClient(model=researcher)
    return LLMClient()


def run_experiment_loop(
    max_iterations: int = 10,
    db_path: str | None = None,
    artifact_dir: str | Path = "data/ml_artifacts",
    llm: LLMClient | None = None,
    mode: TrainingMode = "sklearn",
    timeout: int | None = None,
    researcher: str | None = None,
) -> dict[str, Any]:
    """Run the autoresearch loop.

    Parameters
    ----------
    researcher : str, optional
        Researcher LLM spec.  ``"local"`` uses the default Ollama model
        on CPU/RAM (keeps GPU free for training).  ``"local/qwen2:7b"``
        uses a specific Ollama model.  ``None`` falls back to global
        ``LLM_PROVIDER``.

    Returns a summary dict with keys: iterations, improvements, best_brier,
    best_version, mode, history.
    """
    llm = _resolve_researcher(llm, researcher)
    researcher_label = researcher or "default"
    logger.info("runner [%s]: researcher LLM = %s", mode, researcher_label)

    effective_timeout = timeout or _DEFAULT_TIMEOUTS[mode]
    program = _read_program()
    artifact_dir_str = str(artifact_dir)
    history: list[dict] = []

    baseline_brier, baseline_extras = _run_train(mode, db_path, effective_timeout)
    if baseline_brier is None:
        logger.error("runner: baseline training failed — aborting (%s)", baseline_extras)
        return {"iterations": 0, "improvements": 0, "best_brier": None, "mode": mode, "history": []}

    logger.info("runner [%s]: baseline brier = %.6f", mode, baseline_brier)

    reg = list_versions(artifact_dir)
    best_brier = baseline_brier
    best_version = reg.get("promoted", 0) or reg.get("latest", 0)

    if best_version > 0:
        meta = get_metadata(best_version, artifact_dir)
        if meta and meta.get("brier", 1.0) < best_brier:
            best_brier = meta["brier"]

    improvements = 0

    for i in range(1, max_iterations + 1):
        logger.info(
            "runner [%s]: === iteration %d/%d (best=%.6f) ===",
            mode, i, max_iterations, best_brier,
        )

        backup = _backup_train(mode)
        current_train = _read_train(mode)

        try:
            proposed = _ask_llm_for_edit(
                llm, current_train, best_brier, program, history, mode
            )
        except Exception as exc:
            logger.warning("runner: LLM call failed: %s", exc)
            history.append({
                "iteration": i, "version": None, "brier": None,
                "kept": False, "error": str(exc),
            })
            continue

        if not proposed or "def train(" not in proposed or "brier:" not in proposed:
            logger.warning("runner: LLM output doesn't look like valid train file, skipping")
            history.append({
                "iteration": i, "version": None, "brier": None,
                "kept": False, "error": "invalid_output",
            })
            continue

        _apply_edit(proposed, mode)
        new_brier, extras = _run_train(mode, db_path, effective_timeout)

        if new_brier is None:
            error_type = extras.get("error", "crash")
            logger.warning("runner: proposed file failed (%s), reverting", error_type)
            _restore_train(backup, mode)
            history.append({
                "iteration": i, "version": None, "brier": None,
                "kept": False, "error": error_type,
            })
            continue

        if new_brier < best_brier:
            logger.info("runner: improved %.6f -> %.6f", best_brier, new_brier)

            model = _retrain_for_artifact(mode, db_path)

            if model is not None:
                meta_dict: dict[str, Any] = {
                    "brier": new_brier,
                    "iteration": i,
                    "model_type": mode,
                }
                meta_dict.update(extras)

                version = save_artifact(
                    model, meta_dict, artifact_dir=artifact_dir_str,
                )
                promote(version, artifact_dir=artifact_dir_str)
                best_brier = new_brier
                best_version = version
                improvements += 1
                history.append({
                    "iteration": i, "version": version, "brier": new_brier,
                    "kept": True, **extras,
                })

                # Feed ML feature importance into the ontology graph
                enricher = _get_enricher()
                if enricher is not None:
                    try:
                        full_meta = get_metadata(version, artifact_dir)
                        if full_meta:
                            full_meta["brier"] = new_brier
                            from onto_market.ontology.graph import OntologyGraph
                            onto = OntologyGraph()
                            ml_triples = enricher.from_ml_features(full_meta)
                            if ml_triples:
                                onto.add_triples(ml_triples, persist=True)
                                logger.info(
                                    "runner: fed %d ML triples into ontology "
                                    "(graph now %d nodes, %d edges)",
                                    len(ml_triples),
                                    onto.g.number_of_nodes(),
                                    onto.g.number_of_edges(),
                                )
                    except Exception as exc:
                        logger.debug("runner: ontology enrichment skipped: %s", exc)
            else:
                _restore_train(backup, mode)
                history.append({
                    "iteration": i, "version": None, "brier": new_brier,
                    "kept": False, "error": "no_model",
                })
        else:
            logger.info("runner: rejected %.6f >= %.6f", new_brier, best_brier)
            _restore_train(backup, mode)
            history.append({
                "iteration": i, "version": None, "brier": new_brier,
                "kept": False, **extras,
            })

        Path(backup).unlink(missing_ok=True)

    return {
        "iterations": max_iterations,
        "improvements": improvements,
        "best_brier": best_brier,
        "best_version": best_version,
        "mode": mode,
        "history": history,
    }


def _retrain_for_artifact(
    mode: TrainingMode,
    db_path: str | None,
) -> Any | None:
    """Re-run training in-process to get the model object for artifact storage."""
    import importlib

    if mode == "torch":
        import onto_market.ml_research.torch_train as train_mod
    else:
        import onto_market.ml_research.train as train_mod  # type: ignore[no-redef]

    importlib.reload(train_mod)
    model, _ = train_mod.train(db_path)
    return model


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run autoresearch experiment loop")
    parser.add_argument("--iterations", type=int, default=10)
    parser.add_argument("--db-path", type=str, default=None)
    parser.add_argument("--artifact-dir", type=str, default="data/ml_artifacts")
    parser.add_argument("--mode", type=str, choices=["sklearn", "torch"], default="sklearn")
    parser.add_argument("--timeout", type=int, default=None)
    parser.add_argument(
        "--researcher", type=str, default=None,
        help=(
            "Researcher LLM spec. 'local' = Ollama on CPU/RAM (keeps GPU "
            "free for training). 'local/qwen2:7b' = specific Ollama model. "
            "Omit to use global LLM_PROVIDER."
        ),
    )
    args = parser.parse_args()

    result = run_experiment_loop(
        max_iterations=args.iterations,
        db_path=args.db_path,
        artifact_dir=args.artifact_dir,
        mode=args.mode,
        timeout=args.timeout,
        researcher=args.researcher,
    )
    print("\n=== Autoresearch Complete ===")
    print(f"  Mode:         {result['mode']}")
    print(f"  Researcher:   {args.researcher or 'default'}")
    print(f"  Iterations:   {result['iterations']}")
    print(f"  Improvements: {result['improvements']}")
    print(f"  Best Brier:   {result['best_brier']}")
    print(f"  Best Version: v{result.get('best_version', 0):03d}")
