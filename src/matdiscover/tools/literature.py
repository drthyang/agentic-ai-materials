"""Literature search over the free Crossref API (no key required).

Grounds the agent's hypotheses in prior work: "has anyone made this?"
Results are cached on disk; failures return an error dict, never raise.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import httpx

_CACHE_DIR = Path("data/lit_cache")
_API = "https://api.crossref.org/works"


def search_literature(query: str, rows: int = 5) -> list[dict] | dict:
    """Search Crossref for works matching the query.

    Returns [{"title", "year", "doi", "container"}] or {"error": ...}.
    """
    rows = max(1, min(int(rows), 10))
    key = hashlib.sha256(f"{query}|{rows}".encode()).hexdigest()[:24]
    cache = _CACHE_DIR / f"{key}.json"
    if cache.exists():
        return json.loads(cache.read_text())

    try:
        resp = httpx.get(
            _API,
            params={"query": query, "rows": rows,
                    "select": "title,DOI,issued,container-title"},
            headers={"User-Agent": "matdiscover/0.1 (materials discovery research)"},
            timeout=20.0,
        )
        resp.raise_for_status()
        items = resp.json()["message"]["items"]
    except Exception as exc:
        return {"error": f"literature search failed: {type(exc).__name__}: {exc}"}

    results = []
    for it in items:
        issued = (it.get("issued", {}).get("date-parts") or [[None]])[0][0]
        results.append({
            "title": (it.get("title") or ["(untitled)"])[0][:300],
            "year": issued,
            "doi": it.get("DOI"),
            "container": (it.get("container-title") or [None])[0],
        })
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(results))
    return results
