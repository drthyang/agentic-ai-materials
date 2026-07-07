"""Non-LLM baseline searchers the agent must beat (Phase 3).

Both baselines consume exactly the same budget as the agent (iterations x
max_relaxations_per_iteration), use the same filters, the same scorer, and
record to the same DB schema — the ONLY difference is how substitutions are
chosen. That makes "agent vs baseline" a pure test of hypothesis quality.

- RandomBaseline: uniform random substitutions from the mission palette.
- SimilarityBaseline: greedy chemical similarity — try the most similar
  replacement elements first (periodic-table group/period distance), the
  classic "sensible enumeration" a materials scientist might script.
"""

from __future__ import annotations

import logging
import os
import random
from dataclasses import dataclass

from pymatgen.core import Element

from matdiscover.config import MissionConfig
from matdiscover.db import CandidateDB, CandidateRow
from matdiscover.prototypes import PROTOTYPES, get_prototype
from matdiscover.tools.candidates import substitute_prototype
from matdiscover.tools.filters import filter_candidates
from matdiscover.tools.scoring import relax_and_score

log = logging.getLogger("matdiscover.baselines")


@dataclass
class BaselineResult:
    name: str
    relaxations_used: int
    candidates_scored: int


def element_similarity(a: str, b: str) -> float:
    """Smaller = more similar. Periodic-table distance, group-weighted.

    Same group (chemically analogous) counts much less than same period.
    """
    ea, eb = Element(a), Element(b)
    return abs(ea.group - eb.group) * 3.0 + abs(ea.row - eb.row)


class _BaseRunner:
    name = "base"

    def __init__(self, cfg: MissionConfig, db: CandidateDB, seed: int = 0):
        self.cfg = cfg
        self.db = db
        self.rng = random.Random(seed)
        self.has_mp_key = bool(os.environ.get("MP_API_KEY"))

    # -- strategy hook -----------------------------------------------------
    def choose_substitutions(self, prototype_elements: list[str]) -> dict[str, list[str]]:
        raise NotImplementedError

    # -- shared campaign runner ---------------------------------------------
    def run(self, iterations: int | None = None) -> BaselineResult:
        iterations = iterations or self.cfg.budget.iterations
        total_scored = 0
        total_relax = 0
        for i in range(1, iterations + 1):
            relax_left = self.cfg.budget.max_relaxations_per_iteration
            attempts = 0
            while relax_left > 0 and attempts < 10:
                attempts += 1
                scored = self._one_batch(i, relax_left)
                total_scored += scored
                total_relax += scored
                relax_left -= scored
            log.info("[%s] iteration %d: %d relaxations", self.name, i,
                     self.cfg.budget.max_relaxations_per_iteration - relax_left)
        return BaselineResult(self.name, total_relax, total_scored)

    def _one_batch(self, iteration: int, relax_left: int) -> int:
        proto_name = self.rng.choice(sorted(PROTOTYPES))
        proto = get_prototype(proto_name)
        proto_elements = sorted({site.specie.symbol for site in proto})
        subs = self.choose_substitutions(proto_elements)
        if not subs:
            return 0

        cands = substitute_prototype(
            proto, proto_name, subs, self.cfg,
            max_candidates=self.cfg.budget.max_candidates_proposed_per_iteration,
        )
        results = filter_candidates([c.formula for c in cands], self.cfg)

        scored = 0
        for cand, res in zip(cands, results):
            if self.db.already_seen(cand.formula):
                continue
            if not res.passed:
                self.db.add(CandidateRow(
                    iteration=iteration, formula=cand.formula, status="filtered_out",
                    parent_prototype=proto_name, substitution=cand.substitution,
                    hypothesis=f"baseline:{self.name}", filter_reasons=res.reasons,
                ))
                continue
            if scored >= relax_left:
                break
            novel = None
            if self.has_mp_key:
                from matdiscover.tools.mp_search import is_novel

                novel = is_novel(cand.formula,
                                 holdout=frozenset(self.cfg.evaluation.holdout_formulas))
            s = relax_and_score(cand.structure,
                                max_steps=self.cfg.budget.relaxation_max_steps,
                                with_hull=self.has_mp_key)
            self.db.add(CandidateRow(
                iteration=iteration, formula=cand.formula,
                status="error" if s.error else "scored",
                parent_prototype=proto_name, substitution=cand.substitution,
                hypothesis=f"baseline:{self.name}", is_novel=novel,
                converged=s.converged,
                formation_energy_per_atom=s.formation_energy_per_atom,
                e_above_hull=s.e_above_hull, band_gap_ev=s.band_gap_ev,
                error=s.error,
            ))
            scored += 1
        return scored


class RandomBaseline(_BaseRunner):
    name = "random"

    def choose_substitutions(self, prototype_elements: list[str]) -> dict[str, list[str]]:
        palette = self.cfg.usable_elements
        # substitute 1-2 random sites with 1-3 random replacements each
        n_sites = self.rng.randint(1, min(2, len(prototype_elements)))
        sites = self.rng.sample(prototype_elements, n_sites)
        return {
            el: self.rng.sample(palette, self.rng.randint(1, 3)) for el in sites
        }


class SimilarityBaseline(_BaseRunner):
    name = "similarity"

    def __init__(self, cfg: MissionConfig, db: CandidateDB, seed: int = 0):
        super().__init__(cfg, db, seed)
        self._rank_cursor: dict[str, int] = {}

    def choose_substitutions(self, prototype_elements: list[str]) -> dict[str, list[str]]:
        """Greedy: for a rotating site, take the next-most-similar replacements."""
        site = self.rng.choice(prototype_elements)
        palette = [e for e in self.cfg.usable_elements if e != site]
        ranked = sorted(palette, key=lambda e: element_similarity(site, e))
        start = self._rank_cursor.get(site, 0)
        picks = ranked[start:start + 3]
        self._rank_cursor[site] = start + 3
        if not picks:  # exhausted this site's ranking; start over elsewhere
            self._rank_cursor[site] = 0
            return {}
        return {site: picks}
