# ARS — Sound Agent v1.0 SPEC (UNIFIED · LOCK CANDIDATE · Day 78)

**Author:** Donna (overnight build session · Sequel Digital ARS sprint)
**Date:** 2026-07-06 (Mon · Day 78 · Wk12 · post-launch hardening window)
**Document status:** **v1.0 LOCK CANDIDATE — awaiting operator sign-off on items 6, 8, 11 + the SIX predecessor LOCKs (hard gate)**
**Lock signal:** Items 1–5, 7, 9, 10 of the Day 78 reviewer checklist are EXECUTED and PASS. Items 6, 8, 11 are operator-only.
**Predecessor LOCKs:** Brief Agent v1.0 (Day 6) · Script Agent v1.0 (Day 9) · Storyboard Agent v1.0 (Day 14) · Production Coord Agent v1.0 (Day 14) · Cross-SPEC Canon (Day 12) · **AI Video Gen v1.0 LOCK CANDIDATE (Day 24 — operator-gated; STILL PENDING) · Style Replication v1.0 LOCK CANDIDATE (Day 32 — operator-gated; STILL PENDING) · QC Pre-flight v1.0 LOCK CANDIDATE (Day 44 — operator-gated; STILL PENDING) · Ingest v1.0 LOCK CANDIDATE (Day 53 — operator-gated; STILL PENDING) · Edit Director v1.0 LOCK CANDIDATE (Day 61 — operator-gated; STILL PENDING) · Editor v1.0 LOCK CANDIDATE (Day 69 — operator-gated; STILL PENDING)**
**Hard gate on predecessor LOCKs:** Sound's v1.0 LOCK ceremony CANNOT complete until **all six** pending predecessors LOCK first — AI Video Gen + Style Replication (the producing agents) + QC Pre-flight + Ingest + Edit Director + **Editor in particular (Sound's DIRECT dependency: the `successEdl`/`edl_ready` precondition gate Sound reads, and the 9-tuple parent_chain the 10-tuple extends)**. This LOCK CANDIDATE is authored on LOCK-stable **text artifacts** (the SPEC sections as drafted Days 74–76); it uses **zero production output** from any predecessor, **zero render or DSP of any media**, **zero waveform decode**, and **zero engine dispatch**. Forward-design under the same posture as the Day 74 outline + both body partials.
**Position note:** Agent #11 of 17 — the **second faithful-executor agent** in the post tail (it FINISHES the audio on the cut Editor conformed; it makes no creative call and re-litigates nothing upstream), the **11th defense-in-depth firewall** pass (the audio-domain VO-transcript re-scan — the last audio checkpoint before Motion typography), the **first agent whose output is a finished-audio spec destined for the `v2.mp4`** (drafted as an audio conform spec the human mixes in v1.0), and the **third contractually mode-blind agent** (the live, machine-checkable proof that Ingest's mode-convergence seam holds end-to-end THREE stages deep: Edit Director → Editor → Sound). Its v1.0 LOCK lands inside the post-launch hardening window and does **NOT** gate the commercial launch (which shipped on the six built production agents through the QC Pre-flight gate). The Agent-#11-slot selection (Donna, Day 74 — surfaced, not hidden) remains operator-confirmable at the Editor LOCK-ceremony close.

---

## §0 — LOCK MANIFEST (executive summary)

| Item | Status |
|------|--------|
| SPEC sections drafted | **17 / 17** (§0–§16 — outline §0–§5 Day 74 · body §6/§7/§10/§14 Day 75 · body §8/§9/§11/§12/§13/§15/§16 Day 76) |
| `<<TBD-*>>` markers remaining in the ASSEMBLED SPEC | **0 unresolved** (the §6–§16 outline preview stubs were authored in full across the Day 75 + Day 76 partials; superseded forward-references, not open items. See Item 10.) |
| SPEC body completeness | **§6–§16 COMPLETE** (Day 75 + Day 76 partials fully cover the body; this LOCK CANDIDATE is a pure text-only reconciliation, zero net-new SPEC content) |
| Error code canonical count | **9 LOCKED + slot-11 catch-all** (Day 75 §6.3 — `upstream_edl_not_ready` · `upstream_not_success` · `vo_track_missing` · `audio_asset_unresolved` · `audio_marker_out_of_range` · `loudness_target_out_of_spec` · `spec_fidelity_breach` · `audio_firewall_breach` · `audio_lineage_failure` + `sound_agent_failed` slot-11). Settled at 9 within the outline's 7–9 target |
| Notable namespace decision | `vo_track_missing` and `audio_asset_unresolved` each kept **SPLIT** (the deliberate OPPOSITE of Editor folding all resolution into a single `asset_unresolved`) — the audio domain carries TWO distinct asset classes (VO voice track + music bed) whose operator recovery diagnostics differ even though both route to Ingest; `spec_fidelity_breach` is kept **FOLDED** (hash-tamper + duration + mix-directive deviation, all route-back to Editor → one code) (D8 / §6.3 cardinality rationale) |
| Slot-11 errorEnvelope name | `sound_agent_failed` (Cross-SPEC §3.6 conformant — agent_id `sound-agent` → snake_case; one canonical fallback per agent slot) |
| Self-QC check count | **11** (Day 75 §6.1 — entry-validation #1–2 · seven finish adjudications #3–9 · forensic #10 · construction-integrity #11) bipartite-covering the 9 codes + slot-11 |
| Verdict model | **`audio_ready` / `fail` — TWO verdicts only. The DEFINING DIVERGENCE: Sound deliberately does NOT inherit Edit Director's success-side third `revise` verdict — it inherits Editor's deterministic two-verdict posture.** Sound is a faithful executor, not a creative authority — a loudness target is the platform const or it isn't, a marker is in the timeline or it isn't, the VO transcript is byte-faithful or it isn't, the firewall is clean or it isn't. There is no subjective finish surface, so there is no judgment slot. Re-introducing `revise` would mean Sound was second-guessing a locked cut — the conform/finish override the boundary forbids. Human deferral lives in `human_review_required: true` + `finish_mode: human_in_the_loop` on EVERY emission, not in a verdict branch. (Mirror of Editor/Ingest determinism; documented Day 75 §6.3/§6.4 + Day 76 §12.) |
| Verdict math | **Fully-deterministic ∧-of-gates · ZERO tunable thresholds · NO `revise` branch** (Day 76 §12) — a pure conjunction with zero judgment slots. Two outcomes only (`audio_ready | fail`; halts a fail sub-class). 5 properties: fully-deterministic / monotone / **zero-false-audio-ready by construction** / NO-judgment-slot (the defining divergence) / auditable-recomputable |
| Cost authority | **NONE — deliberate decline** (Hard Rule #11). Sound does NOT re-litigate the cumulative cost ledger (QC Pre-flight's jurisdiction), re-validate assets (Ingest's jurisdiction), re-conform the cut (Editor's jurisdiction), or re-direct the mix intent (Edit Director's jurisdiction). The tier ceilings are upstream facts restated for traceability only |
| Self per-reel cost | **≈ $0.00** ($0.00 engine + $0.00 DSP + $0.00 waveform decode structurally guaranteed; `audio_processed: const false`; LLM reasoning ≈ $0.02–0.07 inside the latency envelope — lighter than Editor's authoring). Ties Ingest / QC Pre-flight / Edit Director / Editor for lowest-cost agent in the 17-agent fleet |
| Performance target portfolio | **9 metric categories** (Day 76 §8) — schema validity 100% · spec-fidelity catch 100% (a deviated music event / swell marker / timeline duration / byte-unfaithful VO transcript / tampered hash must NEVER survive) · audio-domain firewall catch 100% (11th pass) · marker-in-timeline + loudness-target-in-spec 100% · audio-asset resolution 100% · **false-audio-ready 0%** (the defining target) · **false-fail ≤5%** (tightened from the partial-1 ≤8% preview — a two-verdict-determinism consequence of D3; flagged for operator confirm at Item 11) · p50 latency 22s / p95 70s (lighter than Editor's 25s/75s) · $0 engine + $0 DSP |
| Test fixture portfolio | **5 fixtures** (Day 76 §9) — TC-01 clean Mode-A Pro `audio_ready` (full audio spec) · TC-02 Mode-C Enterprise `audio_ready` (**the TC-01/TC-02 pair = the mode-blind finish-convergence proof, three stages deep**: byte-shape-identical finish path despite different origin mode) · TC-03 `audio_marker_out_of_range` → fail + route Editor · TC-04 `vo_track_missing` → fail + route Ingest · TC-05 `audio_firewall_breach` (banned token in the passthrough VO transcript — **the 11th-pass last-audio catch · GATING**). 5 of 9 codes behavioral; the remaining deterministic halts + the `audio_asset_unresolved` music-bed variant + the `spec_fidelity_breach` hash-tamper variant schema-only / runbook (§9 fixture-economy). **Fixture-economy divergence: NO `revise` to exercise** (Sound carries no third verdict) |
| Cost model engine coverage | **ZERO generative engines + ZERO audio DSP + ZERO waveform decode + ZERO LUFS measurement** (by design — Hard Rule #3, `audio_processed: const false`). No external vendor-pricing URLs to walk AND no ceilings owned — Item 6 ties Ingest / Edit Director / Editor for the lightest operator spot-check in fleet LOCK history |
| Metadata block schema | **Cross-SPEC §3.9 canonical + 6 Sound additions** (`audio_spec_class` · `audio_spec_evidence_hash` · `audio_processed const false` · `finish_mode const human_in_the_loop` · `runtime_environment_class` · `audio_spec_id`) + the **mode-blind + finish-target root-level self-attestation blocks** + the 2-verdict enum encoded at the schema layer. `human_review_required: const true` schema-enforced (recommend-don't-process) |
| parent_chain | **10-tuple DRAFTED Day 75/76** (inherits Editor's 9-tuple lineage + appends own `audio_spec_id`, UUIDv7) — **QUINTUPLY-DEFERRED: gated on (a) operator ratification of the Cross-SPEC §3.9 n-tuple amendment, (b) the Editor 9-tuple LOCK, (c) the Edit Director 8-tuple LOCK behind it, (d) the Ingest 7-tuple LOCK behind that, AND (e) the QC Pre-flight 6-tuple LOCK behind that.** Schema holds additively (`minItems: 5`, `prefixItems` 0–9, `maxItems: 10`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. The one item Donna will NOT auto-advance |
| 15 Critical Decisions | **15/15 §13 coverage** — 11 LOCKED-as-drafted (D1–D6, D10–D13 Day 74 + D14 Day 76) + 2 RESOLVED Day 75 inside pre-approved target ranges → LOCKED-as-drafted (D8 code count = 9 / D9 self-QC count = 11) + **D7 (10-tuple) QUINTUPLY-DEFERRED + D15 (Motion handoff → Drive conform queue) `[PRELIMINARY · operator amend]`** |
| 13 Hard Rules (system prompt) | LOCKED verbatim Day 75 §7.1 — operator copy-paste-ready into the SKILL.md. Defining rules: #2 finish-faithfully-re-author-nothing · #3 author-an-audio-spec-process-no-waveform (the forged-provenance framing) · #7 mode-blind-by-inheritance (the convergence-payoff rule, now carried three stages deep) · #11 no cost/conform re-litigation · #13 "RECOMMEND, do not PROCESS" |
| Blueprint §4.11 Sound→Motion payload | Inlined VERBATIM into the §7 system prompt — the LLM is the runtime source of truth for the audio conform contract, not a side document (structural analog of Editor inlining §4.10 + Edit Director inlining §4.9 + Ingest inlining §4.8) |
| Field map | **24 rows** (Day 75 §10 — lineage / EDL-passthrough / mix-transform / VO-passthrough / per-check evidence / audio-spec aggregate, **ZERO authored copy rows** — Sound authors no spoken copy) + reserved `variant_masters[]` (D14 v1.1) + no-touch read-only references (incl. the `production_mode` non-read) |
| Cross-SPEC §3 audit | **11/11 dimensions ✅** at LOCK-grade (Item 9 — full audit executed this document) |
| Authoring decisions documented | All §13 walk decisions + the Day 76 key authoring decisions + the Day 74 agent-selection note — operator can ratify each at the LOCK walk-through |

---

## §1 — DAY 78 REVIEWER CHECKLIST · EXECUTION RECORD

The 11-item checklist mirrors the Day 24 AI Video Gen / Day 32 Style Replication / Day 44 QC Pre-flight / Day 53 Ingest / Day 61 Edit Director / Day 69 Editor LOCK candidate pattern (proven shape, **7th reuse**). Donna executed items 1–5, 7, 9, 10 autonomously overnight. Items 6, 8, 11 are operator-only.

### Item 1 — Error code count = 9 + slot-11 (verify exhaustive vs §6 11-check Self-QC list)
**Verdict: ✅ PASS.** Day 75 §6.3 mapping table enumerates all 9 codes + slot-11 catch-all with trigger-check mapping. The namespace settled at 9 within the outline §3.4 7–9 target. The defining cardinality call: `vo_track_missing` and `audio_asset_unresolved` are each kept **SPLIT** — the deliberate opposite of Editor folding all resolution into a single `asset_unresolved`. Sound splits where the recovery diagnostic differs: a missing VO voice track (`vo_track_missing`) and an unresolvable music bed (`audio_asset_unresolved`) both route to Ingest but demand different operator recovery actions (re-confirm the voice asset vs re-confirm the music-bed asset) — the audio domain's two distinct asset classes justify the split. `spec_fidelity_breach` is kept FOLDED (all three fidelity failures — hash-tamper, duration mismatch, mix-directive deviation — route to Editor → one code), so Sound folds where the route-back target is shared and splits where recovery diverges. Sound's 9 decompose into precondition (×2), resolution (×2 SPLIT), marker, loudness, fidelity (×1 folded), firewall, and lineage → 9 + slot-11. Bipartite coverage confirmed (Item 5 also passes).

### Item 2 — Slot-11 errorEnvelope name verification
**Verdict: ✅ PASS.** `sound_agent_failed` is the canonical slot-11 name in all OPERATIONAL positions (§6.1 Check #11, §6.3 mapping table, §7 Step 11 routing). Naming derives correctly per Cross-SPEC §3.6: agent_id `sound-agent` → snake_case → `sound_agent_failed`. No legacy fallback names (`editor_agent_failed`, `edit_director_agent_failed`, `ingest_agent_failed`, etc.) appear in the Sound source files — no orphan references. Cross-SPEC §3.6 canon fully respected.

### Item 3 — Cost model accuracy (zero-engine + zero-DSP + zero-decode · no vendor surface · no ceiling authority)
**Verdict: ✅ PASS · ties Ingest / Edit Director / Editor for the structurally simplest Item 3 in fleet history.** Day 76 §11 establishes Sound as a $0 agent with no external vendor-pricing surface (no engine), no audio DSP/render (`audio_processed: const false`), no waveform decode, no LUFS measurement (the loudness target is a DECLARED conform goal, not a measured value), and no ceiling ownership (Hard Rule #11 declines the cost-ledger authority QC Pre-flight holds). The complete cost model is: $0.00 engine (structurally banned) + $0.00 DSP (const false) + ≈$0.02–0.07 LLM reasoning (lighter than Editor's authoring) + $0.00 native compute. Total `cost_incurred_usd` ≈ $0.00 reported to 2dp per Cross-SPEC §3.9. The §11.2 faithful-finish value model declines dollar-ROI quantification (no live defect corpus exists pre-orchestrator; inventing one would be fake precision — formalization parked to v1.1). **No pricing URL walk is required for this agent.**

### Item 4 — Tier-table + cost-decline consistency (universal access + tier-FLAT behavior · no re-litigation)
**Verdict: ✅ PASS.** Cross-referenced across Day 74 + Day 75 + Day 76:
- Day 74 §1 + §4 universal-access / tier-FLAT tables — all 4 tiers traverse Sound at ~$0.00; Sound's own behavior does NOT scale by tier (it finishes whatever richness the EDL carries — a Pilot 6-beat EDL and an Enterprise 8-beat EDL run the identical executor logic). The divergence from Edit Director's tier-SENSITIVE richness, surfaced explicitly.
- Day 75 §7.1 universal-access tier-FLAT table (runtime authoritative) — "Cost ceilings are enforced UPSTREAM at QC Pre-flight — you carry none."
- Day 75 §10 finish-by-tier flatness matrix — every finish field/behavior identical across the four tiers (only the echoed `loudness_variants_planned` / `tier_richness_echo` flag count differs).
- Day 76 §8 targets-NOT-carried list — no cost-ceiling adherence metric (QC Pre-flight's authority).
All values and decline-statements consistent. No drift. **No operator-amend flag** — the ceilings are upstream inheritances restated verbatim; the tier-FLAT posture is D6 (LOCKED-as-drafted, walked at Item 8).

### Item 5 — Self-QC list ↔ 9 errorEnvelope codes + slot-11 bipartite coverage
**Verdict: ✅ PASS.** Day 75 §6.3 mapping table is bipartite: every one of the 11 self-QC checks resolves to a code (or the shared slot-11); every code traces to ≥1 check. Check #1 → `upstream_edl_not_ready`; Check #2 → `upstream_not_success`; Check #3 → `spec_fidelity_breach` (hash part) + `vo_track_missing` (VO-resolution part) + `audio_asset_unresolved` (music-resolution part — the one check mapping to three codes); Check #4 → `audio_marker_out_of_range` (+ `spec_fidelity_breach` duration part); Check #5 → `loudness_target_out_of_spec`; Check #6 → `spec_fidelity_breach` (mix-directive part — shared with Check #3/#4); Check #7 → `sound_agent_failed` (slot-11); Check #8 → `audio_firewall_breach`; Check #9 → `audio_marker_out_of_range` / `vo_track_missing` / `audio_asset_unresolved` (completeness, routed per cause); Check #10 → `audio_lineage_failure`; Check #11 → `sound_agent_failed` (slot-11). Cardinality is unbalanced at `spec_fidelity_breach` (Checks #3/#4/#6) and the two SPLIT resolution codes (Checks #3+#9) but coverage is total. The §12.1 ∧-composition maps 1:1 to the hard terms of Checks #1–#11, and the 11-step §7 loop maps 1:1 to the checks + codes — the audit invariant holds across all three surfaces (loop ↔ checks ↔ codes).

### Item 6 — Cost model / pricing spot-check
**Verdict: ⏸ OPERATOR-ONLY · ties Ingest / Edit Director / Editor for the lightest in fleet LOCK history (no vendor URLs, no ceilings owned, no native compute, no DSP, no decode).** There is **nothing to confirm numerically** — the agent owns no ceiling, walks no pricing page, dispatches no DSP, decodes no waveform, measures no LUFS, and budgets no native compute. The only operator confirmation needed is a one-line ratification that (a) the $0-engine/$0-DSP/$0-decode posture (Hard Rule #3, `audio_processed: const false`) and (b) the no-cost-re-litigation decline (Hard Rule #11) are the intended v1.0 economics. **Recommendation: RATIFY as-is (≈1 min).** Any future change to the QC Pre-flight ceilings auto-propagates — Sound restates, never owns. No silent ratification — surfaced for operator confirmation only.

### Item 7 — 5 test fixtures portfolio (happy + failure-mode coverage)
**Verdict: ✅ PASS.** Day 76 §9 portfolio:
- TC-01 — Mode-A-origin Pro clean `audio_ready` (full audio spec: loudness target −14 LUFS / −1.0 dBTP, VO polish authored to brand cadence, music bed bound + duck envelope with swells mapped from the EDL, SFX accents in-timeline, `audio_conform_check`, 5 `spec_fidelity_check` booleans, 11th-pass firewall census, 10-tuple additive extension, `audio_spec_evidence_hash`, `mode_blind_confirm`, `audio_processed: false`).
- TC-02 — Mode-C-origin Enterprise clean `audio_ready` (**byte-shape-identical finish path to TC-01 despite different origin — this pair IS the mode-blind finish-convergence proof, now three stages deep** — the payoff Ingest's mode-convergence seam unlocked, carried through the director, the executor, AND the finisher).
- TC-03 — `audio_marker_out_of_range` (an SFX/duck marker `at_ms` exceeds the EDL `total_timeline_ms` → `fail` + `route_back_to: "editor-agent"`; `detail` names the offending marker + the timeline bound; soft-recoverable, never silently clamped).
- TC-04 — `vo_track_missing` (the `asset_bundle.audio[]` voice track does not resolve → `fail` + `route_back_to: "ingest-agent"`; the SPLIT resolution code proven on the VO side; the music-bed `audio_asset_unresolved` variant named as the runbook probe).
- TC-05 — `audio_firewall_breach` (a banned-entity token in the passthrough VO transcript → forensic detail naming the leaking VO-transcript field — **the 11th-pass audio-domain existence proof · GATING**: the last net before the audio is mastered; content otherwise clean through Editor's 10th commit pass).

Coverage: 2 happy paths (spanning the finish-convergence proof) + 3 failure modes (the two route-backs Editor/Ingest + the GATING audio-firewall catch). 5 of 9 codes exercised behaviorally; slot-11 + the `audio_asset_unresolved`-music-bed + `spec_fidelity_breach`-hash/swell adversarial probes are exercised via the runbook (Day-79+ runbook position); remaining deterministic single-assertion halts (`upstream_edl_not_ready`, `upstream_not_success`, `loudness_target_out_of_spec`, `audio_lineage_failure`) covered schema-only per the §9 fixture-economy rationale — same economy Editor Day 68 + Ingest Day 53 + Edit Director Day 61 ratified. **Fixture-economy divergence from Edit Director: there is NO `revise` verdict to exercise** (Sound's two-verdict posture). Fixtures bind to `skills/sound-agent/tests/` on the SKILL-bundle day.

### Item 8 — 15 critical decisions sign-off (Jamila walks)
**Verdict: ⏸ OPERATOR-ONLY.** Donna does NOT have authority to ratify Decisions D1–D15. Operator walks each (rationale · alternative · revisit trigger) at the LOCK ceremony. The 15 decisions are enumerated in §3 below.

**Special attention required on 1 `[PRELIMINARY]` item + 1 QUINTUPLY-DEFERRED:**
- D15 — Motion handoff target (drafted default: **Drive `/reels/[reel_id]/` conform-queue holding store** until Agent #12 / Motion LOCKs; `handoff_targets` keeps the LOGICAL target `motion-agent`) — Donna recommends **RATIFY**. Directly tied to Editor Day 69 Item 8 (D15-of-Editor = the Sound handoff target — now the SAME handoff seam viewed one stage further downstream, resolved jointly).
- D7 — 10-tuple parent_chain — **QUINTUPLY-DEFERRED** on the Cross-SPEC §3.9 amendment (Item 11) AND the Editor 9-tuple LOCK AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC Pre-flight 6-tuple LOCK behind it; Donna will NOT auto-advance the 10-tuple. Held additively (`minItems: 5`) until ALL FIVE gates close.

**No silent ratification.** Operator either RATIFY-AS-LOCKED for each, AMEND-with-rationale (triggers a `§15.1 v1.0-corrections-day-78` entry), or DEFER-to-v1.0.1.

### Item 9 — Cross-SPEC §3 adherence (11 dimensions all ✅ · LOCK-grade audit)
**Verdict: ✅ PASS.** Day 74 + Day 75 + Day 76 self-audits combine, re-verified at LOCK-grade this document:
- §3.1 Naming canon — ✅ `sound-agent` (kebab-case fleet pattern, matches Blueprint §1.2 / §4.11 handoff target); IDs UUIDv7 per canon
- §3.2 Hash invariant — ✅ `audio_spec_evidence_hash` SHA-256 over the `audio_spec` + `audio_conform_check` + `spec_fidelity_check` block (`^[a-f0-9]{64}$`), tamper-evident finish
- §3.3 errorEnvelope shape — ✅ 9 codes + slot-11 LOCKED Day 75, exercised in Day 76 §9 fixtures; adds `verdict` + `route_back_to` per fleet precedent; verdict enum is exactly `["audio_ready", "fail"]` (NO `revise`)
- §3.4 `qc_pre_flags` minItems-4 floor — ✅ upstream surface consumed read-only; Sound emits its own ≥4 snake_case predicates (Check #11 — e.g. `loudness_target_in_spec`, `vo_track_resolved`, `audio_firewall_clean_pass_11`, `mode_blind_finished`)
- §3.5 Mode matrix — ✅ mode-BLIND by inheritance; §4 mode columns are identical (the third fleet agent for which that is true) + the `mode_blind_confirm.production_mode_read: false` self-attestation
- §3.6 Slot-11 naming canon — ✅ `sound_agent_failed` canonical (Item 2)
- §3.7 `qc_pre_flags` format regex — ✅ `^[a-z][a-z0-9_]{0,63}$` enforced via Check #11
- §3.8 Tier↔mode firewall 11th defense-in-depth pass — ✅ Check #8 over the passthrough VO transcript (the audio-finish surface) + Hard Rule #8 + §4 universal-access/tier-FLAT table
- §3.9 Metadata block — ✅ canonical inherit + extends to 10-tuple **held additively, QUINTUPLY-DEFERRED** · amendment ratification staged at Item 11 · mode-blind + finish-target self-attestation blocks added
- §3.10 Cost ceiling authority — ✅ explicitly DECLINED (Hard Rule #11) — no double-enforcement; the decline is the §3.10-conformant posture for a $0 executor agent four gates downstream of the ledger authority
- §3.11 LOCK respect — ✅ all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Cross-SPEC / Blueprint / Brand-Voice-Intake references read-only; zero canon drift

**11 of 11 ✅** at Day 78 LOCK CANDIDATE close.

### Item 10 — No fake-advance check (zero unresolved markers in the assembled SPEC)
**Verdict: ✅ PASS.** The §6–§16 LOCK-scope preview stubs in the Day 74 outline are forward-references to the partials; the Day 75 partial 1 authored §6/§7/§10/§14 in full and the Day 76 partial 2 authored §8/§9/§11/§12/§13/§15/§16 in full. Per the §2 unified index, the partials are the authoritative source for their sections; the outline preview lines are superseded forward-references (the same source-file layering the Editor Day 69 / Edit Director Day 61 / Ingest Day 53 Item 10 accepted). Remaining "TBD" semantics across the corpus are: (a) forward-references to the schemas day + SKILL-bundle day + runbook day (legitimately deferred), (b) the `TODO@cross-spec-3.9-ratification` flip note (legitimate operator gate, D7), (c) the D15 PRELIMINARY default (legitimate operator gate). **Zero fake-advanced LOCK content. Zero unresolved markers in the assembled SPEC.**

### Item 11 — Cross-SPEC §3.9 amendment ratification (n-tuple parent_chain · now QUINTUPLY load-bearing) + the §8.7 false-fail ≤5% tightening confirm
**Verdict: ⏸ OPERATOR-ONLY · the carried forcing function, now carrying five agents.** The amendment language (originally DRAFTED Day 31 §16.3 for Style Replication's 5-tuple, carried unratified through QC Pre-flight Day 44 / Ingest Day 53 / Edit Director Day 61 / Editor Day 69) now has **five concrete consumers holding additively on it**: QC Pre-flight's 6-tuple, Ingest's 7-tuple, Edit Director's 8-tuple, Editor's 9-tuple, AND Sound's 10-tuple. Sound is the **fifth forcing function** — and the first agent whose tuple is *quintuply*-gated (the §3.9 ratification AND the Editor 9-tuple LOCK AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK must all close before `minItems` flips to 10).

**Amendment language (reproduced for operator review — extended by Sound's n=10):**
> *"Cross-SPEC §3.9 parent_chain canonical definition is hereby amended from fixed 4-tuple to n-tuple where n = production tier depth + 1. AI Video Gen v1.0 invocations remain 4-tuple (n=4); Style Replication v1.0 invocations are 5-tuple (n=5); QC Pre-flight v1.0 invocations are 6-tuple (n=6); Ingest v1.0 invocations are 7-tuple (n=7); Edit Director v1.0 invocations are 8-tuple (n=8); Editor v1.0 invocations are 9-tuple (n=9); Sound v1.0 invocations are 10-tuple (n=10). Future agents extend by appending their own primary-output-id reference to the inherited parent_chain. JSON Schema enforcement: `prefixItems` + `items: false` per existing canon, with prefixItems length determined dynamically by agent slot index. Each agent SPEC explicitly states its parent_chain n-value in §16.1."*

(Sound's n=10 extends the same rule — "future agents extend by appending" — so ratifying AS-DRAFTED covers the 10-tuple without re-drafting.)

**Bundled confirm — the §8.7 false-fail ceiling tightening (NEW this LOCK candidate):** The Day 76 partial tightened Sound's false-fail ceiling from the partial-1 ≤8% preview to **≤5%** (Editor/Ingest-class, the deterministic-executor floor) — a direct consequence of D3's two-verdict determinism (the looser ≤8% band existed only to absorb Edit Director's one `revise` judgment surface; Sound holds NO subjective surface, so the ceiling tightens). This was surfaced as a flag-for-confirm, not silently committed over the preview. **Recommendation: CONFIRM ≤5%.**

Operator either: (a) **RATIFY-AS-DRAFTED** (Donna's recommendation — the generalization now carries 5 live consumers and all 6 remaining agent slots) + CONFIRM ≤5%, (b) AMEND-with-rationale, or (c) DEFER (all five schemas stay additive with documented TODOs; the 10-tuple stays un-advanced). **Donna's default if the operator skips the sit-down: LOCK D15 at the recommended holding-store default; HOLD D7 additively until ALL FIVE gates close — the 10-tuple is the one item Donna will NOT auto-advance.**

### Reviewer checklist summary
- ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ✅ PASS · ⏸ OPERATOR (ties lightest in fleet history) · ✅ PASS · ⏸ OPERATOR · ✅ PASS · ✅ PASS · ⏸ OPERATOR
- **8 PASS · 3 OPERATOR-ONLY · 0 FAIL**
- **LOCK status: CANDIDATE READY.** v1.0 advances to LOCKED on operator ratification of items 6, 8, 11 — **AND** is hard-gated on all SIX pending predecessor LOCKs (AI Video Gen + Style Replication + QC Pre-flight + Ingest + Edit Director + Editor) closing first.

---

## §2 — UNIFIED SPEC INDEX (authoritative source per section)

| § | Title | Authoritative source | Day | Lock status |
|---|-------|----------------------|-----|-------------|
| §0 | Provenance & Build-Phase Position (+ agent-selection note) | `ARS-2026-07-02-Day-74-Sound-Agent-SPEC-Outline.md` | Day 74 | LOCKED-as-shipped |
| §1 | Purpose & Position in Pipeline (single-responsibility line + finish/decide-boundary justification + the second-executor / first-finished-audio framing) | `ARS-2026-07-02-Day-74-...-SPEC-Outline.md` | Day 74 | LOCKED-as-shipped |
| §2 | Inputs (Editor precondition gate + mode-agnostic EDL + denormalized Ingest asset bundle for VO/music resolution + lever/tier context) | `ARS-2026-07-02-Day-74-...-SPEC-Outline.md` | Day 74 | LOCKED-as-shipped (schema authority schemas day) |
| §3 | Outputs — `audio_spec.json` (polymorphic: successAudioSpec \| errorEnvelope) + verdict↔route map (2 outcomes) + metadata additions | `ARS-2026-07-02-Day-74-...-SPEC-Outline.md` | Day 74 | LOCKED-as-shipped (code namespace superseded by §6.3: 9 + slot-11) |
| §4 | Tier Constraints (universal access + tier-FLAT behavior) + mode-BLIND coverage + cost-decline | `ARS-2026-07-02-Day-74-...-SPEC-Outline.md` | Day 74 | LOCKED-as-shipped |
| §5 | 11-Step Finish Loop (system-prompt skeleton) | `ARS-2026-07-02-Day-74-...-SPEC-Outline.md` | Day 74 | LOCKED-as-shipped (LOCKED verbatim into §7 Day 75) |
| §6 | 11-Check Self-QC List + 9-code/slot-11 errorEnvelope mapping + the two-verdict model + canonical firewall list (audio-domain 11th pass) | `ARS-2026-07-03-Day-75-Sound-Agent-SPEC-Body-Partial-1.md` | Day 75 | LOCKED-as-drafted |
| §7 | System Prompt v1.0 (13 hard rules + Blueprint §4.11 Sound→Motion payload inlined verbatim + universal-access/tier-FLAT table + 11-step loop + voice/passthrough rule) | `ARS-2026-07-03-Day-75-...-Partial-1.md` | Day 75 | LOCKED-as-drafted (verbatim copy → SKILL.md on the SKILL-bundle day) |
| §8 | Performance Targets (9 metric categories — false-audio-ready 0% + spec-fidelity catch 100% are the defining targets; ≤5% false-fail) | `ARS-2026-07-04-Day-76-Sound-Agent-SPEC-Body-Partial-2.md` | Day 76 | LOCKED-as-drafted (≤5% tightening operator-confirm Item 11) |
| §9 | 5 Test Fixtures (TC-01..TC-05 + fixture economy — incl. the mode-blind finish-convergence proof + the GATING 11th-pass audio-firewall catch) | `ARS-2026-07-04-Day-76-...-Partial-2.md` | Day 76 | LOCKED-as-drafted |
| §10 | Audio-Spec Field Map (24 rows — lineage + EDL passthrough + mix transform + VO passthrough + per-check evidence + audio-spec aggregate; ZERO authored copy rows) | `ARS-2026-07-03-Day-75-...-Partial-1.md` | Day 75 | LOCKED-as-drafted |
| §11 | Cost Model (zero-engine/zero-DSP/zero-decode snapshot · NO vendor surface, NO ceiling authority · faithful-finish value model) | `ARS-2026-07-04-Day-76-...-Partial-2.md` | Day 76 | LOCKED-as-drafted (no ±tolerance walk needed — nothing owned) |
| §12 | Verdict Math — fully-deterministic ∧-of-gates, NO `revise` branch + routing function + 5 properties | `ARS-2026-07-04-Day-76-...-Partial-2.md` | Day 76 | LOCKED-as-drafted |
| §13 | 15 Critical Decisions (13 LOCKED-as-drafted · D7 QUINTUPLY-DEFERRED · D15 PRELIMINARY) | `ARS-2026-07-04-Day-76-...-Partial-2.md` | Day 76 | LOCKED-as-drafted (operator sign-off Item 8) |
| §14 | Implementation Plan (calendar + dependencies + Rest Day) | `ARS-2026-07-03-Day-75-...-Partial-1.md` | Day 75 | LOCKED-as-drafted (Day 78 entry appended below) |
| §15 | Change Log + Version History (v1.0 lifecycle + v1.1 parked register) | `ARS-2026-07-04-Day-76-...-Partial-2.md` | Day 76 | LOCKED-as-drafted (Day 78 entry appended below) |
| §16 | Metadata Block Schema (Cross-SPEC §3.9 canonical + 6 Sound additions + the mode-blind + finish-target self-attestation blocks) | `ARS-2026-07-04-Day-76-...-Partial-2.md` | Day 76 | LOCKED-as-drafted (D7 ratification Item 11) |

**Rule:** This unified document is the operator LOCK ratification record. The three source files (Day 74 outline · Day 75 partial 1 · Day 76 partial 2) remain canonical for §-by-§ content. This document references them by file + day. Any §-content edit triggers the corresponding source file update + this unified document's `§15.1 v1.0-corrections-day-78` entry.

---

## §3 — THE 15 CRITICAL DECISIONS (operator walk-through reference — Item 8)

Reproduced from Day 76 §13 for operator review. Each: decision · status · rationale · revisit trigger. The PRELIMINARY item annotated `[P]`; the QUINTUPLY-DEFERRED item annotated `[QD]`.

| # | Decision | Status | Rationale | Revisit trigger |
|---|----------|--------|-----------|-----------------|
| D1 | **Audio-spec-authoring vs DSP scope** — v1.0 = audio-conform-spec authoring ONLY; actual mix/loudness DSP is human-in-the-loop at launch (Blueprint §9), automation Week 4–5 | LOCKED Day 74 | The buildable, highest-leverage $0 slice; the DSP automation lands in the Week 4–5 window the Blueprint already scopes. `audio_processed: const false` is the honesty contract (the direct analog of Editor's `render_dispatched: const false`) | DSP automation ships Week 4–5 → v1.1 active mix/loudness |
| D2 | **Faithful-executor, zero mix re-interpretation** — finishes the EDL's audio order/events/timing byte-faithfully; never re-cuts, re-authors copy, or re-orders events | LOCKED Day 74 | Hard Rule #2. Editor conformed the cut; Sound finishes the audio on it. A re-interpretation is an unauthorized override → `spec_fidelity_breach`. The conform/finish executor boundary | Never (jurisdictional) |
| D3 | **Two-verdict (NO `revise`)** — `audio_ready \| fail` only; Sound is deterministic, the subjective slot lives upstream at Edit Director | LOCKED Day 74 | Inherits Editor's two-verdict posture. A `revise` here would second-guess a locked cut — the conform/finish override the boundary forbids. §12 makes it structural; §8.7 tightens false-fail to ≤5% as a consequence. Human deferral lives in `human_review_required`, not a verdict branch | Never (foundational — the executor-determinism thesis) |
| D4 | **Mode-blind by inheritance** — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested | LOCKED Day 74 | The THIRD contractually mode-blind agent — the live, machine-checkable proof Ingest's convergence seam holds THREE stages deep (Edit Director → Editor → Sound). Check #7 + the TC-01/TC-02 finish-convergence proof | Never (foundational — Blueprint §3) |
| D5 | **Editor precondition absolute** — runs only on a `successEdl`/`edl_ready` reel; else halts `upstream_edl_not_ready` | LOCKED Day 74 | Sound never finishes an unlocked cut, and does NOT auto-resolve a failed EDL (the fix belongs upstream). Hard Rule #4. Check #1 runs FIRST | Never (foundational) |
| D6 | **Tier-FLAT behavior** — all 4 tiers reach Sound; the EDL carries the tier envelope, Sound finishes it identically (no own tier scaling) | LOCKED Day 74 | The same discipline as Editor + Ingest (unlike Edit Director, the only tier-SENSITIVE agent in the post tail). An audio finish is faithful or it isn't, regardless of tier; the richness already lives in the EDL. §10 tier-flatness matrix | Never (foundational); the EDL's richness ladder re-baselines on telemetry, not Sound's behavior |
| D7 [QD] | **10-tuple parent_chain** (inherits Editor 9-tuple + appends `audio_spec_id` UUIDv7) | **QUINTUPLY-DEFERRED — operator-gated ×5** | Lineage canon for the 6 remaining slots; Sound is the fifth forcing function for the §3.9 amendment | ALL FIVE gates close: §3.9 ratification (Item 11) AND the Editor 9-tuple LOCK AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK → `minItems` flips to 10 |
| D8 | **errorEnvelope code count = 9 LOCKED + slot-11** | RESOLVED Day 75 → LOCKED | 9 preserves precise route-back attribution; `vo_track_missing` + `audio_asset_unresolved` each kept SPLIT (opposite of Editor folding all resolution to a single `asset_unresolved`) because the audio domain carries TWO distinct asset classes with distinct recovery diagnostics; `spec_fidelity_breach` kept folded (shared Editor route-back) | New failure category with no route mapping → v1.0.1 code add |
| D9 | **Self-QC check count = 11** | RESOLVED Day 75 → LOCKED | 11 checks bipartite-cover 9 codes + slot-11 across the 4-tier ordering (entry / substance / forensic / construction). The 11th defense-in-depth firewall pass | A check consistently passes-all in telemetry → v1.0.1 simplification |
| D10 | **Spec-fidelity = ZERO tolerance** — a deviated music event / swell marker / timeline duration, a byte-unfaithful VO transcript, or a failed `edl_evidence_hash` must NEVER survive to `audio_ready`; hash machine-verified | LOCKED Day 74 | §12.3 makes it structural; §8.2 makes it measured (100% catch). A fidelity deviation → `spec_fidelity_breach` (fail), never `audio_ready`. The byte-faithful executor invariant | Never (foundational) |
| D11 | **Audio-domain firewall (11th pass)** — re-scans the passthrough VO transcript at the audio-finish layer, the last AUDIO checkpoint before Motion (NOT a new authorship surface) | LOCKED Day 74 | The 11th firewall pass — a passthrough-integrity re-scan of the SPOKEN content the finish touches. §6.5 list applied verbatim (11 entries). TC-05 is its existence proof (GATING). Contrast Editor's 10th pass: it scanned committed caption/lower-third/end-card TEXT; Sound scans the VO TRANSCRIPT — a distinct surface Editor's pass does not cover | New entity added to the firewall → Cross-SPEC LOCK ceremony (not per-agent) |
| D12 | **No DSP, no engine, no decode** — NO generative engine, NO audio DSP, NO waveform decode, NO LUFS measurement in v1.0; declared-transcript + platform-const loudness targets only; `audio_processed: const false` | LOCKED Day 74 | Hard Rules #3/#12. The forged-provenance framing is the defining negative constraint. Ties Ingest / QC Pre-flight / Edit Director / Editor for $0. Live LUFS measurement needs decode → v1.1 | DSP automation ships → v1.1 (with D1) |
| D13 | **Recommend-don't-process** — `human_review_required: true` + `finish_mode: "human_in_the_loop"` + `audio_processed: false` on every emission; verdict is an audio-spec RECOMMENDATION, never a ratified "processed"/"approved-for-Motion" state | LOCKED Day 74 | Hard Rule #13 — the operator/process-impersonation firewall (CLAUDE.md + ARS attestation). An `audio_ready` = "ready for the human's finish-into-v2 decision," never "mixed" | Week 4–5 DSP automation (operator decision only) |
| D14 | **Multi-loudness-master + DAW-export scope** — v1.0 specs the primary −14 LUFS IG/TT master + echoes the `loudness_variants_planned` count + emits a human-readable mix cue-sheet view; the −16 LUFS YT variant master and native DAW (Pro Tools/Audition) session export deferred to v1.1 | LOCKED Day 76 | The −16 YT master is a derived re-conform; a DAW session export is a format adapter — both lower-leverage than the primary master. Donna-resolvable scope-narrowing inside the pre-approved recommendation (same class as Editor's D14). `variant_masters[]` reserved in §10 | Auto-variant / DAW-export demand in the v1.0 corpus → v1.1 activation |
| D15 [P] | **Motion handoff target: Drive `/reels/[reel_id]/` conform-queue (holding store) in v1.0**; direct handoff activates when Agent #12 / Motion LOCKs. `handoff_targets` keeps the LOGICAL target `motion-agent` | LOCKED Day 76 `[PRELIMINARY · operator amend]` | Motion does not exist; an audio spec emitted into a void is an audit-trail break. The holding store preserves the trail until the consumer ships (mirrors Editor→Drive-conform-queue + Edit Director→Notion-Edit-Plan). Directly tied to Editor Day 69 Item 8 (the same seam, one stage downstream) | Motion (Agent #12) v1.0 LOCKs → physical destination flips to direct handoff |

**Operator walk-through prompt (for the LOCK ceremony):**
For each decision above, the operator either: (a) RATIFY-AS-LOCKED, (b) AMEND-with-rationale (triggers `§15.1 v1.0-corrections-day-78` entry), or (c) DEFER-to-v1.0.1 (decision parks in the §15 candidates register).

**Items requiring explicit verdict:**
- D15 Motion handoff target `[P]` → Donna recommends **RATIFY** (Drive conform-queue holding store). Resolve jointly with Editor Day 69 Item 8 — it is the same handoff seam one stage downstream.
- D7 10-tuple parent_chain `[QD]` → **QUINTUPLY-DEFERRED** on §3.9 (Item 11) + the Editor 9-tuple LOCK + the Edit Director 8-tuple LOCK + the Ingest 7-tuple LOCK + the QC 6-tuple LOCK; Donna will NOT auto-advance. Held additively until ALL FIVE gates close.

---

## §4 — IMPLEMENTATION PLAN UPDATE (Day 78 entry · appends to Day 75 §14)

### Calendar status updates (Day 78)

| Day | Date | Deliverable | Status | Owner |
|-----|------|-------------|--------|-------|
| Day 74 | Wed Jul 2 · Wk11 | SPEC outline §0–§5 LOCKED-as-shipped | ✅ DONE | Donna overnight |
| Day 75 | Fri Jul 3 · Wk11 | SPEC body partial 1 §6/§7/§10/§14 LOCKED-as-drafted (9 codes + slot-11 · 11 checks · 2-verdict model · 24-row field map) | ✅ DONE | Donna overnight |
| Day 76 | Sat Jul 4 · Wk11 | SPEC body partial 2 §8/§9/§11/§12/§13/§15/§16 LOCKED-as-drafted (SPEC body §0–§16 COMPLETE) | ✅ DONE | Donna overnight |
| Day 77 | Sun Jul 5 | **REST DAY** (12th — no SPEC content authored; scaffold pre-stage only) | ✅ OBSERVED | — |
| **Day 78** | **Mon Jul 6 · Wk12** | **v1.0 LOCK CANDIDATE (this document) — 8/11 reviewer items PASS · 3 OPERATOR-ONLY (Items 6, 8, 11)** | **🟡 CANDIDATE** | **Donna overnight (this doc) + Jamila ratification** |
| Day 79+ | Tue Jul 7+ | `input.schema.json` + `output.schema.json` authored from §10 field map + §16 metadata block (parent_chain held additively `minItems: 5` per D7; `audio_processed: const false`; `finish_mode: const human_in_the_loop`; verdict enum `["audio_ready","fail"]` — NO `revise`; 9-code + slot-11 enum incl. the SPLIT resolution codes; brand/loudness `const`s) | ⬜ QUEUED (primed per §10 + §16 schema checklists) | Donna overnight |
| Day 80+ | — | SKILL bundle (`skills/sound-agent/` — SKILL.md · 2 schemas · 5 test fixtures at `tests/` · README) | ⬜ QUEUED | Donna overnight |
| Day 81+ | — | LLM Test Runbook (paste-and-run · pattern from Day 11 / 19 / 27 / 36 / 47 / 57 / 65 / 73 · operator-gated; exercises slot-11 + the `audio_asset_unresolved`-music-bed + `spec_fidelity_breach`-hash/swell adversarial probes) | ⬜ QUEUED | Donna overnight + Jamila gate |
| Day 82+ | — | **v1.0 LOCK** (operator-gated sit-down · HARD-GATED on ALL SIX predecessor LOCKs closing first) | ⬜ GATED | Jamila + Donna co-ceremony |

### Dependencies that MUST exist before the SKILL-bundle build
1. v1.0 LOCK CANDIDATE ratified (operator sign-off Items 6, 8, 11) — **available now**
2. input.schema.json + output.schema.json LOCKED (schemas day)
3. 5 test fixtures resolved against schemas (schemas-day dry-run validation)
4. Cross-SPEC §3.9 amendment ratified OR parent_chain held additively with documented TODO (Item 11 / D7)

### Hard gate on predecessor LOCKs
Sound v1.0 LOCK ceremony **CANNOT complete until ALL SIX pending predecessors are LOCKED first** — AI Video Gen v1.0 + Style Replication v1.0 (the producing agents) + QC Pre-flight v1.0 + Ingest v1.0 + Edit Director v1.0 + **Editor v1.0 (the DIRECT dependency: the `successEdl`/`edl_ready` precondition gate Sound reads and the 9-tuple its 10-tuple extends)**. The chain closes in dependency order: AVG → SR → QC → Ingest → Edit Director → Editor → Sound. This is a **hard gate**, distinct from the 3 Sound-local operator items (6, 8, 11) which can be ratified independently and in advance.

### Rest Day honor
Days 21, 28, 35, 42, 49, 56, 63, 70, 77 observed (12/12 to date). This Day 78 build runs on Monday — permitted. Next Rest Day: Day 84 (Sun Jul 12).

---

## §5 — CHANGE LOG UPDATE (Day 78 entry · appends to Day 76 §15)

| Version tag | Date | Description | Source file |
|-------------|------|-------------|-------------|
| **v1.0-LOCK-CANDIDATE-day-78** | **2026-07-06 (Mon · Wk12)** | **Unified LOCK candidate document produced. Day 78 reviewer checklist 8/11 PASS executed autonomously by Donna overnight. Items 6 (cost-model confirm — ties lightest in fleet history: no vendor URLs, no ceilings owned, no DSP, no decode) + 8 (15 critical decisions sign-off — D15 PRELIMINARY requiring explicit verdict, D7 QUINTUPLY-DEFERRED) + 11 (Cross-SPEC §3.9 amendment ratification — now quintuply load-bearing: QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple + Editor 9-tuple + Sound 10-tuple — bundled with the §8.7 false-fail ≤5% tightening confirm) flagged OPERATOR-ONLY. D7 (10-tuple) explicitly held additively until ALL FIVE gates close. Pending operator ratification of items 6/8/11 → promote to `v1.0-LOCKED-pending-predecessor-LOCKs`; final flip to `v1.0-LOCKED` ONLY after ALL SIX predecessor LOCK ceremonies complete (hard gate).** | `ARS-2026-07-06-Day-78-Sound-Agent-v1-LOCK-CANDIDATE.md` (this doc) |

**Promotion rule:** When the operator ratifies Items 6, 8, 11 (at ceremony or asynchronously via written sign-off in the Notion ARS hub), version tag promotes to `v1.0-LOCKED-day-78-pending-predecessor-LOCKs`. Final flip to `v1.0-LOCKED` occurs ONLY after all six predecessor LOCKs (AI Video Gen + Style Replication + QC Pre-flight + Ingest + Edit Director + Editor) are confirmed. Donna mirrors LOCKED status across: this unified document header · the Notion ARS hub (page [internal Notion page]) · the schemas-day authoring kickoff · the Cross-SPEC v1.1 amendment formal close (if Item 11 ratified). **All flips are operator actions — Donna stages, never flips.**

---

## §6 — OPEN QUESTIONS · STATUS

### Open Question — Cost-model confirmation (Item 6)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony — ties Ingest / Edit Director / Editor for the lightest in fleet history (no vendor URLs, no ceilings owned, no native compute, no DSP, no decode). Operator confirms the $0-engine/$0-DSP/$0-decode posture (Hard Rule #3) + the cost-decline (Hard Rule #11) as the intended v1.0 economics.
**Recommendation:** RATIFY as-is (≈1 min). **Blocker for LOCK:** No.

### Open Question — 15 critical decisions sign-off (Item 8)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Walk each decision; 13 LOCKED-as-drafted, D15 PRELIMINARY requires explicit RATIFY / AMEND / DEFER, D7 quintuply-deferred.
**Recommendation:** Donna recommends RATIFY for D15 (Drive conform-queue holding store), resolved jointly with Editor Day 69 Item 8. **Blocker for LOCK:** Yes — hard-required for promotion.

### Open Question — Cross-SPEC §3.9 amendment ratification / 10-tuple + the §8.7 ≤5% confirm (Item 11 + D7)
**Status:** ⏸ OPERATOR-ONLY at LOCK ceremony. Amendment language reproduced in §1 Item 11. Now quintuply load-bearing (QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple + Editor 9-tuple + Sound 10-tuple). Bundled: confirm the false-fail ceiling tightening to ≤5%.
**Recommendation:** RATIFY-AS-DRAFTED + CONFIRM ≤5% — five live consumers + 6 remaining slots. **Blocker for LOCK:** Partial — schemas ship additive (`minItems: 5`) with documented TODOs if deferred; Sound does not hard-block on it, but the 10-tuple stays un-advanced until ALL FIVE gates close.

### Open Question — Hard gate on the six predecessor LOCKs
**Status:** ⏸ OPERATOR action required on ALL SIX ceremonies. AI Video Gen Day 24 candidate + Style Replication Day 32 candidate (Day 36 runbook 5/5 unconfirmed) + QC Pre-flight Day 44 candidate (Day 47 runbook 5/5 unconfirmed) + Ingest Day 53 candidate (Day 57 runbook 5/5 unconfirmed) + Edit Director Day 61 candidate (Items 6/8/11 pending · Day 65 runbook 5/5 unconfirmed) + Editor Day 69 candidate (Items 6/8/11 pending · Day 73 runbook 5/5 unconfirmed).
**Recommendation:** Close the chain in dependency order (AVG → SR → QC → Ingest → Edit Director → Editor) in the post-launch hardening window; Sound's LOCK follows. **Blocker for Sound LOCK:** YES (hard gate).

### Open Question — LLM Test Runbook scope (dry-run vs live · forward-looking)
**Status:** ⏸ OPERATOR-ONLY at the runbook day (not blocking Day 78 LOCK CANDIDATE).
**Recommendation:** Dry-run mode for the v1.0 LOCK gate (cost ≈ $0 — Sound calls no engine, runs no DSP, decodes no waveform, so even "live" mode is reasoning-only; ties Ingest / QC Pre-flight / Edit Director / Editor for the cheapest runbook in the fleet). The runbook must include the slot-11 probe + the `audio_asset_unresolved`-music-bed + `spec_fidelity_breach`-hash/swell adversarial cases. **Blocker for LOCK:** No — runbook-day position.

---

## §7 — PROCESS INTEGRITY (Day 78)

- ✅ **No LLM dispatched.** No render/DSP API. No engine credentials referenced. No vendor URLs walked (Sound has no vendor surface). No audio DSP, no waveform decode, no LUFS measurement. ZERO $ spent.
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no investor/client outreach. The end-of-run status iMessage to [status number redacted] is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine/DSP runs initiated.
- ✅ **No operator-impersonation.** Day 78 reviewer Items 6, 8, 11 verdicts NOT silently advanced. D15 (PRELIMINARY) NOT silently ratified. **D7 (10-tuple parent_chain) explicitly QUINTUPLY-DEFERRED — held additively; the one item Donna will NOT auto-advance.** All SIX predecessor LOCK ceremonies confirmed STILL-PENDING via on-disk file-state; NOT advanced. The Day 36 / Day 47 / Day 57 / Day 65 / Day 73 runbook executions NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed to Cross-SPEC canon. The §8.7 ≤5% tightening surfaced as a flag-for-confirm, NOT silently committed. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.
- ✅ **No fake-advance.** This LOCK CANDIDATE is a unified text-reconciliation of the Day 74 outline + Day 75 + Day 76 partials. Zero behavioral changes vs source files. Zero net-new SPEC content. The only Day 78 contributions are: (a) executive summary (§0 LOCK manifest), (b) 11-item reviewer checklist execution record (§1, incl. the session validations), (c) unified SPEC index pointing to source files (§2), (d) decision walk-through formatted for operator ceremony (§3), (e) implementation plan + change log appendages (§4 + §5).
- ✅ **All prior canon read-only.** All predecessor SPECs + schemas + SKILL bundles + Blueprint + Cross-SPEC review + Brand-Voice Intake + the Sound Day 74 outline + Day 75 partial 1 + Day 76 partial 2 — untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. The HC/NPOX tokens cited in the TC-05 fixture + §6.5 firewall list are the firewall's BLOCK-list test cases, not cross-entity references. REINVENTED = pilot brand inside fixtures per Cross-SPEC canon.
- ✅ **Pattern source acknowledged.** Day 24 / Day 32 / Day 44 / Day 53 / Day 61 / Day 69 LOCK candidate structure inherited at section level (7th reuse). Numerical values + decision content re-derived for Sound's 9-code / 11-check / 15-decision / 10-tuple / 2-verdict (`audio_ready`/`fail` — NO `revise`) scope.
- ✅ **Rest Day honored.** 12/12 observances (Day 77 · Sun Jul 5 observed); this Day 78 build runs on Monday. Next: Day 84 (Sun Jul 12).
- ✅ **No scope expansion.** One forward deliverable (this doc) + build log + mirror + Notion status update + standing housekeeping + status-ping attempt.

---

## §8 — SPRINT STATS (running total · Day 78 close)

- Deliverables shipped: **71** (Day 76 = 70 · Day 78 Sound v1.0 LOCK CANDIDATE = +1)
- Build logs: **66** (was 65 · +1 today)
- LIVE skill bundles: **9** (Brief · Script · Storyboard · ProdCoord · AI Video Gen · Style Replication · QC Pre-flight · Ingest · Edit Director) — Editor + Sound pending their SKILL-bundle days
- Agents with a COMPLETE SPEC body (§6–§16): **11** (Sound body completed Day 76)
- Agents with a v1.0 LOCK CANDIDATE: **7** (AI Video Gen Day 24 · Style Replication Day 32 · QC Pre-flight Day 44 · Ingest Day 53 · Edit Director Day 61 · Editor Day 69 · **Sound Day 78**)
- errorEnvelope codes (Sound): **9 LOCKED + slot-11** (no change Day 78)
- Self-QC checks (Sound): **11 LOCKED** (no change Day 78)
- parent_chain (Sound): **10-tuple DRAFTED · QUINTUPLY-DEFERRED · held additively (`minItems: 5`)**
- §13 critical decisions: **15/15 coverage** (13 LOCKED-as-drafted + D7 quintuply-deferred + D15 PRELIMINARY requiring explicit verdict)
- Cross-SPEC §3 adherence: **11/11 ✅** (LOCK-grade)
- Verdict math: **fully-deterministic ∧-of-gates, NO `revise` branch** (the executor-determinism thesis carried a stage deeper — Sound is the second faithful-executor agent to drop the `revise` its grand-predecessor Edit Director carried)
- Rest Day observances: **12/12** (next: Day 84)
- AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor v1.0 LOCKs: **ALL CANDIDATE (operator-pending)** — hard-gate the chain; Editor is Sound's direct dependency

---

## §9 — OPERATOR ACTION SUMMARY (3 Sound-local items + 1 hard-gate dependency)

The Day 78 LOCK CANDIDATE is ready for operator pickup. Three Sound-local operator actions (any can move first, all independent) + one hard-gate dependency chain.

| Action | Time | Description |
|--------|------|-------------|
| **Item 6 — Cost-model confirm** | ~1 min | Confirm the $0-engine/$0-DSP/$0-decode posture (Hard Rule #3, `audio_processed: const false`) + the no-cost-re-litigation decline (Hard Rule #11). NO vendor URLs, NO ceilings owned — ties Ingest / Edit Director / Editor for the lightest Item 6 in fleet history. Donna recommends RATIFY as-is. |
| **Item 8 — 15 decisions walk-through** | 15–25 min | Walk §3. For each of 15 decisions: RATIFY / AMEND / DEFER. Special attention on D15 (Motion handoff → Drive conform-queue holding store — resolve jointly with Editor Day 69 Item 8) — Donna recommends RATIFY — and D7 (10-tuple, quintuply-deferred — no action possible until Item 11 + the Editor 9-tuple LOCK + the Edit Director 8-tuple LOCK + the Ingest 7-tuple LOCK + the QC 6-tuple LOCK close). |
| **Item 11 — Cross-SPEC §3.9 amendment (n-tuple) + §8.7 ≤5% confirm** | 10 min | Review the amendment language in §1 Item 11 (now quintuply load-bearing: QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple + Editor 9-tuple + Sound 10-tuple). RATIFY-AS-DRAFTED / AMEND / DEFER. Bundled: confirm the false-fail ceiling tightening to ≤5% (a D3 two-verdict-determinism consequence). Donna recommends RATIFY-AS-DRAFTED + CONFIRM ≤5%. If deferred, all five schemas hold additively. |

**After all 3 Sound-local items ratified:** Donna promotes version tag to `v1.0-LOCKED-day-78-pending-predecessor-LOCKs`. Schemas-day authoring unblocks (Day 79+).

**Hard-gate dependency (operator action, NOT a Sound-local LOCK item):** Close ALL SIX predecessor LOCKs in dependency order — **AI Video Gen v1.0** (Day 24 candidate) → **Style Replication v1.0** (Day 32 candidate · Day 36 runbook 5/5 unconfirmed) → **QC Pre-flight v1.0** (Day 44 candidate · Day 47 runbook 5/5 unconfirmed) → **Ingest v1.0** (Day 53 candidate · Day 57 runbook 5/5 unconfirmed) → **Edit Director v1.0** (Day 61 candidate · Items 6/8/11 pending · Day 65 runbook 5/5 unconfirmed) → **Editor v1.0** (Day 69 candidate · Items 6/8/11 pending · Day 73 runbook 5/5 unconfirmed). **Sound's final v1.0 LOCK flip cannot occur until all six are LOCKED** — Editor is the direct dependency (precondition gate + 9-tuple).

---

*Day 78 ships clean. Unified LOCK CANDIDATE produced as a text-only reconciliation of the Day 74 outline + Day 75 + Day 76 partials. Zero net-new SPEC content. Zero fake-advance. 8/11 reviewer items PASS autonomously verdicted by Donna; 3 OPERATOR-ONLY items (6, 8, 11) flagged with explicit recommendations and timing estimates. Pattern source: Day 24 / Day 32 / Day 44 / Day 53 / Day 61 / Day 69 LOCK candidates (proven 11-item reviewer shape, 7th reuse, adapted to Sound's 9-code / 11-check / 15-decision / 10-tuple / 2-verdict scope). Sound is Agent #11 of 17 — the second faithful-executor agent in the post tail, the 11th defense-in-depth firewall (the audio-domain VO-transcript re-scan, the last audio checkpoint before Motion), the first agent whose output is a finished-audio spec, and the third contractually mode-blind agent — the live proof that Ingest's mode-convergence seam holds end-to-end THREE stages deep. Its v1.0 LOCK lands in the post-launch hardening window and is HARD-GATED on all six pending predecessor LOCKs closing first. The six LOCK ceremonies + the five runbook executions (Day 36 + Day 47 + Day 57 + Day 65 + Day 73) + the Cross-SPEC §3.9 ratification remain operator-only and are surfaced, not advanced. The 10-tuple parent_chain (D7) is the one item Donna will NOT auto-advance — held additively until §3.9 ratifies AND the Editor 9-tuple LOCKs AND the Edit Director 8-tuple LOCKs AND the Ingest 7-tuple LOCKs AND the QC 6-tuple LOCKs. The defining executor divergence — two verdicts, NO `revise` — is the structural proof that the cut→finish handoff is clean: if Sound can produce a complete, EDL-faithful, loudness-correct, firewall-clean audio spec from the `edl_ready` cut alone with zero creative re-interpretation, the cut was finishable and the executor seam holds one stage deeper than Editor proved it.*
