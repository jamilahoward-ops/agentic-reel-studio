# ARS — QC Pre-flight Agent v1.0 SPEC BODY PARTIAL 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16)

**Date:** Mon Jun 1, 2026 (Day 43 of 42+ · Wk6 · commercial-launch target day)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** REMAINING SPEC BODY — §8 (Performance Targets) · §9 (5 Test Fixtures) · §11 (Cost Model) · §12 (Verdict Math — deterministic ∧-of-gates) · §13 (Critical Decisions LOCKED) · §15 (Change Log + Version History) · §16 (Metadata Block Schema) all drafted to LOCK-quality. **Day 41 sections §6 / §7 / §10 / §14 NOT TOUCHED** — inherited verbatim from `ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md`. SPEC body §6–§16 is COMPLETE at this document's close. The Day 44+ LOCK CANDIDATE reconciles the Day 41 + Day 43 partials into the single v1.0 LOCK CANDIDATE document. **No LLM dispatched. No render API touched. No engine credentials referenced. No external comms beyond the CLAUDE.md status SMS. No financial commitments. ZERO $ spent.**
**Pattern source:** `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` §8 / §9 / §11 / §12 / §13 / §15 / §16 (Day 31 LOCKED — verbatim structural shape inherited; numerical values re-derived for QC Pre-flight's reasoning-only, near-zero cost class). `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` §8 / §13 / §15 (Day 23 grandparent pattern).
**Predecessor partial:** `ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` (Day 41 — §6 / §7 / §10 / §14 LOCKED-as-drafted; this document is the missing complement).
**Predecessor outline:** `ARS-2026-05-29-Day-40-QC-Preflight-Agent-SPEC-Outline.md` (§0–§5 SHIPPED Day 40; 12 critical decisions pre-scaffolded — 8 LOCKED-as-drafted Day 40, 2 RESOLVED Day 41, 2 PRELIMINARY operator-amend Day 43).
**11-point gate source:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §13 (LOCKED — the canonical acceptance gate, inlined verbatim into §7 on Day 41; re-referenced here for the §9 fixtures + §12 verdict math).
**Cross-spec canon:** `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — §3 adherence re-audited at end of this document). **§3.9 n-tuple amendment ratification remains OPERATOR-PENDING** — the 6-tuple parent_chain (§16.3) is the hard forcing function and is explicitly NOT advanced here.

---

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this partial's authoring, on-disk file-state confirms **both prior production-tier LOCK ceremonies remain OPERATOR-GATED.** AI Video Gen SKILL.md frontmatter still reads `status: v1.0 SKILL bundle SHIPPED — LLM execution Day 27 locks v1.0` (no flip to LOCKED). Style Replication SKILL.md still reads `v1.0 LOCK target: Day 37 — hard-gated on AI Video Gen v1.0 LOCK ceremony first` (no flip). The Day 36 Style Replication LLM Test Runbook execution + both LOCK ceremonies are unconfirmed. QC Pre-flight v1.0 LOCK will hard-gate itself on those closing first — this body partial is forward-design over LOCK-stable text artifacts only, with ZERO production output consumed. The 6-tuple parent_chain (§16) is BLOCKED on the Cross-SPEC §3.9 amendment ratification (operator-pending) and is NOT silently committed.

> **Day 43 launch-day note (sequencing honesty, carried from outline §0 + §1):** Today is the canon commercial-launch target. The 42-day sprint's headline deliverable — the **Mode B Pro single-reel commercial demo** threaded through the six launch-critical agents — does NOT depend on QC Pre-flight. QC Pre-flight is Agent #7; its v1.0 LOCK lands inside the **post-launch hardening window**. The operator's Day 42-demo call is the gate on a commercial-launch pivot; that call is operator-only and is NOT made here. The autonomous forward deliverable for Day 43 is therefore this SPEC body partial 2, completing the QC Pre-flight SPEC body so the gate is LOCK-ready early in hardening. No launch chip is flipped, no demo is ratified, no LOCK ceremony is performed.

---

## DAY 43 AUTHORING SCOPE

This document completes the QC Pre-flight Agent v1.0 SPEC body. Seven sections are LOCKED-as-drafted today:

- **§8** — Performance Targets (9 metric categories calibrated for a reasoning-only terminal quality gate; the defining target is **false-pass rate 0%** — a brand-safety gate must never pass a breach).
- **§9** — 5 Test Fixtures (TC-01 Mode B Pro PASS · TC-02 Mode C Enterprise PASS · TC-03 `entity_firewall_breach` · TC-04 `format_spec_violation` · TC-05 `drift_unresolved` soft-hold). 2 PASS branches + 3 non-pass verdict outcomes exercised live; the remaining 6 LOCKED codes covered by schema-only fixtures on the schemas day.
- **§11** — Cost Model (near-zero engine snapshot: $0.00 reasoning base + optional native pHash/CLIP re-verify $0.001/shot on contested drift only; effective per-reel $0.00–$0.02). Value model = **catch-cost-avoidance**, not direct margin — the lowest-cost agent in the fleet and the highest catch-leverage.
- **§12** — Verdict Math (deterministic ∧-of-gates; pure boolean composition over the upstream evidence surface; **zero thresholds to tune** — the deliberate inverse of Style Replication's weighted drift score).
- **§13** — Critical Decisions LOCKED (12 pre-enumerated Day 40 outline; 8 LOCKED-as-drafted Day 40, 2 RESOLVED Day 41, 2 PRELIMINARY closed today + 2 net-new resolved from outline Open Questions → **14 of 14 §13 coverage at partial 2 close**, with the single 6-tuple item explicitly DEFERRED on operator ratification).
- **§15** — Change Log + Version History (lifecycle entries from Day 40 outline through the post-launch v1.0 LOCK target).
- **§16** — Metadata Block Schema (canonical Cross-SPEC §3.9 block + 4 QC Pre-flight-specific additions + the §3.9 6-tuple amendment dependency, drafted for the operator ratification ceremony — NOT ratified here).

The **9-errorEnvelope-code + slot-11 namespace** LOCKED in Day 41 partial 1 §6.3 and the **12-check self-QC list** LOCKED in Day 41 §6.1 are RE-ASSERTED in §13 (Decisions #6, #7) and §15. The Day 44+ LOCK CANDIDATE reviewer is the gating reconciliation authority for the Day 41 + Day 43 partial reconciliation.

---

## §8 — Performance Targets (LOCKED-as-drafted Day 43)

QC Pre-flight v1.0 ships against the following measurable performance envelope. Because the agent calls **no generative engine** and produces **judgments rather than pixels**, its target profile is fundamentally different from the two production-tier agents: latency is fast (reasoning-only), engine cost is zero, and the central metric is not throughput or fidelity but **decision correctness** — specifically, never passing a breach.

Targets are calibrated for the **first 30 reels of any mode that traverse the gate** (Lever 3 — every verdict is a human-ratified recommendation at v1.0). Unlike the production agents, QC Pre-flight does NOT exclude any mode from the rolling-30 window: a brand-safety gate's correctness must be measured across every reel it sees, regardless of mode or tier.

**Reading rule:** every target below is a v1.0 commit. The LLM Test Runbook (post-launch hardening day) produces the first empirical reading; the v1.0 LOCK ceremony locks the target table. Below-target metrics are calibration signal for v1.1 planning — **except false-pass rate, which has zero tolerance and is a blocking defect at any non-zero value.**

### §8.1 The 9 metric categories

| # | Metric | v1.0 Target | Failure threshold | Measurement window | Source field |
|---|--------|------------:|------------------:|-------------------:|--------------|
| 1 | **Schema validity rate** (output validates clean against `output.schema.json`) | 100% | < 99% | Per-reel, rolling 30 | Self-QC Check #12; final post-§6 validator |
| 2 | **Firewall catch rate** (7th-pass entity firewall — zero banned tokens reach a `pass` verdict; every injected breach is caught) | 100% | ≥ 1 miss | Per-reel, ALL reels | Check #2; `entity_firewall_pass_7.hits` audit |
| 3 | **False-pass rate** (reels emitted `pass` that carried ANY real defect — firewall leak, failed brand-voice point, format/caption/cost violation, unresolved drift) | **0%** | **> 0% (any single false-pass)** | Per-reel, ALL reels | Verdict audit vs. ground-truth fixture + post-hoc human review |
| 4 | **False-fail (over-block) rate** (clean reels emitted `fail`/`reshoot`/`hold` that human review reverses to `pass`) | ≤ 5% | > 10% | Per-reel, rolling 30 | Verdict audit vs. human ratification outcome |
| 5 | **11-point Brand Voice adjudication completeness** (every verdict carries exactly 11 `per_point` entries, each with non-empty evidence) | 100% | < 100% | Per-reel, ALL reels | Check #3; `brand_voice_qc.per_point[]` length + evidence non-null |
| 6 | **Route-back accuracy** (every non-pass verdict routes to the correct responsible agent per the §3.2 verdict↔route map) | 100% | < 95% | Per-reel, rolling 30 | Check #10; `route_back_to` vs. ground-truth responsible agent |
| 7 | **Wall-clock latency** (reasoning-only; p50 / p95 across all tiers — no engine wait) | p50 ≤ 30 sec · p95 ≤ 90 sec | p95 > 180 sec | Per-reel, rolling 30 | `metadata.latency_ms` |
| 8 | **Engine-cost discipline** (no generative engine dispatched; effective per-reel cost within the reasoning + optional-fingerprint envelope) | $0.00 base; ≤ $0.02 with contested-drift pHash/CLIP re-verify | any generative-engine dispatch (≠ $0 render) OR > $0.05/reel | Per-reel, ALL reels | `cost_incurred_usd`; engine-call audit (must be empty) |
| 9 | **qc_pre_flags floor-adjudication accuracy** (correctly identifies every short/malformed/negative-predicate upstream array; never passes a floor breach) | 100% | < 100% | Per-reel, ALL reels | Check #7; `qc_pre_flags_adjudication.floor_met_all` vs. ground-truth |

**Comparison to the production-agent §8 numbers (sanity check):**

| Metric class | AI Video Gen / Style Replication §8 | QC Pre-flight Day 43 §8.1 | Delta rationale |
|--------------|-------------------------------------|---------------------------|------------------|
| Schema validity | 100% / <99% | 100% / <99% | Identical (schema discipline is fleet canon, not agent-specific) |
| Firewall catch | 100% / ≥1 leak | 100% / ≥1 miss | Identical *standard*, **higher stakes** — QC Pre-flight is the LAST automated pass; a miss here reaches a published surface |
| Primary correctness metric | drift rate ≤12% / per-engine success ≥90% | **false-pass 0%** | QC Pre-flight has no generative output to score — its correctness IS the verdict. Zero false-pass is the only acceptable target for a terminal brand-safety gate |
| Over-block tolerance | (n/a — production agents don't block) | ≤5% / >10% | NEW — over-blocking is the SAFE failure direction; a false-fail costs a re-review, a false-pass costs a brand-safety incident |
| Latency p95 | Pro ≤8 min / Enterprise ≤14 min (render-bound) | ≤90 sec (reasoning-only) | ~6–9× faster — no engine wait; the agent reasons over already-produced output |
| Engine cost | $16–$60/reel (render + grade) | $0.00–$0.02/reel | ~1000× cheaper — pure reasoning + optional native fingerprint compute |
| Retry rate | ≤0.15–0.20 | (folded into §8.3 self-QC) | QC Pre-flight retries the *report*, not a render; tracked as self-QC two-attempt rate |

### §8.2 The false-pass / false-fail asymmetry (the gate's defining target discipline)

QC Pre-flight is the only agent in the fleet whose two error directions have **radically asymmetric cost**:

| Error direction | What it costs | v1.0 policy |
|-----------------|---------------|-------------|
| **False-pass** (passed a reel that should have failed) | A brand-safety incident on a published surface — the single most expensive defect class in the pipeline. Irreversible once published. | **ZERO tolerance.** Bias every ambiguity toward fail/hold. Decision #8 (§13). |
| **False-fail** (blocked a clean reel) | One human re-review + a possible re-run cycle. Annoying, fully recoverable, costs minutes. | Acceptable up to ≤5%; >10% triggers a v1.1 over-block-calibration review (the gate is too aggressive and is wasting operator review cycles). |

This asymmetry is **why the verdict math (§12) has no tunable threshold** — there is no "confidence score" to trade off. Every gate is a hard boolean, and any ambiguity resolves to the safe side (fail/hold). The gate would rather block 5 clean reels than pass 1 dirty one.

### §8.3 Self-QC pass rate (report-construction reliability)

| Metric | Target | Failure threshold |
|--------|-------:|------------------:|
| First-attempt pass rate (all 12 self-QC checks PASS on first run, no regenerate) | ≥ 92% | < 80% |
| Two-attempt pass rate (regenerate-and-pass within the §6 2-strike ceiling) | ≥ 99% | < 95% |
| Final fail rate (`preflight_qc_agent_failed` emitted with `attempts: 2`) | ≤ 1% | > 4% |

**Stricter than both production agents** (Style Replication §8.3 = 88% / 98% / 2%) because QC Pre-flight's 12-check list is built entirely around **adjudication + assertion** checks (does the report carry 11 points? does every non-pass carry a route? is the evidence hash present?) — not generative validations. A well-formed report should self-validate more reliably than a generated payload. A high `preflight_qc_agent_failed` rate is itself a signal the upstream evidence surface is malformed, not that the gate is unreliable.

### §8.4 Calibration windows

- **First 10 reels (post-LOCK):** ANY single target miss is informational only — calibration data, not failure. **EXCEPTION:** a single false-pass (metric #3) is a blocking defect at any volume and triggers an immediate root-cause review, not a calibration note.
- **First 30 reels (Lever-2 graduation gate):** aggregated rolling-30 window evaluated. Any metric ≥ its "Failure threshold" blocks Lever-2 graduation. Over-block rate (metric #4) > 10% triggers an aggressiveness re-tune; false-pass at any value blocks graduation outright.
- **First 90 reels (Lever-1 graduation gate):** both Lever-2 conditions held + each metric stable within ±10% across the last 30. **Note:** because false-pass tolerance is zero, QC Pre-flight is the natural Lever-3 sit-down agent (outline §0) and may be the LAST agent to graduate off human review — by design. Its verdict is exactly the artifact the operator ratifies; graduating it to Lever-2 means trusting the gate to advance reels without a human glance, which the operator gates explicitly.

### §8.5 What is intentionally NOT in §8 (v1.0 scope discipline)

- Per-platform aesthetic scoring (subjective creative QC) — v1.1+, data-gated on a v1.0 production corpus.
- LUFS / loudness verification — requires the Sound agent's output (not built); deferred to the full pre-publish #14 gate (Decision #11, §13).
- ML brand-likeness classifier accuracy — v1.1+, data-gated.
- Auto-fix patch-quality scoring — v1.0 only *routes*; it does not patch (Decision #13, §13).
- Cross-reel verdict-consistency drift (does Reel #7 get judged the same way as Reel #6?) — Loop Agent / post-v1.0 calibration territory.

### §8.6 Performance target measurement source — runtime hooks

Per Cross-SPEC §3.9, every verdict emits the following metric-hook fields that the §8 dashboard aggregates:

```
verdict
output_type
entity_firewall_pass_7.hits
brand_voice_qc.points_passed
brand_voice_qc.per_point[*].status
format_spec_check.{aspect_ratio_violations, duration_violations, caption_burn_parity_violations}
caption_spec_check.{burn_in_firewall_status, parity_status}
cost_ledger_check.{cumulative_reel_usd, status}
qc_pre_flags_adjudication.{agents_reporting, floor_met_all, negative_predicates}
drift_reconciliation.{unresolved_drift_count, human_signoff_required}
route_back_to
failure_code (null on pass)
failed_check_id (null on pass)
cost_incurred_usd
metadata.latency_ms
metadata.self_qc_attempts (1 or 2)
metadata.self_qc_failed_check_id (null on success, 1..12 on failure)
metadata.verdict_evidence_hash
metadata.production_mode ("A" | "B" | "C")
metadata.human_review_required (always true at v1.0 Lever-3)
```

These hooks are the contract surface between QC Pre-flight v1.0 and the §8 dashboard. The **false-pass audit (metric #3)** additionally requires a ground-truth label per reel (from the fixture set during testing, from post-hoc human review in production) — this is the only metric that cannot be computed from the verdict payload alone, because by definition a false-pass *looks* clean to the agent that emitted it.

---

## §9 — Test Fixtures (LOCKED-as-drafted Day 43)

Five test fixtures form the validation portfolio for QC Pre-flight v1.0. Pattern source: Style Replication Day 31 §9 (TC-01..TC-05). Coverage is rebalanced for a quality-gate agent — the portfolio deliberately includes **the 7th-pass firewall catch (TC-03)** as the single most important fixture, since catching an upstream leak is the agent's reason to exist.

- **TC-01** — Mode B Pro clean PASS (the dominant volume path: rendered → replicated → cleared to post)
- **TC-02** — Mode C Enterprise clean PASS (the highest-margin hot-path reel)
- **TC-03** — `entity_firewall_breach` (injected banned token slipped past six upstream passes — the 7th-pass catch)
- **TC-04** — `format_spec_violation` (aspect mismatch vs. a `platform_variants[]` entry → `fail` + `route_back_to`)
- **TC-05** — `drift_unresolved` (carried `style_drift_exceeded` with no Lever-3 sign-off → soft-hold, human review)

**Code coverage reconciliation (precise):** the live-run portfolio exercises **2 success branches + 3 distinct non-pass verdict outcomes** — 5 verdict outcomes across 5 fixtures. The 3 codes exercised live are `entity_firewall_breach` (TC-03), `format_spec_violation` (TC-04), and the `drift_unresolved` soft-hold (TC-05). The remaining 6 LOCKED codes — `upstream_not_success`, `brand_voice_qc_failed`, `caption_spec_violation`, `cost_ledger_overrun`, `qc_pre_flags_floor_breach`, `lineage_integrity_failure` — plus the slot-11 catch-all `preflight_qc_agent_failed` are covered by **schema-only fixtures** authored on the schemas day (same discipline as Style Replication §9, where 2 codes were schema-only). This avoids stretching the proven 5-fixture LLM-test pattern (AI Video Gen Day 27 / Style Replication Day 36 precedent) while still binding every code to a fixture.

Each fixture is the 5-tuple: `(input.json, expected_output.json, expected_verdict, expected_code_or_null, scenario_description)`. Fixtures live at `skills/qc-preflight-agent/tests/`.

### §9.1 TC-01 — Mode B Pro clean PASS

**Scenario:** Style Replication has emitted a `successReplicatedShots` payload for a 5-shot REINVENTED reel at Pro tier. AI Video Gen `rendered_shots` is also present for the Mode B forensic SHA-256 cross-check. All six upstream agents contributed ≥4 `qc_pre_flags`. Two `platform_variants` requested (9:16 reels + 1:1 feed). No carried drift. Cumulative cost $0.40 (Style Replication only; AI Video Gen $0.00 in this fixture's render-credit scenario) — well within the $450 Pro combined ceiling.

**Input fixture file:** `tests/TC-01-mode-b-pro-clean-pass-input.json`

```json
{
  "production_mode": "B",
  "tier": "pro",
  "replicated_shots": [
    { "shot_id": "shot-001", "asset_uri": "ars://replicated/REINVENTED/sess-2026-05-29/shot-001.mp4", "drift_warning_bool": false, "qc_pre_flags": ["anchor_identity_verified", "drift_within_tolerance", "brand_finish_applied", "cost_within_ceiling"] },
    { "shot_id": "shot-002", "asset_uri": "ars://replicated/REINVENTED/sess-2026-05-29/shot-002.mp4", "drift_warning_bool": false, "qc_pre_flags": ["anchor_identity_verified", "drift_within_tolerance", "brand_finish_applied", "cost_within_ceiling"] }
  ],
  "rendered_shots": [
    { "shot_id": "shot-001", "negative_prompt_sha256": "9f2c...", "render_status": "completed" }
  ],
  "production_plan": {
    "platform_variants": [
      { "platform": "instagram-reels", "aspect": "9:16", "duration_s": 28, "caption_burn": true },
      { "platform": "instagram-feed", "aspect": "1:1", "duration_s": 28, "caption_burn": true }
    ],
    "tier": "pro"
  },
  "brief_ref": { "brief_id": "brief-REINVENTED-2026-05-29-001" },
  "cost_ledger": { "ai_video_gen_actual_usd": 0.00, "style_replication_actual_usd": 0.40, "tier_combined_ceiling_usd": 450 },
  "accumulated_qc_pre_flags": {
    "brief-agent": ["no_banned_vocabulary", "hook_within_3s", "tier_mode_authorized", "no_buildings_declared"],
    "script-agent": ["hook_verbatim_from_brief", "duration_within_band", "do_not_say_absent", "cta_block_present"],
    "storyboard-agent": ["shot_count_within_tier", "audio_pillar_voice_present", "no_buildings_per_shot", "platform_variants_complete"],
    "production-coord-agent": ["mode_routed", "vendor_assigned", "budget_envelope_set", "qc_pre_flags_propagated"],
    "ai-video-gen-agent": ["negative_prompt_attached", "render_status_completed", "cost_within_ceiling", "firewall_prompt_clean"],
    "style-replication-agent": ["anchor_identity_verified", "drift_within_tolerance", "brand_finish_applied", "cost_within_ceiling"]
  },
  "metadata": {
    "production_mode": "B", "tier": "pro", "brand_id": "REINVENTED",
    "parent_chain": ["brief-001", "script-001", "storyboard-001", "production_plan-001", "replication-set-001"],
    "negative_prompt_sha256": "9f2c...",
    "lever_state": "lever-3", "session_id": "sess-2026-05-29-reinvented-pro-01"
  }
}
```

**Expected output (success path):** `successPreflightReport` branch · `verdict: "pass"` · `route_back_to: null` · `handoff_targets: ["localization", "publishing"]`.

**Key invariants exercised:**
- 5-tuple inbound `parent_chain` extends to 6-tuple (append `preflight_report_id`) — **schema-blocked until §3.9 ratifies; v1.0 SKILL emits the 6th position but the schema validates at minLength-5 until amendment LOCK**.
- `entity_firewall_pass_7.hits == 0` across all leaf strings + 2 captions + burn-in text.
- `brand_voice_qc.points_passed == 11` (all 11 points pass, each with non-empty evidence).
- `format_spec_check.platform_variants_checked == 2`, all violation counts 0.
- Mode B forensic cross-check: single `negative_prompt_sha256` matches across `rendered_shots` and the Style Replication output → `mode_b_chain_check.passthrough_intact_bool == true`.
- `qc_pre_flags_adjudication`: `agents_reporting == 6`, `floor_met_all == true`, `negative_predicates == 0`.
- `cost_ledger_check.status == "within_ceiling"` ($0.40 ≤ $450).
- All 12 self-QC checks PASS first attempt.

**Validation matrix (against §6 12-check list):**

| Check # | Status | Notes |
|--------:|--------|-------|
| 1 — upstream success | PASS | `output_type == successReplicatedShots`; Mode B `successRenderedShots` present |
| 2 — entity firewall (7th pass) | PASS | 0 hits across all strings + 2 captions + burn-in |
| 3 — 11-point gate complete | PASS | 11/11 `per_point`, every evidence non-empty |
| 4 — format spec complete | PASS | both variants checked; 0 violations |
| 5 — caption spec complete | PASS | burn-in firewall pass + parity pass (Pro ≤ Starter? No — Pro is above Starter; `caption_burn` honored as requested in plan) |
| 6 — cost ledger reconciled | PASS | $0.40 cumulative ≤ $450 |
| 7 — qc_pre_flags floor | PASS | 6 agents × ≥4 flags; snake_case; 0 negative predicates |
| 8 — drift reconciliation | PASS | `unresolved_drift_count == 0` |
| 9 — lineage integrity | PASS | well-formed 5-tuple inbound; Mode B SHA-256 intact |
| 10 — verdict↔route map | PASS | `pass → route_back_to: null` + handoff set |
| 11 — handoff + evidence hash | PASS | `handoff_targets` non-empty; `verdict_evidence_hash` present |
| 12 — output shape + recommend-don't-approve | PASS | schema-valid; `human_review_required: true` |

### §9.2 TC-02 — Mode C Enterprise clean PASS

**Scenario:** Enterprise client (REINVENTED) Mode C hot-path reel — Style Replication produced grade-pass output directly against the LOCKED anchor; AI Video Gen was NOT invoked, so there is **no `rendered_shots` and no Mode B forensic cross-check** (`mode_b_chain_check` reports `null`). 3 `platform_variants`. No carried drift. Cumulative cost $0.55 — well within the $870 Enterprise combined ceiling.

**Input fixture file:** `tests/TC-02-mode-c-enterprise-clean-pass-input.json`

**Expected output (success path):** `successPreflightReport` · `verdict: "pass"` · `route_back_to: null` · `handoff_targets: ["localization", "publishing"]`.

**Key invariants exercised:**
- Mode-agnostic verdict logic produces the same PASS shape as TC-01 with **`mode_b_chain_check: null`** (Mode C has no AI Video Gen passthrough to forensically verify — §10.5 matrix).
- `route_back_to: "production-coord-agent"` (reshoot) is **unreachable** in Mode C (reshoot is Mode A-exclusive — Decision #14, §13).
- `cost_ledger_check.tier_combined_ceiling_usd == 870`.
- `qc_pre_flags_adjudication.agents_reporting`: in Mode C the AI Video Gen stage emits a `mode-c-direct` marker rather than render flags; the floor check confirms the **Style Replication + content-stage** flags still satisfy the ≥4 floor per contributing agent. (Mode C floor adjudication is the one place the `agents_reporting` count is mode-sensitive; the SKILL-bundle dispatch logic encodes this per §10.5.)
- All 12 self-QC checks PASS first attempt.

**Why this fixture matters:** it proves the gate is genuinely **mode-agnostic in verdict but mode-aware in reporting** — the same PASS decision, with the Mode B-only fields correctly nulled. Without TC-02, a regression that hard-required `rendered_shots` (a TC-01 assumption) would silently fail every Mode C reel — the highest-margin path.

### §9.3 TC-03 — `entity_firewall_breach` (the 7th-pass catch)

**Scenario:** A Mode B Pro reel where an upstream agent leaked a banned entity token. The `style-replication-agent` `replication_notes` field contains the string `"brand finish matched to 4821 Main reference grade"` — `4821 main` is entry #2 on the canonical firewall list (§6.5). Six prior passes missed it (an upstream bug). QC Pre-flight, the 7th and final pass, catches it.

**Input fixture file:** `tests/TC-03-entity-firewall-breach-input.json` (TC-01 base + one injected banned token in `replicated_shots[0].replication_notes`)

**Expected output (failure path):**

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "entity_firewall_breach",
  "failed_check_id": 2,
  "attempts": 1,
  "route_back_to": "style-replication-agent",
  "reel_ref": { "preflight_report_id": "preflight-REINVENTED-2026-05-29-003" },
  "cost_incurred_usd": 0.01,
  "detail": {
    "violation": "Banned entity token '4821 main' found in replicated_shots[0].replication_notes",
    "leaking_upstream_stage": "style-replication-agent",
    "matched_firewall_entry": 2,
    "recovery_path": "Forensic-log the leak; route to style-replication-agent to strip the entity reference from replication_notes; re-run the 7th pass."
  },
  "metadata": { "production_mode": "B", "human_review_required": true, "verdict_evidence_hash": "..." }
}
```

**Key invariants exercised:**
- The firewall is a **token-boundary, case-insensitive** match — `4821 main` is caught even mid-sentence inside a free-text field.
- `failed_check_id: 2`, `failure_code: "entity_firewall_breach"`, `route_back_to: "style-replication-agent"` (the leaking stage, named forensically in `detail.leaking_upstream_stage`).
- `human_review_required: true` — even a clear breach is a *recommendation* to the operator (recommend-don't-approve, Rule #12), never an autonomous quarantine.
- `attempts: 1` — a real reel defect is a valid verdict on first construction, NOT a self-QC regenerate loop.
- **This is the most important fixture in the portfolio.** It is the proof that the agent's reason to exist — being the net that catches what six prior passes missed — actually fires. A v1.0 LOCK is BLOCKED if TC-03 does not catch the injected token.

### §9.4 TC-04 — `format_spec_violation` (aspect mismatch → fail + route)

**Scenario:** A Mode B Pro reel where `production_plan.platform_variants[1]` requests a 1:1 Instagram-feed crop, but every `replicated_shots[*]` was produced at 9:16 only. The format spec check finds the missing 1:1 variant → `fail`, routes back to the responsible production agent.

**Input fixture file:** `tests/TC-04-format-spec-violation-input.json`

**Expected output (failure path):**

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "format_spec_violation",
  "failed_check_id": 4,
  "attempts": 1,
  "route_back_to": "style-replication-agent",
  "reel_ref": { "preflight_report_id": "preflight-REINVENTED-2026-05-29-004" },
  "cost_incurred_usd": 0.01,
  "detail": {
    "violation": "platform_variants[1] requested aspect 1:1 but replicated_shots[*] rendered at 9:16 only",
    "affected_platform": "instagram-feed",
    "format_spec_check": { "platform_variants_checked": 2, "aspect_ratio_violations": 1 },
    "recovery_path": "Re-run Style Replication grade pass with a 1:1 crop token OR drop the 1:1 variant from platform_variants."
  },
  "metadata": { "production_mode": "B", "human_review_required": true, "verdict_evidence_hash": "..." }
}
```

**Key invariants exercised:**
- `format_spec_check.platform_variants_checked == len(platform_variants)` — coverage is complete (no variant skipped); the violation is a real mismatch, not under-reporting.
- `route_back_to: "style-replication-agent"` (the agent that produces the deliverable aspect) — **not** `production-coord-agent`, because this is a Mode B render-side defect, not an unrecoverable live-footage source (Mode A reshoot). The §10.5 matrix governs the route choice.
- The `recovery_path` offers BOTH a fix-it route and a drop-the-variant route — advisory, not auto-executed (Decision #13 route-back automation depth: advisory in v1.0).

### §9.5 TC-05 — `drift_unresolved` (carried drift → human-review soft-hold)

**Scenario:** A Mode B Pro reel where Style Replication flagged `shot-003` with `drift_warning_bool: true` / a carried `style_drift_exceeded` signal, and there is **no Lever-3 human sign-off** on the carried drift. QC Pre-flight does NOT auto-fail (a human may accept the drift) and does NOT auto-pass (the drift is real and unsigned). It emits the **soft-hold** — the one non-binary outcome.

**Input fixture file:** `tests/TC-05-drift-unresolved-input.json`

**Expected output (soft-hold path):**

```json
{
  "output_type": "errorEnvelope",
  "verdict": "hold",
  "failure_code": "drift_unresolved",
  "failed_check_id": 8,
  "attempts": 1,
  "route_back_to": "human-review",
  "reel_ref": { "preflight_report_id": "preflight-REINVENTED-2026-05-29-005" },
  "cost_incurred_usd": 0.01,
  "detail": {
    "drift_reconciliation": { "unresolved_drift_count": 1, "human_signoff_required": true },
    "affected_shot": "shot-003",
    "note": "Carried style_drift_exceeded on shot-003 with no Lever-3 sign-off. NOT auto-failed, NOT auto-passed. Held for operator judgment.",
    "recovery_path": "Operator reviews shot-003 drift and either (a) signs off (drift accepted → re-run gate, verdict resolves to pass) or (b) rejects (route to style-replication-agent for re-grade)."
  },
  "metadata": { "production_mode": "B", "human_review_required": true, "verdict_evidence_hash": "..." }
}
```

**Key invariants exercised:**
- `verdict: "hold"` — the fourth verdict value (the `drift_unresolved` soft-hold), distinct from `pass`/`fail`/`reshoot`.
- The agent **may NEVER emit `pass` while `unresolved_drift_count > 0`** (Rule #10) — self-QC Check #8 catches a forbidden auto-pass-over-drift before emission.
- `route_back_to: "human-review"` — the only verdict that routes to the human rather than an upstream agent.
- This is the **operationalization of the recommend-don't-approve discipline** at its sharpest: faced with genuine ambiguity, the agent declines to render a machine verdict and defers to the operator — exactly the Lever-3 behavior the gate exists to support.

### §9.6 Fixture validation gate (LLM Test Runbook trigger — post-launch hardening day)

All 5 fixtures must validate clean against the schemas-day `input.schema.json` AND produce their expected output branch when run through the SKILL-bundle-day dispatch logic. **Failure criterion:** any fixture producing an output branch other than its expected branch → the v1.0 LOCK ceremony is BLOCKED until the SPEC, schema, or SKILL is patched. **TC-03 is the gating fixture** — if the 7th-pass firewall does not catch the injected `4821 main` token, LOCK is hard-blocked regardless of the other four.

Run mode at the LLM Test Runbook: **dry-run by default** (cost ~$3 Opus tokens for SPEC + fixtures load + 5 attempts; QC Pre-flight calls no engine, so even a "live" run dispatches nothing — the only cost is reasoning tokens). This is the cheapest test runbook in the fleet.

---

## §11 — Cost Model (LOCKED-as-drafted Day 43)

QC Pre-flight is the **lowest-cost agent in the entire 17-agent fleet** and the highest catch-leverage. It calls no generative engine; its only optional spend is a native fingerprint re-verification on contested drift.

### §11.1 Cost surface v1.0 (snapshot Jun 2026)

| Cost component | Function | Cost per reel | When incurred | Notes |
|----------------|----------|--------------:|---------------|-------|
| **Reasoning tokens** (Opus, SPEC + input + verdict construction) | The full 11-step verdict loop + 12-check self-QC | $0.00–$0.01 / reel | EVERY reel | Dominant (and usually only) cost. Input is already-produced output (judgments, not pixels), so token volume is bounded and predictable. |
| **Native pHash / CLIP re-verify** | Recompute a brand-finish fingerprint ONLY when a drift flag is contested | $0.001 / shot | CONTESTED-DRIFT ONLY | Native compute, no external API. Embedded in the SKILL bundle (inherits Style Replication §11 CLIP+pHash native row). Typically 0–5 shots → $0.000–$0.005. |
| **Generative engine** | — | **$0.00 — FORBIDDEN** | NEVER | Hard Rule #2. Any generative dispatch is a metric-#8 failure (§8.1). The agent reasons over output; it does not produce it. |

**Effective per-reel cost: $0.00–$0.02.** Base case (no contested drift) ≈ $0.00–$0.01 reasoning only. Worst realistic case (contested drift, full fingerprint re-verify on ~10 shots) ≈ $0.02.

### §11.2 Per-tier cost (all tiers, all modes)

| Tier × Mode | Typical reasoning cost | Optional fingerprint re-verify | Effective per-reel | vs. tier combined ceiling |
|-------------|-----------------------:|-------------------------------:|-------------------:|--------------------------:|
| Pilot / Starter × Mode A | ~$0.005 | rare (Mode A grades against source) | ~$0.005–$0.01 | negligible vs. ≤$40 |
| Pro × Mode B | ~$0.01 | 0–5 shots → $0.000–$0.005 | ~$0.01–$0.015 | negligible vs. $450 |
| Enterprise × Mode B | ~$0.01 | 0–8 shots → $0.000–$0.008 | ~$0.01–$0.02 | negligible vs. $870 |
| Enterprise × Mode C | ~$0.01 | 0–5 shots → $0.000–$0.005 | ~$0.01–$0.015 | negligible vs. $870 |

QC Pre-flight's self-cost is **rounding error** against every tier's combined production ceiling — it adds < 0.005% to the most expensive Enterprise reel. This is by design: a safety gate must be cheap enough to run on **every** reel without economic friction (Decision #2 universal access, §13).

### §11.3 The catch-cost-avoidance value model (the agent's economic justification)

QC Pre-flight produces **no direct margin** — it is a cost center, not a revenue line. Its economic justification is entirely **downstream-cost prevention + brand-safety-incident avoidance**:

| Defect caught at the gate | Cost if it had escaped | Cost to catch at the gate |
|---------------------------|------------------------|---------------------------|
| Entity-firewall leak (TC-03) | Brand-safety incident on a published surface — reputational + client-trust cost, potentially a lost retainer. Irreversible. | ~$0.01 reasoning |
| Format-spec violation (TC-04) | A reel published at the wrong aspect on a paid placement → re-shoot/re-edit cycle + re-publish + lost spend. | ~$0.01 reasoning |
| Cost-ledger overrun | A reel that silently blew the tier ceiling → margin erosion across the retainer. | ~$0.01 reasoning |
| Unresolved drift auto-passed (TC-05) | An off-brand reel published as brand-canonical → brand-consistency erosion compounding across the content library. | ~$0.01 reasoning |

The value ratio is extreme — **$0.01 to prevent defects that cost from hundreds of dollars (re-work) to a lost retainer (brand-safety incident).** This is why the gate runs on every reel of every tier: there is no reel cheap enough to skip a $0.01 safety check.

### §11.4 Cost discipline rules (LOCKED Day 43)

1. **Generative-engine spend is forbidden, not bounded** (Hard Rule #2). The ceiling is $0, and any non-zero render spend is a defect — not an overrun to be approved.
2. **Fingerprint re-verify is contested-drift-only.** The agent does NOT routinely recompute CLIP/pHash (Style Replication already verified the anchor); re-verify fires only when a drift flag is contested and the operator/agent needs a second read before the soft-hold.
3. **No per-reel cost ceiling check on QC Pre-flight's own spend** — it is too small to gate. The agent's `cost_incurred_usd` is reported for telemetry, not enforced against a ceiling. (The agent DOES enforce the **combined production ceiling** in Step 7 — but that is the upstream agents' spend, not its own.)
4. **Cost snapshot expiration:** §11.1 token-cost figures track the Opus pricing in effect Jun 2026; refresh at the v1.0.x cadence if Opus per-token pricing shifts > 25%.

### §11.5 What is intentionally NOT in §11

- Multi-model cost arbitrage (running the gate on a cheaper model for low-risk reels) — v1.1+; at v1.0 the gate runs on Opus uniformly because false-pass tolerance is zero and a cheaper model is a false-pass risk.
- Per-brand verdict-cost benchmarking — Analytics / Loop Agent layer, post-Week 6.
- Frame-level visual QC cost (frame extraction + classifier) — deferred to the full pre-publish #14 gate (v1.1+).

---

## §12 — Verdict Math (LOCKED-as-drafted Day 43)

QC Pre-flight's "math" is the deliberate **inverse** of the production agents' continuous scoring. Where Style Replication §12 / AI Video Gen §12 compute a weighted drift score (`0.40×CLIP + 0.30×pHash + 0.20×palette + 0.10×motion`) with a tunable `drift_threshold = 0.85`, QC Pre-flight has **no continuous score and no tunable threshold**. Its verdict is pure boolean composition over the upstream evidence surface.

### §12.1 The PASS predicate (deterministic ∧-of-gates)

A reel earns `verdict: "pass"` **if and only if** every one of the following boolean gates is true:

```
PASS  ⇔  (entity_firewall_pass_7.hits == 0)
       ∧ (brand_voice_qc.points_passed == 11)
       ∧ (format_spec_check.aspect_ratio_violations == 0)
       ∧ (format_spec_check.duration_violations == 0)
       ∧ (format_spec_check.caption_burn_parity_violations == 0)
       ∧ (caption_spec_check.burn_in_firewall_status == "pass")
       ∧ (caption_spec_check.parity_status == "pass")
       ∧ (cost_ledger_check.status == "within_ceiling")
       ∧ (qc_pre_flags_adjudication.floor_met_all == true)
       ∧ (qc_pre_flags_adjudication.negative_predicates == 0)
       ∧ (drift_reconciliation.unresolved_drift_count == 0)
       ∧ (lineage_integrity intact: parent_chain well-formed ∧ (Mode B ⇒ negative_prompt_sha256 passthrough intact))
       ∧ (upstream output_type ∈ {successReplicatedShots, successRenderedShots})
```

Any single ∧-term false ⇒ the reel does NOT pass. There is **no partial credit, no weighting, no score** — a brand-safety gate is a conjunction, not an average. One firewall hit fails the whole reel even if all 11 brand-voice points pass.

### §12.2 The non-pass routing decision tree (which non-pass outcome)

When the PASS predicate is false, the verdict resolves to exactly one of `fail` / `reshoot` / `hold` by the first matching rule, evaluated in this order:

```
1. upstream output_type ∉ success branches
        → verdict: fail   · code: upstream_not_success    · route_back_to: the failed upstream agent
2. entity_firewall_pass_7.hits > 0
        → verdict: fail   · code: entity_firewall_breach  · route_back_to: the leaking upstream stage
3. lineage broken (malformed parent_chain OR Mode B SHA-256 mismatch)
        → verdict: fail   · code: lineage_integrity_failure · route_back_to: the breaking upstream stage
4. qc_pre_flags floor breached OR shape-malformed OR negative predicate
        → verdict: fail   · code: qc_pre_flags_floor_breach · route_back_to: the under-emitting upstream agent
5. cost_ledger_check.status == "overrun"
        → verdict: fail   · code: cost_ledger_overrun      · route_back_to: operator (cost decision)
6. ≥1 of the 11 brand-voice points fails
        → verdict: fail   · code: brand_voice_qc_failed    · route_back_to: script-agent / storyboard-agent
7. format spec violation
        → verdict: fail (or RESHOOT if Mode A source unrecoverable)
          · code: format_spec_violation
          · route_back_to: style-replication-agent / ai-video-gen-agent  (Mode A unrecoverable → production-coord-agent)
8. caption spec violation
        → verdict: fail   · code: caption_spec_violation   · route_back_to: the responsible caption-producing stage
9. unresolved drift, no Lever-3 sign-off
        → verdict: HOLD   · code: drift_unresolved         · route_back_to: human-review
```

**Ordering rationale:** the tree is ordered **hardest/cheapest-to-detect-and-most-fundamental first**. Upstream-failure and firewall breach (rules 1–2) halt before any further adjudication — there is no point evaluating brand-voice on a payload that already failed or already leaked. Lineage and floor (rules 3–4) are forensic/structural. Cost, brand-voice, format, caption (rules 5–8) are the substantive content defects. Drift soft-hold (rule 9) is LAST because it is the only non-binary outcome — it fires only when every binary gate is otherwise clean but drift is carried and unsigned. This mirrors the §6.2 check-ordering rationale (entry → substance → deferral).

### §12.3 Why no threshold (the design-honest contrast with the production agents)

| Property | Style Replication / AI Video Gen §12 | QC Pre-flight §12 |
|----------|--------------------------------------|-------------------|
| Output of the math | continuous `inheritance_match_score_0_1` ∈ [0,1] | boolean PASS / NON-PASS |
| Tunable parameter | `drift_threshold = 0.85` + 4 component weights | **NONE** |
| Calibration surface | re-weight components, re-bid threshold per brand | **NONE — nothing to calibrate** |
| Ambiguity handling | WARN band (0.85–0.90) routes to human | every ambiguity resolves to fail/hold (the safe side) |
| Failure direction bias | symmetric (drift is drift) | **asymmetric — biased to over-block** (§8.2) |

**The absence of a threshold is a feature, not a gap.** A terminal brand-safety gate with a tunable confidence knob is a gate someone can turn down under launch pressure. By making every gate a hard boolean with no knob, QC Pre-flight removes the "just lower the threshold to ship this reel" failure mode entirely. The only way to pass a reel is to fix the defect — there is no setting that passes a dirty reel.

### §12.4 Drift: the one place QC Pre-flight reads a continuous upstream signal (but renders a boolean)

QC Pre-flight does NOT recompute drift — Style Replication already did, producing `inheritance_match_score_0_1` and a `drift_warning_bool`. QC Pre-flight reads the **boolean** `drift_warning_bool` + any carried `style_drift_exceeded` flag and asks a binary question: *is there carried drift the human has not signed off on?* If yes → soft-hold. It never re-derives the score, never re-bids the 0.85 threshold (that is Style Replication's canon), and never decides *for* the human whether the drift is acceptable. The continuous math lives upstream; QC Pre-flight consumes its boolean conclusion. This is the **canon-sharing discipline** (Style Replication §12.5) viewed from the consumer side — QC Pre-flight inherits the drift verdict rather than re-litigating the drift math.

### §12.5 Verdict evidence hash (tamper-evident verdict)

Every emitted verdict carries `metadata.verdict_evidence_hash` = SHA-256 over the canonicalized per-check evidence block (the 13 ∧-terms of §12.1 with their evidence strings, serialized in a fixed key order). This is the forensic invariant (Cross-SPEC §3.2): given the same input, the same verdict yields the same hash; any post-hoc tamper with the evidence block (e.g., flipping a `fail` evidence string to make a reel look passed) breaks the hash. The hash is the audit anchor for the false-pass review (§8.1 metric #3) — it proves the verdict the agent emitted is the verdict it computed.

---

## §13 — Critical Decisions LOCKED (14 of 14 · LOCKED-as-drafted Day 43)

The Day 40 outline §13 pre-enumerated **12 critical decisions**. Day 41 partial 1 RESOLVED 2 (errorEnvelope code count → 9 + slot-11; self-QC check count → 12). Today's Day 43 partial 2 closes the 2 remaining PRELIMINARY items at Donna's recommended defaults with explicit `[PRELIMINARY · operator amend at LOCK CANDIDATE]` annotations, and adds 2 net-new decisions resolved from the Day 40 Open Questions (drift soft-hold semantics; reshoot Mode A-exclusivity) → **14 of 14 §13 coverage at partial 2 close.** The single 6-tuple parent_chain item remains explicitly DEFERRED on operator ratification of the Cross-SPEC §3.9 amendment.

| # | Decision | Verdict | Rationale | Alternative considered | Revisit trigger |
|---|----------|---------|-----------|------------------------|-----------------|
| 1 | **Pre-flight scope only at v1.0** (production → post boundary; full #14 pre-publish gate deferred) | LOCKED-as-drafted Day 40 | The in-post fleet (Ingest/Edit/Sound/Motion) is not built; v1.0 gates the production output it can see. Highest-leverage buildable slice. | Build the full #14 pre-publish gate now — rejected: cannot gate post-production that doesn't exist | In-post fleet ships → v1.1 full pre-publish #14 gate |
| 2 | **Universal tier access** (all 4 tiers traverse the gate) | LOCKED-as-drafted Day 40 | Safety is not a tier feature; a Pilot leak is the same incident as a Enterprise leak. | Gate Pro/Enterprise only (like Style Replication) — rejected: would leave Pilot/Starter Mode A reels with no final safety pass | Never (foundational) |
| 3 | **Verdict model: Pass / Fail / Reshoot + `drift_unresolved` soft-hold (4th outcome)** | LOCKED-as-drafted Day 40 | Three machine verdicts + one human-deferred outcome covers every routing need. | Pass/Fail only — rejected: conflates "fix it" (fail) with "re-shoot it" (reshoot) and "ask the human" (hold), destroying routing signal | New routing category surfaces in production telemetry |
| 4 | **Route-back map** (fail → responsible agent · reshoot → ProdCoord · hold → human) | LOCKED Day 43 `[PRELIMINARY · operator amend at LOCK CANDIDATE]` | Each non-pass outcome routes to the precise stage that can fix it — the routing signal is the gate's whole downstream purpose. | Single generic "route back to orchestrator" — rejected: loses the responsible-agent attribution that lets the orchestrator re-enter at the right point | Orchestrator auto-re-entry built (Decision #13) → route map gains auto-dispatch semantics |
| 5 | **6-tuple parent_chain** (inherit Style Replication 5-tuple + append `preflight_report_id`) | **DEFERRED — gated on Cross-SPEC §3.9 n-tuple amendment ratification (operator-pending)** | QC Pre-flight is the first 6-tuple consumer and the hard forcing function for the §3.9 amendment. | Stay at 5-tuple (no own ID) — rejected: loses the forensic trail of which verdict produced a given report | Operator ratifies §3.9 → schema `prefixItems` cardinality flips from minLength-5 to exact-6 |
| 6 | **errorEnvelope code count = 9 LOCKED + slot-11 catch-all** | RESOLVED Day 41 partial 1 §6.3 | 9 codes preserve precise route-back attribution across 6 upstream agents + format/caption/cost/drift/lineage; folding below 9 forces ambiguous routing. Narrowed from 11 candidates (2 folds). | 7 codes (outline floor) — rejected: would collapse distinct root causes. 11 codes — rejected: 2 are semantic aliases (format-violation/floor-breach; chain-break/lineage) | New failure category with no route mapping → v1.0.1 code add |
| 7 | **Self-QC check count = 12** | RESOLVED Day 41 partial 1 §6.1 | 12 checks bipartite-cover the 9 codes + slot-11 (entry / substance / deferral / report-integrity tiers). | 10 checks (outline floor) — rejected: under-covers the report-construction integrity tier (Checks #10–#12) that prevents a malformed PASS | A check consistently passes-all in telemetry → v1.0.1 simplification |
| 8 | **False-pass tolerance = ZERO** (bias all ambiguity to fail/hold) | LOCKED-as-drafted Day 40 | A terminal brand-safety gate must never pass a breach; over-blocking is the safe failure direction (§8.2 asymmetry). | Tunable confidence threshold — rejected: a knob someone lowers under launch pressure = a false-pass risk (§12.3) | Never (foundational) |
| 9 | **Engine policy: NO generative engine; optional native pHash/CLIP re-verify on contested drift only** | LOCKED-as-drafted Day 40 | The agent reasons over output; it does not produce it. $0 render ceiling is forbidden-spend, not bounded-spend (§11.4). | Allow a cheap re-render to fix defects in-gate — rejected: that is the production agents' job; the gate adjudicates, it does not patch | Frame-level visual QC need (v1.1+) may add bounded native compute |
| 10 | **Recommend-don't-approve** (emit `human_review_required: true` + a verdict recommendation; never "approved for publish") | LOCKED-as-drafted Day 40 | The operator-impersonation firewall (CLAUDE.md + ARS attestation). A `pass` means "clear to advance to the human's publish decision," not "published." | Auto-approve clean reels — rejected: a non-negotiable violation of the Lever-3 operator-only ratification | Lever-2 graduation (post-90 reels, operator-gated) may relax the human-review default — operator decision only |
| 11 | **LUFS / loudness check DEFERRED to v1.1** | LOCKED-as-drafted Day 40 | Requires the Sound agent's output (−14 LUFS IG/TT, −16 LUFS YT per Blueprint #12); the in-post fleet is not built. | Stub a LUFS check now — rejected: cannot verify loudness on output that doesn't exist yet | In-post fleet ships → full pre-publish #14 gate |
| 12 | **Schema strategy: new `preflight_report` output schema; reuse Cross-SPEC errorEnvelope + metadata shapes** | LOCKED-as-drafted Day 40 | The report is a net-new artifact (judgments, not transformations); errorEnvelope + metadata are fleet canon and reused unchanged. | Extend Style Replication's output schema — rejected: a verdict report is structurally unlike a shot array | Never (foundational) |
| 13 | **Route-back automation depth: ADVISORY in v1.0** (emit `route_back_to` + `recovery_path`; the orchestrator does NOT auto-re-enter) | LOCKED Day 43 `[PRELIMINARY · operator amend at LOCK CANDIDATE]` | v1.0 surfaces the route + recovery path for operator dispatch; auto-re-entry is an orchestrator feature, not a gate feature. Keeps the human in the loop at v1.0 Lever-3. | Auto-re-enter the pipeline on fail — rejected: premature automation before the orchestrator's re-entry logic is built + tested | Orchestrator re-entry logic ships → v1.1 auto-dispatch |
| 14 | **`reshoot` verdict is Mode A-exclusive** | LOCKED-as-drafted Day 43 (from outline Open Question #6) | Live footage can be re-shot; AI output is re-generated, never re-shot. Mode B/C defects route as `fail` to the production agent. | `reshoot` reachable in all modes — rejected: nonsensical for AI-generated output | Never (foundational mode semantics) |

**Net-new resolved from Day 40 Open Questions (folded into the table above):**
- **OQ #2 (drift soft-hold semantics)** → Decision #3 + §6.1 Check #8 + §9.5 TC-05: carried drift is a **hold** (human-deferred), NOT an auto-fail. Donna's recommended default, LOCKED-as-drafted Day 43.
- **OQ #6 (reshoot scope)** → Decision #14: `reshoot` is Mode A-exclusive.
- OQ #1 (pre-flight scope) → Decision #1. OQ #3 (6-tuple) → Decision #5 (DEFERRED). OQ #4 (route-back automation) → Decision #13. OQ #5 (false-pass tolerance) → Decision #8. All 6 Day-40 Open Questions are now mapped to a §13 decision.

**Summary of decision lifecycle:**
- 8 LOCKED-as-drafted Day 40 outline (Decisions #1, #2, #3, #8, #9, #10, #11, #12)
- 2 RESOLVED Day 41 partial 1 (Decisions #6, #7)
- 2 LOCKED Day 43 with `[PRELIMINARY · operator amend]` annotation (Decisions #4, #13)
- 2 net-new LOCKED-as-drafted Day 43 (Decisions #3 drift semantics confirmation + #14 reshoot scope)
- **1 DEFERRED on operator ratification** (Decision #5 — 6-tuple parent_chain, gated on Cross-SPEC §3.9)

**14 of 14 §13 coverage at partial 2 close** (13 LOCKED-as-drafted + 1 explicitly DEFERRED). The LOCK CANDIDATE reviewer ratifies the 2 `[PRELIMINARY]` items and the Cross-SPEC §3.9 amendment for Decision #5.

**LOCK CANDIDATE reviewer behavior for `[PRELIMINARY]` + DEFERRED items:** RATIFY the default (no document change) OR AMEND-with-rationale (patch in real time) OR DEFER-to-v1.0.1 (patch to remove the v1.0 commit + add a §15 reservation). For Decision #5 specifically: the reviewer ratifies the **Cross-SPEC §3.9 n-tuple amendment** (which unblocks the 6-tuple) OR holds it, in which case the schema author stays at minLength-5 with a documented TODO. **Donna's default if the operator skips the sit-down: LOCK the 2 `[PRELIMINARY]` items at the recommended defaults; HOLD Decision #5 at 5-tuple until the operator ratifies §3.9 — the 6-tuple is the one item Donna will NOT auto-advance.**

---

## §15 — Change Log + Version History (LOCKED-as-drafted Day 43)

| Version tag | Date | Day | Author | Status | Notes |
|-------------|------|----:|--------|--------|-------|
| `v1.0-outline-day-40` | 2026-05-29 (Fri) | 40 | Donna (autonomous) | OUTLINE SHIPPED | §0–§5 LOCKED-as-drafted · 12 critical decisions pre-scaffolded · 8 LOCKED · 2 PRELIMINARY · 2 reserved for partial resolution |
| `v1.0-spec-body-partial-1-day-41` | 2026-05-30 (Sat) | 41 | Donna (autonomous) | PARTIAL 1 LOCKED-AS-DRAFTED | §6 (12-check self-QC) + §7 (system prompt + 11-point gate inlined verbatim) + §10 (26-row field map) + §14 · 9 errorEnvelope codes + slot-11 LOCKED (narrowed from 11) · 12 self-QC checks LOCKED · Cross-SPEC §3 11/11 ✅ |
| `v1.0-rest day-day-42` | 2026-05-31 (Sun) | 42 | — | REST DAY — NO BUILD | 6th Rest Day observance. Pre-stage partial 2 scaffold only (the §8/§9/§11/§12/§13/§15/§16 TBD stubs + authoring runways already in the Day 41 partial 1 §14.6). No build canon advanced. |
| `v1.0-spec-body-partial-2-day-43` | 2026-06-01 (Mon) | 43 | Donna (autonomous) | PARTIAL 2 LOCKED-AS-DRAFTED **(THIS DOCUMENT)** | §8 + §9 + §11 + §12 + §13 + §15 + §16 · 14/14 §13 decisions resolved (13 LOCKED-as-drafted + 1 DEFERRED on §3.9) · §12 deterministic ∧-of-gates (zero tunable thresholds) · §16 6-tuple amendment dependency drafted for operator ratification · SPEC body §6–§16 COMPLETE. Commercial-launch pivot is operator-gated and NOT made here. |
| `v1.0-lock-candidate-day-44+` | 2026-06-02+ (Tue+) | 44+ | Donna + operator (sit-down) | LOCK CANDIDATE — RESERVED | Unified Day 41 + Day 43 partial reconciliation · 11-item reviewer checklist (mirror Style Replication Day 32 pattern) · Cross-SPEC §3.9 n-tuple amendment ratification ceremony (unblocks Decision #5 6-tuple) · 2 `[PRELIMINARY]` items ratified |
| `v1.0-schemas-day-45+` | post-launch hardening | 45+ | Donna (autonomous) | SCHEMAS RESERVED | `input.schema.json` (polymorphic predecessor input) + `output.schema.json` (`successPreflightReport` \| `errorEnvelope` · `verdict` enum pass/fail/reshoot/hold · 9-code + slot-11 enum · `parent_chain` minLength-5 until §3.9 ratifies then exact-6 · `per_point` minItems/maxItems 11 · `verdict_evidence_hash` hex-64 pattern) |
| `v1.0-skill-bundle-day-46+` | post-launch hardening | 46+ | Donna (autonomous) | SKILL BUNDLE RESERVED | ~10–15 files · 5 test fixtures (TC-01..TC-05 input.json + expected_output.json) + schema-only fixtures for the 6 uncovered codes · `dispatch.py` mode-aware reporting logic per §10.5 matrix · system prompt from §7 copied into SKILL.md verbatim |
| `v1.0-runbook-day-47+` | post-launch hardening | 47+ | Donna (autonomous) | LLM TEST RUNBOOK RESERVED | Paste-and-run runbook (dry-run default, ~$3 Opus; no engine dispatch by design) · TC-03 is the gating fixture (7th-pass firewall catch) · 5/5 PASS is the LOCK gate |
| `v1.0-lock-day-48+` | post-launch hardening | 48+ | Donna + operator | LOCK — RESERVED · HARD-GATED | v1.0 LOCK ceremony. **Hard-gated on:** (1) AI Video Gen v1.0 LOCK + (2) Style Replication v1.0 LOCK + (3) Day 36 Style Replication runbook 5/5 PASS + (4) Cross-SPEC §3.9 amendment ratification. Version tag flip; production canon promoted. |

**QC Pre-flight v1.0 LOCK is hard-gated on FOUR operator-pending items** (the two production-tier LOCKs + the Day 36 runbook execution + the §3.9 amendment). As of Day 43 authoring, all four remain UNCONFIRMED via on-disk file-state. QC Pre-flight's LOCK lands in the post-launch hardening window and does NOT gate the Day 42/43 commercial launch.

### §15.2 v1.0.1 reservations (parked from v1.0)

- Per-platform aesthetic scoring (Decision #1 / §8.5 revisit)
- Auto-fix patch generation (Decision #13 revisit trigger — orchestrator auto-re-entry)
- Multi-model verdict cost arbitrage (§11.5 — cheaper model for low-risk reels)
- errorEnvelope code expansion if a new failure category surfaces (Decision #6 revisit trigger)
- Self-QC check simplification if a check consistently passes-all (Decision #7 revisit trigger)
- Over-block (false-fail) calibration if metric #4 > 10% (§8.4)

### §15.3 v1.1+ reservations (the full pre-publish #14 gate)

- LUFS / loudness verification (Decision #11 — requires the Sound agent)
- ML brand-likeness classifier (data-gated on a v1.0 production corpus)
- Per-shot frame-level visual QC (frame extraction + classifier)
- Final pre-**publish** QC (the full Blueprint #14 gate, post-Motion) — built once the in-post fleet (Ingest / Edit Director / Editor / Sound / Motion) ships
- Multi-reel batch pre-flight (v1.0 = one reel per invocation)
- Reshoot-cost estimation + auto-rebook (ProdCoord round-trip automation)

---

## §16 — Metadata Block Schema (LOCKED-as-drafted Day 43)

QC Pre-flight emits the canonical Cross-SPEC §3.9 metadata block plus 4 QC Pre-flight-specific additions. Both blocks merge in the final `metadata` field of every output (`successPreflightReport` and `errorEnvelope` branches).

### §16.1 Cross-SPEC §3.9 canonical metadata block (inherited)

```json
{
  "agent_id": "qc-preflight-agent-v1.0",
  "agent_version": "1.0",
  "session_id": "sess-2026-05-29-reinvented-pro-01",
  "trace_id": "trace-...",
  "tier": "pilot" | "starter" | "pro" | "enterprise",
  "production_mode": "A" | "B" | "C",
  "parent_chain": [
    "brief-001",
    "script-001",
    "storyboard-001",
    "production_plan-001",
    "replication-set-001",
    "preflight-report-001"
  ],
  "lever_state": "lever-1" | "lever-2" | "lever-3",
  "self_qc_attempts": 1 | 2,
  "self_qc_failed_check_id": null | 1 | 2 | ... | 12,
  "human_review_required": true,
  "timestamps": { "agent_started_at": "...", "agent_completed_at": "..." },
  "latency_ms": 0
}
```

### §16.2 QC Pre-flight-specific additions (4 fields)

```json
{
  "parent_chain_6tuple_extension": "preflight-report-001",
  "qc_gate_class": "pre_flight",
  "verdict_evidence_hash": "a1b2c3...64-hex-chars...",
  "runtime_environment_class": "dev" | "staging" | "production"
}
```

- **`parent_chain` 6th position (`preflight_report_id`)** — QC Pre-flight is the first 6-tuple consumer (inherits Style Replication's 5-tuple + appends its own `preflight_report_id` at position [5]). **BLOCKED on the Cross-SPEC §3.9 n-tuple amendment ratification (operator-pending — §16.3).** Until ratified, the v1.0 SKILL emits the 6th position but the schema validates at `minItems: 5` (additive, backward-compatible); the exact-6 `prefixItems` cardinality cannot LOCK until the amendment ratifies. This is the hard forcing function.
- **`qc_gate_class`** — enum (`pre_flight` for v1.0 · `pre_publish` reserved for v1.1+). Distinguishes the production→post boundary gate (v1.0) from the post-Motion pre-publish gate (v1.1+).
- **`verdict_evidence_hash`** — SHA-256 (lowercase hex, 64 chars) over the canonicalized per-check evidence block (§12.5). Tamper-evident verdict; the audit anchor for the false-pass review (§8.1 metric #3).
- **`runtime_environment_class`** — enum (`dev` / `staging` / `production`), inherited from AI Video Gen §16. Gates production-only behaviors (e.g., contested-drift fingerprint re-verify is staging/production only).

### §16.3 Cross-SPEC §3.9 amendment dependency (the 6-tuple forcing function — operator ratification required)

The §3.9 n-tuple-as-lineage amendment was **DRAFTED at Style Replication Day 31 §16.3** (the 5-tuple extension) and remains **operator-unratified**. QC Pre-flight is the first agent to require the **6th** position, making it the concrete forcing function.

**Style Replication Day 31 §16.3 draft amendment language (read-only — the basis):**

> "Every agent emits a `parent_chain` representing upstream lineage... **Style Replication Agent emits a 5-tuple** (extends AI Video Gen's 4-tuple with own `replication_set_id`)... All subsequent downstream agents inherit + extend this n-tuple by appending their own session_id at the next position."

**QC Pre-flight's required extension (for the operator ratification ceremony):**

> "**QC Pre-flight Agent emits a 6-tuple** (extends Style Replication's 5-tuple with its own `preflight_report_id` at position [5]). The n-tuple-as-lineage pattern is now demonstrated across two consecutive downstream agents (Style Replication 5-tuple → QC Pre-flight 6-tuple), confirming the pattern generalizes to all 17 agents: any agent that emits output appends its own session_id, producing an n-tuple where n = the agent's depth in the pipeline. Schema cardinality is `minItems: <depth>` (additive, backward-compatible) rather than `exact-n`, so a downstream consumer that reads `parent_chain[0..3]` (the original 4-tuple positions) always gets the original values."

**Why this amendment must ratify before QC Pre-flight LOCKs:**
- Without it, QC Pre-flight's output schema cannot bind the 6-tuple `prefixItems` cardinality — the verdict report's lineage is structurally unverifiable.
- The amendment generalizes cleanly: Style Replication (5) → QC Pre-flight (6) → Localization (7) → Publishing (8). Ratifying it once unblocks every remaining downstream agent.
- Backward-compat is preserved (additive `minItems`, never `exact-n` below the agent's depth) — confirmed across both the Style Replication 5-tuple and the QC Pre-flight 6-tuple.

**Donna recommends: RATIFY-AS-DRAFTED.** This is surfaced as an operator action item, NOT advanced. The schema author holds at `minItems: 5` until ratification.

### §16.4 Field defaults and nullability

| Field | Nullable? | Default | Constraint |
|-------|----------|---------|------------|
| `agent_id` | NO | (hard-coded) | exactly `"qc-preflight-agent-v1.0"` |
| `agent_version` | NO | `"1.0"` | semver — v1.0 LOCK pins to `"1.0"` |
| `session_id` | NO | (generated per invocation) | UUID v7 string (Cross-SPEC §3.9 ID canon) |
| `trace_id` | YES | null | inherits from upstream session if present |
| `tier` | NO | (from input) | enum: `"pilot" \| "starter" \| "pro" \| "enterprise"` (universal — all 4) |
| `production_mode` | NO | (from input) | enum: `"A" \| "B" \| "C"` |
| `parent_chain` | NO | (extended from input) | array `minItems: 5` until §3.9 ratifies → then `prefixItems` exact-6 |
| `lever_state` | NO | (from input) | enum: `"lever-1" \| "lever-2" \| "lever-3"` (v1.0 = lever-3) |
| `self_qc_attempts` | NO | 1 | 1 (first attempt) or 2 (regenerate) — per §6 2-strike ceiling |
| `self_qc_failed_check_id` | YES | null | null on success, 1..12 on failure |
| `human_review_required` | NO | **true** | const `true` at v1.0 Lever-3 (recommend-don't-approve, Rule #12) |
| `timestamps.agent_started_at` | NO | (per invocation) | ISO-8601 |
| `timestamps.agent_completed_at` | NO | (per invocation) | ISO-8601 |
| `latency_ms` | NO | (measured) | integer ≥ 0 (reasoning-only; target p95 ≤ 90000) |
| `qc_gate_class` | NO | `"pre_flight"` | enum: `"pre_flight" \| "pre_publish"` (v1.0 = pre_flight) |
| `verdict_evidence_hash` | NO | (computed) | `pattern: "^[a-f0-9]{64}$"` (lowercase hex, 64 chars) |
| `runtime_environment_class` | NO | (from env) | enum: `"dev" \| "staging" \| "production"` |

### §16.5 Schema authoring notes for the schemas day

1. **`parent_chain` cardinality:** `minItems: 5` (additive, backward-compatible) UNTIL the Cross-SPEC §3.9 amendment ratifies, then flip to `prefixItems: [..×6]` + `items: false` for exact-6. Ship the schema with a documented TODO at the 6th position; do NOT hard-bind exact-6 before ratification.
2. **`output_type` polymorphism:** `oneOf [successPreflightReport, errorEnvelope]` (mirrors AI Video Gen / Style Replication schemas-day pattern).
3. **`verdict` enum:** `["pass", "fail", "reshoot", "hold"]`.
4. **`failure_code` enum (errorEnvelope branch):** exactly the 9 LOCKED codes (§6.3) + `preflight_qc_agent_failed`. MUST NOT enumerate the folded codes (`qc_pre_flags_format_violation`, `negative_prompt_chain_break`).
5. **`brand_voice_qc.per_point`:** `minItems: 11, maxItems: 11`; each item's `name` constrained to the 11 snake_case point names from §7 (`pillar_tag_present` … `brand_safety_clean`).
6. **`verdict_evidence_hash`:** `pattern: "^[a-f0-9]{64}$"`.
7. **`human_review_required`:** `const: true` at v1.0 (the recommend-don't-approve invariant is schema-enforced, not just prompt-enforced).
8. **`mode_b_chain_check` nullability:** `type: ["object", "null"]` (populated Mode B; null Mode A/C — §10.5 matrix).
9. **Backward-compat test fixtures:** one fixture with a 5-tuple inbound `parent_chain` that the schema MUST accept (current canon); one with a 6-tuple that the schema MUST accept under `minItems: 5` (the QC Pre-flight extension preview); after §3.9 ratification, one with a 4-tuple that the schema MUST reject (proves the amendment is enforced).

---

## Cross-SPEC §3 adherence (Day 43 partial 2 audit)

| Dimension | Status |
|-----------|--------|
| §3.1 naming canon (snake_case agent_id) | ✅ `qc-preflight-agent`; slot-11 `preflight_qc_agent_failed` |
| §3.2 hash invariant | ✅ `verdict_evidence_hash` SHA-256 over evidence block (§12.5); Mode B negative-prompt SHA-256 cross-check (§9.1/§12.1) |
| §3.3 errorEnvelope shape | ✅ Fleet shape + `verdict` + `route_back_to` (§9.3/§9.4/§9.5 fixtures exercise it) |
| §3.4 qc_pre_flags minItems 4 + snake_case | ✅ The agent IS the §3.4 floor adjudicator (§12.1 ∧-term; §8.1 metric #9) |
| §3.5 mode matrix | ✅ Mode-agnostic verdict + mode-aware reporting (§9.2 Mode C proves null Mode-B fields) |
| §3.6 slot-11 reserved naming | ✅ `preflight_qc_agent_failed` (§13 Decision #7) |
| §3.7 qc_pre_flags format regex | ✅ `^[a-z][a-z0-9_]{0,63}$` (§8.6 hooks; §12.1 floor check) |
| §3.8 tier↔mode firewall (7th defense-in-depth) | ✅ Universal-tier (§13 Decision #2); 7th-pass firewall (§9.3 TC-03) |
| §3.9 metadata block + n-tuple parent_chain | ✅ Canonical block + 4 additions (§16.1/§16.2). **6-tuple = forcing function for the §3.9 amendment (operator-pending, §16.3) — NOT advanced** |
| §3.10 cost ceiling authority | ✅ Combined-ceiling enforcement ($450 Pro / $870 Enterprise, §12.1 ∧-term; §11.2) — first agent with total-spend visibility |
| §3.11 LOCK respect (no modification of upstream LOCKED canon) | ✅ AI Video Gen + Style Replication + Cross-SPEC + Brand Voice Intake + Day 40 outline + Day 41 partial 1 all read-only; zero modifications |

**11 of 11 ✅** at partial 2 stage. Full audit at the LOCK CANDIDATE day.

---

## Process integrity (Day 43)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked. (QC Pre-flight by design calls no generative engine — Hard Rule #2.)
- ✅ **No external comms beyond the CLAUDE.md status SMS.** No emails, DMs, social posts, investor/client outreach. The status SMS to [status number redacted] announces build status only; it transacts no business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs. **ZERO $ spent.**
- ✅ **No operator-impersonation.** Both production-tier LOCK ceremonies confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Day 36 Style Replication runbook execution NOT assumed. **Cross-SPEC §3.9 amendment NOT silently committed — Decision #5 (6-tuple parent_chain) is explicitly DEFERRED and the schema holds at minItems-5 (§16.3/§16.5).** No launch chip flipped; no Day 42-demo commercial-launch pivot ratified (operator-only call).
- ✅ **No fake-advance.** This partial is forward-design over LOCK-stable text artifacts, explicitly labeled LOCKED-as-drafted (not LOCKED). QC Pre-flight v1.0 LOCK hard-gates on all four operator-pending items. Zero net-new modifications to any LOCKED canon — all references read-only.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication SPECs + schemas + SKILL bundles + Cross-SPEC review + Brand Voice Intake + the Day 40 outline + the Day 41 partial 1 — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. The HC/NPOX tokens in the §9.3 firewall fixture are the firewall's BLOCK-list test case (so the agent rejects them), not a cross-entity reference. REINVENTED remains brand-as-pilot-customer per Cross-SPEC canon.
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at partial 2 stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Style Replication Day 31 partial 2 structure inherited verbatim at section level. Numerical values re-derived for QC Pre-flight's reasoning-only, near-zero cost class. AI Video Gen Day 23 §8/§13/§15 grandparent + Brand Voice Intake §13 11-point gate (referenced) used as the grounding spine.
- ✅ **Rest Day honored.** Day 42 (Sun May 31) was observed — no build; partial 2 scaffold pre-staged only. This Day 43 build runs on Monday. 6th Rest Day observance complete.

---

## Section coverage summary

| Section | Status at Day 43 close | Source of truth |
|---------|------------------------|-----------------|
| §0 Provenance | LOCKED-as-drafted Day 40 | Outline |
| §1 Purpose & Position | LOCKED-as-drafted Day 40 | Outline |
| §2 Inputs | LOCKED-as-drafted Day 40 | Outline |
| §3 Outputs skeleton | LOCKED-as-drafted Day 40 | Outline |
| §4 Tier constraints | LOCKED-as-drafted Day 40 | Outline |
| §5 Process (11-step verdict loop) | LOCKED-as-drafted Day 40 | Outline |
| §6 12-Check Self-QC | LOCKED-as-drafted Day 41 | Partial 1 |
| §7 System Prompt v1.0 | LOCKED-as-drafted Day 41 | Partial 1 |
| §8 Performance Targets | LOCKED-as-drafted Day 43 | **Partial 2 (this doc)** |
| §9 Test Fixtures | LOCKED-as-drafted Day 43 | **Partial 2 (this doc)** |
| §10 Field Map | LOCKED-as-drafted Day 41 | Partial 1 |
| §11 Cost Model | LOCKED-as-drafted Day 43 | **Partial 2 (this doc)** |
| §12 Verdict Math | LOCKED-as-drafted Day 43 | **Partial 2 (this doc)** |
| §13 Critical Decisions | 14/14 LOCKED-as-drafted Day 43 (8 Day 40 + 2 Day 41 + 4 Day 43; 1 DEFERRED on §3.9) | Outline + Partial 1 + **Partial 2** |
| §14 Implementation Plan | LOCKED-as-drafted Day 41 | Partial 1 |
| §15 Change Log | LOCKED-as-drafted Day 43 | **Partial 2 (this doc)** |
| §16 Metadata Block | LOCKED-as-drafted Day 43 | **Partial 2 (this doc)** |

**SPEC body §6–§16 COMPLETE at Day 43 close. The Day 44+ LOCK CANDIDATE = unified reconciliation of the Day 41 + Day 43 partials into a single v1.0 LOCK CANDIDATE document with an 11-item reviewer checklist (mirror Style Replication Day 32 pattern).**

---

## What's next (Day 44+, post-launch hardening window)

**Primary:** v1.0 LOCK CANDIDATE document — unified Day 41 + Day 43 reconciliation. Target file: `ARS-2026-06-02-Day-44-QC-Preflight-Agent-v1-LOCK-CANDIDATE.md`. Pattern source: `ARS-2026-05-21-Day-32-Style-Replication-Agent-v1-LOCK-CANDIDATE.md` (proven 11-item reviewer checklist shape). Includes:

1. Unified §0–§16 document (merge the Day 41 + Day 43 partials — text-only reconciliation, no behavioral changes).
2. 11-item reviewer checklist (autonomous PASS on most; OPERATOR-ONLY on the Cross-SPEC §3.9 amendment ratification + the 2 `[PRELIMINARY]` items).
3. Cross-SPEC §3.9 n-tuple amendment ratification ceremony (unblocks Decision #5 / the 6-tuple parent_chain).
4. The 2 `[PRELIMINARY]` §13 items either ratified (no doc change) or amended (patched in real time).

**Operator action items (4 — all independent, surfaced NOT advanced):**

1. **AI Video Gen v1.0 LOCK ceremony** — STILL PENDING (file-state confirmed). Hard-gates Style Replication LOCK.
2. **Style Replication v1.0 LOCK ceremony** — STILL PENDING (file-state confirmed).
3. **Day 36 Style Replication LLM Test Runbook execution** — paste-and-run sit-down; 5/5 PASS is the LOCK gate. Outcome unconfirmed.
4. **Cross-SPEC §3.9 n-tuple amendment ratification** — the hard forcing function for QC Pre-flight's 6-tuple parent_chain (Decision #5 / §16.3). Donna recommends RATIFY-AS-DRAFTED.

QC Pre-flight v1.0 LOCK hard-gates on items 1–2 closing + item 4 ratifying. All four are operator-only and were NOT advanced this run.

---

*Day 43 ships clean. QC Pre-flight SPEC body §6–§16 is COMPLETE across the Day 41 + Day 43 partials. 14/14 §13 decisions resolved (13 LOCKED-as-drafted + 1 DEFERRED on the §3.9 amendment). §12 verdict math is pure deterministic boolean composition — zero tunable thresholds, the deliberate inverse of the production agents' weighted drift score. QC Pre-flight is Agent #7 of 17 — the 7th and final automated defense-in-depth firewall, the first universal-tier gate since Brief, and the agent the qc_pre_flags minItems-4 floor was built for. The Day 44+ LOCK CANDIDATE is primed. Operator pickup (4 items, all independent, surfaced NOT advanced): AI Video Gen LOCK · Style Replication LOCK · Day 36 runbook execution · Cross-SPEC §3.9 amendment ratification. Rest Day honored (Day 42). Commercial-launch pivot remains the operator's Day 42-demo call — NOT made here.*
