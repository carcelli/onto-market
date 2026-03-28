from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from ._paths import resolve_repo_root


@dataclass(frozen=True)
class CycleSnapshot:
    root: Path
    cycles_found: int = 0


def analyze(root: str | Path | None = None) -> CycleSnapshot:
    return CycleSnapshot(root=resolve_repo_root(root))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scaffold for dependency cycle detection")
    parser.add_argument("--root", type=Path, default=None, help="Repository root to analyze")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = analyze(root=args.root)
    print(f"Cycle detector scaffold ready at {result.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
