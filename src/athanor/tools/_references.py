"""CHGNet elemental reference energies for formation-energy estimates.

Computed once per element by relaxing the element's most stable Materials
Project structure with CHGNet, then cached to disk together with where the
structure came from. Consistent with using CHGNet total energies for
compounds (same level of theory on both sides).

Cache history: until 2026-10 the cache (data/elemental_refs.json, bare
floats) was filled by a lookup that silently fell back to a 4-atom FCC cell
whenever the MP query failed. S, Se and Te were cached that way, 1.26, 0.69
and 0.33 eV/atom above their real CHGNet ground states (Ga 0.04), which made
every chalcogenide formation energy too negative. Formation energy is reported but
is not part of the hit rule. The cache now lives in elemental_refs.v2.json
with a source per element, and an MP failure raises instead of guessing.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

_CACHE = Path("data/elemental_refs.v2.json")
_memory: dict[str, dict] = {}

log = logging.getLogger("athanor.references")


def elemental_reference_energy(symbol: str) -> float:
    """CHGNet energy per atom of the element's ground-state structure (eV/atom)."""
    if not _memory and _CACHE.exists():
        _memory.update(json.loads(_CACHE.read_text()))
    if symbol in _memory:
        return _memory[symbol]["e"]

    structure, source = _elemental_structure(symbol)
    from athanor.tools.scoring import _chgnet, relax_structure

    relaxed, _converged = relax_structure(structure, max_steps=100)
    e = float(_chgnet().predict_structure(relaxed)["e"])

    _memory[symbol] = {"e": e, "source": source}
    _CACHE.parent.mkdir(parents=True, exist_ok=True)
    _CACHE.write_text(json.dumps(_memory, indent=0))
    return e


def _elemental_structure(symbol: str):
    """(structure, source) for the element's ground state.

    With MP_API_KEY set, the most stable Materials Project polymorph; an MP
    error raises (scoring records it as a failed evaluation) rather than
    silently substituting a made-up cell. Without a key — the documented
    offline mode — a simple FCC cell, crude but consistent for ranking.
    """
    if os.environ.get("MP_API_KEY"):
        from mp_api.client import MPRester

        with MPRester(os.environ["MP_API_KEY"]) as mpr:
            docs = mpr.materials.summary.search(
                chemsys=symbol, is_stable=True, fields=["material_id"]
            )
            if docs:
                mid = str(docs[0].material_id)
                return mpr.get_structure_by_material_id(mid), mid
        log.warning("MP lists no stable %s polymorph; using an FCC cell", symbol)

    from pymatgen.core import Lattice, Structure

    return (Structure(Lattice.cubic(4.0), [symbol] * 4,
                      [[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]]),
            "fcc-fallback")
