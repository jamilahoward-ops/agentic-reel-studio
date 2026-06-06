# TC-01 — Mode B Pro clean PASS

**Expected verdict:** `pass` · **branch:** `successPreflightReport` · **code:** none · **route_back_to:** null

Style Replication emitted a `successReplicatedShots` payload for a 5-shot REINVENTED reel at Pro
tier. AI Video Gen `rendered_shots` is present for the Mode B forensic SHA-256 cross-check. All six
upstream agents contributed >=4 `qc_pre_flags`. Two `platform_variants` requested (9:16 reels +
1:1 feed). No carried drift. Cumulative cost $0.42 — well within the $450 Pro combined ceiling.

This is the dominant volume path: rendered -> replicated -> cleared to post.

**Key invariants exercised**
- 5-tuple inbound `parent_chain` extends to 6-tuple (append `preflight_report_id`); schema accepts both (held at minItems 5, maxItems 6 until Cross-SPEC §3.9 ratifies).
- `entity_firewall_pass_7.hits == 0` across all leaf strings + 2 captions + burn-in text.
- `brand_voice_qc.points_passed == 11`; every `per_point.status == "pass"` (false-pass structurally impossible).
- `format_spec_check.platform_variants_checked == 2`, all violation counts 0.
- Mode B forensic cross-check: single `negative_prompt_sha256` matches across `rendered_shots` and the input -> `mode_b_chain_check.passthrough_intact_bool == true`.
- `qc_pre_flags_adjudication`: `agents_reporting == 6`, `floor_met_all == true`, `negative_predicates == 0`.
- `cost_ledger_check.status == "within_ceiling"` ($0.42 <= $450).
- All 12 self-QC checks PASS first attempt.
