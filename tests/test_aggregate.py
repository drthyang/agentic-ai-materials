"""Statistics in scripts/aggregate_ablation.py."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import aggregate_ablation as agg  # noqa: E402


def test_permutation_p_is_two_sided_by_default():
    a, b = [5.0, 6.0, 7.0], [1.0, 2.0, 3.0]
    # complete separation, 3 vs 3: one-sided 1/20, two-sided 2/20
    assert agg.permutation_p(a, b, two_sided=False) == pytest.approx(1 / 20)
    assert agg.permutation_p(a, b) == pytest.approx(2 / 20)
    # symmetric: the direction no longer matters
    assert agg.permutation_p(b, a) == pytest.approx(2 / 20)


def test_auto_approvals_recovered_from_a_run_log(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data/logs").mkdir(parents=True)
    (tmp_path / "data/logs/sonnet-nosurr-seed12.log").write_text(
        "12:00 athanor.critic INFO critic: 5/5 approved\n"
        "12:01 athanor.critic WARNING critic reply JSON invalid; approving all\n"
        "12:01 athanor.critic INFO critic: 7/7 approved\n")
    run = tmp_path / "data/benchmark/20261011-010913-seed12-sonnet-nosurr"
    assert agg.critic_auto_approved_from_log(run) == 7
    assert agg.critic_auto_approved_from_log(tmp_path / "20260707-1212") is None


def test_audits_key_on_the_route_not_just_the_formula(tmp_path, monkeypatch):
    import json

    import structure_audit as sa

    from athanor.db import CandidateDB, CandidateRow

    monkeypatch.delenv("MP_API_KEY", raising=False)
    db = CandidateDB(tmp_path / "agent.db")
    hit = dict(status="scored", converged=True, band_gap_ev=1.4, e_above_hull=0.0, is_novel=True)
    db.add(CandidateRow(iteration=1, formula="AgGaSe2", parent_prototype="chalcopyrite-CuInSe2",
                        substitution={"Cu": "Ag", "In": "Ga"}, **hit))
    db.add(CandidateRow(iteration=2, formula="AgGaSe2", parent_prototype="zincblende-GaAs",
                        substitution={"Ga": "Ag", "As": "Se"}, **hit))
    db.close()
    spec = tmp_path / "arms.json"
    spec.write_text(json.dumps({"mission": str(Path("config/mission.yaml").resolve()),
                                "arms": {"a": {"db": "agent.db", "runs": [str(tmp_path)]}}}))
    hits, _ = sa.distinct_hits(spec)
    assert len(hits) == 2 and {h["parent_prototype"] for h in hits} == {
        "chalcopyrite-CuInSe2", "zincblende-GaAs"}
    assert sa.route_key("X", "p", '{"b": "c", "a": "d"}') == sa.route_key("X", "p", {"a": "d", "b": "c"})


def test_rescored_hits_count_distinct_compositions_under_each_fix():
    from athanor.config import load_mission

    cfg = load_mission("config/mission.yaml")
    common = {"status": "scored", "is_novel": "1", "converged": "1", "cellfix_error": "",
              "cellfix_converged": "True"}
    rows = [
        # hit on the old hull, off the window once the cell is fixed
        {**common, "formula": "A2B", "band_gap_ev": "1.4", "hull_corrected_same_cell": "0.01",
         "cellfix_band_gap_ev": "0.3", "cellfix_e_above_hull": "0.0"},
        # unstable on the corrected hull in its own cell, a hit in the correct cell
        {**common, "formula": "CD", "band_gap_ev": "1.4", "hull_corrected_same_cell": "0.2",
         "cellfix_band_gap_ev": "1.5", "cellfix_e_above_hull": "0.02"},
        # the same composition twice counts once
        {**common, "formula": "CD", "band_gap_ev": "1.4", "hull_corrected_same_cell": "0.2",
         "cellfix_band_gap_ev": "1.5", "cellfix_e_above_hull": "0.02"},
        # known to Materials Project: never a hit
        {**common, "formula": "EF", "is_novel": "0", "band_gap_ev": "1.4",
         "hull_corrected_same_cell": "0.0", "cellfix_band_gap_ev": "1.4",
         "cellfix_e_above_hull": "0.0"},
    ]
    assert agg.rescored_hits(rows, cfg) == (1, 1)
