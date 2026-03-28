from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from ._paths import resolve_repo_root


@dataclass(frozen=True)
class ImportGraphSnapshot:
    root: Path
    modules_scanned: int = 0
    edges: int = 0


def analyze(root: str | Path | None = None) -> ImportGraphSnapshot:
    return ImportGraphSnapshot(root=resolve_repo_root(root))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Scaffold for repo import graph analysis")
    parser.add_argument("--root", type=Path, default=None, help="Repository root to analyze")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    result = analyze(root=args.root)
    print(f"Import graph scaffold ready at {result.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
