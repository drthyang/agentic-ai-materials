#!/usr/bin/env bash
# The exact commands behind results/2026-10-13-novelty-baselines/: the three
# PV baselines rerun as their -novel variants, which skip compositions
# Materials Project already has before relaxing them (as the agent is told
# to) and may draw up to 50 batches per iteration so the skips do not leave
# budget unspent. Everything else matches the pv-base step of
# scripts/run_fixed_prototypes.sh: same mission, seeds 0-7, 5 iterations x 20
# relaxations, both scoring fixes. Local only, $0 of API credit.
#
# Why: the original baselines relax known compositions too, which a hit can
# never be, so "agent vs baseline" partly measured that handicap.
#
#   scripts/run_novelty_baselines.sh
#
# Re-running is safe: a seed whose run directory already holds metrics.json
# is skipped.
set -u
cd "$(dirname "$0")/.."

TAG=fx-pv-novel
OUT=results/2026-10-13-novelty-baselines
mkdir -p data/logs "$OUT"

already_done() { ls data/benchmark/*-seed"$1"-"$TAG"/metrics.json >/dev/null 2>&1; }

for s in 0 1 2 3 4 5 6 7; do
  if already_done "$s"; then echo "$(date '+%F %T') skip  $TAG seed$s (done)"; continue; fi
  echo "$(date '+%F %T') start $TAG seed$s"
  env -u ANTHROPIC_API_KEY uv run athanor benchmark --skip-agent \
    --baselines random-novel,similarity-novel,bayesopt-novel \
    --iterations 5 --seed "$s" --tag "$TAG" > "data/logs/$TAG-seed$s.log" 2>&1
  echo "$(date '+%F %T') end   $TAG seed$s exit=$?"
done
