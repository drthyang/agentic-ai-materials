"""Phase 3 benchmark: agent vs baselines at identical compute budget.

Each strategy gets its own DB/notebook under data/benchmark/<stamp>/ so runs
never contaminate each other; metrics come from the shared definition in
metrics.py. Output: printed table + markdown summary + bar plot.
"""

from __future__ import annotations

import logging
import os
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from athanor.baselines import BayesOptBaseline, RandomBaseline, SimilarityBaseline
from athanor.config import MissionConfig
from athanor.db import CandidateDB
from athanor.metrics import CampaignMetrics, comparison_table, compute_metrics

log = logging.getLogger("athanor.benchmark")

_LOCK = Path("data/benchmark/.lock")


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
) -> Path:
    """Run all strategies at equal budget; returns the results directory."""
    with _benchmark_lock():
        return _run_benchmark_locked(cfg, iterations, include_agent, seed)


def _run_benchmark_locked(
    cfg: MissionConfig,
    iterations: int | None,
    include_agent: bool,
    seed: int,
) -> Path:
    iterations = iterations or cfg.budget.iterations
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + f"-seed{seed}"
    outdir = Path("data/benchmark") / stamp
    outdir.mkdir(parents=True, exist_ok=True)
    # stable pointer for the dashboard: athanor dashboard --latest
    latest = Path("data/benchmark/latest")
    latest.unlink(missing_ok=True)
    latest.symlink_to(stamp)

    results: list[CampaignMetrics] = []

    for cls in (RandomBaseline, SimilarityBaseline, BayesOptBaseline):
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
        run_campaign(agent_cfg, make_backend(cfg.llm), iterations=iterations)
        db = CandidateDB(agent_cfg.paths.db)
        results.append(compute_metrics(f"agent ({cfg.llm.model})", db, cfg))
        db.close()

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
