#!/usr/bin/env bash
# The exact commands behind results/2026-10-12-fixed-prototypes/: the
# benchmark rerun with both scoring defects fixed — correct 16-atom
# chalcopyrite and kesterite prototypes (2aa21eb) and the convex hull on
# CHGNet's MP2020-corrected energy scale (edc49f9). Local only, $0 of API
# credit. Two runs started before the hull fix were discarded.
#
#   scripts/run_fixed_prototypes.sh            # whole queue, in priority order
#   scripts/run_fixed_prototypes.sh <step>...  # only the named steps
#
# Steps: qwen, pv-base, qd-base (the default queue), and sonnet (a separate
# lane, below). Default order: the large local models run
# first, so the shared Mac's memory is freed early). Re-running is safe: a run whose directory
# already holds metrics.json is skipped.
#
# API use: on 2026-10-12 the user first stopped API benchmarking (the
# original Claude arms were cancelled before any started), then approved one
# Claude arm once the local qwen3:32b arm had finished, so the analysis
# compares like with like: Sonnet 5.5, 5 runs, the gemma4:26b critic, a $20
# cap on this study's ledger enforced by the spend tracker; + rank_by_surrogate
# only if the ledger still shows clear room. No Opus. The Claude lane runs
# beside the baselines under its own benchmark lock:
#
#   ATHANOR_BENCHMARK_LOCK=data/benchmark/.lock-api scripts/run_fixed_prototypes.sh sonnet
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
OUT=results/2026-10-12-fixed-prototypes
LEDGER=$OUT/api-spend-ledger.csv
CAP=20
mkdir -p data/logs "$OUT"

with_key() { ANTHROPIC_API_KEY="$(tr -d '\n\r ' < ~/.config/anthropic/key)" "$@"; }

loaded_models() { curl -s localhost:11434/api/ps | grep -o '"name":"[^"]*"' | cut -d'"' -f4; }
free_pct() { memory_pressure 2>/dev/null | awk -F': ' '/free percentage/{gsub("%","",$2); print $2}'; }
pressure_ok() { [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -lt 4 ]; }
room_for_qwen() {
  ! loaded_models | grep -qv '^gemma4:26b$' \
    && [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -eq 1 ] \
    && [ "$(free_pct)" -ge 45 ]
}

already_done() { ls data/benchmark/*-seed"$1"-"$2"/metrics.json >/dev/null 2>&1; }
qwen_arm_done() {
  already_done 0 fx-qwen-nosurr && already_done 6 fx-qwen-nosurr && already_done 7 fx-qwen-nosurr
}
claude_may_start() {  # the qwen arm has finished and released its model
  qwen_arm_done && ! loaded_models | grep -qv '^gemma4:26b$' && pressure_ok
}
ledger_usd() {
  uv run python -c "from athanor.benchmark import ledger_total_usd; print(f'{ledger_total_usd(\"$LEDGER\"):.2f}')"
}

run() {  # run <guard> <seed> <tag> <command...>
  local guard=$1 seed=$2 tag=$3; shift 3
  if already_done "$seed" "$tag"; then echo "$(date '+%F %T') skip  $tag seed$seed (done)"; return; fi
  until "$guard"; do echo "$(date '+%F %T') waiting: $guard for $tag seed$seed"; sleep 600; done
  echo "$(date '+%F %T') start $tag seed$seed"
  if [ "$1" = with_key ]; then
    "$@" --iterations 5 --seed "$seed" --tag "$tag" > "data/logs/$tag-seed$seed.log" 2>&1
  else
    env -u ANTHROPIC_API_KEY "$@" --iterations 5 --seed "$seed" --tag "$tag" \
      > "data/logs/$tag-seed$seed.log" 2>&1
  fi
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
    sonnet)  # Claude Sonnet 5.5 on both fixes; same seeds as October
      for i in 1 2 3 4 5; do
        run claude_may_start $((10 + i)) fx-sonnet-nosurr with_key uv run athanor benchmark \
          --baselines none --backend anthropic --model claude-sonnet-5-5 --effort high \
          --no-surrogate --max-cost-usd 1.25 --ledger "$LEDGER" --spend-cap-usd "$CAP"
      done
      # the surrogate arm only with clear room: 5 more runs at <= $1.25 each
      if awk "BEGIN{exit !($(ledger_usd) <= 10)}"; then
        for i in 1 2 3 4 5; do
          run claude_may_start $((20 + i)) fx-sonnet-surr with_key uv run athanor benchmark \
            --baselines none --backend anthropic --model claude-sonnet-5-5 --effort high \
            --max-cost-usd 1.25 --ledger "$LEDGER" --spend-cap-usd "$CAP"
        done
      else
        echo "$(date '+%F %T') skip  fx-sonnet-surr: ledger at \$$(ledger_usd), no clear room"
      fi
      echo "$(date '+%F %T') lane done: sonnet (ledger \$$(ledger_usd))" ;;
    *) echo "unknown step $1" >&2; return 2 ;;
  esac
}

steps=("$@")
[ ${#steps[@]} -eq 0 ] && steps=(qwen pv-base qd-base)
for s in "${steps[@]}"; do step "$s"; done
