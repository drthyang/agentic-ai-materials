#!/usr/bin/env bash
# The exact commands behind results/2026-10-12-fixed-prototypes/: the
# benchmark rerun on the corrected 16-atom chalcopyrite and kesterite
# prototypes (commit 2aa21eb). Local only, $0 of API credit.
#
#   scripts/run_fixed_prototypes.sh            # whole queue, in priority order
#   scripts/run_fixed_prototypes.sh <step>...  # only the named steps
#
# Steps: qwen, pv-base, qd-base (in that order: the large local models run
# first, so the shared Mac's memory is freed early). Re-running is safe: a run whose directory
# already holds metrics.json is skipped.
#
# The Claude arms of the October study are NOT rerun here. They were queued
# and cancelled before any of them started: on 2026-10-12 the user decided
# to stop using the API for benchmarking until the builds reach an
# acceptable level, so only local models (qwen3:32b proposer, gemma4:26b
# critic) and the non-LLM baselines run.
#
# Same protocol and seeds as before (5 iterations x 20 relaxations; the
# baselines' seeds 0-7 on PV and 8-12 on QD; the July qwen agent seeds 0, 6,
# 7), so baseline choices are paired run for run with the defective-prototype
# runs. Strictly sequential on a shared Mac: qwen3:32b runs start only when
# no large model other than the gemma4:26b critic is loaded, pressure is
# normal and 45% of memory is free.
set -u
cd "$(dirname "$0")/.."

QD=config/missions/qd-emitter.yaml
mkdir -p data/logs

loaded_models() { curl -s localhost:11434/api/ps | grep -o '"name":"[^"]*"' | cut -d'"' -f4; }
free_pct() { memory_pressure 2>/dev/null | awk -F': ' '/free percentage/{gsub("%","",$2); print $2}'; }
pressure_ok() { [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -lt 4 ]; }
room_for_qwen() {
  ! loaded_models | grep -qv '^gemma4:26b$' \
    && [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -eq 1 ] \
    && [ "$(free_pct)" -ge 45 ]
}

already_done() { ls data/benchmark/*-seed"$1"-"$2"/metrics.json >/dev/null 2>&1; }

run() {  # run <guard> <seed> <tag> <command...>
  local guard=$1 seed=$2 tag=$3; shift 3
  if already_done "$seed" "$tag"; then echo "$(date '+%F %T') skip  $tag seed$seed (done)"; return; fi
  until "$guard"; do echo "$(date '+%F %T') waiting: $guard for $tag seed$seed"; sleep 600; done
  echo "$(date '+%F %T') start $tag seed$seed"
  env -u ANTHROPIC_API_KEY "$@" --iterations 5 --seed "$seed" --tag "$tag" \
    > "data/logs/$tag-seed$seed.log" 2>&1
  local rc=$?
  echo "$(date '+%F %T') end   $tag seed$seed exit=$rc"
}

step() {
  case "$1" in
    pv-base)
      for s in 0 1 2 3 4 5 6 7; do
        run pressure_ok "$s" fx-pv-base uv run athanor benchmark --skip-agent
      done ;;
    qwen)  # the July protocol and agent seeds; proposer and critic both local
      for s in 0 6 7; do
        run room_for_qwen "$s" fx-qwen-nosurr uv run athanor benchmark --baselines none \
          --backend ollama --model qwen3:32b --no-surrogate
      done ;;
    qd-base)
      for s in 8 9 10 11 12; do
        run pressure_ok "$s" fx-qd-base uv run athanor benchmark --skip-agent --mission "$QD"
      done ;;
    *) echo "unknown step $1" >&2; return 2 ;;
  esac
}

steps=("$@")
[ ${#steps[@]} -eq 0 ] && steps=(qwen pv-base qd-base)
for s in "${steps[@]}"; do step "$s"; done
