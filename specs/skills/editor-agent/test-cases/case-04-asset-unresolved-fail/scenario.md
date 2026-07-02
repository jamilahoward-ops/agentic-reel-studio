# Case 04 — Asset unresolved → `fail` / `asset_unresolved`

**Proves:** the FOLDED resolution code — an unresolvable cut asset routes back to Ingest.

The Edit Plan directs a cut whose `asset_uri` is `ars://reinvented/shots/shot-099.mp4`, but no such handle exists in the Ingest `asset_bundle.raw_footage[]`. Editor cannot bind that cut event to real media (Hard Rule #5).

**Expected verdict:** `fail`, `failure_code: asset_unresolved`, `failed_check_id: 3`, `route_back_to: ingest-agent`. `asset_unresolved` is deliberately FOLDED — cut-asset, music-bed, and voice-track resolution failures all carry this single code because they share one route-back destination (Ingest). This is the opposite of Edit Director keeping `duration_envelope_breach` standalone: Editor clusters its defect surface by route-back destination, not by defect taxonomy (D8).
