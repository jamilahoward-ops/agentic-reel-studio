# ARS — Style Replication Agent v1.0 SPEC (Body §8 / §9 / §11 / §12 / §13 / §15 / §16 — Day 31 LOCKED-as-drafted)

**Date:** Wed May 20, 2026 (Day 31 of 42 · Wk5D5)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** REMAINING SPEC BODY — §8 (Performance Targets) · §9 (5 Test Fixtures) · §11 (Cost Model per-engine $/shot) · §12 (Style Consistency Math — verbatim inherit from AI Video Gen Day 23 §12) · §13 (15 Critical Decisions LOCKED) · §15 (Change Log + Version History) · §16 (Metadata Block Schema) all drafted to LOCK-quality. **Day 30 sections §6 / §7 / §10 / §14 NOT TOUCHED** — inherited verbatim from `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md`. On Day 32 the two Day-30 + Day-31 partial-SPEC files are reconciled into the single v1.0 LOCK CANDIDATE document. **No LLM dispatched. No render API touched. No engine credentials referenced. No external comms. No financial commitments. No vendor subscriptions purchased.**
**Pattern source:** `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` §8 / §9 / §11 / §12 / §13 / §15 / §16 (Day 23 LOCKED — verbatim structural shape inherited; numerical values re-derived for Style Replication cost class which is roughly 1/8th of AI Video Gen per-reel envelope)
**Predecessor partial:** `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` (Day 30 — §6 / §7 / §10 / §14 LOCKED-as-drafted; this document is the missing complement)
**Predecessor outline:** `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` (§0–§5 SHIPPED Day 29; 15 critical decisions pre-scaffolded — 9 LOCKED-as-drafted Day 29, 2 RESOLVED Day 30, 4 PRELIMINARY operator-amend Day 31)
**Predecessor schemas:** `skills/ai-video-gen-agent/schemas/output.schema.json` (Day 25 LOCKED — read-only reference for Mode B input contract). `skills/production-coord-agent/schemas/output.schema.json` (Day 17 LOCKED — read-only reference for Mode A + Mode C input contracts).
**Cross-spec canon:** `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — §3 adherence re-audited at end of this document). **§3.9 amendment scoped for Day 32 LOCK ceremony** (5-tuple parent_chain extension at Style Replication layer; flagged Day 30, drafted in §16 of this document for Day 32 ratification).

---

## DAY 31 AUTHORING SCOPE

This document completes the Style Replication Agent v1.0 SPEC body. Seven sections are LOCKED-as-drafted today:

- **§8** — Performance Targets (9 metric categories with concrete v1.0 numbers; calibration windows for first 10 / 30 / 90 Mode B+C reels enumerated). Lower volume than AI Video Gen because Mode C hot-path reels are Enterprise-only and rarer in v1.0.
- **§9** — 5 Test Fixtures (TC-01 Mode B Pro happy path · TC-02 Mode C Enterprise happy path · TC-03 anchor_unavailable failure · TC-04 cost_overrun failure · TC-05 style_drift_exceeded failure). Pattern from AI Video Gen Day 23 §9 portfolio; mode coverage rebalanced for Style Replication (Mode C is the high-margin path that justifies the agent's existence and gets its own fixture).
- **§11** — Cost Model per-engine $/shot lookup (RESEARCH-ONLY snapshot — vendor pricing canon verification deferred to Day 32 LOCK CANDIDATE reviewer; 4 engines × per-model rows for style fingerprint extraction + grade pass). Smaller engine surface than AI Video Gen (8 engines) because Style Replication does NOT call render engines for net-new generation in Mode C hot path.
- **§12** — Style Consistency Math (drift_threshold derivation, inheritance_match_score_0_1 algorithm, v1.0 literal_fingerprint_inherit semantics, calibration plan). **Verbatim shape inherited from AI Video Gen Day 23 §12 — zero net-new math.** The two agents share a single mathematical canon for drift / palette / motion-grade tolerance; Style Replication operationalizes it at the brand-aesthetic gate, AI Video Gen operationalizes it at the render gate. Re-deriving identical math twice would create canon drift.
- **§13** — 15 Critical Decisions LOCKED (Day 29 outline pre-enumerated 15 decisions; Day 30 partial 1 RESOLVED 2 [failure mode coverage → 6 codes · 5-tuple parent_chain extension]; today's Day 31 partial 2 RATIFIES 4 PRELIMINARY items at Donna's recommended defaults with explicit operator-amend annotations on each; 9 LOCKED-as-drafted Day 29 items re-validated against Day 30 partial 1 §6 + §7 + §10 + §14 LOCK and any deltas surfaced). **Net: 13 LOCKED + 2 RATIFIED-with-operator-amend-annotation = 15/15 §13 coverage at partial 2 close.**
- **§15** — Change Log + Version History (7 entries from Day 29 outline through Day 37 LOCK target — calendar-shaped, version-tagged, lifecycle-annotated)
- **§16** — Metadata Block Schema (canonical Cross-SPEC §3.9 block + 3 Style Replication-specific additions + **the Cross-SPEC §3.9 amendment language Day 32 LOCK ceremony must ratify** — drafted here for review)

The 6-errorEnvelope-code count LOCKED in Day 30 partial 1 §6.3 is RE-ASSERTED in §13 Decision #11 and §15 v1.0-draft-day-30 entry. Day 32 LOCK CANDIDATE reviewer is the gating reconciliation authority for Day 30 + Day 31 partial reconciliation into v1.0 LOCK CANDIDATE.

---

## §8 — Performance Targets (LOCKED-as-drafted Day 31)

The Style Replication Agent v1.0 ships against the following measurable performance envelope. Targets are calibrated for the **first 30 Mode B + Mode C reels combined** (Lever 3 — every reel reviewed by human via QC Agent). Mode A is excluded from rolling-30 targets at v1.0 because Mode A grade-pass volume is expected to be very low (operator+videographer-driven only, sporadic) — Mode A reels are calibration-informational only.

Lever 2 graduation (after 30) and Lever 1 graduation (after 90) require re-calibration via §12.4 calibration plan and §13 Decision #14 (deferred to post-Day 37 once Style Replication v1.0 is LIVE on first paying Sequel pilot reel).

**Reading rule:** every target below is a v1.0 commit. Day 36 LLM Test Runbook produces the first empirical reading; Day 37 LOCK ceremony locks the target table; the first 5 production Mode B/C reels become the first calibration data points (no Lever transition triggered until volume passes 30). Below-target metrics are calibration signal for v1.1 planning, NOT failure.

### §8.1 The 9 metric categories

| # | Metric | v1.0 Target | Failure threshold | Measurement window | Source field |
|---|--------|------------:|------------------:|-------------------:|--------------|
| 1 | **Schema validity rate** (output validates clean against `output.schema.json`) | 100% | < 99% | Per-reel, rolling 30 | Self-QC Check #8 + #11 + #12; final post-§6 validator |
| 2 | **Firewall catch rate** (entity firewall + banned vocab + no-buildings + tier↔mode — zero leaks reach `successReplicatedShots`) | 100% | ≥ 1 leak | Per-reel, ALL reels | Check #1 + #2; `qc_warnings[]` audit |
| 3 | **Anchor fingerprint resolve rate** (Mode B + C: anchor_id resolves to LOCKED anchor + SHA-256 matches cache + freshness ≤ 90 days) | ≥ 98% | < 92% | Per-reel, rolling 30 | `brand_anchor_reference.anchor_sha256` match + `anchor_locked_date` within 90 days |
| 4 | **Style drift rate** (per-shot `inheritance_match_score_0_1` < `drift_threshold` 0.85 across inheritor shots) | ≤ 12% per reel | > 20% per reel | Per-shot, rolling 30 | `replicated_shots[*].inheritance_match_score_0_1` |
| 5 | **Grade-pass success rate by engine** (per-engine: completed / dispatched) | ≥ 90% per engine; ≥ 96% portfolio-weighted | < 82% any engine; < 90% portfolio | Per-engine, rolling 30 | `replication_telemetry.per_engine_*`; `retry_log[*]` |
| 6 | **Budget variance distribution** (actual / estimate) | 0.92 ≤ ratio ≤ 1.08 for ≥ 85% of reels; HARD ceiling ratio ≤ 1.10 | ratio > 1.10 (any reel) OR < 0.85 for > 30% of reels (under-estimating upstream) | Per-reel, ALL reels | `replication_telemetry.budget_variance_pct` |
| 7 | **Wall-clock latency** (Pro tier p50 / p95; Enterprise tier p50 / p95) | Pro p50 ≤ 4 min · p95 ≤ 8 min · Enterprise p50 ≤ 7 min · p95 ≤ 14 min | Pro p95 > 12 min OR Enterprise p95 > 20 min | Per-reel, rolling 30 | `replication_telemetry.total_wall_clock_minutes` |
| 8 | **Retry rate** (`retry_count_total / total_shots`) | ≤ 0.15 (Pro) · ≤ 0.20 (Enterprise) | > 0.30 (Pro) · > 0.35 (Enterprise) | Per-reel, rolling 30 | `replication_telemetry.retry_count_total` ÷ `total_shots` |
| 9 | **Mode C coverage envelope match rate** (Mode C reels where new prompts stay within anchor coverage envelope — does NOT fall back to Mode B) | ≥ 75% | < 50% | Per-reel, rolling 30 (Mode C only) | `metadata.mode_c_coverage_match_bool` |

**Comparison to AI Video Gen §8 numbers (sanity check):**

| Metric class | AI Video Gen Day 23 §8.1 | Style Replication Day 31 §8.1 | Delta rationale |
|--------------|--------------------------|--------------------------------|------------------|
| Schema validity rate | 100% / <99% | 100% / <99% | Identical (no agent-specific reason to drift) |
| Firewall catch rate | 100% / ≥1 leak | 100% / ≥1 leak | Identical (firewall is brand-safety canon, not agent-specific) |
| Anchor success | ≥92% / <85% (anchor RENDER) | ≥98% / <92% (anchor FINGERPRINT RESOLVE) | Higher target because fingerprint resolve is a cache lookup, not a render — should fail less frequently than a render |
| Style drift | ≤15% / >25% | ≤12% / >20% | Stricter because Style Replication's economic justification IS drift prevention; if Style Replication can't beat AI Video Gen's inherent drift rate, the agent has no reason to exist |
| Per-engine success | ≥88% / <80% | ≥90% / <82% | Slightly stricter because Style Replication engines (Pika Style Tokens / Runway Style Reference) are operating at lower cost & lower task complexity than render engines |
| Budget variance | ≤1.10 / >1.10 ceiling | ≤1.10 / >1.10 ceiling | Identical ceiling (variance discipline is canon, not agent-specific) |
| Latency Pro p95 | ≤18 min / >25 min | ≤8 min / >12 min | Much faster because Style Replication doesn't generate net-new video — grade pass + inherit only |
| Retry rate Pro | ≤0.20 / >0.40 | ≤0.15 / >0.30 | Stricter because retry on a grade pass is cheaper than a re-render, so we should retry less aggressively to avoid runaway cost in Lever 3 |
| Mode C coverage match | N/A | ≥75% / <50% | NEW metric — measures whether Mode C hot path is doing its margin-justifying job |

### §8.2 Per-tier cost discipline (sub-targets of §8.1 #6)

| Tier | Average actual cost ÷ ceiling | Target | Failure threshold |
|------|------------------------------:|-------:|------------------:|
| Pro ($50 ceiling — Mode B only) | Mean over rolling 30 reels | 0.40 ≤ mean ≤ 0.80 | mean > 0.95 (squeezing ceiling) OR mean < 0.30 (over-engineered estimate) |
| Enterprise ($120 ceiling — Mode A + B + C) | Mean over rolling 30 reels | 0.40 ≤ mean ≤ 0.80 | mean > 0.95 OR mean < 0.30 |

**Rationale:** ceiling utilization in the 40–80% band proves the cost model is well-calibrated for a lower-cost-class agent. Wider band than AI Video Gen's 55–85% because Style Replication has more variance source (Mode C cache hit vs. Mode B inherit have very different cost profiles — Mode C ~$15–$30/reel, Mode B ~$25–$45/reel; ceiling spans both paths). Above 95% utilization means we're routinely flirting with `cost_overrun` — re-bid the engine assignment heuristic. Below 30% means we're systematically over-estimating — operator margin is fine but ProdCoord's `total_replication_cost_usd_estimated` model needs tightening (v1.1+ ProdCoord retro).

### §8.3 Self-QC pass rate

| Metric | Target | Failure threshold |
|--------|-------:|------------------:|
| First-attempt pass rate (all 12 checks PASS on first run, no regenerate) | ≥ 88% | < 75% |
| Two-attempt pass rate (regenerate-and-pass within Rule #13's 2-strike ceiling) | ≥ 98% | < 94% |
| Final fail rate (errorEnvelope emitted with `attempts: 2`) | ≤ 2% | > 6% |

**Stricter than AI Video Gen §8.3 (85% / 97% / 3%)** because Style Replication's 12-check QC list is built around lookup + comparison checks, not generative checks — lookups should pass more reliably than generative validations.

### §8.4 Calibration windows

Performance targets above are v1.0 commits with the following calibration rule:

- **First 10 Mode B + C reels (Day 37+ onward):** ANY single target miss is informational only — calibration data, not failure. Operator reviews telemetry, no v1.1 trigger.
- **First 30 reels (Lever 2 graduation gate):** Aggregated 30-reel rolling window evaluated. Any metric ≥ "Failure threshold" column = blocking Lever 2 graduation. Operator re-tunes engine assignment heuristic OR cost ceiling buffer OR drift threshold (per §12.4).
- **First 90 reels (Lever 1 graduation gate):** Aggregated 90-reel rolling window. Both Lever 2 metrics held + lower-volatility verification (each metric stable within ±10% across last 30) = Lever 1 eligible. Per Orchestration Blueprint §6 lever framework.

**Mode A reels** are excluded from rolling-30 targets at v1.0 (volume too low for statistical reading); aggregated as a separate Mode A cohort, target review at v1.0.1.

### §8.5 What is intentionally NOT in §8 (v1.0 scope discipline)

The following are deferred to v1.1+ and explicitly out-of-scope for v1.0 performance targets:

- Per-engine quality bias profiling (Pika Style Tokens vs Runway Style Reference comparative bake-off — v1.1+ once volume justifies)
- Cross-reel anchor consistency (does Reel #7's Style Replication output visually echo Reel #6 from same anchor?) — Loop Agent (post-Week 6) territory + post-v1.0 calibration item
- Brand-aesthetic operator satisfaction score (NPS-style human rating of grade-pass output) — Sequel Digital sales feedback layer, not agent telemetry
- Multi-pass grade refinement bake-off (single-stage vs. 2-stage refinement) — v1.1+ Enterprise creative-tier feature
- Anchor cache hit-rate optimization (LRU eviction, anchor version pinning) — v1.1+ infra layer

### §8.6 Performance target measurement source — runtime hooks

Per Cross-SPEC §3.9 metadata block, every reel emits the following metric-hook fields that §8 dashboard (per Day 30 retro + Week 6 commercial launch deliverable) aggregates:

```
replication_telemetry.total_replication_seconds_actual
replication_telemetry.total_replication_cost_usd_actual
replication_telemetry.budget_variance_pct
replication_telemetry.per_engine_cost_usd[*]
replication_telemetry.retry_count_total
replication_telemetry.failure_count_total
replication_telemetry.total_wall_clock_minutes
replicated_shots[*].inheritance_match_score_0_1
replicated_shots[*].grade_pass_status
brand_anchor_reference.anchor_sha256 (resolution success)
brand_anchor_reference.anchor_locked_date (freshness)
metadata.self_qc_attempts (1 or 2)
metadata.self_qc_failed_check_id (null on success, 1..12 on failure)
metadata.mode_c_coverage_match_bool (Mode C reels only)
metadata.production_mode ("A" | "B" | "C")
```

These hooks are the contract surface between Style Replication v1.0 and the §8 dashboard. Adding metrics in v1.0.x patches requires adding fields here; backward-compat preserved via optional-field discipline (Cross-SPEC §3.4 canon).

---

## §9 — Test Fixtures (LOCKED-as-drafted Day 31)

Five test fixtures form the validation portfolio for Style Replication v1.0. Pattern source: AI Video Gen Day 23 §9 (5 fixtures TC-01..TC-05). Coverage rebalanced for Style Replication:

- **TC-01** — Mode B Pro happy path (inherit + grade pass) — the dominant volume path
- **TC-02** — Mode C Enterprise happy path (hot path / cache hit) — the margin-justifying path
- **TC-03** — Mode C anchor_unavailable failure (cache miss → errorEnvelope)
- **TC-04** — Mode B Enterprise cost_overrun failure (engine cascade pushes past $120 ceiling)
- **TC-05** — Mode B Pro style_drift_exceeded failure (inheritor shot fingerprint falls below 0.85 drift threshold after engine grade pass)

Mode A is intentionally NOT covered by a v1.0 fixture — Mode A volume is too low to justify dedicated fixture authoring at v1.0; a Mode A fixture is reserved for v1.0.1 (Open Question parked, §13 Decision #14).

The fixture portfolio targets full errorEnvelope code coverage: 4 of 6 codes covered by TC-01..TC-05 (`anchor_unavailable`, `cost_overrun`, `style_drift_exceeded`, `style_replication_agent_failed`); the 2 uncovered (`brand_finish_layer_missing`, `qc_pre_flags_format_violation`) are covered by schema-only fixtures Day 33 schema-authoring session (per Day 30 partial 1 §6.3 narrowing rationale).

### §9.1 TC-01 — Mode B Pro happy path (inherit + grade pass)

**Scenario:** AI Video Gen has just emitted a `successRenderedShots` payload for a 5-shot REINVENTED reel at Pro tier ($400 AI Video Gen ceiling well-utilized at $312 actual). All 5 shots rendered successfully. Anchor shot is `shot-001` (Operator close-up at iMac, golden hour). Style Replication is invoked to apply brand finish layer + verify inheritance_match across the 4 inheritor shots.

**Input fixture file:** `fixtures/TC-01-mode-b-pro-happy-path-input.json`

```json
{
  "production_mode": "B",
  "tier": "pro",
  "rendered_shots": [
    { "shot_id": "shot-001", "render_status": "completed", "asset_uri": "ars://renders/REINVENTED/sess-2026-05-26/shot-001.mp4", "negative_prompt_sha256": "abc123...", "shot_intent": "anchor" },
    { "shot_id": "shot-002", "render_status": "completed", "asset_uri": "ars://renders/REINVENTED/sess-2026-05-26/shot-002.mp4", "negative_prompt_sha256": "abc123...", "shot_intent": "supporting" },
    { "shot_id": "shot-003", "render_status": "completed", "asset_uri": "ars://renders/REINVENTED/sess-2026-05-26/shot-003.mp4", "negative_prompt_sha256": "abc123...", "shot_intent": "supporting" },
    { "shot_id": "shot-004", "render_status": "completed", "asset_uri": "ars://renders/REINVENTED/sess-2026-05-26/shot-004.mp4", "negative_prompt_sha256": "abc123...", "shot_intent": "supporting" },
    { "shot_id": "shot-005", "render_status": "completed", "asset_uri": "ars://renders/REINVENTED/sess-2026-05-26/shot-005.mp4", "negative_prompt_sha256": "abc123...", "shot_intent": "supporting" }
  ],
  "anchor_shot_id": "shot-001",
  "brand_anchor_reference": {
    "anchor_id": "anchor-REINVENTED-v2-locked-2026-05-15",
    "anchor_uri": "ars://brand_anchor_cache/REINVENTED/anchor-REINVENTED-v2-locked-2026-05-15.json",
    "anchor_locked_date": "2026-05-15",
    "anchor_sha256": "def456..."
  },
  "metadata": {
    "agent_id": "style-replication-agent-v1.0",
    "production_mode": "B",
    "tier": "pro",
    "parent_chain": ["brief-001", "script-001", "storyboard-001", "production_plan-001", "ai-video-gen-001"],
    "lever_state": "lever-3",
    "session_id": "sess-2026-05-26-reinvented-pro-01"
  }
}
```

**Expected output (success path):** `successReplicatedShots` branch.

**Key invariants exercised:**
- 5-tuple parent_chain inherits + extends to 6-tuple (5 from input + this agent's `replication_set_id`)
- `inheritance_match_score_0_1` ≥ 0.85 for all 4 inheritor shots
- Per-engine retries 0 (single-pass Pika Style Tokens grade pass succeeds first-try)
- `replication_telemetry.total_replication_cost_usd_actual` ~ $28–$35 (well within $50 Pro ceiling)
- All 12 self-QC checks PASS first attempt

**Validation matrix (against §6 12-check list):**

| Check # | Status | Notes |
|--------:|--------|-------|
| 1 — entity firewall | PASS | No banned vocab in any output field |
| 2 — no buildings | PASS | Anchor + inheritors all human-subject framed |
| 3 — tier↔mode firewall | PASS | Pro tier + Mode B = allowed |
| 4 — anchor_id resolves | PASS | Cache hit + SHA-256 match + freshness 11 days |
| 5 — anchor render status | PASS | shot-001 has `render_status == "completed"` |
| 6 — drift score (tri-state) | PASS | All 4 inheritor shots ≥ 0.85 inheritance_match |
| 7 — brand finish layer | PASS | REINVENTED v2 brand finish applied to all 5 shots |
| 8 — schema partial validation | PASS | Mid-process validator passes |
| 9 — cost projection | PASS | Estimated $32 + actual $28 — variance 0.875 within band |
| 10 — negative_prompt_sha256 invariant | PASS | Single hash across all 5 input shots verified |
| 11 — slot 11 reserved | PASS | `style_replication_agent_failed` slot reserved per §3.6 canon |
| 12 — final schema validation | PASS | Output validates clean against `output.schema.json` |

### §9.2 TC-02 — Mode C Enterprise happy path (hot path / cache hit)

**Scenario:** Enterprise client (REINVENTED) has 3 new reels queued. Each reel uses Mode C hot path against the LOCKED `anchor-REINVENTED-v2-locked-2026-05-15` anchor. AI Video Gen is NOT invoked — Style Replication consumes the anchor cache directly and produces grade-pass output on top of 3 new shot prompts that stay within the anchor's coverage envelope.

**Input fixture file:** `fixtures/TC-02-mode-c-enterprise-happy-path-input.json`

```json
{
  "production_mode": "C",
  "tier": "enterprise",
  "production_plan": {
    "mode_c_plan": {
      "new_shot_prompts": [
        { "shot_id": "shot-001", "prompt_text": "Operator close-up at iMac, golden hour, brand-anchor inherited, 9:16 vertical", "shot_intent": "hero" },
        { "shot_id": "shot-002", "prompt_text": "Hands-on-keyboard medium shot, golden hour, brand-anchor inherited, 9:16 vertical", "shot_intent": "supporting" },
        { "shot_id": "shot-003", "prompt_text": "iMac screen detail with subtle motion, golden hour, brand-anchor inherited, 9:16 vertical", "shot_intent": "detail" }
      ]
    }
  },
  "brand_anchor_reference": {
    "anchor_id": "anchor-REINVENTED-v2-locked-2026-05-15",
    "anchor_uri": "ars://brand_anchor_cache/REINVENTED/anchor-REINVENTED-v2-locked-2026-05-15.json",
    "anchor_locked_date": "2026-05-15",
    "anchor_sha256": "def456..."
  },
  "metadata": {
    "agent_id": "style-replication-agent-v1.0",
    "production_mode": "C",
    "tier": "enterprise",
    "parent_chain": ["brief-002", "script-002", "storyboard-002", "production_plan-002", "mode-c-direct"],
    "lever_state": "lever-3",
    "session_id": "sess-2026-05-27-reinvented-enterprise-01"
  }
}
```

**Expected output (success path):** `successReplicatedShots` branch.

**Key invariants exercised:**
- Mode C `production_mode == "C"` AND `mode_c_plan != null` AND tier `enterprise` (all three required, all three present)
- Coverage envelope check PASSES (all 3 prompts stay within "operator + iMac + golden hour" envelope of the anchor)
- `replication_telemetry.total_replication_cost_usd_actual` ~ $45–$70 (well within $120 Enterprise ceiling — Mode C is highest-margin path)
- `metadata.mode_c_coverage_match_bool == true`
- 5-tuple parent_chain extension: `["brief-002", "script-002", "storyboard-002", "production_plan-002", "mode-c-direct"]` extends to 6-tuple with this agent's `replication_set_id` appended

**Margin demonstration (the reason Mode C exists):**

| Cost component | Mode B equivalent | Mode C (this fixture) | Delta |
|----------------|------------------:|----------------------:|------:|
| AI Video Gen (render) | $612 (Enterprise §9 TC-02 from AI Video Gen Day 23) | $0 (skipped) | -$612 |
| Style Replication | $80 | $55 | -$25 |
| **Total per reel** | **$692** | **$55** | **-$637 (-92%)** |

At Enterprise tier Enterprise-tier/mo retainer (per Day 6 pricing canon), 1 Mode C reel saves $637 in production cost vs. 1 Mode B reel — directly contributing to Sequel Digital gross margin. Mode C is the **most economically important fixture in the v1.0 portfolio.**

### §9.3 TC-03 — Mode C anchor_unavailable failure

**Scenario:** Enterprise client requests a Mode C reel but the requested `anchor_id` does not exist in `brand_anchor_cache/` (e.g., anchor was rotated to v3 LOCKED 2026-05-19 and v2 was deprecated; the client's ProdCoord output still references v2). Style Replication detects cache miss → `anchor_unavailable` errorEnvelope.

**Input fixture file:** `fixtures/TC-03-mode-c-anchor-unavailable-input.json`

```json
{
  "production_mode": "C",
  "tier": "enterprise",
  "production_plan": { "mode_c_plan": { "new_shot_prompts": [ { "shot_id": "shot-001", "prompt_text": "...", "shot_intent": "hero" } ] } },
  "brand_anchor_reference": {
    "anchor_id": "anchor-REINVENTED-v2-DEPRECATED-2026-05-15",
    "anchor_uri": "ars://brand_anchor_cache/REINVENTED/anchor-REINVENTED-v2-DEPRECATED-2026-05-15.json",
    "anchor_locked_date": "2026-05-15",
    "anchor_sha256": "old-hash-..."
  },
  "metadata": { "production_mode": "C", "tier": "enterprise", "parent_chain": ["brief-003", "script-003", "storyboard-003", "production_plan-003", "mode-c-direct"], "lever_state": "lever-3", "session_id": "sess-2026-05-28-reinvented-enterprise-02" }
}
```

**Expected output (failure path):**

```json
{
  "errorEnvelope": {
    "agent_id": "style-replication-agent-v1.0",
    "error_code": "anchor_unavailable",
    "error_message": "Anchor 'anchor-REINVENTED-v2-DEPRECATED-2026-05-15' not found in brand_anchor_cache/ — current LOCKED anchor for REINVENTED is 'anchor-REINVENTED-v3-locked-2026-05-19'. Update production_plan or escalate to operator.",
    "error_context": {
      "requested_anchor_id": "anchor-REINVENTED-v2-DEPRECATED-2026-05-15",
      "available_locked_anchor_ids_for_brand": ["anchor-REINVENTED-v3-locked-2026-05-19"],
      "brand_id": "REINVENTED",
      "production_mode": "C"
    },
    "human_review_required": false,
    "retry_recommended": false,
    "recovery_path": "Update upstream production_plan with current LOCKED anchor_id, OR fall back to Mode B by invoking AI Video Gen first",
    "attempts": 1,
    "metadata": { /* full metadata block */ }
  }
}
```

**Key invariants exercised:**
- errorEnvelope shape per Cross-SPEC §3.3 canon
- `error_code` is one of the 6 LOCKED codes (slot 11 reserved `style_replication_agent_failed` NOT used here — that's the agent-internal failure slot; cache miss is a legitimate input-failure code)
- `human_review_required: false` (cache miss is a deterministic input error; no human judgment needed)
- `retry_recommended: false` (retrying the same cache lookup will fail identically)
- `attempts: 1` (no self-regenerate attempted — cache miss is hard fail per Rule #13)
- 5-tuple parent_chain preserved in errorEnvelope metadata

### §9.4 TC-04 — Mode B Enterprise cost_overrun failure

**Scenario:** Enterprise client Mode B reel with 8 inheritor shots (above typical 4-shot envelope). Initial cost projection $95 estimated. During grade pass, 3 shots require fallback engine activation (Pika Style Tokens → Runway Style Reference cascade) at higher per-shot cost. Cumulative actual cost projection reaches $128 mid-process → exceeds $120 Enterprise ceiling → halt with `cost_overrun` errorEnvelope before completing the last 2 shots.

**Input fixture file:** `fixtures/TC-04-mode-b-enterprise-cost-overrun-input.json`

```json
{
  "production_mode": "B",
  "tier": "enterprise",
  "rendered_shots": [ /* 8 shots, all render_status completed */ ],
  "anchor_shot_id": "shot-001",
  "brand_anchor_reference": { "anchor_id": "anchor-REINVENTED-v3-locked-2026-05-19", "anchor_sha256": "...", "anchor_locked_date": "2026-05-19", "anchor_uri": "..." },
  "metadata": { "production_mode": "B", "tier": "enterprise", "parent_chain": ["brief-004", "script-004", "storyboard-004", "production_plan-004", "ai-video-gen-004"], "lever_state": "lever-3", "session_id": "sess-2026-05-29-reinvented-enterprise-03" }
}
```

**Expected output (failure path):**

```json
{
  "errorEnvelope": {
    "agent_id": "style-replication-agent-v1.0",
    "error_code": "cost_overrun",
    "error_message": "Per-reel cost ceiling exceeded: $128.40 projected actual vs. $120.00 Enterprise ceiling. Halted after 6 of 8 shots processed.",
    "error_context": {
      "tier": "enterprise",
      "ceiling_usd": 120.00,
      "projected_actual_usd": 128.40,
      "shots_processed": 6,
      "shots_remaining": 2,
      "fallback_activations": [{"shot_id": "shot-003", "primary_engine": "pika-style-tokens", "fallback_engine": "runway-style-reference", "additional_cost_usd": 0.18}, {"shot_id": "shot-005", "primary_engine": "pika-style-tokens", "fallback_engine": "runway-style-reference", "additional_cost_usd": 0.22}, {"shot_id": "shot-006", "primary_engine": "pika-style-tokens", "fallback_engine": "runway-style-reference", "additional_cost_usd": 0.19}]
    },
    "human_review_required": true,
    "retry_recommended": true,
    "recovery_path": "Operator decision required: (a) approve $128.40 overrun this reel (one-time Lever-3 override · log to v1.0.1 calibration set), (b) reduce shot count to 6 + accept partial reel, (c) re-bid via Mode A live shoot, or (d) defer reel and re-author ProdCoord output with tighter shot budget.",
    "attempts": 1,
    "metadata": { /* full metadata block */ }
  }
}
```

**Key invariants exercised:**
- Cost ceiling enforcement gates output BEFORE completion (Rule #6 hard ceiling)
- `human_review_required: true` (Lever-3 default for cost decisions)
- `retry_recommended: true` (with operator-supplied recovery path)
- Telemetry preservation: `error_context.fallback_activations[]` enables Day 30 retro analysis of which engines triggered the cascade

### §9.5 TC-05 — Mode B Pro style_drift_exceeded failure

**Scenario:** Pro tier Mode B reel with 5 inheritor shots. Style Replication completes grade pass on all 5 shots, but `inheritance_match_score_0_1` for shot-003 returns 0.78 (below 0.85 drift threshold). First-attempt fail on Check #6 (tri-state: PASS / WARN / FAIL). Per §13 Decision #6 (Day 30 LOCKED), drift threshold violations route to: (a) auto-regenerate the affected shot's grade pass with stricter engine constraints, (b) if still fails, route to human review via Lever-3 `human_review_required: true`. This fixture exercises the "regenerate-then-still-fail" path.

**Input fixture file:** `fixtures/TC-05-mode-b-pro-style-drift-exceeded-input.json`

**Expected output (failure path after 2 attempts):**

```json
{
  "errorEnvelope": {
    "agent_id": "style-replication-agent-v1.0",
    "error_code": "style_drift_exceeded",
    "error_message": "Inheritor shot 'shot-003' drift score 0.78 below threshold 0.85 after 2 regenerate attempts. Halting per Rule #13 2-strike ceiling.",
    "error_context": {
      "tier": "pro",
      "anchor_shot_id": "shot-001",
      "drift_threshold": 0.85,
      "failing_shot_id": "shot-003",
      "drift_scores_by_attempt": [{"attempt": 1, "inheritance_match_score_0_1": 0.78, "engine": "pika-style-tokens"}, {"attempt": 2, "inheritance_match_score_0_1": 0.81, "engine": "runway-style-reference"}],
      "successful_shots": ["shot-001", "shot-002", "shot-004", "shot-005"]
    },
    "human_review_required": true,
    "retry_recommended": false,
    "recovery_path": "Operator review required: (a) approve as-is at 0.81 drift score (one-time override · log to v1.0.1 calibration set + tighten drift threshold for this brand), (b) drop shot-003 from reel and ship 4-shot final, (c) re-render shot-003 upstream via AI Video Gen with brand-anchor-explicit prompt (upgrade reel to higher cost path).",
    "attempts": 2,
    "metadata": { /* full metadata block · self_qc_attempts: 2 · self_qc_failed_check_id: 6 */ }
  }
}
```

**Key invariants exercised:**
- Tri-state Check #6 (PASS / WARN / FAIL) — this fixture exercises FAIL path twice
- Rule #13 2-strike ceiling enforced
- `attempts: 2` (max) + `self_qc_failed_check_id: 6` (drift)
- Partial work preserved in `error_context.successful_shots[]` (4 of 5 shots completed cleanly — operator can recover the reel without re-running 4 successful shots)
- 5-tuple parent_chain preserved

### §9.6 Fixture validation gate (Day 36 LLM Test Runbook trigger)

All 5 fixtures must validate clean against the Day 33 `input.schema.json` AND produce expected output branches when run through the Day 34 SKILL bundle. **Failure criterion:** Any fixture producing an output branch other than its expected branch → v1.0 LOCK ceremony (Day 37) is BLOCKED until SPEC or schema or SKILL is patched.

Run mode at Day 36 LLM Test Runbook: **dry-run by default** (cost ~$3 Opus tokens for SPEC + fixtures load + 5 attempts). Live mode (with actual engine calls) is v1.0.1 reservation per AI Video Gen Day 27 LLM Test Runbook canon precedent.

---

## §11 — Cost Model per-engine $/shot snapshot (LOCKED-as-drafted Day 31)

This section is **RESEARCH-ONLY** at Day 31 authoring. Vendor pricing snapshot canon will be verified by Day 32 LOCK CANDIDATE reviewer (Item #6 on the 11-item reviewer checklist — same as AI Video Gen Day 24 reviewer checklist Item #6 pattern). Numbers below are Donna's best-effort May 2026 snapshot from public pricing pages; operator should spot-check 2 random engine rows during Day 32 sit-down.

**Engine surface smaller than AI Video Gen §11:** AI Video Gen tracked 8 render engines (Runway / Pika / Kling / Hailuo / Sora / Luma / Vidu / Hedra). Style Replication tracks 4 engines because the cost class is fundamentally different — no net-new generation, only style transfer + fingerprint compute + grade pass.

### §11.1 Style Replication engine cost table v1.0 (snapshot May 2026)

| Engine | Function | Cost per shot | Latency p50 / p95 | v1.0 role | Notes |
|--------|----------|--------------:|------------------:|-----------|-------|
| **Pika Style Tokens** | Style transfer / grade pass | $0.08–$0.18 / shot | 12 sec / 28 sec | **PRIMARY** (Mode A + B + C grade pass) | Lowest cost per Donna's §13 Decision #5 recommendation; supports token-based brand-anchor injection |
| **Runway Style Reference** | Style transfer / grade pass (fallback) | $0.15–$0.32 / shot | 18 sec / 38 sec | **FALLBACK** (when Pika first-pass drift > 0.85 threshold) | Higher quality on motion-heavy shots; ~2× cost of Pika |
| **CLIP + pHash native** | Fingerprint extraction (read-only) | $0.001 / shot | <2 sec | Required for all 3 modes | Native compute, no external API; embedded in SKILL bundle |
| **Palette extraction** (native k-means + LAB color space) | Palette-delta scoring | $0.0005 / shot | <1 sec | Required for §12 drift math Check #6 | Native compute, no external API |

**Cost ceiling reconciliation:** Pro $50 / Enterprise $120 ceilings (Day 6 pricing canon · §13 Decision #2 LOCKED Day 31 with operator-amend annotation) cover the following typical envelopes:

| Tier × Mode | Typical shot count | Typical cost | Ceiling utilization | Notes |
|-------------|-------------------:|-------------:|---------------------:|-------|
| Pro × Mode B (5 shots, 4 inheritors) | 5 | ~$15 + Pika 4 × $0.13 + extraction 5 × $0.0015 = **~$16** | 32% of $50 | Comfortable headroom |
| Enterprise × Mode B (8 shots, 7 inheritors) | 8 | ~$25 + Pika 7 × $0.13 + extraction 8 × $0.0015 = **~$26** | 22% of $120 | Comfortable headroom |
| Enterprise × Mode C (5 shots, 5 fresh prompts) | 5 | ~$20 + Pika 5 × $0.13 + extraction 5 × $0.0015 = **~$21** | 18% of $120 | Highest-margin path — large headroom for retry/fallback |
| Enterprise × Mode B + fallback cascade (8 shots, 3 fallback) | 8 | ~$26 base + (3 × $0.24 Runway delta) = **~$33** | 28% of $120 | Still comfortable; TC-04 cost_overrun fixture exercises a more pathological 6-fallback case |
| Enterprise × Mode B + edge case (12 shots — beyond v1.0 typical envelope) | 12 | ~$40 base + worst-case 6 fallback = **~$60** | 50% of $120 | Still well under ceiling but flag for v1.1 ceiling review |

**Why these ceilings are comfortable:** AI Video Gen §11 cost projections were tight against ceilings (60–85% utilization typical) because render-engine $/sec is the dominant cost driver. Style Replication operates at 18–50% ceiling utilization in typical cases because grade-pass + fingerprint compute is structurally cheaper than render. This headroom is **intentional** — it absorbs vendor price hikes, fallback cascades, and v1.0.1 Mode A volume without requiring tier-ceiling re-bid.

### §11.2 Cost discipline rules (LOCKED Day 31)

1. **Hard ceiling enforcement:** any projected actual `total_replication_cost_usd_actual` ≥ tier ceiling → halt with `cost_overrun` errorEnvelope (TC-04 exercises this).
2. **Soft warning threshold:** projected actual ≥ 0.85 × ceiling → emit `qc_warning` "approaching cost ceiling" but proceed; surfaces in Day 30 retro telemetry.
3. **Per-shot ceiling deferred to v1.1+:** per Day 29 outline §1 in-scope/deferred matrix. v1.0 enforces per-reel envelope only.
4. **Mode A grade-pass cost cap:** $4 per user-clip shot (Mode A typically 1–3 shots so envelope is well within $50 Pro / $120 Enterprise ceiling). Hardcoded in §7 system prompt Rule #11.
5. **Fallback engine activation cost-tracked:** every fallback to Runway from Pika logs `additional_cost_usd` to telemetry — feeds Day 30 retro analysis and §8.1 metric #9 (fallback activation rate ≤ 8%).

### §11.3 Pricing canon verification protocol (Day 32 LOCK CANDIDATE reviewer)

Day 32 LOCK CANDIDATE reviewer Item #6 (mirror of AI Video Gen Day 24 reviewer Item #6):

> "Spot-check 2 random engine rows in §11.1 cost table against current vendor pricing pages. If both match within ±15% of snapshot value, ratify §11.1 LOCK. If either drifts >15%, patch the row, re-spot-check 1 more row, then ratify."

**Pricing canon expiration:** §11.1 snapshot expires Day 60 of v1.0 lifecycle (Day 60 since LOCK = roughly mid-July 2026 if LOCK lands Day 37 = May 26). At Day 60, operator runs a refresh sweep — patch row deltas, re-ratify. v1.0.1 release if any row delta > 25%.

### §11.4 What is intentionally NOT in §11

- Multi-vendor cost arbitrage (algorithmic engine selection across Pika + Runway based on real-time price signals) — v1.1+ feature, far out of v1.0 scope
- Per-brand cost benchmarking (REINVENTED's average $/reel vs. Sequel client averages) — Loop Agent + Analytics layer, post-Week 6
- Cost forecasting beyond per-reel scope — Day 60 Sequel commercial pricing tier review territory

---

## §12 — Style Consistency Math (LOCKED-as-drafted Day 31 — VERBATIM INHERIT)

**This section is a verbatim inheritance from AI Video Gen Day 23 §12.** The two agents share a single mathematical canon for drift / palette / motion-grade tolerance. Re-deriving identical math twice would create canon drift; instead, Style Replication operationalizes the AI Video Gen §12 math at the brand-aesthetic gate.

### §12.1 Inheritance match score — algorithm (UNCHANGED FROM AI VIDEO GEN)

The `inheritance_match_score_0_1` is a composite score in [0.0, 1.0] computed per-inheritor-shot against the anchor shot. Components:

```
inheritance_match_score_0_1 =
  (0.40 × clip_cosine_similarity) +
  (0.30 × phash_hamming_proximity) +
  (0.20 × palette_delta_normalized) +
  (0.10 × motion_grade_delta_normalized)
```

Where:

- **`clip_cosine_similarity`** ∈ [0, 1] — CLIP ViT-L/14 embedding cosine similarity between anchor frame (mid-frame) and inheritor frame (mid-frame). Higher = more semantically similar.
- **`phash_hamming_proximity`** ∈ [0, 1] — Perceptual hash Hamming distance normalized to [0, 1] (closer = higher; 0 = identical, 1 = pure entropy). Anchor pHash 64-bit; inheritor pHash 64-bit; distance ÷ 64 normalized to [0, 1] then inverted.
- **`palette_delta_normalized`** ∈ [0, 1] — k-means (k=5) palette extracted in LAB color space; CIEDE2000 ΔE distance between centroid pairs (best-matched 5-pair assignment); normalized to [0, 1] by dividing by ΔE=15 ceiling.
- **`motion_grade_delta_normalized`** ∈ [0, 1] — Per-frame contrast + saturation + LUT-bias delta between anchor and inheritor; normalized to [0, 1] by clipping to ±20% range.

### §12.2 Drift threshold v1.0 (LOCKED — UNCHANGED FROM AI VIDEO GEN)

**`drift_threshold = 0.85`** — inherited verbatim from AI Video Gen Day 23 §12.2. Any inheritor shot with `inheritance_match_score_0_1 < 0.85` triggers Check #6 FAIL state (or WARN if 0.85 ≤ score < 0.90, which is the WARN band — Lever-3 routes WARN to human review per §13 Decision #6).

**Why 0.85 (not 0.90 or 0.80):**
- 0.90 too strict — empirical analysis from AI Video Gen test fixtures showed cross-engine drift typically lands 0.86–0.94 for well-anchored inheritor shots; a 0.90 threshold would FAIL 30%+ of legitimate inheritor shots.
- 0.80 too loose — accepts shots a human eye would flag as visually inconsistent with anchor.
- 0.85 is the calibration mid-point; first 30 reels worth of telemetry (post-Day 37 LOCK) feeds re-calibration if the empirical distribution drifts.

### §12.3 literal_fingerprint_inherit semantics (LOCKED — Style Replication variant of AI Video Gen `literal_seed_inherit`)

AI Video Gen §12.3 introduced `literal_seed_inherit` semantics (per-engine random-seed pass-through to ensure regenerate calls produce visually consistent output). Style Replication's analog is `literal_fingerprint_inherit`:

```
literal_fingerprint_inherit = {
  "anchor_clip_embedding_uri": "ars://brand_anchor_cache/REINVENTED/anchor-v2-locked-2026-05-15.embeddings.bin",
  "anchor_phash_64bit": "0x4a7b9c2e1f8d6a30",
  "anchor_palette_lab_centroids": [ ... 5 LAB triplets ... ],
  "anchor_motion_grade_baseline": { "contrast_target": 1.12, "saturation_target": 1.08, "lut_id": "REINVENTED-finish-v2-2026-05-15" }
}
```

Every Mode B + C reel emits `literal_fingerprint_inherit` block in metadata so Day 30 retro telemetry can re-validate consistency across reels using the same anchor. Mode A reels emit a partial block (no anchor pHash — Mode A grades against the user-provided source clip's own fingerprint).

### §12.4 Calibration plan (LOCKED — UNCHANGED FROM AI VIDEO GEN)

Drift threshold + component weights (0.40 / 0.30 / 0.20 / 0.10) are v1.0 LOCK values. Re-calibration triggers:

- **Per-brand drift drift:** Any brand's rolling-30 drift rate > 20% per reel for 2 consecutive 30-reel windows → operator re-bids the brand's drift_threshold from 0.85 to 0.80–0.83 (brand-specific override permitted in v1.0.1 via brand_anchor block).
- **Cross-engine bias:** If Pika Style Tokens average drift consistently 0.05+ lower than Runway Style Reference average drift on the same brand → operator considers re-weighting CLIP similarity vs. pHash proximity (currently 0.40 / 0.30 = 0.70 combined; re-weighting deferred to v1.1+).
- **Component blow-up:** Any single component (palette delta, motion grade delta) consistently dominating drift score (>50% of variance) → operator triggers v1.0.1 re-weighting review.

**Calibration cadence:** Day 30 of each 30-reel rolling window post-LOCK. First calibration ~Day 60 of v1.0 lifecycle (~mid-July 2026).

### §12.5 What §12 explicitly inherits vs. re-implements

| Item | Source | This SPEC role |
|------|--------|----------------|
| `inheritance_match_score_0_1` algorithm | AI Video Gen Day 23 §12.1 — IDENTICAL | Read-only canon reference; no re-derivation |
| `drift_threshold = 0.85` value | AI Video Gen Day 23 §12.2 — IDENTICAL | Read-only canon reference; first re-calibration trigger is per §12.4 |
| `literal_seed_inherit` → `literal_fingerprint_inherit` analog | AI Video Gen Day 23 §12.3 — STRUCTURALLY ANALOGOUS, semantically agent-specific | New emission block; sibling of AI Video Gen's literal_seed_inherit |
| Calibration plan | AI Video Gen Day 23 §12.4 — IDENTICAL | Read-only canon reference; calibration cadence shared with AI Video Gen |
| Tri-state Check #6 (PASS / WARN / FAIL) | AI Video Gen Day 22 §6 Check #6 — IDENTICAL structure | Re-asserted in Day 30 partial 1 §6 — already LOCKED |

**Zero net-new math in §12.** This is the deliberate canon-sharing pattern that prevents drift between the two production-tier agents. AI Video Gen §12 + Style Replication §12 are kept in lockstep at every revision.

---

## §13 — Critical Decisions LOCKED (15 of 15 · LOCKED-as-drafted Day 31)

Style Replication SPEC Outline §13 (Day 29) pre-enumerated **15 critical decisions** (parallel to AI Video Gen's 17 — fewer because Style Replication's cost class is narrower + Mode coverage is downstream of AI Video Gen's mode authority). Day 30 partial 1 RESOLVED 2 of 6 PRELIMINARY items. Today's Day 31 partial 2 closes the remaining 4 PRELIMINARY items at Donna's recommended defaults with explicit `[PRELIMINARY · operator amend Day 32 LOCK CANDIDATE]` annotations. **All 15 decisions are LOCK-quality at Day 31 partial 2 close. Day 32 LOCK CANDIDATE reviewer ratifies.**

| # | Decision | Verdict | Rationale | Alternative considered | Revisit trigger |
|---|----------|---------|-----------|------------------------|-----------------|
| 1 | **Three-mode coverage (A + B + C) at v1.0** | LOCKED-as-drafted Day 29 | Mode B + Mode C deliver the bulk of margin justification; Mode A required at v1.0 because operator+videographer-driven reels need a brand grade pass and there is no downstream agent to fill that gap | Mode B + C only (defer A to v1.0.1) — rejected: Mode A reels would have no brand-aesthetic gate, creating brand-consistency liability | Mode A reel count > 10/month sustained, AND grade-pass quality complaints surface |
| 2 | **Per-reel cost ceiling Pro $50 / Enterprise $120** | LOCKED-as-drafted Day 29 · RATIFIED Day 31 `[PRELIMINARY · operator amend Day 32 LOCK CANDIDATE]` | At §11.1 typical envelopes 18–50% ceiling utilization, ceilings are comfortable. Provides absorption buffer for fallback cascades and vendor price hikes without tier re-bid | Pro $35 / Enterprise $80 — rejected: too tight, would force Mode A grade-pass into Enterprise-only despite Pro tier including Mode A. Pro $70 / Enterprise $150 — rejected: too loose, undermines cost discipline signal | First 30 reels post-LOCK telemetry shows mean utilization > 80% OR < 30% per §8.2 |
| 3 | **Drift threshold = 0.85 (inherit from AI Video Gen §12.2)** | LOCKED-as-drafted Day 29 | Canon-sharing with AI Video Gen prevents math drift; 0.85 empirically validated in AI Video Gen Day 23 test fixtures | Brand-specific override at v1.0 — rejected: ships too much config surface at v1.0; deferred to v1.0.1 | Per-brand drift rate > 20% per reel for 2 consecutive 30-reel windows |
| 4 | **Coverage envelope check ON for Mode C** | LOCKED-as-drafted Day 29 | Mode C economic justification depends on staying within the anchor's coverage envelope; out-of-envelope prompts fall back to Mode B | Coverage envelope OFF (let Mode C try any prompt) — rejected: would produce wildly drifted grade-pass output, breaking Mode C's brand-consistency contract | Operator decides to expand Mode C coverage envelope beyond anchor scope (post-v1.0.1 multi-anchor support) |
| 5 | **Style transfer engine v1.0 primary = Pika Style Tokens** | LOCKED Day 31 `[PRELIMINARY · operator amend Day 32 LOCK CANDIDATE]` | Lowest $/shot (Pika ~$0.13 avg vs. Runway ~$0.24 avg); Runway as fallback when Pika drift > 0.85 — balances cost discipline + quality recovery path | Runway Style Reference primary (higher quality first-pass) — rejected: ~85% cost overhead vs. Pika; ceiling utilization would jump from 20–30% range to 40–60% range, eroding headroom for v1.0.1 Mode A volume expansion | Pika sustained drift > 25% per reel OR Pika API SLA degradation beyond ±15% latency for 2+ weeks |
| 6 | **Tri-state Check #6 routing (PASS / WARN / FAIL) — WARN routes to human review** | LOCKED-as-drafted Day 29 | Drift in 0.85–0.90 band is the calibration-uncertainty zone; routing WARN to human review surfaces these reels for telemetry observation in early v1.0 production without auto-failing | WARN → auto-PASS (no human review) — rejected: would miss calibration signal | Lever 2 graduation (after 30 reels) auto-promotes WARN to auto-PASS once stable |
| 7 | **QC pre-flight check count = 6** | LOCKED Day 31 `[PRELIMINARY · operator amend Day 32 LOCK CANDIDATE]` | Six checks: anchor identity / drift score / palette delta / motion grade tolerance / brand finish presence / cost projection. Mirrors AI Video Gen's pre-flight check count (6) per Cross-SPEC §3.4 minimum-4 floor. 6 = Cross-SPEC compatible + agent-specific complete | 4 checks (minimum per §3.4) — rejected: too few for an agent that gates brand-aesthetic on cache lookups + drift math. 8+ checks — rejected: unnecessary; 6 already covers all 6 LOCKED errorEnvelope code paths at pre-flight | Day 30 retro telemetry shows any check consistently PASS-all (informative for v1.0.1 simplification) |
| 8 | **5-tuple parent_chain extension** | RESOLVED Day 30 partial 1 | Style Replication appends own `replication_set_id` at position [4] of incoming 4-tuple → 5-tuple emitted; Cross-SPEC §3.9 amendment scoped for Day 32 LOCK CANDIDATE ceremony | 4-tuple pass-through (no own ID appended) — rejected: would lose forensic trail of which Style Replication invocation produced the output; downstream debug becomes impossible | Cross-SPEC §3.9 amendment ratified Day 32; any future agent appends its own ID similarly |
| 9 | **6 LOCKED errorEnvelope codes** | RESOLVED Day 30 partial 1 | `anchor_unavailable` / `style_drift_exceeded` / `brand_finish_layer_missing` / `cost_overrun` / `qc_pre_flags_format_violation` / `style_replication_agent_failed`. Narrowed from 9 outline candidates by collapsing semantic-alias pairs; bipartite coverage of 12 checks × 6 codes maintained | 9 codes (outline candidate count) — rejected: redundant codes (palette_extraction_failure + motion_grade_mismatch both alias to style_drift_exceeded) | New failure category surfaces in v1.0 production telemetry that doesn't map to any of the 6 → v1.0.1 codes add |
| 10 | **Mode C Enterprise-only at v1.0** | LOCKED-as-drafted Day 29 · RATIFIED Day 31 `[PRELIMINARY · operator amend Day 32 LOCK CANDIDATE]` | Mode C is highest-margin path AND requires LOCKED brand anchor which is only created during Enterprise onboarding at v1.0; opening to Pro at v1.0 would create premature anchor-management complexity | Mode C Pro tier unlock — rejected: requires Pro-tier brand-anchor onboarding pipeline not built at v1.0; v1.0.1+ feature | First 3 Enterprise clients with established LOCKED anchors request Pro-tier sub-account Mode C access |
| 11 | **6th defense-in-depth firewall pass** | LOCKED-as-drafted Day 29 | Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication = 6 passes; matches Cross-SPEC §3.8 defense-in-depth canon | 5th pass (skip Style Replication firewall re-check) — rejected: Mode A user-provided clips bypass all 5 prior gates, making Style Replication the ONLY gate for those reels; defense-in-depth integrity demands its own pass | Any firewall breach reaches `successReplicatedShots` in production (telemetry-flagged immediately) |
| 12 | **Brand anchor freshness window = 90 days** | LOCKED-as-drafted Day 29 | Brand anchors evolve over time (logo refresh, palette updates, motion-grade tuning); 90-day freshness gate forces explicit re-validation of stale anchors. Day 29 outline §2.4 already specifies this | 30 days — rejected: too aggressive, would re-validate REINVENTED v2 anchor before any v2-anchored reels ship. 180 days — rejected: too long, brand drift risk | Any brand requests >90-day anchor extension (v1.0.1 brand-specific override) |
| 13 | **Mode A grade-pass single-stage** | LOCKED-as-drafted Day 29 | Multi-pass grade refinement is v1.1+ Enterprise creative tier feature; v1.0 single-stage covers 95%+ of operator+videographer use cases | Two-pass grade refinement — rejected: requires SPEC + schema + SKILL build-out far beyond Day 37 LOCK target | Sustained operator complaints about Mode A grade-pass quality |
| 14 | **Mode A fixture deferred to v1.0.1** | LOCKED Day 31 (this section) | Mode A volume too low in v1.0 launch to justify dedicated fixture authoring; 5-fixture portfolio TC-01..TC-05 covers Mode B + C end-to-end | Include TC-06 Mode A happy path — rejected: stretches Day 36 LLM Test Runbook scope beyond proven 5-fixture-test pattern (AI Video Gen Day 27 runbook precedent) | First 5 Mode A reels in production telemetry surface unique error modes |
| 15 | **§12 verbatim inherit from AI Video Gen** | RESOLVED Day 30 partial 1 (referenced) · ASSERTED Day 31 §12 | Canon-sharing prevents math drift between the two production-tier agents; AI Video Gen + Style Replication share single mathematical canon | Re-derive Style Replication-specific math — rejected: high risk of canon drift, low value gain | AI Video Gen §12 changes in v1.1+ → Style Replication §12 stays in lockstep |

**Summary of decision lifecycle:**
- 9 LOCKED-as-drafted Day 29 (outline §13 work)
- 2 RESOLVED Day 30 partial 1 (failure mode coverage + 5-tuple parent_chain) — items #8, #9
- 4 LOCKED Day 31 with `[PRELIMINARY · operator amend Day 32 LOCK CANDIDATE]` annotations — items #2, #5, #7, #10
- 0 DEFERRED to v1.0.1 from §13 (all 15 items have v1.0 verdict; 14 of the 15 also have explicit v1.0.1 revisit triggers documented above)

**Day 32 LOCK CANDIDATE reviewer behavior for `[PRELIMINARY]` items:**
- Reviewer either RATIFIES the default (no document change) OR AMENDS-with-rationale (document patched in real time during sit-down) OR DEFERS-to-v1.0.1 (document patched to remove the v1.0 commit and add a §15 v1.0.1 reservation entry).
- Donna's default behavior if reviewer skips Day 32 sit-down by Day 33: LOCK at the recommended defaults documented above and proceed with Day 33 schema authoring.

---

## §15 — Change Log + Version History (LOCKED-as-drafted Day 31)

| Version tag | Date | Day | Author | Status | Notes |
|-------------|------|----:|--------|--------|-------|
| `v1.0-outline-day-29` | 2026-05-18 (Mon) | 29 | Donna (autonomous) | OUTLINE SHIPPED | §0–§5 LOCKED-as-drafted · 15 critical decisions pre-scaffolded · 9 LOCKED · 6 PRELIMINARY |
| `v1.0-spec-body-partial-1-day-30` | 2026-05-19 (Tue) | 30 | Donna (autonomous) | PARTIAL 1 LOCKED-AS-DRAFTED | §6 + §7 + §10 + §14 · 6 errorEnvelope codes LOCKED (narrowed from 9 candidates) · 5-tuple parent_chain LOCKED · 11/15 §13 decisions LOCKED-as-drafted · Cross-SPEC §3 11/11 ✅ |
| `v1.0-spec-body-partial-2-day-31` | 2026-05-20 (Wed) | 31 | Donna (autonomous) | PARTIAL 2 LOCKED-AS-DRAFTED **(THIS DOCUMENT)** | §8 + §9 + §11 + §12 + §13 + §15 + §16 · 15/15 §13 decisions LOCKED-as-drafted (13 LOCKED + 2 RATIFIED with operator-amend annotation) · §12 verbatim inherit from AI Video Gen Day 23 §12 (zero new math) · §16 Cross-SPEC §3.9 amendment language drafted for Day 32 ratification |
| `v1.0-lock-candidate-day-32` | 2026-05-21 (Thu) | 32 | Donna + operator (sit-down) | LOCK CANDIDATE — RESERVED | Unified Day 30 + Day 31 partial reconciliation · 11-item reviewer checklist (mirror Day 24 AI Video Gen LOCK candidate pattern) · Cross-SPEC §3.9 amendment ratification ceremony |
| `v1.0-schemas-day-33` | 2026-05-22 (Fri) | 33 | Donna (autonomous) | SCHEMAS RESERVED | `input.schema.json` (Draft 2020-12 · 3-mode polymorphic input) + `output.schema.json` (polymorphic `successReplicatedShots` \| `errorEnvelope` · 5-tuple parent_chain `prefixItems` cardinality exact-5) · 6 LOCKED errorEnvelope codes encoded in enum |
| `v1.0-skill-bundle-day-34` | 2026-05-23 (Sat) | 34 | Donna (autonomous) | SKILL BUNDLE RESERVED | ~10–15 files · 5 test fixtures input.json + expected output.json · `dispatch.py` mode-switch logic per §10.5 mode-by-mode field activation matrix |
| `v1.0-lock-day-37` | 2026-05-26 (Tue) | 37 | Donna + operator | LOCK — RESERVED · HARD-GATED on AI Video Gen v1.0 LOCK | LLM Test Runbook (Day 36) outcome ratified · Day 37 v1.0 LOCK ceremony · version tag flip · production canon promoted |

**Style Replication v1.0 LOCK ceremony is hard-gated on AI Video Gen v1.0 LOCK first.** As of Day 31 authoring, AI Video Gen v1.0 LOCK status is CANDIDATE READY + BUNDLE BUILT + RUNBOOK AUTHORED · operator sit-down (Items 8 + 11) STILL UNCONFIRMED. **Operator runway: 6 days (Day 31 → Day 37) to close AI Video Gen LOCK before Style Replication LOCK ceremony is blocked.**

### §15.2 v1.0.1 reservations (parked from v1.0 §13)

- Per-engine drift threshold recalibration (§13 #3 revisit trigger)
- Multi-pass Mode A grade refinement (§13 #13 revisit trigger)
- Brand-anchor onboarding pipeline for Pro tier (§13 #10 revisit trigger)
- Mode A dedicated test fixture (§13 #14 revisit trigger)
- Anchor freshness window per-brand override (§13 #12 revisit trigger)
- 6 errorEnvelope codes expansion if new failure category surfaces (§13 #9 revisit trigger)

### §15.3 v1.1+ reservations (Sequel Digital scale path)

- Custom LoRA inheritance per brand (Day 29 outline §1.4 deferred matrix)
- Third-party LUT import (DaVinci .cube file support — creative path)
- Multi-vendor cost arbitrage (algorithmic engine selection across Pika + Runway based on real-time price signals)
- Auto-anchor-switch on coverage envelope mismatch (Mode C escape hatch deferred)
- Per-shot cost ceiling (vs. current per-reel envelope)

---

## §16 — Metadata Block Schema (LOCKED-as-drafted Day 31)

Style Replication emits the canonical Cross-SPEC §3.9 metadata block plus 3 Style Replication-specific additions. Both blocks are merged in the final `metadata` field of every output (success and errorEnvelope branches).

### §16.1 Cross-SPEC §3.9 canonical metadata block (11 fields)

```json
{
  "agent_id": "style-replication-agent-v1.0",
  "agent_version": "1.0",
  "session_id": "sess-2026-05-26-reinvented-pro-01",
  "trace_id": "trace-...",
  "tier": "pro" | "enterprise",
  "production_mode": "A" | "B" | "C",
  "parent_chain": [
    "brief-001",
    "script-001",
    "storyboard-001",
    "production_plan-001",
    "ai-video-gen-001-or-mode-c-direct",
    "replication-set-001"
  ],
  "lever_state": "lever-1" | "lever-2" | "lever-3",
  "self_qc_attempts": 1 | 2,
  "self_qc_failed_check_id": null | 1 | 2 | ... | 12,
  "timestamps": { "agent_started_at": "...", "agent_completed_at": "..." }
}
```

**5-tuple → 6-tuple parent_chain extension:** Cross-SPEC §3.9 currently specifies 4-tuple. Day 30 partial 1 RESOLVED 5-tuple extension at Style Replication layer (`replication_set_id` appended at position [5]). Day 32 LOCK CANDIDATE ratifies Cross-SPEC §3.9 amendment. Amendment language drafted below.

### §16.2 Style Replication-specific additions (3 fields)

```json
{
  "literal_fingerprint_inherit": {
    "anchor_clip_embedding_uri": "ars://brand_anchor_cache/REINVENTED/anchor-v2-locked-2026-05-15.embeddings.bin",
    "anchor_phash_64bit": "0x4a7b9c2e1f8d6a30",
    "anchor_palette_lab_centroids": [ ... 5 LAB triplets ... ],
    "anchor_motion_grade_baseline": { "contrast_target": 1.12, "saturation_target": 1.08, "lut_id": "REINVENTED-finish-v2-2026-05-15" }
  },
  "mode_c_coverage_match_bool": true | false | null,
  "replication_set_id": "replication-set-001"
}
```

- **`literal_fingerprint_inherit`** (defined §12.3 — the brand-anchor immutable fingerprint passed downstream so QC Agent + Loop Agent can re-validate consistency without recomputing CLIP/pHash) — present on ALL Mode B + C reels; partial on Mode A; null on errorEnvelope branch.
- **`mode_c_coverage_match_bool`** — true on Mode C reel that passed coverage envelope check; false on Mode C reel that fell back to Mode B; null on Mode A and Mode B reels (not applicable).
- **`replication_set_id`** — own agent invocation ID, used to extend the parent_chain to 6-tuple. Generated per session at agent start.

### §16.3 Cross-SPEC §3.9 amendment language (DRAFT for Day 32 LOCK ceremony ratification)

**Current §3.9 canon (LOCKED — read-only as of Day 31):**

> "Every agent emits a 4-tuple `parent_chain` in its metadata block, representing Brief → Script → Storyboard → ProdCoord lineage. Agents downstream of ProdCoord (AI Video Gen, Style Replication, Edit Director, QC, Localization, Publishing) inherit + emit this 4-tuple unchanged."

**Proposed Day 32 amendment language:**

> "Every agent emits a `parent_chain` in its metadata block representing the upstream lineage. Brief Agent emits a 0-tuple (nothing upstream). Script Agent emits a 1-tuple. Storyboard Agent emits a 2-tuple. Production Coord Agent emits a 3-tuple. AI Video Gen Agent emits a 4-tuple (extends ProdCoord's 3-tuple with own `ai_video_gen_session_id`). **Style Replication Agent emits a 5-tuple (extends AI Video Gen's 4-tuple with own `replication_set_id` for Mode B, or appends a `mode-c-direct` marker + own `replication_set_id` for Mode C, producing 5-tuple in both modes).** All subsequent downstream agents (Edit Director, QC, Localization, Publishing) inherit + extend this n-tuple by appending their own session_id at the next position."

**Why this amendment is necessary:**
- Without it, Style Replication has no forensic trail for which invocation produced a given `replicated_shots.json` — debug becomes impossible.
- The n-tuple-as-lineage pattern generalizes cleanly to all 17 agents in the Orchestration Blueprint (any agent that emits output appends its own session_id, producing an n-tuple where n = agent's depth in pipeline).
- Backward-compat is preserved: any consumer of the metadata block that reads `parent_chain[0..3]` (the original 4-tuple positions) still gets the original 4-tuple values; the 5-tuple extension is purely additive.

### §16.4 Field defaults and nullability

| Field | Nullable? | Default | Constraint |
|-------|----------|---------|------------|
| `agent_id` | NO | (hard-coded) | exactly `"style-replication-agent-v1.0"` |
| `agent_version` | NO | `"1.0"` | semver — v1.0 LOCK pins to `"1.0"` |
| `session_id` | NO | (generated per invocation) | UUID v4 string |
| `trace_id` | YES | null | inherits from upstream session if present |
| `tier` | NO | (from input) | enum: `"pro" \| "enterprise"` (Mode C blocks Pilot/Starter upstream) |
| `production_mode` | NO | (from input) | enum: `"A" \| "B" \| "C"` |
| `parent_chain` | NO | (extended from input) | array length ≥ 5 (Day 32 amendment) |
| `lever_state` | NO | (from input) | enum: `"lever-1" \| "lever-2" \| "lever-3"` |
| `self_qc_attempts` | NO | 1 | 1 (first attempt) or 2 (regenerate path) — per Rule #13 2-strike ceiling |
| `self_qc_failed_check_id` | YES | null | null on success, 1..12 on failure |
| `timestamps.agent_started_at` | NO | (per invocation) | ISO-8601 timestamp |
| `timestamps.agent_completed_at` | NO | (per invocation) | ISO-8601 timestamp |
| `literal_fingerprint_inherit` | YES | (present on Mode B + C, partial on Mode A, null on errorEnvelope) | object — see §12.3 |
| `mode_c_coverage_match_bool` | YES | null (non-Mode-C reels) | bool on Mode C reels; null on others |
| `replication_set_id` | NO | (generated per invocation) | UUID v4 string |

### §16.5 Schema authoring notes for Day 33

When the input + output schemas are authored Day 33:

1. **`parent_chain` `prefixItems` cardinality on output schema:** exactly 5 (Cross-SPEC §3.9 amendment Day 32 binds this). Day 33 schema must use Draft 2020-12 `prefixItems` keyword to encode 5-tuple structure with proper type constraints per position.
2. **`mode_c_coverage_match_bool` nullable encoding:** schema `type` = `[ "boolean", "null" ]` per Draft 2020-12 union.
3. **`literal_fingerprint_inherit` partial encoding:** Mode A emits a subset (missing `anchor_phash_64bit`); schema uses `oneOf` for the three Mode variants OR a single `anyOf` with optional fields — Day 33 author decides (DEFERRED note in schema authoring brief).
4. **`replication_set_id` UUID format:** `format: "uuid"` keyword applied (Draft 2020-12 supported).
5. **`self_qc_failed_check_id` enum + null:** `oneOf: [ { type: null }, { type: integer, minimum: 1, maximum: 12 } ]`.
6. **Backward-compat assertion:** schema test fixtures must include one fixture with the legacy 4-tuple parent_chain that schema MUST reject (proves the Day 32 amendment is enforced). One fixture with 5-tuple parent_chain that schema MUST accept. One fixture with 6-tuple (Edit Director extension preview) that schema MUST accept under "minLength: 5" rather than "exact-5" constraint.

---

## Cross-SPEC §3 adherence (Day 31 partial 2 audit)

| Dimension | Status |
|-----------|--------|
| §3.1 naming canon | ✅ |
| §3.2 literal_seed_inherit precedent | ✅ (as `literal_fingerprint_inherit` analog — §12.3 + §16.2) |
| §3.3 errorEnvelope shape | ✅ (6 codes from Day 30 partial 1 § 6.3 LOCKED) |
| §3.4 qc_pre_flags array minimum 4 + snake_case | ✅ (6 pre-flight checks LOCKED §13 #7) |
| §3.5 mode matrix per Day 12 | ✅ |
| §3.6 slot 11 naming canon | ✅ |
| §3.7 qc_pre_flags format regex | ✅ |
| §3.8 tier↔mode firewall 6th defense-in-depth pass | ✅ (§13 #11 LOCKED) |
| §3.9 metadata block | ✅ (5-tuple parent_chain extension Day 30 RESOLVED · amendment language drafted §16.3 for Day 32) |
| §3.10 cost ceiling authority $ per tier | ✅ (§13 #2 LOCKED with operator-amend annotation) |
| §3.11 LOCK respect | ✅ (AI Video Gen §12 + §11 + §6 canon all read-only; zero net-new math in §12) |

**11 of 11 ✅** at partial 2 stage. Full audit Day 32 LOCK CANDIDATE.

---

## Daily integrity checks (Day 31 — passed)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked.
- ✅ **No external comms.** No emails sent, no DMs, no social posts, no investor outreach, no client outreach.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine API runs initiated.
- ✅ **No operator-impersonation.** Day 27 LLM Test sit-down outcome NOT assumed. Items 8 + 11 ratification NOT silently advanced. AI Video Gen v1.0 LOCK status remains CANDIDATE READY + BUNDLE BUILT + RUNBOOK AUTHORED until operator confirms. Style Replication §13 4 PRELIMINARY items LOCKED at recommended defaults with explicit `[PRELIMINARY · operator amend Day 32 LOCK CANDIDATE]` annotations — NOT silently ratified as if operator had reviewed.
- ✅ **No fake-advance.** Style Replication SPEC body partial 2 is LOCK-as-drafted authoring, explicitly labeled LOCKED-AS-DRAFTED. Zero net-new modifications to AI Video Gen v1.0 canon — §12 inherits verbatim. Style Replication v1.0 LOCK on Day 37 will hard-gate itself on AI Video Gen v1.0 being LOCKED first.
- ✅ **All prior canon read-only.** Day 22 partial 1 + Day 23 partial 2 + Day 24 LOCK candidate + Day 25 schemas + Day 26 SKILL bundle + Day 27 runbook + Day 28 primer + Day 29 outline + Day 30 partial 1 all untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon.
- ✅ **Pattern source acknowledged.** AI Video Gen Day 23 partial 2 structure inherited verbatim at section level. Numerical values re-derived for Style Replication cost class (roughly 1/8th of AI Video Gen per-reel envelope). §12 IDENTICAL inheritance enforced — no canon drift.

---

## Section coverage summary

| Section | Status at Day 31 close | Source of truth |
|---------|------------------------|-----------------|
| §0 Provenance | LOCKED-as-drafted Day 29 | Outline |
| §1 Purpose & Position | LOCKED-as-drafted Day 29 | Outline |
| §2 Inputs (3 modes) | LOCKED-as-drafted Day 29 | Outline |
| §3 Outputs skeleton | LOCKED-as-drafted Day 29 | Outline |
| §4 Tier constraints | LOCKED-as-drafted Day 29 | Outline |
| §5 Process (11-step) | LOCKED-as-drafted Day 29 | Outline |
| §6 12-Check Self-QC | LOCKED-as-drafted Day 30 | Partial 1 |
| §7 System Prompt v1.0 | LOCKED-as-drafted Day 30 | Partial 1 |
| §8 Performance Targets | LOCKED-as-drafted Day 31 | **Partial 2 (this doc)** |
| §9 Test Fixtures | LOCKED-as-drafted Day 31 | **Partial 2 (this doc)** |
| §10 Field Map | LOCKED-as-drafted Day 30 | Partial 1 |
| §11 Cost Model | LOCKED-as-drafted Day 31 | **Partial 2 (this doc)** |
| §12 Style Consistency Math | LOCKED-as-drafted Day 31 (VERBATIM INHERIT) | **Partial 2 (this doc) + AI Video Gen Day 23** |
| §13 Critical Decisions | 15/15 LOCKED-as-drafted Day 31 (9 Day 29 + 2 Day 30 + 4 Day 31 RATIFIED) | Outline + Partial 1 + **Partial 2** |
| §14 Implementation Plan | LOCKED-as-drafted Day 30 | Partial 1 |
| §15 Change Log | LOCKED-as-drafted Day 31 | **Partial 2 (this doc)** |
| §16 Metadata Block | LOCKED-as-drafted Day 31 | **Partial 2 (this doc)** |

**SPEC body COMPLETE at Day 31 close. Day 32 LOCK CANDIDATE = unified reconciliation of Day 30 + Day 31 partials into single v1.0 LOCK CANDIDATE document with 11-item reviewer checklist (mirror Day 24 AI Video Gen pattern).**

---

## What's next (Day 32)

**Primary:** v1.0 LOCK CANDIDATE document — unified reconciliation. Target file: `ARS-2026-05-21-Day-32-Style-Replication-Agent-v1-LOCK-CANDIDATE.md`. Pattern source: `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` (Day 24 LOCK candidate — proven 11-item reviewer checklist shape). Includes:

1. Unified §0–§16 document (merge Day 30 + Day 31 partials with no behavioral changes — text-only reconciliation)
2. 11-item reviewer checklist (autonomous PASS verdict on 9; OPERATOR-ONLY on 2: Item #6 cost canon spot-check + Item #11 Cross-SPEC §3.9 amendment ratification ceremony)
3. Cross-SPEC §3.9 amendment ratification (5-tuple parent_chain language drafted §16.3 of THIS document)
4. 4 PRELIMINARY §13 items either ratified (no doc change) OR amended (doc patched in real time)

**Stretch:** If operator amends 4 PRELIMINARY items + ratifies Cross-SPEC §3.9 amendment + spot-checks 2 cost canon rows in single Day 32 sit-down → v1.0 LOCK candidate has all 11 reviewer items PASS verdicted same-day; Day 33 schemas authoring proceeds clean.

**Day 37 hard-gate reminder:** Style Replication v1.0 LOCK requires AI Video Gen v1.0 LOCK confirmed FIRST. Operator runway: 6 days from Day 31 → Day 37. Items 8 + 11 of AI Video Gen Day 24 LOCK candidate STILL UNCONFIRMED.

---

*Day 31 ships clean. SPEC body §6–§16 fully drafted across Day 30 + Day 31 partials. 15/15 §13 decisions resolved (13 LOCKED + 4 with operator-amend annotation, 2 RESOLVED in Day 30 already). §12 inherits verbatim from AI Video Gen — zero canon drift. Cross-SPEC §3 11/11 ✅ at partial 2 close. Day 32 LOCK CANDIDATE primed.*
