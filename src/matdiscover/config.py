"""Mission configuration: pydantic models over config/mission.yaml."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, field_validator


class MissionInfo(BaseModel):
    name: str
    description: str


class Target(BaseModel):
    band_gap_ev: tuple[float, float]
    band_gap_ideal_ev: float
    e_above_hull_max_ev_per_atom: float


class Chemistry(BaseModel):
    allowed_elements: list[str]
    excluded_elements: list[str] = []
    max_elements_per_compound: int = 4
    max_atoms_per_cell: int = 50

    @field_validator("allowed_elements", "excluded_elements", mode="before")
    @classmethod
    def _flatten_comma_lists(cls, v: list[str]) -> list[str]:
        # YAML entries may be comma-separated strings ("Cu, Ag, Zn") for readability.
        out: list[str] = []
        for item in v:
            out.extend(s.strip() for s in str(item).split(",") if s.strip())
        return out


class Budget(BaseModel):
    iterations: int = 10
    max_candidates_proposed_per_iteration: int = 50
    max_relaxations_per_iteration: int = 20
    relaxation_max_steps: int = 200


class Paths(BaseModel):
    db: Path = Path("data/candidates.db")
    notebook: Path = Path("data/lab_notebook.md")
    reports: Path = Path("data/reports")


class MissionConfig(BaseModel):
    mission: MissionInfo
    target: Target
    chemistry: Chemistry
    budget: Budget
    paths: Paths = Paths()

    @property
    def usable_elements(self) -> list[str]:
        excluded = set(self.chemistry.excluded_elements)
        return [e for e in self.chemistry.allowed_elements if e not in excluded]


def load_mission(path: str | Path = "config/mission.yaml") -> MissionConfig:
    with open(path) as f:
        raw = yaml.safe_load(f)
    return MissionConfig.model_validate(raw)
