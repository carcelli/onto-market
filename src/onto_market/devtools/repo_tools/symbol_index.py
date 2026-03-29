"""Index all public symbols (classes, functions, dataclasses, enums) via AST.

Outputs:
  reports/symbol_index.json  — [{name, kind, module, file, line, bases}]
  reports/symbol_index.md    — sorted human-readable table
"""
from __future__ import annotations

import argparse
import ast
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from ._common import find_python_files, module_name
from ._paths import resolve_output_path, resolve_repo_root


@dataclass
class Symbol:
    name: str
    kind: str
    module: str
    file: str
    line: int
    bases: list[str]


def _base_names(bases: list[ast.expr]) -> list[str]:
    names: list[str] = []
    for b in bases:
        if isinstance(b, ast.Name):
            names.append(b.id)
        elif isinstance(b, ast.Attribute):
            names.append(f"{getattr(b.value, 'id', '?')}.{b.attr}")
    return names


def _is_dataclass(node: ast.ClassDef) -> bool:
    for dec in node.decorator_list:
        if isinstance(dec, ast.Name) and dec.id == "dataclass":
            return True
        if isinstance(dec, ast.Attribute) and dec.attr == "dataclass":
            return True
    return False


def _is_enum(node: ast.ClassDef) -> bool:
    return any(b in {"Enum", "IntEnum", "StrEnum", "Flag", "IntFlag"} for b in _base_names(node.bases))


def _extract(path: Path, root: Path) -> list[Symbol]:
    mod = module_name(path, root)
    file_str = str(path.relative_to(root))
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError:
        return []

    symbols: list[Symbol] = []
    class_names: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            if node.name.startswith("_"):
                continue
            class_names.add(node.name)
            kind = "dataclass" if _is_dataclass(node) else ("enum" if _is_enum(node) else "class")
            symbols.append(Symbol(node.name, kind, mod, file_str, node.lineno, _base_names(node.bases)))
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if item.name.startswith("_") and item.name != "__init__":
                        continue
                    symbols.append(Symbol(f"{node.name}.{item.name}", "method", mod, file_str, item.lineno, []))

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("_"):
                continue
            # Skip class methods (already captured)
            symbols.append(Symbol(node.name, "function", mod, file_str, node.lineno, []))

    # Deduplicate
    seen: set[tuple[str, str, int]] = set()
    deduped: list[Symbol] = []
    for s in symbols:
        key = (s.module, s.name, s.line)
        if key not in seen:
            seen.add(key)
            deduped.append(s)

    return deduped


def run(root: Path | None = None) -> list[Symbol]:
    repo_root = resolve_repo_root(root)
    all_symbols: list[Symbol] = []
    for path in find_python_files(repo_root):
        all_symbols.extend(_extract(path, repo_root))
    return sorted(all_symbols, key=lambda s: (s.module, s.line))


def write_report(
    symbols: list[Symbol],
    root: Path | None = None,
    reports_dir: Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "symbol_index.json"
    md_path = output_dir / "symbol_index.md"

    data = [{"name": s.name, "kind": s.kind, "module": s.module, "file": s.file, "line": s.line, "bases": s.bases} for s in symbols]
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    lines = [
        "# Symbol Index",
        "",
        f"Total symbols: **{len(symbols)}**",
        "",
        "| Symbol | Kind | Module | Line |",
        "|--------|------|--------|-----:|",
    ]
    for s in symbols:
        bases = f" ({', '.join(s.bases)})" if s.bases and s.kind in {"class", "enum"} else ""
        lines.append(f"| `{s.name}{bases}` | {s.kind} | `{s.module}` | {s.line} |")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    return json_path, md_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Index all symbols in the repo")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    args = parser.parse_args(argv)

    symbols = run(args.root)
    json_path, md_path = write_report(symbols, args.root, args.reports_dir)

    by_kind: dict[str, int] = {}
    for s in symbols:
        by_kind[s.kind] = by_kind.get(s.kind, 0) + 1
    for kind, count in sorted(by_kind.items()):
        print(f"  {kind}: {count}")
    print(f"Total: {len(symbols)}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
