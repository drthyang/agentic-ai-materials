"""Athanor: agentic AI for materials discovery."""

import os
from pathlib import Path

__version__ = "0.1.0"


def _load_dotenv() -> None:
    """Load KEY=value pairs from a repo-root .env without overriding the shell env."""
    env = Path(__file__).resolve().parents[2] / ".env"
    if not env.exists():
        return
    for line in env.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            os.environ.setdefault(k.strip(), v.strip())


_load_dotenv()
