# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 63 | 4 | 6.35 | 0 | 0.009 |
| similarity | 50 | 4 | 8.0 | 0 | 0.044 |
| bayesopt | 68 | 3 | 4.41 | 0 | 0.044 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
