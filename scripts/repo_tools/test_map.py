#!/usr/bin/env python3
"""Shim: delegates to src/devtools/repo_tools/test_map.py."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from devtools.repo_tools.test_map import main

if __name__ == "__main__":
    raise SystemExit(main())
