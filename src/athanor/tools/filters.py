"""Cheap pre-compute filters: charge balance, electronegativity, mission chemistry rules.

These run before any ML-potential compute is spent, so they should be fast and
strict. A composition that fails here is never relaxed.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import smact
from smact.screening import smact_validity
from pymatgen.core import Composition

from athanor.config import MissionConfig


@dataclass
class FilterResult:
    formula: str
    passed: bool
    reasons: list[str] = field(default_factory=list)


def check_composition(formula: str, cfg: MissionConfig) -> FilterResult:
    """Validate one composition against mission chemistry rules + SMACT sanity."""
    reasons: list[str] = []
    try:
        comp = Composition(formula)
    except Exception as exc:
        return FilterResult(formula, False, [f"unparseable formula: {exc}"])

    elements = [el.symbol for el in comp.elements]

    excluded = set(cfg.chemistry.excluded_elements) & set(elements)
    if excluded:
        reasons.append(f"contains excluded elements: {sorted(excluded)}")

    allowed = set(cfg.usable_elements)
    outside = set(elements) - allowed
    if outside:
        reasons.append(f"elements outside mission palette: {sorted(outside)}")

    if len(elements) > cfg.chemistry.max_elements_per_compound:
        reasons.append(
            f"{len(elements)} elements > max {cfg.chemistry.max_elements_per_compound}"
        )

    if len(elements) < 2:
        reasons.append("single-element composition is not a discovery candidate")

    if not reasons and not _smact_valid(comp):
        reasons.append("fails SMACT charge-balance/electronegativity screen")

    return FilterResult(formula, passed=not reasons, reasons=reasons)


def _smact_valid(comp: Composition) -> bool:
    """SMACT validity: some charge-balanced oxidation-state assignment exists."""
    try:
        return smact_validity(comp)
    except TypeError:
        # Older smact versions want (symbols, counts) rather than a Composition.
        el_amt = comp.get_el_amt_dict()
        symbols = tuple(el_amt.keys())
        counts = tuple(int(v) for v in el_amt.values())
        return smact_validity((symbols, counts))


def filter_candidates(formulas: list[str], cfg: MissionConfig) -> list[FilterResult]:
    """Batch-filter compositions; preserves input order."""
    return [check_composition(f, cfg) for f in formulas]
