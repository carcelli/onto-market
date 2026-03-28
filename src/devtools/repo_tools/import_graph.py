"""Build a directed import graph from Python AST.

Outputs:
  reports/import_graph.json   — machine-readable node/edge list
  reports/import_graph.mmd    — Mermaid LR diagram
  reports/import_graph.dot    — Graphviz DOT digraph
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

from devtools.repo_tools._common import (
    OUTPUT_DIR,
    ROOT,
    find_python_files,
    is_internal,
    module_name,
    normalize_internal_target,
    parse_imports,
)


def build_graph(root: Path = ROOT) -> dict[str, set[str]]:
    files = find_python_files(root)
    known_modules: set[str] = {module_name(p, root) for p in files}
    graph: dict[str, set[str]] = defaultdict(set)

    for path in files:
        src = module_name(path, root)
        imports = parse_imports(path)
        for imported in imports:
            if is_internal(imported, known_modules):
                dst = normalize_internal_target(imported, known_modules)
                if src != dst:
                    graph[src].add(dst)
        graph.setdefault(src, set())

    return graph


def write_json(graph: dict[str, set[str]], out_dir: Path = OUTPUT_DIR) -> Path:
    data = {
        "nodes": sorted(graph.keys()),
        "edges": sorted(
            [{"source": src, "target": dst} for src, targets in graph.items() for dst in targets],
            key=lambda x: (x["source"], x["target"]),
        ),
    }
    path = out_dir / "import_graph.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def write_mermaid(graph: dict[str, set[str]], out_dir: Path = OUTPUT_DIR) -> Path:
    lines = ["graph LR"]
    for src in sorted(graph):
        targets = graph[src]
        if not targets:
            lines.append(f'    "{src}"')
        for dst in sorted(targets):
            lines.append(f'    "{src}" --> "{dst}"')
    path = out_dir / "import_graph.mmd"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_dot(graph: dict[str, set[str]], out_dir: Path = OUTPUT_DIR) -> Path:
    lines = ['digraph ImportGraph {', '  rankdir="LR";']
    for src in sorted(graph):
        targets = graph[src]
        if not targets:
            lines.append(f'  "{src}";')
        for dst in sorted(targets):
            lines.append(f'  "{src}" -> "{dst}";')
    lines.append("}")
    path = out_dir / "import_graph.dot"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    graph = build_graph()
    json_path = write_json(graph)
    mmd_path = write_mermaid(graph)
    dot_path = write_dot(graph)

    edge_count = sum(len(v) for v in graph.values())
    print(f"Modules : {len(graph)}")
    print(f"Edges   : {edge_count}")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {mmd_path}")
    print(f"Wrote: {dot_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
