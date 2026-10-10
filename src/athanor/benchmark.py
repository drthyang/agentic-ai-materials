"""Phase 3 benchmark: agent vs baselines under the same relaxation budget.

Each strategy gets its own DB/notebook under data/benchmark/<stamp>/ so runs
never contaminate each other; metrics come from the shared definition in
metrics.py. Output: printed table + markdown summary + bar plot.
"""

from __future__ import annotations

import csv
import json
import logging
import os
import subprocess
from contextlib import contextmanager
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

from athanor.baselines import BayesOptBaseline, RandomBaseline, SimilarityBaseline
from athanor.config import MissionConfig
from athanor.db import CandidateDB
from athanor.metrics import CampaignMetrics, comparison_table, compute_metrics

log = logging.getLogger("athanor.benchmark")

_LOCK = Path("data/benchmark/.lock")

BASELINES = {cls.name: cls for cls in (RandomBaseline, SimilarityBaseline, BayesOptBaseline)}

# Columns of the API spend ledger (no secrets: token counts and prices only).
LEDGER_FIELDS = [
    "finished_utc", "run_dir", "mission", "backend", "model", "effort", "calls",
    "input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens",
    "output_tokens", "cost_usd", "status",
]

# Reserved headroom under a global spend cap: one request can overshoot the
# per-run stop by its own cost before the check fires.
_CAP_MARGIN_USD = 0.50


@contextmanager
def _benchmark_lock():
    """Refuse to start when another benchmark is running (concurrent runs
    share Ollama/GPU and corrupt each other's wall-clock — learned the hard
    way on 2026-07-07). Stale locks from dead processes are reclaimed."""
    if _LOCK.exists():
        try:
            pid = int(_LOCK.read_text().strip())
            os.kill(pid, 0)  # raises if pid is dead
            raise SystemExit(
                f"another benchmark is already running (pid {pid}, {_LOCK}). "
                "Wait for it or remove the lock file if you are sure it is dead."
            )
        except (ValueError, ProcessLookupError, PermissionError):
            log.warning("reclaiming stale benchmark lock %s", _LOCK)
    _LOCK.parent.mkdir(parents=True, exist_ok=True)
    _LOCK.write_text(str(os.getpid()))
    try:
        yield
    finally:
        _LOCK.unlink(missing_ok=True)


def run_benchmark(
    cfg: MissionConfig,
    iterations: int | None = None,
    include_agent: bool = True,
    seed: int = 0,
    baselines: list[str] | None = None,
    tag: str = "",
    ledger: Path | None = None,
    spend_cap_usd: float | None = None,
) -> Path:
    """Run strategies under the same relaxation cap; returns the results directory.

    baselines: which non-LLM baselines to run (default: all). Baselines are
    deterministic per seed, so agent-only replicates can pass [] instead of
    recomputing them. tag: appended to the run directory name.
    ledger / spend_cap_usd: append the agent's API spend to a CSV ledger, and
    refuse to start (or stop mid-run) once the ledger total reaches the cap.
    """
    names = list(BASELINES) if baselines is None else list(baselines)
    unknown = [n for n in names if n not in BASELINES]
    if unknown:
        raise ValueError(f"unknown baselines {unknown}; choose from {sorted(BASELINES)}")
    with _benchmark_lock():
        return _run_benchmark_locked(cfg, iterations, include_agent, seed,
                                     names, tag, ledger, spend_cap_usd)


def _run_benchmark_locked(
    cfg: MissionConfig,
    iterations: int | None,
    include_agent: bool,
    seed: int,
    baselines: list[str],
    tag: str,
    ledger: Path | None,
    spend_cap_usd: float | None,
) -> Path:
    iterations = iterations or cfg.budget.iterations
    remaining = None
    if include_agent and spend_cap_usd is not None and cfg.llm.backend == "anthropic":
        spent = ledger_total_usd(ledger) if ledger else 0.0
        remaining = spend_cap_usd - spent - _CAP_MARGIN_USD
        if remaining <= 0:
            raise SystemExit(
                f"spend cap reached: ledger shows ${spent:.2f} of ${spend_cap_usd:.2f} "
                f"(keeping ${_CAP_MARGIN_USD:.2f} headroom); not starting"
            )
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + f"-seed{seed}"
    if tag:
        stamp += f"-{tag}"
    outdir = Path("data/benchmark") / stamp
    outdir.mkdir(parents=True, exist_ok=True)
    # stable pointer for the dashboard: athanor dashboard --latest
    latest = Path("data/benchmark/latest")
    latest.unlink(missing_ok=True)
    latest.symlink_to(stamp)
    _write_run_config(outdir, cfg, iterations, seed, baselines, include_agent)

    results: list[CampaignMetrics] = []

    for name in baselines:
        cls = BASELINES[name]
        db = CandidateDB(outdir / f"{cls.name}.db")
        log.info("--- running %s baseline (%d iterations) ---", cls.name, iterations)
        cls(cfg, db, seed=seed).run(iterations)
        results.append(compute_metrics(cls.name, db, cfg))
        db.close()

    if include_agent:
        from athanor.agent.loop import run_campaign
        from athanor.llm import make_backend

        agent_cfg = cfg.model_copy(deep=True)
        agent_cfg.paths.db = outdir / "agent.db"
        agent_cfg.paths.notebook = outdir / "agent_notebook.md"
        agent_cfg.paths.reports = outdir
        log.info("--- running agent campaign (%d iterations, %s/%s) ---",
                 iterations, cfg.llm.backend, cfg.llm.model)
        backend = make_backend(cfg.llm)
        if remaining is not None:
            cap = getattr(backend, "max_cost_usd", None)
            backend.max_cost_usd = remaining if cap is None else min(cap, remaining)
            log.info("agent spend cap for this run: $%.2f", backend.max_cost_usd)
        if hasattr(backend, "usage_path"):
            backend.usage_path = outdir / "usage.json"
        run_stats: dict = {}
        status = "error"
        try:
            run_campaign(agent_cfg, backend, iterations=iterations, run_stats=run_stats)
            status = "ok" if not run_stats.get("aborted_turns") else "aborted_turns"
        finally:
            (outdir / "agent_stats.json").write_text(json.dumps(run_stats, indent=1))
            if hasattr(backend, "usage_summary"):
                usage = backend.usage_summary()
                (outdir / "usage.json").write_text(json.dumps(usage, indent=1))
                if ledger:
                    append_ledger(ledger, outdir, cfg.mission.name, usage, status)
        db = CandidateDB(agent_cfg.paths.db)
        results.append(compute_metrics(f"agent ({cfg.llm.model})", db, cfg))
        db.close()

    (outdir / "metrics.json").write_text(
        json.dumps([asdict(m) for m in results], indent=1))

    table = comparison_table(results)
    summary = (
        f"# Benchmark: {cfg.mission.name}\n\n"
        f"budget: {iterations} iterations x "
        f"{cfg.budget.max_relaxations_per_iteration} relaxations\n\n"
        f"{table}\n\n"
        f"hit = converged + gap in {list(cfg.target.band_gap_ev)} eV + "
        f"e_above_hull <= {cfg.target.e_above_hull_max_ev_per_atom} eV/atom + "
        f"not a confirmed-known material\n"
    )
    (outdir / "benchmark.md").write_text(summary)
    _plot(results, outdir / "benchmark.png")
    print("\n" + summary)
    return outdir


def _git_commit() -> str | None:
    try:
        out = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                             text=True, timeout=10, check=True)
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "src", "config"],
                               capture_output=True, text=True, timeout=10).stdout.strip()
        return out.stdout.strip() + ("-dirty" if dirty else "")
    except Exception:
        return None


def _write_run_config(outdir: Path, cfg: MissionConfig, iterations: int, seed: int,
                      baselines: list[str], include_agent: bool) -> None:
    """Record exactly what ran: the effective (post-override) mission config,
    code version, and arm settings. Contains no credentials — the mission
    config never holds keys; those come from the environment."""
    snapshot = {
        "started_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "git_commit": _git_commit(),
        "iterations": iterations,
        "seed": seed,
        "baselines": baselines,
        "include_agent": include_agent,
        "mission_config": cfg.model_dump(mode="json"),
    }
    (outdir / "run_config.json").write_text(json.dumps(snapshot, indent=1))


def ledger_total_usd(path: Path | None) -> float:
    if path is None or not Path(path).exists():
        return 0.0
    with open(path, newline="") as f:
        return sum(float(r["cost_usd"] or 0) for r in csv.DictReader(f))


def append_ledger(path: Path, run_dir: Path, mission: str, usage: dict,
                  status: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    new = not path.exists()
    row = {
        "finished_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "run_dir": str(run_dir),
        "mission": mission,
        "status": status,
        **{k: usage.get(k) for k in LEDGER_FIELDS
           if k not in ("finished_utc", "run_dir", "mission", "status")},
    }
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=LEDGER_FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def _plot(results: list[CampaignMetrics], path: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    names = [m.name for m in results]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.5))
    ax1.bar(names, [m.hits for m in results], color="#4C72B0")
    ax1.set_title("hits (novel, near-stable, on-target)")
    ax2.bar(names, [m.hits_per_100_relaxations for m in results], color="#55A868")
    ax2.set_title("hits per 100 relaxations")
    for ax in (ax1, ax2):
        ax.tick_params(axis="x", rotation=15)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
