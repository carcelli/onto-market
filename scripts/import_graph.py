#!/usr/bin/env python
"""Thin script wrapper for the repo import-graph tools.

Usage:
    python scripts/import_graph.py                  # import graph only
    python scripts/import_graph.py --boundary       # + boundary matrix
    python scripts/import_graph.py --cycles         # + cycle detector
    python scripts/import_graph.py --drift          # + architecture drift
    python scripts/import_graph.py --all            # all four tools

Delegates all logic to onto_market.devtools.repo_tools.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from onto_market.devtools.repo_tools import (  # noqa: E402
    import_graph,
    boundary_matrix,
    cycle_detector,
    architecture_drift,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="onto-market repo import-graph analysis suite"
    )
    parser.add_argument("--root", type=Path, default=None, help="Repository root")
    parser.add_argument(
        "--reports-dir", type=Path, default=None, help="Output directory"
    )
    parser.add_argument(
        "--boundary", action="store_true", help="Also run boundary matrix"
    )
    parser.add_argument(
        "--cycles", action="store_true", help="Also run cycle detector"
    )
    parser.add_argument(
        "--drift", action="store_true", help="Also run architecture drift audit"
    )
    parser.add_argument(
        "--all", dest="all_tools", action="store_true", help="Run all four tools"
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    kwargs = {"root": args.root, "reports_dir": args.reports_dir}

    import_graph.run(**kwargs)

    run_boundary = args.boundary or args.all_tools
    run_cycles = args.cycles or args.all_tools
    run_drift = args.drift or args.all_tools

    if run_boundary:
        boundary_matrix.run(**kwargs)
    if run_cycles:
        cycle_detector.run(**kwargs)
    if run_drift:
        architecture_drift.run(**kwargs)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
