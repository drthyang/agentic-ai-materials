"""Phase 2 tests: registry dispatch, budgets, and the loop — no network, no CHGNet.

A scripted FakeBackend plays the model; scoring is monkeypatched to canned
results so tests run in milliseconds.
"""

from __future__ import annotations

import json

import pytest

from athanor.agent.loop import run_campaign
from athanor.agent.registry import ToolRegistry
from athanor.agent.tools import CampaignContext, build_registry
from athanor.config import load_mission
from athanor.db import CandidateDB
from athanor.llm.base import LLMBackend, LLMResponse, ToolCall, ToolSpec
from athanor.notebook import LabNotebook
from athanor.tools.scoring import ScoreResult


# --------------------------------------------------------------------------
# fixtures
# --------------------------------------------------------------------------

@pytest.fixture
def cfg(tmp_path, monkeypatch):
    # hermetic tests: no Materials Project network calls even if a key is set
    monkeypatch.delenv("MP_API_KEY", raising=False)
    c = load_mission("config/mission.yaml")
    c.paths.db = tmp_path / "c.db"
    c.paths.notebook = tmp_path / "nb.md"
    c.paths.reports = tmp_path / "reports"
    c.critic.enabled = False  # critic has dedicated tests; keep scripts exact here
    return c


@pytest.fixture
def ctx(cfg):
    return CampaignContext(
        cfg=cfg, db=CandidateDB(cfg.paths.db), notebook=LabNotebook(cfg.paths.notebook)
    )


@pytest.fixture
def registry(ctx, monkeypatch):
    # evaluate_candidates must not touch CHGNet in tests
    def fake_score(structure, max_steps=200, with_hull=True):
        return ScoreResult(
            formula=structure.composition.reduced_formula,
            converged=True, formation_energy_per_atom=-0.5,
            e_above_hull=None, band_gap_ev=1.4, volume_change_pct=-2.0,
        )

    monkeypatch.setattr("athanor.agent.tools.relax_and_score", fake_score)
    return build_registry(ctx)


def call(name: str, **arguments) -> ToolCall:
    return ToolCall(id="t1", name=name, arguments=arguments)


# --------------------------------------------------------------------------
# registry dispatch
# --------------------------------------------------------------------------

def test_unknown_tool_returns_error_listing_tools(registry):
    out = json.loads(registry.execute(call("does_not_exist")))
    assert "unknown tool" in out["error"]
    assert "propose_candidates" in out["error"]


def test_missing_required_arg(registry):
    out = json.loads(registry.execute(call("propose_candidates")))
    assert "missing required arguments" in out["error"]


def test_unknown_arg_rejected(registry):
    out = json.loads(registry.execute(
        call("read_notebook", bogus_argument=1)
    ))
    assert "unknown arguments" in out["error"]


def test_parse_error_bounced_back(registry):
    tc = ToolCall(id="t1", name="read_notebook", arguments={},
                  parse_error="could not parse tool arguments: bad JSON")
    out = json.loads(registry.execute(tc))
    assert "re-send" in out["error"]


def test_tool_exception_captured(registry):
    out = json.loads(registry.execute(
        call("propose_candidates", substitutions={"Xx": ["Yy"]}, hypothesis="h")
    ))
    assert "error" in out  # unknown element in prototype -> captured, not raised


# --------------------------------------------------------------------------
# propose -> evaluate flow with budget
# --------------------------------------------------------------------------

def test_propose_then_evaluate_records_to_db(registry, ctx):
    out = json.loads(registry.execute(call(
        "propose_candidates",
        substitutions={"In": ["Ga", "Al"]},
        hypothesis="lighter group-III cations widen the gap",
    )))
    formulas = [p["formula"] for p in out["proposed"]]
    assert len(formulas) == 2

    out = json.loads(registry.execute(call("evaluate_candidates", formulas=formulas)))
    assert len(out["results"]) == 2
    assert all(r["gap_in_target_window"] for r in out["results"])

    top = json.loads(registry.execute(call("get_top_candidates")))
    assert len(top["top_candidates"]) == 2
    # hypothesis carried through from proposal to scored row
    assert "group-III" in top["top_candidates"][0]["hypothesis"]


def test_relaxation_budget_enforced(registry, ctx):
    ctx.cfg.budget.max_relaxations_per_iteration = 1
    out = json.loads(registry.execute(call(
        "propose_candidates",
        substitutions={"Se": ["S", "Te"]},
        hypothesis="anion series tunes the gap",
    )))
    formulas = [p["formula"] for p in out["proposed"]]
    out = json.loads(registry.execute(call("evaluate_candidates", formulas=formulas)))
    assert len(out["results"]) == 1
    assert len(out["skipped"]) == 1
    assert "budget" in out["skipped"][0]["reason"]


def test_evaluate_unproposed_formula_skipped(registry):
    out = json.loads(registry.execute(call("evaluate_candidates", formulas=["NaCl"])))
    assert out["results"] == []
    assert "propose it first" in out["skipped"][0]["reason"]


def test_duplicate_proposal_rejected(registry, ctx):
    a1 = json.loads(registry.execute(call(
        "propose_candidates", substitutions={"In": ["Ga"]}, hypothesis="h1")))
    assert len(a1["proposed"]) == 1
    a2 = json.loads(registry.execute(call(
        "propose_candidates", substitutions={"In": ["Ga"]}, hypothesis="h2")))
    assert a2["proposed"] == []
    assert "already considered" in a2["rejected"][0]["reasons"][0]


# --------------------------------------------------------------------------
# rank_by_surrogate (acquisition tool)
# --------------------------------------------------------------------------

def _seed_scored(ctx, rows):
    from athanor.db import CandidateRow

    for formula, gap, hull in rows:
        ctx.db.add(CandidateRow(
            iteration=1, formula=formula, status="scored", converged=True,
            formation_energy_per_atom=-0.5, e_above_hull=hull, band_gap_ev=gap,
        ))


SEED_ROWS = [
    ("CuInSe2", 1.35, 0.01), ("CuGaSe2", 1.60, 0.00), ("CuInS2", 1.50, 0.02),
    ("AgInSe2", 1.20, 0.04), ("ZnSnP2", 1.90, 0.08), ("CuAlSe2", 2.60, 0.03),
    ("AgGaS2", 2.70, 0.01), ("ZnGeAs2", 1.15, 0.06),
]


def test_surrogate_rank_cold_start_reports_insufficient_data(registry):
    out = json.loads(registry.execute(call("rank_by_surrogate", formulas=["CuInSe2"])))
    assert out["status"] == "insufficient_data"
    assert out["scored_compositions"] == 0
    assert out["needed"] == 6


def test_surrogate_rank_orders_and_stays_json_native(registry, ctx):
    _seed_scored(ctx, SEED_ROWS)
    out = json.loads(registry.execute(call(
        "rank_by_surrogate", formulas=["CuGaS2", "BaTiO3", "AgAlSe2"])))
    assert out["trained_on"] == len(SEED_ROWS)
    assert [type(e["expected_improvement"]) for e in out["ranked"]] == [float] * 3
    ei = [e["expected_improvement"] for e in out["ranked"]]
    assert ei == sorted(ei, reverse=True)
    assert {e["formula"] for e in out["ranked"]} == {"CuGaS2", "BaTiO3", "AgAlSe2"}
    assert all("predicted_utility" in e and "uncertainty" in e for e in out["ranked"])


def test_surrogate_rank_defaults_to_pending_proposals(registry, ctx):
    _seed_scored(ctx, SEED_ROWS)
    proposed = json.loads(registry.execute(call(
        "propose_candidates", substitutions={"In": ["Ga", "Al"]},
        hypothesis="lighter group-III cations widen the gap")))
    pending = {p["formula"] for p in proposed["proposed"]}
    out = json.loads(registry.execute(call("rank_by_surrogate")))
    assert {e["formula"] for e in out["ranked"]} == pending


def test_surrogate_rank_with_nothing_pending_is_an_error(registry, ctx):
    _seed_scored(ctx, SEED_ROWS)
    out = json.loads(registry.execute(call("rank_by_surrogate")))
    assert "nothing to rank" in out["error"]


def test_surrogate_rank_reports_bad_formulas_per_item(registry, ctx):
    _seed_scored(ctx, SEED_ROWS)
    out = json.loads(registry.execute(call(
        "rank_by_surrogate", formulas=["CuGaS2", "notachemical!!"])))
    assert [e["formula"] for e in out["ranked"]] == ["CuGaS2"]
    assert out["invalid"][0]["formula"] == "notachemical!!"


def test_surrogate_tool_disabled_by_config(cfg, monkeypatch):
    cfg.acquisition.enabled = False
    ctx = CampaignContext(
        cfg=cfg, db=CandidateDB(cfg.paths.db), notebook=LabNotebook(cfg.paths.notebook)
    )
    reg = build_registry(ctx)
    assert "rank_by_surrogate" not in {s.name for s in reg.specs}
    out = json.loads(reg.execute(call("rank_by_surrogate")))
    assert "unknown tool" in out["error"]


def test_surrogate_tool_and_bayesopt_share_one_utility(cfg, tmp_path):
    from athanor.baselines import BayesOptBaseline, mission_utility

    bo = BayesOptBaseline(cfg, CandidateDB(tmp_path / "u.db"), seed=0)
    for gap, hull in [(1.4, 0.0), (2.1, 0.12), (None, 0.0), (0.9, None)]:
        assert bo.utility(gap, hull) == mission_utility(cfg, gap, hull)


def test_kickoff_mentions_surrogate_only_when_enabled(cfg):
    from athanor.agent.prompts import iteration_kickoff

    assert "rank_by_surrogate" in iteration_kickoff(cfg, 1, 10)
    cfg.acquisition.enabled = False
    assert "rank_by_surrogate" not in iteration_kickoff(cfg, 1, 10)


# --------------------------------------------------------------------------
# the loop with a scripted backend
# --------------------------------------------------------------------------

class ScriptedBackend(LLMBackend):
    """Plays a fixed sequence of responses; records what it was sent."""

    name = "scripted"

    def __init__(self, script: list[LLMResponse]):
        self.script = list(script)
        self.seen: list[list[dict]] = []

    def chat(self, system, messages, tools):
        self.seen.append([dict(m) for m in messages])
        if not self.script:
            return LLMResponse(text="done")
        return self.script.pop(0)


def _tc(name, i="c1", **args):
    return ToolCall(id=i, name=name, arguments=args)


def test_full_iteration_with_scripted_backend(cfg, monkeypatch):
    def fake_score(structure, max_steps=200, with_hull=True):
        return ScoreResult(
            formula=structure.composition.reduced_formula, converged=True,
            formation_energy_per_atom=-0.7, e_above_hull=None,
            band_gap_ev=1.5, volume_change_pct=0.0,
        )

    monkeypatch.setattr("athanor.agent.tools.relax_and_score", fake_score)

    script = [
        # iteration 1
        LLMResponse(tool_calls=[_tc("read_notebook")]),
        LLMResponse(tool_calls=[_tc("write_notebook", entry_type="hypothesis",
                                    text="Ga-for-In narrows lattice, widens gap")]),
        LLMResponse(tool_calls=[_tc("propose_candidates",
                                    substitutions={"In": ["Ga"]},
                                    hypothesis="Ga-for-In widens gap")]),
        LLMResponse(tool_calls=[_tc("evaluate_candidates", formulas=["CuGaSe2"])]),
        LLMResponse(tool_calls=[_tc("write_notebook", entry_type="reflection",
                                    text="hypothesis held; gap 1.5 eV on target")]),
        LLMResponse(text="Iteration 1: CuGaSe2 hit the target window."),
        # final report turn
        LLMResponse(tool_calls=[_tc("get_top_candidates")]),
        LLMResponse(text="# Campaign report\nCuGaSe2 is the top candidate."),
    ]
    backend = ScriptedBackend(script)
    report_path = run_campaign(cfg, backend, iterations=1)

    assert report_path.exists()
    assert "CuGaSe2" in report_path.read_text()
    notebook = cfg.paths.notebook.read_text()
    assert "hypothesis" in notebook and "reflection" in notebook

    # fresh context per iteration: the final-report turn starts with 1 message
    assert len(backend.seen[6]) == 1


def test_tool_call_budget_terminates_runaway_turn(cfg, monkeypatch):
    def fake_score(structure, max_steps=200, with_hull=True):
        return ScoreResult(formula="X", converged=True)

    monkeypatch.setattr("athanor.agent.tools.relax_and_score", fake_score)
    cfg.budget.max_tool_calls_per_iteration = 3

    # model that calls read_notebook forever and never yields text
    class RunawayBackend(LLMBackend):
        name = "runaway"

        def chat(self, system, messages, tools):
            return LLMResponse(tool_calls=[_tc("read_notebook")])

    report = run_campaign(cfg, RunawayBackend(), iterations=1)
    assert report.exists()  # loop terminated instead of hanging


# --------------------------------------------------------------------------
# openai-compat wire translation (no network — pure format checks)
# --------------------------------------------------------------------------

def test_openai_wire_format_roundtrip():
    from athanor.llm.openai_compat import OpenAICompatBackend

    wire = OpenAICompatBackend._to_wire(
        {"role": "assistant", "content": "thinking...",
         "tool_calls": [{"id": "c1", "name": "f", "arguments": {"x": 1}}]}
    )
    assert wire["tool_calls"][0]["function"]["arguments"] == '{"x": 1}'

    wire = OpenAICompatBackend._to_wire(
        {"role": "tool", "tool_call_id": "c1", "name": "f", "content": "{}"}
    )
    assert wire == {"role": "tool", "tool_call_id": "c1", "content": "{}"}
