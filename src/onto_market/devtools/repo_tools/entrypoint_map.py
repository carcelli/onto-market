"""Discover real execution entrypoints in the repo via AST analysis.

Detects:
  - if __name__ == "__main__" blocks
  - Typer / Click app definitions
  - FastAPI / Starlette apps
  - LangGraph StateGraph definitions
  - Scheduled jobs (APScheduler, schedule lib)
  - pyproject.toml [project.scripts] entries

Outputs:
  reports/entrypoint_map.json  — machine-readable list
  reports/entrypoint_map.md    — human-readable table
"""
from __future__ import annotations

import argparse
import ast
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from ._common import find_python_files, module_name, should_skip
from ._paths import resolve_output_path, resolve_repo_root

TOML_SCRIPTS_RE = re.compile(r"^\s*(\S+)\s*=\s*\"([^\"]+)\"", re.MULTILINE)


@dataclass
class Entrypoint:
    kind: str
    module: str
    file: str
    line: int
    detail: str = ""


def _func_name(node: ast.Call) -> str:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        parts: list[str] = [func.attr]
        val = func.value
        while isinstance(val, ast.Attribute):
            parts.append(val.attr)
            val = val.value
        if isinstance(val, ast.Name):
            parts.append(val.id)
        return ".".join(reversed(parts))
    return ""


def _has_dunder_main(tree: ast.Module) -> int | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            test = node.test
            if (
                isinstance(test, ast.Compare)
                and isinstance(test.left, ast.Name)
                and test.left.id == "__name__"
                and len(test.ops) == 1
                and isinstance(test.ops[0], ast.Eq)
                and len(test.comparators) == 1
                and isinstance(test.comparators[0], ast.Constant)
                and test.comparators[0].value == "__main__"
            ):
                return node.lineno
    return None


def _detect_frameworks(tree: ast.Module, mod: str, file_str: str) -> list[Entrypoint]:
    found: list[Entrypoint] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            fname = _func_name(node.value)
            if fname in {"typer.Typer", "click.Group", "click.group"}:
                found.append(Entrypoint("typer/click", mod, file_str, node.lineno, fname))
            elif fname in {"FastAPI", "Starlette", "flask.Flask"}:
                found.append(Entrypoint("web-app", mod, file_str, node.lineno, fname))
            elif "StateGraph" in fname:
                found.append(Entrypoint("langgraph", mod, file_str, node.lineno, fname))
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            fname = _func_name(node.value)
            if isinstance(node.value.func, ast.Attribute):
                attr = node.value.func.attr
                if attr in {"add_node", "compile"}:
                    found.append(Entrypoint("langgraph", mod, file_str, node.lineno, f".{attr}()"))
                if attr in {"add_job", "start"} and "scheduler" in fname.lower():
                    found.append(Entrypoint("scheduler", mod, file_str, node.lineno, f".{attr}()"))
    return found


def _pyproject_scripts(root: Path) -> list[Entrypoint]:
    toml_path = root / "pyproject.toml"
    if not toml_path.exists():
        return []
    text = toml_path.read_text(encoding="utf-8")
    in_section = False
    entries: list[Entrypoint] = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.strip() == "[project.scripts]":
            in_section = True
            continue
        if in_section:
            if line.startswith("["):
                break
            m = TOML_SCRIPTS_RE.match(line)
            if m:
                cmd, target = m.group(1), m.group(2)
                entries.append(
                    Entrypoint("console-script", target.split(":")[0], "pyproject.toml", i, f"{cmd} = {target}")
                )
    return entries


def run(root: Path | None = None) -> list[Entrypoint]:
    repo_root = resolve_repo_root(root)
    results: list[Entrypoint] = []

    for path in find_python_files(repo_root):
        mod = module_name(path, repo_root)
        file_str = str(path.relative_to(repo_root))
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(text, filename=str(path))
        except SyntaxError:
            continue
        line = _has_dunder_main(tree)
        if line:
            results.append(Entrypoint("__main__", mod, file_str, line))
        results.extend(_detect_frameworks(tree, mod, file_str))

    results.extend(_pyproject_scripts(repo_root))

    seen: set[tuple[str, str, int]] = set()
    deduped: list[Entrypoint] = []
    for ep in results:
        key = (ep.kind, ep.module, ep.line)
        if key not in seen:
            seen.add(key)
            deduped.append(ep)

    return sorted(deduped, key=lambda e: (e.kind, e.file, e.line))


def write_report(
    entries: list[Entrypoint],
    root: Path | None = None,
    reports_dir: Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "entrypoint_map.json"
    md_path = output_dir / "entrypoint_map.md"

    data = [{"kind": e.kind, "module": e.module, "file": e.file, "line": e.line, "detail": e.detail} for e in entries]
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    lines = [
        "# Entrypoint Map",
        "",
        f"Total entrypoints: **{len(entries)}**",
        "",
        "| Kind | File | Line | Detail |",
        "|------|------|-----:|--------|",
    ]
    for e in entries:
        lines.append(f"| `{e.kind}` | `{e.file}` | {e.line} | `{e.detail}` |")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    return json_path, md_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Map execution entrypoints")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    args = parser.parse_args(argv)

    entries = run(args.root)
    json_path, md_path = write_report(entries, args.root, args.reports_dir)

    by_kind: dict[str, int] = {}
    for e in entries:
        by_kind[e.kind] = by_kind.get(e.kind, 0) + 1
    for kind, count in sorted(by_kind.items()):
        print(f"  {kind}: {count}")
    print(f"Total: {len(entries)}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
