# Verification Guide

## Purpose
This guide explains how to verify the integrity and provenance of the published data so that third parties can trust that results were not tampered with.

## Verify Checksums
1. Download the repository (or the `data/` folder) for a given tag (e.g., `v0.1.0`).
2. Compute SHA‑256 for each file locally and compare with entries in `data/MANIFEST.json`.
   - On Linux/macOS:
     - `shasum -a 256 data/* data/legacy_csv/*`
   - On Windows (PowerShell):
     - `Get-FileHash data/* -Algorithm SHA256`
     - `Get-FileHash data/legacy_csv/* -Algorithm SHA256`
3. Every file’s hash must match the corresponding `sha256` field in `data/MANIFEST.json`. Any mismatch indicates tampering.

## Verify Provenance
Open `data/provenance.json`:
- `git_commit` — commit hash of the published state
- `python_version`, `platform` — environment details recorded at export time

Cross‑check that:
- The `git_commit` exists on the repository main branch or tagged release.
- The tag used (e.g., `v0.1.0`) points to the same commit or earlier parent, ensuring reproducibility.

## Reproduce Summaries (Optional)
If you have the working scripts and datasets:
- Run the benchmark scripts (real‑world, stress, sweep, visual) and re‑generate CSV/JSON.
- Compare newly generated CSV/JSON to the published files; hashes will differ if values change, but the measured ranges and official policy thresholds should remain consistent.

## What’s Tamper‑Evident
- Any change to `data/*` alters the SHA‑256 in `MANIFEST.json` and can be detected.
- Tags (e.g., `v0.1.0`) freeze the repository state; published checksums allow integrity checking across mirrors.

## Limitations
- Runtime depends on hardware/OS; minor timing differences are expected across machines.
- For fairness, speedups are defined as baseline time divided by HE‑IBG time; interpretation is documented in README.
