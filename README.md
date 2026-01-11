# HE‑IBG: Hyperbolic‑Enhanced Inertial Barrier Gate for Minimax Routing

HE‑IBG (Hyperbolic‑Enhanced Inertial Barrier Gate) is a routing approach optimized for the minimax (bottleneck) objective. Unlike “shortest path” methods that minimize the sum of weights, HE‑IBG minimizes the largest obstacle along the route (h_max), ensuring corridor width/clearance and robustness on real terrains.

## What Makes HE‑IBG Different
- Minimax (bottleneck) instead of sum of weights: guarantees on the worst obstacle along the route, relevant for safe/wide corridors.
- Hyperbolic geometry: tunable speed/quality trade‑off via kappa, lambda_geo, K, R.
- Quality control: reference h* (bottleneck optimum via minimax Dijkstra/Union‑Find) and gap |h_max−h*|/h* per scene.
- Resource efficiency: stable RAM usage and real execution times on large grids up to 8192×8192.

## Comparison to Other Methods
- Dijkstra (minimax): provides the reference h* but is slower; HE‑IBG achieves close values much faster.
- Euclidean‑IBG: Euclidean baseline for bottleneck; HE‑IBG is faster and more robust on real fields.
- A*: a different objective (“shortest path” by sum), not directly comparable to bottleneck; marked as “different objective” in reports.

## Official Speedup Ranges
- Euclidean vs HE‑IBG: 21× – 46×
- Dijkstra vs HE‑IBG: 2× – 6×
- Sources: data/speedup_constants.json, data/visual_compare_summary.csv

## Capabilities and Applications
- Robotics and navigation: routes with guaranteed corridor width (bottleneck clearance).
- Evacuation and logistics: capacity‑constrained routes robust to noise/obstacles.
- Network routing: paths with minimum guaranteed bottleneck capacity.
- Game AI: path selection with sufficient width/clearance in complex levels.

## Results and Data
- Comparison summary: data/visual_compare_summary.csv
- HE‑only parameters/quality: data/he_only_summary.csv
- Stress tests: data/stress_summary.csv
- Parameter sweeps: data/sweep_summary.csv
- Non‑standard cases: data/nonstandard_summary.csv
- Official subset (meets minimum thresholds): data/official_scenes.json
- Full CSV archive: data/legacy_csv

## Reproducibility and Authenticity
- All scenes include dataset SHA‑256; time, RAM (proc/avail), h_max, h*, and gap are measured live and recorded in JSON/CSV.
- Reproduction commands live in the working repository (run_real_world_full.py, run_real_world_stress.py, run_real_world_sweep.py, run_visual_compare.py, run_visual_he_only.py).

## Policy
- Official ranges are conservative statements (21×–46× for Euclidean vs HE‑IBG; 2×–6× for Dijkstra vs HE‑IBG).
- Measured results can be higher; official publications use a subset of scenes that meet the minimum thresholds.
