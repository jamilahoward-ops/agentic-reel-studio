# ARS — Ingest Agent v1.0 SPEC (UNIFIED · LOCK CANDIDATE · Day 53)

**Author:** Donna (overnight build session · Sequel Digital ARS sprint)
**Date:** 2026-06-11 (Thu · Day 53 · Wk8 · post-launch hardening window)
**Document status:** **v1.0 LOCK CANDIDATE — awaiting operator sign-off on items 6, 8, 11 + the THREE predecessor LOCKs (hard gate)**
**Lock signal:** Items 1–5, 7, 9, 10 of the Day 53 reviewer checklist are EXECUTED and PASS. Items 6, 8, 11 are operator-only.
**Predecessor LOCKs:** Brief Agent v1.0 (Day 6) · Script Agent v1.0 (Day 9) · Storyboard Agent v1.0 (Day 14) · Production Coord Agent v1.0 (Day 14) · Cross-SPEC Canon (Day 12) · **AI Video Gen v1.0 LOCK CANDIDATE (Day 24 — operator-gated; STILL PENDING) · Style Replication v1.0 LOCK CANDIDATE (Day 32 — operator-gated; STILL PENDING) · QC Pre-flight v1.0 LOCK CANDIDATE (Day 44 — operator-gated; STILL PENDING)**
**Hard gate on predecessor LOCKs:** Ingest's v1.0 LOCK ceremony CANNOT complete until **all three** pending predecessors LOCK first — AI Video Gen + Style Replication (the producing agents whose asset sets Ingest consumes) and **QC Pre-flight in particular (Ingest's DIRECT dependency: the 6-tuple parent_chain the 7-tuple extends, and the `preflight_report.json` precondition gate)**. This LOCK CANDIDATE is authored on LOCK-stable **text artifacts** (the SPECs + schemas as drafted); it uses **zero production output** from any predecessor. Forward-design under the same posture as the Day 48 outline and both body partials.
**Position note:** Agent #8 of 17 — the FIRST post-production agent, the 8th defense-in-depth firewall pass (asset layer, a NEW surface), and the mode-convergence seam (Blueprint §3: "from Ingest onward, post-production is mode-agnostic"). Its v1.0 LOCK lands inside the post-launch hardening window and does **NOT** gate the commercial launch (which ships on the six built production agents through the QC Pre-flight gate). The Agent-#8-slot selection (Donna, Day 48 — surfaced not hidden) remains operator-confirmable at the QC Pre-flight LOCK-ceremony close.

---

## §0 — LOCK MANIFEST (executive summary)

| Item | Status |
|------|--------|
| SPEC sections drafted | **17 / 17** (§0–§16 — outline §0–§5 Day 48 · body §6/§7/§10/§14 Day 51 · body §8/§9/§11/§12/§13/§15/§16 Day 52) |
| `<<TBD-D52>>` markers remaining in the ASSEMBLED SPEC | **0 unresolved** (grep-verified: outline 0 · partial 2 0 · partial 1 carries 7 — ALL are the §8–§16 placeholder stubs whose authoritative content partial 2 authored; superseded forward-references, not open items. See Item 10.) |
| SPEC body completeness | **§6–§16 COMPLETE** (Day 51 + Day 52 partials fully cover the body; this LOCK CANDIDATE is a pure text-only reconciliation, zero net-new SPEC content) |
| Error code canonical count | **8 LOCKED + slot-11 catch-all** (Day 51 §6.3 — `upstream_qc_not_passed` · `upstream_not_success` · `asset_uri_integrity_failure` · `asset_spec_violation` · `missing_shot_coverage` · `audio_sync_failure` · `asset_firewall_breach` · `manifest_lineage_failure` + `ingest_agent_failed` slot-11) — narrowed from the outline's 9+alias via the D14 duration fold |
| Slot-11 errorEnvelope name | `ingest_agent_failed` (Cross-SPEC §3.6 conformant — agent_id `ingest-agent` → snake_case; one canonical fallback code per agent slot, no orphan references) |
| Self-QC check count | **11** (Day 51 §6.1 — entry-validation #1–2 · five asset adjudications #3–7 · forensic #8 · manifest-construction integrity #9–11) bipartite-covering the 8 codes + slot-11 |
| Verdict model | **Pass / Fail / Reshoot — NO `hold`** (deliberate divergence from QC Pre-flight §6.4, documented: Ingest's domain is deterministic — a file is present or absent; there is no asset-layer ambiguity for a human to adjudicate mid-verdict. Human deferral lives in `human_review_required: true` on EVERY emission, not in a verdict value.) `reshoot` is Mode-A-exclusive (D3) |
| Verdict math | **Deterministic ∧-of-8-gates · ZERO tunable thresholds** (Day 52 §12) — one term per Check #1–#8; halts adjudicate before fails; first-failing-check-in-tier-order names the headline code with no short-circuit nulls; Mode A take-substitution ladder encoded. Properties: deterministic / monotone / zero-false-pass-by-construction / auditable-recomputable |
| Cost authority | **NONE — deliberate decline** (Hard Rule #10). Ingest does NOT re-litigate the cumulative cost ledger (QC Pre-flight's jurisdiction). The combined tier ceilings ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter Mode A) are upstream facts restated for traceability only |
| Self per-reel cost | **≈ $0.00** ($0.00 engine + $0.00 probe structurally guaranteed; LLM reasoning ≈ $0.02–0.08 inside the latency envelope). Ties QC Pre-flight for lowest-cost agent in the 17-agent fleet — and is the only agent with NO native-compute option at all |
| Performance target portfolio | **9 metric categories** (Day 52 §8) — schema validity 100% · asset-firewall catch 100% (8th pass) · coverage-gap catch 100% / **zero phantom coverage** · **false-pass 0%** (the defining target) · false-fail ≤5% (asymmetric tolerance, deliberate) · URI-integrity catch 100% · p50 ≤25s / p95 ≤75s · $0.00 engine+probe (structural invariant, not a budget) · self-QC first-pass yield ≥90% / slot-11 halt <2% |
| Test fixture portfolio | **5 fixtures** (Day 52 §9) — TC-01 Mode B Pro clean PASS · TC-02 Mode C Enterprise clean PASS (**the TC-01/TC-02 pair = the mode-convergence proof**: byte-shape-identical downstream of `mode_convergence`) · TC-03 Mode A coverage gap, ladder exhausted → `reshoot` + ProdCoord route · TC-04 aspect mismatch → `fail` + route · TC-05 banned token in a FILENAME + sidecar metadata → `asset_firewall_breach` (**the 8th-pass existence proof**). 5 of 8 codes behavioral; 3 entry/forensic halts + slot-11 schema-only (§9.1 fixture-economy rationale) |
| Cost model engine coverage | **ZERO generative engines + ZERO byte-probe** (by design — Hard Rule #2, `byte_probe_performed: const false`). **No external vendor-pricing URLs to walk AND no ceilings owned** — Item 6 below is the lightest operator spot-check in fleet LOCK history, lighter even than QC Pre-flight's |
| Metadata block schema | **Cross-SPEC §3.9 canonical + 5 Ingest additions** (`parent_chain` 7-tuple · `asset_manifest_class` · `manifest_evidence_hash` · `runtime_environment_class` · `byte_probe_performed const false`) — audit invariant. `human_review_required: const true` schema-enforced (recommend-don't-clear) |
| parent_chain | **7-tuple DRAFTED Day 51/52** (inherits QC Pre-flight's 6-tuple lineage + appends own `asset_manifest_id`, UUIDv7) — **DOUBLY-DEFERRED: gated on operator ratification of the Cross-SPEC §3.9 n-tuple amendment AND the QC Pre-flight 6-tuple LOCK.** Schema holds additively (`minItems: 5`, `prefixItems` 0–6, `maxItems: 7`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. The one item Donna will NOT auto-advance |
| 15 Critical Decisions | **15/15 §13 coverage** — 10 LOCKED-as-drafted Day 48 (D1–D5, D9–D13) + 3 RESOLVED Day 51 inside pre-approved target ranges → LOCKED-as-drafted (D7 code count / D8 self-QC count / D14 duration fold) + **D6 (7-tuple) DOUBLY-DEFERRED + D15 (Edit-Director handoff → Notion holding store) `[PRELIMINARY · operator amend]`** |
| 12 Hard Rules (system prompt) | LOCKED verbatim Day 51 §7.1 — operator copy-paste-ready into the SKILL.md. Defining rules: #2 no-engine/no-probe with the forged-provenance framing · #10 no cost re-litigation (the explicit decline) · #12 "RECOMMEND, do not CLEAR" |
| Blueprint §4.8 manifest shape | Inlined VERBATIM into the §7 system prompt — the LLM is the runtime source of truth for the `asset_bundle`/`spec_check` contract, not a side document (structural analog of QC Pre-flight inlining the 11-point gate) |
| Field map | **25 rows** (Day 51 §10 — 9 lineage + 5 bundle normalization [the mode-convergence map] + 6 per-check evidence + 5 manifest aggregate) + 4 v1.1 reserved fields + no-touch read-only references |
| Cross-SPEC §3 audit | **11/11 dimensions ✅** at LOCK-grade (Item 9 — full audit executed this document) |
| Authoring decisions documented | All §13 walk decisions + the 5 Day 52 key authoring decisions + the Day 48 agent-selection note — operator can ratify each at the LOCK walk-through |

---

## §1 — DAY 53 REVIEWER CHECKLIST · EXECUTION RECORD

The 11-item checklist mirrors the Day 24 AI Video Gen / Day 32 Style Replication / Day 44 QC Pre-flight LOCK candidate pattern (proven shape, **4th reuse**). Donna executed items 1–5, 7, 9, 10 autonomously overnight. Items 6, 8, 11 are operator-only.

### Item 1 — Error code count = 8 + slot-11 (verify exhaustive vs §6 11-check Self-QC list)
**Verdict: ✅ PASS.** Day 51 §6.3 mapping table enumerates all 8 codes + slot-11 catch-all with trigger-check mapping. The namespace was narrowed from the outline's 9 numbered codes + `duration_envelope_breach` alias via one deliberate fold: `duration_envelope_breach` → `asset_spec_violation` (an out-of-band duration is structurally a declared-spec mismatch — same defect family, same route-back target; `detail.subtype: "duration_envelope"` preserves the diagnostic). The fold resolves outline Open Question 6 exactly as recommended and mirrors the QC Pre-flight §6.3 narrowing discipline. Why 8 (vs QC Pre-flight's 9): Ingest's failure surface is narrower — one physical question ("can the editor open and cut these files?") decomposed into precondition, presence, spec, coverage, audio, firewall, and lineage. 8 is the floor that preserves precise route-back attribution at the asset layer; folding further (e.g. coverage into spec) would merge defects with *different* recovery paths (re-gen a missing shot vs re-grade an off-spec one), destroying the routing signal. Bipartite coverage confirmed (Item 5 also passes).

### Item 2 — Slot-11 errorEnvelope name verification
**Verdict: ✅ PASS.** Grep across Day 48 + Day 51 + Day 52 confirms `ingest_agent_failed` is the canonical slot-11 name in all OPERATIONAL positions (§6.1 Checks #9/#10/#11, §6.3 mapping table, §10.1 aggregate rows, §10.4 schema notes, §12 routing). Naming derives correctly per Cross-SPEC §3.6: agent_id `ingest-agent` → snake_case → `ingest_agent_failed`. Grep for legacy fallback names (`preflight_qc_agent_failed`, `style_replication_agent_failed`, `ai_video_gen_agent_failed`) across all three Ingest source files returns **zero hits** — no orphan references at all, operational or otherwise. Cross-SPEC §3.6 canon fully respected.

### Item 3 — Cost model accuracy (zero-engine + zero-probe · no vendor surface · no ceiling authority)
**Verdict: ✅ PASS · the structurally simplest Item 3 in fleet history.** Day 52 §11 establishes Ingest as the only agent with **neither** an external vendor-pricing surface (no engine — like QC Pre-flight) **nor** any native-compute option (unlike QC Pre-flight's optional $0.001/shot pHash/CLIP re-verify) **nor** any ceiling ownership (Hard Rule #10 explicitly declines the cost-ledger authority QC Pre-flight holds). The complete cost model is: $0.00 engine (structurally banned) + $0.00 probe (`byte_probe_performed: const false`) + ≈$0.02–0.08 LLM reasoning + $0.00 native compute/storage. Total `cost_incurred_usd` ≈ $0.00 reported to 2dp per Cross-SPEC §3.9. The §11.2 catch-cost-avoidance value model deliberately declines dollar-ROI quantification (no live defect corpus exists pre-orchestrator; inventing one would be fake precision — formalization parked to v1.1). **No pricing URL walk is required for this agent.**

### Item 4 — Tier-table + cost-decline consistency (universal access · no re-litigation)
**Verdict: ✅ PASS.** Cross-referenced across Day 48 + Day 51 + Day 52:
- Day 48 §1 + §4 universal-tier tables — all 4 tiers traverse Ingest at ~$0.00, verdict authority identical
- Day 51 §7.1 universal-tier table (runtime authoritative) — "Cost ceilings are enforced UPSTREAM at QC Pre-flight (Rule 10) — you carry none"
- Day 51 §7.3 cost posture — ceilings ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter Mode A) restated for traceability only, NOT re-litigated
- Day 52 §11.1 — "no cost ceiling and no ledger authority (Hard Rule #10 — QC Pre-flight's jurisdiction)"
- Day 52 §8 targets-NOT-carried list — no cost-ceiling adherence metric (QC Pre-flight's authority)
All values and decline-statements consistent. No drift. **No operator-amend flag** — the ceilings are upstream inheritances of QC Pre-flight canon restated verbatim; the universal-access posture is D2 (LOCKED-as-drafted, walked at Item 8). The margin-floor pricing conversation remains an inherited open item at the production-agent layer, NOT re-litigated by Ingest.

### Item 5 — Self-QC list ↔ 8 errorEnvelope codes + slot-11 bipartite coverage
**Verdict: ✅ PASS.** Day 51 §6.3 mapping table is bipartite: every one of the 11 self-QC checks resolves to exactly one code (or the shared slot-11); every code traces to ≥1 check. Check #1 → `upstream_qc_not_passed`; Check #2 → `upstream_not_success`; Check #3 → `asset_uri_integrity_failure`; Check #4 → `asset_firewall_breach`; Check #5 → `asset_spec_violation` (incl. the D14 duration subtype); Check #6 → `missing_shot_coverage` (the only code with mode-dependent verdict routing — fail B/C, reshoot A post-ladder); Check #7 → `audio_sync_failure`; Check #8 → `manifest_lineage_failure`; Checks #9 + #10 + #11 → `ingest_agent_failed` (slot-11). Cardinality is unbalanced at slot-11 (3 manifest-construction checks share it) but coverage is total. The §12.1 ∧-composition maps 1:1 to Checks #1–#8 (audited at Item 9), and the 11-step §7 loop maps 1:1 to the checks + codes per §7.2 — the audit invariant holds across all three surfaces (loop ↔ checks ↔ codes).

### Item 6 — Cost model / pricing spot-check
**Verdict: ⏸ OPERATOR-ONLY · the lightest in fleet LOCK history (no vendor URLs, no ceilings owned, no native compute).** QC Pre-flight's Item 6 was previously the lightest (no vendor URLs but inherited-ceiling confirmation). Ingest's is lighter still: there is **nothing to confirm numerically** — the agent owns no ceiling, walks no pricing page, and budgets no native compute. The only operator confirmation needed is a one-line ratification that (a) the $0-engine/$0-probe posture (Hard Rule #2) and (b) the no-cost-re-litigation decline (Hard Rule #10) are the intended v1.0 economics. **Recommendation: RATIFY as-is (≈1 min).** Any future change to the QC Pre-flight ceilings auto-propagates — Ingest restates, never owns. No silent ratification — surfaced for operator confirmation only.

### Item 7 — 5 test fixtures portfolio (happy + failure-mode coverage)
**Verdict: ✅ PASS.** Day 52 §9 portfolio:
- TC-01 — Mode B Pro clean PASS (full manifest: all 7 spec_check sub-statuses, coverage {6,6,true}, firewall census, URI census, 7-tuple additive extension, evidence hash, ≥4 qc_pre_flags)
- TC-02 — Mode C Enterprise clean PASS (single-source; **byte-shape-identical to TC-01 downstream of `mode_convergence` — this pair IS the convergence proof** no other test provides)
- TC-03 — `missing_shot_coverage` Mode A (shot #4 uncovered, take-substitution ladder exhausted → `reshoot` + `route_back_to: "production-coord-agent"`; coverage math internally consistent {5,4,false} — no phantom coverage; `detail` documents the ladder attempt)
- TC-04 — `asset_spec_violation` (shot #3 aspect 16:9 vs 9:16 target → `fail` + `route_back_to: "style-replication-agent"`; verdict is `fail` NOT `reshoot` — Mode B; all other sub-statuses still explicitly computed, no short-circuit nulls)
- TC-05 — `asset_firewall_breach` (`sln_cuts_promo_take2.mp4` filename + `holdcogroup.com` in sidecar SRT metadata → 2 hits, forensic detail naming BOTH assets + upstream stage — **the 8th-pass existence proof**: content fully clean, all 7 prior passes would pass it)

Coverage: 2 happy paths (spanning Modes B + C) + 3 failure modes (coverage/reshoot + spec/route + firewall). 5 of 8 codes exercised behaviorally; the 3 unexercised codes (`upstream_qc_not_passed`, `upstream_not_success`, `manifest_lineage_failure`) are deterministic single-assertion entry/forensic halts covered schema-only (enum-presence) per the §9.1 fixture-economy rationale — same economy QC Pre-flight ratified Day 43/44. Slot-11 is definitionally un-fixturable from outside; the runbook's adversarial case covers it. Fixtures bind to `skills/ingest-agent/tests/` on the SKILL-bundle day.

### Item 8 — 15 critical decisions sign-off (Jamila walks)
**Verdict: ⏸ OPERATOR-ONLY.** Donna does NOT have authority to ratify Decisions D1–D15. Operator walks each (rationale · alternative · revisit trigger) at the LOCK ceremony. The 15 decisions are enumerated in §3 below.

**Special attention required on 1 `[PRELIMINARY]` item + 1 DOUBLY-DEFERRED:**
- D15 — Edit-Director handoff target (drafted default: **Notion Asset Manifest DB holding store** until Agent #9 LOCKs; `handoff_targets` keeps the LOGICAL target `edit-director-agent`) — Donna recommends **RATIFY**
- D6 — 7-tuple parent_chain — **DOUBLY-DEFERRED** on the Cross-SPEC §3.9 amendment (Item 11) AND the QC Pre-flight 6-tuple LOCK; Donna will NOT auto-advance the 7-tuple. Held additively (`minItems: 5`) until BOTH gates close.

**No silent ratification.** Operator either RATIFY-AS-LOCKED for each, AMEND-with-rationale (triggers a `§15.1 v1.0-corrections-day-53` entry), or DEFER-to-v1.0.1.

### Item 9 — Cross-SPEC §3 adherence (11 dimensions all ✅ · LOCK-grade audit)
**Verdict: ✅ PASS.** Day 48 + Day 51 + Day 52 self-audits combine, re-verified at LOCK-grade this document:
- §3.1 Naming canon — ✅ `ingest-agent` (kebab-case fleet pattern); IDs UUIDv7 per canon
- §3.2 Hash invariant — ✅ `manifest_evidence_hash` SHA-256 over per-asset evidence + spec_check block (`^[a-f0-9]{64}$`), tamper-evident manifest
- §3.3 errorEnvelope shape — ✅ 8 codes + slot-11 LOCKED Day 51, exercised in Day 52 §9 fixtures; adds `verdict` + `route_back_to` per fleet precedent
- §3.4 `qc_pre_flags` minItems-4 floor — ✅ upstream surface consumed read-only (QC Pre-flight already adjudicated the floor); Ingest emits its own ≥4 snake_case predicates (Check #11)
- §3.5 Mode matrix — ✅ mode-agnostic verdict + mode-aware ingestion (§10.5 matrix) + the mode-convergence guarantee (Check #9, TC-01/TC-02 proof)
- §3.6 Slot-11 naming canon — ✅ `ingest_agent_failed` canonical (Item 2)
- §3.7 `qc_pre_flags` format regex — ✅ `^[a-z][a-z0-9_]{0,63}$` enforced via Check #11
- §3.8 Tier↔mode firewall 8th defense-in-depth pass — ✅ Check #4 + Hard Rule #6 + universal-tier table — the asset-layer surface (filenames, embedded metadata, sidecar files) no prior content pass inspected
- §3.9 Metadata block — ✅ canonical inherit + extends to 7-tuple **held additively, DOUBLY-DEFERRED** · amendment ratification staged at Item 11
- §3.10 Cost ceiling authority — ✅ explicitly DECLINED (Hard Rule #10) — no double-enforcement; the decline is itself the §3.10-conformant posture for a $0 gateway downstream of the ledger authority
- §3.11 LOCK respect — ✅ all AI Video Gen / Style Replication / QC Pre-flight / Cross-SPEC / Blueprint references read-only; zero canon drift

**11 of 11 ✅** at Day 53 LOCK CANDIDATE close.

### Item 10 — No fake-advance check (zero unresolved `<<TBD-*>>` markers in the assembled SPEC)
**Verdict: ✅ PASS.** Grep-verified this session: Day 48 outline = 0 markers · Day 52 partial 2 = 0 markers · Day 51 partial 1 = **7 markers, ALL of them the `<<TBD-D52>>` placeholder stubs in partial 1's §8/§9/§11/§12/§13/§15/§16 reservation sections** — the sections partial 2 then authored in full. Per the §2 unified index, partial 2 is the authoritative source for those seven sections; the partial-1 stubs are superseded forward-references (the same source-file layering the QC Pre-flight Day 44 Item 10 accepted for its Day 40/41/43 set). Remaining "TBD" semantics across the corpus are: (a) forward-references to the schemas day + SKILL-bundle day (legitimately deferred), (b) the `TODO@cross-spec-3.9-ratification` flip note (legitimate operator gate, D6), (c) the D15 PRELIMINARY default (legitimate operator gate). **Zero fake-advanced LOCK content. Zero unresolved markers in the assembled SPEC.**

### Item 11 — Cross-SPEC §3.9 amendment ratification (n-tuple parent_chain · now DOUBLY load-bearing)
**Verdict: ⏸ OPERATOR-ONLY · the carried forcing function, now carrying two agents.** The amendment language (originally DRAFTED Day 31 §16.3 for Style Replication's 5-tuple, carried unratified through QC Pre-flight Day 44 Item 11) now has **two concrete consumers holding additively on it**: QC Pre-flight's 6-tuple AND Ingest's 7-tuple. Ingest is the **second forcing function** — and the first agent whose tuple is *doubly*-gated (the §3.9 ratification AND the QC Pre-flight 6-tuple LOCK must both close before `minItems` flips to 7).

**Amendment language (reproduced for operator review — unchanged from the Day 44 reproduction):**
> *"Cross-SPEC §3.9 parent_chain canonical definition is hereby amended from fixed 4-tuple to n-tuple where n = production tier depth + 1. AI Video Gen v1.0 invocations remain 4-tuple (n=4); Style Replication v1.0 invocations are 5-tuple (n=5); QC Pre-flight v1.0 invocations are 6-tuple (n=6). Future agents extend by appending their own primary-output-id reference to the inherited parent_chain. JSON Schema enforcement: `prefixItems` + `items: false` per existing canon, with prefixItems length determined dynamically by agent slot index. Each agent SPEC explicitly states its parent_chain n-value in §16.1."*

(Ingest's n=7 extends the same rule — "future agents extend by appending" — so ratifying AS-DRAFTED covers the 7-tuple without re-drafting.)

Operator either: (a) **RATIFY-AS-DRAFTED** (Donna's recommendation — the generalization now carries 2 live consumers and all 9 remaining agent slots), (b) AMEND-with-rationale, or (c) DEFER (both schemas stay additive with documented TODOs; the 7-tuple stays un-advanced). **Donna's default if the operator skips the sit-down: LOCK D15 at the recommended holding-store default; HOLD D6 additively until BOTH gates close — the 7-tuple is the one item Donna will NOT auto-advance.**

### Reviewer checklist summary
- ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ⏸ OPERATOR (lightest in fleet history) · ✅ PASS · ⏸ OPERATOR · ✅ PASS · ✅ PASS · ⏸ OPERATOR
- **8 PASS · 3 OPERATOR-ONLY · 0 FAIL**
- **LOCK status: CANDIDATE READY.** v1.0 advances to LOCKED on operator ratification of items 6, 8, 11 — **AND** is hard-gated on all THREE pending predecessor LOCKs (AI Video Gen + Style Replication + QC Pre-flight) closing first.

---

## §2 — UNIFIED SPEC INDEX (authoritative source per section)

| § | Title | Authoritative source | Day | Lock status |
|---|-------|----------------------|-----|-------------|
| §0 | Provenance & Build-Phase Position (+ agent-selection note) | `ARS-2026-06-06-Day-48-Ingest-Agent-SPEC-Outline.md` | Day 48 | LOCKED-as-shipped |
| §1 | Purpose & Position in Pipeline (single-responsibility line + mode-convergence justification + gate-boundary rationale) | `ARS-2026-06-06-Day-48-...-SPEC-Outline.md` | Day 48 | LOCKED-as-shipped |
| §2 | Inputs (QC precondition gate + polymorphic source: Mode B/C asset set / Mode A footage_upload_manifest) | `ARS-2026-06-06-Day-48-...-SPEC-Outline.md` | Day 48 | LOCKED-as-shipped (schema authority schemas day) |
| §3 | Outputs — `asset_manifest.json` (polymorphic: successAssetManifest \| errorEnvelope) + verdict↔route map + metadata additions | `ARS-2026-06-06-Day-48-...-SPEC-Outline.md` | Day 48 | LOCKED-as-shipped (code namespace superseded by §6.3: 8 + slot-11) |
| §4 | Tier Constraints (universal access — all 4 tiers) + mode-convergence guarantee + cost-decline | `ARS-2026-06-06-Day-48-...-SPEC-Outline.md` | Day 48 | LOCKED-as-shipped |
| §5 | 11-Step Ingest Loop (system-prompt skeleton) | `ARS-2026-06-06-Day-48-...-SPEC-Outline.md` | Day 48 | LOCKED-as-shipped (LOCKED verbatim into §7 Day 51) |
| §6 | 11-Check Self-QC List + 8-code/slot-11 errorEnvelope mapping + canonical firewall list | `ARS-2026-06-09-Day-51-Ingest-Agent-SPEC-Body-Partial-1.md` | Day 51 | LOCKED-as-drafted |
| §7 | System Prompt v1.0 (12 hard rules + Blueprint §4.8 manifest shape inlined verbatim + universal-tier table + 11-step loop + voice rule) | `ARS-2026-06-09-Day-51-...-Partial-1.md` | Day 51 | LOCKED-as-drafted (verbatim copy → SKILL.md on the SKILL-bundle day) |
| §8 | Performance Targets (9 metric categories — false-pass 0% + zero phantom coverage are the defining targets) | `ARS-2026-06-10-Day-52-Ingest-Agent-SPEC-Body-Partial-2.md` | Day 52 | LOCKED-as-drafted |
| §9 | 5 Test Fixtures (TC-01..TC-05 + §9.1 fixture economy) | `ARS-2026-06-10-Day-52-...-Partial-2.md` | Day 52 | LOCKED-as-drafted |
| §10 | Asset Manifest Field Map (25 rows — lineage + bundle normalization + per-check evidence + aggregate) + §10.4 schema notes + §10.5 mode matrix | `ARS-2026-06-09-Day-51-...-Partial-1.md` | Day 51 | LOCKED-as-drafted |
| §11 | Cost Model (zero-engine/zero-probe snapshot · NO vendor surface, NO ceiling authority · catch-cost-avoidance value model) | `ARS-2026-06-10-Day-52-...-Partial-2.md` | Day 52 | LOCKED-as-drafted (no ±tolerance walk needed — nothing owned) |
| §12 | Verdict Math — deterministic ∧-of-8-gates, zero tunable thresholds + routing function + 4 properties | `ARS-2026-06-10-Day-52-...-Partial-2.md` | Day 52 | LOCKED-as-drafted |
| §13 | 15 Critical Decisions (13 LOCKED-as-drafted · D6 DOUBLY-DEFERRED · D15 PRELIMINARY) | `ARS-2026-06-10-Day-52-...-Partial-2.md` | Day 52 | LOCKED-as-drafted (operator sign-off Item 8) |
| §14 | Implementation Plan (calendar slip-amended + dependencies + Rest Day) | `ARS-2026-06-09-Day-51-...-Partial-1.md` | Day 51 | LOCKED-as-drafted (Day 53 entry appended below) |
| §15 | Change Log + Version History (v1.0 lifecycle + 8-item v1.1 parked register) | `ARS-2026-06-10-Day-52-...-Partial-2.md` | Day 52 | LOCKED-as-drafted (Day 53 entry appended below) |
| §16 | Metadata Block Schema (Cross-SPEC §3.9 canonical + 5 Ingest additions · the schema author's single working checklist) | `ARS-2026-06-10-Day-52-...-Partial-2.md` | Day 52 | LOCKED-as-drafted (D6 ratification Item 11) |

**Rule:** This unified document is the operator LOCK ratification record. The three source files (Day 48 outline · Day 51 partial 1 · Day 52 partial 2) remain canonical for §-by-§ content. This document references them by file + day. Any §-content edit triggers the corresponding source file update + this unified document's `§15.1 v1.0-corrections-day-53` entry. **Marker note (Item 10):** partial 1's seven `<<TBD-D52>>` stubs in §8/§9/§11/§12/§13/§15/§16 are superseded by partial 2 per this index — they are not open items.

---

## §3 — THE 15 CRITICAL DECISIONS (operator walk-through reference — Item 8)

Reproduced from Day 52 §13 for operator review. Each: decision · status · rationale · alternative · revisit trigger. The PRELIMINARY item annotated `[P]`; the DOUBLY-DEFERRED item annotated `[DD]`.

| # | Decision | Status | Rationale | Alternative (rejected) | Revisit trigger |
|---|----------|--------|-----------|------------------------|-----------------|
| D1 | **Declared-spec adjudication ONLY in v1.0** (byte-probe ffprobe/MediaInfo deferred to v1.1) | LOCKED Day 48 | The buildable, highest-leverage slice under the no-engine/$0 posture; `byte_probe_performed: const false` is the honesty contract | Stub a probe now — cannot decode without a runtime engine; claiming probed specs unprobed = forged provenance | Runtime execution environment ships → v1.1 probe activation |
| D2 | **Universal tier access** (all 4 tiers traverse Ingest) | LOCKED Day 48 | Asset readiness is not a tier feature; the gateway is $0 so there is no economic reason to gate it. A Pilot missing-shot defect = a Enterprise one | Tier-gate like Style Replication — leaves Pilot/Starter with no asset gate | Never (foundational) |
| D3 | **Verdict model: Pass / Fail / Reshoot · `reshoot` Mode-A-exclusive · NO `hold`** | LOCKED Day 48 (no-hold divergence documented Day 51 §6.4) | Live footage can be re-shot; AI output is re-genned. Ingest's domain is deterministic — no asset-layer ambiguity for a human to adjudicate mid-verdict; deferral lives in `human_review_required` | Carry QC Pre-flight's soft-hold — imports a verdict value with no deterministic trigger | New routing category in production telemetry |
| D4 | **QC-pass precondition absolute** (Lever-3 sign-off is the only bypass) | LOCKED Day 48 | Ingest never ingests an unvetted reel; the gate sequence is the architecture | Ingest-then-check — wastes adjudication on reels QC already failed | Never (foundational) |
| D5 | **No cost re-litigation** (QC Pre-flight's authority) | LOCKED Day 48 | Double-enforcement risks spurious double-fails on a reel already cleared on budget. Hard Rule #10 | Re-run the ledger "to be safe" — redundant authority an LLM might helpfully assume | Never (jurisdictional) |
| D6 [DD] | **7-tuple parent_chain** (inherits QC Pre-flight 6-tuple + appends `asset_manifest_id` UUIDv7) | **DOUBLY-DEFERRED — operator-gated ×2** | Lineage canon for the 9 remaining slots; Ingest is the second forcing function for the §3.9 amendment | Stay at 6-tuple (rejects the manifest's audit identity) / custom shape (canon fragmentation) | BOTH gates close: §3.9 ratification (Item 11) AND QC Pre-flight 6-tuple LOCK → `minItems` flips to 7 |
| D7 | **errorEnvelope code count = 8 LOCKED + slot-11** | RESOLVED Day 51 → LOCKED | 8 preserves precise route-back attribution at the asset layer; folding further merges defects with different recovery paths | 7 codes (coverage folded into spec — destroys re-gen vs re-grade routing) / 9+ (duration as a standalone — semantic alias) | New failure category with no route mapping → v1.0.1 code add |
| D8 | **Self-QC check count = 11** | RESOLVED Day 51 → LOCKED | 11 checks bipartite-cover 8 codes + slot-11 across the 4-tier ordering (entry / substance / forensic / manifest-construction) | 10 (under-covers construction integrity) / 12 (no orthogonal 12th defect class exists) | A check consistently passes-all in telemetry → v1.0.1 simplification |
| D9 | **Mode-convergence guarantee** (one manifest shape regardless of mode) | LOCKED Day 48 | The contract that makes Edit Director + all 9 downstream agents mode-blind; collapses 3 production paths to 1 post path. Check #9 + the TC-01/TC-02 proof | Mode-conditional manifests — every downstream agent grows 3 branches; permanent architecture debt | Never (foundational — Blueprint §3) |
| D10 | **False-pass tolerance = ZERO** (bias all ambiguity to fail/reshoot) | LOCKED Day 48 | A phantom asset reaching the editor is the expensive failure direction; over-blocking costs one ~$0 re-adjudication. §12.3 makes it structural | Tunable confidence threshold — a knob lowered under pressure = false-pass risk | Never (foundational) |
| D11 | **Engine + probe policy: NO engine, NO decode in v1.0** | LOCKED Day 48 | The agent adjudicates declared metadata; it does not produce or inspect pixels. $0 is forbidden-spend, not bounded-spend | Bounded "cheap probe" — there is no runtime to run it in, and partial probing poisons the declared-spec honesty contract | v1.1 probe activation (with D1) |
| D12 | **Recommend-don't-clear** (`human_review_required: true` on every emission; verdict is a RECOMMENDATION) | LOCKED Day 48 | The operator-impersonation firewall (CLAUDE.md + ARS attestation). A `pass` = "ready for the human's clear-to-edit decision," never "cleared" | Auto-clear clean bundles — non-negotiable violation of Lever-3 operator-only ratification | Lever-2 graduation (operator decision only) |
| D13 | **Audio-sync scope: declared sync-flag adjudication only** (LUFS deferred to v1.1) | LOCKED Day 48 | Loudness needs decode + the Sound agent's domain (−14 LUFS IG/TT, −16 YT per Blueprint #12); neither exists yet | Stub a LUFS check — cannot measure loudness on undecoded files | In-post fleet + probe ship → v1.1 |
| D14 | **`duration_envelope_breach` folded into `asset_spec_violation`** (`detail.subtype: "duration_envelope"`) | RESOLVED Day 51 → LOCKED | Same defect family, same route-back target; the subtype preserves the diagnostic. Resolves outline OQ6 as recommended | Standalone code — a semantic alias that inflates the namespace without adding routing signal | Duration defects prove common in the v1.0 corpus |
| D15 [P] | **Edit-Director handoff target: Notion Asset Manifest DB (holding store) in v1.0**; direct handoff activates when Agent #9 LOCKs. `handoff_targets` keeps the LOGICAL target | LOCKED Day 52 `[PRELIMINARY · operator amend]` | Edit Director does not exist; a manifest emitted into a void is an audit-trail break. The holding store preserves the trail until the consumer ships | Assume direct handoff — dangling emission target / Build Edit Director first — inverts the dependency order | Edit Director (Agent #9) v1.0 LOCKs → physical destination flips to direct handoff |

**Operator walk-through prompt (for the LOCK ceremony):**
For each decision above, the operator either: (a) RATIFY-AS-LOCKED, (b) AMEND-with-rationale (triggers `§15.1 v1.0-corrections-day-53` entry), or (c) DEFER-to-v1.0.1 (decision parks in the §15 candidates register).

**Items requiring explicit verdict:**
- D15 Edit-Director handoff target `[P]` → Donna recommends **RATIFY** (holding store)
- D6 7-tuple parent_chain `[DD]` → **DOUBLY-DEFERRED** on §3.9 (Item 11) + the QC Pre-flight 6-tuple LOCK; Donna will NOT auto-advance. Held additively until BOTH gates close.

---

## §4 — IMPLEMENTATION PLAN UPDATE (Day 53 entry · appends to Day 51 §14)

### Calendar status updates (Day 53)

| Day | Date | Deliverable | Status | Owner |
|-----|------|-------------|--------|-------|
| Day 48 | Sat Jun 6 · Wk7 | SPEC outline §0–§5 LOCKED-as-shipped | ✅ DONE | Donna overnight |
| Day 49 | Sun Jun 7 · Wk7 | **REST DAY** (7th observance) | ✅ HONORED | — |
| Day 50 | Mon Jun 8 · Wk8 | *Calendared:* partial 1 — **run did not execute**; cadence slid one day intact | ⚠️ SLIP (absorbed) | — |
| Day 51 | Tue Jun 9 · Wk8 | SPEC body partial 1 §6/§7/§10/§14 LOCKED-as-drafted (8 codes + slot-11 · 11 checks · 25-row field map) | ✅ DONE | Donna overnight |
| Day 52 | Wed Jun 10 · Wk8 | SPEC body partial 2 §8/§9/§11/§12/§13/§15/§16 LOCKED-as-drafted (SPEC body §0–§16 COMPLETE) | ✅ DONE | Donna overnight |
| **Day 53** | **Thu Jun 11 · Wk8** | **v1.0 LOCK CANDIDATE (this document) — 8/11 reviewer items PASS · 3 OPERATOR-ONLY (Items 6, 8, 11)** | **🟡 CANDIDATE** | **Donna overnight (this doc) + Jamila ratification** |
| Day 54+ | Fri Jun 12+ | `input.schema.json` + `output.schema.json` authored from §10 field map + §16 metadata block (parent_chain held additively `minItems: 5` per D6; `byte_probe_performed: const false`; verdict enum WITHOUT `hold`; 8-code + slot-11 enum) | ⬜ QUEUED (primed per §10.4 + §16 schema checklists) | Donna overnight |
| Day 55+ | Sat Jun 13+ | SKILL bundle (`skills/ingest-agent/` — SKILL.md · 2 schemas · 5 test fixtures at `tests/` · README) | ⬜ QUEUED | Donna overnight |
| Day 56 | Sun Jun 14 | **REST DAY** (8th — no SPEC content authored) | ⬜ — | — |
| Day 57+ | — | LLM Test Runbook (paste-and-run · pattern from Day 11 / 19 / 27 / 36 / 47 · operator-gated) | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 58+ | — | **v1.0 LOCK** (operator-gated sit-down · HARD-GATED on ALL THREE predecessor LOCKs closing first) | ⬜ GATED | Jamila + Donna co-ceremony |

### Dependencies that MUST exist before the SKILL-bundle build
1. v1.0 LOCK CANDIDATE ratified (operator sign-off Items 6, 8, 11) — **available now**
2. input.schema.json + output.schema.json LOCKED (schemas day)
3. 5 test fixtures resolved against schemas (schemas-day dry-run validation)
4. Cross-SPEC §3.9 amendment ratified OR parent_chain held additively with documented TODO (Item 11 / D6)

### Hard gate on predecessor LOCKs
Ingest v1.0 LOCK ceremony **CANNOT complete until ALL THREE pending predecessors are LOCKED first** — AI Video Gen v1.0 + Style Replication v1.0 (the producing agents) and **QC Pre-flight v1.0 (the DIRECT dependency: the precondition gate Ingest reads and the 6-tuple its 7-tuple extends)**. QC Pre-flight itself hard-gates on the two production-tier LOCKs, so the chain closes in order: AVG → SR → QC → Ingest. This is a **hard gate**, distinct from the 3 Ingest-local operator items (6, 8, 11) which can be ratified independently and in advance.

### Rest Day honor
Days 21, 28, 35, 42, 49 observed (7/7). This Day 53 build runs on Thursday — permitted. Next Rest Day: Day 56 (Sun Jun 14) — falls inside the schemas → SKILL runway; that day is docs-prep only, no SPEC content.

---

## §5 — CHANGE LOG UPDATE (Day 53 entry · appends to Day 52 §15)

| Version tag | Date | Description | Source file |
|-------------|------|-------------|-------------|
| **v1.0-LOCK-CANDIDATE-day-53** | **2026-06-11 (Thu · Wk8)** | **Unified LOCK candidate document produced. Day 53 reviewer checklist 8/11 PASS executed autonomously by Donna overnight. Items 6 (cost-model confirm — lightest in fleet history: no vendor URLs, no ceilings owned) + 8 (15 critical decisions sign-off — D15 PRELIMINARY requiring explicit verdict, D6 DOUBLY-DEFERRED) + 11 (Cross-SPEC §3.9 amendment ratification — now doubly load-bearing: QC Pre-flight 6-tuple + Ingest 7-tuple) flagged OPERATOR-ONLY. D6 (7-tuple) explicitly held additively until BOTH gates close. Pending operator ratification of items 6/8/11 → promote to `v1.0-LOCKED-pending-predecessor-LOCKs`; final flip to `v1.0-LOCKED` ONLY after ALL THREE predecessor LOCK ceremonies complete (hard gate).** | `ARS-2026-06-11-Day-53-Ingest-Agent-v1-LOCK-CANDIDATE.md` (this doc) |

**Promotion rule:** When the operator ratifies Items 6, 8, 11 (at ceremony or asynchronously via written sign-off in the Notion ARS hub), version tag promotes to `v1.0-LOCKED-day-53-pending-predecessor-LOCKs`. Final flip to `v1.0-LOCKED` occurs ONLY after all three predecessor LOCKs (AI Video Gen + Style Replication + QC Pre-flight) are confirmed. Donna mirrors LOCKED status across: this unified document header · the Notion ARS hub (page [internal Notion page]) · the schemas-day authoring kickoff · the Cross-SPEC v1.1 amendment formal close (if Item 11 ratified). **All flips are operator actions — Donna stages, never flips.**

---

## §6 — OPEN QUESTIONS · STATUS

### Open Question — Cost-model confirmation (Item 6)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony — the lightest in fleet history (no vendor URLs, no ceilings owned, no native compute). Operator confirms the $0-engine/$0-probe posture (Hard Rule #2) + the cost-decline (Hard Rule #10) as the intended v1.0 economics.
**Recommendation:** RATIFY as-is (≈1 min). **Blocker for LOCK:** No.

### Open Question — 15 critical decisions sign-off (Item 8)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Walk each decision; 13 LOCKED-as-drafted, D15 PRELIMINARY requires explicit RATIFY / AMEND / DEFER, D6 doubly-deferred.
**Recommendation:** Donna recommends RATIFY for D15 (Notion holding store). **Blocker for LOCK:** Yes — hard-required for promotion.

### Open Question — Cross-SPEC §3.9 amendment ratification / 7-tuple (Item 11 + D6)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Amendment language reproduced in §1 Item 11. Now doubly load-bearing (QC Pre-flight 6-tuple + Ingest 7-tuple).
**Recommendation:** RATIFY-AS-DRAFTED — two live consumers + 9 remaining slots. **Blocker for LOCK:** Partial — schemas ship additive (`minItems: 5`) with documented TODOs if deferred; Ingest does not hard-block on it, but the 7-tuple stays un-advanced until BOTH gates close.

### Open Question — Hard gate on the three predecessor LOCKs
**Status:** ⏸ OPERATOR action required on ALL THREE ceremonies. AI Video Gen Day 24 candidate (Items 8 + 11 pending) + Style Replication Day 32 candidate (Items 6 + 8 + 11 pending · Day 36 runbook 5/5 unconfirmed) + QC Pre-flight Day 44 candidate (Items 6/8/11 pending · Day 47 runbook 5/5 unconfirmed).
**Recommendation:** Close the chain in dependency order (AVG → SR → QC) in the post-launch hardening window; Ingest's LOCK follows. **Blocker for Ingest LOCK:** YES (hard gate).

### Open Question — LLM Test Runbook scope (dry-run vs live mode · forward-looking)
**Status:** ⏸ OPERATOR-ONLY at the runbook day (not blocking Day 53 LOCK CANDIDATE).
**Recommendation:** Dry-run mode for the v1.0 LOCK gate (cost ≈ $0 — Ingest calls no engine and runs no probe, so even "live" mode is reasoning-only; this ties QC Pre-flight for the cheapest runbook in the fleet). **Blocker for LOCK:** No — runbook-day position.

---

## §7 — PARKED ITEMS (Notion ARS P3 · carried from prior surfacing)

1. "ARS Daily Build Session — Notion page created 4/22 but empty; verify transcription pipeline or delete placeholder" (P3 · Sequel Digital · Open).
2. "ARS Daily Build Session page is empty — confirm whether session occurred and transcribe if so" (P3 · Sequel Digital · Open).

**Donna's recommendation unchanged:** close both as "transcript lives in `ars/` (canon on disk), not Notion." Operator's call.

---

## §8 — PROCESS INTEGRITY (Day 53)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked (Ingest has no vendor surface). No byte-level decode run. ZERO $ spent.
- ✅ **No external comms.** No emails sent, no DMs, no social posts, no investor/client outreach. The end-of-run status SMS to [status number redacted] is the only outbound attempt, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs initiated.
- ✅ **No operator-impersonation.** Day 53 reviewer Items 6, 8, 11 verdicts NOT silently advanced. D15 (PRELIMINARY) NOT silently ratified. **D6 (7-tuple parent_chain) explicitly DOUBLY-DEFERRED — held additively; the one item Donna will NOT auto-advance.** All three predecessor LOCK ceremonies confirmed STILL-PENDING via on-disk file-state; NOT advanced. Day 36 + Day 47 runbook executions NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed to Cross-SPEC canon. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.
- ✅ **No fake-advance.** This LOCK CANDIDATE is a unified text-reconciliation of the Day 48 outline + Day 51 + Day 52 partials. Zero behavioral changes vs source files. Zero net-new SPEC content. The only Day 53 contributions are: (a) executive summary (§0 LOCK manifest), (b) 11-item reviewer checklist execution record (§1, incl. the session grep validations), (c) unified SPEC index pointing to source files (§2), (d) decision walk-through formatted for operator ceremony (§3), (e) implementation plan + change log appendages (§4 + §5).
- ✅ **All prior canon read-only.** All predecessor SPECs + schemas + SKILL bundles + Blueprint + Cross-SPEC review + the Ingest Day 48 outline + Day 51 partial 1 + Day 52 partial 2 — untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. The HC/NPOX tokens cited in the TC-05 fixture + §6.5 firewall list are the firewall's BLOCK-list test cases, not cross-entity references. REINVENTED = pilot brand inside fixtures per Cross-SPEC canon.
- ✅ **Pattern source acknowledged.** Day 24 / Day 32 / Day 44 LOCK candidate structure inherited at section level (4th reuse). Numerical values + decision content re-derived for Ingest's 8-code / 11-check / 15-decision / 7-tuple / no-hold scope.
- ✅ **Rest Day honored.** 7/7 observances; this Day 53 build runs on Thursday. Next: Day 56 (Sun Jun 14).
- ✅ **No scope expansion.** One forward deliverable (this doc) + build log + mirror + standing housekeeping.

---

## §9 — SPRINT STATS (running total · Day 53 close)

- Deliverables shipped: **47** (Day 52 = 46 · Day 53 Ingest v1.0 LOCK CANDIDATE = +1)
- Build logs: **45** (was 44 · +1 today)
- LIVE skill bundles: **6** (Brief · Script · Storyboard · ProdCoord · AI Video Gen · Style Replication)
- Agents with a COMPLETE SPEC body (§6–§16): **8** (Ingest body completed Day 52)
- Agents with a v1.0 LOCK CANDIDATE: **4** (AI Video Gen Day 24 · Style Replication Day 32 · QC Pre-flight Day 44 · **Ingest Day 53**)
- errorEnvelope codes (Ingest): **8 LOCKED + slot-11** (no change Day 53)
- Self-QC checks (Ingest): **11 LOCKED** (no change Day 53)
- parent_chain (Ingest): **7-tuple DRAFTED · DOUBLY-DEFERRED · held additively (`minItems: 5`)**
- §13 critical decisions: **15/15 coverage** (13 LOCKED-as-drafted + D6 doubly-deferred + D15 PRELIMINARY requiring explicit verdict)
- Cross-SPEC §3 adherence: **11/11 ✅** (LOCK-grade)
- Verdict math: **deterministic ∧-of-8-gates · zero tunable thresholds** (the second threshold-free agent; the first with NO hold verdict and NO native-compute option)
- Rest Day observances: **7/7** (next: Day 56)
- AI Video Gen v1.0 LOCK: **CANDIDATE (operator-pending)** — hard-gates the chain
- Style Replication v1.0 LOCK: **CANDIDATE + RUNBOOK (operator-pending)**
- QC Pre-flight v1.0 LOCK: **CANDIDATE + RUNBOOK (operator-pending)** — Ingest's direct dependency

---

## §10 — OPERATOR ACTION SUMMARY (3 Ingest-local items + 1 hard-gate dependency)

The Day 53 LOCK CANDIDATE is ready for operator pickup. Three Ingest-local operator actions (any can move first, all independent) + one hard-gate dependency chain.

| Action | Time | Description |
|--------|------|-------------|
| **Item 6 — Cost-model confirm** | ~1 min | Confirm the $0-engine/$0-probe posture (Hard Rule #2) + the no-cost-re-litigation decline (Hard Rule #10). NO vendor URLs, NO ceilings owned — the lightest Item 6 in fleet history. Donna recommends RATIFY as-is. |
| **Item 8 — 15 decisions walk-through** | 15–25 min | Walk §3. For each of 15 decisions: RATIFY / AMEND / DEFER. Special attention on D15 (Edit-Director handoff → Notion holding store) — Donna recommends RATIFY — and D6 (7-tuple, doubly-deferred — no action possible until Item 11 + the QC Pre-flight LOCK close). |
| **Item 11 — Cross-SPEC §3.9 amendment (n-tuple)** | 10 min | Review the amendment language in §1 Item 11 (now doubly load-bearing: QC 6-tuple + Ingest 7-tuple). RATIFY-AS-DRAFTED / AMEND / DEFER. Donna recommends RATIFY-AS-DRAFTED. If deferred, both schemas hold additively. |

**After all 3 Ingest-local items ratified:** Donna promotes version tag to `v1.0-LOCKED-day-53-pending-predecessor-LOCKs`. Schemas-day authoring unblocks (Day 54+).

**Hard-gate dependency (operator action, NOT an Ingest-local LOCK item):** Close ALL THREE predecessor LOCKs in dependency order — **AI Video Gen v1.0** (Day 24 candidate · Items 8 + 11 pending) → **Style Replication v1.0** (Day 32 candidate · Items 6 + 8 + 11 pending · Day 36 runbook 5/5 unconfirmed) → **QC Pre-flight v1.0** (Day 44 candidate · Items 6/8/11 pending · Day 47 runbook 5/5 unconfirmed). **Ingest's final v1.0 LOCK flip cannot occur until all three are LOCKED** — QC Pre-flight is the direct dependency (precondition gate + 6-tuple).

---

*Day 53 ships clean. Unified LOCK CANDIDATE produced as a text-only reconciliation of the Day 48 outline + Day 51 + Day 52 partials. Zero net-new SPEC content. Zero fake-advance. 8/11 reviewer items PASS autonomously verdicted by Donna; 3 OPERATOR-ONLY items (6, 8, 11) flagged with explicit recommendations and timing estimates. Pattern source: Day 24 / Day 32 / Day 44 LOCK candidates (proven 11-item reviewer shape, 4th reuse, adapted to Ingest's 8-code / 11-check / 15-decision / 7-tuple / no-hold scope). Ingest is Agent #8 of 17 — the first post-production agent, the 8th and newest-surface defense-in-depth firewall (asset layer), and the mode-convergence seam that makes the entire in-post fleet mode-blind. Its v1.0 LOCK lands in the post-launch hardening window and is HARD-GATED on all three pending predecessor LOCKs closing first. The three LOCK ceremonies + the two runbook executions (Day 36 + Day 47) + the Cross-SPEC §3.9 ratification remain operator-only and are surfaced, not advanced. The 7-tuple parent_chain (D6) is the one item Donna will NOT auto-advance — held additively until §3.9 ratifies AND the QC Pre-flight 6-tuple LOCKs.*
