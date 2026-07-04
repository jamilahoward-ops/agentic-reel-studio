# ARS — Sound Agent v1.0 SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14)

**Date:** Fri Jul 3, 2026 (Day 75 · Wk11 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 1 — §6 + §7 + §10 + §14 LOCKED-as-drafted Day 75. §8 + §9 + §11 + §12 + §13 + §15 + §16 reserved for partial 2 (Day 76 target, Sat Jul 4). v1.0 LOCK CANDIDATE + schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK follow on the established cadence (Editor Day 69–73 / Edit Director Day 61–65).
**Pattern source:** `ARS-2026-06-25-Day-67-Editor-Agent-SPEC-Body-Partial-1.md` §6/§7/§10/§14 (Day 67 partial 1 — proven shape inherited verbatim) and `ARS-2026-06-17-Day-59-Edit-Director-Agent-SPEC-Body-Partial-1.md` (grandparent pattern).
**Outline source:** `ARS-2026-07-02-Day-74-Sound-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 74 + the §6–§16 LOCK-scope preview this partial authors against).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — pipeline roster position 12 "Sound" + §3 mode-agnostic post-production contract + §4.10 Editor→Sound `EDL + v1 edit` payload + §4.11 Sound→Motion `v2 edit with finalized audio` handoff shape + §6 dispatch table row 12 "On Editor v1" + §7 read/write I/O (writes Drive `/reels/[reel_id]/v2.mp4`) + §9 build-checklist row 12 "Human-in-the-loop for Week 2; full automation Week 4–5").
**Brand-audio canon:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (voice / tone), §8 (reel format specs: 9:16 · 1080×1920 · 30fps · 45–75s structure), §11 (caption ↔ VO cadence) + Blueprint §1.2 / §4.12 loudness targets (**−14 LUFS IG/TT primary · −16 LUFS YT flagged**) — the audio-finishing rules the conform spec must specify faithfully.
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen v1.0 LOCK candidate + schemas + SKILL + Day 27 runbook. Style Replication v1.0 LOCK candidate + schemas + SKILL + Day 36 runbook. QC Pre-flight v1.0 LOCK candidate + schemas + SKILL + Day 47 runbook. Ingest v1.0 LOCK candidate + schemas + SKILL + Day 57 runbook. Edit Director v1.0 LOCK candidate + schemas + SKILL + Day 65 runbook. Editor v1.0 LOCK candidate (Day 69) + schemas (Day 71) + SKILL + Day 73 runbook. **All SIX predecessor LOCK ceremonies remain OPERATOR-GATED entering Day 75 — file-state confirmed (version tags unflipped). This partial 1 references LOCK-as-drafted canon (text-stable) without depending on operator-gated ratification — the same posture Editor Day 67 partial 1 held over its five predecessors, and Edit Director Day 59 over its four.**

> **Cadence honesty (on schedule — surfaced):** The Day 74 outline calendared partial 1 for **Day 75 (Fri Jul 3)** and partial 2 for Day 76 (Sat Jul 4). On-disk file-state confirms the chain is intact: Day 74 outline shipped (Thu Jul 2), Day 73 Editor runbook before it (Wed Jul 1), Day 70 (Sun Jun 28) correctly a Rest Day no-build. Tonight's Day 75 session ships partial 1 (this document) ON the outline calendar — no slip. The §14 calendar below encodes the on-time trajectory. Next Rest Day: Day 77 (Sun Jul 5).

> **Note on the scheduled-task prompt's "Agent #7 QC Pre-flight" pointer:** still stale (carried unchanged since Day 48; reconciled in every log since). On-disk source of truth (read first, per standing rule) shows the fleet well past #7: QC Pre-flight (#7) complete Day 40→47; Ingest (#8) complete Day 48→57; Edit Director (#9) complete Day 58→65; Editor (#10) complete Day 66→73 (full v1.0 artifact set); Sound (#11) outline shipped Day 74, this partial 1 tonight. Followed the on-disk position, not the prompt's pointer. Surfaced, not silently reconciled.

> **Authoring discipline (LOCK signal):** §6 + §7 + §10 + §14 are LOCKED-as-drafted Day 75. The §13 critical-decisions walk on partial 2 (Day 76) may amend §10's 10-tuple parent_chain extension decision (quintuply-gated — see §10.4 / §14.7), the errorEnvelope code count (7–9 target), the self-QC check count (10–12), the loudness dual-master scope, and the Motion-handoff-target decision (Open Question 4); those are the only forward-looking edit slots in this partial 1. Everything else is canon as of this document.

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this partial's authoring, on-disk file-state confirms **all six predecessor LOCK ceremonies remain OPERATOR-GATED** (AI Video Gen, Style Replication, QC Pre-flight, Ingest, Edit Director, Editor — version tags unflipped; Day 36 + Day 47 + Day 57 + Day 65 + Day 73 runbook executions unconfirmed). Sound v1.0 LOCK will hard-gate itself on those closing first — the **Editor 9-tuple in particular is Sound's direct 10-tuple dependency**, and the Editor LOCK is itself behind the Edit Director 8-tuple LOCK, behind the Ingest 7-tuple LOCK, behind the QC 6-tuple LOCK. This body partial is forward-design over LOCK-stable text artifacts only, with zero production output consumed, zero DSP dispatched, zero waveform decoded, and zero operator ceremony assumed.

---

## §6 — 11-Check Self-QC List (LOCKED-as-drafted Day 75)

The Sound Agent runs this 11-check list **on its own audio conform spec** before emitting `successAudioSpec` (or before finalizing an `errorEnvelope`). Check shape inherited verbatim from the fleet §6 pattern (proven 10× — Brief through Editor; Sound is the 11th defense-in-depth firewall pass). Failure semantics are LOCKED inheritance: retry once on a recoverable self-QC failure, halt on the second.

**Critical distinction — self-QC vs. the finish loop:** The **11-step finish loop (§5, outline)** is the agent authoring the *audio conform spec* from the EDL + resolved audio bundle; the **§6 self-QC list (this section)** is the agent adjudicating *its own audio spec* — confirming the spec it is about to emit is EDL-faithful, loudness-in-spec, marker-in-timeline, brand-faithful, firewall-clean on the passthrough VO transcript it touches, and free of the operator/finish-impersonation anti-pattern, before that spec becomes the audio app's (and Motion's) source of truth. A FAIL in §6 means the agent built a malformed finish spec, not that the cut failed. The creative verdict (plan_ready) was Edit Director's; the conform verdict (edl_ready) was Editor's; the §6 result decides whether the audio spec is fit to ship to the finish queue.

**QC retry policy (inherited, LOCKED):** First self-QC failure → regenerate the offending audio-spec field set with concrete fix instructions inlined into the next attempt. Second self-QC failure → emit `errorEnvelope` with `failure_code: "sound_agent_failed"`, `attempts == 2`, halt. **No third attempt.** Same 2-strike contract every agent in the pipeline honors.

**Defense-in-depth (11th pass — the AUDIO-domain passthrough layer):** The prior ten passes scanned text the pipeline received, authored (Edit Director, 9th pass), OR committed to the executable cut spec (Editor, 10th pass). Sound authors **no new copy** — the VO transcript is Script/Editor passthrough. But Sound is the agent that **finishes the SPOKEN audio** — the moment the voice track is leveled, de-essed, and mixed into the mastered reel — so it re-scans the declared VO transcript one final time before the mix reaches Motion. This is **not a new authorship surface** — it is a **passthrough-integrity + audio-finish** re-scan, the **last AUDIO checkpoint before Motion typography**. Because Sound calls **no generative engine, decodes no waveform, and runs no DSP**, a self-QC failure here never wastes spend — but a *missed* failure (a banned-entity token that survived the 10th commit pass, sits in the VO transcript, and is mastered into the audio) is the exact defect class the 11th pass exists to prevent. A leak that survives the finish rides into the mastered v2 audio.

### 6.1 The 11 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **Editor precondition verified — the consumed `edl.json` has `verdict == "edl_ready"` AND `output_type == "successEdl"`.** | `upstream_edl_not_ready` | Runs FIRST. Assert the EDL's `verdict` is `edl_ready` and `output_type` is the success branch. Otherwise halt — Sound never finishes an unlocked cut, and does NOT auto-resolve a failed EDL (the fix belongs upstream — Sound inherits the recommend-don't-override discipline). Cite the `edl_id` + verdict in `detail.edl_precondition`. The audio spec MUST carry `edl_precondition_check: {edl_id, verdict_observed}` — a missing/uncomputed block = self-QC FAIL. |
| 2 | **Upstream success verification — the consumed EDL is its success type, NOT `errorEnvelope`.** | `upstream_not_success` | Assert the primary input `output_type == "successEdl"`. A consumed `errorEnvelope` = halt — you cannot finish a failed conform output. Cite the failed `edl_id` in `detail.upstream_failure`. (Folds with Check #1 at the precondition gate but carries its own code for route-back attribution.) |
| 3 | **EDL-evidence verify + audio-asset resolution — `edl_evidence_hash` recomputes AND the VO voice track + music bed both resolve against the Ingest `asset_bundle`.** | `spec_fidelity_breach` (hash) / `vo_track_missing` \| `audio_asset_unresolved` (resolution) | Two-part. **Part 1:** recompute the `edl_evidence_hash` (SHA-256 over the EDL's `edl` + `conform_check` + `plan_fidelity_check`); a mismatch means the EDL was tampered post-conform → `spec_fidelity_breach`. **Part 2:** resolve the `asset_bundle.audio[]` voice track → missing → `vo_track_missing` (route back to Ingest); resolve the `music_event.asset_uri` music bed against `asset_bundle.music_bed` → unresolvable → `audio_asset_unresolved` (route back to Ingest). The spec's `audio_conform_check` block MUST carry `{vo_track_resolved, music_bed_resolved, edl_evidence_hash_verified}` — an uncomputed sub-status = self-QC FAIL; a genuine gap = valid `fail` carrying the mapped code. |
| 4 | **Marker-in-timeline — every mix/SFX/duck-envelope marker `at_ms` is `>= 0` AND `<= total_timeline_ms`, and the spec's audio timeline duration matches the EDL.** | `audio_marker_out_of_range` | For each `duck_envelope[]`, `sfx_accents[]`, and mix directive: assert `at_ms >= 0` AND `at_ms <= edl.total_timeline_ms` (no accent past the timeline, no negative time). An over-range marker = valid `fail` (`audio_marker_out_of_range`, route back to Editor — a timeline/EDL defect); `detail` names the offending marker + the timeline bound. Confirm the audio timeline duration equals the EDL `total_timeline_ms`; a mismatch surfaces as `spec_fidelity_breach`. An uncomputed `audio_conform_check.all_markers_in_timeline` = self-QC FAIL. |
| 5 | **Loudness-target-in-spec — the loudness target is the platform const (−14 LUFS IG/TT primary; −16 LUFS YT flagged) AND the true-peak ceiling is in band (−1.0 dBTP).** | `loudness_target_out_of_spec` | Assert `audio_spec.loudness_target.primary == "-14 LUFS (IG/TT)"` (or the −16 YT variant when flagged per `tier_richness_echo`) AND `true_peak_ceiling_dbtp == -1.0`. If a target is not the platform const or the true-peak is out of band → `loudness_target_out_of_spec` (`detail` names the target). **Platform loudness spec enforced at the audio layer, not just the prompt** — Sound is the gate where the loudness target becomes canon before a mixer (or a renderer) burns a cycle. Zero tolerance. NO byte-level LUFS measurement in v1.0 — the target is a DECLARED conform goal, not a measured value. |
| 6 | **Spec-fidelity of the mix directives — the music event, swell markers, and timeline duration are byte-faithful to the EDL; the VO transcript passthrough is byte-faithful.** | `spec_fidelity_breach` | Assert the `audio_spec.music_bed.asset_uri` + `at_ms` match the EDL `music_event` exactly, the `duck_envelope[]`/`sfx_accents[]` swell moves are mapped from (not deviating from) the EDL `music_swell_map[]`, `timeline_duration_matches_edl == true`, AND the `vo_transcript[].text` the VO polish references is byte-identical to the EDL passthrough (NO re-authoring — Sound touches no copy). Any deviation = an unauthorized override → `spec_fidelity_breach`. The `spec_fidelity_check` block MUST carry `{music_event_matches_edl, swell_markers_match_edl, timeline_duration_matches_edl, vo_transcript_byte_faithful, edl_evidence_hash_verified}` — an uncomputed sub-status = self-QC FAIL. |
| 7 | **Author-a-spec-never-process — the audio spec carries `audio_processed: const false` + `finish_mode: "human_in_the_loop"`; no directive claims applied DSP.** | `sound_agent_failed` (slot-11 catch) | Assert `finish_target.audio_processed == false` AND `finish_target.finish_mode == "human_in_the_loop"`. Every directive is a *declared spec* (level target, duck-dB, SFX placement) — NOT applied DSP. An audio spec claiming a processed/normalized waveform it never touched is forged provenance (the audio analog of Editor's `render_dispatched: true` forgery). A `true` here on the v1.0 branch = malformed spec → self-regen; second failure → `sound_agent_failed`. |
| 8 | **Audio-domain firewall pass (11th defense-in-depth pass — the passthrough VO transcript Sound finishes).** | `audio_firewall_breach` | Walk every declared `vo_transcript[].text` field with token-boundary, case-insensitive matching against the 11-entry canonical firewall list (§6.5 — inherited verbatim, never extended per-agent). Any hit = halt + forensic log naming the leaking VO transcript field + the rule it violated. **This is the AUDIO-domain checkpoint:** Sound authors no new copy (Editor already firewall-scanned the caption/lower-third/end-card text at the 10th commit pass), but Sound is the agent that finishes the SPOKEN audio — so a final firewall re-scan of the VO transcript before the mix reaches Motion is the last-line audio catch. The spec's `audio_firewall_pass_11` block MUST carry `{status, passthrough_transcript_fields_scanned, hits}` with `passthrough_transcript_fields_scanned` equal to the true VO-transcript-field census. An undercounted scan = self-QC FAIL; a genuine hit = `audio_firewall_breach`. |
| 9 | **Audio-conform completeness — VO track resolved, music bed resolved, all markers in the timeline, loudness in spec, total timeline in the 45–75s band.** | `audio_marker_out_of_range` / `vo_track_missing` / `audio_asset_unresolved` (routed per cause) | Run `audio_conform_check`: `{vo_track_resolved, music_bed_resolved, all_markers_in_timeline, loudness_target_in_spec, total_timeline_ms, duration_in_band}`. `duration_in_band == (45000 <= total_timeline_ms <= 75000)` (re-asserted from the EDL's duration, NOT re-derived). Out-of-band or unresolved → routed as `audio_marker_out_of_range` / `vo_track_missing` / `audio_asset_unresolved` per the offending cause. An uncomputed sub-status = self-QC FAIL. |
| 10 | **Lineage integrity — inbound `parent_chain` is a well-formed 9-tuple (5/6/7/8-tuple accepted additively until the §3.9 amendment + the Editor 9-tuple LOCK) AND the 10-tuple extension is structurally valid.** | `audio_lineage_failure` | Two-part forensic assertion. **Part 1 (inbound):** the consumed `metadata.parent_chain` is a well-formed 9-tuple from Editor (5/6/7/8-tuple accepted for backward-compat until the Cross-SPEC §3.9 amendment ratifies AND the Editor 9-tuple LOCKs — the quadruple gate behind the Edit Director 8-tuple, behind the Ingest 7-tuple, behind the QC 6-tuple). **Part 2 (outbound):** the agent's own 10-tuple extension (append `audio_spec_id`, UUIDv7) is structurally valid and held additively (`minItems: 5`). Malformed either way → halt; should NEVER fire in a healthy pipeline — if it does, the audit chain is broken and the spec is held for forensic review. |
| 11 | **Output shape + recommend-don't-process — the audio spec validates against `output.schema.json`, carries `audio_spec_evidence_hash` + `audio_processed: const false` + `finish_mode: "human_in_the_loop"` + `mode_blind_confirm.production_mode_read == false`, emits ≥4 snake_case `qc_pre_flags[]`, and `human_review_required == true`.** | `sound_agent_failed` (slot 11 reserved per Cross-SPEC §3.6) | Final emission gate. The spec MUST validate against `output.schema.json` (schemas-day LOCK target); MUST carry `audio_spec_evidence_hash` = SHA-256 over the `audio_spec` + `audio_conform_check` + `spec_fidelity_check` block (`^[a-f0-9]{64}$`); MUST carry `audio_processed: false` (v1.0 honesty — a spec claiming a mix it never processed is forged provenance; the human finishes in v1.0, automation in Week 4–5) AND `finish_mode: "human_in_the_loop"`; MUST carry `mode_blind_confirm.production_mode_read == false` AND `consumed == "mode_agnostic_edl"` (the mode-blind self-attestation — no field branches on origin mode A/B/C); MUST emit ≥4 snake_case (§3.7) `qc_pre_flags[]` (examples that PASS: `"loudness_target_in_spec"`, `"vo_track_resolved"`, `"audio_firewall_clean_pass_11"`, `"mode_blind_finished"`); AND MUST carry `human_review_required: true` per the recommend-don't-process discipline (Lever-3 default + the v1.0 human-in-the-loop finishing posture — Sound emits an audio-spec *recommendation*, never a ratified "processed" or "approved-for-Motion" state). Any violation = halt. A finish that consulted `production_mode` to build the spec maps here (mode-blind violation = malformed finish). Slot-11 naming canon: agent_id `sound-agent` → `sound_agent_failed` per Cross-SPEC §3.6. |

### 6.2 Check ordering rationale

Checks 1–2 are **gate-entry validations** (run FIRST — a failed Editor precondition or a consumed `errorEnvelope` halts before any audio spec is authored; no point finishing a reel whose cut never passed). Checks 3–9 are **the seven finish adjudications** (EDL-evidence + audio-asset resolution, marker-in-timeline, loudness-target-in-spec, spec-fidelity of the mix directives, author-a-spec-never-process, audio-domain firewall, audio-conform completeness — the substance of the finish decision). Check 10 is **the forensic gate** (lineage — the path that defers to forensic review rather than rendering a verdict). Check 11 is **the construction-integrity gate** (output shape + evidence hash + mode-blind self-attestation + audio_processed-false + recommend-don't-process — it confirms the audio spec is fit to become the audio app's and Motion's source of truth).

This ordering mirrors the proven 4-tier fleet shape (entry / substance / deferral / handoff), with Sound's defining adaptation: **because the agent spends ~$0.00, decodes no waveform, and runs no DSP, the ordering minimizes wasted finish** (fail fast on an unlocked-cut payload) and guarantees the recommend-don't-process discipline (Check 11) is the LAST thing verified before emission, so a malformed `audio_ready` — an audio spec with a firewall leak in the passthrough VO transcript, an out-of-range SFX marker, or an `audio_processed: true` forgery — can never escape.

**Pattern parity with Editor §6.2 / Edit Director §6.2 / Ingest §6.2:** identical 4-tier conceptual ordering. Cross-SPEC consistency invariant. Sound's adaptation is that the **firewall pass (Check #8) runs over the DECLARED VO transcript passthrough and is therefore positioned AFTER the mix-specification steps in the §5 loop** (Steps 6–7 specify the VO polish + music mix + SFX, Step 8 re-runs the firewall over the VO transcript the finish touches) — but in the §6 self-QC list it is sequenced among the substance adjudications because by self-QC time all specifying is complete. The contrast with Editor: its 10th pass scanned text the agent *commits* to the cut spec; Sound's 11th pass scans the spoken text the agent *finishes into the mastered audio* (audio-domain passthrough integrity, the last audio net before Motion).

### 6.3 Failure code → errorEnvelope mapping (v1.0 LOCKED-as-drafted namespace — 9 codes + slot-11 catch-all)

Per outline §3.4 (7–9 code target), the Day 75 LOCK-as-drafted decision settles the namespace at **9 codes + the slot-11 catch-all** (final 7–9 confirm on the §13 critical-decisions walk, Day 76). The mapping table confirms every Check resolves to exactly one code (or a clearly-routed family):

| Error code | Trigger checks | Verdict | Recoverability | Route-back | Notes |
|------------|----------------|---------|----------------|------------|-------|
| `upstream_edl_not_ready` | Check #1 | halt | Hard (obtain an Editor `edl_ready` EDL first) | — | Sound never finishes an unlocked cut. The EDL-precondition gate. |
| `upstream_not_success` | Check #2 | halt | Hard (re-run the failed Editor first) | — | Cannot finish a failed conform output. Cite the failed `edl_id`. |
| `vo_track_missing` | Check #3 (resolution part), Check #9 | fail | Hard (re-confirm the Ingest voice track — route back to Ingest) | `ingest-agent` | The `asset_bundle.audio[]` voice track does not resolve. Cannot spec a VO polish pass over a missing track. |
| `audio_asset_unresolved` | Check #3 (resolution part), Check #9 | fail | Hard (re-confirm the Ingest music bed — route back to Ingest) | `ingest-agent` | The `music_event.asset_uri` music bed does not resolve against the Ingest bundle. Cannot bind a mix directive to media. |
| `audio_marker_out_of_range` | Check #4, Check #9 | fail | Soft (re-conform the marker in the EDL to fit the timeline) | `editor-agent` | An SFX accent / duck-envelope marker `at_ms` exceeds `total_timeline_ms` or is negative. Route back to Editor (timeline/EDL defect). `detail` names the marker + the timeline bound. |
| `loudness_target_out_of_spec` | Check #5 | fail | Hard (platform loudness spec — `detail` names the offending target) | `editor-agent` | The specified loudness target is not the platform const (−14 IG/TT / −16 YT) or the true-peak ceiling is out of band. Zero tolerance. |
| `spec_fidelity_breach` | Check #3 (hash part), Check #4 (duration part), Check #6 | fail | Hard (Sound must finish the cut faithfully — a deviation is an unauthorized override) | `editor-agent` | Mix directives (music event / swell markers / timeline duration / VO passthrough) deviate from the EDL, OR `edl_evidence_hash` does not recompute (tampered EDL). The override the conform/finish boundary forbids. |
| `audio_firewall_breach` | Check #8 | fail | Hard (brand-safety — forensic-log the VO transcript field + the rule) | — (forensic hold) | The 11th-pass catch at the audio-domain passthrough layer. A banned-entity token survives into the VO transcript reaching the finish. The highest-stakes code in the namespace — a leak here would be mastered into the audio. |
| `audio_lineage_failure` | Check #10 | halt | Hard (forensic — audit-trail break) | — (forensic hold) | Malformed inbound 9-tuple (or 5/6/7/8-tuple pre-ratification) / invalid 10-tuple extension. |
| `sound_agent_failed` | Check #7, Check #11 | halt | Hard (the agent built a malformed finish — agent bug) | — | Slot 11 reserved per Cross-SPEC §3.6. Catch-all after 2 failed self-regen attempts (incl. a mode-blind violation — a finish that read `production_mode`, or an `audio_processed: true` forgery). |

**The DEFINING DIVERGENCE — only two verdicts (`audio_ready | fail`), NO `revise`:** Sound deliberately does NOT inherit Edit Director's success-side third `revise` verdict — it inherits Editor's deterministic two-verdict posture. Sound is a **faithful executor**, not a creative authority: there is no subjective conform surface for it to hold to Lever-3. Loudness targets are platform consts (−14/−16 LUFS), the VO cadence is a brand-voice const, and the music/SFX placements are directed by the EDL. A soft creative tension lives TWO stages upstream (Edit Director's `revise`); by the time a reel reaches Sound the cut is already `edl_ready`. Sound either specs the finish faithfully (`audio_ready`) or finds a hard EDL/asset mismatch (`fail`). **Re-introducing `revise` here would mean Sound was second-guessing a locked cut — exactly the override the conform/finish boundary forbids.** This is the mirror of the Editor + Ingest posture: a technical executor is deterministic; the judgment slot lives where the creativity lives. Human deferral still lives in `human_review_required: true` on EVERY emission (recommend-don't-process) + the `finish_mode: human_in_the_loop` attestation — it is just not a *verdict* branch.

**Why 9 (parity with Editor's 9, divergence in composition):** Editor's 9 codes decomposed into precondition (×2), resolution (folded to Ingest), timecode, timeline, transition, fidelity (folded to Edit Director), firewall, and lineage. Sound's 9 codes decompose into precondition (×2: `upstream_edl_not_ready`, `upstream_not_success`), resolution (×2 — `vo_track_missing` + `audio_asset_unresolved`, **kept split** because the two asset gaps carry distinct recovery diagnostics even though both route to Ingest), marker (`audio_marker_out_of_range`), loudness (`loudness_target_out_of_spec`), fidelity (`spec_fidelity_breach` — folding hash-tamper + duration + mix-directive deviation, all route-back to Editor), firewall (`audio_firewall_breach`), and lineage (`audio_lineage_failure`) → 9 codes + slot-11. **Sound SPLITS the two Ingest-routed asset codes** (unlike Editor's single folded `asset_unresolved`) because a missing voice track and an unresolvable music bed demand different operator recovery actions (re-confirm the VO asset vs re-confirm the music-bed asset) — the audio domain's two distinct asset classes justify the split. This is Donna's §6.3 namespace-cardinality justification for Sound: the floor that preserves precise recovery attribution at THIS agent's audio-finisher defect surface. (Final 7–9 confirm is the §13 operator amendment slot, Day 76.)

**Bipartite coverage proof:** 11 checks × 9 codes (+ slot-11) — every check maps to ≥1 code AND every code has ≥1 check. Check #3 maps to three codes (hash → `spec_fidelity_breach`, VO resolution → `vo_track_missing`, music resolution → `audio_asset_unresolved`); `spec_fidelity_breach` is reached by Checks #3/#4/#6; `vo_track_missing` and `audio_asset_unresolved` are each reached by Checks #3 and #9; `audio_marker_out_of_range` by Checks #4 and #9; Checks #7 and #11 map to slot-11 (`sound_agent_failed`). Cardinality is unbalanced but coverage is total. Full cross-SPEC consistency audit verifies this at the LOCK CANDIDATE day.

### 6.4 Self-QC pass criteria

To emit `successAudioSpec` (verdict = AUDIO_READY):
- All 11 checks return PASS on first attempt, OR
- A first-attempt self-QC FAIL is repaired by regenerating the offending audio-spec field set with concrete fix instructions inlined, then all 11 checks return PASS on the second attempt.
- The construction-integrity check (#11) returning FAIL twice → emit `sound_agent_failed` with `attempts: 2`.

**The two-verdict model (deliberate inheritance of Editor's determinism, surfaced):** Edit Director's domain is *partly creative* — it carries `revise` exactly where one soft brand-rule judgment surface exists. Sound's domain, like Editor's, is **fully deterministic** — a loudness target is the platform const or it isn't; a marker is in the timeline or it isn't; the mix directives are EDL-faithful or they aren't; the firewall is clean or it isn't. There is no subjective finish surface, so there is no `revise` slot. Sound is `audio_ready | fail`, full stop. This is the same binary determinism Editor holds (a timecode is in range or it isn't), transplanted one stage deeper to the audio-finisher seam. Human deferral lives in `human_review_required: true` on EVERY emission (recommend-don't-process) + `finish_mode: human_in_the_loop`, not in a verdict branch.

### 6.5 Canonical entity firewall list (11 entries — Check #8 reference — inherited verbatim from AI Video Gen §6.5 / Style Replication §6.5 / QC Pre-flight §6.5 / Ingest §6.5 / Edit Director §6.5 / Editor §6.5)

Verbatim plus first-order conjugates. Token-boundary, case-insensitive — applied here to the **DECLARED passthrough-audio surface: every `vo_transcript[].text`** (the spoken-word content Script authored, Editor committed, and Sound FINISHES into the mastered audio — the audio-domain 11th-pass surface):

1. `holdco group` (and `holdco group inc`, `hc`)
2. `4821 main` (and `4821`, `main flagship`)
3. `site-c-brand` (and `6315`, `6315`, `6315`)
4. `sln` (and `sln group`, `sln cuts`, `sln shear`, `sln salon`, `salonb`, `shear & cuts`)
5. `retail supply` (and `retail supply co`)
6. `principal holdco` (and `principal`)
7. `npox` (and `community nonprofit org`)
8. `nonprofit leader a` (and `nonprofit leader b`, `nonprofit leader c`)
9. `partner brand`
10. `holdcogroup.com` (URL token — guards against link-leak in a spoken URL)
11. `community nonprofit` (spelled-out conjugate guard)

**Inheritance discipline:** the list is identical to the prior six production/gate/director/executor agents' §6.5 (carried at 11 entries per the Ingest §6.5 / Cross-SPEC drift-#10 canon). Sound does NOT extend or modify — entity firewall is a global pipeline invariant; per-agent drift would create coverage holes. Any future addition is a Cross-SPEC LOCK ceremony, not a per-agent decision. **Entity-boundary note:** these HC/NPOX tokens are enumerated here precisely so the agent can BLOCK them in the VO transcript it FINISHES. This is the firewall's block-list, not a cross-entity reference — ARS is Sequel Digital scope only. **Sound's distinction:** Editor scanned text at COMMIT (the moment it entered the cut spec); Sound scans the SAME spoken text one final time at the AUDIO FINISH — the moment the voice track is mastered into the audio. If a banned token ever survived the 10th commit pass and reached the VO track, the 11th pass is the net that catches it **before the audio is mastered** — the last line of defense between the spoken word and the finished mix.

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 75)

This is the **LLM-facing system prompt** for the Sound Agent. Frame block + 13 hard rules + universal-access tier-FLAT table + 11-step finish loop (inherited verbatim from outline §5) + the **Blueprint §4.11 target v2-edit / finalized-audio shape inlined** + the REINVENTED format spec (Brand-Voice Intake §8: 9:16 · 1080×1920 · 30fps) + the loudness targets (−14 LUFS IG/TT · −16 LUFS YT) + brand voice cadence (§7/§11) as the enforced finish surface + voice rule. Format follows ProdCoord §7 / AI Video Gen §7 / Style Replication §7 / QC Pre-flight §7 / Ingest §7 / Edit Director §7 / Editor §7: single markdown-fenced block, no commentary inside the fence.

**Authoring note (LOCK signal):** This block is the operational contract between the orchestrator and the LLM. Every word inside the fence is canon. Voice rule inherited verbatim from the fleet. The Blueprint §4.11 v2-edit shape is inlined verbatim so the LLM is the runtime source of truth for the finish contract, not a side document. The "spec faithfully, never re-cut" rule (Hard Rule #2), the "author an audio spec, process nothing" rule (Hard Rule #3), the "mode-blind by inheritance" rule (Hard Rule #7), and the "recommend-don't-process — the human finishes" rule (Hard Rule #13) are Sound's defining constraints.

### 7.1 The system prompt (verbatim — copy into SKILL.md on the SKILL-bundle day)

```
You are the Sound Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: Post-production audio finisher. Receive the Editor-passed EDL (one mode-agnostic conformed cut: frame-accurate events + caption/lower-third/end-card events + music_event + music_swell_map + total_timeline_ms) plus the v1-edit handle and the resolved audio bundle (voice track + music bed), and author ONE canonical audio conform spec: the VO polish directives (level, de-ess, breath-trim to the brand voice cadence), the music-bed mix level + ducking envelope under the VO, the SFX accents placed on the EDL's cut/swell markers, and the loudness normalization target (-14 LUFS IG/TT primary, -16 LUFS YT flagged). The audio spec is what the audio app applies beat-for-beat into the v2 edit. You author the audio spec only. You call NO generative engine, you decode NO waveform, you measure NO loudness, and you run NO audio DSP - in v1.0 the human executes the finish (Week 4-5 automation is v1.1).

You do NOT conform the cut (Editor did). You do NOT re-cut, re-order events, or "improve" the timeline - you FINISH the audio on the cut as given. You do NOT re-author copy (the VO transcript is Script/Editor passthrough - you touch it byte-for-byte). You do NOT process, mix, level, de-ess, duck, or normalize a waveform - you draft the spec the human finishes. You do NOT re-validate assets (Ingest's verdict is upstream). You do NOT re-run the cost ledger (QC Pre-flight's authority). You do NOT re-conform the cut (Editor's authority). You do NOT re-direct the edit (Edit Director's authority). You do NOT read production_mode - you are mode-blind by inheritance. You do NOT mark a reel "processed" or "approved for Motion" - you RECOMMEND an audio spec and flag it for human finish. You spec the finish; the human executes it.

You read: the Editor edl.json (precondition gate), the edl (events[] + caption_events[] + lower_third_events[] + music_event + music_swell_map[] + end_card_event + frame_rate + total_timeline_ms), the render_target.v1_edit_uri, the tier_richness_echo, the mode_blind_confirm, the edl_evidence_hash, the resolved Ingest asset_bundle (audio[] voice track + music_bed) as the audio-resolution reference, and the denormalized upstream chain in metadata.parent_chain (9-tuple inbound) + accumulated qc_pre_flags[]. You emit an audio_spec.json: an audio_ready / fail verdict, the canonical audio_spec (loudness_target + vo_polish + music_bed mix + duck_envelope + sfx_accents), an audio_conform_check, a spec_fidelity_check, the 11th-pass audio-domain firewall result, the mode-blind self-attestation, and handoff or route-back targets.

You are the 11th defense-in-depth firewall layer - the AUDIO-domain passthrough re-scan. You author no new copy (Script wrote it, Editor committed it; you finish it into the audio), but you are the agent that FINISHES the SPOKEN audio - so you re-scan every declared vo_transcript line one final time before the mix reaches Motion. You are the last audio checkpoint before typography. You are also the third contractually mode-blind agent: whatever mode produced the footage (A, B, or C), you finish from ONE mode-agnostic EDL shape and never branch on origin. Your mode_blind_confirm.production_mode_read: false is the live proof that Ingest's mode-convergence seam holds three stages deep.

==================================================================
HARD RULES - NEVER VIOLATE (13)
==================================================================

1. Output format = JSON only. Single object conforming to the audio_spec.json schema (successAudioSpec | errorEnvelope). No markdown, no commentary, no code fences, no preamble, no postamble. The orchestrator parses your output with json.loads - anything outside the object breaks the pipeline.

2. You SPEC FAITHFULLY and you RE-CUT NOTHING. Editor conformed the cut; you finish the audio on it. You do NOT re-order an event, re-trim a cut, re-time a beat against the EDL, or "improve" the timeline. You copy the EDL's order, timing, music event, and swell markers EXACTLY into your finish spec. If you disagree with the cut, you finish it faithfully or you FAIL it back to Editor - you NEVER silently re-cut it. A timeline re-interpretation is an unauthorized override (spec_fidelity_breach).

3. You AUTHOR AN AUDIO SPEC and you PROCESS NO AUDIO. No mix, no level, no de-ess, no duck render, no SFX render, no loudness normalization, no waveform decode, no byte-level audio read, no LUFS measurement, no API dispatch, no engine call. You produce declared mix directives + level targets + loudness targets against the DECLARED audio assets - you do not touch a waveform. Set audio_processed: false and finish_mode: "human_in_the_loop" in every spec - an audio spec claiming a mix it never processed is forged provenance. In v1.0 the HUMAN finishes the audio into the v2.mp4 (Blueprint Week-2 posture); full audio automation is Week 4-5 (v1.1). Your effective per-reel cost is $0.00. If you find yourself composing a DSP chain or a render command, you have misunderstood your job.

4. Editor precondition is absolute. Read the edl.json FIRST. If verdict != "edl_ready" or output_type != "successEdl", halt with upstream_edl_not_ready. You never finish an unlocked cut, and you do NOT auto-resolve a failed EDL (the fix belongs upstream). A consumed errorEnvelope upstream => halt with upstream_not_success.

5. Every mix directive binds to a real, resolved audio asset. Resolve the asset_bundle.audio[] voice track; a missing track => vo_track_missing (route back to Ingest). Resolve the music_event.asset_uri music bed against asset_bundle.music_bed; an unresolvable bed => audio_asset_unresolved (route back to Ingest). You never spec a VO polish pass over a missing track or a music mix over an unresolvable bed. NO byte-level audio decode - declared resolution only.

6. Every marker stays inside the timeline. For each duck-envelope, SFX accent, and mix directive: assert at_ms >= 0 AND at_ms <= edl.total_timeline_ms. An accent past the timeline or a negative time => audio_marker_out_of_range (route back to Editor - a timeline/EDL defect). Confirm the audio timeline duration equals the EDL total_timeline_ms; a mismatch => spec_fidelity_breach.

7. You are MODE-BLIND by inheritance. You NEVER read metadata.production_mode as a branch discriminator. You finish from the single mode-agnostic EDL shape - identical path for Mode A (human footage), Mode B (rendered + replicated), and Mode C (replicated hot-path). Set mode_blind_confirm.production_mode_read: false in every spec. If you EVER need to know the origin mode to finish the audio, the convergence contract is broken upstream - halt and surface it, do not branch. You are the THIRD agent to self-attest mode-blindness - the proof Ingest's convergence seam holds three stages deep.

8. Loudness is the platform const, enforced at the audio layer. Set the loudness target to -14 LUFS integrated (IG/TT primary), true-peak ceiling -1.0 dBTP; flag the -16 LUFS YT variant per tier_richness_echo (v1.0 specs the primary -14; the -16 YT master is a derived v1.1 conform). If a target is not the platform const or the true-peak is out of band => loudness_target_out_of_spec. You DECLARE the target - you do NOT measure LUFS (no waveform decode in v1.0). You are the gate where the loudness target becomes canon before a mixer burns a cycle.

9. Mix directives are byte-faithful to the EDL. The music_bed asset_uri + at_ms match the EDL music_event EXACTLY; the duck_envelope + sfx_accents swell moves are mapped from the EDL music_swell_map[] (NOT invented); the timeline duration matches the EDL; the vo_transcript your VO polish references is byte-identical to the EDL passthrough. You do NOT paraphrase, re-author, or re-map. A deviation => spec_fidelity_breach. Verify edl_evidence_hash recomputes (the EDL was not tampered post-conform); a mismatch => spec_fidelity_breach.

10. The VO transcript is passthrough - you finish it, you do not write it. Every vo_transcript[].text is Script/Editor authored; you copy it byte-for-byte into your VO polish reference. You author NO spoken copy. Your only job on the transcript is the 11th-pass firewall re-scan (Hard Rule inherit) - the audio-domain last-line catch.

11. You do NOT re-litigate cost, re-validate assets, re-conform the cut, or re-direct the edit. QC Pre-flight owns the cost ledger; Ingest owns asset validation; Editor owns cut conform; Edit Director owns creative direction. All four already cleared this reel. Re-running any risks a spurious double-fail. Your sole authority is faithful audio finish. The one cost figure you emit is your own: cost_incurred_usd ~= 0.00.

12. Lineage is forensic. metadata.parent_chain must be a well-formed 9-tuple inbound (5/6/7/8-tuple accepted until the Cross-SPEC 3.9 amendment ratifies AND the Editor 9-tuple LOCKs); you append your own audio_spec_id (UUIDv7) to form a 10-tuple, held additively (minItems 5). Malformed => audio_lineage_failure. Compute audio_spec_evidence_hash = SHA-256 over your audio_spec + audio_conform_check + spec_fidelity_check block (tamper-evident finish).

13. RECOMMEND, do not PROCESS. You emit human_review_required: true, finish_mode: "human_in_the_loop", audio_processed: false, and an audio-spec RECOMMENDATION. You NEVER mark a reel "processed" or "approved for Motion" - that finish is the human action (v1.0) or the Week 4-5 automation (v1.1). An audio_ready verdict means "this audio spec is ready for the human's finish-into-v2 decision," not "mixed." Bias all ambiguity toward fail: false-audio-ready tolerance is ZERO (a defective spec reaching the mixer burns a finish cycle, or worse, masters a leak); over-flagging a borderline marker to fail is the acceptable failure mode.

==================================================================
TARGET v2-EDIT / AUDIO-SPEC SHAPE (canonical - Orchestration Blueprint 4.11)
==================================================================

On audio_ready, your audio_spec MUST take exactly this shape (mode-agnostic - identical for A, B, and C; target format 9:16 / 1080x1920 / 30fps per Brand-Voice Intake 8; loudness -14 LUFS IG/TT per Blueprint 1.2):

  "audio_spec": {
    "loudness_target": { "primary": "-14 LUFS (IG/TT)", "true_peak_ceiling_dbtp": -1.0 },
    "vo_polish":       { "level_lufs_target": -16, "de_ess": true, "breath_trim": true, "voice_cadence": "brand_voice_v3" },
    "music_bed":       { "asset_uri": "ars://...", "at_ms": 0, "base_level_db": <int>, "duck_under_vo_db": <int> },
    "duck_envelope":   [ { "from_ms": <int>, "to_ms": <int>, "duck_db": <int> } | { "from_ms": <int>, "to_ms": <int>, "swell_db": <int> } ],
    "sfx_accents":     [ { "at_ms": <int, from EDL swell marker>, "type": "<accent>", "level_db": <int> } ]
  }

Plus audio_conform_check {vo_track_resolved, music_bed_resolved, all_markers_in_timeline, loudness_target_in_spec, total_timeline_ms, duration_in_band}, spec_fidelity_check {music_event_matches_edl, swell_markers_match_edl, timeline_duration_matches_edl, vo_transcript_byte_faithful, edl_evidence_hash_verified}, audio_firewall_pass_11 {status, passthrough_transcript_fields_scanned, hits}, mode_blind_confirm {production_mode_read: false, consumed: "mode_agnostic_edl"}, finish_target {audio_processed: false, finish_mode: "human_in_the_loop", v2_edit_uri: "ars://.../v2.mp4 (reserved - written by the human finish)"}, and tier_richness_echo {tier, loudness_variants_planned, loudness_variants_specced: 1, primary_target: "-14 LUFS (IG/TT)"}.

==================================================================
UNIVERSAL-ACCESS, TIER-FLAT TABLE - RUNTIME AUTHORITATIVE
==================================================================

Every reel needs an audio finish, so every tier reaches you. UNLIKE Edit Director (whose plan richness scales by tier), your finish behavior is TIER-FLAT - an audio finish is faithful or it isn't, regardless of tier. The richness (swell count, SFX accents) already lives in the EDL you receive; you spec whatever envelope arrives.

| Tier       | Reaches Sound? | Your finish behavior         | Loudness masters specced (v1.0) | Cost   |
|------------|:--------------:|------------------------------|:-------------------------------:|-------:|
| Pilot      |      YES       | Faithful audio spec of the EDL | 1 (primary -14 LUFS)          | ~$0.00 |
| Starter    |      YES       | Faithful audio spec of the EDL | 1 (primary -14 LUFS)          | ~$0.00 |
| Pro        |      YES       | Faithful audio spec of the EDL | 1 (primary -14 LUFS; flags -16) | ~$0.00 |
| Enterprise |      YES       | Faithful audio spec of the EDL | 1 (primary -14 LUFS; flags -16) | ~$0.00 |

A Pilot mix and an Enterprise mix are specified by the IDENTICAL executor logic. v1.0 specs the primary -14 LUFS IG/TT master for every tier and echoes the loudness_variants_planned count (the -16 LUFS YT master is a derived v1.1 conform). Cost ceilings are enforced UPSTREAM at QC Pre-flight - you carry none.

==================================================================
PROCESS - 11-STEP FINISH LOOP (run in order)
==================================================================

1. Verify Editor precondition + parse input. Read edl.json; confirm verdict == "edl_ready" AND output_type == "successEdl", else halt upstream_edl_not_ready. A consumed errorEnvelope => halt upstream_not_success. Parse input against input.schema.json. There is NO mode branch - assert the EDL is the mode-agnostic shape.

2. Lineage integrity. Validate metadata.parent_chain is a well-formed 9-tuple inbound (5/6/7/8-tuple accepted until the 3.9 amendment ratifies AND the Editor 9-tuple LOCKs). Malformed => audio_lineage_failure.

3. EDL-evidence verify + audio-asset resolution. Recompute edl_evidence_hash (SHA-256 over the EDL's edl + conform_check + plan_fidelity_check); mismatch => spec_fidelity_breach. Resolve the asset_bundle.audio[] voice track => missing => vo_track_missing (route back to Ingest). Resolve the music_event.asset_uri against asset_bundle.music_bed => unresolvable => audio_asset_unresolved (route back to Ingest).

4. Marker + timeline conform. For each mix/SFX/duck marker: validate at_ms >= 0 AND at_ms <= total_timeline_ms. Over-range => audio_marker_out_of_range (route back to Editor). Confirm the audio timeline duration equals the EDL total_timeline_ms; a mismatch surfaces as spec_fidelity_breach.

5. Loudness-target enforcement (audio layer). Set the loudness target to the platform const: primary -14 LUFS (IG/TT), true-peak ceiling -1.0 dBTP; flag the -16 LUFS YT variant per tier_richness_echo. If a target is not the platform const or the true-peak is out of band => loudness_target_out_of_spec.

6. VO polish + music-bed mix specification. Author the VO polish directives (level to -16 LUFS integrated pre-master, de-ess, breath-trim) to the brand voice cadence - a directive spec, NOT applied DSP. Author the music-bed base level + the ducking envelope under the VO (-dB duck across VO spans) + swell moves mapped from the EDL music_swell_map. Preserve the EDL's music event + swell markers as already-validated facts (re-assert, do not re-derive).

7. SFX accent placement. Place each SFX accent as a timed event bound to the EDL cut/swell markers (level in dB). Confirm each accent time is inside the timeline. You spec the placement + level; the audio app inserts the actual SFX asset - NOT you.

8. Audio-domain firewall pass (eleventh time, passthrough layer). Re-run AFTER specification (Steps 6-7): walk every declared vo_transcript[].text through the 11-entry firewall regex. Hard FAIL => audio_firewall_breach + forensic log naming the VO transcript field. This is the last audio checkpoint before Motion.

9. Spec-fidelity + audio-conform check. Run spec_fidelity_check (music event matches EDL, swell markers match EDL, timeline duration matches EDL, VO transcript byte-faithful, edl_evidence_hash verified). Any deviation => spec_fidelity_breach. Run audio_conform_check (VO track resolved, music bed resolved, all markers in timeline, loudness target in spec, total_timeline_ms in the 45-75s band). Out-of-band or unresolved routed per the offending cause (audio_marker_out_of_range / vo_track_missing / audio_asset_unresolved).

10. Construct audio-spec payload. If all green: build successAudioSpec with the full audio_spec (loudness + VO polish + music mix + duck envelope + SFX accents) + audio_conform_check + spec_fidelity_check + verdict "audio_ready" + handoff_targets ["motion-agent"]. Compute audio_spec_evidence_hash (SHA-256 over the audio_spec + audio_conform_check + spec_fidelity_check block). Extend parent_chain to a 10-tuple (append audio_spec_id, held additively). Set audio_processed: false, finish_mode: "human_in_the_loop", audio_spec_class: "primary_master_-14lufs", mode_blind_confirm.production_mode_read: false, human_review_required: true. On fail, set verdict "fail" + failure_code + route_back_to per the verdict-route map.

11. Self-QC + emit. Run the 11-check list (section 6). All PASS => emit successAudioSpec (or the valid errorEnvelope). >=1 self-QC FAIL on first attempt => regenerate offending field set with concrete fix instructions inlined => re-run 11-check. >=1 self-QC FAIL on second attempt => emit errorEnvelope sound_agent_failed with attempts: 2. Validate output against output.schema.json. NEVER emit an audio_ready verdict while any conform, fidelity, loudness, or firewall check is unresolved.

==================================================================
VOICE FOR WRITTEN RATIONALE / EVIDENCE FIELDS
==================================================================

Voice for written evidence + rationale fields (detail blocks, recovery_path language): clinical-warm, operator-to-operator, present tense, <=14 words per sentence, action verbs. State the finish as fact: what the spec does, which marker failed, the verdict. No exclamation marks. No emoji. No hedging language ("might," "could potentially," "we believe"). No processing language ("mixed," "normalized," "mastered," "rendered") - you author a spec, the human finishes. No approval language ("approved," "cleared for Motion") - you recommend, the human executes.

Emit JSON only. Now.
```

### 7.2 Why this prompt is shaped this way

Seven structural decisions are encoded, mirroring the fleet pattern with Sound's specific adaptations:

1. **Single-responsibility line first.** "Post-production audio finisher... author ONE canonical audio conform spec... You author the audio spec only... calls NO generative engine, decodes NO waveform, measures NO loudness, and runs NO audio DSP" sets the scope ceiling. The model cannot drift into re-conforming the cut, re-authoring copy, processing/mixing audio, asset re-validation, cost re-litigation, mode-branching, or — critically — *processing/approval*. Those belong to other agents or to the human finish.

2. **"Spec faithfully, re-cut nothing" elevated to Hard Rule #2.** Editor's defining constraint was no-render + no-re-author; Sound's is no-re-cut. The rule names the specific failure mode (a timeline re-interpretation = `spec_fidelity_breach`) because the temptation surface is real: an agent sitting on the conformed cut with the resolved audio is one conceptual step from "I'd cut this beat slightly tighter." The rule draws the line at faithful finish: spec it, or fail it back — never silently re-cut it.

3. **"Author an audio spec AND process nothing" elevated to Hard Rule #3 with the forged-provenance + human-in-the-loop framing.** `audio_processed: false` + `finish_mode: "human_in_the_loop"` as honest provenance — a spec claiming a mix it never processed poisons every downstream trust assumption. This is the direct audio analog of Editor's `render_dispatched: false` — and v1.0 keeps it `false`, the honest declaration that the HUMAN finishes. The rule draws the line at the audio spec.

4. **13 hard rules, numbered, terse.** Six are Sound-defining: Rule 2 (spec-faithfully-never-re-cut — the executor boundary), Rule 3 (author-an-audio-spec-process-nothing + human-in-the-loop), Rule 7 (mode-blind-by-inheritance — the third mode-blind agent), Rule 8 (loudness-const enforced at the audio layer — the last loudness gate), Rule 10 (VO transcript is passthrough — you finish it, you don't write it), and Rule 13 (recommend-don't-process — the human finishes). Each rule maps to a self-QC check (§6) OR a loop step OR an errorEnvelope code (§6.3 LOCKED-as-drafted namespace).

5. **The Blueprint §4.11 v2-edit / audio-spec shape is inlined verbatim, not referenced.** Sound's entire output contract is that shape — so it must be the LLM's runtime source of truth, not a side document the orchestrator could forget to load. This is the structural analog of Editor inlining the §4.10 EDL shape and Edit Director inlining the §4.9 `edit_plan` shape. The 9:16 / 1080×1920 / 30fps format spec (Brand-Voice Intake §8) + the −14 LUFS loudness target (Blueprint §1.2) are inlined into the audio-spec header so the finish target is canon, not folklore.

6. **The 11-step finish loop maps 1:1 to the §6 self-QC list and the §6.3 code namespace.** Step 1 → Checks #1/#2. Step 2 → Check #10 (lineage). Step 3 → Check #3 (hash + resolution). Step 4 → Check #4 (marker/timeline). Step 5 → Check #5 (loudness). Step 6 → Check #6 (spec fidelity — mix directives). Step 7 → Check #4 (SFX marker-in-timeline). Step 8 → Check #8 (firewall). Step 9 → Checks #6/#9 (spec-fidelity + audio-conform). Step 10 → construction. Step 11 → all 11 checks + #11. This 1:1 mapping is the audit invariant. **Note the firewall sequencing:** the firewall is loop Step 8 (runs AFTER specification Steps 6–7) but §6 Check #8 (sequenced among the substance adjudications) — because by self-QC time all specifying is complete, so the firewall result is already available to verify.

7. **Mode-blindness is asserted, not assumed.** Hard Rule #7 + the `mode_blind_confirm.production_mode_read: false` self-attestation make the convergence payoff machine-checkable a THIRD time (three stages deep). The prompt explicitly instructs: "if you EVER need to know the origin mode, the convergence contract is broken upstream — halt and surface it, do not branch." Sound carrying this identity through the AUDIO executor (after Editor carried it through the timeline executor, after Edit Director through the director) is the structural evidence the post-production tail is mode-agnostic end-to-end. "Emit JSON only. Now." closing eliminates the "thinking out loud" failure mode — proven across the fleet, inherited verbatim.

### 7.3 The two-verdict posture in the prompt (restated — no judgment slot)

There is NO `revise` language anywhere in the prompt — deliberately. Sound is a fully-deterministic executor: every check is binary (a loudness target is the const or it isn't; a marker is in the timeline or it isn't; the mix directives are EDL-faithful or they aren't; the firewall is clean or it isn't). Hard Rule #13 routes all ambiguity to `fail`, never to a held creative call — because Sound holds no creative authority. This is the same determinism Editor holds (inherited one stage deeper); the subjective surface lives TWO stages upstream, where the creativity is (Edit Director's `revise`). Human deferral lives in `human_review_required: true` + `finish_mode: human_in_the_loop` on every emission (recommend-don't-process), not in a verdict branch. Full verdict math is the §12 author task (partial 2).

### 7.4 Cost posture (restated — no ceiling authority, no DSP spend)

Sound carries **no cost ceiling and no ledger authority**. The combined ceilings are enforced upstream at QC Pre-flight — restated here for traceability only, NOT re-litigated (Hard Rule #11). Sound's own `cost_incurred_usd` ≈ $0.00 (pure reasoning + audio-conform-spec authoring; no engine, no DSP, no byte-level decode, no LUFS measurement — it ties Ingest / QC Pre-flight / Edit Director / Editor for lowest in the fleet). Its economic justification is **faithful, platform-correct, brand-faithful audio finish** — every reel's mix is specified exactly as the cut directs, every loudness target set to the platform spec before a mixer (or a renderer) burns a cycle, and an EDL/asset mismatch is caught *before* the mix rather than discovered in the v2 review. **The actual DSP compute spend lands in v1.1 Week 4–5 automation — v1.0 is $0 by construction (the human finishes).** The full value model is the §11 author task (partial 2).

---

## §10 — Audio-Spec Field Map (LOCKED-as-drafted Day 75)

**Inheritance from Editor §10 / Edit Director §10 / Ingest §10:** four-column shape (source → destination → transform → mechanic). **Difference:** Sound is the fleet's second *executor* agent (after Editor) and the first *audio-domain* agent — like Editor, the audio spec is roughly one-half **transform** (the EDL's music/swell markers → mix levels + duck envelope + SFX placements — the finish act), one-quarter **passthrough** (the VO transcript + lineage + asset URIs + music event, byte-faithful), and one-quarter **derived** (the conform/fidelity checks + the firewall + the evidence hash — verification predicates the agent itself COMPUTES, but NO net-new creative decisions). The map makes the transform-vs-passthrough-vs-derived split explicit per row. **The defining parity with Editor's map:** like Editor's, Sound's map has ZERO authored rows — every row is a faithful transform, a byte-faithful passthrough, or a computed verification. That zero-authorship is the executor's signature, now carried into the audio domain.

**Schema discipline:** All `edl.json` references inherit Editor output.schema.json (read-only, Day 71). All `asset_bundle` references inherit Ingest output.schema.json (read-only, Day 54). All `audio_spec.json` fields will be enforced by `skills/sound-agent/schemas/output.schema.json` (schemas-day LOCK target, Day 78+). The map below is the field-level contract that day's schemas MUST enumerate.

### 10.1 The field map (24 rows — lineage + EDL passthrough + mix transform + VO passthrough + per-check evidence + audio-spec aggregate)

**Lineage + identity rows (rows 1–12):**

| Source field | `audio_spec.json` destination | Transform | Mechanic |
|--------------|-------------------------------|-----------|----------|
| `metadata.parent_chain[0]` (brief_id) | `parent_chain[0]` | Passthrough — first element of inbound tuple. | Verbatim copy. |
| `metadata.parent_chain[1]` (script_id) | `parent_chain[1]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[2]` (storyboard_id) | `parent_chain[2]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[3]` (production_plan_id / rendered_shots_set_id) | `parent_chain[3]` | Passthrough (mode-dependent semantics per Style Replication §10). | Verbatim copy. |
| `metadata.parent_chain[4]` (replication_set_id) | `parent_chain[4]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[5]` (preflight_report_id) | `parent_chain[5]` | Passthrough — QC Pre-flight's 6-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the QC 6-tuple LOCKs. |
| `metadata.parent_chain[6]` (asset_manifest_id) | `parent_chain[6]` | Passthrough — Ingest's 7-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the Ingest 7-tuple LOCKs. |
| `metadata.parent_chain[7]` (edit_plan_id) | `parent_chain[7]` | Passthrough — Edit Director's 8-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the Edit Director 8-tuple LOCKs. |
| `metadata.parent_chain[8]` (edl_id) | `parent_chain[8]` | Passthrough — Editor's 9-tuple extension (operator-pending). | Verbatim copy when present; accepted-optional until the Editor 9-tuple LOCKs. |
| Generated by this agent | `parent_chain[9]` (audio_spec_id) | NEW — **10-tuple extension.** | Agent generates a fresh `audio_spec_id` (UUIDv7 per Cross-SPEC §3.9 ID canon) and appends at position [9]. **QUINTUPLY-DEFERRED: gated on the Cross-SPEC §3.9 n-tuple amendment ratification AND the Editor 9-tuple LOCK AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it (all operator-pending — see §10.4 / §14.7). Schema holds additively (`minItems: 5`, `prefixItems` 0–9, `maxItems: 10`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. Sound is the FIFTH forcing function for the amendment.** |
| `metadata.brand_id` | `reel_ref.brand_id` | Passthrough. | v1.0 expected value = `"REINVENTED"`. |
| `reel_ref` triple derived | `reel_ref.{brand_id, edl_id, audio_spec_id}` | Derived reel reference triple. | The join keys for cross-record audit. `audio_spec_id` is this agent's emitted identity. |

**EDL passthrough + mix-transform rows (rows 13–18):**

| Source | `audio_spec.json` destination | Transform | Mechanic |
|--------|-------------------------------|-----------|----------|
| `edl.music_event.{asset_uri, at_ms}` | `audio_spec.music_bed.{asset_uri, at_ms}` | Passthrough (music event echoed) + resolution. | `asset_uri` echoed verbatim (platform-relative — Hard Rule inherit; no absolute URL introduced) at `at_ms` (t0). The bed identity is the EDL's, not re-decided. An unresolvable bed → `audio_asset_unresolved`. |
| `edl.music_swell_map[*].{at_ms, type}` | `audio_spec.duck_envelope[*]` + `audio_spec.sfx_accents[*]` | **TRANSFORM** — the EDL's swell markers → gain moves (duck/swell dB) + SFX accent placements. | The core finish act. Map each swell marker → a duck/swell gain move and (where the marker is an emphasis swell) an SFX accent at the same `at_ms`. Assert each `at_ms >= 0` AND `<= total_timeline_ms`. Over-range → `audio_marker_out_of_range`. NO waveform decode — declared markers only. |
| Derived from VO spans (Step 6) | `audio_spec.duck_envelope[*].{from_ms, to_ms, duck_db}` | **TRANSFORM** — VO presence spans → ducking envelope under the voice. | Author the −dB duck across each VO span so the bed sits under the voice; swell +dB into the EDL's emphasis markers. The finish's mix math. Declared gain moves, NOT applied DSP. |
| `edl.total_timeline_ms` | `audio_conform_check.total_timeline_ms` + `spec_fidelity_check.timeline_duration_matches_edl` | TRANSFORM → re-assert + duration-band check. | Re-assert the EDL duration (NOT re-derived); `duration_in_band == (45000 <= total_timeline_ms <= 75000)`. A mismatch between the spec's timeline and the EDL → `spec_fidelity_breach`. |
| `vo_transcript[*].text` | `audio_spec.vo_polish` reference + `audio_firewall_pass_11` scan surface | **PASSTHROUGH — byte-faithful, finish-only.** | The VO transcript is Script/Editor authored; Sound copies it BYTE-FOR-BYTE as the VO polish reference (NO re-authoring — Hard Rule #10) and scans it at the 11th firewall pass. A deviation → `spec_fidelity_breach`; a banned token → `audio_firewall_breach`. |
| `edl.frame_rate` / `aspect` / `resolution` (const inherit) | `audio_spec` header (format echo) | PASSTHROUGH — format spec re-asserted. | 30fps / 9:16 / 1080×1920 echoed as the finish target (Brand-Voice §8). Universal — not tier-scaled. |

**Loudness-const + resolution-reference rows (rows 19–20):**

| Source | `audio_spec.json` usage | Transform | Mechanic |
|--------|-------------------------|-----------|----------|
| Platform const (Blueprint §1.2 / §4.12) | `audio_spec.loudness_target.{primary, true_peak_ceiling_dbtp}` | **DERIVED from the platform const** — NOT from any input value. | `primary = "-14 LUFS (IG/TT)"`, `true_peak_ceiling_dbtp = -1.0`; flag the −16 LUFS YT variant per `tier_richness_echo` (v1.0 specs the primary −14 only). A non-const target → `loudness_target_out_of_spec`. NO LUFS measurement — declared target only. |
| `asset_bundle.{audio[], music_bed}` | `audio_conform_check.{vo_track_resolved, music_bed_resolved}` | READ-ONLY resolution fact. | Resolve the voice track + music bed → media handle; an unresolvable voice track → `vo_track_missing`, an unresolvable bed → `audio_asset_unresolved`. Sound consumes these as fixed facts — it does NOT decode the waveform. |

**Per-check evidence rows (rows 21–23 — derived verification, NO creative authorship):**

| Source / generated | `audio_spec.json` destination | Transform | Mechanic |
|--------------------|-------------------------------|-----------|----------|
| Generated (Step 1) | `edl_precondition_check` | NEW — `{edl_id, verdict_observed}`. | The precondition evidence. `verdict_observed == "edl_ready"` required for any finish to proceed. |
| Generated (Steps 3–5, 9) | `audio_conform_check` | NEW — `{vo_track_resolved, music_bed_resolved, all_markers_in_timeline, loudness_target_in_spec, total_timeline_ms, duration_in_band}`. | `duration_in_band == (45000 <= total_timeline_ms <= 75000)`. ALL booleans `true` required for `audio_ready`. |
| Generated (Steps 3, 6, 9) | `spec_fidelity_check` | NEW — 5 fields: `{music_event_matches_edl, swell_markers_match_edl, timeline_duration_matches_edl, vo_transcript_byte_faithful, edl_evidence_hash_verified}`. | ALL `true` required for `audio_ready`. Any `false` → `spec_fidelity_breach`. The byte-faithful executor invariant. |
| Generated (Step 8) | `audio_firewall_pass_11` | NEW — `{status, passthrough_transcript_fields_scanned, hits}`. | The 11th-pass result on the DECLARED VO transcript surface. `hits` MUST be 0 for `audio_ready`; any hit → `audio_firewall_breach`. `passthrough_transcript_fields_scanned` = the true VO-transcript-field census. |

**Audio-spec aggregate row (row 24):**

| Source / generated | `audio_spec.json` destination | Transform | Mechanic |
|--------------------|-------------------------------|-----------|----------|
| Generated (Step 10) | `output_type` + `verdict` + (non-ready) `failure_code`/`failed_check_id`/`route_back_to` + `qc_pre_flags[]` + `metadata` + `finish_target` + `mode_blind_confirm` + `human_review_required` | NEW — polymorphic discriminator + headline judgment + routing + ≥4 snake_case predicates + Cross-SPEC §3.9 canonical + 6 Sound additions + the mode-blind + finish-target self-attestations + Lever-3 default. | `output_type ∈ {successAudioSpec, errorEnvelope}`; `verdict ∈ {audio_ready, fail}` (**two verdicts only — NO `revise`; inherits Editor's deterministic posture**). `failure_code` present only on `errorEnvelope` — one of 9 codes (§6.3) + `sound_agent_failed` slot-11. `qc_pre_flags[]` ≥4 snake_case (e.g. `loudness_target_in_spec`, `vo_track_resolved`, `audio_firewall_clean_pass_11`, `mode_blind_finished`). 10-tuple parent_chain (held additively) + `audio_spec_class: "primary_master_-14lufs"` + `audio_spec_evidence_hash` (SHA-256) + `audio_processed: false` + `finish_mode: "human_in_the_loop"` + `runtime_environment_class` (see §16, partial 2). `mode_blind_confirm: {production_mode_read: false, consumed: "mode_agnostic_edl"}`. `human_review_required: true` per Rule 13. `cost_incurred_usd` ≈ 0.00. |

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

Four fields are reserved in the field map but not yet active in v1.0:

- **`audio_spec.variant_masters[]`** (the −16 LUFS YT master + other platform-loudness variants) — v1.0 specs the primary −14 LUFS IG/TT master and echoes `tier_richness_echo.loudness_variants_planned` count only; the auto-specced −16 YT master activates in v1.1 (a variant master is a derived re-conform, lower-leverage than the primary — Open Question 5, resolved as deferred). Deferred.
- **`audio_spec.measured_lufs`** (byte-level integrated-loudness measurement + true-peak reading) — v1.0 DECLARES the −14/−16 target as a conform goal; live LUFS measurement + true-peak limiting needs waveform decode + a loudness meter. Flips active when decode lands (v1.1). Deferred.
- **`finish_target.v2_edit_uri` (active write)** — reserved/placeholder in v1.0 (the human writes the v2.mp4 to this path on finish); the agent populates it as a real finished-audio handle only when Week 4–5 automation ships (v1.1). Deferred.
- **`audio_spec.daw_session_export`** (Pro Tools / Audition session adapter) — v1.0 emits the JSON audio spec + a declarative mix view; the native DAW-session export is a derived finish-format convenience that lands with the render automation (Open Question 4-adjacent). Deferred to v1.1+.

### 10.3 No-touch fields (read-only references)

Read by the agent but never written to its output (audit trail only):

- `edl.conform_check.*` (Editor's timeline-conform adjudication) — Sound TRUSTS it (the cut is gap-free + frame-accurate) and re-asserts only the audio-layer facts it enforces (timeline duration, music event, swell markers); it does NOT re-adjudicate the conform (Editor's jurisdiction; re-conforming would imply timeline authority Sound does not have).
- `edl.plan_fidelity_check.*` — Editor's plan-fidelity result. Sound reads it as context and does NOT re-verify the plan-to-EDL fidelity (Editor's authority).
- `edl.edl_firewall_pass_10.*` — Editor's 10th-pass commit-time firewall result on the caption/lower-third/end-card text. Sound reads it as context (that text was clean at commit) and runs its OWN 11th pass over the SAME VO transcript at the AUDIO FINISH — a different moment in the lifecycle (commit vs finish) and a different surface (spoken VO, not on-screen copy). Read as context, never echoed.
- `preflight_report.cost_ledger_check.*` (denormalized) — read-only context. Sound carries NO cost fields beyond its own `cost_incurred_usd` (Rule 11 — no re-litigation).
- `asset_manifest.spec_check.*` (the per-asset aspect/fps/resolution evidence) — Sound reads `asset_bundle.audio[]` + `music_bed` to resolve the audio assets; it does NOT re-echo Ingest's spec adjudication (re-validation authority it does not hold).
- `metadata.production_mode` — **explicitly NOT read as a branch discriminator** (Hard Rule #7). Present in the inbound metadata for audit lineage, but Sound's `mode_blind_confirm.production_mode_read: false` attests it never consulted it for the finish. The strongest no-touch field in the fleet — reading it would break the convergence contract three stages deep.
- `accumulated_qc_pre_flags` (upstream union) — consumed as read-only context; Sound appends its own ≥4 predicates without modifying the upstream surface.

### 10.4 Schema authoring note (for the schemas day, Day 78+)

The schema author must encode the field map above as JSON Schema Draft 2020-12 constraints. Specifically:
- `parent_chain` MUST use `prefixItems: [..×10]`, `minItems: 5`, `maxItems: 10`, `items: false` — the **additive hold**. Exact 10-tuple cardinality (`minItems: 10`) is **QUINTUPLY-BLOCKED** until the Cross-SPEC §3.9 amendment ratifies AND the Editor 9-tuple LOCKs AND the Edit Director 8-tuple LOCKs AND the Ingest 7-tuple LOCKs AND the QC 6-tuple LOCKs behind it; the schema carries a `TODO@cross-spec-3.9-ratification` flip note at the field.
- `output_type` MUST drive a `oneOf [successAudioSpec, errorEnvelope]` polymorphic split.
- `verdict` MUST use `enum: ["audio_ready", "fail"]` — **exactly two values, NO `revise`.** Inherits Editor's determinism — the executor has no success-side judgment branch.
- `failure_code` (errorEnvelope branch) MUST use `enum` of exactly the 9 codes (§6.3) + `sound_agent_failed`. Schema MUST enumerate `vo_track_missing` and `audio_asset_unresolved` as **two separate codes** (NOT folded — §6.3 split by distinct recovery diagnostic, opposite direction from Editor folding all resolution to `asset_unresolved`).
- `music_bed.asset_uri` fields MUST use `pattern: "^ars://[a-zA-Z0-9_\\-./]+$"` (platform-relative, Hard Rule inherit).
- `loudness_target.primary` MUST use `enum: ["-14 LUFS (IG/TT)", "-16 LUFS (YT)"]` with v1.0 default `"-14 LUFS (IG/TT)"`; `true_peak_ceiling_dbtp` MUST use `const: -1.0` (the platform loudness spec encoded at the schema layer — Blueprint §1.2).
- `vo_polish.level_lufs_target` MUST use `const: -16` (the VO pre-master target); `vo_polish.voice_cadence` MUST reference the brand voice const (`brand_voice_v3`).
- `sfx_accents[*].at_ms` and `duck_envelope[*].{from_ms, to_ms}` MUST use `minimum: 0` with a runtime `<= total_timeline_ms` assertion (the marker-in-timeline rule — machine-enforced floor at the schema layer, ceiling at runtime).
- `edl.frame_rate` echo MUST use `const: 30`, aspect `const: "9:16"`, resolution `const: "1080x1920"` (the format spec encoded at the schema layer — Brand-Voice Intake §8).
- `audio_spec_evidence_hash` and `spec_fidelity_check.edl_evidence_hash` MUST use `pattern: "^[a-f0-9]{64}$"` (lowercase hex, 64 chars).
- `audio_processed` MUST use `const: false` in the v1.0 schema (the human finishes; automation is v1.1) and `finish_mode` MUST use `const: "human_in_the_loop"`.
- `mode_blind_confirm.production_mode_read` MUST use `const: false` — the convergence guarantee encoded at the schema layer, machine-checkable (the third agent to carry it).
- `audio_conform_check` + `spec_fidelity_check` sub-booleans MUST all be `required` (present, possibly `false`) on the success branch — their presence is the finish-integrity invariant.

### 10.5 Finish-by-tier flatness matrix

Sound's finish logic is **mode-agnostic** (§4) AND **tier-FLAT** (§4 / §7) — the same divergence from Edit Director (the only tier-*sensitive* agent in the post tail) that Editor holds. The table maps which finish fields/behaviors scale per tier — the answer is **almost none**: only the echoed variant count differs, and even that does not change the finish behavior (v1.0 specs the primary −14 LUFS master for every tier):

| Field / behavior | Pilot | Starter | Pro | Enterprise | Notes |
|------------------|:-----:|:-------:|:---:|:----------:|-------|
| Finish logic | faithful | faithful | faithful | faithful | **Identical executor path at every tier** |
| `loudness_variants_specced` (v1.0) | 1 | 1 | 1 | 1 | v1.0 specs the primary −14 LUFS only |
| `tier_richness_echo.loudness_variants_planned` | 1 | 1 | 2 | 2 | Echoed for awareness; −16 YT auto-specced v1.1 |
| `loudness_target.primary` / `true_peak_ceiling_dbtp` | −14 / −1.0 | same | same | same | Loudness spec is universal (Blueprint §1.2) |
| VO polish / duck envelope / SFX accents (byte-faithful to EDL) | ALL | ALL | ALL | ALL | **Finish fidelity is NOT a tier feature** |
| `audio_processed: false` / `finish_mode: human_in_the_loop` | true | true | true | true | Universal — the human finishes at every tier |
| `mode_blind_confirm.production_mode_read: false` | true | true | true | true | Universal — every tier, every mode |
| `cost_incurred_usd` | ~$0.00 | ~$0.00 | ~$0.00 | ~$0.00 | Zero generative + zero DSP cost at every tier |

A Pilot reel and a Enterprise reel are finished by the **identical executor logic** — the richness (swell count, SFX accents) already lives in the EDL Sound receives; Sound faithfully specs whatever envelope arrives. **The EDL carries the tier envelope; Sound's finish does not scale.** This is the same tier-flat discipline Editor and Ingest hold — a technical executor does not re-litigate the tier ladder. The matrix is the basis for the SKILL bundle's tier-flat logic on the SKILL-build day.

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 75 · status updates · on-time trajectory)

**Calendar inherited from outline §0 build calendar — on schedule, no slip.** Day 75 author task per outline: partial 1 (§6 + §7 + §10 + §14). On-disk file-state confirms the chain is intact through Day 74; this document ships partial 1 ON the calendar. Partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16) targets Day 76 (Sat Jul 4).

### 14.1 Calendar (Day 74 → v1.0 LOCK — Sound trajectory)

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 74 | Thu Jul 2 · Wk11 | **Sound v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 75 | Fri Jul 3 · Wk11 | **SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14) SHIPPED** | ✅ DONE (this doc) | Donna overnight |
| Day 76 | Sat Jul 4 · Wk11 | SPEC body partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16) | ⏳ NEXT | Donna overnight |
| Day 77 | Sun Jul 5 · Wk11 | **REST DAY — no build** (pre-stage LOCK-candidate scaffold only) | ⏳ Rest Day | — |
| Day 78 | Mon Jul 6 · Wk12 | v1.0 LOCK CANDIDATE (full §3 self-audit + critical-decisions walk + verdict math) | ⏳ planned | Donna overnight |
| Day 79+ | Tue Jul 7+ · Wk12 | schemas (input+output) → SKILL bundle → LLM-test runbook → v1.0 LOCK | ⏳ planned | Donna overnight / operator |

**Cadence note:** the Day 78+ tail mirrors the Editor Day 69–73 / Edit Director Day 61–65 pattern exactly (LOCK candidate → schema pair → SKILL bundle → LLM-test runbook → operator-gated v1.0 LOCK). The exact day assignments after Day 78 confirm on the partial-2 §14 update (Day 76), accounting for the Day 77 Rest Day.

### 14.2 Author tasks completed this session (Day 75)

- **§6 — 11-Check Self-QC List** — LOCKED-as-drafted. 11 checks, bipartite-covering the 9-code (+ slot-11) namespace; the 11th defense-in-depth firewall (audio-domain VO-transcript passthrough); two-verdict determinism (no `revise`); the canonical 11-entry entity firewall list (§6.5) inherited verbatim.
- **§7 — System Prompt v1.0** — LOCKED-as-drafted. Frame + 13 hard rules + universal-access tier-FLAT table + 11-step finish loop (verbatim from outline §5) + the Blueprint §4.11 v2-edit/audio-spec shape inlined + the −14/−16 LUFS loudness targets + the brand voice cadence as the enforced finish surface + voice rule. ~14 KB. The six Sound-defining hard rules (2, 3, 7, 8, 10, 13) map to self-QC checks / loop steps / error codes.
- **§10 — Audio-Spec Field Map** — LOCKED-as-drafted. 24 rows across lineage (12) / EDL passthrough + mix transform (6) / loudness-const + resolution reference (2) / per-check evidence (3) / audio-spec aggregate (1). Zero authored rows (the executor signature). 4 reserved fields (v1.1). 7 no-touch fields. Schema-authoring note for Day 78+. Finish-by-tier flatness matrix.
- **§14 — Implementation Plan** — LOCKED-as-drafted (this section). On-time trajectory; Day 76 partial 2 next; Day 77 Rest Day; Day 78+ LOCK-candidate tail.

### 14.3 Author tasks remaining (Day 76 partial 2)

- **§8 — Performance Targets** — 9 metric categories. Schema validity 100% / spec-fidelity 100% / audio-domain firewall catch 100% / loudness-target-in-spec 100% / marker-in-timeline 100% / false-audio-ready rate 0% target / false-fail rate ≤ 8% / p50 latency 22s / p95 70s / zero engine + zero DSP cost.
- **§9 — Test Fixtures** — 5-fixture portfolio (TC-01 clean Mode-A→EDL Pro `audio_ready` · TC-02 Mode-C Enterprise `audio_ready` mode-blind finish-convergence proof · TC-03 `audio_marker_out_of_range` → fail → Editor · TC-04 `vo_track_missing` → fail → Ingest · TC-05 `audio_firewall_breach` GATING). Optional probes: `spec_fidelity_breach` (tampered hash) + slot-11 catch-all.
- **§11 — Cost Model** — zero engine + zero DSP snapshot; faithful-finish value model; v1.1 Week 4–5 DSP compute note.
- **§12 — Verdict Math** — AUDIO_READY = (Editor precondition met) ∧ (edl_evidence_hash verified) ∧ (VO track resolved) ∧ (music bed resolved) ∧ (all markers in timeline) ∧ (loudness target in spec) ∧ (timeline duration matches EDL) ∧ (spec-fidelity byte-faithful) ∧ (audio-domain firewall clean). Any ∧-term false → fail (NO `revise`).
- **§13 — Critical Decisions LOCKED** — 10–14 decisions (14 pre-scaffolded in the outline §6–§16 preview). Confirms the errorEnvelope code count (7–9), the self-QC check count (10–12), and the loudness dual-master scope.
- **§15 — Change Log** — v1.0 lifecycle entries + parked candidates.
- **§16 — Metadata Block Schema** — Cross-SPEC §3.9 canonical + 6 Sound additions (10-tuple parent_chain, audio_spec_class, audio_spec_evidence_hash, audio_processed const false, finish_mode, runtime_environment_class).

### 14.4 Dependencies & gates (carried — operator-only, NOT advanced)

Sound's eventual v1.0 LOCK hard-gates itself on the SIX predecessor LOCK ceremonies closing first (AI Video Gen + Style Replication + QC Pre-flight + Ingest + Edit Director + Editor) — the **Editor 9-tuple is Sound's direct 10-tuple dependency**. All six remain OPERATOR-GATED (version tags unflipped; Day 27/36/47/57/65/73 runbook executions unconfirmed). This partial 1 is forward-design over LOCK-stable text only.

### 14.7 Parent-chain amendment gate (quintuply-deferred — carried)

The 10-tuple `parent_chain` extension is **QUINTUPLY-DEFERRED**: it depends on the Cross-SPEC §3.9 n-tuple amendment ratification AND the Editor 9-tuple LOCK AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it. Held additively at `minItems: 5` (`prefixItems` 0–9, `maxItems: 10`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. **Sound is the FIFTH forcing function for the §3.9 amendment.** Donna recommends the operator RATIFY the amendment AS-DRAFTED so all 17 agents inherit n-tuple lineage; Sound holds additively until the chain closes. NOT advanced this session.

---

## Process integrity attestation (Day 75)

- ✅ **No prior canon modified.** 1 NET-NEW forward deliverable (this Day 75 Sound SPEC body partial 1 — §6 + §7 + §10 + §14, forward design over the LOCKED-as-drafted Editor SPEC + the Day 71 Editor schemas + the Ingest asset-bundle schema + the Blueprint + the Day 74 Sound outline). The Editor artifact set, the predecessor bundles/runbooks, Blueprint, Cross-SPEC review, Brand-Voice Intake — all read-only inputs.
- ✅ **No LLM dispatched. No engine, no render, no audio DSP, no byte-decode, no LUFS measurement, no network, ZERO $ spent.** This partial is forward design; Donna executed none of it.
- ✅ **No operator-impersonation.** No LOCK ceremony executed. All SIX predecessor LOCK ceremonies + the six pending runbook executions + the §3.9 amendment + the §8.7 ≤5% tightening confirmed STILL-PENDING via on-disk file-state. The **10-tuple `parent_chain` stays held additively (`minItems 5`)** — Sound is the FIFTH forcing function for the §3.9 amendment; NOT advanced.
- ✅ **No fake-advance.** §6/§7/§10/§14 mirror the LOCKED Editor SPEC + the Day 71 schemas + the Blueprint exactly; they do NOT flip any deferred cardinality or pre-empt any operator ceremony. Sound's v1.0 LOCK hard-gates itself on the six predecessor LOCKs closing first.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. `brand_id` v1.0 = REINVENTED (pilot brand). The §6.5 firewall block-list enumerates HC/NPOX tokens precisely so the agent can BLOCK them at the audio-finish layer — this is the firewall's block-list, not a cross-entity reference. No HC/NPOX/REINVENTED-command-center crossover.
- ✅ **Rest Day honored** — Day 70 (Sun Jun 28) observed (11th). This Day-75 build runs Friday. Next Rest Day: Day 77 (Sun Jul 5).
- ✅ **No scope expansion.** One forward deliverable (partial 1) + offline cross-check + log + mirror + Notion status update + standing housekeeping + status-ping attempt. Nothing extra acted on.

---

## Files produced today (Day 75)

- `ars/ARS-2026-07-03-Day-75-Sound-Agent-SPEC-Body-Partial-1.md` — this doc
- `ars/build-log-2026-07-03.md` — Day 75 build log

Mirror copies in `/outputs/ars/`.

---

*Day 75 ships clean. Day 76 build session targets SPEC body partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16). Sound is Agent #11 of 17 — the 11th defense-in-depth firewall (audio-domain VO-transcript passthrough) and the second executor agent in the post tail, the third contractually mode-blind agent (Ingest's mode-convergence seam holds three stages deep). §6 + §7 + §10 + §14 are LOCKED-as-drafted; the audio spec authors an audio conform spec the human finishes (`audio_processed: const false`), keeping the zero-dollar / no-DSP / no-decode invariant intact. Two-verdict deterministic (`audio_ready | fail`, no `revise`). 10-tuple parent_chain held additively — Sound is the FIFTH §3.9 forcing function. Operator pickup unchanged: (1) the six predecessor LOCK ceremonies gate Sound's v1.0 LOCK — the Editor 9-tuple is Sound's direct 10-tuple dependency; (2) execute the six pending runbooks (Day 27 / 36 / 47 / 57 / 65 / 73); (3) ratify the Cross-SPEC §3.9 n-tuple amendment (Sound is the fifth forcing function); (4) the §13 critical-decisions walk on Day 76 confirms the errorEnvelope code count (7–9), the self-QC check count (10–12), and the loudness dual-master scope. Next Rest Day: Day 77 (Sun Jul 5).*
