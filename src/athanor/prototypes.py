"""Built-in prototype structures the agent can substitute on.

Idealized conventional cells built from their space groups — CHGNet
relaxation fixes the geometry, so approximate lattice parameters and
Wyckoff coordinates are fine as starting points. What is NOT fine is the
wrong structure: until 2026-10 the chalcopyrite and kesterite entries were
8-atom half-cells (P2 symmetry, a ~7 Å empty slab along c), and every
candidate built on them was relaxed from that start. tests/test_prototypes.py
now pins each prototype's space group, stoichiometry, coordination, and the
absence of any vacuum gap.
"""

from __future__ import annotations

from pymatgen.core import Lattice, Structure


def chalcopyrite_cuinse2() -> Structure:
    """Chalcopyrite CuInSe2 (I-42d, No. 122), 16-atom conventional cell.

    Cu 4a (0,0,0), In 4b (0,0,1/2), Se 8d (u,1/4,1/8) with u = 0.23.
    I-III-VI2 family parent.
    """
    return Structure.from_spacegroup(
        "I-42d", Lattice.tetragonal(5.78, 11.62), ["Cu", "In", "Se"],
        [[0.0, 0.0, 0.0], [0.0, 0.0, 0.5], [0.23, 0.25, 0.125]],
    )


def kesterite_cu2znsns4() -> Structure:
    """Kesterite Cu2ZnSnS4 (I-4, No. 82), 16-atom conventional cell.

    Cu 2a (0,0,0) and 2c (0,1/2,1/4), Zn 2d (0,1/2,3/4), Sn 2b (0,0,1/2),
    S 8g (0.756, 0.757, 0.872). I2-II-IV-VI4 family parent.
    """
    return Structure.from_spacegroup(
        "I-4", Lattice.tetragonal(5.43, 10.86), ["Cu", "Cu", "Zn", "Sn", "S"],
        [[0.0, 0.0, 0.0], [0.0, 0.5, 0.25], [0.0, 0.5, 0.75], [0.0, 0.0, 0.5],
         [0.756, 0.757, 0.872]],
    )


def zincblende_gaas() -> Structure:
    """Zinc blende GaAs (F-43m), 8-atom conventional cell. III-V family parent."""
    lattice = Lattice.cubic(5.65)
    species = ["Ga", "Ga", "Ga", "Ga", "As", "As", "As", "As"]
    coords = [
        [0.0, 0.0, 0.0], [0.5, 0.5, 0.0], [0.5, 0.0, 0.5], [0.0, 0.5, 0.5],
        [0.25, 0.25, 0.25], [0.75, 0.75, 0.25], [0.75, 0.25, 0.75], [0.25, 0.75, 0.75],
    ]
    return Structure(lattice, species, coords)


PROTOTYPES: dict[str, callable] = {
    "chalcopyrite-CuInSe2": chalcopyrite_cuinse2,
    "kesterite-Cu2ZnSnS4": kesterite_cu2znsns4,
    "zincblende-GaAs": zincblende_gaas,
}


def get_prototype(name: str) -> Structure:
    if name not in PROTOTYPES:
        raise KeyError(
            f"unknown prototype {name!r}; available: {sorted(PROTOTYPES)}"
        )
    return PROTOTYPES[name]()
