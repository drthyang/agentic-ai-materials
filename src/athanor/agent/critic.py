"""The critic: an independent reviewer that vets candidates BEFORE compute.

Runs as a separate LLM conversation (fresh context, skeptical persona) so it
can't be swayed by the proposer's enthusiasm. Wired into evaluate_candidates:
vetoed candidates never reach CHGNet, so a veto costs zero relaxation budget.

Fail-open by design: if the critic's response can't be parsed, everything is
approved and the campaign continues — a flaky reviewer must never block
science, it can only save compute.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass

from pymatgen.core import Composition

from athanor.config import MissionConfig
from athanor.llm.base import LLMBackend

log = logging.getLogger("athanor.critic")

CRITIC_SYSTEM = """\
You are a skeptical senior materials scientist reviewing computational
screening proposals before expensive calculations are run. You are NOT the
proposer; judge each candidate on its merits:

- Oxidation-state plausibility beyond simple charge balance (e.g. Cu2+ vs Cu+
  in chalcogenides, Sn2+/Sn4+ ambiguity)
- Likely phase competition: is a simpler binary obviously more stable?
- Synthesizability red flags: extreme size mismatch, volatile constituents,
  known-difficult chemistries
- Whether the candidate actually tests the stated hypothesis

Approve when in doubt — a wasted relaxation is cheap; a blocked good idea is
not. Veto only with a concrete, falsifiable reason.

Reply with ONLY a JSON object, no prose, in exactly this shape:
{"verdicts": [{"formula": "...", "approve": true, "reason": "..."}]}"""

CRITIC_PROMPT = """\
Mission target: band gap in {gap_window} eV, energy above hull <= {hull_max} eV/atom.

Proposer's hypothesis: {hypothesis}

Candidates to review (formula, substitution applied to prototype):
{candidates}

Return your verdicts JSON now."""


@dataclass
class Verdict:
    approve: bool
    reason: str
    addressed: bool = True  # False when auto-approved without a critic verdict


class Critic:
    def __init__(self, backend: LLMBackend, cfg: MissionConfig):
        self.backend = backend
        self.cfg = cfg
        # fail-open is silent by design, so count it: an ablation must be
        # able to show the critic actually reviewed rather than auto-approved
        # failed_open: reviews whose whole batch was auto-approved because the
        # critic was unreachable or its reply unparseable; unaddressed:
        # candidates auto-approved because no verdict named them
        # auto_approved: candidates waved through without a verdict (both causes)
        self.stats = {"reviews": 0, "candidates": 0, "approved": 0,
                      "vetoed": 0, "failed_open": 0, "unaddressed": 0,
                      "auto_approved": 0}
        self.consecutive_failures = 0

    def review(self, batch: list[dict], hypothesis: str) -> dict[str, Verdict]:
        """batch: [{"formula": ..., "substitution": {...}}]. Returns per-formula verdicts."""
        formulas = [b["formula"] for b in batch]
        prompt = CRITIC_PROMPT.format(
            gap_window=list(self.cfg.target.band_gap_ev),
            hull_max=self.cfg.target.e_above_hull_max_ev_per_atom,
            hypothesis=hypothesis,
            candidates=json.dumps(batch, indent=1),
        )
        self.stats["reviews"] += 1
        self.stats["candidates"] += len(formulas)
        limit = self.cfg.critic.max_consecutive_failures
        try:
            resp = self.backend.chat(CRITIC_SYSTEM,
                                     [{"role": "user", "content": prompt}], tools=[])
            verdicts, parsed = self._parse(resp.text, formulas)
        except Exception as exc:  # fail open
            log.warning("critic unavailable (%s); approving all", exc)
            self._failed(limit, f"{type(exc).__name__}: {exc}")
            self.stats["failed_open"] += 1
            self.stats["auto_approved"] += len(formulas)
            self.stats["approved"] += len(formulas)
            return {f: Verdict(True, "critic unavailable; auto-approved", addressed=False)
                    for f in formulas}
        n_auto = sum(v.addressed is False for v in verdicts.values())
        self.stats["auto_approved"] += n_auto
        if not parsed:
            self._failed(limit, "reply had no parseable verdicts: " + repr(resp.text[:200]))
            self.stats["failed_open"] += 1
        else:
            self.consecutive_failures = 0
            self.stats["unaddressed"] += n_auto
        vetoed = [f for f, v in verdicts.items() if not v.approve]
        self.stats["vetoed"] += len(vetoed)
        self.stats["approved"] += len(formulas) - len(vetoed)
        log.info("critic: %d/%d approved%s", len(formulas) - len(vetoed),
                 len(formulas), f", vetoed: {vetoed}" if vetoed else "")
        return verdicts

    def _failed(self, limit: int, detail: str) -> None:
        """Count a failed review; past the limit, stop the campaign before
        this batch is relaxed (fail closed when the critic is gone)."""
        self.consecutive_failures += 1
        if limit and self.consecutive_failures >= limit:
            from athanor.agent.registry import CampaignAbort

            self.stats["failed_open"] += 1
            raise CampaignAbort(
                "critic_unavailable",
                f"critic failed {self.consecutive_failures} reviews in a row "
                f"(last: {detail}); stopping the campaign rather than run without it")

    @staticmethod
    def _parse(text: str, formulas: list[str]) -> tuple[dict[str, Verdict], bool]:
        """Extract the verdicts JSON. Returns (verdicts, parsed).

        Unparseable reply -> every candidate approved, parsed=False (counted
        as a fail-open review). A candidate no verdict names -> approved with
        addressed=False (counted as unaddressed). Verdicts are matched by
        composition, so "Ag2CdGeSe4" still matches "CdAg2GeSe4".
        """
        def auto(reason: str) -> dict[str, Verdict]:
            return {f: Verdict(True, reason, addressed=False) for f in formulas}

        # tolerate code fences and surrounding prose: take the outermost {...}
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            log.warning("critic reply had no JSON; approving all")
            return auto("critic reply unparseable; auto-approved"), False
        try:
            data = json.loads(match.group(0))
        except json.JSONDecodeError:
            log.warning("critic reply JSON invalid; approving all")
            return auto("critic reply unparseable; auto-approved"), False
        out = auto("not addressed by critic; auto-approved")
        by_comp = {}
        for f in formulas:
            try:
                by_comp[Composition(f).reduced_composition] = f
            except Exception:
                pass
        for v in data.get("verdicts", []) if isinstance(data, dict) else []:
            f = v.get("formula") if isinstance(v, dict) else None
            if f not in out:
                try:
                    f = by_comp.get(Composition(str(f)).reduced_composition)
                except Exception:
                    f = None
            if f in out:
                out[f] = Verdict(bool(v.get("approve", True)),
                                 str(v.get("reason", ""))[:500])
        unaddressed = [f for f, v in out.items() if v.addressed is False]
        if unaddressed:
            log.warning("critic gave no verdict for %s; auto-approved", unaddressed)
        return out, True
