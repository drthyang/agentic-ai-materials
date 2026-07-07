"""CHGNet elemental reference energies for formation-energy estimates.

Computed once per element by relaxing the pymatgen elemental ground-state
structure with CHGNet, then cached to disk. Consistent with using CHGNet
total energies for compounds (same level of theory on both sides).
"""

from __future__ import annotations

import json
from pathlib import Path

_CACHE = Path("data/elemental_refs.json")
_memory: dict[str, float] = {}


def elemental_reference_energy(symbol: str) -> float:
    """CHGNet energy per atom of the element's ground-state structure (eV/atom)."""
    if not _memory and _CACHE.exists():
        _memory.update(json.loads(_CACHE.read_text()))
    if symbol in _memory:
        return _memory[symbol]

    structure = _elemental_structure(symbol)
    from matdiscover.tools.scoring import _chgnet, relax_structure

    relaxed, _converged = relax_structure(structure, max_steps=100)
    e = float(_chgnet().predict_structure(relaxed)["e"])

    _memory[symbol] = e
    _CACHE.parent.mkdir(parents=True, exist_ok=True)
    _CACHE.write_text(json.dumps(_memory, indent=0))
    return e


def _elemental_structure(symbol: str):
    """Best-effort elemental ground-state structure.

    Prefers Materials Project (most stable polymorph) when a key is set;
    falls back to a simple FCC cell, which is crude but consistent enough
    for ranking candidates against each other.
    """
    import os

    if os.environ.get("MP_API_KEY"):
        try:
            from mp_api.client import MPRester

            with MPRester(os.environ["MP_API_KEY"]) as mpr:
                docs = mpr.materials.summary.search(
                    chemsys=symbol, is_stable=True, fields=["material_id"]
                )
                if docs:
                    return mpr.get_structure_by_material_id(str(docs[0].material_id))
        except Exception:
            pass

    from pymatgen.core import Lattice, Structure

    return Structure(Lattice.cubic(4.0), [symbol] * 4,
                     [[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]])
