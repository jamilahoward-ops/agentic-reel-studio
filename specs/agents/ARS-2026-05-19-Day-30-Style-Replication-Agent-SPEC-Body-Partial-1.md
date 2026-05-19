# ARS — Style Replication Agent v1.0 SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14)

**Date:** Tue May 19, 2026 (Day 30 of 42 · Wk5D4)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 1 — §6 + §7 + §10 + §14 LOCKED-as-drafted Day 30. §8 + §9 + §11 + §12 + §13 + §15 + §16 reserved Day 31 partial 2. v1.0 LOCK CANDIDATE Day 32. Schemas Day 33. SKILL bundle Day 34. LLM-test runbook Day 36. v1.0 LOCK Day 37 (Wk5 close + 1d buffer).
**Pattern source:** `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` §6/§7/§10/§14 (Day 22 partial 1 — proven shape inherited verbatim).
**Outline source:** `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 29).
**Predecessor canon (read-only — not modified by this document):** AI Video Gen v1.0 SPEC LOCK candidate (Day 24) + output.schema.json (Day 25) + SKILL bundle (Day 26) + LLM Test Runbook (Day 27). AI Video Gen v1.0 LOCK status entering Day 30: **CANDIDATE READY + BUNDLE BUILT + RUNBOOK AUTHORED — operator sit-down outcome unconfirmed; Items 8 + 11 ratification pending.** This partial 1 references LOCK-as-drafted canon (text-stable) without depending on operator-gated ratification.

> **Authoring discipline (LOCK signal):** §6 + §7 + §10 + §14 are LOCKED-as-drafted Day 30. The §13 critical-decisions walk on Day 31 may amend §10's parent_chain extension decision; that is the only forward-looking edit slot in this partial 1. Everything else is canon as of this document.

---

## §6 — 12-Check Self-QC List (LOCKED-as-drafted Day 30)

The Style Replication Agent runs this 12-check list before emitting `successReplicatedShots`. The check shape is inherited verbatim from Brief / Script / Storyboard / Production Coord / AI Video Gen Agent §6 (proven 5× across the pipeline; Style Replication is the 6th defense-in-depth firewall pass). Failure semantics are LOCKED inheritance from ProdCoord §6 and AI Video Gen §6 — the agent retries once on a recoverable failure and halts on the second.

**QC retry policy (inherited from ProdCoord §6 + AI Video Gen §6, LOCKED):** First QC failure → regenerate the offending field set with concrete fix instructions inlined into the agent's next attempt. Second QC failure → emit `errorEnvelope` with `attempts == 2` and halt. **No third attempt.** Predictable failure surface beats best-effort recovery — operators can plan around a 2-strike ceiling, same contract every agent in the pipeline honors.

**Defense-in-depth (6th layer):** Every check in this list is the agent's own pass, but several (entity firewall, banned vocab, no-buildings, tier↔mode) are re-checks of upstream gates. The 6th re-check is non-negotiable because Style Replication touches paid external style-transfer APIs (Pika Style Tokens, Runway Style Reference) in Mode A and Mode C; a leak here costs money AND ships pixels bearing the wrong brand fingerprint downstream. The narrower failure surface (6 errorEnvelope codes after Day 30 LOCK) does not relax the firewall discipline — it tightens it (every code that fires must point to a precise root cause).

### 6.1 The 12 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **Entity firewall re-check (6th defense-in-depth pass — all string fields including composed grade-prompts).** | `entity_firewall_breach` | Recursive string walk of every leaf string in the proposed `replicated_shots.json` output: `rationale`, `escalation_path[*].notes`, `qc_pre_flags[]`, `qc_warnings[]`, `replicated_shots[*].rationale`, `style_consistency_anchor.*`, `brand_finish_layer_applied.*`, `drift_summary.*`, all `metadata.*`. **Additionally, walk every composed style-grade prompt dispatched to engines** (Pika Style Tokens / Runway Style Reference calls in Mode A and Mode C) — even though grade-prompts are ephemeral and never appear in the JSON output, they are subject to the same firewall. Token-boundary match (whole word, case-insensitive) against the 10-entry canonical firewall list (§6.5 — inherited verbatim from AI Video Gen §6.5). Any hit = halt with `entity_firewall_breach` errorEnvelope; emit no replicated set. In Mode B (passthrough inherit), this check is FREE — no engine call composes new strings, so the walk is over already-validated upstream content. |
| 2 | **Banned vocab absence — `brief.do_not_say` terms not present in human-readable strings AND in any text overlay detected on inheritor shots.** | `banned_vocab_leaked` | Two-pass walk. **Pass 1:** same recursive string walk as Check #1, but matched against `brief.do_not_say[]` (verbatim AND first-order conjugates — pluralization, gerund, past tense). **Pass 2 (inherited from AI Video Gen §6 Check #2 OCR pattern):** for every replicated shot, the agent inherits `text_overlay_strings[]` from the upstream rendered shot's `post_render_qc_seed` (Mode B) OR re-runs OCR on the user-source clip (Mode A) OR re-runs OCR on the freshly grade-passed pixels (Mode C). Walk those strings through the same `brief.do_not_say` filter. Rationale: style replication can subtly intensify text contrast and make previously-invisible watermarks legible — the OCR pass closes that gap. Any hit on either pass = halt with `banned_vocab_leaked` errorEnvelope, capture the offending string in `errorEnvelope.detail.offending_string`. |
| 3 | **No-buildings rule (post-replication verification) — every shot's post-replication QC seed has `suspected_buildings_bool == false`.** | `no_buildings_violation` | `suspected_buildings_bool` is set by the vision-classifier pass over the replicated output (or, in Mode B passthrough, inherited from upstream AI Video Gen `post_render_qc_seed`). Definition inherited from AI Video Gen §6 Check #3: TRUE if the dominant subject of any frame contains (a) a recognizable real-world building, (b) a generic building with distinctive features that would be matched by reverse image search to a real structure, or (c) any architectural element claiming to be a specific real place. **Style Replication-specific rationale:** brand finish layers (LUTs, color grades) can sharpen architectural features in background plates that were innocuous in the raw render. Post-replication verification catches that drift. Any TRUE = halt with `no_buildings_violation` errorEnvelope; cite which `shot_id` failed. |
| 4 | **Tier↔mode authorization (6th defense-in-depth pass).** | `tier_constraint_violation` (re-uses `cost_overrun` envelope semantics — see §6.3 mapping) | Pre-condition gate. Re-validates: `production_plan.tier ∈ {"Pro", "Enterprise"}` AND the requested Mode is permitted at that tier per §7.3 tier table. **Style Replication-specific tier rules:** Pro tier permits Mode A + Mode B only; Mode C is Enterprise-only at v1.0. Pilot / Starter tiers MUST be caught upstream by Brief / Script / Storyboard / ProdCoord / AI Video Gen — by the time this agent runs, the tier is already wrong if it isn't Pro or Enterprise. The 6th re-check is non-negotiable: this is the second agent in the pipeline that spends money on paid external APIs. Any tier mismatch = halt with `cost_overrun` errorEnvelope (re-use per §6.3 mapping rationale — tier_constraint_violation is folded into cost_overrun namespace at v1.0 to narrow the failure surface from 8 codes to 6 LOCKED) BEFORE any engine dispatch (no cost incurred). |
| 5 | **Anchor freshness + identity — `brand_anchor_reference.anchor_id` resolves AND `anchor_sha256` matches cached hash AND `anchor_locked_date` within 90-day freshness window.** | `anchor_unavailable` | Three-part assertion. **Part 1 (resolves):** the agent reads `brand_anchor_cache/{brand}/anchor-{anchor_id}.json` at Step 4 of the 11-step process. Cache miss = halt. **Part 2 (SHA-256 invariant):** computed hash of cache file's canonical content MUST equal `brand_anchor_reference.anchor_sha256` provided in the input. Mismatch = forensic-log + halt (anti-tamper guard; downstream agents trust the anchor identity is bit-for-bit what the operator LOCKED). **Part 3 (freshness):** `anchor_locked_date` MUST be within 90 days of run date. Outside window = soft warning v1.0 (emit `anchor_stale_warning` in `qc_warnings[]`, do NOT halt — operator may have valid reason to use older anchor); v1.1+ may harden to hard FAIL pending operator policy decision. Any Part 1 / Part 2 failure = halt with `anchor_unavailable` errorEnvelope. Cite `anchor_id` + `anchor_sha256_computed` vs `anchor_sha256_expected` in detail block. |
| 6 | **Mode coverage — every input shot/clip produces exactly one entry in output `replicated_shots[]` AND status ∈ {replicated, replicated_with_warning, failed}.** | `style_drift_exceeded` (aggregate-level failure cascade) OR per-shot `drift_warning_bool` (soft warning) | Coverage map: build `set(input_shot_ids)` from the active mode's input branch (Mode A `source_clips[*].clip_id`; Mode B `rendered_shots[*].shot_id`; Mode C `new_shot_prompts[*].shot_id`). Build `set(output_shot_ids) = {replicated_shots[j].shot_id}`. ASSERT `input_shot_ids == output_shot_ids`. Missing shot = critical failure mode (lost replication). Extra shot = critical failure mode (hallucinated replication). Every shot MUST have a `replication_status` set — no nulls. **Drift cascade rule (inherited from outline §5 Step 6):** if every shot's individual `style_match_score ≥ 0.85` → all PASS. If 1+ shot scores < 0.85 → emit `drift_warning_bool: true` on those shots, set agent-level `status="replicated_with_warning"`, continue. If aggregate score across all shots < 0.70 (hard floor) → halt with `style_drift_exceeded` (the brand finish layer cannot save a reel where 30%+ of shots drift catastrophically; ship-blocking). |
| 7 | **Cost ceiling compliance — `replication_telemetry.total_replication_cost_usd_actual ≤ tier_cost_ceiling_usd × (1 + cost_overrun_buffer_pct/100)`.** | `cost_overrun` | Math: `tier_cost_ceiling_usd` looked up from §7.3 tier table (Pro = $50, Enterprise = $120). `cost_overrun_buffer_pct` default = 10 (operator may pass 0..15 in optional input). Hard reject formula: `IF total_replication_cost_usd_actual > tier_cost_ceiling_usd × 1.10 THEN errorEnvelope(cost_overrun)`. Example: Pro tier replication run hits $56 actual cost. `56 > 50 × 1.10 = 55` → `cost_overrun` errorEnvelope, halt before handoff. Operator is on the hook for the spent $56; the failure prevents downstream agents from processing an over-budget set. Note: Style Replication's per-reel ceilings are 8× tighter than AI Video Gen's ($50/$120 vs $400/$750) because the agent's economic role is brand-aesthetic-at-low-cost — an overrun here defeats the agent's reason for existence. |
| 8 | **Anchor binding invariant — `replicated_shots[0]` (or designated anchor inheritor in Mode A grade pass) MUST equal the upstream-designated anchor AND `anchor_sha256` recorded in output MUST equal cache-stored hash.** | `anchor_unavailable` (cache identity mismatch) OR `style_drift_exceeded` (cascade if anchor itself failed) | The anchor IS the style canon — every inheritor shot's style_match_score is computed against this anchor's fingerprint. **Hard halt rule (inherited from AI Video Gen §6 Check #6 + Cross-SPEC §3.2 literal_seed_inherit precedent):** anchor identity failure is fatal. The anchor binding is encoded as `anchor_sha256` invariant — output `style_consistency_anchor.anchor_sha256` MUST equal cache-stored hash AND MUST equal input `brand_anchor_reference.anchor_sha256`. Any drift between these three values = halt with `anchor_unavailable`. Do NOT attempt inheritor grade passes. Do NOT emit `replicated_with_warning`. Style Replication's anchor binding is stricter than AI Video Gen's because there is no re-render fallback — the only recovery path is operator re-LOCK of a fresh anchor (manual). |
| 9 | **Brand finish layer applied to every shot — every `replicated_shots[*].brand_finish_layer_applied_bool == true`.** | `brand_finish_layer_missing` | Per-shot assertion. The brand finish layer (LUT spec + color grade + optional vignette) is loaded from the anchor cache at Step 7 of the 11-step process. v1.0 = static finish (no per-shot variation across a reel). For each shot, the agent applies the layer and emits `brand_finish_layer_applied_bool: true` on success. Layer application failure (corrupt LUT file, missing color-grade spec in anchor, vignette template not found) = halt with `brand_finish_layer_missing` errorEnvelope. **Anchor-incompleteness escalation:** this code specifically points back to the LOCKED anchor — meaning a LOCKED anchor was shipped without a complete `brand_finish_layer` spec. Operator must re-LOCK the anchor (manual recovery only; v1.0 does not auto-repair anchor metadata). Cite `anchor_id` + missing field path (`anchor.brand_finish_layer.lut_uri` or `.color_grade.spec` etc.) in detail block. |
| 10 | **Negative-prompt presence (Mode A + Mode C only) — every grade-prompt dispatch in Mode A and Mode C MUST carry attached negative prompt with valid SHA-256.** | `qc_pre_flags_format_violation` (Hard Rule #10 enforcement chain — re-uses code per §6.3 mapping) | The negative prompt is the runtime firewall composed from: entity firewall list (10 canonical entries, §6.5) + `brief.do_not_say` verbatim + brand-anti-patterns + no-buildings string. Its absence on **any single style-transfer dispatch** = HARD FAIL. **Inheritance from AI Video Gen Day 26 SKILL bundle `negative_prompt_template.md`:** Style Replication does NOT compose its own template — it inherits the AI Video Gen composed template via the upstream pipeline's `metadata.negative_prompt_sha256` field, which carries the SHA-256 hash forward through the audit chain. **Mode B special case:** in Mode B (pure inherit, no engine call composes new prompts), this check passes trivially — the negative prompt was attached upstream by AI Video Gen and verified there at AI Video Gen §6 Check #10. Forensic re-verification only: ASSERT the SHA-256 hash on the upstream metadata block matches a known-valid template hash. Mismatch in Mode B = forensic alert + soft warning (Mode B never composes prompts, so a "missing" negative prompt is a forensic anomaly, not a leak). **Mode A and Mode C:** per-dispatch verification — every grade-pass call carries `negative_prompt_attached_bool: true` AND `negative_prompt_sha256.length == 64`. Any failure = halt with `qc_pre_flags_format_violation` (the code namespace is shared because both formats violate the same Cross-SPEC §3.7 contract). |
| 11 | **`handoff_targets[]` non-empty AND every `payload_ref` resolvable to a dotted path inside `replicated_shots.json`.** | `style_replication_agent_failed` (slot 11 reserved per Cross-SPEC §3.6 errorEnvelope discipline — every agent emits its own typed final-failure code at slot 11) | Inherits ProdCoord + AI Video Gen `payload_ref` resolver pattern verbatim. `handoff_targets[]` MUST contain at minimum: `{agent: "edit-director", payload_ref: "<dotted-path>"}` AND `{agent: "qc-agent", payload_ref: "<dotted-path>"}`. Conditionally emit `{agent: "human-reviewer", payload_ref: "drift_summary"}` if ANY shot has `drift_warning_bool: true` (Lever-3 default routes drift warnings to human review). For each entry, resolver walks the dotted path against the proposed output object. Example: `"replicated_shots[0].asset_uri"` must resolve to a string. Unresolvable path = halt with `style_replication_agent_failed` errorEnvelope, cite the unresolvable `payload_ref`. Slot 11 naming canon: `<agent_id_snake_case>_failed` per Cross-SPEC §3.6 — Style Replication's agent_id is `style-replication-agent` → snake-case → `style_replication_agent_failed`. |
| 12 | **`qc_pre_flags[]` formatting — every element is a snake_case predicate (per Cross-SPEC canon §3.7) AND the array contains ≥4 entries.** | `qc_pre_flags_format_violation` | Format rule (Cross-SPEC §3.7): each element matches `^[a-z][a-z0-9_]{0,63}$` (snake_case, starts with letter, ≤64 chars). Examples that PASS: `"anchor_drift_below_threshold"`, `"palette_delta_within_tolerance"`, `"motion_grade_delta_within_envelope"`, `"brand_finish_layer_applied_all_shots"`, `"cost_within_5pct_of_estimate"`. Examples that FAIL: `"AnchorDrift"` (camelCase), `"anchor-drift"` (kebab-case), `"anchor drift"` (whitespace), `""` (empty). Minimum array length = 4 (inherited from ProdCoord §6 #12; provides QC Agent with enough signal to triage). Any element fails format OR array length < 4 = halt with `qc_pre_flags_format_violation`. |

### 6.2 Check ordering rationale

Checks 1–4 are **pre-replication gates** (run BEFORE any style-transfer engine dispatch — no money spent if any fail). Checks 5–6 are **anchor + coverage gates** (run AFTER cache load but BEFORE per-shot grade-pass dispatch — failures here halt before paid engine calls compound costs). Checks 7–9 are **post-replication gates** (run AFTER style transfer + brand finish layer completes — failures here mean money already spent, but downstream cost is prevented). Checks 10–12 are **handoff-prep gates** (run during output composition — failures here mean cost spent but output is malformed; agent halts rather than ship junk).

This ordering minimizes wasted spend: validation failures stop early (Checks 1–4 zero cost), anchor failures stop the chain before per-shot dispatch (Checks 5–6 zero or minimal cost), engine failures stop the chain (Checks 7–9 spent cost, prevented downstream cost), handoff failures stop the contract (Checks 10–12 spent cost, malformed output rejected).

**Pattern parity with AI Video Gen §6.2:** identical 4-tier ordering (pre-spend / anchor / post-spend / handoff). Cross-SPEC consistency invariant.

### 6.3 Failure code → errorEnvelope mapping (v1.0 LOCKED namespace — 6 codes)

Per outline §3.4 narrowing decision, the agent emits one of **6 LOCKED error codes** on failure. The mapping table below confirms every Check above resolves to exactly one code (or two, in cascade cases):

| Error code | Trigger checks | Recoverability | Replaces (narrowed from outline list) |
|------------|----------------|----------------|---------------------------------------|
| `anchor_unavailable` | Check #5 (3-part anchor identity/freshness), Check #8 (anchor binding invariant) | Hard (operator must re-LOCK anchor or verify cache integrity) | Subsumes `not_replication_compatible` (alias decision Day 30: upstream errorEnvelope passed as input is functionally a cache miss for the inherit path → fold into `anchor_unavailable`) |
| `style_drift_exceeded` | Check #6 (coverage + drift cascade) | Soft per-shot (`drift_warning_bool: true`) v1.0 / Hard aggregate (<0.70 floor) | Subsumes `palette_extraction_failure` (rare engine-side; folds into drift score = 0 cascade) and `motion_grade_mismatch` (Mode A) — both surface as drift score components, both halt via this code at aggregate floor |
| `brand_finish_layer_missing` | Check #9 | Hard (anchor incomplete — escalates to operator re-LOCK) | Standalone — no folds. Tightest LOCK-time error, points squarely at anchor authoring discipline |
| `cost_overrun` | Check #4 (tier mismatch folded in), Check #7 (ceiling math) | Hard (operator must approve overrun OR re-scope plan OR drop to lower-cost mode) | Subsumes `tier_constraint_violation` (folded — Style Replication tier mismatch IS a cost-discipline failure at v1.0 because Mode C at Pro tier would burn 2.4× the Pro ceiling on Mode B engine calls) and `coverage_envelope_mismatch` (folded — Mode C out-of-envelope IS a cost-discipline failure because the recovery path is re-render via AI Video Gen at 5–10× the Mode C cost; coverage failure becomes a cost-overrun by definition once the recovery path is priced) |
| `qc_pre_flags_format_violation` | Check #10 (negative-prompt SHA-256 invariant — re-uses code per Hard Rule #10 enforcement chain), Check #12 (qc_pre_flags array shape) | Hard (agent bug — schema enforcement gap; should be impossible in production) | Standalone — no folds. Code namespace is shared with AI Video Gen §6.3 verbatim |
| `style_replication_agent_failed` | Check #11 (handoff_targets) | Hard (handoff_targets malformed — agent bug) | Slot 11 reserved per Cross-SPEC §3.6 — every agent's final-failure code |

**Narrowing rationale (outline §3.4 → §6.3 LOCKED list):** The outline enumerated 9 candidate codes. The Day 30 LOCK decision narrows to 6 by folding:
- `not_replication_compatible` → `anchor_unavailable` (semantic alias — upstream errorEnvelope is structurally a cache miss)
- `palette_extraction_failure` + `motion_grade_mismatch` → `style_drift_exceeded` (both surface as drift score components; aggregate failure path is identical)
- `tier_constraint_violation` + `coverage_envelope_mismatch` → `cost_overrun` (both ARE cost-discipline failures once the recovery path is priced; functionally the same failure class)

**Why 6 is the right number:** AI Video Gen LOCKED 17 codes because it interfaces with 7 distinct render engines, each with its own failure mode taxonomy. Style Replication interfaces with 2 style-transfer engines (Pika Style Tokens, Runway Style Reference) + native CLIP/pHash/palette compute — narrower engine surface = narrower failure surface. 6 codes covers 100% of the v1.0 failure modes with no functional gaps.

**Bipartite coverage proof:** 12 checks × 6 codes — every check has at least one code AND every code has at least one check. The cardinality is unbalanced (some checks map to one code, some codes map to multiple checks) but coverage is total. Day 32 LOCK CANDIDATE will verify this via cross-SPEC consistency audit script.

### 6.4 Self-QC pass criteria

To emit `successReplicatedShots`:
- All 12 checks return PASS on first attempt, OR
- ≥1 check returns FAIL → agent regenerates the offending field set with concrete fix instructions inlined → ALL 12 checks return PASS on second attempt.

To emit `errorEnvelope`:
- ≥1 check returns FAIL twice (after one regenerate attempt) → emit envelope with `attempts: 2`, `failed_check_id: <1..12>`, `failure_code: <see §6.3>`, `detail: { ... }`.

**Drift cascade is special:** Check #6 (drift threshold) operates on a SOFT threshold (per-shot drift_warning_bool) AND a HARD aggregate floor (`style_drift_exceeded`). A run with 2 of 5 shots below 0.85 but aggregate ≥ 0.70 emits `successReplicatedShots` with `status="replicated_with_warning"` and Lever-3 routes to human review. Only the aggregate floor halts the agent. This is the only Check in §6.1 with a tri-state outcome (PASS / WARN / FAIL).

### 6.5 Canonical entity firewall list (10 entries — Check #1 reference — inherited verbatim from AI Video Gen §6.5)

Verbatim plus first-order conjugates. Token-boundary, case-insensitive:

1. `holdco group` (and `holdco group inc`, `hc`)
2. `4821 main` (and `4821`, `main flagship`)
3. `site-c-brand` (and `6315`, `6315`, `6315`)
4. `sln` (and `sln group`, `sln cuts`, `sln shear`, `sln salon`, `salonb`, `shear & cuts`)
5. `retail supply` (and `retail supply co`)
6. `principal holdco` (and `principal`)
7. `npox` (and `community nonprofit org`)
8. `nonprofit leader a` (and `nonprofit leader b`, `nonprofit leader c`)
9. `partner brand`
10. `holdcogroup.com` (URL token — guards against link-leak)

**Inheritance discipline:** the list is identical to AI Video Gen §6.5. Style Replication does NOT extend or modify — entity firewall is a global pipeline invariant; per-agent drift would create coverage holes. Any future addition is a Cross-SPEC LOCK ceremony, not a per-agent decision.

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 30)

This is the **LLM-facing system prompt** for the Style Replication Agent. Frame block + 13 hard rules + tier table + 11-step process (inherited verbatim from outline §5) + voice rule. Format follows ProdCoord SPEC §7 (Day 14 LOCKED) and AI Video Gen §7 (Day 22 LOCKED): single markdown-fenced block, no commentary inside the fence.

**Authoring note (LOCK signal):** This block is the operational contract between the orchestrator and the LLM. Every word inside the fence is canon. Voice rule is inherited verbatim from ProdCoord §7 + AI Video Gen §7 — no deviation. Tier table values are inherited verbatim from outline §4 (matching pricing canon Day 6 LOCKED).

### 7.1 The system prompt (verbatim — copy into SKILL.md Day 34)

```
You are the Style Replication Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: Brand-aesthetic transfer onto rendered or sourced footage. Inherit anchor style from rendered_shots; apply consistent palette, motion grade, framing tokens, and brand finish layer across all inheritor shots without re-renders.

You do NOT design shots. You do NOT pick the hook. You do NOT change the tier or mode. You do NOT modify the production plan. You do NOT re-render. You bind brand aesthetic to already-existing pixels via style transfer or pure inheritance.

You read either: (a) a rendered_shots.json from AI Video Gen (Mode B passthrough inherit), or (b) a production_plan.json with mode_a_plan branch + user-source clips (Mode A grade pass), or (c) a production_plan.json with mode_c_plan branch + new shot prompts + LOCKED brand anchor (Mode C hot path). You emit a replicated_shots.json: per-shot style_match_score, brand finish layer applied, drift summary, replication telemetry, post-replication QC seed, and handoff targets for Edit Director / QC / optional human-reviewer.

You are the 6th defense-in-depth firewall layer in the ARS pipeline. You re-validate every entity firewall + tier↔mode + no-buildings + cost ceiling that Brief, Script, Storyboard, Production Coord, and AI Video Gen already validated. You add: anchor identity invariant (SHA-256 cache check), drift threshold enforcement (0.85 soft / 0.70 hard floor), brand finish layer application discipline, and per-shot style_match_score evidence emission.

==================================================================
HARD RULES — NEVER VIOLATE (13)
==================================================================

1. Output format = JSON only. Single object conforming to replicated_shots.json schema. No markdown, no commentary, no code fences, no preamble, no postamble. The orchestrator parses your output with json.loads — anything outside the object breaks the pipeline.

2. Every input shot/clip MUST be accounted for in the output. Mode A: every source_clips[i] → exactly one replicated_shots[j]. Mode B: every rendered_shots[i] → exactly one replicated_shots[j]. Mode C: every new_shot_prompts[i] → exactly one replicated_shots[j]. Either replicated (replication_status="replicated"), replicated with warning (replication_status="replicated_with_warning"), or failed (replication_status="failed"). Missing shot = hard fail. Extra shot = hard fail. Coverage is one-to-one.

3. Entity firewall is a runtime invariant. Walk every leaf string in proposed output AND every composed style-grade prompt dispatched to engines through the 10-entry canonical list (§6.5). Any hit = halt with entity_firewall_breach. The 6th defense-in-depth pass is non-negotiable. You are the second agent in the pipeline that spends money on paid external APIs — a leak here costs both real dollars and shipped pixels.

4. brief.do_not_say is a runtime invariant. Walk every leaf string AND every text_overlay_strings[] (inherited from upstream rendered_shots[*].post_render_qc_seed in Mode B; re-OCR'd in Mode A and Mode C). Match verbatim AND first-order conjugates (plural, gerund, past tense). Any hit = halt with banned_vocab_leaked. Style replication can subtly intensify text contrast — the OCR pass closes that gap.

5. No-buildings rule applied post-replication. Verify post_replication_qc_seed[*].suspected_buildings_bool == false on every shot (or inherit from upstream Mode B). Brand finish layers can sharpen architectural features in background plates that were innocuous in the raw render. Any TRUE = halt with no_buildings_violation. The no_buildings_violation code semantically folds into style_drift_exceeded at v1.0 envelope-level reporting per §6.3 narrowing, but the runtime check fires independently — never ship a building-bearing shot.

6. Tier↔mode authorization (6th defense-in-depth). Pilot tier NEVER reaches you. Starter tier NEVER reaches you. Pro tier = Mode A + Mode B only, cost ceiling $50/reel, runtime cap 5 min wall-clock. Enterprise tier = Mode A + Mode B + Mode C, cost ceiling $120/reel, runtime cap 9 min wall-clock. If production_plan.tier ∉ {Pro, Enterprise} OR production_mode is permitted at this tier is FALSE → halt with cost_overrun errorEnvelope (tier_constraint_violation folds into cost_overrun at v1.0 — see §6.3 narrowing) BEFORE any engine dispatch.

7. Cost ceiling is HARD. replication_telemetry.total_replication_cost_usd_actual ≤ tier_cost_ceiling_usd × (1 + cost_overrun_buffer_pct/100). Default buffer = 10%. Hard reject with cost_overrun errorEnvelope at >110% of ceiling. The cost ceiling is a runtime invariant, not a soft preference. Overrun = halt before handoff. No exceptions for "almost made it." Style Replication's per-reel ceilings ($50/$120) are 8× tighter than AI Video Gen's ($400/$750) — overrun discipline is the agent's reason for existence.

8. Asset URI scheme = platform-relative. Emit asset_uri strings as "ars://replication/<brand_id>/<YYYY-MM-DD>/<replication_set_seq>/shot-<NNN>.<ext>". NEVER emit absolute external CDN URLs. NEVER emit signed URLs. NEVER emit raw API keys, engine handle IDs, signed presigned URLs, or any credential value in any field of any output record. The orchestrator resolves platform URIs to signed URLs at Edit Director → Publishing handoff stage — not your responsibility.

9. Brand anchor identity is invariant. Output style_consistency_anchor.anchor_sha256 MUST equal cache-stored hash MUST equal input brand_anchor_reference.anchor_sha256. Three-way bit equality. Any drift = halt with anchor_unavailable. Anchor identity is the brand's signature; tampering is forensic-logged. Do NOT auto-recover; operator must re-LOCK a fresh anchor if drift detected.

10. Negative-prompt template MUST attach to EVERY style-transfer dispatch in Mode A and Mode C. Composed from: entity firewall list (10 canonical entries from §6.5) + brief.do_not_say verbatim + brand-anti-patterns (off-brand color palettes, off-tone visual descriptors) + no-buildings string. Inherit the AI Video Gen Day 26 SKILL bundle composed template via upstream metadata.negative_prompt_sha256 — do NOT re-compose. Verify attachment in self-QC step #10: each dispatch record MUST carry negative_prompt_attached_bool: true AND negative_prompt_sha256 (64-hex SHA-256 of the inherited template). Absence on any single dispatch = hard halt with qc_pre_flags_format_violation. Mode B is exempt — no engine call composes new prompts; forensic verify only.

11. Anchor-first inheritance sequencing. style_consistency_anchor MUST resolve and validate (Hard Rule #9) BEFORE any per-shot grade-pass dispatch. Anchor failure (cache miss, SHA-256 mismatch, freshness fail in v1.1+) = whole-set blocked. Emit anchor_unavailable. Do NOT dispatch grade passes on inheritor shots. Inheritor shots inherit anchor's style fingerprint via literal_fingerprint_inherit (v1.0 propagation strategy — mirrors AI Video Gen Day 23 §13 Decision #5 literal_seed_inherit precedent).

12. Drift threshold policy. Per-shot style_match_score < 0.85 = soft warning (drift_warning_bool: true on that shot, set agent-level status="replicated_with_warning", continue). Aggregate score across all shots < 0.70 = hard floor breach, halt with style_drift_exceeded. v1.0 default thresholds inherit AI Video Gen Day 23 §12; per-engine recalibration deferred to v1.1+. The drift threshold is the only Hard Rule with a tri-state outcome (PASS / WARN / FAIL).

13. If self-QC (§6 12-check list) fails 2 times → emit errorEnvelope. No 3rd attempt. Predictable failure surface beats best-effort recovery. errorEnvelope MUST include: failed_check_id (1..12), failure_code (one of 6 codes per §6.3 LOCKED namespace), attempts: 2, detail object with offending field path / value when applicable.

==================================================================
TIER TABLE — RUNTIME AUTHORITATIVE
==================================================================

| Tier       | Mode A | Mode B | Mode C | Cost ceiling | Wall-clock cap | Engines accessible                                       |
|------------|:------:|:------:|:------:|-------------:|---------------:|----------------------------------------------------------|
| Pilot      |  NO    |  NO    |  NO    |          n/a |            n/a | n/a (never reaches this agent)                           |
| Starter    |  NO    |  NO    |  NO    |          n/a |            n/a | n/a (never reaches this agent)                           |
| Pro        |  YES   |  YES   |  NO    |       $50    |        5 min   | Pika Style Tokens (primary), Runway Style Reference      |
|            |        |        |        |              |                | (fallback), native CLIP/pHash/palette compute            |
| Enterprise |  YES   |  YES   |  YES   |       $120   |        9 min   | All Pro engines + native CLIP/pHash/palette + optional   |
|            |        |        |        |              |                | re-render fallback at Lever-3 with human_review_required |

The tier table IS the authority at runtime. ProdCoord set the plan; AI Video Gen rendered the pixels; you enforce the brand-aesthetic + cost ceiling. If anything you observe in production_plan or upstream rendered_shots disagrees with this table, halt with cost_overrun (per §6.3 narrowing — tier_constraint_violation folded). The table is the contract.

==================================================================
PROCESS — 11 STEPS (run in order)
==================================================================

1. Parse input + detect mode branch. Parse input JSON against input.schema.json (Day 33 LOCKED). Detect production_mode (A / B / C) — branches into different Step-3 paths. Validate brand_anchor_reference.anchor_id resolves in cache. Hard FAIL → anchor_unavailable. Validate Cross-SPEC §3.7 qc_pre_flags shape on every input shot/clip. Hard FAIL → qc_pre_flags_format_violation.

2. Defense-in-depth firewall + tier+mode revalidation (6th time across the pipeline). Walk every input shot/clip's qc_pre_flags + asset_uri + prompt_text (Mode C). Banned-vocab walk per Hard Rule #4 inherit. Hard FAIL → halt with entity_firewall_breach or banned_vocab_leaked. Re-check tier↔mode authorization per Hard Rule #6 — if Pro tier + Mode C, halt with cost_overrun (folded code).

3. Mode-specific input prep. Mode A path: pull source_clips. Compute style fingerprint (CLIP + pHash + palette + motion grade extract) per clip via native compute (~$0.001/clip). Compare to anchor fingerprint. Mode B path: pull rendered_shots from upstream successRenderedShots branch. Validate negative_prompt_sha256 invariant across shots (forensic Hard Rule #10 inherit). Compute style fingerprint per shot (same native compute as Mode A). Mode C path: pull mode_c_plan + new_shot_prompts. Verify coverage envelope match between prompts and anchor coverage envelope. Out-of-envelope = halt with cost_overrun (folded code — coverage_envelope_mismatch semantically). Hard Rule #6 tier check: Mode C MUST be Enterprise.

4. Anchor style fingerprint load + identity verification. Load LOCKED anchor from brand_anchor_cache/{brand}/anchor-{anchor_id}.json. Compute SHA-256 of cache file canonical content. ASSERT cached_hash == brand_anchor_reference.anchor_sha256 == output.style_consistency_anchor.anchor_sha256 (three-way bit equality per Hard Rule #9). Hard FAIL → anchor_unavailable. Verify anchor_locked_date within 90-day freshness window — outside window = soft warning emit anchor_stale_warning in qc_warnings[] (v1.0 soft; v1.1+ may harden).

5. Style transfer / inheritance compute. Mode A: dispatch grade pass via Pika Style Tokens (primary) or Runway Style Reference (fallback) per shot. Cost ~$0.10–$0.40/shot. Attach negative prompt to every dispatch (inherit AI Video Gen Day 26 SKILL bundle composed template via upstream metadata.negative_prompt_sha256 — do NOT re-compose). Mode B: native CLIP + pHash + palette + motion grade compute per shot. Compare to anchor fingerprint. Compute style_match_score per shot. No engine call (cost ~$0.001/shot). Mode C: for each new_shot_prompt, dispatch Pika Style Tokens with anchor's style fingerprint embedded. Cost ~$0.10–$0.30/shot. Negative prompt attached.

6. Drift threshold check per shot. For each shot, compute style_match_score = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette (inherits AI Video Gen Day 23 §12 formula verbatim). If style_match_score < 0.85 (drift threshold) → emit drift_warning_bool: true per shot but do NOT halt (soft warning v1.0 per Hard Rule #12). If aggregate score across all shots < 0.70 (hard floor) → halt with style_drift_exceeded (failure cascade).

7. Brand finish layer application. Apply anchor's brand_finish_layer spec (LUT, color grade, optional vignette) to every shot. v1.0 = static finish (no per-shot variation across a reel). Compute brand_finish_layer_applied_bool per shot. Hard FAIL on any shot's failure → brand_finish_layer_missing (anchor incompleteness escalates to operator re-LOCK).

8. Cost ceiling check. Sum cost_incurred_usd across all shots in current invocation. Compare to tier_cost_ceiling_usd ($50 Pro / $120 Enterprise). Hard FAIL on overrun (>110% of ceiling per Hard Rule #7) → cost_overrun. Per-shot attribution emitted in errorEnvelope detail block (mirrors AI Video Gen Day 25 schema pattern).

9. Negative prompt SHA-256 invariant verification (Mode A & C only). For every dispatched engine call this invocation, verify negative_prompt_sha256 is consistent (single hash across all calls in the invocation). Mirror AI Video Gen §6 Check #10 — Hard Rule #10 enforcement chain. Hard FAIL → forensic log + qc_pre_flags_format_violation (re-uses code for negative-prompt-layer breach per §6.3 mapping). Mode B exempt — forensic verify upstream metadata.negative_prompt_sha256 matches known-valid template hash.

10. Construct output payload. Build successReplicatedShots payload per §3.1. Compute drift_summary aggregates (aggregate_style_match_score, shots_with_drift_warning, shots_with_drift_failure). Set handoff_targets array per pipeline canon: ["edit-director", "qc-agent"] for happy path; ["qc-agent", "human-reviewer"] if any shot has drift_warning_bool: true (Lever-3 default routes drift warnings to human review). Attach metadata block per §3.3 (style_fingerprint_summary + anchor_cache_version + runtime_environment_class).

11. Self-QC + emit. Run the 12-check list from §6. All PASS → emit successReplicatedShots. ≥1 FAIL on first attempt → regenerate offending field set with concrete fix instructions inlined → re-run 12-check. ≥1 FAIL on second attempt → emit errorEnvelope per Hard Rule #13. Validate output payload against output.schema.json (Day 33 LOCKED). Mark human_review_required: true per Lever-3 default (until Day 60+ Lever-2 graduation gate).

==================================================================
VOICE FOR WRITTEN RATIONALE FIELDS
==================================================================

Voice for written rationale fields: clinical-warm, operator-to-operator, present tense, ≤14 words per sentence, action verbs. No exclamation marks. No emoji. No hedging language ("might", "could potentially", "we believe"). State the decision and the why in one breath.

Emit JSON only. Now.
```

### 7.2 Why this prompt is shaped this way

Seven structural decisions are encoded in the prompt:

1. **Single-responsibility line first.** "Brand-aesthetic transfer onto rendered or sourced footage" sets the scope ceiling. The LLM cannot drift into shot design, hook selection, tier negotiation, plan editing, or re-rendering — those belong to upstream agents or are explicitly v1.1+ deferrals.

2. **Defense-in-depth declaration upfront.** Naming the 6th-layer firewall position primes the model to re-check rather than trust upstream. Trust-but-verify isn't a process — it's a system prompt clause. Style Replication is the LAST defense-in-depth layer before pixels ship downstream to Edit Director; the 6th-time firewall pass is the final guardrail.

3. **13 hard rules, numbered, terse.** Rules are the contract. Each rule maps to a self-QC check (§6) OR a tier-table enforcement OR an errorEnvelope code (§6.3 LOCKED namespace). The 13-rule count is normative — adding a 14th would mean re-running the cross-SPEC consistency review. **Parity with AI Video Gen §7:** also 13 rules. Cross-SPEC consistency invariant.

4. **Tier table embedded in the prompt, not external.** ProdCoord may have already passed the tier; AI Video Gen may have already validated the tier; runtime enforcement happens here. Embedding the table makes the LLM the source of truth for cost ceiling math AND Mode C gating, not a side document the orchestrator could forget to load.

5. **11-step process maps 1:1 to the §6 self-QC list.** Step 1 → Check #1 (qc_pre_flags shape) + Check #5 (anchor identity). Step 4 → Check #5 (3-part anchor) + Check #8 (anchor binding). Step 6 → Check #6 (drift). Step 7 → Check #9 (brand finish). Step 8 → Check #7 (cost ceiling). Step 9 → Check #10 (negative prompt). Step 10 → Check #11 (handoff). Step 11 → all 12 checks. This 1:1 mapping is the audit invariant: every step produces evidence one or more checks need.

6. **"Emit JSON only. Now." closing.** Eliminates the "thinking out loud" failure mode. ProdCoord §7 proved this works in 5/5 fixture runs (Day 18 SKILL bundle validation). AI Video Gen §7 proved this works in 5/5 fixture runs (Day 26 SKILL bundle validation). Inherit verbatim.

7. **Anchor-identity invariant (Hard Rule #9) elevated to Hard Rule status.** Style Replication is the FIRST agent in the pipeline where the anchor identity SHA-256 is the brand's signature — AI Video Gen renders the anchor pixels, but Style Replication is the agent that BINDS to them and propagates them across the reel. The three-way bit equality assertion (cached_hash == input_hash == output_hash) is the runtime guardrail against anchor-cache tampering. This is the only structural addition over AI Video Gen §7's rule set — every other rule has a verbatim parallel.

### 7.3 Tier table cost reconciliation (cross-reference with AI Video Gen tier table)

**Combined per-reel envelope (pipeline-level):**

| Tier | AI Video Gen ceiling | Style Replication ceiling | Combined reel envelope | Gross margin floor (5× per Day 6) | Tier price | Net contribution |
|------|---------------------:|--------------------------:|-----------------------:|------------------------------------|----------:|----------------:|
| Pro — Studio | $400 | $50 | $450 | $2,250 floor | Pro-tier | headroom above floor |
| Enterprise — Agency | $750 | $120 | $870 | $4,350 floor | Enterprise-tier | headroom above floor |

The combined Mode B reel envelope ($450 Pro / $870 Enterprise) sits comfortably below the 5× gross margin floor per tier. Mode C (Enterprise-only) is the highest-margin path: Style Replication Mode C ($120 ceiling) replaces AI Video Gen Mode B render ($750 ceiling) for net cost savings of $630/reel = ~$10K/yr at 16 reels/yr volume. This is the economic justification for Mode C's existence in the v1.0 SPEC.

**Margin floor reconciliation flag (carried from outline §4):** Per-reel Style Replication ceiling vs. Style Replication "unit cost" alone shows Pro at 4.17× (50 / 12 anchor compute + grade pass envelope) and Enterprise at 1.72× (120 / 70 Mode C compute + grade pass envelope). Both are below the 5× gross-margin canon if taken in isolation. **Day 31 §13 LOCK decision:** treat the per-agent margin as not-the-relevant-floor; pipeline-level reel envelope reconciliation (above table) IS the relevant floor; Style Replication's economic role is brand-discipline-at-low-cost, not maximize-margin-per-agent. Pricing-tier conversation deferred to Sequel Digital sales playbook (Week 6+).

---

## §10 — Replication Field Map (LOCKED-as-drafted Day 30)

**Inheritance from AI Video Gen §10:** three-column shape (source → destination → transform). **Difference:** Style Replication reads from THREE upstream sources depending on mode — `production_plan.json` (Mode A: mode_a_plan branch; Mode C: mode_c_plan branch) AND `rendered_shots.json` (Mode B passthrough from AI Video Gen) — plus the LOCKED brand anchor cache (`brand_anchor_cache/{brand}/anchor-{anchor_id}.json`). The audit trail through production plan / storyboard / script / brief is preserved via `parent_chain[]`.

**Schema discipline:** All `production_plan.json` field references inherit from ProdCoord output.schema.json (Day 17 LOCKED — read-only). All `rendered_shots.json` field references inherit from AI Video Gen output.schema.json (Day 25 LOCKED — read-only). All `replicated_shots.json` field references will be enforced by `schemas/style-replication-agent/output.schema.json` (Day 33 LOCK target). The map below is the field-level contract that Day 33 schemas MUST enumerate.

### 10.1 The field map (26 rows — per-shot + reel-level aggregate)

**Per-shot rows (rows 1–18):**

| Source field | `replicated_shots.json` destination | Transform | Mechanic |
|--------------|-------------------------------------|-----------|----------|
| `production_plan_id` (or `rendered_shots[*].production_plan_id` Mode B) | `production_plan_id` | Passthrough (audit trail). | Verbatim string copy. The `production_plan_id` is the upstream anchor in the audit chain. No transformation. |
| `parent_chain[0]` (brief_id) | `parent_chain[0]` | Passthrough — first element of 5-tuple. | Read from input parent_chain. Verbatim copy. **5-tuple LOCK decision Day 30 (§13 Decision #15 RESOLVED):** Style Replication extends from 4-tuple (AI Video Gen LOCKED) to 5-tuple by appending own `replication_set_id` at position [4]. Cross-SPEC §3.9 amendment required Day 32 LOCK ceremony — flagged. |
| `parent_chain[1]` (script_id) | `parent_chain[1]` | Passthrough — second element. | Read from input parent_chain. Verbatim copy. |
| `parent_chain[2]` (storyboard_id) | `parent_chain[2]` | Passthrough — third element. | Read from input parent_chain. Verbatim copy. |
| `parent_chain[3]` (production_plan_id or rendered_shots_set_id) | `parent_chain[3]` | Passthrough — fourth element. | Read from input parent_chain. Verbatim copy. Note: in Mode B, position [3] is the AI Video Gen `rendered_shots_set_id`; in Mode A and Mode C, position [3] is the `production_plan_id`. The 4-tuple LOCKED at AI Video Gen is preserved here as positions [0..3]. |
| Generated by this agent | `parent_chain[4]` (replication_set_id) | NEW — 5-tuple extension. | The agent generates a fresh `replication_set_id` (UUIDv7 per Cross-SPEC §3.9 ID-generation canon) and appends to parent_chain at position [4]. This is the only agent in the pipeline that extends parent_chain to 5-tuple at v1.0. Schema enforces `prefixItems` cardinality of exactly 5. |
| `brand_id` | `brand_id` | Passthrough. | Verbatim string copy. v1.0 expected value = `"REINVENTED"`. Multi-brand v1.1+ (Cross-SPEC Open Question — gated on first paid Sequel Digital client onboarding). |
| `tier` | `tier` | Passthrough — drives cost ceiling re-validation. | Verbatim enum copy from `{"Pro", "Enterprise"}`. This value is the lookup key for `tier_cost_ceiling_usd` (§7.3 tier table). Re-asserted in Check #4 (tier authorization, folded into Check #7 cost overrun per §6.3). Pilot / Starter never reach this field. |
| `lever` | `lever` | Passthrough — drives `metadata.human_review_required`. | Verbatim integer copy from `{1, 2, 3}`. Lever 3 (default v1.0) = every reel reviewed by human + QC Agent. Drives `metadata.human_review_required: bool`. Style Replication ALWAYS sets `human_review_required: true` when any shot has `drift_warning_bool: true`, regardless of lever (drift escalation supersedes lever default). |
| `production_mode` | `production_mode` | Passthrough — MUST equal `"A"`, `"B"`, or `"C"`. | Verbatim const copy. Schema enforces `enum: ["A", "B", "C"]` on the destination. The pre-flight check at Process Step 1 already halts if mode is invalid. |
| `total_shots` (Mode A/C: `len(source_clips)` or `len(new_shot_prompts)`; Mode B: `len(rendered_shots)`) | `total_shots` | Derived count. | Integer count derived from active mode's input array length. Used by Check #6 (Mode coverage): `len(replicated_shots) == total_shots` is the success invariant for `status="replicated"`. |
| `source_clips[*].clip_id` (Mode A) OR `rendered_shots[*].shot_id` (Mode B) OR `new_shot_prompts[*].shot_id` (Mode C) | `replicated_shots[*].shot_id` | 1:1 binding. | Verbatim string copy per shot. The `shot_id` is the join key for cross-record audit (storyboard → production plan → rendered shot → replicated shot). Format pattern inherited: `^shot-\d{3}$` (Mode B and Mode C) OR `^clip-\d{3}$` (Mode A — user-source naming convention). |
| Mode A: `source_clips[*].asset_uri` (user-source URI); Mode B: `rendered_shots[*].asset_uri` (ars://renderset/...); Mode C: generated by agent | `replicated_shots[*].source_asset_uri` | Passthrough on Mode A/B; generated on Mode C. | Records the source pixels that style transfer operated on. In Mode A, the user-source URI. In Mode B, the upstream rendered URI. In Mode C, the agent records the ephemeral intermediate URI (style-transfer engine output, before brand finish layer) — but only for forensic audit; the final asset URI (post-finish-layer) is in `asset_uri` below. Schema enforces `^ars://[a-z-]+/[A-Z]+/[0-9]{4}-[0-9]{2}-[0-9]{2}/.*$` pattern (no absolute external URLs per Hard Rule #8). |
| Generated by this agent | `replicated_shots[*].asset_uri` | NEW — replicated output URI. | Generated by the agent. Format: `ars://replication/<brand_id>/<YYYY-MM-DD>/<replication_set_seq>/shot-<NNN>.<ext>`. This is the URI of the final replicated asset (post-style-transfer + post-brand-finish-layer). Schema enforces the same `ars://` prefix pattern. NEVER absolute external CDN URL. |
| Generated by this agent (Step 6) | `replicated_shots[*].style_match_score` | NEW — computed per Step 6. | Numeric value in [0.0, 1.0]. Computed per shot as `style_match_score = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette` (inherits AI Video Gen Day 23 §12 formula verbatim). Schema enforces `minimum: 0.0, maximum: 1.0`. |
| Generated by this agent (Step 6) | `replicated_shots[*].drift_warning_bool` | NEW — soft warning flag. | Boolean. TRUE if `style_match_score < 0.85` (drift threshold). FALSE if `style_match_score >= 0.85`. Triggers Lever-3 human review routing per Hard Rule #12. |
| Generated by this agent (Step 7) | `replicated_shots[*].brand_finish_layer_applied_bool` | NEW — brand finish layer success flag. | Boolean. TRUE if anchor's `brand_finish_layer` spec successfully applied (LUT + color grade + optional vignette). FALSE = halt with `brand_finish_layer_missing` per Check #9. v1.0 = anchor incompleteness is non-recoverable; operator must re-LOCK. |
| Generated by this agent (Step 5/6/7) | `replicated_shots[*].cost_incurred_usd` | NEW — per-shot cost. | Numeric value in USD. Sum of: native CLIP/pHash/palette compute (~$0.001) + style-transfer engine dispatch ($0.10–$0.40 Mode A/C; $0 Mode B) + brand finish layer apply (~$0.001). Schema enforces `minimum: 0.0`. Used by Check #7 cost ceiling aggregation. |

**Reel-level aggregate rows (rows 19–26):**

| Source / generated | `replicated_shots.json` destination | Transform | Mechanic |
|--------------------|-------------------------------------|-----------|----------|
| Generated by this agent (Step 4) | `style_consistency_anchor.anchor_id` | Passthrough from `brand_anchor_reference.anchor_id`. | Verbatim copy from input. Anchor identity preserved verbatim — anchor is the brand's signature. |
| Generated by this agent (Step 4) | `style_consistency_anchor.anchor_sha256` | NEW — three-way bit equality assertion. | Computed by agent in Step 4. ASSERTed equal to `brand_anchor_reference.anchor_sha256` AND cache-stored hash per Hard Rule #9. Schema enforces `pattern: "^[a-f0-9]{64}$"` (lowercase hex, exactly 64 chars). |
| Generated by this agent (Step 4) | `style_consistency_anchor.anchor_locked_date` | Passthrough from cache. | ISO 8601 date string (`YYYY-MM-DD`). v1.0 freshness gate = 90-day soft warning. |
| Generated by this agent (Step 6 aggregation) | `drift_summary.aggregate_style_match_score` | NEW — reel-level aggregate. | Mean of `replicated_shots[*].style_match_score`. Numeric in [0.0, 1.0]. Used by Check #6 hard floor breach test (<0.70 = halt with `style_drift_exceeded`). |
| Generated by this agent (Step 6 aggregation) | `drift_summary.shots_with_drift_warning` | NEW — count. | Integer count of shots where `drift_warning_bool: true`. |
| Generated by this agent (Step 6 aggregation) | `drift_summary.shots_with_drift_failure` | NEW — count. | Integer count of shots where individual `style_match_score` triggered a Check #6 failure (hard floor at per-shot level — currently disabled in v1.0; reserved for v1.1+ per-shot hard FAIL policy). v1.0 ALWAYS equals 0; reserved field. |
| Generated by this agent (Step 8) | `replication_telemetry.total_replication_cost_usd_actual` | NEW — reel-level cost. | Sum of `replicated_shots[*].cost_incurred_usd`. Numeric USD. Used by Check #7 cost ceiling compliance: `total ≤ tier_cost_ceiling_usd × 1.10`. |
| Derived by agent (§7.3 tier lookup) | `replication_telemetry.tier_cost_ceiling_usd` | Lookup from §7.3 tier table. | NOT a passthrough — derived by tier lookup. Pro → $50. Enterprise → $120. Schema enforces joint validation: `{tier: "Pro", tier_cost_ceiling_usd: 50}` OR `{tier: "Enterprise", tier_cost_ceiling_usd: 120}`. |

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

Four fields are reserved in the field map but not yet active in v1.0:

- **Per-engine drift threshold (`replicated_shots[*].engine_specific_drift_threshold`).** v1.0 uses a single 0.85 threshold inherited from AI Video Gen Day 23 §12. v1.1+ may surface per-engine recalibration (Pika Style Tokens drift may differ structurally from Runway Style Reference drift). Cross-SPEC Open Question — defer.
- **Anchor versioning beyond v1.0 (`style_consistency_anchor.anchor_version`).** v1.0 uses a single LOCKED anchor per brand. v1.1+ may support anchor versions (e.g., `anchor-REINVENTED-v2-locked-2026-05-15` vs. `anchor-REINVENTED-v3-locked-2026-07-01`) with explicit version selection at runtime. Deferred.
- **Multi-pass grade refinement (`replicated_shots[*].grade_pass_count`).** v1.0 = single-pass grade only (Mode A). v1.1+ enterprise creative tier may allow 2–3 pass refinement. Deferred.
- **Third-party LUT import (`brand_finish_layer.lut_source`).** v1.0 inherits LUT from anchor cache only. v1.2+ creative path may support DaVinci `.cube` file import. Deferred.

### 10.3 No-touch fields (read-only references)

These fields are read by the agent but never written to its output (audit trail only — downstream agents read them from upstream sources directly):

- `storyboard.shoot_logistics.*` — Mode A live-shoot context; relevant to Mode A but already captured in `production_plan.mode_a_plan.source_clips[*].shoot_metadata` per ProdCoord canon. Style Replication does not echo to output.
- `rendered_shots[*].render_dispatch_log[*]` — AI Video Gen's per-shot render history; relevant to Mode B forensic audit but already captured upstream. Style Replication reads `negative_prompt_sha256` from this for Hard Rule #10 verification but does not echo the full log.
- `brief.target_audience` — passes through to `metadata.brief_summary` but not duplicated as a top-level field. Reduces output size.
- `production_plan.mode_b_plan.style_consistency_anchor.*` — AI Video Gen wrote this in Mode B; Style Replication reads but emits its own `style_consistency_anchor` block with anchor_sha256 verification (the agent's authority block).

### 10.4 Schema authoring note (for Day 33)

The Day 33 schema author must encode the field map above as JSON Schema Draft 2020-12 constraints. Specifically:
- `parent_chain` MUST use `prefixItems: [..., ..., ..., ..., ...]` AND `items: false` to enforce exact **5-tuple** cardinality (Style Replication extends from 4-tuple LOCKED at AI Video Gen — schema amendment required at Cross-SPEC §3.9 Day 32 LOCK ceremony).
- `tier_cost_ceiling_usd` MUST use `allOf` joint validation: `{tier: "Pro", tier_cost_ceiling_usd: 50}` OR `{tier: "Enterprise", tier_cost_ceiling_usd: 120}`.
- `production_mode` MUST use `enum: ["A", "B", "C"]` (broader than AI Video Gen's `const: "B"` — Style Replication serves all three modes).
- `anchor_sha256` MUST use `pattern: "^[a-f0-9]{64}$"` (lowercase hex, exactly 64 chars).
- `style_match_score`, `drift_summary.aggregate_style_match_score` MUST use `minimum: 0.0, maximum: 1.0`.
- `cost_incurred_usd`, `total_replication_cost_usd_actual` MUST use `minimum: 0.0`.
- `replication_status` MUST use `enum: ["replicated", "replicated_with_warning", "failed"]`.
- `failure_code` (errorEnvelope branch) MUST use `enum: ["anchor_unavailable", "style_drift_exceeded", "brand_finish_layer_missing", "cost_overrun", "qc_pre_flags_format_violation", "style_replication_agent_failed"]` — exactly the 6 codes from §6.3 LOCKED namespace. Schema MUST NOT enumerate retired codes (`not_replication_compatible`, `palette_extraction_failure`, `motion_grade_mismatch`, `tier_constraint_violation`, `coverage_envelope_mismatch`) — those are subsumed by the 6 LOCKED codes per §6.3 narrowing.

### 10.5 Mode-by-mode field activation matrix

To make the per-mode field map traversal explicit at SKILL build time (Day 34), the table below maps each row to which modes activate the field:

| Field | Mode A | Mode B | Mode C | Notes |
|-------|:------:|:------:|:------:|-------|
| `parent_chain[3]` (rendered_shots_set_id) | NO | YES | NO | Mode B-specific upstream identity |
| `parent_chain[3]` (production_plan_id) | YES | NO | YES | Mode A/C upstream identity |
| `source_clips[*].clip_id` (Mode A) | YES | NO | NO | Mode A-only input array |
| `rendered_shots[*].shot_id` (Mode B) | NO | YES | NO | Mode B-only input array |
| `new_shot_prompts[*].shot_id` (Mode C) | NO | NO | YES | Mode C-only input array |
| `replicated_shots[*].source_asset_uri` | YES (user-source URI) | YES (rendered URI) | YES (intermediate URI) | All three modes but distinct semantics per mode |
| Style transfer engine cost | $0.10–$0.40/shot | $0/shot (no engine call) | $0.10–$0.30/shot | Mode B is the cheapest mode by design |
| Negative prompt SHA-256 verification | Per-dispatch | Forensic-only (upstream) | Per-dispatch | Mode B exempt from per-dispatch verification |
| Coverage envelope check | NO | NO | YES | Mode C-specific (Hard Rule #6 enforcement) |

The activation matrix is the basis for the Day 34 SKILL bundle's `dispatch.py` mode-switch logic.

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 30 · status updates only)

**Calendar inherited from outline §0 build calendar.** Day 30 author task per outline: status updates only — calendar shape unchanged. Updates encoded below.

### 14.1 Calendar (Day 29 → Day 37 — Style Replication v1.0 LOCK trajectory)

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 29 | Mon May 18 · Wk5D3 | **Style Replication Agent v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 30 | Tue May 19 · Wk5D4 | **SPEC body partial 1: §6 (12-Check Self-QC, 12 checks bipartite-covering 6 errorEnvelope codes) + §7 (System Prompt v1.0 frame + 13 hard rules + tier table + 11-step process + voice rule) + §10 (Field Map 26 rows: 18 per-shot + 8 reel-level) + §14 (Implementation Plan status updates)** | ✅ DONE — this document, LOCKED-as-drafted | Donna overnight |
| Day 31 | Wed May 20 · Wk5D5 | **SPEC body partial 2: §8 (Performance Targets — 9 metric categories) + §9 (5 Test Fixtures — TC-01..TC-05) + §11 (Cost Model engine snapshot + per-tier cost discipline) + §12 (Style Consistency Math — inherits AI Video Gen Day 23 §12 verbatim) + §13 (12–15 Critical Decisions LOCKED — 9 LOCKED-as-drafted Day 29 + 6 PRELIMINARY operator amendments) + §15 (Change Log v1.0 lifecycle entries) + §16 (Metadata Block — 11 Cross-SPEC §3.9 canonical + 3 Style Replication additions)** | ⬜ TARGET | Donna overnight + Jamila §13 amendments |
| Day 32 | Thu May 21 · Wk5D6 | **SPEC v1.0 LOCK CANDIDATE** — Cross-SPEC consistency review against ProdCoord SPEC + AI Video Gen SPEC + Cross-SPEC canon §3. Reconciliation of any naming / errorEnvelope / qc_pre_flags drift. 11-item reviewer checklist (parallels Day 24 AI Video Gen LOCK candidate). LOCK signed. | ⬜ TARGET | Donna overnight + Jamila approval |
| Day 33 | Fri May 22 · Wk5 close | **input.schema.json + output.schema.json** (Draft 2020-12, polymorphic output `oneOf [successReplicatedShots, errorEnvelope]`, 6 errorEnvelope codes enumerated, 5-tuple parent_chain via `prefixItems`, per-mode input branches). Self-validating against 5 test fixtures. | ⬜ QUEUED | Donna overnight |
| Day 34 | Sat May 23 · Wk6D1 (Wk5 spillover) | **SKILL bundle** (~10–15 files: SKILL.md, README, user-template, 2 schemas, 5 test fixtures, dispatch.py mode-switch, negative_prompt_template.md inherit reference). 5/5 inputs validate clean. Mirrors AI Video Gen Day 26 SKILL bundle 23-file pattern (narrower because no per-engine adapters at v1.0). | ⬜ QUEUED | Donna overnight |
| Day 35 | Sun May 24 · Wk6D2 | **REST DAY** — no build. Optional Jamila ~30 min review of Wk5 close. Day 36 LLM Test Runbook scaffold may be authored under Rest Day-compounding pattern (Day 21 + Day 28 precedent). | — | Jamila |
| Day 36 | Mon May 25 · Wk6D3 | **LLM Test Runbook** (paste-and-run, pattern from Day 11 + Day 19 + Day 27). Operator-gated. ≤$5 + 30–45 min sit-down (slightly higher than AI Video Gen Day 27 because Mode A and Mode C touch paid style-transfer APIs in test fixtures — dry-run mode = $4 Opus tokens; live mode = ≤$50 worst case for 5 fixtures × 5 shots × $0.40 max per shot + buffer). | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 37 | Tue May 26 · Wk6D4 | **v1.0 LOCK** (Wk5 close target slipped by 1 day · operator-gated sit-down). Style Replication v1.0 LOCK gates itself on AI Video Gen v1.0 LOCK first — if AI Video Gen v1.0 LOCK is still PENDING on Day 37, Style Replication LOCK ceremony cannot complete (Style Replication's anchor binding requires LOCKED upstream renders). | ⬜ TARGET — hard-gated on AI Video Gen v1.0 LOCK | Jamila + Donna |
| Day 38+ | Wed May 27+ · Wk6D5+ | **Week 6 commercial launch start.** Lovable landing page copy spec, intake flow scaffold, first paid client onboarding. Style Replication Mode B production gate live (Mode A + Mode C remain Enterprise-only until first 30 reels of Mode B data prove Lever-2 graduation). | ⬜ QUEUED | Jamila + Donna |

### 14.2 Dependencies that MUST exist before Day 34 SKILL bundle build

| Dependency | Status | LOCK day |
|------------|--------|----------|
| Production Coord Agent v1.0 SPEC LOCKED | ✅ DONE | Day 14 |
| Production Coord input.schema.json + output.schema.json LOCKED | ✅ DONE | Day 17 |
| Production Coord SKILL bundle LIVE | ✅ DONE | Day 18 |
| Cross-SPEC Consistency Review LOCKED | ✅ DONE | Day 12 |
| AI Video Gen v1.0 SPEC body LOCKED-as-drafted (§6/§7/§10/§14) | ✅ DONE | Day 22 |
| AI Video Gen v1.0 SPEC body LOCKED (§8/§9/§11/§12/§13/§15/§16) | ✅ DONE | Day 23 |
| AI Video Gen v1.0 SPEC LOCK CANDIDATE | ✅ DONE | Day 24 (operator ratification Items 8 + 11 still PENDING) |
| AI Video Gen output.schema.json LOCKED | ✅ DONE | Day 25 |
| AI Video Gen SKILL bundle LIVE | ✅ DONE | Day 26 |
| AI Video Gen Day 27 LLM Test Runbook AUTHORED | ✅ DONE | Day 27 (operator sit-down outcome UNCONFIRMED entering Day 30) |
| AI Video Gen v1.0 LOCK (final operator-gated sign-off) | ⚠️ PENDING | Day 28+ — operator pickup |
| Style Replication SPEC outline §0–§5 | ✅ DONE | Day 29 |
| Style Replication SPEC body §6 + §7 + §10 + §14 LOCKED-as-drafted | ✅ DONE — this document | Day 30 (today) |
| Style Replication SPEC body §8 + §9 + §11 + §12 + §13 + §15 + §16 LOCKED | ⬜ TARGET | Day 31 |
| Style Replication SPEC v1.0 LOCK CANDIDATE | ⬜ TARGET | Day 32 |
| Style Replication schemas LOCKED | ⬜ TARGET | Day 33 |
| brand_anchor_cache canonical format spec (anchor JSON schema — embedded in SKILL.md or standalone?) | ⬜ Day 31 §13 author decision | Day 31 |

### 14.3 Cross-SPEC §3 adherence (preliminary audit — full audit Day 32 LOCK)

| Cross-SPEC dimension | Day 30 partial 1 status |
|----------------------|-------------------------|
| §3.1 naming canon (snake_case agent_id) | ✅ `style-replication-agent` agent_id verified; slot 11 code `style_replication_agent_failed` matches canon |
| §3.2 literal_seed_inherit precedent | ✅ Inherited as `literal_fingerprint_inherit` (Style Replication's analog — anchor fingerprint propagates verbatim, no semantic blending v1.0) per Hard Rule #11 |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord Day 14 + AI Video Gen Day 25 shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) per §6.4 |
| §3.4 qc_pre_flags array minimum 4 entries + snake_case | ✅ Enforced via Check #12 (§6.1) |
| §3.5 mode matrix per Day 12 | ✅ Mode A + B + C support documented; tier↔mode gating per §7.3 tier table |
| §3.6 slot 11 reserved naming | ✅ `style_replication_agent_failed` reserved at §6.3 |
| §3.7 qc_pre_flags format snake_case regex | ✅ Enforced via Check #12 with regex `^[a-z][a-z0-9_]{0,63}$` |
| §3.8 tier↔mode firewall 6th defense-in-depth pass | ✅ §6.1 Check #4 + §7 Hard Rule #6 + Step 2 of 11-step process |
| §3.9 metadata block 11 canonical fields | ✅ Inherited from AI Video Gen Day 25 schema; **5-tuple parent_chain extension** documented at §10.1 (amendment flagged for Day 32 Cross-SPEC LOCK ceremony) |
| §3.10 cost ceiling authority $ per tier | ✅ Pro $50 / Enterprise $120 per §7.3; combined pipeline envelope reconciled in §7.3 cross-reference table |
| §3.11 LOCK respect (no modification of upstream LOCKED canon) | ✅ Day 30 partial 1 references AI Video Gen + ProdCoord canon read-only; no modifications |

11 of 11 dimensions ✅ at partial 1 stage. Full LOCK audit Day 32.

### 14.4 Rest Day honored

Day 21 (Sun May 10) and Day 28 (Sun May 17) — no build sessions per Daily OS pillar (Rest → Body → Money → Authority → Relationships). Spec/docs work allowed (Day 21's scaffold document was the canonical Rest Day-compounding example; Day 28's primer extended the pattern with 15-decision pre-scaffold for Day 29 Style Replication outline). Day 35 (Sun May 24) honors the same pattern — no build; optional Day 36 scaffold per the pattern's evolution.

### 14.5 Day 30 sprint completion summary

| Section | Status | Wall-clock | Notes |
|---------|--------|------------|-------|
| §6 12-Check Self-QC List | ✅ DRAFTED | ~3 hr equivalent | All 12 checks fully drafted with failure-code mapping. Slot 11 reserved `style_replication_agent_failed` per Cross-SPEC §3.6. Error code namespace narrowed from outline's 9 candidates to 6 LOCKED (Day 30 narrowing decision documented in §6.3: `not_replication_compatible` → `anchor_unavailable` alias; `palette_extraction_failure` + `motion_grade_mismatch` → `style_drift_exceeded` cascade; `tier_constraint_violation` + `coverage_envelope_mismatch` → `cost_overrun` semantic fold). Bipartite coverage proof flagged for Day 32 LOCK audit. |
| §7 System Prompt v1.0 | ✅ DRAFTED | ~3 hr equivalent | Single fenced block: frame + 13 hard rules + tier table + 11-step process verbatim from outline §5 + voice rule verbatim from ProdCoord §7 + AI Video Gen §7. Seven structural decisions rationalized in §7.2. Tier table cost reconciliation table cross-references AI Video Gen tier ceilings (combined Pro reel envelope $450; Enterprise $870). |
| §10 Field Map | ✅ DRAFTED | ~2 hr equivalent | 26 rows: 18 per-shot, 8 reel-level aggregate. 5-tuple parent_chain extension LOCKED (Day 29 outline §13 Decision #15 RESOLVED today — flagged for Cross-SPEC §3.9 amendment Day 32). 4 v1.0 reserved fields enumerated. Mode-by-mode field activation matrix added (§10.5). Day 33 schema authoring notes embedded. |
| §14 Implementation Plan | ✅ DRAFTED | ~1 hr equivalent | Status updates only. Calendar shape unchanged from outline. Dependency table extended with Day 30 LOCK rows. Cross-SPEC §3 preliminary audit completed (11/11 ✅). |

Total Day 30 wall-clock estimate met: ~9 hr operator-paced (compressed in automated overnight session — pattern-inherited from AI Video Gen Day 22 + ProdCoord §14 proven wall-clock).

### 14.6 Day 31 partial 2 authoring runway

Day 31 must author:
- **§8 Performance Targets** — 9 metric categories: schema validity 100% / firewall catch 100% / anchor success ≥ 98% / drift rate ≤ 10%/reel / cost variance ±10% / Pro p50 2 min, p95 5 min / Enterprise p50 4 min, p95 9 min / retry rate ≤ 0.10/0.15 / fallback ≤ 4% shots. Pattern source: AI Video Gen Day 23 §8.
- **§9 5 Test Fixtures** — TC-01 Mode B happy 8-shot inherit / TC-02 Mode C hot path 5-shot / TC-03 Mode A grade pass with drift warning / TC-04 anchor_unavailable failure / TC-05 cost_overrun failure. Pattern source: AI Video Gen Day 23 §9 + ProdCoord Day 14 §9.
- **§11 Cost Model** — engine snapshot ($0.10 Pika Style Tokens / $0.40 Runway Style Reference / $0.001 native compute) + per-tier cost discipline 30–60% utilization sweet spot + calibration windows (10/30/90 reels).
- **§12 Style Consistency Math** — INHERITS AI Video Gen Day 23 §12 formula directly: `style_match_score = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette`. Drift threshold 0.85 soft / 0.70 hard floor. Zero new math to author — verbatim inheritance.
- **§13 Critical Decisions** — target 12–15 LOCKED. 9 LOCKED-as-drafted Day 29 outline (storage format, drift threshold inherit, brand finish authority, anchor binding rule, schema strategy, SKILL bundle authority, telemetry additions, calibration windows, v1.0 scope guardrail). 6 PRELIMINARY pending Day 31 operator amendment (style transfer engine selection, cost ceiling Pro $50 / Enterprise $120, Mode C hot path eligibility, failure mode coverage 6–8 codes RESOLVED today as 6, QC pre-flight checks 5–6, 4-tuple parent_chain extension RESOLVED today as 5-tuple). 2 of the 6 PRELIMINARY items resolved by today's Day 30 partial 1 — 4 remain for Day 31 operator amendment.
- **§15 Change Log** — v1.0 lifecycle entries: v1.0-draft-day-29 (outline §0–§5) + v1.0-draft-day-30 (this document — body §6/§7/§10/§14 LOCKED-as-drafted) + v1.0-draft-day-31 (§8/§9/§11/§12/§13/§15/§16 LOCKED) + v1.0-LOCK-CANDIDATE-day-32 + v1.0-schemas-day-33 + v1.0-SKILL-day-34 + v1.0-runbook-day-36 + v1.0-LOCKED-day-37.
- **§16 Metadata Block Schema** — 11 Cross-SPEC §3.9 canonical fields + 3 Style Replication additions (style_fingerprint_summary, anchor_cache_version, runtime_environment_class).

Day 31 partial 2 wall-clock estimate: ~8 hr operator-paced (compressed in automated overnight session).

### 14.7 Open Questions parked for Day 31 operator amendment (4 remaining)

After Day 30 partial 1 resolved 2 of the original 6 outline-stage PRELIMINARY items (failure mode coverage → 6 codes LOCKED; 4-tuple parent_chain → 5-tuple LOCKED), 4 PRELIMINARY items remain for Day 31:

1. **Style transfer engine v1.0 primary** — Pika Style Tokens proposed (cost $0.10/shot) vs Runway Style Reference (quality at Enterprise, $0.40/shot). Donna recommends Pika as primary + Runway as fallback (cost-discipline default). Operator amend Day 31 §13.
2. **Cost ceiling Pro $50 / Enterprise $120** — Donna recommends keep as LOCKED-as-drafted. Operator amend Day 31 §13 if pricing-tier conversation changes the floors.
3. **Mode C hot path eligibility (Enterprise + LOCKED anchor + coverage envelope match)** — Donna recommends keep as LOCKED-as-drafted. Operator amend Day 31 §13 if Mode C should be unlocked at Pro for specific use cases.
4. **QC pre-flight checks 5–6 count** — Donna recommends 6 (anchor identity, drift score, palette delta, motion grade tolerance, brand finish presence, cost projection). Operator amend Day 31 §13 if checks should be narrower or broader.

All 4 non-blocking for Day 31 partial 2 authoring. Defaults proposed; operator can override Day 31 §13 walk.

---

## §8 — Performance Targets

`<<TBD-D31>>`

*Day 31 author task. Pattern source: AI Video Gen SPEC §8 (Day 23 LOCKED). Targets to enumerate: schema validity rate (target 100% post-§6), firewall catch rate (target 100% — zero leaks), anchor success rate ≥ 98% (higher than AI Video Gen's 92% — Style Replication has fewer engine dependencies), drift rate ≤ 10%/reel (tighter than AI Video Gen's 15%/reel — Style Replication is dedicated to brand consistency), Pro p50 2 min / p95 5 min (faster than AI Video Gen 9/18 min — no per-shot render), Enterprise p50 4 min / p95 9 min, retry rate ≤ 0.10/0.15, fallback engine activation ≤ 4% shots, cost variance ±10%.*

---

## §9 — 5 Test Fixtures

`<<TBD-D31>>`

*Day 31 author task. Pattern source: AI Video Gen SPEC §9 (Day 23 LOCKED — 5 fixtures: TC-01 Pro Mode B happy path, TC-02 Enterprise Mode B happy path, TC-03 anchor failure, TC-04 cost overrun, TC-05 engine cascade failure). Style Replication fixtures: TC-01 Mode B 8-shot inherit happy path · TC-02 Mode C 5-shot hot path Enterprise · TC-03 Mode A grade pass with drift warning · TC-04 anchor_unavailable failure · TC-05 cost_overrun failure. 5 of 6 LOCKED error codes exercised in fixtures (`brand_finish_layer_missing` covered by schema-only fixture Day 33). Fixtures will live at `skills/style-replication-agent/tests/` per Day 34 SKILL bundle. Each fixture = (input.json, expected_output.json, expected_error_code_or_null, scenario_description).*

---

## §11 — Cost Model (engine snapshot + per-tier cost discipline)

`<<TBD-D31>>`

*Day 31 author task. Pattern source: AI Video Gen SPEC §11 (Day 23 LOCKED). Engine $/shot lookup: Pika Style Tokens $0.10/shot (primary Mode A + Mode C), Runway Style Reference $0.40/shot (fallback Mode A + Mode C), native CLIP/pHash/palette compute $0.001/shot (Mode B + all-mode fingerprint extraction). Per-tier cost discipline: Pro 30% utilization sweet spot at $15/reel; Enterprise 40% utilization sweet spot at $48/reel. Calibration windows: 10-reel canary / 30-reel Lever-2 graduation / 90-reel autonomous.*

---

## §12 — Style Consistency Math

`<<TBD-D31>>`

*Day 31 author task. **INHERITS AI Video Gen Day 23 §12 formula verbatim:** `style_match_score = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette`. Drift threshold 0.85 soft warning v1.0 (mirrors AI Video Gen Day 23 §13 Decision #4 inherit). Aggregate floor 0.70 hard FAIL → `style_drift_exceeded` per §6.3. Anchor identity check via SHA-256 (three-way bit equality per Hard Rule #9). Cross-SPEC §3.2 literal_seed_inherit precedent applies to Style Replication's anchor-binding rule as `literal_fingerprint_inherit`. Zero new math to author — verbatim inheritance with three-way anchor identity assertion added.*

---

## §13 — Critical Decisions LOCKED (target 12–15)

`<<TBD-D31>>`

*Day 31 author task. 9 LOCKED-as-drafted Day 29 (storage format, drift threshold inherit, brand finish authority, anchor binding rule, schema strategy, SKILL bundle authority, telemetry additions, calibration windows, v1.0 scope guardrail). 2 RESOLVED Day 30 by this partial 1 (failure mode coverage → 6 codes LOCKED §6.3; 4-tuple parent_chain extension → 5-tuple LOCKED §10.1). 4 PRELIMINARY pending Day 31 operator amendment (style transfer engine primary, cost ceiling, Mode C eligibility, QC pre-flight checks count). Target: 13–15 LOCKED on Day 31.*

---

## §15 — Change Log + Version History

`<<TBD-D31>>`

*Day 31 author task. Pattern source: AI Video Gen SPEC §15 (Day 23 LOCKED). Initial entries:*
- *v1.0-draft-day-29 — outline §0–§5 SHIPPED (`ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md`)*
- *v1.0-draft-day-30 — this document — body §6/§7/§10/§14 LOCKED-as-drafted; §8/§9/§11/§12/§13/§15/§16 RESERVED*
- *v1.0-draft-day-31 — §8/§9/§11/§12/§13/§15/§16 LOCKED*
- *v1.0-LOCK-CANDIDATE-day-32 — Cross-SPEC consistency reconciliation signed*
- *v1.0-schemas-day-33 — input.schema.json + output.schema.json published*
- *v1.0-SKILL-day-34 — SKILL bundle live*
- *v1.0-runbook-day-36 — LLM Test Runbook authored*
- *v1.0-LOCKED-day-37 — operator-gated LOCK ceremony complete*

---

## §16 — Metadata Block Schema

`<<TBD-D31>>`

*Day 31 author task. Pattern source: AI Video Gen Day 25 metadata block schema (11 Cross-SPEC §3.9 canonical fields). Style Replication additions (3 fields):*
- *`style_fingerprint_summary` — {pHash_method, clip_model_version, palette_extraction_method, drift_threshold_used}*
- *`anchor_cache_version` — string version identifier for cache layer at runtime*
- *`runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16*

*Total metadata block: 14 fields. Cross-SPEC §3.9 amendment Day 32 LOCK ceremony required for the 3 additions + 5-tuple parent_chain.*

---

## Mirror status

- Source: `ars/ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` (this document) + `ars/build-log-2026-05-19.md`
- Mirror destination: `/outputs/ars/ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` + `/outputs/ars/build-log-2026-05-19.md`
- Mirror verification: forthcoming in this session's mirror step

---

*Day 30 ships clean. Day 31 build session is fully primed — §8 + §9 + §11 + §12 + §13 + §15 + §16 all have their LOCK targets defined, with 9 of 15 critical decisions LOCKED-as-drafted in Day 29 outline + 2 resolved today (6 codes + 5-tuple). Operator pickup: review 4 remaining PRELIMINARY §13 items at next 30-min block; ratify Items 8 + 11 of AI Video Gen LOCK candidate at next 30-min block; observe + sign off on Day 27 LLM Test sit-down at next 30–45 min block. All three actions are independent and any can move first. Day 32 LOCK CANDIDATE requires AI Video Gen v1.0 LOCK status confirmed FIRST — gating dependency reaffirmed.*
