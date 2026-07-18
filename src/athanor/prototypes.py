"""Built-in prototype structures the agent can substitute on.

Small, hand-built idealized cells — CHGNet relaxation fixes the geometry, so
approximate lattice parameters are fine as starting points.
"""

from __future__ import annotations

from pymatgen.core import Lattice, Structure


def chalcopyrite_cuinse2() -> Structure:
    """Chalcopyrite CuInSe2 (I-42d), 8 atoms/cell. I-III-VI2 family parent."""
    lattice = Lattice.tetragonal(5.78, 11.62)
    species = ["Cu", "Cu", "In", "In", "Se", "Se", "Se", "Se"]
    coords = [
        [0.0, 0.0, 0.0], [0.0, 0.5, 0.25],
        [0.5, 0.5, 0.0], [0.5, 0.0, 0.25],
        [0.25, 0.25, 0.125], [0.75, 0.75, 0.125],
        [0.75, 0.25, 0.875], [0.25, 0.75, 0.875],
    ]
    return Structure(lattice, species, coords)


def kesterite_cu2znsns4() -> Structure:
    """Kesterite Cu2ZnSnS4 (I-4), 8 atoms/cell. I2-II-IV-VI4 family parent."""
    lattice = Lattice.tetragonal(5.43, 10.86)
    species = ["Cu", "Cu", "Zn", "Sn", "S", "S", "S", "S"]
    coords = [
        [0.0, 0.0, 0.0], [0.0, 0.5, 0.25],
        [0.5, 0.5, 0.0], [0.5, 0.0, 0.25],
        [0.25, 0.25, 0.125], [0.75, 0.75, 0.125],
        [0.75, 0.25, 0.875], [0.25, 0.75, 0.875],
    ]
    return Structure(lattice, species, coords)


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
