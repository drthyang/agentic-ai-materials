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

from matdiscover.config import MissionConfig
from matdiscover.llm.base import LLMBackend

log = logging.getLogger("matdiscover.critic")

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


class Critic:
    def __init__(self, backend: LLMBackend, cfg: MissionConfig):
        self.backend = backend
        self.cfg = cfg

    def review(self, batch: list[dict], hypothesis: str) -> dict[str, Verdict]:
        """batch: [{"formula": ..., "substitution": {...}}]. Returns per-formula verdicts."""
        formulas = [b["formula"] for b in batch]
        prompt = CRITIC_PROMPT.format(
            gap_window=list(self.cfg.target.band_gap_ev),
            hull_max=self.cfg.target.e_above_hull_max_ev_per_atom,
            hypothesis=hypothesis,
            candidates=json.dumps(batch, indent=1),
        )
        try:
            resp = self.backend.chat(CRITIC_SYSTEM,
                                     [{"role": "user", "content": prompt}], tools=[])
            verdicts = self._parse(resp.text, formulas)
        except Exception as exc:  # fail open
            log.warning("critic unavailable (%s); approving all", exc)
            return {f: Verdict(True, "critic unavailable; auto-approved") for f in formulas}
        vetoed = [f for f, v in verdicts.items() if not v.approve]
        log.info("critic: %d/%d approved%s", len(formulas) - len(vetoed),
                 len(formulas), f", vetoed: {vetoed}" if vetoed else "")
        return verdicts

    @staticmethod
    def _parse(text: str, formulas: list[str]) -> dict[str, Verdict]:
        """Extract the verdicts JSON; unmentioned/unparseable -> approved."""
        approved_all = {f: Verdict(True, "not addressed by critic; auto-approved")
                        for f in formulas}
        # tolerate code fences and surrounding prose: take the outermost {...}
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            log.warning("critic reply had no JSON; approving all")
            return approved_all
        try:
            data = json.loads(match.group(0))
        except json.JSONDecodeError:
            log.warning("critic reply JSON invalid; approving all")
            return approved_all
        out = dict(approved_all)
        for v in data.get("verdicts", []):
            f = v.get("formula")
            if f in out:
                out[f] = Verdict(bool(v.get("approve", True)),
                                 str(v.get("reason", ""))[:500])
        return out
