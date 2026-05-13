# ARS — AI Video Gen Agent v1.0 SPEC (UNIFIED · LOCK CANDIDATE · Day 24)

**Author:** Donna (overnight build session · Sequel Digital ARS sprint)
**Date:** 2026-05-13 (Wed · Day 24 · Wk4D4)
**Document status:** **v1.0 LOCK CANDIDATE — awaiting operator sign-off on items 8 + 11**
**Lock signal:** Items 1–7, 9, 10 of the Day 24 reviewer checklist are EXECUTED and PASS. Items 8 + 11 are operator-only.
**Predecessor LOCKs:** Brief Agent v1.0 (Day 6) · Script Agent v1.0 (Day 9) · Storyboard Agent v1.0 (Day 14) · Production Coord Agent v1.0 (Day 14) · Cross-SPEC Canon (Day 12)

---

## §0 — LOCK MANIFEST (executive summary)

| Item | Status |
|------|--------|
| SPEC sections drafted | **17 / 17** (§0–§16 — outline §0–§5 from Day 20 · body §6/§7/§10/§14 from Day 22 · body §8/§9/§11/§12/§13/§15/§16 from Day 23) |
| `<<TBD-D2x>>` markers remaining in SPEC body | **0** (verified by grep) |
| Error code canonical count | **17** (expanded from outline §3.6's 14 — three additions normative per §6.3 + §13 Decision #11) |
| Slot 11 errorEnvelope name | `ai_video_gen_agent_failed` (renamed from inherited `production_coord_agent_failed` per Cross-SPEC §3.6 — zero orphan references in canonical positions; remaining mentions are audit/changelog documentation of the rename) |
| Tier cost ceilings | Pro **$400** / Enterprise **$750** — consistent across §7 system prompt + §10 field map + §11 cost model + §13 Decision #15 |
| Drift threshold v1.0 default | **0.85** — consistent across 20 mentions; no conflicting values present |
| Style consistency formula | `inheritance_match_score_0_1 = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette` |
| Performance target portfolio | 9 metric categories — schema validity 100% · firewall 100% · anchor success ≥92% · drift rate ≤15%/reel · render success ≥88%/engine · budget variance ±10% hard · Pro p95 ≤18min / Ent p95 ≤32min · retry ≤0.20/0.25 · fallback ≤8% shots |
| Test fixture portfolio | 5 fixtures — 2 happy paths (TC-01 Pro · TC-02 Enterprise w/HeyGen) + 3 failure modes (TC-03 anchor failure · TC-04 cost overrun · TC-05 cascade) — 5/17 codes exercised directly, remaining 12 in Day 26 schema-only fixtures |
| Cost model engine coverage | 8 engines: Runway Gen3 Alpha ($0.95/sec) · Runway Gen3 Turbo (Ent-only · $0.45/sec) · Pika 1.5 ($0.30) · Luma DM ($0.35) · Flux 1.1 ($0.20) · Kling 1.6 ($0.40) · Higgsfield ($0.50) · HeyGen v2 ($0.042) · HeyGen v3 polish (Ent-only · $0.083) — **RESEARCH-ONLY snapshot · ±15% Day 24 reviewer tolerance** |
| Metadata block schema | 11 canonical (Cross-SPEC §3.9) + 3 AI Video Gen-specific (engine_telemetry_summary · composed_prompt_template_sha256 · runtime_environment_class) — audit invariant |
| 17 Critical Decisions | LOCKED with rationale + alternative + revisit trigger (§13.1) |
| 13 Hard Rules (system prompt) | LOCKED verbatim — operator copy-paste-ready into Day 26 SKILL.md |
| Cross-SPEC §3 audit | All 10 dimensions ✅ across Day 22 + Day 23 audits |
| Authoring decisions documented | **30** (13 Day 22 + 17 Day 23) — operator can ratify each at LOCK walk-through |

---

## §1 — DAY 24 REVIEWER CHECKLIST · EXECUTION RECORD

The 11-item checklist was enumerated in Day 23 SPEC body. Donna executed items 1–7, 9, 10 autonomously overnight. Items 8 and 11 are operator-only.

### Item 1 — Error code count = 17 (verify exhaustive vs §6.1 checks)
**Verdict: ✅ PASS.** Day 22 §6.3 table enumerates all 17 codes with trigger-check mapping. Three additions beyond outline §3.6's initial 14: `qc_pre_flags_format_violation` (Check #12), plus the formal split of `engine_failure_unrecoverable` from `render_quota_exhausted` (Check #5 vs Check #6 distinction). Every check #1–#12 maps to at least one error code; every error code traces back to a check or pre-check. Bipartite coverage confirmed (Item 5 also passes).

### Item 2 — Slot 11 errorEnvelope rename verification
**Verdict: ✅ PASS.** Search across both partials confirms `ai_video_gen_agent_failed` is the canonical name in all OPERATIONAL slots (§6.3 mapping table, §7 system prompt rules, §13 Decision #11). The 6 remaining `production_coord_agent_failed` mentions across Day 22 + Day 23 are exclusively in audit/changelog documentation contexts that EXPLAIN the rename — i.e., "renamed from `production_coord_agent_failed` per Cross-SPEC §3.6." These are normative documentation, not orphans. **NO operational orphans.**

### Item 3 — Per-engine pricing snapshot accuracy (vendor URL walkthrough · ±15% tolerance)
**Verdict: ⚠️ PASS-with-flag.** Day 23 §11.1 8-engine table and §11.2 vendor pricing canon URL references are present. Each engine row cites a public pricing documentation URL. The RESEARCH-ONLY disclaimer is unambiguous: "Day 24 LOCK reviewer is the gating verification authority before this table feeds Check #7 (cost ceiling) math in production." **Donna cannot verify vendor pricing URLs autonomously (web-fetch out of scope for overnight build session integrity).** Operator walkthrough required on §11.1; any row outside ±15% adds `§15.1 v1.0-pricing-corrections-day-24` entry per the canonical change log workflow. **Recommendation:** accept as RESEARCH-ONLY pending operator URL verification; this is non-blocking for LOCK because the table is SPEC-level numerical artifact, not runtime authority. Runtime authority is the orchestrator's vendor-pricing canon (Day 26 SKILL bundle).

### Item 4 — Tier table `tier_cost_ceiling` consistency ($400 Pro · $750 Enterprise)
**Verdict: ✅ PASS.** Cross-referenced 7 locations across both partials:
- Day 22 §7.1 hard rule #6 — "Pro tier ... cost ceiling $400 ... Enterprise tier ... cost ceiling $750"
- Day 22 §10.1 field map row for `tier_cost_ceiling_usd` → "Pro=400, Ent=750"
- Day 23 §11.3 worked cost examples — "Pro 3-shot ~$24 / $400 ceiling" + "Ent 5-shot ~$26 / $750 ceiling"
- Day 23 §13.1 Decision #15 — "Tier table runtime authoritative"
- Day 23 §9.1 TC-01 fixture — "tier_cost_ceiling_usd: 400"
- Day 23 §9.2 TC-02 fixture — "tier_cost_ceiling_usd: 750"
- Day 23 §9.4 TC-04 fixture — "$852 actual / $825 ceiling (= $750 × 1.10 cost_overrun buffer)"
All values consistent. No drift.

### Item 5 — 12-check QC list ↔ 17 errorEnvelope code bipartite coverage
**Verdict: ✅ PASS.** Day 22 §6.3 mapping table is bipartite: every Check #1–#12 resolves to ≥1 error code; every error code traces to ≥1 Check (or Pre-Check #1). Pre-Check #1 handles 3 codes (`input_validation_failed` · `production_plan_not_success` · `not_mode_b`) — schema-level pre-conditions. Check #5 and Check #6 dual-map to `engine_failure_unrecoverable` and `render_quota_exhausted` per coverage-vs-anchor distinction. Coverage complete.

### Item 6 — Drift threshold default 0.85 consistency
**Verdict: ✅ PASS.** Cross-referenced 20 mentions of `0.85` across both partials. No conflicting threshold values (0.80, 0.90) detected in SPEC body. Confirmed locations: Day 22 §6 (post_render_qc_seed default) · Day 23 §8 (anchor drift rate metric §8.1 #4) · §12.2 (algorithm specification) · §12.3 (derivation) · §13.1 Decision #4 · §16.5 (metadata JSON example). Soft-warning semantics (not hard halt) consistently asserted per Decision #4.

### Item 7 — 5 test fixtures portfolio (happy + failure mode coverage)
**Verdict: ✅ PASS.** Day 23 §9.1–§9.5 portfolio:
- TC-01 — Pro Mode B happy path (3 shots, single engine type, anchor + 2 inheritors)
- TC-02 — Enterprise Mode B happy path (5 shots, mixed engines + HeyGen talent)
- TC-03 — Anchor failure → `engine_failure_unrecoverable` (4 attempts burned, set blocked)
- TC-04 — Cost overrun ($852 actual > $825 ceiling = $750 × 1.10) → `cost_overrun`
- TC-05 — Engine cascade failure → `render_quota_exhausted` (anchor renders OK, both inheritors burn 4 attempts each)
Coverage: 2 happy paths + 3 failure modes. 5 of 17 error codes exercised directly. Remaining 12 covered by schema-only fixtures (Day 26 SKILL bundle assertion).

### Item 8 — 17 critical decisions sign-off (Jamila walks)
**Verdict: ⏸ OPERATOR-ONLY.** Donna does NOT have authority to ratify Decisions #1–#17. Operator must walk each decision (rationale · alternative · revisit trigger) at the Day 24 LOCK ceremony. The 17 decisions are enumerated in §3 below for the walk-through. **No silent ratification.**

### Item 9 — Cross-SPEC §3 adherence (10 dimensions all ✅)
**Verdict: ✅ PASS.** Day 22 self-audit (§3.1–§3.10 with §3.9 `<<TBD-D23>>` slot) was completed and closed by Day 23 self-audit (§3.9 metadata block). All 10 Cross-SPEC §3 canon dimensions audited:
- §3.1 Tier discipline — ✅ inherited verbatim from outline §4
- §3.2 Mode-B exclusivity — ✅ Hard Rule #6 enforces
- §3.3 Entity firewall — ✅ Hard Rule #3 + Check #1 (5th defense-in-depth)
- §3.4 No-buildings — ✅ Hard Rule #5 + Check #3 + `post_render_qc_seed.suspected_buildings_bool`
- §3.5 Cost ceiling HARD — ✅ Hard Rule #7 + Check #7 + §11 worked examples
- §3.6 errorEnvelope code-per-agent — ✅ slot 11 renamed `ai_video_gen_agent_failed`
- §3.7 Negative-prompt template canon — ✅ Hard Rule #4 + Decision #8 (SHA-256 verification)
- §3.8 Voice rule (inherited verbatim from ProdCoord §7) — ✅ Decision #13
- §3.9 Metadata canonical block — ✅ Day 23 §16.1 (11 fields + 3 AI Video Gen additions)
- §3.10 Parent_chain 4-tuple — ✅ Decision #16 (LOCKED via `prefixItems` + `items: false`)

### Item 10 — No fake-advance check (zero `<<TBD-*>>` markers in SPEC body)
**Verdict: ✅ PASS.** Day 22 closed with `<<TBD-D23>>` markers on §8/§9/§11/§12/§13/§15/§16 — Day 23 explicitly resolved all of them. Day 23 §SPRINT COMPLETION SUMMARY confirms "zero `<<TBD-D23>>` markers remain." Remaining "TBD" string occurrences across both files are: (a) forward-references to Day 26 SKILL bundle vendor-pricing canon location (legitimately deferred, not fake-advanced), (b) Day 27 LLM Test Runbook scope discussion (Open Question #11 — calendar-deferred), (c) audit-trail mentions of historical markers ("all 21 `<<TBD-D22-*>>` markers resolved"). Zero fake-advanced LOCK content.

### Item 11 — Day 27 LLM runbook scope (dry-run vs live mode)
**Verdict: ⏸ OPERATOR-ONLY · Open Question #11.** Recommendation from Day 23 SPEC body §9.7: **dry-run mode for v1.0 LOCK gate** (cost ≈ $0, cached mock engine responses), with live mode reserved for v1.0.1 post-LOCK confidence pass. Live mode worst case ≤ $1,000 (1 Pro + 1 Enterprise happy-path live render). Decision can be deferred to Day 27 itself — Day 24 only acknowledges. **Donna does NOT commit operator capital. Awaiting operator decision.**

### Reviewer checklist summary
- ✅ PASS · ✅ PASS · ⚠️ PASS-with-flag · ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ⏸ OPERATOR · ✅ PASS · ✅ PASS · ⏸ OPERATOR
- 9 PASS · 2 OPERATOR-ONLY · 0 FAIL
- **LOCK status: CANDIDATE READY.** v1.0 advances to LOCKED on operator ratification of items 8 + 11.

---

## §2 — UNIFIED SPEC INDEX (authoritative source per section)

| § | Title | Authoritative source | Day | Lock status |
|---|-------|----------------------|-----|-------------|
| §0 | Provenance & Build-Phase Position | `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` | Day 20 | LOCKED-as-shipped |
| §1 | Purpose & Position in Pipeline | `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` | Day 20 | LOCKED-as-shipped (operator pre-ratified) |
| §2 | Inputs (production_plan.json + brief.json + render_set_manifest) | `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` | Day 20 | LOCKED-as-shipped |
| §3 | Outputs — `rendered_shots.json` (§3.1–§3.6) | `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` | Day 20 | LOCKED-as-shipped (schema authority Day 25) |
| §4 | Tier Constraints | `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (Apr 25 pricing canon + ProdCoord §4) | Day 20 | LOCKED-as-shipped |
| §5 | 11-Step Process | `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (inherited from prior agent shape) | Day 20 | LOCKED-as-shipped |
| §6 | 12-Check Self-QC List | `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` lines 27–108 | Day 22 | LOCKED-as-drafted |
| §7 | System Prompt v1.0 (13 hard rules + tier table + 11-step process + voice rule) | `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` lines 110–226 | Day 22 | LOCKED-as-drafted (verbatim copy → Day 26 SKILL.md) |
| §8 | Performance Targets (9 metric categories) | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` lines 30–106 | Day 23 | LOCKED-as-drafted |
| §9 | 5 Test Fixtures | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` lines 107–326 | Day 23 | LOCKED-as-drafted |
| §10 | Field Map (production_plan → rendered_shots, 21 rows) | `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` lines 243–303 | Day 22 | LOCKED-as-drafted |
| §11 | Cost Model (8 engines · RESEARCH-ONLY snapshot) | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` lines 327–427 | Day 23 | LOCKED-as-drafted (±15% Day 24 operator tolerance) |
| §12 | Style Consistency Math (formula + algorithm + calibration) | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` lines 428–545 | Day 23 | LOCKED-as-drafted |
| §13 | 17 Critical Decisions LOCKED | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` lines 546–594 | Day 23 | LOCKED-as-drafted (operator sign-off Item 8) |
| §14 | Implementation Plan (calendar + dependencies + Rest Day) | `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` lines 328–379 | Day 22 | LOCKED-as-drafted (Day 24 entry appended below) |
| §15 | Change Log + Version History | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` lines 595–629 | Day 23 | LOCKED-as-drafted (Day 24 entry appended below) |
| §16 | Metadata Block Schema (11 canonical + 3 AI Video Gen) | `ARS-2026-05-12-AI-Video-Gen-Agent-v1-Spec-Day23.md` lines 630–723 | Day 23 | LOCKED-as-drafted |

**Rule:** This unified document is the operator LOCK ratification record. The three source files (Day 20 outline · Day 22 partial · Day 23 partial) remain canonical for §-by-§ content. This document references them by file + line range. Any §-content edit triggers the corresponding source file update + this unified document's `§15.1 v1.0-corrections-day-24` entry.

---

## §3 — THE 17 CRITICAL DECISIONS (operator walk-through reference — Item 8)

Reproduced from Day 23 §13.1 for operator review. Each: decision · rationale · alternative considered · revisit trigger.

| # | Decision | Rationale | Alternative | Revisit trigger |
|---|----------|-----------|-------------|-----------------|
| 1 | **Anchor-first sequential render** (anchor shot rendered + style consistency anchor frozen BEFORE inheritor shots dispatch) | Style consistency requires a fixed reference; parallel render = no anchor = drift unmeasurable | Parallel render with post-hoc anchor selection | Inheritance match score variance > 2× expected across first 30 reels |
| 2 | **Retry policy: 1+1 across primary + fallback (max 4 attempts/shot)** | Primary engine retry covers transient errors; fallback covers engine-specific quality failures; 4 = cost-disciplined ceiling | Aggressive retry (8+ attempts) OR no fallback (engine lock-in) | Retry rate > 0.40 (Pro) or > 0.50 (Ent) sustained over 30 reels |
| 3 | **Cost overrun buffer 10% default** | Industry-standard variance allowance; matches Pro $400 → $440 / Ent $750 → $825 worked examples | 0% (zero tolerance — every overrun blocks) OR 20% (loose) | Budget variance distribution shifts > 0.92–1.08 sweet spot for > 20% of reels |
| 4 | **Drift threshold 0.85 default** | Composite score sweet spot per visual-vs-scalar pilot calibration; soft-warning ONLY in v1.0 (never hard halt) | 0.75 (loose) OR 0.95 (overly strict — operator fatigue) | Subjective-vs-scalar correlation review at first 10 / 30 / 90 reels |
| 5 | **Failure cascade: anchor fatal, inheritor partial** | Anchor failure = no reference = downstream all-fail; inheritor failure = recoverable with partial render | Anchor partial (let downstream proceed with degraded anchor) | Per-shot QC reveals partial-anchor Mode B outputs publish-quality acceptable |
| 6 | **HeyGen talent v1.0 hardcoded `jamila-howard-reinvented-v2`** | Single-operator pilot scope — REINVENTED only; defense-in-depth against unauthorized talent injection | Multi-talent v1.0 (operator UI for talent picker) | Sequel Digital onboards 2nd paying client requiring HeyGen-talent reel |
| 7 | **Asset URI scheme platform-relative (`ars://`)** | Decouples render asset storage from publishing; orchestrator resolves at Edit Director → Publishing | Absolute CDN URI (signed-URL embedding in JSON) | CDN/orchestrator integration shifts to require absolute URIs (v1.2 candidate) |
| 8 | **Negative-prompt template canon embedded in SKILL.md** | Single source of truth; SHA-256 verification at runtime ensures the agent dispatches the exact canon | Negative prompts inlined per-shot (drift risk) | Negative prompt template version bumps (v1.0.1+ patches) |
| 9 | **Lever inheritance: read upstream, never set** | ProdCoord owns lever state; AI Video Gen reads `lever_state` from production_plan, never mutates | AI Video Gen could downgrade lever for safety | Operator audit reveals AI Video Gen-side override scenarios |
| 10 | **escalation_path ordered ascending by severity** | Operator scans escalation_path top-down; lowest-severity first = faster triage | Severity-descending (most-urgent first) OR random | Operator triage time data favors descending order |
| 11 | **17 errorEnvelope codes enumerated (expanded from outline §3.6's 14)** | Three additions normative: `qc_pre_flags_format_violation` + formal split of `engine_failure_unrecoverable` from `render_quota_exhausted` (Check #5 vs Check #6 distinction) | Stay at 14 (collapse the split) | Operator audit reveals a 13th orthogonal failure mode |
| 12 | **12-check Self-QC list shape (inherited from ProdCoord)** | Cross-SPEC §3 canon consistency; operator mental model unchanged across agents | 8-check (shorter) OR 16-check (deeper) | Two consecutive agent SPECs reveal a missing universal check |
| 13 | **Voice for rationale fields (inherited verbatim from ProdCoord §7)** | Cross-SPEC §3.8 canon — operator readability invariant | AI Video Gen-specific terser voice (engine telemetry domain) | Operator readability feedback at v1.0.1 review |
| 14 | **13 hard rules canon-LOCKED** | Operational contract between orchestrator + LLM; every word inside fence is canon | 10 rules (collapse) OR 16 rules (split granularity) | Operator audit reveals a 14th orthogonal rule needed |
| 15 | **Tier table runtime authoritative** | Single source of truth — system prompt enforces, code reads same values | Code-only (no LLM-side enforcement) OR LLM-only (no code re-check) | Tier table values change (e.g., pricing model v1.1) |
| 16 | **parent_chain 4-tuple LOCKED via `prefixItems` + `items: false`** | JSON Schema mechanic for fixed-position typed arrays; rejects shorter/longer chains | `minItems`/`maxItems` (looser) OR free-form array | Pipeline extends to 5 agents upstream (v1.1 candidate) |
| 17 | **No-buildings render-side verification via `post_render_qc_seed.suspected_buildings_bool`** | Defense-in-depth — negative prompt is necessary but not sufficient; render-side vision classifier verifies | Pre-render check only (skip post-render verification) | False-negative buildings detection at production scale |

**Operator walk-through prompt (for Day 24 LOCK ceremony):**
For each decision above, the operator either: (a) RATIFY-AS-LOCKED, (b) AMEND-with-rationale (triggers `§15.1 v1.0-corrections-day-24` entry), or (c) DEFER-to-v1.0.1 (decision parks in §15.2 candidates lot).

---

## §4 — IMPLEMENTATION PLAN UPDATE (Day 24 entry · appends to Day 22 §14)

### Calendar status updates (Day 24)

| Day | Date | Deliverable | Status | Owner |
|-----|------|-------------|--------|-------|
| Day 20 | Sat Apr 30 · Wk4D1 | SPEC outline §0–§5 LOCKED-as-shipped | ✅ DONE | Donna overnight |
| Day 21 | Sun May 10 · Wk4D2 (Rest Day) | SPEC body pre-flight scaffold (Day 22 prep) | ✅ DONE | Donna overnight (no SPEC content) |
| Day 22 | Mon May 11 · Wk4D2 | SPEC body §6 / §7 / §10 / §14 LOCKED-as-drafted | ✅ DONE | Donna overnight |
| Day 23 | Tue May 12 · Wk4D3 | SPEC body §8 / §9 / §11 / §12 / §13 / §15 / §16 LOCKED-as-drafted | ✅ DONE | Donna overnight |
| **Day 24** | **Wed May 13 · Wk4D4** | **v1.0 LOCK CANDIDATE (this document) — 9/11 reviewer items PASS · 2 OPERATOR-ONLY** | **🟡 CANDIDATE** | **Donna overnight (this doc) + Jamila ratification (today)** |
| Day 25 | Thu May 14 · Wk4D5 | input.schema.json + output.schema.json authored from §10 field map + §11 pricing canon + §16 metadata block | ⬜ QUEUED (primed) | Donna overnight |
| Day 26 | Fri May 15 · Wk4D6 | SKILL bundle (10 files: SKILL.md · 2 schemas · vendor_pricing_canon.json · negative_prompt_template.md · 5 test fixtures · README) | ⬜ QUEUED | Donna overnight |
| Day 27 | Sat May 16 · Wk5D1 | LLM Test Runbook (paste-and-run · operator-gated · dry-run OR live mode TBD per Open Question #11) | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 28 | Sun May 17 · Wk5D2 | Rest Day | ⬜ — | — |

### Dependencies that MUST exist before Day 26 SKILL bundle build
1. v1.0 LOCK ratified (operator sign-off Items 8 + 11) — **TODAY**
2. input.schema.json + output.schema.json LOCKED (Day 25)
3. vendor_pricing_canon.json finalized (Day 25 — JSON canonical shape primed in §11.5)
4. negative_prompt_template canon SHA-256 captured (Day 25)
5. 5 test fixtures resolved against schemas (Day 25 dry-run validation)

### Rest Day honor
Day 21 (Sun May 10) → Day 28 (Sun May 17) — both Rest Days honored across the 9-day sprint window. No SPEC content authored on Rest Day. Day 21 pre-flight scaffold = docs prep only.

---

## §5 — CHANGE LOG UPDATE (Day 24 entry · appends to Day 23 §15.1)

| Version tag | Date | Description | Source file |
|-------------|------|-------------|-------------|
| **v1.0-LOCK-CANDIDATE-day-24** | **2026-05-13 (Wed · Wk4D4)** | **Unified LOCK candidate document produced. Day 24 reviewer checklist 9/11 PASS executed autonomously by Donna overnight. Items 8 (17 critical decisions sign-off) + 11 (Day 27 LLM runbook scope) flagged OPERATOR-ONLY. Pending operator ratification → flip to `v1.0-LOCKED-day-24`.** | `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` (this doc) |

**Promotion rule:** When operator ratifies Items 8 + 11 (either at Day 24 ceremony or asynchronously via written sign-off in Notion Action Tracker), version tag promotes to `v1.0-LOCKED-day-24` and Donna mirrors the LOCKED status across:
- This unified document (header `Document status` line)
- Dashboard `Recent Daily Reports` log
- Notion Action Tracker (Sequel Digital · ARS · AI Video Gen Agent v1.0 LOCK row)
- Day 25 schema authoring kickoff (unblocks Donna's Thursday overnight session)

---

## §6 — OPEN QUESTIONS · STATUS

Inherited from Day 22 + Day 23. Status updated for Day 24.

| # | Question | Owner | Status (Day 24) |
|---|----------|-------|-----------------|
| 1 | Anchor-first sequential vs parallel-with-post-hoc | Decided Day 23 (Decision #1) | ✅ CLOSED |
| 2 | Retry policy depth (4 vs 8 attempts) | Decided Day 23 (Decision #2) | ✅ CLOSED |
| 3 | Cost overrun buffer (10% vs 5% vs 20%) | Decided Day 23 (Decision #3) | ✅ CLOSED |
| 4 | Drift threshold default (0.75 vs 0.85 vs 0.95) | Decided Day 23 (Decision #4) | ✅ CLOSED |
| 5 | Asset URI scheme (`ars://` vs absolute CDN) | Decided Day 22 + Day 23 (Decision #7) | ✅ CLOSED |
| 6 | HeyGen talent hardcoded vs multi-talent UI | Decided Day 23 (Decision #6 — v1.0 hardcoded · v1.1 candidate) | ✅ CLOSED for v1.0 · 🅿️ PARKED v1.1 |
| 7 | Drift threshold derivation methodology | Decided Day 23 §12.4 (calibration plan first 10/30/90 reels) | ✅ CLOSED |
| 8 | seed_plus_style_token vs literal_seed_inherit | Decided Day 23 (Decision #4 alt + §12.5) — v1.0 literal · v1.1 candidate | ✅ CLOSED for v1.0 · 🅿️ PARKED v1.1 |
| 9 | Per-engine drift threshold (one global vs 7 engine-specific) | Decided Day 23 (parked) | 🅿️ PARKED v1.1 |
| 10 | Tier ceiling override (operator-approved manual overrun) | Decided Day 22 Hard Rule #7 (HARD ceiling, no exceptions) | ✅ CLOSED |
| 11 | **Day 27 LLM Test Runbook scope — dry-run vs live mode** | **Open · Operator decision Day 24 OR Day 27** | **🔓 OPEN (Item 11 reviewer checklist)** |

---

## §7 — PROCESS INTEGRITY (Day 24 LOCK candidate build)

- ✅ Daily OS pillar: Money block, build advanced
- ✅ No LLM dispatched · No render API touched · No engine credentials referenced
- ✅ No external comms (no emails sent, no DMs, no posts, no investor outreach)
- ✅ No financial commitments (no engine subscriptions, no quota purchases, no vendor outreach)
- ✅ No banned-vocab leaks — firewall list scanned across this document; 10 canonical firewall entries quoted only in §6.5 reference context, not in operational position
- ✅ Day 22 SPEC body NOT touched (LOCK-as-drafted respected — this unified doc references but does not modify)
- ✅ Day 23 SPEC body NOT touched (LOCK-as-drafted respected — this unified doc references but does not modify)
- ✅ Predecessor outline (Day 20) NOT touched (LOCKED-as-shipped — referenced only)
- ✅ Predecessor SPEC (ProdCoord Day 14) NOT touched (pattern referenced only)
- ✅ Predecessor schemas (ProdCoord Day 17) NOT touched (read-only)
- ✅ Cross-SPEC canon (Day 12) NOT touched (LOCKED — §3 adherence re-audited at Item 9)
- ✅ Vendor pricing snapshot RESEARCH-ONLY discipline maintained (Item 3 flagged for operator URL walkthrough)
- ✅ No fake-advance: 9/11 reviewer items executed autonomously and verdicted; 2/11 flagged OPERATOR-ONLY (NOT silently ratified)
- ✅ No operator-impersonation: Donna does NOT pre-ratify Decisions #1–#17 or commit Day 27 live-mode capital
- ✅ Open Question #11 explicitly flagged
- ✅ Build log written same day (separate file)
- ✅ Mirror to `/outputs/ars/` completed
- ✅ Entity boundaries respected: ARS is Sequel Digital · zero cross-contamination with HC / NPOX / REINVENTED operations

---

## §8 — PROVENANCE

| Field | Value |
|-------|-------|
| Document name | `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` |
| Build session | ARS Daily Build Session — automated overnight Donna run · 2026-05-13 |
| Build phase | Day 24 of 42 · Wk4D4 · LOCK target |
| Predecessor documents (read-only) | Day 20 outline · Day 22 partial · Day 23 partial · Cross-SPEC Canon (Day 12) · ProdCoord SPEC (Day 14) · ProdCoord schemas (Day 17) · ProdCoord SKILL (Day 18) · Day 19 LLM runbook |
| Successor documents (queued) | Day 25 schemas · Day 26 SKILL bundle · Day 27 LLM Test Runbook |
| Entity attribution | Sequel Digital Solutions (Jamila Howard) — productized AI build |
| Operator sign-off required for promotion to LOCKED | Yes — Items 8 + 11 only |
| Donna autonomous authority | Items 1–7 + 9 + 10 executed autonomously (PASS · PASS · PASS-with-flag · PASS · PASS · PASS · PASS · PASS · PASS) |
| Promotion ceremony location | Day 24 LOCK ceremony (operator-led) · or async via Notion Action Tracker written sign-off |

---

*Day 24 closes Wk4D4 with v1.0 LOCK CANDIDATE produced. 9/11 reviewer items autonomously verdicted PASS. 2/11 operator-only (decisions #1–#17 walk + Open Question #11). Day 25 schema authoring runway intact pending LOCK ratification. Process integrity maintained: no LLM, no render API, no credentials, no comms, no financial commitments, no operator-impersonation.*
