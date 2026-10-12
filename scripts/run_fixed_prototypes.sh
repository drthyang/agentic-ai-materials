#!/usr/bin/env bash
# The exact commands behind results/2026-10-12-fixed-prototypes/: the
# October benchmark matrix rerun on the corrected 16-atom chalcopyrite and
# kesterite prototypes (commit 2aa21eb).
#
#   scripts/run_fixed_prototypes.sh            # whole queue, in priority order
#   scripts/run_fixed_prototypes.sh <step>...  # only the named steps
#
# Steps: pv-base, sonnet-nosurr, qwen, sonnet-surr, nocritic, qd-base, qd-sonnet.
#
# Same protocol as before: 5 iterations x 20 relaxations, gemma4:26b critic
# unless stated, Claude Sonnet 5.5 at effort=high, and the same seeds as the
# October study so baseline choices are paired run for run. Strictly
# sequential on a shared Mac: runs that need the critic start only when no
# large model other than gemma4:26b is loaded; qwen3:32b runs also need 45%
# of memory free. The API key is read into the command environment only;
# the study ledger refuses any run once it reaches $20 (live prices,
# Sonnet 5.5 cache hits at 0.05x input).
set -u
cd "$(dirname "$0")/.."

OUT=results/2026-10-12-fixed-prototypes
LEDGER=$OUT/api-spend-ledger.csv
CAP=20
QD=config/missions/qd-emitter.yaml
mkdir -p data/logs "$OUT"

with_key() { ANTHROPIC_API_KEY="$(tr -d '\n\r ' < ~/.config/anthropic/key)" "$@"; }

loaded_models() { curl -s localhost:11434/api/ps | grep -o '"name":"[^"]*"' | cut -d'"' -f4; }
free_pct() { memory_pressure 2>/dev/null | awk -F': ' '/free percentage/{gsub("%","",$2); print $2}'; }
pressure_ok() { [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -lt 4 ]; }

wait_until() {  # wait_until <description> <command...>
  local what=$1; shift
  until "$@"; do echo "$(date '+%F %T') waiting: $what"; sleep 600; done
}
only_critic_loaded() { pressure_ok && ! loaded_models | grep -qv '^gemma4:26b$'; }
room_for_qwen() {
  only_critic_loaded && [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -eq 1 ] \
    && [ "$(free_pct)" -ge 45 ]
}

run() {  # run <guard> <seed> <tag> [benchmark args...]
  local guard=$1 seed=$2 tag=$3; shift 3
  wait_until "$guard for $tag seed$seed" "$guard"
  echo "$(date '+%F %T') start $tag seed$seed"
  "$@" --iterations 5 --seed "$seed" --tag "$tag" > "data/logs/$tag-seed$seed.log" 2>&1
  local rc=$?
  echo "$(date '+%F %T') end   $tag seed$seed exit=$rc"
}

sonnet() {  # sonnet <guard> <seed> <tag> [extra args...]
  local guard=$1 seed=$2 tag=$3; shift 3
  run "$guard" "$seed" "$tag" with_key uv run athanor benchmark --baselines none \
    --backend anthropic --model claude-sonnet-5-5 --effort high --max-cost-usd 1.25 \
    --ledger "$LEDGER" --spend-cap-usd "$CAP" "$@"
}

base() {  # base <seed> <tag> [extra args...]
  local seed=$1 tag=$2; shift 2
  run pressure_ok "$seed" "$tag" env -u ANTHROPIC_API_KEY uv run athanor benchmark \
    --skip-agent "$@"
}

step() {
  case "$1" in
    pv-base)  for s in 0 1 2 3 4 5 6 7; do base "$s" fx-pv-base; done ;;
    sonnet-nosurr)
      for i in 1 2 3 4 5; do sonnet only_critic_loaded $((10 + i)) fx-sonnet-nosurr --no-surrogate; done ;;
    qwen)  # local, $0: the July protocol and agent seeds
      for s in 0 6 7; do
        run room_for_qwen "$s" fx-qwen-nosurr env -u ANTHROPIC_API_KEY uv run athanor \
          benchmark --baselines none --backend ollama --model qwen3:32b --no-surrogate
      done ;;
    sonnet-surr)
      for i in 1 2 3 4 5; do sonnet only_critic_loaded $((20 + i)) fx-sonnet-surr; done ;;
    nocritic)
      for i in 1 2 3; do
        sonnet pressure_ok $((30 + i)) fx-sonnet-surr-nocritic --no-critic
        sonnet pressure_ok $((60 + i)) fx-sonnet-nosurr-nocritic --no-surrogate --no-critic
      done ;;
    qd-base)  for s in 8 9 10 11 12; do base "$s" fx-qd-base --mission "$QD"; done ;;
    qd-sonnet)
      for i in 1 2 3; do
        sonnet only_critic_loaded $((40 + i)) fx-qd-sonnet-nosurr --mission "$QD" --no-surrogate
      done ;;
    *) echo "unknown step $1" >&2; return 2 ;;
  esac
}

steps=("$@")
[ ${#steps[@]} -eq 0 ] && steps=(pv-base sonnet-nosurr qwen sonnet-surr nocritic qd-base qd-sonnet)
for s in "${steps[@]}"; do step "$s"; done
