"""Prototype cells must be the crystals their names claim.

Until 2026-10 the chalcopyrite and kesterite prototypes were 8-atom
half-cells with P2 symmetry and a ~7 Å empty slab; every candidate built on
them was relaxed from a structure nobody intended, and most benchmark hits
turned out to depend on it (results/2026-10-10-claude-ablation/). These
tests pin what a prototype is, so the defect cannot come back silently.
"""

from __future__ import annotations

import numpy as np
import pytest
from pymatgen.core import Composition
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

from athanor.prototypes import PROTOTYPES, get_prototype

EXPECTED = {
    # name: (space group symbol, number, atoms, reduced formula)
    "chalcopyrite-CuInSe2": ("I-42d", 122, 16, "CuInSe2"),
    "kesterite-Cu2ZnSnS4": ("I-4", 82, 16, "Cu2ZnSnS4"),
    "zincblende-GaAs": ("F-43m", 216, 8, "GaAs"),
}


def test_every_prototype_is_covered():
    assert set(PROTOTYPES) == set(EXPECTED)


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_space_group_atoms_and_stoichiometry(name):
    symbol, number, natoms, formula = EXPECTED[name]
    s = get_prototype(name)
    sga = SpacegroupAnalyzer(s, symprec=0.01)
    assert sga.get_space_group_symbol() == symbol
    assert sga.get_space_group_number() == number
    assert len(s) == natoms
    assert s.composition.reduced_composition == Composition(formula).reduced_composition


def _largest_empty_slab(s) -> float:
    """Widest atom-free slab (Å) perpendicular to any lattice vector."""
    widest = 0.0
    for axis, hkl in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
        f = np.sort(np.mod(s.frac_coords[:, axis], 1.0))
        gaps = np.diff(np.append(f, f[0] + 1.0))
        widest = max(widest, gaps.max() * s.lattice.d_hkl(hkl))
    return widest


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_no_vacuum_gap(name):
    # tetrahedral semiconductors stack atomic planes ~1.4-1.6 Å apart; the
    # old half-cells had a 7.3 Å empty slab
    assert _largest_empty_slab(get_prototype(name)) < 2.0


@pytest.mark.parametrize("name", sorted(EXPECTED))
def test_every_atom_is_tetrahedrally_coordinated(name):
    s = get_prototype(name)
    for i, site in enumerate(s):
        neighbours = s.get_neighbors(site, 2.9)
        assert len(neighbours) == 4, (name, i, site.specie, len(neighbours))
        # bonds join cations to anions only
        anion = site.specie.symbol in {"Se", "S", "As"}
        assert all((n.specie.symbol in {"Se", "S", "As"}) != anion for n in neighbours)


@pytest.mark.parametrize("name,mapping,symbol", [
    ("chalcopyrite-CuInSe2", {"Cu": "Ag", "In": "Ga"}, "I-42d"),
    ("chalcopyrite-CuInSe2", {"Se": "S"}, "I-42d"),
    ("kesterite-Cu2ZnSnS4", {"Cu": "Ag", "Zn": "Cd", "Sn": "Ge", "S": "Se"}, "I-4"),
    ("zincblende-GaAs", {"Ga": "Al", "As": "Sb"}, "F-43m"),
])
def test_one_to_one_substitution_keeps_the_space_group(name, mapping, symbol):
    s = get_prototype(name).copy()
    s.replace_species(mapping)
    assert SpacegroupAnalyzer(s, symprec=0.01).get_space_group_symbol() == symbol


def test_prototypes_are_fresh_objects():
    a, b = get_prototype("kesterite-Cu2ZnSnS4"), get_prototype("kesterite-Cu2ZnSnS4")
    a.replace_species({"Cu": "Ag"})
    assert "Cu" in {sp.symbol for sp in b.species}
