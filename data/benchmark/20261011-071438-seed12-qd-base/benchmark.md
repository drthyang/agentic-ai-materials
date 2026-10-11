# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 53 | 4 | 7.55 | 0 | 0.025 |
| similarity | 45 | 4 | 8.89 | 0 | 0.108 |
| bayesopt | 72 | 9 | 12.5 | 0 | 0.021 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
