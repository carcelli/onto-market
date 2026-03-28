"""Discover real execution entrypoints in the repo via AST analysis.

Detects:
  - if __name__ == "__main__" blocks
  - Typer / Click app definitions (app = typer.Typer(), @app.command)
  - FastAPI app definitions
  - LangGraph graph definitions (StateGraph, add_node, compile)
  - Scheduled / cron-style scripts (APScheduler, schedule lib)
  - pyproject.toml [project.scripts] entries

Outputs:
  reports/entrypoint_map.json  — machine-readable list of entrypoints
  reports/entrypoint_map.md    — human-readable table
"""
from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files, module_name

TOML_SCRIPTS_RE = re.compile(r"^\s*(\S+)\s*=\s*\"([^\"]+)\"", re.MULTILINE)


@dataclass
class Entrypoint:
    kind: str
    module: str
    file: str
    line: int
    detail: str = ""


def _has_dunder_main(tree: ast.Module) -> int | None:
    """Return the line number of `if __name__ == '__main__':` or None."""
    for node in ast.walk(tree):
        if not isinstance(node, ast.If):
            continue
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


def _detect_framework_patterns(
    tree: ast.Module, mod: str, file_str: str
) -> list[Entrypoint]:
    found: list[Entrypoint] = []

    for node in ast.walk(tree):
        # Typer / Click: app = typer.Typer() or cli = typer.Typer()
        if isinstance(node, ast.Assign):
            if isinstance(node.value, ast.Call):
                call = node.value
                func = call.func
                func_str = ""
                if isinstance(func, ast.Attribute):
                    func_str = f"{getattr(func.value, 'id', '')}." + func.attr
                elif isinstance(func, ast.Name):
                    func_str = func.id
                if func_str in {"typer.Typer", "click.Group", "click.group"}:
                    found.append(
                        Entrypoint("typer/click", mod, file_str, node.lineno, func_str)
                    )
                if "StateGraph" in func_str or func_str == "StateGraph":
                    found.append(
                        Entrypoint("langgraph", mod, file_str, node.lineno, func_str)
                    )
                if func_str in {"FastAPI", "flask.Flask", "Starlette"}:
                    found.append(
                        Entrypoint("web-app", mod, file_str, node.lineno, func_str)
                    )

        # FastAPI / LangGraph / APScheduler via attribute call:
        # e.g. workflow.add_node(...) or scheduler.add_job(...)
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            call = node.value
            if isinstance(call.func, ast.Attribute):
                attr = call.func.attr
                if attr in {"add_node", "compile"} and isinstance(
                    call.func.value, ast.Name
                ):
                    found.append(
                        Entrypoint(
                            "langgraph",
                            mod,
                            file_str,
                            node.lineno,
                            f".{attr}()",
                        )
                    )
                if attr in {"add_job", "start"} and isinstance(
                    call.func.value, ast.Name
                ):
                    found.append(
                        Entrypoint(
                            "scheduler",
                            mod,
                            file_str,
                            node.lineno,
                            f".{attr}()",
                        )
                    )

    return found


def _pyproject_scripts(root: Path) -> list[Entrypoint]:
    toml_path = root / "pyproject.toml"
    if not toml_path.exists():
        return []
    text = toml_path.read_text(encoding="utf-8")
    # Find [project.scripts] section
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
                    Entrypoint(
                        "console-script",
                        target.split(":")[0],
                        "pyproject.toml",
                        i,
                        f"{cmd} = {target}",
                    )
                )
    return entries


def run(root: Path = ROOT) -> list[Entrypoint]:
    results: list[Entrypoint] = []

    for path in find_python_files(root):
        mod = module_name(path, root)
        file_str = str(path.relative_to(root))
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(text, filename=str(path))
        except SyntaxError:
            continue

        line = _has_dunder_main(tree)
        if line:
            results.append(Entrypoint("__main__", mod, file_str, line))

        results.extend(_detect_framework_patterns(tree, mod, file_str))

    results.extend(_pyproject_scripts(root))

    # Deduplicate by (kind, module, line)
    seen: set[tuple[str, str, int]] = set()
    deduped: list[Entrypoint] = []
    for ep in results:
        key = (ep.kind, ep.module, ep.line)
        if key not in seen:
            seen.add(key)
            deduped.append(ep)

    return sorted(deduped, key=lambda e: (e.kind, e.file, e.line))


def write_json(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:
    data = [
        {
            "kind": e.kind,
            "module": e.module,
            "file": e.file,
            "line": e.line,
            "detail": e.detail,
        }
        for e in entries
    ]
    path = out_dir / "entrypoint_map.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def write_md(entries: list[Entrypoint], out_dir: Path = OUTPUT_DIR) -> Path:
    lines = [
        "# Entrypoint Map",
        "",
        "| Kind | File | Line | Detail |",
        "|------|------|-----:|--------|",
    ]
    for e in entries:
        lines.append(f"| `{e.kind}` | `{e.file}` | {e.line} | `{e.detail}` |")

    path = out_dir / "entrypoint_map.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    entries = run()
    json_path = write_json(entries)
    md_path = write_md(entries)

    by_kind: dict[str, int] = {}
    for e in entries:
        by_kind[e.kind] = by_kind.get(e.kind, 0) + 1
    for kind, count in sorted(by_kind.items()):
        print(f"  {kind}: {count}")
    print(f"Total entrypoints: {len(entries)}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
