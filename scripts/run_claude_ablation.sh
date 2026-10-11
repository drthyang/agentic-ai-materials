#!/usr/bin/env bash
# The exact commands behind results/2026-10-10-claude-ablation/.
#
#   scripts/run_claude_ablation.sh            # whole queue, in priority order
#   scripts/run_claude_ablation.sh <step>...  # only the named steps
#
# Steps: bo-pv, sonnet-ablation, nocritic, qd, opus (the first queue, run as
# one invocation with no arguments), then nocritic-nosurr and opus3, then the
# local same-day qwen3:32b arms qwen-nosurr and qwen-surr (no API key passed),
# then nocritic-n5 (4 Sonnet runs, $5 cap).
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

ollama_is_free() {  # no model loaded by anyone, normal pressure, >= 45% free
  local loaded free
  loaded=$(curl -s localhost:11434/api/ps | grep -c '"name"')
  free=$(memory_pressure 2>/dev/null | awk -F': ' '/free percentage/{gsub("%","",$2); print $2}')
  [ "$loaded" -eq 0 ] && [ "$(sysctl -n kern.memorystatus_vm_pressure_level)" -eq 1 ] \
    && [ "${free:-0}" -ge 45 ]
}

local_agent() { # local_agent <seed> <tag> [extra benchmark args...] — qwen3:32b, $0 API
  local seed=$1 tag=$2; shift 2
  # the Mac is shared (another session runs qwen3:32b evals): never contend
  until ollama_is_free; do
    echo "$(date '+%F %T') ollama busy or memory tight; re-checking in 10 min"; sleep 600
  done
  echo "$(date '+%F %T') start $tag seed$seed"
  env -u ANTHROPIC_API_KEY uv run athanor benchmark --iterations 5 --seed "$seed" \
    --baselines none --tag "$tag" --backend ollama --model qwen3:32b "$@" \
    > "data/logs/$tag-seed$seed.log" 2>&1
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
    # --- follow-ups added after the first queue finished (budget allowed) ---
    nocritic-nosurr)  # completes the Sonnet 2x2: no surrogate, critic off
      for i in 1 2 3; do
        agent $((60 + i)) sonnet-nosurr-nocritic claude-sonnet-5-5 3 --no-surrogate --no-critic
      done ;;
    opus3)  # third Opus run: two runs disagreed by 2x
      agent 53 opus-nosurr claude-opus-5-5 6 --no-surrogate ;;
    # --- local, $0 API: same-day qwen3:32b arms (2026-10-11) ---
    qwen-nosurr)  # the July protocol and July agent seeds, run again today
      for s in 0 6 7; do local_agent "$s" qwen-nosurr-oct --no-surrogate; done ;;
    qwen-surr)  # fourth cell of model x tool
      for i in 1 2 3; do local_agent $((70 + i)) qwen-surr-oct; done ;;
    # --- paid, approved 2026-10-11 with a $5 cap: balance the PV 2x2 at n=5 ---
    nocritic-n5)
      CAP=23.05  # ledger stood at $18.05 (restated) + the $5 approved for this step
      for i in 4 5; do
        agent $((30 + i)) sonnet-surr-nocritic claude-sonnet-5-5 1.25 --no-critic
        agent $((60 + i)) sonnet-nosurr-nocritic claude-sonnet-5-5 1.25 --no-surrogate --no-critic
      done ;;
    *) echo "unknown step $1" >&2; return 2 ;;
  esac
}

steps=("$@")
[ ${#steps[@]} -eq 0 ] && steps=(bo-pv sonnet-ablation nocritic qd opus nocritic-nosurr opus3 \
  qwen-nosurr qwen-surr nocritic-n5)
for s in "${steps[@]}"; do step "$s"; done
