"""Aggregate benchmark run directories into per-arm statistics.

    uv run python scripts/aggregate_ablation.py results/<study>/arms.json

arms.json names each arm and lists its run directories:

    {"mission": "config/mission.yaml",
     "arms": {"random": {"db": "random.db", "runs": ["data/benchmark/..."]},
              "agent: sonnet": {"db": "agent.db", "runs": [...]}},
     "comparisons": [["agent: sonnet", "agent: qwen"], ...]}

Metrics are recomputed from each run's SQLite DB with the shared hit rule
(metrics.compute_metrics), never copied from a run's own summary, so every
arm is scored by identical code. Writes per-run and per-arm tables (CSV +
markdown) next to arms.json. Statistics are deliberately small-sample
honest: per-run values are always shown, the mean comes with a bootstrap
interval, and arm-vs-arm comparisons use an exact permutation test.
"""

from __future__ import annotations

import csv
import itertools
import json
import math
import random
import statistics
import sys
from pathlib import Path

from athanor.config import MissionConfig, load_mission
from athanor.db import CandidateDB
from athanor.metrics import compute_metrics

METRICS = ("hits_per_100_relaxations", "hits", "relaxations")


def run_row(arm: str, run_dir: Path, db_name: str, cfg: MissionConfig) -> dict:
    db = CandidateDB(run_dir / db_name)
    m = compute_metrics(arm, db, cfg)
    novel = db._conn.execute(
        "SELECT COUNT(*) FROM candidates WHERE status IN ('scored','error') "
        "AND is_novel = 1").fetchone()[0]
    db.close()
    relax = m.scored + m.errors
    row = {
        "arm": arm,
        "run": run_dir.name,
        "relaxations": relax,
        "hits": m.hits,
        "hits_per_100_relaxations": round(m.hits_per_100_relaxations, 2),
        "best_gap_distance_ev": m.best_gap_distance_ev,
        "novel_fraction_evaluated": round(novel / relax, 3) if relax else None,
        "critic_vetoes": None,
        "hit_formulas": " ".join(sorted(m.hit_formulas)),
        "api_cost_usd": None,
        "api_calls": None,
        "cache_read_share": None,
        "tool_calls": None,
    }
    usage_f = run_dir / "usage.json"
    if db_name == "agent.db" and usage_f.exists():
        u = json.loads(usage_f.read_text())
        row["api_cost_usd"] = u.get("cost_usd")
        row["api_calls"] = u.get("calls")
        total_in = (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                    + u.get("cache_creation_input_tokens", 0))
        if total_in:
            row["cache_read_share"] = round(u.get("cache_read_input_tokens", 0) / total_in, 3)
    stats_f = run_dir / "agent_stats.json"
    if db_name == "agent.db" and stats_f.exists():
        st = json.loads(stats_f.read_text())
        row["tool_calls"] = json.dumps(st.get("tool_calls", {}), sort_keys=True)
        if "critic" in st:
            row["critic_vetoes"] = st["critic"].get("vetoed")
    if row["critic_vetoes"] is None and db_name == "agent.db":
        db = CandidateDB(run_dir / db_name)
        row["critic_vetoes"] = db._conn.execute(
            "SELECT COUNT(*) FROM candidates WHERE status='filtered_out' "
            "AND filter_reasons LIKE '%critic:%'").fetchone()[0]
        db.close()
    return row


def bootstrap_ci(values: list[float], n_boot: int = 20000, seed: int = 0,
                 level: float = 0.95) -> tuple[float, float] | None:
    if len(values) < 2:
        return None
    rng = random.Random(seed)
    means = sorted(
        statistics.fmean(rng.choices(values, k=len(values))) for _ in range(n_boot)
    )
    lo = means[int((1 - level) / 2 * n_boot)]
    hi = means[int((1 + level) / 2 * n_boot) - 1]
    return lo, hi


def permutation_p(a: list[float], b: list[float]) -> float:
    """Exact one-sided p-value for mean(a) > mean(b) under exchangeability."""
    pooled = a + b
    observed = statistics.fmean(a) - statistics.fmean(b)
    n, count, total = len(a), 0, 0
    for idx in itertools.combinations(range(len(pooled)), n):
        chosen = set(idx)
        xa = [pooled[i] for i in idx]
        xb = [pooled[i] for i in range(len(pooled)) if i not in chosen]
        total += 1
        if statistics.fmean(xa) - statistics.fmean(xb) >= observed - 1e-12:
            count += 1
    return count / total


def prob_superiority(a: list[float], b: list[float]) -> float:
    """P(A > B) + 0.5 P(A = B) over all cross pairs (common-language effect)."""
    wins = sum((x > y) + 0.5 * (x == y) for x in a for y in b)
    return wins / (len(a) * len(b))


def summarize(rows: list[dict], metric: str) -> dict:
    vals = [float(r[metric]) for r in rows if r[metric] is not None]
    out = {"n": len(vals), "values": vals}
    if not vals:
        return out
    out["mean"] = statistics.fmean(vals)
    out["sd"] = statistics.stdev(vals) if len(vals) > 1 else None
    out["median"] = statistics.median(vals)
    out["min"], out["max"] = min(vals), max(vals)
    out["ci95"] = bootstrap_ci(vals)
    return out


def _fmt(x, digits=2):
    if x is None:
        return "—"
    if isinstance(x, float):
        return f"{x:.{digits}f}"
    return str(x)


def main(spec_path: str) -> None:
    spec_path = Path(spec_path)
    spec = json.loads(spec_path.read_text())
    default_cfg = load_mission(spec.get("mission", "config/mission.yaml"))
    rows: list[dict] = []
    for arm, arm_spec in spec["arms"].items():
        cfg = load_mission(arm_spec["mission"]) if "mission" in arm_spec else default_cfg
        for run in arm_spec["runs"]:
            rows.append(run_row(arm, Path(run), arm_spec["db"], cfg))

    outdir = spec_path.parent
    with open(outdir / "per_run.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    by_arm: dict[str, list[dict]] = {}
    for r in rows:
        by_arm.setdefault(r["arm"], []).append(r)

    lines = ["## Per-arm summary", "",
             "| arm | n | hits/100 relax: mean ± sd [95% bootstrap CI] | median (min–max) "
             "| hits/run: mean ± sd (min–max) | relaxations/run: mean (min–max) |",
             "|---|---|---|---|---|---|"]
    summary_json = {}
    for arm, arm_rows in by_arm.items():
        h100 = summarize(arm_rows, "hits_per_100_relaxations")
        hits = summarize(arm_rows, "hits")
        rel = summarize(arm_rows, "relaxations")
        summary_json[arm] = {"hits_per_100_relaxations": h100, "hits": hits,
                             "relaxations": rel}
        ci = h100.get("ci95")
        ci_s = f"[{ci[0]:.1f}, {ci[1]:.1f}]" if ci else "—"
        lines.append(
            f"| {arm} | {h100['n']} | {_fmt(h100['mean'], 1)} ± {_fmt(h100['sd'], 1)} {ci_s} "
            f"| {_fmt(h100['median'], 1)} ({_fmt(h100['min'], 1)}–{_fmt(h100['max'], 1)}) "
            f"| {_fmt(hits['mean'], 1)} ± {_fmt(hits['sd'], 1)} "
            f"({int(hits['min'])}–{int(hits['max'])}) "
            f"| {_fmt(rel['mean'], 1)} ({int(rel['min'])}–{int(rel['max'])}) |"
        )

    lines += ["", "## Per-run values", "",
              "| arm | run | relax | hits | hits/100 | best \\|Δgap\\| | novel frac "
              "| critic vetoes | API $ | cache-read share | hit formulas |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(
            f"| {r['arm']} | {r['run']} | {r['relaxations']} | {r['hits']} "
            f"| {_fmt(r['hits_per_100_relaxations'], 1)} | {_fmt(r['best_gap_distance_ev'], 3)} "
            f"| {_fmt(r['novel_fraction_evaluated'])} | {_fmt(r['critic_vetoes'])} "
            f"| {_fmt(r['api_cost_usd'])} | {_fmt(r['cache_read_share'])} "
            f"| {r['hit_formulas'] or '—'} |")

    comps = spec.get("comparisons", [])
    if comps:
        lines += ["", "## Comparisons (one-sided exact permutation test on the mean; "
                  "P(A>B) = probability of superiority over all run pairs)", "",
                  "| A | B | metric | mean A | mean B | P(A>B) | p (A > B) |",
                  "|---|---|---|---|---|---|---|"]
        summary_json["_comparisons"] = []
        for a, b in comps:
            for metric in METRICS:
                va = [float(r[metric]) for r in by_arm[a]]
                vb = [float(r[metric]) for r in by_arm[b]]
                if math.comb(len(va) + len(vb), len(va)) > 2_000_000:
                    p = None
                else:
                    p = permutation_p(va, vb)
                ps = prob_superiority(va, vb)
                summary_json["_comparisons"].append(
                    {"a": a, "b": b, "metric": metric, "p_one_sided": p,
                     "prob_superiority": ps})
                lines.append(
                    f"| {a} | {b} | {metric} | {statistics.fmean(va):.2f} "
                    f"| {statistics.fmean(vb):.2f} | {ps:.2f} | {_fmt(p, 4)} |")

    (outdir / "summary.md").write_text("\n".join(lines) + "\n")
    (outdir / "summary.json").write_text(json.dumps(summary_json, indent=1))
    print("\n".join(lines))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
