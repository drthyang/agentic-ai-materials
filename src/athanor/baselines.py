"""Non-LLM baseline searchers the agent must beat (Phase 3).

Both baselines consume exactly the same budget as the agent (iterations x
max_relaxations_per_iteration), use the same filters, the same scorer, and
record to the same DB schema — the ONLY difference is how substitutions are
chosen. That makes "agent vs baseline" a pure test of hypothesis quality.

- RandomBaseline: uniform random substitutions from the mission palette.
- SimilarityBaseline: greedy chemical similarity — try the most similar
  replacement elements first (periodic-table group/period distance), the
  classic "sensible enumeration" a materials scientist might script.
- BayesOptBaseline: GP + expected improvement over composition features —
  the sequential model-based search a materials-informatics group would run.
"""

from __future__ import annotations

import logging
import os
import random
from dataclasses import dataclass

from pymatgen.core import Element

from athanor.config import MissionConfig
from athanor.db import CandidateDB, CandidateRow
from athanor.prototypes import PROTOTYPES, get_prototype
from athanor.tools.candidates import substitute_prototype
from athanor.tools.filters import filter_candidates
from athanor.tools.scoring import relax_and_score

log = logging.getLogger("athanor.baselines")


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

    # -- strategy hooks ----------------------------------------------------
    def choose_substitutions(self, prototype_elements: list[str]) -> dict[str, list[str]]:
        raise NotImplementedError

    def rank_candidates(self, cands: list) -> list:
        """Order filter-survivors before spending relaxations (best first).

        Default: generation order, which keeps RandomBaseline and
        SimilarityBaseline byte-identical to their pre-hook behavior.
        """
        return cands

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

        pool = []
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
            pool.append(cand)

        scored = 0
        for cand in self.rank_candidates(pool):
            if scored >= relax_left:
                break
            novel = None
            if self.has_mp_key:
                from athanor.tools.mp_search import is_novel

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


def featurize_composition(formula: str) -> "np.ndarray":
    """Fraction-weighted elemental-property statistics for a composition.

    Mean and standard deviation of (Z, group, row, electronegativity,
    atomic mass) plus the element count: an 11-dim numpy vector. Deliberately
    magpie-lite — enough signal for a GP over a few dozen points, zero new
    dependencies.
    """
    import numpy as np
    from pymatgen.core import Composition

    comp = Composition(formula).fractional_composition
    props = []
    fracs = []
    for el, frac in comp.items():
        x = el.X if el.X is not None else 1.5  # noble-gas fallback
        props.append([el.Z, el.group, el.row, x, float(el.atomic_mass)])
        fracs.append(frac)
    p = np.asarray(props, dtype=float)
    w = np.asarray(fracs, dtype=float)
    w = w / w.sum()
    mean = w @ p
    std = np.sqrt(np.maximum(w @ (p - mean) ** 2, 0.0))
    return np.concatenate([mean, std, [len(fracs)]])


class _GP:
    """Minimal RBF-kernel Gaussian process (numpy only, fixed hyperparams).

    Lengthscale from the median-distance heuristic; noise floor keeps the
    Cholesky stable. Good enough to rank ~50 candidates from ~100 training
    points; not a general-purpose GP.
    """

    def __init__(self):
        import numpy as np

        self.np = np
        self.ready = False

    def fit(self, X, y):
        np = self.np
        X = np.asarray(X, float)
        y = np.asarray(y, float)
        self.x_mean, self.x_std = X.mean(0), X.std(0) + 1e-9
        Xs = (X - self.x_mean) / self.x_std
        d2 = ((Xs[:, None, :] - Xs[None, :, :]) ** 2).sum(-1)
        off = d2[d2 > 1e-12]
        self.ls2 = float(np.median(off)) if off.size else 1.0
        self.y_mean = float(y.mean())
        yc = y - self.y_mean
        K = np.exp(-d2 / (2 * self.ls2))
        noise = 1e-4 * float(yc.var()) + 1e-8
        self.L = np.linalg.cholesky(K + noise * np.eye(len(y)))
        self.alpha = np.linalg.solve(self.L.T, np.linalg.solve(self.L, yc))
        self.Xs = Xs
        self.y_best = float(y.max())
        self.ready = True

    def predict(self, X):
        np = self.np
        Xq = (np.asarray(X, float) - self.x_mean) / self.x_std
        d2 = ((Xq[:, None, :] - self.Xs[None, :, :]) ** 2).sum(-1)
        Ks = np.exp(-d2 / (2 * self.ls2))
        mu = Ks @ self.alpha + self.y_mean
        v = np.linalg.solve(self.L, Ks.T)
        var = np.maximum(1.0 - (v ** 2).sum(0), 1e-12)
        return mu, var

    def expected_improvement(self, X, xi: float = 0.01):
        from math import erf, exp, pi, sqrt

        np = self.np
        mu, var = self.predict(X)
        sigma = np.sqrt(var)
        z = (mu - self.y_best - xi) / sigma
        cdf = np.array([0.5 * (1 + erf(zi / sqrt(2))) for zi in z])
        pdf = np.array([exp(-zi * zi / 2) / sqrt(2 * pi) for zi in z])
        return (mu - self.y_best - xi) * cdf + sigma * pdf


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


class BayesOptBaseline(_BaseRunner):
    """GP + expected improvement over composition features.

    Proposes like RandomBaseline (wide pools), but before spending any
    relaxation it ranks the filter-survivors by expected improvement of a
    mission-utility GP trained on every composition this campaign has
    scored. Until enough training data exists (min_train) it explores in
    shuffled order. The standard materials-informatics control: what does
    sequential model-based search achieve at the same budget, with no
    language model involved?
    """

    name = "bayesopt"
    min_train = 6

    def utility(self, gap: float | None, hull: float | None) -> float | None:
        """Scalar 'goodness' of a scored composition; higher is better.

        Gap distance in eV and hull excess in eV/atom x10 are comparable
        scales, so a candidate 0.1 eV/atom above the near-stable bar pays
        like a 1 eV gap miss.
        """
        if gap is None:
            return None
        y = -abs(gap - self.cfg.target.band_gap_ideal_ev)
        if hull is not None:
            y -= 10.0 * max(0.0, hull - self.cfg.target.e_above_hull_max_ev_per_atom)
        return y

    def choose_substitutions(self, prototype_elements: list[str]) -> dict[str, list[str]]:
        palette = self.cfg.usable_elements
        n_sites = self.rng.randint(1, min(2, len(prototype_elements)))
        sites = self.rng.sample(prototype_elements, n_sites)
        return {
            el: self.rng.sample(palette, self.rng.randint(2, 3)) for el in sites
        }

    def rank_candidates(self, cands: list) -> list:
        if not cands:  # dedup/filters can empty a batch late in a campaign
            return cands
        X, y = [], []
        for r in self.db.all_scored():
            u = self.utility(r["band_gap_ev"], r["e_above_hull"])
            if u is not None and r["converged"]:
                X.append(featurize_composition(r["formula"]))
                y.append(u)
        if len(y) < self.min_train:
            self.rng.shuffle(cands)
            return cands
        try:
            gp = _GP()
            gp.fit(X, y)
            ei = gp.expected_improvement(
                [featurize_composition(c.formula) for c in cands])
            order = sorted(range(len(cands)), key=lambda i: -ei[i])
            return [cands[i] for i in order]
        except Exception as exc:
            # Fail open, like the critic: a flaky ranker may cost efficiency,
            # never a campaign.
            log.warning("[bayesopt] EI ranking failed (%s); shuffling", exc)
            self.rng.shuffle(cands)
            return cands
