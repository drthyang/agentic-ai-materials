"""Campaign tools: the agent-facing surface over the Phase 1 tool layer.

Design notes:
- propose_candidates fuses generate+filter+novelty into one call: fewer round
  trips for a local model, and no way to sneak an unfiltered structure to the
  scorer. Structures live in the context keyed by formula; the model only
  handles formula strings.
- evaluate_candidates enforces the per-iteration relaxation budget in code.
- Every proposal and score is recorded to the DB as a side effect; the model
  cannot forget to log.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

from pymatgen.core import Structure

from matdiscover.config import MissionConfig
from matdiscover.db import CandidateDB, CandidateRow
from matdiscover.llm.base import ToolSpec
from matdiscover.notebook import LabNotebook
from matdiscover.prototypes import PROTOTYPES, get_prototype
from matdiscover.agent.registry import ToolRegistry
from matdiscover.tools.candidates import substitute_prototype
from matdiscover.tools.filters import filter_candidates
from matdiscover.tools.scoring import relax_and_score


@dataclass
class Proposed:
    structure: Structure
    hypothesis: str
    prototype: str
    substitution: dict
    is_novel: bool | None


@dataclass
class CampaignContext:
    cfg: MissionConfig
    db: CandidateDB
    notebook: LabNotebook
    iteration: int = 0
    relaxations_used: int = 0
    structures: dict[str, Proposed] = field(default_factory=dict)

    def start_iteration(self, i: int) -> None:
        self.iteration = i
        self.relaxations_used = 0

    @property
    def relaxations_left(self) -> int:
        return self.cfg.budget.max_relaxations_per_iteration - self.relaxations_used


def build_registry(ctx: CampaignContext) -> ToolRegistry:
    reg = ToolRegistry()
    cfg = ctx.cfg
    has_mp_key = bool(os.environ.get("MP_API_KEY"))

    # -- read_notebook ------------------------------------------------------
    def read_notebook(last_n_entries: int = 10) -> dict:
        return {"notebook": ctx.notebook.read(last_n_entries=last_n_entries)}

    reg.register(
        ToolSpec(
            name="read_notebook",
            description=(
                "Read the lab notebook — your memory of previous iterations: "
                "hypotheses tried, results observed, reflections recorded. "
                "Check it before proposing candidates."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "last_n_entries": {
                        "type": "integer",
                        "description": "How many most-recent entries to return (default 10)",
                    }
                },
            },
        ),
        read_notebook,
    )

    # -- write_notebook -----------------------------------------------------
    def write_notebook(entry_type: str, text: str) -> dict:
        ctx.notebook.write(entry_type, ctx.iteration, text)
        return {"recorded": entry_type}

    reg.register(
        ToolSpec(
            name="write_notebook",
            description=(
                "Record an entry in the lab notebook. Use entry_type 'hypothesis' "
                "before proposing candidates (state the chemical reasoning), "
                "'observation' after evaluating them, and 'reflection' at the end "
                "of an iteration (what worked, what to try next)."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "entry_type": {
                        "type": "string",
                        "enum": ["hypothesis", "observation", "reflection", "decision"],
                    },
                    "text": {"type": "string"},
                },
                "required": ["entry_type", "text"],
            },
        ),
        write_notebook,
    )

    # -- search_known_materials ---------------------------------------------
    def search_known_materials(chemsys_or_formula: str) -> dict:
        if not has_mp_key:
            return {"error": "MP_API_KEY not set; database search unavailable"}
        from pymatgen.core import Composition

        from matdiscover.tools.mp_search import search_known_materials as _search

        # rediscovery hold-out: masked materials must not leak via search
        masked = {Composition(f).reduced_formula
                  for f in cfg.evaluation.holdout_formulas}
        results = [m for m in _search(chemsys_or_formula)
                   if Composition(m.formula).reduced_formula not in masked]
        return {
            "count": len(results),
            "materials": [
                {
                    "formula": m.formula,
                    "band_gap_ev": m.band_gap,
                    "e_above_hull": m.energy_above_hull,
                    "is_stable": m.is_stable,
                }
                for m in results[:25]
            ],
        }

    reg.register(
        ToolSpec(
            name="search_known_materials",
            description=(
                "Search the Materials Project database of known materials by "
                "chemical system (e.g. 'Cu-In-Se') or formula (e.g. 'CuInSe2'). "
                "Use this to ground hypotheses in what is already known."
            ),
            input_schema={
                "type": "object",
                "properties": {"chemsys_or_formula": {"type": "string"}},
                "required": ["chemsys_or_formula"],
            },
        ),
        search_known_materials,
    )

    # -- propose_candidates --------------------------------------------------
    def propose_candidates(substitutions: dict, hypothesis: str,
                           prototype: str = "chalcopyrite-CuInSe2") -> dict:
        proto = get_prototype(prototype)
        subs = {el: (reps if isinstance(reps, list) else [reps])
                for el, reps in substitutions.items()}
        cands = substitute_prototype(
            proto, prototype, subs, cfg,
            max_candidates=cfg.budget.max_candidates_proposed_per_iteration,
        )
        results = filter_candidates([c.formula for c in cands], cfg)

        passed, rejected = [], []
        for cand, res in zip(cands, results):
            if ctx.db.already_seen(cand.formula):
                rejected.append({"formula": cand.formula,
                                 "reasons": ["already considered this campaign"]})
                continue
            if not res.passed:
                rejected.append({"formula": cand.formula, "reasons": res.reasons})
                ctx.db.add(CandidateRow(
                    iteration=ctx.iteration, formula=cand.formula,
                    status="filtered_out", parent_prototype=prototype,
                    substitution=cand.substitution, hypothesis=hypothesis,
                    filter_reasons=res.reasons,
                ))
                continue
            novel = None
            if has_mp_key:
                from matdiscover.tools.mp_search import is_novel

                novel = is_novel(
                    cand.formula,
                    holdout=frozenset(cfg.evaluation.holdout_formulas),
                )
            ctx.structures[cand.formula] = Proposed(
                structure=cand.structure, hypothesis=hypothesis,
                prototype=prototype, substitution=cand.substitution, is_novel=novel,
            )
            ctx.db.add(CandidateRow(
                iteration=ctx.iteration, formula=cand.formula, status="proposed",
                parent_prototype=prototype, substitution=cand.substitution,
                hypothesis=hypothesis, is_novel=novel,
            ))
            passed.append({"formula": cand.formula, "novel_vs_materials_project": novel})

        return {
            "prototype": prototype,
            "proposed": passed,
            "rejected": rejected,
            "note": (
                f"{len(passed)} candidates ready for evaluate_candidates; "
                f"relaxation budget left this iteration: {ctx.relaxations_left}"
            ),
        }

    reg.register(
        ToolSpec(
            name="propose_candidates",
            description=(
                "Generate candidate materials by element substitution on a known "
                "prototype structure, with charge-balance and chemistry filters "
                "applied automatically. State your hypothesis for WHY these "
                "substitutions should hit the target. Returns which candidates "
                f"passed filters. Available prototypes: {sorted(PROTOTYPES)}. "
                "substitutions maps a prototype element to replacement element(s), "
                'e.g. {"In": ["Ga", "Al"], "Se": ["S"]}.'
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "substitutions": {
                        "type": "object",
                        "description": "prototype element -> list of replacements",
                    },
                    "hypothesis": {
                        "type": "string",
                        "description": "chemical reasoning behind this batch",
                    },
                    "prototype": {
                        "type": "string",
                        "enum": sorted(PROTOTYPES),
                    },
                },
                "required": ["substitutions", "hypothesis"],
            },
        ),
        propose_candidates,
    )

    # -- evaluate_candidates --------------------------------------------------
    def evaluate_candidates(formulas: list[str]) -> dict:
        lo, hi = cfg.target.band_gap_ev
        out, skipped = [], []
        for formula in formulas:
            if formula not in ctx.structures:
                skipped.append({"formula": formula,
                                "reason": "not a proposed candidate (propose it first)"})
                continue
            if ctx.relaxations_left <= 0:
                skipped.append({"formula": formula,
                                "reason": "relaxation budget for this iteration exhausted"})
                continue
            ctx.relaxations_used += 1
            prop = ctx.structures[formula]
            s = relax_and_score(
                prop.structure,
                max_steps=cfg.budget.relaxation_max_steps,
                with_hull=has_mp_key,
            )
            row = CandidateRow(
                iteration=ctx.iteration, formula=formula,
                status="error" if s.error else "scored",
                parent_prototype=prop.prototype, substitution=prop.substitution,
                hypothesis=prop.hypothesis, is_novel=prop.is_novel,
                converged=s.converged,
                formation_energy_per_atom=s.formation_energy_per_atom,
                e_above_hull=s.e_above_hull, band_gap_ev=s.band_gap_ev,
                error=s.error,
            )
            ctx.db.add(row)
            if s.error:
                out.append({"formula": formula, "error": s.error})
                continue
            on_target_gap = s.band_gap_ev is not None and lo <= s.band_gap_ev <= hi
            near_hull = (
                s.e_above_hull is not None
                and s.e_above_hull <= cfg.target.e_above_hull_max_ev_per_atom
            )
            out.append({
                "formula": formula,
                "converged": s.converged,
                "formation_energy_ev_per_atom": _r(s.formation_energy_per_atom),
                "e_above_hull_ev_per_atom": _r(s.e_above_hull),
                "band_gap_ev": _r(s.band_gap_ev),
                "gap_in_target_window": on_target_gap,
                "near_stable": near_hull,
            })
        return {
            "results": out,
            "skipped": skipped,
            "relaxation_budget_left": ctx.relaxations_left,
            "target": {"band_gap_ev": [lo, hi],
                       "e_above_hull_max": cfg.target.e_above_hull_max_ev_per_atom},
        }

    reg.register(
        ToolSpec(
            name="evaluate_candidates",
            description=(
                "Run the physics evaluation on proposed candidates: CHGNet structure "
                "relaxation, formation energy, energy above convex hull (stability), "
                "and HSE-fidelity band gap. This is the expensive step — each "
                "evaluation costs one unit of the per-iteration relaxation budget. "
                "Prioritize the candidates your hypothesis is most confident about."
            ),
            input_schema={
                "type": "object",
                "properties": {
                    "formulas": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "formulas previously returned by propose_candidates",
                    }
                },
                "required": ["formulas"],
            },
        ),
        evaluate_candidates,
    )

    # -- get_top_candidates ---------------------------------------------------
    def get_top_candidates(limit: int = 10) -> dict:
        rows = ctx.db.top_candidates(limit=limit)
        return {
            "top_candidates": [
                {
                    "formula": r["formula"],
                    "iteration": r["iteration"],
                    "e_above_hull": _r(r["e_above_hull"]),
                    "band_gap_ev": _r(r["band_gap_ev"]),
                    "hypothesis": r["hypothesis"],
                }
                for r in rows
            ]
        }

    reg.register(
        ToolSpec(
            name="get_top_candidates",
            description=(
                "List the best candidates found so far across the whole campaign "
                "(novel, converged, sorted by stability)."
            ),
            input_schema={
                "type": "object",
                "properties": {"limit": {"type": "integer"}},
            },
        ),
        get_top_candidates,
    )

    return reg


def _r(x: float | None, digits: int = 3) -> float | None:
    # cast: numpy floats aren't JSON-serializable and stringify via default=str
    return None if x is None else round(float(x), digits)
