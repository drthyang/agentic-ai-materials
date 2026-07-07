"""Command-line entry point.

Phase 1 exposes environment checks; the campaign runner lands in Phase 2:
    matdiscover check          # verify env, keys, model availability
    matdiscover run ...        # (Phase 2) run a discovery campaign
"""

from __future__ import annotations

import argparse
import os
import sys


def cmd_check(_args: argparse.Namespace) -> int:
    from matdiscover.config import load_mission

    cfg = load_mission("config/mission.yaml")
    print(f"mission: {cfg.mission.name}")
    print(f"palette: {len(cfg.usable_elements)} elements")

    ok = True
    if os.environ.get("MP_API_KEY"):
        print("MP_API_KEY: set")
    else:
        ok = False
        print("MP_API_KEY: MISSING — novelty/hull checks disabled "
              "(get a free key at https://materialsproject.org/api)")
    if os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY: set")
    else:
        print("ANTHROPIC_API_KEY: missing (only needed for the agent loop, Phase 2)")

    try:
        import chgnet  # noqa: F401
        import matgl  # noqa: F401
        print("models: chgnet + matgl importable")
    except ImportError as exc:
        ok = False
        print(f"models: import failure: {exc}")

    print("status:", "ready" if ok else "issues found (see above)")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(prog="matdiscover")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="verify environment and configuration")

    args = parser.parse_args()
    if args.command == "check":
        sys.exit(cmd_check(args))


if __name__ == "__main__":
    main()
