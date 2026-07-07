"""The agent's lab notebook: append-only markdown, one entry per event.

The notebook is the agent's long-term memory across iterations and the
human-readable record of the campaign. Entries are timestamped and typed so
the agent (and tests) can parse them back.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

ENTRY_TYPES = ("hypothesis", "observation", "reflection", "decision", "report")


class LabNotebook:
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("# Lab Notebook\n")

    def write(self, entry_type: str, iteration: int, text: str) -> None:
        if entry_type not in ENTRY_TYPES:
            raise ValueError(f"entry_type must be one of {ENTRY_TYPES}")
        stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        block = (
            f"\n## [{entry_type}] iteration {iteration} — {stamp}\n\n{text.strip()}\n"
        )
        with open(self.path, "a") as f:
            f.write(block)

    def read(self, last_n_entries: int | None = None) -> str:
        text = self.path.read_text()
        if last_n_entries is None:
            return text
        parts = text.split("\n## ")
        header, entries = parts[0], parts[1:]
        keep = entries[-last_n_entries:]
        return header + "".join("\n## " + e for e in keep)
