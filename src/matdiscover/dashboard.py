"""Live campaign dashboard: watch the agent explore, zero extra dependencies.

A stdlib http.server renders one self-contained HTML page per request straight
from the campaign DB + notebook (auto-refresh every 10 s): iteration stats,
top candidates, a gap-vs-hull map with the target region, and the notebook
stream. Run alongside `matdiscover run`:

    uv run matdiscover dashboard          # http://localhost:8517
"""

from __future__ import annotations

import base64
import html
import io
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from matdiscover.config import MissionConfig
from matdiscover.db import CandidateDB
from matdiscover.notebook import LabNotebook


def campaign_snapshot(cfg: MissionConfig) -> dict:
    """Everything the dashboard shows, read fresh from disk."""
    snap = {"scored": [], "iterations": {}, "top": [], "notebook": ""}
    if cfg.paths.db.exists():
        db = CandidateDB(cfg.paths.db)
        snap["scored"] = db.all_scored()
        iters = sorted({r["iteration"] for r in snap["scored"]})
        snap["iterations"] = {i: db.iteration_summary(i) for i in iters}
        snap["top"] = db.top_candidates(10)
        db.close()
    if cfg.paths.notebook.exists():
        snap["notebook"] = LabNotebook(cfg.paths.notebook).read(last_n_entries=8)
    return snap


def _scatter_png(cfg: MissionConfig, scored: list[dict]) -> str | None:
    """Gap-vs-hull map as base64 PNG; None when nothing to plot."""
    pts = [(r["e_above_hull"], r["band_gap_ev"], r["iteration"]) for r in scored
           if r["e_above_hull"] is not None and r["band_gap_ev"] is not None]
    if not pts:
        return None

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    lo, hi = cfg.target.band_gap_ev
    hull_max = cfg.target.e_above_hull_max_ev_per_atom
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    xs, ys, cs = zip(*pts)
    sc = ax.scatter(xs, ys, c=cs, cmap="viridis", s=42, edgecolor="k", linewidth=0.4)
    ax.add_patch(Rectangle((0, lo), hull_max, hi - lo, alpha=0.18, color="green",
                           label="target region"))
    ax.set_xlabel("energy above hull (eV/atom)")
    ax.set_ylabel("band gap, HSE fidelity (eV)")
    ax.set_xlim(left=-0.005)
    ax.legend(loc="upper right", fontsize=8)
    fig.colorbar(sc, ax=ax, label="iteration")
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=110)
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode()


def render_html(cfg: MissionConfig) -> str:
    snap = campaign_snapshot(cfg)
    lo, hi = cfg.target.band_gap_ev

    iter_rows = "".join(
        f"<tr><td>{i}</td><td>{stats.get('proposed', 0)}</td>"
        f"<td>{stats.get('filtered_out', 0)}</td><td>{stats.get('scored', 0)}</td>"
        f"<td>{stats.get('error', 0)}</td></tr>"
        for i, stats in snap["iterations"].items()
    ) or "<tr><td colspan=5>no data yet</td></tr>"

    top_rows = "".join(
        f"<tr><td>{html.escape(r['formula'])}</td>"
        f"<td>{r['band_gap_ev']:.2f}</td><td>{r['e_above_hull']:.3f}</td>"
        f"<td>{r['iteration']}</td>"
        f"<td>{html.escape((r['hypothesis'] or '')[:120])}</td></tr>"
        for r in snap["top"]
        if r["band_gap_ev"] is not None and r["e_above_hull"] is not None
    ) or "<tr><td colspan=5>none yet</td></tr>"

    png = _scatter_png(cfg, snap["scored"])
    plot_html = (f'<img src="data:image/png;base64,{png}" alt="gap vs hull">'
                 if png else "<p><em>no scored candidates yet</em></p>")

    notebook_html = html.escape(snap["notebook"][-6000:]) or "(empty)"

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta http-equiv="refresh" content="10">
<title>matdiscover — {html.escape(cfg.mission.name)}</title>
<style>
 body {{ font-family: -apple-system, sans-serif; margin: 2rem; color: #1a1a1a; }}
 h1 {{ font-size: 1.3rem; }} h2 {{ font-size: 1.05rem; margin-top: 1.6rem; }}
 table {{ border-collapse: collapse; font-size: 0.85rem; }}
 td, th {{ border: 1px solid #ccc; padding: 4px 10px; text-align: left; }}
 th {{ background: #f0f0f0; }}
 pre {{ background: #f7f7f5; padding: 1rem; font-size: 0.78rem;
        white-space: pre-wrap; max-height: 24rem; overflow-y: auto; }}
 .grid {{ display: flex; gap: 2.5rem; flex-wrap: wrap; }}
</style></head><body>
<h1>matdiscover: {html.escape(cfg.mission.name)}</h1>
<p>target: gap in [{lo}, {hi}] eV &middot; hull &le;
{cfg.target.e_above_hull_max_ev_per_atom} eV/atom &middot;
backend: {html.escape(cfg.llm.backend)} ({html.escape(cfg.llm.model)}) &middot;
auto-refreshes every 10 s</p>
<div class="grid">
<div><h2>iterations</h2>
<table><tr><th>iter</th><th>proposed</th><th>filtered</th><th>scored</th><th>errors</th></tr>
{iter_rows}</table></div>
<div><h2>composition-space map</h2>{plot_html}</div>
</div>
<h2>top candidates</h2>
<table><tr><th>formula</th><th>gap (eV)</th><th>hull (eV/atom)</th><th>iter</th><th>hypothesis</th></tr>
{top_rows}</table>
<h2>lab notebook (latest entries)</h2>
<pre>{notebook_html}</pre>
</body></html>"""


def serve(cfg: MissionConfig, port: int = 8517) -> None:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 (stdlib API)
            if self.path not in ("/", "/index.html"):
                self.send_response(404)
                self.end_headers()
                return
            body = render_html(cfg).encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):  # quiet
            pass

    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"dashboard: http://localhost:{port} (ctrl-c to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
