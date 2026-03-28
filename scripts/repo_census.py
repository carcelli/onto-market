#!/usr/bin/env python3
"""Shim: delegates to src/devtools/repo_tools/census.py."""
from __future__ import annotations

from _bootstrap import run

if __name__ == "__main__":
    raise SystemExit(run("devtools.repo_tools.census"))
