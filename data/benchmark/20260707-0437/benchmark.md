# Benchmark: pv-absorber-v1

budget: 1 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 19 | 0 | 0.0 | 0 | 0.249 |
| similarity | 19 | 1 | 5.26 | 0 | 0.041 |

hit = converged + gap in [1.1, 1.7] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
