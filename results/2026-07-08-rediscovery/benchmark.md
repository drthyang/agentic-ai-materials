# Benchmark: pv-absorber-rediscovery-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 63 | 2 | 3.17 | 0 | 0.153 |
| similarity | 79 | 2 | 2.53 | 1 | 0.041 |
| agent (qwen3:32b) | 14 | 5 | 35.71 | 1 | 0.018 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
