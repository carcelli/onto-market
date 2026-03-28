"""Cross-reference: for each indexed symbol, show where it is imported or referenced.

Reads reports/symbol_index.json (run symbol_index first).
Scans all Python files for `from X import Y` and bare name usage.

Outputs:
  reports/symbol_xref.json  — {symbol: [{file, line, context}]}
  reports/symbol_xref.md    — grouped Markdown with back-references
"""
from __future__ import annotations

import ast
import json
from collections import defaultdict
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, ROOT, find_python_files


def _load_symbol_index(out_dir: Path) -> list[dict]:
    path = out_dir / "symbol_index.json"
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run symbol_index first:\n"
            "  python -m devtools.repo_tools.symbol_index"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def _extract_names_imported(tree: ast.Module) -> set[str]:
    """Return bare names imported in this file via 'from X import name'."""
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                names.add(alias.asname or alias.name)
    return names


def _find_references(
    path: Path, target_names: set[str], root: Path
) -> list[dict]:
    """Return lines in `path` where any target name appears (import or usage)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(text, filename=str(path))
    except SyntaxError:
        return []

    file_str = str(path.relative_to(root))
    refs: list[dict] = []
    lines = text.splitlines()

    for node in ast.walk(tree):
        # from module import SymbolName
        if isinstance(node, ast.ImportFrom):
            for alias in node.names:
                bare = alias.asname or alias.name
                if bare in target_names:
                    ctx = lines[node.lineno - 1].strip() if node.lineno <= len(lines) else ""
                    refs.append({"file": file_str, "line": node.lineno, "context": ctx, "kind": "import"})

        # Direct name usage: SymbolName(...)  or  x: SymbolName
        elif isinstance(node, ast.Name) and node.id in target_names:
            ctx = lines[node.lineno - 1].strip() if node.lineno <= len(lines) else ""
            refs.append({"file": file_str, "line": node.lineno, "context": ctx, "kind": "usage"})

    return refs


def run(root: Path = ROOT, out_dir: Path = OUTPUT_DIR) -> dict[str, list[dict]]:
    index = _load_symbol_index(out_dir)

    # Build lookup: bare symbol name → list of full qualified names in index
    # (a symbol like "OntologyGraph" may appear in multiple modules)
    name_to_syms: dict[str, list[str]] = defaultdict(list)
    for sym in index:
        bare = sym["name"].split(".")[-1]  # strip class prefix for methods
        name_to_syms[bare].append(f"{sym['module']}.{sym['name']}")

    all_target_names: set[str] = set(name_to_syms.keys())

    # Map: qualified_symbol → list of references
    xref: dict[str, list[dict]] = {
        f"{sym['module']}.{sym['name']}": [] for sym in index
    }

    for path in find_python_files(root):
        refs = _find_references(path, all_target_names, root)
        for ref in refs:
            # The context bare name could match multiple symbols; assign to all
            ctx = ref["context"]
            for bare, qualified_names in name_to_syms.items():
                if bare in ctx:
                    for qname in qualified_names:
                        xref[qname].append(ref)

    # Deduplicate within each symbol's ref list
    for qname in xref:
        seen: set[tuple[str, int]] = set()
        deduped: list[dict] = []
        for r in xref[qname]:
            key = (r["file"], r["line"])
            if key not in seen:
                seen.add(key)
                deduped.append(r)
        xref[qname] = sorted(deduped, key=lambda r: (r["file"], r["line"]))

    return xref


def write_json(xref: dict[str, list[dict]], out_dir: Path = OUTPUT_DIR) -> Path:
    path = out_dir / "symbol_xref.json"
    path.write_text(json.dumps(xref, indent=2), encoding="utf-8")
    return path


def write_md(xref: dict[str, list[dict]], out_dir: Path = OUTPUT_DIR) -> Path:
    lines = [
        "# Symbol Cross-Reference",
        "",
        "Each symbol shows every file/line where it is imported or used.",
        "",
    ]
    for sym, refs in sorted(xref.items()):
        ref_count = len(refs)
        lines.append(f"## `{sym}` ({ref_count} refs)")
        if not refs:
            lines.append("_No references found._")
        else:
            lines.append("")
            lines.append("| File | Line | Kind | Context |")
            lines.append("|------|-----:|------|---------|")
            for r in refs:
                ctx = r["context"].replace("|", "\\|")[:80]
                lines.append(f"| `{r['file']}` | {r['line']} | {r['kind']} | `{ctx}` |")
        lines.append("")

    path = out_dir / "symbol_xref.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    xref = run()
    json_path = write_json(xref)
    md_path = write_md(xref)

    total_refs = sum(len(v) for v in xref.values())
    zero_ref = sum(1 for v in xref.values() if not v)
    print(f"Symbols indexed: {len(xref)}")
    print(f"Total references: {total_refs}")
    print(f"Unreferenced symbols: {zero_ref}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
