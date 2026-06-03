# ARS — QC Pre-flight Agent v1.0 SPEC (UNIFIED · LOCK CANDIDATE · Day 44)

**Author:** Donna (overnight build session · Sequel Digital ARS sprint)
**Date:** 2026-06-02 (Tue · Day 44 · Wk7D1 · post-launch hardening window)
**Document status:** **v1.0 LOCK CANDIDATE — awaiting operator sign-off on items 6, 8, 11 + the 2 production-tier predecessor LOCKs (hard gate)**
**Lock signal:** Items 1–5, 7, 9, 10 of the Day 44 reviewer checklist are EXECUTED and PASS. Items 6, 8, 11 are operator-only.
**Predecessor LOCKs:** Brief Agent v1.0 (Day 6) · Script Agent v1.0 (Day 9) · Storyboard Agent v1.0 (Day 14) · Production Coord Agent v1.0 (Day 14) · Cross-SPEC Canon (Day 12) · **AI Video Gen Agent v1.0 LOCK CANDIDATE (Day 24 — operator-gated; STILL PENDING) · Style Replication Agent v1.0 LOCK CANDIDATE (Day 32 — operator-gated; STILL PENDING)**
**Hard gate on production-tier LOCKs:** QC Pre-flight's v1.0 LOCK ceremony CANNOT complete until **both** AI Video Gen v1.0 and Style Replication v1.0 are LOCKED first — QC Pre-flight consumes both as input branches. This LOCK CANDIDATE is authored on LOCK-stable **text artifacts** (the SPECs + schemas as drafted); it uses **zero production output** from either agent. Forward-design under the same posture as the Day 29 / Day 40 outlines.
**Position note:** Agent #7 of 17. QC Pre-flight extends the fleet PAST the six launch-critical agents. Its v1.0 LOCK lands inside the post-launch hardening window and does **NOT** gate the Day 42/43 commercial launch (which ships on the six built agents).

---

## §0 — LOCK MANIFEST (executive summary)

| Item | Status |
|------|--------|
| SPEC sections drafted | **17 / 17** (§0–§16 — outline §0–§5 Day 40 · body §6/§7/§10/§14 Day 41 · body §8/§9/§11/§12/§13/§15/§16 Day 43) |
| `<<TBD-D4x>>` markers remaining in SPEC body | **0** (verified by grep across Day 40 outline + Day 41 + Day 43 partials) |
| SPEC body completeness | **§6–§16 COMPLETE** (Day 41 + Day 43 partials fully cover the body; this LOCK CANDIDATE is a pure text-only reconciliation, zero net-new SPEC content) |
| Error code canonical count | **9 LOCKED + slot-11 catch-all** (Day 41 §6.3 — `upstream_not_success` · `entity_firewall_breach` · `brand_voice_qc_failed` · `format_spec_violation` · `caption_spec_violation` · `cost_ledger_overrun` · `qc_pre_flags_floor_breach` · `drift_unresolved` · `lineage_integrity_failure` + `preflight_qc_agent_failed` slot-11) — narrowed from 11 candidates (2 folds: format/floor + chain-break/lineage) |
| Slot-11 errorEnvelope name | `preflight_qc_agent_failed` (Cross-SPEC §3.6 conformant — one canonical fallback code per agent slot, no orphan references) |
| Self-QC check count | **12** (Day 41 §6.1 — entry-validation #1–2 · verdict-adjudication #3–7 · forensic/deferral #8–9 · report-integrity #10–12) bipartite-covering the 9 codes + slot-11 |
| Verdict model | **Pass / Fail / Reshoot + `drift_unresolved` soft-hold** (3 machine verdicts + 1 human-deferred 4th outcome `hold`) |
| Verdict math | **Deterministic ∧-of-gates · ZERO tunable thresholds** — 13-term PASS conjunction; non-pass resolves via an ordered 9-rule routing decision tree. The deliberate inverse of the production agents' weighted drift score; no calibration knob = no pressure-driven false-pass |
| Combined tier cost ceilings (QC Pre-flight enforces) | **Pro $450** ($400 AVG + $50 SR) · **Enterprise $870** ($750 + $120) · **Pilot/Starter Mode A ≤$40** — first agent with total-spend visibility across both production agents |
| Self per-reel cost | **$0.00–$0.02** — reasoning-only; optional native pHash/CLIP re-verify $0.001/shot on contested drift only. Generative engine spend is **FORBIDDEN** ($0 ceiling, not bounded). Lowest-cost agent in the 17-agent fleet |
| Performance target portfolio | **9 metric categories** — schema validity 100% · firewall catch 100% (7th pass perfect by construction) · **false-pass rate 0%** (the defining target — a brand-safety gate must never pass a breach) · false-fail ≤5% (over-blocking is the safe failure direction · §8.2 asymmetry) · p50 ≤30s / p95 ≤90s (reasoning-only, ~6–9× faster than render-bound agents) · engine cost $0.00 · self-QC first-attempt ≥92% |
| Test fixture portfolio | **5 fixtures** — TC-01 Mode B Pro clean PASS · TC-02 Mode C Enterprise clean PASS (mode-agnostic verdict + null Mode-B fields) · TC-03 `entity_firewall_breach` (the 7th-pass catch — gating fixture) · TC-04 `format_spec_violation` (aspect mismatch → fail + route) · TC-05 `drift_unresolved` (carried drift → soft-hold/human review). 2 success + 3 non-pass live; remaining 6 LOCKED codes + slot-11 = schema-only fixtures (schemas day) |
| Cost model engine coverage | **ZERO generative engines** (by design — QC Pre-flight calls no engine). Optional native CLIP+pHash re-verify ($0.001/shot · native compute, contested-drift only). **No external vendor pricing URLs to walk** — the cost model has no vendor-pricing canon surface (unlike Style Replication's 4-engine table) |
| Metadata block schema | **Cross-SPEC §3.9 canonical (9 fields) + 4 QC Pre-flight additions** (`parent_chain` 6-tuple · `qc_gate_class` · `verdict_evidence_hash` · `runtime_environment_class`) — audit invariant. `human_review_required: const true` schema-enforced (recommend-don't-approve) |
| parent_chain | **6-tuple DRAFTED Day 43** (inherits Style Replication's 5-tuple lineage + appends own `preflight_report_id` ref) — **DEFERRED on operator ratification of the Cross-SPEC §3.9 n-tuple amendment.** Schema holds at `minItems: 5` until ratified. The one item Donna will NOT auto-advance |
| 14 Critical Decisions | **14/14 §13 coverage** — 8 LOCKED-as-drafted Day 40 (#1/#2/#3/#8/#9/#10/#11/#12) + 2 RESOLVED Day 41 (#6 code count / #7 self-QC count) + 2 LOCKED Day 43 `[PRELIMINARY · operator amend]` (#4 route-back map / #13 route-back automation depth) + 2 net-new LOCKED Day 43 (#3 drift soft-hold confirm / #14 reshoot Mode-A-exclusivity). **Decision #5 (6-tuple parent_chain) explicitly DEFERRED** on §3.9 |
| 12 Hard Rules (system prompt) | LOCKED verbatim Day 41 §7.1 — operator copy-paste-ready into the SKILL.md. Hard Rule #12 = "recommend-don't-approve" (QC Pre-flight's defining, non-inherited rule) |
| 11-point Brand Voice QC gate | Inlined verbatim from Brand Voice Intake v1.0 §13 (LOCKED) into §7 system prompt — the LLM is the runtime source of truth for the gate, not a side document |
| Cross-SPEC §3 audit | **11/11 dimensions ✅** across Day 40 + Day 41 + Day 43 audits |
| Authoring decisions documented | **14** (8 Day 40 + 2 Day 41 + 4 Day 43) — operator can ratify each at LOCK walk-through |

---

## §1 — DAY 44 REVIEWER CHECKLIST · EXECUTION RECORD

The 11-item checklist mirrors the Day 24 AI Video Gen / Day 32 Style Replication LOCK candidate pattern (proven shape, 3rd reuse). Donna executed items 1–5, 7, 9, 10 autonomously overnight. Items 6, 8, 11 are operator-only.

### Item 1 — Error code count = 9 + slot-11 (verify exhaustive vs §6 12-check Self-QC list)
**Verdict: ✅ PASS.** Day 41 §6.3 mapping table enumerates all 9 codes + slot-11 catch-all with trigger-check mapping. The namespace was narrowed from 11 candidates via 2 deliberate folds: (a) `qc_pre_flags_format_violation` folded into `qc_pre_flags_floor_breach` (a short array and a malformed array are the same defect class — under-provisioned audit surface); (b) `negative_prompt_chain_break` folded into `lineage_integrity_failure` (the Mode B SHA-256 passthrough break is structurally a forensic chain-integrity break). Both folds mirror Style Replication §6.3's narrowing discipline. 9 codes preserve precise route-back attribution across the 6 upstream agents + format/caption/cost/drift/lineage; folding below 9 would force ambiguous routing. Bipartite coverage confirmed (Item 5 also passes).

### Item 2 — Slot-11 errorEnvelope name verification
**Verdict: ✅ PASS.** Search across Day 40 + Day 41 + Day 43 confirms `preflight_qc_agent_failed` is the canonical slot-11 name in all OPERATIONAL positions (§6.1 Checks #10/#11, §6.3 mapping table, §3.2 errorEnvelope). Naming derives correctly per Cross-SPEC §3.6: agent_id `qc-preflight-agent` → snake_case → `preflight_qc_agent_failed`. No legacy `style_replication_agent_failed` or `ai_video_gen_agent_failed` references in operational positions. **NO operational orphans.** Cross-SPEC §3.6 canon — one canonical fallback code per agent slot — fully respected.

### Item 3 — Cost model accuracy (near-zero reasoning + native compute · no vendor URL walk required)
**Verdict: ✅ PASS · structurally distinct from the production agents' Item 3.** Day 43 §11 establishes QC Pre-flight as the only agent in the fleet with **no external vendor-pricing surface**: it calls no generative engine, so there is no Pika/Runway/vendor pricing table to spot-check (the friction that made Item 3/6 a deferred operator walk for AI Video Gen and Style Replication). The cost model is (a) $0.00–$0.01 reasoning + (b) optional native CLIP+pHash re-verify at $0.001/shot on contested drift only — **native compute, no vendor URL.** Effective $0.00–$0.02/reel. The combined tier ceilings QC Pre-flight enforces ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter) are **inherited verbatim** from the already-LOCKED AI Video Gen §7 + Style Replication §7.3 reconciliations, not re-derived here. **No pricing URL walk is required for this agent** — Item 6 below is consequently the lightest operator spot-check in the fleet's LOCK history.

### Item 4 — Combined tier ceiling consistency ($450 Pro · $870 Enterprise · ≤$40 Pilot-Starter)
**Verdict: ✅ PASS.** Cross-referenced across Day 40 + Day 41 + Day 43:
- Day 40 §4 combined-ceiling table — "Pro $400 + $50 = **$450** · Enterprise $750 + $120 = **$870** · Pilot/Starter Mode A **≤$40**"
- Day 41 §6.1 Check #6 — "$450 Pro ($400 + $50) / $870 Enterprise ($750 + $120) / ≤$40 Pilot-Starter Mode A — taken verbatim from Style Replication §7.3 reconciliation"
- Day 41 §7.3 tier table cost reconciliation (the combined-ceiling authority restatement)
- Day 43 §11.2 per-tier cost table + §11.3 catch-cost-avoidance worked examples
- Day 43 §9.1 TC-01 fixture (`tier_combined_ceiling_usd: 450`) + §9.2 TC-02 fixture (`tier_combined_ceiling_usd: 870`)
All values consistent. No drift. **No operator-amend flag** — these ceilings are downstream inheritances of LOCKED production-agent canon, not net-new QC Pre-flight decisions (the margin-floor pricing conversation remains an inherited open item flagged for the operator at the production-agent layer, NOT re-litigated by QC Pre-flight per Day 40 §4).

### Item 5 — Self-QC list ↔ 9 errorEnvelope code + slot-11 bipartite coverage
**Verdict: ✅ PASS.** Day 41 §6.3 mapping table is bipartite: every one of the 12 self-QC checks resolves to ≥1 code; every code traces to ≥1 check. Check #1 → `upstream_not_success`; Check #2 → `entity_firewall_breach`; Check #3 → `brand_voice_qc_failed`; Check #4 → `format_spec_violation`; Check #5 → `caption_spec_violation`; Check #6 → `cost_ledger_overrun`; Check #7 + #12 → `qc_pre_flags_floor_breach`; Check #8 → `drift_unresolved` (soft-hold); Check #9 → `lineage_integrity_failure`; Checks #10 + #11 → `preflight_qc_agent_failed` (slot-11). Coverage complete. The 12-check tiering (entry #1–2 / adjudication #3–7 / forensic-deferral #8–9 / report-integrity #10–12) is structurally complete.

### Item 6 — Cost model / pricing spot-check
**Verdict: ⏸ OPERATOR-ONLY · but the lightest in fleet history (no vendor URLs).** Unlike AI Video Gen and Style Replication — whose Item 6 required walking live vendor pricing pages (Pika, Runway) — QC Pre-flight has **no external vendor-pricing surface to verify** (it calls no generative engine; see Item 3). The only operator confirmation needed is a one-line ratification that the **inherited** combined ceilings ($450 / $870 / ≤$40) still match the production-agent canon as those agents reach their own LOCK. Donna does NOT walk URLs autonomously (web-fetch out of scope for overnight build session integrity per Day 22+ Process Integrity canon), but here there is nothing to walk. **Recommendation:** RATIFY the inherited ceilings as-is at the LOCK ceremony (≈2 min). Any future change to the production-agent ceilings auto-propagates to QC Pre-flight via the inheritance reference — no QC Pre-flight-local pricing canon to drift. **No silent ratification** — surfaced for operator confirmation only.

### Item 7 — 5 test fixtures portfolio (happy + failure mode + soft-hold coverage)
**Verdict: ✅ PASS.** Day 43 §9.1–§9.5 portfolio:
- TC-01 — Mode B Pro clean PASS (full green path, all 13 ∧-terms true)
- TC-02 — Mode C Enterprise clean PASS (proves mode-agnostic verdict + null Mode-B forensic fields; `reshoot` route unreachable in Mode C per Decision #14)
- TC-03 — `entity_firewall_breach` (injected `4821 main` banned token → the 7th-pass catch · the gating fixture proving the agent's reason-to-exist fires)
- TC-04 — `format_spec_violation` (aspect 1:1 requested but shots rendered 9:16 → `fail` + `route_back_to` production agent · advisory recovery path, not auto-executed)
- TC-05 — `drift_unresolved` (carried `style_drift_exceeded`, no Lever-3 sign-off → `verdict: "hold"` soft-hold, `human_review_required: true` · the 4th verdict value)

Coverage: 2 happy paths (TC-01 + TC-02 · spanning Mode B + Mode C) + 2 hard failures (TC-03 firewall + TC-04 format) + 1 soft-hold (TC-05 drift). 3 codes exercised live (`entity_firewall_breach`, `format_spec_violation`, `drift_unresolved`); the remaining 6 LOCKED codes + slot-11 covered by schema-only fixtures on the schemas day (same discipline as Style Replication §9, where 2 codes were schema-only · AI Video Gen Day 27 precedent for the 5-fixture LLM-test ceiling). This avoids stretching the proven 5-fixture pattern while binding every code to a fixture.

### Item 8 — 14 critical decisions sign-off (Jamila walks)
**Verdict: ⏸ OPERATOR-ONLY.** Donna does NOT have authority to ratify Decisions #1–#14. Operator walks each (rationale · alternative · revisit trigger) at the LOCK ceremony. The 14 decisions are enumerated in §3 below.

**Special attention required on 2 `[PRELIMINARY · operator amend]` items + 1 DEFERRED:**
- Decision #4 — Route-back map (fail→responsible agent · reshoot→ProdCoord · hold→human) — Donna recommends **RATIFY**
- Decision #13 — Route-back automation depth = ADVISORY in v1.0 (no orchestrator auto-re-entry) — Donna recommends **RATIFY**
- Decision #5 — 6-tuple parent_chain — **DEFERRED** on the Cross-SPEC §3.9 amendment (see Item 11); Donna will NOT auto-advance the 6-tuple. Held at 5-tuple (`minItems: 5`) until §3.9 ratifies.

**No silent ratification.** Operator either RATIFY-AS-LOCKED for each, AMEND-with-rationale (triggers a `§15.1 v1.0-corrections-day-44` entry), or DEFER-to-v1.0.1.

### Item 9 — Cross-SPEC §3 adherence (11 dimensions all ✅)
**Verdict: ✅ PASS.** Day 40 + Day 41 + Day 43 self-audits combine to cover all 11 Cross-SPEC §3 canon dimensions:
- §3.1 Naming canon — ✅ `qc-preflight-agent` (kebab-case fleet pattern)
- §3.2 hash invariant precedent — ✅ `verdict_evidence_hash` SHA-256 over evidence block + Mode B negative-prompt SHA-256 cross-check
- §3.3 errorEnvelope shape — ✅ 9 codes + slot-11 LOCKED Day 41, exercised in Day 43 §9 fixtures; adds `verdict` + `route_back_to`
- §3.4 `qc_pre_flags` minItems-4 floor + snake_case — ✅ **QC Pre-flight is the adjudicator of the §3.4 floor** (Step 3 / Check #7 enforces it across all 6 upstream stages)
- §3.5 Mode matrix — ✅ §4 mode-agnostic verdict + mode-aware reporting (A/B/C)
- §3.6 Slot-11 naming canon — ✅ `preflight_qc_agent_failed` canonical
- §3.7 `qc_pre_flags` format regex — ✅ Day 41 §6.1 Check #7 shape adjudication
- §3.8 Tier↔mode firewall 7th defense-in-depth pass — ✅ Day 41 §7 Step 2 + §4 universal-tier table
- §3.9 Metadata block — ✅ canonical inherit + extends to 6-tuple · amendment language §16.3 DRAFTED for ceremony (Item 11)
- §3.10 Cost ceiling authority — ✅ combined-ceiling reconciliation + Step 7 enforcement (first agent with total-spend visibility)
- §3.11 LOCK respect — ✅ all AI Video Gen / Style Replication / Cross-SPEC references read-only; zero canon drift

**11 of 11 ✅** at Day 44 LOCK CANDIDATE close.

### Item 10 — No fake-advance check (zero `<<TBD-*>>` markers in SPEC body)
**Verdict: ✅ PASS.** Day 40 outline reserved §6–§16 for partial authoring; Day 41 resolved §6/§7/§10/§14; Day 43 resolved §8/§9/§11/§12/§13/§15/§16. The SPEC body §6–§16 is COMPLETE with zero `<<TBD-D4x>>` markers (grep-verified). Remaining "TBD" string occurrences across the three files are: (a) forward-references to the schemas day + SKILL bundle day (legitimately deferred, not fake-advanced), (b) the Cross-SPEC §3.9 amendment language §16.3 explicitly labeled operator-ratification-required (legitimate operator gate), (c) the Decision #5 6-tuple item explicitly DEFERRED, (d) audit-trail mentions of historical markers. Zero fake-advanced LOCK content.

### Item 11 — Cross-SPEC §3.9 amendment ratification (6-tuple parent_chain extension)
**Verdict: ⏸ OPERATOR-ONLY · the carried forcing function.** Day 43 §16.3 reproduces the Cross-SPEC §3.9 amendment language (originally DRAFTED Day 31 §16.3 for Style Replication's 5-tuple, carried unratified through Style Replication Day 32 Item 11 → QC Pre-flight Day 40 Open Question #3). QC Pre-flight is the **first concrete 6-tuple consumer** and the **forcing function** for the amendment's ratification.

**Amendment language drafted (reproduced for operator review):**
> *"Cross-SPEC §3.9 parent_chain canonical definition is hereby amended from fixed 4-tuple to n-tuple where n = production tier depth + 1. AI Video Gen v1.0 invocations remain 4-tuple (n=4); Style Replication v1.0 invocations are 5-tuple (n=5); QC Pre-flight v1.0 invocations are 6-tuple (n=6). Future agents extend by appending their own primary-output-id reference to the inherited parent_chain. JSON Schema enforcement: `prefixItems` + `items: false` per existing canon, with prefixItems length determined dynamically by agent slot index. Each agent SPEC explicitly states its parent_chain n-value in §16.1."*

Operator either: (a) **RATIFY-AS-DRAFTED** (Donna's recommendation — generalization is necessary for the 10 remaining agent slots beyond QC Pre-flight; QC Pre-flight is the natural ratification moment because it is the first 6-tuple consumer), (b) AMEND-with-rationale, or (c) DEFER (schema author stays at `minItems: 5` with a documented TODO; QC Pre-flight's parent_chain re-derives to fit existing canon at v1.1). **Donna's default if the operator skips the sit-down: LOCK the 2 `[PRELIMINARY]` items at recommended defaults; HOLD Decision #5 at 5-tuple until §3.9 ratifies — the 6-tuple is the one item Donna will NOT auto-advance.**

### Reviewer checklist summary
- ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ⏸ OPERATOR (lightest — no vendor URLs) · ✅ PASS · ⏸ OPERATOR · ✅ PASS · ✅ PASS · ⏸ OPERATOR
- **8 PASS · 3 OPERATOR-ONLY · 0 FAIL**
- **LOCK status: CANDIDATE READY.** v1.0 advances to LOCKED on operator ratification of items 6, 8, 11 — **AND** is hard-gated on both production-tier predecessor LOCKs (AI Video Gen + Style Replication) closing first.

---

## §2 — UNIFIED SPEC INDEX (authoritative source per section)

| § | Title | Authoritative source | Day | Lock status |
|---|-------|----------------------|-----|-------------|
| §0 | Provenance & Build-Phase Position | `ARS-2026-05-29-Day-40-QC-Preflight-Agent-SPEC-Outline.md` | Day 40 | LOCKED-as-shipped |
| §1 | Purpose & Position in Pipeline (single-responsibility line) | `ARS-2026-05-29-Day-40-...-SPEC-Outline.md` | Day 40 | LOCKED-as-shipped (operator pre-ratified — single-responsibility line) |
| §2 | Inputs (mode-agnostic; primary replicated_shots + Mode B forensic rendered_shots + accumulated qc_pre_flags surface) | `ARS-2026-05-29-Day-40-...-SPEC-Outline.md` | Day 40 | LOCKED-as-shipped (schema authority schemas day) |
| §3 | Outputs — `preflight_report.json` (polymorphic: successPreflightReport \| errorEnvelope) + verdict↔route map | `ARS-2026-05-29-Day-40-...-SPEC-Outline.md` | Day 40 | LOCKED-as-shipped (schema authority schemas day) |
| §4 | Tier Constraints (universal access — all 4 tiers) + combined cost-ledger authority | `ARS-2026-05-29-Day-40-...-SPEC-Outline.md` | Day 40 | LOCKED-as-shipped |
| §5 | 11-Step Verdict Loop (system-prompt skeleton) | `ARS-2026-05-29-Day-40-...-SPEC-Outline.md` | Day 40 | LOCKED-as-shipped (LOCKED verbatim into §7 Day 41) |
| §6 | 12-Check Self-QC List + 9-code/slot-11 errorEnvelope mapping | `ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` | Day 41 | LOCKED-as-drafted |
| §7 | System Prompt v1.0 (12 hard rules + universal-tier table + 11-step loop + 11-point Brand Voice QC gate inlined verbatim + voice rule) | `ARS-2026-05-30-Day-41-...-Partial-1.md` | Day 41 | LOCKED-as-drafted (verbatim copy → SKILL.md on the SKILL-bundle day) |
| §8 | Performance Targets (9 metric categories — false-pass 0% is the defining target) | `ARS-2026-06-01-Day-43-QC-Preflight-Agent-SPEC-Body-Partial-2.md` | Day 43 | LOCKED-as-drafted |
| §9 | 5 Test Fixtures (TC-01..TC-05) | `ARS-2026-06-01-Day-43-...-Partial-2.md` | Day 43 | LOCKED-as-drafted |
| §10 | Pre-flight Report Field Map (26 rows — lineage + per-check evidence + reel-level verdict aggregate) | `ARS-2026-05-30-Day-41-...-Partial-1.md` | Day 41 | LOCKED-as-drafted |
| §11 | Cost Model (near-zero reasoning + native compute · NO vendor-pricing surface · catch-cost-avoidance value model) | `ARS-2026-06-01-Day-43-...-Partial-2.md` | Day 43 | LOCKED-as-drafted (no ±tolerance walk needed — no vendor URLs) |
| §12 | Verdict Math — deterministic ∧-of-gates, zero tunable thresholds (13-term PASS conjunction + 9-rule routing tree) | `ARS-2026-06-01-Day-43-...-Partial-2.md` | Day 43 | LOCKED-as-drafted |
| §13 | 14 Critical Decisions LOCKED (8 Day 40 + 2 Day 41 RESOLVED + 4 Day 43; 1 DEFERRED on §3.9) | `ARS-2026-06-01-Day-43-...-Partial-2.md` | Day 43 | LOCKED-as-drafted (operator sign-off Item 8 — Decisions #4/#13 PRELIMINARY) |
| §14 | Implementation Plan (calendar + dependencies + Rest Day) | `ARS-2026-05-30-Day-41-...-Partial-1.md` | Day 41 | LOCKED-as-drafted (Day 44 entry appended below) |
| §15 | Change Log + Version History (outline-day-40 → LOCKED · v1.0.1 + v1.1+ reservations) | `ARS-2026-06-01-Day-43-...-Partial-2.md` | Day 43 | LOCKED-as-drafted (Day 44 entry appended below) |
| §16 | Metadata Block Schema (Cross-SPEC §3.9 canonical + 4 QC Pre-flight additions) · §16.3 §3.9 amendment language for ceremony | `ARS-2026-06-01-Day-43-...-Partial-2.md` | Day 43 | LOCKED-as-drafted (operator ratification Item 11) |

**Rule:** This unified document is the operator LOCK ratification record. The three source files (Day 40 outline · Day 41 partial 1 · Day 43 partial 2) remain canonical for §-by-§ content. This document references them by file + day. Any §-content edit triggers the corresponding source file update + this unified document's `§15.1 v1.0-corrections-day-44` entry.

---

## §3 — THE 14 CRITICAL DECISIONS (operator walk-through reference — Item 8)

Reproduced from Day 43 §13 for operator review. Each: decision · status · rationale · alternative · revisit trigger. PRELIMINARY items annotated `[P]`; the DEFERRED item annotated `[D]`.

| # | Decision | Status | Rationale | Alternative (rejected) | Revisit trigger |
|---|----------|--------|-----------|------------------------|-----------------|
| 1 | **Pre-flight scope only at v1.0** (production → post boundary; full #14 pre-publish gate deferred) | LOCKED Day 40 | In-post fleet (Ingest/Edit/Sound/Motion) not built; v1.0 gates the output it can see — highest-leverage buildable slice | Build full #14 gate now — cannot gate post-production that doesn't exist | In-post fleet ships → v1.1 full pre-publish #14 gate |
| 2 | **Universal tier access** (all 4 tiers traverse the gate) | LOCKED Day 40 | Safety is not a tier feature; a Pilot leak = the same incident as a Enterprise leak | Gate Pro/Enterprise only (like Style Replication) — leaves Pilot/Starter Mode A with no final safety pass | Never (foundational) |
| 3 | **Verdict model: Pass/Fail/Reshoot + `drift_unresolved` soft-hold (4th outcome)** | LOCKED Day 40 (drift semantics confirmed Day 43) | Three machine verdicts + one human-deferred outcome covers every routing need; carried drift is held, never auto-passed/failed | Pass/Fail only — conflates fix-it / re-shoot / ask-the-human, destroying routing signal | New routing category surfaces in production telemetry |
| 4 [P] | **Route-back map** (fail→responsible agent · reshoot→ProdCoord · hold→human) | LOCKED Day 43 `[PRELIMINARY · operator amend]` | Each non-pass outcome routes to the precise stage that can fix it — the routing signal is the gate's whole downstream purpose | Single generic "route back to orchestrator" — loses responsible-agent attribution | Orchestrator auto-re-entry built (Dec #13) → route map gains auto-dispatch |
| 5 [D] | **6-tuple parent_chain** (inherits Style Replication 5-tuple + appends `preflight_report_id`) | **DEFERRED on Cross-SPEC §3.9 ratification** | Generalization required for the 10 remaining agent slots; QC Pre-flight is the first 6-tuple consumer = the forcing function | Stay at 5-tuple (rejects QC appendage) / per-agent custom shape (canon fragmentation) | Cross-SPEC §3.9 n-tuple amendment ratified (Item 11) |
| 6 | **errorEnvelope code count = 9 LOCKED + slot-11 catch-all** | RESOLVED Day 41 §6.3 | 9 codes preserve precise route-back attribution; folding below 9 forces ambiguous routing. Narrowed from 11 (2 folds) | 7 codes (collapses distinct root causes) / 11 codes (2 are semantic aliases) | New failure category with no route mapping → v1.0.1 code add |
| 7 | **Self-QC check count = 12** | RESOLVED Day 41 §6.1 | 12 checks bipartite-cover the 9 codes + slot-11 (entry / substance / deferral / report-integrity tiers) | 10 checks — under-covers report-construction integrity tier (#10–#12) that prevents a malformed PASS | A check consistently passes-all in telemetry → v1.0.1 simplification |
| 8 | **False-pass tolerance = ZERO** (bias all ambiguity to fail/hold) | LOCKED Day 40 | A terminal brand-safety gate must never pass a breach; over-blocking is the safe failure direction (§8.2 asymmetry) | Tunable confidence threshold — a knob someone lowers under launch pressure = false-pass risk (§12.3) | Never (foundational) |
| 9 | **Engine policy: NO generative engine; optional native pHash/CLIP re-verify on contested drift only** | LOCKED Day 40 | The agent reasons over output; it does not produce it. $0 render ceiling is forbidden-spend, not bounded-spend (§11.4) | Allow a cheap re-render to fix defects in-gate — that's the production agents' job; the gate adjudicates, not patches | Frame-level visual QC need (v1.1+) may add bounded native compute |
| 10 | **Recommend-don't-approve** (emit `human_review_required: true` + recommendation; never "approved for publish") | LOCKED Day 40 | The operator-impersonation firewall (CLAUDE.md + ARS attestation). A `pass` = "clear to advance to the human's publish decision," not "published" | Auto-approve clean reels — non-negotiable violation of Lever-3 operator-only ratification | Lever-2 graduation (post-90 reels, operator-gated) may relax the human-review default — operator decision only |
| 11 | **LUFS / loudness check DEFERRED to v1.1** | LOCKED Day 40 | Requires the Sound agent's output (−14 LUFS IG/TT, −16 LUFS YT per Blueprint #12); in-post fleet not built | Stub a LUFS check now — cannot verify loudness on output that doesn't exist | In-post fleet ships → full pre-publish #14 gate |
| 12 | **Schema strategy: new `preflight_report` output schema; reuse Cross-SPEC errorEnvelope + metadata shapes** | LOCKED Day 40 | The report is a net-new artifact (judgments, not transformations); errorEnvelope + metadata are fleet canon reused unchanged | Extend Style Replication's output schema — a verdict report is structurally unlike a shot array | Never (foundational) |
| 13 [P] | **Route-back automation depth: ADVISORY in v1.0** (emit `route_back_to` + `recovery_path`; no auto-re-entry) | LOCKED Day 43 `[PRELIMINARY · operator amend]` | v1.0 surfaces the route for operator dispatch; auto-re-entry is an orchestrator feature, not a gate feature. Keeps the human in the loop at Lever-3 | Auto-re-enter the pipeline on fail — premature automation before orchestrator re-entry logic is built + tested | Orchestrator re-entry logic ships → v1.1 auto-dispatch |
| 14 | **`reshoot` verdict is Mode A-exclusive** | LOCKED Day 43 (from outline OQ #6) | Live footage can be re-shot; AI output is re-generated, never re-shot. Mode B/C defects route as `fail` to the production agent | `reshoot` reachable in all modes — nonsensical for AI-generated output | Never (foundational mode semantics) |

**Operator walk-through prompt (for the LOCK ceremony):**
For each decision above, the operator either: (a) RATIFY-AS-LOCKED, (b) AMEND-with-rationale (triggers `§15.1 v1.0-corrections-day-44` entry), or (c) DEFER-to-v1.0.1 (decision parks in §15.2 candidates lot).

**Items requiring explicit verdict:**
- #4 Route-back map `[P]` → Donna recommends **RATIFY**
- #13 Route-back automation depth `[P]` → Donna recommends **RATIFY**
- #5 6-tuple parent_chain `[D]` → **DEFERRED** on §3.9 amendment (Item 11); Donna will NOT auto-advance. Hold at 5-tuple until ratified.

---

## §4 — IMPLEMENTATION PLAN UPDATE (Day 44 entry · appends to Day 41 §14)

### Calendar status updates (Day 44)

| Day | Date | Deliverable | Status | Owner |
|-----|------|-------------|--------|-------|
| Day 40 | Fri May 29 · Wk6 | SPEC outline §0–§5 LOCKED-as-shipped | ✅ DONE | Donna overnight |
| Day 41 | Sat May 30 · Wk6 | SPEC body partial 1 §6 / §7 / §10 / §14 LOCKED-as-drafted (9 codes + slot-11 LOCKED · 12 self-QC checks LOCKED) | ✅ DONE | Donna overnight |
| Day 42 | Sun May 31 · Wk6 | **REST DAY** (6th observance) — pre-stage partial 2 scaffold only | ✅ HONORED | — |
| Day 43 | Mon Jun 1 · Wk6 | SPEC body partial 2 §8 / §9 / §11 / §12 / §13 / §15 / §16 LOCKED-as-drafted (14/14 §13; SPEC body §6–§16 COMPLETE) | ✅ DONE | Donna overnight |
| **Day 44** | **Tue Jun 2 · Wk7D1** | **v1.0 LOCK CANDIDATE (this document) — 8/11 reviewer items PASS · 3 OPERATOR-ONLY (Items 6, 8, 11)** | **🟡 CANDIDATE** | **Donna overnight (this doc) + Jamila ratification** |
| Day 45+ | Wed Jun 3+ | `input.schema.json` + `output.schema.json` authored from §10 field map + §16 metadata block (schema holds parent_chain `minItems: 5` until §3.9 ratifies) | ⬜ QUEUED (primed per §16.5 encoding decisions) | Donna overnight |
| Day 46+ | Thu Jun 4+ | SKILL bundle (SKILL.md · 2 schemas · 5 test fixtures · README) | ⬜ QUEUED | Donna overnight |
| Sun | — | **REST DAY** (no SPEC content authored) | ⬜ — | — |
| Day 47+ | — | LLM Test Runbook (paste-and-run · pattern from Day 11 / 19 / 27 / 36 · operator-gated) | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 48+ | — | **v1.0 LOCK** (operator-gated sit-down · HARD-GATED on AI Video Gen v1.0 LOCK + Style Replication v1.0 LOCK first) | ⬜ GATED | Jamila + Donna co-ceremony |

### Dependencies that MUST exist before the SKILL-bundle build
1. v1.0 LOCK CANDIDATE ratified (operator sign-off Items 6, 8, 11) — **available now**
2. input.schema.json + output.schema.json LOCKED (schemas day)
3. 5 test fixtures resolved against schemas (schemas-day dry-run validation)
4. Cross-SPEC §3.9 amendment ratified OR parent_chain held at `minItems: 5` with documented TODO (Item 11)

### Hard gate on production-tier LOCKs
QC Pre-flight v1.0 LOCK ceremony **CANNOT complete until BOTH AI Video Gen v1.0 AND Style Replication v1.0 are LOCKED first** — QC Pre-flight consumes both as input branches (it cannot terminally gate output whose producing agents are not themselves LOCKED). Both predecessor LOCK candidates are operator-gated with items still pending (see §6). This is a **hard gate**, distinct from the 3 QC-local operator items (6, 8, 11) which can be ratified independently and in advance.

### Rest Day honor
Day 42 (Sun May 31) honored — 6th observance. The next Sunday in the schemas → SKILL → runbook runway is a no-SPEC-content day (docs prep only). This Day 44 build runs on Tuesday — permitted.

---

## §5 — CHANGE LOG UPDATE (Day 44 entry · appends to Day 43 §15)

| Version tag | Date | Description | Source file |
|-------------|------|-------------|-------------|
| **v1.0-LOCK-CANDIDATE-day-44** | **2026-06-02 (Tue · Wk7D1)** | **Unified LOCK candidate document produced. Day 44 reviewer checklist 8/11 PASS executed autonomously by Donna overnight. Items 6 (cost-model/inherited-ceiling confirm — no vendor URLs to walk) + 8 (14 critical decisions sign-off, Decisions #4/#13 PRELIMINARY requiring explicit verdict) + 11 (Cross-SPEC §3.9 amendment ratification — 6-tuple parent_chain extension, the carried forcing function) flagged OPERATOR-ONLY. Decision #5 (6-tuple) explicitly DEFERRED — held at 5-tuple until §3.9 ratifies. Pending operator ratification of items 6/8/11 → promote to `v1.0-LOCKED-pending-predecessor-LOCKs`; final flip to `v1.0-LOCKED` ONLY after BOTH AI Video Gen v1.0 + Style Replication v1.0 LOCK ceremonies complete (hard gate).** | `ARS-2026-06-02-Day-44-QC-Preflight-Agent-v1-LOCK-CANDIDATE.md` (this doc) |

**Promotion rule:** When the operator ratifies Items 6, 8, 11 (at ceremony or asynchronously via written sign-off in the Notion ARS hub), version tag promotes to `v1.0-LOCKED-day-44-pending-predecessor-LOCKs`. Final flip to `v1.0-LOCKED` occurs ONLY after BOTH production-tier predecessor LOCKs (AI Video Gen + Style Replication) are confirmed. Donna mirrors LOCKED status across: this unified document header · the Notion ARS hub (page [internal Notion page]) · the schemas-day authoring kickoff · the Cross-SPEC v1.1 amendment formal close (if Item 11 ratified).

---

## §6 — OPEN QUESTIONS · STATUS

### Open Question — Cost-model / inherited-ceiling confirmation (Item 6)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony — the lightest in fleet history (no vendor-pricing URLs; QC Pre-flight calls no engine). Operator confirms the inherited combined ceilings ($450 / $870 / ≤$40) still match production-agent canon.
**Recommendation:** RATIFY as-is (≈2 min). **Blocker for LOCK:** No — ceilings are downstream inheritances, not QC-local canon.

### Open Question — 14 critical decisions sign-off (Item 8)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Walk each decision; 12 LOCKED-as-drafted, 2 PRELIMINARY (#4, #13) require explicit RATIFY / AMEND / DEFER.
**Recommendation:** Donna recommends RATIFY for both PRELIMINARY items. **Blocker for LOCK:** Yes — hard-required for promotion.

### Open Question — Cross-SPEC §3.9 amendment ratification / 6-tuple (Item 11 + Decision #5)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Amendment language §16.3 reproduced in §1 Item 11. QC Pre-flight is the first 6-tuple consumer = the forcing function.
**Recommendation:** RATIFY-AS-DRAFTED — generalization is necessary for the 10 remaining agent slots. **Blocker for LOCK:** Partial — schema can ship at `minItems: 5` with a documented TODO if the operator defers; QC Pre-flight does not hard-block on it, but the 6-tuple stays un-advanced until ratified.

### Open Question — Hard gate on production-tier LOCKs (AI Video Gen + Style Replication)
**Status:** ⏸ OPERATOR action required on BOTH predecessor LOCK ceremonies. AI Video Gen Day 24 LOCK candidate (Items 8 + 11 pending) + Style Replication Day 32 LOCK candidate (Items 6 + 8 + 11 pending) + the Day 36 Style Replication LLM Test Runbook execution (5/5 PASS is the LOCK gate; outcome unconfirmed) all remain operator-pending.
**Recommendation:** Donna recommends the operator close both production-tier LOCKs in the post-launch hardening window. **Blocker for QC Pre-flight LOCK:** YES (hard gate) — QC Pre-flight's terminal-gate LOCK cannot complete until both producing agents are LOCKED.

### Open Question — LLM Test Runbook scope (dry-run vs live mode · forward-looking)
**Status:** ⏸ OPERATOR-ONLY at the runbook day (not blocking Day 44 LOCK CANDIDATE).
**Recommendation:** Donna recommends **dry-run mode for the v1.0 LOCK gate** (cost ≈ $0 — QC Pre-flight calls no engine anyway, so even "live" mode is reasoning-only at near-zero cost; the optional native pHash/CLIP re-verify is the only non-zero line and fires only on contested drift). This is the cheapest runbook in the fleet. **Blocker for LOCK:** No — runbook-day position.

---

## §7 — PARKED ITEMS (Notion ARS P3 · carried from prior surfacing)

1. "ARS Daily Build Session — Notion page created 4/22 but empty; verify transcription pipeline or delete placeholder" (P3 · Sequel Digital · Open).
2. "ARS Daily Build Session page is empty — confirm whether session occurred and transcribe if so" (P3 · Sequel Digital · Open).

**Donna's recommendation unchanged:** close both as "transcript lives in `ars/` (canon on disk: outline + 2 partials + LOCK candidate + build logs + 6 LIVE skill bundles), not Notion." Operator's call.

---

## §8 — PROCESS INTEGRITY (Day 44)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked (QC Pre-flight has no vendor-pricing surface — Item 6 is the lightest operator confirm in fleet history). ZERO $ spent.
- ✅ **No external comms.** No emails sent, no DMs, no social posts, no investor/client outreach. The end-of-run status SMS to [status number redacted] is the only outbound attempt, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs initiated.
- ✅ **No operator-impersonation.** Day 44 reviewer Items 6, 8, 11 verdicts NOT silently advanced. Decisions #4/#13 (PRELIMINARY) NOT silently ratified. **Decision #5 (6-tuple parent_chain) explicitly DEFERRED — held at 5-tuple; the one item Donna will NOT auto-advance.** Both production-tier predecessor LOCK ceremonies confirmed STILL-PENDING via on-disk file-state; NOT advanced. Day 36 Style Replication runbook execution NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed to Cross-SPEC canon.
- ✅ **No fake-advance.** This LOCK CANDIDATE is a unified text-reconciliation of the Day 40 outline + Day 41 + Day 43 partials. Zero behavioral changes vs source files. Zero net-new SPEC content. The only Day 44 contributions are: (a) executive summary (§0 LOCK manifest), (b) 11-item reviewer checklist execution record (§1), (c) unified SPEC index pointing to source files (§2), (d) decision walk-through formatted for operator ceremony (§3), (e) implementation plan + change log appendages (§4 + §5).
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication SPECs + schemas + SKILL bundles + the QC Pre-flight Day 40 outline + Day 41 partial 1 + Day 43 partial 2 all untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. The HC/NPOX tokens in the §9.3 TC-03 fixture + the §5 Step 2 entity-firewall regex are the firewall's BLOCK-list test cases, not cross-entity references.
- ✅ **Pattern source acknowledged.** Day 24 AI Video Gen + Day 32 Style Replication LOCK candidate structure inherited at section level (§0 manifest · §1 reviewer execution · §2 unified index · §3 decisions walk-through · §4 implementation plan · §5 change log · §6 open questions). Numerical values + decision content re-derived for QC Pre-flight's 9-code / 12-check / 14-decision / 6-tuple scope.
- ✅ **Rest Day honored.** Day 42 (Sun May 31) observed; this Day 44 build runs on Tuesday.

---

## §9 — SPRINT STATS (running total · Day 44 close)

- Deliverables shipped: **39** (Day 43 = 38 · Day 44 QC Pre-flight v1.0 LOCK CANDIDATE = +1)
- Build logs: **38** (was 37 · +1 today)
- LIVE skill bundles: **6** (Brief · Script · Storyboard · ProdCoord · AI Video Gen · Style Replication — both production-tier LOCKs still operator-pending)
- Agents with a COMPLETE SPEC body (§6–§16): **7** (QC Pre-flight body completed Day 43)
- Agents with a v1.0 LOCK CANDIDATE: **3** (AI Video Gen Day 24 · Style Replication Day 32 · **QC Pre-flight Day 44**)
- errorEnvelope codes (QC Pre-flight): **9 LOCKED + slot-11** (no change Day 44)
- Self-QC checks (QC Pre-flight): **12 LOCKED** (no change Day 44)
- parent_chain (QC Pre-flight): **6-tuple DRAFTED Day 43 · DEFERRED on §3.9 · held at 5-tuple (`minItems: 5`)**
- §13 critical decisions: **14/14 §13 coverage** (13 LOCKED-as-drafted + 1 DEFERRED) — Decisions #4/#13 PRELIMINARY require explicit verdict at the ceremony
- Cross-SPEC §3 adherence: **11/11 ✅**
- Verdict math: **deterministic ∧-of-gates · zero tunable thresholds** (the only agent whose correctness is a boolean conjunction with no calibration surface)
- Rest Day observances: **6/6**
- AI Video Gen v1.0 LOCK: **CANDIDATE (operator-pending)** — hard-gates QC Pre-flight LOCK
- Style Replication v1.0 LOCK: **CANDIDATE + RUNBOOK (operator-pending)** — hard-gates QC Pre-flight LOCK

---

## §10 — OPERATOR ACTION SUMMARY (3 QC-local items + 1 hard-gate dependency)

The Day 44 LOCK CANDIDATE is ready for operator pickup. Three QC-local operator actions (any can move first, all independent) + one hard-gate dependency.

| Action | Time | Description |
|--------|------|-------------|
| **Item 6 — Cost-model / inherited-ceiling confirm** | ~2 min | Confirm the inherited combined ceilings ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter) still match production-agent canon. NO vendor URLs to walk (QC Pre-flight calls no engine). Donna recommends RATIFY as-is. |
| **Item 8 — 14 decisions walk-through** | 15–25 min | Walk §3. For each of 14 decisions: RATIFY / AMEND / DEFER. Special attention on 2 PRELIMINARY items (#4 route-back map, #13 route-back automation depth) — Donna recommends RATIFY for both. |
| **Item 11 — Cross-SPEC §3.9 amendment (6-tuple)** | 10 min | Review the amendment language in §1 Item 11 (n-tuple parent_chain generalization; QC Pre-flight = first 6-tuple consumer). RATIFY-AS-DRAFTED / AMEND / DEFER. Donna recommends RATIFY-AS-DRAFTED. If deferred, schema holds at `minItems: 5`. |

**After all 3 QC-local items ratified:** Donna promotes version tag to `v1.0-LOCKED-day-44-pending-predecessor-LOCKs`. Schemas-day authoring unblocks.

**Hard-gate dependency (operator action, NOT a QC-local LOCK item):** Close BOTH production-tier predecessor LOCKs — **AI Video Gen v1.0** (Day 24 candidate · Items 8 + 11 pending) and **Style Replication v1.0** (Day 32 candidate · Items 6 + 8 + 11 pending · Day 36 LLM runbook 5/5 PASS unconfirmed). **QC Pre-flight's final v1.0 LOCK flip cannot occur until both are LOCKED** — it is the terminal gate that consumes both as input branches.

---

*Day 44 ships clean. Unified LOCK CANDIDATE produced as a text-only reconciliation of the Day 40 outline + Day 41 + Day 43 partials. Zero net-new SPEC content. Zero fake-advance. 8/11 reviewer items PASS autonomously verdicted by Donna; 3 OPERATOR-ONLY items (6, 8, 11) flagged with explicit recommendations and timing estimates. Pattern source: Day 24 AI Video Gen + Day 32 Style Replication LOCK candidates (proven 11-item reviewer shape, 3rd reuse, adapted to QC Pre-flight's 9-code / 12-check / 14-decision / 6-tuple scope). QC Pre-flight is Agent #7 of 17 — the 7th and LAST automated defense-in-depth firewall, the first universal-tier gate since Brief, and the only agent with threshold-free deterministic verdict math. Its v1.0 LOCK lands in the post-launch hardening window and is HARD-GATED on both production-tier predecessor LOCKs closing first. The two production-tier LOCK ceremonies + the Day 36 runbook execution + the Cross-SPEC §3.9 amendment ratification remain operator-only and are surfaced, not advanced. The 6-tuple parent_chain (Decision #5) is the one item Donna will NOT auto-advance — held at 5-tuple until §3.9 ratifies.*
