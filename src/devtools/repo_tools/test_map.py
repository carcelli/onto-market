"""Map source modules to their test files, and highlight coverage gaps.

Strategy:
  - A test file "covers" a source module if:
    a) it imports from that module, OR
    b) its filename matches test_{module_leaf}.py / {module_leaf}_test.py

Outputs:
  reports/test_map.json  — {source_module: [test_files], covered: bool}
  reports/test_map.md    — table with gap markers
"""
from __future__ import annotations

import ast
import json
from pathlib import Path

from devtools.repo_tools._common import (
    OUTPUT_DIR,
    ROOT,
    find_python_files,
    module_name,
    parse_imports,
)

# Modules whose test-absence is expected / not a gap
EXEMPT_PREFIXES: tuple[str, ...] = (
    "devtools.",
    "scripts.",
    "tests.",
    "config.",
    "main",
)


def _is_test_file(path: Path) -> bool:
    name = path.stem
    return name.startswith("test_") or name.endswith("_test")


def _source_modules(root: Path) -> list[str]:
    result: list[str] = []
    for path in find_python_files(root):
        mod = module_name(path, root)
        if _is_test_file(path):
            continue
        if any(mod.startswith(p) for p in EXEMPT_PREFIXES):
            continue
        if mod.endswith("__init__"):
            continue
        result.append(mod)
    return sorted(result)


def _test_files(root: Path) -> list[Path]:
    return [p for p in find_python_files(root) if _is_test_file(p)]


def _leaf(module: str) -> str:
    return module.split(".")[-1]


def build_map(root: Path = ROOT) -> dict[str, dict]:
    source_mods = _source_modules(root)
    test_paths = _test_files(root)

    # For each test file, collect the set of modules it imports
    test_imports: dict[str, set[str]] = {}
    for tp in test_paths:
        test_imports[str(tp)] = parse_imports(tp)

    results: dict[str, dict] = {}
    for mod in source_mods:
        covering_tests: list[str] = []
        leaf = _leaf(mod)

        for tp in test_paths:
            tp_rel = str(tp.relative_to(root))
            tp_stem = tp.stem  # e.g. "test_memory"

            # Name-based match: test_memory.py covers memory.manager etc.
            if tp_stem in {f"test_{leaf}", f"{leaf}_test"}:
                covering_tests.append(tp_rel)
                continue

            # Import-based match
            imported = test_imports.get(str(tp), set())
            if any(
                imp == mod or imp.startswith(mod + ".") or mod.startswith(imp + ".")
                for imp in imported
            ):
                covering_tests.append(tp_rel)

        results[mod] = {
            "covered": len(covering_tests) > 0,
            "test_files": sorted(set(covering_tests)),
        }

    return results


def write_json(coverage: dict[str, dict], out_dir: Path = OUTPUT_DIR) -> Path:
    data = [
        {"module": mod, "covered": info["covered"], "test_files": info["test_files"]}
        for mod, info in sorted(coverage.items())
    ]
    path = out_dir / "test_map.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def write_md(coverage: dict[str, dict], out_dir: Path = OUTPUT_DIR) -> Path:
    covered = [m for m, i in coverage.items() if i["covered"]]
    uncovered = [m for m, i in coverage.items() if not i["covered"]]
    pct = 100 * len(covered) / len(coverage) if coverage else 0

    lines = [
        "# Test Map",
        "",
        f"Source modules: **{len(coverage)}** | "
        f"Covered: **{len(covered)}** | "
        f"Gaps: **{len(uncovered)}** | "
        f"Coverage: **{pct:.0f}%**",
        "",
        "## Coverage gaps (untested modules)",
        "",
    ]
    if uncovered:
        for mod in sorted(uncovered):
            lines.append(f"- `{mod}`")
    else:
        lines.append("_All modules have at least one test._")
    lines.append("")

    lines += [
        "## Full coverage table",
        "",
        "| Module | Covered | Test Files |",
        "|--------|:-------:|------------|",
    ]
    for mod in sorted(coverage):
        info = coverage[mod]
        tick = "yes" if info["covered"] else "**NO**"
        tests = ", ".join(f"`{t}`" for t in info["test_files"]) or "_none_"
        lines.append(f"| `{mod}` | {tick} | {tests} |")

    path = out_dir / "test_map.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    coverage = build_map()
    json_path = write_json(coverage)
    md_path = write_md(coverage)

    covered = sum(1 for i in coverage.values() if i["covered"])
    total = len(coverage)
    pct = 100 * covered / total if total else 0
    print(f"Source modules: {total}")
    print(f"Covered: {covered} ({pct:.0f}%)")
    print(f"Gaps: {total - covered}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
