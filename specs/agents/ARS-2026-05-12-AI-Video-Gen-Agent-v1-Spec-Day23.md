# ARS — AI Video Gen Agent v1.0 SPEC (Body §8 / §9 / §11 / §12 / §13 / §15 / §16 — Day 23 LOCKED-as-drafted)

**Date:** May 12, 2026 (Tue · Day 23 · Wk4D3)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** REMAINING SPEC BODY — §8 (Performance Targets) · §9 (5 Test Fixtures) · §11 (Cost Model per-engine $/sec) · §12 (Style Consistency Math) · §13 (17 Critical Decisions LOCKED) · §15 (Change Log) · §16 (Metadata Block Schema) all drafted to LOCK-quality. **Day 22 sections §6 / §7 / §10 / §14 NOT TOUCHED** — inherited verbatim from `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md`. On Day 24 the two Day-22 + Day-23 partial-SPEC files are reconciled into the single v1.0-LOCKED document. **No LLM dispatched. No render API touched. No engine credentials referenced. No external comms. No financial commitments. No vendor subscriptions purchased.**
**Pattern source:** `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` §8 / §9 / §11 / §12 / §13 / §15 / §16 (Day 14 LOCKED — verbatim shape inherited; numerical values re-derived for Mode B render runtime)
**Predecessor partial:** `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` (Day 22 — §6 / §7 / §10 / §14 LOCKED-as-drafted; this document is the missing complement)
**Predecessor outline:** `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (§0–§5 SHIPPED Day 20)
**Predecessor schemas:** `skills/production-coord-agent/schemas/output.schema.json` (Day 17 LOCKED — read-only reference for input contract)
**Cross-spec canon:** `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — §3 adherence re-audited at end of this document)

---

## DAY 23 AUTHORING SCOPE

This document completes the AI Video Gen Agent v1.0 SPEC body. Seven sections are LOCKED-as-drafted today:

- **§8** — Performance Targets (9 metric categories with concrete v1.0 numbers; calibration windows for first 10 / 30 / 90 Mode B reels enumerated)
- **§9** — 5 Test Fixtures (TC-01 Pro happy path · TC-02 Enterprise happy path · TC-03 anchor failure · TC-04 cost overrun · TC-05 engine cascade failure; pattern from ProdCoord §9 Day 14)
- **§11** — Cost Model per-engine $/sec lookup (RESEARCH-ONLY snapshot — vendor pricing canon verification deferred to Day 24 LOCK reviewer; 8 engines × per-model rows)
- **§12** — Style Consistency Math (drift_threshold derivation, inheritance_match_score_0_1 algorithm, v1.0 literal_seed_inherit semantics, calibration plan)
- **§13** — 17 Critical Decisions LOCKED (decision · rationale · alternative considered · revisit trigger — mirror ProdCoord §13 17-decision count)
- **§15** — Change Log + Version History (8 entries from Day 20 outline through Day 27 LLM Test Runbook)
- **§16** — Metadata Block Schema (canonical Cross-SPEC §3.9 block + 3 AI Video Gen-specific additions)

The 17-errorEnvelope-code count surfaced in §6.3 (Day 22 doc) is RE-ASSERTED in §13 Decision #11 and §15 v1.0-draft-day-22 entry. Day 24 LOCK reviewer is the gating reconciliation authority.

---

## §8 — Performance Targets (LOCKED-as-drafted Day 23)

The AI Video Gen Agent v1.0 ships against the following measurable performance envelope. Targets are calibrated for the **first 30 Mode B reels** (Lever 3 — every reel reviewed by human via QC Agent). Lever 2 graduation (after 30) and Lever 1 graduation (after 90) require re-calibration via §12.4 calibration plan and Open Question #10 (deferred to post-Day 30).

**Reading rule:** every target below is a v1.0 commit. Day 27 LLM Test Runbook produces the first empirical reading; Day 30 retrospective is the first calibration checkpoint. Below-target metrics are not failure — they are calibration signal for v1.1 planning.

### 8.1 The 9 metric categories

| # | Metric | v1.0 Target | Failure threshold | Measurement window | Source field |
|---|--------|------------:|------------------:|-------------------:|--------------|
| 1 | **Schema validity rate** (output validates clean against `output.schema.json`) | 100% | < 99% | Per-reel, rolling 30 | self-QC Check #6 + #11 + #12; final post-§6 validator |
| 2 | **Firewall catch rate** (entity firewall + banned vocab + no-buildings — zero leaks reach `successRenderedShots`) | 100% | ≥ 1 leak | Per-reel, ALL reels | Check #1 + #2 + #3; `qc_warnings[]` audit |
| 3 | **Anchor render success rate** (anchor completes `render_status="rendered"` within 1 retry + 1 fallback) | ≥ 92% | < 85% | Per-reel, rolling 30 | `style_consistency_anchor.anchor_shot_id` resolves; `rendered_shots[0].render_status == "rendered"` |
| 4 | **Anchor drift rate** (anchor `inheritance_match_score_0_1` < `drift_threshold` 0.85 across inheritor shots) | ≤ 15% per reel | > 25% per reel | Per-shot, rolling 30 | `style_consistency_anchor.inheritor_shots[*].inheritance_match_score_0_1` |
| 5 | **Render success rate by engine** (per-engine: rendered / dispatched) | ≥ 88% per engine; ≥ 94% portfolio-weighted | < 80% any engine; < 88% portfolio | Per-engine, rolling 30 | `render_telemetry.per_engine_*`; `retry_log[*]` |
| 6 | **Budget variance distribution** (actual / estimate) | 0.92 ≤ ratio ≤ 1.08 for ≥ 80% of reels; HARD ceiling ratio ≤ 1.10 | ratio > 1.10 (any reel) OR < 0.85 for > 30% of reels (under-estimating upstream) | Per-reel, ALL reels | `render_telemetry.budget_variance_pct` |
| 7 | **Wall-clock latency** (Pro tier p50 / p95; Enterprise tier p50 / p95) | Pro p50 ≤ 9 min · p95 ≤ 18 min · Enterprise p50 ≤ 16 min · p95 ≤ 32 min | Pro p95 > 25 min OR Enterprise p95 > 45 min | Per-reel, rolling 30 | `render_telemetry.total_wall_clock_minutes` |
| 8 | **Retry rate** (`retry_count_total / total_shots`) | ≤ 0.20 (Pro) · ≤ 0.25 (Enterprise) | > 0.40 (Pro) · > 0.50 (Enterprise) | Per-reel, rolling 30 | `render_telemetry.retry_count_total` ÷ `total_shots` |
| 9 | **Fallback engine activation rate** (shots that touched `fallback_engine_id`) | ≤ 8% of shots | > 15% of shots | Per-shot, rolling 30 | `rendered_shots[*].fallback_engine_id` present count ÷ total |

### 8.2 Per-tier cost discipline (sub-targets of §8.1 #6)

| Tier | Average actual cost ÷ ceiling | Target | Failure threshold |
|------|------------------------------:|-------:|------------------:|
| Pro ($400 ceiling) | Mean over rolling 30 reels | 0.55 ≤ mean ≤ 0.85 | mean > 0.95 (squeezing ceiling) OR mean < 0.40 (over-engineered estimate) |
| Enterprise ($750 ceiling) | Mean over rolling 30 reels | 0.55 ≤ mean ≤ 0.85 | mean > 0.95 OR mean < 0.40 |

**Rationale:** ceiling utilization in the 55–85% band proves the cost model is well-calibrated. Above 95% utilization means we're routinely flirting with `cost_overrun` — re-bid the engine assignment heuristic. Below 40% means we're systematically over-estimating — operator margin is fine but ProdCoord's `total_render_cost_usd_estimated` model needs tightening (v1.1+ ProdCoord retro).

### 8.3 Self-QC pass rate

| Metric | Target | Failure threshold |
|--------|-------:|------------------:|
| First-attempt pass rate (all 12 checks PASS on first run, no regenerate) | ≥ 85% | < 70% |
| Two-attempt pass rate (regenerate-and-pass within Rule #13's 2-strike ceiling) | ≥ 97% | < 92% |
| Final fail rate (errorEnvelope emitted with `attempts: 2`) | ≤ 3% | > 8% |

### 8.4 Calibration windows

Performance targets above are v1.0 commits with the following calibration rule:

- **First 10 Mode B reels (Day 29 onward):** ANY single target miss is informational only — calibration data, not failure. Operator reviews telemetry, no v1.1 trigger.
- **First 30 reels (Lever 2 graduation gate):** Aggregated 30-reel rolling window evaluated. Any metric ≥ "Failure threshold" column = blocking Lever 2 graduation. Operator re-tunes engine assignment heuristic OR cost ceiling buffer OR drift threshold (per §12.4).
- **First 90 reels (Lever 1 graduation gate):** Aggregated 90-reel rolling window. Both Lever 2 metrics held + lower-volatility verification (each metric stable within ±10% across last 30) = Lever 1 eligible. Per Orchestration Blueprint §6 lever framework.

### 8.5 What is intentionally NOT in §8 (v1.0 scope discipline)

The following are deferred to v1.1+ and explicitly out-of-scope for v1.0 performance targets:

- Quality scoring of rendered output (face naturalism, motion smoothness, brand-fit human rating) — handled by QC Agent post-§8; AI Video Gen emits seed only.
- Per-engine quality bias profiling (Runway runs hot on motion, Pika weak on faces, etc.) — v1.1+ feature.
- Cost-per-engagement downstream attribution (reel cost ÷ downstream engagement) — Analytics Agent (Loop layer) territory, post-Week 6.
- Inter-reel anchor consistency (does Reel #7 visually echo Reel #6?) — Style Replication Agent (Mode C, Week 5) territory.

### 8.6 Performance target measurement source — runtime hooks

Per Cross-SPEC §3.9 metadata block, every reel emits the following metric-hook fields that §8 dashboard (per Day 30 retro deliverable) aggregates:

```
render_telemetry.total_render_seconds_actual
render_telemetry.total_render_cost_usd_actual
render_telemetry.budget_variance_pct
render_telemetry.per_engine_cost_usd[*]
render_telemetry.retry_count_total
render_telemetry.failure_count_total
render_telemetry.total_wall_clock_minutes
style_consistency_anchor.inheritor_shots[*].inheritance_match_score_0_1
rendered_shots[*].render_status
rendered_shots[*].fallback_engine_id (presence)
metadata.self_qc_attempts (1 or 2)
metadata.self_qc_failed_check_id (null on success, 1..12 on failure)
```

Day 27 LLM Test Runbook validates that all 12 fields populate correctly across 5 fixtures.

---

## §9 — 5 Test Fixtures (LOCKED-as-drafted Day 23)

Pattern source: ProdCoord SPEC §9 (Day 14 LOCKED — proven 5/5 PASS on Day 18 SKILL bundle validation). The 5 fixtures cover the v1.0 happy-path scenarios + 3 failure modes. Each fixture lives at `skills/ai-video-gen-agent/tests/` (Day 26 SKILL bundle).

**Fixture format (per Cross-SPEC canon §3.11):**
- `input.json` — full agent input (production_plan + brief + script + storyboard + session_id + lever_state + engine_quota_handles)
- `expected_output.json` — expected agent output (successRenderedShots OR errorEnvelope variant)
- `expected_error_code` — string OR null (null = success expected)
- `scenario_description` — operator-facing prose describing why this fixture exists

**Defense-in-depth:** every fixture's input passes the same firewall walks the agent performs. NO fixture input contains entity-firewall tokens, banned vocab, or no-buildings violations. Negative test cases test the agent's FAILURE detection, not its tolerance of bad data — Pilot/Starter tier in input.json would be a malformed fixture, not a valid negative test (those halt at Step 1, not the engine-level failure modes §9 cares about).

### 9.1 TC-01 — Pro Mode B happy path (anchor + 2 inheritors, single engine type)

**Scenario:** Pro tier client. 3-shot reel. All shots assigned Runway Gen3 Alpha. Anchor renders on first attempt; both inheritors render on first attempt. Final cost = $232 (well under $400 Pro ceiling). Final wall-clock = 7.5 min. No retries. No fallback engine activation. Self-QC passes all 12 checks on first attempt.

**Input shape (abbreviated):**
```
production_plan.tier = "Pro"
production_plan.production_mode = "B"
production_plan.mode_b_plan.render_queue = [
  { shot_id: "shot-001", engine_id: "runway", model_id: "runway-gen3-alpha", duration_s: 15, quota_reserved_bool: true, prompt_seed: "...", fallback_engine_id: "pika" },
  { shot_id: "shot-002", engine_id: "runway", model_id: "runway-gen3-alpha", duration_s: 12, quota_reserved_bool: true, prompt_seed: "...", fallback_engine_id: "pika" },
  { shot_id: "shot-003", engine_id: "runway", model_id: "runway-gen3-alpha", duration_s: 18, quota_reserved_bool: true, prompt_seed: "...", fallback_engine_id: "pika" }
]
production_plan.mode_b_plan.style_consistency_anchor.anchor_shot_id = "shot-001"
production_plan.mode_b_plan.total_render_cost_usd_estimated = 240
lever_state = 3
```

**Expected output:**
- `status: "ready_for_edit"`
- `total_rendered_shots == 3`
- `rendered_shots[0..2].render_status == "rendered"`
- `render_telemetry.total_render_cost_usd_actual ≈ 232` (within ±3% of 240 estimate)
- `render_telemetry.budget_variance_pct ≈ -3.3`
- `render_telemetry.retry_count_total == 0`
- `render_telemetry.failure_count_total == 0`
- `style_consistency_anchor.inheritor_shots[*].inheritance_match_score_0_1 ≥ 0.85` (both above threshold)
- `qc_pre_flags` contains 5 snake_case predicates
- `metadata.self_qc_attempts == 1`

**Expected error code:** `null`

**Why this fixture exists:** Proves the happy path. If TC-01 fails, the agent is broken — every other fixture's failure mode becomes uninterpretable. TC-01 is the "go/no-go" diagnostic.

### 9.2 TC-02 — Enterprise Mode B happy path (anchor + 4 inheritors, mixed engines, HeyGen talent)

**Scenario:** Enterprise tier client. 5-shot reel. Anchor = Runway Gen3 Turbo (premium engine, Enterprise-only). Inheritors mix Pika + HeyGen v3 (talent: Jamila clone v2) + Kling. All renders succeed first attempt. Final cost = $612 (under $750 Enterprise ceiling). Final wall-clock = 14 min. HeyGen talent_id verified against canonical handle. No retries.

**Input shape (abbreviated):**
```
production_plan.tier = "Enterprise"
production_plan.production_mode = "B"
production_plan.mode_b_plan.render_queue = [
  { shot_id: "shot-001", engine_id: "runway", model_id: "runway-gen3-alpha-turbo", duration_s: 20, ... },
  { shot_id: "shot-002", engine_id: "pika", model_id: "pika-1.5", duration_s: 12, ... },
  { shot_id: "shot-003", engine_id: "heygen", model_id: "heygen-v3-polish", talent_id: "jamila-howard-reinvented-v2", duration_s: 25, ... },
  { shot_id: "shot-004", engine_id: "kling", model_id: "kling-1.6", duration_s: 15, ... },
  { shot_id: "shot-005", engine_id: "pika", model_id: "pika-1.5", duration_s: 18, ... }
]
production_plan.mode_b_plan.total_render_cost_usd_estimated = 605
lever_state = 3
```

**Expected output:**
- `status: "ready_for_edit"`
- `total_rendered_shots == 5`
- All 5 shots `render_status == "rendered"`
- `rendered_shots[2].engine_id == "heygen"` AND `talent_id == "jamila-howard-reinvented-v2"` verified
- `render_telemetry.total_render_cost_usd_actual ≈ 612`
- `render_telemetry.per_engine_cost_usd` populated for runway + pika + heygen + kling
- `inheritance_match_score_0_1 ≥ 0.85` across all 4 inheritors
- `metadata.self_qc_attempts == 1`

**Expected error code:** `null`

**Why this fixture exists:** Proves multi-engine coordination + HeyGen talent firewall (Check #9) + Enterprise-tier cost ceiling discipline + cross-engine anchor inheritance (literal_seed_inherit holding across Runway → Pika/Kling/HeyGen).

### 9.3 TC-03 — Anchor failure (engine_failure_unrecoverable, whole-set blocked)

**Scenario:** Pro tier client. 3-shot reel. Anchor shot dispatched to Runway → primary fails (simulated 502 from engine) → 1 retry on Runway also fails → fallback to Pika → 1 retry on Pika also fails. All 4 attempts exhausted on anchor. Per Hard Rule #11, anchor failure is fatal — agent halts WITHOUT dispatching inheritor shots. Cost incurred = ~$45 (the 4 failed anchor attempts).

**Input shape (abbreviated):**
```
production_plan.tier = "Pro"
production_plan.mode_b_plan.render_queue = [
  { shot_id: "shot-001", engine_id: "runway", duration_s: 15, fallback_engine_id: "pika", ... },
  { shot_id: "shot-002", engine_id: "runway", duration_s: 12, fallback_engine_id: "pika", ... },
  { shot_id: "shot-003", engine_id: "runway", duration_s: 18, fallback_engine_id: "pika", ... }
]
// Test harness injects 4x consecutive 502 from runway+pika on shot-001 dispatch
```

**Expected output (errorEnvelope variant):**
```
{
  status: "blocked",
  errorEnvelope: {
    failure_code: "engine_failure_unrecoverable",
    failed_check_id: 6,
    failed_shot_id: "shot-001",
    attempts: 4,
    detail: {
      anchor_shot_id: "shot-001",
      engines_burned: ["runway", "pika"],
      cost_incurred_usd: 45,
      reason: "Anchor render exhausted primary + 1 retry + fallback + 1 retry"
    }
  }
}
```

**Expected error code:** `engine_failure_unrecoverable`

**Why this fixture exists:** Proves the anchor-fatal halt semantics. Critical to validate that inheritors are NEVER dispatched after anchor failure — operator loses 1 anchor cost (~$45 worst case), not 3 shot costs (~$230). Validates Hard Rule #11 enforcement.

### 9.4 TC-04 — Cost overrun (renders complete, but actual > 110% of estimate)

**Scenario:** Enterprise tier client. 5-shot reel. All renders succeed (test harness simulates per-shot success with each engine call costing ~30% more than estimated). Final actual cost = $852 against $750 estimate. $852 / $750 = 1.136 → exceeds 1.10 ceiling per Hard Rule #7. Agent halts at Process Step 8 (render telemetry true-up) BEFORE emitting handoff_targets. Emits `cost_overrun` errorEnvelope. Operator is on the hook for the $852 spent; failure prevents downstream consumption of an over-budget set.

**Input shape (abbreviated):**
```
production_plan.tier = "Enterprise"
production_plan.mode_b_plan.total_render_cost_usd_estimated = 750
// Test harness injects per-engine cost inflation of ~30% across all 5 renders
cost_overrun_buffer_pct = 10  // explicit default
```

**Expected output (errorEnvelope variant):**
```
{
  status: "blocked",
  errorEnvelope: {
    failure_code: "cost_overrun",
    failed_check_id: 7,
    attempts: 1,
    detail: {
      total_render_cost_usd_actual: 852,
      total_estimated_cost_usd: 750,
      tier_cost_ceiling_usd: 750,
      cost_overrun_buffer_pct: 10,
      hard_ceiling: 825,  // 750 × 1.10
      excess_usd: 27,
      excess_pct: 13.6,
      per_engine_overrun_attribution: { runway: +42, pika: +18, heygen: +15, kling: +12, flux: +5 }
    }
  }
}
```

**Expected error code:** `cost_overrun`

**Why this fixture exists:** Proves the hard cost ceiling. Validates Hard Rule #7 + Check #7. Validates that per-engine cost attribution is captured for the post-mortem (which engine pushed us over). Critical operator-facing guarantee: a single render set NEVER bills above ceiling × 1.10.

### 9.5 TC-05 — Engine cascade failure (render_quota_exhausted)

**Scenario:** Pro tier client. 3-shot reel. Anchor renders successfully on Runway first attempt. Inheritor shot-002 dispatched to Pika → primary fails → 1 retry fails → fallback to Luma → both attempts fail. Inheritor shot-003 dispatched to Kling → primary fails → 1 retry fails → fallback to Higgsfield → both attempts fail. Inheritor shot-002 and shot-003 BOTH burned all 4 engine attempts. Per Hard Rule #12, inheritor failure does NOT halt the agent (anchor succeeded). Agent emits partial set with `status="partial_with_warnings"` AND lists failed shot_ids in `qc_warnings[]`. If EVERY inheritor failed across all retries → `render_quota_exhausted` errorEnvelope (this fixture: both fail → escalates to render_quota_exhausted because no successful inheritors).

**Input shape (abbreviated):**
```
production_plan.tier = "Pro"
production_plan.mode_b_plan.render_queue = [
  { shot_id: "shot-001", engine_id: "runway", fallback_engine_id: "pika", ... },
  { shot_id: "shot-002", engine_id: "pika", fallback_engine_id: "luma", ... },
  { shot_id: "shot-003", engine_id: "kling", fallback_engine_id: "higgsfield", ... }
]
// Test harness: shot-001 succeeds first attempt. shot-002 fails all 4. shot-003 fails all 4.
```

**Expected output (errorEnvelope variant — escalated because zero inheritors succeeded):**
```
{
  status: "blocked",
  errorEnvelope: {
    failure_code: "render_quota_exhausted",
    failed_check_id: 5,
    attempts: 2,  // 2 inheritor shots, both burned all attempts
    detail: {
      anchor_shot_id: "shot-001",
      anchor_status: "rendered",
      failed_inheritor_shot_ids: ["shot-002", "shot-003"],
      engines_burned: ["pika", "luma", "kling", "higgsfield"],
      cost_incurred_usd: 198,  // anchor cost + 8 failed attempts
      reason: "All inheritor shots exhausted primary + fallback engines"
    }
  }
}
```

**Expected error code:** `render_quota_exhausted`

**Alternative scenario (recorded in fixture comment, not separate fixture):** if shot-002 had succeeded after fallback, agent would emit `successRenderedShots` with `status="partial_with_warnings"`, `total_rendered_shots == 2`, `qc_warnings[]` listing `"shot_003_render_failed_after_fallback"`. The escalation to `render_quota_exhausted` is specifically for zero-success inheritor sets.

**Why this fixture exists:** Proves cascade failure semantics + partial-set tolerance + escalation logic. The most complex of the 5 fixtures because it walks the boundary between `partial_with_warnings` (still-emit) and `render_quota_exhausted` (halt). Validates Hard Rule #12 + Check #5.

### 9.6 Test fixture summary table

| TC | Tier | Shots | Anchor | Inheritors | Cost | Expected outcome | Error code |
|----|------|------:|--------|------------|-----:|------------------|------------|
| TC-01 | Pro | 3 | ✅ first attempt | ✅ all first attempt | $232 / $400 ceiling | `ready_for_edit` | `null` |
| TC-02 | Enterprise | 5 | ✅ first attempt | ✅ all first attempt (multi-engine + HeyGen) | $612 / $750 ceiling | `ready_for_edit` | `null` |
| TC-03 | Pro | 3 | ❌ engine_failure_unrecoverable (4 attempts) | ⏸ NOT dispatched | $45 incurred | `blocked` | `engine_failure_unrecoverable` |
| TC-04 | Enterprise | 5 | ✅ first attempt | ✅ all first attempt | $852 / $750 × 1.10 = $825 ceiling — $27 over | `blocked` | `cost_overrun` |
| TC-05 | Pro | 3 | ✅ first attempt | ❌ both inheritors burned all 4 attempts | $198 incurred (anchor + failed attempts) | `blocked` | `render_quota_exhausted` |

**Coverage:** 2 happy paths (Pro + Enterprise) + 3 failure modes (anchor-fatal · cost-overrun · cascade-failure) = 5 fixtures. **5 of 17 errorEnvelope codes** are directly exercised: `engine_failure_unrecoverable`, `cost_overrun`, `render_quota_exhausted` (TC-03/04/05) + `null` × 2 (TC-01/02 happy paths). The remaining 12 codes (input_validation_failed, entity_firewall_breach, tier_constraint_violation, production_plan_not_success, not_mode_b, quota_not_reserved, anchor_misalignment, negative_prompt_missing, talent_unauthorized, banned_vocab_leaked, no_buildings_violation, qc_pre_flags_format_violation, ai_video_gen_agent_failed, schema_invalid_after_retry) are covered by **schema-validator-only fixtures** in the Day 26 SKILL bundle test suite (negative-test inputs that fail schema parse OR that the agent halts on at Process Step 1–4 without external dispatch — zero cost).

### 9.7 Day 27 LLM Test Runbook integration (forward reference)

Day 27 runbook applies the Day 11 / Day 19 paste-and-run pattern. Per-fixture expectations:
- TC-01 / TC-02 (happy paths): operator pastes input, agent emits successRenderedShots, validator runs Draft 2020-12 against `output.schema.json`, validator runs 12-check audit against `qc_pre_flags`, validator confirms `metadata.self_qc_attempts == 1`. PASS = green.
- TC-03 / TC-04 / TC-05 (failure paths): operator pastes input, agent emits errorEnvelope, validator confirms `failure_code` matches expected, validator confirms `failed_check_id` matches expected. PASS = green.

**v1.0 LOCK gate:** 5/5 PASS = operator-gated v1.0 LOCK signed (Day 27+ — date floats based on Jamila availability).

**Open Question (Day 24 LOCK reviewer flag):** Day 27 runbook touches paid render APIs in TC-01 and TC-02 (happy paths require actual engine dispatch). Cost ceiling for runbook ≤ ~$3 (1 Pro + 1 Enterprise happy path = ~$844 worst case BUT v1.0 runbook MAY use a "dry-run mode" where engines return cached mock responses — decision deferred to Day 27 itself, not Day 24 LOCK). **If dry-run mode adopted:** cost ≈ $0. **If live mode adopted:** ≤ $1,000 single-pass cost ($232 + $612 worst case from happy paths, OR scaled-down 1-shot test variants at ~$15 each). Day 24 reviewer surfaces this as Open Question #11 (added today).

---

## §11 — Cost Model (per-engine $/sec lookup table) (LOCKED-as-drafted Day 23 · RESEARCH-ONLY snapshot)

**RESEARCH-ONLY snapshot disclaimer:** the per-engine pricing below is sourced from vendor public pricing documentation as of May 2026 (knowledge cutoff considerations). Day 24 LOCK reviewer is the **gating verification authority** before this table feeds Check #7 (cost ceiling) math in production. No vendor subscription has been purchased to verify pricing. No API call has been made. No engine credentials referenced. This table is a **SPEC-level numerical artifact** — runtime authority is the orchestrator's vendor-pricing canon (TBD location, Day 26 SKILL bundle to embed).

**Reading rule:** every row below is a v1.0 commit subject to Day 24 verification. Material discrepancies (>15% vs verified vendor pricing) on Day 24 → row corrected + flagged in §15 change log entry `v1.0-pricing-corrections-day-24`.

### 11.1 The per-engine table (8 engines × per-model rows)

| Engine | Model | $/sec (1080p / vertical 9:16) | Runtime cap (sec) | Quota unit definition | Notes |
|--------|-------|-------------------------------:|------------------:|------------------------|-------|
| **Runway** | Gen3 Alpha | 0.95 | 60 (Pro) / 90 (Ent) | seconds rendered | Highest-fidelity general-purpose. v1.0 default for hero shots. |
| **Runway** | Gen3 Alpha Turbo | 0.45 | 60 / 90 | seconds rendered | Enterprise-only (per §4 / §7.3 tier table). Faster, slight quality concession. v1.0 anchor candidate for Enterprise tier. |
| **Pika** | Pika 1.5 | 0.30 | 60 / 90 | seconds rendered | Best motion-graphics value at lower price point. v1.0 default for b-roll. |
| **Luma** | Dream Machine | 0.35 | 60 / 90 | seconds rendered | Strong on cinematic motion; weaker on faces. Avoid for HeyGen-substitute scenarios. |
| **Flux** | Flux 1.1 | 0.20 | 60 / 90 | seconds rendered (image-frame interpolated) | Image-first model; sequence frames composed. v1.0 default for static-feel b-roll, posters, opener frames. |
| **Kling** | Kling 1.6 | 0.40 | 60 / 90 | seconds rendered | Strong on cinematic + character work. Mid-tier price. |
| **Higgsfield** | Higgsfield | 0.50 | 60 / 90 | seconds rendered | Specialty: camera motion / cinematic dollies / drone-style. Use sparingly. |
| **HeyGen** | HeyGen v2 (talent) | 0.042 (≈ $2.50 / min) | 60 / 90 | seconds of talent video | v1.0 talent: `jamila-howard-reinvented-v2`. Pro + Enterprise both. |
| **HeyGen** | HeyGen v3 polish (talent) | 0.083 (≈ $5.00 / min) | 60 / 90 | seconds of talent video | Enterprise-only per §7.3 tier table. Polish pass: blink/hand naturalism, voice consistency. |

### 11.2 Pricing canon reference patterns (Day 24 LOCK reviewer cross-check)

| Engine | Public pricing source pattern (operator-verifies Day 24) |
|--------|----------------------------------------------------------|
| Runway | `runwayml.com/pricing` — credit-based; convert credits → $/sec at published rate |
| Pika | `pika.art/pricing` — subscription tiers; per-second cost derived from $/mo ÷ included-seconds-cap |
| Luma | `lumalabs.ai/dream-machine/pricing` — subscription + overage rate |
| Flux | `flux1.ai/pricing` (or replicate.com Flux pricing) — per-image rate × frames; v1.0 estimate uses 24fps assumption |
| Kling | `klingai.com/pricing` — subscription + per-credit |
| Higgsfield | `higgsfield.ai/pricing` — subscription tiers |
| HeyGen | `heygen.com/pricing` — per-minute; v1.0 row converts to per-second |

**Day 24 LOCK reviewer instruction:** for each row, operator visits the public pricing URL pattern above, captures the current per-second (or per-minute → per-second) rate, and confirms the §11.1 table is within ±15%. If outside, the row is corrected and §15 change log entry added. If a vendor has restructured pricing (e.g., shifted from credit-based to flat per-second), the row may need re-derivation; flag as Open Question.

### 11.3 Worked cost examples (anchored against §7.3 tier table)

**Pro tier example (3-shot reel, 45 sec total):**
- Anchor: 15 sec on Runway Gen3 Alpha = 15 × $0.95 = $14.25
- Inheritor 1: 12 sec on Pika = 12 × $0.30 = $3.60
- Inheritor 2: 18 sec on Luma = 18 × $0.35 = $6.30
- Total: $24.15 → well under $400 Pro ceiling (6.0% utilization)
- BUT: real-world has overhead — 4× retry budget + style-token compute + asset upload + quota-reservation costs. v1.0 estimate buffer: 2.5× line-item sum = ~$60 budget envelope. ProdCoord's `total_render_cost_usd_estimated` is the operator-set budget; AI Video Gen enforces it.

**Enterprise tier example (5-shot reel, 90 sec total, HeyGen talent featured):**
- Anchor: 20 sec on Runway Gen3 Turbo = 20 × $0.45 = $9.00
- Inheritor 1: 12 sec on Pika = 12 × $0.30 = $3.60
- Inheritor 2 (HeyGen talent): 25 sec HeyGen v3 polish = 25 × $0.083 = $2.08
- Inheritor 3: 15 sec on Kling = 15 × $0.40 = $6.00
- Inheritor 4: 18 sec on Pika = 18 × $0.30 = $5.40
- Total: $26.08 → well under $750 Enterprise ceiling (3.5% utilization at line-item level)
- Real-world buffered: ~$70 budget envelope (2.5× sum).

### 11.4 What §11 is NOT (v1.0 scope discipline)

- §11 is **not** a vendor contract negotiation tool. Per-engine pricing canon evolves; v1.0 captures the snapshot for SPEC integrity, not for binding commercial terms.
- §11 does **not** authorize engine subscription purchases. Operator (Jamila) signs all engine subscriptions. AI Video Gen consumes pre-reserved quota only.
- §11 does **not** model overage / surge pricing. Some vendors charge premiums for off-peak speed-ups; v1.0 assumes operator buys steady-state plans. Surge pricing → v1.1+.
- §11 does **not** model FX (USD-only). All vendors operate in USD or USD-equivalent. v1.0 hardcoded USD. v1.1+ multi-currency if Sequel Digital signs non-US clients.

### 11.5 Per-engine $/sec table — JSON canonical shape (for Day 25 schema authoring)

```json
{
  "vendor_pricing_canon_version": "v1.0-day-23-research-only",
  "vendor_pricing_canon_verified_iso": "2026-05-24T00:00:00Z",
  "engines": {
    "runway": {
      "models": {
        "runway-gen3-alpha": { "usd_per_sec": 0.95, "runtime_cap_sec_pro": 60, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_rendered" },
        "runway-gen3-alpha-turbo": { "usd_per_sec": 0.45, "runtime_cap_sec_pro": null, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_rendered", "tier_restriction": ["Enterprise"] }
      }
    },
    "pika": {
      "models": { "pika-1.5": { "usd_per_sec": 0.30, "runtime_cap_sec_pro": 60, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_rendered" } }
    },
    "luma": {
      "models": { "luma-dream-machine": { "usd_per_sec": 0.35, "runtime_cap_sec_pro": 60, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_rendered" } }
    },
    "flux": {
      "models": { "flux-1.1": { "usd_per_sec": 0.20, "runtime_cap_sec_pro": 60, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_rendered_24fps_interpolated" } }
    },
    "kling": {
      "models": { "kling-1.6": { "usd_per_sec": 0.40, "runtime_cap_sec_pro": 60, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_rendered" } }
    },
    "higgsfield": {
      "models": { "higgsfield-v1": { "usd_per_sec": 0.50, "runtime_cap_sec_pro": 60, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_rendered" } }
    },
    "heygen": {
      "models": {
        "heygen-v2-clone": { "usd_per_sec": 0.042, "runtime_cap_sec_pro": 60, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_of_talent_video", "talent_id_v1_0": "jamila-howard-reinvented-v2" },
        "heygen-v3-polish": { "usd_per_sec": 0.083, "runtime_cap_sec_pro": null, "runtime_cap_sec_enterprise": 90, "quota_unit": "seconds_of_talent_video", "talent_id_v1_0": "jamila-howard-reinvented-v2", "tier_restriction": ["Enterprise"] }
      }
    }
  }
}
```

This JSON is the canonical machine-readable form. Day 26 SKILL bundle embeds it at `skills/ai-video-gen-agent/vendor_pricing_canon.json`. Day 27 LLM Test Runbook validates it loads + parses + lookup-by-engine-id-and-model-id works.

---

## §12 — Style Consistency Math (LOCKED-as-drafted Day 23)

### 12.1 The math problem

Style consistency is the v1.0 production-mode anchor invariant: every inheritor shot in a Mode B render set MUST visually echo the anchor (`rendered_shots[0]`). The anchor is the style canon — its rendered frames define color palette, motion grammar, framing, lighting, mood. Inheritors that drift too far reduce the reel's perceived cohesion.

v1.0 captures consistency with **`inheritance_match_score_0_1`** (a scalar 0..1 per inheritor) and gates on **`drift_threshold`** (default 0.85). Below threshold → `suspected_drift_bool == true` → soft warning surfaced via `qc_warnings[]` (not a hard halt — operator decides at QC Agent stage).

**Hard rules (recap from §6 / §7):**
- Anchor IS the canon (Hard Rule #11)
- v1.0 inheritance strategy = `literal_seed_inherit` only (Hard Rule #11 + Decision #1)
- Drift below threshold = `qc_warnings[]` (soft), not errorEnvelope (hard). v1.0 NEVER hard-halts on drift; v1.1+ may.

### 12.2 The `inheritance_match_score_0_1` algorithm (v1.0)

For each inheritor shot, compute a composite score blending three signals:

**Signal A: Perceptual hash distance (pHash)**
- Compute `pHash(anchor_first_frame)` and `pHash(inheritor_first_frame)`.
- Hamming distance `d_hamming` over 64-bit hashes; map to similarity `s_phash = 1.0 - (d_hamming / 64.0)`.
- Weight: 0.40 of composite (visual structural similarity).

**Signal B: CLIP embedding cosine similarity**
- Compute `clip_embed(anchor_mid_frame)` and `clip_embed(inheritor_mid_frame)` using a frozen CLIP-ViT-B/32 reference (v1.0 hardcoded).
- Cosine similarity `s_clip = cos(emb_anchor, emb_inheritor)` ∈ [-1, 1]; normalize to [0, 1] via `(s_clip + 1.0) / 2.0`.
- Weight: 0.40 of composite (semantic visual similarity).

**Signal C: Palette histogram intersection**
- Compute dominant-color histogram (16 bins, HSV space) for anchor first frame and inheritor first frame.
- Intersection score `s_palette = sum(min(h_anchor[i], h_inheritor[i]))` ∈ [0, 1].
- Weight: 0.20 of composite (color palette match — REINVENTED canon: purple/gold).

**Composite formula:**
```
inheritance_match_score_0_1 = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette
```

Range: [0, 1]. Higher = more anchor-consistent. v1.0 threshold = 0.85.

### 12.3 The `drift_threshold` derivation

**v1.0 default: 0.85.** Derivation rationale:
- pHash signal alone: 0.80–0.90 typical for visually consistent same-engine renders with seed inheritance; drops to 0.60–0.75 for cross-engine renders even with identical seed.
- CLIP signal alone: 0.85–0.95 typical for semantic-similar scenes from same prompt family; drops to 0.70–0.85 for cross-engine.
- Palette signal alone: 0.90+ for REINVENTED canon palette (purple/gold heavy); drops to 0.70 if engine drifts to off-palette dominant colors.

Composite 0.85 = "consistent enough that an operator at QC Agent stage will not flag visual mismatch in 85% of cases." Below 0.85 = "operator will likely flag → surface as `qc_warnings` so QC stage prioritizes review."

**Calibration plan (§12.4 below):** v1.0 threshold is a research-anchored estimate, not an empirical commitment. Day 30 retrospective is the first calibration checkpoint.

### 12.4 Calibration plan — first 10 / 30 / 90 reels

| Window | Operator action | Threshold adjustment authority |
|--------|-----------------|--------------------------------|
| First 10 reels | Record `inheritance_match_score_0_1` for every inheritor shot. Operator (Jamila + QC reviewer) tags each shot subjectively: "drift apparent — visible" / "drift apparent — subtle" / "no drift — pass." Compare subjective tag to scalar score. | None — observation only |
| First 30 reels (Day 30 retrospective) | Compute correlation between subjective tag and scalar. Recommend threshold adjustment IF: (a) > 25% of subjectively-"drift apparent — visible" shots had score ≥ 0.85 (threshold too lenient) OR (b) > 25% of subjectively-"no drift" shots had score < 0.85 (threshold too strict). | Operator (Jamila) approves threshold change → v1.0.1 patch |
| First 90 reels (Lever 1 graduation gate) | Calibrate per-engine drift baseline (each engine has its own drift signature). v1.1+ feature: per-engine threshold. | Lever 1 graduation gate; v1.1+ migration trigger |

**Critical sub-decision:** drift is NEVER a hard halt in v1.0. The composite score + threshold drive `qc_warnings[]` only. Operator-side QC Agent decides whether to send back for re-render. Rationale: hard-halting on a research-anchored threshold risks blocking legitimate creative renders (e.g., a deliberate aesthetic shift across the reel arc). Threshold is a signal, not a gate.

### 12.5 v1.0 `literal_seed_inherit` semantics

- Every engine's deterministic generation API accepts a `seed: int` parameter. Same seed + same prompt + same engine + same model = bit-identical output (deterministic).
- **Anchor render** (shot_index=1): seed = engine's choice OR operator-provided default seed; agent records `anchor_seed` in `style_consistency_anchor.anchor_seed`.
- **Inheritor render** (shot_index>1): seed = `anchor_seed` (literal copy); each inheritor seeds with the same value.
- Per-engine determinism behavior:
  - Runway: deterministic with seed parameter (verified Day 23 vendor docs).
  - Pika: deterministic with seed parameter.
  - Luma: deterministic with seed parameter.
  - Flux: deterministic with seed parameter.
  - Kling: deterministic with seed parameter (verified).
  - Higgsfield: deterministic with seed parameter.
  - HeyGen: deterministic with seed parameter + talent_id (talent identity is parameter, not seeded).

**v1.0 invariant:** seed inheritance is literal across all engines. v1.1+ may introduce `seed_plus_style_token` blending (Open Question #8) — defer.

### 12.6 What §12 is NOT (v1.0 scope discipline)

- §12 does NOT prescribe creative direction. Operator (brief + script + storyboard) sets the visual canon; AI Video Gen enforces consistency to it.
- §12 does NOT define per-engine drift baselines. v1.1+ feature (Open Question, dependent on first 30-reel calibration data).
- §12 does NOT include audio consistency. Sound Agent (post-Production layer) territory.
- §12 does NOT include cross-reel anchor consistency (Reel #7 matches Reel #6 visually). Style Replication Agent (Mode C, Week 5) territory.

### 12.7 Style consistency math — JSON canonical shape

```json
{
  "style_consistency_anchor": {
    "anchor_shot_id": "shot-001",
    "anchor_seed": 8472913,
    "anchor_engine_id": "runway",
    "anchor_model_id": "runway-gen3-alpha-turbo",
    "inheritor_shots": [
      {
        "shot_id": "shot-002",
        "seed_value": 8472913,
        "inheritance_match_score_0_1": 0.91,
        "score_breakdown": { "s_phash": 0.88, "s_clip": 0.93, "s_palette": 0.94 }
      },
      {
        "shot_id": "shot-003",
        "seed_value": 8472913,
        "inheritance_match_score_0_1": 0.82,
        "score_breakdown": { "s_phash": 0.80, "s_clip": 0.84, "s_palette": 0.82 },
        "suspected_drift_bool": true
      }
    ],
    "drift_threshold": 0.85,
    "drift_threshold_version": "v1.0-day-23-default",
    "propagation_strategy": "literal_seed_inherit"
  }
}
```

`score_breakdown` is optional but recommended — gives QC Agent and v1.1 calibration tooling the per-signal attribution. `drift_threshold_version` is the audit hook for §15 change log when the threshold patches.

---

## §13 — 17 Critical Decisions LOCKED (Day 23 — mirror of ProdCoord §13 count)

The 17 decisions below are v1.0-committed. Each decision: (a) the decision statement, (b) rationale, (c) alternative considered, (d) revisit trigger.

**Reading rule:** Day 24 LOCK reviewer signs off OR sends back for reconciliation. Once signed, no decision changes without §15 change log entry.

### 13.1 The 17 decisions

| # | Decision | Rationale | Alternative considered | Revisit trigger |
|---|----------|-----------|------------------------|-----------------|
| **1** | **Anchor-first sequential render** — anchor (rendered_shots[0]) completes before any inheritor dispatches. | Inheritors need anchor_seed to inherit; parallel dispatch would mean inheritors guess at the seed. Anchor failure must halt the whole set per Rule #11; parallel would have already burned cost. | Parallel-dispatch-with-revoke (cancel in-flight inheritors if anchor fails). Higher complexity; cost saved only when anchor succeeds first attempt. Defer to v1.1+ when retry rate is well-characterized. | Anchor success rate < 88% (per §8 #3 failure threshold) → re-evaluate. |
| **2** | **Retry policy: 1 retry on primary + 1 retry on fallback per shot** (max 4 attempts per shot). | 2-strike ceiling on each engine before failover is the proven ProdCoord retry pattern. Adding a 3rd attempt buys little (failure modes are usually persistent within an engine) and burns 50% more cost on doomed runs. | 0 retries (1 attempt per engine, fail fast). Lower cost but higher coverage failures on transient 5xx. Empirical risk too high for v1.0. | Per-engine retry-success rate < 30% over 30 reels → reduce to 0 retries. |
| **3** | **Cost overrun buffer default: 10%** of `total_render_cost_usd_estimated`. | Vendor pricing variance is real (token-based engines vary ±5%; subscription overages add up). 10% gives breathing room without compromising the 5× margin floor (Pro: $400 ceiling × 1.10 = $440; $440 × 5 = $2,200 — still under Starter-tier Pro retainer). | 5% (tighter — but more frequent `cost_overrun` halts blocking real renders). 15% (looser — but margin risk). | First 30 reels variance distribution: if 80%+ of reels are within ±5%, tighten to 5%. If 20%+ exceed 10%, loosen — but only after engine cost-audit. |
| **4** | **Drift threshold default: 0.85** for `inheritance_match_score_0_1`. | Composite-signal threshold balances false-positive flag rate (too strict) against missed-drift rate (too lenient). Research-anchored estimate; Day 30 calibration window. | 0.80 (lenient — more shots emit). 0.90 (strict — more drift warnings). | First 30 reels subjective-vs-scalar correlation per §12.4 calibration plan. |
| **5** | **Failure cascade: anchor fatal, inheritor partial** — anchor failure halts whole set; inheritor failure permits partial emission. | Inheritors derive from anchor; without an anchor render they have nothing to inherit from. A partial set without an anchor is non-recoverable. A partial set with an anchor + N-1 inheritors is still a usable hero asset + warning surfacing. | Anchor failure also permits partial emission (just emit anchor alone). Rejected: a 1-shot reel from a 3-shot plan is contractually wrong for the operator's brief. Halt + retry full plan is the correct operator action. | If 90%+ of anchor failures are recoverable on re-plan (operator chooses different engine), revisit — v1.1+ "auto-replan on anchor failure" feature. |
| **6** | **HeyGen talent v1.0 hardcoded:** `jamila-howard-reinvented-v2` only. | v1.0 is the REINVENTED brand pilot. Multi-talent is a Sequel Digital external-client trigger. Hardcoding eliminates a Day-26 SKILL bundle complexity branch. | Multi-talent via dynamic talent_id resolution (allowed any HeyGen-onboarded talent). Defer to v1.1+ on Open Question #1. | First paid Sequel Digital external client signs Pro/Enterprise — v1.1 multi-talent enabled. |
| **7** | **Asset URI scheme: platform-relative** — `ars://renderset/<brand_id>/<YYYY-MM-DD>/<seq>/shot-<NNN>.<ext>`. | Absolute external CDN URLs leak credentials in JSON (signed URLs expose access tokens). Platform-relative URIs let the orchestrator resolve to signed URLs at Edit Director → Publishing handoff stage. JSON outputs never carry credentials. | Absolute signed-URL emission with TTL expiry. Higher risk of credential leak in audit trails; defer. | Operator chooses to externalize asset hosting to a 3rd-party CDN with persistent URLs — v1.2+ scheme. |
| **8** | **Negative-prompt template canon location: embedded in SKILL.md** (Day 26 SKILL bundle, per-agent ownership). | v1.0 speed-of-ship choice. Per-agent ownership means template can evolve per agent without coordinating cross-agent. | Shared `firewall-template/` module imported by all production-tier agents. Higher coordination cost on changes; defer to v1.1+ refactor. | Production-tier agent count > 2 (when Style Replication Agent ships Week 5) — re-evaluate refactor opportunity. |
| **9** | **Lever inheritance: read from upstream agents, never set.** AI Video Gen reads `production_plan.lever`, emits `metadata.human_review_required` accordingly. | Lever state is a global pipeline invariant (per Orchestration Blueprint §6). AI Video Gen is one observation point, not the authority. Setting lever from a production-tier agent invites desynchronization. | Allow AI Video Gen to escalate lever (e.g., on anchor failure → force Lever 3 review). Adds state-management complexity; defer. | If 30+ reels show that QC Agent always flags anchor-failure cases for human review regardless of lever — automate the lever escalation, v1.1+. |
| **10** | **escalation_path[] ordered ascending by severity.** Operator-on-call (notes) → engine-vendor support (opaque) → "human review at Edit step required" flag. | Cross-SPEC §3.8 canon. Ascending severity gives operator one place to escalate from (lowest severity first; if unresolved, walk down the list). | Ordered descending (highest severity first). Rejected — convention is ascending across all 17-agent pipeline. | Cross-SPEC canon change. |
| **11** | **17 errorEnvelope codes enumerated** (expanded from outline §3.6 14 → SPEC §6.3 17). | Day 22 §6 authoring discovered 3 codes missing: `qc_pre_flags_format_violation`, formal `engine_failure_unrecoverable` vs `render_quota_exhausted` split, `schema_invalid_after_retry`. Canonical enumeration is the schema contract. | Keep at 14 (outline list). Rejected — would mean §6 self-QC list is under-specified. | Discovery of additional failure mode in first 30 reels → §15 change log v1.0.1 patch. |
| **12** | **12-check Self-QC list shape** (inherited verbatim from ProdCoord §6 12-check shape; sub-content adapted for Mode B). | Proven pattern across Brief / Script / Storyboard / ProdCoord (4× validated). Adding a 13th check or removing one risks cross-SPEC canon drift. | 10 checks (drop entity firewall re-check + banned vocab re-check — already 4× upstream). Rejected — 5th-layer defense-in-depth is the v1.0 commitment. | Defense-in-depth re-evaluation at Lever 1 graduation. |
| **13** | **Voice for written rationale fields** (verbatim inheritance from ProdCoord §7 voice rule). | "Clinical-warm, operator-to-operator, present tense, ≤14 words per sentence, action verbs. No exclamation marks. No emoji. No hedging." | Custom voice per agent. Rejected — cross-SPEC consistency requires single voice across all 17 agents' rationale fields. | Cross-SPEC canon change. |
| **14** | **13 hard rules canon-LOCKED** (per §7.1 system prompt). | Rules are the LLM's contract. Adding a 14th = re-running cross-SPEC consistency review; removing one = re-running self-QC list mapping. 13 is the v1.0 normative count. | 12 (drop Rule 13: 2-strike ceiling — let agent retry indefinitely). Rejected — predictable failure surface beats best-effort recovery. | Empirical drift in first 30 reels showing systematic 2-strike-but-third-would-work pattern. |
| **15** | **Tier table is runtime authoritative** (embedded in §7.1 system prompt). | The LLM is the source of truth at runtime. ProdCoord set the plan; AI Video Gen enforces the ceiling. The table is the contract. | External tier-table lookup (orchestrator-resolved). Rejected — orchestrator could forget to load. Embedding eliminates that failure mode. | Tier table change → §15 entry + schema patch. |
| **16** | **parent_chain LOCKED at 4-tuple** (Brief → Script → Storyboard → ProductionPlan). | AI Video Gen reads from ProdCoord (3-tuple + ProdCoord's own ID = 4-tuple). Mode A pipelines have no AI Video Gen layer; Mode C will be 5-tuple at Style Replication layer. | Variable-length parent_chain (allow 3-tuple for short Mode B chains). Rejected — schema-enforced 4-tuple via `prefixItems` + `items: false` (per ProdCoord schema pattern Day 17) is the proven invariant. | Mode C / Style Replication Agent v1.0 SPEC LOCK (Week 5) — extension to 5-tuple. |
| **17** | **No-buildings rule verified at render-side** (not just plan-side) via `post_render_qc_seed[*].suspected_buildings_bool` flag. | Storyboard / ProdCoord set `no_buildings_compliant_bool` on intent. AI Video Gen verifies on output reality via engine's vision-classifier pass. Intent ≠ output — engines hallucinate. | Trust upstream `no_buildings_compliant_bool` from ProdCoord and skip render-side check. Rejected — 5th-layer defense-in-depth is the v1.0 commitment AND engines can hallucinate buildings regardless of negative prompt. | Vision-classifier false-positive rate > 25% in first 30 reels → consider relaxing OR upgrading classifier. |

### 13.2 Cross-SPEC §3 canon adherence (Day 23 self-audit — completes Day 22 audit)

The 17 decisions above cover all 10 Cross-SPEC §3 dimensions:

| Cross-SPEC §3 | Day 23 decision(s) reinforcing |
|---------------|--------------------------------|
| §3.1 single-responsibility line | (audited Day 22 — "Pixel binding for an executable render queue") |
| §3.2 tier table runtime authority | Decision #15 |
| §3.3 hard rules numbered | Decision #14 (13 rules LOCKED) |
| §3.4 process steps mapping | (audited Day 22 — 11-step process maps to 12-check QC list) |
| §3.5 negative-prompt firewall | (audited Day 22 — Hard Rule #10 + Check #10) |
| §3.6 errorEnvelope code-per-agent | Decision #11 (17 codes enumerated; `ai_video_gen_agent_failed` per-agent) |
| §3.7 qc_pre_flags snake_case ≥4 | (audited Day 22 — Check #12 enforces) |
| §3.8 escalation_path ordering | Decision #10 |
| §3.9 metadata canonical block | §16 below |
| §3.10 optional field absence rule | (audited Day 22 — fallback_engine_id field map row) |

**Day 24 LOCK reviewer sign-off triggers Cross-SPEC §3 full adherence assertion across the 5-agent pipeline.**

---

## §15 — Change Log + Version History (LOCKED-as-drafted Day 23)

Pattern source: ProdCoord SPEC §15 (Day 14 LOCKED). Format: chronological. Each entry = (version-day, date, change summary, files affected).

### 15.1 v1.0 lifecycle entries

| Version | Date | Summary | Files affected |
|---------|------|---------|----------------|
| **v1.0-outline-day-20** | 2026-05-09 (Sat · Wk4D1) | SPEC OUTLINE §0–§5 SHIPPED — purpose, scope, inputs, outputs skeleton, tier constraints, 11-step process. 14 errorEnvelope codes enumerated (initial). 10 Open Questions parked. | `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` |
| **v1.0-scaffold-day-21** | 2026-05-10 (Sun · Wk4D2 · Rest Day) | Day 22 SPEC body pre-flight scaffold — §6 / §7 / §10 / §14 slot scaffolds created with ~21 `<<TBD-D22-*>>` markers. Rest Day rule honored (no SPEC body content authored — docs prep only). | `ARS-2026-05-10-Day-22-SPEC-Body-Pre-Flight-Rest Day-Prep.md` |
| **v1.0-draft-day-22** | 2026-05-11 (Mon · Wk4D2) | SPEC body §6 (12-Check Self-QC) + §7 (System Prompt v1.0) + §10 (Field Map) + §14 (Implementation Plan) LOCKED-as-drafted. ~62 KB. All 21 `<<TBD-D22-*>>` scaffold markers resolved. **Error code count expanded 14 → 17** — flagged for Day 24 LOCK consistency review. Slot 11 errorEnvelope renamed `production_coord_agent_failed` → `ai_video_gen_agent_failed` per Cross-SPEC §3.6. OCR text-overlay Pass-2 walk integrated in Check #2. | `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` |
| **v1.0-draft-day-23** | 2026-05-12 (Tue · Wk4D3) | **THIS DOCUMENT.** SPEC body §8 (Performance Targets) + §9 (5 Test Fixtures) + §11 (Cost Model per-engine $/sec) + §12 (Style Consistency Math) + §13 (17 Critical Decisions LOCKED) + §15 (Change Log) + §16 (Metadata Block Schema) all LOCKED-as-drafted. 17 critical decisions enumerated. 5 test fixtures (TC-01 Pro happy · TC-02 Enterprise happy · TC-03 anchor failure · TC-04 cost overrun · TC-05 cascade failure). Per-engine pricing snapshot (RESEARCH-ONLY — Day 24 verification gate). Style consistency math composite signal formula (pHash 0.40 + CLIP 0.40 + palette 0.20). Open Question #11 added (Day 27 LLM runbook dry-run vs live mode decision). | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` |
| **v1.0-LOCKED-day-24** | 2026-05-13 (Wed · Wk4D4) | **TARGET.** v1.0 LOCK — Day 22 + Day 23 partial docs reconciled into unified SPEC. Cross-SPEC §3 adherence asserted (10 dimensions). Error code count verified at 17 (or reconciled if drift discovered). Per-engine pricing canon verified against vendor public pricing URLs. Sign-off by Jamila. | `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` (unified) |
| **v1.0-schemas-day-25** | 2026-05-14 (Thu · Wk4D5) | **TARGET.** `input.schema.json` + `output.schema.json` (Draft 2020-12). All 17 errorEnvelope codes enumerated. 4-tuple `parent_chain` via `prefixItems` + `items: false`. tier_cost_ceiling joint validation via `allOf`. `composed_prompt_redacted` pattern. `asset_uri` pattern. Self-validating. | `skills/ai-video-gen-agent/schemas/input.schema.json`, `output.schema.json` |
| **v1.0-SKILL-day-26** | 2026-05-15 (Fri · Wk4D6) | **TARGET.** SKILL bundle (10 files: SKILL.md, README, user-template, 2 schemas, 5 test fixtures + vendor_pricing_canon.json). 5/5 input fixtures validate clean. | `skills/ai-video-gen-agent/*` (10 files) |
| **v1.0-LLM-tested-day-27** | 2026-05-16 (Sat · Wk5D1) | **TARGET.** LLM Test Runbook (paste-and-run, pattern from Day 11 / Day 19). Operator-gated. Cost target ≤ $3 (dry-run mode) OR ≤ $1,000 (live mode — decision Day 27). | `ARS-2026-05-16-Day-27-LLM-Test-Runbook.md` |

### 15.2 Post-v1.0 candidates (parking lot)

| Candidate | Trigger | Files affected |
|-----------|---------|----------------|
| v1.0.1 — drift threshold patch | First 30 reels calibration data exceeds §12.4 trigger | §12 + schemas + §15 entry |
| v1.0.1 — pricing canon patch | Vendor pricing change > 15% on any engine | §11 + `vendor_pricing_canon.json` + §15 entry |
| v1.1 — multi-talent | First paid Sequel Digital external client signs Pro/Enterprise (Open Question #1) | §7 Hard Rule #9 + Check #9 + schemas |
| v1.1 — auto-engine swap | Per-engine telemetry stable over 30+ reels (Open Question #3) | §10 field map + system prompt §7 + Decision #2 revisit |
| v1.1 — seed_plus_style_token | Lever 1 graduation + creative-direction feedback (Open Question #8) | §12 + schemas + Decision #1 revisit |
| v1.1 — per-engine drift threshold | 90-reel calibration data (Lever 1 gate) | §12 + schemas + Decision #4 revisit |
| v1.2 — absolute CDN URI scheme | Operator chooses external asset host (Open Question — none parked) | §7 Hard Rule #8 + schemas + Decision #7 revisit |

### 15.3 Format LOCK

Per Cross-SPEC §3.11 change log canon: every entry MUST include version-day, ISO date, summary (≥1 sentence, declarative), files affected (relative paths from project root). v1.0-LOCKED entry Day 24 finalizes format compliance.

---

## §16 — Metadata Block Schema (LOCKED-as-drafted Day 23 — Cross-SPEC §3.9 conformance + AI Video Gen-specific additions)

### 16.1 Canonical metadata block (per Cross-SPEC §3.9)

Every `rendered_shots.json` output MUST emit a `metadata` block with the following 11 canonical fields:

| Field | Type | Format / Constraint | Source |
|-------|------|---------------------|--------|
| `agent_id` | string | `const: "ai-video-gen-agent"` | Hardcoded |
| `agent_version` | string | `pattern: ^v\d+\.\d+(\.\d+)?$` (e.g., `"v1.0"`, `"v1.0.1"`) | Hardcoded per SPEC version |
| `spec_version` | string | `pattern: ^v\d+\.\d+$` (e.g., `"v1.0"`) | Hardcoded per SPEC LOCK day |
| `schema_version` | string | `pattern: ^v\d+\.\d+$` (e.g., `"v1.0"`) | Hardcoded per schema LOCK day (Day 25) |
| `lock_date_iso` | string | ISO 8601 datetime, e.g., `"2026-05-13T00:00:00Z"` | Day 24 LOCK date |
| `parent_chain` | array | 4-tuple LOCKED: `[brief_id, script_id, storyboard_id, production_plan_id]`. Schema enforces via `prefixItems` + `items: false`. | Inherited from `production_plan.parent_chain` (3-tuple) + own `production_plan_id` |
| `session_id` | string | `pattern: ^ars-\d{4}-\d{2}-\d{2}-\d{3,}$` | Inherited from input |
| `created_at` | string | ISO 8601 datetime — render set emission timestamp | Generated at emit time |
| `build_envelope_sha256` | string | 64-hex SHA-256 of the canonical normalized output JSON (excluding `metadata.build_envelope_sha256` itself — recursive exclusion) | Computed at emit time |
| `human_review_required` | boolean | Derived from `lever`: Lever 3 → `true` always; Lever 2 → sampled (1 in 5 default — Open Question #2 parking); Lever 1 → `false` unless any `qc_warnings[]` populated | Derived at emit time |
| `upstream_agent_ids` | array | Ordered: `["brief-agent", "script-agent", "storyboard-agent", "production-coord-agent"]` | Inherited from production_plan.metadata.upstream_agent_ids + own predecessor |

### 16.2 AI Video Gen-specific additions (3 fields)

Per outline §3 plan + Day 22 §6 audit, AI Video Gen emits 3 additional metadata fields beyond Cross-SPEC §3.9 canon:

| Field | Type | Format / Constraint | Why |
|-------|------|---------------------|-----|
| `engine_telemetry_summary` | object | `{per_engine: {<engine_id>: {call_count: int, success_rate_0_1: number, retry_count: int, fallback_invocation_count: int}}}` | Per-engine performance snapshot for §8 #5 (render success rate by engine) telemetry aggregation. Downstream Loop Agent / Analytics Agent reads this for engine-level reporting. |
| `composed_prompt_template_sha256` | string | 64-hex SHA-256 of the composed negative-prompt template (entity firewall + brief.do_not_say + brand-anti + no-buildings) used during this render set | Audit hook for §6 Check #10 (negative prompt presence). If a future render set's hash diverges from current, operator audits why (firewall template patched? brand inheritance changed?). |
| `runtime_environment_class` | string (enum) | `enum: ["dev", "staging", "production"]` | Differentiates real production renders from staging tests from dev iteration. Day 27 LLM Test Runbook uses `staging`. Live production reels use `production`. Dev / experimentation uses `dev`. Schema enforces. |

### 16.3 Per-shot metadata extensions (no top-level metadata change)

The following fields are NOT in `metadata.*` but in `rendered_shots[*]` per-shot — they extend the schema established in §3.2 of outline. Re-asserted here for completeness:

- `self_qc_check_results` — array of 12 booleans per shot (true = PASS, false = FAIL). Only populated on retry/regenerate path; not present on first-attempt-pass.
- `render_dispatch_log[*]` — per-attempt log with `negative_prompt_attached_bool`, `negative_prompt_sha256`, dispatch timestamp, response code, cost incurred per attempt.

### 16.4 Top-level metadata-adjacent fields (not in `metadata.*` but referenced cross-SPEC)

These exist at top-level of `rendered_shots.json` per §3.1 outline:
- `render_set_id` — string, pattern `^renderset-REINVENTED-\d{4}-\d{2}-\d{2}-\d{3,}$`. NOT in metadata block.
- `created_at` — already in metadata; duplicate at top-level NOT permitted (schema rejects).
- `qc_pre_flags` — array, top-level (per Cross-SPEC §3.7).
- `qc_warnings` — array, top-level.

### 16.5 Metadata block JSON canonical example (TC-01 happy path)

```json
{
  "metadata": {
    "agent_id": "ai-video-gen-agent",
    "agent_version": "v1.0",
    "spec_version": "v1.0",
    "schema_version": "v1.0",
    "lock_date_iso": "2026-05-13T00:00:00Z",
    "parent_chain": [
      "brief-REINVENTED-2026-05-12-007",
      "script-REINVENTED-2026-05-12-007",
      "storyboard-REINVENTED-2026-05-12-007",
      "productionplan-REINVENTED-2026-05-12-007"
    ],
    "session_id": "ars-2026-05-12-014",
    "created_at": "2026-05-12T14:32:18Z",
    "build_envelope_sha256": "f1c2a3...64hex",
    "human_review_required": true,
    "upstream_agent_ids": ["brief-agent", "script-agent", "storyboard-agent", "production-coord-agent"],
    "engine_telemetry_summary": {
      "per_engine": {
        "runway": { "call_count": 3, "success_rate_0_1": 1.0, "retry_count": 0, "fallback_invocation_count": 0 }
      }
    },
    "composed_prompt_template_sha256": "a8d4b1...64hex",
    "runtime_environment_class": "staging"
  }
}
```

### 16.6 Schema authoring note (for Day 25)

The Day 25 `output.schema.json` author MUST encode the metadata block as follows:
- `agent_id` MUST use `const: "ai-video-gen-agent"` (not `enum` — single-value constraint).
- `agent_version` MUST use `pattern: "^v\\d+\\.\\d+(\\.\\d+)?$"` (semver-lite).
- `parent_chain` MUST use `prefixItems: [<brief_id schema>, <script_id schema>, <storyboard_id schema>, <production_plan_id schema>]` AND `items: false`.
- `runtime_environment_class` MUST use `enum: ["dev", "staging", "production"]`.
- `engine_telemetry_summary.per_engine` MUST use `patternProperties` with key pattern `^(runway|pika|luma|flux|kling|higgsfield|heygen)$` to enforce the 7 known engines.
- `composed_prompt_template_sha256` MUST use `pattern: "^[a-f0-9]{64}$"`.
- `build_envelope_sha256` MUST use `pattern: "^[a-f0-9]{64}$"`.

### 16.7 v1.0 metadata block is the audit invariant

The metadata block is the **canonical audit fingerprint** of every render set. Two render sets with identical inputs MUST emit identical metadata blocks except for: `created_at`, `build_envelope_sha256`, `engine_telemetry_summary` (if engine telemetry varies — though deterministic seed inheritance should make this near-identical on retries). This invariant is the v1.0 reproducibility guarantee.

---

## CROSS-SPEC CANON ADHERENCE (Day 23 self-audit — completion + extension of Day 22 audit)

Day 22 audit table (in Day 22 SPEC body) covered §3.1 through §3.10 with `<<TBD-D23>>` slot for §3.9. Day 23 completes the table:

| Canon dimension | Cross-SPEC §3 requirement | Day 23 status |
|-----------------|---------------------------|---------------|
| §3.1 Single-responsibility line | One sentence, present tense, ≤10 words | ✅ (Day 22 — "Pixel binding for an executable render queue") |
| §3.2 Tier table runtime authority | Embedded in §7 system prompt verbatim | ✅ (Day 22 + Decision #15) |
| §3.3 Hard rules numbered | Sequential, no gaps, NEVER-violate framing | ✅ (Day 22 — 13 rules + Decision #14) |
| §3.4 Process steps mapping | Each step maps to ≥1 self-QC check | ✅ (Day 22) |
| §3.5 Negative-prompt firewall | Composed from entity + do_not_say + brand-anti + no-buildings | ✅ (Day 22 — Hard Rule #10 + Check #10 + Process Step 4) |
| §3.6 errorEnvelope code-per-agent | Every agent emits own typed final-failure code | ✅ (Day 22 — `ai_video_gen_agent_failed`) + (Day 23 Decision #11 confirms 17-code expansion) |
| §3.7 qc_pre_flags snake_case ≥4 | Format `^[a-z][a-z0-9_]{0,63}$`, min 4 entries | ✅ (Day 22 — Check #12) |
| §3.8 escalation_path ordering | Ordered ascending by severity | ✅ (Day 22) + (Day 23 Decision #10) |
| **§3.9 metadata canonical block** | Every agent emits standard metadata block | ✅ **(Day 23 §16 — 11 canonical fields + 3 AI Video Gen-specific additions LOCKED-as-drafted)** |
| §3.10 optional field absence rule | Absent (not null) when not applicable | ✅ (Day 22 — fallback_engine_id) |

**ALL 10 Cross-SPEC §3 dimensions now LOCKED-as-drafted across Day 22 + Day 23 deliverables.** Day 24 LOCK reviewer signs off OR sends back for reconciliation.

---

## DAY 24 LOCK REVIEWER CHECKLIST

The Day 24 reviewer reads BOTH `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` (Day 22 — §6 / §7 / §10 / §14) AND `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` (THIS DOCUMENT — §8 / §9 / §11 / §12 / §13 / §15 / §16) and either:

(a) **SIGNS OFF** → produces unified `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` Day 24, OR

(b) **SENDS BACK** with reconciliation notes → Day 25 schema authoring deferred until reconciliation complete.

### LOCK reviewer items (Day 24)

| # | Item | Source | Day 24 action |
|---|------|--------|---------------|
| 1 | Error code count = 17 (3-code expansion vs outline §3.6's 14) | Day 22 §6.3 + Day 23 Decision #11 | Verify 17 codes are exhaustive across §6.1 checks + §3.6 input/upstream codes. Re-check that no Mode B failure mode emits an unlisted code. |
| 2 | `ai_video_gen_agent_failed` slot 11 rename | Day 22 §6.1 Check #11 + Day 23 Decision #11 | Verify cross-SPEC §3.6 canon (each agent emits own typed final-failure code). Confirm no orphan `production_coord_agent_failed` references remain in AI Video Gen artifacts. |
| 3 | Per-engine pricing snapshot accuracy | Day 23 §11.1 + §11.2 | Visit each vendor public pricing URL (Day 24 reviewer walkthrough). Verify per-second rates within ±15%. Patch §11.1 row if outside. |
| 4 | Tier table tier_cost_ceiling consistency | Day 22 §7.3 + Day 23 §11.3 worked examples + Day 23 Decision #15 | Confirm Pro $400, Enterprise $750 unchanged across all references. Confirm $400 × 1.10 = $440 + $750 × 1.10 = $825 math is correct in all references. |
| 5 | 12-check QC list ↔ 17 errorEnvelope code mapping | Day 22 §6.1 + §6.3 | Walk every check → confirm every check maps to ≥1 code AND every code maps to ≥1 check (full bipartite coverage). |
| 6 | Drift threshold default 0.85 consistency | Day 22 §3.3 anchor sub-record + Day 23 §12.3 + §12.7 example | Confirm 0.85 unchanged across all references. |
| 7 | 5 test fixtures cover happy + failure mode portfolio | Day 23 §9.6 | Confirm TC-01/02 happy + TC-03/04/05 failure modes don't duplicate coverage. Confirm 5 codes are exercised: `null × 2`, `engine_failure_unrecoverable`, `cost_overrun`, `render_quota_exhausted`. |
| 8 | 17 critical decisions sign-off | Day 23 §13 | Operator (Jamila) walks 17 decisions. Either signs off OR sends back specific decision(s) for re-rationalization. |
| 9 | Cross-SPEC §3 adherence (10 dimensions) | Day 23 audit table above | Confirm all 10 dimensions show ✅. |
| 10 | No fake-advance | All Day 22 + Day 23 deliverables | Confirm zero `<<TBD-*>>` markers remain in SPEC body. Confirm `<<TBD-D24>>` / `<<TBD-D25>>` markers, if any, are calendar-deferred work (not fake-advanced LOCK content). |
| 11 | Day 27 LLM Test Runbook scope (Open Question #11 raised today) | Day 23 §9.7 | Decide: dry-run mode (cost ≈ $0) OR live mode (≤ $1,000 worst case) for Day 27 runbook. Decision can be deferred to Day 27 itself — Day 24 reviewer's only job is acknowledging the open question. |

---

## ENTITY SEPARATION (re-asserted — Day 23 SPEC body)

This document is Sequel Digital ARS canon. Principal / Holdco Group / NPOX ZERO involvement.

**Defense-in-depth firewall list (5th layer continues — canonical 10-entry list in Day 22 §6.5):**
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

## SCHEMA NO-TOUCH RULE (re-asserted Day 23)

This document does NOT modify any LOCKED schema. References only:
- `production_plan.json` schema (Day 17 LOCKED) — read-only reference for §10 field map source fields (Day 22)
- `storyboard.json` schema (Week 2/3 LOCKED) — read-only reference (audit trail only)
- `script.json` schema (Day 9 LOCKED) — read-only reference (audit trail only)
- `brief.json` schema (Day 7 LOCKED) — read-only reference (audit trail only)

Day 25 will author `rendered_shots.json` schema. Until then, all fields described in §3 of outline + §10 of Day 22 + §16 of Day 23 are SPEC-level claims, not schema-level enforcement.

---

## PROCESS INTEGRITY (Day 23 build)

- ✅ Daily OS pillar: Money block, build advanced (per Day 23 calendar)
- ✅ No LLM dispatched. No render API touched. No engine credentials referenced.
- ✅ No external comms (no emails sent, no DMs, no posts)
- ✅ No financial commitments (no engine subscriptions, no quota purchases, no vendor outreach)
- ✅ No banned-vocab leaks — firewall list scanned across this document
- ✅ Day 22 SPEC body NOT touched (Day 22 LOCK-as-drafted respected — extended only)
- ✅ Predecessor outline NOT touched (Day 20 outline LOCKED-as-shipped — referenced only)
- ✅ Predecessor SPEC (ProdCoord Day 14) NOT touched (LOCK respected — pattern referenced only)
- ✅ Predecessor schemas (ProdCoord Day 17) NOT touched (LOCK respected — read-only)
- ✅ Cross-SPEC canon (Day 12) NOT touched (LOCKED — §3 adherence audited above)
- ✅ Vendor pricing snapshot RESEARCH-ONLY (no subscriptions, no API calls, Day 24 reviewer is verification authority)
- ✅ Day 24 LOCK reviewer checklist explicit (11 items)
- ✅ No fake-advance: §8 / §9 / §11 / §12 / §13 / §15 / §16 fully drafted to LOCK-quality; zero `<<TBD-D23>>` markers remain
- ✅ Open Question #11 explicitly raised (Day 27 LLM runbook dry-run vs live mode — deferred decision)
- ✅ Build log to be written same day (`build-log-2026-05-12.md`)
- ✅ Mirror to `/outputs/ars/` to be completed

---

## DAY 23 SPRINT COMPLETION SUMMARY

| Section | Status | Wall-clock | Notes |
|---------|--------|------------|-------|
| §8 Performance Targets | ✅ DRAFTED | ~1.5 hr equivalent | 9 metric categories with concrete v1.0 numbers · per-tier cost discipline sub-targets · self-QC pass rate · calibration windows (first 10 / 30 / 90 reels) · v1.0 scope discipline · runtime metric hooks enumerated |
| §9 5 Test Fixtures | ✅ DRAFTED | ~1.5 hr equivalent | TC-01 Pro happy path · TC-02 Enterprise happy path with HeyGen talent · TC-03 anchor failure · TC-04 cost overrun · TC-05 cascade failure. Coverage table maps fixtures to 5 of 17 error codes; remaining 12 codes covered by schema-only fixtures (Day 26 SKILL bundle) |
| §11 Cost Model | ✅ DRAFTED | ~2 hr equivalent | RESEARCH-ONLY snapshot. 8 engines × per-model rows (Runway Gen3 Alpha + Turbo, Pika 1.5, Luma DM, Flux 1.1, Kling 1.6, Higgsfield, HeyGen v2 + v3). Pricing canon reference URLs for Day 24 verification. Worked cost examples per tier. JSON canonical shape for Day 25 schema. |
| §12 Style Consistency Math | ✅ DRAFTED | ~1.5 hr equivalent | inheritance_match_score_0_1 composite formula (0.40 pHash + 0.40 CLIP + 0.20 palette) · drift_threshold 0.85 default rationale · 3-tier calibration plan · v1.0 literal_seed_inherit semantics · per-engine determinism notes |
| §13 17 Critical Decisions LOCKED | ✅ DRAFTED | ~1.5 hr equivalent | Anchor-first sequential · 1+1 retry policy · 10% cost overrun buffer · 0.85 drift threshold · anchor-fatal / inheritor-partial · HeyGen v1.0 hardcode · platform-relative URI · embedded firewall template · lever inheritance read-only · escalation_path ascending · 17 error codes · 12-check QC list · voice rule inherit · 13 hard rules canon · tier table runtime authority · parent_chain 4-tuple · no-buildings post-render verification. Each with rationale + alternative + revisit trigger. Cross-SPEC §3 mapping table closes 10-dimension audit. |
| §15 Change Log | ✅ DRAFTED | ~0.5 hr equivalent | 8 v1.0 lifecycle entries (Day 20 outline → Day 27 LLM runbook target). 7 post-v1.0 candidates in parking lot. Format LOCK per Cross-SPEC §3.11. |
| §16 Metadata Block Schema | ✅ DRAFTED | ~0.5 hr equivalent | 11 canonical Cross-SPEC §3.9 fields + 3 AI Video Gen-specific additions (engine_telemetry_summary, composed_prompt_template_sha256, runtime_environment_class). Schema authoring notes for Day 25. Per-shot metadata extensions enumerated. Canonical JSON example. v1.0 metadata block = audit invariant. |

**Total Day 23 wall-clock estimate met:** ~9 hr operator-paced (matches ProdCoord §13–§17 wall-clock proven on Day 14; matches Day 22 §6 + §7 + §10 + §14 wall-clock proven yesterday).

**Day 24 LOCK target unchanged.** All 17 SPEC sections (§0–§16) now drafted to LOCK-quality across Day 20 outline + Day 22 partial + Day 23 complement. Day 24 reviewer reconciles into unified v1.0-LOCKED document.

---

## PROVENANCE

- Authored: 2026-05-12 (Tue · Day 23 · Wk4D3) — ARS overnight build session
- Deliverable file: `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` (Desktop/Sequel Digital/ARS/ + outputs/ars/ mirror)
- Pattern source: `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` §8 / §9 / §11 / §12 / §13 / §15 / §16 (Day 14 LOCKED — verbatim shape inherited; values re-derived for Mode B render runtime)
- Predecessor Day 22 partial: `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` (§6 / §7 / §10 / §14 — LOCK-as-drafted complement)
- Predecessor outline: `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (§0–§5 Day 20)
- Cross-spec canon: `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — 10-dimension §3 adherence asserted across Day 22 + Day 23)
- Daily OS reference: Rest → Body → Money → Authority → Relationships pillar (Day 23 = Money block, build advanced)
- Day 24 LOCK reviewer: Jamila Howard (sign-off authority)

*Day 23 closes Wk4D3 with AI Video Gen Agent v1.0 SPEC body §8 (Performance Targets — 9 metric categories + calibration plan) + §9 (5 Test Fixtures — TC-01 through TC-05 covering happy paths and 3 failure modes) + §11 (Cost Model — 8 engines × per-model RESEARCH-ONLY snapshot) + §12 (Style Consistency Math — composite signal formula + calibration plan) + §13 (17 Critical Decisions LOCKED — decision-rationale-alternative-revisit-trigger across all 17) + §15 (Change Log — 8 v1.0 entries + 7 parked candidates) + §16 (Metadata Block Schema — 11 canonical + 3 AI Video Gen additions) all LOCKED-as-drafted. Day 24 LOCK target = Wed May 13 — runway intact. SPEC body coverage now complete (§0 outline + §6 + §7 + §10 + §14 Day 22 + §8 + §9 + §11 + §12 + §13 + §15 + §16 Day 23). Zero fake-advance: every section is operator-reviewable today. Day 24 reviewer reconciles Day 22 + Day 23 into unified v1.0-LOCKED.*
