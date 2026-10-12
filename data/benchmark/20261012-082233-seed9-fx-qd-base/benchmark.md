# Benchmark: qd-emitter-v1

budget: 5 iterations x 20 relaxations

| strategy | scored | hits | hits/100 relax | rediscoveries | best |gap-ideal| (eV) |
|---|---|---|---|---|---|
| random | 53 | 0 | 0.0 | 0 | 0.047 |
| similarity | 40 | 0 | 0.0 | 0 | 0.236 |
| bayesopt | 65 | 0 | 0.0 | 0 | 0.12 |

hit = converged + gap in [1.8, 3.1] eV + e_above_hull <= 0.05 eV/atom + not a confirmed-known material
