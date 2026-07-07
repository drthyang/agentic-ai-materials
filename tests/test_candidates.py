import pytest
from pymatgen.core import Lattice, Structure

from matdiscover.config import load_mission
from matdiscover.tools.candidates import substitute_prototype


@pytest.fixture
def proto():
    lattice = Lattice.tetragonal(5.78, 11.62)
    species = ["Cu", "Cu", "In", "In", "Se", "Se", "Se", "Se"]
    coords = [
        [0.0, 0.0, 0.0], [0.0, 0.5, 0.25],
        [0.5, 0.5, 0.0], [0.5, 0.0, 0.25],
        [0.25, 0.25, 0.125], [0.75, 0.75, 0.125],
        [0.75, 0.25, 0.875], [0.25, 0.75, 0.875],
    ]
    return Structure(lattice, species, coords)


@pytest.fixture
def cfg():
    return load_mission("config/mission.yaml")


def test_identity_excluded(proto, cfg):
    cands = substitute_prototype(
        proto, "chalcopyrite", {"Cu": ["Cu"], "In": ["In"], "Se": ["Se"]}, cfg
    )
    assert cands == []


def test_substitution_produces_expected_formula(proto, cfg):
    cands = substitute_prototype(proto, "chalcopyrite", {"In": ["Ga"]}, cfg)
    assert len(cands) == 1
    # compare as compositions: pymatgen's canonical string ordering may differ
    from pymatgen.core import Composition
    assert Composition(cands[0].formula) == Composition("CuGaSe2")
    assert cands[0].substitution == {"In": "Ga"}


def test_stoichiometry_preserved(proto, cfg):
    cands = substitute_prototype(proto, "chalcopyrite", {"Se": ["S"]}, cfg)
    assert len(cands[0].structure) == len(proto)


def test_unknown_prototype_element_raises(proto, cfg):
    with pytest.raises(ValueError):
        substitute_prototype(proto, "chalcopyrite", {"Fe": ["Co"]}, cfg)


def test_dedup_by_formula(proto, cfg):
    cands = substitute_prototype(
        proto, "chalcopyrite",
        {"Cu": ["Cu", "Ag"], "In": ["In", "Ga"], "Se": ["Se", "S"]},
        cfg,
    )
    formulas = [c.formula for c in cands]
    assert len(formulas) == len(set(formulas))
    assert "CuInSe2" not in formulas  # identity excluded
    # 2*2*2 combos - identity = 7 unique formulas
    assert len(formulas) == 7


def test_palette_respected(proto, cfg):
    # Hg is in excluded_elements, so it should never appear
    cands = substitute_prototype(proto, "chalcopyrite", {"Cu": ["Hg", "Ag"]}, cfg)
    assert all("Hg" not in c.formula for c in cands)
