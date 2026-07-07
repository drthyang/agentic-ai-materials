"""Every mission config in the repo must load and be internally coherent."""

from __future__ import annotations

from pathlib import Path

import pytest

from matdiscover.config import load_mission

MISSIONS = ["config/mission.yaml", *sorted(Path("config/missions").glob("*.yaml"))]


@pytest.mark.parametrize("path", MISSIONS, ids=lambda p: str(p))
def test_mission_loads_and_is_coherent(path):
    cfg = load_mission(path)
    lo, hi = cfg.target.band_gap_ev
    assert lo < hi
    assert lo <= cfg.target.band_gap_ideal_ev <= hi
    assert cfg.target.e_above_hull_max_ev_per_atom > 0
    assert len(cfg.usable_elements) >= 2
    # excluded elements must actually be excluded from the usable palette
    assert not set(cfg.chemistry.excluded_elements) & set(cfg.usable_elements)
    assert cfg.budget.max_relaxations_per_iteration > 0
