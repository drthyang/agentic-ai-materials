"""Re-score benchmark hits in proper bulk cells of their prototype (no API cost).

    uv run python scripts/structure_audit.py results/<study>/arms-pv.json [...]

Why: until the 2026-10-12 fix, the chalcopyrite and kesterite prototypes were
8-atom cells that hold half of the 16-atom conventional cell's atoms in the
full c = 11.6 Å box — all atoms sit within z in [-0.125, 0.25], leaving a
~7 Å empty gap — and their symmetry is P2, not I-42d / I-4. Every
chalcopyrite- or kesterite-derived candidate in every strategy (agent and
baselines alike) was relaxed from that starting geometry.

This audit takes each distinct hit composition, applies the same element
substitution to a correct 16-atom conventional cell of the same structure
type (built from the space group), starts it at a predicted volume, and
scores it with the unchanged pipeline (`relax_and_score`: CHGNet, MP hull,
MEGNet HSE gap, 200 steps). A hit that stays a hit is robust to the
prototype defect; one that does not was produced by it. Zinc-blende hits
are re-scored too as a control (that prototype is a correct cell).

Writes structure-audit.csv next to the first spec and prints a summary.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from pymatgen.core import Composition, Structure

from athanor.config import load_mission
from athanor.db import CandidateDB
from athanor.metrics import row_flags
from athanor.prototypes import get_prototype
from athanor.tools.scoring import relax_and_score


def bulk_cell(prototype: str) -> Structure:
    """Correct conventional cell for a prototype name.

    Since the 2026-10-12 fix these are exactly the cells in prototypes.py
    (site for site), so auditing runs made after the fix re-scores the same
    structure from a different starting volume; for runs made before it,
    this is the correct cell the defective 8-atom prototype should have been.
    """
    return get_prototype(prototype).copy()


def build(prototype: str, substitution: dict) -> Structure:
    s = bulk_cell(prototype)
    s.replace_species({k: v for k, v in substitution.items() if k != v})
    try:  # start near a sensible volume, as the 8-atom route effectively did
        from pymatgen.analysis.structure_prediction.volume_predictor import (
            DLSVolumePredictor,
        )
        s = DLSVolumePredictor().get_predicted_structure(s)
    except Exception:
        pass
    return s


def distinct_hits(spec_path: Path) -> tuple[list[dict], object]:
    spec = json.loads(spec_path.read_text())
    cfg = load_mission(spec.get("mission", "config/mission.yaml"))
    seen: dict[str, dict] = {}
    for arm, a in spec["arms"].items():
        kind = "agent" if a["db"] == "agent.db" else "baseline"
        for run in a["runs"]:
            db = CandidateDB(Path(run) / a["db"])
            for r in db._conn.execute("SELECT * FROM candidates WHERE status='scored'"):
                r = dict(r)
                if not row_flags(r, cfg)["hit"]:
                    continue
                red = Composition(r["formula"]).reduced_formula
                h = seen.setdefault(red, {**r, "formula": red, "kinds": set()})
                h["kinds"].add(kind)
            db.close()
    return sorted(seen.values(), key=lambda h: h["formula"]), cfg


def main(specs: list[str]) -> None:
    rows = []
    for spec in specs:
        hits, cfg = distinct_hits(Path(spec))
        for h in hits:
            s = build(h["parent_prototype"], json.loads(h["substitution"] or "{}"))
            r = relax_and_score(s, max_steps=cfg.budget.relaxation_max_steps)
            row = {"status": "scored" if not r.error else "error",
                   "converged": r.converged, "band_gap_ev": r.band_gap_ev,
                   "e_above_hull": r.e_above_hull, "is_novel": h["is_novel"],
                   "formula": h["formula"]}
            still = row_flags(row, cfg)["hit"] if not r.error else False
            rows.append({
                "mission": cfg.mission.name, "formula": h["formula"],
                "found_by": "+".join(sorted(h["kinds"])), "prototype": h["parent_prototype"],
                "gap_8atom": round(h["band_gap_ev"], 2), "hull_8atom": round(h["e_above_hull"], 3),
                "natoms_bulk": len(s), "converged_bulk": r.converged,
                "gap_bulk": None if r.band_gap_ev is None else round(r.band_gap_ev, 2),
                "hull_bulk": None if r.e_above_hull is None else round(r.e_above_hull, 3),
                "still_hit": still, "error": r.error,
            })
            print(f"{cfg.mission.name:<16} {h['formula']:<14} {h['parent_prototype']:<22} "
                  f"8-atom gap {h['band_gap_ev']:.2f} hull {h['e_above_hull']:.3f} | "
                  f"bulk gap {rows[-1]['gap_bulk']} hull {rows[-1]['hull_bulk']} "
                  f"conv {r.converged} -> {'HIT' if still else 'no'}", flush=True)
    out = Path(specs[0]).parent / "structure-audit.csv"
    with open(out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    groups: dict[tuple, list] = {}
    for r in rows:
        for who in ("agent", "baseline"):
            if who in r["found_by"]:
                groups.setdefault((r["mission"], who, r["prototype"]), []).append(r)
    print("\n| mission | found by | prototype | distinct hits | still hits in bulk cell |")
    print("|---|---|---|---|---|")
    for (m, who, p), rs in sorted(groups.items()):
        print(f"| {m} | {who} | {p} | {len(rs)} | {sum(r['still_hit'] for r in rs)} |")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
