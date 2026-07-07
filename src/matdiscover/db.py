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
        """Best scored candidates: novel, converged, sorted by hull distance."""
        cur = self._conn.execute(
            """SELECT * FROM candidates
               WHERE status = 'scored' AND converged = 1 AND is_novel = 1
               ORDER BY e_above_hull ASC NULLS LAST LIMIT ?""",
            (limit,),
        )
        return [dict(r) for r in cur.fetchall()]

    def iteration_summary(self, iteration: int) -> dict:
        cur = self._conn.execute(
            """SELECT status, COUNT(*) n FROM candidates
               WHERE iteration = ? GROUP BY status""",
            (iteration,),
        )
        return {r["status"]: r["n"] for r in cur.fetchall()}

    def close(self) -> None:
        self._conn.close()
