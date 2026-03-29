"""Autonomous experiment loop — the autoresearch engine.

Cycle:
  1. Read ``program.md`` for research instructions
  2. Load current best Brier score from the artifact registry
  3. Ask the LLM to propose an edit to ``train.py``
  4. Apply the edit, run ``train.py``, parse ``brier: <float>`` from stdout
  5. If Brier improves → save artifact, update registry
  6. If Brier regresses → reject, restore ``train.py``
  7. Repeat
"""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from onto_market.ml_research.artifacts import (
    get_metadata,
    list_versions,
    promote,
    save_artifact,
)
from onto_market.utils.llm_client import LLMClient
from onto_market.utils.logger import get_logger

logger = get_logger(__name__)

_HERE = Path(__file__).resolve().parent
_TRAIN_PY = _HERE / "train.py"
_PROGRAM_MD = _HERE / "program.md"
_BRIER_RE = re.compile(r"^brier:\s*([\d.]+)", re.MULTILINE)


def _read_program() -> str:
    if _PROGRAM_MD.exists():
        return _PROGRAM_MD.read_text()
    return "Minimize Brier score on the validation set by editing train.py."


def _read_train() -> str:
    return _TRAIN_PY.read_text()


def _backup_train() -> str:
    """Copy current train.py to a tempfile, return the temp path."""
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".py", delete=False, prefix="train_backup_"
    )
    tmp.write(_read_train())
    tmp.close()
    return tmp.name


def _restore_train(backup_path: str) -> None:
    shutil.copy2(backup_path, _TRAIN_PY)


def _apply_edit(new_contents: str) -> None:
    _TRAIN_PY.write_text(new_contents)


def _run_train(db_path: str | None = None, timeout: int = 120) -> float | None:
    """Execute train.py in a subprocess and parse the Brier score."""
    cmd = [sys.executable, str(_TRAIN_PY)]
    if db_path:
        cmd.append(db_path)

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, cwd=str(_HERE.parents[2])
        )
    except subprocess.TimeoutExpired:
        logger.warning("runner: train.py timed out after %ds", timeout)
        return None

    stdout = result.stdout
    stderr = result.stderr

    if result.returncode != 0:
        logger.warning("runner: train.py exited %d\nstderr: %s", result.returncode, stderr[:500])
        return None

    match = _BRIER_RE.search(stdout)
    if not match:
        logger.warning("runner: could not parse brier from stdout:\n%s", stdout[:500])
        return None

    return float(match.group(1))


def _ask_llm_for_edit(
    llm: LLMClient,
    current_train: str,
    best_brier: float,
    program: str,
    history: list[dict],
) -> str:
    """Ask the LLM to propose a new version of train.py."""
    history_text = ""
    if history:
        recent = history[-5:]
        history_text = "\n\nRecent experiment history:\n" + "\n".join(
            f"  v{h['version']}: brier={h['brier']:.6f} {'✓ kept' if h['kept'] else '✗ rejected'}"
            for h in recent
        )

    messages = [
        llm.system(
            "You are an ML research assistant optimizing a Polymarket forecaster.\n"
            "You will receive the current train.py and must output a COMPLETE "
            "replacement version of the file.\n\n"
            "Rules:\n"
            "- You may change MODEL_PARAMS, USE_VOCAB, MAX_VOCAB, build_model(), "
            "and the training logic.\n"
            "- You must NOT change the function signatures of train() or the "
            "brier: <float> output contract.\n"
            "- You must NOT change imports from sibling modules.\n"
            "- Only use scikit-learn and numpy (no torch, no new deps).\n"
            "- Respond with ONLY the Python file contents, no markdown fences.\n\n"
            f"Research instructions:\n{program}"
        ),
        llm.user(
            f"Current best Brier score: {best_brier:.6f}\n"
            f"{history_text}\n\n"
            f"Current train.py:\n```python\n{current_train}\n```\n\n"
            "Propose an improved version. Output the complete file."
        ),
    ]

    response = llm.chat(messages, temperature=0.4)
    cleaned = llm.strip_think_tags(response)
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[-1].rsplit("```", 1)[0]
    return cleaned.strip()


def run_experiment_loop(
    max_iterations: int = 10,
    db_path: str | None = None,
    artifact_dir: str | Path = "data/ml_artifacts",
    llm: LLMClient | None = None,
) -> dict[str, Any]:
    """Run the autoresearch loop.

    Returns a summary dict with keys: iterations, improvements, best_brier,
    best_version, history.
    """
    if llm is None:
        llm = LLMClient()

    program = _read_program()
    artifact_dir_str = str(artifact_dir)
    history: list[dict] = []

    baseline_brier = _run_train(db_path)
    if baseline_brier is None:
        logger.error("runner: baseline training failed — aborting")
        return {"iterations": 0, "improvements": 0, "best_brier": None, "history": []}

    logger.info("runner: baseline brier = %.6f", baseline_brier)

    reg = list_versions(artifact_dir)
    best_brier = baseline_brier
    best_version = reg.get("promoted", 0) or reg.get("latest", 0)

    if best_version > 0:
        meta = get_metadata(best_version, artifact_dir)
        if meta and meta.get("brier", 1.0) < best_brier:
            best_brier = meta["brier"]

    improvements = 0

    for i in range(1, max_iterations + 1):
        logger.info("runner: === iteration %d/%d (best=%.6f) ===", i, max_iterations, best_brier)

        backup = _backup_train()
        current_train = _read_train()

        try:
            proposed = _ask_llm_for_edit(llm, current_train, best_brier, program, history)
        except Exception as exc:
            logger.warning("runner: LLM call failed: %s", exc)
            history.append({"iteration": i, "version": None, "brier": None, "kept": False, "error": str(exc)})
            continue

        if not proposed or "def train(" not in proposed or "brier:" not in proposed:
            logger.warning("runner: LLM output doesn't look like valid train.py, skipping")
            history.append({"iteration": i, "version": None, "brier": None, "kept": False, "error": "invalid_output"})
            continue

        _apply_edit(proposed)
        new_brier = _run_train(db_path)

        if new_brier is None:
            logger.warning("runner: proposed train.py crashed, reverting")
            _restore_train(backup)
            history.append({"iteration": i, "version": None, "brier": None, "kept": False, "error": "crash"})
            continue

        if new_brier < best_brier:
            logger.info("runner: ✓ improved %.6f → %.6f", best_brier, new_brier)

            import importlib
            import onto_market.ml_research.train as train_mod
            importlib.reload(train_mod)
            model, _ = train_mod.train(db_path)

            if model is not None:
                version = save_artifact(
                    model,
                    {"brier": new_brier, "iteration": i},
                    artifact_dir=artifact_dir_str,
                )
                promote(version, artifact_dir=artifact_dir_str)
                best_brier = new_brier
                best_version = version
                improvements += 1
                history.append({"iteration": i, "version": version, "brier": new_brier, "kept": True})
            else:
                _restore_train(backup)
                history.append({"iteration": i, "version": None, "brier": new_brier, "kept": False, "error": "no_model"})
        else:
            logger.info("runner: ✗ rejected %.6f ≥ %.6f", new_brier, best_brier)
            _restore_train(backup)
            history.append({"iteration": i, "version": None, "brier": new_brier, "kept": False})

        Path(backup).unlink(missing_ok=True)

    return {
        "iterations": max_iterations,
        "improvements": improvements,
        "best_brier": best_brier,
        "best_version": best_version,
        "history": history,
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run autoresearch experiment loop")
    parser.add_argument("--iterations", type=int, default=10)
    parser.add_argument("--db-path", type=str, default=None)
    parser.add_argument("--artifact-dir", type=str, default="data/ml_artifacts")
    args = parser.parse_args()

    result = run_experiment_loop(
        max_iterations=args.iterations,
        db_path=args.db_path,
        artifact_dir=args.artifact_dir,
    )
    print("\n=== Autoresearch Complete ===")
    print(f"  Iterations:   {result['iterations']}")
    print(f"  Improvements: {result['improvements']}")
    print(f"  Best Brier:   {result['best_brier']}")
    print(f"  Best Version: v{result.get('best_version', 0):03d}")
