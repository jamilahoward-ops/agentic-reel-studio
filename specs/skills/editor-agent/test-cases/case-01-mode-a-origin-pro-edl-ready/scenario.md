# Case 01 — Mode-A origin, Pro tier → `edl_ready`

**Proves:** the full faithful-conform happy path.

A Pro-tier reel whose footage originated in **Mode A** (human videographer upload). Edit Director emitted a `plan_ready` Edit Plan: 6-shot cut order, 4 caption lines, 2 lower-thirds, hard-cuts-only, one music bed + 2 swell markers, the mandatory end-card. Every `cut_order[].asset_uri` resolves in the Ingest `asset_bundle`; every `out_ms` (9500) sits inside each shot's declared 12.0s media; the record timeline lays gap-free (6 × 9500ms = 57000, end-card 57000→58500, total in the 45–75s band); committed copy is byte-faithful; the 10th-pass commit-time firewall is clean.

**Expected verdict:** `edl_ready`. `render_dispatched: false`, `conform_mode: human_in_the_loop`, `human_review_required: true` — the EDL is *recommended* for the human conform, never "rendered." Editor authored zero creative decisions; every EDL row is a transform, a byte-faithful passthrough, or a computed verification.
