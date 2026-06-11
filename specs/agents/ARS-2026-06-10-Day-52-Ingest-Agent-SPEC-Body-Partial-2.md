# ARS — Ingest Agent v1.0 SPEC BODY PARTIAL 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16)

**Date:** Wed Jun 10, 2026 (Day 52 · Wk8 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 2 — §8 + §9 + §11 + §12 + §15 + §16 LOCKED-as-drafted Day 52. §13 critical decisions: **13 LOCKED-as-drafted + 2 carried open** (D6 7-tuple DOUBLY-DEFERRED; D15 Edit-Director handoff PRELIMINARY — drafted to Donna's recommended default, operator ratification pending). With this partial, the Ingest v1.0 SPEC body is **complete**: §0–§16 all authored. Next: v1.0 LOCK CANDIDATE assembly → input/output schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK on the established cadence.
**Pattern source:** `ARS-2026-06-01-Day-43-QC-Preflight-Agent-SPEC-Body-Partial-2.md` (Day 43 partial 2 — proven shape inherited) and `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` (grandparent pattern).
**Partial 1 source:** `ARS-2026-06-09-Day-51-Ingest-Agent-SPEC-Body-Partial-1.md` (§6 + §7 + §10 + §14 LOCKED-as-drafted Day 51).
**Outline source:** `ARS-2026-06-06-Day-48-Ingest-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 48).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — roster position 09 + §3 mode-convergence contract + §4.8 manifest shape).
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen / Style Replication / QC Pre-flight v1.0 LOCK candidates + schemas + SKILL bundles + runbooks. **All THREE predecessor LOCK ceremonies remain OPERATOR-GATED entering Day 52 — file-state confirmed (version tags unflipped). Same forward-design posture as partials 1.**

> **Cadence note:** The Day 48 outline calendared partial 2 for Day 51; the Day 50 missed run slid the cadence one day intact (surfaced in partial 1 §14.1 and the build logs). Tonight's Day 52 session ships partial 2 exactly per the slip-amended calendar — the slide has been absorbed; the trajectory is back on its stated rail.

> **Authoring discipline (LOCK signal):** §8 + §9 + §11 + §12 + §15 + §16 are LOCKED-as-drafted Day 52. §13 carries the only two forward-looking edit slots in the entire SPEC (D6 + D15 — both operator-gated). Everything else is canon as of this document.

> **LOCK-state awareness (CRITICAL — do not silently advance):** On-disk file-state confirms all three predecessor LOCK ceremonies remain OPERATOR-GATED (version tags unflipped; Day 36 + Day 47 runbook executions unconfirmed). Ingest v1.0 LOCK hard-gates on those closing + the Cross-SPEC §3.9 ratification. This partial is forward-design over LOCK-stable text artifacts only; zero production output consumed.

---

## §8 — Performance Targets (LOCKED-as-drafted Day 52)

Nine metric categories, per the outline §8 preview and the partial 1 §14.6 runway. Pattern parity: QC Pre-flight §8 / AI Video Gen §8 (category → target → measurement → rationale). Ingest's defining posture: **a deterministic, $0, reasoning-only gateway must be judged almost entirely on catch-rates and shape-validity — there is no quality gradient to score, only correctness.**

| # | Metric category | v1.0 target | Measured how | Rationale |
|---|----------------|-------------|--------------|-----------|
| 1 | **Schema validity** | **100%** of emissions validate against `output.schema.json` (success AND error branches) | Validator harness on every fixture run + every runbook case | The manifest is the editor's source of truth and the orchestrator parses it blind. A malformed manifest is a pipeline-halting defect by definition. No tolerance. |
| 2 | **Asset-firewall catch (8th pass)** | **100%** of seeded banned tokens in filenames / embedded metadata / sidecar files caught | TC-05 class fixtures: tokens injected at the asset layer across all 10 firewall entries + conjugates | The 8th pass exists because no content pass can see this surface. By construction the check is a deterministic token-boundary scan — anything below 100% means the scan itself is broken. |
| 3 | **Coverage-gap catch** | **100%** of seeded uncovered storyboard shots caught; **zero phantom coverage** | TC-03 class fixtures: shots removed from the asset set with coverage math audited | The phantom-coverage manifest (claiming a shot is covered when no asset exists) is THE defect class Ingest exists to prevent. Check #6's internal-consistency math makes this deterministic. |
| 4 | **False-pass rate** | **0%** (ZERO tolerance — D10) | Across the full fixture corpus + runbook: no `pass` verdict on any reel seeded with any defect | A phantom/off-spec/missing asset reaching Edit Director burns a full edit cycle and poisons downstream trust. Bias all ambiguity toward fail/reshoot. The expensive failure direction is the one we never accept. |
| 5 | **False-fail rate** | **≤ 5%** | Clean fixtures (TC-01/TC-02 class): proportion incorrectly failed | Over-blocking is the acceptable failure direction — a false fail costs one re-adjudication pass (~$0); a false pass costs an edit cycle. Asymmetric tolerance is deliberate (mirrors QC Pre-flight §8). |
| 6 | **URI-integrity catch** | **100%** of seeded non-relative / empty / dangling URIs caught | Fixture variants with absolute URLs, empty strings, nulls in required positions | Hard Rule #5: the editor cannot open a file that is not there. Regex + census assertion is deterministic; 100% is structural, not aspirational. |
| 7 | **Latency** | **p50 ≤ 25s · p95 ≤ 75s** per reel | Wall-clock per runbook case + fixture run | Reasoning-only, no engine wait, no decode I/O. Ingest must never be the pipeline's bottleneck — the gateway is fast or it is friction. |
| 8 | **Cost** | **$0.00 engine + $0.00 probe — structurally guaranteed** | Audit: zero engine calls, zero decode invocations, `byte_probe_performed: false` on every emission | Hard Rule #2. Cost here is not a budget to manage but an invariant to attest. Any non-zero engine/probe figure = a Hard Rule violation, not an overrun. |
| 9 | **Self-QC first-pass yield** | **≥ 90%** of emissions pass the 11-check list on attempt 1; retry (2-strike) consumed in **≤ 10%** of runs; `ingest_agent_failed` halt rate **< 2%** | `attempts` field census across fixture + runbook corpus | The 2-strike retry exists for resilience, not as a crutch. A high retry consumption means the manifest constructor is sloppy; a high slot-11 rate means the agent design itself is defective. |

**Measurement context (v1.0):** All targets are adjudicated against the §9 fixture portfolio + the LLM-test runbook corpus (operator-executed, paste-and-run, $0). No live-pipeline telemetry exists until the orchestrator ships — these are design-acceptance targets, re-baselined when runtime telemetry lands (v1.1).

**Targets NOT carried (deliberate, surfaced):** No brand-voice quality score (QC Pre-flight's jurisdiction — Rule re-adjudication ban), no render-quality metric (production agents' domain), no cost-ceiling adherence metric (QC Pre-flight's authority — Hard Rule #10). Ingest's scoreboard measures exactly its own job: catch everything, fail nothing falsely past 5%, stay fast, stay free.

---

## §9 — 5 Test Fixtures (LOCKED-as-drafted Day 52)

Pattern source: Style Replication §9 / QC Pre-flight §9. Fixture contract: each = **(input.json, expected_output.json, expected_verdict, expected_code_or_null, scenario_description)**. Fixtures live at `skills/ingest-agent/tests/` (authored on the SKILL-bundle day; this section is their binding specification). All fixtures use the canonical REINVENTED brand-anchor (Cross-SPEC fixture canon) and platform-relative `ars://` URIs. **5 of 8 LOCKED codes exercised behaviorally; the remaining 3 (`upstream_qc_not_passed`, `upstream_not_success`, `manifest_lineage_failure`) + slot-11 are exercised schema-only** (enum-presence validation), mirroring the fleet's fixture-economy precedent.

### TC-01 — Clean Mode B Pro reel → PASS (full manifest)

- **Scenario:** A QC-passed (verdict `pass`) Mode B Pro reel: `replicated_shots` (Style Replication success branch) + `rendered_shots` cross-reference (AI Video Gen), 6-shot storyboard, all assets declared-spec-conformant (9:16, 30fps, 1080×1920, mp4/h264), full coverage, sync audio declared on the 2 dialogue shots, music bed present, firewall-clean filenames, 6-tuple inbound parent_chain.
- **Expected verdict:** `pass` · **Expected code:** `null`
- **Asserts:** `successAssetManifest` validates; `asset_bundle` normalized to canonical shape with `source: "style-replication-agent"` rows; all 7 `spec_check` sub-statuses `true`/`[]`; `coverage_check {6, 6, true}`; `asset_firewall_pass_8.hits == 0` with census counts matching; `asset_uri_integrity {N, 0, 0}`; `mode_convergence {B, mode_agnostic_manifest}`; `route_back_to: null`; `handoff_targets: ["edit-director-agent"]`; `byte_probe_performed: false`; `human_review_required: true`; ≥4 snake_case `qc_pre_flags[]`; `manifest_evidence_hash` matches `^[a-f0-9]{64}$`; parent_chain extended to 7-tuple additively.

### TC-02 — Clean Mode C Enterprise reel → PASS (single-source)

- **Scenario:** Mode C Enterprise: `replicated_shots` single-source (no AI-Video-Gen cross-ref), 8-shot storyboard, all declared specs match the Enterprise platform-variant target, full coverage, firewall-clean.
- **Expected verdict:** `pass` · **Expected code:** `null`
- **Asserts:** Manifest is **byte-shape-identical** to TC-01's downstream of the `mode_convergence` block (the mode-convergence guarantee, Check #9 — this pair IS the convergence proof); `ingested_mode: "C"`; no mode-conditional fields leak; universal-tier table honored (Enterprise traverses identically at ~$0.00).

### TC-03 — Mode A coverage gap, no covering take → RESHOOT

- **Scenario:** Mode A Starter reel: `footage_upload_manifest` with 5-shot storyboard, shot #4 has NO uploaded clip with a matching `shot_ref` and **no alternate take covers it** (take-substitution ladder exhausted — takes exist only for shots 1/2/3/5). QC precondition met.
- **Expected verdict:** `reshoot` · **Expected code:** `missing_shot_coverage`
- **Asserts:** `errorEnvelope` with `failed_check_id: 6`; `spec_check.missing_shots == [4]`; `coverage_check {5, 4, false}` (internally consistent — no phantom coverage); `route_back_to: "production-coord-agent"`; `ingested_mode == "A"` (reshoot is Mode-A-exclusive — Check #10 route-map integrity); `detail` documents the take-substitution attempt before escalation (Hard Rule #8 ladder, D-Open-Q2 resolution); `human_review_required: true`.

### TC-04 — Declared-spec violation (aspect mismatch) → FAIL + route

- **Scenario:** Mode B Pro reel: shot #3's `declared_spec.aspect` is 16:9 against a 9:16 platform target; every other gate clean.
- **Expected verdict:** `fail` · **Expected code:** `asset_spec_violation`
- **Asserts:** `failed_check_id: 5`; `spec_check.aspect_ok: false`; `route_back_to: "style-replication-agent"` (the responsible production agent per the §3.2 map); `detail` names shot #3 + observed-vs-target aspect; verdict is `fail` NOT `reshoot` (Mode B — AI output is re-genned, never re-shot); the rest of the spec_check sub-statuses still explicitly computed (no short-circuit nulls — Check #5).

### TC-05 — Asset-layer firewall breach (banned token in a FILENAME) → FAIL (the 8th-pass new-surface catch)

- **Scenario:** Mode A reel, content fully clean (all 7 prior passes would pass it) — but one uploaded clip arrives as `sln_cuts_promo_take2.mp4` (firewall entry #4 token in the filename) and a sidecar SRT carries `holdcogroup.com` in a metadata comment field.
- **Expected verdict:** `fail` · **Expected code:** `asset_firewall_breach`
- **Asserts:** `failed_check_id: 4`; `asset_firewall_pass_8 {status: "breach", filenames_scanned: N, metadata_fields_scanned: M, hits: 2}` with censuses matching the true asset count; forensic `detail` names BOTH leaking assets + the upstream stage (`videographer_upload`); the catch occurs at the asset layer a content pass cannot see — **this fixture is the 8th pass's existence proof**; entity firewall list applied verbatim (10 entries, token-boundary, case-insensitive).

### 9.1 Fixture-economy rationale (surfaced)

The 3 unexercised codes are all **deterministic entry/forensic halts** (precondition gate, upstream-failure gate, lineage gate) whose trigger logic is a single equality/shape assertion — behaviorally trivial, schema-enforced, and identical in mechanism to the fleet's proven entry-gate fixtures. Spending fixture slots on them would displace the two clean-PASS convergence proofs (TC-01/TC-02) that no other test can provide. Slot-11 (`ingest_agent_failed`) is definitionally un-fixturable from outside (it requires inducing the agent to build a malformed manifest twice); the runbook's adversarial case covers its semantics. Same economy QC Pre-flight ratified at Day 43.

---

## §11 — Cost Model (LOCKED-as-drafted Day 52)

### 11.1 Zero-engine, zero-probe snapshot (v1.0)

| Cost component | Per-reel v1.0 | Mechanism |
|----------------|---------------|-----------|
| Generative engine calls | **$0.00** | None — structurally banned (Hard Rule #2) |
| Byte-level decode (ffprobe/MediaInfo) | **$0.00** | None in v1.0 — declared-spec only; `byte_probe_performed: const false` |
| LLM reasoning (manifest construction + adjudication) | **≈ $0.02–0.08** | One model pass over declared metadata + manifest assembly; bounded by the p95 75s latency envelope |
| Native compute / storage | **$0.00** | No fetch, no transcode, no asset movement — Ingest reads manifests and emits one JSON |
| **Total `cost_incurred_usd`** | **≈ $0.00 (reported to 2dp)** | Carried in `metadata` per Cross-SPEC §3.9 |

Ingest holds **no cost ceiling and no ledger authority** (Hard Rule #10 — QC Pre-flight's jurisdiction). The tier ceilings ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter Mode A) are upstream facts, restated for traceability only.

### 11.2 Catch-cost-avoidance value model (the economic justification)

Ingest produces no margin directly. Its value is **downstream-cost prevention**, quantified across the two defect classes it uniquely catches:

| Prevented failure | Without Ingest | Cost of the miss | Ingest catch cost |
|-------------------|----------------|------------------|-------------------|
| **Phantom/missing/off-spec asset reaches Edit Director** | Editor discovers mid-cut; reel re-enters production; full edit cycle burned + route-back latency | 1 wasted edit cycle ≈ 2–6 operator-hours equivalent + 1–2 day reel slip; at commercial tiers, a blown client SLA | ≈ $0.00 + ≤75s |
| **Asset-layer entity leak reaches a published surface** | A banned token in a filename/metadata field survives to export (filenames travel into CMS slugs, captions, and platform metadata) | Brand-safety incident on a PUBLISHED surface — reputational, not monetary; the one failure class with no post-hoc fix | ≈ $0.00 + ≤75s |
| **Mode-shape leak breaks Edit Director's mode-blindness** | Downstream agents grow mode-conditional logic; the convergence contract erodes fleet-wide | Permanent architecture debt across 9 downstream agents | ≈ $0.00 (Check #9) |

**The asymmetry is the whole argument:** every defect Ingest can catch costs effectively nothing to catch and materially more to miss. A gateway with a $0 toll and a 100%-catch mandate is pure option value — which is why the universal-tier table opens it to every reel at every tier with no ceiling. ROI formalization against live defect telemetry is a v1.1 task (no real corpus exists pre-orchestrator).

---

## §12 — Verdict Math (LOCKED-as-drafted Day 52)

### 12.1 The ∧-of-gates composition

Deterministic boolean composition over declared evidence — **no thresholds, no weights, no scores, nothing to tune**:

```
PASS = (qc_precondition_met)            # Check 1  — preflight verdict == "pass" ∨ lever3_signoff
     ∧ (upstream_success)               # Check 2  — no errorEnvelope branch consumed
     ∧ (all_uris_integral)              # Check 3  — non_relative == 0 ∧ dangling == 0
     ∧ (asset_firewall_clean)           # Check 4  — hits == 0 (8th pass, asset layer)
     ∧ (declared_specs_match)           # Check 5  — all 5 spec booleans ∧ duration in band
     ∧ (full_storyboard_coverage)       # Check 6  — shots_covered == shots_required
     ∧ (audio_adjudicated_ok)           # Check 7  — every sync-shot dispositioned true
     ∧ (lineage_intact)                 # Check 8  — well-formed inbound tuple
```

### 12.2 Non-pass routing (the verdict function)

Any single ∧-term false → the verdict function routes per the §3.2 map:

```
if ¬qc_precondition_met        → halt  upstream_qc_not_passed
if ¬upstream_success           → halt  upstream_not_success
if ¬lineage_intact             → halt  manifest_lineage_failure        (forensic)
if ¬all_uris_integral          → fail  asset_uri_integrity_failure     (re-emit URIs)
if ¬asset_firewall_clean       → fail  asset_firewall_breach           (forensic log + upstream attribution)
if ¬declared_specs_match       → fail  asset_spec_violation            (route_back: producer | re-upload)
if ¬audio_adjudicated_ok       → fail  audio_sync_failure              (route_back: producer | re-upload)
if ¬full_storyboard_coverage   → Mode B/C: fail   missing_shot_coverage (route_back: producer — re-gen)
                                 Mode A:   take-substitution ladder:
                                           ∃ covering take → substitute, recompute coverage
                                           ∄ covering take → reshoot (route_back: production-coord-agent)
```

**Precedence:** halts (entry/forensic gates) adjudicate before fails; among fails, the FIRST failing check in §6.2 tier order names the headline `failure_code`, with all computed evidence still emitted (no short-circuit nulls — every sub-status explicitly dispositioned regardless of the headline). `reshoot` is reachable ONLY via the Mode A coverage branch (Check #10 enforces).

### 12.3 Properties (why this is the right math for a gateway)

1. **Deterministic** — same inputs, same verdict, every run. No sampling variance to manage; the LLM is constructing and attesting, not judging on a gradient.
2. **Monotone** — adding a defect can never improve the verdict. There is no compensatory scoring where strong coverage offsets a bad URI.
3. **Zero-false-pass by construction** — `pass` requires EVERY term true; ambiguity biases to the failing branch (Hard Rule #12). The 0% false-pass target (§8.4) is a property of the composition, not a tuned threshold.
4. **Auditable** — the emitted manifest carries the evidence for every term (§10 per-check evidence rows), so any verdict is recomputable by a human from the manifest alone. Recommend-don't-clear depends on exactly this recomputability.

---

## §13 — Critical Decisions (Day 52 walk — 13 LOCKED-as-drafted · 2 carried open for operator)

Target was 10–14 LOCKED. The Day 52 walk lands **13 LOCKED-as-drafted** (within target), with **2 carried open** — both operator-gated, both drafted to Donna's recommended default so the SPEC is buildable while the gates close. **Per the process-integrity attestation, Donna does NOT ratify PRELIMINARY/critical-decision items — D6 and D15 are surfaced, not advanced.**

| # | Decision | Status | Resolution |
|---|----------|--------|------------|
| D1 | Asset-readiness vs full-decode scope — v1.0 = **declared-spec adjudication ONLY**; byte-probe (ffprobe/MediaInfo) deferred to v1.1 | **LOCKED-as-drafted Day 48** | Resolves outline Open Question 1 per recommendation: the buildable, highest-leverage slice under the no-engine/$0 posture. `byte_probe_performed: const false` is the honesty contract. |
| D2 | Universal tier access — all 4 tiers traverse Ingest | **LOCKED-as-drafted Day 48** | Asset readiness is not a tier feature; the gateway is $0 so there is no economic reason to gate it. |
| D3 | Verdict model — `pass / fail / reshoot`; `reshoot` Mode-A-exclusive | **LOCKED-as-drafted Day 48** | AI output is re-genned, never re-shot. Enforced by Check #10. |
| D4 | QC-pass precondition absolute | **LOCKED-as-drafted Day 48** | Ingest never ingests an unvetted reel; Lever-3 sign-off is the only bypass. |
| D5 | No cost re-litigation | **LOCKED-as-drafted Day 48** | QC Pre-flight's authority; double-enforcement risks spurious double-fails. Hard Rule #10. |
| D6 | **7-tuple parent_chain** — inherits QC Pre-flight 6-tuple + appends `asset_manifest_id` (UUIDv7) | **DOUBLY-DEFERRED — operator-gated** | Held additively (`minItems: 5`, `maxItems: 7`, `items: false`) pending BOTH the Cross-SPEC §3.9 ratification AND the QC Pre-flight 6-tuple LOCK. `TODO@cross-spec-3.9-ratification` flip note embedded for the schema author. **NOT advanced tonight.** |
| D7 | errorEnvelope code count → **8 LOCKED + slot-11** | **RESOLVED Day 51 → LOCKED-as-drafted** | Settled within the 7–9 target via the duration fold (D14). Namespace-cardinality rationale at §6.3. |
| D8 | Self-QC check count → **11** | **RESOLVED Day 51 → LOCKED-as-drafted** | Within the 10–12 target; 4-tier ordering (entry / substance / forensic / manifest-construction). |
| D9 | Mode-convergence guarantee — one manifest shape regardless of mode | **LOCKED-as-drafted Day 48** | The contract that makes Edit Director and all 9 downstream agents mode-blind. Check #9 + TC-01/TC-02 convergence proof. |
| D10 | False-pass tolerance — **ZERO** | **LOCKED-as-drafted Day 48** | Resolves outline Open Question 5 per recommendation. §12.3 makes it structural; §8.4 makes it measured. |
| D11 | Engine + probe policy — NO engine, NO decode in v1.0 | **LOCKED-as-drafted Day 48** | Hard Rule #2. The forged-provenance framing is the defining negative constraint. |
| D12 | Recommend-don't-clear — `human_review_required: true` on every emission; verdict is a RECOMMENDATION | **LOCKED-as-drafted Day 48** | Hard Rule #12. The operator clears; the agent never does. Lever-3 default. |
| D13 | Audio-sync scope — declared sync-flag adjudication only; LUFS deferred to v1.1 | **LOCKED-as-drafted Day 48** | Loudness needs decode + the Sound agent's domain (−14 LUFS IG/TT, −16 YT per Blueprint #12). |
| D14 | `duration_envelope_breach` → **folded into `asset_spec_violation`** with `detail.subtype: "duration_envelope"` | **RESOLVED Day 51 → LOCKED-as-drafted** | Resolves outline Open Question 6 per recommendation. Same defect family, same route-back; the subtype preserves the diagnostic. Revisit only if duration defects prove common in the v1.0 corpus. |
| D15 | **Edit-Director handoff target** — v1.0 emits the manifest to the **Notion Asset Manifest DB (holding store)**; direct agent-to-agent handoff activates when Edit Director (Agent #9) LOCKs | **PRELIMINARY — drafted to recommended default · operator ratification pending** | Outline Open Question 4. Donna recommends the holding store: Edit Director does not exist yet, and a manifest emitted into a void is an audit-trail break. `handoff_targets: ["edit-director-agent"]` names the LOGICAL target; the PHYSICAL v1.0 destination is the holding store. **Operator may override on this walk's review.** |

**Decision-walk integrity note:** D7/D8/D14 were PRELIMINARY at Day 48, resolved by the Day 51 partial 1 authoring exactly as the outline's recommended defaults, and are LOCKED-as-drafted here — these were *Donna-resolvable* (authoring-level settlements inside pre-approved target ranges). D6 and D15 are *operator-only* (a Cross-SPEC amendment ratification and a pipeline-topology commitment) and remain open. This is the same Donna-resolvable vs operator-only line the QC Pre-flight Day 43 walk drew.

---

## §15 — Change Log + Version History (LOCKED-as-drafted Day 52)

| Version tag | Day | Date | Event |
|-------------|-----|------|-------|
| v1.0-draft-day-48 | 48 | Sat Jun 6 | Outline §0–§5 SHIPPED (`ARS-2026-06-06-Day-48-Ingest-Agent-SPEC-Outline.md`) — 6 open questions parked |
| — | 49 | Sun Jun 7 | **Rest Day** (7th observance — no build) |
| — | 50 | Mon Jun 8 | Calendared partial 1; **overnight run did not execute** — cadence slid one day intact (surfaced §14.1) |
| v1.0-draft-day-51 | 51 | Tue Jun 9 | Body partial 1: §6/§7/§10/§14 LOCKED-as-drafted; namespace settled 8+slot-11; self-QC settled 11; duration fold resolved |
| v1.0-draft-day-52 | 52 | Wed Jun 10 | **Body partial 2 (this document): §8/§9/§11/§12/§15/§16 LOCKED-as-drafted; §13 walk = 13 LOCKED + D6/D15 carried open. SPEC body §0–§16 COMPLETE.** |
| v1.0-LOCK-CANDIDATE | 53+ | TBD | Assembly of the full SPEC + cross-SPEC §3 full audit (hard-gated: 3 predecessor LOCKs + §3.9 ratification) |
| v1.0-schemas | TBD | TBD | `input.schema.json` + `output.schema.json` per §10.4 authoring notes |
| v1.0-SKILL | TBD | TBD | `skills/ingest-agent/` bundle + §9 fixtures at `tests/` |
| v1.0-runbook | TBD | TBD | LLM-test runbook (operator paste-and-run, 5 cases) |
| v1.0-LOCKED | TBD | TBD | **Operator LOCK ceremony** — tag flip + Notion + chip (operator-only) |

**Parked candidates (v1.1+ register):** byte-probe activation (`probed_spec` + `byte_probe_performed` flip), `loudness_check` (LUFS), `conform_plan` (auto-transcode routing), `take_dedup_report` (perceptual hashing), `re_ingest` manifest class, duration-fold revisit (D14 telemetry condition), direct Edit-Director handoff (D15 activation condition), live-telemetry re-baseline of §8 targets.

---

## §16 — Metadata Block Schema (LOCKED-as-drafted Day 52)

Cross-SPEC §3.9 canonical fields + **5 Ingest additions**. Pattern source: QC Pre-flight §16 / AI Video Gen §16. This is the binding contract for the schemas-day `metadata` object:

```
"metadata": {
  // ---- Cross-SPEC §3.9 canonical (inherited verbatim) ----
  "agent_id":            "ingest-agent",                  // const
  "agent_version":       "1.0",                           // semver string
  "production_mode":     "A" | "B" | "C",
  "brand_id":            "REINVENTED",                    // v1.0 expected value
  "parent_chain":        [ ... ],                         // see addition 1
  "cost_incurred_usd":   0.00,                            // ≈ $0 — reasoning only
  "human_review_required": true,                          // const true (Hard Rule #12)
  "timestamp_utc":       "<ISO-8601>",

  // ---- Ingest additions (5) ----
  "asset_manifest_class":      "pre_edit",                // 1. enum: ["pre_edit"] v1.0 · "re_ingest" reserved v1.1+
  "manifest_evidence_hash":    "<sha256-hex-64>",         // 2. SHA-256 over per-asset evidence + spec_check (^[a-f0-9]{64}$)
  "runtime_environment_class": "dev"|"staging"|"production", // 3. inherit AI Video Gen §16
  "byte_probe_performed":      false,                     // 4. const false v1.0 (declared-spec honesty; flips v1.1)
  "asset_manifest_id":         "<UUIDv7>"                 // 5. this agent's emitted identity (also parent_chain[6])
}
```

**Addition 1 — `parent_chain` (the doubly-deferred 7-tuple):** `prefixItems` positions 0–6 = `[brief_id, script_id, storyboard_id, production_plan_id|rendered_shots_set_id, replication_set_id, preflight_report_id, asset_manifest_id]` · `minItems: 5` · `maxItems: 7` · `items: false`. Accepts the 5-tuple (pre-ratification), the 6-tuple (QC Pre-flight extension pending its LOCK), and the 7-tuple (this agent's append). Rejects a 4-tuple. `TODO@cross-spec-3.9-ratification` flips `minItems` to 7 ONLY after both gates close (D6). The schema author copies this constraint verbatim per §10.4.

**Schema-day cross-references:** `output_type` oneOf split, the 8-code + slot-11 `failure_code` enum (NO `duration_envelope_breach` — folded per D14), the `ars://` URI pattern, the verdict enum WITHOUT `hold` (§6.4 divergence), and `spec_check.missing_shots` required-on-success — all per §10.4, restated here as the single checklist the schema author works from.

---

## Day 53+ runway (next forward deliverable)

**Next up: Ingest Agent v1.0 LOCK CANDIDATE assembly** — merge outline + partial 1 + partial 2 into the single LOCK-candidate document, run the FULL Cross-SPEC §3 audit (11 dimensions, LOCK-grade), final bipartite-coverage proof, and stage the §13 walk for the operator. Then schemas → SKILL bundle → runbook per the §15 lifecycle. The LOCK itself remains hard-gated on the three predecessor ceremonies + the §3.9 ratification (all operator-pending — see partial 1 §14.7).

---

## Mirror status

- Source: `ars/ARS-2026-06-10-Day-52-Ingest-Agent-SPEC-Body-Partial-2.md` (this document) + `ars/build-log-2026-06-10.md`
- Mirror destination: `/outputs/ars/` (both files)
- Mirror verification: in this session's mirror step.

---

## Process integrity (Day 52)

- ✅ **No LLM dispatched. No engine, no probe, no network, ZERO $ spent.** Validation was structural (pattern parity + §12 composition audit + fixture-spec consistency), not a model run.
- ✅ **No operator-impersonation.** All THREE predecessor LOCK ceremonies confirmed STILL-PENDING via file-state. D6 NOT ratified (7-tuple held additively). D15 NOT ratified (drafted to recommended default, explicitly PRELIMINARY). No runbook executed, no version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.
- ✅ **No fake-advance.** §13 distinguishes Donna-resolvable settlements (D7/D8/D14 — inside pre-approved target ranges) from operator-only ratifications (D6/D15 — carried open). The partial is LOCKED-as-drafted, not LOCKED.
- ✅ **All prior canon read-only.** Partial 1, outline, Blueprint, Cross-SPEC review, all predecessor SPECs/schemas/SKILLs/runbooks — untouched.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. HC/NPOX tokens appear only as the §6.5 firewall BLOCK-list (referenced, not restated). REINVENTED = pilot brand inside fixtures per Cross-SPEC canon.
- ✅ **Rest Day honored.** Tonight is Wednesday (Day 52). Next Rest Day: Day 56 (Sun Jun 14).
- ✅ **No scope expansion.** One forward deliverable (this partial 2) + build log + mirror + standing housekeeping. Nothing extra acted on.

---

*Day 52 ships on the slip-amended calendar. The Ingest Agent v1.0 SPEC body is COMPLETE — §0–§16 all authored across the outline (Day 48), partial 1 (Day 51), and this partial 2 (Day 52). 13 of 15 critical decisions LOCKED-as-drafted; D6 (7-tuple — doubly-gated) and D15 (Edit-Director handoff — drafted to the Notion holding-store default) remain operator-gated. Next forward deliverable: v1.0 LOCK CANDIDATE assembly. Operator pickup unchanged: three predecessor LOCK ceremonies, two runbook executions (Day 36 + Day 47), the Cross-SPEC §3.9 ratification (doubly load-bearing), the Agent-#8 slot confirmation — now plus the D15 handoff-target ratification staged by this walk.*
