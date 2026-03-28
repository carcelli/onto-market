"""Shared constants and utilities for all repo_tools modules."""
from __future__ import annotations

import ast
from pathlib import Path
from typing import Iterable

ROOT = Path(".").resolve()

OUTPUT_DIR = ROOT / "reports"

SKIP_DIRS: frozenset[str] = frozenset(
    {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        "node_modules",
        "dist",
        "build",
        ".idea",
        ".vscode",
        "onto_market.egg-info",
    }
)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def find_python_files(root: Path = ROOT) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.py"):
        if should_skip(path):
            continue
        files.append(path)
    return sorted(files)


def module_name(path: Path, root: Path = ROOT) -> str:
    """Convert a file path to a dotted module name relative to root."""
    rel = path.relative_to(root)
    no_suffix = rel.with_suffix("")
    parts = list(no_suffix.parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def parse_imports(path: Path) -> set[str]:
    """Return all imported module names (top-level and from-imports) in a file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError as exc:
        print(f"  [warn] SyntaxError in {path}: {exc}")
        return set()

    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module)
    return imports


def is_internal(module: str, known_modules: set[str]) -> bool:
    if module in known_modules:
        return True
    return any(
        known == module
        or known.startswith(module + ".")
        or module.startswith(known + ".")
        for known in known_modules
    )


def normalize_internal_target(module: str, known_modules: set[str]) -> str:
    if module in known_modules:
        return module
    prefix_matches = [k for k in known_modules if k.startswith(module + ".")]
    if prefix_matches:
        return sorted(prefix_matches, key=len)[0]
    suffix_matches = [k for k in known_modules if module.startswith(k + ".")]
    if suffix_matches:
        return sorted(suffix_matches, key=len, reverse=True)[0]
    return module


def load_import_graph_json(reports_dir: Path = OUTPUT_DIR) -> dict:
    """Load the pre-built import graph from reports/import_graph.json."""
    path = reports_dir / "import_graph.json"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run import_graph first:\n"
            "  python -m devtools.repo_tools.import_graph"
        )
    import json
    return json.loads(path.read_text(encoding="utf-8"))
