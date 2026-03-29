"""Full repo cartography pipeline runner.

Runs all tools in dependency order:
  1.  census           — what exists
  2.  import_graph     — directed import graph (NetworkX + JSON + Mermaid + DOT)
  3.  boundary_matrix  — domain-level coupling table
  4.  entrypoint_map   — real execution origins
  5.  symbol_index     — symbol catalog
  6.  symbol_xref      — cross-references (requires symbol_index)
  7.  test_map         — coverage gaps
  8.  config_surface   — env vars + config file surface
  9.  cycle_detector   — circular imports
  10. dead_weight       — unreachable / stale files
  11. architecture_drift — boundary violations
"""
from __future__ import annotations

import argparse
import time
from pathlib import Path
from typing import Callable, Sequence

from ._paths import resolve_output_path, resolve_repo_root

Step = tuple[str, Callable[..., int]]


def _steps() -> list[Step]:
    from onto_market.devtools.repo_tools import (
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


def run(root: Path | None = None, reports_dir: Path | None = None) -> int:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    steps = _steps()
    total_start = time.monotonic()
    errors: list[str] = []

    print(f"\n{'='*60}")
    print("  Repo Cartography Pipeline")
    print(f"{'='*60}\n")

    # Build argv for tools that accept --root / --reports-dir
    extra: list[str] = []
    if root:
        extra += ["--root", str(repo_root)]
    if reports_dir:
        extra += ["--reports-dir", str(output_dir)]

    for name, fn in steps:
        print(f"--- {name} ---")
        step_start = time.monotonic()
        try:
            rc = fn(extra if extra else None)
            if rc and rc != 0:
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
    print(f"  Reports: {output_dir}/")
    print(f"{'='*60}\n")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the full repo cartography pipeline")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    args = parser.parse_args(argv)
    return run(args.root, args.reports_dir)


if __name__ == "__main__":
    raise SystemExit(main())
