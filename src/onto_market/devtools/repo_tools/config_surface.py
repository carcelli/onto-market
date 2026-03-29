"""Map the configuration surface: env vars, dotenv loads, config file reads.

Detects via AST:
  - os.environ["KEY"] / os.environ.get("KEY") / os.getenv("KEY")
  - load_dotenv(), dotenv_values()
  - yaml.safe_load, json.load, toml.load, tomllib.load

Outputs:
  reports/config_surface.json  — {key: [{file, line, kind}]}
  reports/config_surface.md    — summary tables
"""
from __future__ import annotations

import argparse
import ast
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from ._common import find_python_files
from ._paths import resolve_output_path, resolve_repo_root

CONFIG_SUFFIXES: frozenset[str] = frozenset({".env", ".yaml", ".yml", ".json", ".toml", ".ini", ".cfg"})


@dataclass
class ConfigRef:
    key: str
    kind: str
    file: str
    line: int


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


def _str_val(node: ast.expr) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _extract(path: Path, root: Path) -> list[ConfigRef]:
    file_str = str(path.relative_to(root))
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError:
        return []

    refs: list[ConfigRef] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fname = _func_name(node)
            if fname in {"os.environ.get", "os.getenv"} and node.args:
                key = _str_val(node.args[0])
                if key:
                    refs.append(ConfigRef(key, "env_var", file_str, node.lineno))
            elif fname in {"load_dotenv", "dotenv.load_dotenv", "dotenv_values"}:
                refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))
            elif fname in {"yaml.safe_load", "yaml.load"}:
                refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))
            elif fname in {"json.load", "json.loads"}:
                refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))
            elif fname in {"toml.load", "tomllib.load", "tomli.load", "tomllib.loads"}:
                refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))

        # os.environ["KEY"] subscript access
        if isinstance(node, ast.Subscript):
            val = node.value
            if (
                isinstance(val, ast.Attribute)
                and val.attr == "environ"
                and isinstance(val.value, ast.Name)
                and val.value.id == "os"
            ):
                key = _str_val(node.slice)
                if key:
                    refs.append(ConfigRef(key, "env_var", file_str, node.lineno))

    return refs


def run(root: Path | None = None) -> dict[str, list[dict]]:
    repo_root = resolve_repo_root(root)
    by_key: dict[str, list[dict]] = defaultdict(list)
    for path in find_python_files(repo_root):
        for ref in _extract(path, repo_root):
            by_key[ref.key].append({"file": ref.file, "line": ref.line, "kind": ref.kind})
    for key in by_key:
        by_key[key].sort(key=lambda r: (r["file"], r["line"]))
    return dict(sorted(by_key.items()))


def write_report(
    surface: dict[str, list[dict]],
    root: Path | None = None,
    reports_dir: Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "config_surface.json"
    md_path = output_dir / "config_surface.md"

    json_path.write_text(json.dumps(surface, indent=2), encoding="utf-8")

    env_vars = {k: v for k, v in surface.items() if any(r["kind"] == "env_var" for r in v)}
    config_loads = {k: v for k, v in surface.items() if any(r["kind"] != "env_var" for r in v)}

    lines = [
        "# Config Surface",
        "",
        f"Env vars: **{len(env_vars)}** | Config file loads: **{len(config_loads)}**",
        "",
        "## Environment Variables",
        "",
        "| Variable | Files |",
        "|----------|-------|",
    ]
    for key in sorted(env_vars):
        files = sorted({r["file"] for r in env_vars[key] if r["kind"] == "env_var"})
        lines.append(f"| `{key}` | {', '.join(f'`{f}`' for f in files)} |")

    lines += ["", "## Config File Loads", "", "| Pattern | Kind | File | Line |", "|---------|------|------|-----:|"]
    for key in sorted(config_loads):
        for ref in config_loads[key]:
            if ref["kind"] != "env_var":
                lines.append(f"| `{key}` | {ref['kind']} | `{ref['file']}` | {ref['line']} |")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Surface config and env var usage")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    args = parser.parse_args(argv)

    surface = run(args.root)
    json_path, md_path = write_report(surface, args.root, args.reports_dir)

    env_count = sum(1 for v in surface.values() if any(r["kind"] == "env_var" for r in v))
    print(f"Unique env vars: {env_count} | Config keys total: {len(surface)}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
