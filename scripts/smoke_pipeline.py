"""Phase 1 milestone: hand-chained pipeline, no agent.

Generates substitutions of the chalcopyrite CuInSe2 prototype, filters them,
relaxes + scores a few with CHGNet/MEGNet, and prints a results table.

Works without MP_API_KEY (novelty + hull checks are skipped); with a key set
you get the full pipeline. First run downloads CHGNet/MEGNet weights.

Usage: uv run python scripts/smoke_pipeline.py [--max-score N]
"""

from __future__ import annotations

import argparse
import os

from pymatgen.core import Lattice, Structure

from athanor.config import load_mission
from athanor.tools.candidates import substitute_prototype
from athanor.tools.filters import filter_candidates
from athanor.tools.scoring import relax_and_score


def chalcopyrite_prototype() -> Structure:
    """Idealized chalcopyrite CuInSe2 (I-42d), 8 atoms/cell."""
    lattice = Lattice.tetragonal(5.78, 11.62)
    species = ["Cu", "Cu", "In", "In", "Se", "Se", "Se", "Se"]
    coords = [
        [0.0, 0.0, 0.0], [0.0, 0.5, 0.25],
        [0.5, 0.5, 0.0], [0.5, 0.0, 0.25],
        [0.25, 0.25, 0.125], [0.75, 0.75, 0.125],
        [0.75, 0.25, 0.875], [0.25, 0.75, 0.875],
    ]
    return Structure(lattice, species, coords)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-score", type=int, default=3,
                        help="how many candidates to relax+score (default 3)")
    args = parser.parse_args()

    cfg = load_mission("config/mission.yaml")
    proto = chalcopyrite_prototype()
    has_mp_key = bool(os.environ.get("MP_API_KEY"))

    print(f"Mission: {cfg.mission.name}")
    print(f"MP_API_KEY set: {has_mp_key} "
          f"({'full pipeline' if has_mp_key else 'novelty/hull checks skipped'})\n")

    # 1. Generate: substitute on the chalcopyrite I-III-VI2 family
    candidates = substitute_prototype(
        proto,
        "chalcopyrite-CuInSe2",
        substitutions={
            "Cu": ["Cu", "Ag"],
            "In": ["In", "Ga", "Al"],
            "Se": ["Se", "S", "Te"],
        },
        cfg=cfg,
    )
    print(f"Generated {len(candidates)} candidate structures "
          f"(unique formulas, identity excluded)")

    # 2. Filter: SMACT + mission chemistry
    results = filter_candidates([c.formula for c in candidates], cfg)
    passed = [c for c, r in zip(candidates, results) if r.passed]
    for c, r in zip(candidates, results):
        mark = "PASS" if r.passed else f"FAIL ({'; '.join(r.reasons)})"
        print(f"  {c.formula:16s} {mark}")
    print(f"\n{len(passed)}/{len(candidates)} passed cheap filters")

    # 3. Novelty check (needs MP key)
    if has_mp_key:
        from athanor.tools.mp_search import is_novel
        for c in passed:
            c_novel = is_novel(c.formula)
            print(f"  {c.formula:16s} novel vs MP: {c_novel}")

    # 4. Relax + score the first few
    to_score = passed[: args.max_score]
    print(f"\nRelaxing + scoring {len(to_score)} candidates with CHGNet/MEGNet "
          f"(first run downloads model weights)...\n")
    print(f"{'formula':16s} {'conv':5s} {'E_form (eV/at)':>15s} "
          f"{'E_hull (eV/at)':>15s} {'gap (eV)':>9s} {'dV %':>6s}")
    for c in to_score:
        s = relax_and_score(c.structure,
                            max_steps=cfg.budget.relaxation_max_steps,
                            with_hull=has_mp_key)
        if s.error:
            print(f"{s.formula:16s} ERROR: {s.error}")
            continue
        hull = f"{s.e_above_hull:15.3f}" if s.e_above_hull is not None else f"{'—':>15s}"
        print(f"{s.formula:16s} {str(s.converged):5s} "
              f"{s.formation_energy_per_atom:15.3f} {hull} "
              f"{s.band_gap_ev:9.2f} {s.volume_change_pct:6.1f}")

    print("\nSmoke pipeline complete.")


if __name__ == "__main__":
    main()
