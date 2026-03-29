"""Cross-reference: for each indexed symbol, show where it is imported/referenced.

Requires reports/symbol_index.json (run symbol_index first).

Outputs:
  reports/symbol_xref.json  — {qualified_symbol: [{file, line, context, kind}]}
  reports/symbol_xref.md    — grouped Markdown with back-references
"""
from __future__ import annotations

import argparse
import ast
import json
from collections import defaultdict
from pathlib import Path
from typing import Sequence

from ._common import find_python_files
from ._paths import resolve_output_path, resolve_repo_root


def _load_symbol_index(output_dir: Path) -> list[dict]:
    path = output_dir / "symbol_index.json"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found — run `make symbol-index` first."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def _find_refs(path: Path, target_names: set[str], root: Path) -> list[dict]:
    file_str = str(path.relative_to(root))
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError:
        return []

    lines_text = text.splitlines()
    refs: list[dict] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                bare = alias.asname or alias.name
                if bare in target_names:
                    ctx = lines_text[node.lineno - 1].strip() if node.lineno <= len(lines_text) else ""
                    refs.append({"file": file_str, "line": node.lineno, "context": ctx, "kind": "import"})
        elif isinstance(node, ast.Name) and node.id in target_names:
            ctx = lines_text[node.lineno - 1].strip() if node.lineno <= len(lines_text) else ""
            refs.append({"file": file_str, "line": node.lineno, "context": ctx, "kind": "usage"})

    return refs


def run(root: Path | None = None, reports_dir: Path | None = None) -> dict[str, list[dict]]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    index = _load_symbol_index(output_dir)

    name_to_syms: dict[str, list[str]] = defaultdict(list)
    for sym in index:
        bare = sym["name"].split(".")[-1]
        name_to_syms[bare].append(f"{sym['module']}.{sym['name']}")

    all_names: set[str] = set(name_to_syms.keys())
    xref: dict[str, list[dict]] = {f"{sym['module']}.{sym['name']}": [] for sym in index}

    for path in find_python_files(repo_root):
        refs = _find_refs(path, all_names, repo_root)
        for ref in refs:
            for bare, qnames in name_to_syms.items():
                if bare in ref["context"]:
                    for qname in qnames:
                        xref[qname].append(ref)

    for qname in xref:
        seen: set[tuple[str, int]] = set()
        deduped = []
        for r in xref[qname]:
            key = (r["file"], r["line"])
            if key not in seen:
                seen.add(key)
                deduped.append(r)
        xref[qname] = sorted(deduped, key=lambda r: (r["file"], r["line"]))

    return xref


def write_report(
    xref: dict[str, list[dict]],
    root: Path | None = None,
    reports_dir: Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "symbol_xref.json"
    md_path = output_dir / "symbol_xref.md"

    json_path.write_text(json.dumps(xref, indent=2), encoding="utf-8")

    lines = ["# Symbol Cross-Reference", "", "Each symbol shows where it is imported or used.", ""]
    for sym, refs in sorted(xref.items()):
        lines.append(f"## `{sym}` ({len(refs)} refs)")
        if not refs:
            lines.append("_No references found._")
        else:
            lines += ["", "| File | Line | Kind | Context |", "|------|-----:|------|---------|"]
            for r in refs:
                ctx = r["context"].replace("|", "\\|")[:80]
                lines.append(f"| `{r['file']}` | {r['line']} | {r['kind']} | `{ctx}` |")
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Cross-reference symbol usages")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    args = parser.parse_args(argv)

    xref = run(args.root, args.reports_dir)
    json_path, md_path = write_report(xref, args.root, args.reports_dir)

    total_refs = sum(len(v) for v in xref.values())
    zero_ref = sum(1 for v in xref.values() if not v)
    print(f"Symbols: {len(xref)} | Total refs: {total_refs} | Unreferenced: {zero_ref}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
