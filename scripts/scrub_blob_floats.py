#!/usr/bin/env python3
"""Scrub legacy float32 BLOBs out of candidate databases. Stdlib only.

Campaigns run before the numpy coercion in db.add() (the July 2026 runs)
stored CHGNet's float32 values as raw 4-byte BLOBs: sqlite3 binds numpy
scalars through the buffer protocol instead of as numbers. This decodes
every such BLOB in place to a REAL. It changes no measurement — each BLOB
is the little-endian IEEE bytes of the recorded value — and it is
idempotent: a clean database reports zero and is left untouched.

Usage:
    python3 scripts/scrub_blob_floats.py              # every *.db under data/
    python3 scripts/scrub_blob_floats.py PATH [...]   # specific databases

Run it while no campaign is writing to the database.
"""

from __future__ import annotations

import pathlib
import sqlite3
import struct
import sys

NUM_COLS = ("formation_energy_per_atom", "e_above_hull", "band_gap_ev")


def scrub(path: pathlib.Path) -> int | None:
    """Decode float BLOBs in one database; return count, or None if skipped."""
    conn = sqlite3.connect(path)
    try:
        tables = {r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'")}
        if "candidates" not in tables:
            return None  # mp_cache / unrelated database
        n = 0
        for col in NUM_COLS:
            rows = conn.execute(
                f"SELECT rowid, {col} FROM candidates WHERE typeof({col})='blob'"
            ).fetchall()
            for rowid, blob in rows:
                fmt = {4: "<f", 8: "<d"}.get(len(blob))
                if fmt is None:  # not IEEE float bytes — never guess
                    raise SystemExit(
                        f"{path}: rowid {rowid} column {col} holds a "
                        f"{len(blob)}-byte blob; refusing to decode it")
                conn.execute(
                    f"UPDATE candidates SET {col}=? WHERE rowid=?",
                    (struct.unpack(fmt, blob)[0], rowid))
                n += 1
        conn.commit()
        return n
    finally:
        conn.close()


def main(argv: list[str]) -> int:
    paths = ([pathlib.Path(a) for a in argv]
             or sorted(pathlib.Path("data").rglob("*.db")))
    if not paths:
        print("no databases found (run from the repo root, or pass paths)")
        return 1
    total = 0
    for p in paths:
        if not p.exists():
            print(f"{p}: not found")
            return 1
        try:
            n = scrub(p)
        except sqlite3.OperationalError as exc:
            print(f"{p}: {exc} — is a campaign writing to it?")
            return 1
        if n is None:
            print(f"{p}: no candidates table, skipped")
        else:
            print(f"{p}: {n} blob value(s) decoded to REAL")
            total += n
    print(f"done: {total} value(s) repaired")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
