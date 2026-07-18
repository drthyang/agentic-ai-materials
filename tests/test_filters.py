from athanor.config import load_mission
from athanor.tools.filters import check_composition, filter_candidates


def cfg():
    return load_mission("config/mission.yaml")


def test_known_good_composition_passes():
    r = check_composition("CuInSe2", cfg())
    assert r.passed, r.reasons


def test_excluded_element_fails():
    r = check_composition("PbS", cfg())
    assert not r.passed
    assert any("excluded" in reason for reason in r.reasons)


def test_outside_palette_fails():
    r = check_composition("UO2", cfg())
    assert not r.passed


def test_single_element_fails():
    r = check_composition("Si", cfg())
    assert not r.passed


def test_unparseable_fails():
    r = check_composition("not_a_formula!!", cfg())
    assert not r.passed


def test_charge_imbalanced_fails_smact():
    # Cu+ and Cl- can't charge-balance at 1:3 with common oxidation states
    r = check_composition("NaCl2", cfg())
    assert not r.passed


def test_batch_preserves_order():
    formulas = ["CuInSe2", "PbS", "AgGaTe2"]
    results = filter_candidates(formulas, cfg())
    assert [r.formula for r in results] == formulas
