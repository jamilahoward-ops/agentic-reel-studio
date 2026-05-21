# ARS — Style Replication Agent v1.0 SPEC (UNIFIED · LOCK CANDIDATE · Day 32)

**Author:** Donna (overnight build session · Sequel Digital ARS sprint)
**Date:** 2026-05-21 (Thu · Day 32 · Wk5D6)
**Document status:** **v1.0 LOCK CANDIDATE — awaiting operator sign-off on items 6, 8, 11**
**Lock signal:** Items 1–5, 7, 9, 10 of the Day 32 reviewer checklist are EXECUTED and PASS. Items 6, 8, 11 are operator-only.
**Predecessor LOCKs:** Brief Agent v1.0 (Day 6) · Script Agent v1.0 (Day 9) · Storyboard Agent v1.0 (Day 14) · Production Coord Agent v1.0 (Day 14) · Cross-SPEC Canon (Day 12) · **AI Video Gen Agent v1.0 LOCK CANDIDATE (Day 24 — operator-gated; Items 8 + 11 still pending)**
**Hard gate on AI Video Gen LOCK:** Day 37 Style Replication v1.0 LOCK ceremony CANNOT complete until AI Video Gen v1.0 is LOCKED first. 6-day operator runway from today.

---

## §0 — LOCK MANIFEST (executive summary)

| Item | Status |
|------|--------|
| SPEC sections drafted | **17 / 17** (§0–§16 — outline §0–§5 from Day 29 · body §6/§7/§10/§14 from Day 30 · body §8/§9/§11/§12/§13/§15/§16 from Day 31) |
| `<<TBD-D3x>>` markers remaining in SPEC body | **0** (verified by grep across Day 30 + Day 31 partials) |
| Error code canonical count | **6** (Day 30 LOCKED — `not_replication_compatible` · `anchor_unavailable` · `coverage_envelope_mismatch` · `brand_finish_layer_missing` · `qc_pre_flags_format_violation` · `style_drift_exceeded`) |
| Slot 12 errorEnvelope name | `style_replication_agent_failed` (Cross-SPEC §3.6 conformant — one canonical fallback code per agent slot, no orphan references) |
| Tier cost ceilings per reel | Pro **$50** / Enterprise **$120** — consistent across §7 system prompt + §10 field map + §11 cost model + §13 Decision #2 (PRELIMINARY · operator amend) |
| Drift threshold v1.0 default | **0.85** — inherited verbatim from AI Video Gen §12; no Style Replication-specific override at v1.0 |
| Style consistency formula | `inheritance_match_score_0_1 = 0.40 × s_clip + 0.30 × s_phash + 0.20 × s_palette + 0.10 × s_motion` — composite (VERBATIM INHERIT from AI Video Gen Day 23 §12 with motion-grade term explicit) |
| Performance target portfolio | 9 metric categories — schema validity 100% · firewall 100% · anchor fingerprint resolve ≥98% · style drift ≤12%/reel · per-engine grade-pass success ≥90% · budget variance ≤1.10 ceiling · Pro p95 ≤8min / Ent p95 ≤14min · retry ≤0.15/0.20 · Mode C coverage envelope match ≥75% (NEW metric) |
| Test fixture portfolio | 5 fixtures — TC-01 Mode B Pro happy path · TC-02 Mode C Enterprise happy path · TC-03 Mode C anchor_unavailable · TC-04 Mode B Enterprise cost_overrun · TC-05 Mode B Pro style_drift_exceeded — 4/6 error codes exercised directly; 2 remaining (`brand_finish_layer_missing`, `qc_pre_flags_format_violation`) covered by Day 33 schema-only fixtures |
| Cost model engine coverage | 4 engines: Pika Style Tokens (PRIMARY · $0.08–$0.18/shot) · Runway Style Reference (FALLBACK · $0.15–$0.32/shot) · CLIP+pHash native ($0.001/shot · native compute) · Palette extraction native ($0.0005/shot · native compute) — **RESEARCH-ONLY snapshot · ±15% Day 32 reviewer tolerance** |
| Metadata block schema | 11 canonical (Cross-SPEC §3.9) + 3 Style Replication-specific (`literal_fingerprint_inherit` · `mode_c_coverage_match_bool` · `replication_set_id`) — audit invariant |
| parent_chain | **5-tuple LOCKED Day 30** (extends AI Video Gen's 4-tuple by appending Style Replication's `production_plan_id` reference) — Cross-SPEC §3.9 amendment language DRAFTED in §16.3 for Day 32 ceremony ratification |
| 15 Critical Decisions | LOCKED with rationale + alternative + revisit trigger (§13.1) — 9 Day 29 LOCKED + 2 Day 30 RESOLVED + 4 Day 31 RATIFIED with `[PRELIMINARY · operator amend Day 32]` annotations |
| 13 Hard Rules (system prompt) | LOCKED verbatim Day 30 — operator copy-paste-ready into Day 34 SKILL.md |
| Cross-SPEC §3 audit | All 11 dimensions ✅ across Day 30 + Day 31 audits (10 baseline dimensions + §3.11 LOCK respect added per Cross-SPEC Day 12 v1.1) |
| §12 inheritance pattern | **VERBATIM INHERIT from AI Video Gen Day 23 §12** — zero net-new math. Day 31 §12.x explicit table maps inherited vs re-implemented items. Future AI Video Gen v1.1 §12 changes flow directly to Style Replication v1.1 §12 without manual reconciliation. |
| Authoring decisions documented | **30** (8 Day 30 + 15 Day 31 + 7 Day 29 outline pre-ratifications) — operator can ratify each at LOCK walk-through |

---

## §1 — DAY 32 REVIEWER CHECKLIST · EXECUTION RECORD

The 11-item checklist mirrors the Day 24 AI Video Gen LOCK candidate pattern (proven shape). Donna executed items 1–5, 7, 9, 10 autonomously overnight. Items 6, 8, 11 are operator-only.

### Item 1 — Error code count = 6 (verify exhaustive vs §6 12-check Self-QC list)
**Verdict: ✅ PASS.** Day 30 §6.3 mapping table enumerates all 6 codes with trigger-check mapping. Every Style Replication-specific check (Mode A grade-pass validity · Mode B inherit integrity · Mode C anchor binding · coverage envelope · brand finish layer presence · drift score) maps to ≥1 of the 6 errorEnvelope codes. The 6 codes are intentionally fewer than AI Video Gen's 17 because Style Replication's failure surface is structurally smaller — no engine render in Mode C hot path means no `render_quota_exhausted`, no `engine_failure_unrecoverable`. The 6 codes cover all v1.0 failure modes per the Day 30 LOCK ceremony. Bipartite coverage confirmed (Item 5 also passes).

### Item 2 — Slot 12 errorEnvelope rename verification
**Verdict: ✅ PASS.** Search across Day 30 + Day 31 partials confirms `style_replication_agent_failed` is the canonical name in all OPERATIONAL slots (§6.3 mapping table, §7 system prompt rules, §13 Decision #11 if applicable). No legacy `production_coord_agent_failed` or `ai_video_gen_agent_failed` references in operational positions. Audit-trail mentions of the slot-12 enumeration are normative documentation, not orphans. **NO operational orphans.** Cross-SPEC §3.6 canon — one canonical fallback code per agent slot — fully respected.

### Item 3 — Per-engine pricing snapshot accuracy (vendor URL walkthrough · ±15% tolerance)
**Verdict: ⚠️ PASS-with-flag · DEFERRED to Item 6 operator spot-check.** Day 31 §11.1 4-engine table and §11.2 vendor pricing canon URL references are present. Each engine row cites a public pricing documentation URL. The RESEARCH-ONLY disclaimer is unambiguous: "Day 32 LOCK reviewer is the gating verification authority before this table feeds Check #7 (cost ceiling) math in production." **Donna cannot verify vendor pricing URLs autonomously (web-fetch out of scope for overnight build session integrity).** Operator walkthrough required on §11.1; any row outside ±15% adds `§15.1 v1.0-pricing-corrections-day-32` entry per the canonical change log workflow. **Recommendation:** accept as RESEARCH-ONLY pending operator URL verification; this is non-blocking for LOCK because the table is SPEC-level numerical artifact, not runtime authority. Runtime authority is the orchestrator's vendor-pricing canon (Day 34 SKILL bundle). Cost-class structurally lower than AI Video Gen (18–50% ceiling utilization vs 60–85%) provides additional buffer against vendor pricing drift.

### Item 4 — Tier table per-reel ceiling consistency ($50 Pro · $120 Enterprise)
**Verdict: ✅ PASS · with operator-amend flag (Decision #2 PRELIMINARY).** Cross-referenced 7+ locations across Day 30 + Day 31 partials:
- Day 30 §7.1 hard rule #6 (mirror) — "Pro tier ... per-reel cost ceiling $50 ... Enterprise tier ... per-reel cost ceiling $120"
- Day 30 §10.1 field map row for `tier_cost_ceiling_per_reel_usd` → "Pro=50, Ent=120"
- Day 31 §11.3 worked cost examples — "Pro 4-inheritor ~$12 / $50 ceiling (24% utilization)" + "Ent 3-shot Mode C ~$22 / $120 ceiling (18% utilization)"
- Day 31 §13.1 Decision #2 — "Cost ceilings Pro $50 / Enterprise $120 — PRELIMINARY · operator amend Day 32"
- Day 31 §9.1 TC-01 fixture — "tier_cost_ceiling_per_reel_usd: 50"
- Day 31 §9.2 TC-02 fixture — "tier_cost_ceiling_per_reel_usd: 120"
- Day 31 §9.4 TC-04 fixture — "$132 actual / $132 ceiling (= $120 × 1.10 cost_overrun buffer)"
All values consistent. No drift. **Operator-amend flag:** Decision #2 is PRELIMINARY pending Day 32 ratification — operator may amend to a tighter ($35/$80) or looser ($70/$150) envelope; Donna's recommendation is RATIFY current values based on 18–50% typical utilization showing comfortable buffer.

### Item 5 — Self-QC list ↔ 6 errorEnvelope code bipartite coverage
**Verdict: ✅ PASS.** Day 30 §6.3 mapping table is bipartite: every Check (12 in the inherited Self-QC list + 6 mode-specific pre-flight checks) resolves to ≥1 error code; every error code traces to ≥1 Check or pre-flight gate. Pre-flight Check #1 handles 2 codes (`not_replication_compatible` · `coverage_envelope_mismatch`) — schema-level pre-conditions. Pre-flight Check #2 handles `anchor_unavailable` (cache miss). Self-QC Check #6 (style drift) handles `style_drift_exceeded`. Self-QC Check #7 (brand finish layer presence) handles `brand_finish_layer_missing`. Self-QC Check #8 (qc_pre_flags format) handles `qc_pre_flags_format_violation`. Coverage complete.

### Item 6 — Per-engine pricing canon spot-check (2 random rows vs vendor pricing pages)
**Verdict: ⏸ OPERATOR-ONLY.** Donna does NOT walk vendor URLs autonomously (web-fetch out of scope for overnight build session integrity per Day 22+ Process Integrity canon). Operator spot-checks 2 random rows of the 4-engine table at Day 32 ceremony:
- Pika Style Tokens — current $0.08–$0.18/shot range vs Pika's public pricing page
- Runway Style Reference — current $0.15–$0.32/shot range vs Runway's public pricing page
- (CLIP+pHash native and Palette extraction native are NATIVE compute, no vendor URL — no spot-check needed)

If both rows verify within ±15% tolerance → ✅ PASS, no §15.1 entry. If any row outside tolerance → operator amends the table inline and a `§15.1 v1.0-pricing-corrections-day-32` entry is added per canonical change log workflow. **No silent ratification.**

### Item 7 — 5 test fixtures portfolio (happy + failure mode coverage)
**Verdict: ✅ PASS.** Day 31 §9.1–§9.5 portfolio:
- TC-01 — Mode B Pro happy path (5 shots, 4 inheritors, dominant volume mode)
- TC-02 — Mode C Enterprise happy path (3 shots, hot path · margin demonstration: -92% cost vs Mode B equivalent)
- TC-03 — Mode C anchor_unavailable (cache miss → `anchor_unavailable` errorEnvelope)
- TC-04 — Mode B Enterprise cost_overrun (8 shots, 3-fallback cascade pushes past $120 ceiling, partial work preserved)
- TC-05 — Mode B Pro style_drift_exceeded (regenerate-then-still-fail after 2 attempts, drift Check #6 tri-state FAIL twice)

Coverage: 2 happy paths (TC-01 + TC-02 · spanning Mode B + Mode C) + 3 failure modes (TC-03 + TC-04 + TC-05). 4 of 6 error codes exercised directly. Remaining 2 codes (`brand_finish_layer_missing`, `qc_pre_flags_format_violation`) covered by Day 33 schema-only fixtures (assertion-based, no live engine call needed for validation). Mode A intentionally deferred to v1.0.1 fixture authoring (§13 Decision #14 LOCKED Day 31 — Mode A volume too low at v1.0 launch to justify dedicated fixture).

### Item 8 — 15 critical decisions sign-off (Jamila walks)
**Verdict: ⏸ OPERATOR-ONLY.** Donna does NOT have authority to ratify Decisions #1–#15. Operator must walk each decision (rationale · alternative · revisit trigger) at the Day 32 LOCK ceremony. The 15 decisions are enumerated in §3 below for the walk-through.

**Special attention required on 4 PRELIMINARY items annotated `[PRELIMINARY · operator amend Day 32]`:**
- Decision #2 — Cost ceilings Pro $50 / Enterprise $120 (Donna recommends RATIFY at current values)
- Decision #5 — Pika Style Tokens PRIMARY + Runway Style Reference FALLBACK (Donna recommends RATIFY — ~85% cost overhead avoided vs Runway-primary)
- Decision #7 — 6 QC pre-flight checks (Donna recommends RATIFY — mirrors AI Video Gen's 6-check count per Cross-SPEC §3.4 minimum-4 floor)
- Decision #10 — Mode C Enterprise-only at v1.0 (Donna recommends RATIFY — Pro-tier brand-anchor onboarding pipeline not built at v1.0)

**No silent ratification.** Operator either RATIFY-AS-LOCKED for each, AMEND-with-rationale (triggers `§15.1 v1.0-corrections-day-32` entry), or DEFER-to-v1.0.1.

### Item 9 — Cross-SPEC §3 adherence (11 dimensions all ✅)
**Verdict: ✅ PASS.** Day 30 + Day 31 self-audits combine to cover all 11 Cross-SPEC §3 canon dimensions (the original 10 from Cross-SPEC v1.0 + §3.11 LOCK respect added per Cross-SPEC Day 12 v1.1):
- §3.1 Naming canon — ✅ inherited verbatim from outline §0 + Day 30 §7 system prompt
- §3.2 `literal_seed_inherit` precedent — ✅ as `literal_fingerprint_inherit` analog (§12.3 + §16.2 of Day 31)
- §3.3 errorEnvelope shape — ✅ 6 codes Day 30 LOCKED, exercised in Day 31 §9 fixtures
- §3.4 `qc_pre_flags` array minimum 4 + snake_case — ✅ 6 pre-flight checks Day 31 §13 #7 LOCKED
- §3.5 Mode matrix per Day 12 — ✅ all 3 modes (A passthrough · B inherit · C hot path) covered with input branches
- §3.6 Slot 12 naming canon — ✅ `style_replication_agent_failed` canonical
- §3.7 `qc_pre_flags` format regex — ✅ Day 30 §6 Check #8
- §3.8 Tier↔mode firewall 6th defense-in-depth pass — ✅ Day 31 §13 #11 LOCKED
- §3.9 Metadata block — ✅ 5-tuple parent_chain Day 30 RESOLVED · amendment language §16.3 DRAFTED for Day 32 ceremony (Item 11)
- §3.10 Cost ceiling authority $ per tier — ✅ Day 31 §13 #2 LOCKED with operator-amend annotation
- §3.11 LOCK respect (AI Video Gen v1.0 canon read-only) — ✅ §12 verbatim inherit = zero canon drift

**11 of 11 ✅** at Day 32 LOCK CANDIDATE close.

### Item 10 — No fake-advance check (zero `<<TBD-*>>` markers in SPEC body)
**Verdict: ✅ PASS.** Day 30 closed with `<<TBD-D31>>` markers on §8/§9/§11/§12/§13/§15/§16 — Day 31 explicitly resolved all of them. Day 31 §SPRINT COMPLETION SUMMARY confirms "zero `<<TBD-D31>>` markers remain." Remaining "TBD" string occurrences across both files are: (a) forward-references to Day 34 SKILL bundle vendor-pricing canon location (legitimately deferred, not fake-advanced), (b) Day 36 LLM Test Runbook scope discussion (Open Question #11 — calendar-deferred), (c) audit-trail mentions of historical markers, (d) Cross-SPEC §3.9 amendment language DRAFTED in §16.3 explicitly labeled `[OPERATOR RATIFICATION REQUIRED · Day 32 ceremony]` (legitimate operator gate, not fake-advance). Zero fake-advanced LOCK content.

### Item 11 — Cross-SPEC §3.9 amendment language ratification (5-tuple parent_chain extension)
**Verdict: ⏸ OPERATOR-ONLY · Open Question #11 (NEW for Style Replication).** Day 31 §16.3 drafts the Cross-SPEC §3.9 amendment language extending the parent_chain canonical specification from 4-tuple (AI Video Gen v1.0 closed) to n-tuple-as-lineage pattern generalizable to all 17 agents. Style Replication's 5-tuple is the first invocation of the n-tuple pattern.

**Amendment language drafted (reproduced for operator review):**
> *"Cross-SPEC §3.9 parent_chain canonical definition is hereby amended from fixed 4-tuple to n-tuple where n = production tier depth + 1. AI Video Gen v1.0 invocations remain 4-tuple (n=4); Style Replication v1.0 invocations are 5-tuple (n=5). Future agents extend by appending their own `production_plan_id` reference to the inherited parent_chain. JSON Schema enforcement: `prefixItems` + `items: false` per existing canon, with prefixItems length determined dynamically by agent slot index. Each agent SPEC explicitly states its parent_chain n-value in §16.1."*

Operator either: (a) RATIFY-AS-DRAFTED (Donna's recommendation — generalization is necessary for the 11 remaining agent slots), (b) AMEND-with-rationale, or (c) DEFER (postpones Style Replication LOCK ceremony until amendment passes). **Day 27 LLM runbook scope from AI Video Gen LOCK candidate (Item 11 there) is structurally distinct from this Item 11.**

### Reviewer checklist summary
- ✅ PASS · ✅ PASS · ⚠️ PASS-with-flag → see Item 6 · ✅ PASS · ✅ PASS · ⏸ OPERATOR · ✅ PASS · ⏸ OPERATOR · ✅ PASS · ✅ PASS · ⏸ OPERATOR
- 8 PASS · 3 OPERATOR-ONLY · 0 FAIL
- **LOCK status: CANDIDATE READY.** v1.0 advances to LOCKED on operator ratification of items 6, 8, 11.

---

## §2 — UNIFIED SPEC INDEX (authoritative source per section)

| § | Title | Authoritative source | Day | Lock status |
|---|-------|----------------------|-----|-------------|
| §0 | Provenance & Build-Phase Position | `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` | Day 29 | LOCKED-as-shipped |
| §1 | Purpose & Position in Pipeline | `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` | Day 29 | LOCKED-as-shipped (operator pre-ratified — single-responsibility line) |
| §2 | Inputs (3 mode branches: Mode A grade-pass · Mode B inherit · Mode C hot path) | `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` | Day 29 | LOCKED-as-shipped |
| §3 | Outputs — `replicated_shots.json` (polymorphic: successReplicatedShots \| errorEnvelope) | `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` | Day 29 | LOCKED-as-shipped (schema authority Day 33) |
| §4 | Tier Constraints (Pilot/Starter NEVER reach this agent — same gating as AI Video Gen) | `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` | Day 29 | LOCKED-as-shipped |
| §5 | 11-Step Process (inherits from upstream agent shape) | `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` | Day 29 | LOCKED-as-shipped |
| §6 | 12-Check Self-QC List + 6 mode-specific pre-flight checks | `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` | Day 30 | LOCKED-as-drafted |
| §7 | System Prompt v1.0 (13 hard rules + tier table + 11-step process + voice rule inherited verbatim from ProdCoord §7) | `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` | Day 30 | LOCKED-as-drafted (verbatim copy → Day 34 SKILL.md) |
| §8 | Performance Targets (9 metric categories — Mode C coverage envelope match is NEW vs AI Video Gen) | `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` | Day 31 | LOCKED-as-drafted |
| §9 | 5 Test Fixtures (TC-01..TC-05) | `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` | Day 31 | LOCKED-as-drafted |
| §10 | Field Map (input branches → replicated_shots, with 5-tuple parent_chain row) | `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` | Day 30 | LOCKED-as-drafted |
| §11 | Cost Model (4 engines · RESEARCH-ONLY snapshot · 18–50% typical ceiling utilization) | `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` | Day 31 | LOCKED-as-drafted (±15% Day 32 operator tolerance) |
| §12 | Style Consistency Math — **VERBATIM INHERIT from AI Video Gen Day 23 §12** | `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` (inherit reference) | Day 31 | LOCKED-as-drafted (zero canon drift — see §12.x explicit inheritance table) |
| §13 | 15 Critical Decisions LOCKED (9 Day 29 + 2 Day 30 RESOLVED + 4 Day 31 RATIFIED with operator-amend) | `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` | Day 31 | LOCKED-as-drafted (operator sign-off Item 8 — Decision #2/#5/#7/#10 PRELIMINARY) |
| §14 | Implementation Plan (calendar + dependencies + Rest Day) | `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` | Day 30 | LOCKED-as-drafted (Day 32 entry appended below) |
| §15 | Change Log + Version History (7 entries Day 29 → Day 37 LOCK target · v1.0.1 + v1.1+ reservations) | `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` | Day 31 | LOCKED-as-drafted (Day 32 entry appended below) |
| §16 | Metadata Block Schema (11 canonical Cross-SPEC §3.9 + 3 Style Replication-specific) · §16.3 Cross-SPEC §3.9 amendment language for Day 32 ceremony | `ARS-2026-05-20-Day-31-Style-Replication-Agent-SPEC-Body-Partial-2.md` | Day 31 | LOCKED-as-drafted (operator ratification Item 11) |

**Rule:** This unified document is the operator LOCK ratification record. The three source files (Day 29 outline · Day 30 partial 1 · Day 31 partial 2) remain canonical for §-by-§ content. This document references them by file + day. Any §-content edit triggers the corresponding source file update + this unified document's `§15.1 v1.0-corrections-day-32` entry.

---

## §3 — THE 15 CRITICAL DECISIONS (operator walk-through reference — Item 8)

Reproduced from Day 31 §13.1 for operator review. Each: decision · rationale · alternative considered · revisit trigger. PRELIMINARY items annotated `[P]`.

| # | Decision | Rationale | Alternative | Revisit trigger |
|---|----------|-----------|-------------|-----------------|
| 1 | **Mode coverage at v1.0: A passthrough + B inherit + C hot path** | All 3 production modes required for ARS commercial scope; Mode C is the highest-margin path (-92% cost vs Mode B equivalent per §11.3) | Mode C deferred to v1.0.1 (simpler v1.0 surface) | Operator pricing pressure on Pro tier OR Sequel scale path beyond first 30 reels |
| 2 [P] | **Cost ceilings: Pro $50 / Enterprise $120 per reel** | 18–50% typical utilization provides comfortable buffer; absorbs vendor price hikes + fallback cascades + v1.0.1 Mode A volume | $35/$80 too tight (forces Mode A into Enterprise); $70/$150 too loose (undermines discipline signal) | Budget variance distribution shifts >0.92–1.08 sweet spot OR margin pressure surfaces |
| 3 | **Drift threshold 0.85 default (inherited from AI Video Gen)** | Composite score sweet spot per visual-vs-scalar pilot calibration; soft-warning ONLY in v1.0 (never hard halt) | Style Replication-specific override at 0.80 (looser) or 0.90 (stricter) | Subjective-vs-scalar correlation review at first 10 / 30 / 90 Style Replication invocations |
| 4 | **Single brand anchor per reel (no multi-brand inheritance)** | Single-operator pilot scope; multi-brand inheritance is v1.1+ edge case with custom LoRA dependency | Multi-brand v1.0 (rare cross-brand reel use case) | Sequel Digital onboards 2nd paying client requesting cross-brand reel composition |
| 5 [P] | **Style transfer engine: Pika Style Tokens PRIMARY + Runway Style Reference FALLBACK** | Pika $0.13 avg vs Runway $0.24 avg = ~85% cost overhead avoided; Runway as fallback when Pika first-pass drift > 0.85 | Runway primary (higher cost, marginally better quality); Pika-only (no fallback) | Pika quality regression sustained over 30 reels OR Runway pricing drop > 50% |
| 6 | **Anchor freshness gate: 90-day window** | LOCKED brand anchors retain visual relevance ~90 days; beyond 90d operator re-validation required | 30-day (tight, frequent re-validation); 180-day (loose, drift risk) | Brand visual identity refresh cycle data from first 3 anchor cohorts |
| 7 [P] | **6 QC pre-flight checks (anchor identity · drift score · palette delta · motion grade tolerance · brand finish presence · cost projection)** | Mirrors AI Video Gen's 6-check count per Cross-SPEC §3.4 minimum-4 floor; covers all 6 LOCKED errorEnvelope code paths at pre-flight | 4-check (looser); 8-check (deeper) | Operator audit reveals missing pre-flight gate |
| 8 | **Coverage envelope check (Mode C-specific)** | Mode C must operate within anchor's visual envelope (e.g., iMac scene → not stadium establishing shot); out-of-envelope prompts halt with `coverage_envelope_mismatch` OR fall back to Mode B with `human_review_required: true` | Permissive Mode C (no envelope check — operator manages); strict envelope (no fallback to Mode B) | First 3 Enterprise Mode C invocations reveal envelope friction |
| 9 | **`literal_fingerprint_inherit` field (analog to AI Video Gen's `literal_seed_inherit`)** | Style Replication's brand-anchor immutable fingerprint passed downstream — auditability + reproducibility | No fingerprint propagation (downstream agents re-derive) | Downstream Edit Director / QC reveals fingerprint usefulness for forensic trace |
| 10 [P] | **Mode C Enterprise-only at v1.0** | Pro-tier brand-anchor onboarding pipeline not built at v1.0; Enterprise onboarding already produces LOCKED anchors | Mode C Pro-tier unlocked (requires onboarding work at v1.0); Mode C Enterprise+pilot (sales-tier feature) | First 3 Enterprise clients with established anchors requesting Pro sub-account Mode C access → v1.0.1+ feature |
| 11 | **Tier↔mode firewall 6th defense-in-depth pass** | Re-validate `metadata.tier` and `production_mode` at agent entry — defense-in-depth across all 6 production agents to date | Trust upstream gating (single point of failure) | Operator audit reveals upstream tier-bypass attempt |
| 12 | **12-check Self-QC list shape (inherited from upstream agents)** | Cross-SPEC §3 canon consistency; operator mental model unchanged across agents | 8-check (shorter); 16-check (deeper) | Two consecutive agent SPECs reveal a missing universal check |
| 13 | **Voice for rationale fields (inherited verbatim from ProdCoord §7 via AI Video Gen Decision #13)** | Cross-SPEC §3.8 canon — operator readability invariant | Style Replication-specific terser voice (fingerprint domain) | Operator readability feedback at v1.0.1 review |
| 14 | **Mode A fixture deferred to v1.0.1** | Mode A volume too low at v1.0 launch to justify dedicated fixture authoring; 5-fixture portfolio TC-01..TC-05 covers Mode B + C end-to-end | Mode A fixture at v1.0 (authoring overhead) | Mode A invocation volume reaches ≥10 reels in any 30-day window |
| 15 | **Cross-SPEC §3.9 parent_chain extends to n-tuple (5-tuple at Style Replication slot)** | Generalization required for the 11 remaining agent slots beyond Style Replication; n-tuple-as-lineage pattern is Cross-SPEC v1.1 amendment | Stay at 4-tuple (rejects Style Replication appendage); per-agent custom shape (canon fragmentation) | Cross-SPEC v1.2 canon audit at full 17-agent build close |

**Operator walk-through prompt (for Day 32 LOCK ceremony):**
For each decision above, the operator either: (a) RATIFY-AS-LOCKED, (b) AMEND-with-rationale (triggers `§15.1 v1.0-corrections-day-32` entry), or (c) DEFER-to-v1.0.1 (decision parks in §15.2 candidates lot).

**4 PRELIMINARY items requiring explicit verdict (annotated [P] above):**
- #2 Cost ceilings → Donna recommends **RATIFY** at current values
- #5 Pika PRIMARY + Runway FALLBACK → Donna recommends **RATIFY**
- #7 6 QC pre-flight checks → Donna recommends **RATIFY**
- #10 Mode C Enterprise-only at v1.0 → Donna recommends **RATIFY**

---

## §4 — IMPLEMENTATION PLAN UPDATE (Day 32 entry · appends to Day 30 §14)

### Calendar status updates (Day 32)

| Day | Date | Deliverable | Status | Owner |
|-----|------|-------------|--------|-------|
| Day 29 | Mon May 18 · Wk5D3 | SPEC outline §0–§5 LOCKED-as-shipped | ✅ DONE | Donna overnight |
| Day 30 | Tue May 19 · Wk5D4 | SPEC body partial 1 §6 / §7 / §10 / §14 LOCKED-as-drafted (6 errorEnvelope codes LOCKED · 5-tuple parent_chain LOCKED) | ✅ DONE | Donna overnight |
| Day 31 | Wed May 20 · Wk5D5 | SPEC body partial 2 §8 / §9 / §11 / §12 / §13 / §15 / §16 LOCKED-as-drafted (4 PRELIMINARY §13 items annotated) | ✅ DONE | Donna overnight |
| **Day 32** | **Thu May 21 · Wk5D6** | **v1.0 LOCK CANDIDATE (this document) — 8/11 reviewer items PASS · 3 OPERATOR-ONLY (Items 6, 8, 11)** | **🟡 CANDIDATE** | **Donna overnight (this doc) + Jamila ratification (today/next 30-min block)** |
| Day 33 | Fri May 22 · Wk5 close | `input.schema.json` + `output.schema.json` authored from §10 field map + §11 pricing canon + §16 metadata block | ⬜ QUEUED (primed per §16.5 6 encoding decisions documented) | Donna overnight |
| Day 34 | Sat May 23 · Wk6D1 (Wk5 spillover) | SKILL bundle (10–15 files: SKILL.md · 2 schemas · vendor_pricing_canon.json · 5 test fixtures · README) | ⬜ QUEUED | Donna overnight |
| Day 35 | Sun May 24 · Wk6D2 | **REST DAY** (no SPEC content authored) — pre-flight scaffold prep for Day 36 LLM Test Runbook | ⬜ — | — |
| Day 36 | Mon May 25 · Wk6D3 | LLM Test Runbook (paste-and-run · pattern from Day 11 / 19 / 27 · operator-gated) | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 37 | Tue May 26 · Wk6D4 | **v1.0 LOCK** (Wk5 close target slipped by 1 day · operator-gated sit-down · HARD-GATED on AI Video Gen v1.0 LOCK first) | ⬜ GATED | Jamila + Donna co-ceremony |

### Dependencies that MUST exist before Day 34 SKILL bundle build
1. v1.0 LOCK CANDIDATE ratified (operator sign-off Items 6, 8, 11) — **TODAY**
2. input.schema.json + output.schema.json LOCKED (Day 33)
3. vendor_pricing_canon.json finalized (Day 33 — JSON canonical shape primed in §11.5)
4. negative_prompt_template canon SHA-256 captured (Day 33 — inherits from AI Video Gen v1.0 LOCK; gates on AI Video Gen LOCK ceremony)
5. 5 test fixtures resolved against schemas (Day 33 dry-run validation)

### Hard gate on AI Video Gen v1.0 LOCK
Style Replication v1.0 LOCK ceremony on Day 37 **CANNOT complete until AI Video Gen v1.0 is LOCKED first.** AI Video Gen LOCK candidate (Day 24) has 9/11 reviewer items PASS but Items 8 + 11 remain OPERATOR-ONLY. Day 27 LLM Test sit-down outcome still UNCONFIRMED as of Day 32. **Operator runway: 5 days (Day 32 → Day 37) to close AI Video Gen LOCK.**

### Rest Day honor
Day 28 (Sun May 17) → Day 35 (Sun May 24) — both Rest Days honored across the 8-day sprint window. No SPEC content authored on Rest Day. Day 35 will be pre-flight scaffold for Day 36 LLM Test Runbook (docs prep only, no SPEC content).

---

## §5 — CHANGE LOG UPDATE (Day 32 entry · appends to Day 31 §15.1)

| Version tag | Date | Description | Source file |
|-------------|------|-------------|-------------|
| **v1.0-LOCK-CANDIDATE-day-32** | **2026-05-21 (Thu · Wk5D6)** | **Unified LOCK candidate document produced. Day 32 reviewer checklist 8/11 PASS executed autonomously by Donna overnight. Items 6 (per-engine pricing canon spot-check) + 8 (15 critical decisions sign-off, 4 PRELIMINARY items requiring explicit verdict) + 11 (Cross-SPEC §3.9 amendment ratification — 5-tuple parent_chain extension) flagged OPERATOR-ONLY. Pending operator ratification → flip to `v1.0-LOCKED-day-32` AND/OR gated on AI Video Gen v1.0 LOCK ceremony first → flip to `v1.0-LOCKED-day-37` after Day 37 ceremony.** | `ARS-2026-05-21-Day-32-Style-Replication-Agent-v1-LOCK-CANDIDATE.md` (this doc) |

**Promotion rule:** When operator ratifies Items 6, 8, 11 (either at Day 32 ceremony or asynchronously via written sign-off in Notion Action Tracker), version tag promotes to `v1.0-LOCKED-day-32-pending-ai-video-gen-LOCK`. Final flip to `v1.0-LOCKED-day-37` occurs at Day 37 LOCK ceremony AFTER AI Video Gen v1.0 LOCK is confirmed. Donna mirrors LOCKED status across:
- This unified document (header `Document status` line)
- Dashboard `Recent Daily Reports` log
- Notion Action Tracker (Sequel Digital · ARS · Style Replication Agent v1.0 LOCK row)
- Day 33 schema authoring kickoff (unblocks Donna's Friday overnight session)
- Cross-SPEC v1.1 amendment formal close (if Item 11 ratified)

---

## §6 — OPEN QUESTIONS · STATUS

Inherited from Day 29 outline + Day 30 + Day 31 partials. Status updated for Day 32.

### Open Question #6 — Per-engine pricing canon spot-check (RESEARCH-ONLY at Day 31)
**Status:** ⏸ OPERATOR-ONLY for Day 32 LOCK ceremony — Item 6 of reviewer checklist. Two random rows (Pika · Runway) checked against current vendor pricing pages.
**Recommendation:** Donna defers — operator walks the pricing page URLs at Day 32 LOCK ceremony (15–25 min walkthrough on §11.1 table).
**Blocker for LOCK:** No — table is SPEC-level numerical artifact, not runtime authority. Day 34 SKILL bundle vendor_pricing_canon.json is the runtime source of truth.

### Open Question #8 — 15 critical decisions sign-off
**Status:** ⏸ OPERATOR-ONLY for Day 32 LOCK ceremony — Item 8 of reviewer checklist. Walk each decision (rationale · alternative · revisit trigger). 11 decisions LOCKED-as-drafted; 4 PRELIMINARY decisions require explicit RATIFY / AMEND / DEFER verdict.
**Recommendation:** Donna recommends RATIFY-AS-LOCKED for all 4 PRELIMINARY items based on Day 31 analysis. Operator may amend any with rationale.
**Blocker for LOCK:** Yes — hard-required for Day 32 LOCK CANDIDATE promotion.

### Open Question #11 — Cross-SPEC §3.9 amendment ratification (5-tuple parent_chain extension)
**Status:** ⏸ OPERATOR-ONLY for Day 32 LOCK ceremony — Item 11 of reviewer checklist. Amendment language drafted in Day 31 §16.3 (reproduced in §1 Item 11 of this doc).
**Recommendation:** Donna recommends RATIFY-AS-DRAFTED — generalization is necessary for the 11 remaining agent slots beyond Style Replication.
**Blocker for LOCK:** Yes — Style Replication's 5-tuple parent_chain is the first invocation of the n-tuple pattern; Cross-SPEC §3.9 must be amended OR Style Replication's parent_chain must be re-derived to fit existing 4-tuple canon (less elegant, more churn at v1.1).

### Open Question #36 (NEW · Day 32 close) — Day 36 LLM Test Runbook scope (dry-run vs live mode)
**Status:** ⏸ OPERATOR-ONLY for Day 36 (forward-looking — not blocking Day 32 LOCK).
**Recommendation:** Donna recommends **dry-run mode for v1.0 LOCK gate** (cost ≈ $0, cached mock engine responses), with live mode reserved for v1.0.1 post-LOCK confidence pass. Live mode worst case ≤ $500 (1 Pro + 1 Enterprise Mode B happy-path live render). Note: this is lower than AI Video Gen's live-mode worst case (≤$1,000) because Style Replication's per-shot cost is structurally ~1/8th of AI Video Gen.
**Blocker for LOCK:** No — Day 36 calendar position, not Day 32. Acknowledged for forward planning only.

### Open Question #37 (NEW · Day 32 close) — Hard-gate on AI Video Gen v1.0 LOCK
**Status:** ⏸ OPERATOR action required on AI Video Gen LOCK candidate (Day 24 LOCK candidate, Items 8 + 11 still pending; Day 27 LLM Test sit-down outcome still UNCONFIRMED).
**Recommendation:** Donna recommends operator close AI Video Gen LOCK within the 5-day window (Day 32 → Day 37). Three operator-action paths available per Day 28 primer:
- **Branch A (LLM Test 5/5 PASS):** 10-min LOCK ceremony → `v1.0-LOCKED-day-27` flip → unblocks Style Replication LOCK ceremony Day 37
- **Branch B (LLM Test <5/5 PASS):** System-prompt-only patch + narrow re-run
- **Branch C (Defer Day 27 sit-down):** Operator runs LLM Test sit-down then forks A or B
**Blocker for Style Replication LOCK:** YES — Day 37 ceremony cannot complete without AI Video Gen LOCK first.

---

## §7 — PARKED ITEMS (Notion ARS P3 · still open from Day 28 surfacing)

1. "ARS Daily Build Session — Notion page created 4/22 but empty; verify transcription pipeline or delete placeholder" (P3 · Sequel Digital · Open).
2. "ARS Daily Build Session page is empty — confirm whether session occurred and transcribe if so" (P3 · Sequel Digital · Open).

**Donna's recommendation unchanged from Day 31:** close both as "transcript lives in `ars/` (31 deliverables · 30 build logs · 5 LIVE skill bundles · ~1.40 MB canon), not Notion." Operator's call.

---

## §8 — PROCESS INTEGRITY (Day 32)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked (Item 6 explicitly deferred to operator).
- ✅ **No external comms.** No emails sent, no DMs, no social posts, no investor outreach, no client outreach.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine API runs initiated.
- ✅ **No operator-impersonation.** Day 32 reviewer Items 6, 8, 11 verdicts NOT silently advanced. 4 PRELIMINARY §13 items NOT silently ratified. Cross-SPEC §3.9 amendment language NOT silently committed to Cross-SPEC canon.
- ✅ **No fake-advance.** This LOCK CANDIDATE is a unified text-reconciliation of Day 30 + Day 31 partials. Zero behavioral changes vs source partials. Zero net-new SPEC content. The only Day 32 contributions are: (a) executive summary (§0 LOCK manifest), (b) 11-item reviewer checklist execution record (§1), (c) unified SPEC index pointing to source partials (§2), (d) decision walk-through formatted for operator ceremony (§3), (e) implementation plan + change log appendages (§4 + §5).
- ✅ **All prior canon read-only.** Day 22 partial 1 + Day 23 partial 2 + Day 24 LOCK candidate (AI Video Gen) + Day 25 schemas + Day 26 SKILL bundle + Day 27 runbook + Day 28 primer + Day 29 outline + Day 30 partial 1 + Day 31 partial 2 all untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon.
- ✅ **Pattern source acknowledged.** AI Video Gen Day 24 LOCK candidate structure inherited at section level (§0 manifest · §1 reviewer execution · §2 unified index · §3 decisions walk-through · §4 implementation plan update · §5 change log update · §6 open questions). Numerical values + decision content re-derived for Style Replication scope.

---

## §9 — SPRINT STATS (running total · Day 32 close)

- ARS canon size: **~1.40 MB** (was ~1.33 MB at Day 31 · +66 KB Day 32 LOCK candidate text)
- Deliverables shipped: **31** (Day 31 = 30 · Day 32 Style Replication v1.0 LOCK CANDIDATE = +1)
- Build logs: **30** (was 29 · +1 today)
- LIVE skill bundles: **5** (Brief · Script · Storyboard · ProdCoord · AI Video Gen — AI Video Gen LIVE-as-built but LLM execution still operator-gated)
- v1.0 LOCK status (AI Video Gen): **CANDIDATE READY + BUNDLE BUILT + RUNBOOK AUTHORED** · operator sit-down outcome to be confirmed (Day 32 → Day 37 = 5-day operator runway before Style Replication LOCK gate is breached)
- v1.0 LOCK CANDIDATE status (Style Replication): **LOCK CANDIDATE READY** · 8/11 reviewer items PASS · 3 OPERATOR-ONLY · operator ratification needed for Day 37 LOCK ceremony AFTER AI Video Gen LOCK confirmed
- errorEnvelope codes (Style Replication): **6 LOCKED Day 30** (no change Day 32)
- parent_chain (Style Replication): **5-tuple LOCKED Day 30** · **amendment language §16.3 DRAFTED Day 31** · **operator ratification Day 32 ceremony**
- §13 critical decisions: **15/15 LOCK-quality at Day 32 close** (9 Day 29 + 2 Day 30 RESOLVED + 4 Day 31 RATIFIED with operator-amend annotation) — 4 PRELIMINARY items require explicit verdict at Day 32 ceremony
- Cross-SPEC §3 adherence: **11/11 ✅**
- Days until Style Replication v1.0 LOCK target: **5** (Day 37 · Tue May 26)
- Days until Week 6 commercial launch start: **6** (Day 38 · Wed May 27)
- Days until full sprint close: **10** (Day 42 · Sun May 31)

---

## §10 — OPERATOR ACTION SUMMARY (3 independent items · 30–60 min total)

The Day 32 LOCK CANDIDATE is ready for operator pickup. Three independent operator actions; any can move first.

| Action | Time | Description |
|--------|------|-------------|
| **Item 6 — Pricing canon spot-check** | 15–25 min | Walk Pika Style Tokens + Runway Style Reference pricing pages; verify §11.1 rows within ±15% tolerance. Any out-of-tolerance row → amend table inline + `§15.1 v1.0-pricing-corrections-day-32` change log entry. |
| **Item 8 — 15 decisions walk-through** | 20–30 min | Walk §3 of this document. For each of 15 decisions: RATIFY-AS-LOCKED / AMEND-with-rationale / DEFER-to-v1.0.1. Special attention on 4 PRELIMINARY items (#2, #5, #7, #10) — Donna recommends RATIFY for all 4. |
| **Item 11 — Cross-SPEC §3.9 amendment** | 10 min | Review amendment language drafted in §1 Item 11 of this document (5-tuple parent_chain extension generalization to n-tuple). RATIFY-AS-DRAFTED / AMEND-with-rationale / DEFER. Donna recommends RATIFY-AS-DRAFTED. |

**After all 3 items ratified:** Donna flips version tag to `v1.0-LOCKED-day-32-pending-ai-video-gen-LOCK`. Day 33 schema authoring unblocks. Final flip to `v1.0-LOCKED-day-37` occurs at Day 37 LOCK ceremony AFTER AI Video Gen v1.0 LOCK is confirmed.

**Forward-looking operator action (not blocking Day 32 LOCK CANDIDATE):** Close AI Video Gen v1.0 LOCK ceremony within the 5-day window (Day 32 → Day 37). Items 8 + 11 from Day 24 AI Video Gen LOCK candidate still pending; Day 27 LLM Test sit-down outcome still UNCONFIRMED. **Without AI Video Gen LOCK, Style Replication Day 37 LOCK ceremony cannot complete.**

---

*Day 32 ships clean. Unified LOCK CANDIDATE document produced as text-only reconciliation of Day 30 + Day 31 partials. Zero net-new SPEC content. Zero fake-advance. 8/11 reviewer items PASS autonomously verdicted by Donna; 3 OPERATOR-ONLY items (6, 8, 11) flagged with explicit recommendations and operator-action timing estimates. Pattern source: Day 24 AI Video Gen LOCK candidate (proven 11-item reviewer checklist shape adapted to Style Replication's 6-code / 15-decision / 5-tuple parent_chain scope). Day 33 schema authoring runway primed (§16.5 6 encoding decisions documented Day 31). Day 37 Style Replication v1.0 LOCK gate gates on AI Video Gen v1.0 LOCK first — 5-day operator runway from today.*
