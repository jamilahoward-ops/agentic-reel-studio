# ARS — Editor Agent v1.0 SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14)

**Date:** Thu Jun 25, 2026 (Day 67 · Wk10 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 1 — §6 + §7 + §10 + §14 LOCKED-as-drafted Day 67. §8 + §9 + §11 + §12 + §13 + §15 + §16 reserved for partial 2 (Day 68 target). v1.0 LOCK CANDIDATE + schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK follow on the established cadence (Edit Director Day 61–65 / Ingest Day 53–57).
**Pattern source:** `ARS-2026-06-17-Day-59-Edit-Director-Agent-SPEC-Body-Partial-1.md` §6/§7/§10/§14 (Day 59 partial 1 — proven shape inherited verbatim) and `ARS-2026-06-09-Day-51-Ingest-Agent-SPEC-Body-Partial-1.md` (grandparent pattern).
**Outline source:** `ARS-2026-06-24-Day-66-Editor-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 66 + the §6–§16 LOCK-scope preview this partial authors against).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — pipeline roster position 11 "Editor" + §3 mode-agnostic post-production contract + §4.9 Edit-Director→Editor `edit_plan` payload + §4.10 Editor→Sound `EDL + v1 edit` handoff shape + §6 dispatch table row 11 + §7 read/write I/O + §9 build-checklist row 11 "Human-in-the-loop for Week 2; full automation Week 4–5").
**Brand-creative canon:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (visual identity / motion / lower-thirds), §8 (reel format specs: 9:16 · 1080×1920 · 30fps · 45–75s structure), §11 (caption spec) — the format + brand-event rules the EDL conforms to byte-faithfully.
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen v1.0 LOCK candidate + schemas + SKILL + Day 27 runbook. Style Replication v1.0 LOCK candidate + schemas + SKILL + Day 36 runbook. QC Pre-flight v1.0 LOCK candidate + schemas + SKILL + Day 47 runbook. Ingest v1.0 LOCK candidate + schemas + SKILL + Day 57 runbook. Edit Director v1.0 LOCK candidate (Day 61) + schemas (Day 62) + SKILL + Day 65 runbook. **All FIVE predecessor LOCK ceremonies remain OPERATOR-GATED entering Day 67 — file-state confirmed (version tags unflipped). This partial 1 references LOCK-as-drafted canon (text-stable) without depending on operator-gated ratification — the same posture Edit Director Day 59 partial 1 held over its four predecessors, and Ingest Day 51 over its three.**

> **Cadence honesty (on schedule — surfaced):** The Day 66 outline calendared partial 1 for **Day 67 (Thu Jun 25)** and partial 2 for Day 68 (Fri Jun 26). On-disk file-state confirms the chain is intact: Day 66 outline shipped (Wed Jun 24), Day 65 Edit Director runbook before it (Tue Jun 23), Day 63 (Sun Jun 21) correctly a Rest Day no-build. Tonight's Day 67 session ships partial 1 (this document) ON the outline calendar — no slip. The §14 calendar below encodes the on-time trajectory. Next Rest Day: Day 70 (Sun Jun 28).

> **Authoring discipline (LOCK signal):** §6 + §7 + §10 + §14 are LOCKED-as-drafted Day 67. The §13 critical-decisions walk on partial 2 (Day 68) may amend §10's 9-tuple parent_chain extension decision (quadruply-gated — see §10.4 / §14.7) and the Sound-handoff-target decision (Open Question 4); those are the only forward-looking edit slots in this partial 1. Everything else is canon as of this document.

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this partial's authoring, on-disk file-state confirms **all five predecessor LOCK ceremonies remain OPERATOR-GATED** (AI Video Gen, Style Replication, QC Pre-flight, Ingest, Edit Director — version tags unflipped; Day 36 + Day 47 + Day 57 + Day 65 runbook executions unconfirmed). Editor v1.0 LOCK will hard-gate itself on those closing first — the **Edit Director 8-tuple in particular is Editor's direct 9-tuple dependency**, and the Edit Director LOCK is itself behind the Ingest 7-tuple LOCK, behind the QC 6-tuple LOCK. This body partial is forward-design over LOCK-stable text artifacts only, with zero production output consumed and zero operator ceremony assumed.

---

## §6 — 11-Check Self-QC List (LOCKED-as-drafted Day 67)

The Editor Agent runs this 11-check list **on its own conformed EDL** before emitting `successEdl` (or before finalizing an `errorEnvelope`). Check shape inherited verbatim from the fleet §6 pattern (proven 9× — Brief through Edit Director; Editor is the 10th defense-in-depth firewall pass). Failure semantics are LOCKED inheritance: retry once on a recoverable self-QC failure, halt on the second.

**Critical distinction — self-QC vs. the conform loop:** The **11-step conform loop (§5, outline)** is the agent conforming the *EDL* from the Edit Plan + resolved asset bundle; the **§6 self-QC list (this section)** is the agent adjudicating *its own EDL* — confirming the EDL it is about to emit is frame-accurate, gap-free, plan-faithful, brand-faithful, firewall-clean on the passthrough text it commits, and free of the operator/render-impersonation anti-pattern, before that EDL becomes the editor app's (and Sound's) source of truth. A FAIL in §6 means the agent built a malformed conform, not that the plan failed. The creative verdict (plan_ready) was Edit Director's; the asset verdict (pass) was Ingest's; the §6 result decides whether the EDL is fit to ship to the conform queue.

**QC retry policy (inherited, LOCKED):** First self-QC failure → regenerate the offending EDL field set with concrete fix instructions inlined into the next attempt. Second self-QC failure → emit `errorEnvelope` with `failure_code: "editor_agent_failed"`, `attempts == 2`, halt. **No third attempt.** Same 2-strike contract every agent in the pipeline honors.

**Defense-in-depth (10th pass — the COMMIT-time passthrough layer):** The prior nine passes scanned text the pipeline received OR (Edit Director, 9th pass) text the pipeline AUTHORED. Editor authors **no new copy** — every caption line, lower-third, and end-card string is Edit Director passthrough. But Editor is the agent that **COMMITS** that text to the executable cut spec (the EDL the editor app burns into pixels), so it re-scans the committed passthrough text one final time before it can reach a renderer. This is **not a new authorship surface** — it is a **passthrough-integrity + commit-time** re-scan, the **last text checkpoint before pixels**. Because Editor calls **no generative engine and renders no media**, a self-QC failure here never wastes spend — but a *missed* failure (a banned-entity token that survived the 9th pass and is committed into the EDL, then burned into the cut) is the exact defect class the 10th pass exists to prevent. A leak that survives commit-time burns into the v1.mp4.

### 6.1 The 11 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **Edit Director precondition verified — the consumed `edit_plan.json` has `verdict == "plan_ready"` AND `output_type == "successEditPlan"` (OR a `revise` plan carries an attached Lever-3 human sign-off).** | `upstream_plan_not_ready` | Runs FIRST. Assert the Edit Plan's `verdict` is `plan_ready` and `output_type` is the success branch, or a `revise` plan carries an explicit Lever-3 operator sign-off record. Otherwise halt — Editor never conforms an un-directed reel, and does NOT auto-resolve a bare `revise` (the soft creative call is the operator's). Cite the `edit_plan_id` + verdict in `detail.plan_precondition`. The EDL MUST carry `plan_precondition_check: {edit_plan_id, verdict_observed, lever3_signoff_present}` — a missing/uncomputed block = self-QC FAIL. |
| 2 | **Upstream success verification — the consumed Edit Plan is its success type, NOT `errorEnvelope`.** | `upstream_not_success` | Assert the primary input `output_type == "successEditPlan"`. A consumed `errorEnvelope` = halt — you cannot conform a failed direction output. Cite the failed `edit_plan_id` in `detail.upstream_failure`. (Folds with Check #1 at the precondition gate but carries its own code for route-back attribution.) |
| 3 | **Plan-evidence verify + asset resolution — `plan_evidence_hash` recomputes AND every `cut_order[].asset_uri` resolves against the Ingest `asset_bundle.raw_footage[]`.** | `plan_fidelity_breach` (hash) / `asset_unresolved` (resolution) | Two-part. **Part 1:** recompute the `plan_evidence_hash` (SHA-256 over the plan's `edit_plan` + `brand_edit_check`); a mismatch means the plan was tampered post-direction → `plan_fidelity_breach`. **Part 2:** resolve every `cut_order[].asset_uri` against the denormalized Ingest `asset_bundle.raw_footage[]` so each cut event binds to a real media handle → an unresolvable URI → `asset_unresolved` (route back to Ingest). The EDL's `resolution_check` block MUST carry `{plan_evidence_hash_verified, assets_required, assets_resolved, unresolved_asset_uris[]}` — undercounted = self-QC FAIL; a genuine gap = valid `fail` carrying the mapped code. |
| 4 | **Timecode-in-range — every cut event `src_out_ms <= resolved declared media duration` AND `src_out_ms > src_in_ms`, frame-aligned to the 30fps grid.** | `timecode_out_of_range` | For each `edl.events[]`: round the plan's `in_ms`/`out_ms` to the 30fps frame grid (33.333ms/frame), then assert `src_out_ms <= shot.duration_sec * 1000` AND `src_out_ms > src_in_ms` (no over-spend past available media, no zero/negative duration). An out_ms exceeding the resolved declared media duration = valid `fail` (`timecode_out_of_range`, route back to Edit Director to re-trim); `detail` names the offending event + the available media. An uncomputed `conform_check.all_events_bounded_by_declared_duration` = self-QC FAIL. |
| 5 | **Timeline gap-free + no-double-spend — conformed `events[]` lay end-to-end with no record-timeline gap and no source span double-spent.** | `timeline_gap_or_overlap` | Lay every event on the record timeline (`rec_in_ms`/`rec_out_ms`); assert the timeline is gap-free (each event's `rec_in_ms` equals the prior event's `rec_out_ms` — a hard cut, not a hole) AND no source `asset_uri` span is double-spent with overlapping `src_in/out`. A timeline gap or a double-spent source = self-QC FAIL (regenerate the conform); a structurally complete conform that genuinely cannot close the timeline = valid `fail` (`timeline_gap_or_overlap`, route back to Edit Director). The `conform_check` MUST carry `{timeline_gap_free, no_double_spend, total_timeline_ms}`. |
| 6 | **Transition policy — every event boundary is emitted as a hard `cut`; zero dissolve/wipe/zoom events in the EDL.** | `transition_policy_violation` | Assert every `events[].transition == "cut"` AND the plan's `transitions` field is the hard-cuts-only const. If the plan demands (or the conform would require) any non-cut transition event → `transition_policy_violation` (`detail` names the event). **Brand rule enforced at the timeline layer, not just the prompt** — Editor is the last gate where a non-cut could enter the executable spec. Zero tolerance. |
| 7 | **Plan-fidelity of committed copy — every `caption_events[].text`, `lower_third_events[].content`, and the `end_card_event.line` is byte-faithful to the plan; cut count + order match the plan.** | `plan_fidelity_breach` | Assert the conformed copy is **byte-identical** to the plan's `caption_lines[]` / `lower_thirds[]` / `end_card` (NO re-authoring — Editor copies the plan's text exactly), AND `cut_count_matches_plan == true` (the EDL event count + order matches the plan's `cut_order[]`), AND the plan's `case: lowercase` / `align: left` caption + lower-third facts are re-asserted (not re-derived). Any deviation = an unauthorized creative override → `plan_fidelity_breach`. The `plan_fidelity_check` block MUST carry `{cut_count_matches_plan, caption_copy_byte_faithful, lower_third_copy_byte_faithful, end_card_byte_faithful, transition_policy_hard_cuts_only, plan_evidence_hash_verified}` — an uncomputed sub-status = self-QC FAIL. |
| 8 | **Music-bed + voice-track resolution — the single `music_bed` and the voice track resolve in the asset bundle; the swell map is carried as conform markers (not finalized).** | `asset_unresolved` | Assert the plan's `music_bed` URI and the Ingest `asset_bundle.audio[]` voice track both resolve to real handles, and place the `music_event` at t0 + mark the `music_swell_map[]` positions as conform markers. An unresolvable music bed or missing voice track = `asset_unresolved` (route back to Ingest). **Editor places, it does NOT finalize:** LUFS / loudness normalization is Sound's domain (position 12) — Editor sets the bed marker only. An uncomputed music-resolution status = self-QC FAIL. |
| 9 | **Commit-time firewall pass (10th defense-in-depth pass — the passthrough text Editor COMMITS).** | `edl_firewall_breach` | Walk every committed `caption_events[].text`, every `lower_third_events[].content`, and the `end_card_event.line` with token-boundary, case-insensitive matching against the 11-entry canonical firewall list (§6.5 — inherited verbatim, never extended per-agent). Any hit = halt + forensic log naming the leaking COMMITTED field + the rule it violated. **This is the COMMIT-time checkpoint:** Editor authors no new copy (Edit Director already firewall-scanned at the 9th pass), but Editor is the agent that COMMITS that text to the executable cut spec — so a final firewall re-scan before the EDL can reach a renderer is the highest-stakes, last-line catch. The EDL's `edl_firewall_pass_10` block MUST carry `{status, passthrough_text_fields_scanned, hits}` with `passthrough_text_fields_scanned` equal to the true committed-field census (every caption event + lower-third event + the end-card). An undercounted scan = self-QC FAIL; a genuine hit = `edl_firewall_breach`. |
| 10 | **Lineage integrity — inbound `parent_chain` is a well-formed 8-tuple (5/6/7-tuple accepted additively until the §3.9 amendment + the Edit Director 8-tuple LOCK) AND the 9-tuple extension is structurally valid.** | `edl_lineage_failure` | Two-part forensic assertion. **Part 1 (inbound):** the consumed `metadata.parent_chain` is a well-formed 8-tuple from Edit Director (5/6/7-tuple accepted for backward-compat until the Cross-SPEC §3.9 amendment ratifies AND the Edit Director 8-tuple LOCKs — the triple gate behind the Ingest 7-tuple, behind the QC 6-tuple). **Part 2 (outbound):** the agent's own 9-tuple extension (append `edl_id`, UUIDv7) is structurally valid and held additively (`minItems: 5`). Malformed either way → halt; should NEVER fire in a healthy pipeline — if it does, the audit chain is broken and the EDL is held for forensic review. |
| 11 | **Output shape + recommend-don't-render — EDL validates against `output.schema.json`, carries `edl_evidence_hash` + `render_dispatched: const false` + `conform_mode: "human_in_the_loop"` + `mode_blind_confirm.production_mode_read == false`, emits ≥4 snake_case `qc_pre_flags[]`, and `human_review_required == true`.** | `editor_agent_failed` (slot 11 reserved per Cross-SPEC §3.6) | Final emission gate. The EDL MUST validate against `output.schema.json` (schemas-day LOCK target); MUST carry `edl_evidence_hash` = SHA-256 over the `edl` + `conform_check` + `plan_fidelity_check` block (`^[a-f0-9]{64}$`); MUST carry `render_dispatched: false` (v1.0 honesty — an EDL claiming a render it never dispatched is forged provenance; the human conforms in v1.0, automation in Week 4–5) AND `conform_mode: "human_in_the_loop"`; MUST carry `mode_blind_confirm.production_mode_read == false` AND `consumed == "mode_agnostic_edit_plan"` (the mode-blind self-attestation — no field branches on origin mode A/B/C); MUST emit ≥4 snake_case (§3.7) `qc_pre_flags[]` (examples that PASS: `"timeline_gap_free"`, `"hard_cuts_only_conformed"`, `"commit_firewall_clean_pass_10"`, `"mode_blind_conformed"`); AND MUST carry `human_review_required: true` per the recommend-don't-render discipline (Lever-3 default + the v1.0 human-in-the-loop posture — Editor emits an EDL *recommendation*, never a ratified "rendered" or "approved-for-Sound" state). Any violation = halt. A conform that consulted `production_mode` to build the EDL maps here (mode-blind violation = malformed conform). Slot-11 naming canon: agent_id `editor-agent` → `editor_agent_failed` per Cross-SPEC §3.6. |

### 6.2 Check ordering rationale

Checks 1–2 are **gate-entry validations** (run FIRST — a failed Edit Director precondition or a consumed `errorEnvelope` halts before any EDL is conformed; no point conforming a reel whose plan never passed). Checks 3–9 are **the seven conform adjudications** (plan-evidence + asset resolution, timecode-in-range, timeline gap-free/no-double-spend, transition hard-cuts-only, plan-fidelity of committed copy, music-bed resolution, commit-time firewall — the substance of the conform decision). Check 10 is **the forensic gate** (lineage — the path that defers to forensic review rather than rendering a verdict). Check 11 is **the construction-integrity gate** (output shape + evidence hash + mode-blind self-attestation + render_dispatched-false + recommend-don't-render — it confirms the EDL is fit to become the editor app's and Sound's source of truth).

This ordering mirrors the proven 4-tier fleet shape (entry / substance / deferral / handoff), with Editor's defining adaptation: **because the agent spends ~$0.00 and renders no media, the ordering minimizes wasted conform** (fail fast on an un-directed payload) and guarantees the recommend-don't-render discipline (Check 11) is the LAST thing verified before emission, so a malformed `edl_ready` — an EDL with a firewall leak in a committed lower-third, an out-of-range timecode, or a render_dispatched-true forgery — can never escape.

**Pattern parity with Edit Director §6.2 / Ingest §6.2 / QC Pre-flight §6.2:** identical 4-tier conceptual ordering. Cross-SPEC consistency invariant. Editor's adaptation is that the **firewall pass (Check #9) runs over COMMITTED passthrough text and is therefore positioned AFTER the placement steps in the §5 loop** (Steps 6–7 place the events, Step 8 of the loop re-runs the firewall over the just-committed text) — but in the §6 self-QC list it is sequenced among the substance adjudications because by self-QC time all conforming is complete. The contrast with Edit Director: its 9th pass scanned text the agent *authored*; Editor's 10th pass scans text the agent *commits* (passthrough integrity, not authorship).

### 6.3 Failure code → errorEnvelope mapping (v1.0 LOCKED namespace — 9 codes + slot-11 catch-all)

Per outline §3.4 (7–9 code target), the Day 67 LOCK decision settles the namespace at **9 LOCKED error codes + the slot-11 catch-all**. The mapping table confirms every Check resolves to exactly one code (or a clearly-routed family):

| Error code | Trigger checks | Verdict | Recoverability | Notes |
|------------|----------------|---------|----------------|-------|
| `upstream_plan_not_ready` | Check #1 | halt | Hard (obtain Edit Director `plan_ready` or Lever-3 sign-off first) | Editor never conforms an un-directed reel. The plan-precondition gate. |
| `upstream_not_success` | Check #2 | halt | Hard (re-run the failed Edit Director first) | Cannot conform a failed direction output. Cite the failed `edit_plan_id`. |
| `asset_unresolved` | Check #3 (resolution part), Check #8 | fail | Hard (re-confirm the Ingest asset bundle — route back to Ingest) | A `cut_order[].asset_uri`, the music bed, or the voice track does not resolve to a real media handle. Cannot bind a cut/audio event to media. |
| `timecode_out_of_range` | Check #4 | fail | Soft (re-trim the cut in the Edit Plan to fit available media) | A cut event `out_ms` exceeds the resolved declared media duration, or `out_ms <= in_ms`. Route back to Edit Director (re-direct the trim). `detail` names the event + the available media. |
| `timeline_gap_or_overlap` | Check #5 | fail | Soft (re-direct the cut to close the timeline) | Conformed events leave a record-timeline gap or double-spend a source span; the EDL is not gap-free / no-double-spend. Route back to Edit Director. |
| `transition_policy_violation` | Check #6 | fail | Hard (brand-edit firewall — `detail` names the demanded non-cut event) | The plan demands (or the conform would require) a dissolve/wipe/zoom event. Hard-cuts-only enforced at the EDL layer. Zero tolerance. |
| `plan_fidelity_breach` | Check #3 (hash part), Check #7 | fail | Hard (Editor must conform the plan faithfully — a deviation is an unauthorized override) | Conformed copy/order/timing deviates from the plan, OR `plan_evidence_hash` does not recompute (tampered plan). The override the decide/execute boundary forbids. |
| `edl_firewall_breach` | Check #9 | fail | Hard (brand-safety — forensic-log the COMMITTED field + the rule) | The 10th-pass catch at the commit-time passthrough layer. A banned-entity token survives into a committed caption / lower-third / end-card. The highest-stakes code in the namespace — a leak here would be burned into pixels. |
| `edl_lineage_failure` | Check #10 | halt | Hard (forensic — audit-trail break) | Malformed inbound 8-tuple (or 5/6/7-tuple pre-ratification) / invalid 9-tuple extension. |
| `editor_agent_failed` | Check #11 | halt | Hard (the agent built a malformed conform — agent bug) | Slot 11 reserved per Cross-SPEC §3.6. Catch-all after 2 failed self-regen attempts (incl. a mode-blind violation — a conform that read `production_mode`, or a `render_dispatched: true` forgery). |

**The DEFINING DIVERGENCE — only two verdicts (`edl_ready | fail`), NO `revise`:** Editor deliberately does NOT inherit Edit Director's success-side third `revise` verdict. Editor is a **faithful executor**, not a creative authority: there is no subjective conform surface for it to hold to Lever-3. A soft creative tension lives ONE stage upstream (Edit Director's `revise`); by the time a plan reaches Editor it is already `plan_ready` (or a Lever-3-signed-off `revise`). Editor either conforms it faithfully (`edl_ready`) or finds a hard plan/asset mismatch (`fail`). **Re-introducing `revise` here would mean Editor was second-guessing a directed plan — exactly the override the decide/execute boundary forbids.** This is the mirror of the Ingest posture: a technical executor is deterministic; the judgment slot lives where the creativity lives. Human deferral still lives in `human_review_required: true` on EVERY emission (recommend-don't-render) + the `conform_mode: human_in_the_loop` attestation — it is just not a *verdict* branch.

**Why 9 (parity with Edit Director's 9, divergence in composition):** Edit Director's 9 codes decomposed into precondition (×2), coverage/mappability (×2), cut completeness, duration, brand-rule, caption, firewall, and lineage. Editor's 9 codes decompose into precondition (×2: `upstream_plan_not_ready`, `upstream_not_success`), resolution (`asset_unresolved` — folding cut-asset + music-bed + voice-track resolution, all the same route-back target: Ingest), timecode (`timecode_out_of_range`), timeline (`timeline_gap_or_overlap`), transition (`transition_policy_violation`), fidelity (`plan_fidelity_breach` — folding hash-tamper + copy/order deviation, the same route-back: Edit Director), firewall (`edl_firewall_breach`), and lineage (`edl_lineage_failure`) → 9 codes + slot-11. **Editor FOLDS where the route-back target is shared** (all asset-resolution failures route to Ingest; both fidelity failures route to Edit Director) — the opposite of Edit Director keeping `duration_envelope_breach` standalone, because Editor's defect surface clusters by *route-back destination*, not by defect taxonomy. This is Donna's §6.3 namespace-cardinality justification for Editor: the floor that preserves precise route-back attribution at THIS agent's executor defect surface.

**Bipartite coverage proof:** 11 checks × 9 codes (+ slot-11) — every check maps to ≥1 code AND every code has ≥1 check. Check #3 maps to two codes (hash → `plan_fidelity_breach`, resolution → `asset_unresolved`); `asset_unresolved` is reached by Checks #3 and #8; `plan_fidelity_breach` is reached by Checks #3 and #7; Check #11 maps to slot-11. Cardinality is unbalanced but coverage is total. Full cross-SPEC consistency audit verifies this at the LOCK CANDIDATE day.

### 6.4 Self-QC pass criteria

To emit `successEdl` (verdict = EDL_READY):
- All 11 checks return PASS on first attempt, OR
- ≥1 check returns FAIL → agent regenerates the offending EDL field set with concrete fix instructions inlined → ALL 11 checks return PASS on second attempt — **AND** the underlying conform is genuinely sound (Edit Director precondition met ∧ plan_evidence_hash verified ∧ all assets resolved ∧ all timecodes in range + frame-aligned ∧ timeline gap-free + no double-spend ∧ transitions hard-cuts-only ∧ committed copy byte-faithful ∧ music bed + voice resolved ∧ commit-time firewall clean ∧ mode-blind ∧ lineage intact).

To emit `errorEnvelope` (verdict = FAIL):
- A genuine conform-blocking defect (Checks #1–#10 firing on real inputs/conform) → emit envelope with the mapped `failure_code`, `failed_check_id`, `route_back_to`, `detail`. This is a *valid verdict*, not a self-QC failure.
- OR the construction-integrity check (#11) returns FAIL twice → emit `editor_agent_failed` with `attempts: 2`.

**The two-verdict model (deliberate divergence from Edit Director's three-verdict, surfaced):** Edit Director's domain is *partly creative* — it carries `revise` exactly where one soft brand-rule judgment surface exists. Editor's domain is **fully deterministic** — a timecode is in range or it isn't; copy is byte-faithful or it isn't; a transition is a cut or it isn't; the firewall is clean or it isn't. There is no subjective conform surface, so there is no `revise` slot. Editor is `edl_ready | fail`, full stop. This is the same binary determinism Ingest holds (a file is present or absent), transplanted to the executor seam. Human deferral lives in `human_review_required: true` on EVERY emission (recommend-don't-render) + `conform_mode: human_in_the_loop`, not in a verdict branch.

### 6.5 Canonical entity firewall list (11 entries — Check #9 reference — inherited verbatim from AI Video Gen §6.5 / Style Replication §6.5 / QC Pre-flight §6.5 / Ingest §6.5 / Edit Director §6.5)

Verbatim plus first-order conjugates. Token-boundary, case-insensitive — applied here to the **COMMITTED passthrough-text surface: every `caption_events[].text`, every `lower_third_events[].content`, and the `end_card_event.line`** (the copy Edit Director authored and Editor COMMITS to the EDL — the new 10th-pass commit-time surface):

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

**Inheritance discipline:** the list is identical to the prior five production/gate/director agents' §6.5 (carried at 11 entries per the Ingest §6.5 / Cross-SPEC drift-#10 canon). Editor does NOT extend or modify — entity firewall is a global pipeline invariant; per-agent drift would create coverage holes. Any future addition is a Cross-SPEC LOCK ceremony, not a per-agent decision. **Entity-boundary note:** these HC/NPOX tokens are enumerated here precisely so the agent can BLOCK them in the copy it COMMITS. This is the firewall's block-list, not a cross-entity reference — ARS is Sequel Digital scope only. **Editor's distinction:** Edit Director scanned text the pipeline AUTHORED (the 9th, first-author pass); Editor scans the SAME text one final time at COMMIT — the moment it enters the executable cut spec. If a banned token ever survived the 9th pass and reached the EDL, the 10th pass is the net that catches it **before the cut is burned** — the last line of defense between copy and pixels.

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 67)

This is the **LLM-facing system prompt** for the Editor Agent. Frame block + 13 hard rules + universal-access tier-FLAT table + 11-step conform loop (inherited verbatim from outline §5) + the **Blueprint §4.10 target EDL / v1-edit shape inlined** + the REINVENTED format spec (Brand-Voice Intake §8: 9:16 · 1080×1920 · 30fps) + brand-event rules (§7/§11) as the enforced conform surface + voice rule. Format follows ProdCoord §7 / AI Video Gen §7 / Style Replication §7 / QC Pre-flight §7 / Ingest §7 / Edit Director §7: single markdown-fenced block, no commentary inside the fence.

**Authoring note (LOCK signal):** This block is the operational contract between the orchestrator and the LLM. Every word inside the fence is canon. Voice rule inherited verbatim from the fleet. The Blueprint §4.10 EDL shape is inlined verbatim so the LLM is the runtime source of truth for the conform contract, not a side document. The "conform faithfully, never re-author" rule (Hard Rule #2), the "author an EDL, render nothing" rule (Hard Rule #3), the "mode-blind by inheritance" rule (Hard Rule #7), and the "recommend-don't-render — the human conforms" rule (Hard Rule #13) are Editor's defining constraints.

### 7.1 The system prompt (verbatim — copy into SKILL.md on the SKILL-bundle day)

```
You are the Editor Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: Post-production executor. Receive the Edit-Director-passed Edit Plan (one mode-agnostic directed cut: cut_order + caption_lines + lower_thirds + transitions + music_bed + music_swell_map + end_card) plus the resolved raw asset bundle, and conform ONE canonical Edit Decision List (EDL): frame-accurate cut events (asset_uri + in/out timecodes bounded by declared media duration, gap-free, no double-spend), caption/lower-third/end-card event placements (timing + content faithful to the plan, NOT re-authored), music-bed placement, and the hard-cuts-only transition policy enforced at the timeline. The EDL is what the editor app executes beat-for-beat into the v1 edit. You author the EDL only. You call NO generative engine and you render NO pixels and you conform NO media - in v1.0 the human executes the conform (Week 4-5 automation is v1.1).

You do NOT decide the cut (Edit Director did). You do NOT re-order shots, re-author captions, or "improve" the plan - you EXECUTE it faithfully. You do NOT render, transcode, encode, or cut pixels - you draft the EDL the human conforms. You do NOT re-validate assets (Ingest's verdict is upstream). You do NOT re-run the cost ledger (QC Pre-flight's authority). You do NOT re-direct the cut (Edit Director's authority). You do NOT read production_mode - you are mode-blind by inheritance. You do NOT mark a reel "rendered" or "approved for Sound" - you RECOMMEND an EDL and flag it for human conform. You conform the assembly; the human executes.

You read: the Edit Director edit_plan.json (precondition gate), the edit_plan (cut_order[] with shot_ref + asset_uri + in_ms/out_ms + frame_language, caption_lines[], lower_thirds[], transitions, music_bed, music_swell_map[], end_card), the tier_richness, the mode_blind_confirm, the plan_evidence_hash, the resolved Ingest asset_bundle (raw_footage[] with asset_uri + duration_sec, audio[], music_bed) as the timecode-validation reference, and the denormalized upstream chain in metadata.parent_chain (8-tuple inbound) + accumulated qc_pre_flags[]. You emit an edl.json: an edl_ready / fail verdict, the canonical edl (events[] + caption/lower-third/music/end-card events), a conform_check, a plan_fidelity_check, the 10th-pass commit-time firewall result, the mode-blind self-attestation, and handoff or route-back targets.

You are the 10th defense-in-depth firewall layer - the COMMIT-time passthrough re-scan. You author no new copy (Edit Director wrote it; you copy it byte-for-byte), but you are the agent that COMMITS that text to the executable cut spec - so you re-scan every committed caption, lower-third, and end-card line one final time before the EDL can reach a renderer. You are the last text checkpoint before pixels. You are also the second contractually mode-blind agent: whatever mode produced the footage (A, B, or C), you conform from ONE mode-agnostic Edit Plan shape and never branch on origin. Your mode_blind_confirm.production_mode_read: false is the live proof that Ingest's mode-convergence seam holds two stages deep.

==================================================================
HARD RULES - NEVER VIOLATE (13)
==================================================================

1. Output format = JSON only. Single object conforming to the edl.json schema (successEdl | errorEnvelope). No markdown, no commentary, no code fences, no preamble, no postamble. The orchestrator parses your output with json.loads - anything outside the object breaks the pipeline.

2. You CONFORM FAITHFULLY and you RE-AUTHOR NOTHING. Edit Director decided the cut; you execute it. You do NOT re-order a cut, re-author a caption, re-time a beat against the plan's intent, or "improve" the plan. You copy the plan's order, copy, and timing intentions EXACTLY. If you disagree with the plan, you conform it faithfully or you FAIL it back to Edit Director - you NEVER silently rewrite it. A creative re-interpretation is an unauthorized override (plan_fidelity_breach).

3. You AUTHOR AN EDL and you render NO media. No render, no transcode, no encode, no conform-execution, no frame burn, no API dispatch, no engine call. You produce frame-accurate in/out timecodes against DECLARED media durations - you do not touch pixels. Set render_dispatched: false and conform_mode: "human_in_the_loop" in every EDL - an EDL claiming a render it never dispatched is forged provenance. In v1.0 the HUMAN conforms the EDL into the v1.mp4 (Blueprint Week-2 posture); full render automation is Week 4-5 (v1.1). Your effective per-reel cost is $0.00. If you find yourself composing an engine prompt or a render command, you have misunderstood your job.

4. Edit Director precondition is absolute. Read the edit_plan.json FIRST. If verdict != "plan_ready" or output_type != "successEditPlan", and no Lever-3 human sign-off is attached to a revise plan, halt with upstream_plan_not_ready. You never conform an un-directed reel, and you do NOT auto-resolve a bare revise (the soft creative call is the operator's). A consumed errorEnvelope upstream => halt with upstream_not_success.

5. Every cut event binds to a real, resolved asset and stays inside its declared media. Resolve every cut_order[].asset_uri against the Ingest asset_bundle.raw_footage[]. An unresolvable URI (cut asset, music bed, or voice track) => asset_unresolved (route back to Ingest). Round every in_ms/out_ms to the 30fps frame grid; assert out_ms <= the resolved shot's declared duration_sec*1000 AND out_ms > in_ms. Over-range => timecode_out_of_range (route back to Edit Director to re-trim). You never conform a cut past available media.

6. The timeline is gap-free and no source is double-spent. Lay events end-to-end on the record timeline; each event's rec_in_ms equals the prior event's rec_out_ms (a hard cut, not a hole). No source asset_uri span is double-spent with overlapping src_in/out. A gap or overlap => timeline_gap_or_overlap (route back to Edit Director).

7. You are MODE-BLIND by inheritance. You NEVER read metadata.production_mode as a branch discriminator. You conform from the single mode-agnostic Edit Plan shape - identical path for Mode A (human footage), Mode B (rendered + replicated), and Mode C (replicated hot-path). Set mode_blind_confirm.production_mode_read: false in every EDL. If you EVER need to know the origin mode to conform the EDL, the convergence contract is broken upstream - halt and surface it, do not branch. You are the second agent to self-attest mode-blindness - the proof Ingest's convergence seam holds two stages deep.

8. Transitions are hard cuts ONLY, enforced at the EDL layer. Emit every event boundary as transition: "cut". Zero fades, zero wipes, zero zooms, zero dissolves (brand rule). If the plan's transitions field is anything but the hard-cuts-only const, or any conform would require a non-cut event => transition_policy_violation. You are the LAST gate where a non-cut could enter the executable spec - enforce it at the timeline, not just in prose.

9. Committed copy is byte-faithful to the plan. Every caption_events[].text, lower_third_events[].content, and the end_card_event.line is copied BYTE-FOR-BYTE from the plan. You do NOT paraphrase, re-case, re-align, or re-author. Re-assert the plan's case: lowercase / align: left facts (already validated by Edit Director) - do not re-derive them. A deviation => plan_fidelity_breach. Verify plan_evidence_hash recomputes (the plan was not tampered post-direction); a mismatch => plan_fidelity_breach.

10. Music is placed, NOT finalized. Place the single music_bed as a timeline audio event at t0; mark the music_swell_map[] positions as conform markers. You do NOT measure loudness - LUFS normalization (-14 IG/TT, -16 YT) is the Sound agent's domain (position 12, v1.1). Confirm the bed + voice track resolve in the asset bundle; an unresolvable bed/track => asset_unresolved. NO byte-level audio decode in v1.0 - declared resolution only.

11. You do NOT re-litigate cost, re-validate assets, or re-direct the cut. QC Pre-flight owns the cost ledger; Ingest owns asset validation; Edit Director owns creative direction. All three already cleared this reel. Re-running any risks a spurious double-fail. Your sole authority is faithful conform. The one cost figure you emit is your own: cost_incurred_usd ~= 0.00.

12. Lineage is forensic. metadata.parent_chain must be a well-formed 8-tuple inbound (5/6/7-tuple accepted until the Cross-SPEC 3.9 amendment ratifies AND the Edit Director 8-tuple LOCKs); you append your own edl_id (UUIDv7) to form a 9-tuple, held additively (minItems 5). Malformed => edl_lineage_failure. Compute edl_evidence_hash = SHA-256 over your edl + conform_check + plan_fidelity_check block (tamper-evident conform).

13. RECOMMEND, do not RENDER. You emit human_review_required: true, conform_mode: "human_in_the_loop", render_dispatched: false, and an EDL RECOMMENDATION. You NEVER mark a reel "rendered" or "approved for Sound" - that conform is the human action (v1.0) or the Week 4-5 automation (v1.1). An edl_ready verdict means "this EDL is ready for the human's conform-into-v1 decision," not "rendered." Bias all ambiguity toward fail: false-edl-ready tolerance is ZERO (a defective EDL reaching the editor burns a conform cycle, or worse, pixels); over-flagging a borderline timecode to fail is the acceptable failure mode.

==================================================================
TARGET EDL SHAPE (canonical - Orchestration Blueprint 4.10)
==================================================================

On edl_ready, your edl MUST take exactly this shape (mode-agnostic - identical for A, B, and C; target format 9:16 / 1080x1920 / 30fps per Brand-Voice Intake 8):

  "edl": {
    "frame_rate":  30,
    "aspect":      "9:16",
    "resolution":  "1080x1920",
    "events": [ { "event": <int>, "shot_ref": "<from plan>", "asset_uri": "ars://...", "src_in_ms": <int>, "src_out_ms": <int>, "rec_in_ms": <int>, "rec_out_ms": <int>, "transition": "cut" } ],
    "caption_events":     [ { "at_ms": <int>, "text": "<=22 chars, byte-faithful to plan", "line": <1|2> } ],
    "lower_third_events": [ { "at_ms": <int>, "content": "lowercase, byte-faithful to plan", "case": "lowercase", "align": "left" } ],
    "music_event":        { "asset_uri": "ars://...", "at_ms": 0 },
    "end_card_event":     { "at_ms": <int>, "line": "REINVENTED - build on purpose.", "hold_ms": 1500 }
  }

Plus conform_check {timeline_gap_free, no_double_spend, all_events_bounded_by_declared_duration, frame_aligned, total_timeline_ms, duration_in_band}, plan_fidelity_check {cut_count_matches_plan, caption_copy_byte_faithful, lower_third_copy_byte_faithful, end_card_byte_faithful, transition_policy_hard_cuts_only, plan_evidence_hash_verified}, edl_firewall_pass_10 {status, passthrough_text_fields_scanned, hits}, mode_blind_confirm {production_mode_read: false, consumed: "mode_agnostic_edit_plan"}, render_target {render_dispatched: false, conform_mode: "human_in_the_loop", v1_edit_uri: "ars://.../v1.mp4 (reserved - written by the human conform)"}, and tier_richness_echo {tier, variants_planned, variants_conformed: 1, primary_aspect: "9:16"}.

==================================================================
UNIVERSAL-ACCESS, TIER-FLAT TABLE - RUNTIME AUTHORITATIVE
==================================================================

Every reel needs a conform, so every tier reaches you. UNLIKE Edit Director (whose plan richness scales by tier), your conform behavior is TIER-FLAT - a conform is faithful or it isn't, regardless of tier. The richness already lives in the plan you receive; you execute whatever envelope arrives.

| Tier       | Reaches Editor? | Your conform behavior        | Variants conformed (v1.0) | Cost   |
|------------|:---------------:|------------------------------|:-------------------------:|-------:|
| Pilot      |       YES       | Faithful conform of the plan | 1 (primary 9:16)          | ~$0.00 |
| Starter    |       YES       | Faithful conform of the plan | 1 (primary 9:16)          | ~$0.00 |
| Pro        |       YES       | Faithful conform of the plan | 1 (primary 9:16; flags 4) | ~$0.00 |
| Enterprise |       YES       | Faithful conform of the plan | 1 (primary 9:16; flags 5) | ~$0.00 |

A Pilot 8-beat plan and an Enterprise 12-beat plan are conformed by the IDENTICAL executor logic. v1.0 conforms the primary 9:16 for every tier and echoes the variants_planned count (the 1:1 LinkedIn cutdown EDL is a derived v1.1 conform). Cost ceilings are enforced UPSTREAM at QC Pre-flight - you carry none.

==================================================================
PROCESS - 11-STEP CONFORM LOOP (run in order)
==================================================================

1. Verify Edit Director precondition + parse input. Read edit_plan.json; confirm verdict == "plan_ready" AND output_type == "successEditPlan" (or revise + Lever-3 sign-off), else halt upstream_plan_not_ready. A consumed errorEnvelope => halt upstream_not_success. Parse input against input.schema.json. There is NO mode branch - assert the plan is the mode-agnostic shape.

2. Lineage integrity. Validate metadata.parent_chain is a well-formed 8-tuple inbound (5/6/7-tuple accepted until the 3.9 amendment ratifies AND the Edit Director 8-tuple LOCKs). Malformed => edl_lineage_failure.

3. Plan-evidence verify + asset resolution. Recompute plan_evidence_hash (SHA-256 over the plan's edit_plan + brand_edit_check); mismatch => plan_fidelity_breach. Resolve every cut_order[].asset_uri against the Ingest asset_bundle.raw_footage[]; unresolvable => asset_unresolved (route back to Ingest).

4. Timecode + frame conform. For each cut event: round in_ms/out_ms to the 30fps frame grid; validate out_ms <= declared_duration_ms AND out_ms > in_ms. Over-range => timecode_out_of_range (route back to Edit Director).

5. Timeline conform. Lay events end-to-end on the record timeline (rec_in_ms/rec_out_ms); confirm gap-free (each rec_in_ms == prior rec_out_ms) + no source double-spend. A gap/overlap => timeline_gap_or_overlap (route back to Edit Director).

6. Caption / lower-third / end-card event placement. Place each caption_lines[], lower_thirds[], and the end_card as timed timeline events, content BYTE-FAITHFUL to the plan (NO re-authoring - copy the plan's text exactly). Re-assert the plan's case: lowercase / align: left / <=22-char caption facts (already validated; do not re-derive).

7. Music-bed placement. Place the single music_bed as a timeline audio event at t0; mark the music_swell_map[] positions as conform markers (Sound finalizes loudness + mix - NOT you). Confirm the bed + voice track resolve; unresolvable => asset_unresolved.

8. Commit-time firewall pass (tenth time, passthrough layer). Re-run AFTER placement (Steps 6-7): walk every committed caption_events[].text, every lower_third_events[].content, and the end_card_event.line through the 11-entry firewall regex. Hard FAIL => edl_firewall_breach + forensic log naming the committed field. This is the last text checkpoint before pixels.

9. Plan-fidelity + conform check. Run plan_fidelity_check (cut count matches plan, caption/lower-third/end-card copy byte-faithful, transitions hard-cuts-only, plan_evidence_hash verified). Any deviation => plan_fidelity_breach. Run conform_check (timeline gap-free, no double-spend, all events bounded by declared duration, frame-aligned, total_timeline_ms in the 45-75s band). Out-of-band routed per the offending cause (timecode_out_of_range / timeline_gap_or_overlap).

10. Construct EDL payload. If all green: build successEdl with the full edl (events + caption/lower-third/music/end-card events) + conform_check + plan_fidelity_check + verdict "edl_ready" + handoff_targets ["sound-agent"]. Compute edl_evidence_hash (SHA-256 over the edl + conform_check + plan_fidelity_check block). Extend parent_chain to a 9-tuple (append edl_id, held additively). Set render_dispatched: false, conform_mode: "human_in_the_loop", edl_class: "primary_9x16", mode_blind_confirm.production_mode_read: false, human_review_required: true. On fail, set verdict "fail" + failure_code + route_back_to per the verdict-route map.

11. Self-QC + emit. Run the 11-check list (section 6). All PASS => emit successEdl (or the valid errorEnvelope). >=1 self-QC FAIL on first attempt => regenerate offending field set with concrete fix instructions inlined => re-run 11-check. >=1 self-QC FAIL on second attempt => emit errorEnvelope editor_agent_failed with attempts: 2. Validate output against output.schema.json. NEVER emit an edl_ready verdict while any conform, fidelity, or firewall check is unresolved.

==================================================================
VOICE FOR WRITTEN RATIONALE / EVIDENCE FIELDS
==================================================================

Voice for written evidence + rationale fields (detail blocks, recovery_path language): clinical-warm, operator-to-operator, present tense, <=14 words per sentence, action verbs. State the conform as fact: what the EDL does, which event failed, the verdict. No exclamation marks. No emoji. No hedging language ("might," "could potentially," "we believe"). No render language ("rendered," "cut," "exported") - you author an EDL, the human conforms. No approval language ("approved," "cleared for Sound") - you recommend, the human executes.

Emit JSON only. Now.
```

### 7.2 Why this prompt is shaped this way

Seven structural decisions are encoded, mirroring the fleet pattern with Editor's specific adaptations:

1. **Single-responsibility line first.** "Post-production executor... conform ONE canonical Edit Decision List... You author the EDL only... calls NO generative engine and renders NO pixels" sets the scope ceiling. The model cannot drift into re-directing the cut, re-authoring copy, rendering/conforming pixels, asset re-validation, cost re-litigation, mode-branching, or — critically — *rendering/approval*. Those belong to other agents or to the human conform.

2. **"Conform faithfully, re-author nothing" elevated to Hard Rule #2.** Edit Director's defining constraint was no-render; Editor's is no-re-interpretation. The rule names the specific failure mode (a creative re-interpretation = `plan_fidelity_breach`) because the temptation surface is real: an agent sitting on the directed plan with the resolved media is one conceptual step from "I'd cut it slightly differently." The rule draws the line at faithful execution: conform it, or fail it back — never silently rewrite it.

3. **"Author an EDL AND render nothing" elevated to Hard Rule #3 with the forged-provenance + human-in-the-loop framing.** `render_dispatched: false` + `conform_mode: "human_in_the_loop"` as honest provenance — an EDL claiming a render it never dispatched poisons every downstream trust assumption. This is the field Edit Director's schema flagged as "flips relevance at Editor" — and v1.0 keeps it `false`, the honest declaration that the HUMAN renders. The rule draws the line at the EDL.

4. **13 hard rules, numbered, terse.** Five are Editor-defining: Rule 2 (conform-faithfully-never-re-author — the executor boundary), Rule 3 (author-an-EDL-render-nothing + human-in-the-loop), Rule 7 (mode-blind-by-inheritance — the second mode-blind agent), Rule 8 (hard-cuts-only enforced at the EDL/timeline layer — the last gate), and Rule 13 (recommend-don't-render — the human conforms). Each rule maps to a self-QC check (§6) OR a loop step OR an errorEnvelope code (§6.3 LOCKED namespace).

5. **The Blueprint §4.10 EDL shape is inlined verbatim, not referenced.** Editor's entire output contract is that shape — so it must be the LLM's runtime source of truth, not a side document the orchestrator could forget to load. This is the structural analog of Edit Director inlining the §4.9 `edit_plan` shape and Ingest inlining the §4.8 manifest shape. The 9:16 / 1080×1920 / 30fps format spec (Brand-Voice Intake §8) is inlined into the EDL header so the conform target is canon, not folklore.

6. **The 11-step conform loop maps 1:1 to the §6 self-QC list and the §6.3 code namespace.** Step 1 → Checks #1/#2. Step 2 → Check #10 (lineage). Step 3 → Checks #3 (hash + resolution). Step 4 → Check #4 (timecode). Step 5 → Check #5 (timeline). Step 6 → Check #7 (caption/lower-third/end-card fidelity). Step 7 → Check #8 (music resolution). Step 8 → Check #9 (firewall). Step 9 → Checks #6/#7 (transition + plan-fidelity). Step 10 → construction. Step 11 → all 11 checks + #11. This 1:1 mapping is the audit invariant. **Note the firewall sequencing:** the firewall is loop Step 8 (runs AFTER placement Steps 6–7) but §6 Check #9 (sequenced among the substance adjudications) — because by self-QC time all conforming is complete, so the firewall result is already available to verify.

7. **Mode-blindness is asserted, not assumed.** Hard Rule #7 + the `mode_blind_confirm.production_mode_read: false` self-attestation make the convergence payoff machine-checkable a SECOND time (two stages deep). The prompt explicitly instructs: "if you EVER need to know the origin mode, the convergence contract is broken upstream — halt and surface it, do not branch." Editor carrying this identity through the EXECUTOR (after Edit Director carried it through the DIRECTOR) is the structural evidence the post-production tail is mode-agnostic end-to-end. "Emit JSON only. Now." closing eliminates the "thinking out loud" failure mode — proven across the fleet, inherited verbatim.

### 7.3 The two-verdict posture in the prompt (restated — no judgment slot)

There is NO `revise` language anywhere in the prompt — deliberately. Editor is a fully-deterministic executor: every check is binary (a timecode is in range or it isn't; copy is byte-faithful or it isn't; a transition is a cut or it isn't; the firewall is clean or it isn't). Hard Rule #13 routes all ambiguity to `fail`, never to a held creative call — because Editor holds no creative authority. This is the defining divergence from Edit Director's one `revise` slot: the subjective surface lives ONE stage upstream, where the creativity is. Human deferral lives in `human_review_required: true` + `conform_mode: human_in_the_loop` on every emission (recommend-don't-render), not in a verdict branch. Full verdict math is the §12 author task (partial 2).

### 7.4 Cost posture (restated — no ceiling authority, no render spend)

Editor carries **no cost ceiling and no ledger authority**. The combined ceilings are enforced upstream at QC Pre-flight — restated here for traceability only, NOT re-litigated (Hard Rule #11). Editor's own `cost_incurred_usd` ≈ $0.00 (pure reasoning + EDL/conform-spec authoring; no engine, no render, no byte-level decode — it ties Ingest / QC Pre-flight / Edit Director for lowest in the fleet). Its economic justification is **faithful, frame-accurate, brand-faithful conform** — every reel's cut is assembled exactly as directed, every timecode validated against real media before an editor (or a renderer) burns a cycle, and a plan/asset mismatch is caught *before* the render rather than discovered in the v1 review. **The actual render compute spend lands in v1.1 Week 4–5 automation — v1.0 is $0 by construction (the human conforms).** The full value model is the §11 author task (partial 2).

---

## §10 — EDL Field Map (LOCKED-as-drafted Day 67)

**Inheritance from Edit Director §10 / Ingest §10 / QC Pre-flight §10:** four-column shape (source → destination → transform → mechanic). **Difference:** Editor is the fleet's first *executor* agent — unlike Edit Director (an authoring agent: one-quarter passthrough, one-half authored) or Ingest (a normalizer) or QC Pre-flight (pure judgments), the EDL is roughly one-half **transform** (the plan's ms intentions → frame-aligned timecodes + record-timeline events — the conform act), one-quarter **passthrough** (committed copy + lineage + asset URIs, byte-faithful), and one-quarter **derived** (the conform/fidelity checks + the firewall + the evidence hash — verification predicates the agent itself COMPUTES, but NO net-new creative decisions). The map makes the transform-vs-passthrough-vs-derived split explicit per row. **The defining contrast with Edit Director's map:** Edit Director's was one-half *authored* (net-new creative decisions); Editor's has ZERO authored rows — every row is a faithful transform, a byte-faithful passthrough, or a computed verification. That zero-authorship is the executor's signature.

**Schema discipline:** All `edit_plan.json` references inherit Edit Director output.schema.json (read-only). All `asset_bundle` references inherit Ingest output.schema.json (read-only). All `edl.json` fields will be enforced by `skills/editor-agent/schemas/output.schema.json` (schemas-day LOCK target). The map below is the field-level contract that day's schemas MUST enumerate.

### 10.1 The field map (26 rows — lineage + plan passthrough + timecode transform + committed copy + per-check evidence + EDL aggregate)

**Lineage + identity rows (rows 1–11):**

| Source field | `edl.json` destination | Transform | Mechanic |
|--------------|------------------------|-----------|----------|
| `metadata.parent_chain[0]` (brief_id) | `parent_chain[0]` | Passthrough — first element of inbound tuple. | Verbatim copy. |
| `metadata.parent_chain[1]` (script_id) | `parent_chain[1]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[2]` (storyboard_id) | `parent_chain[2]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[3]` (production_plan_id / rendered_shots_set_id) | `parent_chain[3]` | Passthrough (mode-dependent semantics per Style Replication §10). | Verbatim copy. |
| `metadata.parent_chain[4]` (replication_set_id) | `parent_chain[4]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[5]` (preflight_report_id) | `parent_chain[5]` | Passthrough — QC Pre-flight's 6-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the QC 6-tuple LOCKs. |
| `metadata.parent_chain[6]` (asset_manifest_id) | `parent_chain[6]` | Passthrough — Ingest's 7-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the Ingest 7-tuple LOCKs. |
| `metadata.parent_chain[7]` (edit_plan_id) | `parent_chain[7]` | Passthrough — Edit Director's 8-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the Edit Director 8-tuple LOCKs. |
| Generated by this agent | `parent_chain[8]` (edl_id) | NEW — **9-tuple extension.** | Agent generates a fresh `edl_id` (UUIDv7 per Cross-SPEC §3.9 ID canon) and appends at position [8]. **QUADRUPLY-DEFERRED: gated on the Cross-SPEC §3.9 n-tuple amendment ratification AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it (all operator-pending — see §10.4 / §14.7). Schema holds additively (`minItems: 5`, `prefixItems` 0–8, `maxItems: 9`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. Editor is the FOURTH forcing function for the amendment.** |
| `metadata.brand_id` | `reel_ref.brand_id` | Passthrough. | v1.0 expected value = `"REINVENTED"`. |
| `reel_ref` triple derived | `reel_ref.{brand_id, edit_plan_id, edl_id}` | Derived reel reference triple. | The join keys for cross-record audit. `edl_id` is this agent's emitted identity. |

**Plan passthrough + timecode-transform rows (rows 12–18):**

| Source | `edl.json` destination | Transform | Mechanic |
|--------|------------------------|-----------|----------|
| `edit_plan.cut_order[*].{shot_ref, asset_uri}` | `edl.events[*].{shot_ref, asset_uri}` | Passthrough (joined by event order). | `shot_ref` + `asset_uri` echoed verbatim (platform-relative — Hard Rule inherit; no absolute URL introduced). The cut identity is the plan's, not re-decided. |
| `edit_plan.cut_order[*].{in_ms, out_ms}` + `asset_bundle.raw_footage[*].duration_sec` | `edl.events[*].{src_in_ms, src_out_ms}` | **TRANSFORM** — the plan's ms intentions → 30fps-frame-aligned source timecodes, validated against declared media duration. | The core conform act. Round to the 30fps grid (33.333ms/frame); assert `src_out_ms <= duration_sec*1000` AND `src_out_ms > src_in_ms`. Over-range → `timecode_out_of_range`. NO byte-level decode — declared duration only. |
| Derived from cut order (Step 5) | `edl.events[*].{rec_in_ms, rec_out_ms}` | **TRANSFORM** — source events → record-timeline positions, gap-free. | Lay events end-to-end; each `rec_in_ms` == prior `rec_out_ms`. A gap/overlap → `timeline_gap_or_overlap`. The conform's timeline math. |
| `edit_plan.transitions` (const) | `edl.events[*].transition` | TRANSFORM → per-event `"cut"`. | Every boundary emitted as a hard `cut`. A demanded non-cut → `transition_policy_violation`. Brand rule enforced at the timeline layer. |
| `edit_plan.caption_lines[*].{at_ms, text, line}` | `edl.caption_events[*].{at_ms, text, line}` | **PASSTHROUGH — byte-faithful copy + placement.** | `text` copied BYTE-FOR-BYTE (NO re-authoring — Hard Rule #9); `at_ms` placed on the conformed timeline. A deviation → `plan_fidelity_breach`. |
| `edit_plan.lower_thirds[*].{at_ms, content, case, align}` | `edl.lower_third_events[*].{at_ms, content, case, align}` | PASSTHROUGH — byte-faithful copy + placement. | `content` copied byte-for-byte; `case: "lowercase"` / `align: "left"` re-asserted (not re-derived). A deviation → `plan_fidelity_breach`. |
| `edit_plan.end_card` + `edit_plan.music_bed` + `music_swell_map[]` | `edl.end_card_event` + `edl.music_event` + swell markers | PASSTHROUGH (copy + URI) + TRANSFORM (placement). | `end_card_event.line` byte-faithful; `music_event.asset_uri` passthrough at t0; swell positions marked as conform markers (Sound finalizes — NOT Editor). An unresolvable bed → `asset_unresolved`. |

**Resolution-reference rows (rows 19–20 — read-only validation inputs):**

| Source | `edl.json` usage | Transform | Mechanic |
|--------|------------------|-----------|----------|
| `asset_bundle.raw_footage[*].{asset_uri, duration_sec}` | (validation reference — not echoed as new content) | READ-ONLY resolution fact. | Resolve each `cut_order[].asset_uri` → media handle; validate timecodes against `duration_sec`. Editor consumes these as fixed facts — it does NOT re-decode media. |
| `asset_bundle.{audio[], music_bed}` | `edl.music_event` resolution | READ-ONLY resolution fact. | Confirm the music bed + voice track resolve; an unresolvable handle → `asset_unresolved`. |

**Per-check evidence rows (rows 21–24 — derived verification, NO creative authorship):**

| Source / generated | `edl.json` destination | Transform | Mechanic |
|--------------------|------------------------|-----------|----------|
| Generated (Step 1) | `plan_precondition_check` | NEW — `{edit_plan_id, verdict_observed, lever3_signoff_present}`. | The precondition evidence. `verdict_observed == "plan_ready"` OR `lever3_signoff_present == true` required for any conform to proceed. |
| Generated (Steps 4–5, 9) | `conform_check` | NEW — `{timeline_gap_free, no_double_spend, all_events_bounded_by_declared_duration, frame_aligned, total_timeline_ms, duration_in_band}`. | `duration_in_band == (45000 <= total_timeline_ms <= 75000)`. ALL booleans `true` required for `edl_ready`. |
| Generated (Steps 3, 6–9) | `plan_fidelity_check` | NEW — 6 fields: `{cut_count_matches_plan, caption_copy_byte_faithful, lower_third_copy_byte_faithful, end_card_byte_faithful, transition_policy_hard_cuts_only, plan_evidence_hash_verified}`. | ALL `true` required for `edl_ready`. Any `false` → `plan_fidelity_breach`. The byte-faithful executor invariant. |
| Generated (Step 8) | `edl_firewall_pass_10` | NEW — `{status, passthrough_text_fields_scanned, hits}`. | The 10th-pass result on the COMMITTED passthrough-text surface. `hits` MUST be 0 for `edl_ready`; any hit → `edl_firewall_breach`. `passthrough_text_fields_scanned` = the true committed-field census (every caption event + lower-third event + the end-card). |

**EDL aggregate rows (rows 25–26):**

| Source / generated | `edl.json` destination | Transform | Mechanic |
|--------------------|------------------------|-----------|----------|
| Generated (Step 10) | `output_type` + `verdict` + (non-ready) `failure_code`/`failed_check_id`/`route_back_to` + `qc_pre_flags[]` | NEW — polymorphic discriminator + headline judgment + routing + ≥4 snake_case predicates. | `output_type ∈ {successEdl, errorEnvelope}`; `verdict ∈ {edl_ready, fail}` (**two verdicts only — NO `revise`; the defining divergence from Edit Director's 3-verdict success-side**). `failure_code` present only on `errorEnvelope` — one of 9 LOCKED codes (§6.3) + `editor_agent_failed` slot-11. `qc_pre_flags[]` ≥4 snake_case (e.g. `timeline_gap_free`, `hard_cuts_only_conformed`, `commit_firewall_clean_pass_10`, `mode_blind_conformed`). |
| Generated (Step 10/11) | `metadata` + `render_target` + `mode_blind_confirm` + `human_review_required` | NEW — Cross-SPEC §3.9 canonical + 6 Editor additions + the mode-blind + render-target self-attestations + Lever-3 default. | 9-tuple parent_chain (held additively) + `edl_class: "primary_9x16"` + `edl_evidence_hash` (SHA-256) + `render_dispatched: false` + `conform_mode: "human_in_the_loop"` + `runtime_environment_class` (see §16, partial 2). `mode_blind_confirm: {production_mode_read: false, consumed: "mode_agnostic_edit_plan"}`. `human_review_required: true` per Rule 13. `cost_incurred_usd` ≈ 0.00. |

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

Four fields are reserved in the field map but not yet active in v1.0:

- **`edl.variant_edls[]`** (1:1 LinkedIn cutdown + other aspect-variant EDLs) — v1.0 conforms the primary 9:16 EDL and echoes `tier_richness_echo.variants_planned` count only; the auto-conformed cutdown EDLs activate in v1.1 (a cutdown is a derived re-conform, lower-leverage than the primary — Open Question 5, resolved as deferred). Deferred.
- **`edl.events[*].frame_exact`** (sub-frame / waveform-accurate conform points) — v1.0 frame-rounds to the declared 30fps grid; sub-frame trim needs byte-level media decode + a runtime editor. Flips active when decode lands (v1.1). Deferred.
- **`render_target.v1_edit_uri` (active write)** — reserved/placeholder in v1.0 (the human writes the v1.mp4 to this path on conform); the agent populates it as a real render handle only when Week 4–5 automation ships (v1.1). Deferred.
- **`edl.nle_project_export`** (Premiere/Resolve XML adapter) — v1.0 emits the JSON EDL + a CMX3600-faithful event view; the native NLE-project export is a derived conform-format convenience that lands with the render automation (Open Question 5). Deferred to v1.1+.

### 10.3 No-touch fields (read-only references)

Read by the agent but never written to its output (audit trail only):

- `edit_plan.brand_edit_check.*` (Edit Director's brand-rule adjudication) — Editor TRUSTS it (the plan is brand-compliant) and re-asserts only the timeline-layer facts it enforces (hard-cuts-only, end-card present); it does NOT re-adjudicate the brand ruleset (Edit Director's jurisdiction; re-adjudicating would imply creative authority Editor does not have).
- `edit_plan.edit_plan_firewall_pass_9.*` — Edit Director's 9th-pass authored-text firewall result. Editor reads it as context (the copy was clean when authored) and runs its OWN 10th pass over the SAME text at COMMIT — a different moment in the lifecycle (authorship vs commit). Read as context, never echoed.
- `preflight_report.cost_ledger_check.*` (denormalized) — read-only context. Editor carries NO cost fields beyond its own `cost_incurred_usd` (Rule 11 — no re-litigation).
- `asset_manifest.spec_check.*` (the per-asset aspect/fps/resolution evidence) — Editor reads `raw_footage[].duration_sec` to validate timecodes; it does NOT re-echo Ingest's spec adjudication (re-validation authority it does not hold).
- `metadata.production_mode` — **explicitly NOT read as a branch discriminator** (Hard Rule #7). Present in the inbound metadata for audit lineage, but Editor's `mode_blind_confirm.production_mode_read: false` attests it never consulted it for the conform. The strongest no-touch field in the fleet — reading it would break the convergence contract two stages deep.
- `accumulated_qc_pre_flags` (upstream union) — consumed as read-only context; Editor appends its own ≥4 predicates without modifying the upstream surface.

### 10.4 Schema authoring note (for the schemas day)

The schema author must encode the field map above as JSON Schema Draft 2020-12 constraints. Specifically:
- `parent_chain` MUST use `prefixItems: [..×9]`, `minItems: 5`, `maxItems: 9`, `items: false` — the **additive hold**. Exact 9-tuple cardinality (`minItems: 9`) is **QUADRUPLY-BLOCKED** until the Cross-SPEC §3.9 amendment ratifies AND the Edit Director 8-tuple LOCKs AND the Ingest 7-tuple LOCKs AND the QC 6-tuple LOCKs behind it; the schema carries a `TODO@cross-spec-3.9-ratification` flip note at the field.
- `output_type` MUST drive a `oneOf [successEdl, errorEnvelope]` polymorphic split.
- `verdict` MUST use `enum: ["edl_ready", "fail"]` — **exactly two values, NO `revise`.** This is the schema's defining divergence from Edit Director (`plan_ready`/`fail`/`revise`) — the executor is deterministic; the success-side has no judgment branch.
- `failure_code` (errorEnvelope branch) MUST use `enum` of exactly the 9 LOCKED codes (§6.3) + `editor_agent_failed`. Schema MUST enumerate `asset_unresolved` and `plan_fidelity_breach` each as a single folded code (NOT split — §6.3 narrowing by shared route-back target, opposite direction from Edit Director keeping `duration_envelope_breach` standalone).
- `events[*].asset_uri` and `music_event.asset_uri` fields MUST use `pattern: "^ars://[a-zA-Z0-9_\\-./]+$"` (platform-relative, Hard Rule inherit).
- `caption_events[*].text` MUST use `maxLength: 22` (the brand caption rule, machine-enforced at the schema layer — re-asserted from the plan, not re-derived).
- `events[*].transition` MUST use `const: "cut"` — the hard-cuts-only rule encoded at the EDL-event layer, not just the prompt.
- `lower_third_events[*].case` MUST use `const: "lowercase"` and `lower_third_events[*].align` MUST use `const: "left"`.
- `end_card_event.line` MUST use `const: "REINVENTED — build on purpose."` and `end_card_event.hold_ms` `const: 1500`.
- `edl.frame_rate` MUST use `const: 30`, `edl.aspect` `const: "9:16"`, `edl.resolution` `const: "1080x1920"` (the format spec encoded at the schema layer — Brand-Voice Intake §8).
- `edl_evidence_hash` and `plan_fidelity_check.plan_evidence_hash` MUST use `pattern: "^[a-f0-9]{64}$"` (lowercase hex, 64 chars).
- `render_dispatched` MUST use `const: false` in the v1.0 schema (the human conforms; automation is v1.1) and `conform_mode` MUST use `const: "human_in_the_loop"`.
- `mode_blind_confirm.production_mode_read` MUST use `const: false` — the convergence guarantee encoded at the schema layer, machine-checkable (the second agent to carry it).
- `conform_check` + `plan_fidelity_check` sub-booleans MUST all be `required` (present, possibly `false`) on the success branch — their presence is the conform-integrity invariant.

### 10.5 Conform-by-tier flatness matrix

Editor's conform logic is **mode-agnostic** (§4) AND **tier-FLAT** (§4 / §7) — the divergence from Edit Director (the only tier-*sensitive* agent in the post tail). The table maps which conform fields/behaviors scale per tier — the answer is **almost none**: only the echoed variant count differs, and even that does not change the conform behavior (v1.0 conforms the primary 9:16 for every tier):

| Field / behavior | Pilot | Starter | Pro | Enterprise | Notes |
|------------------|:-----:|:-------:|:---:|:----------:|-------|
| Conform logic | faithful | faithful | faithful | faithful | **Identical executor path at every tier** |
| `variants_conformed` (v1.0) | 1 | 1 | 1 | 1 | v1.0 conforms the primary 9:16 only |
| `tier_richness_echo.variants_planned` | 3 | 3 | 4 | 5 | Echoed for awareness; auto-conformed v1.1 |
| `edl.frame_rate` / `aspect` / `resolution` | 30 / 9:16 / 1080×1920 | same | same | same | Format spec is universal (Brand-Voice §8) |
| `transition: "cut"` / end-card / byte-faithful copy | ALL | ALL | ALL | ALL | **Conform fidelity is NOT a tier feature** |
| `render_dispatched: false` / `conform_mode: human_in_the_loop` | true | true | true | true | Universal — the human conforms at every tier |
| `mode_blind_confirm.production_mode_read: false` | true | true | true | true | Universal — every tier, every mode |
| `cost_incurred_usd` | ~$0.00 | ~$0.00 | ~$0.00 | ~$0.00 | Zero generative + zero render cost at every tier |

A Pilot reel and a Enterprise reel are conformed by the **identical executor logic** — the richness already lives in the plan Editor receives; Editor faithfully executes whatever envelope arrives. **The plan carries the tier envelope; Editor's conform does not scale.** This is the same tier-flat discipline Ingest holds — a technical executor does not re-litigate the tier ladder. The matrix is the basis for the SKILL bundle's tier-flat logic on the SKILL-build day.

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 67 · status updates · on-time trajectory)

**Calendar inherited from outline §0 build calendar — on schedule, no slip.** Day 67 author task per outline: partial 1 (§6 + §7 + §10 + §14). On-disk file-state confirms the chain is intact through Day 66; this document ships partial 1 ON the calendar. Partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16) targets Day 68 (Fri Jun 26).

### 14.1 Calendar (Day 66 → v1.0 LOCK — Editor trajectory)

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 66 | Wed Jun 24 · Wk10 | **Editor v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 67 | Thu Jun 25 · Wk10 | **SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14) SHIPPED** | ✅ DONE (this doc) | Donna overnight |
| Day 68 | Fri Jun 26 · Wk10 | SPEC body partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16) | ⏳ NEXT | Donna overnight |
| Day 69 | Sat Jun 27 · Wk10 | v1.0 LOCK CANDIDATE (full §3 self-audit + critical-decisions walk + verdict math) | ⏳ planned | Donna overnight |
| Day 70 | Sun Jun 28 · Wk10 | **REST DAY — no build** (pre-stage schemas scaffold only) | ⏳ Rest Day | — |
| Day 71 | Mon Jun 29 · Wk11 | input.schema.json + output.schema.json (the 9-tuple additive hold + the 2-verdict enum + brand/format `const`s) | ⏳ planned | Donna overnight |
| Day 72+ | TBD | SKILL bundle (`skills/editor-agent/`) → Editor LLM-test runbook → v1.0 LOCK candidate close | ⏳ planned | Donna overnight |

**Cadence note:** This trajectory mirrors the proven Edit Director Day 58→65 and Ingest Day 48→57 8-day agent-build cadence (outline → 2 body partials → LOCK candidate → schemas → SKILL → runbook → LOCK). The Day 70 Rest Day falls between the LOCK candidate and the schemas — pre-stage only, no SPEC content (the Day 21/28/35/42/49/56/63 Rest Day-compounding pattern).

### 14.2 What partial 2 (Day 68) authors

Reserved sections, with the pre-scaffolded scope from the outline §6–§16 preview:
- **§8 Performance Targets** — 9 metric categories. Schema validity 100% / plan-fidelity 100% (a conformed copy/order deviation must never survive) / commit-time firewall catch 100% / timecode-in-range 100% / gap-free 100% / false-edl-ready rate 0% target / false-fail rate ≤8% (over-flagging a borderline timecode to `fail` is the acceptable direction) / p50 latency 25s / p95 75s (conform reasoning — lighter than Edit Director's authoring) / zero engine + zero render cost.
- **§9 Test Fixtures** — 5-fixture portfolio: TC-01 clean Mode-A→plan Pro `edl_ready` (full EDL) · TC-02 Mode-C Enterprise `edl_ready` (mode-blind conform-convergence proof — byte-identical conform path to TC-01 despite different origin) · TC-03 `timecode_out_of_range` → fail+route to Edit Director (a cut out_ms exceeds declared media) · TC-04 `asset_unresolved` → fail+route to Ingest (a cut_order asset_uri not in the bundle) · TC-05 `edl_firewall_breach` (a banned token in a committed passthrough lower-third reaching commit — the 10th-pass last-line catch; GATING fixture). TC-01/TC-02 carry the mode-blind conform-convergence proof. Optional probes: `plan_fidelity_breach` (tampered `plan_evidence_hash`) + slot-11 `editor_agent_failed`.
- **§11 Cost Model** — zero-engine + zero-render snapshot + faithful-conform value model. Explicit note: the actual render compute spend lands in v1.1 Week 4–5 automation — v1.0 is $0 by construction.
- **§12 Verdict Math** — `EDL_READY = (Edit Director precondition) ∧ (plan_evidence_hash verified) ∧ (all assets resolved) ∧ (all timecodes in range) ∧ (timeline gap-free + no double-spend) ∧ (transitions hard-cuts-only) ∧ (all events frame-aligned) ∧ (duration in band) ∧ (plan-fidelity byte-faithful) ∧ (commit-time firewall clean)`. Any single ∧-term false → `fail` (NO `revise` branch). Fully deterministic — zero judgment slots (the defining divergence from Edit Director's one `revise` slot).
- **§13 Critical Decisions LOCKED** — 14 pre-scaffolded decisions (outline §13). The §10 9-tuple decision (#7, quadruply-deferred) and the Sound-handoff-target decision (Open Question 4) are the only forward edit slots.
- **§15 Change Log** — v1.0 lifecycle entries (outline-66 → body-67 → body-68 → LOCK-candidate → schemas → SKILL → runbook → LOCKED) + parked-candidates list.
- **§16 Metadata Block Schema** — Cross-SPEC §3.9 canonical + 6 Editor additions (9-tuple parent_chain, edl_class, edl_evidence_hash, render_dispatched const false, conform_mode, runtime_environment_class).

### 14.3 What this partial LOCKED (Day 67)

- **§6** — 11-check self-QC list, 4-tier ordering, 9-code errorEnvelope namespace + slot-11, the 2-verdict model (`edl_ready`/`fail` — NO `revise`), the 11-entry firewall list applied to COMMITTED passthrough text (10th pass, commit-time layer). LOCKED-as-drafted.
- **§7** — full LLM system prompt (frame + 13 hard rules + universal-access tier-FLAT table + 11-step conform loop + Blueprint §4.10 EDL shape inlined + 9:16/1080×1920/30fps format spec + voice rule). LOCKED-as-drafted; copies verbatim into SKILL.md on the SKILL-bundle day.
- **§10** — 26-row field map (transform/passthrough/derived split, ZERO authored rows) + reserved fields + no-touch fields (incl. the `production_mode` non-read) + schema authoring note (the 9-tuple additive hold + the 2-verdict enum + brand/format `const`s) + tier-flatness matrix. LOCKED-as-drafted.
- **§14** — this calendar + status. LOCKED-as-drafted.

### 14.4–14.7 Carried dependencies + operator gates (surfaced, NOT advanced)

- **§14.4 — Predecessor LOCK ceremonies (5, operator-only):** AI Video Gen v1.0, Style Replication v1.0, QC Pre-flight v1.0, Ingest v1.0, Edit Director v1.0 — all five STILL PENDING (file-state confirmed; version tags unflipped). They gate Editor's eventual v1.0 LOCK. The **Edit Director 8-tuple LOCK is Editor's DIRECT 9-tuple dependency** (the `plan_ready` precondition + the 8-tuple the 9-tuple extends).
- **§14.5 — LLM Test Runbook executions (4, operator-only):** Day 36 Style Replication, Day 47 QC Pre-flight, Day 57 Ingest, Day 65 Edit Director — all paste-and-run, all pending. 5/5 each opens the respective LOCK gate.
- **§14.6 — Edit Director Day 61 LOCK-candidate items (carried):** Item 6 (cost-model confirm ~$0.00, recommend RATIFY); Item 8 (15-decisions walk — D15 Editor handoff to the Notion Edit Plan holding store now DIRECTLY relevant, recommend RATIFY D15); Item 11 (§3.9 amendment review = carried item below).
- **§14.7 — Cross-SPEC §3.9 n-tuple amendment ratification (operator-only):** now **QUADRUPLY load-bearing** (QC 6-tuple + Ingest 7-tuple + Edit Director 8-tuple + **Editor 9-tuple**). Until ratified AND the chain LOCKs, all four n-tuples stay at the additive `minItems: 5` hold. Recommend RATIFY-AS-DRAFTED — Editor is the fourth forcing function.

---

## Cross-SPEC §3 adherence (partial-1 re-confirm — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `editor-agent` (kebab-case); slot-11 `editor_agent_failed` |
| §3.2 hash invariant | ✅ `edl_evidence_hash` SHA-256 over the edl + conform_check + plan_fidelity_check block (§6.1 #11 / §10); `plan_evidence_hash` re-verified (inherits Edit Director's anchor) |
| §3.3 errorEnvelope shape | ✅ §6.3 mirrors fleet shape (failure_code, failed_check_id, attempts, detail, cost_incurred_usd, route_back_to, metadata, human_review_required) + adds `verdict` + `route_back_to` |
| §3.4 qc_pre_flags minItems 4 | ✅ §6.1 #11 + §10 row 25 enforce ≥4 snake_case predicates |
| §3.5 Mode coverage matrix | ✅ §6.1 #11 mode-blind self-attestation — the SECOND agent for which the mode columns are identical (convergence proof two stages deep) |
| §3.6 Slot 11 naming canon | ✅ `editor_agent_failed` (§6.1 #11, §6.3) |
| §3.7 qc_pre_flags format | ✅ snake_case predicates (§6.1 #11) |
| §3.8 Tier↔mode firewall (10th defense-in-depth) | ✅ §6.1 #9 COMMIT-time passthrough firewall (last checkpoint before pixels) + §7 universal-access tier-FLAT table |
| §3.9 Metadata + n-tuple parent_chain | ✅ §10 inherits canonical + extends to 9-tuple, held additively. **Quadruply-deferred** — gated on the §3.9 amendment ratification AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK |
| §3.10 Cost ceiling authority | ✅ §7 Hard Rule #11 DECLINES to re-litigate cost (QC's authority), re-validate assets (Ingest's authority), OR re-direct the cut (Edit Director's authority) — $0-cost agent |
| §3.11 LOCK respect | ✅ This partial does NOT modify any LOCKED canon — all predecessor SPECs / schemas / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at partial-1 stage.** Full §3 self-audit embedded in the Day 69 LOCK candidate.

---

## Files produced today (Day 67)

- `ars/ARS-2026-06-25-Day-67-Editor-Agent-SPEC-Body-Partial-1.md` — this doc
- `ars/build-log-2026-06-25.md` — Day 67 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 67)

- ✅ **No LLM dispatched.** No render API, no engine credentials referenced, no vendor URLs walked, no media render, no byte-level decode. (Editor by design authors an EDL and renders no pixels in v1.0 — the human conforms; full automation is the Week 4–5 v1.1 scope.)
- ✅ **No external comms transacted.** No emails, no DMs, no social posts, no client/investor outreach. The end-of-run status iMessage to Jamila ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business. (Notification-channel status carried — see build log.)
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, no render compute, ZERO $ spent.
- ✅ **No operator-impersonation.** AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director LOCK ceremonies NOT assumed — all five confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Edit Director Day 61 Items 6/8/11 + the four runbook executions NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed. The 9-tuple stays held additively (`minItems: 5`), NOT flipped to exact-9.
- ✅ **No fake-advance.** This partial is forward-design over LOCK-stable text artifacts only, explicitly labeled BODY PARTIAL 1. Zero net-new modifications to any LOCKED canon. Editor v1.0 LOCK will hard-gate itself on the upstream LOCKs (especially the Edit Director 8-tuple) being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §6.5 enumerates HC/NPOX tokens precisely so the agent can BLOCK them in the copy it COMMITS — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence re-confirm complete.** 11 of 11 dimensions ✅ at partial-1 stage. Full LOCK audit at the Day 69 LOCK candidate.
- ✅ **Pattern source acknowledged.** Edit Director Day 59 partial 1 (§6/§7/§10/§14) structure inherited verbatim. Orchestration Blueprint §4.10 (EDL shape) + Cross-SPEC §3 + Brand-Voice Intake §7–§11 used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-67 build runs Thursday (Pacific). Next Rest Day: Day 70 (Sun Jun 28 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 67 ships clean. Day 68 build session targets SPEC body partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16). Editor is Agent #10 of 17 — the 10th defense-in-depth firewall (the COMMIT-time passthrough re-scan, the last text checkpoint before pixels), the first executor agent in the post tail, and the second contractually mode-blind agent (the continued proof that Ingest's mode-convergence seam holds two stages deep). This partial LOCKs the self-QC list (11 checks, 9 codes + slot-11, the 2-verdict model with NO `revise`), the full LLM system prompt (13 hard rules incl. conform-faithfully-never-re-author + author-an-EDL-never-render + recommend-don't-render), and the 26-row field map (transform/passthrough/derived split with ZERO authored rows — the executor's signature + the quadruply-deferred 9-tuple + the 2-verdict enum + brand/format `const`s machine-enforced at the schema layer). Editor is the inflection the whole fleet was built toward (first output destined for a media file) — yet v1.0 produces NO media: it authors the EDL the human conforms (`render_dispatched: const false`, render automation deferred to Week 4–5), keeping the zero-dollar / no-render invariant intact. Operator pickup: (1) the five predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight + Ingest + Edit Director) remain pending and gate Editor's eventual v1.0 LOCK — the Edit Director 8-tuple is the direct 9-tuple dependency; (2) execute the four pending runbooks (Day 36 / Day 47 / Day 57 / Day 65); (3) ratify the Cross-SPEC §3.9 n-tuple amendment so the 9-tuple is canon (Editor is now the fourth forcing function). Day 70 (Jun 28) = next Rest Day.*
