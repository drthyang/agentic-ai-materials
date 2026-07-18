"""The campaign loop: iterations of hypothesize -> propose -> screen -> reflect.

Context strategy: each iteration starts a FRESH message list (mission kickoff
only). Cross-iteration memory lives in the lab notebook, which the agent reads
via its read_notebook tool. This keeps prompts small — essential for local
models whose effective context is limited — and makes the notebook the
authoritative scientific record.
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path

from athanor.agent.prompts import FINAL_REPORT_PROMPT, SYSTEM_PROMPT, iteration_kickoff
from athanor.agent.registry import ToolRegistry
from athanor.agent.tools import CampaignContext, build_registry
from athanor.config import MissionConfig
from athanor.db import CandidateDB
from athanor.llm.base import LLMBackend
from athanor.notebook import LabNotebook

log = logging.getLogger("athanor.loop")


def run_campaign(
    cfg: MissionConfig,
    backend: LLMBackend,
    iterations: int | None = None,
) -> Path:
    """Run a discovery campaign; returns the path of the final report."""
    iterations = iterations or cfg.budget.iterations
    ctx = CampaignContext(
        cfg=cfg,
        db=CandidateDB(cfg.paths.db),
        notebook=LabNotebook(cfg.paths.notebook),
    )
    if cfg.critic.enabled:
        from athanor.agent.critic import Critic

        critic_backend = backend
        if cfg.critic.backend or cfg.critic.model:
            from athanor.llm import make_backend

            llm = cfg.llm.model_copy()
            llm.backend = cfg.critic.backend or llm.backend
            llm.model = cfg.critic.model or llm.model
            critic_backend = make_backend(llm)
        ctx.critic = Critic(critic_backend, cfg)
        log.info("critic enabled: %s (%s)", critic_backend.name,
                 getattr(critic_backend, "model", "?"))
    registry = build_registry(ctx)

    for i in range(1, iterations + 1):
        ctx.start_iteration(i)
        log.info("=== iteration %d/%d ===", i, iterations)
        summary = _run_agent_turn(
            backend, registry,
            kickoff=iteration_kickoff(cfg, i, iterations),
            max_tool_calls=cfg.budget.max_tool_calls_per_iteration,
        )
        log.info("iteration %d summary: %s", i, summary[:500])
        stats = ctx.db.iteration_summary(i)
        log.info("iteration %d db: %s, relaxations used: %d",
                 i, stats, ctx.relaxations_used)

    # Final report: ground-truth data is injected into the prompt so the model
    # writes prose around real numbers instead of recalling (or inventing) them.
    ctx.start_iteration(iterations + 1)
    import json as _json

    scored = ctx.db.all_scored()
    stats = {f"iteration_{i}": ctx.db.iteration_summary(i) for i in range(1, iterations + 1)}
    report = _run_agent_turn(
        backend, registry,
        kickoff=FINAL_REPORT_PROMPT.format(
            mission_name=cfg.mission.name,
            notebook=ctx.notebook.read(),
            candidates=_json.dumps(scored, indent=1, default=str),
            stats=_json.dumps(stats),
        ),
        max_tool_calls=6,
    )
    report_path = _write_report(cfg, report)
    log.info("report written to %s", report_path)
    ctx.db.close()
    return report_path


def _run_agent_turn(
    backend: LLMBackend,
    registry: ToolRegistry,
    kickoff: str,
    max_tool_calls: int,
) -> str:
    """One agent conversation: kickoff -> tool loop -> final plain-text reply."""
    messages: list[dict] = [{"role": "user", "content": kickoff}]
    calls_used = 0

    while True:
        try:
            response = backend.chat(SYSTEM_PROMPT, messages, registry.specs)
        except Exception as exc:
            # A dead backend must cost one iteration, not the whole campaign
            # (hours of compute). Backend-level retries have already run.
            log.error("backend failed mid-turn (%s: %s); aborting this turn",
                      type(exc).__name__, exc)
            return f"(iteration aborted: backend error: {type(exc).__name__})"

        if not response.tool_calls:
            return response.text.strip() or "(no summary provided)"

        messages.append({
            "role": "assistant",
            "content": response.text,
            "tool_calls": [tc.as_dict() for tc in response.tool_calls],
        })
        for tc in response.tool_calls:
            calls_used += 1
            if calls_used > max_tool_calls:
                result = (
                    '{"error": "tool-call budget for this iteration is exhausted. '
                    'Reply now with your plain-text summary; do not call more tools."}'
                )
            else:
                result = registry.execute(tc)
                log.debug("tool %s(%s) -> %s", tc.name, tc.arguments, result[:300])
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "name": tc.name,
                "content": result,
            })

        # Safety net: if the model ignores the budget message repeatedly,
        # force-terminate the turn rather than looping forever.
        if calls_used > max_tool_calls + 5:
            return "(iteration terminated: tool-call budget exceeded)"


def _write_report(cfg: MissionConfig, report: str) -> Path:
    cfg.paths.reports.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    path = cfg.paths.reports / f"report-{cfg.mission.name}-{stamp}.md"
    path.write_text(report + "\n")
    return path
