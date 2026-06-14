# Case 02 — Mode C Enterprise clean PASS

**Verdict:** `pass` -> `successAssetManifest`

An Enterprise-tier Mode C reel: single-source `replicated_shots` (no `rendered_shots`), `parent_chain[3] = mode-c-direct`. Same 6-shot clean bundle.

**Proves the mode-convergence guarantee:** downstream of `mode_convergence`, the `asset_bundle` + `spec_check` + `coverage_check` are **byte-shape-identical to Case 01** despite a different ingested mode and tier. Only `mode_convergence.ingested_mode` and lineage differ. This TC-01/TC-02 pair is the convergence proof no other fixture provides (Decision #9 / Blueprint §3).
