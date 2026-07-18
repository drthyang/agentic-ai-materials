"""Command-line entry point.

    athanor check                    # verify env, keys, model availability
    athanor run --iterations 3       # run a discovery campaign
"""

from __future__ import annotations

import argparse
import os
import sys


def cmd_check(_args: argparse.Namespace) -> int:
    from athanor.config import load_mission

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


def cmd_run(args: argparse.Namespace) -> int:
    import logging

    from athanor.agent.loop import run_campaign
    from athanor.config import load_mission
    from athanor.llm import make_backend

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    cfg = load_mission(args.mission)
    if args.backend:
        cfg.llm.backend = args.backend
    if args.model:
        cfg.llm.model = args.model

    backend = make_backend(cfg.llm)
    print(f"mission: {cfg.mission.name} | backend: {cfg.llm.backend} "
          f"({cfg.llm.model}) | iterations: {args.iterations or cfg.budget.iterations}")
    report = run_campaign(cfg, backend, iterations=args.iterations)
    print(f"\ncampaign complete — report: {report}")
    return 0


def cmd_benchmark(args: argparse.Namespace) -> int:
    import logging

    from athanor.benchmark import run_benchmark
    from athanor.config import load_mission

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    cfg = load_mission(args.mission)
    outdir = run_benchmark(
        cfg, iterations=args.iterations,
        include_agent=not args.skip_agent, seed=args.seed,
    )
    print(f"benchmark artifacts: {outdir}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(prog="athanor")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="verify environment and configuration")

    run_p = sub.add_parser("run", help="run a discovery campaign")
    run_p.add_argument("--mission", default="config/mission.yaml")
    run_p.add_argument("--iterations", type=int, default=None,
                       help="override budget.iterations from mission config")
    run_p.add_argument("--backend", default=None,
                       help="override llm.backend (ollama | openai-compat | anthropic)")
    run_p.add_argument("--model", default=None, help="override llm.model")
    run_p.add_argument("--verbose", action="store_true")

    bench_p = sub.add_parser(
        "benchmark", help="agent vs random/similarity baselines at equal budget"
    )
    bench_p.add_argument("--mission", default="config/mission.yaml")
    bench_p.add_argument("--iterations", type=int, default=None)
    bench_p.add_argument("--seed", type=int, default=0)
    bench_p.add_argument("--skip-agent", action="store_true",
                         help="run only the non-LLM baselines")
    bench_p.add_argument("--verbose", action="store_true")

    dash_p = sub.add_parser("dashboard", help="live campaign dashboard (localhost)")
    dash_p.add_argument("--mission", default="config/mission.yaml")
    dash_p.add_argument("--port", type=int, default=8517)
    dash_p.add_argument("--db", default=None,
                        help="watch a specific campaign DB instead of the mission default")
    dash_p.add_argument("--notebook", default=None)
    dash_p.add_argument("--latest", action="store_true",
                        help="watch the agent leg of the most recent benchmark run")

    args = parser.parse_args()
    if args.command == "check":
        sys.exit(cmd_check(args))
    if args.command == "run":
        sys.exit(cmd_run(args))
    if args.command == "benchmark":
        sys.exit(cmd_benchmark(args))
    if args.command == "dashboard":
        from pathlib import Path

        from athanor.config import load_mission
        from athanor.dashboard import serve

        cfg = load_mission(args.mission)
        if args.latest:
            cfg.paths.db = Path("data/benchmark/latest/agent.db")
            cfg.paths.notebook = Path("data/benchmark/latest/agent_notebook.md")
        if args.db:
            cfg.paths.db = Path(args.db)
        if args.notebook:
            cfg.paths.notebook = Path(args.notebook)
        serve(cfg, port=args.port)
        sys.exit(0)


if __name__ == "__main__":
    main()
