from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Sequence

from ._paths import resolve_output_path, resolve_repo_root

SKIP_DIRS = {
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
}

IMPORTANT_FILES = {
    "pyproject.toml",
    "requirements.txt",
    "requirements-dev.txt",
    "uv.lock",
    "poetry.lock",
    "Pipfile",
    "Pipfile.lock",
    "setup.py",
    "setup.cfg",
    "Makefile",
    "Dockerfile",
    "docker-compose.yml",
    ".gitignore",
    ".gitattributes",
    "README.md",
    "pyrightconfig.json",
    "mypy.ini",
    "ruff.toml",
    ".pre-commit-config.yaml",
    "langgraph.json",
}

CODE_EXTENSIONS = {".py", ".pyi"}
DOC_EXTENSIONS = {".md", ".rst", ".txt"}
DATA_EXTENSIONS = {".json", ".jsonl", ".csv", ".parquet", ".yaml", ".yml", ".toml"}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def top_level_category(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    parts = rel.parts
    if not parts:
        return "root"

    first = parts[0]

    if first in {"tests", "test"}:
        return "tests"
    if first in {"scripts", "bin"}:
        return "scripts"
    if first in {"docs", "documentation"}:
        return "docs"
    if first in {"data", "datasets", "artifacts", "models"}:
        return "data"
    if first in {".github"}:
        return "ci"
    if first in {"src"}:
        return "src"
    if path.name in IMPORTANT_FILES:
        return "repo_config"
    if path.suffix in CODE_EXTENSIONS:
        return "python_code"
    if path.suffix in DOC_EXTENSIONS:
        return "docs_misc"
    if path.suffix in DATA_EXTENSIONS:
        return "data_misc"
    return "other"


def build_report(root: str | Path | None = None) -> dict[str, object]:
    repo_root = resolve_repo_root(root)

    all_files: list[Path] = []
    top_level_dirs: set[str] = set()
    suffix_counts: Counter[str] = Counter()
    category_counts: Counter[str] = Counter()
    python_files: list[str] = []
    important_files: list[str] = []
    top_level_python: list[str] = []

    for path in repo_root.rglob("*"):
        if should_skip(path):
            continue

        rel = path.relative_to(repo_root)

        if path.is_dir():
            if len(rel.parts) == 1:
                top_level_dirs.add(rel.parts[0])
            continue

        all_files.append(path)
        category = top_level_category(path, repo_root)
        category_counts[category] += 1
        suffix_counts[path.suffix or "<no_ext>"] += 1

        if path.name in IMPORTANT_FILES:
            important_files.append(str(rel))

        if path.suffix in CODE_EXTENSIONS:
            python_files.append(str(rel))
            if len(rel.parts) == 1:
                top_level_python.append(str(rel))

    by_folder: dict[str, list[str]] = defaultdict(list)
    for path_str in python_files:
        first = Path(path_str).parts[0]
        by_folder[first].append(path_str)

    return {
        "repo_root": str(repo_root),
        "top_level_dirs": sorted(top_level_dirs),
        "important_files": sorted(important_files),
        "top_level_python_files": sorted(top_level_python),
        "category_counts": dict(category_counts),
        "top_extensions": dict(suffix_counts.most_common(20)),
        "python_files_by_top_level": {
            key: sorted(values)[:200] for key, values in sorted(by_folder.items())
        },
        "total_files": len(all_files),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines: list[str] = []
    lines.append("# Repo Census\n")
    lines.append(f"- Repo root: `{report['repo_root']}`")
    lines.append(f"- Total files counted: **{report['total_files']}**\n")

    lines.append("## Top-level directories")
    for directory in report["top_level_dirs"]:
        lines.append(f"- `{directory}`")
    lines.append("")

    lines.append("## Important repo files")
    for path in report["important_files"]:
        lines.append(f"- `{path}`")
    lines.append("")

    lines.append("## Top-level Python files")
    for path in report["top_level_python_files"]:
        lines.append(f"- `{path}`")
    lines.append("")

    lines.append("## Category counts")
    for key, value in sorted(report["category_counts"].items()):
        lines.append(f"- `{key}`: {value}")
    lines.append("")

    lines.append("## Top file extensions")
    for key, value in report["top_extensions"].items():
        lines.append(f"- `{key}`: {value}")
    lines.append("")

    lines.append("## Python files by top-level area")
    for folder, files in report["python_files_by_top_level"].items():
        lines.append(f"### `{folder}`")
        for path in files:
            lines.append(f"- `{path}`")
        lines.append("")

    return "\n".join(lines)


def write_report(
    report: dict[str, object],
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "repo_census.json"
    md_path = output_dir / "repo_census.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(render_markdown(report), encoding="utf-8")

    return json_path, md_path


def run(
    root: str | Path | None = None,
    reports_dir: str | Path | None = None,
) -> tuple[Path, Path]:
    report = build_report(root=root)
    return write_report(report=report, root=root, reports_dir=reports_dir)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a repo census report")
    parser.add_argument("--root", type=Path, default=None, help="Repository root to analyze")
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=None,
        help="Output directory for repo_census.json and repo_census.md",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    json_path, md_path = run(root=args.root, reports_dir=args.reports_dir)
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
