"""Phase 3 tests: baselines, metrics, holdout masking — hermetic (no network/CHGNet)."""

from __future__ import annotations

import numpy as np
import pytest

from athanor.baselines import RandomBaseline, SimilarityBaseline, element_similarity
from athanor.config import load_mission
from athanor.db import CandidateDB, CandidateRow
from athanor.metrics import comparison_table, compute_metrics
from athanor.tools.scoring import ScoreResult


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    monkeypatch.delenv("MP_API_KEY", raising=False)
    c = load_mission("config/mission.yaml")
    c.paths.db = tmp_path / "c.db"
    c.budget.iterations = 2
    c.budget.max_relaxations_per_iteration = 5
    return c


@pytest.fixture
def fake_scoring(monkeypatch):
    """Deterministic scoring: gap keyed to formula hash, always near-stable."""

    def fake(structure, max_steps=200, with_hull=True):
        f = structure.composition.reduced_formula
        gap = 0.5 + (hash(f) % 20) / 10.0  # 0.5 .. 2.4 eV, deterministic per formula
        return ScoreResult(formula=f, converged=True,
                           formation_energy_per_atom=-0.5,
                           e_above_hull=0.01, band_gap_ev=gap,
                           volume_change_pct=0.0)

    monkeypatch.setattr("athanor.baselines.relax_and_score", fake)
    return fake


# --------------------------------------------------------------------------
# baselines
# --------------------------------------------------------------------------

def test_random_baseline_respects_budget(cfg, fake_scoring, tmp_path):
    db = CandidateDB(tmp_path / "r.db")
    result = RandomBaseline(cfg, db, seed=42).run()
    assert result.relaxations_used <= 2 * 5
    assert result.relaxations_used > 0
    # every scored row is tagged with the strategy
    rows = db.all_scored()
    assert all(r["hypothesis"] == "baseline:random" for r in rows)


def test_random_baseline_deterministic_with_seed(cfg, fake_scoring, tmp_path):
    r1 = RandomBaseline(cfg, CandidateDB(tmp_path / "a.db"), seed=7).run()
    r2 = RandomBaseline(cfg, CandidateDB(tmp_path / "b.db"), seed=7).run()
    a = [r["formula"] for r in CandidateDB(tmp_path / "a.db").all_scored()]
    b = [r["formula"] for r in CandidateDB(tmp_path / "b.db").all_scored()]
    assert a == b


def test_similarity_baseline_runs_and_prefers_similar(cfg, fake_scoring, tmp_path):
    db = CandidateDB(tmp_path / "s.db")
    result = SimilarityBaseline(cfg, db, seed=1).run()
    assert result.candidates_scored > 0
    # sanity of the similarity metric itself: same group < cross group
    assert element_similarity("Se", "S") < element_similarity("Se", "K")
    assert element_similarity("In", "Ga") < element_similarity("In", "Cl")


def test_bayesopt_baseline_respects_budget_and_is_deterministic(
        cfg, fake_scoring, tmp_path):
    from athanor.baselines import BayesOptBaseline

    r1 = BayesOptBaseline(cfg, CandidateDB(tmp_path / "a.db"), seed=3).run()
    r2 = BayesOptBaseline(cfg, CandidateDB(tmp_path / "b.db"), seed=3).run()
    assert 0 < r1.relaxations_used <= 2 * 5
    a = [r["formula"] for r in CandidateDB(tmp_path / "a.db").all_scored()]
    b = [r["formula"] for r in CandidateDB(tmp_path / "b.db").all_scored()]
    assert a == b
    rows = CandidateDB(tmp_path / "a.db").all_scored()
    assert all(r["hypothesis"] == "baseline:bayesopt" for r in rows)


def test_bayesopt_rank_survives_empty_pool_and_gp_failure(cfg, tmp_path):
    """Regression: dedup can empty a late batch; EI on 0 candidates crashed."""
    from athanor.baselines import BayesOptBaseline

    db = CandidateDB(tmp_path / "e.db")
    for i, f in enumerate(["CuGaSe2", "AgGaSe2", "CuInS2", "CuGaS2",
                           "AgAlSe2", "ZnGeAs2"]):
        db.add(_scored_row(1, f, 1.0 + i / 10, 0.01))
    bo = BayesOptBaseline(cfg, db, seed=0)
    assert bo.rank_candidates([]) == []  # enough training data, empty pool

    class _Cand:
        formula = "not a formula ///"  # featurization must not kill the run
    assert len(bo.rank_candidates([_Cand()])) == 1


def test_bayesopt_gp_ranks_known_good_region_first():
    import numpy as np

    from athanor.baselines import _GP

    rng = np.random.default_rng(0)
    # utility peaks at x = 2; train on noisy samples, ask EI to rank probes
    X = rng.uniform(0, 4, size=(40, 1))
    y = -np.abs(X[:, 0] - 2.0)
    gp = _GP()
    gp.fit(X, y)
    ei = gp.expected_improvement(np.array([[2.0], [0.1], [3.9]]))
    assert ei[0] == max(ei)  # the peak region beats both edges

    mu, _ = gp.predict(np.array([[2.0], [0.0]]))
    assert mu[0] > mu[1]  # GP mean recovers the shape


def test_bayesopt_featurizer_shape_and_signal():
    from athanor.baselines import featurize_composition

    v1 = featurize_composition("CuGaSe2")
    v2 = featurize_composition("CuGaS2")
    v3 = featurize_composition("BaTiO3")
    assert v1.shape == (11,)
    # anion swap is a small move; a different chemistry is a big one
    assert np.linalg.norm(v1 - v2) < np.linalg.norm(v1 - v3)


def test_bayesopt_utility_prefers_window_and_stability(cfg, tmp_path):
    from athanor.baselines import BayesOptBaseline

    bo = BayesOptBaseline(cfg, CandidateDB(tmp_path / "u.db"), seed=0)
    ideal = cfg.target.band_gap_ideal_ev
    assert bo.utility(ideal, 0.0) > bo.utility(ideal + 0.5, 0.0)
    assert bo.utility(ideal, 0.0) > bo.utility(ideal, 0.2)
    assert bo.utility(None, 0.0) is None


# --------------------------------------------------------------------------
# metrics
# --------------------------------------------------------------------------

def _scored_row(iteration, formula, gap, hull, novel=True, converged=True):
    return CandidateRow(
        iteration=iteration, formula=formula, status="scored",
        converged=converged, formation_energy_per_atom=-0.5,
        e_above_hull=hull, band_gap_ev=gap, is_novel=novel,
    )


def test_metrics_hit_definition(cfg, tmp_path):
    db = CandidateDB(tmp_path / "m.db")
    db.add(_scored_row(1, "AgAlSe2", gap=1.4, hull=0.01))            # hit
    db.add(_scored_row(1, "AgAlTe2", gap=2.5, hull=0.01))            # gap off-target
    db.add(_scored_row(1, "AgGaSe2", gap=1.4, hull=0.30))            # unstable
    db.add(_scored_row(2, "AgInSe2", gap=1.4, hull=0.01, novel=False))  # known
    db.add(_scored_row(2, "CuAlTe2", gap=1.4, hull=0.01, converged=False))  # unconverged
    db.add(_scored_row(2, "KCuSe2", gap=1.4, hull=0.01, novel=None))  # unknown novelty: hit
    m = compute_metrics("test", db, cfg)
    assert m.scored == 6
    assert m.hits == 2
    assert set(m.hit_formulas) == {"AgAlSe2", "KCuSe2"}
    assert m.hits_per_100_relaxations == pytest.approx(100 * 2 / 6)
    assert m.best_gap_distance_ev == 0.0


def test_metrics_rediscovery(cfg, tmp_path):
    cfg.evaluation.holdout_formulas = ["CuGaSe2"]
    db = CandidateDB(tmp_path / "h.db")
    db.add(_scored_row(1, "GaCuSe2", gap=1.4, hull=0.01))  # holdout member, on target
    db.add(_scored_row(1, "AgAlS2", gap=1.4, hull=0.01))
    m = compute_metrics("test", db, cfg)
    assert m.rediscoveries == ["GaCuSe2"]  # matched via reduced-formula comparison


def test_comparison_table_renders(cfg, tmp_path):
    db = CandidateDB(tmp_path / "t.db")
    db.add(_scored_row(1, "AgAlSe2", gap=1.4, hull=0.01))
    table = comparison_table([compute_metrics("random", db, cfg)])
    assert "| strategy |" in table and "| random |" in table


# --------------------------------------------------------------------------
# benchmark lock
# --------------------------------------------------------------------------

def test_benchmark_lock_blocks_concurrent_run(tmp_path, monkeypatch):
    import os

    import athanor.benchmark as bm

    monkeypatch.setattr(bm, "_LOCK", tmp_path / ".lock")
    (tmp_path / ".lock").write_text(str(os.getpid()))  # "another" live process
    with pytest.raises(SystemExit, match="already running"):
        with bm._benchmark_lock():
            pass


def test_benchmark_lock_reclaims_stale_and_cleans_up(tmp_path, monkeypatch):
    import athanor.benchmark as bm

    lock = tmp_path / ".lock"
    monkeypatch.setattr(bm, "_LOCK", lock)
    lock.write_text("999999999")  # dead pid -> stale
    with bm._benchmark_lock():
        assert lock.exists()  # held during the run
    assert not lock.exists()  # released after


# --------------------------------------------------------------------------
# holdout masking
# --------------------------------------------------------------------------

def test_is_novel_holdout_short_circuits_without_network():
    from athanor.tools.mp_search import is_novel

    # holdout member -> treated as novel, no MP call attempted (no key needed)
    assert is_novel("CuGaSe2", holdout=frozenset({"GaCuSe2"})) is True


def test_agent_search_masks_holdout(cfg, tmp_path, monkeypatch):
    from athanor.agent.tools import CampaignContext, build_registry
    from athanor.llm.base import ToolCall
    from athanor.notebook import LabNotebook
    import athanor.tools.mp_search as mp

    monkeypatch.setenv("MP_API_KEY", "fake-key-for-test")
    from athanor.tools.mp_search import KnownMaterial

    def fake_search(q, use_cache=True):
        return [KnownMaterial("mp-1", "CuGaSe2", 1.2, 0.0, True),
                KnownMaterial("mp-2", "CuInSe2", 1.0, 0.0, True)]

    monkeypatch.setattr(mp, "search_known_materials", fake_search)
    cfg.evaluation.holdout_formulas = ["CuGaSe2"]
    ctx = CampaignContext(cfg=cfg, db=CandidateDB(tmp_path / "x.db"),
                          notebook=LabNotebook(tmp_path / "nb.md"))
    reg = build_registry(ctx)
    import json
    out = json.loads(reg.execute(
        ToolCall(id="1", name="search_known_materials",
                 arguments={"chemsys_or_formula": "Cu-Ga-Se"})
    ))
    formulas = [m["formula"] for m in out["materials"]]
    assert "CuInSe2" in formulas
    assert "CuGaSe2" not in formulas  # masked
