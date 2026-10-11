#!/usr/bin/env bash
# The exact commands behind results/2026-10-10-claude-ablation/.
#
#   scripts/run_claude_ablation.sh            # whole queue, in priority order
#   scripts/run_claude_ablation.sh <step>...  # only the named steps
#
# Steps: bo-pv, sonnet-ablation, nocritic, qd, opus.
#
# Every agent run: 5 iterations x 20 relaxations (the cap the July qwen
# runs used), the local gemma4:26b critic unless stated, Claude at
# effort=high (the Sonnet 5.5 API default, set explicitly). Runs are strictly
# sequential, and each waits while macOS reports critical memory pressure:
# the Mac is shared, and the critic alone is an 18 GB local model. The API
# key is read into the command environment only; spend goes to the ledger
# and the study refuses to start a run past $40.
set -u
cd "$(dirname "$0")/.."

LEDGER=results/2026-10-10-claude-ablation/api-spend-ledger.csv
CAP=40
mkdir -p data/logs

with_key() { ANTHROPIC_API_KEY="$(tr -d '\n\r ' < ~/.config/anthropic/key)" "$@"; }

wait_for_memory() {  # kern.memorystatus_vm_pressure_level: 1 normal, 2 warn, 4 critical
  while [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -ge 4 ]; do
    echo "$(date '+%F %T') memory pressure critical; waiting"; sleep 60
  done
}

agent() { # agent <seed> <tag> <model> <max-cost> [extra benchmark args...]
  local seed=$1 tag=$2 model=$3 cost=$4; shift 4
  wait_for_memory
  echo "$(date '+%F %T') start $tag seed$seed"
  with_key uv run athanor benchmark --iterations 5 --seed "$seed" --baselines none \
    --tag "$tag" --backend anthropic --model "$model" --effort high \
    --max-cost-usd "$cost" --ledger "$LEDGER" --spend-cap-usd "$CAP" "$@" \
    > "data/logs/$tag-seed$seed.log" 2>&1
  local rc=$?
  echo "$(date '+%F %T') end   $tag seed$seed exit=$rc"
}

baselines() { # baselines <seed> <tag> <which> [extra args...]
  local seed=$1 tag=$2 which=$3; shift 3
  wait_for_memory
  echo "$(date '+%F %T') start $tag seed$seed"
  uv run athanor benchmark --iterations 5 --seed "$seed" --skip-agent \
    --baselines "$which" --tag "$tag" "$@" > "data/logs/$tag-seed$seed.log" 2>&1
  local rc=$?
  echo "$(date '+%F %T') end   $tag seed$seed exit=$rc"
}

step() {
  case "$1" in
    bo-pv)  # seeds 2-7 bring BO to the n=8 random/similarity already have
      for s in 2 3 4 5 6 7; do baselines "$s" bo-pv bayesopt; done ;;
    sonnet-ablation)
      # model ablation (no surrogate = the July qwen configuration),
      # interleaved with the tool ablation (rank_by_surrogate on = current default)
      for i in 1 2 3 4 5; do
        agent $((10 + i)) sonnet-nosurr claude-sonnet-5-5 3 --no-surrogate
        agent $((20 + i)) sonnet-surr claude-sonnet-5-5 3
      done ;;
    nocritic)  # critic ablation: Sonnet + surrogate, critic off
      for i in 1 2 3; do
        agent $((30 + i)) sonnet-surr-nocritic claude-sonnet-5-5 3 --no-critic
      done ;;
    qd)  # second mission: baselines (seed 8 repeats July), then Sonnet in the
         # July qwen QD configuration (no surrogate)
      for s in 8 9 10 11 12; do
        baselines "$s" qd-base random,similarity,bayesopt \
          --mission config/missions/qd-emitter.yaml
      done
      for i in 1 2 3; do
        agent $((40 + i)) qd-sonnet-nosurr claude-sonnet-5-5 3 \
          --mission config/missions/qd-emitter.yaml --no-surrogate
      done ;;
    opus)  # small capability check: Opus 5.5 in the model-ablation configuration
      for i in 1 2; do agent $((50 + i)) opus-nosurr claude-opus-5-5 6 --no-surrogate; done ;;
    *) echo "unknown step $1" >&2; return 2 ;;
  esac
}

steps=("$@")
[ ${#steps[@]} -eq 0 ] && steps=(bo-pv sonnet-ablation nocritic qd opus)
for s in "${steps[@]}"; do step "$s"; done
