"""onto-market — Live Repo Ontology Dashboard.

Launch:  streamlit run reports/streamlit_app.py
   or:   make dashboard
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------------------
# Make onto_market importable regardless of how Streamlit was launched
# ---------------------------------------------------------------------------
_SRC = Path(__file__).resolve().parent.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

_REPO_ROOT = Path(__file__).resolve().parent.parent

from onto_market.devtools.repo_tools import (  # noqa: E402
    census,
    import_graph,
    boundary_matrix,
    cycle_detector,
    architecture_drift,
)
from onto_market.devtools.repo_tools._paths import resolve_repo_root  # noqa: E402

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="onto-market repo dashboard",
    page_icon="\U0001f9ec",  # DNA emoji
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Cached data loaders — rebuild the graph once per 5 min (or on explicit refresh)
# ---------------------------------------------------------------------------

@st.cache_data(ttl=300, show_spinner="Scanning modules...")
def _load_census() -> dict:
    return census.build_report(root=_REPO_ROOT)


@st.cache_data(ttl=300, show_spinner="Building import graph...")
def _load_import_snapshot() -> dict:
    snap, g = import_graph.analyze(root=_REPO_ROOT)
    import networkx as nx
    return {
        "modules_scanned": snap.modules_scanned,
        "edges": snap.edges,
        "cycles": snap.cycles,
        "isolated": snap.isolated,
        "top_importers": snap.top_importers,
        "top_imported": snap.top_imported,
        "adjacency": snap.adjacency,
        "node_link": nx.node_link_data(g, edges="links"),
    }


@st.cache_data(ttl=300, show_spinner="Computing boundary matrix...")
def _load_boundary() -> dict:
    snap = boundary_matrix.analyze(root=_REPO_ROOT)
    return {
        "domains": snap.domains,
        "matrix": snap.matrix,
        "top_couplings": snap.top_couplings,
        "boundaries_checked": snap.boundaries_checked,
    }


@st.cache_data(ttl=300, show_spinner="Detecting cycles...")
def _load_cycles() -> dict:
    snap = cycle_detector.analyze(root=_REPO_ROOT)
    return {
        "modules_scanned": snap.modules_scanned,
        "cycles_found": snap.cycles_found,
        "scc_groups": snap.scc_groups,
        "simple_cycles": snap.simple_cycles,
    }


@st.cache_data(ttl=300, show_spinner="Auditing architecture drift...")
def _load_drift() -> dict:
    snap = architecture_drift.analyze(root=_REPO_ROOT)
    return {
        "modules_scanned": snap.modules_scanned,
        "edges_checked": snap.edges_checked,
        "violations_found": snap.violations_found,
        "violations": [
            {
                "from": v.src_module,
                "to": v.dst_module,
                "src_domain": v.src_domain,
                "dst_domain": v.dst_domain,
                "reason": v.reason,
            }
            for v in snap.violations
        ],
        "unknown_domains": snap.unknown_domains,
    }


@st.cache_data(ttl=300, show_spinner="Loading ontology graph...")
def _load_ontology() -> dict:
    onto_path = _REPO_ROOT / "data" / "ontology.json"
    if not onto_path.exists():
        return {"nodes": 0, "edges": 0, "top_entities": [], "edge_list": []}

    from onto_market.ontology.graph import OntologyGraph
    og = OntologyGraph(persist_path=str(onto_path))
    stats = og.stats()
    edge_list = [
        {
            "subject": u,
            "predicate": d.get("predicate", "related_to"),
            "object": v,
            "confidence": round(d.get("confidence", 0.0), 2),
        }
        for u, v, d in og.g.edges(data=True)
    ]
    return {
        "nodes": stats["nodes"],
        "edges": stats["edges"],
        "top_entities": stats["top_entities"],
        "edge_list": edge_list,
    }


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("onto-market")
    st.caption("Live repo ontology dashboard")

    if st.button("Refresh all data", type="primary", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

    st.divider()
    st.markdown(f"**Root** `{_REPO_ROOT}`")
    st.caption(f"Last loaded {datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}")

    st.divider()
    st.markdown("**Quick commands**")
    st.code("make repo-health\nmake dashboard\nmake dryrun", language="bash")

# ---------------------------------------------------------------------------
# Tab layout
# ---------------------------------------------------------------------------
tab_overview, tab_graph, tab_boundaries, tab_ontology, tab_census = st.tabs(
    ["Overview", "Import Graph", "Boundaries + Drift", "Ontology", "Census"]
)

# ===== TAB 1: Overview =====================================================
with tab_overview:
    st.header("Repository Overview")

    cen = _load_census()
    ig = _load_import_snapshot()
    cyc = _load_cycles()
    drift = _load_drift()
    onto = _load_ontology()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total files", cen.get("total_files", 0))
        py_count = sum(
            len(v) for v in cen.get("python_files_by_top_level", {}).values()
        )
        st.metric("Python modules", py_count)
    with c2:
        st.metric("Import edges", ig["edges"])
        st.metric("Modules scanned", ig["modules_scanned"])
    with c3:
        delta_color = "off" if cyc["cycles_found"] == 0 else "inverse"
        st.metric("Import cycles", cyc["cycles_found"], delta_color=delta_color)
        v_count = drift["violations_found"]
        st.metric(
            "Drift violations",
            v_count,
            delta=f"{v_count} issues" if v_count else "clean",
            delta_color="off" if v_count == 0 else "inverse",
        )
    with c4:
        st.metric("Ontology nodes", onto["nodes"])
        st.metric("Ontology edges", onto["edges"])

    st.divider()

    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("Top importers (out-degree)")
        import pandas as pd
        if ig["top_importers"]:
            df_imp = pd.DataFrame(ig["top_importers"], columns=["Module", "Imports"])
            df_imp["Module"] = df_imp["Module"].str.replace("onto_market.", "", regex=False)
            st.bar_chart(df_imp.set_index("Module"), horizontal=True)
        else:
            st.info("No import edges found.")

    with col_r:
        st.subheader("Most imported (in-degree)")
        if ig["top_imported"]:
            df_dep = pd.DataFrame(ig["top_imported"], columns=["Module", "Imported by"])
            df_dep["Module"] = df_dep["Module"].str.replace("onto_market.", "", regex=False)
            st.bar_chart(df_dep.set_index("Module"), horizontal=True)
        else:
            st.info("No import edges found.")


# ===== TAB 2: Import Graph =================================================
with tab_graph:
    st.header("Module Import Graph")
    st.caption(
        f"{ig['modules_scanned']} modules, {ig['edges']} edges, "
        f"{ig['isolated']} isolated"
    )

    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib

    matplotlib.use("Agg")

    g = nx.node_link_graph(ig["node_link"], directed=True, multigraph=False, edges="links")

    # Strip common prefix for readability
    label_map = {n: n.replace("onto_market.", "") for n in g.nodes()}
    g_display = nx.relabel_nodes(g, label_map)

    # Colour by domain
    _DOMAIN_COLORS = {
        "agents": "#4CAF50",
        "config": "#9E9E9E",
        "connectors": "#2196F3",
        "context": "#FF9800",
        "core": "#673AB7",
        "devtools": "#795548",
        "main": "#607D8B",
        "memory": "#00BCD4",
        "ontology": "#E91E63",
        "polymarket_agents": "#FFC107",
        "swarm": "#3F51B5",
        "trading": "#F44336",
        "utils": "#8BC34A",
    }

    def _node_domain(name: str) -> str:
        parts = name.split(".")
        return parts[0] if parts else "other"

    node_colors = [
        _DOMAIN_COLORS.get(_node_domain(n), "#BDBDBD") for n in g_display.nodes()
    ]

    fig, ax = plt.subplots(figsize=(16, 10))
    fig.patch.set_facecolor("#0E1117")
    ax.set_facecolor("#0E1117")

    # Remove isolated nodes for cleaner layout
    non_iso = [n for n in g_display.nodes() if g_display.degree(n) > 0]
    sub = g_display.subgraph(non_iso)
    sub_colors = [
        _DOMAIN_COLORS.get(_node_domain(n), "#BDBDBD") for n in sub.nodes()
    ]

    pos = nx.spring_layout(sub, k=2.2, iterations=80, seed=42)
    nx.draw_networkx_edges(sub, pos, ax=ax, alpha=0.25, edge_color="#555555",
                           arrows=True, arrowsize=10, connectionstyle="arc3,rad=0.08")
    nx.draw_networkx_nodes(sub, pos, ax=ax, node_color=sub_colors, node_size=350,
                           edgecolors="#222222", linewidths=0.5)
    nx.draw_networkx_labels(sub, pos, ax=ax, font_size=6, font_color="white",
                            font_weight="bold")
    ax.set_title("onto_market import graph (isolated nodes hidden)",
                 color="white", fontsize=12, pad=12)
    ax.axis("off")

    # Legend
    from matplotlib.lines import Line2D
    legend_items = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor=c,
               markersize=8, label=d)
        for d, c in sorted(_DOMAIN_COLORS.items())
        if any(_node_domain(n) == d for n in sub.nodes())
    ]
    ax.legend(handles=legend_items, loc="lower left", fontsize=7,
              facecolor="#1a1a2e", edgecolor="#333", labelcolor="white",
              framealpha=0.9)

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)

    # Adjacency table
    with st.expander("Full adjacency list", expanded=False):
        rows = []
        for mod, deps in sorted(ig["adjacency"].items()):
            if deps:
                short = mod.replace("onto_market.", "")
                rows.append({
                    "Module": short,
                    "Imports": ", ".join(d.replace("onto_market.", "") for d in deps),
                    "Count": len(deps),
                })
        if rows:
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


# ===== TAB 3: Boundaries + Drift ==========================================
with tab_boundaries:
    st.header("Cross-Domain Boundaries")

    bnd = _load_boundary()
    st.metric("Cross-boundary edges", bnd["boundaries_checked"])

    if bnd["top_couplings"]:
        st.subheader("Top couplings")
        df_coup = pd.DataFrame(
            bnd["top_couplings"], columns=["From", "To", "Edges"]
        )
        st.dataframe(df_coup, use_container_width=True, hide_index=True)

    # NxN heatmap
    domains = bnd["domains"]
    if domains:
        st.subheader("Coupling matrix")
        matrix_rows = []
        for sd in domains:
            row = {dd: bnd["matrix"].get(sd, {}).get(dd, 0) for dd in domains}
            matrix_rows.append(row)
        df_matrix = pd.DataFrame(matrix_rows, index=domains, columns=domains)

        fig_heat, ax_heat = plt.subplots(figsize=(10, 8))
        fig_heat.patch.set_facecolor("#0E1117")
        ax_heat.set_facecolor("#0E1117")

        cmap = plt.colormaps.get_cmap("YlOrRd")
        im = ax_heat.imshow(df_matrix.values, cmap=cmap, aspect="auto")
        ax_heat.set_xticks(range(len(domains)))
        ax_heat.set_yticks(range(len(domains)))
        ax_heat.set_xticklabels(domains, rotation=45, ha="right", fontsize=8, color="white")
        ax_heat.set_yticklabels(domains, fontsize=8, color="white")
        ax_heat.set_xlabel("imports from", color="white", fontsize=9)
        ax_heat.set_ylabel("domain", color="white", fontsize=9)
        ax_heat.tick_params(colors="white")

        for i in range(len(domains)):
            for j in range(len(domains)):
                val = df_matrix.values[i, j]
                if val > 0:
                    ax_heat.text(j, i, str(int(val)), ha="center", va="center",
                                 fontsize=8, color="black" if val > 3 else "white")

        cbar = fig_heat.colorbar(im, ax=ax_heat, shrink=0.8)
        cbar.ax.yaxis.set_tick_params(color="white")
        cbar.ax.tick_params(labelcolor="white")
        fig_heat.tight_layout()
        st.pyplot(fig_heat, use_container_width=True)
        plt.close(fig_heat)

    st.divider()

    # Architecture drift
    st.header("Architecture Drift")
    drift_data = _load_drift()

    if drift_data["violations_found"] == 0:
        st.success("No architecture violations. Import graph conforms to the layer policy.")
    else:
        st.warning(f"{drift_data['violations_found']} violation(s) detected")
        df_v = pd.DataFrame(drift_data["violations"])
        df_v.columns = ["From module", "To module", "Src domain", "Dst domain", "Reason"]
        st.dataframe(df_v, use_container_width=True, hide_index=True)

    if drift_data["unknown_domains"]:
        st.info(
            "Unknown domains (not in policy): "
            + ", ".join(f"`{d}`" for d in drift_data["unknown_domains"])
        )


# ===== TAB 4: Ontology =====================================================
with tab_ontology:
    st.header("Knowledge Ontology Graph")
    onto_data = _load_ontology()

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Nodes", onto_data["nodes"])
    with c2:
        st.metric("Edges", onto_data["edges"])

    if onto_data["top_entities"]:
        st.subheader("Top entities by degree")
        df_ent = pd.DataFrame(onto_data["top_entities"], columns=["Entity", "Degree"])
        st.dataframe(df_ent, use_container_width=True, hide_index=True)

    if onto_data["edge_list"]:
        st.subheader("All triples")
        df_triples = pd.DataFrame(onto_data["edge_list"])
        df_triples.columns = ["Subject", "Predicate", "Object", "Confidence"]
        st.dataframe(df_triples, use_container_width=True, hide_index=True)

        st.subheader("Ontology graph")
        onto_path = _REPO_ROOT / "data" / "ontology.json"
        if onto_path.exists():
            from onto_market.ontology.graph import OntologyGraph
            og = OntologyGraph(persist_path=str(onto_path))
            og_display = nx.relabel_nodes(og.g, {n: n for n in og.g.nodes()})

            fig_onto, ax_onto = plt.subplots(figsize=(12, 8))
            fig_onto.patch.set_facecolor("#0E1117")
            ax_onto.set_facecolor("#0E1117")

            if og_display.number_of_nodes() > 0:
                pos_onto = nx.spring_layout(og_display, k=2.5, iterations=60, seed=7)
                edge_labels = {
                    (u, v): d.get("predicate", "")
                    for u, v, d in og_display.edges(data=True)
                }
                confs = [
                    d.get("confidence", 0.5) for _, _, d in og_display.edges(data=True)
                ]
                nx.draw_networkx_edges(
                    og_display, pos_onto, ax=ax_onto, alpha=0.4,
                    edge_color="#888", arrows=True, arrowsize=12,
                    width=[max(0.5, c * 3) for c in confs] if confs else [1],
                )
                nx.draw_networkx_nodes(
                    og_display, pos_onto, ax=ax_onto,
                    node_color="#E91E63", node_size=500,
                    edgecolors="#333", linewidths=0.8,
                )
                nx.draw_networkx_labels(
                    og_display, pos_onto, ax=ax_onto,
                    font_size=7, font_color="white", font_weight="bold",
                )
                nx.draw_networkx_edge_labels(
                    og_display, pos_onto, edge_labels=edge_labels,
                    ax=ax_onto, font_size=6, font_color="#aaa",
                )

            ax_onto.set_title("data/ontology.json", color="white", fontsize=11)
            ax_onto.axis("off")
            st.pyplot(fig_onto, use_container_width=True)
            plt.close(fig_onto)
    else:
        st.info(
            "No ontology triples yet. Run `make plan QUERY='...'` to populate "
            "the ontology graph."
        )


# ===== TAB 5: Census =======================================================
with tab_census:
    st.header("Full Repo Census")
    cen_data = _load_census()

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Files by category")
        cats = cen_data.get("category_counts", {})
        if cats:
            df_cat = pd.DataFrame(
                sorted(cats.items(), key=lambda x: -x[1]),
                columns=["Category", "Count"],
            )
            st.bar_chart(df_cat.set_index("Category"))

    with col_b:
        st.subheader("File extensions")
        exts = cen_data.get("top_extensions", {})
        if exts:
            df_ext = pd.DataFrame(
                list(exts.items()), columns=["Extension", "Count"]
            )
            st.bar_chart(df_ext.set_index("Extension"))

    st.subheader("Top-level directories")
    st.write(", ".join(f"`{d}`" for d in cen_data.get("top_level_dirs", [])))

    st.subheader("Important repo files")
    for f in cen_data.get("important_files", []):
        st.text(f"  {f}")

    st.subheader("Python files by area")
    for area, files in sorted(cen_data.get("python_files_by_top_level", {}).items()):
        with st.expander(f"{area}/ ({len(files)} files)"):
            for f in files:
                st.text(f"  {f}")

    with st.expander("Raw census JSON"):
        st.json(cen_data, expanded=False)
