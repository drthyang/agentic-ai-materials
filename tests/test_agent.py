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
        self.tools_seen: list[list[str]] = []

    def chat(self, system, messages, tools):
        self.seen.append([dict(m) for m in messages])
        self.tools_seen.append([t.name for t in tools])
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
        # final report turn: offered no tools, answers in one reply
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
    # ... and is offered no tools (it must not propose, relax or write)
    assert backend.tools_seen[6] == [] and "evaluate_candidates" in backend.tools_seen[0]


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


# --- 2026-10 review fixes ----------------------------------------------------

def test_final_report_ignores_tool_calls_and_relaxes_nothing(cfg, monkeypatch):
    calls = []

    def fake_score(structure, max_steps=200, with_hull=True):
        calls.append(structure.composition.reduced_formula)
        return ScoreResult(formula="X", converged=True, band_gap_ev=1.4)

    monkeypatch.setattr("athanor.agent.tools.relax_and_score", fake_score)
    script = [
        LLMResponse(text="iteration done"),
        # the report turn tries to call tools anyway: must not execute
        LLMResponse(text="# report", tool_calls=[_tc("evaluate_candidates", formulas=["CuGaSe2"])]),
    ]
    report = run_campaign(cfg, ScriptedBackend(script), iterations=1)
    assert report.read_text().startswith("# report") and calls == []


def test_a_proposal_is_relaxed_at_most_once(registry, ctx):
    out = json.loads(registry.execute(
        _tc("propose_candidates", substitutions={"In": ["Ga"]}, hypothesis="h")))
    f = out["proposed"][0]["formula"]
    first = json.loads(registry.execute(_tc("evaluate_candidates", formulas=[f])))
    again = json.loads(registry.execute(_tc("evaluate_candidates", formulas=[f])))
    assert len(first["results"]) == 1 and again["results"] == []
    assert again["skipped"][0]["reason"] == "already evaluated this campaign"
    assert ctx.relaxations_used == 1


def test_hits_count_once_per_composition(cfg, tmp_path):
    from athanor.db import CandidateDB, CandidateRow
    from athanor.metrics import compute_metrics

    db = CandidateDB(tmp_path / "d.db")
    for f in ("CuGaSe2", "GaCuSe2"):  # same composition, two rows
        db.add(CandidateRow(iteration=1, formula=f, status="scored", converged=True,
                            band_gap_ev=1.4, e_above_hull=0.0, is_novel=True))
    m = compute_metrics("x", db, cfg)
    assert m.scored == 2 and m.hits == 1


@pytest.mark.parametrize("backend,model", [("anthropic", "gemma4:26b"),
                                           ("ollama", "claude-sonnet-5-5"),
                                           ("openai-compat", "claude-opus-5-5")])
def test_critic_pairings_that_would_fail_open_are_refused(cfg, backend, model):
    cfg.critic.enabled = True
    cfg.critic.backend, cfg.critic.model = backend, model
    with pytest.raises(ValueError, match="critic"):
        run_campaign(cfg, ScriptedBackend([]), iterations=1)


def test_a_run_whose_critic_always_failed_open_is_flagged(cfg, monkeypatch):
    from athanor.agent import loop

    class Down(LLMBackend):
        def chat(self, system, messages, tools):
            raise ConnectionError("critic down")

    monkeypatch.setattr("athanor.llm.make_backend", lambda llm: Down())
    monkeypatch.setattr("athanor.agent.tools.relax_and_score",
                        lambda s, max_steps=200, with_hull=True: ScoreResult(formula="X", converged=True))
    cfg.critic.enabled = True
    script = [
        LLMResponse(tool_calls=[_tc("propose_candidates", substitutions={"In": ["Ga"]}, hypothesis="h")]),
        LLMResponse(tool_calls=[_tc("evaluate_candidates", formulas=["GaCuSe2"], i="c2")]),
        LLMResponse(text="done"),
        LLMResponse(text="# report"),
    ]
    stats: dict = {}
    loop.run_campaign(cfg, ScriptedBackend(script), iterations=1, run_stats=stats)
    assert stats["critic"]["failed_open"] == stats["critic"]["reviews"] == 1
    assert stats["critic_all_failed_open"] is True


# --- fail closed: a critic that keeps failing stops the campaign -------------

class _CriticReplies(LLMBackend):
    def __init__(self, replies):
        self.replies = list(replies)

    def chat(self, system, messages, tools):
        return LLMResponse(text=self.replies.pop(0) if self.replies else "")


def _three_batches():
    from pymatgen.core import Composition

    script = [LLMResponse(tool_calls=[_tc("propose_candidates",
                                          substitutions={"In": ["Ga", "Al"], "Se": ["Se", "S"]},
                                          hypothesis="h")])]
    for i, f in enumerate(["CuGaSe2", "CuAlSe2", "CuGaS2"]):
        f = Composition(f).reduced_formula
        script.append(LLMResponse(tool_calls=[_tc("evaluate_candidates", formulas=[f], i=f"e{i}")]))
    return script + [LLMResponse(text="done"), LLMResponse(text="# report")]


def test_critic_failing_three_times_in_a_row_stops_the_campaign(cfg, monkeypatch):
    relaxed = []
    monkeypatch.setattr("athanor.agent.tools.relax_and_score",
                        lambda s, max_steps=200, with_hull=True:
                        relaxed.append(s.composition.reduced_formula) or ScoreResult(formula="X", converged=True))
    monkeypatch.setattr("athanor.llm.make_backend", lambda llm: _CriticReplies(["no json"] * 5))
    cfg.critic.enabled = True
    stats: dict = {}
    report = run_campaign(cfg, ScriptedBackend(_three_batches()), iterations=1, run_stats=stats)
    assert stats["aborted"] == "critic_unavailable"
    assert "3 reviews in a row" in stats["abort_reason"]
    assert stats["critic"]["failed_open"] == 3
    assert len(relaxed) == 2  # the batch that hit the limit was never relaxed
    assert report.read_text().startswith("# Campaign stopped early: critic_unavailable")


def test_a_good_review_resets_the_failure_count(cfg, monkeypatch):
    monkeypatch.setattr("athanor.agent.tools.relax_and_score",
                        lambda s, max_steps=200, with_hull=True: ScoreResult(formula="X", converged=True))
    ok = json.dumps({"verdicts": [{"formula": "CuAlSe2", "approve": True, "reason": "ok"}]})
    monkeypatch.setattr("athanor.llm.make_backend",
                        lambda llm: _CriticReplies(["no json", ok, "no json"]))
    cfg.critic.enabled = True
    stats: dict = {}
    run_campaign(cfg, ScriptedBackend(_three_batches()), iterations=1, run_stats=stats)
    assert "aborted" not in stats and stats["critic"]["failed_open"] == 2


def test_benchmark_records_critic_unavailable_in_the_ledger(cfg, tmp_path, monkeypatch):
    import csv as _csv

    from athanor.benchmark import run_benchmark
    from athanor.llm.anthropic_backend import AnthropicBackend
    from types import SimpleNamespace

    monkeypatch.chdir(tmp_path)

    class Proposer(AnthropicBackend):
        def __init__(self):
            super().__init__(model="claude-sonnet-5-5", client=SimpleNamespace())
            self.script = _three_batches()

        def chat(self, system, messages, tools):
            return self.script.pop(0)

    proposer = Proposer()
    monkeypatch.setattr("athanor.llm.make_backend",
                        lambda llm: proposer if llm.backend == "anthropic" else _CriticReplies(["x"] * 5))
    monkeypatch.setattr("athanor.agent.tools.relax_and_score",
                        lambda s, max_steps=200, with_hull=True: ScoreResult(formula="X", converged=True))
    cfg.llm.backend, cfg.llm.model = "anthropic", "claude-sonnet-5-5"
    cfg.critic.enabled, cfg.critic.backend = True, "ollama"
    ledger = tmp_path / "ledger.csv"
    run_benchmark(cfg, iterations=1, baselines=[], ledger=ledger, spend_cap_usd=20)
    rows = list(_csv.DictReader(open(ledger)))
    assert rows[-1]["status"] == "critic_unavailable"
