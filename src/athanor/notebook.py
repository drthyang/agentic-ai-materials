"""The agent's lab notebook: append-only markdown, one entry per event.

The notebook is the agent's long-term memory across iterations and the
human-readable record of the campaign. Entries are timestamped and typed so
the agent (and tests) can parse them back.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ENTRY_TYPES = ("hypothesis", "observation", "reflection", "decision", "report")

_HEADER = re.compile(
    r"^\[(?P<type>\w+)\] iteration (?P<iteration>\d+) — (?P<when>.+?)\s*$"
)


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

    def entries(self, last_n: int | None = None) -> list[dict]:
        """Structured entries for the dashboard: newest last.

        Each dict: {type, iteration, when, text}. Blocks whose header doesn't
        match the write() format are skipped rather than crashing the page.
        """
        blocks = self.path.read_text().split("\n## ")[1:]
        out = []
        for block in blocks:
            head, _, body = block.partition("\n")
            m = _HEADER.match(head)
            if not m:
                continue
            out.append({
                "type": m["type"],
                "iteration": int(m["iteration"]),
                "when": m["when"],
                "text": body.strip(),
            })
        return out[-last_n:] if last_n is not None else out
