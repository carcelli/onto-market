"""
Zero-dependency ontology explorer server.

Serves the D3 force-graph HTML and the live ontology.json via a REST-ish API.
The HTML polls /api/ontology every 5 seconds, so any planning_agent run that
writes to data/ontology.json is reflected in the browser automatically.

Usage:
    python -m onto_market.dashboard.serve          # default port 8765
    python -m onto_market.dashboard.serve --port 9000
    make explorer                                  # via Makefile

Endpoints:
    GET /              → explorer.html
    GET /api/ontology  → data/ontology.json (live, CORS-enabled)
    GET /api/stats     → {nodes, edges, top_entities} from OntologyGraph
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from functools import lru_cache
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_REPO = _HERE.parent.parent.parent  # workspace root
_ONTOLOGY = _REPO / "data" / "ontology.json"
_EXPLORER = _HERE / "explorer.html"


class ExplorerHandler(SimpleHTTPRequestHandler):
    """Custom handler: routes /api/* to data, everything else to the HTML."""

    def do_GET(self) -> None:
        if self.path == "/" or self.path == "/index.html":
            self._serve_file(_EXPLORER, "text/html")
        elif self.path == "/api/ontology":
            self._serve_ontology()
        elif self.path == "/api/stats":
            self._serve_stats()
        else:
            self.send_error(404)

    def _serve_ontology(self) -> None:
        if not _ONTOLOGY.exists():
            self._json_response(
                {"directed": True, "multigraph": False, "graph": {}, "nodes": [], "edges": []},
                status=200,
            )
            return
        data = _ONTOLOGY.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self._cors_headers()
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache, no-store")
        self.end_headers()
        self.wfile.write(data)

    def _serve_stats(self) -> None:
        if not _ONTOLOGY.exists():
            self._json_response({"nodes": 0, "edges": 0, "top_entities": []})
            return
        try:
            raw = json.loads(_ONTOLOGY.read_text("utf-8"))
            nodes = raw.get("nodes", [])
            edges = raw.get("links", raw.get("edges", []))
            deg: dict[str, int] = {}
            for n in nodes:
                deg[n["id"]] = 0
            for e in edges:
                s = e["source"] if isinstance(e["source"], str) else e["source"]["id"]
                t = e["target"] if isinstance(e["target"], str) else e["target"]["id"]
                deg[s] = deg.get(s, 0) + 1
                deg[t] = deg.get(t, 0) + 1
            top = sorted(deg.items(), key=lambda x: -x[1])[:10]
            self._json_response({
                "nodes": len(nodes),
                "edges": len(edges),
                "top_entities": [{"entity": n, "degree": d} for n, d in top],
            })
        except Exception as exc:
            self._json_response({"error": str(exc)}, status=500)

    def _serve_file(self, path: Path, content_type: str) -> None:
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def _json_response(self, obj: dict, status: int = 200) -> None:
        body = json.dumps(obj).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self._cors_headers()
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-cache, no-store")
        self.end_headers()
        self.wfile.write(body)

    def _cors_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET")

    def log_message(self, fmt: str, *args) -> None:
        # quieter logs — skip static asset noise
        if args and "/api/" in str(args[0]):
            super().log_message(fmt, *args)


def main() -> None:
    parser = argparse.ArgumentParser(description="onto-market ontology explorer")
    parser.add_argument("--port", type=int, default=8765, help="HTTP port (default: 8765)")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host (default: 0.0.0.0)")
    args = parser.parse_args()

    if not _ONTOLOGY.exists():
        print(f"⚠  {_ONTOLOGY} not found — explorer will show empty graph until an agent runs.")

    server = HTTPServer((args.host, args.port), ExplorerHandler)
    url = f"http://localhost:{args.port}"
    print(f"✦ Ontology Explorer running at {url}")
    print(f"  Data source: {_ONTOLOGY}")
    print(f"  Auto-refreshes every 5s — run planning_agent queries to grow the graph.")
    print(f"  Ctrl+C to stop.\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n✦ Explorer stopped.")
        server.server_close()


if __name__ == "__main__":
    main()
