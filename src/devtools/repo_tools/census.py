"""Repo census: inventory of files, extensions, categories, and entrypoints."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, ROOT, SKIP_DIRS, should_skip

IMPORTANT_FILES: frozenset[str] = frozenset(
    {
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
)

CODE_EXTENSIONS: frozenset[str] = frozenset({".py", ".pyi"})
DOC_EXTENSIONS: frozenset[str] = frozenset({".md", ".rst", ".txt"})
DATA_EXTENSIONS: frozenset[str] = frozenset(
    {".json", ".jsonl", ".csv", ".parquet", ".yaml", ".yml", ".toml"}
)


def _category(path: Path) -> str:
    rel = path.relative_to(ROOT)
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
    if first == ".github":
        return "ci"
    if first == "src":
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


def run(root: Path = ROOT) -> dict:
    all_files: list[Path] = []
    top_level_dirs: set[str] = set()
    suffix_counts: Counter[str] = Counter()
    category_counts: Counter[str] = Counter()
    python_files: list[str] = []
    important_files: list[str] = []
    top_level_python: list[str] = []

    for path in root.rglob("*"):
        if should_skip(path):
            continue
        rel = path.relative_to(root)
        if path.is_dir():
            if len(rel.parts) == 1:
                top_level_dirs.add(rel.parts[0])
            continue

        all_files.append(path)
        cat = _category(path)
        category_counts[cat] += 1
        suffix_counts[path.suffix or "<no_ext>"] += 1

        if path.name in IMPORTANT_FILES:
            important_files.append(str(rel))
        if path.suffix in CODE_EXTENSIONS:
            python_files.append(str(rel))
            if len(rel.parts) == 1:
                top_level_python.append(str(rel))

    by_folder: dict[str, list[str]] = defaultdict(list)
    for p in python_files:
        first = Path(p).parts[0]
        by_folder[first].append(p)

    return {
        "repo_root": str(root),
        "top_level_dirs": sorted(top_level_dirs),
        "important_files": sorted(important_files),
        "top_level_python_files": sorted(top_level_python),
        "category_counts": dict(category_counts),
        "top_extensions": dict(suffix_counts.most_common(20)),
        "python_files_by_top_level": {
            k: sorted(v)[:200] for k, v in sorted(by_folder.items())
        },
        "total_files": len(all_files),
    }


def write_outputs(report: dict, out_dir: Path = OUTPUT_DIR) -> tuple[Path, Path]:
    out_dir.mkdir(exist_ok=True)
    json_path = out_dir / "repo_census.json"
    md_path = out_dir / "repo_census.md"

    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines: list[str] = [
        "# Repo Census\n",
        f"- Repo root: `{report['repo_root']}`",
        f"- Total files counted: **{report['total_files']}**\n",
        "## Top-level directories",
    ]
    for d in report["top_level_dirs"]:
        lines.append(f"- `{d}`")
    lines.append("")

    lines.append("## Important repo files")
    for f in report["important_files"]:
        lines.append(f"- `{f}`")
    lines.append("")

    lines.append("## Top-level Python files")
    for f in report["top_level_python_files"]:
        lines.append(f"- `{f}`")
    lines.append("")

    lines.append("## Category counts")
    for k, v in sorted(report["category_counts"].items()):
        lines.append(f"- `{k}`: {v}")
    lines.append("")

    lines.append("## Top file extensions")
    for k, v in report["top_extensions"].items():
        lines.append(f"- `{k}`: {v}")
    lines.append("")

    lines.append("## Python files by top-level area")
    for folder, files in report["python_files_by_top_level"].items():
        lines.append(f"### `{folder}`")
        for f in files:
            lines.append(f"- `{f}`")
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def main() -> int:
    report = run()
    json_path, md_path = write_outputs(report)
    print(f"Total files: {report['total_files']}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    main()
