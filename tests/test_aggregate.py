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
