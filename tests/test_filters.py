from matdiscover.config import load_mission
from matdiscover.tools.filters import check_composition, filter_candidates


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


def test_textbook_iii_v_and_ii_vi_semiconductors_pass():
    # Regression: smact 4.0's default ICSD24 "medium" commonality filter drops
    # P3-, falsely rejecting InP/GaP; the wrapper retries with the smact14 set.
    for formula in ["InP", "GaP", "GaAs", "InSb", "ZnSe"]:
        r = check_composition(formula, cfg())
        assert r.passed, f"{formula}: {r.reasons}"


def test_batch_preserves_order():
    formulas = ["CuInSe2", "PbS", "AgGaTe2"]
    results = filter_candidates(formulas, cfg())
    assert [r.formula for r in results] == formulas
