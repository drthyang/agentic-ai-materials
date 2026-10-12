"""Re-score every recorded candidate with the corrected pipeline (no API cost).

    uv run python scripts/rescore_runs.py results/<study>/arms-pv.json [more specs...]

Two scoring defects were found in 2026-10: the chalcopyrite and kesterite
prototypes were 8-atom half-cells (fixed in 2aa21eb), and the convex hull was
built from Materials Project's uncorrected energies while CHGNet predicts on
the MP2020-corrected scale (fixed in edc49f9). The runs' *choices* are on
record; this script re-scores them so each defect's effect is visible on its
own.

1. **Hull scale only (no relaxation).** Each scored row's CHGNet total energy
   is reconstructed from its stored formation energy and the elemental
   reference energies (data/elemental_refs.json, frozen into
   ``elemental-refs-as-used.json``). The reconstruction is validated by
   reproducing the stored e_above_hull on the old uncorrected scale, then the
   hull distance is recomputed on the corrected scale — same cell the run
   relaxed.
2. **Correct cell and corrected hull.** Every distinct (formula, prototype,
   substitution) is rebuilt in today's prototypes and scored by today's
   ``relax_and_score``. Results are cached in ``rescore-candidates.csv``, so
   an interrupted run resumes.

Writes, next to the first spec: rescore-rows.csv (one line per scored row in
every run) and rescore-candidates.csv. aggregate_ablation.py picks
rescore-rows.csv up and reports hits under each correction.

The counterfactual is limited: an agent's later iterations reacted to the
defective scores it was shown, so "what this run's choices score correctly"
is not "what a run with correct scoring would have chosen". Only a rerun
answers that.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from pymatgen.core import Composition

from athanor.config import load_mission
from athanor.db import CandidateDB
from athanor.prototypes import get_prototype
from athanor.tools.scoring import hull_distance, hull_entries, relax_and_score

REFS = Path("data/elemental_refs.json")
CAND_FIELDS = ["formula", "prototype", "substitution", "natoms", "converged",
               "band_gap_ev", "e_above_hull", "formation_energy_per_atom", "error"]


def canonical_sub(sub_json: str | None) -> str:
    return json.dumps(json.loads(sub_json or "{}"), sort_keys=True)


def reconstruct_e_total(formula: str, e_form: float, refs: dict) -> tuple[Composition, float]:
    """Total CHGNet energy (eV) of one reduced formula unit."""
    comp = Composition(formula).reduced_composition
    n = comp.num_atoms
    e_ref = sum(refs[el.symbol] * amt for el, amt in comp.items())
    return comp, e_form * n + e_ref


def load_candidates(path: Path) -> dict[tuple, dict]:
    if not path.exists():
        return {}
    with open(path, newline="") as f:
        return {(r["formula"], r["prototype"], r["substitution"]): r for r in csv.DictReader(f)}


def score_candidate(formula: str, prototype: str, sub: str) -> dict:
    s = get_prototype(prototype).copy()
    s.replace_species({k: v for k, v in json.loads(sub).items() if k != v})
    r = relax_and_score(s)
    return {"formula": formula, "prototype": prototype, "substitution": sub,
            "natoms": len(s), "converged": r.converged, "band_gap_ev": r.band_gap_ev,
            "e_above_hull": r.e_above_hull,
            "formation_energy_per_atom": r.formation_energy_per_atom, "error": r.error}


def main(specs: list[str]) -> None:
    outdir = Path(specs[0]).parent
    refs = json.loads(REFS.read_text())
    (outdir / "elemental-refs-as-used.json").write_text(json.dumps(refs, indent=1))

    rows = []
    for spec_path in specs:
        spec = json.loads(Path(spec_path).read_text())
        cfg = load_mission(spec.get("mission", "config/mission.yaml"))
        for arm, a in spec["arms"].items():
            for run in a["runs"]:
                db = CandidateDB(Path(run) / a["db"])
                for r in db._conn.execute("SELECT * FROM candidates WHERE status IN ('scored','error')"):
                    r = dict(r)
                    row = {"mission": cfg.mission.name, "arm": arm, "run": Path(run).name,
                           "db": a["db"], "id": r["id"], "status": r["status"],
                           "formula": Composition(r["formula"]).reduced_formula,
                           "prototype": r["parent_prototype"],
                           "substitution": canonical_sub(r["substitution"]),
                           "is_novel": r["is_novel"], "converged": r["converged"],
                           "band_gap_ev": r["band_gap_ev"], "e_above_hull": r["e_above_hull"],
                           "hull_old_recon": None, "hull_corrected_same_cell": None}
                    ef = r["formation_energy_per_atom"]
                    if r["status"] == "scored" and ef is not None:
                        comp, e_tot = reconstruct_e_total(r["formula"], ef, refs)
                        chemsys = "-".join(sorted(el.symbol for el in comp.elements))
                        entries = hull_entries(chemsys)
                        row["hull_old_recon"] = hull_distance(entries, comp, e_tot, corrected=False)
                        row["hull_corrected_same_cell"] = hull_distance(entries, comp, e_tot)
                    rows.append(row)
                db.close()
        print(f"{spec_path}: {len(rows)} rows so far", flush=True)

    # part 2: correct cells, corrected hull, one relaxation per distinct route
    cand_path = outdir / "rescore-candidates.csv"
    done = load_candidates(cand_path)
    todo = sorted({(r["formula"], r["prototype"], r["substitution"]) for r in rows} - set(done))
    print(f"{len(done)} candidates cached, {len(todo)} to relax", flush=True)
    new = not cand_path.exists()
    with open(cand_path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CAND_FIELDS)
        if new:
            w.writeheader()
        for i, key in enumerate(todo, 1):
            c = score_candidate(*key)
            w.writerow(c)
            f.flush()
            done[key] = {k: str(v) if v is not None else "" for k, v in c.items()}
            if i % 50 == 0:
                print(f"  relaxed {i}/{len(todo)}", flush=True)

    for r in rows:
        c = done[(r["formula"], r["prototype"], r["substitution"])]
        r["cellfix_converged"] = c["converged"]
        r["cellfix_band_gap_ev"] = c["band_gap_ev"]
        r["cellfix_e_above_hull"] = c["e_above_hull"]
        r["cellfix_error"] = c["error"]
    with open(outdir / "rescore-rows.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    # validation of the energy reconstruction against what the runs stored
    checked = [r for r in rows if r["hull_old_recon"] is not None and r["e_above_hull"] is not None]
    match = sum(abs(r["hull_old_recon"] - r["e_above_hull"]) < 2e-3 for r in checked)
    print(f"reconstruction reproduces the stored (old-scale) hull for {match}/{len(checked)} rows")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
