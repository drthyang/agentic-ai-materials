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
