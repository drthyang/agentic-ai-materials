"""Phase 4 tests: critic gating, literature tool, dashboard — hermetic."""

from __future__ import annotations

import json

import pytest

from athanor.agent.critic import Critic
from athanor.agent.tools import CampaignContext, build_registry
from athanor.config import load_mission
from athanor.db import CandidateDB, CandidateRow
from athanor.llm.base import LLMBackend, LLMResponse, ToolCall
from athanor.notebook import LabNotebook
from athanor.tools.scoring import ScoreResult


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    monkeypatch.delenv("MP_API_KEY", raising=False)
    c = load_mission("config/mission.yaml")
    c.paths.db = tmp_path / "c.db"
    c.paths.notebook = tmp_path / "nb.md"
    return c


class OneShotBackend(LLMBackend):
    """Returns a fixed text reply (for critic conversations)."""

    name = "oneshot"

    def __init__(self, text: str):
        self.text = text
        self.calls = 0

    def chat(self, system, messages, tools):
        self.calls += 1
        return LLMResponse(text=self.text)


# --------------------------------------------------------------------------
# critic parsing
# --------------------------------------------------------------------------

def test_critic_parses_plain_json(cfg):
    backend = OneShotBackend(json.dumps({
        "verdicts": [
            {"formula": "GaCuSe2", "approve": True, "reason": "sound"},
            {"formula": "AlCuTe2", "approve": False, "reason": "size mismatch"},
        ]
    }))
    v = Critic(backend, cfg).review(
        [{"formula": "GaCuSe2"}, {"formula": "AlCuTe2"}], "h")
    assert v["GaCuSe2"].approve is True
    assert v["AlCuTe2"].approve is False
    assert "size mismatch" in v["AlCuTe2"].reason


def test_critic_parses_json_in_code_fence(cfg):
    backend = OneShotBackend(
        'Sure! Here are my verdicts:\n```json\n'
        '{"verdicts": [{"formula": "X2Y", "approve": false, "reason": "no"}]}\n```'
    )
    v = Critic(backend, cfg).review([{"formula": "X2Y"}], "h")
    assert v["X2Y"].approve is False


def test_critic_garbage_fails_open(cfg):
    v = Critic(OneShotBackend("I cannot comply."), cfg).review(
        [{"formula": "A"}, {"formula": "B"}], "h")
    assert all(verdict.approve for verdict in v.values())


def test_critic_exception_fails_open(cfg):
    class Broken(LLMBackend):
        name = "broken"

        def chat(self, *a, **k):
            raise RuntimeError("connection refused")

    v = Critic(Broken(), cfg).review([{"formula": "A"}], "h")
    assert v["A"].approve is True


def test_critic_unmentioned_formula_approved(cfg):
    backend = OneShotBackend(
        '{"verdicts": [{"formula": "OnlyThis", "approve": false, "reason": "r"}]}'
    )
    v = Critic(backend, cfg).review(
        [{"formula": "OnlyThis"}, {"formula": "Forgotten"}], "h")
    assert v["Forgotten"].approve is True


# --------------------------------------------------------------------------
# critic gating inside evaluate_candidates
# --------------------------------------------------------------------------

def test_critic_veto_costs_no_budget(cfg, monkeypatch):
    def fake_score(structure, max_steps=200, with_hull=True):
        return ScoreResult(formula=structure.composition.reduced_formula,
                           converged=True, formation_energy_per_atom=-0.5,
                           e_above_hull=0.01, band_gap_ev=1.4)

    monkeypatch.setattr("athanor.agent.tools.relax_and_score", fake_score)
    ctx = CampaignContext(cfg=cfg, db=CandidateDB(cfg.paths.db),
                          notebook=LabNotebook(cfg.paths.notebook))
    reg = build_registry(ctx)
    out = json.loads(reg.execute(ToolCall(
        id="1", name="propose_candidates",
        arguments={"substitutions": {"In": ["Ga", "Al"]}, "hypothesis": "h"})))
    formulas = [p["formula"] for p in out["proposed"]]
    assert len(formulas) == 2

    # critic vetoes the first formula, approves the second
    ctx.critic = Critic(OneShotBackend(json.dumps({
        "verdicts": [{"formula": formulas[0], "approve": False,
                      "reason": "phase competition"}]
    })), cfg)
    out = json.loads(reg.execute(ToolCall(
        id="2", name="evaluate_candidates", arguments={"formulas": formulas})))

    assert len(out["results"]) == 1
    assert out["results"][0]["formula"] == formulas[1]
    assert ctx.relaxations_used == 1  # veto cost nothing
    assert any("critic vetoed" in s["reason"] for s in out["skipped"])
    assert "critic_vetoes" in out
    # veto recorded in DB as filtered_out with reason
    row = ctx.db._conn.execute(
        "SELECT * FROM candidates WHERE formula=? AND status='filtered_out'",
        (formulas[0],)).fetchone()
    assert row is not None and "critic" in row["filter_reasons"]
    # vetoed structure is gone: re-evaluation is refused
    out2 = json.loads(reg.execute(ToolCall(
        id="3", name="evaluate_candidates", arguments={"formulas": [formulas[0]]})))
    assert out2["results"] == []


def test_no_critic_means_no_gate(cfg, monkeypatch):
    def fake_score(structure, max_steps=200, with_hull=True):
        return ScoreResult(formula=structure.composition.reduced_formula,
                           converged=True, band_gap_ev=1.4, e_above_hull=0.01,
                           formation_energy_per_atom=-0.5)

    monkeypatch.setattr("athanor.agent.tools.relax_and_score", fake_score)
    ctx = CampaignContext(cfg=cfg, db=CandidateDB(cfg.paths.db),
                          notebook=LabNotebook(cfg.paths.notebook))
    reg = build_registry(ctx)
    out = json.loads(reg.execute(ToolCall(
        id="1", name="propose_candidates",
        arguments={"substitutions": {"In": ["Ga"]}, "hypothesis": "h"})))
    out = json.loads(reg.execute(ToolCall(
        id="2", name="evaluate_candidates",
        arguments={"formulas": [p["formula"] for p in out["proposed"]]})))
    assert len(out["results"]) == 1
    assert "critic_vetoes" not in out


# --------------------------------------------------------------------------
# backend resilience (from the dead-replicates incident, 2026-07-08)
# --------------------------------------------------------------------------

def test_openai_backend_retries_timeouts(monkeypatch):
    import httpx

    from athanor.llm import openai_compat
    from athanor.llm.openai_compat import OpenAICompatBackend

    monkeypatch.setattr(openai_compat.time, "sleep", lambda s: None)
    backend = OpenAICompatBackend(model="test")
    calls = {"n": 0}

    class FakeResp:
        def raise_for_status(self):
            pass

        def json(self):
            return {"choices": [{"message": {"content": "ok", "tool_calls": None}}]}

    def flaky_post(url, json=None):
        calls["n"] += 1
        if calls["n"] == 1:
            raise httpx.ReadTimeout("timed out")
        return FakeResp()

    monkeypatch.setattr(backend._client, "post", flaky_post)
    resp = backend.chat("sys", [{"role": "user", "content": "hi"}], [])
    assert resp.text == "ok"
    assert calls["n"] == 2  # one failure, one retry, success


def test_openai_backend_gives_up_after_retries(monkeypatch):
    import httpx

    from athanor.llm import openai_compat
    from athanor.llm.openai_compat import OpenAICompatBackend

    monkeypatch.setattr(openai_compat.time, "sleep", lambda s: None)
    backend = OpenAICompatBackend(model="test")

    def always_timeout(url, json=None):
        raise httpx.ReadTimeout("timed out")

    monkeypatch.setattr(backend._client, "post", always_timeout)
    with pytest.raises(httpx.ReadTimeout):
        backend.chat("sys", [{"role": "user", "content": "hi"}], [])


def test_campaign_survives_dead_backend(cfg, monkeypatch, tmp_path):
    """A backend that dies mid-campaign costs iterations, not the whole run."""
    from athanor.agent.loop import run_campaign

    cfg.paths.reports = tmp_path / "reports"
    cfg.critic.enabled = False

    class DeadBackend(LLMBackend):
        name = "dead"

        def chat(self, *a, **k):
            raise RuntimeError("connection refused")

    report = run_campaign(cfg, DeadBackend(), iterations=2)
    assert report.exists()  # campaign completed and wrote a report
    assert "aborted" in report.read_text()


# --------------------------------------------------------------------------
# literature tool
# --------------------------------------------------------------------------

def test_literature_parses_and_caches(cfg, monkeypatch, tmp_path):
    import athanor.tools.literature as lit

    monkeypatch.setattr(lit, "_CACHE_DIR", tmp_path / "lit")
    calls = {"n": 0}

    class FakeResp:
        def raise_for_status(self):
            pass

        def json(self):
            return {"message": {"items": [{
                "title": ["Growth of CuGaSe2 thin films"],
                "DOI": "10.1000/xyz",
                "issued": {"date-parts": [[2019, 5]]},
                "container-title": ["J. Cryst. Growth"],
            }]}}

    def fake_get(*a, **k):
        calls["n"] += 1
        return FakeResp()

    monkeypatch.setattr(lit.httpx, "get", fake_get)
    r1 = lit.search_literature("CuGaSe2 growth")
    assert r1[0]["year"] == 2019 and r1[0]["doi"] == "10.1000/xyz"
    r2 = lit.search_literature("CuGaSe2 growth")  # cache hit
    assert r2 == r1
    assert calls["n"] == 1


def test_literature_error_returns_dict_not_raise(cfg, monkeypatch):
    import athanor.tools.literature as lit

    def boom(*a, **k):
        raise OSError("network down")

    monkeypatch.setattr(lit.httpx, "get", boom)
    out = lit.search_literature("anything else entirely")
    assert "error" in out


def test_literature_registered_as_agent_tool(cfg):
    ctx = CampaignContext(cfg=cfg, db=CandidateDB(cfg.paths.db),
                          notebook=LabNotebook(cfg.paths.notebook))
    names = [s.name for s in build_registry(ctx).specs]
    assert "search_literature" in names


# --------------------------------------------------------------------------
# dashboard
# --------------------------------------------------------------------------

def _seed_campaign(cfg):
    """One of each: hit, chemistry-filtered, critic-vetoed, error."""
    db = CandidateDB(cfg.paths.db)
    db.add(CandidateRow(iteration=1, formula="AgAlSe2", status="scored",
                        converged=True, formation_energy_per_atom=-0.5,
                        e_above_hull=0.02, band_gap_ev=1.38, is_novel=True,
                        hypothesis="test hypothesis"))
    db.add(CandidateRow(iteration=1, formula="PbSe", status="filtered_out",
                        filter_reasons=["excluded element Pb"]))
    db.add(CandidateRow(iteration=1, formula="Cu3SbS4", status="filtered_out",
                        filter_reasons=["critic: likely known famatinite"]))
    db.add(CandidateRow(iteration=1, formula="AgGaTe2", status="error",
                        error="relaxation exceeded max steps"))
    db.close()
    LabNotebook(cfg.paths.notebook).write("hypothesis", 1, "try silver")


def test_snapshot_totals_flags_and_feed(cfg):
    _seed_campaign(cfg)
    from athanor.dashboard import campaign_snapshot

    snap = campaign_snapshot(cfg)
    t = snap["totals"]
    assert (t["proposed"], t["scored"], t["errors"]) == (4, 1, 1)
    assert t["filtered_out"] == 2 and t["vetoed"] == 1
    assert t["hits"] == 1 and t["relaxations_used"] == 2

    hit = next(c for c in snap["candidates"] if c["formula"] == "AgAlSe2")
    assert hit["flags"]["hit"] is True and hit["flags"]["rediscovery"] is False

    kinds = {e["kind"] for e in snap["feed"]}
    assert {"hit", "veto", "filtered", "error", "notebook"} <= kinds
    veto = next(e for e in snap["feed"] if e["kind"] == "veto")
    assert veto["formula"] == "Cu3SbS4" and "famatinite" in veto["text"]

    assert snap["notebook"][0]["type"] == "hypothesis"
    assert snap["notebook"][0]["text"] == "try silver"
    json.dumps(snap)  # the whole snapshot must be JSON-serializable


def test_snapshot_rediscovery_flag(cfg):
    cfg.evaluation.holdout_formulas = ["CuGaSe2"]
    db = CandidateDB(cfg.paths.db)
    db.add(CandidateRow(iteration=1, formula="CuGaSe2", status="scored",
                        converged=True, e_above_hull=0.01, band_gap_ev=1.42,
                        is_novel=True))
    db.close()
    from athanor.dashboard import campaign_snapshot

    snap = campaign_snapshot(cfg)
    assert snap["totals"]["rediscoveries"] == 1
    assert snap["candidates"][0]["flags"]["rediscovery"] is True


def test_snapshot_repairs_legacy_blob_floats(cfg):
    """Old DBs hold numpy float32 values stored as raw 4-byte BLOBs."""
    import struct

    db = CandidateDB(cfg.paths.db)
    db.add(CandidateRow(iteration=1, formula="GaCuSe2", status="scored",
                        converged=True, e_above_hull=0.01, band_gap_ev=1.2,
                        is_novel=True))
    db._conn.execute("UPDATE candidates SET formation_energy_per_atom = ?",
                     (struct.pack("<f", -0.75),))
    db._conn.commit()
    db.close()
    from athanor.dashboard import campaign_snapshot

    snap = campaign_snapshot(cfg)
    e = snap["candidates"][0]["formation_energy_per_atom"]
    assert abs(e - (-0.75)) < 1e-6
    json.dumps(snap)


def test_db_add_coerces_numpy_scalars(cfg):
    np = pytest.importorskip("numpy")
    db = CandidateDB(cfg.paths.db)
    db.add(CandidateRow(iteration=1, formula="InP", status="scored",
                        converged=True,
                        formation_energy_per_atom=np.float32(-0.5),
                        e_above_hull=np.float64(0.02),
                        band_gap_ev=np.float32(1.3), is_novel=True))
    row = db.all_scored()[0]
    db.close()
    assert isinstance(row["formation_energy_per_atom"], float)
    assert isinstance(row["band_gap_ev"], float)


def test_snapshot_empty_campaign(cfg):
    from athanor.dashboard import campaign_snapshot

    snap = campaign_snapshot(cfg)  # no db, no notebook on disk
    assert snap["totals"]["iterations_done"] == 0
    assert snap["candidates"] == [] and snap["feed"] == []
    assert snap["meta"]["running"] is False
    json.dumps(snap)


def test_notebook_structured_entries(cfg):
    nb = LabNotebook(cfg.paths.notebook)
    nb.write("hypothesis", 1, "first idea")
    nb.write("reflection", 2, "it worked")
    entries = nb.entries()
    assert [e["type"] for e in entries] == ["hypothesis", "reflection"]
    assert entries[1]["iteration"] == 2 and entries[1]["text"] == "it worked"
    assert nb.entries(last_n=1)[0]["type"] == "reflection"


def test_benchmark_snapshot_parses_markdown(tmp_path):
    from athanor.dashboard import benchmark_snapshot

    (tmp_path / "benchmark.md").write_text(
        "# Benchmark: pv-absorber-v1\n\nbudget: 5 x 20\n\n"
        "| strategy | hits |\n|---|---|\n| random | 1 |\n| agent | 4 |\n\n"
        "hit = converged + on-target\n")
    b = benchmark_snapshot(tmp_path)
    assert b["available"] and b["title"] == "pv-absorber-v1"
    assert b["rows"][1] == {"strategy": "agent", "hits": "4"}
    assert b["has_plot"] is False
    assert benchmark_snapshot(tmp_path / "missing") == {"available": False}


def test_web_shell_ships_with_package():
    from athanor.dashboard import WEB_DIR

    index = (WEB_DIR / "index.html").read_text()
    for mount in ("mission-card", "pipeline", "map", "feed", "top-body"):
        assert f'id="{mount}"' in index
    for asset in ("app.css", "app.js", "ibm-plex-sans-var.woff2"):
        assert (WEB_DIR / asset).exists()
