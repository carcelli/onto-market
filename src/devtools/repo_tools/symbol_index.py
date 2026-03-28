"""Index all public symbols (classes, functions, dataclasses, enums) via AST.

Outputs:
  reports/symbol_index.json  — {symbol: {kind, module, file, line, bases}}
  reports/symbol_index.md    — sorted human-readable table
"""
from __future__ import annotations

import ast
import json
from dataclasses import dataclass
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, module_name


@dataclass
class Symbol:
    name: str
    kind: str          # "class" | "function" | "method" | "dataclass" | "enum"
    module: str
    file: str
    line: int
    bases: list[str] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.bases is None:
            self.bases = []


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


def extract_symbols(path: Path, root: Path = ROOT) -> list[Symbol]:
    mod = module_name(path, root)
    file_str = str(path.relative_to(root))
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError:
        return []

    symbols: list[Symbol] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            if node.name.startswith("_"):
                continue
            if _is_dataclass(node):
                kind = "dataclass"
            elif _is_enum(node):
                kind = "enum"
            else:
                kind = "class"
            symbols.append(
                Symbol(node.name, kind, mod, file_str, node.lineno, _base_names(node.bases))
            )
            # Methods inside the class
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if item.name.startswith("_") and item.name != "__init__":
                        continue
                    symbols.append(
                        Symbol(
                            f"{node.name}.{item.name}",
                            "method",
                            mod,
                            file_str,
                            item.lineno,
                        )
                    )

        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Top-level functions only (not methods — caught above)
            if node.name.startswith("_"):
                continue
            # Skip if parent is a ClassDef (already captured as method)
            symbols.append(Symbol(node.name, "function", mod, file_str, node.lineno))

    # De-duplicate methods already captured via class walk
    # (ast.walk visits both class body and top-level, so we may get dupes)
    seen: set[tuple[str, str, int]] = set()
    deduped: list[Symbol] = []
    for s in symbols:
        key = (s.module, s.name, s.line)
        if key not in seen:
            seen.add(key)
            deduped.append(s)

    return deduped


def run(root: Path = ROOT) -> list[Symbol]:
    all_symbols: list[Symbol] = []
    for path in find_python_files(root):
        all_symbols.extend(extract_symbols(path, root))
    return sorted(all_symbols, key=lambda s: (s.module, s.line))


def write_json(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:
    data = [
        {
            "name": s.name,
            "kind": s.kind,
            "module": s.module,
            "file": s.file,
            "line": s.line,
            "bases": s.bases,
        }
        for s in symbols
    ]
    path = out_dir / "symbol_index.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def write_md(symbols: list[Symbol], out_dir: Path = OUTPUT_DIR) -> Path:
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

    path = out_dir / "symbol_index.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    symbols = run()
    json_path = write_json(symbols)
    md_path = write_md(symbols)

    by_kind: dict[str, int] = {}
    for s in symbols:
        by_kind[s.kind] = by_kind.get(s.kind, 0) + 1
    for kind, count in sorted(by_kind.items()):
        print(f"  {kind}: {count}")
    print(f"Total symbols: {len(symbols)}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
