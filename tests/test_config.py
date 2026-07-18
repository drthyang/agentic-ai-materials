from athanor.config import load_mission


def test_mission_loads():
    cfg = load_mission("config/mission.yaml")
    assert cfg.mission.name == "pv-absorber-v1"
    assert cfg.target.band_gap_ev == (1.1, 1.7)


def test_comma_lists_flattened():
    cfg = load_mission("config/mission.yaml")
    assert "Cu" in cfg.chemistry.allowed_elements
    assert "Se" in cfg.chemistry.allowed_elements
    assert all("," not in e for e in cfg.chemistry.allowed_elements)


def test_usable_elements_excludes_veto():
    cfg = load_mission("config/mission.yaml")
    assert "Pb" not in cfg.usable_elements
    assert "Cu" in cfg.usable_elements
