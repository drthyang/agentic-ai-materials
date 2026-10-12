"""Physics-grounded scoring: CHGNet relaxation, hull stability, MEGNet band gap.

Model loading is lazy and cached at module level — CHGNet/MEGNet weights
download on first use (~100 MB total) and take seconds to load.
"""

from __future__ import annotations

import json
import warnings
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from pymatgen.core import Structure


@dataclass
class ScoreResult:
    formula: str
    converged: bool
    formation_energy_per_atom: float | None = None
    e_above_hull: float | None = None
    band_gap_ev: float | None = None
    volume_change_pct: float | None = None
    error: str | None = None


@lru_cache(maxsize=1)
def _chgnet():
    from chgnet.model import CHGNet

    return CHGNet.load()


@lru_cache(maxsize=1)
def _relaxer():
    from chgnet.model import StructOptimizer

    return StructOptimizer()


@lru_cache(maxsize=1)
def _bandgap_model():
    import matgl

    return matgl.load_model("MEGNet-BandGap-mfi-MP-2019.4.1")


def relax_structure(structure: Structure, max_steps: int = 200) -> tuple[Structure, bool]:
    """CHGNet relaxation. Returns (relaxed structure, converged)."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        result = _relaxer().relax(structure, steps=max_steps, verbose=False)
    relaxed = result["final_structure"]
    # StructOptimizer uses FIRE; treat hitting the step cap as non-converged.
    n_steps = len(result["trajectory"].energies)
    return relaxed, n_steps < max_steps


def formation_energy_per_atom(structure: Structure) -> float:
    """Formation energy per atom from CHGNet total energy vs elemental references.

    Uses MP-compatible elemental reference energies shipped with pymatgen via
    the patched entry pipeline below (see e_above_hull), but for a quick score
    we approximate with CHGNet energies of elemental ground states, cached.
    """
    from athanor.tools._references import elemental_reference_energy

    e_total = _chgnet().predict_structure(structure)["e"] * len(structure)
    comp = structure.composition
    e_refs = sum(
        elemental_reference_energy(el.symbol) * amt for el, amt in comp.items()
    )
    return (e_total - e_refs) / len(structure)


_HULL_CACHE = Path("data/mp_cache/hull")


def hull_entries(chemsys: str, use_cache: bool = True) -> list[dict]:
    """Materials Project GGA/GGA+U entries for a chemical system, as plain rows.

    Each row keeps both energy scales: ``energy`` (MP2020-corrected, what
    the hull must use) and ``uncorrected_energy`` (raw GGA/GGA+U, kept only
    so values computed before the 2026-10 fix can be reproduced). Cached on
    disk per chemical system, so a campaign or a re-score sees one frozen
    snapshot of MP instead of re-querying it for every candidate.
    """
    cache = _HULL_CACHE / f"{chemsys}.json"
    if use_cache and cache.exists():
        return json.loads(cache.read_text())

    from mp_api.client import MPRester

    from athanor.tools.mp_search import _require_key

    with MPRester(_require_key()) as mpr:
        # Pin to the GGA/GGA+U hull: MP's default mixed hull includes r2SCAN
        # entries whose absolute energy scale differs by eV/atom.
        entries = mpr.get_entries_in_chemsys(
            chemsys, additional_criteria={"thermo_types": ["GGA_GGA+U"]}
        )
    rows = [{"entry_id": str(e.entry_id), "formula": e.composition.formula,
             "energy": float(e.energy), "uncorrected_energy": float(e.uncorrected_energy)}
            for e in entries]
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(rows, indent=0))
    return rows


def hull_distance(rows: list[dict], composition, e_total: float,
                  corrected: bool = True) -> float | None:
    """Energy above the hull (eV/atom) of a candidate with total energy
    ``e_total`` (eV) against MP rows from :func:`hull_entries`.

    CHGNet is trained on MPtrj energies that carry MP2020 compatibility
    corrections, so the hull must be built from MP's *corrected* energies.
    Until 2026-10 it used the uncorrected ones, which made every oxide,
    chalcogenide, halide and nitride candidate look 0.1-0.35 eV/atom more
    stable than it is (zinc-blende CaO, MgO and KCl came out on the hull).
    ``corrected=False`` reproduces that old behaviour and exists only for
    re-scoring recorded runs.
    """
    from pymatgen.analysis.phase_diagram import PDEntry, PhaseDiagram
    from pymatgen.core import Composition

    if not rows:
        return None
    key = "energy" if corrected else "uncorrected_energy"
    candidate = PDEntry(Composition(composition), e_total)
    pd = PhaseDiagram([PDEntry(Composition(r["formula"]), r[key]) for r in rows]
                      + [candidate])
    return float(pd.get_e_above_hull(candidate))


def e_above_hull(structure: Structure, use_cache: bool = True) -> float | None:
    """Energy above the MP convex hull (eV/atom) for the relaxed structure.

    Builds a phase diagram from MP entries in the candidate's chemical system
    (MP2020-corrected scale, matching CHGNet) plus the CHGNet-scored
    candidate itself. Requires MP_API_KEY; returns None if unavailable.
    """
    import os

    if not os.environ.get("MP_API_KEY"):
        return None
    chemsys = "-".join(sorted(el.symbol for el in structure.composition.elements))
    rows = hull_entries(chemsys, use_cache=use_cache)
    e_total = _chgnet().predict_structure(structure)["e"] * len(structure)
    return hull_distance(rows, structure.composition, e_total)


# Multi-fidelity MEGNet state indices, verified against Si reference gaps
# (PBE 0.61, GLLB-SC ~1.2, HSE 1.17, SCAN ~0.8 eV).
FIDELITY = {"PBE": 0, "GLLB-SC": 1, "HSE": 2, "SCAN": 3}


def predict_band_gap(structure: Structure, fidelity: str = "HSE") -> float:
    """MEGNet multi-fidelity band gap prediction (eV).

    Defaults to HSE fidelity: PBE systematically collapses gaps of the
    chalcogenide semiconductors this mission targets, while HSE tracks
    experiment closely enough for screening.
    """
    import torch

    model = _bandgap_model()
    with torch.no_grad():
        gap = model.predict_structure(
            structure, state_attr=torch.tensor([FIDELITY[fidelity]])
        )
    return float(gap)


def relax_and_score(
    structure: Structure,
    max_steps: int = 200,
    with_hull: bool = True,
) -> ScoreResult:
    """Full evaluation pipeline for one candidate structure."""
    formula = structure.composition.reduced_formula
    try:
        v0 = structure.volume
        relaxed, converged = relax_structure(structure, max_steps=max_steps)
        result = ScoreResult(
            formula=formula,
            converged=converged,
            formation_energy_per_atom=formation_energy_per_atom(relaxed),
            band_gap_ev=predict_band_gap(relaxed),
            volume_change_pct=100.0 * (relaxed.volume - v0) / v0,
        )
        if with_hull:
            result.e_above_hull = e_above_hull(relaxed)
        return result
    except Exception as exc:  # scoring must never crash a campaign
        return ScoreResult(formula=formula, converged=False, error=str(exc))
