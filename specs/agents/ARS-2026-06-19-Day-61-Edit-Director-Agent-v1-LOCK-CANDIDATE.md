# ARS — Edit Director Agent v1.0 SPEC (UNIFIED · LOCK CANDIDATE · Day 61)

**Author:** Donna (overnight build session · Sequel Digital ARS sprint)
**Date:** 2026-06-19 (Fri · Day 61 · Wk9 · post-launch hardening window)
**Document status:** **v1.0 LOCK CANDIDATE — awaiting operator sign-off on items 6, 8, 11 + the FOUR predecessor LOCKs (hard gate)**
**Lock signal:** Items 1–5, 7, 9, 10 of the Day 61 reviewer checklist are EXECUTED and PASS. Items 6, 8, 11 are operator-only.
**Predecessor LOCKs:** Brief Agent v1.0 (Day 6) · Script Agent v1.0 (Day 9) · Storyboard Agent v1.0 (Day 14) · Production Coord Agent v1.0 (Day 14) · Cross-SPEC Canon (Day 12) · **AI Video Gen v1.0 LOCK CANDIDATE (Day 24 — operator-gated; STILL PENDING) · Style Replication v1.0 LOCK CANDIDATE (Day 32 — operator-gated; STILL PENDING) · QC Pre-flight v1.0 LOCK CANDIDATE (Day 44 — operator-gated; STILL PENDING) · Ingest v1.0 LOCK CANDIDATE (Day 53 — operator-gated; STILL PENDING)**
**Hard gate on predecessor LOCKs:** Edit Director's v1.0 LOCK ceremony CANNOT complete until **all four** pending predecessors LOCK first — AI Video Gen + Style Replication (the producing agents) + QC Pre-flight + **Ingest in particular (Edit Director's DIRECT dependency: the `successAssetManifest`/`pass` precondition gate Edit Director reads, and the 7-tuple parent_chain the 8-tuple extends)**. This LOCK CANDIDATE is authored on LOCK-stable **text artifacts** (the SPEC sections as drafted Days 58–60); it uses **zero production output** from any predecessor and **zero render of any media**. Forward-design under the same posture as the Day 58 outline + both body partials.
**Position note:** Agent #9 of 17 — the **first creative-authoring agent** in the post tail (it MAKES cut/pacing/caption decisions, it does not validate), the **9th defense-in-depth firewall** pass (the AUTHORED-text surface — the first agent to firewall copy it writes itself), and the **first contractually mode-blind agent** (the live, machine-checkable proof that Ingest's mode-convergence seam holds end-to-end). Its v1.0 LOCK lands inside the post-launch hardening window and does **NOT** gate the commercial launch (which shipped on the six built production agents through the QC Pre-flight gate). The Agent-#9-slot selection (Donna, Day 58 — surfaced, not hidden) remains operator-confirmable at the Ingest LOCK-ceremony close.

---

## §0 — LOCK MANIFEST (executive summary)

| Item | Status |
|------|--------|
| SPEC sections drafted | **17 / 17** (§0–§16 — outline §0–§5 Day 58 · body §6/§7/§10/§14 Day 59 · body §8/§9/§11/§12/§13/§15/§16 Day 60) |
| `<<TBD-*>>` markers remaining in the ASSEMBLED SPEC | **0 unresolved** (the §6–§16 outline preview stubs were authored in full across the Day 59 + Day 60 partials; superseded forward-references, not open items. See Item 10.) |
| SPEC body completeness | **§6–§16 COMPLETE** (Day 59 + Day 60 partials fully cover the body; this LOCK CANDIDATE is a pure text-only reconciliation, zero net-new SPEC content) |
| Error code canonical count | **9 LOCKED + slot-11 catch-all** (Day 59 §6.3 — `upstream_ingest_not_passed` · `upstream_not_success` · `incomplete_shot_coverage` · `beat_map_unmappable` · `cut_order_incomplete` · `duration_envelope_breach` · `brand_edit_rule_conflict` · `caption_spec_violation` · `edit_plan_firewall_breach` + `plan_lineage_failure` (forensic halt) + `edit_director_agent_failed` slot-11). Settled at 9 within the outline's 7–9 target |
| Notable namespace decision | `duration_envelope_breach` kept **STANDALONE** (NOT folded) — the deliberate OPPOSITE of Ingest's fold-into-`asset_spec_violation`. At the *authoring* layer an out-of-band duration is a creative-trim outcome with a distinct recovery path (re-trim the cut, not re-spec an asset); folding would destroy the routing signal (D7 / §6.3 cardinality rationale) |
| Slot-11 errorEnvelope name | `edit_director_agent_failed` (Cross-SPEC §3.6 conformant — agent_id `edit-director-agent` → snake_case; one canonical fallback per agent slot) |
| Self-QC check count | **11** (Day 59 §6.1 — entry-validation #1–2 · six authoring adjudications #3–8 · forensic #9 · plan-construction integrity #10–11) bipartite-covering the 9 codes + slot-11 |
| Verdict model | **plan_ready / fail / revise — the FIRST 3-verdict fleet agent with a success-side third outcome.** `revise` is a `successEditPlan`-shaped payload (NOT an errorEnvelope) carrying a `revise_rationale`, held for Lever-3. It is the QC-`hold` analog, transplanted to the one place Edit Director's domain is genuinely subjective: soft brand-rule creative tension. Everything else is binary. (Deliberate divergence from Ingest's pass/fail/reshoot, documented Day 59 §6.4 + Day 60 §12.3.) |
| Verdict math | **Deterministic ∧-of-11-gates on the HARD rules · ZERO tunable thresholds** (Day 60 §12) — one conjunct per hard term + exactly ONE isolated judgment slot (`revise`, reachable ONLY when all hard rules pass ∧ a soft-rule tension exists; never auto-resolves). Halts adjudicate before fails; first-failing-check-in-tier-order names the headline code with no short-circuit nulls. Properties: deterministic-on-hard-rules / monotone / zero-false-plan-ready-by-construction / one-judgment-slot-routed-to-human / auditable-recomputable |
| Cost authority | **NONE — deliberate decline** (Hard Rule #10). Edit Director does NOT re-litigate the cumulative cost ledger (QC Pre-flight's jurisdiction) or re-validate assets (Ingest's jurisdiction). The tier ceilings are upstream facts restated for traceability only |
| Self per-reel cost | **≈ $0.00** ($0.00 engine + $0.00 render structurally guaranteed; `render_dispatched: const false`; LLM reasoning ≈ $0.03–0.10 inside the latency envelope). Ties Ingest / QC Pre-flight for lowest-cost agent in the 17-agent fleet |
| Performance target portfolio | **9 metric categories** (Day 60 §8) — schema validity 100% · brand-edit-rule catch 100% (a fade/wipe/zoom/all-caps-LT/sales-CTA/missing-end-card must NEVER survive) · authored-text firewall catch 100% (9th pass) · duration-in-band 100% · **false-plan-ready 0%** (the defining target) · **false-fail/over-revise ≤8%** (looser than Ingest's ≤5% — deliberate: the one subjective `revise` surface makes some over-flagging correct conservatism, not error) · p50 latency 30s / p95 90s · $0 engine+render · self-QC first-pass yield ≥90% |
| Test fixture portfolio | **5 fixtures** (Day 60 §9) — TC-01 Mode-A→manifest Pro PASS (full plan) · TC-02 Mode-C Enterprise PASS (**the TC-01/TC-02 pair = the mode-blind convergence proof**: byte-shape-identical authoring path despite different origin) · TC-03 `incomplete_shot_coverage` → fail + route to Ingest · TC-04 `brand_edit_rule_conflict` (a beat that only resolves with a fade → hard FAIL, NOT revise) · TC-05 `edit_plan_firewall_breach` (banned token authored into a lower-third — **the 9th-pass self-authored existence proof**). 5 of 9 codes behavioral; the `revise` + slot-11 exercised via the runbook adversarial case; remaining deterministic halts schema-only (§9 fixture-economy rationale) |
| Cost model engine coverage | **ZERO generative engines + ZERO media render** (by design — Hard Rule #2, `render_dispatched: const false`). No external vendor-pricing URLs to walk AND no ceilings owned — Item 6 is among the lightest operator spot-checks in fleet LOCK history (ties Ingest) |
| Metadata block schema | **Cross-SPEC §3.9 canonical + 5 Edit-Director additions** (`parent_chain` 8-tuple · `edit_plan_class` · `plan_evidence_hash` · `render_dispatched const false` · `runtime_environment_class`) + the **`mode_blind_confirm` companion block** (the §16 structural difference — `production_mode` carried for audit lineage but attested never-READ). `human_review_required: const true` schema-enforced (recommend-don't-approve) |
| parent_chain | **8-tuple DRAFTED Day 59/60** (inherits Ingest's 7-tuple lineage + appends own `edit_plan_id`, UUIDv7) — **TRIPLY-DEFERRED: gated on (a) operator ratification of the Cross-SPEC §3.9 n-tuple amendment, (b) the Ingest 7-tuple LOCK, AND (c) the QC Pre-flight 6-tuple LOCK behind it.** Schema holds additively (`minItems: 5`, `prefixItems` 0–7, `maxItems: 8`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. The one item Donna will NOT auto-advance |
| 15 Critical Decisions | **15/15 §13 coverage** — 11 LOCKED-as-drafted (D1–D5, D9–D13 Day 58 + D14 Day 60) + 2 RESOLVED Day 59 inside pre-approved target ranges → LOCKED-as-drafted (D7 code count = 9 / D8 self-QC count = 11) + **D6 (8-tuple) TRIPLY-DEFERRED + D15 (Editor handoff → Notion holding store) `[PRELIMINARY · operator amend]`** |
| 12 Hard Rules (system prompt) | LOCKED verbatim Day 59 §7.1 — operator copy-paste-ready into the SKILL.md. Defining rules: #2 no-render with the forged-provenance framing · #6 mode-blind-by-construction (the convergence-payoff rule no prior agent could carry) · #8 direct-don't-re-author · #10 no cost re-litigation · #12 "RECOMMEND, do not APPROVE" |
| Blueprint §4.9 edit_plan shape | Inlined VERBATIM into the §7 system prompt — the LLM is the runtime source of truth for the `edit_plan` contract, not a side document (structural analog of Ingest inlining §4.8 + QC Pre-flight inlining the 11-point gate) |
| Field map | **27 rows** (Day 59 §10 — 10 lineage/identity + 7 manifest-passthrough/intent-transform + 3 authored-plan + per-check evidence + plan aggregate) + reserved `variant_plans[]` (D14 v1.1) + no-touch read-only references |
| Cross-SPEC §3 audit | **11/11 dimensions ✅** at LOCK-grade (Item 9 — full audit executed this document) |
| Authoring decisions documented | All §13 walk decisions + the Day 60 key authoring decisions + the Day 58 agent-selection note — operator can ratify each at the LOCK walk-through |

---

## §1 — DAY 61 REVIEWER CHECKLIST · EXECUTION RECORD

The 11-item checklist mirrors the Day 24 AI Video Gen / Day 32 Style Replication / Day 44 QC Pre-flight / Day 53 Ingest LOCK candidate pattern (proven shape, **5th reuse**). Donna executed items 1–5, 7, 9, 10 autonomously overnight. Items 6, 8, 11 are operator-only.

### Item 1 — Error code count = 9 + slot-11 (verify exhaustive vs §6 11-check Self-QC list)
**Verdict: ✅ PASS.** Day 59 §6.3 mapping table enumerates all 9 codes + slot-11 catch-all with trigger-check mapping. The namespace settled at 9 within the outline §3.4 7–9 target. The defining cardinality call: `duration_envelope_breach` is kept **STANDALONE** — the deliberate opposite of Ingest's fold of the same code into `asset_spec_violation`. At the asset layer an out-of-band duration is a declared-spec mismatch (same route-back as a spec violation → fold). At the *authoring* layer it is a creative-trim outcome with a distinct recovery path (re-trim the cut, not re-spec/re-gen an asset), so folding would merge defects with different recoveries and destroy the routing signal. Edit Director's defect surface decomposes into precondition (×2), coverage/mappability (×2), cut completeness, duration, brand-rule, caption, and firewall → 9 is the floor that preserves precise route-back attribution. Bipartite coverage confirmed (Item 5 also passes).

### Item 2 — Slot-11 errorEnvelope name verification
**Verdict: ✅ PASS.** `edit_director_agent_failed` is the canonical slot-11 name in all OPERATIONAL positions (§6.1 Checks #10/#11, §6.3 mapping table, §12.2 routing). Naming derives correctly per Cross-SPEC §3.6: agent_id `edit-director-agent` → snake_case → `edit_director_agent_failed`. No legacy fallback names (`ingest_agent_failed`, `preflight_qc_agent_failed`, etc.) appear in the Edit Director source files — no orphan references. Cross-SPEC §3.6 canon fully respected.

### Item 3 — Cost model accuracy (zero-engine + zero-render · no vendor surface · no ceiling authority)
**Verdict: ✅ PASS · ties Ingest for the structurally simplest Item 3 in fleet history.** Day 60 §11 establishes Edit Director as a $0 agent with no external vendor-pricing surface (no engine), no media render (`render_dispatched: const false`), and no ceiling ownership (Hard Rule #10 declines the cost-ledger authority QC Pre-flight holds). The complete cost model is: $0.00 engine (structurally banned) + $0.00 render (const false) + ≈$0.03–0.10 LLM reasoning + $0.00 native compute. Total `cost_incurred_usd` ≈ $0.00 reported to 2dp per Cross-SPEC §3.9. The §11 directed-coherence value model declines dollar-ROI quantification (no live defect corpus exists pre-orchestrator; inventing one would be fake precision — formalization parked to v1.1). **No pricing URL walk is required for this agent.**

### Item 4 — Tier-table + cost-decline consistency (universal access + tier-sensitive richness · no re-litigation)
**Verdict: ✅ PASS.** Cross-referenced across Day 58 + Day 59 + Day 60:
- Day 58 §1 + §4 universal-access / tier-sensitive-richness tables — all 4 tiers traverse Edit Director at ~$0.00; richness scales (≤8 vs ≤12 cut beats; b-roll ceilings; 1/1/2/3 swells; 3/3/4/5 variants); brand-rule compliance does NOT scale.
- Day 59 §7.1 universal-access table (runtime authoritative) — "Cost ceilings are enforced UPSTREAM at QC Pre-flight — you carry none."
- Day 59 §7.4 cost posture — ceilings restated for traceability only, NOT re-litigated.
- Day 60 §8 targets-NOT-carried list — no cost-ceiling adherence metric (QC Pre-flight's authority).
All values and decline-statements consistent. No drift. The richness ladder is inherited verbatim from the Script Agent Day 9 tier table so the edit honors the same envelope the script was written into. **No operator-amend flag** — the ceilings are upstream inheritances restated verbatim; the universal-access posture is D2 (LOCKED-as-drafted, walked at Item 8).

### Item 5 — Self-QC list ↔ 9 errorEnvelope codes + slot-11 bipartite coverage
**Verdict: ✅ PASS.** Day 59 §6.3 mapping table is bipartite: every one of the 11 self-QC checks resolves to a code (or the shared slot-11); every code traces to ≥1 check. Check #1 → `upstream_ingest_not_passed`; Check #2 → `upstream_not_success`; Check #3 → `incomplete_shot_coverage` (coverage part) + `beat_map_unmappable` (mappability part — the one check mapping to two codes); Check #4 → `edit_plan_firewall_breach`; Check #5 → `cut_order_incomplete`; Check #6 → `duration_envelope_breach`; Check #7 → `brand_edit_rule_conflict` (hard branch) + `revise` (soft branch — the judgment slot, NOT a code); Check #8 → `caption_spec_violation`; Check #9 → `plan_lineage_failure`; Checks #10 + #11 → `edit_director_agent_failed` (slot-11). Cardinality is unbalanced at slot-11 (2 plan-construction checks share it) and at Checks #3/#7 (two outcomes each) but coverage is total. The §12.1 ∧-composition maps 1:1 to the hard terms of Checks #1–#11, and the 11-step §7 loop maps 1:1 to the checks + codes per §7.2 — the audit invariant holds across all three surfaces (loop ↔ checks ↔ codes).

### Item 6 — Cost model / pricing spot-check
**Verdict: ⏸ OPERATOR-ONLY · ties Ingest for the lightest in fleet LOCK history (no vendor URLs, no ceilings owned, no native compute, no render).** There is **nothing to confirm numerically** — the agent owns no ceiling, walks no pricing page, dispatches no render, and budgets no native compute. The only operator confirmation needed is a one-line ratification that (a) the $0-engine/$0-render posture (Hard Rule #2, `render_dispatched: const false`) and (b) the no-cost-re-litigation decline (Hard Rule #10) are the intended v1.0 economics. **Recommendation: RATIFY as-is (≈1 min).** Any future change to the QC Pre-flight ceilings auto-propagates — Edit Director restates, never owns. No silent ratification — surfaced for operator confirmation only.

### Item 7 — 5 test fixtures portfolio (happy + failure-mode coverage)
**Verdict: ✅ PASS.** Day 60 §9 portfolio:
- TC-01 — Mode-A-origin → manifest, Pro clean PASS (full plan: cut_order, pacing, captions, lower-thirds, music+swell map, end-card, structure_check, brand_edit_check, 9th-pass firewall census, 8-tuple additive extension, evidence hash, mode_blind_confirm).
- TC-02 — Mode-C-origin Enterprise clean PASS (**byte-shape-identical authoring path to TC-01 despite different origin — this pair IS the mode-blind convergence proof** no other test provides; the payoff Ingest's mode-convergence seam unlocked).
- TC-03 — `incomplete_shot_coverage` (coverage hole → `fail` + `route_back_to: "ingest-agent"`; coverage_remap math internally consistent — no phantom coverage).
- TC-04 — `brand_edit_rule_conflict` (a beat that resolves only with a fade → hard `fail`, **NOT** `revise`; proves a fade can never survive to `plan_ready` — the hard/soft rule split is exercised on the hard side).
- TC-05 — `edit_plan_firewall_breach` (a banned-entity token authored into a lower-third Edit Director itself WROTE → forensic detail naming the AUTHORED field — **the 9th-pass self-authored existence proof**: a surface no prior pass owned; content otherwise clean).

Coverage: 2 happy paths (spanning the convergence proof) + 3 failure modes (coverage/route + hard-brand-rule + the new authored-text firewall). 5 of 9 codes exercised behaviorally; the `revise` verdict + slot-11 are exercised via the runbook adversarial case (Day-65 runbook position); remaining deterministic single-assertion halts (`upstream_ingest_not_passed`, `upstream_not_success`, `cut_order_incomplete`, `duration_envelope_breach`, `caption_spec_violation`, `plan_lineage_failure`) covered schema-only per the §9 fixture-economy rationale — same economy Ingest ratified Day 53. Fixtures bind to `skills/edit-director-agent/tests/` on the SKILL-bundle day.

### Item 8 — 15 critical decisions sign-off (Jamila walks)
**Verdict: ⏸ OPERATOR-ONLY.** Donna does NOT have authority to ratify Decisions D1–D15. Operator walks each (rationale · alternative · revisit trigger) at the LOCK ceremony. The 15 decisions are enumerated in §3 below.

**Special attention required on 1 `[PRELIMINARY]` item + 1 TRIPLY-DEFERRED:**
- D15 — Editor handoff target (drafted default: **Notion Edit Plan block holding store** until Agent #10 / Editor LOCKs; `handoff_targets` keeps the LOGICAL target `editor-agent`) — Donna recommends **RATIFY**. Directly tied to Ingest Day 53 Item 8 (D15-of-Ingest = the Edit-Director handoff target — now the SAME decision viewed from both ends).
- D6 — 8-tuple parent_chain — **TRIPLY-DEFERRED** on the Cross-SPEC §3.9 amendment (Item 11) AND the Ingest 7-tuple LOCK AND the QC Pre-flight 6-tuple LOCK behind it; Donna will NOT auto-advance the 8-tuple. Held additively (`minItems: 5`) until ALL THREE gates close.

**No silent ratification.** Operator either RATIFY-AS-LOCKED for each, AMEND-with-rationale (triggers a `§15.1 v1.0-corrections-day-61` entry), or DEFER-to-v1.0.1.

### Item 9 — Cross-SPEC §3 adherence (11 dimensions all ✅ · LOCK-grade audit)
**Verdict: ✅ PASS.** Day 58 + Day 59 + Day 60 self-audits combine, re-verified at LOCK-grade this document:
- §3.1 Naming canon — ✅ `edit-director-agent` (kebab-case fleet pattern, matches Blueprint §4.9 handoff target); IDs UUIDv7 per canon
- §3.2 Hash invariant — ✅ `plan_evidence_hash` SHA-256 over the `edit_plan` + `brand_edit_check` block (`^[a-f0-9]{64}$`), tamper-evident plan
- §3.3 errorEnvelope shape — ✅ 9 codes + slot-11 LOCKED Day 59, exercised in Day 60 §9 fixtures; adds `verdict` + `route_back_to` per fleet precedent; `revise` is a success-branch verdict, not an errorEnvelope code
- §3.4 `qc_pre_flags` minItems-4 floor — ✅ upstream surface consumed read-only; Edit Director emits its own ≥4 snake_case predicates (Check #11)
- §3.5 Mode matrix — ✅ mode-BLIND by construction; §4 mode columns are identical (the first fleet agent for which that is true) + the `mode_blind_confirm.production_mode_read: false` self-attestation
- §3.6 Slot-11 naming canon — ✅ `edit_director_agent_failed` canonical (Item 2)
- §3.7 `qc_pre_flags` format regex — ✅ `^[a-z][a-z0-9_]{0,63}$` enforced via Check #11
- §3.8 Tier↔mode firewall 9th defense-in-depth pass — ✅ Check #4 over AUTHORED text (the new surface) + Hard Rule #5 + §4 universal-access/tier-richness table
- §3.9 Metadata block — ✅ canonical inherit + extends to 8-tuple **held additively, TRIPLY-DEFERRED** · amendment ratification staged at Item 11 · `mode_blind_confirm` companion block added
- §3.10 Cost ceiling authority — ✅ explicitly DECLINED (Hard Rule #10) — no double-enforcement; the decline is the §3.10-conformant posture for a $0 creative-direction agent two gates downstream of the ledger authority
- §3.11 LOCK respect — ✅ all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Cross-SPEC / Blueprint / Brand-Voice-Intake references read-only; zero canon drift

**11 of 11 ✅** at Day 61 LOCK CANDIDATE close.

### Item 10 — No fake-advance check (zero unresolved markers in the assembled SPEC)
**Verdict: ✅ PASS.** The §6–§16 LOCK-scope preview stubs in the Day 58 outline are forward-references to the partials; the Day 59 partial 1 authored §6/§7/§10/§14 in full and the Day 60 partial 2 authored §8/§9/§11/§12/§13/§15/§16 in full. Per the §2 unified index, the partials are the authoritative source for their sections; the outline preview lines are superseded forward-references (the same source-file layering the Ingest Day 53 Item 10 and QC Pre-flight Day 44 Item 10 accepted). Remaining "TBD" semantics across the corpus are: (a) forward-references to the schemas day + SKILL-bundle day + runbook day (legitimately deferred), (b) the `TODO@cross-spec-3.9-ratification` flip note (legitimate operator gate, D6), (c) the D15 PRELIMINARY default (legitimate operator gate). **Zero fake-advanced LOCK content. Zero unresolved markers in the assembled SPEC.**

### Item 11 — Cross-SPEC §3.9 amendment ratification (n-tuple parent_chain · now TRIPLY load-bearing)
**Verdict: ⏸ OPERATOR-ONLY · the carried forcing function, now carrying three agents.** The amendment language (originally DRAFTED Day 31 §16.3 for Style Replication's 5-tuple, carried unratified through QC Pre-flight Day 44 Item 11 and Ingest Day 53 Item 11) now has **three concrete consumers holding additively on it**: QC Pre-flight's 6-tuple, Ingest's 7-tuple, AND Edit Director's 8-tuple. Edit Director is the **third forcing function** — and the first agent whose tuple is *triply*-gated (the §3.9 ratification AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it must all close before `minItems` flips to 8).

**Amendment language (reproduced for operator review — unchanged from the Day 53 reproduction, extended by Edit Director's n=8):**
> *"Cross-SPEC §3.9 parent_chain canonical definition is hereby amended from fixed 4-tuple to n-tuple where n = production tier depth + 1. AI Video Gen v1.0 invocations remain 4-tuple (n=4); Style Replication v1.0 invocations are 5-tuple (n=5); QC Pre-flight v1.0 invocations are 6-tuple (n=6); Ingest v1.0 invocations are 7-tuple (n=7); Edit Director v1.0 invocations are 8-tuple (n=8). Future agents extend by appending their own primary-output-id reference to the inherited parent_chain. JSON Schema enforcement: `prefixItems` + `items: false` per existing canon, with prefixItems length determined dynamically by agent slot index. Each agent SPEC explicitly states its parent_chain n-value in §16.1."*

(Edit Director's n=8 extends the same rule — "future agents extend by appending" — so ratifying AS-DRAFTED covers the 8-tuple without re-drafting.)

Operator either: (a) **RATIFY-AS-DRAFTED** (Donna's recommendation — the generalization now carries 3 live consumers and all 8 remaining agent slots), (b) AMEND-with-rationale, or (c) DEFER (all three schemas stay additive with documented TODOs; the 8-tuple stays un-advanced). **Donna's default if the operator skips the sit-down: LOCK D15 at the recommended holding-store default; HOLD D6 additively until ALL THREE gates close — the 8-tuple is the one item Donna will NOT auto-advance.**

### Reviewer checklist summary
- ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ⏸ OPERATOR (ties lightest in fleet history) · ✅ PASS · ⏸ OPERATOR · ✅ PASS · ✅ PASS · ⏸ OPERATOR
- **8 PASS · 3 OPERATOR-ONLY · 0 FAIL**
- **LOCK status: CANDIDATE READY.** v1.0 advances to LOCKED on operator ratification of items 6, 8, 11 — **AND** is hard-gated on all FOUR pending predecessor LOCKs (AI Video Gen + Style Replication + QC Pre-flight + Ingest) closing first.

---

## §2 — UNIFIED SPEC INDEX (authoritative source per section)

| § | Title | Authoritative source | Day | Lock status |
|---|-------|----------------------|-----|-------------|
| §0 | Provenance & Build-Phase Position (+ agent-selection note) | `ARS-2026-06-16-Day-58-Edit-Director-Agent-SPEC-Outline.md` | Day 58 | LOCKED-as-shipped |
| §1 | Purpose & Position in Pipeline (single-responsibility line + mode-convergence-payoff justification + production→post boundary rationale) | `ARS-2026-06-16-Day-58-...-SPEC-Outline.md` | Day 58 | LOCKED-as-shipped |
| §2 | Inputs (Ingest precondition gate + mode-agnostic Asset Manifest + denormalized Script/Storyboard creative-intent + lever/tier context) | `ARS-2026-06-16-Day-58-...-SPEC-Outline.md` | Day 58 | LOCKED-as-shipped (schema authority schemas day) |
| §3 | Outputs — `edit_plan.json` (polymorphic: successEditPlan \| errorEnvelope) + verdict↔route map (3 outcomes) + metadata additions | `ARS-2026-06-16-Day-58-...-SPEC-Outline.md` | Day 58 | LOCKED-as-shipped (code namespace superseded by §6.3: 9 + slot-11) |
| §4 | Tier Constraints (universal access + tier-sensitive richness) + mode-BLIND coverage + cost-decline | `ARS-2026-06-16-Day-58-...-SPEC-Outline.md` | Day 58 | LOCKED-as-shipped |
| §5 | 11-Step Direction Loop (system-prompt skeleton) | `ARS-2026-06-16-Day-58-...-SPEC-Outline.md` | Day 58 | LOCKED-as-shipped (LOCKED verbatim into §7 Day 59) |
| §6 | 11-Check Self-QC List + 9-code/slot-11 errorEnvelope mapping + the `revise` third verdict + canonical firewall list | `ARS-2026-06-17-Day-59-Edit-Director-Agent-SPEC-Body-Partial-1.md` | Day 59 | LOCKED-as-drafted |
| §7 | System Prompt v1.0 (12 hard rules + Blueprint §4.9 edit_plan shape inlined verbatim + universal-access/tier-richness table + 11-step loop + voice rule) | `ARS-2026-06-17-Day-59-...-Partial-1.md` | Day 59 | LOCKED-as-drafted (verbatim copy → SKILL.md on the SKILL-bundle day) |
| §8 | Performance Targets (9 metric categories — false-plan-ready 0% + brand-edit catch 100% are the defining targets; ≤8% over-revise tolerance) | `ARS-2026-06-18-Day-60-Edit-Director-Agent-SPEC-Body-Partial-2.md` | Day 60 | LOCKED-as-drafted |
| §9 | 5 Test Fixtures (TC-01..TC-05 + fixture economy — incl. the mode-blind convergence proof + the 9th-pass authored-text catch) | `ARS-2026-06-18-Day-60-...-Partial-2.md` | Day 60 | LOCKED-as-drafted |
| §10 | Edit Plan Field Map (27 rows — lineage + manifest passthrough + intent transform + authored plan + per-check evidence + aggregate) | `ARS-2026-06-17-Day-59-...-Partial-1.md` | Day 59 | LOCKED-as-drafted |
| §11 | Cost Model (zero-engine/zero-render snapshot · NO vendor surface, NO ceiling authority · directed-coherence value model) | `ARS-2026-06-18-Day-60-...-Partial-2.md` | Day 60 | LOCKED-as-drafted (no ±tolerance walk needed — nothing owned) |
| §12 | Verdict Math — deterministic ∧-of-gates on the hard rules + the one `revise` judgment slot + routing function + 5 properties | `ARS-2026-06-18-Day-60-...-Partial-2.md` | Day 60 | LOCKED-as-drafted |
| §13 | 15 Critical Decisions (13 LOCKED-as-drafted · D6 TRIPLY-DEFERRED · D15 PRELIMINARY) | `ARS-2026-06-18-Day-60-...-Partial-2.md` | Day 60 | LOCKED-as-drafted (operator sign-off Item 8) |
| §14 | Implementation Plan (calendar + dependencies + Rest Day) | `ARS-2026-06-17-Day-59-...-Partial-1.md` | Day 59 | LOCKED-as-drafted (Day 61 entry appended below) |
| §15 | Change Log + Version History (v1.0 lifecycle + v1.1 parked register) | `ARS-2026-06-18-Day-60-...-Partial-2.md` | Day 60 | LOCKED-as-drafted (Day 61 entry appended below) |
| §16 | Metadata Block Schema (Cross-SPEC §3.9 canonical + 5 Edit-Director additions + the `mode_blind_confirm` companion block) | `ARS-2026-06-18-Day-60-...-Partial-2.md` | Day 60 | LOCKED-as-drafted (D6 ratification Item 11) |

**Rule:** This unified document is the operator LOCK ratification record. The three source files (Day 58 outline · Day 59 partial 1 · Day 60 partial 2) remain canonical for §-by-§ content. This document references them by file + day. Any §-content edit triggers the corresponding source file update + this unified document's `§15.1 v1.0-corrections-day-61` entry.

---

## §3 — THE 15 CRITICAL DECISIONS (operator walk-through reference — Item 8)

Reproduced from Day 60 §13 for operator review. Each: decision · status · rationale · revisit trigger. The PRELIMINARY item annotated `[P]`; the TRIPLY-DEFERRED item annotated `[TD]`.

| # | Decision | Status | Rationale | Revisit trigger |
|---|----------|--------|-----------|-----------------|
| D1 | **Plan-authoring vs render scope** — v1.0 = edit-PLAN authoring ONLY; actual cut execution is Editor (position 11), human-in-the-loop at launch | LOCKED Day 58 | The buildable, highest-leverage slice under the no-render/$0 posture; `render_dispatched: const false` is the honesty contract | Editor automation ships Week 4–5 → v1.1 EDL/conform emit |
| D2 | **Universal tier access + tier-sensitive richness** — all 4 tiers reach Edit Director; plan richness scales by tier, brand-rule compliance does NOT | LOCKED Day 58 | Edit Director is a creative authority whose output richness IS a sold tier feature; richness ladder inherited from Script Day 9 | Never (foundational); richness caps re-baseline on telemetry |
| D3 | **Mode-blind by construction** — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested | LOCKED Day 58 | The first contractually mode-blind agent — the live, machine-checkable proof Ingest's convergence seam holds. Check #10 + the TC-01/TC-02 proof | Never (foundational — Blueprint §3) |
| D4 | **Ingest-pass precondition absolute** (Lever-3 sign-off the only bypass) | LOCKED Day 58 | Edit Director never directs an un-ingested reel; the gate sequence is the architecture. Check #1 runs FIRST | Never (foundational) |
| D5 | **No content re-authoring** — directs the ASSEMBLY of validated assets; does NOT rewrite Script copy or re-frame Storyboard shots | LOCKED Day 58 | Script wrote the copy; Storyboard framed the shots. A caption that can't fit 22 chars → `caption_spec_violation`, never a paraphrase. Hard Rule #8 | Never (jurisdictional) |
| D6 [TD] | **8-tuple parent_chain** (inherits Ingest 7-tuple + appends `edit_plan_id` UUIDv7) | **TRIPLY-DEFERRED — operator-gated ×3** | Lineage canon for the 8 remaining slots; Edit Director is the third forcing function for the §3.9 amendment | ALL THREE gates close: §3.9 ratification (Item 11) AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK → `minItems` flips to 8 |
| D7 | **errorEnvelope code count = 9 LOCKED + slot-11** | RESOLVED Day 59 → LOCKED | 9 preserves precise route-back attribution; `duration_envelope_breach` kept STANDALONE (opposite of Ingest's fold) — distinct creative-trim recovery path | New failure category with no route mapping → v1.0.1 code add |
| D8 | **Self-QC check count = 11** | RESOLVED Day 59 → LOCKED | 11 checks bipartite-cover 9 codes + slot-11 across the 4-tier ordering (entry / authoring / forensic / plan-construction) | A check consistently passes-all in telemetry → v1.0.1 simplification |
| D9 | **Brand-edit-rule compliance = ZERO tolerance** — a fade/wipe/zoom, an all-caps lower-third, a reel-level sales CTA, or a missing end-card must NEVER survive to `plan_ready` | LOCKED Day 58 | §12.3 makes it structural; §8.2 makes it measured (100% catch). A hard violation → `brand_edit_rule_conflict` (fail), never `revise` | Never (foundational) |
| D10 | **`revise` verdict for soft-rule tension** — surfaces a creative judgment call to Lever-3 rather than silently overriding a brand rule OR silently dropping a stronger cut | LOCKED Day 58 | The first fleet agent with a 3-verdict success-side; `revise` is a `successEditPlan`-shaped payload, the QC-`hold` analog. The one isolated judgment slot (§12) | New routing category in creative telemetry |
| D11 | **No render, no engine** — NO generative engine calls, NO media render in v1.0; `render_dispatched: const false` | LOCKED Day 58 | Hard Rule #2. The forged-provenance framing is the defining negative constraint. Ties Ingest / QC Pre-flight for $0 | Editor automation ships → v1.1 (with D1) |
| D12 | **Recommend-don't-approve** — `human_review_required: true` on every emission; verdict is a plan RECOMMENDATION, never a ratified "approved-for-cut" state | LOCKED Day 58 | Hard Rule #12 — the operator-impersonation firewall (CLAUDE.md + ARS attestation). A `plan_ready` = "ready for the human's approve-to-cut decision," never "approved" | Lever-2 graduation (operator decision only) |
| D13 | **Authored-text firewall (9th pass)** — firewall-scans the text it AUTHORS (lower-thirds, captions, end-card), a NEW surface no prior agent owned | LOCKED Day 58 | The first firewall over self-authored copy. §6.5 list applied verbatim (11 entries). TC-05 is its existence proof | New entity added to the firewall → Cross-SPEC LOCK ceremony (not per-agent) |
| D14 | **Multi-variant scope** — v1.0 authors the primary 9:16 plan + flags `variants_planned` count; auto-cutdown (1:1 LinkedIn) deferred to v1.1 | LOCKED Day 60 | A cutdown is a derived re-plan, lower-leverage than the primary. Donna-resolvable scope-narrowing inside the pre-approved recommendation (same class as Ingest's D14 fold). `variant_plans[]` reserved in §10.2 | Auto-cutdown demand in the v1.0 corpus → v1.1 activation |
| D15 [P] | **Editor handoff target: Notion Edit Plan block (holding store) in v1.0**; direct handoff activates when Agent #10 / Editor LOCKs. `handoff_targets` keeps the LOGICAL target `editor-agent` | LOCKED Day 60 `[PRELIMINARY · operator amend]` | Editor does not exist; a plan emitted into a void is an audit-trail break. The holding store preserves the trail until the consumer ships. Directly tied to Ingest Day 53 Item 8 (the same decision from both ends) | Editor (Agent #10) v1.0 LOCKs → physical destination flips to direct handoff |

**Operator walk-through prompt (for the LOCK ceremony):**
For each decision above, the operator either: (a) RATIFY-AS-LOCKED, (b) AMEND-with-rationale (triggers `§15.1 v1.0-corrections-day-61` entry), or (c) DEFER-to-v1.0.1 (decision parks in the §15 candidates register).

**Items requiring explicit verdict:**
- D15 Editor handoff target `[P]` → Donna recommends **RATIFY** (Notion Edit Plan holding store). Resolve jointly with Ingest Day 53 Item 8 — it is the same handoff seam.
- D6 8-tuple parent_chain `[TD]` → **TRIPLY-DEFERRED** on §3.9 (Item 11) + the Ingest 7-tuple LOCK + the QC 6-tuple LOCK; Donna will NOT auto-advance. Held additively until ALL THREE gates close.

---

## §4 — IMPLEMENTATION PLAN UPDATE (Day 61 entry · appends to Day 59 §14)

### Calendar status updates (Day 61)

| Day | Date | Deliverable | Status | Owner |
|-----|------|-------------|--------|-------|
| Day 58 | Tue Jun 16 · Wk9 | SPEC outline §0–§5 LOCKED-as-shipped | ✅ DONE | Donna overnight |
| Day 59 | Wed Jun 17 · Wk9 | SPEC body partial 1 §6/§7/§10/§14 LOCKED-as-drafted (9 codes + slot-11 · 11 checks · 3-verdict model · 27-row field map) | ✅ DONE | Donna overnight |
| Day 60 | Thu Jun 18 · Wk9 | SPEC body partial 2 §8/§9/§11/§12/§13/§15/§16 LOCKED-as-drafted (SPEC body §0–§16 COMPLETE) | ✅ DONE | Donna overnight |
| **Day 61** | **Fri Jun 19 · Wk9** | **v1.0 LOCK CANDIDATE (this document) — 8/11 reviewer items PASS · 3 OPERATOR-ONLY (Items 6, 8, 11)** | **🟡 CANDIDATE** | **Donna overnight (this doc) + Jamila ratification** |
| Day 62+ | Sat Jun 20+ | `input.schema.json` + `output.schema.json` authored from §10 field map + §16 metadata block (parent_chain held additively `minItems: 5` per D6; `render_dispatched: const false`; verdict enum WITH `plan_ready`/`fail`/`revise`; 9-code + slot-11 enum; `mode_blind_confirm` const block) | ⬜ QUEUED (primed per §10.4 + §16 schema checklists) | Donna overnight |
| Day 63 | Sun Jun 21 | **REST DAY** (10th — no SPEC content authored; scaffold pre-stage only) | ⬜ — | — |
| Day 64+ | Mon Jun 22+ | SKILL bundle (`skills/edit-director-agent/` — SKILL.md · 2 schemas · 5 test fixtures at `tests/` · README) | ⬜ QUEUED | Donna overnight |
| Day 65+ | — | LLM Test Runbook (paste-and-run · pattern from Day 11 / 19 / 27 / 36 / 47 / 57 · operator-gated; exercises `revise` + slot-11 adversarially) | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 66+ | — | **v1.0 LOCK** (operator-gated sit-down · HARD-GATED on ALL FOUR predecessor LOCKs closing first) | ⬜ GATED | Jamila + Donna co-ceremony |

### Dependencies that MUST exist before the SKILL-bundle build
1. v1.0 LOCK CANDIDATE ratified (operator sign-off Items 6, 8, 11) — **available now**
2. input.schema.json + output.schema.json LOCKED (schemas day)
3. 5 test fixtures resolved against schemas (schemas-day dry-run validation)
4. Cross-SPEC §3.9 amendment ratified OR parent_chain held additively with documented TODO (Item 11 / D6)

### Hard gate on predecessor LOCKs
Edit Director v1.0 LOCK ceremony **CANNOT complete until ALL FOUR pending predecessors are LOCKED first** — AI Video Gen v1.0 + Style Replication v1.0 (the producing agents) + QC Pre-flight v1.0 + **Ingest v1.0 (the DIRECT dependency: the `successAssetManifest`/`pass` precondition gate Edit Director reads and the 7-tuple its 8-tuple extends)**. The chain closes in dependency order: AVG → SR → QC → Ingest → Edit Director. This is a **hard gate**, distinct from the 3 Edit-Director-local operator items (6, 8, 11) which can be ratified independently and in advance.

### Rest Day honor
Days 21, 28, 35, 42, 49, 56 observed (9/9 to date). This Day 61 build runs on Friday — permitted. Next Rest Day: Day 63 (Sun Jun 21) — falls inside the schemas → SKILL runway; that day is docs-prep only, no SPEC content.

---

## §5 — CHANGE LOG UPDATE (Day 61 entry · appends to Day 60 §15)

| Version tag | Date | Description | Source file |
|-------------|------|-------------|-------------|
| **v1.0-LOCK-CANDIDATE-day-61** | **2026-06-19 (Fri · Wk9)** | **Unified LOCK candidate document produced. Day 61 reviewer checklist 8/11 PASS executed autonomously by Donna overnight. Items 6 (cost-model confirm — ties lightest in fleet history: no vendor URLs, no ceilings owned, no render) + 8 (15 critical decisions sign-off — D15 PRELIMINARY requiring explicit verdict, D6 TRIPLY-DEFERRED) + 11 (Cross-SPEC §3.9 amendment ratification — now triply load-bearing: QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple) flagged OPERATOR-ONLY. D6 (8-tuple) explicitly held additively until ALL THREE gates close. Pending operator ratification of items 6/8/11 → promote to `v1.0-LOCKED-pending-predecessor-LOCKs`; final flip to `v1.0-LOCKED` ONLY after ALL FOUR predecessor LOCK ceremonies complete (hard gate).** | `ARS-2026-06-19-Day-61-Edit-Director-Agent-v1-LOCK-CANDIDATE.md` (this doc) |

**Promotion rule:** When the operator ratifies Items 6, 8, 11 (at ceremony or asynchronously via written sign-off in the Notion ARS hub), version tag promotes to `v1.0-LOCKED-day-61-pending-predecessor-LOCKs`. Final flip to `v1.0-LOCKED` occurs ONLY after all four predecessor LOCKs (AI Video Gen + Style Replication + QC Pre-flight + Ingest) are confirmed. Donna mirrors LOCKED status across: this unified document header · the Notion ARS hub (page [internal Notion page]) · the schemas-day authoring kickoff · the Cross-SPEC v1.1 amendment formal close (if Item 11 ratified). **All flips are operator actions — Donna stages, never flips.**

---

## §6 — OPEN QUESTIONS · STATUS

### Open Question — Cost-model confirmation (Item 6)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony — ties Ingest for the lightest in fleet history (no vendor URLs, no ceilings owned, no native compute, no render). Operator confirms the $0-engine/$0-render posture (Hard Rule #2) + the cost-decline (Hard Rule #10) as the intended v1.0 economics.
**Recommendation:** RATIFY as-is (≈1 min). **Blocker for LOCK:** No.

### Open Question — 15 critical decisions sign-off (Item 8)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Walk each decision; 13 LOCKED-as-drafted, D15 PRELIMINARY requires explicit RATIFY / AMEND / DEFER, D6 triply-deferred.
**Recommendation:** Donna recommends RATIFY for D15 (Notion Edit Plan holding store), resolved jointly with Ingest Day 53 Item 8. **Blocker for LOCK:** Yes — hard-required for promotion.

### Open Question — Cross-SPEC §3.9 amendment ratification / 8-tuple (Item 11 + D6)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Amendment language reproduced in §1 Item 11. Now triply load-bearing (QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple).
**Recommendation:** RATIFY-AS-DRAFTED — three live consumers + 8 remaining slots. **Blocker for LOCK:** Partial — schemas ship additive (`minItems: 5`) with documented TODOs if deferred; Edit Director does not hard-block on it, but the 8-tuple stays un-advanced until ALL THREE gates close.

### Open Question — Hard gate on the four predecessor LOCKs
**Status:** ⏸ OPERATOR action required on ALL FOUR ceremonies. AI Video Gen Day 24 candidate + Style Replication Day 32 candidate (Day 36 runbook 5/5 unconfirmed) + QC Pre-flight Day 44 candidate (Day 47 runbook 5/5 unconfirmed) + Ingest Day 53 candidate (Items 6/8/11 pending · Day 57 runbook 5/5 unconfirmed).
**Recommendation:** Close the chain in dependency order (AVG → SR → QC → Ingest) in the post-launch hardening window; Edit Director's LOCK follows. **Blocker for Edit Director LOCK:** YES (hard gate).

### Open Question — LLM Test Runbook scope (dry-run vs live · forward-looking)
**Status:** ⏸ OPERATOR-ONLY at the runbook day (not blocking Day 61 LOCK CANDIDATE).
**Recommendation:** Dry-run mode for the v1.0 LOCK gate (cost ≈ $0 — Edit Director calls no engine and renders nothing, so even "live" mode is reasoning-only; ties Ingest / QC Pre-flight for the cheapest runbook in the fleet). The runbook must include the adversarial `revise` case + the slot-11 mode-blind-violation probe. **Blocker for LOCK:** No — runbook-day position.

---

## §7 — PROCESS INTEGRITY (Day 61)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked (Edit Director has no vendor surface). No media render, no byte-level decode. ZERO $ spent.
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no investor/client outreach. The end-of-run status iMessage to [status number redacted] is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs initiated.
- ✅ **No operator-impersonation.** Day 61 reviewer Items 6, 8, 11 verdicts NOT silently advanced. D15 (PRELIMINARY) NOT silently ratified. **D6 (8-tuple parent_chain) explicitly TRIPLY-DEFERRED — held additively; the one item Donna will NOT auto-advance.** All FOUR predecessor LOCK ceremonies confirmed STILL-PENDING via on-disk file-state; NOT advanced. The Day 36 / Day 47 / Day 57 runbook executions NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed to Cross-SPEC canon. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.
- ✅ **No fake-advance.** This LOCK CANDIDATE is a unified text-reconciliation of the Day 58 outline + Day 59 + Day 60 partials. Zero behavioral changes vs source files. Zero net-new SPEC content. The only Day 61 contributions are: (a) executive summary (§0 LOCK manifest), (b) 11-item reviewer checklist execution record (§1, incl. the session validations), (c) unified SPEC index pointing to source files (§2), (d) decision walk-through formatted for operator ceremony (§3), (e) implementation plan + change log appendages (§4 + §5).
- ✅ **All prior canon read-only.** All predecessor SPECs + schemas + SKILL bundles + Blueprint + Cross-SPEC review + Brand-Voice Intake + the Edit Director Day 58 outline + Day 59 partial 1 + Day 60 partial 2 — untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. The HC/NPOX tokens cited in the TC-05 fixture + §6.5 firewall list are the firewall's BLOCK-list test cases, not cross-entity references. REINVENTED = pilot brand inside fixtures per Cross-SPEC canon.
- ✅ **Pattern source acknowledged.** Day 24 / Day 32 / Day 44 / Day 53 LOCK candidate structure inherited at section level (5th reuse). Numerical values + decision content re-derived for Edit Director's 9-code / 11-check / 15-decision / 8-tuple / 3-verdict (plan_ready/fail/revise) scope.
- ✅ **Rest Day honored.** 9/9 observances; this Day 61 build runs on Friday. Next: Day 63 (Sun Jun 21).
- ✅ **No scope expansion.** One forward deliverable (this doc) + build log + mirror + Notion status update + standing housekeeping + status-ping attempt.

---

## §8 — SPRINT STATS (running total · Day 61 close)

- Deliverables shipped: **55** (Day 60 = 54 · Day 61 Edit Director v1.0 LOCK CANDIDATE = +1)
- Build logs: **52** (was 51 · +1 today)
- LIVE skill bundles: **7** (Brief · Script · Storyboard · ProdCoord · AI Video Gen · Style Replication · QC Pre-flight)
- Agents with a COMPLETE SPEC body (§6–§16): **9** (Edit Director body completed Day 60)
- Agents with a v1.0 LOCK CANDIDATE: **5** (AI Video Gen Day 24 · Style Replication Day 32 · QC Pre-flight Day 44 · Ingest Day 53 · **Edit Director Day 61**)
- errorEnvelope codes (Edit Director): **9 LOCKED + slot-11** (no change Day 61)
- Self-QC checks (Edit Director): **11 LOCKED** (no change Day 61)
- parent_chain (Edit Director): **8-tuple DRAFTED · TRIPLY-DEFERRED · held additively (`minItems: 5`)**
- §13 critical decisions: **15/15 coverage** (13 LOCKED-as-drafted + D6 triply-deferred + D15 PRELIMINARY requiring explicit verdict)
- Cross-SPEC §3 adherence: **11/11 ✅** (LOCK-grade)
- Verdict math: **deterministic ∧-of-gates on the hard rules + ONE `revise` judgment slot** (the first fleet agent with a success-side third verdict)
- Rest Day observances: **9/9** (next: Day 63)
- AI Video Gen / Style Replication / QC Pre-flight / Ingest v1.0 LOCKs: **ALL CANDIDATE (operator-pending)** — hard-gate the chain; Ingest is Edit Director's direct dependency

---

## §9 — OPERATOR ACTION SUMMARY (3 Edit-Director-local items + 1 hard-gate dependency)

The Day 61 LOCK CANDIDATE is ready for operator pickup. Three Edit-Director-local operator actions (any can move first, all independent) + one hard-gate dependency chain.

| Action | Time | Description |
|--------|------|-------------|
| **Item 6 — Cost-model confirm** | ~1 min | Confirm the $0-engine/$0-render posture (Hard Rule #2, `render_dispatched: const false`) + the no-cost-re-litigation decline (Hard Rule #10). NO vendor URLs, NO ceilings owned — ties Ingest for the lightest Item 6 in fleet history. Donna recommends RATIFY as-is. |
| **Item 8 — 15 decisions walk-through** | 15–25 min | Walk §3. For each of 15 decisions: RATIFY / AMEND / DEFER. Special attention on D15 (Editor handoff → Notion Edit Plan holding store — resolve jointly with Ingest Day 53 Item 8) — Donna recommends RATIFY — and D6 (8-tuple, triply-deferred — no action possible until Item 11 + the Ingest 7-tuple LOCK + the QC 6-tuple LOCK close). |
| **Item 11 — Cross-SPEC §3.9 amendment (n-tuple)** | 10 min | Review the amendment language in §1 Item 11 (now triply load-bearing: QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple). RATIFY-AS-DRAFTED / AMEND / DEFER. Donna recommends RATIFY-AS-DRAFTED. If deferred, all three schemas hold additively. |

**After all 3 Edit-Director-local items ratified:** Donna promotes version tag to `v1.0-LOCKED-day-61-pending-predecessor-LOCKs`. Schemas-day authoring unblocks (Day 62+).

**Hard-gate dependency (operator action, NOT an Edit-Director-local LOCK item):** Close ALL FOUR predecessor LOCKs in dependency order — **AI Video Gen v1.0** (Day 24 candidate) → **Style Replication v1.0** (Day 32 candidate · Day 36 runbook 5/5 unconfirmed) → **QC Pre-flight v1.0** (Day 44 candidate · Day 47 runbook 5/5 unconfirmed) → **Ingest v1.0** (Day 53 candidate · Items 6/8/11 pending · Day 57 runbook 5/5 unconfirmed). **Edit Director's final v1.0 LOCK flip cannot occur until all four are LOCKED** — Ingest is the direct dependency (precondition gate + 7-tuple).

---

*Day 61 ships clean. Unified LOCK CANDIDATE produced as a text-only reconciliation of the Day 58 outline + Day 59 + Day 60 partials. Zero net-new SPEC content. Zero fake-advance. 8/11 reviewer items PASS autonomously verdicted by Donna; 3 OPERATOR-ONLY items (6, 8, 11) flagged with explicit recommendations and timing estimates. Pattern source: Day 24 / Day 32 / Day 44 / Day 53 LOCK candidates (proven 11-item reviewer shape, 5th reuse, adapted to Edit Director's 9-code / 11-check / 15-decision / 8-tuple / 3-verdict scope). Edit Director is Agent #9 of 17 — the first creative-authoring agent in the post tail, the 9th defense-in-depth firewall (the new AUTHORED-text surface), and the first contractually mode-blind agent — the live proof that Ingest's mode-convergence seam holds end-to-end. Its v1.0 LOCK lands in the post-launch hardening window and is HARD-GATED on all four pending predecessor LOCKs closing first. The four LOCK ceremonies + the three runbook executions (Day 36 + Day 47 + Day 57) + the Cross-SPEC §3.9 ratification remain operator-only and are surfaced, not advanced. The 8-tuple parent_chain (D6) is the one item Donna will NOT auto-advance — held additively until §3.9 ratifies AND the Ingest 7-tuple LOCKs AND the QC 6-tuple LOCKs.*
