"""Novelty audit of benchmark hits against open databases (no API credit).

    uv run python scripts/novelty_audit.py results/<study>/arms-pv.json [more specs...]

A "hit" is MP-novel by construction: the shared hit rule requires that the
composition is absent from Materials Project. That is a database-membership
test, not novelty to science. This audit asks two more open databases about
every distinct hit composition in the given arm specs (the same specs
aggregate_ablation.py reads):

- **OQMD** (oqmd.org, public REST API): is there any entry with the same
  reduced composition? Does any carry an ICSD id, i.e. was it imported from
  an experimentally reported ICSD structure? Is any in the same space group
  as the intended structure type (the campaign's substitution applied to a
  correct bulk cell of its prototype)?
- **COD** (Crystallography Open Database, OPTIMADE): any experimental
  structure whose composition matches within 0.03 atomic fraction per
  element (COD records partial occupancies, e.g. Cu0.978InSe1.988)?

ICSD itself is licensed and is not queried; an OQMD entry with an ICSD id is
the closest open proxy. Every response is cached under data/novelty_cache/,
so the audit re-runs offline and is reviewable. Writes
<spec>-novelty.csv and novelty-audit.md next to the first spec.
"""

from __future__ import annotations

import csv
import hashlib
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from pymatgen.core import Composition
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer

from athanor.config import load_mission
from athanor.db import CandidateDB
from athanor.metrics import row_flags

CACHE = Path("data/novelty_cache")
OQMD_URL = "https://oqmd.org/oqmdapi/formationenergy"
COD_URL = "https://www.crystallography.net/cod/optimade/v1/structures"
COD_TOL = 0.03


def _get_json(url: str, kind: str, retries: int = 200, wait_s: float = 20.0) -> dict:
    key = hashlib.sha1(url.encode()).hexdigest()[:24]
    path = CACHE / kind / f"{key}.json"
    if path.exists():
        return json.loads(path.read_text())["response"]
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "athanor-novelty-audit"})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.loads(r.read().decode())
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"url": url, "response": data}, indent=1))
            return data
        except Exception as exc:  # 5xx / timeouts: OQMD is often briefly down
            last = exc
            time.sleep(wait_s)
    raise RuntimeError(f"{kind} unreachable after {retries} tries: {last}")


def _alpha_formula(comp: Composition) -> str:
    """Integer reduced formula, elements alphabetical (OPTIMADE/OQMD style)."""
    red = comp.reduced_composition
    return "".join(f"{el}{'' if n == 1 else int(n)}"
                   for el, n in sorted((e.symbol, a) for e, a in red.items()))


def oqmd_lookup(comp: Composition) -> list[dict]:
    q = urllib.parse.urlencode({
        "composition": _alpha_formula(comp),
        "fields": "name,entry_id,icsd_id,spacegroup,prototype,delta_e,stability,natoms",
        "limit": 100, "format": "json",
    })
    data = _get_json(f"{OQMD_URL}?{q}", "oqmd")
    want = comp.reduced_composition
    # verify client-side: keep only exact reduced-composition matches
    return [d for d in data.get("data", [])
            if d.get("name") and Composition(d["name"]).reduced_composition.almost_equals(want)]


def cod_lookup(comp: Composition) -> list[dict]:
    els = sorted(e.symbol for e in comp.elements)
    filt = (f'elements HAS ALL {",".join(chr(34) + e + chr(34) for e in els)} '
            f"AND nelements={len(els)}")
    url = (f"{COD_URL}?{urllib.parse.urlencode({'filter': filt, 'page_limit': 100})}"
           "&response_fields=chemical_formula_descriptive")
    hits, target = [], comp.fractional_composition
    while url:
        data = _get_json(url, "cod")
        for d in data.get("data", []):
            f = (d.get("attributes") or {}).get("chemical_formula_descriptive")
            try:
                c = Composition(f.replace(" ", "")).fractional_composition
            except Exception:
                continue
            if all(abs(c[e] - target[e]) <= COD_TOL for e in set(c) | set(target)):
                hits.append({"id": d["id"], "formula": f})
        url = (data.get("links") or {}).get("next")
        if isinstance(url, dict):
            url = url.get("href")
    return hits


def built_spacegroup(prototype: str, substitution: dict) -> str | None:
    """Space group of the intended structure type: the substitution applied
    to a correct bulk cell of the prototype. (The repo's own 8-atom
    chalcopyrite/kesterite cells have P2 symmetry and a vacuum gap — see
    structure_audit.py — so their symmetry would match nothing meaningful.)"""
    try:
        from structure_audit import build

        return SpacegroupAnalyzer(build(prototype, substitution),
                                  symprec=0.1).get_space_group_symbol()
    except Exception:
        return None


def collect_hits(spec_path: Path) -> dict[str, dict]:
    spec = json.loads(spec_path.read_text())
    cfg = load_mission(spec.get("mission", "config/mission.yaml"))
    out: dict[str, dict] = {}
    for arm, a in spec["arms"].items():
        kind = "agent" if a["db"] == "agent.db" else "baseline"
        for run in a["runs"]:
            db = CandidateDB(Path(run) / a["db"])
            for r in db._conn.execute("SELECT * FROM candidates WHERE status='scored'"):
                r = dict(r)
                if not row_flags(r, cfg)["hit"]:
                    continue
                red = Composition(r["formula"]).reduced_formula
                h = out.setdefault(red, {
                    "formula": red, "mission": cfg.mission.name, "kinds": set(),
                    "arms": set(), "runs": 0, "gap_ev": r["band_gap_ev"],
                    "e_above_hull": r["e_above_hull"], "prototype": r["parent_prototype"],
                    "substitution": json.loads(r["substitution"] or "{}"),
                })
                h["kinds"].add(kind)
                h["arms"].add(arm)
                h["runs"] += 1
            db.close()
    return out


def main(specs: list[str]) -> None:
    rows = []
    for spec in specs:
        hits = collect_hits(Path(spec))
        for h in sorted(hits.values(), key=lambda h: h["formula"]):
            comp = Composition(h["formula"])
            oq = oqmd_lookup(comp)
            cod = cod_lookup(comp)
            sg = built_spacegroup(h["prototype"], h["substitution"])
            rows.append({
                "mission": h["mission"], "formula": h["formula"],
                "found_by": "+".join(sorted(h["kinds"])), "hit_runs": h["runs"],
                "gap_ev": round(h["gap_ev"], 2), "e_above_hull": round(h["e_above_hull"], 3),
                "built_spacegroup": sg,
                "oqmd_entries": len(oq),
                "oqmd_icsd_entries": sum(1 for d in oq if d.get("icsd_id")),
                "oqmd_same_spacegroup": sum(1 for d in oq if sg and d.get("spacegroup") == sg),
                "oqmd_spacegroups": " ".join(sorted({str(d.get("spacegroup")) for d in oq})),
                "cod_matches": len(cod),
                "cod_ids": " ".join(c["id"] for c in cod[:5]),
            })
            print(f"{h['mission']:<16} {h['formula']:<14} oqmd={len(oq)} "
                  f"icsd={rows[-1]['oqmd_icsd_entries']} cod={len(cod)}", flush=True)

    outdir = Path(specs[0]).parent
    with open(outdir / "novelty-audit.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(summarize(rows))


def summarize(rows: list[dict]) -> str:
    lines = ["| mission | found by | distinct hits | in OQMD (any entry) "
             "| in OQMD with ICSD id | same space group in OQMD | in COD "
             "| absent from OQMD and COD |", "|---|---|---|---|---|---|---|---|"]
    groups: dict[tuple, list] = {}
    for r in rows:
        for who in ("agent", "baseline"):
            if who in r["found_by"]:
                groups.setdefault((r["mission"], who), []).append(r)
    for (mission, who), rs in sorted(groups.items()):
        lines.append(
            f"| {mission} | {who} | {len(rs)} | {sum(r['oqmd_entries'] > 0 for r in rs)} "
            f"| {sum(r['oqmd_icsd_entries'] > 0 for r in rs)} "
            f"| {sum(r['oqmd_same_spacegroup'] > 0 for r in rs)} "
            f"| {sum(r['cod_matches'] > 0 for r in rs)} "
            f"| {sum(r['oqmd_entries'] == 0 and r['cod_matches'] == 0 for r in rs)} |")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))  # for structure_audit.build
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
