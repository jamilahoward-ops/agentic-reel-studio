# TC-03 — Platform variant does not match the tier promise → FAIL + route to Motion

**Input:** A Motion-passed Pro reel where `declared_format.platform_variants` carries ONE variant (instagram 9:16) but `tier_richness_echo.platform_variants_promised == 2` — the Pro plan was sold two variants and the finished master delivered one. Every other gate is clean.

**Expected verdict:** `fail` · **Expected code:** `format_spec_mismatch` (Check #7).

**Proves:** The delivery-promise gap **only full QC reads** — it is the only agent that reads `tier_richness_echo` against the delivered set. `errorEnvelope` with `failed_check_id: 7`; `detail.format_sub_status {aspect_ok: true, resolution_ok: true, duration_in_band: true, caption_burn_in_ok: true, variants_match_promise: false}` — every OTHER format sub-status still explicitly computed (no short-circuit nulls — the completeness rule, §6.2); `detail` names the promised-vs-delivered delta (`{platform_variants_promised: 2, platform_variants_delivered: 1, missing: ["tiktok"]}`); `route_back_to: "motion-agent"` (the finish layer that produced the variant set — the §6.3 drafted default, D8b); verdict is `fail` — **post-fixable** (re-spec the missing variant from the existing master), NOT a halt and NOT a `reshoot` (no production round-trip is needed to produce a second aspect variant); `human_review_required: true`.
