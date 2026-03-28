"""Tests for repo-cartography tooling."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import time

import networkx as nx

SRC_ROOT = Path(__file__).resolve().parents[1] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from onto_market.devtools.repo_tools import census, ontology_audit, repo_map


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
