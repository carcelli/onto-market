"""Full repo cartography pipeline runner.

Runs all tools in dependency order:
  1. census           — what exists
  2. import_graph     — what depends on what (builds reports/import_graph.json)
  3. boundary_matrix  — domain-level architecture flow (reads import_graph.json)
  4. entrypoint_map   — real execution origins
  5. symbol_index     — symbol catalog (builds reports/symbol_index.json)
  6. symbol_xref      — cross-references (reads symbol_index.json)
  7. test_map         — coverage gaps
  8. config_surface   — env vars + config file surface
  9. cycle_detector   — circular imports (reads import_graph.json)
  10. dead_weight      — unreachable / stale files (reads import_graph.json)
  11. architecture_drift — boundary violations (reads import_graph.json)
"""
from __future__ import annotations

import time
from pathlib import Path
from typing import Callable

from devtools.repo_tools._common import OUTPUT_DIR

Step = tuple[str, Callable[[], int]]


def _steps() -> list[Step]:
    # Import lazily so each module is independently runnable
    from devtools.repo_tools import (
        census,
        import_graph,
        boundary_matrix,
        entrypoint_map,
        symbol_index,
        symbol_xref,
        test_map,
        config_surface,
        cycle_detector,
        dead_weight,
        architecture_drift,
    )

    return [
        ("census", census.main),
        ("import_graph", import_graph.main),
        ("boundary_matrix", boundary_matrix.main),
        ("entrypoint_map", entrypoint_map.main),
        ("symbol_index", symbol_index.main),
        ("symbol_xref", symbol_xref.main),
        ("test_map", test_map.main),
        ("config_surface", config_surface.main),
        ("cycle_detector", cycle_detector.main),
        ("dead_weight", dead_weight.main),
        ("architecture_drift", architecture_drift.main),
    ]


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    steps = _steps()
    total_start = time.monotonic()
    errors: list[str] = []

    print(f"\n{'='*60}")
    print("  Repo Cartography Pipeline")
    print(f"{'='*60}\n")

    for name, fn in steps:
        print(f"--- {name} ---")
        step_start = time.monotonic()
        try:
            rc = fn()
            if rc != 0:
                errors.append(f"{name}: exited with code {rc}")
        except Exception as exc:
            errors.append(f"{name}: {exc}")
            print(f"  ERROR: {exc}")
        elapsed = time.monotonic() - step_start
        print(f"  done ({elapsed:.1f}s)\n")

    total = time.monotonic() - total_start
    print(f"{'='*60}")
    if errors:
        print(f"  {len(errors)} step(s) failed:")
        for e in errors:
            print(f"    - {e}")
        print(f"{'='*60}\n")
        return 1
    print(f"  All {len(steps)} steps completed in {total:.1f}s")
    print(f"  Reports: {OUTPUT_DIR}/")
    print(f"{'='*60}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
