"""Map source modules to their test files; highlight coverage gaps.

A module is "covered" if:
  a) a test file imports it, OR
  b) the test filename matches test_{module_leaf}.py

Outputs:
  reports/test_map.json  — [{module, covered, test_files}]
  reports/test_map.md    — table with gap markers
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from ._common import find_python_files, module_name, parse_imports
from ._paths import resolve_output_path, resolve_repo_root

EXEMPT_PREFIXES: tuple[str, ...] = (
    "onto_market.devtools.",
    "devtools.",
    "scripts.",
    "tests.",
    "onto_market.config",
    "onto_market.main",
    "main",
)


def _is_test(path: Path) -> bool:
    name = path.stem
    return name.startswith("test_") or name.endswith("_test")


def _leaf(mod: str) -> str:
    return mod.split(".")[-1]


def build_map(root: Path | None = None) -> dict[str, dict]:
    repo_root = resolve_repo_root(root)
    all_files = find_python_files(repo_root)

    source_mods: list[tuple[str, Path]] = []
    test_files: list[Path] = []

    for path in all_files:
        mod = module_name(path, repo_root)
        if _is_test(path):
            test_files.append(path)
            continue
        if any(mod.startswith(p) for p in EXEMPT_PREFIXES):
            continue
        if mod.endswith("__init__") or mod == "__init__":
            continue
        source_mods.append((mod, path))

    test_imports: dict[str, set[str]] = {str(tp): parse_imports(tp) for tp in test_files}

    results: dict[str, dict] = {}
    for mod, _ in source_mods:
        leaf = _leaf(mod)
        covering: list[str] = []
        for tp in test_files:
            tp_rel = str(tp.relative_to(repo_root))
            if tp.stem in {f"test_{leaf}", f"{leaf}_test"}:
                covering.append(tp_rel)
                continue
            imported = test_imports.get(str(tp), set())
            if any(imp == mod or imp.startswith(mod + ".") or mod.startswith(imp + ".") for imp in imported):
                covering.append(tp_rel)
        results[mod] = {"covered": bool(covering), "test_files": sorted(set(covering))}

    return results


def write_report(
    coverage: dict[str, dict],
    root: Path | None = None,
    reports_dir: Path | None = None,
) -> tuple[Path, Path]:
    repo_root = resolve_repo_root(root)
    output_dir = resolve_output_path(repo_root, reports_dir, "reports")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "test_map.json"
    md_path = output_dir / "test_map.md"

    data = [{"module": m, "covered": i["covered"], "test_files": i["test_files"]} for m, i in sorted(coverage.items())]
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    covered_list = [m for m, i in coverage.items() if i["covered"]]
    uncovered = [m for m, i in coverage.items() if not i["covered"]]
    pct = 100 * len(covered_list) / len(coverage) if coverage else 0

    lines = [
        "# Test Map",
        "",
        f"Source modules: **{len(coverage)}** | Covered: **{len(covered_list)}** | Gaps: **{len(uncovered)}** | Coverage: **{pct:.0f}%**",
        "",
        "## Coverage Gaps (untested modules)",
        "",
    ]
    if uncovered:
        for mod in sorted(uncovered):
            lines.append(f"- `{mod}`")
    else:
        lines.append("_All source modules have at least one test._")
    lines += ["", "## Full Coverage Table", "", "| Module | Covered | Test Files |", "|--------|:-------:|------------|"]
    for mod in sorted(coverage):
        info = coverage[mod]
        tick = "yes" if info["covered"] else "**NO**"
        tests = ", ".join(f"`{t}`" for t in info["test_files"]) or "_none_"
        lines.append(f"| `{mod}` | {tick} | {tests} |")

    md_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, md_path


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Map source modules to test files")
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--reports-dir", type=Path, default=None)
    args = parser.parse_args(argv)

    coverage = build_map(args.root)
    json_path, md_path = write_report(coverage, args.root, args.reports_dir)

    covered = sum(1 for i in coverage.values() if i["covered"])
    total = len(coverage)
    pct = 100 * covered / total if total else 0
    print(f"Source modules: {total} | Covered: {covered} ({pct:.0f}%) | Gaps: {total - covered}")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
