"""Materials Project queries: known-materials search and novelty checks.

Requires MP_API_KEY in the environment. All results are cached on disk so
repeated campaign runs don't re-hit the API.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

from pymatgen.core import Composition

_CACHE_DIR = Path("data/mp_cache")


@dataclass
class KnownMaterial:
    material_id: str
    formula: str
    band_gap: float | None
    energy_above_hull: float | None
    is_stable: bool | None


def _require_key() -> str:
    key = os.environ.get("MP_API_KEY", "")
    if not key:
        raise RuntimeError(
            "MP_API_KEY is not set. Get a free key at https://materialsproject.org/api "
            "and export MP_API_KEY=<key>."
        )
    return key


def _cache_path(kind: str, key: str) -> Path:
    safe = key.replace("/", "_").replace(" ", "")
    return _CACHE_DIR / f"{kind}__{safe}.json"


def search_known_materials(
    chemsys_or_formula: str,
    use_cache: bool = True,
) -> list[KnownMaterial]:
    """Query MP by chemical system ('Cu-In-Se') or formula ('CuInSe2')."""
    cache = _cache_path("search", chemsys_or_formula)
    if use_cache and cache.exists():
        rows = json.loads(cache.read_text())
        return [KnownMaterial(**r) for r in rows]

    from mp_api.client import MPRester

    is_chemsys = "-" in chemsys_or_formula
    with MPRester(_require_key()) as mpr:
        docs = mpr.materials.summary.search(
            chemsys=chemsys_or_formula if is_chemsys else None,
            formula=None if is_chemsys else chemsys_or_formula,
            fields=["material_id", "formula_pretty", "band_gap", "energy_above_hull", "is_stable"],
        )
    results = [
        KnownMaterial(
            material_id=str(d.material_id),
            formula=d.formula_pretty,
            band_gap=d.band_gap,
            energy_above_hull=d.energy_above_hull,
            is_stable=d.is_stable,
        )
        for d in docs
    ]
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps([r.__dict__ for r in results]))
    return results


def is_novel(formula: str, use_cache: bool = True) -> bool:
    """True if no MP entry has this reduced formula (i.e. worth pursuing as 'new')."""
    reduced = Composition(formula).reduced_formula
    return len(search_known_materials(reduced, use_cache=use_cache)) == 0


def get_structure_by_id(material_id: str):
    """Fetch a relaxed structure from MP (e.g. the prototype to substitute on)."""
    from mp_api.client import MPRester

    with MPRester(_require_key()) as mpr:
        return mpr.get_structure_by_material_id(material_id)
