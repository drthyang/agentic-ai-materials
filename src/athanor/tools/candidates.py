"""Candidate generation: element substitution on known prototype structures.

Strategy: start from an experimentally known prototype (e.g., chalcopyrite
CuInSe2), swap elements site-by-site within the mission palette, and return new
Structure objects. Keeping the prototype geometry means cells stay small and
CHGNet relaxations stay cheap.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from pymatgen.core import Structure

from athanor.config import MissionConfig


@dataclass
class Candidate:
    formula: str
    structure: Structure
    parent_prototype: str
    substitution: dict[str, str]  # original element -> replacement


def substitute_prototype(
    prototype: Structure,
    prototype_name: str,
    substitutions: dict[str, list[str]],
    cfg: MissionConfig,
    max_candidates: int | None = None,
) -> list[Candidate]:
    """Enumerate substituted variants of a prototype structure.

    `substitutions` maps each element in the prototype to the list of allowed
    replacements (include the original symbol to keep it as an option).
    The identity substitution (nothing changed) is skipped.
    """
    proto_elements = sorted({site.specie.symbol for site in prototype})
    for el in substitutions:
        if el not in proto_elements:
            raise ValueError(f"{el} not in prototype {prototype_name} ({proto_elements})")

    palette = set(cfg.usable_elements)
    slots = [(el, [r for r in reps if r in palette]) for el, reps in substitutions.items()]

    out: list[Candidate] = []
    for combo in product(*(reps for _, reps in slots)):
        mapping = {el: rep for (el, _), rep in zip(slots, combo)}
        if all(k == v for k, v in mapping.items()):
            continue  # identity
        # Two prototype elements collapsing to one replacement changes the
        # structure type; allow it only if it stays within element budget.
        new_struct = prototype.copy()
        new_struct.replace_species({k: v for k, v in mapping.items() if k != v})
        comp = new_struct.composition
        if len(comp.elements) > cfg.chemistry.max_elements_per_compound:
            continue
        if len(new_struct) > cfg.chemistry.max_atoms_per_cell:
            continue
        out.append(
            Candidate(
                formula=comp.reduced_formula,
                structure=new_struct,
                parent_prototype=prototype_name,
                substitution={k: v for k, v in mapping.items() if k != v},
            )
        )
        if max_candidates is not None and len(out) >= max_candidates:
            break

    # Same reduced formula can arise from different substitution routes; keep first.
    seen: set[str] = set()
    deduped: list[Candidate] = []
    for c in out:
        if c.formula not in seen:
            seen.add(c.formula)
            deduped.append(c)
    return deduped
