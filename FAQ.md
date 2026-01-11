# FAQ

## What does “speedup” mean here?
It is a runtime ratio against HE‑IBG. For example, `speedup_E_over_HE = time_E / time_HE`. Values > 1 indicate HE‑IBG is faster than the baseline.

## Is HE‑IBG always faster than Euclidean‑IBG or Dijkstra?
Official conservative ranges (Euclidean vs HE: 21×–46×; Dijkstra vs HE: 2×–6×) summarize typical results on our benchmark set. Individual scenes may vary, but measured results are consistently at or above these minima in the official subset.

## Why include A*?
A* solves a different objective (sum‑of‑weights shortest path). It is provided for reference only; speedup vs A* does not imply the same bottleneck quality target.

## What is h* and gap?
`h*` is the minimax bottleneck optimum (reference) computed via minimax Dijkstra/Union‑Find. `gap = |h_max − h*| / h*`; lower is better. HE‑IBG aims to minimize `h_max` while being much faster.

## How are datasets authenticated?
Each scene includes a SHA‑256 of the source field to verify integrity. Runtime and RAM (proc/avail) are measured live during execution.

## What is the “official subset”?
Scenes meeting minimum thresholds: `speedup_E_over_HE ≥ 21` and `speedup_D_over_HE ≥ 2`. See `data/official_scenes.json`.

## Can I reproduce results?
Use the working scripts referenced in README (real‑world/stress/sweep/visual). Hardware and OS differences affect runtime; we report process RAM and available RAM to aid comparability.
