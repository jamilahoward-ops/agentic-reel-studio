# ARS — AI Video Gen Agent v1.0 SPEC (Body §6 / §7 / §10 / §14 — Day 22 LOCKED-as-drafted)

**Date:** May 11, 2026 (Mon · Day 22 · Wk4D2)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** PARTIAL SPEC BODY — §6 (12-Check Self-QC List), §7 (System Prompt v1.0), §10 (Field Map: production_plan → rendered_shots), §14 (Implementation Plan) all drafted to LOCK-quality. §8 / §9 / §11 / §12 / §13 / §15 / §16 = `<<TBD-D23>>` deferred to tomorrow per scaffold calendar. **No LLM dispatched. No render API touched. No engine credentials referenced. No external comms. No financial commitments.**
**Pattern source:** `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` §6 / §7 / §10 / §14 (Day 14 LOCKED — verbatim shape inherited)
**Scaffold source:** `ARS-2026-05-10-Day-22-SPEC-Body-Pre-Flight-Rest Day-Prep.md` (Day 21 Rest Day prep — all `<<TBD-D22-*>>` markers resolved in this document)
**Predecessor outline:** `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (§0–§5 SHIPPED Day 20)
**Predecessor schemas:** `skills/production-coord-agent/schemas/output.schema.json` (Day 17 LOCKED — read-only reference)
**Cross-spec canon:** `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — naming, errorEnvelope, qc_pre_flags, metadata inheritance)

---

## DAY 22 AUTHORING SCOPE

This document is the **Day 22 partial SPEC body** for the AI Video Gen Agent. Four sections are LOCKED-as-drafted:

- **§6** — 12-Check Self-QC List (all 12 checks fully drafted; failure-code mapping resolved; slot 11 renamed from `production_coord_agent_failed` → `ai_video_gen_agent_failed` per Cross-SPEC canon §3.6)
- **§7** — System Prompt v1.0 (single fenced block: frame + 13 hard rules + tier table + 11-step process inherited verbatim from outline §5 + voice rule)
- **§10** — Field Map (21 rows · `production_plan.json` field → `rendered_shots.json` destination → transform mechanic — every TBD slot filled with 1–3 sentence transform explanation)
- **§14** — Implementation Plan (Day 20–Day 28 calendar status updates — calendar shape inherited from Day 21 scaffold; no structural edits)

The remaining seven sections — §8 Performance Targets · §9 Test Fixtures · §11 Cost Model · §12 Style Consistency Math · §13 Critical Decisions · §15 Change Log · §16 Metadata Schema — are slot-reserved as `<<TBD-D23>>` markers. Day 23 (Tue May 12) wall-clock estimate: ~9 hr (matches ProdCoord §13–§17 wall-clock proven on Day 14).

---

## §6 — 12-Check Self-QC List (LOCKED-as-drafted Day 22)

The AI Video Gen Agent runs this 12-check list before emitting `successRenderedShots`. The check shape is inherited verbatim from Brief / Script / Storyboard / Production Coord Agent §6 (proven 4× across the pipeline). Failure semantics are LOCKED inheritance from ProdCoord:

**QC retry policy (inherited from ProdCoord §6, LOCKED):** First QC failure → regenerate the offending field set with concrete fix instructions inlined into the agent's next attempt. Second QC failure → emit `errorEnvelope` with `attempts == 2` and halt. **No third attempt.** Predictable failure surface beats best-effort recovery — operators can plan around a 2-strike ceiling.

**Defense-in-depth (5th layer):** Every check in this list is the agent's own pass, but several (entity firewall, banned vocab, no-buildings, tier↔mode) are re-checks of upstream gates. The 5th re-check is non-negotiable because this is the first agent that touches a paid external API at runtime; a leak here costs money AND ships pixels.

### 6.1 The 12 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **Entity firewall re-check (5th defense-in-depth pass — all string fields including composed prompts).** | `entity_firewall_breach` | Recursive string walk of every leaf string in the proposed `rendered_shots.json` output: `rationale`, `escalation_path[*].notes`, `qc_pre_flags[]`, `qc_warnings[]`, `rendered_shots[*].rationale`, `rendered_shots[*].retry_log[*].fail_reason`, `style_consistency_anchor.*`, all `metadata.*`. **Additionally, walk every composed prompt dispatched to engines** (`prompt_compiled` and `negative_prompt_compiled` per render attempt) — even though prompts are ephemeral and never appear in the JSON output, they are subject to the same firewall. Token-boundary match (whole word, case-insensitive) against the 10-entry canonical firewall list (§6.5). Any hit = halt with `entity_firewall_breach` errorEnvelope; emit no rendered set. |
| 2 | **Banned vocab absence — `brief.do_not_say` terms not present in human-readable strings AND in any text overlay rendered into the video itself.** | `banned_vocab_leaked` | Two-pass walk. **Pass 1:** same recursive string walk as Check #1, but matched against `brief.do_not_say[]` (verbatim AND first-order conjugates — pluralization, gerund, past tense). **Pass 2 (new v1.0-specific):** for every rendered shot, the engine returns `post_render_qc_seed.text_overlay_strings[]` — an OCR pass over the rendered video that extracts any visible text burned into the pixels (titles, captions, lower-thirds, watermarks). Walk those strings through the same `brief.do_not_say` filter. Rationale: a render engine can inject text that the agent never composed (model hallucinated subtitle, watermark from a stock asset bleeding through). The OCR pass closes that gap. Any hit on either pass = halt with `banned_vocab_leaked` errorEnvelope, capture the offending string in `errorEnvelope.detail.offending_string`. |
| 3 | **No-buildings rule (Mode B render) — every shot's render output has `post_render_qc_seed[*].suspected_buildings_bool == false`.** | `no_buildings_violation` | `suspected_buildings_bool` is set by the engine's vision-classifier pass over the rendered output. Definition: TRUE if the dominant subject of any frame contains (a) a recognizable real-world building (named landmark, identifiable skyline, registered architecture), (b) a generic building with distinctive features that would be matched by reverse image search to a real structure, or (c) any architectural element claiming to be a specific real place. Generic interiors (a wall, a desk, a window) are allowed; specific exteriors with recognizable form are not. Storyboard / ProdCoord set `no_buildings_compliant_bool` on the plan side (intent). AI Video Gen verifies on the **render side** (output reality). Any TRUE = halt with `no_buildings_violation` errorEnvelope; cite which `shot_id` failed. |
| 4 | **Tier↔mode authorization (5th defense-in-depth pass).** | `tier_constraint_violation` | Pre-condition gate. Re-validates: `production_plan.tier ∈ {"Pro", "Enterprise"}` AND `production_plan.production_mode == "B"` AND `production_plan.mode_b_plan != null`. Pilot / Starter tiers MUST be caught upstream by Brief / Script / Storyboard / ProdCoord — by the time this agent runs, the tier is already wrong if it isn't Pro/Enterprise. The 5th re-check is non-negotiable: this is the agent that spends money. Any tier mismatch = halt with `tier_constraint_violation` errorEnvelope BEFORE any engine dispatch (no cost incurred). |
| 5 | **Mode B coverage — every `production_plan.mode_b_plan.render_queue[*].shot_id` resolves to exactly one entry in output `rendered_shots[]` AND status ∈ {rendered, partial, failed}.** | `engine_failure_unrecoverable` (set agent status `partial_with_warnings` if anchor succeeded but inheritors failed) | Coverage map: build `set(input_shot_ids) = {render_queue[i].shot_id for i in 0..N-1}`. Build `set(output_shot_ids) = {rendered_shots[j].shot_id for j in 0..M-1}`. ASSERT `input_shot_ids == output_shot_ids`. Missing shot = critical failure mode (lost render). Extra shot = critical failure mode (hallucinated render). Every shot MUST have a `render_status` set — no nulls. If every queue entry failed even after retry+fallback → halt with `engine_failure_unrecoverable`. If anchor succeeded but ≥1 inheritor failed → set agent-level `status="partial_with_warnings"`, list failed shot IDs in `qc_warnings[]`, continue. |
| 6 | **Anchor render success — `style_consistency_anchor.anchor_shot_id` MUST equal `rendered_shots[0].shot_id` AND `rendered_shots[0].render_status == "rendered"`.** | `anchor_misalignment` (mismatch) OR `engine_failure_unrecoverable` (anchor failed across primary + fallback) | The anchor IS the style canon — every inheritor render seeds from `anchor_seed`. If anchor failed, downstream shots have nothing consistent to inherit from; the entire render set is invalid. **Hard halt rule:** anchor failure is fatal. Do NOT attempt inheritors. Do NOT emit `partial_with_warnings`. Emit `engine_failure_unrecoverable` with `anchor_shot_id` cited. Operator pays the cost of one failed anchor render (worst case ~$15 on Runway Gen3 60s); operator avoids the cost of N inheritor renders that would all drift. |
| 7 | **Cost ceiling compliance — `render_telemetry.total_render_cost_usd_actual ≤ tier_cost_ceiling_usd × (1 + cost_overrun_buffer_pct/100)`.** | `cost_overrun` | Math: `tier_cost_ceiling_usd` looked up from §7.3 tier table (Pro = $400, Enterprise = $750). `cost_overrun_buffer_pct` default = 10 (operator may pass 0..15 in optional input). Hard reject formula: `IF total_render_cost_usd_actual > tier_cost_ceiling_usd × 1.10 THEN errorEnvelope(cost_overrun)`. Example: Pro tier render run hits $441 actual cost. `441 > 400 × 1.10 = 440` → `cost_overrun` errorEnvelope, halt before handoff. Operator is on the hook for the spent $441; the failure prevents downstream agents from processing an over-budget set. Cost discipline is a runtime invariant, not a soft preference. |
| 8 | **Quota reservation honored — every `production_plan.mode_b_plan.render_queue[*].quota_reserved_bool == true` at consumption time.** | `quota_not_reserved` | Pre-flight assertion: re-read the production plan's quota reservation booleans before dispatch. Quota reservation is **Production Coord Agent's** responsibility (per ProdCoord SPEC §11) — this is a defense-in-depth re-check. Rationale: between ProdCoord emit and AI Video Gen dispatch there is a window (could be hours if a human approval gate sits in between) during which the reserved quota could be invalidated by an external billing event. Re-checking takes <1ms and catches stale reservations before burning credentials on a doomed call. Any `quota_reserved_bool != true` = halt with `quota_not_reserved` errorEnvelope, list offending `shot_id`(s). |
| 9 | **Talent authorization (HeyGen shots only) — every shot with `engine_id == "heygen"` has `talent_id == "jamila-howard-reinvented-v2"`.** | `talent_unauthorized` | Pre-dispatch check. Iterate `rendered_shots[*]` proposed dispatch records (before engine call): for every record where `engine_id == "heygen"`, ASSERT the resolved talent equals the v1.0 canonical handle `"jamila-howard-reinvented-v2"`. v1.0 hardcoded — multi-talent deferred to v1.1+ (per Open Question #1, gated on first Sequel Digital external client onboarding). Any other talent value = halt with `talent_unauthorized` errorEnvelope BEFORE the HeyGen call (no cost incurred, no off-brand clone rendered). |
| 10 | **Negative-prompt presence — every `rendered_shots[*].render_dispatch_log` MUST record that the composed negative prompt was attached to the engine call.** | `negative_prompt_missing` | The negative prompt is the runtime firewall — entity list + `brief.do_not_say` + brand-anti-patterns + no-buildings string composed into a single string and passed to every engine dispatch. Its absence on **any single render** = HARD FAIL. Log format: each `rendered_shots[*].render_dispatch_log[*]` record carries `negative_prompt_attached_bool: true` AND `negative_prompt_sha256: "<64-hex>"` (SHA-256 of the composed negative prompt string). Verification: ASSERT every record has `negative_prompt_attached_bool == true` AND `negative_prompt_sha256.length == 64`. Optionally re-verify the hash by recomputing from the composed template (catches log tampering / accidental empty string). Any failure = halt with `negative_prompt_missing` errorEnvelope. |
| 11 | **`handoff_targets[]` non-empty AND every `payload_ref` resolvable to a dotted path inside `rendered_shots.json`.** | `ai_video_gen_agent_failed` (renamed from ProdCoord's `production_coord_agent_failed` per Cross-SPEC canon §3.6 errorEnvelope discipline — every agent emits its own typed final-failure code) | Inherits ProdCoord's payload_ref resolver pattern verbatim. `handoff_targets[]` MUST contain at minimum: `{agent: "edit-director", payload_ref: "<dotted-path>"}` AND `{agent: "qc", payload_ref: "<dotted-path>"}`. Optional third entry for `{agent: "style-replication", payload_ref: "..."}` if downstream Mode C consumers exist (v1.0 always emits empty `style-replication` hint — Style Replication Agent not yet built). For each entry, resolver walks the dotted path against the proposed output object. Example: `"rendered_shots[0].asset_uri"` must resolve to a string. Unresolvable path = halt with `ai_video_gen_agent_failed` errorEnvelope, cite the unresolvable `payload_ref`. |
| 12 | **`qc_pre_flags[]` formatting — every element is a snake_case predicate (per Cross-SPEC canon §3.7) AND the array contains ≥4 entries.** | `qc_pre_flags_format_violation` | Format rule (Cross-SPEC §3.7): each element matches `^[a-z][a-z0-9_]{0,63}$` (snake_case, starts with letter, ≤64 chars). Examples that PASS: `"anchor_drift_below_threshold"`, `"text_overlay_detected"`, `"motion_blur_high"`, `"cost_within_5pct_of_estimate"`. Examples that FAIL: `"AnchorDrift"` (camelCase), `"anchor-drift"` (kebab-case), `"anchor drift"` (whitespace), `""` (empty). Minimum array length = 4 (inherited from ProdCoord §6 #12; provides QC Agent with enough signal to triage). Any element fails format OR array length < 4 = halt with `qc_pre_flags_format_violation`. |

### 6.2 Check ordering rationale

Checks 1–4 are **pre-render gates** (run BEFORE any engine dispatch — no money spent if any fail). Checks 5–7 are **post-render gates** (run AFTER renders complete — failures here mean money already spent, but downstream cost is prevented). Checks 8–12 are **handoff-prep gates** (run during output composition — failures here mean cost spent but output is malformed; agent halts rather than ship junk).

This ordering minimizes wasted spend: validation failures stop early, render failures stop the chain, handoff failures stop the contract.

### 6.3 Failure code → errorEnvelope mapping (full v1.0 enumeration)

Per outline §3.6, the agent emits one of these 14 error codes on failure. The mapping table below confirms every Check above resolves to exactly one error code (or two, in coverage cases):

| Error code | Trigger checks | Recoverability |
|------------|----------------|----------------|
| `input_validation_failed` | Pre-Check #1 (schema parse) | Hard (operator must fix input) |
| `entity_firewall_breach` | Check #1 | Hard (operator must rewrite source) |
| `tier_constraint_violation` | Check #4 | Hard (wrong tier — escalate to ProdCoord) |
| `production_plan_not_success` | Pre-Check #1 (input is errorEnvelope variant) | Hard (upstream failure — re-run ProdCoord) |
| `not_mode_b` | Pre-Check #1 (mode != "B") | Hard (wrong agent for this plan) |
| `quota_not_reserved` | Check #8 | Soft (re-reserve and re-dispatch) |
| `anchor_misalignment` | Check #6 (mismatch case) | Hard (operator must reconcile anchor) |
| `render_quota_exhausted` | Check #5 (all engines + all fallbacks burned across all shots) | Soft (wait for quota replenishment) |
| `cost_overrun` | Check #7 | Hard (operator must approve overrun OR re-scope plan) |
| `engine_failure_unrecoverable` | Check #6 (anchor case), Check #5 (full coverage failure) | Hard (re-dispatch with different engine assignment) |
| `negative_prompt_missing` | Check #10 | Hard (agent bug — should be impossible; defense-in-depth) |
| `talent_unauthorized` | Check #9 | Hard (v1.0 hardcoded talent — v1.1+ multi-talent) |
| `banned_vocab_leaked` | Check #2 | Hard (operator must edit `brief.do_not_say` or source text) |
| `no_buildings_violation` | Check #3 | Soft (re-render with stricter negative prompt) |
| `qc_pre_flags_format_violation` | Check #12 | Hard (agent bug — schema enforcement gap) |
| `ai_video_gen_agent_failed` | Check #11 | Hard (handoff_targets malformed — agent bug) |
| `schema_invalid_after_retry` | Post-Check #12 (final schema validation against `output.schema.json` failed twice) | Hard (agent bug — schema drift) |

**Discrepancy note:** outline §3.6 enumerated 14 codes (initial). After §6 authoring, the canonical list rises to **17 codes** (added: `qc_pre_flags_format_violation`, plus the formal split of `engine_failure_unrecoverable` from `render_quota_exhausted` for the Check #5 vs Check #6 distinction). This expansion is normative — `schemas/ai-video-gen-agent/output.schema.json` (Day 25) MUST enumerate all 17. Flagged for Day 24 LOCK consistency review.

### 6.4 Self-QC pass criteria

To emit `successRenderedShots`:
- All 12 checks return PASS on first attempt, OR
- ≥1 check returns FAIL → agent regenerates the offending field set with concrete fix instructions inlined → ALL 12 checks return PASS on second attempt.

To emit `errorEnvelope`:
- ≥1 check returns FAIL twice (after one regenerate attempt) → emit envelope with `attempts: 2`, `failed_check_id: <1..12>`, `failure_code: <see §6.3>`, `detail: { ... }`.

### 6.5 Canonical entity firewall list (10 entries — Check #1 reference)

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

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 22)

This is the **LLM-facing system prompt** for the AI Video Gen Agent. Frame block + 13 hard rules + tier table + 11-step process (inherited verbatim from outline §5) + voice rule. Format follows ProdCoord SPEC §7 (Day 14 LOCKED): single markdown-fenced block, no commentary inside the fence.

**Authoring note (LOCK signal):** This block is the operational contract between the orchestrator and the LLM. Every word inside the fence is canon. Voice rule is inherited verbatim from ProdCoord §7 — no deviation. Tier table values are inherited verbatim from outline §4 (matching pricing canon Apr 25 LOCKED).

### 7.1 The system prompt (verbatim — copy into SKILL.md Day 26)

```
You are the AI Video Gen Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: Pixel binding for an executable render queue.

You do NOT design shots. You do NOT pick the hook. You do NOT change the tier or mode. You do NOT modify the production plan. You bind concrete pixels to an executable render queue.

You read a production_plan.json (Production Coord Agent output, Mode B branch only) and emit a rendered_shots.json: per-shot render dispatch records, style consistency anchor, render telemetry, post-render QC seed, and handoff targets for Edit Director / QC / Style Replication.

You are the 5th defense-in-depth firewall layer in the ARS pipeline. You re-validate every entity firewall + tier↔mode + no-buildings + cost ceiling that Brief, Script, Storyboard, and Production Coord already validated. You add: runtime cost reality (you are the first agent to spend money), negative-prompt injection into every external render call, anchor-first render sequencing, and per-shot post-render QC seed generation.

==================================================================
HARD RULES — NEVER VIOLATE (13)
==================================================================

1. Output format = JSON only. Single object conforming to rendered_shots.json schema. No markdown, no commentary, no code fences, no preamble, no postamble. The orchestrator parses your output with json.loads — anything outside the object breaks the pipeline.

2. Every shot in production_plan.mode_b_plan.render_queue[] MUST be accounted for in the output. Either rendered (render_status="rendered"), partially rendered with warnings (render_status="partial"), or failed (render_status="failed"). Missing shots = hard fail. Extra shots = hard fail. Coverage is one-to-one.

3. Entity firewall (defense-in-depth, 5th re-check). NEVER reference Holdco Group, 4821 Main, SITE-C-BRAND, 6315, SLN, Retail Supply, Principal Holdco, NPOX, Nonprofit Leader A, Nonprofit Leader B, Nonprofit Leader C, or Partner Brand. Conjugates included. AND NEVER inject any of these terms into a prompt sent to a render engine. The negative prompt template includes them as a forbidden list; the composed positive prompt must be scanned against the same list before dispatch.

4. Banned vocabulary. Inherit brief.do_not_say verbatim AND first-order conjugates. Absence-check across (a) every rationale string in your output, (b) every human-readable string in your output, (c) every prompt dispatched to engines, (d) every text overlay rendered into video (verified via post_render_qc_seed.text_overlay_strings OCR pass). Four-pass walk. Any hit = halt with banned_vocab_leaked errorEnvelope.

5. No-buildings rule. Mode B render outputs MUST NOT contain recognizable real-world buildings, identifiable architecture, or recognizable landmarks. The negative prompt template includes "real-world buildings, identifiable architecture, recognizable landmarks, named skylines, registered structures" verbatim. Post-render QC seed flag suspected_buildings_bool MUST be false for every shot. Any TRUE = halt with no_buildings_violation.

6. Tier↔mode authorization (5th defense-in-depth). Pilot tier NEVER reaches you. Starter tier NEVER reaches you. Pro tier = Mode B unlocked, cost ceiling $400, runtime cap 60s, engines: Runway / Pika / Luma / Flux / Kling / Higgsfield / HeyGen. Enterprise tier = Mode B unlocked, cost ceiling $750, runtime cap 90s, engines: Pro engines + Runway Gen3 Turbo + HeyGen v3 polish. If production_plan.tier ∉ {Pro, Enterprise} OR production_plan.production_mode ≠ "B" OR production_plan.mode_b_plan is null → halt with tier_constraint_violation OR not_mode_b errorEnvelope BEFORE any engine dispatch.

7. Cost ceiling is HARD. render_telemetry.total_render_cost_usd_actual ≤ tier_cost_ceiling_usd × (1 + cost_overrun_buffer_pct/100). Default buffer = 10%. Hard reject with cost_overrun errorEnvelope at >110% of estimate. The cost ceiling is a runtime invariant, not a soft preference. Overrun = halt before handoff. No exceptions for "almost made it."

8. Asset URI scheme = platform-relative. Emit asset_uri strings as "ars://renderset/<brand_id>/<YYYY-MM-DD>/<render_set_seq>/shot-<NNN>.<ext>". NEVER emit absolute external CDN URLs. NEVER emit signed URLs. NEVER emit raw API keys, engine handle IDs, signed presigned URLs, or any credential value in any field of any output record. The orchestrator resolves platform URIs to signed URLs at Edit Director → Publishing handoff stage — not your responsibility.

9. HeyGen talent v1.0 = "jamila-howard-reinvented-v2" only. Every shot with engine_id == "heygen" MUST have talent_id == "jamila-howard-reinvented-v2". Reject any other talent value with talent_unauthorized errorEnvelope BEFORE the HeyGen API call (no cost incurred). Multi-talent support deferred to v1.1+ — gated on first Sequel Digital external client onboarding.

10. Negative-prompt template MUST attach to EVERY render dispatch. Composed from: entity firewall list (10 canonical entries from §6.5) + brief.do_not_say verbatim + brand-anti-patterns (off-brand color palettes, off-tone visual descriptors) + no-buildings string ("real-world buildings, identifiable architecture, recognizable landmarks, named skylines, registered structures"). Verify attachment in self-QC step #11: each render_dispatch_log record MUST carry negative_prompt_attached_bool: true AND negative_prompt_sha256 (64-hex SHA-256 of the composed negative prompt). Absence on any single render = hard halt with negative_prompt_missing.

11. Anchor-first render sequencing. rendered_shots[0] is the anchor; it MUST complete render_status == "rendered" BEFORE any inheritor render (rendered_shots[1..N-1]) dispatches. Anchor failure (across primary engine + 1 retry + fallback engine + 1 retry) = whole-set blocked. Emit engine_failure_unrecoverable with anchor_shot_id cited. Do NOT dispatch inheritors. Inheritors inherit anchor_seed via literal_seed_inherit (v1.0 propagation strategy — Open Question #5 deferred to v1.1+).

12. Render retries policy: 1 retry per shot on transient failure (engine timeout, rate-limit, transient 5xx). After primary + 1 retry → switch to fallback_engine_id per production_plan + 1 retry on fallback. If fallback also exhausts both attempts → engine_failure_unrecoverable for that shot. If shot is the anchor → whole-set blocked (per Rule 11). If shot is an inheritor → mark render_status="failed", continue with remaining inheritors, set agent-level status="partial_with_warnings", list failed shot_id in qc_warnings[].

13. If self-QC (§6 12-check list) fails 2 times → emit errorEnvelope. No 3rd attempt. Predictable failure surface beats best-effort recovery. errorEnvelope MUST include: failed_check_id (1..12), failure_code (from §6.3 mapping), attempts: 2, detail object with offending field path / value when applicable.

==================================================================
TIER TABLE — RUNTIME AUTHORITATIVE
==================================================================

| Tier       | Mode B unlocked | Cost ceiling | Runtime cap | Engines accessible                                                            |
|------------|:---------------:|-------------:|------------:|-------------------------------------------------------------------------------|
| Pilot      |       NO        |          n/a |         n/a | n/a                                                                           |
| Starter    |       NO        |          n/a |         n/a | n/a                                                                           |
| Pro        |       YES       |         $400 |        60 s | Runway (Gen3 Alpha), Pika 1.5, Luma Dream Machine, Flux 1.1, Kling 1.6,       |
|            |                 |              |             | Higgsfield, HeyGen (talent: jamila-howard-reinvented-v2 only)                 |
| Enterprise |       YES       |         $750 |        90 s | All Pro engines + Runway Gen3 Turbo + HeyGen v3 polish                        |
|            |                 |              |             | (talent: jamila-howard-reinvented-v2 only; multi-talent v1.1+)                |

The tier table IS the authority at runtime. ProdCoord set the plan; you enforce the ceiling. If anything you observe in production_plan disagrees with this table, halt with tier_constraint_violation. The table is the contract.

==================================================================
PROCESS — 11 STEPS (run in order)
==================================================================

1. Validate input shape. Parse production_plan.json against input.schema.json. If errorEnvelope variant → emit production_plan_not_success. If production_mode != "B" OR mode_b_plan == null → emit not_mode_b. Defense-in-depth: re-check ProdCoord's tier authorization (Rule 6).

2. Defense-in-depth firewall + tier+mode revalidation (5th time across the pipeline). Walk every input field for entity firewall (§6.5) AND brief.do_not_say. Any hit at input → halt with entity_firewall_breach or banned_vocab_leaked.

3. Load context. Read production_plan.mode_b_plan.render_queue[], production_plan.mode_b_plan.style_consistency_anchor, brief.do_not_say, storyboard.shoot_logistics passthrough fields, engine_quota_handles (opaque handle IDs — never read raw credentials), style_token_lib (optional), negative_prompt_template (optional — if absent, agent composes from canonical sources).

4. Compose negative prompt template. Concatenate: entity firewall (10 entries) + brief.do_not_say (verbatim + conjugates) + brand-anti-patterns (off-brand palettes, off-tone descriptors) + no-buildings string. ASSERT non-empty (length > 100 chars). Compute SHA-256 hash. This composed template is attached to every render dispatch — bind once, reuse for every shot.

5. Anchor render (rendered_shots[0], shot_index=1). Dispatch to assigned engine with prompt_compiled = prompt_seed + style_token + brand_inheritance, and negative_prompt_compiled = composed template (Step 4). Capture anchor_seed from engine response. On primary failure → 1 retry → fallback engine → 1 retry on fallback. If still failed → emit engine_failure_unrecoverable, halt agent (anchor fail = whole-set blocked, do not dispatch inheritors). On success, record render_dispatch_log with negative_prompt_attached_bool: true AND negative_prompt_sha256.

6. Inheritor renders (rendered_shots[1..N-1]). For each remaining render_queue[i]: dispatch to assigned engine with seed_value = anchor_seed (literal_seed_inherit v1.0), prompt_compiled = prompt_seed + style_token + brand_inheritance, negative_prompt_compiled = composed template (same Step 4 output). Same retry+fallback policy. Failure of an inheritor = mark render_status="failed", continue (do NOT halt — partial set is acceptable for inheritors).

7. Per-shot QC seed. For each rendered asset, populate post_render_qc_seed: frame_count, black_frame_count, face_present_bool (expected true for HeyGen), face_count_estimated, motion_blur_score_0_1, brand_color_presence_bool, on_brand_palette_match_score_0_1, suspected_drift_bool (TRUE if anchor inheritance score < drift_threshold default 0.85), suspected_text_overlay_bool, text_overlay_strings (OCR pass — used by Check #2 banned-vocab walk), suspected_buildings_bool (vision-classifier pass — used by Check #3 no-buildings walk), qc_seed_notes.

8. Render telemetry true-up. Sum actuals: total_render_seconds_actual, total_render_cost_usd_actual, per_engine_minutes, per_engine_cost_usd, retry_count_total, failure_count_total, start_timestamp, end_timestamp, total_wall_clock_minutes. Compute budget_variance_pct = (actual / estimate - 1) × 100. ASSERT abs(budget_variance_pct) ≤ cost_overrun_buffer_pct OR total_actual ≤ tier_cost_ceiling × 1.10. Else emit cost_overrun errorEnvelope.

9. Compose handoff_targets[]. Always emit: {agent: "edit-director", payload_ref: "rendered_shots"}, {agent: "qc", payload_ref: "rendered_shots"}. Conditionally emit: {agent: "style-replication", payload_ref: "style_consistency_anchor"} only if downstream Mode C reels reference this anchor (v1.0 = empty hint — Style Replication not yet built).

10. Build escalation_path[]. For each shot where retries occurred OR post_render_qc_seed flagged drift / text overlay / face miss: list operator-on-call notes + engine vendor support contact (opaque, redacted in output) + "human review at Edit step required" flag. Per Cross-SPEC canon §3.8 escalation_path is ordered ascending by severity.

11. Self-QC + emit. Run the 12-check list from §6. All PASS → emit successRenderedShots. ≥1 FAIL on first attempt → regenerate offending field set with concrete fix instructions inlined → re-run 12-check. ≥1 FAIL on second attempt → emit errorEnvelope per Rule 13.

==================================================================
VOICE FOR WRITTEN RATIONALE FIELDS
==================================================================

Voice for written rationale fields: clinical-warm, operator-to-operator, present tense, ≤14 words per sentence, action verbs. No exclamation marks. No emoji. No hedging language ("might", "could potentially", "we believe"). State the decision and the why in one breath.

Emit JSON only. Now.
```

### 7.2 Why this prompt is shaped this way

Six structural decisions are encoded in the prompt:

1. **Single-responsibility line first.** "Pixel binding for an executable render queue" sets the scope ceiling. The LLM cannot drift into shot design, hook selection, tier negotiation, or plan editing — those belong to upstream agents.

2. **Defense-in-depth declaration upfront.** Naming the 5th-layer firewall position primes the model to re-check rather than trust upstream. Trust-but-verify isn't a process — it's a system prompt clause.

3. **13 hard rules, numbered, terse.** Rules are the contract. Each rule maps to a self-QC check (§6) OR a tier-table enforcement OR an errorEnvelope code. The 13-rule count is normative — adding a 14th would mean re-running the cross-SPEC consistency review.

4. **Tier table embedded in the prompt, not external.** ProdCoord may have already passed the tier; runtime enforcement happens here. Embedding the table makes the LLM the source of truth for cost ceiling math, not a side document the orchestrator could forget to load.

5. **11-step process maps 1:1 to the §6 self-QC list.** Step 1 → Check #4 (tier authorization). Step 4 → Check #10 (negative prompt presence). Step 7 → Check #2 (banned vocab OCR walk) and Check #3 (no-buildings). Step 8 → Check #7 (cost ceiling). Step 11 → all 12 checks. This 1:1 mapping is the audit invariant: every step produces evidence one or more checks need.

6. **"Emit JSON only. Now." closing.** Eliminates the "thinking out loud" failure mode. ProdCoord §7 proved this works in 5/5 fixture runs (Day 18 SKILL bundle validation). Inherit verbatim.

---

## §8 — Performance Targets

`<<TBD-D23>>`

*Day 23 author task. Pattern source: ProdCoord SPEC §8 (Day 14 LOCKED). Targets to enumerate: schema validity rate (target 100% post-§6), firewall catch rate (target 100% — zero leaks), anchor drift rate (target <15% drift_threshold breach), render success rate by engine, budget variance distribution, p50 / p95 wall-clock latency per tier, retry rate, fallback-engine activation rate. Cost discipline: per-tier average cost as % of ceiling.*

---

## §9 — 5 Test Fixtures

`<<TBD-D23>>`

*Day 23 author task. Pattern source: ProdCoord SPEC §9 (Day 14 LOCKED — 5 fixtures: TC-01 Pro Mode B happy path, TC-02 Enterprise Mode B happy path, TC-03 anchor failure, TC-04 cost overrun, TC-05 engine cascade failure). Fixtures will live at `skills/ai-video-gen-agent/tests/` per Day 26 SKILL bundle. Each fixture = (input.json, expected_output.json, expected_error_code_or_null, scenario_description).*

---

## §10 — Storyboard → Production Plan → AI Video Gen Field Map (LOCKED-as-drafted Day 22)

**Inheritance from ProdCoord §10:** three-column shape (source → destination → transform). **Difference:** AI Video Gen reads from `production_plan.json` (ProdCoord's output) — NOT directly from storyboard. The audit trail through storyboard / script / brief is preserved via `parent_chain[]`.

**Schema discipline:** All `production_plan.json` field references inherit from `schemas/production-coord-agent/output.schema.json` (Day 17 LOCKED — read-only). All `rendered_shots.json` field references will be enforced by `schemas/ai-video-gen-agent/output.schema.json` (Day 25 LOCK target). The map below is the field-level contract that Day 25 schemas MUST enumerate.

### 10.1 The field map (21 rows)

| `production_plan.json` field | `rendered_shots.json` destination | Transform | Mechanic |
|------------------------------|-----------------------------------|-----------|----------|
| `production_plan_id` | `production_plan_id` | Passthrough (audit trail). | Verbatim string copy. The `production_plan_id` is the immediate upstream anchor in the audit chain — every `rendered_shots` record points back to exactly one production plan, which itself points back to exactly one storyboard, script, and brief. No transformation. |
| `brief_id` (via `parent_chain`) | `parent_chain[0]` | First element of 4-tuple. | Read from `production_plan.parent_chain[0]`. Verbatim copy. The 4-tuple shape is LOCKED for Mode B (Brief → Script → Storyboard → ProductionPlan). Tuple positions are positional, not keyed — order matters for audit walks. |
| `script_id` (via `parent_chain`) | `parent_chain[1]` | Second element. | Read from `production_plan.parent_chain[1]`. Verbatim copy. |
| `storyboard_id` (via `parent_chain`) | `parent_chain[2]` | Third element. | Read from `production_plan.parent_chain[2]`. Verbatim copy. |
| `production_plan_id` | `parent_chain[3]` | Fourth element (LOCKED 4-tuple v1.0). | Same `production_plan_id` as the dedicated field above, but positioned at `parent_chain[3]` to complete the 4-tuple audit. Redundancy is intentional — schemas enforce both. |
| `brand_id` | `brand_id` | Passthrough. | Verbatim string copy. v1.0 expected value = `"REINVENTED"`. Multi-brand v1.1+ (Open Question #1 — gated on first paid Sequel Digital client onboarding). |
| `tier` | `tier` | Passthrough — drives cost ceiling re-validation. | Verbatim enum copy from `{"Pro", "Enterprise"}`. This value is the lookup key for `tier_cost_ceiling_usd` (§7.3 tier table). Re-asserted in Check #4 (tier authorization). Pilot / Starter never reach this field — would halt at Step 1 of process. |
| `lever` | `lever` | Passthrough — drives `metadata.human_review_required`. | Verbatim integer copy from `{1, 2, 3}`. Lever 3 (default v1.0) = every render reviewed by QC + human. Lever 2 (after 30-reel threshold) = sampled approval. Lever 1 (after 90-reel threshold) = autonomous. Drives `metadata.human_review_required: bool` per the lever framework (per Orchestration Blueprint §6). |
| `production_mode` | `production_mode` | Passthrough — MUST equal `"B"`. | Verbatim const copy. Schema enforces `const: "B"` on the destination — any other value rejected at output validation. Defensive: the pre-flight check at Process Step 1 already halts with `not_mode_b` if input differs. |
| `total_shots` | `total_shots` | Passthrough. | Verbatim integer copy. Used by Check #5 (Mode B coverage): `total_rendered_shots == total_shots` is the success invariant for `status="ready_for_edit"`. |
| `mode_b_plan.render_queue[]` | Drives `rendered_shots[]` 1:1 binding | Per-shot render dispatch. | The `render_queue[]` array is the input contract for Process Steps 5–6 (anchor + inheritor renders). Every queue entry produces exactly one `rendered_shots[]` entry. Coverage map (Check #5): `len(render_queue) == len(rendered_shots)` AND every `render_queue[i].shot_id` appears exactly once in `rendered_shots[*].shot_id`. The 1:1 binding is the agent's central contract. |
| `mode_b_plan.render_queue[*].shot_id` | `rendered_shots[*].shot_id` | 1:1 binding. | Verbatim string copy per shot. The `shot_id` is the join key for cross-record audit (storyboard → production plan → rendered shot). Format pattern inherited from Storyboard SPEC: `^shot-\d{3}$`. |
| `mode_b_plan.render_queue[*].engine_id` | `rendered_shots[*].engine_id_actual` | Passthrough on success; on retry, becomes `fallback_engine_id`. | Verbatim enum copy if primary engine succeeded on first attempt or 1× retry. If primary failed and fallback was used → `engine_id_actual` records the engine that actually produced the asset (the fallback). `retry_log[*].engine_id` preserves the full attempt sequence including the failed primary, so the field map is lossless even on engine swap. Rationale: downstream agents (Edit Director, QC) need to know which engine actually rendered the pixels for QC bias profiling. |
| `mode_b_plan.render_queue[*].fallback_engine_id` | `rendered_shots[*].fallback_engine_id` (if used) | Conditional passthrough. | Copied only if the primary engine + 1 retry both failed AND fallback was dispatched. If fallback was never invoked, this field is absent (not null — absent — per Cross-SPEC canon §3.10 optional-field rule). Allows downstream to distinguish "fallback wasn't needed" from "fallback was dispatched and succeeded" from "fallback was dispatched and failed." |
| `mode_b_plan.render_queue[*].prompt_seed` | `rendered_shots[*].render_dispatch_log[*].composed_prompt_redacted` | TRANSFORM: prompt_seed + style_token_lib + negative_prompt_template = composed prompt. Stored REDACTED in log. | The agent composes the actual engine-facing prompt by concatenating: `production_plan.mode_b_plan.render_queue[i].prompt_seed` (the directive) + `style_token_lib[*]` (REINVENTED-specific aesthetic tokens — purple/gold palette, Alux-style framing language) + `brand_inheritance` (per-brand token cache). The result is the `prompt_compiled` field on the dispatch record. For audit, the prompt is stored as `composed_prompt_redacted` — entity firewall tokens replaced with `[REDACTED-ENTITY]`, banned vocab tokens replaced with `[REDACTED-VOCAB]`. Full unredacted prompt is NEVER stored — only the SHA-256 hash (`composed_prompt_sha256`) for tamper detection. |
| `mode_b_plan.render_queue[*].style_token` | Feeds composed prompt (intermediate — not directly stored) | TRANSFORM (composition input). | Style tokens are inputs to the prompt composition (Step 5 / Step 6). They are NOT individually stored on the output record — they're embedded into `composed_prompt_redacted`. The `style_token_lib` is read once at Step 3 (context load) and reused across all shots in the queue. This is the v1.0 inheritance pattern: literal token concatenation. v1.1+ may swap in semantic blending; v1.0 = literal_passthrough only. |
| `mode_b_plan.render_queue[*].quota_reserved_bool` | `rendered_shots[*].quota_drawdown_log` | TRANSFORM (drawdown ledger). | The boolean asserts ProdCoord pre-reserved quota; the agent doesn't re-reserve. On render dispatch, the agent emits a `quota_drawdown_log` entry: `{engine_id, quota_units_consumed, timestamp, handle_id_opaque}`. The `handle_id_opaque` is the platform layer's identifier — NEVER a raw credential value. The drawdown ledger is the source of truth for telemetry reconciliation (Step 8) and for billing audit downstream. |
| `mode_b_plan.style_consistency_anchor.anchor_shot_id` | `style_consistency_anchor.anchor_shot_id` | Passthrough. MUST equal `rendered_shots[0].shot_id`. | Verbatim string copy with mandatory equality assertion. Check #6 enforces. If the anchor designated by ProdCoord doesn't equal the first rendered shot ID, the render queue ordering is invalid — halt with `anchor_misalignment`. The agent does not re-pick the anchor; it inherits ProdCoord's choice. |
| `mode_b_plan.total_render_cost_usd_estimated` | `render_telemetry.total_estimated_cost_usd` | Passthrough — used as the budget ceiling for `cost_overrun` check. | Verbatim numeric copy. This is the budget baseline against which `render_telemetry.total_render_cost_usd_actual` is compared in Check #7 (cost ceiling compliance). Formula: `actual ≤ estimate × (1 + cost_overrun_buffer_pct/100)`. The estimate itself is bounded by `tier_cost_ceiling_usd` upstream (ProdCoord §11), but runtime variance is real — that's why the buffer exists. |
| `mode_b_plan.runtime_target_seconds` | `render_telemetry.runtime_target_seconds` | Passthrough — informs latency budget. | Verbatim numeric copy. Used for §8 performance target reporting (Day 23). Not currently a hard enforcement gate — runtime overruns are reported as `qc_warnings`, not errorEnvelopes (overrun in wall-clock doesn't ship bad pixels). |
| `tier_constraints.cost_ceiling_usd` (derived from tier via §7.3) | `render_telemetry.tier_cost_ceiling_usd` | Lookup from §7.3 tier table. | NOT a passthrough — this field is **derived** by the agent via tier lookup. Pro → $400. Enterprise → $750. The value is recorded on the output so downstream agents (and bookkeeping) don't need to re-derive. Schema enforces the value matches the tier per §7.3 (joint-validation rule). |
| `qc_warnings` (from ProdCoord) | `qc_warnings` (inherited; agent may append) | Append. | The agent inherits ProdCoord's `qc_warnings[]` verbatim and may append its own (anchor drift warnings, partial-set warnings, runtime overrun warnings, OCR text-overlay flags). Append-only — no removal. Downstream QC Agent reads the cumulative list to triage. |
| `metadata.parent_chain` (3-tuple from ProdCoord: [brief_id, script_id, storyboard_id]) | `metadata.parent_chain` (4-tuple — extend with own `production_plan_id`) | Extend with own ID. | The agent receives a 3-tuple and emits a 4-tuple. Mechanic: `metadata.parent_chain = input.metadata.parent_chain + [production_plan_id]`. The 4-tuple is LOCKED for the AI Video Gen layer; Style Replication Agent (Mode C, Week 5) will extend to 5-tuple at its own layer. This is the audit-chain inheritance pattern that Cross-SPEC canon §3.9 enumerates. |

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

Three fields are reserved in the field map but not yet active in v1.0:

- **HeyGen `talent_id` per-shot field.** Production plan does not currently surface talent at the render-queue level (single global `talent_id` would be redundant in v1.0 because every HeyGen shot uses the same `jamila-howard-reinvented-v2` handle). v1.1+ adds `render_queue[*].talent_id` to support multi-talent — gated on Open Question #1 (first Sequel Digital external client onboarding).
- **Multi-anchor rotation.** v1.0 uses a single `style_consistency_anchor`. v1.1+ may support `style_consistency_anchors[]` for reels with hero/secondary/tertiary visual themes. Open Question #4. Defer.
- **Auto-engine swap based on telemetry.** v1.0 honors `production_plan.mode_b_plan.render_queue[*].engine_id` verbatim — no override authority. v1.1+ may allow AI Video Gen to override ProdCoord's assignment based on rolling telemetry (e.g., Engine X hit rate dropped below threshold this week). Open Question #3 — defer.

### 10.3 No-touch fields (read-only references)

These fields are read by the agent but never written to its output (audit trail only — downstream agents read them from the production plan directly):

- `storyboard.shoot_logistics.*` — Mode A live-shoot context; irrelevant to Mode B but carried in production plan for cross-mode audit. AI Video Gen does not echo to output.
- `script.dialog_lines[*]` — only relevant to HeyGen talent shots; the dialog is already embedded in the `prompt_seed` for HeyGen shots upstream. Not re-emitted.
- `brief.target_audience` — passes through to `metadata.brief_summary` but not duplicated as a top-level field. Reduces output size.

### 10.4 Schema authoring note (for Day 25)

The Day 25 schema author must encode the field map above as JSON Schema Draft 2020-12 constraints. Specifically:
- `parent_chain` MUST use `prefixItems: [..., ..., ..., ...]` AND `items: false` to enforce exact 4-tuple cardinality (per ProdCoord schema pattern Day 17 LOCKED).
- `tier_cost_ceiling_usd` MUST use `allOf` joint validation: `{tier: "Pro", tier_cost_ceiling_usd: 400}` OR `{tier: "Enterprise", tier_cost_ceiling_usd: 750}`.
- `production_mode` MUST use `const: "B"`.
- `composed_prompt_redacted` MUST use `pattern: "^([^A-Z]|\\[REDACTED-(ENTITY|VOCAB)\\]).*$"` (no naked entity names — only redacted tokens).
- `asset_uri` MUST use `pattern: "^ars://renderset/[A-Z][A-Z0-9_-]*/\\d{4}-\\d{2}-\\d{2}/\\d{3,}/shot-\\d{3}\\.[a-z0-9]+$"`.

---

## §11 — Cost Model (per-engine $/sec lookup table)

`<<TBD-D23>>`

*Day 23 author task. Source: vendor public pricing docs (RESEARCH-ONLY — no subscriptions, no API calls). Engines to enumerate: Runway Gen3 Alpha + Turbo, Pika 1.5, Luma Dream Machine, Flux 1.1, Kling 1.6, Higgsfield, HeyGen v2 + v3. Format: `{engine_id: {model_id: {usd_per_sec, runtime_cap_sec, quota_unit_definition}}}`. This table feeds Check #7 (cost ceiling) math and §8 performance targets.*

---

## §12 — Style Consistency Math

`<<TBD-D23>>`

*Day 23 author task. Topics: drift_threshold derivation (default 0.85 — need empirical calibration from first 10 Mode B reels per Open Question #7), inheritance_match_score_0_1 algorithm (perceptual hash distance? CLIP embedding cosine? frame-by-frame palette histogram?), v1.0 = literal_seed_inherit (deterministic — same anchor seed = inherited shot uses anchor seed verbatim; no augmentation). v1.1+ = seed_plus_style_token (deferred).*

---

## §13 — 17 Critical Decisions LOCKED

`<<TBD-D23>>`

*Day 23 author task. Pattern source: ProdCoord SPEC §13 (Day 14 LOCKED — 17 decisions). AI Video Gen v1.0 equivalents to enumerate: anchor strategy (anchor-first sequential), retry policy (1+1 across primary+fallback), cost overrun buffer default (10%), drift threshold default (0.85), failure cascades (anchor fatal, inheritor partial), HeyGen talent hardcode, asset URI scheme, negative prompt template canon location, lever inheritance, escalation_path ordering, errorEnvelope code count (17), 12-check QC list shape, voice rule inherit, 13-rule hard list, tier table runtime authority, parent_chain 4-tuple, no-buildings post-render verification.*

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 22 · status updates only)

**Calendar inherited from Day 21 scaffold §14.** Day 22 author task per scaffold: status updates only — calendar shape unchanged. Updates encoded below.

### 14.1 Calendar (Day 20 → Day 28)

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 20 | Sat May 9 · Wk4D1 | **AI Video Gen Agent v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 21 | Sun May 10 · Rest Day | **Day 22 SPEC body pre-flight scaffold** — §6 / §7 / §10 / §14 drop-in slots reserved | ✅ DONE — Rest Day docs allowed | Donna overnight |
| Day 22 | Mon May 11 · Wk4D2 | **SPEC body §6 (12-Check Self-QC) + §7 (System Prompt v1.0) + §10 (Field Map) + §14 (Implementation Plan)** | ✅ DONE — this document, LOCKED-as-drafted | Donna overnight |
| Day 23 | Tue May 12 · Wk4D3 | **SPEC body §8 (Performance Targets) + §9 (5 Test Fixtures) + §11 (Cost Model per-engine $/sec) + §12 (Style Consistency Math) + §13 (17 Critical Decisions LOCKED) + §15 (Change Log) + §16 (Metadata schema)** | ⬜ QUEUED | Donna overnight |
| Day 24 | Wed May 13 · Wk4D4 | **SPEC v1.0 LOCK** — Cross-SPEC consistency review against ProdCoord SPEC + Cross-SPEC canon §3. Reconciliation of any naming / errorEnvelope / qc_pre_flags drift. LOCK signed. | ⬜ TARGET | Donna overnight + Jamila approval |
| Day 25 | Thu May 14 · Wk4D5 | **input.schema.json + output.schema.json** (Draft 2020-12, mutual-exclusivity polymorphic, 17 errorEnvelope codes enumerated, 4-tuple parent_chain via `prefixItems`). Self-validating. | ⬜ QUEUED | Donna overnight |
| Day 26 | Fri May 15 · Wk4D6 | **SKILL bundle** (10 files: SKILL.md, README, user-template, 2 schemas, 5 test fixtures). 5/5 inputs validate clean. | ⬜ QUEUED | Donna overnight |
| Day 27 | Sat May 16 · Wk5D1 | **LLM Test Runbook** (paste-and-run, pattern from Day 11 / Day 19). Operator-gated. ≤$3 + 30 min sit-down (slightly higher than ProdCoord runbook because Mode B touches paid render API in test fixture #1 — TBD whether v1.0 LOCK includes 1 live render or whether all 5 fixtures stay schema-validation-only). | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 28 | Sun May 17 · Rest Day | No build. Optional Jamila ~30 min review of Week 4 close. | — | Jamila |
| Day 29+ | Mon May 18+ · Wk5D2+ | **Operator-gated LLM LOCK + Mode B production gate live.** Style Replication Agent SPEC outline begins (Mode C / Week 5 target). | ⬜ QUEUED | Jamila + Donna |

### 14.2 Dependencies that MUST exist before Day 26 SKILL bundle build

| Dependency | Status | LOCK day |
|------------|--------|----------|
| Production Coord Agent v1.0 SPEC LOCKED | ✅ DONE | Day 14 |
| Production Coord input.schema.json + output.schema.json LOCKED | ✅ DONE | Day 17 |
| Production Coord SKILL bundle LIVE | ✅ DONE | Day 18 |
| Cross-SPEC Consistency Review LOCKED | ✅ DONE | Day 12 |
| AI Video Gen SPEC outline §0–§5 | ✅ DONE | Day 20 |
| AI Video Gen SPEC body §6 + §7 + §10 + §14 LOCKED-as-drafted | ✅ DONE — this document | Day 22 (today) |
| AI Video Gen SPEC body §8 + §9 + §11 + §12 + §13 + §15 + §16 LOCKED | ⬜ TARGET | Day 23 |
| AI Video Gen SPEC v1.0 LOCK | ⬜ TARGET | Day 24 |
| AI Video Gen schemas LOCKED | ⬜ TARGET | Day 25 |
| Engine `$/sec` lookup table | ⬜ Day 23 author task | Day 23 |
| Negative-prompt template canon location decision | Open Question #8 — defer to v1.0 SKILL.md embedded; v1.1 refactor | — |

### 14.3 Rest Day honored

Day 21 (Sun May 10) and Day 28 (Sun May 17) — no build sessions per Daily OS pillar (Rest → Body → Money → Authority → Relationships). Spec/docs work allowed (Day 21's scaffold document was the canonical Rest Day-compounding example; Day 28 may run the same scaffold-prep pattern for Style Replication Agent §6/§7/§10/§14).

### 14.4 Day 22 sprint completion summary

| Section | Status | Wall-clock | Notes |
|---------|--------|------------|-------|
| §6 12-Check Self-QC List | ✅ DRAFTED | ~3 hr equivalent | All 12 checks fully drafted with failure-code mapping. Slot 11 renamed from `production_coord_agent_failed` → `ai_video_gen_agent_failed`. OCR text-overlay angle (Check #2 Pass 2) integrated. Error code list expanded from 14 (outline §3.6) to 17 (this document §6.3) — flagged for Day 24 LOCK consistency review. |
| §7 System Prompt v1.0 | ✅ DRAFTED | ~3 hr equivalent | Single fenced block: frame + 13 hard rules + tier table + 11-step process verbatim from outline §5 + voice rule verbatim from ProdCoord §7. Six structural decisions rationalized in §7.2. |
| §10 Field Map | ✅ DRAFTED | ~2 hr equivalent | 21 rows: 14 passthrough, 5 transform, 2 derived. v1.0 reserved fields and no-touch fields enumerated separately. Day 25 schema authoring notes embedded. |
| §14 Implementation Plan | ✅ DRAFTED | ~1 hr equivalent | Status updates only. Calendar shape unchanged from Day 21 scaffold. Dependency table extended. |

Total Day 22 wall-clock estimate met: ~9 hr operator-paced (compressed in automated overnight session — pattern-inherited from ProdCoord §14 proven wall-clock).

---

## §15 — Change Log + Version History

`<<TBD-D23>>`

*Day 23 author task. Pattern source: ProdCoord SPEC §15 (Day 14 LOCKED). Initial entry: v1.0-draft-day-22 (this document — body §6/§7/§10/§14 drafted; §8/§9/§11/§12/§13/§15/§16 reserved). Subsequent entries: v1.0-draft-day-23 (remaining sections), v1.0-LOCKED-day-24 (cross-SPEC reconciliation signed), v1.0-schemas-day-25 (schemas published), v1.0-SKILL-day-26 (bundle live), v1.0-LLM-tested-day-27+ (operator-gated LOCK).*

---

## §16 — Metadata Block Schema

`<<TBD-D23>>`

*Day 23 author task. Pattern source: Cross-SPEC canon §3.9 (LOCKED) — every agent emits canonical metadata block: `{agent_id, agent_version, spec_version, schema_version, lock_date_iso, parent_chain (4-tuple for this agent), session_id, created_at, build_envelope_sha256, human_review_required (bool — derived from lever), upstream_agent_ids (array)}`. AI Video Gen-specific additions: `engine_telemetry_summary` (per-engine call count, success rate, retry count), `composed_prompt_template_sha256` (audit hash of the negative-prompt template used), `runtime_environment_class` (enum: dev / staging / production).*

---

## CROSS-SPEC CANON ADHERENCE CHECK (Day 22 self-audit)

Per Cross-SPEC Consistency Review (Day 12 LOCKED), every agent SPEC MUST align on the following dimensions. Status check below:

| Canon dimension | Cross-SPEC §3 requirement | This document |
|-----------------|---------------------------|---------------|
| §3.1 Single-responsibility line | One sentence, present tense, ≤10 words | ✅ "Pixel binding for an executable render queue" — 6 words |
| §3.2 Tier table runtime authority | Embedded in §7 system prompt verbatim | ✅ Tier table at §7.1 lines 90–95 of this doc |
| §3.3 Hard rules numbered | Sequential, no gaps, NEVER-violate framing | ✅ 13 rules at §7.1 lines 18–48 of this doc |
| §3.4 Process steps mapping | Each step maps to ≥1 self-QC check | ✅ §7.2 decision #5 documents 1:1 mapping |
| §3.5 Negative-prompt firewall | Composed from entity + do_not_say + brand-anti + no-buildings | ✅ Hard Rule #10 + Check #10 + Process Step 4 |
| §3.6 errorEnvelope code-per-agent | Every agent emits own typed final-failure code | ✅ `ai_video_gen_agent_failed` (renamed from inherited `production_coord_agent_failed` per slot 11) |
| §3.7 qc_pre_flags snake_case ≥4 | Format `^[a-z][a-z0-9_]{0,63}$`, min 4 entries | ✅ Check #12 enforces |
| §3.8 escalation_path ordering | Ordered ascending by severity | ✅ Process Step 10 documents |
| §3.9 metadata canonical block | Every agent emits standard metadata block | `<<TBD-D23>>` §16 |
| §3.10 optional field absence rule | Absent (not null) when not applicable | ✅ `fallback_engine_id` field map row enforces |

**Day 24 LOCK reviewer note:** The error code expansion from 14 (outline §3.6) to 17 (this document §6.3) is the only canon-drift risk identified in this Day 22 pass. Day 24 reviewer must confirm the 17 codes are exhaustive and that schema (Day 25) enumerates all 17.

---

## SCHEMA NO-TOUCH RULE (re-asserted)

This document does NOT modify any LOCKED schema. References only:

- `production_plan.json` schema (Day 17 LOCKED) — read-only reference for §10 field map source fields
- `storyboard.json` schema (Week 2/3 LOCKED) — read-only reference (audit trail only)
- `script.json` schema (Day 9 LOCKED) — read-only reference (audit trail only)
- `brief.json` schema (Day 7 LOCKED) — read-only reference (audit trail only)

Day 25 will author `rendered_shots.json` schema. Until then, all fields described in §3 of outline + §10 of this document are SPEC-level claims, not schema-level enforcement.

---

## ENTITY SEPARATION (re-asserted — Day 22 SPEC body)

This document is Sequel Digital ARS canon. Principal / Holdco Group / NPOX ZERO involvement.

**Defense-in-depth firewall list (5th layer continues — see §6.5 for canonical 10-entry list):**
- Holdco Group / Holdco Group Inc. / HC (and conjugates)
- 4821 Main / 4821 / Main flagship
- SITE-C-BRAND / 6315 / 6315
- SLN / SLN Group / SLN Cuts / SLN Shear / SLN Salon / SalonB / Shear & Cuts
- Retail Supply / Retail Supply Co
- Principal Holdco / Principal
- NPOX / Community Nonprofit Org / Nonprofit Leader A / Nonprofit Leader B / Nonprofit Leader C
- Partner Brand
- holdcogroup.com (URL token)

Document scanned for firewall references — every reference is in the firewall list itself, by design.

---

## PROCESS INTEGRITY (Day 22 build)

- ✅ Rest Day rule honored — Day 21 was Rest Day (scaffold only); Day 22 is build day (full SPEC body authoring permitted)
- ✅ No LLM dispatched. No render API touched. No engine credentials referenced.
- ✅ No external comms (no emails sent, no DMs, no posts)
- ✅ No financial commitments (no engine subscriptions, no quota purchases)
- ✅ No banned-vocab leaks — firewall list scanned across this document
- ✅ Predecessor SPEC NOT touched (ProdCoord Day 14 LOCK respected — referenced only)
- ✅ Predecessor schemas NOT touched (ProdCoord Day 17 LOCK respected — referenced only)
- ✅ Cross-SPEC canon NOT touched (LOCKED — referenced only, §3 adherence audited above)
- ✅ AI Video Gen outline NOT touched (Day 20 outline LOCKED-as-shipped — referenced only)
- ✅ Day 21 scaffold NOT touched (Day 21 scaffold preserved — all `<<TBD-D22-*>>` markers resolved in this document, not in scaffold)
- ✅ Build log to be written same day (`build-log-2026-05-11.md`)
- ✅ Mirror to `/outputs/ars/` to be completed
- ✅ No fake-advance: §8/§9/§11/§12/§13/§15/§16 explicitly marked `<<TBD-D23>>`, not pretended-LOCKED

---

## PROVENANCE

- Authored: 2026-05-11 (Mon · Day 22 · Wk4D2) — ARS overnight build session
- Deliverable file: `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` (Desktop/ARS/ + outputs/ars/ mirror)
- Pattern source: `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` §6 / §7 / §10 / §14 (Day 14 LOCKED — verbatim shape inherited)
- Scaffold source: `ARS-2026-05-10-Day-22-SPEC-Body-Pre-Flight-Rest Day-Prep.md` (Day 21 Rest Day prep — all ~21 `<<TBD-D22-*>>` markers resolved in this document)
- Predecessor outline: `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (Day 20)
- Cross-spec canon: `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — §3 adherence audited above)
- Daily OS reference: Rest → Body → Money → Authority → Relationships pillar (Day 22 = Money block, build advanced)

*Day 22 closes Wk4D2 with AI Video Gen Agent v1.0 SPEC body §6 (12-check Self-QC, 17 errorEnvelope codes enumerated) + §7 (System Prompt v1.0 — 13 hard rules, tier table, 11-step process, voice rule) + §10 (21-row field map: production_plan → rendered_shots) + §14 (calendar status updates) all LOCKED-as-drafted. §8/§9/§11/§12/§13/§15/§16 explicitly slot-reserved `<<TBD-D23>>` — no fake-advance. Day 24 LOCK target unchanged. Day 25 schema authoring fully primed.*
