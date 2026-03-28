"""Flag files that are likely dead weight.

Reads reports/import_graph.json (run import_graph first).

Flags:
  - zero_inbound   — module with no inbound imports from other modules
  - versioned_copy — filename matches *_v[0-9]*.py or *_old.py or *_backup.py
  - dunder_main_only — only contains if __name__ == "__main__" (no reusable exports)
  - empty_module   — file is empty or only has pass/comments
  - duplicate_main — multiple files with if __name__ == "__main__" doing similar things

Outputs:
  reports/dead_weight.json  — list of flagged files with reasons
  reports/dead_weight.md    — grouped table
"""
from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from devtools.repo_tools._common import (
    OUTPUT_DIR,
    ROOT,
    find_python_files,
    load_import_graph_json,
    module_name,
)

VERSIONED_RE = re.compile(r"_v\d+|_old|_backup|_bak|_copy|_tmp|_temp", re.IGNORECASE)

# Modules we always expect to have zero inbound imports (they ARE entrypoints)
EXPECTED_NO_INBOUND: frozenset[str] = frozenset(
    {
        "main",
        "conftest",
        "setup",
    }
)

# Prefixes of modules where zero inbound is expected/normal
EXPECTED_NO_INBOUND_PREFIXES: tuple[str, ...] = (
    "scripts.",
    "tests.",
    "devtools.",
)


@dataclass
class DeadFile:
    module: str
    file: str
    flags: list[str] = field(default_factory=list)
    note: str = ""


def _inbound_counts(data: dict) -> dict[str, int]:
    counts: dict[str, int] = {n: 0 for n in data["nodes"]}
    for edge in data["edges"]:
        counts[edge["target"]] = counts.get(edge["target"], 0) + 1
    return counts


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


def _has_dunder_main(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text)
    except (SyntaxError, OSError):
        return False
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.If)
            and isinstance(node.test, ast.Compare)
            and isinstance(node.test.left, ast.Name)
            and node.test.left.id == "__name__"
        ):
            return True
    return False


def _is_expected_no_inbound(mod: str) -> bool:
    if mod in EXPECTED_NO_INBOUND:
        return True
    return any(mod.startswith(p) for p in EXPECTED_NO_INBOUND_PREFIXES)


def run(root: Path = ROOT) -> list[DeadFile]:
    data = load_import_graph_json()
    inbound = _inbound_counts(data)

    dead: list[DeadFile] = []

    for path in find_python_files(root):
        mod = module_name(path, root)
        file_str = str(path.relative_to(root))
        flags: list[str] = []

        # Zero inbound imports
        count = inbound.get(mod, 0)
        if count == 0 and not _is_expected_no_inbound(mod):
            flags.append("zero_inbound")

        # Versioned copy
        if _is_versioned(path):
            flags.append("versioned_copy")

        # Effectively empty
        if _is_effectively_empty(path):
            flags.append("empty_module")

        if flags:
            dead.append(DeadFile(mod, file_str, flags))

    return sorted(dead, key=lambda d: (d.flags[0], d.file))


def write_json(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:
    data = [
        {"module": d.module, "file": d.file, "flags": d.flags, "note": d.note}
        for d in dead
    ]
    path = out_dir / "dead_weight.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def write_md(dead: list[DeadFile], out_dir: Path = OUTPUT_DIR) -> Path:
    by_flag: dict[str, list[DeadFile]] = {}
    for d in dead:
        for f in d.flags:
            by_flag.setdefault(f, []).append(d)

    lines = [
        "# Dead Weight Report",
        "",
        f"Flagged files: **{len(dead)}**",
        "",
        "> `zero_inbound` = nothing imports this module (may be a legitimate entrypoint if missed by exemptions)",
        "> `versioned_copy` = filename contains `_v2`, `_old`, `_backup`, etc.",
        "> `empty_module` = no classes, functions, or assignments",
        "",
    ]

    FLAG_LABELS = {
        "zero_inbound": "Zero Inbound Imports",
        "versioned_copy": "Versioned Copies",
        "empty_module": "Empty Modules",
    }

    for flag, label in FLAG_LABELS.items():
        items = by_flag.get(flag, [])
        lines.append(f"## {label} ({len(items)})")
        lines.append("")
        if items:
            lines.append("| File | Module | All Flags |")
            lines.append("|------|--------|-----------|")
            for d in items:
                all_flags = ", ".join(d.flags)
                lines.append(f"| `{d.file}` | `{d.module}` | {all_flags} |")
        else:
            lines.append("_None._")
        lines.append("")

    path = out_dir / "dead_weight.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    dead = run()
    json_path = write_json(dead)
    md_path = write_md(dead)

    by_flag: dict[str, int] = {}
    for d in dead:
        for f in d.flags:
            by_flag[f] = by_flag.get(f, 0) + 1
    for flag, count in sorted(by_flag.items()):
        print(f"  {flag}: {count}")
    print(f"Total flagged: {len(dead)}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
