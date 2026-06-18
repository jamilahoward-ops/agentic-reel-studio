# ARS — Edit Director Agent v1.0 SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14)

**Date:** Wed Jun 17, 2026 (Day 59 · Wk9 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 1 — §6 + §7 + §10 + §14 LOCKED-as-drafted Day 59. §8 + §9 + §11 + §12 + §13 + §15 + §16 reserved for partial 2 (Day 60 target). v1.0 LOCK CANDIDATE + schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK follow on the established cadence (Ingest Day 53–57 / QC Pre-flight Day 44–47).
**Pattern source:** `ARS-2026-06-09-Day-51-Ingest-Agent-SPEC-Body-Partial-1.md` §6/§7/§10/§14 (Day 51 partial 1 — proven shape inherited verbatim) and `ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` (grandparent pattern).
**Outline source:** `ARS-2026-06-16-Day-58-Edit-Director-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 58 + the §6–§16 LOCK-scope preview this partial authors against).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — pipeline roster position 10 "Edit Director" + §3 mode-agnostic post-production contract + §4.8 Ingest→Edit-Director payload + §4.9 Edit-Director→Editor `edit_plan` handoff shape + §7 dispatch I/O).
**Brand-creative canon:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (visual identity / motion / lower-thirds), §8 (reel format / 45–75s structure), §10 (CTA library — internal-question rule), §11 (caption spec) — the enforced rule surface.
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen v1.0 LOCK candidate + schemas + SKILL + Day 27 runbook. Style Replication v1.0 LOCK candidate + schemas + SKILL + Day 36 runbook. QC Pre-flight v1.0 LOCK candidate (Day 44) + schemas (Day 45) + SKILL + Day 47 runbook. Ingest v1.0 LOCK candidate (Day 53) + schemas (Day 54) + SKILL + Day 57 runbook. **All FOUR predecessor LOCK ceremonies remain OPERATOR-GATED entering Day 59 — file-state confirmed (version tags unflipped). This partial 1 references LOCK-as-drafted canon (text-stable) without depending on operator-gated ratification — the same posture Ingest Day 51 partial 1 held over its three predecessors.**

> **Cadence honesty (on schedule — surfaced):** The Day 58 outline calendared partial 1 for **Day 59 (Wed Jun 17)** and partial 2 for Day 60 (Thu Jun 18). On-disk file-state confirms the chain is intact: Day 58 outline shipped (Tue Jun 16), Day 57 Ingest runbook before it (Mon Jun 15), Day 56 (Sun Jun 14) was correctly a Rest Day no-build. Tonight's Day 59 session ships partial 1 (this document) ON the outline calendar — no slip. The §14 calendar below encodes the on-time trajectory. Next Rest Day: Day 63 (Sun Jun 21).

> **Authoring discipline (LOCK signal):** §6 + §7 + §10 + §14 are LOCKED-as-drafted Day 59. The §13 critical-decisions walk on partial 2 (Day 60) may amend §10's 8-tuple parent_chain extension decision (triply-gated — see §10.4 / §14.7) and the Editor-handoff-target decision (Open Question 4); those are the only forward-looking edit slots in this partial 1. Everything else is canon as of this document.

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this partial's authoring, on-disk file-state confirms **all four predecessor LOCK ceremonies remain OPERATOR-GATED** (AI Video Gen, Style Replication, QC Pre-flight, Ingest — version tags unflipped; Day 36 + Day 47 + Day 57 runbook executions unconfirmed). Edit Director v1.0 LOCK will hard-gate itself on those closing first — the **Ingest 7-tuple in particular is Edit Director's direct 8-tuple dependency**, and the Ingest LOCK is itself behind the QC 6-tuple LOCK. This body partial is forward-design over LOCK-stable text artifacts only, with zero production output consumed and zero operator ceremony assumed.

---

## §6 — 11-Check Self-QC List (LOCKED-as-drafted Day 59)

The Edit Director Agent runs this 11-check list **on its own authored Edit Plan** before emitting `successEditPlan` (or before finalizing an `errorEnvelope`). Check shape inherited verbatim from the fleet §6 pattern (proven 8× — Brief through Ingest; Edit Director is the 9th defense-in-depth firewall pass). Failure semantics are LOCKED inheritance: retry once on a recoverable self-QC failure, halt on the second.

**Critical distinction — self-QC vs. the direction loop:** The **11-step direction loop (§5, outline)** is the agent authoring the *edit plan* from the asset bundle + creative intent; the **§6 self-QC list (this section)** is the agent adjudicating *its own plan* — confirming the plan it is about to emit is well-formed, structurally complete, brand-compliant, firewall-clean on its OWN authored text, and free of the operator-impersonation anti-pattern, before that plan becomes the Editor's source of truth. A FAIL in §6 means the agent built a malformed plan, not that the assets failed. The asset verdict (pass/fail) was Ingest's; the creative verdict (plan_ready/fail/revise) is carried in the plan payload; the §6 result decides whether that plan is fit to ship.

**QC retry policy (inherited, LOCKED):** First self-QC failure → regenerate the offending plan field set with concrete fix instructions inlined into the next attempt. Second self-QC failure → emit `errorEnvelope` with `failure_code: "edit_director_agent_failed"`, `attempts == 2`, halt. **No third attempt.** Same 2-strike contract every agent in the pipeline honors.

**Defense-in-depth (9th pass — a NEW surface):** The prior eight passes scanned text the agent *received* (upstream script text, captions, prompts, evidence blocks, asset filenames/metadata). Edit Director's pass scans the **text it AUTHORS ITSELF** — the lower-third copy it writes, the caption strings it lays onto the cut, the end-card line — a surface no prior pass owned, because no prior agent wrote reel-facing copy. Because Edit Director calls **no generative engine and renders no media**, a self-QC failure here never wastes spend — but a *missed* failure (a banned-entity token authored into a lower-third reaching the Editor, then burned into a cut) is the exact defect class the 9th pass exists to prevent.

### 6.1 The 11 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **Ingest precondition verified — the consumed `asset_manifest.json` has `verdict == "pass"` AND `output_type == "successAssetManifest"` OR a Lever-3 human sign-off is attached.** | `upstream_ingest_not_passed` | Runs FIRST. Assert the Ingest manifest's `verdict` is `pass` and `output_type` is the success branch, or a non-pass manifest carries an explicit Lever-3 operator sign-off record. Otherwise halt — Edit Director never directs an un-ingested reel. Cite the manifest id + verdict in `detail.ingest_precondition`. The plan MUST carry `ingest_precondition_check: {asset_manifest_id, verdict_observed, lever3_signoff_present}` — a missing/uncomputed block = self-QC FAIL. |
| 2 | **Upstream success verification — the consumed Asset Manifest is its success type, NOT `errorEnvelope`.** | `upstream_not_success` | Assert the primary input `output_type == "successAssetManifest"`. A consumed `errorEnvelope` = halt — you cannot direct a failed ingest output. Cite the failed manifest id in `detail.upstream_failure`. (Folds with Check #1 at the precondition gate but carries its own code for route-back attribution.) |
| 3 | **Coverage + mappability re-confirm — `coverage_complete == true`, `missing_shots == []`, and every `raw_footage[].shot_ref` resolves to a Script/Storyboard beat (and vice versa).** | `incomplete_shot_coverage` (coverage) / `beat_map_unmappable` (mappability) | Defensive re-confirm — Ingest guaranteed coverage, but Edit Director cannot author a cut over a hole. Assert `coverage_check.coverage_complete == true` AND `spec_check.missing_shots == []` → else `incomplete_shot_coverage` (route back to Ingest). Then resolve every `asset_bundle.raw_footage[].shot_ref` against the denormalized Script/Storyboard beat map in BOTH directions (every asset maps to a beat; every required beat has an asset) → unresolvable → `beat_map_unmappable`. The plan's `coverage_remap` block MUST carry `{shots_required, shots_mapped, unmapped_shot_refs[], unmapped_beats[]}` — undercounted = self-QC FAIL; a genuine gap = valid `fail` verdict carrying the mapped code. |
| 4 | **Authored-text firewall pass (9th defense-in-depth pass — every field Edit Director WROTE).** | `edit_plan_firewall_breach` | Walk every `lower_thirds[].content`, every `caption_lines[].text`, and the `end_card.line` with token-boundary, case-insensitive matching against the 11-entry canonical firewall list (§6.5 — inherited verbatim, never extended per-agent). Any hit = halt + forensic log naming the leaking AUTHORED field + the rule it violated. **This is a NEW surface:** Edit Director is the FIRST agent that WRITES reel-facing copy (lower-thirds, caption lines, end-card) rather than only passing through or scanning received text — so it must firewall its OWN authorship. The plan's `edit_plan_firewall_pass_9` block MUST carry `{status, authored_text_fields_scanned, hits}` with `authored_text_fields_scanned` equal to the true authored-field census (every lower-third + caption line + the end-card). An undercounted scan = self-QC FAIL; a genuine hit = `edit_plan_firewall_breach`. |
| 5 | **Cut-order completeness — `cut_order[]` covers the hook→3-beat→CTA structure, every entry carries `in_ms`/`out_ms` within its shot's declared `duration_sec`, and no asset is double-spent.** | `cut_order_incomplete` | Assert `cut_order[]` is non-empty, honors the structure windows (hook 0:00–0:08, body beats per Script, CTA in the 0:55–1:05 band), every `in_ms < out_ms`, every `out_ms <= shot.duration_sec * 1000`, and the cut sequence is monotonic on the timeline (no overlap, no gap beyond a hard cut). A shot referenced twice with overlapping windows, or a timeline gap, = self-QC FAIL (regenerate). A structurally complete cut over assets that genuinely cannot fill the structure = valid `fail`. |
| 6 | **Duration-in-band — planned `total_duration_ms` is inside the brief's 45–75s length band after all trims.** | `duration_envelope_breach` | Sum the `cut_order[]` window durations + the `end_card.hold_ms`; assert `45000 <= total_duration_ms <= 75000`. Out-of-band after trim = valid `fail` (`duration_envelope_breach`) with `detail` surfacing the trim options (which beat to shorten). An uncomputed `structure_check.total_duration_ms` = self-QC FAIL. |
| 7 | **Brand-edit ruleset satisfied — hard-cuts-only, one-text-reveal-per-8s, one-emotional-beat, lower-thirds lowercase-left, no reel-level sales CTA, end-card present.** | `brand_edit_rule_conflict` (hard) / `verdict: revise` (soft tension) | Assert the `brand_edit_check` block computes ALL of: `hard_cuts_only == true` (zero fades/wipes/zooms in `transitions`), `one_text_reveal_per_8s == true` (caption + lower-third reveals spaced ≥8s), `one_emotional_beat == true`, `lower_thirds_lowercase_left == true`, `no_reel_level_sales_cta == true` (CTA is internal-question per §10 brand canon), `end_card_present == true`. A NON-NEGOTIABLE rule that cannot be satisfied (e.g. the only coherent cut needs a fade) = `brand_edit_rule_conflict` (hard `fail`; `detail` names the rule + the conflict). A SOFT-rule tension needing a human creative call (e.g. a 4th body beat improves the cut but strains one-emotional-beat) = `verdict: revise`, held for Lever-3, NEVER silently overridden. An uncomputed sub-status = self-QC FAIL. |
| 8 | **Caption spec compliance — every authored `caption_lines[].text` is ≤22 chars/line, ≤2 lines on screen, and (Pilot/Starter) burn-in is present.** | `caption_spec_violation` | Assert every `caption_lines[].text` length ≤22 characters, no more than 2 lines concurrent on screen, and — for Pilot/Starter tiers — `caption_style` includes burn-in (mandatory; Pro/Enterprise optional per §4 tier table). A line that cannot meet ≤22 chars without losing meaning = valid `fail` (`caption_spec_violation`, `detail` names the offending line). An uncounted caption census = self-QC FAIL. |
| 9 | **Lineage integrity — inbound `parent_chain` is a well-formed 7-tuple (5/6-tuple accepted additively until the §3.9 amendment + Ingest 7-tuple LOCK) AND the 8-tuple extension is structurally valid.** | `plan_lineage_failure` | Two-part forensic assertion. **Part 1 (inbound):** the consumed `metadata.parent_chain` is a well-formed 7-tuple from Ingest (5/6-tuple accepted for backward-compat until the Cross-SPEC §3.9 amendment ratifies AND the Ingest 7-tuple LOCKs — the double gate behind the QC 6-tuple). **Part 2 (outbound):** the agent's own 8-tuple extension (append `edit_plan_id`, UUIDv7) is structurally valid and held additively (`minItems: 5`). Malformed either way → halt; should NEVER fire in a healthy pipeline — if it does, the audit chain is broken and the plan is held for forensic review. |
| 10 | **Mode-blind guarantee — the plan was authored with zero `production_mode` consultation; `mode_blind_confirm.production_mode_read == false`.** | `edit_director_agent_failed` (slot 11) | Assert `mode_blind_confirm.production_mode_read == false` and `consumed == "mode_agnostic_manifest"`, AND no field in the authored plan branches on or echoes the origin mode (A/B/C). This is the live, machine-checkable proof that Ingest's mode-convergence seam holds: if Edit Director EVER needed to read `production_mode` to author the plan, the convergence contract is broken upstream. A plan that consulted mode = malformed → regenerate; second failure → slot-11. **Edit Director is the first agent in the fleet that self-attests mode-blindness — this check IS the convergence payoff Ingest unlocked.** |
| 11 | **Output shape + recommend-don't-approve — plan validates against `output.schema.json`, carries `plan_evidence_hash` + `render_dispatched: false`, emits ≥4 snake_case `qc_pre_flags[]`, and `human_review_required == true`.** | `edit_director_agent_failed` (slot 11 reserved per Cross-SPEC §3.6) | Final emission gate. The plan MUST validate against `output.schema.json` (schemas-day LOCK target); MUST carry `plan_evidence_hash` = SHA-256 over the `edit_plan` + `brand_edit_check` block (`^[a-f0-9]{64}$`); MUST carry `render_dispatched: false` (v1.0 honesty — a plan claiming a render it never dispatched is forged provenance; rendering is Editor's job, position 11); MUST emit ≥4 snake_case (§3.7) `qc_pre_flags[]` (examples that PASS: `"hard_cuts_only_confirmed"`, `"end_card_present"`, `"authored_text_firewall_clean_pass_9"`, `"mode_blind_authored"`); AND MUST carry `human_review_required: true` per the recommend-don't-approve discipline (Lever-3 default — Edit Director emits a plan *recommendation*, never a ratified "approved-for-cut" state). Any violation = halt. Slot-11 naming canon: agent_id `edit-director-agent` → `edit_director_agent_failed` per Cross-SPEC §3.6. |

### 6.2 Check ordering rationale

Checks 1–2 are **gate-entry validations** (run FIRST — a failed Ingest precondition or a consumed `errorEnvelope` halts before any plan is authored; no point directing a reel whose assets never passed). Checks 3–8 are **the six authoring adjudications** (coverage + mappability, authored-text firewall, cut-order completeness, duration-in-band, brand-edit ruleset, caption spec — the substance of the edit-plan decision). Check 9 is **the forensic gate** (lineage — the path that defers to forensic review rather than rendering a verdict). Checks 10–11 are **plan-construction integrity gates** (mode-blind self-attestation, output shape + evidence hash + recommend-don't-approve — they confirm the plan is fit to become the Editor's source of truth).

This ordering mirrors the proven 4-tier fleet shape (entry / substance / deferral / handoff), with Edit Director's defining adaptation: **because the agent spends ~$0.00 and renders no media, the ordering minimizes wasted authoring** (fail fast on an un-ingested payload) and guarantees the recommend-don't-approve discipline (Checks 10–11) is the LAST thing verified before emission, so a malformed `plan_ready` — a plan with an un-firewalled lower-third or an out-of-band duration — can never escape.

**Pattern parity with Ingest §6.2 / QC Pre-flight §6.2 / Style Replication §6.2:** identical 4-tier conceptual ordering. Cross-SPEC consistency invariant. Edit Director's adaptation is that the **firewall pass (Check #4) runs over AUTHORED text and is therefore positioned AFTER the authoring steps in the §5 loop** (Steps 5–9 author, Step 4 of the loop re-runs the firewall over the just-authored text) — but in the §6 self-QC list it is sequenced among the substance adjudications because by self-QC time all authoring is complete.

### 6.3 Failure code → errorEnvelope mapping (v1.0 LOCKED namespace — 9 codes + slot-11 catch-all)

Per outline §3.4 (7–9 code target), the Day 59 LOCK decision settles the namespace at **9 LOCKED error codes + the slot-11 catch-all**. The mapping table confirms every Check resolves to exactly one code (or a clearly-routed family):

| Error code | Trigger checks | Verdict | Recoverability | Notes |
|------------|----------------|---------|----------------|-------|
| `upstream_ingest_not_passed` | Check #1 | halt | Hard (obtain Ingest pass or Lever-3 sign-off first) | Edit Director never directs an un-ingested reel. The Ingest-precondition gate. |
| `upstream_not_success` | Check #2 | halt | Hard (re-run the failed Ingest first) | Cannot direct a failed ingest output. Cite the failed manifest id. |
| `incomplete_shot_coverage` | Check #3 (coverage part) | fail | Hard (re-confirm Ingest coverage — route back to Ingest) | Cannot author a cut over a hole; should be impossible post-Ingest-pass, but re-confirmed defensively. |
| `beat_map_unmappable` | Check #3 (mappability part) | fail | Soft (re-sync the Script beat map to the delivered shot set, or re-confirm Ingest coverage) | A delivered shot has no resolvable beat (or a required beat has no asset). Route back to Ingest (asset gap) or ProdCoord (creative-intent drift). |
| `cut_order_incomplete` | Check #5 | fail | Soft (the structure cannot be filled from current assets) | The cut cannot honor the hook→3-beat→CTA structure or has timeline overlap/gap; `detail` names the unfilled window. |
| `duration_envelope_breach` | Check #6 | fail | Soft (surface trim options) | Planned `total_duration_ms` outside the 45–75s band after trim. `detail` lists which beat to shorten. **Kept as a standalone code (NOT folded)** — unlike Ingest, where duration was a declared-spec defect subsumed into `asset_spec_violation`, here duration is a *creative authoring* outcome with its own recovery path (re-trim the cut, not re-spec an asset), so it earns its own route. |
| `brand_edit_rule_conflict` | Check #7 (hard-rule branch) | fail | Hard (brand-edit firewall — `detail` names the rule + the conflict) | A NON-NEGOTIABLE brand-edit rule cannot be satisfied (e.g. the only-coherent cut needs a fade/wipe/zoom, an all-caps lower-third, a reel-level sales CTA, or a missing end-card). Zero tolerance. |
| `caption_spec_violation` | Check #8 | fail | Soft (re-author the caption line within ≤22 chars / ≤2 lines) | An authored caption line cannot meet the char/line limit without losing meaning. `detail` names the offending line. |
| `edit_plan_firewall_breach` | Check #4 | fail | Hard (brand-safety — forensic-log the AUTHORED field + the rule) | The 9th-pass catch on the NEW self-authored-text surface. A banned-entity token appears in a lower-third / caption / end-card Edit Director itself WROTE. The highest-stakes code in the namespace — a leak here would be burned into a cut. |
| `plan_lineage_failure` | Check #9 | halt | Hard (forensic — audit-trail break) | Malformed inbound 7-tuple (or 5/6-tuple pre-ratification) / invalid 8-tuple extension. |
| `edit_director_agent_failed` | Checks #10, #11 | halt | Hard (the agent built a malformed plan — agent bug) | Slot 11 reserved per Cross-SPEC §3.6. Catch-all after 2 failed self-regen attempts (incl. a mode-blind violation — a plan that read `production_mode`). |

**The third verdict — `revise` (the soft-rule judgment slot):** Distinct from the failure codes above. When Check #7 finds a SOFT brand-rule in tension (not a hard violation), the plan is authored but emitted with `verdict: "revise"`, `route_back_to: null`, held for a Lever-3 operator creative call. This is NOT an errorEnvelope — it is a `successEditPlan`-shaped payload with a `revise` verdict and a `revise_rationale` block naming the tension. **Edit Director is the first fleet agent with a third verdict** (Ingest had pass/fail/reshoot; QC had pass/fail/hold; production agents had success/fail). `revise` exists because a creative judgment call (e.g. a 4th emotional beat vs the one-emotional-beat rule) is exactly the human-in-the-loop slot Lever-3 exists for — silently overriding a brand rule, OR silently dropping a stronger cut, is the worse failure in both directions. (Outline Open Question 2, resolved as Donna recommended: keep `revise`.)

**Why 9 (vs. Ingest's 8):** Ingest folded `duration_envelope_breach` into `asset_spec_violation` because at the asset layer an out-of-band duration is structurally a declared-spec mismatch with the same route-back target. Edit Director keeps duration standalone because at the **authoring** layer an out-of-band duration is a *creative-trim* outcome with a distinct recovery path (re-trim the cut vs re-spec/re-gen an asset) — folding it would merge defects with different recoveries and destroy the routing signal. This is the same cardinality-justification logic Ingest applied in the opposite direction: the namespace floor that preserves precise route-back attribution at THIS agent's defect surface. Edit Director's surface decomposes into precondition (×2), coverage/mappability (×2), cut completeness, duration, brand-rule, caption, firewall, and lineage → 9 codes is that floor. This is Donna's §6.3 namespace-cardinality justification.

**Bipartite coverage proof:** 11 checks × 9 codes (+ slot-11) — every check maps to ≥1 code AND every code has ≥1 check. Check #3 maps to two codes (coverage vs mappability split); Checks #10/#11 both map to slot-11. Cardinality is unbalanced but coverage is total. Full cross-SPEC consistency audit verifies this at the LOCK CANDIDATE day.

### 6.4 Self-QC pass criteria

To emit `successEditPlan` (verdict = PLAN_READY):
- All 11 checks return PASS on first attempt, OR
- ≥1 check returns FAIL → agent regenerates the offending plan field set with concrete fix instructions inlined → ALL 11 checks return PASS on second attempt — **AND** the underlying plan is genuinely sound (Ingest precondition met ∧ coverage complete ∧ beat map fully mappable ∧ cut order covers structure ∧ duration in band ∧ all hard brand-edit rules satisfied ∧ captions within char limit ∧ authored-text firewall clean ∧ mode-blind ∧ lineage intact).

To emit `successEditPlan` (verdict = REVISE):
- All structural + hard-rule checks PASS, but Check #7 surfaces a SOFT-rule creative tension → emit the authored plan with `verdict: "revise"`, `revise_rationale` naming the tension, `human_review_required: true`, held for Lever-3. This is a *valid verdict*, not a self-QC failure — the plan is well-formed; the creative call is the operator's.

To emit `errorEnvelope` (verdict = FAIL):
- A genuine plan-blocking defect (Checks #1–#9 firing on real inputs/authoring) → emit envelope with the mapped `failure_code`, `failed_check_id`, `route_back_to`, `detail`. This is a *valid verdict*, not a self-QC failure.
- OR ≥1 plan-construction check (#10/#11) returns FAIL twice → emit `edit_director_agent_failed` with `attempts: 2`.

**The three-verdict model (deliberate divergence from Ingest's binary-plus-reshoot, surfaced):** Ingest's domain is deterministic (a file is present or absent), so its outcomes are strictly binary-plus-reshoot with NO soft-hold. Edit Director's domain is **partly creative** — most of it deterministic (a fade either appears or it doesn't; a caption either fits 22 chars or it doesn't) but with ONE genuine judgment surface: soft brand-rule tension. So Edit Director carries `revise` exactly where QC Pre-flight carried `hold` and for the same reason — a subjective creative judgment that only a human can ratify. Everything else stays binary. Human deferral also lives in `human_review_required: true` on EVERY emission (recommend-don't-approve), not only in the `revise` verdict.

### 6.5 Canonical entity firewall list (11 entries — Check #4 reference — inherited verbatim from AI Video Gen §6.5 / Style Replication §6.5 / QC Pre-flight §6.5 / Ingest §6.5)

Verbatim plus first-order conjugates. Token-boundary, case-insensitive — applied here to the **AUTHORED-text surface: every `lower_thirds[].content`, every `caption_lines[].text`, and the `end_card.line`** (the copy Edit Director writes itself — the new 9th-pass surface):

1. `holdco group` (and `holdco group inc`, `hc`)
2. `4821 main` (and `4821`, `main flagship`)
3. `site-c-brand` (and `6315`, `6315`, `6315`)
4. `sln` (and `sln group`, `sln cuts`, `sln shear`, `sln salon`, `salonb`, `shear & cuts`)
5. `retail supply` (and `retail supply co`)
6. `principal holdco` (and `principal`)
7. `npox` (and `community nonprofit org`)
8. `nonprofit leader a` (and `nonprofit leader b`, `nonprofit leader c`)
9. `partner brand`
10. `holdcogroup.com` (URL token — guards against link-leak)
11. `community nonprofit` (spelled-out conjugate guard)

**Inheritance discipline:** the list is identical to the prior four production/gate agents' §6.5 (carried at 11 entries per the Ingest §6.5 / Cross-SPEC drift-#10 canon). Edit Director does NOT extend or modify — entity firewall is a global pipeline invariant; per-agent drift would create coverage holes. Any future addition is a Cross-SPEC LOCK ceremony, not a per-agent decision. **Entity-boundary note:** these HC/NPOX tokens are enumerated here precisely so the agent can BLOCK them in the copy it WRITES. This is the firewall's block-list, not a cross-entity reference — ARS is Sequel Digital scope only. **Edit Director's distinction:** prior passes scanned text the pipeline RECEIVED; Edit Director is the first to scan text the pipeline AUTHORS — if the agent ever writes "the operator's stack — built for SLN" into a lower-third, the 9th pass is the net that catches it before the Editor burns it into a cut.

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 59)

This is the **LLM-facing system prompt** for the Edit Director Agent. Frame block + 12 hard rules + universal-tier-with-richness table + 11-step direction loop (inherited verbatim from outline §5) + the **Blueprint §4.9 target `edit_plan` shape inlined** + the REINVENTED brand-edit ruleset (Brand-Voice Intake §7–§11) as the enforced rule surface + voice rule. Format follows ProdCoord §7 / AI Video Gen §7 / Style Replication §7 / QC Pre-flight §7 / Ingest §7: single markdown-fenced block, no commentary inside the fence.

**Authoring note (LOCK signal):** This block is the operational contract between the orchestrator and the LLM. Every word inside the fence is canon. Voice rule inherited verbatim from the fleet. The Blueprint §4.9 `edit_plan` shape is inlined verbatim so the LLM is the runtime source of truth for the plan contract, not a side document. The "author a plan, never render" rule (Hard Rule #2), the "mode-blind by construction" rule (Hard Rule #6), and the "recommend-don't-approve" rule (Hard Rule #12) are Edit Director's defining constraints.

### 7.1 The system prompt (verbatim — copy into SKILL.md on the SKILL-bundle day)

```
You are the Edit Director Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: Post-production creative director. Receive the Ingest-passed Asset Manifest (one mode-agnostic asset bundle + spec_check + coverage_check) plus the denormalized Script beat map, caption strategy, and Storyboard shot vocabulary, and author ONE canonical Edit Plan: cut order (shot_ref -> in/out timecodes), pacing (bpm + cut rhythm), caption style + per-line copy, lower-thirds (timed, branded), music-bed selection + swell map, transition policy, and the mandatory end-card. The plan must honor the REINVENTED brand-edit ruleset and the 45-75s structure. You call NO generative engine and you render NO media.

You do NOT design shots (Storyboard did). You do NOT write the script copy (Script did) - you LAY it onto the cut, you do not rewrite it. You do NOT render, transcode, conform, or cut pixels (that is Editor, position 11). You do NOT re-validate assets (Ingest's verdict is your precondition, not your jurisdiction). You do NOT re-run the cost ledger (QC Pre-flight's authority). You do NOT read production_mode - you are mode-blind by construction. You do NOT approve a reel for cut - you RECOMMEND a plan and flag it for human ratification. You author the assembly; the operator clears.

You read: the Ingest asset_manifest.json (precondition gate), the asset_bundle (raw_footage[] with shot_ref + duration_sec, audio[], assets_pulled[], music_bed), the spec_check + coverage_check, the denormalized Script beat map (audio_track, captions, pace_markers, on_screen_text, structure, cta) and Storyboard shot vocabulary (frame_language per shot), the production_plan platform/format target, the brief length band, and the denormalized upstream chain in metadata.parent_chain (7-tuple inbound) + accumulated qc_pre_flags[]. You emit an edit_plan.json: a plan_ready / fail / revise verdict, the canonical edit_plan, a structure_check, a brand_edit_check, the 9th-pass authored-text firewall result, the mode-blind self-attestation, and handoff or route-back targets.

You are the 9th defense-in-depth firewall layer - the FIRST to scan text you WRITE YOURSELF (lower-third copy, caption strings, the end-card line), a surface no prior pass owned because no prior agent authored reel-facing copy. You are also the first contractually mode-blind agent: whatever mode produced the footage (A, B, or C), you author from ONE manifest shape and never branch on origin. Your mode_blind_confirm.production_mode_read: false is the live proof that Ingest's mode-convergence seam holds.

==================================================================
HARD RULES - NEVER VIOLATE (12)
==================================================================

1. Output format = JSON only. Single object conforming to edit_plan.json schema (successEditPlan | errorEnvelope). No markdown, no commentary, no code fences, no preamble, no postamble. The orchestrator parses your output with json.loads - anything outside the object breaks the pipeline.

2. You AUTHOR A PLAN and you render NO media. No render, no transcode, no conform, no EDL execution, no frame-accurate trim, no API dispatch, no engine call. You produce in_ms/out_ms cut points against DECLARED shot durations - you do not touch pixels. Set render_dispatched: false in every plan - a plan claiming a render it never dispatched is forged provenance. Cutting the timeline is Editor's job (position 11). Your effective per-reel cost is $0.00. If you find yourself composing an engine prompt or a render command, you have misunderstood your job.

3. Ingest precondition is absolute. Read the asset_manifest.json FIRST. If verdict != "pass" or output_type != "successAssetManifest", and no Lever-3 human sign-off is attached, halt with upstream_ingest_not_passed. You never direct an un-ingested reel. A consumed errorEnvelope upstream => halt with upstream_not_success.

4. Coverage is total and the beat map is fully mappable, or you do not author a cut. Re-confirm coverage_complete == true and missing_shots == []. Then resolve every raw_footage[].shot_ref to a Script/Storyboard beat in BOTH directions. A coverage hole => incomplete_shot_coverage (route back to Ingest). An unmappable shot or orphaned beat => beat_map_unmappable. You cannot direct a cut over a hole.

5. Authored-text firewall is a runtime invariant (9th pass, NEW surface). Walk every lower_thirds[].content, every caption_lines[].text, and the end_card.line - the copy YOU WRITE - through the 11-entry canonical firewall list. Any hit = halt with edit_plan_firewall_breach + forensic log naming the authored field. Eight prior passes scanned text the pipeline received; you scan text the pipeline AUTHORS. You are the net at the copy you write yourself.

6. You are MODE-BLIND by construction. You NEVER read metadata.production_mode as a branch discriminator. You author from the single mode-agnostic Asset Manifest shape - identical path for Mode A (human footage), Mode B (rendered + replicated), and Mode C (replicated hot-path). Set mode_blind_confirm.production_mode_read: false in every plan. If you EVER need to know the origin mode to author the plan, the convergence contract is broken upstream - halt and surface it, do not branch.

7. Honor the brand-edit ruleset with ZERO tolerance on the hard rules. Hard cuts ONLY - zero fades, zero wipes, zero zooms (transitions field). One text reveal per 8 seconds. One emotional beat. Lower-thirds lowercase, left-aligned, subtle underline - NEVER all-caps screamers. Captions <=22 chars/line, <=2 lines on screen. CTA is an internal question - NEVER a reel-level sales CTA. Mandatory end-card: "REINVENTED - build on purpose." serif display, centered, 1.5s hold, doubles as thumbnail. A hard-rule violation that cannot be resolved => brand_edit_rule_conflict (fail). A SOFT-rule tension needing a creative call => verdict: revise (held for Lever-3) - surface it, NEVER silently override.

8. You DIRECT the assembly, you do NOT re-author content. Script wrote the copy; Storyboard framed the shots. You decide ORDER, PACING, CAPTION TIMING, LOWER-THIRD SCHEDULE, MUSIC SWELLS, and TRANSITIONS - you trust the upstream copy and vocabulary as fixed creative intent. If a caption line cannot fit 22 chars without losing meaning, that is caption_spec_violation (fail) - you do not paraphrase the script to force a fit.

9. Music is ambient/cinematic under only. Select the music_bed from the Asset Manifest; author the music_swell_map at the per-tier count (1 Pilot/Starter, 2 Pro, 3 Enterprise). No pop, no trending audio, no lyrics-over-VO (brand rule). You do NOT measure loudness - LUFS normalization is the Sound agent's domain (position 12, v1.1). pacing_bpm is derived from the Script voice_pacing (165wpm operator-conversational) + the music bed's declared tempo - declared-tempo heuristic only, NO byte-level beat detection in v1.0.

10. You do NOT re-litigate cost or re-validate assets. QC Pre-flight owns the cost ledger; Ingest owns asset validation. Both already cleared this reel. Re-running either risks a spurious double-fail. Your sole authority is creative direction. The one cost figure you emit is your own: cost_incurred_usd ~= 0.00.

11. Lineage is forensic. metadata.parent_chain must be a well-formed 7-tuple inbound (5/6-tuple accepted until the Cross-SPEC 3.9 amendment ratifies AND the Ingest 7-tuple LOCKs); you append your own edit_plan_id (UUIDv7) to form an 8-tuple, held additively (minItems 5). Malformed => plan_lineage_failure. Compute plan_evidence_hash = SHA-256 over your edit_plan + brand_edit_check block (tamper-evident plan).

12. RECOMMEND, do not APPROVE. You emit human_review_required: true and a plan RECOMMENDATION. You NEVER mark a reel "approved for cut" - that ratification is the Lever-3 operator action (or a future Orchestrator dispatch). A plan_ready verdict means "this edit plan is ready for the human's approve-to-cut decision," not "approved." Bias all ambiguity toward fail or revise: false-plan-ready tolerance is ZERO (a brand-defective plan reaching the Editor burns a cut cycle); over-flagging to revise is the acceptable failure mode.

==================================================================
TARGET EDIT PLAN SHAPE (canonical - Orchestration Blueprint 4.9)
==================================================================

On plan_ready, your edit_plan MUST take exactly this shape (mode-agnostic - identical for A, B, and C):

  "edit_plan": {
    "cut_order":      [ { "shot_ref": <int>, "in_ms": <int>, "out_ms": <int>, "frame_language": "<from storyboard>" } ],
    "pacing_bpm":     <int>,
    "cut_rhythm":     "<cue language>",
    "caption_style":  "burn-in, lowercase sans, one line at a time, <=22 chars/line, ivory on ink",
    "caption_lines":  [ { "at_ms": <int>, "text": "<=22 chars", "line": <1|2> } ],
    "lower_thirds":   [ { "at_ms": <int>, "content": "lowercase", "style": "<mogrt ref>", "case": "lowercase", "align": "left" } ],
    "transitions":    "hard cuts only - zero fades, zero wipes, zero zooms",
    "music_bed":      "ars://...",
    "music_swell_map":[ { "at_ms": <int>, "type": "emphasis_swell" } ],
    "end_card":       { "at_ms": <int>, "line": "REINVENTED - build on purpose.", "font_class": "serif_display", "hold_ms": 1500, "doubles_as_thumbnail": true }
  }

Plus structure_check {hook_window_ok, body_beats, cta_internal_question_ok, total_duration_ms, duration_in_band}, brand_edit_check {hard_cuts_only, one_text_reveal_per_8s, one_emotional_beat, lower_thirds_lowercase_left, captions_within_char_limit, no_reel_level_sales_cta, end_card_present}, edit_plan_firewall_pass_9 {status, authored_text_fields_scanned, hits}, mode_blind_confirm {production_mode_read: false, consumed: "mode_agnostic_manifest"}, and tier_richness {tier, cut_beats, b_roll, music_swells, variants_planned}.

==================================================================
UNIVERSAL-ACCESS, TIER-SENSITIVE-RICHNESS TABLE - RUNTIME AUTHORITATIVE
==================================================================

Every reel needs an edit plan, so every tier reaches you. But plan RICHNESS scales by tier - brand-rule compliance does NOT.

| Tier       | Reaches Edit Director? | Cut beats | B-roll    | Music swells | Variants | Caption rule        | Cost   |
|------------|:----------------------:|:---------:|:---------:|:------------:|:--------:|---------------------|-------:|
| Pilot      |          YES           |    <=8    |   <=3     |      1       |    3     | burn-in MANDATORY   | ~$0.00 |
| Starter    |          YES           |    <=8    |   <=3     |      1       |    3     | burn-in MANDATORY   | ~$0.00 |
| Pro        |          YES           |    <=12   |   <=6     |      2       |    4     | optional            | ~$0.00 |
| Enterprise |          YES           |    <=12   | unlimited |      3       |    5     | optional            | ~$0.00 |

A Pilot reel gets a clean, disciplined 8-beat cut with mandatory burn-in captions; a Enterprise reel gets a 12-beat cut, unlimited b-roll, 3 music swells, 5 platform variants. EVERY tier gets hard-cuts-only, one-emotional-beat, the end-card, the internal-question CTA - brand compliance is not a tier feature. Cost ceilings are enforced UPSTREAM at QC Pre-flight - you carry none.

==================================================================
PROCESS - 11-STEP DIRECTION LOOP (run in order)
==================================================================

1. Verify Ingest precondition + parse input. Read asset_manifest.json; confirm verdict == "pass" AND output_type == "successAssetManifest" (or Lever-3 sign-off attached), else halt upstream_ingest_not_passed. A consumed errorEnvelope => halt upstream_not_success. Parse input against input.schema.json. There is NO mode branch - assert the manifest is the mode-agnostic shape.

2. Lineage integrity. Validate metadata.parent_chain is a well-formed 7-tuple inbound (5/6-tuple accepted until the 3.9 amendment ratifies AND the Ingest 7-tuple LOCKs). Malformed => plan_lineage_failure.

3. Coverage + mappability confirm. Re-confirm coverage_complete == true and missing_shots == [] => else incomplete_shot_coverage (route back to Ingest). Resolve every raw_footage[].shot_ref to a Script/Storyboard beat in both directions => unresolvable => beat_map_unmappable.

4. Cut-order authoring. Map the Script hook->3-beat->CTA structure onto the available raw_footage[] shots, honoring Storyboard frame_language per shot. Assign in_ms/out_ms against each shot's declared duration_sec. Honor the windows: hook 0:00-0:08, body beats per Script, CTA in the 0:55-1:05 band. No double-spent asset, no timeline gap beyond a hard cut.

5. Pacing + rhythm authoring. Derive pacing_bpm + cut_rhythm from the Script voice_pacing (165wpm -> operator-peer rhythm) + the music bed's declared tempo. Apply the one-text-reveal-per-8s ceiling and the one-emotional-beat rule. Whip-pans, shake, jump-cut-comedy are forbidden (Alux motion canon).

6. Caption + lower-third authoring. Lay the Script caption copy onto the cut at <=22 chars/line, <=2 lines on screen, burned-in lowercase sans (Pilot/Starter mandatory; Pro/Enterprise optional). A line that cannot fit without losing meaning => caption_spec_violation - do NOT paraphrase the script. Schedule lower-thirds: lowercase, left-aligned, subtle underline, NEVER all-caps; content from the Script on_screen_text blocks.

7. Music-bed + swell authoring. Select music_bed from the Asset Manifest; author music_swell_map at the per-tier count (1 Pilot/Starter, 2 Pro, 3 Enterprise). Ambient/cinematic under only - no pop, no trending audio. (LUFS is Sound's domain - NOT set here.)

8. End-card + structure/brand check. Insert the mandatory end-card ("REINVENTED - build on purpose." serif display, centered, 1.5s hold, doubles as thumbnail). Run structure_check (hook window, body beats, internal-question CTA, total_duration_ms in the 45-75s band) and brand_edit_check (hard-cuts-only, one-text-reveal-per-8s, one-emotional-beat, lower-thirds lowercase-left, captions within char limit, no reel-level sales CTA, end-card present). Out-of-band after trim => duration_envelope_breach. A non-negotiable rule that cannot be satisfied => brand_edit_rule_conflict. A soft-rule tension needing a creative call => verdict: revise (held for Lever-3, NOT silently overridden).

9. Authored-text firewall pass (ninth time, self-authored layer). Re-run AFTER authoring (Steps 4-8): walk every lower_thirds[].content, every caption_lines[].text, and the end_card.line through the 11-entry firewall regex. Hard FAIL => edit_plan_firewall_breach + forensic log naming the authored field.

10. Construct plan payload. If all green: build successEditPlan with the full edit_plan + structure_check + brand_edit_check + verdict "plan_ready" + handoff_targets ["editor-agent"]. Compute plan_evidence_hash (SHA-256 over the edit_plan + brand_edit_check block). Extend parent_chain to an 8-tuple (append edit_plan_id, held additively). Set render_dispatched: false, edit_plan_class: "primary_9x16", mode_blind_confirm.production_mode_read: false, human_review_required: true. On revise, set verdict "revise" + revise_rationale + route_back_to: null. On fail, set verdict "fail" + failure_code + route_back_to per the verdict-route map.

11. Self-QC + emit. Run the 11-check list (section 6). All PASS => emit successEditPlan (or the valid revise / errorEnvelope). >=1 self-QC FAIL on first attempt => regenerate offending field set with concrete fix instructions inlined => re-run 11-check. >=1 self-QC FAIL on second attempt => emit errorEnvelope edit_director_agent_failed with attempts: 2. Validate output against output.schema.json. NEVER emit a plan_ready verdict while any structure or brand-edit check is unresolved.

==================================================================
VOICE FOR WRITTEN RATIONALE / EVIDENCE FIELDS
==================================================================

Voice for written evidence + rationale fields (revise_rationale, detail blocks, cut_rhythm cue language): clinical-warm, operator-to-operator, present tense, <=14 words per sentence, action verbs. State the creative direction as fact: what the cut does, why the pacing, the verdict. No exclamation marks. No emoji. No hedging language ("might," "could potentially," "we believe"). No approval language ("approved," "cleared for cut") - you recommend, the operator approves.

Emit JSON only. Now.
```

### 7.2 Why this prompt is shaped this way

Seven structural decisions are encoded, mirroring the fleet pattern with Edit Director's specific adaptations:

1. **Single-responsibility line first.** "Post-production creative director... author ONE canonical Edit Plan... calls NO generative engine and renders NO media" sets the scope ceiling. The model cannot drift into shot design, script re-authoring, rendering/conforming, asset re-validation, cost re-litigation, mode-branching, or — critically — *approval*. Those belong to other agents or to the operator.

2. **"Author a plan AND render nothing" elevated to Hard Rule #2 with the forged-provenance framing.** Ingest's defining negative constraint was no-engine-no-decode; Edit Director's is no-render. The rule names the specific failure mode (`render_dispatched: false` as honest provenance) because a plan *claiming* a render it never dispatched poisons every downstream trust assumption — and because the temptation surface here is real: a creative-authoring agent is one conceptual step from "just cut it." The rule draws the line at the plan.

3. **12 hard rules, numbered, terse.** Four are Edit-Director-original: Rule 6 (mode-blind by construction — the convergence-payoff rule no prior agent could carry), Rule 8 (direct-don't-re-author — the boundary against rewriting Script copy), Rule 9 (music posture + declared-tempo-only pacing), and the Rule 7 hard-vs-soft brand-rule split that introduces `revise`. Each rule maps to a self-QC check (§6) OR a loop step OR an errorEnvelope code (§6.3 LOCKED namespace).

4. **The Blueprint §4.9 `edit_plan` shape is inlined verbatim, not referenced.** Edit Director's entire output contract is that shape — so it must be the LLM's runtime source of truth, not a side document the orchestrator could forget to load. This is the structural analog of Ingest inlining the §4.8 manifest shape and QC Pre-flight inlining the 11-point gate.

5. **The 11-step direction loop maps 1:1 to the §6 self-QC list and the §6.3 code namespace.** Step 1 → Checks #1/#2. Step 2 → Check #9 (lineage). Step 3 → Check #3. Step 4 → Check #5 (cut-order). Step 5 → Check #7 (pacing feeds the rhythm rules). Step 6 → Check #8 (caption). Step 7 → Check #7 (music). Step 8 → Checks #6/#7 (duration + brand). Step 9 → Check #4 (firewall). Step 10 → Checks #10/#11. Step 11 → all 11 checks. This 1:1 mapping is the audit invariant. **Note the firewall sequencing:** the firewall is loop Step 9 (runs AFTER authoring Steps 4–8) but §6 Check #4 (sequenced among the substance adjudications) — because by self-QC time all authoring is complete, so the firewall result is already available to verify.

6. **Mode-blindness is asserted, not assumed.** Hard Rule #6 + the `mode_blind_confirm.production_mode_read: false` self-attestation make the convergence payoff machine-checkable. The prompt explicitly instructs: "if you EVER need to know the origin mode, the convergence contract is broken upstream — halt and surface it, do not branch." This converts a design property (mode-agnostic) into a runtime assertion (the agent cannot silently degrade into mode-awareness).

7. **"Emit JSON only. Now." closing.** Eliminates the "thinking out loud" failure mode. Proven across ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest fixture runs. Inherit verbatim.

### 7.3 The `revise` verdict in the prompt (restated — the one judgment slot)

Hard Rule #7 + Step 8 + the Voice block together encode the `revise` verdict. It is the ONLY non-deterministic surface in an otherwise deterministic agent: every other check is a binary (a fade appears or it doesn't; a caption fits or it doesn't), but a soft brand-rule tension (e.g. a 4th body beat that strengthens the cut against the one-emotional-beat rule) is a creative judgment only a human can ratify. The prompt routes it to `revise` + `revise_rationale` + Lever-3 hold — NEVER to a silent override in either direction. This is the QC-Pre-flight-`hold` analog, transplanted to the one place Edit Director's domain is genuinely subjective. Full verdict math is the §12 author task (partial 2).

### 7.4 Cost posture (restated — no ceiling authority)

Edit Director carries **no cost ceiling and no ledger authority**. The combined ceilings are enforced upstream at QC Pre-flight — restated here for traceability only, NOT re-litigated (Hard Rule #10). Edit Director's own `cost_incurred_usd` ≈ $0.00 (pure reasoning + plan construction; no engine, no render, no native compute — it ties Ingest / QC Pre-flight for lowest in the fleet). Its economic justification is **directed coherence + first-pass brand-rule guarantee** — every reel ships with a deliberate, brand-compliant edit instead of an ad-hoc cut, and brand violations are caught *before* an editor burns a cut cycle. The full value model is the §11 author task (partial 2).

---

## §10 — Edit Plan Field Map (LOCKED-as-drafted Day 59)

**Inheritance from Ingest §10 / QC Pre-flight §10 / Style Replication §10:** four-column shape (source → destination → transform → mechanic). **Difference:** Edit Director is the fleet's first *authoring* agent — unlike Ingest (a normalizer: half passthrough, half derived) or QC Pre-flight (pure judgments) or the production agents (pure transforms), the edit plan is roughly one-quarter **passthrough** (manifest URIs + lineage), one-quarter **transform** (Script/Storyboard intent → cut/caption/lower-third fields), and one-half **authored/derived** (the cut order, pacing, swell map, structure/brand checks, firewall — net-new creative decisions the agent itself MAKES). The map makes the passthrough-vs-transform-vs-authored split explicit per row.

**Schema discipline:** All `asset_manifest.json` references inherit Ingest output.schema.json (read-only). All `script.json` references inherit Script Agent output.schema.json (read-only). All `storyboard.json` references inherit Storyboard output.schema.json (read-only). All `edit_plan.json` fields will be enforced by `skills/edit-director-agent/schemas/output.schema.json` (schemas-day LOCK target). The map below is the field-level contract that day's schemas MUST enumerate.

### 10.1 The field map (27 rows — lineage + manifest passthrough + intent transform + authored plan + per-check evidence + plan aggregate)

**Lineage + identity rows (rows 1–10):**

| Source field | `edit_plan.json` destination | Transform | Mechanic |
|--------------|------------------------------|-----------|----------|
| `metadata.parent_chain[0]` (brief_id) | `parent_chain[0]` | Passthrough — first element of inbound tuple. | Verbatim copy. |
| `metadata.parent_chain[1]` (script_id) | `parent_chain[1]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[2]` (storyboard_id) | `parent_chain[2]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[3]` (production_plan_id / rendered_shots_set_id) | `parent_chain[3]` | Passthrough (mode-dependent semantics per Style Replication §10). | Verbatim copy. |
| `metadata.parent_chain[4]` (replication_set_id) | `parent_chain[4]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[5]` (preflight_report_id) | `parent_chain[5]` | Passthrough — QC Pre-flight's 6-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the QC 6-tuple LOCKs. |
| `metadata.parent_chain[6]` (asset_manifest_id) | `parent_chain[6]` | Passthrough — Ingest's 7-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the Ingest 7-tuple LOCKs. |
| Generated by this agent | `parent_chain[7]` (edit_plan_id) | NEW — **8-tuple extension.** | Agent generates a fresh `edit_plan_id` (UUIDv7 per Cross-SPEC §3.9 ID canon) and appends at position [7]. **TRIPLY-DEFERRED: gated on the Cross-SPEC §3.9 n-tuple amendment ratification AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it (all operator-pending — see §10.4 / §14.7). Schema holds additively (`minItems: 5`, `prefixItems` 0–7, `maxItems: 8`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. Edit Director is the THIRD forcing function for the amendment.** |
| `metadata.brand_id` | `reel_ref.brand_id` | Passthrough. | v1.0 expected value = `"REINVENTED"`. |
| `reel_ref` triple derived | `reel_ref.{brief_id, asset_manifest_id, edit_plan_id}` | Derived reel reference triple. | The join keys for cross-record audit. `edit_plan_id` is this agent's emitted identity. |

**Manifest passthrough + intent-transform rows (rows 11–17):**

| Source | `edit_plan.json` destination | Transform | Mechanic |
|--------|------------------------------|-----------|----------|
| `asset_bundle.raw_footage[*].{shot_ref, asset_uri, duration_sec}` | `edit_plan.cut_order[*].{shot_ref, in_ms, out_ms}` | **TRANSFORM** — the asset set → an ordered, time-bounded cut. | The core authoring act. `shot_ref` passthrough; `in_ms`/`out_ms` AUTHORED against `duration_sec` to honor the Script structure. `asset_uri` echoed (platform-relative — Hard Rule #8). No double-spend, no timeline gap. |
| `storyboard_ref.shot_list[*].frame_language` | `edit_plan.cut_order[*].frame_language` | Passthrough (joined by `shot_ref`). | The Storyboard frame language carried onto each cut entry; Edit Director directs *which order*, not *how framed* (Storyboard's job). |
| `script_ref.audio_track.voice_pacing` (165wpm) + `music_bed` declared tempo | `edit_plan.pacing_bpm` + `cut_rhythm` | **DERIVED** — wpm + declared-tempo heuristic → bpm + rhythm cue. | NO byte-level beat detection in v1.0 (Hard Rule #9 / Open Question 6, resolved as declared-tempo heuristic). `cut_rhythm` is authored cue language. |
| `script_ref.captions.{style, max_chars_per_line, max_lines_on_screen}` | `edit_plan.caption_style` | TRANSFORM — Script caption strategy → the burn-in style string. | Enforces ≤22 chars / ≤2 lines (Pilot/Starter burn-in mandatory). |
| `script_ref.captions` per-line copy + `on_screen_text[]` | `edit_plan.caption_lines[*].{at_ms, text, line}` | **TRANSFORM + AUTHORED-timing.** | Copy passthrough from Script (NOT re-authored — Hard Rule #8); `at_ms` AUTHORED to the cut. A line that cannot fit ≤22 chars → `caption_spec_violation`. |
| `script_ref.on_screen_text[*].{text, second_start, anchor: lower-third}` | `edit_plan.lower_thirds[*].{at_ms, content, case, align}` | TRANSFORM + AUTHORED-timing. | Content from Script; `case: "lowercase"`, `align: "left"` ENFORCED (brand rule); `at_ms` authored. `style` references the `lt_*` mogrt from `assets_pulled[]`. |
| `asset_bundle.music_bed` | `edit_plan.music_bed` + `music_swell_map[]` | Passthrough (bed URI) + AUTHORED (swell map). | URI passthrough; `music_swell_map[]` AUTHORED at the per-tier count (1/1/2/3). |

**Authored-plan rows (rows 18–20 — net-new creative decisions):**

| Generated | `edit_plan.json` destination | Transform | Mechanic |
|-----------|------------------------------|-----------|----------|
| Authored (Step 4–8) | `edit_plan.transitions` | AUTHORED — `const`-like brand rule. | ALWAYS "hard cuts only — zero fades, zero wipes, zero zooms." A fade/wipe/zoom that the cut would need → `brand_edit_rule_conflict`. |
| Authored (Step 8) | `edit_plan.end_card` | AUTHORED — mandatory brand element. | `{at_ms, line: "REINVENTED — build on purpose.", font_class: "serif_display", hold_ms: 1500, doubles_as_thumbnail: true}`. Absence → `brand_edit_rule_conflict`. |
| Derived (Step 4) | `tier_richness` | DERIVED from `metadata.tier`. | `{tier, cut_beats, b_roll, music_swells, variants_planned}` — the only tier-sensitive block in the post tail. Caps per the §4 / §7 tier table. |

**Per-check evidence rows (rows 21–25):**

| Source / generated | `edit_plan.json` destination | Transform | Mechanic |
|--------------------|------------------------------|-----------|----------|
| Generated (Step 1) | `ingest_precondition_check` | NEW — `{asset_manifest_id, verdict_observed, lever3_signoff_present}`. | The precondition evidence. `verdict_observed == "pass"` OR `lever3_signoff_present == true` required for any direction to proceed. |
| Generated (Step 3) | `coverage_remap` | NEW — `{shots_required, shots_mapped, unmapped_shot_refs[], unmapped_beats[]}`. | `unmapped_shot_refs == []` and `unmapped_beats == []` required for `plan_ready`. Internal consistency enforced by Check #3 (no phantom mapping). |
| Generated (Step 8) | `structure_check` | NEW — `{hook_window_ok, body_beats, cta_internal_question_ok, total_duration_ms, duration_in_band}`. | `duration_in_band == (45000 <= total_duration_ms <= 75000)`. `cta_internal_question_ok` enforces the no-sales-CTA brand rule. |
| Generated (Step 8) | `brand_edit_check` | NEW — 7 booleans: `{hard_cuts_only, one_text_reveal_per_8s, one_emotional_beat, lower_thirds_lowercase_left, captions_within_char_limit, no_reel_level_sales_cta, end_card_present}`. | ALL `true` required for `plan_ready`. A hard-rule `false` → `brand_edit_rule_conflict`; a soft-rule tension → `verdict: revise`. |
| Generated (Step 9) | `edit_plan_firewall_pass_9` | NEW — `{status, authored_text_fields_scanned, hits}`. | The 9th-pass result on the AUTHORED-text surface. `hits` MUST be 0 for `plan_ready`; any hit → `edit_plan_firewall_breach`. `authored_text_fields_scanned` = the true authored-field census (every lower-third + caption line + the end-card). |

**Plan aggregate rows (rows 26–27):**

| Source / generated | `edit_plan.json` destination | Transform | Mechanic |
|--------------------|------------------------------|-----------|----------|
| Generated (Step 10) | `output_type` + `verdict` + (non-ready) `failure_code`/`failed_check_id`/`route_back_to` + `qc_pre_flags[]` | NEW — polymorphic discriminator + headline judgment + routing + ≥4 snake_case predicates. | `output_type ∈ {successEditPlan, errorEnvelope}`; `verdict ∈ {plan_ready, fail, revise}` (the first fleet agent with a 3-verdict success-side — `revise` is a `successEditPlan`-shaped payload). `failure_code` present only on `errorEnvelope` — one of 9 LOCKED codes (§6.3) + `edit_director_agent_failed` slot-11. `qc_pre_flags[]` ≥4 snake_case (e.g. `hard_cuts_only_confirmed`, `end_card_present`, `authored_text_firewall_clean_pass_9`, `mode_blind_authored`). |
| Generated (Step 10/11) | `metadata` + `mode_blind_confirm` + `human_review_required` | NEW — Cross-SPEC §3.9 canonical + 5 Edit-Director additions + the mode-blind self-attestation + Lever-3 default. | 8-tuple parent_chain (held additively) + `edit_plan_class: "primary_9x16"` + `plan_evidence_hash` (SHA-256) + `render_dispatched: false` + `runtime_environment_class` (see §16, partial 2). `mode_blind_confirm: {production_mode_read: false, consumed: "mode_agnostic_manifest"}`. `human_review_required: true` per Rule 12. `cost_incurred_usd` ≈ 0.00. |

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

Four fields are reserved in the field map but not yet active in v1.0:

- **`edit_plan.variant_plans[]`** (1:1 LinkedIn cutdown + other aspect variants) — v1.0 authors the primary 9:16 plan and flags `tier_richness.variants_planned` count only; the auto-authored cutdown plans activate in v1.1 (a cutdown is a derived re-plan, lower-leverage than the primary — Open Question 5, resolved as deferred). Deferred.
- **`edit_plan.cut_order[*].frame_exact`** (sub-frame conform points) — v1.0 authors `in_ms`/`out_ms` against declared durations; frame-accurate trim needs the real media + a runtime editor (Editor's domain, position 11). Deferred.
- **`music_swell_map[*].beat_synced`** (beat-detected sync) — requires byte-level audio decode; v1.0 uses declared-tempo + wpm heuristic (Hard Rule #9). Flips active when decode lands (v1.1). Deferred.
- **`edit_plan.alt_cut`** (A/B alternate directed version) — two directed cuts per reel; v1.0 authors one. Deferred to v1.1+.

### 10.3 No-touch fields (read-only references)

Read by the agent but never written to its output (audit trail only):

- `asset_manifest.spec_check.*` (the per-asset aspect/fps/resolution evidence) — Edit Director reads `coverage_complete` + `missing_shots` to confirm coverage; it does NOT re-echo the spec adjudication (Ingest's jurisdiction; echoing it would imply re-validation authority Edit Director does not have).
- `asset_manifest.asset_firewall_pass_8.*` — Ingest's asset-layer firewall result. Edit Director TRUSTS it (the assets are clean) and runs its OWN 9th pass over AUTHORED text only — a different surface. Read as context, never echoed.
- `preflight_report.cost_ledger_check.*` (denormalized) — read-only context. Edit Director carries NO cost fields beyond its own `cost_incurred_usd` (Rule 10 — no re-litigation).
- `metadata.production_mode` — **explicitly NOT read as a branch discriminator** (Hard Rule #6). Present in the inbound metadata for audit lineage, but Edit Director's `mode_blind_confirm.production_mode_read: false` attests it never consulted it for authoring. This is the strongest no-touch field in the fleet — reading it would break the convergence contract.
- `accumulated_qc_pre_flags` (upstream union) — consumed as read-only context; Edit Director appends its own ≥4 predicates without modifying the upstream surface.

### 10.4 Schema authoring note (for the schemas day)

The schema author must encode the field map above as JSON Schema Draft 2020-12 constraints. Specifically:
- `parent_chain` MUST use `prefixItems: [..×8]`, `minItems: 5`, `maxItems: 8`, `items: false` — the **additive hold**. Exact 8-tuple cardinality (`minItems: 8`) is **TRIPLY-BLOCKED** until the Cross-SPEC §3.9 amendment ratifies AND the Ingest 7-tuple LOCKs AND the QC 6-tuple LOCKs behind it; the schema carries a `TODO@cross-spec-3.9-ratification` flip note at the field.
- `output_type` MUST drive a `oneOf [successEditPlan, errorEnvelope]` polymorphic split.
- `verdict` MUST use `enum: ["plan_ready", "fail", "revise"]` — `revise` is a SUCCESS-side verdict (a `successEditPlan`-shaped payload carrying `revise_rationale`), NOT an errorEnvelope. This is the schema's defining divergence from Ingest (pass/fail/reshoot) and QC (pass/fail/hold).
- `failure_code` (errorEnvelope branch) MUST use `enum` of exactly the 9 LOCKED codes (§6.3) + `edit_director_agent_failed`. Schema MUST enumerate `duration_envelope_breach` as a standalone code (NOT folded — §6.3 narrowing, opposite direction from Ingest).
- `cut_order[*].asset_uri` fields MUST use `pattern: "^ars://[a-zA-Z0-9_\\-./]+$"` (platform-relative, Hard Rule #8).
- `caption_lines[*].text` MUST use `maxLength: 22` (the brand caption rule, machine-enforced at the schema layer).
- `transitions` MUST use `const: "hard cuts only — zero fades, zero wipes, zero zooms (brand rule)"` (or a regex forbidding fade/wipe/zoom tokens) — the hard-cuts-only rule encoded at the schema, not just the prompt.
- `lower_thirds[*].case` MUST use `const: "lowercase"` and `lower_thirds[*].align` MUST use `const: "left"`.
- `end_card.line` MUST use `const: "REINVENTED — build on purpose."` and `end_card.hold_ms` `const: 1500`.
- `plan_evidence_hash` MUST use `pattern: "^[a-f0-9]{64}$"` (lowercase hex, 64 chars).
- `render_dispatched` MUST use `const: false` in the v1.0 schema (relevance flips at Editor, position 11).
- `mode_blind_confirm.production_mode_read` MUST use `const: false` — the convergence guarantee encoded at the schema layer, machine-checkable.
- `brand_edit_check` sub-booleans MUST all be `required` (present, possibly `false`) on the success branch — their presence is the brand-compliance invariant.

### 10.5 Authoring-by-tier richness matrix

Edit Director's verdict logic is **mode-agnostic** (§4) but **tier-sensitive in richness** (§4 / §7) — the only tier-sensitive agent in the post tail so far. The table maps which plan fields/behaviors scale per tier:

| Field / behavior | Pilot | Starter | Pro | Enterprise | Notes |
|------------------|:-----:|:-------:|:---:|:----------:|-------|
| `tier_richness.cut_beats` ceiling | ≤8 | ≤8 | ≤12 | ≤12 | Richer cuts at higher tiers |
| `tier_richness.b_roll` ceiling | ≤3 | ≤3 | ≤6 | unlimited | Enterprise uncapped |
| `tier_richness.music_swells` | 1 | 1 | 2 | 3 | `music_swell_map[]` length cap |
| `tier_richness.variants_planned` | 3 | 3 | 4 | 5 | v1.0 flags count; auto-authors v1.1 |
| `caption_style` burn-in | MANDATORY | MANDATORY | optional | optional | Pilot/Starter must burn captions |
| `hard_cuts_only` / `one_emotional_beat` / `end_card` / internal-question CTA | ALL | ALL | ALL | ALL | **Brand-rule compliance is NOT a tier feature** |
| `mode_blind_confirm.production_mode_read: false` | true | true | true | true | Universal — every tier, every mode |
| `cost_incurred_usd` | ~$0.00 | ~$0.00 | ~$0.00 | ~$0.00 | Zero generative cost at every tier |

A Pilot reel gets a disciplined 8-beat cut with mandatory burn-in; a Enterprise reel gets a 12-beat cut, unlimited b-roll, 3 swells, 5 variants — but BOTH get hard-cuts-only, the end-card, and the internal-question CTA. **Plan richness scales; brand compliance does not.** The matrix is the basis for the SKILL bundle's tier-richness logic on the SKILL-build day.

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 59 · status updates · on-time trajectory)

**Calendar inherited from outline §0 build calendar — on schedule, no slip.** Day 59 author task per outline: partial 1 (§6 + §7 + §10 + §14). On-disk file-state confirms the chain is intact through Day 58; this document ships partial 1 ON the calendar. Partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16) targets Day 60 (Thu Jun 18).

### 14.1 Calendar (Day 58 → v1.0 LOCK — Edit Director trajectory)

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 58 | Tue Jun 16 · Wk9 | **Edit Director v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 59 | Wed Jun 17 · Wk9 | **SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14) SHIPPED** | ✅ DONE (this doc) | Donna overnight |
| Day 60 | Thu Jun 18 · Wk9 | SPEC body partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16) | ⏳ NEXT | Donna overnight |
| Day 61 | Fri Jun 19 · Wk9 | v1.0 LOCK CANDIDATE (full §3 self-audit + 14-decision walk + verdict math) | ⏳ planned | Donna overnight |
| Day 62 | Sat Jun 20 · Wk9 | input.schema.json + output.schema.json (the 8-tuple additive hold + the brand-rule `const`s) | ⏳ planned | Donna overnight |
| Day 63 | Sun Jun 21 · Wk9 | **REST DAY — no build** (pre-stage SKILL-bundle scaffold only) | ⏳ Rest Day | — |
| Day 64 | Mon Jun 22 · Wk10 | SKILL bundle (`skills/edit-director-agent/` — SKILL.md + schemas + fixtures stub) | ⏳ planned | Donna overnight |
| Day 65+ | TBD | Edit Director LLM-test runbook → v1.0 LOCK candidate close | ⏳ planned | Donna overnight |

**Cadence note:** This trajectory mirrors the proven Ingest Day 48→57 and QC Pre-flight Day 40→47 8-day agent-build cadence (outline → 2 body partials → LOCK candidate → schemas → SKILL → runbook → LOCK). The Day 63 Rest Day falls between schemas and the SKILL bundle — pre-stage only, no SPEC content (the Day 21/28/35/42/49/56 Rest Day-compounding pattern).

### 14.2 What partial 2 (Day 60) authors

Reserved sections, with the pre-scaffolded scope from the outline §6–§16 preview:
- **§8 Performance Targets** — 9 metric categories. Schema validity 100% / brand-edit-rule catch 100% (a fade/wipe/zoom must never survive) / authored-text firewall catch 100% / duration-in-band 100% / false-plan-ready rate 0% target / false-fail rate ≤8% (over-flagging to `revise` is the acceptable direction) / p50 latency 30s / p95 90s / zero engine cost.
- **§9 Test Fixtures** — 5-fixture portfolio: TC-01 clean Mode-A→manifest Pro PASS (full plan) · TC-02 Mode-C Enterprise PASS (mode-blind convergence proof — byte-identical authoring path to TC-01 despite different origin) · TC-03 `incomplete_shot_coverage` → fail+route to Ingest · TC-04 `brand_edit_rule_conflict` (a beat that only resolves with a fade → hard FAIL) · TC-05 `edit_plan_firewall_breach` (banned token authored into a lower-third — the 9th-pass self-authored catch). TC-01/TC-02 carry the mode-blind convergence proof.
- **§11 Cost Model** — zero-engine snapshot + directed-coherence value model.
- **§12 Verdict Math** — `PLAN_READY = (Ingest precondition) ∧ (coverage complete) ∧ (beat map mappable) ∧ (cut order covers structure) ∧ (duration in band) ∧ (all hard brand-edit rules) ∧ (captions within char limit) ∧ (authored-text firewall clean) ∧ (mode-blind)`. Soft-rule tension → `revise`; hard violation → `fail`. Deterministic on the hard rules; `revise` is the only judgment slot.
- **§13 Critical Decisions LOCKED** — 14 pre-scaffolded decisions (outline §13). The §10 8-tuple decision (#6, triply-deferred) and the Editor-handoff-target decision (Open Question 4) are the only forward edit slots.
- **§15 Change Log** — v1.0 lifecycle entries (outline-58 → body-59 → body-60 → LOCK-candidate → schemas → SKILL → runbook → LOCKED) + parked-candidates list.
- **§16 Metadata Block Schema** — Cross-SPEC §3.9 canonical + 5 Edit-Director additions (8-tuple parent_chain, edit_plan_class, plan_evidence_hash, render_dispatched, runtime_environment_class).

### 14.3 What this partial LOCKED (Day 59)

- **§6** — 11-check self-QC list, 4-tier ordering, 9-code errorEnvelope namespace + slot-11, the 3-verdict model (plan_ready/fail/revise), the 11-entry firewall list applied to AUTHORED text. LOCKED-as-drafted.
- **§7** — full LLM system prompt (frame + 12 hard rules + universal-access tier-richness table + 11-step direction loop + Blueprint §4.9 `edit_plan` shape inlined + voice rule). LOCKED-as-drafted; copies verbatim into SKILL.md on the SKILL-bundle day.
- **§10** — 27-row field map (passthrough/transform/authored split) + reserved fields + no-touch fields (incl. the `production_mode` non-read) + schema authoring note (the 8-tuple additive hold + brand-rule `const`s) + tier-richness matrix. LOCKED-as-drafted.
- **§14** — this calendar + status. LOCKED-as-drafted.

### 14.4–14.7 Carried dependencies + operator gates (surfaced, NOT advanced)

- **§14.4 — Predecessor LOCK ceremonies (4, operator-only):** AI Video Gen v1.0, Style Replication v1.0, QC Pre-flight v1.0, Ingest v1.0 — all four STILL PENDING (file-state confirmed; version tags unflipped). They gate Edit Director's eventual v1.0 LOCK. The **Ingest 7-tuple LOCK is Edit Director's DIRECT 8-tuple dependency**.
- **§14.5 — LLM Test Runbook executions (3, operator-only):** Day 47 QC Pre-flight, Day 36 Style Replication, Day 57 Ingest — all paste-and-run, all pending. 5/5 each opens the respective LOCK gate.
- **§14.6 — Ingest Day 53 LOCK-candidate items (carried):** Item 6 (cost-model confirm ~$0.00, recommend RATIFY); Item 8 (15-decisions walk — D15 Edit-Director handoff to the Notion holding store now DIRECTLY relevant, recommend RATIFY); Item 11 (§3.9 amendment review).
- **§14.7 — Cross-SPEC §3.9 n-tuple amendment ratification (operator-only):** now **TRIPLY load-bearing** (QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple). Until ratified AND the chain LOCKs, all three n-tuples stay at the additive `minItems: 5` hold. Recommend RATIFY-AS-DRAFTED — Edit Director is the third forcing function.

---

## Cross-SPEC §3 adherence (partial-1 re-confirm — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `edit-director-agent` (kebab-case); slot-11 `edit_director_agent_failed` |
| §3.2 hash invariant | ✅ `plan_evidence_hash` SHA-256 over the edit_plan + brand_edit_check block (§6.1 #11 / §10) |
| §3.3 errorEnvelope shape | ✅ §6.3 mirrors fleet shape (failure_code, failed_check_id, attempts, detail, cost_incurred_usd, route_back_to, metadata, human_review_required) |
| §3.4 qc_pre_flags minItems 4 | ✅ §6.1 #11 + §10 row 26 enforce ≥4 snake_case predicates |
| §3.5 Mode coverage matrix | ✅ §6.1 #10 mode-blind self-attestation — the first agent for which the mode columns are identical |
| §3.6 Slot 11 naming canon | ✅ `edit_director_agent_failed` (§6.1 #10/#11, §6.3) |
| §3.7 qc_pre_flags format | ✅ snake_case predicates (§6.1 #11) |
| §3.8 Tier↔mode firewall (9th defense-in-depth) | ✅ §6.1 #4 AUTHORED-text firewall (NEW surface) + §7 universal-access tier-richness table |
| §3.9 Metadata + n-tuple parent_chain | ✅ §10 inherits canonical + extends to 8-tuple, held additively. **Triply-deferred** — gated on the §3.9 amendment ratification AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK |
| §3.10 Cost ceiling authority | ✅ §7 Hard Rule #10 DECLINES to re-litigate cost (QC's authority) or re-validate assets (Ingest's authority) — $0-cost agent |
| §3.11 LOCK respect | ✅ This partial does NOT modify any LOCKED canon — all predecessor SPECs / schemas / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at partial-1 stage.** Full §3 self-audit embedded in the Day 61 LOCK candidate.

---

## Files produced today (Day 59)

- `ars/ARS-2026-06-17-Day-59-Edit-Director-Agent-SPEC-Body-Partial-1.md` — this doc
- `ars/build-log-2026-06-17.md` — Day 59 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 59)

- ✅ **No LLM dispatched.** No render API, no engine credentials referenced, no vendor URLs walked, no media render, no byte-level decode. (Edit Director by design authors a plan and renders no pixels in v1.0 — appropriate for a creative-direction agent.)
- ✅ **No external comms transacted.** No emails, no DMs, no social posts, no client/investor outreach. The end-of-run status iMessage to Jamila ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business. (Notification-channel status carried — see build log.)
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, ZERO $ spent.
- ✅ **No operator-impersonation.** AI Video Gen / Style Replication / QC Pre-flight / Ingest LOCK ceremonies NOT assumed — all four confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Ingest Day 53 Items 6/8/11 + the three runbook executions NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed. The 8-tuple stays held additively (`minItems: 5`), NOT flipped to exact-8.
- ✅ **No fake-advance.** This partial is forward-design over LOCK-stable text artifacts only, explicitly labeled BODY PARTIAL 1. Zero net-new modifications to any LOCKED canon. Edit Director v1.0 LOCK will hard-gate itself on the upstream LOCKs (especially the Ingest 7-tuple) being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §6.5 enumerates HC/NPOX tokens precisely so the agent can BLOCK them in the copy it AUTHORS — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence re-confirm complete.** 11 of 11 dimensions ✅ at partial-1 stage. Full LOCK audit at the Day 61 LOCK candidate.
- ✅ **Pattern source acknowledged.** Ingest Day 51 partial 1 (§6/§7/§10/§14) structure inherited verbatim. Orchestration Blueprint §4.9 (`edit_plan` shape) + Cross-SPEC §3 + Brand-Voice Intake §7–§11 used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-59 build runs Wednesday (Pacific). Next Rest Day: Day 63 (Sun Jun 21 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 59 ships clean. Day 60 build session targets SPEC body partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16). Edit Director is Agent #9 of 17 — the 9th defense-in-depth firewall (the FIRST over self-authored text), the first creative-authoring agent in the post tail, and the first contractually mode-blind agent (the live, machine-checkable proof that Ingest's mode-convergence seam holds). This partial LOCKs the self-QC list (11 checks, 9 codes + slot-11, the new 3-verdict model with `revise`), the full LLM system prompt (12 hard rules incl. mode-blind-by-construction + author-a-plan-never-render + recommend-don't-approve), and the 27-row field map (passthrough/transform/authored split + the triply-deferred 8-tuple + brand-rule `const`s machine-enforced at the schema layer). Operator pickup: (1) the four predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight + Ingest) remain pending and gate Edit Director's eventual v1.0 LOCK — the Ingest 7-tuple is the direct 8-tuple dependency; (2) execute the three pending runbooks (Day 36 / Day 47 / Day 57); (3) ratify the Cross-SPEC §3.9 n-tuple amendment so the 8-tuple is canon (Edit Director is now the third forcing function). Day 63 (Jun 21) = next Rest Day.*
