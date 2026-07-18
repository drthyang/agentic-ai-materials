"""Mission Control: live campaign dashboard (Phase 5).

Same footprint as the Phase 4 dashboard — stdlib http.server, zero new
dependencies — but the page is now a static shell (src/athanor/web/) that
fetches /api/snapshot JSON and renders client-side. The server stays
read-only: it renders the DB, notebook, and mission config; it never edits
them (config-over-code applies to the UI too).

Routes:
    /                    the Mission Control shell (index.html)
    /api/snapshot        full campaign state as JSON, read fresh per request
    /api/benchmark       latest benchmark table + plot, when one exists
    /assets/<name>       css / js / woff2 from the packaged web/ directory
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

from athanor.config import MissionConfig
from athanor.db import CandidateDB
from athanor.metrics import row_flags
from athanor.notebook import LabNotebook

WEB_DIR = Path(__file__).parent / "web"

_NUMERIC = ("formation_energy_per_atom", "e_above_hull", "band_gap_ev")


def _scrub(row: dict) -> dict:
    """Repair legacy rows where numpy scalars were stored as raw BLOBs.

    Older campaign DBs hold 4/8-byte little-endian floats in numeric columns
    (numpy's buffer protocol slipped past sqlite3). The dashboard renders
    history, so it must read them; new writes are coerced in CandidateDB.add.
    """
    import struct

    for k in _NUMERIC:
        v = row.get(k)
        if isinstance(v, bytes):
            row[k] = (struct.unpack("<f", v)[0] if len(v) == 4
                      else struct.unpack("<d", v)[0] if len(v) == 8 else None)
    return row

_ASSET_TYPES = {
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".woff2": "font/woff2",
    ".png": "image/png",
    ".svg": "image/svg+xml",
}


def _feed_events(db_rows: list[dict], nb_entries: list[dict],
                 cfg: MissionConfig, limit: int = 30) -> list[dict]:
    """Merge candidate rows and notebook entries into one recent-first feed."""
    events = []
    for r in db_rows:
        when = (r.get("created_at") or "")[:16]  # YYYY-MM-DD HH:MM
        base = {"when": when, "iteration": r["iteration"], "formula": r["formula"]}
        if r["status"] == "scored":
            flags = row_flags(r, cfg)
            gap = r["band_gap_ev"]
            hull = r["e_above_hull"]
            detail = " · ".join(
                ([f"gap {gap:.2f} eV"] if gap is not None else [])
                + ([f"hull {hull:.3f}"] if hull is not None else [])
            )
            if flags["hit"]:
                kind, text = "hit", f"{detail} — novel, in window"
            elif flags["rediscovery"]:
                kind, text = "rediscovery", f"{detail} — hold-out re-found"
            elif not r["converged"]:
                kind, text = "score", "relaxation did not converge"
            else:
                kind, text = "score", detail or "scored"
            events.append({**base, "kind": kind, "text": text})
        elif r["status"] == "error":
            events.append({**base, "kind": "error",
                           "text": (r.get("error") or "evaluation error")[:140]})
        elif r["status"] == "filtered_out":
            reasons = json.loads(r["filter_reasons"]) if r["filter_reasons"] else []
            veto = next((s for s in reasons if s.startswith("critic:")), None)
            if veto:
                events.append({**base, "kind": "veto",
                               "text": veto.removeprefix("critic:").strip()[:140]})
            else:
                events.append({**base, "kind": "filtered",
                               "text": "; ".join(reasons)[:140] or "filtered"})
        # plain "proposed" rows are working state, not events — skip
    for e in nb_entries:
        # notebook stamp "YYYY-MM-DD HH:MM UTC" -> sortable "YYYY-MM-DD HH:MM"
        events.append({
            "when": e["when"].removesuffix(" UTC"),
            "iteration": e["iteration"], "formula": None,
            "kind": "notebook",
            "text": f"[{e['type']}] {e['text']}"[:180],
        })
    events.sort(key=lambda e: e["when"], reverse=True)
    return events[:limit]


def campaign_snapshot(cfg: MissionConfig) -> dict:
    """Everything the dashboard shows, read fresh from disk."""
    snap: dict = {
        "mission": {
            "name": cfg.mission.name,
            "description": cfg.mission.description,
            "band_gap_ev": list(cfg.target.band_gap_ev),
            "band_gap_ideal_ev": cfg.target.band_gap_ideal_ev,
            "e_above_hull_max": cfg.target.e_above_hull_max_ev_per_atom,
            "allowed_elements": cfg.chemistry.allowed_elements,
            "excluded_elements": cfg.chemistry.excluded_elements,
            "max_elements": cfg.chemistry.max_elements_per_compound,
            "budget": cfg.budget.model_dump(),
            "llm": {"backend": cfg.llm.backend, "model": cfg.llm.model},
            "critic": {"enabled": cfg.critic.enabled,
                       "backend": cfg.critic.backend, "model": cfg.critic.model},
            "holdout_formulas": cfg.evaluation.holdout_formulas,
        },
        "iterations": [], "candidates": [], "top": [],
        "notebook": [], "feed": [], "totals": {},
        "meta": {
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "last_activity": None, "running": False,
        },
    }

    nb_entries = (LabNotebook(cfg.paths.notebook).entries()
                  if cfg.paths.notebook.exists() else [])
    snap["notebook"] = nb_entries

    if cfg.paths.db.exists():
        db = CandidateDB(cfg.paths.db)
        snap["iterations"] = db.counts_by_iteration()
        snap["candidates"] = [
            {**r, "flags": row_flags({**r, "status": "scored"}, cfg)}
            for r in map(_scrub, db.all_scored())
        ]
        snap["top"] = [{**t, "flags": row_flags(t, cfg)}
                       for t in map(_scrub, db.top_candidates(10))]
        recent = [_scrub(r) for r in db.recent_events(60)]
        snap["feed"] = _feed_events(recent, nb_entries[-10:], cfg)
        if recent and recent[0].get("created_at"):
            newest = recent[0]["created_at"]
            snap["meta"]["last_activity"] = newest[:16]
            age = (datetime.now(timezone.utc)
                   - datetime.fromisoformat(newest + "+00:00")).total_seconds()
            snap["meta"]["running"] = age < 300
        db.close()

    t = snap["totals"]
    t["proposed"] = sum(i["proposed"] + i["filtered_out"] + i["scored"] + i["error"]
                        for i in snap["iterations"])
    t["filtered_out"] = sum(i["filtered_out"] for i in snap["iterations"])
    t["vetoed"] = sum(i["vetoed"] for i in snap["iterations"])
    t["scored"] = sum(i["scored"] for i in snap["iterations"])
    t["errors"] = sum(i["error"] for i in snap["iterations"])
    t["hits"] = sum(1 for c in snap["candidates"] if c["flags"]["hit"])
    t["rediscoveries"] = sum(1 for c in snap["candidates"] if c["flags"]["rediscovery"])
    t["iterations_done"] = len(snap["iterations"])
    t["relaxations_used"] = t["scored"] + t["errors"]
    t["relaxations_budget"] = (cfg.budget.iterations
                               * cfg.budget.max_relaxations_per_iteration)
    dists = [c["flags"]["gap_distance"] for c in snap["candidates"]
             if c["flags"]["gap_distance"] is not None]
    t["best_gap_distance"] = round(min(dists), 3) if dists else None
    return snap


def benchmark_snapshot(benchmark_dir: Path = Path("data/benchmark/latest")) -> dict:
    """Latest benchmark comparison, parsed from its markdown artifact."""
    md = benchmark_dir / "benchmark.md"
    if not md.exists():
        return {"available": False}
    lines = md.read_text().splitlines()
    header = next((ln for ln in lines if ln.startswith("# ")), "")
    budget = next((ln for ln in lines if ln.startswith("budget:")), "")
    hit_def = next((ln for ln in lines if ln.startswith("hit =")), "")
    table_lines = [ln for ln in lines if ln.startswith("|")]
    rows = []
    if len(table_lines) >= 3:
        cols = [c.strip() for c in table_lines[0].strip("|").split("|")]
        for ln in table_lines[2:]:
            cells = [c.strip() for c in ln.strip("|").split("|")]
            rows.append(dict(zip(cols, cells)))
    return {
        "available": True,
        "title": header.removeprefix("# ").removeprefix("Benchmark:").strip(),
        "budget": budget.removeprefix("budget:").strip(),
        "hit_definition": hit_def.removeprefix("hit =").strip(),
        "rows": rows,
        "has_plot": (benchmark_dir / "benchmark.png").exists(),
    }


def serve(cfg: MissionConfig, port: int = 8517) -> None:
    benchmark_dir = Path("data/benchmark/latest")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 (stdlib API)
            try:
                if self.path in ("/", "/index.html"):
                    self._send(200, "text/html; charset=utf-8",
                               (WEB_DIR / "index.html").read_bytes())
                elif self.path == "/api/snapshot":
                    body = json.dumps(campaign_snapshot(cfg)).encode()
                    self._send(200, "application/json; charset=utf-8", body)
                elif self.path == "/api/benchmark":
                    body = json.dumps(benchmark_snapshot(benchmark_dir)).encode()
                    self._send(200, "application/json; charset=utf-8", body)
                elif self.path == "/api/benchmark/plot.png":
                    png = benchmark_dir / "benchmark.png"
                    if png.exists():
                        self._send(200, "image/png", png.read_bytes())
                    else:
                        self._send(404, "text/plain", b"no benchmark plot")
                elif self.path.startswith("/assets/"):
                    name = self.path.removeprefix("/assets/").split("?", 1)[0]
                    # flat whitelist: no path separators, known extensions only
                    if re.fullmatch(r"[\w.-]+", name) and (WEB_DIR / name).is_file():
                        ctype = _ASSET_TYPES.get(Path(name).suffix)
                        if ctype:
                            self._send(200, ctype, (WEB_DIR / name).read_bytes())
                            return
                    self._send(404, "text/plain", b"not found")
                else:
                    self._send(404, "text/plain", b"not found")
            except Exception as exc:  # the dashboard must never take down a run
                self._send(500, "text/plain", f"dashboard error: {exc}".encode())

        def _send(self, code: int, ctype: str, body: bytes) -> None:
            self.send_response(code)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            if self.path.endswith((".woff2", ".png")):
                self.send_header("Cache-Control", "max-age=86400")
            elif self.path.startswith("/assets/"):
                self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):  # quiet
            pass

    httpd = HTTPServer(("127.0.0.1", port), Handler)
    print(f"athanor dashboard: http://localhost:{port}  (Ctrl-C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
