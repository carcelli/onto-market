#!/usr/bin/env python3
"""Fail-fast guard: ensure no stale duplicate package trees exist.

Wire into CI or ``make dryrun`` to catch layout regressions early.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN = [
    ROOT / "build",
    ROOT / "agents",
    ROOT / "config",
    ROOT / "core",
    ROOT / "ontology",
    ROOT / "src" / "devtools",
]

errors: list[str] = []
for p in FORBIDDEN:
    if p.exists():
        errors.append(f"  FAIL: stale path exists → {p.relative_to(ROOT)}/")

if errors:
    print("Repo topology check FAILED:")
    print("\n".join(errors))
    print("\nThe canonical package lives at src/onto_market/.")
    print("Delete these paths and re-run.")
    sys.exit(1)

print("Repo topology check passed.")
