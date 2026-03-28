"""Map the configuration surface: env vars, dotenv loads, and config file reads.

Detects via AST:
  - os.environ["KEY"] / os.environ.get("KEY")
  - os.getenv("KEY")
  - dotenv: load_dotenv(), find_dotenv()
  - yaml.safe_load / yaml.load open(...)
  - json.loads / json.load open(...)
  - toml.load / tomllib.load open(...)
  - pathlib Path(...).read_text on .env / .yaml / .json / .toml

Outputs:
  reports/config_surface.json  — {key: [{file, line, kind}]}
  reports/config_surface.md    — summary tables
"""
from __future__ import annotations

import ast
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files

CONFIG_FILE_SUFFIXES: frozenset[str] = frozenset(
    {".env", ".yaml", ".yml", ".json", ".toml", ".ini", ".cfg"}
)


@dataclass
class ConfigRef:
    key: str        # env var name or config-file path fragment
    kind: str       # "env_var" | "dotenv_load" | "yaml_load" | "json_load" | "toml_load" | "path_read"
    file: str
    line: int


def _string_val(node: ast.expr) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def _func_name(node: ast.Call) -> str:
    """Return dotted function name like 'os.environ.get'."""
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


def extract_config_refs(path: Path, root: Path) -> list[ConfigRef]:
    file_str = str(path.relative_to(root))
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError:
        return []

    refs: list[ConfigRef] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        fname = _func_name(node)

        # os.environ["KEY"] — subscript, handled separately below
        # os.environ.get("KEY") / os.getenv("KEY")
        if fname in {"os.environ.get", "os.getenv"} and node.args:
            key = _string_val(node.args[0])
            if key:
                refs.append(ConfigRef(key, "env_var", file_str, node.lineno))

        # load_dotenv(), find_dotenv()
        elif fname in {"load_dotenv", "dotenv.load_dotenv", "dotenv_values"}:
            refs.append(ConfigRef(".env", "dotenv_load", file_str, node.lineno))

        # yaml.safe_load / yaml.load
        elif fname in {"yaml.safe_load", "yaml.load", "ruamel.yaml.load"}:
            refs.append(ConfigRef("*.yaml", "yaml_load", file_str, node.lineno))

        # json.load / json.loads
        elif fname in {"json.load", "json.loads"}:
            refs.append(ConfigRef("*.json", "json_load", file_str, node.lineno))

        # toml.load / tomllib.load / tomli.load
        elif fname in {"toml.load", "tomllib.load", "tomli.load", "tomllib.loads"}:
            refs.append(ConfigRef("*.toml", "toml_load", file_str, node.lineno))

        # configparser.read / ConfigParser().read
        elif fname in {"configparser.read", "read"} or fname.endswith(".read"):
            if node.args:
                key = _string_val(node.args[0])
                if key and any(key.endswith(s) for s in CONFIG_FILE_SUFFIXES):
                    refs.append(ConfigRef(key, "path_read", file_str, node.lineno))

    # Also handle os.environ["KEY"] subscript access
    for node in ast.walk(tree):
        if isinstance(node, ast.Subscript):
            val = node.value
            if (
                isinstance(val, ast.Attribute)
                and val.attr == "environ"
                and isinstance(val.value, ast.Name)
                and val.value.id == "os"
            ):
                key = _string_val(node.slice)
                if key:
                    refs.append(ConfigRef(key, "env_var", file_str, node.lineno))

    return refs


def run(root: Path = ROOT) -> dict[str, list[dict]]:
    by_key: dict[str, list[dict]] = defaultdict(list)

    for path in find_python_files(root):
        for ref in extract_config_refs(path, root):
            by_key[ref.key].append(
                {"file": ref.file, "line": ref.line, "kind": ref.kind}
            )

    # Sort refs within each key
    for key in by_key:
        by_key[key].sort(key=lambda r: (r["file"], r["line"]))

    return dict(sorted(by_key.items()))


def write_json(surface: dict[str, list[dict]], out_dir: Path = OUTPUT_DIR) -> Path:
    path = out_dir / "config_surface.json"
    path.write_text(json.dumps(surface, indent=2), encoding="utf-8")
    return path


def write_md(surface: dict[str, list[dict]], out_dir: Path = OUTPUT_DIR) -> Path:
    env_vars = {k: v for k, v in surface.items() if any(r["kind"] == "env_var" for r in v)}
    config_loads = {k: v for k, v in surface.items() if any(r["kind"] != "env_var" for r in v)}

    lines = [
        "# Config Surface",
        "",
        f"Env vars referenced: **{len(env_vars)}** | Config file loads: **{len(config_loads)}**",
        "",
        "## Environment Variables",
        "",
        "| Variable | Files |",
        "|----------|-------|",
    ]
    for key in sorted(env_vars):
        files = sorted({r["file"] for r in env_vars[key] if r["kind"] == "env_var"})
        lines.append(f"| `{key}` | {', '.join(f'`{f}`' for f in files)} |")

    lines += [
        "",
        "## Config File Loads",
        "",
        "| Pattern | Kind | File | Line |",
        "|---------|------|------|-----:|",
    ]
    for key in sorted(config_loads):
        for ref in config_loads[key]:
            if ref["kind"] != "env_var":
                lines.append(f"| `{key}` | {ref['kind']} | `{ref['file']}` | {ref['line']} |")

    path = out_dir / "config_surface.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    surface = run()
    json_path = write_json(surface)
    md_path = write_md(surface)

    env_vars = {k for k, v in surface.items() if any(r["kind"] == "env_var" for r in v)}
    print(f"Unique env vars: {len(env_vars)}")
    print(f"Config keys total: {len(surface)}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
