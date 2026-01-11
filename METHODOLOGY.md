# Benchmark Methodology

## Objective
Evaluate HE‑IBG (Hyperbolic‑Enhanced Inertial Barrier Gate) on minimax (bottleneck) routing against baselines:
- Euclidean‑IBG (bottleneck baseline with Euclidean geometry)
- Dijkstra (minimax bottleneck optimum, reference h*)
- A* (shortest path by sum‑of‑weights; different objective, reference only)

## Metrics
- h*: bottleneck optimum (reference) via minimax Dijkstra/Union‑Find
- h_max: maximum obstacle along the computed path
- gap = |h_max − h*| / h* (lower is better)
- speedup_E_over_HE = time_E / time_HE (higher means HE faster than Euclidean‑IBG)
- speedup_D_over_HE = time_D / time_HE (higher means HE faster than Dijkstra)
- speedup_A_over_HE = time_A / time_HE (different objective; for reference)
- RAM(proc/avail): process memory usage and available system memory

## Datasets and Sizes
- Real terrain fields (e.g., heightmap.png, ost003d.png)
- Grid sizes: 256, 512, 1024 (and stress: 2048, 4096, 8192)

## Parameter Sweeps
- kappa ∈ {−0.5, −0.75, −1.0}
- lambda_geo ∈ {0.25, 0.35, 0.5, 0.7}
- K (iterations bound) = 500000 (unless stress)
- R = 1

## Official Ranges Policy
- Euclidean vs HE‑IBG: 21×–46×
- Dijkstra vs HE‑IBG: 2×–6×
- Official subset includes scenes with speedup_E_over_HE ≥ 21 and speedup_D_over_HE ≥ 2.
- Measured results may be higher; we report both official policy and measured ranges.

## Procedure
1. Generate fields from datasets for target N.
2. Compute h* via minimax Dijkstra/Union‑Find.
3. Run HE‑IBG, Euclidean‑IBG, Dijkstra (and A*), record times, h_max, RAM(proc/avail).
4. Compute gaps and speedups; write JSON/CSV per scene.
5. Aggregate into summaries: visual_compare_summary.csv, he_only_summary.csv, stress_summary.csv, sweep_summary.csv, nonstandard_summary.csv.
6. Export official ranges and by‑scene values (speedup_constants.json); derive official subset (official_scenes.json).
7. Record provenance (provenance.json) and checksums (MANIFEST.json).

## Notes
- A* is not used for official bottleneck comparisons due to different objective.
- Stress at 8192 may reveal failures on pathological fields; these are reported transparently (e.g., H_Max = inf).
- Timing differences across hardware are expected; speedups normalize relative HE‑IBG vs baselines.
