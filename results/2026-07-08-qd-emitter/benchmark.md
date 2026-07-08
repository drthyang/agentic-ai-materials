# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 51 | 1 | 1.96 | 0 | 0.009 |
| similarity | 62 | 5 | 8.06 | 0 | 0.044 |
| agent (qwen3:32b) | 3 | 2 | 66.67 | 0 | 0.507 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
