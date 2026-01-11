# HE‑IBG: Hyperbolic‑Enhanced Inertial Barrier Gate for Minimax Routing

HE‑IBG (Hyperbolic‑Enhanced Inertial Barrier Gate) is a routing approach optimized for the minimax (bottleneck) objective. Unlike “shortest path” methods that minimize the sum of weights, HE‑IBG minimizes the largest obstacle along the route (h_max), ensuring corridor width/clearance and robustness on real terrains.

## Key Metrics
- Official speedup (Euclidean vs HE‑IBG): 21×–46×
- Official speedup (Dijkstra vs HE‑IBG): 2×–6×
- Measured ranges are provided in data/speedup_constants.json; higher speedup means HE‑IBG is faster than the baseline.

## Scaling Behavior
- Speedups increase with grid size (N) on both datasets:
  - heightmap: Euclidean/HE = [21.53, 31.66, 46.66] at N = [256, 512, 1024]; Dijkstra/HE = [2.01, 2.08, 5.41]
  - ost003d: Euclidean/HE = [21.77, 33.98, 39.78] at N = [256, 512, 1024]; Dijkstra/HE = [2.96, 3.75, 5.37]
- Rationale: HE‑IBG’s JIT‑accelerated O(N²) routines scale better relative to baselines that incur O(N² log N) or heavier per‑step overhead; larger grids amplify the relative advantage.

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
 
## Metric Definitions
- speedup_E_over_HE = time_Euclidean / time_HE; higher means HE‑IBG is faster than Euclidean.
- speedup_D_over_HE = time_Dijkstra / time_HE; higher means HE‑IBG is faster than Dijkstra (minimax).
- speedup_A_over_HE = time_A* / time_HE; A* has a different objective (shortest‑path by sum), so this is for reference only.
- gap = |h_max − h*| / h*; lower is better. Dijkstra (minimax) provides h* and typically has gap=0 by definition.

## Reproducibility and Authenticity
- All scenes include dataset SHA‑256; time, RAM (proc/avail), h_max, h*, and gap are measured live and recorded in JSON/CSV.
- Reproduction commands live in the working repository (run_real_world_full.py, run_real_world_stress.py, run_real_world_sweep.py, run_visual_compare.py, run_visual_he_only.py).
 - Release manifests: data/MANIFEST.json lists per‑file SHA‑256 checksums; data/provenance.json records git commit, platform and Python version.
 - Tagged releases: repository is tagged (e.g., v0.1.0) to freeze state; checksums make tampering evident.

## Policy
- Official ranges are conservative statements (21×–46× for Euclidean vs HE‑IBG; 2×–6× for Dijkstra vs HE‑IBG).
- Measured results can be higher; official publications use a subset of scenes that meet the minimum thresholds.
 
## Interpretations
- Speedup values compare runtime baselines against HE‑IBG (higher = HE‑IBG is faster).
- Euclidean‑IBG baseline implements the same bottleneck objective but with Euclidean geometry (not “shortest path by sum”).
- A* targets a different objective (sum‑of‑weights shortest path); included for reference only.
 
## References
- Data dictionary: DATA_DICTIONARY.md
- Release notes: RELEASE_NOTES.md
- FAQ: FAQ.md
- Verification guide: VERIFICATION_GUIDE.md
- Methodology: METHODOLOGY.md
 
## Quick Verify
- Windows (PowerShell): `Get-FileHash data/* -Algorithm SHA256` and compare to `data/MANIFEST.json`
- macOS/Linux: `shasum -a 256 data/* data/legacy_csv/*` and compare to `data/MANIFEST.json`
- Script: `python tools/check_manifest.py` prints whether all checksums match
  - Includes runtime environment and optimizations (Python + Numba JIT, NumPy arrays, nopython caching)
