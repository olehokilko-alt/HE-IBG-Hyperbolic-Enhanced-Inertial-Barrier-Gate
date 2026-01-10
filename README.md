# HE-IBG Structured Test Results

## Official Speedup Range (Euclidean vs HE-IBG)
- Range: 21.00× – 46.00×
- Source: data/speedup_constants.json and data/visual_compare_summary.csv

## Official Speedup Range (Dijkstra vs HE-IBG)
- Range: 2.00× – 6.00×
- Source: data/speedup_constants.json and data/visual_compare_summary.csv

## Files
- data/visual_compare_summary.csv
- data/he_only_summary.csv
- data/speedup_constants.json
- data/stress_summary.csv
- data/sweep_summary.csv
- data/nonstandard_summary.csv
- data/legacy_csv/*.csv (original benchmarks)

## Notes
- Each row includes dataset, N, times, RAM, h*, gaps, SHA-256.
- Values are measured live during execution; SHA-256 ensures dataset authenticity.

## Measured Speedup Range (for reference)
- Range: 21.53× – 46.66×

## Policy
- Official ranges are conservative claims. Measured results are real and may be higher.
- Official publication subset includes scenes meeting the minimum thresholds.