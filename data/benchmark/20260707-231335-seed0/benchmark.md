# Benchmark: pv-absorber-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 80 | 0 | 0.0 | 0 | 0.249 |
| similarity | 58 | 1 | 1.72 | 0 | 0.041 |
| agent (qwen3:32b) | 7 | 4 | 57.14 | 0 | 0.09 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
