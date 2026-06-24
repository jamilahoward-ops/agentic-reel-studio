# Case 03 — Coverage re-confirm fails → FAIL + route to Ingest

**Verdict:** `fail` → `errorEnvelope` · **Code:** `incomplete_shot_coverage`

Ingest's manifest is consumed, but Edit Director's defensive re-confirm finds `coverage_check.coverage_complete: false` / a missing body-beat asset (`shot-006`) — the boundary case where an Ingest-pass and Edit Director's re-confirm disagree, which must halt rather than author a cut over a hole.

**Proves:** `errorEnvelope` with `failed_check_id: 3` (coverage branch), `detail` naming the unfilled structure window + `unmapped_beats: [6]`, `route_back_to: "ingest-agent"` (the coverage owner per the §6.3 / §3.2 route map), verdict `fail` NOT `revise` (a coverage hole is a hard structural defect, not a creative tension), `human_review_required: true`. The re-confirm is defensive, not redundant — Edit Director cannot direct a cut over a hole even if Ingest passed it.
