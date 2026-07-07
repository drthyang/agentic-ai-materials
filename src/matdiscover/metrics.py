"""Campaign metrics (Phase 3): the numbers that decide agent vs baseline.

A "hit" is the mission's definition of success, computed identically for
every strategy: scored + converged + gap inside the target window +
near-stable + not a confirmed-known material.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from pymatgen.core import Composition

from matdiscover.config import MissionConfig
from matdiscover.db import CandidateDB


@dataclass
class CampaignMetrics:
    name: str
    proposed: int = 0
    filtered_out: int = 0
    scored: int = 0
    errors: int = 0
    hits: int = 0
    hit_formulas: list[str] = field(default_factory=list)
    rediscoveries: list[str] = field(default_factory=list)
    hits_per_100_relaxations: float = 0.0
    best_gap_distance_ev: float | None = None  # |gap - ideal| of best candidate

    def as_row(self) -> dict:
        return {
            "strategy": self.name,
            "scored": self.scored,
            "hits": self.hits,
            "hits/100 relax": round(self.hits_per_100_relaxations, 2),
            "rediscoveries": len(self.rediscoveries),
            "best |gap-ideal| (eV)": self.best_gap_distance_ev,
        }


def compute_metrics(name: str, db: CandidateDB, cfg: MissionConfig) -> CampaignMetrics:
    m = CampaignMetrics(name=name)
    lo, hi = cfg.target.band_gap_ev
    ideal = cfg.target.band_gap_ideal_ev
    hull_max = cfg.target.e_above_hull_max_ev_per_atom
    holdout = {Composition(f).reduced_formula for f in cfg.evaluation.holdout_formulas}

    cur = db._conn.execute("SELECT * FROM candidates")
    rows = [dict(r) for r in cur.fetchall()]

    gap_distances = []
    for r in rows:
        if r["status"] == "filtered_out":
            m.filtered_out += 1
            continue
        if r["status"] == "proposed":
            m.proposed += 1
            continue
        if r["status"] == "error":
            m.errors += 1
            continue
        if r["status"] != "scored":
            continue
        m.scored += 1
        if not r["converged"]:
            continue
        gap = r["band_gap_ev"]
        hull = r["e_above_hull"]
        if gap is not None:
            gap_distances.append(abs(gap - ideal))
        on_target = gap is not None and lo <= gap <= hi
        near_stable = hull is not None and hull <= hull_max
        not_known = r["is_novel"] != 0  # 1 or NULL(unknown) both count
        if on_target and near_stable and not_known:
            m.hits += 1
            m.hit_formulas.append(r["formula"])
        reduced = Composition(r["formula"]).reduced_formula
        if reduced in holdout and on_target:
            m.rediscoveries.append(r["formula"])

    total_relax = m.scored + m.errors
    m.hits_per_100_relaxations = 100.0 * m.hits / total_relax if total_relax else 0.0
    m.best_gap_distance_ev = round(min(gap_distances), 3) if gap_distances else None
    return m


def comparison_table(metrics: list[CampaignMetrics]) -> str:
    """Markdown comparison table."""
    if not metrics:
        return "(no campaigns)"
    cols = list(metrics[0].as_row().keys())
    lines = ["| " + " | ".join(cols) + " |",
             "|" + "|".join("---" for _ in cols) + "|"]
    for m in metrics:
        row = m.as_row()
        lines.append("| " + " | ".join(str(row[c]) for c in cols) + " |")
    return "\n".join(lines)
