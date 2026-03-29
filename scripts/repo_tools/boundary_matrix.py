#!/usr/bin/env python3
"""Shim: delegates to onto_market.devtools.repo_tools.boundary_matrix."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from onto_market.devtools.repo_tools.boundary_matrix import main

if __name__ == "__main__":
    raise SystemExit(main())
