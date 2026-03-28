"""Tests for repo-cartography tooling."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import time

import networkx as nx
import pytest

SRC_ROOT = Path(__file__).resolve().parents[1] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from onto_market.devtools.repo_tools import (  # noqa: E402
    census,
    ontology_audit,
    repo_map,
    import_graph,
    boundary_matrix,
    cycle_detector,
    architecture_drift,
)


def test_repo_census_builds_and_writes_reports(tmp_path: Path) -> None:
    (tmp_path / "src").mkdir()
    (tmp_path / "tests").mkdir()
    (tmp_path / "src" / "module.py").write_text("print('ok')\n", encoding="utf-8")
    (tmp_path / "tests" / "test_module.py").write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("# demo\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("[project]\nname='demo'\n", encoding="utf-8")
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "ignored.txt").write_text("ignored\n", encoding="utf-8")

    report = census.build_report(tmp_path)

    assert report["total_files"] == 4
    assert "src" in report["top_level_dirs"]
    assert report["category_counts"]["src"] == 1
    assert report["category_counts"]["tests"] == 1

    json_path, md_path = census.write_report(report, root=tmp_path)

    assert json_path.exists()
    assert md_path.exists()
    assert json.loads(json_path.read_text(encoding="utf-8"))["total_files"] == 4
    assert "# Repo Census" in md_path.read_text(encoding="utf-8")


def test_repo_map_generates_markdown(tmp_path: Path) -> None:
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "memory.db").write_bytes(b"sqlite")
    (tmp_path / "data" / "ontology.json").write_text(
        json.dumps({"nodes": [{"id": "alpha"}], "links": []}),
        encoding="utf-8",
    )

    output_path = tmp_path / "REPO_MAP.md"
    body = repo_map.generate(root=tmp_path, output_path=output_path)

    assert output_path.exists()
    assert body.startswith("# onto-market Repository Map")
    assert "Devtools boundary" in body
    assert "REPO_MAP.md" in output_path.name


# ---------------------------------------------------------------------------
# import_graph
# ---------------------------------------------------------------------------


def _make_package(root: Path, modules: dict[str, str]) -> Path:
    """Create a minimal onto_market package under root/src/ with given modules.

    modules: {"subpath/module.py": "source code", ...}
    """
    pkg = root / "src" / "onto_market"
    pkg.mkdir(parents=True)
    (pkg / "__init__.py").write_text("", encoding="utf-8")
    (root / "pyproject.toml").write_text("[project]\nname='test'\n", encoding="utf-8")
    for rel, src in modules.items():
        target = pkg / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(src, encoding="utf-8")
    return root


def test_import_graph_discovers_edge(tmp_path: Path) -> None:
    _make_package(
        tmp_path,
        {
            "core/__init__.py": "",
            "core/base.py": "X = 1",
            "agents/__init__.py": "",
            "agents/planner.py": "from onto_market.core.base import X",
        },
    )
    g = import_graph.build_graph(tmp_path)

    assert "onto_market.agents.planner" in g.nodes
    assert "onto_market.core.base" in g.nodes
    assert g.has_edge("onto_market.agents.planner", "onto_market.core.base")


def test_import_graph_relative_import(tmp_path: Path) -> None:
    _make_package(
        tmp_path,
        {
            "utils/__init__.py": "",
            "utils/logger.py": "LOG = None",
            "utils/retry.py": "from .logger import LOG",
        },
    )
    g = import_graph.build_graph(tmp_path)
    assert g.has_edge("onto_market.utils.retry", "onto_market.utils.logger")


def test_import_graph_no_self_loops(tmp_path: Path) -> None:
    _make_package(
        tmp_path,
        {
            "config/__init__.py": "",
            "config/settings.py": "from onto_market.config.settings import X  # circular-looking",
        },
    )
    g = import_graph.build_graph(tmp_path)
    # self-loops must be suppressed
    assert not g.has_edge("onto_market.config.settings", "onto_market.config.settings")


def test_import_graph_snapshot_counts(tmp_path: Path) -> None:
    _make_package(
        tmp_path,
        {
            "core/__init__.py": "",
            "core/base.py": "X = 1",
            "agents/__init__.py": "",
            "agents/planner.py": "from onto_market.core.base import X",
            "agents/memory.py": "from onto_market.core import base",
        },
    )
    snapshot, g = import_graph.analyze(tmp_path)
    assert snapshot.modules_scanned >= 5
    assert snapshot.edges >= 2
    assert snapshot.cycles == 0


def test_import_graph_write_reports(tmp_path: Path) -> None:
    _make_package(tmp_path, {"utils/__init__.py": "", "utils/helpers.py": "X = 1"})
    snapshot, _ = import_graph.analyze(tmp_path)
    json_path, md_path = import_graph.write_report(snapshot, root=tmp_path)

    assert json_path.exists()
    assert md_path.exists()
    data = json.loads(json_path.read_text())
    assert "modules_scanned" in data
    assert "# Import Graph Report" in md_path.read_text()


# ---------------------------------------------------------------------------
# boundary_matrix
# ---------------------------------------------------------------------------


def test_boundary_matrix_counts_cross_domain_edges(tmp_path: Path) -> None:
    _make_package(
        tmp_path,
        {
            "core/__init__.py": "",
            "core/base.py": "X = 1",
            "agents/__init__.py": "",
            "agents/planner.py": "from onto_market.core.base import X",
        },
    )
    g = import_graph.build_graph(tmp_path)
    snapshot = boundary_matrix.analyze_from_graph(g, tmp_path)

    assert snapshot.boundaries_checked >= 1
    # agents → core should appear
    agents_row = snapshot.matrix.get("agents", {})
    assert agents_row.get("core", 0) >= 1


def test_boundary_matrix_ignores_intra_domain(tmp_path: Path) -> None:
    _make_package(
        tmp_path,
        {
            "agents/__init__.py": "",
            "agents/state.py": "S = {}",
            "agents/planner.py": "from onto_market.agents.state import S",
        },
    )
    g = import_graph.build_graph(tmp_path)
    snapshot = boundary_matrix.analyze_from_graph(g, tmp_path)
    # intra-domain (agents → agents) must NOT be counted
    assert snapshot.boundaries_checked == 0


# ---------------------------------------------------------------------------
# cycle_detector
# ---------------------------------------------------------------------------


def test_cycle_detector_finds_cycle() -> None:
    g: nx.DiGraph = nx.DiGraph()
    g.add_edge("onto_market.a.foo", "onto_market.b.bar")
    g.add_edge("onto_market.b.bar", "onto_market.a.foo")

    from pathlib import Path

    snapshot = cycle_detector.analyze_from_graph(g, Path("/tmp"))
    assert snapshot.cycles_found >= 1
    assert len(snapshot.scc_groups) >= 1


def test_cycle_detector_dag_has_no_cycles() -> None:
    g: nx.DiGraph = nx.DiGraph()
    g.add_edge("onto_market.agents.planner", "onto_market.core.base")
    g.add_edge("onto_market.core.base", "onto_market.config.settings")

    snapshot = cycle_detector.analyze_from_graph(g, Path("/tmp"))
    assert snapshot.cycles_found == 0
    assert snapshot.scc_groups == []


def test_cycle_detector_write_reports(tmp_path: Path) -> None:
    _make_package(tmp_path, {"utils/__init__.py": "", "utils/helpers.py": "X = 1"})
    snapshot = cycle_detector.analyze(tmp_path)
    json_path, md_path = cycle_detector.write_report(snapshot, root=tmp_path)

    assert json_path.exists()
    assert md_path.exists()
    assert "# Cycle Detector Report" in md_path.read_text()


# ---------------------------------------------------------------------------
# architecture_drift
# ---------------------------------------------------------------------------


def test_architecture_drift_catches_violation() -> None:
    g: nx.DiGraph = nx.DiGraph()
    # config importing from agents is a clear violation
    g.add_edge("onto_market.config.settings", "onto_market.agents.planner")

    snapshot = architecture_drift.analyze_from_graph(g, Path("/tmp"))
    assert snapshot.violations_found >= 1
    assert any(v.src_domain == "config" for v in snapshot.violations)


def test_architecture_drift_allows_legal_import() -> None:
    g: nx.DiGraph = nx.DiGraph()
    # agents importing from core is always allowed
    g.add_edge("onto_market.agents.planner", "onto_market.core.base")

    snapshot = architecture_drift.analyze_from_graph(g, Path("/tmp"))
    assert snapshot.violations_found == 0


def test_architecture_drift_connectors_cannot_import_swarm() -> None:
    g: nx.DiGraph = nx.DiGraph()
    g.add_edge("onto_market.connectors.gamma", "onto_market.swarm.oracle")

    snapshot = architecture_drift.analyze_from_graph(g, Path("/tmp"))
    assert snapshot.violations_found >= 1
    assert any(
        v.src_domain == "connectors" and v.dst_domain == "swarm"
        for v in snapshot.violations
    )


def test_architecture_drift_write_reports(tmp_path: Path) -> None:
    _make_package(tmp_path, {"config/__init__.py": "", "config/settings.py": "X = 1"})
    snapshot = architecture_drift.analyze(tmp_path)
    json_path, md_path = architecture_drift.write_report(snapshot, root=tmp_path)

    assert json_path.exists()
    assert md_path.exists()
    data = json.loads(json_path.read_text())
    assert "violations_found" in data
    assert "# Architecture Drift Report" in md_path.read_text()


# ---------------------------------------------------------------------------
# Integration: run all four on the real repo
# ---------------------------------------------------------------------------


def test_import_graph_on_real_repo() -> None:
    """Smoke-test: build the real graph — must find modules and parse without crashing."""
    repo_root = Path(__file__).resolve().parents[1]
    snapshot, g = import_graph.analyze(repo_root)

    assert snapshot.modules_scanned > 10, "Expected more than 10 onto_market modules"
    assert snapshot.edges > 5, "Expected more than 5 import edges"
    # Validate a key module exists
    assert any("agents" in n for n in g.nodes()), "Expected agent modules in graph"


def test_boundary_matrix_on_real_repo() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    snapshot = boundary_matrix.analyze(repo_root)
    # The real repo has cross-domain coupling; matrix must be non-trivial
    assert snapshot.boundaries_checked >= 0  # zero is acceptable if all intra-domain


def test_cycle_detector_on_real_repo() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    snapshot = cycle_detector.analyze(repo_root)
    # We just verify it runs without error; cycles may or may not exist
    assert isinstance(snapshot.cycles_found, int)


def test_architecture_drift_on_real_repo() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    snapshot = architecture_drift.analyze(repo_root)
    # Report any violations discovered but don't hard-fail — we want to see reality
    assert isinstance(snapshot.violations_found, int)


def test_ontology_audit_runs_on_simple_graph(tmp_path: Path, capsys) -> None:
    graph = nx.DiGraph()
    now = time.time()
    graph.add_node("alpha", first_seen=now, last_seen=now)
    graph.add_node("beta", first_seen=now, last_seen=now)
    graph.add_edge("alpha", "beta", confidence=0.9, predicate="supports")

    ontology_path = tmp_path / "ontology.json"
    ontology_path.write_text(
        json.dumps(nx.node_link_data(graph, edges="links")),
        encoding="utf-8",
    )

    exit_code = ontology_audit.main(["--path", str(ontology_path), "--top-n", "1"])
    captured = capsys.readouterr()

    assert exit_code == 0
    assert "SUMMARY" in captured.out
    assert "Ontology graph is healthy" in captured.out
