# Data Dictionary

## Visual Comparison (data/visual_compare_summary.csv)
- dataset: image name (source field)
- N: grid size
- h_star: minimax bottleneck optimum (reference)
- time_HE: runtime of HE‑IBG
- time_E: runtime of Euclidean‑IBG baseline
- time_D: runtime of Dijkstra (minimax) baseline
- time_A: runtime of A* (different objective)
- ram_*_mb: process RAM for the method
- gap_*: normalized deviation from h* (|h_max − h*| / h*). Lower is better.
- speedup_E_over_HE: time_E / time_HE (higher means HE‑IBG is faster than Euclidean).
- speedup_D_over_HE: time_D / time_HE (higher means HE‑IBG is faster than Dijkstra).
- speedup_A_over_HE: time_A / time_HE (A* has a different objective; for reference).
- sha256: dataset integrity hash

## HE‑Only (data/he_only_summary.csv)
- dataset, N, time_HE, h_max_HE, ram_HE_mb
- h_star: minimax reference
- gap_HE: |h_max_HE − h*| / h*
- kappa, lambda_geo, K, R: HE‑IBG parameters
- sha256: dataset integrity hash

## Stress (data/stress_summary.csv)
- Grid_Size, Image, H_Max
- K_Used: iterations bound actually used
- RAM_Available_GB, RAM_Needed_GB
- Status (Success/Fail), Success (True/False), Time_Sec

## Sweep (data/sweep_summary.csv)
- Image, Grid_Size, kappa, lambda_geo, K
- h_star
- HE_time, HE_h_max, HE_gap, HE_success
- DIJ_time, DIJ_h_max, DIJ_gap, DIJ_success
- Speedup_Dijkstra_vs_HE = DIJ_time / HE_time (higher means HE‑IBG is faster)

## Non‑standard (data/nonstandard_summary.csv)
- Aggregated results for labyrinth/micro/mandatory/dynamic scenarios
- Fields mirror Visual Comparison where applicable

## Official Scenes (data/official_scenes.json)
- official_subset: scenes meeting minimum thresholds (speedup_E_over_HE ≥ 21, speedup_D_over_HE ≥ 2)
