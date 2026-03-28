"""Find circular imports via Tarjan's strongly connected components (SCC).

Reads reports/import_graph.json (run import_graph first).
A cycle exists when an SCC has more than one node, or a single node
with a self-edge.

Outputs:
  reports/cycle_detector.json  — list of SCCs (cycles) with member modules
  reports/cycle_detector.md    — human-readable report with cycle members
"""
from __future__ import annotations

import json
from pathlib import Path

from devtools.repo_tools._common import OUTPUT_DIR, load_import_graph_json


def _tarjan_scc(adj: dict[str, list[str]]) -> list[list[str]]:
    """Iterative Tarjan SCC — avoids Python recursion limit on large graphs."""
    index_counter = [0]
    index: dict[str, int] = {}
    lowlink: dict[str, int] = {}
    on_stack: dict[str, bool] = {}
    stack: list[str] = []
    sccs: list[list[str]] = []

    def strongconnect(v: str) -> None:
        # Iterative version using an explicit call stack
        call_stack: list[tuple[str, list[str], int]] = []
        call_stack.append((v, list(adj.get(v, [])), 0))
        index[v] = index_counter[0]
        lowlink[v] = index_counter[0]
        index_counter[0] += 1
        stack.append(v)
        on_stack[v] = True

        while call_stack:
            node, neighbors, ni = call_stack[-1]
            if ni < len(neighbors):
                call_stack[-1] = (node, neighbors, ni + 1)
                w = neighbors[ni]
                if w not in index:
                    index[w] = index_counter[0]
                    lowlink[w] = index_counter[0]
                    index_counter[0] += 1
                    stack.append(w)
                    on_stack[w] = True
                    call_stack.append((w, list(adj.get(w, [])), 0))
                elif on_stack.get(w):
                    lowlink[node] = min(lowlink[node], index[w])
            else:
                call_stack.pop()
                if call_stack:
                    parent = call_stack[-1][0]
                    lowlink[parent] = min(lowlink[parent], lowlink[node])
                if lowlink[node] == index[node]:
                    scc: list[str] = []
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        scc.append(w)
                        if w == node:
                            break
                    sccs.append(scc)

    for v in list(adj.keys()):
        if v not in index:
            strongconnect(v)

    return sccs


def build_adj(data: dict) -> dict[str, list[str]]:
    adj: dict[str, list[str]] = {n: [] for n in data["nodes"]}
    for edge in data["edges"]:
        adj[edge["source"]].append(edge["target"])
    return adj


def find_cycles(data: dict) -> list[dict]:
    adj = build_adj(data)
    sccs = _tarjan_scc(adj)
    edge_set = {(e["source"], e["target"]) for e in data["edges"]}

    cycles: list[dict] = []
    for scc in sccs:
        if len(scc) > 1:
            cycles.append({"size": len(scc), "members": sorted(scc), "kind": "multi-node"})
        elif len(scc) == 1:
            node = scc[0]
            if (node, node) in edge_set:
                cycles.append({"size": 1, "members": [node], "kind": "self-loop"})

    return sorted(cycles, key=lambda c: -c["size"])


def write_json(cycles: list[dict], out_dir: Path = OUTPUT_DIR) -> Path:
    path = out_dir / "cycle_detector.json"
    path.write_text(json.dumps(cycles, indent=2), encoding="utf-8")
    return path


def write_md(cycles: list[dict], out_dir: Path = OUTPUT_DIR) -> Path:
    lines = ["# Cycle Detector", ""]
    if not cycles:
        lines += [
            "> No circular imports detected. Import graph is a DAG.",
            "",
        ]
    else:
        lines += [
            f"> **{len(cycles)} cycle(s) detected.** Cycles indicate tightly coupled identity clusters.",
            f"> Resolve by introducing an interface module or inverting the dependency.",
            "",
            "| # | Kind | Size | Members |",
            "|---|------|-----:|---------|",
        ]
        for i, c in enumerate(cycles, 1):
            members = ", ".join(f"`{m}`" for m in c["members"])
            lines.append(f"| {i} | {c['kind']} | {c['size']} | {members} |")
        lines.append("")

        lines.append("## Cycle Details")
        lines.append("")
        for i, c in enumerate(cycles, 1):
            lines.append(f"### Cycle {i} ({c['kind']}, {c['size']} modules)")
            for m in c["members"]:
                lines.append(f"- `{m}`")
            lines.append("")

    path = out_dir / "cycle_detector.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main() -> int:
    OUTPUT_DIR.mkdir(exist_ok=True)
    data = load_import_graph_json()
    cycles = find_cycles(data)
    json_path = write_json(cycles)
    md_path = write_md(cycles)

    if cycles:
        print(f"Cycles found: {len(cycles)}")
        for c in cycles:
            print(f"  [{c['kind']}] {' -> '.join(c['members'][:4])}{'...' if len(c['members']) > 4 else ''}")
    else:
        print("No circular imports — graph is a DAG.")
    print(f"Wrote: {json_path}")
    print(f"Wrote: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
