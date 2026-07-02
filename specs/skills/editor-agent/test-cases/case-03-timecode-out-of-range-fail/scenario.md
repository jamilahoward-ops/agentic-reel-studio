# Case 03 — Timecode out of range → `fail` / `timecode_out_of_range`

**Proves:** a cut that over-runs its declared media is caught at the conform layer and routed back to Edit Director to re-trim.

The Edit Plan directs `shot-003` with `out_ms: 15000`, but the Ingest `asset_bundle` declares that shot at 12.0s (12000ms). `15000 > 12000` — the cut would conform past available media. Editor never conforms a cut past its declared duration (Hard Rule #5).

**Expected verdict:** `fail`, `failure_code: timecode_out_of_range`, `failed_check_id: 4`, `route_back_to: edit-director-agent` (the trim is the director's to re-cut). `detail` names the offending event + the available media. Soft-recoverable: re-trim the cut in the plan.
