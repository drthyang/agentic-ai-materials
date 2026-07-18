"""Campaign persistence: every candidate ever considered, in SQLite."""

from __future__ import annotations

import json
import sqlite3
from dataclasses import asdict, dataclass
from pathlib import Path

_SCHEMA = """
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    iteration INTEGER NOT NULL,
    formula TEXT NOT NULL,
    parent_prototype TEXT,
    substitution TEXT,          -- JSON {from: to}
    hypothesis TEXT,            -- the agent's stated reason for proposing it
    status TEXT NOT NULL,       -- proposed | filtered_out | scored | error
    filter_reasons TEXT,        -- JSON list
    converged INTEGER,
    formation_energy_per_atom REAL,
    e_above_hull REAL,
    band_gap_ev REAL,
    is_novel INTEGER,
    error TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_candidates_formula ON candidates(formula);
"""


@dataclass
class CandidateRow:
    iteration: int
    formula: str
    status: str
    parent_prototype: str | None = None
    substitution: dict | None = None
    hypothesis: str | None = None
    filter_reasons: list[str] | None = None
    converged: bool | None = None
    formation_energy_per_atom: float | None = None
    e_above_hull: float | None = None
    band_gap_ev: float | None = None
    is_novel: bool | None = None
    error: str | None = None


class CandidateDB:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.path)
        self._conn.row_factory = sqlite3.Row
        self._conn.executescript(_SCHEMA)

    def add(self, row: CandidateRow) -> int:
        d = asdict(row)
        d["substitution"] = json.dumps(d["substitution"]) if d["substitution"] else None
        d["filter_reasons"] = json.dumps(d["filter_reasons"]) if d["filter_reasons"] else None
        # numpy scalars (e.g. CHGNet's float32) bind as BLOBs via the buffer
        # protocol — coerce so numbers are stored as SQLite REALs.
        for k in ("formation_energy_per_atom", "e_above_hull", "band_gap_ev"):
            if d[k] is not None:
                d[k] = float(d[k])
        cols = ", ".join(d)
        placeholders = ", ".join(f":{k}" for k in d)
        cur = self._conn.execute(
            f"INSERT INTO candidates ({cols}) VALUES ({placeholders})", d
        )
        self._conn.commit()
        return cur.lastrowid

    def already_seen(self, formula: str) -> bool:
        cur = self._conn.execute(
            "SELECT 1 FROM candidates WHERE formula = ? LIMIT 1", (formula,)
        )
        return cur.fetchone() is not None

    def top_candidates(self, limit: int = 20) -> list[dict]:
        """Best scored candidates, sorted by hull distance.

        is_novel NULL (no MP key -> novelty unknown) is included; only
        confirmed-known materials (is_novel = 0) are excluded.
        """
        cur = self._conn.execute(
            """SELECT * FROM candidates
               WHERE status = 'scored' AND converged = 1
                 AND (is_novel = 1 OR is_novel IS NULL)
               ORDER BY e_above_hull ASC NULLS LAST LIMIT ?""",
            (limit,),
        )
        return [dict(r) for r in cur.fetchall()]

    def all_scored(self) -> list[dict]:
        """Every scored candidate with its key numbers, campaign-wide."""
        cur = self._conn.execute(
            """SELECT iteration, formula, converged, formation_energy_per_atom,
                      e_above_hull, band_gap_ev, is_novel, hypothesis
               FROM candidates WHERE status = 'scored'
               ORDER BY iteration, e_above_hull ASC NULLS LAST"""
        )
        return [dict(r) for r in cur.fetchall()]

    def iteration_summary(self, iteration: int) -> dict:
        cur = self._conn.execute(
            """SELECT status, COUNT(*) n FROM candidates
               WHERE iteration = ? GROUP BY status""",
            (iteration,),
        )
        return {r["status"]: r["n"] for r in cur.fetchall()}

    def counts_by_iteration(self) -> list[dict]:
        """Per-iteration funnel: status counts plus critic vetoes.

        Vetoes are the subset of filtered_out whose filter_reasons carry the
        "critic:" prefix written by evaluate_candidates.
        """
        cur = self._conn.execute(
            """SELECT iteration, status, COUNT(*) n,
                      SUM(CASE WHEN status = 'filtered_out'
                               AND filter_reasons LIKE '%critic:%'
                          THEN 1 ELSE 0 END) vetoed
               FROM candidates GROUP BY iteration, status ORDER BY iteration"""
        )
        out: dict[int, dict] = {}
        for r in cur.fetchall():
            row = out.setdefault(
                r["iteration"],
                {"iteration": r["iteration"], "proposed": 0, "filtered_out": 0,
                 "vetoed": 0, "scored": 0, "error": 0},
            )
            if r["status"] in row:
                row[r["status"]] = r["n"]
            row["vetoed"] += r["vetoed"] or 0
        return list(out.values())

    def recent_events(self, limit: int = 40) -> list[dict]:
        """Newest candidate rows for the dashboard feed (all statuses)."""
        cur = self._conn.execute(
            """SELECT iteration, formula, status, filter_reasons, hypothesis,
                      converged, e_above_hull, band_gap_ev, is_novel, error,
                      created_at
               FROM candidates ORDER BY id DESC LIMIT ?""",
            (limit,),
        )
        return [dict(r) for r in cur.fetchall()]

    def close(self) -> None:
        self._conn.close()
