# ARS — Edit Director Agent v1.0 SPEC BODY PARTIAL 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16)

**Date:** Thu Jun 18, 2026 (Day 60 · Wk9 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 2 — §8 + §9 + §11 + §12 + §15 + §16 LOCKED-as-drafted Day 60. §13 critical decisions: **13 LOCKED-as-drafted + 2 carried open** (D6 8-tuple TRIPLY-DEFERRED; D15 Editor-handoff PRELIMINARY — drafted to Donna's recommended default, operator ratification pending). With this partial, the Edit Director v1.0 SPEC body is **COMPLETE**: §0–§16 all authored across the outline (Day 58), partial 1 (Day 59), and this partial 2 (Day 60). Next: v1.0 LOCK CANDIDATE assembly → input/output schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK on the established cadence (Ingest Day 53–57 / QC Pre-flight Day 44–47).
**Pattern source:** `ARS-2026-06-10-Day-52-Ingest-Agent-SPEC-Body-Partial-2.md` (Day 52 partial 2 — proven shape inherited verbatim) and `ARS-2026-06-01-Day-43-QC-Preflight-Agent-SPEC-Body-Partial-2.md` (grandparent pattern).
**Partial 1 source:** `ARS-2026-06-17-Day-59-Edit-Director-Agent-SPEC-Body-Partial-1.md` (§6 + §7 + §10 + §14 LOCKED-as-drafted Day 59).
**Outline source:** `ARS-2026-06-16-Day-58-Edit-Director-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 58 + the §6–§16 LOCK-scope preview).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — roster position 10 "Edit Director" + §3 mode-agnostic post-production contract + §4.8 Ingest→Edit-Director payload + §4.9 Edit-Director→Editor `edit_plan` handoff shape + §7 dispatch I/O).
**Brand-creative canon:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (visual identity / motion / lower-thirds), §8 (reel format / 45–75s structure), §10 (CTA library — internal-question rule), §11 (caption spec) — the enforced rule surface.
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen / Style Replication / QC Pre-flight / Ingest v1.0 LOCK candidates + schemas + SKILL bundles + runbooks. **All FOUR predecessor LOCK ceremonies remain OPERATOR-GATED entering Day 60 — file-state confirmed (version tags unflipped). Same forward-design posture as partial 1.**

> **Cadence honesty (on schedule — surfaced):** The Day 58 outline calendared partial 1 for Day 59 (Wed Jun 17) and partial 2 for **Day 60 (Thu Jun 18)**. On-disk file-state confirms the chain is intact: Day 59 partial 1 shipped (Wed Jun 17), Day 58 outline before it (Tue Jun 16). Tonight's Day 60 session ships partial 2 (this document) ON the outline calendar — no slip. Next Rest Day: Day 63 (Sun Jun 21).

> **Authoring discipline (LOCK signal):** §8 + §9 + §11 + §12 + §15 + §16 are LOCKED-as-drafted Day 60. §13 carries the only two forward-looking edit slots in the entire SPEC (D6 8-tuple + D15 Editor-handoff — both operator-gated). Everything else is canon as of this document. With partial 1's §6/§7/§10/§14, the Edit Director v1.0 SPEC body is now complete end-to-end.

> **LOCK-state awareness (CRITICAL — do not silently advance):** On-disk file-state confirms all four predecessor LOCK ceremonies remain OPERATOR-GATED (version tags unflipped; Day 36 + Day 47 + Day 57 runbook executions unconfirmed). Edit Director v1.0 LOCK hard-gates on those closing + the Cross-SPEC §3.9 ratification. The **Ingest 7-tuple LOCK is Edit Director's DIRECT 8-tuple dependency**, and the Ingest LOCK is itself behind the QC 6-tuple LOCK. This partial is forward-design over LOCK-stable text artifacts only; zero production output consumed, zero operator ceremony assumed.

---

## §8 — Performance Targets (LOCKED-as-drafted Day 60)

Nine metric categories, per the outline §8 preview and the partial 1 §14.2 runway. Pattern parity: Ingest §8 / QC Pre-flight §8 / AI Video Gen §8 (category → target → measurement → rationale). Edit Director's defining posture: **a $0, render-free, almost-entirely-deterministic creative-direction agent must be judged on brand-rule catch-rates, shape-validity, and the asymmetry of its one judgment slot — there is no render quality to score, only plan correctness and brand compliance.**

| # | Metric category | v1.0 target | Measured how | Rationale |
|---|----------------|-------------|--------------|-----------|
| 1 | **Schema validity** | **100%** of emissions validate against `output.schema.json` (success — incl. `revise` — AND error branches) | Validator harness on every fixture run + every runbook case | The edit plan is the Editor's source of truth and the orchestrator parses it blind. A malformed plan is a pipeline-halting defect by definition. No tolerance. |
| 2 | **Brand-edit-rule catch** | **100%** of seeded hard-rule violations caught (a fade/wipe/zoom, an all-caps lower-third, a reel-level sales CTA, a missing end-card must NEVER survive to `plan_ready`) | TC-04 class fixtures: each hard brand-edit rule violated in isolation; `brand_edit_check` sub-status audited | A brand-defective plan reaching the Editor burns a full cut cycle and can surface on a PUBLISHED reel. The `brand_edit_check` booleans make this a deterministic conjunction — anything below 100% means a rule is unenforced. Zero tolerance (D9). |
| 3 | **Authored-text firewall catch (9th pass)** | **100%** of seeded banned tokens in AUTHORED lower-thirds / caption lines / the end-card line caught | TC-05 class fixtures: tokens injected into the copy Edit Director WRITES, across all 11 firewall entries + conjugates | The 9th pass is the FIRST over self-authored text — no content pass scans the copy Edit Director itself writes. By construction the check is a deterministic token-boundary scan; below 100% means the scan is broken. A miss here would be burned into a cut. |
| 4 | **Duration-in-band** | **100%** of plans emitted with `plan_ready` have `45000 ≤ total_duration_ms ≤ 75000` | Fixture + runbook: `structure_check.total_duration_ms` audited against the 45–75s band | An out-of-band reel violates the §8 brand format spec. The trim math is deterministic (sum of cut windows + end-card hold); 100% is structural. Out-of-band after trim is a valid `fail` (`duration_envelope_breach`), never a `plan_ready` escape. |
| 5 | **False-plan-ready rate** | **0%** (ZERO tolerance — D9/D12) | Across the full fixture corpus + runbook: no `plan_ready` verdict on any reel seeded with any hard defect | A brand-defective or structurally-incomplete plan reaching the Editor burns an edit cycle and poisons downstream trust. Bias all ambiguity toward `fail` or `revise`. The expensive failure direction is the one we never accept. |
| 6 | **False-fail / over-revise rate** | **≤ 8%** | Clean fixtures (TC-01/TC-02 class): proportion incorrectly failed OR incorrectly routed to `revise` | Over-flagging is the acceptable failure direction — a false `fail`/`revise` costs one re-adjudication or one operator creative call (~$0); a false `plan_ready` costs a cut cycle. The ≤8% ceiling is slightly looser than Ingest's ≤5% **because Edit Director carries one genuinely subjective surface** (soft brand-rule tension → `revise`), where some over-flagging is correct conservatism, not error. Asymmetric tolerance is deliberate. |
| 7 | **Latency** | **p50 ≤ 30s · p95 ≤ 90s** per reel | Wall-clock per runbook case + fixture run | Reasoning + plan authoring, no engine wait, no render, no decode I/O. Slightly higher than Ingest's p50 25s / p95 75s because authoring a cut/caption/lower-third/swell plan is more generative work than normalizing a manifest — but Edit Director must still never be the pipeline's bottleneck. |
| 8 | **Cost** | **$0.00 engine + $0.00 render — structurally guaranteed** | Audit: zero engine calls, zero render dispatch, `render_dispatched: false` on every emission | Hard Rule #2. Cost here is not a budget to manage but an invariant to attest. Any non-zero engine/render figure = a Hard Rule violation, not an overrun. Ties Ingest / QC Pre-flight for lowest in the fleet. |
| 9 | **Self-QC first-pass yield** | **≥ 90%** of emissions pass the 11-check list on attempt 1; retry (2-strike) consumed in **≤ 10%** of runs; `edit_director_agent_failed` halt rate **< 2%** | `attempts` field census across fixture + runbook corpus | The 2-strike retry exists for resilience, not as a crutch. High retry consumption means the plan constructor is sloppy; a high slot-11 rate means the agent design itself is defective. |

**Measurement context (v1.0):** All targets are adjudicated against the §9 fixture portfolio + the LLM-test runbook corpus (operator-executed, paste-and-run, $0). No live-pipeline telemetry exists until the orchestrator ships — these are design-acceptance targets, re-baselined when runtime telemetry lands (v1.1).

**Targets NOT carried (deliberate, surfaced):** No render-quality metric (Editor's domain, position 11), no LUFS/loudness metric (Sound's domain, position 12), no asset-validity metric (Ingest's jurisdiction — Rule re-adjudication ban), no cost-ceiling adherence metric (QC Pre-flight's authority — Hard Rule #10), no brand-voice quality score (Script/QC jurisdiction). Edit Director's scoreboard measures exactly its own job: author a brand-compliant, structurally-complete cut plan; catch every hard brand violation and every authored-text leak; over-flag conservatively; stay fast; stay free.

---

## §9 — 5 Test Fixtures (LOCKED-as-drafted Day 60)

Pattern source: Ingest §9 / Style Replication §9 / QC Pre-flight §9. Fixture contract: each = **(input.json, expected_output.json, expected_verdict, expected_code_or_null, scenario_description)**. Fixtures live at `skills/edit-director-agent/tests/` (authored on the SKILL-bundle day; this section is their binding specification). All fixtures use the canonical REINVENTED brand-anchor (Cross-SPEC fixture canon) and platform-relative `ars://` URIs. **5 of the 9 LOCKED codes are exercised behaviorally; the remaining 4 (`upstream_ingest_not_passed`, `upstream_not_success`, `beat_map_unmappable`, `caption_spec_violation`, `cut_order_incomplete`, `duration_envelope_breach`, `plan_lineage_failure`) + slot-11 + the `revise` verdict are exercised schema-only** (enum-presence validation) or in the runbook's adversarial case, mirroring the fleet's fixture-economy precedent. The behavioral 5 are chosen to cover the two highest-stakes Edit-Director-original surfaces (the mode-blind convergence proof, the authored-text firewall) plus the two PASS-side anchors.

### TC-01 — Clean Mode-A-origin → manifest, Pro reel → PLAN_READY (full plan)

- **Scenario:** An Ingest-passed (verdict `pass`) Pro reel whose Asset Manifest originated from Mode A (human footage): full `asset_bundle.raw_footage` (6 shots, declared `duration_sec` each), Storyboard frame-language per shot, Script beat map (hook→3-beat→CTA, captions, on_screen_text, 165wpm voice_pacing), music bed present, full coverage, firewall-clean upstream text, 7-tuple inbound parent_chain.
- **Expected verdict:** `plan_ready` · **Expected code:** `null`
- **Asserts:** `successEditPlan` validates; `edit_plan` carries a complete `cut_order[]` (≤12 Pro cut beats, every `in_ms < out_ms ≤ duration_sec*1000`, no double-spend, no timeline gap); `pacing_bpm` + `cut_rhythm` derived from 165wpm + declared music tempo; `caption_lines[]` all ≤22 chars; `lower_thirds[]` all `case: "lowercase"`, `align: "left"`; `transitions` = hard-cuts-only; `music_swell_map[]` length == 2 (Pro); mandatory `end_card` present (`"REINVENTED — build on purpose."`, `hold_ms: 1500`); `structure_check {hook_window_ok, body_beats: 3, cta_internal_question_ok, total_duration_ms ∈ [45000,75000], duration_in_band: true}`; all 7 `brand_edit_check` booleans `true`; `edit_plan_firewall_pass_9 {status: "clean", hits: 0}` with census matching the authored-field count; `mode_blind_confirm {production_mode_read: false, consumed: "mode_agnostic_manifest"}`; `render_dispatched: false`; `route_back_to: null`; `handoff_targets: ["editor-agent"]`; `human_review_required: true`; ≥4 snake_case `qc_pre_flags[]`; `plan_evidence_hash` matches `^[a-f0-9]{64}$`; parent_chain extended to 8-tuple additively.

### TC-02 — Clean Mode-C-origin Enterprise reel → PLAN_READY (mode-blind convergence proof)

- **Scenario:** An Ingest-passed Enterprise reel whose Asset Manifest originated from Mode C (replicated hot-path): 8-shot bundle, all declared specs match the Enterprise platform target, full coverage, firewall-clean. The ONLY input difference from TC-01 is `metadata.production_mode == "C"` and the richer Enterprise envelope.
- **Expected verdict:** `plan_ready` · **Expected code:** `null`
- **Asserts:** The authored plan is **byte-shape-identical** to TC-01's downstream of the `tier_richness` block — the cut-order authoring, caption logic, lower-third logic, firewall pass, and `mode_blind_confirm` are produced by an IDENTICAL code path despite the different origin mode (this pair IS the **mode-blind convergence proof** — the Edit-Director analog of Ingest's mode-convergence proof, Check #10). `mode_blind_confirm.production_mode_read: false` (the agent never consulted the origin mode); no mode-conditional field leaks into the plan; `tier_richness` honors the Enterprise ceilings (≤12 cut beats, unlimited b-roll, 3 music swells, 5 variants flagged) while EVERY brand rule (hard-cuts-only, one-emotional-beat, end-card, internal-question CTA) is identical to the Pilot/Pro path. **This fixture is the convergence payoff Ingest unlocked — the first fleet test where the mode columns are behaviorally identical.**

### TC-03 — Coverage gap re-confirm fails → FAIL + route to Ingest

- **Scenario:** A reel where Ingest's manifest is consumed but the defensive re-confirm finds `coverage_check.coverage_complete == false` / `spec_check.missing_shots == [4]` (a shot the cut structure needs has no resolvable asset) — the boundary case where an Ingest-pass and Edit Director's re-confirm disagree, which must halt rather than author a cut over a hole.
- **Expected verdict:** `fail` · **Expected code:** `incomplete_shot_coverage`
- **Asserts:** `errorEnvelope` with `failed_check_id: 3` (coverage branch); `coverage_remap {shots_required, shots_mapped, unmapped_shot_refs: [...], unmapped_beats: [4]}` internally consistent (no phantom mapping); `route_back_to: "ingest-agent"` (the coverage owner per the §6.3 / §3.2 route map); `detail` names the unfilled structure window; verdict is `fail` NOT `revise` (a coverage hole is a hard structural defect, not a creative tension); `human_review_required: true`. **The re-confirm is defensive, not redundant — Edit Director cannot direct a cut over a hole even if Ingest passed it.**

### TC-04 — Brand-edit rule conflict (a beat that only resolves with a fade) → hard FAIL

- **Scenario:** A Pro reel whose only coherent cut between beats 2 and 3 would require a cross-fade (the available shots cannot hard-cut cleanly without a jarring jump), and no alternate ordering avoids it. Every other gate is clean. The hard-cuts-only rule is NON-NEGOTIABLE (brand canon §7), so this cannot be silently overridden.
- **Expected verdict:** `fail` · **Expected code:** `brand_edit_rule_conflict`
- **Asserts:** `failed_check_id: 7` (hard-rule branch); `brand_edit_check.hard_cuts_only: false` with all other sub-statuses still explicitly computed (no short-circuit nulls); `detail` names the offending beat transition + the rule violated; verdict is `fail` NOT `revise` (a HARD brand rule that cannot be satisfied is a hard fail — `revise` is reserved for SOFT-rule creative tension, not non-negotiable violations); `route_back_to: "production-coord-agent"` (the cut cannot be filled from current assets/intent — re-spec the shot coverage). **This fixture is the zero-tolerance brand-edit firewall's existence proof: a fade must NEVER survive to `plan_ready`.**

### TC-05 — Authored-text firewall breach (banned token in a LOWER-THIRD Edit Director WROTE) → hard FAIL (the 9th-pass new-surface catch)

- **Scenario:** A Mode-B-origin reel, all upstream content fully clean (Ingest's 8th pass passed it; all 8 prior passes would pass it) — but during caption/lower-third authoring the agent composes a lower-third reading `built for operators like sln` (firewall entry #4 token in the copy Edit Director itself WROTE) and a caption line referencing `holdcogroup.com`.
- **Expected verdict:** `fail` · **Expected code:** `edit_plan_firewall_breach`
- **Asserts:** `failed_check_id: 4`; `edit_plan_firewall_pass_9 {status: "breach", authored_text_fields_scanned: N, hits: 2}` with `authored_text_fields_scanned` matching the true authored-field census (every lower-third + caption line + the end-card); forensic `detail` names BOTH leaking AUTHORED fields + the rule each violated; the catch occurs on a surface NO content pass and NO prior firewall pass could see — **this fixture is the 9th pass's existence proof** (the FIRST firewall over self-authored text); entity firewall list applied verbatim (11 entries, token-boundary, case-insensitive). **The single highest-stakes code in the namespace — a leak here would be burned into a published cut.**

### 9.1 Fixture-economy rationale (surfaced)

The unexercised codes are all either **deterministic entry/forensic halts** (`upstream_ingest_not_passed`, `upstream_not_success`, `plan_lineage_failure` — single equality/shape assertions, behaviorally trivial, schema-enforced, identical in mechanism to the fleet's proven entry-gate fixtures) or **substance codes whose mechanic is fully covered by a sibling behavioral fixture** (`beat_map_unmappable` shares TC-03's coverage-remap machinery; `cut_order_incomplete` and `duration_envelope_breach` share TC-04's structural-adjudication machinery; `caption_spec_violation` is a deterministic ≤22-char length assertion). Spending fixture slots on them would displace the two clean-PLAN_READY convergence proofs (TC-01/TC-02) and the two highest-stakes Edit-Director-original catches (TC-04 hard brand conflict, TC-05 authored-text firewall) that no other test can provide.

**The `revise` verdict is exercised in the runbook's adversarial case, not a fixture** — by design it requires inducing a genuine SOFT-rule creative tension (e.g. a 4th body beat that strengthens the cut against the one-emotional-beat rule), which is a judgment surface better probed by the operator-executed runbook than asserted as a fixed expected_output. Slot-11 (`edit_director_agent_failed`) is definitionally un-fixturable from outside (it requires inducing the agent to build a malformed plan twice); the runbook's adversarial case covers its semantics. Same economy Ingest ratified at Day 52 and QC Pre-flight at Day 43.

---

## §11 — Cost Model (LOCKED-as-drafted Day 60)

### 11.1 Zero-engine, zero-render snapshot (v1.0)

| Cost component | Per-reel v1.0 | Mechanism |
|----------------|---------------|-----------|
| Generative engine calls | **$0.00** | None — structurally banned (Hard Rule #2) |
| Media render / transcode / conform / EDL execution | **$0.00** | None in v1.0 — plan authoring only; `render_dispatched: const false`. Rendering is Editor's job (position 11). |
| Byte-level audio decode (beat detection) | **$0.00** | None in v1.0 — declared-tempo + wpm heuristic only (Hard Rule #9); beat-sync deferred to v1.1 |
| LLM reasoning (plan authoring + adjudication) | **≈ $0.03–0.10** | One model pass over the manifest + creative-intent inputs + plan assembly; bounded by the p95 90s latency envelope. Slightly higher than Ingest's $0.02–0.08 — authoring a cut/caption/swell plan is more generative than normalizing a manifest. |
| Native compute / storage | **$0.00** | No fetch, no transcode, no asset movement — Edit Director reads the manifest + intent and emits one JSON plan |
| **Total `cost_incurred_usd`** | **≈ $0.00 (reported to 2dp)** | Carried in `metadata` per Cross-SPEC §3.9 |

Edit Director holds **no cost ceiling and no ledger authority** (Hard Rule #10 — QC Pre-flight's jurisdiction). The tier ceilings are upstream facts, enforced two gates back; restated for traceability only, NOT re-litigated.

### 11.2 Directed-coherence value model (the economic justification)

Edit Director produces no margin directly. Its value is **first-pass brand-compliant direction + downstream-cost prevention**, quantified across the defect classes it uniquely prevents:

| Prevented failure | Without Edit Director | Cost of the miss | Edit Director catch cost |
|-------------------|----------------------|------------------|--------------------------|
| **Ad-hoc / inconsistent cut reaches the Editor** | Editor improvises order, pacing, captions per reel; no deliberate brand-compliant assembly; quality varies reel-to-reel | Inconsistent brand output at scale + re-cut churn; the agency-quality promise erodes | ≈ $0.00 + ≤90s |
| **A brand-edit violation (fade/wipe/zoom, all-caps lower-third, sales CTA, missing end-card) survives to a cut** | Editor cuts it; the defect surfaces post-Motion or on a PUBLISHED reel | 1 wasted cut cycle ≈ 2–6 operator-hours + 1–2 day reel slip; at commercial tiers, a blown brand-consistency SLA | ≈ $0.00 + ≤90s |
| **An entity leak in AUTHORED copy reaches a published surface** | A banned token Edit Director WROTE into a lower-third/caption survives to export (burned into the cut, into thumbnails, into platform metadata) | Brand-safety incident on a PUBLISHED surface — reputational, not monetary; the one failure class with no post-hoc fix | ≈ $0.00 + ≤90s (9th pass) |
| **A creative judgment is silently auto-resolved (a brand rule overridden OR a stronger cut dropped)** | The agent picks a side without a human; brand erosion OR creative loss, invisibly | Either a brand-rule breach or a weaker reel — both silent, both compounding | ≈ $0.00 (`revise` → Lever-3) |

**The asymmetry is the whole argument:** every defect Edit Director can catch costs effectively nothing to catch and materially more to miss — and the one genuinely subjective call (`revise`) is routed to a human rather than auto-resolved in either wrong direction. A creative-direction gate with a $0 toll, a 100%-hard-rule-catch mandate, and a human-in-the-loop slot for the one judgment surface is pure option value — which is why the universal-tier table opens it to every reel at every tier with no ceiling, scaling only richness. ROI formalization against live defect telemetry is a v1.1 task (no real corpus exists pre-orchestrator).

---

## §12 — Verdict Math (LOCKED-as-drafted Day 60)

### 12.1 The ∧-of-gates composition (with the one judgment slot)

Deterministic boolean composition over declared evidence on the HARD rules — **no thresholds, no weights, no scores on the deterministic surface** — with exactly ONE subjective branch (`revise`) carved out for soft brand-rule creative tension:

```
PLAN_READY = (ingest_precondition_met)        # Check 1  — manifest verdict == "pass" ∨ lever3_signoff
           ∧ (upstream_success)               # Check 2  — no errorEnvelope branch consumed
           ∧ (coverage_complete)              # Check 3  — coverage_complete ∧ missing_shots == []
           ∧ (beat_map_mappable)              # Check 3  — every shot_ref ↔ a Script/Storyboard beat
           ∧ (authored_text_firewall_clean)   # Check 4  — hits == 0 (9th pass, self-authored surface)
           ∧ (cut_order_covers_structure)     # Check 5  — hook→3-beat→CTA, no double-spend, no gap
           ∧ (duration_in_band)               # Check 6  — 45000 ≤ total_duration_ms ≤ 75000
           ∧ (all_hard_brand_rules_satisfied) # Check 7  — hard_cuts_only ∧ end_card ∧ lower_thirds_lowercase_left ∧ no_reel_level_sales_cta
           ∧ (captions_within_char_limit)     # Check 8  — every caption_lines[].text ≤ 22 chars
           ∧ (mode_blind)                      # Check 10 — production_mode_read == false
           ∧ (lineage_intact)                  # Check 9  — well-formed inbound tuple + valid 8-tuple extension
```

### 12.2 Non-pass routing (the verdict function — three outcomes)

Any single ∧-term false → the verdict function routes per the §6.3 / §3.2 map. The `revise` branch is reached ONLY by a soft-rule tension, never by a hard-rule failure:

```
# Halts (entry / forensic gates)
if ¬ingest_precondition_met       → halt  upstream_ingest_not_passed
if ¬upstream_success              → halt  upstream_not_success
if ¬lineage_intact                → halt  plan_lineage_failure            (forensic)
if ¬mode_blind                    → halt  edit_director_agent_failed      (slot-11 — agent read production_mode)

# Fails (substance adjudications)
if ¬coverage_complete             → fail  incomplete_shot_coverage        (route_back: ingest-agent)
if ¬beat_map_mappable             → fail  beat_map_unmappable             (route_back: ingest-agent | production-coord-agent)
if ¬cut_order_covers_structure    → fail  cut_order_incomplete            (route_back: production-coord-agent)
if ¬duration_in_band              → fail  duration_envelope_breach        (surface trim options)
if ¬all_hard_brand_rules          → fail  brand_edit_rule_conflict        (forensic log + rule named)
if ¬captions_within_char_limit    → fail  caption_spec_violation          (re-author line ≤22 chars)
if ¬authored_text_firewall_clean  → fail  edit_plan_firewall_breach       (forensic log + authored field named)

# Revise (the ONE judgment slot — a successEditPlan-shaped payload, NOT an errorEnvelope)
if (all_hard_rules_pass) ∧ (soft_brand_rule_tension)
                                  → revise  verdict: "revise"             (route_back: null; revise_rationale; held for Lever-3)
```

**Precedence:** halts (entry/forensic/mode gates) adjudicate before fails; among fails, the FIRST failing check in §6.2 tier order names the headline `failure_code`, with all computed evidence still emitted (no short-circuit nulls — every sub-status explicitly dispositioned regardless of the headline). `revise` is reachable ONLY when EVERY hard term is true AND Check #7 surfaces a soft-rule tension (Check #7's soft branch is the sole non-deterministic surface).

### 12.3 Properties (why this is the right math for a creative-direction gate)

1. **Deterministic on the hard rules** — same inputs, same verdict, every run, for every term except the one soft-rule tension surface. The LLM is constructing + attesting on the hard rules, not judging on a gradient.
2. **Monotone on the hard rules** — adding a defect can never improve the verdict. There is no compensatory scoring where a strong cut offsets a banned-token lower-third or an out-of-band duration.
3. **Zero-false-plan-ready by construction** — `plan_ready` requires EVERY hard term true; ambiguity biases to `fail` or `revise` (Hard Rule #12). The 0% false-plan-ready target (§8.5) is a property of the composition, not a tuned threshold.
4. **The one judgment slot is isolated and routed to a human** — `revise` is the ONLY non-deterministic branch, it cannot be reached while any hard rule fails, and it never auto-resolves; it surfaces to Lever-3 with a `revise_rationale`. This is the deliberate, bounded subjectivity a creative-direction agent needs — contained to exactly one surface, defaulting to human ratification (the QC-`hold` analog).
5. **Auditable** — the emitted plan carries the evidence for every term (§10 per-check evidence rows), so any verdict is recomputable by a human from the plan alone. Recommend-don't-approve depends on exactly this recomputability.

**Divergence from Ingest's binary-plus-reshoot (surfaced):** Ingest's domain is deterministic (a file is present or absent), so its outcomes are strictly `pass/fail/reshoot` with NO soft-hold. Edit Director's domain is partly creative — most deterministic (a fade appears or it doesn't; a caption fits 22 chars or it doesn't) but with ONE genuine judgment surface. So Edit Director carries `revise` exactly where QC Pre-flight carried `hold`, and for the same reason: a subjective creative judgment only a human can ratify. Everything else stays binary.

---

## §13 — Critical Decisions (Day 60 walk — 13 LOCKED-as-drafted · 2 carried open for operator)

Target was 10–14 LOCKED (outline §13). The Day 60 walk lands **13 LOCKED-as-drafted** (within target), with **2 carried open** — both operator-gated, both drafted to Donna's recommended default so the SPEC is buildable while the gates close. **Per the process-integrity attestation, Donna does NOT ratify PRELIMINARY/critical-decision items — D6 and D15 are surfaced, not advanced.** The 14-item outline scaffold maps below, with the Editor-handoff target (Open Question 4) added as D15.

| # | Decision | Status | Resolution |
|---|----------|--------|------------|
| D1 | Plan-authoring vs render scope — v1.0 = **edit-PLAN authoring ONLY**; actual cut execution is Editor (position 11), human-in-the-loop at launch | **LOCKED-as-drafted Day 58** | Resolves outline Open Question 1 per recommendation: the plan is the buildable, highest-leverage slice; the EDL/conform emit lands when Editor automation ships Week 4–5. `render_dispatched: const false` is the honesty contract. |
| D2 | Universal tier access + tier-sensitive richness — all 4 tiers reach Edit Director; plan richness scales by tier, brand-rule compliance does NOT | **LOCKED-as-drafted Day 58** | Edit Director is a creative authority whose output richness IS a sold tier feature (8 vs 12 cut beats, b-roll ceilings, swell counts, variant counts). Richness ladder inherited from the Script Day 9 table. |
| D3 | Mode-blind by construction — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested | **LOCKED-as-drafted Day 58** | The first contractually mode-blind agent — the live, machine-checkable proof that Ingest's mode-convergence seam holds. Check #10 + TC-01/TC-02 convergence proof. |
| D4 | Ingest-pass precondition absolute — runs only on a `successAssetManifest`/`pass` (or Lever-3 approved) reel; else halts `upstream_ingest_not_passed` | **LOCKED-as-drafted Day 58** | Edit Director never directs an un-ingested reel; Lever-3 sign-off is the only bypass. Check #1 runs FIRST. |
| D5 | No content re-authoring — Edit Director directs the ASSEMBLY of validated assets; it does NOT rewrite Script copy or re-frame Storyboard shots | **LOCKED-as-drafted Day 58** | Script wrote the copy; Storyboard framed the shots. Edit Director decides order, pacing, caption timing, lower-third schedule, swells, transitions. A caption that can't fit 22 chars → `caption_spec_violation`, NOT a paraphrase. Hard Rule #8. |
| D6 | **8-tuple parent_chain** — inherits Ingest 7-tuple + appends `edit_plan_id` (UUIDv7) | **TRIPLY-DEFERRED — operator-gated** | Held additively (`minItems: 5`, `prefixItems` 0–7, `maxItems: 8`, `items: false`) pending the Cross-SPEC §3.9 ratification AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it. `TODO@cross-spec-3.9-ratification` flip note embedded for the schema author. Edit Director is the THIRD forcing function for the amendment. **NOT advanced tonight.** |
| D7 | errorEnvelope code count → **9 LOCKED + slot-11** | **RESOLVED Day 59 → LOCKED-as-drafted** | Settled within the 7–9 target. `duration_envelope_breach` kept STANDALONE (NOT folded — opposite of Ingest's fold) because at the authoring layer it has a distinct recovery path (re-trim the cut, not re-spec an asset). Namespace-cardinality rationale at §6.3. |
| D8 | Self-QC check count → **11** | **RESOLVED Day 59 → LOCKED-as-drafted** | Within the 10–12 target; 4-tier ordering (entry / substance / forensic / plan-construction). |
| D9 | Brand-edit-rule compliance = ZERO tolerance — a fade/wipe/zoom, an all-caps lower-third, a reel-level sales CTA, or a missing end-card must NEVER survive to `plan_ready` | **LOCKED-as-drafted Day 58** | §12.3 makes it structural; §8.2 makes it measured (100% catch). A hard violation → `brand_edit_rule_conflict` (fail), never `revise`. |
| D10 | `revise` verdict for soft-rule tension — Edit Director surfaces a creative judgment call to Lever-3 rather than silently overriding a brand rule OR silently dropping a stronger cut | **LOCKED-as-drafted Day 58** | Resolves outline Open Question 2 per recommendation. The first fleet agent with a 3-verdict success-side; `revise` is a `successEditPlan`-shaped payload, the QC-`hold` analog. The one isolated judgment slot (§12). |
| D11 | No render, no engine — NO generative engine calls, NO media render in v1.0; `render_dispatched: const false` | **LOCKED-as-drafted Day 58** | Hard Rule #2. The forged-provenance framing ("a plan claiming a render it never dispatched") is the defining negative constraint. Ties Ingest / QC Pre-flight for $0. |
| D12 | Recommend-don't-approve — `human_review_required: true` on every emission; verdict is a plan RECOMMENDATION, never a ratified "approved-for-cut" state | **LOCKED-as-drafted Day 58** | Hard Rule #12. The operator clears; the agent never does. Lever-3 default. |
| D13 | Authored-text firewall (9th pass) — Edit Director firewall-scans the text it AUTHORS (lower-thirds, captions, end-card), a NEW surface no prior agent owned | **LOCKED-as-drafted Day 58** | The first firewall over self-authored copy. §6.5 list applied verbatim (11 entries). TC-05 is its existence proof. |
| D14 | Multi-variant scope — v1.0 authors the primary 9:16 plan + flags `variants_planned` count; auto-cutdown generation (1:1 LinkedIn) deferred to v1.1 | **LOCKED-as-drafted Day 60** | Resolves outline Open Question 5 per recommendation: a cutdown is a derived re-plan, lower-leverage than the primary. Authoring-level scope-narrowing inside the pre-approved recommendation (Donna-resolvable, same class as Ingest's D14 duration-fold). `variant_plans[]` reserved in the §10.2 field map. |
| D15 | **Editor handoff target** — v1.0 emits the plan to the **Notion Edit Plan block (holding store)**; direct agent-to-agent handoff activates when Editor (Agent #10) LOCKs | **PRELIMINARY — drafted to recommended default · operator ratification pending** | Outline Open Question 4. Donna recommends the holding store: Editor does not exist yet, and a plan emitted into a void is an audit-trail break. `handoff_targets: ["editor-agent"]` names the LOGICAL target; the PHYSICAL v1.0 destination is the Notion Edit Plan block (per Blueprint §7 I/O — mirrors the Ingest→Notion-Asset-Manifest holding-store decision, Ingest D15). **Operator may override on this walk's review.** Directly tied to Ingest Day 53 Item 8 (D15-of-Ingest = the Edit-Director handoff target). |

**Decision-walk integrity note:** D7/D8 were PRELIMINARY at Day 58, resolved by the Day 59 partial 1 authoring exactly as the outline's recommended defaults, and are LOCKED-as-drafted here; D14 is a Donna-resolvable scope-narrowing inside the pre-approved recommendation (same class as Ingest's D14 duration-fold). D6 and D15 are *operator-only* (a Cross-SPEC amendment ratification + a triply-gated lineage flip; and a pipeline-topology commitment) and remain open. This is the same Donna-resolvable vs operator-only line the Ingest Day 52 and QC Pre-flight Day 43 walks drew.

---

## §15 — Change Log + Version History (LOCKED-as-drafted Day 60)

| Version tag | Day | Date | Event |
|-------------|-----|------|-------|
| v1.0-draft-day-58 | 58 | Tue Jun 16 | Outline §0–§5 SHIPPED (`ARS-2026-06-16-Day-58-Edit-Director-Agent-SPEC-Outline.md`) — 6 open questions parked |
| v1.0-draft-day-59 | 59 | Wed Jun 17 | Body partial 1: §6/§7/§10/§14 LOCKED-as-drafted; namespace settled 9+slot-11; self-QC settled 11; 3-verdict model with `revise` settled; duration kept standalone |
| v1.0-draft-day-60 | 60 | Thu Jun 18 | **Body partial 2 (this document): §8/§9/§11/§12/§15/§16 LOCKED-as-drafted; §13 walk = 13 LOCKED + D6/D15 carried open. SPEC body §0–§16 COMPLETE.** |
| v1.0-LOCK-CANDIDATE | 61+ | TBD | Assembly of the full SPEC + cross-SPEC §3 full audit + 15-decision walk staged for operator (hard-gated: 4 predecessor LOCKs + §3.9 ratification) |
| v1.0-schemas | TBD | TBD | `input.schema.json` + `output.schema.json` per §10.4 authoring notes (the 8-tuple additive hold + the brand-rule `const`s) |
| v1.0-SKILL | TBD | TBD | `skills/edit-director-agent/` bundle + §9 fixtures at `tests/` |
| v1.0-runbook | TBD | TBD | LLM-test runbook (operator paste-and-run, 5 cases + the `revise` + slot-11 adversarial probes) |
| v1.0-LOCKED | TBD | TBD | **Operator LOCK ceremony** — tag flip + Notion + chip (operator-only) |

**Parked candidates (v1.1+ register):** `variant_plans[]` auto-cutdown activation (D14 v1.1 condition), `cut_order[*].frame_exact` sub-frame conform (needs real media + the Editor runtime), `music_swell_map[*].beat_synced` (needs byte-level decode), `edit_plan.alt_cut` (A/B directed version), the `revise` verdict's full creative-tension taxonomy (telemetry-driven), direct Editor handoff (D15 activation condition), live-telemetry re-baseline of §8 targets.

---

## §16 — Metadata Block Schema (LOCKED-as-drafted Day 60)

Cross-SPEC §3.9 canonical fields + **5 Edit-Director additions**. Pattern source: Ingest §16 / QC Pre-flight §16 / AI Video Gen §16. This is the binding contract for the schemas-day `metadata` object:

```
"metadata": {
  // ---- Cross-SPEC §3.9 canonical (inherited verbatim) ----
  "agent_id":            "edit-director-agent",            // const
  "agent_version":       "1.0",                            // semver string
  "production_mode":     "A" | "B" | "C",                  // PRESENT for audit lineage; NOT read as a branch (Hard Rule #6)
  "brand_id":            "REINVENTED",                     // v1.0 expected value
  "parent_chain":        [ ... ],                          // see addition 1
  "cost_incurred_usd":   0.00,                             // ≈ $0 — reasoning + plan authoring only
  "human_review_required": true,                           // const true (Hard Rule #12 — recommend-don't-approve)
  "timestamp_utc":       "<ISO-8601>",

  // ---- Edit-Director additions (5) ----
  "edit_plan_class":           "primary_9x16",             // 1. enum: ["primary_9x16"] v1.0 · "variant_cutdown" reserved v1.1+
  "plan_evidence_hash":        "<sha256-hex-64>",          // 2. SHA-256 over the edit_plan + brand_edit_check block (^[a-f0-9]{64}$)
  "render_dispatched":         false,                      // 3. const false v1.0 (authors a plan, renders nothing; flips relevance at Editor)
  "runtime_environment_class": "dev"|"staging"|"production", // 4. inherit AI Video Gen §16
  "edit_plan_id":              "<UUIDv7>"                  // 5. this agent's emitted identity (also parent_chain[7])
}
```

**Addition 1 — `parent_chain` (the triply-deferred 8-tuple):** `prefixItems` positions 0–7 = `[brief_id, script_id, storyboard_id, production_plan_id|rendered_shots_set_id, replication_set_id, preflight_report_id, asset_manifest_id, edit_plan_id]` · `minItems: 5` · `maxItems: 8` · `items: false`. Accepts the 5-tuple (pre-ratification), the 6-tuple (QC Pre-flight extension pending its LOCK), the 7-tuple (Ingest extension pending its LOCK), and the 8-tuple (this agent's append). Rejects a 4-tuple. `TODO@cross-spec-3.9-ratification` flips `minItems` to 8 ONLY after all three gates close (D6). The schema author copies this constraint verbatim per §10.4.

**Mode-blind self-attestation block (the §16 companion — NOT in `metadata` but in the success payload root):** `mode_blind_confirm: {production_mode_read: false (const), consumed: "mode_agnostic_manifest" (const)}`. Encoded at the schema layer as the machine-checkable convergence guarantee (§10.4). This is the structural difference from every prior agent's §16: Edit Director's metadata carries `production_mode` for audit lineage, but a sibling root-level block attests it was never READ — the live proof of Ingest's convergence seam.

**Schema-day cross-references:** `output_type` oneOf split (`successEditPlan` | `errorEnvelope`), the 9-code + slot-11 `failure_code` enum (`duration_envelope_breach` STANDALONE, NOT folded — per D7), the `verdict` enum WITH `revise` (`["plan_ready", "fail", "revise"]` — `revise` is a SUCCESS-side payload, the divergence from Ingest's pass/fail/reshoot and QC's pass/fail/hold), the `ars://` URI pattern, `caption_lines[*].text maxLength: 22`, `transitions const` (hard-cuts-only), `lower_thirds[*].case const "lowercase"` + `align const "left"`, `end_card.line const` + `hold_ms const 1500`, `render_dispatched const false`, `mode_blind_confirm.production_mode_read const false`, and `brand_edit_check` sub-booleans all required-on-success — all per §10.4, restated here as the single checklist the schema author works from.

---

## Day 61+ runway (next forward deliverable)

**Next up: Edit Director Agent v1.0 LOCK CANDIDATE assembly (Day 61, Fri Jun 19)** — merge outline (Day 58) + partial 1 (Day 59) + partial 2 (this document) into the single LOCK-candidate document, run the FULL Cross-SPEC §3 audit (11 dimensions, LOCK-grade), final bipartite-coverage proof (11 checks × 9 codes + slot-11), the full verdict math, and stage the 15-decision §13 walk for the operator. Then schemas (Day 62) → Rest Day (Day 63) → SKILL bundle (Day 64) → runbook (Day 65+) per the §15 lifecycle. The LOCK itself remains hard-gated on the four predecessor ceremonies + the §3.9 ratification (all operator-pending — see partial 1 §14.4–14.7). The **Ingest 7-tuple LOCK is the direct 8-tuple dependency**.

---

## Mirror status

- Source: `ars/ARS-2026-06-18-Day-60-Edit-Director-Agent-SPEC-Body-Partial-2.md` (this document) + `ars/build-log-2026-06-18.md`
- Mirror destination: `/outputs/ars/` (both files)
- Mirror verification: in this session's mirror step.

---

## Process integrity (Day 60)

- ✅ **No LLM dispatched. No engine, no render, no byte-probe, no network, ZERO $ spent.** Validation was structural (pattern parity vs Ingest Day 52 partial 2 + §12 composition audit + fixture-spec consistency + bipartite-coverage re-confirm), not a model run.
- ✅ **No operator-impersonation.** All FOUR predecessor LOCK ceremonies (AI Video Gen / Style Replication / QC Pre-flight / Ingest) confirmed STILL-PENDING via on-disk file-state (version tags unflipped). D6 NOT ratified (8-tuple held additively at `minItems: 5`). D15 NOT ratified (drafted to recommended default, explicitly PRELIMINARY). No runbook executed, no version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.
- ✅ **No fake-advance.** §13 distinguishes Donna-resolvable settlements (D7/D8/D14 — inside pre-approved target ranges) from operator-only ratifications (D6/D15 — carried open). The partial is LOCKED-as-drafted, not LOCKED. The SPEC body is complete (§0–§16); the v1.0 LOCK is a future operator ceremony.
- ✅ **All prior canon read-only.** Partial 1, outline, Blueprint, Cross-SPEC review, Brand-Voice Intake, all predecessor SPECs/schemas/SKILLs/runbooks — untouched.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. HC/NPOX tokens appear only as the §6.5 firewall BLOCK-list (referenced in the TC-05 fixture as the seeded-leak test surface, not restated as a cross-entity reference). REINVENTED = pilot brand inside fixtures per Cross-SPEC canon.
- ✅ **Rest Day honored.** Tonight is Thursday (Day 60). Next Rest Day: Day 63 (Sun Jun 21) — docs-prep / SKILL-scaffold pre-stage only, no SPEC content.
- ✅ **No scope expansion.** One forward deliverable (this partial 2) + build log + mirror + Notion status update + standing housekeeping + status-ping attempt. Nothing extra acted on.

---

*Day 60 ships clean ON the outline calendar. The Edit Director Agent v1.0 SPEC body is COMPLETE — §0–§16 all authored across the outline (Day 58), partial 1 (Day 59), and this partial 2 (Day 60). 13 of 15 critical decisions LOCKED-as-drafted; D6 (8-tuple — triply-gated) and D15 (Editor handoff — drafted to the Notion Edit Plan holding-store default) remain operator-gated. Next forward deliverable: v1.0 LOCK CANDIDATE assembly (Day 61). Operator pickup unchanged: the four predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight + Ingest — the Ingest 7-tuple is the direct 8-tuple dependency), the three pending runbook executions (Day 36 / Day 47 / Day 57), the Cross-SPEC §3.9 n-tuple amendment ratification (now TRIPLY load-bearing — Edit Director is the third forcing function), the Ingest Day 53 Items 6/8/11 (Item 8's D15-of-Ingest = this agent's handoff target, now directly relevant), and the new D15 Editor-handoff-target ratification staged by this walk. Day 63 (Jun 21) = next Rest Day.*
