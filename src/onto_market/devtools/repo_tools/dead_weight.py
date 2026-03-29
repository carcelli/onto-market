"""Flag files that are likely dead weight.

Uses the NetworkX import graph from import_graph.build_graph().

Flags:
  - zero_inbound   — module with no inbound imports (excluding known entrypoints)
  - versioned_copy — filename matches *_v[0-9]*, *_old*, *_backup*, etc.
  - empty_module   — file has no classes, functions, or assignments

Outputs:
  reports/dead_weight.json  — [{module, file, flags}]
  reports/dead_weight.md    — grouped table
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from ._common import find_python_files, module_name
from ._paths import resolve_output_path, resolve_repo_root
from .import_graph import build_graph

VERSIONED_RE = re.compile(r"_v\d+|_old|_backup|_bak|_copy|_tmp|_temp", re.IGNORECASE)

EXPECTED_NO_INBOUND_STEMS: frozenset[str] = frozenset({"main", "conftest", "setup", "__main__"})
EXPECTED_NO_INBOUND_PREFIXES: tuple[str, ...] = (
    "onto_market.devtools.",
    "devtools.",
    "scripts.",
    "tests.",
)


@dataclass
class DeadFile:
    module: str
    file: str
    flags: list[str] = field(default_factory=list)


def _is_versioned(path: Path) -> bool:
    return bool(VERSIONED_RE.search(path.stem))


def _is_effectively_empty(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace").strip()
    except OSError:
        return False
    if not text:
        return True
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return False
    non_trivial = [
        n for n in ast.walk(tree)
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Assign, ast.AugAssign))
    ]
    return len(non_trivial) == 0


def _is_expected_no_inbound(mod: str) -> bool:
    leaf = mod.split(".")[-1]
    if leaf in EXPECTED_NO_INBOUND_STEMS:
        return True
    return any(mod.startswith(p) for p in EXPECTED_NO_INBOUND_PREFIXES)


def run(root: Path | None = None) -> list[DeadFile]:
    repo_root = resolve_repo_root(root)
    g = build_graph(repo_root)
    inbound: dict[str, int] = {n: 0 for n in g.nodes()}
    for src, dst in g.edges():
        inbound[dst] = inbound.get(dst, 0) + 1

    dead: list[DeadFile] = []
    for path in find_python_files(repo_root):
        mod = module_name(path, repo_root)
        file_str = str(path.relative_to(repo_root))
        flags: list[str] = []

        count = inbound.get(mod, 0)
        if count == 0 and not _is_expected_no_inbound(mod):
            flags.append("zero_inbound")
        if _is_versioned(path):
            flags.append("versioned_copy")
        if _is_effectively_empty(path):
            flags.append("empty_module")

        if flags:
            dead.append(DeadFile(mod, file_str, flags))

    return sorted(dead, key=lambda d: (d.flags[0], d.file))


def write_report(
    dead: list[DeadFile],
    root: Path | None = None,
    reports_dir: Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "dead_weight.json"
    md_path = output_dir / "dead_weight.md"

    json_path.write_text(
        json.dumps([{"module": d.module, "file": d.file, "flags": d.flags} for d in dead], indent=2),
        encoding="utf-8",
    )

    by_flag: dict[str, list[DeadFile]] = {}
    for d in dead:
        for f in d.flags:
            by_flag.setdefault(f, []).append(d)

    lines = [
        "# Dead Weight Report",
        "",
        f"Flagged files: **{len(dead)}**",
        "",
        "> `zero_inbound` = nothing imports this module (may be a legitimate entrypoint)",
        "> `versioned_copy` = filename contains `_v2`, `_old`, `_backup`, etc.",
        "> `empty_module` = no classes, functions, or assignments",
        "",
    ]

    for flag, label in [
        ("zero_inbound", "Zero Inbound Imports"),
        ("versioned_copy", "Versioned Copies"),
        ("empty_module", "Empty Modules"),
    ]:
        items = by_flag.get(flag, [])
        lines.append(f"## {label} ({len(items)})")
        lines.append("")
        if items:
            lines += ["| File | Module | All Flags |", "|------|--------|-----------|"]
            for d in items:
                lines.append(f"| `{d.file}` | `{d.module}` | {', '.join(d.flags)} |")
        else:
            lines.append("_None._")
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Flag dead weight files")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    args = parser.parse_args(argv)

    dead = run(args.root)
    json_path, md_path = write_report(dead, args.root, args.reports_dir)

    by_flag: dict[str, int] = {}
    for d in dead:
        for f in d.flags:
            by_flag[f] = by_flag.get(f, 0) + 1
    for flag, count in sorted(by_flag.items()):
        print(f"  {flag}: {count}")
    print(f"Total flagged: {len(dead)}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
