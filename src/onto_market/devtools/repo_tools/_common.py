"""Shared helpers for repo_tools modules.

Provides file discovery and AST parsing utilities, using _paths.py
for repo-root resolution so all tools work regardless of CWD.
"""
from __future__ import annotations

import ast
from pathlib import Path

from ._paths import resolve_repo_root

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

# src/ sub-roots that function as Python package namespaces
_SRC_ROOTS: frozenset[str] = frozenset({"src"})


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def find_python_files(root: Path | None = None) -> list[Path]:
    repo_root = resolve_repo_root(root)
    files: list[Path] = []
    for path in repo_root.rglob("*.py"):
        if should_skip(path):
            continue
        files.append(path)
    return sorted(files)


def module_name(path: Path, root: Path) -> str:
    """Convert a file path to a dotted Python module name.

    Strips a leading src/ component when present so that
    src/onto_market/agents/state.py → onto_market.agents.state
    (matching how Python's import system resolves it).
    """
    rel = path.relative_to(root)
    parts = list(rel.with_suffix("").parts)
    if parts and parts[-1] == "__init__":
        parts = parts[:-1]
    # Strip leading src/ if present — that's just the build layout root
    if parts and parts[0] in _SRC_ROOTS:
        parts = parts[1:]
    return ".".join(parts)


def parse_imports(path: Path) -> set[str]:
    """Return all module names referenced by import/from-import statements."""
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
