# ARS — Sound Agent v1.0 SPEC BODY PARTIAL 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16)

**Date:** Sat Jul 4, 2026 (Day 76 · Wk11 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 2 — §8 + §9 + §11 + §12 + §15 + §16 LOCKED-as-drafted Day 76. §13 critical decisions: **13 LOCKED-as-drafted + 2 carried open** (D7 10-tuple QUINTUPLY-DEFERRED; D15 Motion-handoff PRELIMINARY — drafted to Donna's recommended default, operator ratification pending). With this partial, the Sound Agent v1.0 SPEC body is **COMPLETE**: §0–§16 all authored across the outline (Day 74), partial 1 (Day 75), and this partial 2 (Day 76). Next: v1.0 LOCK CANDIDATE assembly → input/output schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK on the established cadence (Editor Day 69–73 / Edit Director Day 61–65 / Ingest Day 53–57).
**Pattern source:** `ARS-2026-06-26-Day-68-Editor-Agent-SPEC-Body-Partial-2.md` (Day 68 partial 2 — proven shape inherited verbatim) and `ARS-2026-06-18-Day-60-Edit-Director-Agent-SPEC-Body-Partial-2.md` (grandparent pattern).
**Partial 1 source:** `ARS-2026-07-03-Day-75-Sound-Agent-SPEC-Body-Partial-1.md` (§6 + §7 + §10 + §14 LOCKED-as-drafted Day 75).
**Outline source:** `ARS-2026-07-02-Day-74-Sound-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 74 + the §6–§16 LOCK-scope preview + the Open Questions).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — roster position 12 "Sound" + §3 mode-agnostic post-production contract + §4.10 Editor→Sound `EDL + v1 edit` payload + §4.11 Sound→Motion `v2 edit with finalized audio` handoff shape + §7 dispatch I/O + §9 build-checklist row 12 "Human-in-the-loop for Week 2; full automation Week 4–5").
**Brand-audio canon:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (voice / tone), §8 (reel format specs: 9:16 · 1080×1920 · 30fps · 45–75s structure), §11 (caption ↔ VO cadence) + Blueprint §1.2 / §4.12 loudness targets (**−14 LUFS IG/TT · −16 LUFS YT**) — the audio-finishing rules the conform spec specifies faithfully.
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor v1.0 LOCK candidates + schemas + SKILL bundles + runbooks. **All SIX predecessor LOCK ceremonies remain OPERATOR-GATED entering Day 76 — file-state confirmed (version tags unflipped). Same forward-design posture as partial 1.**

> **Cadence honesty (on schedule — surfaced):** The Day 74 outline calendared partial 1 for Day 75 (Fri Jul 3) and partial 2 for **Day 76 (Sat Jul 4)**. On-disk file-state confirms the chain is intact: Day 75 partial 1 shipped (Fri Jul 3), Day 74 outline before it (Thu Jul 2), Day 73 Editor runbook (Tue Jul 1), Day 70 (Sun Jun 28) correctly a Rest Day no-build. Tonight's Day 76 session ships partial 2 (this document) ON the outline calendar — no slip. Clock verified at run start: **Sat Jul 4 (Pacific)** — not Rest Day, build allowed. Next Rest Day: Day 77 (Sun Jul 5).

> **Scheduled-task "Agent #7 QC Pre-flight" pointer (still stale — reconciled again):** the task prompt's "next up = Agent #7 QC Pre-flight" line has been stale since Day 48 and is reconciled in every log/partial since. On-disk source of truth (read first, per standing rule) shows the fleet well past #7: QC Pre-flight (#7) Day 40→47; Ingest (#8) Day 48→57; Edit Director (#9) Day 58→65; Editor (#10) Day 66→73; Sound (#11) outline Day 74, partial 1 Day 75, **partial 2 tonight**. Followed the on-disk position, not the prompt's pointer. Surfaced, not silently reconciled.

> **Authoring discipline (LOCK signal):** §8 + §9 + §11 + §12 + §15 + §16 are LOCKED-as-drafted Day 76. §13 carries the only two forward-looking edit slots in the entire SPEC (D7 10-tuple + D15 Motion-handoff — both operator-gated). Everything else is canon as of this document. With partial 1's §6/§7/§10/§14, the Sound Agent v1.0 SPEC body is now complete end-to-end (§0–§16).

> **LOCK-state awareness (CRITICAL — do not silently advance):** On-disk file-state confirms all six predecessor LOCK ceremonies remain OPERATOR-GATED (version tags unflipped; Day 27 + Day 36 + Day 47 + Day 57 + Day 65 + Day 73 runbook executions unconfirmed). Sound v1.0 LOCK hard-gates on those closing + the Cross-SPEC §3.9 ratification. The **Editor 9-tuple LOCK is Sound's DIRECT 10-tuple dependency** (the `edl_ready` precondition + the 9-tuple the 10-tuple extends), and the Editor LOCK is itself behind the Edit Director 8-tuple LOCK, behind the Ingest 7-tuple LOCK, behind the QC 6-tuple LOCK. This partial is forward-design over LOCK-stable text artifacts only; zero production output consumed, zero operator ceremony assumed.

---

## §8 — Performance Targets (LOCKED-as-drafted Day 76)

Nine metric categories, per the outline §8 preview and the partial 1 §14.2 runway. Pattern parity: Editor §8 / Edit Director §8 / Ingest §8 / QC Pre-flight §8 (category → target → measurement → rationale). Sound's defining posture: **a $0, DSP-free, FULLY-deterministic executor agent must be judged on audio-conform correctness, spec-fidelity catch-rates, loudness-target-in-spec, and shape-validity — there is no mix quality to score and NO judgment slot to tune, only whether the audio spec is EDL-faithful, loudness-correct, brand-faithful, and firewall-clean at emission.**

| # | Metric category | v1.0 target | Measured how | Rationale |
|---|----------------|-------------|--------------|-----------|
| 1 | **Schema validity** | **100%** of emissions validate against `output.schema.json` (`successAudioSpec` AND `errorEnvelope` branches) | Validator harness on every fixture run + every runbook case | The audio spec is the audio app's (and Motion's) source of truth and the orchestrator parses it blind. A malformed audio spec is a pipeline-halting defect by definition. No tolerance. |
| 2 | **Spec-fidelity catch** | **100%** of seeded spec-fidelity deviations caught (an altered music event, a moved/dropped swell marker, a timeline-duration mismatch, a byte-unfaithful VO transcript, a tampered `edl_evidence_hash` must NEVER survive to `audio_ready`) | TC-class fixtures: each fidelity deviation seeded in isolation; `spec_fidelity_check` sub-status audited | An EDL-unfaithful audio spec is an unauthorized override burned into the mix. The `spec_fidelity_check` booleans make this a deterministic conjunction — anything below 100% means the executor silently re-finished against a plan it wasn't given. Zero tolerance (D10). |
| 3 | **Audio-domain firewall catch (11th pass)** | **100%** of seeded banned tokens in the passthrough VO transcript caught before the mix reaches Motion | TC-05 class fixtures: tokens injected into the `vo_transcript[].text` Sound finishes, across all 11 firewall entries + conjugates | The 11th pass is the LAST AUDIO checkpoint before Motion typography. Sound authors no new copy, but it finishes the SPOKEN audio — a leak that survives here rides into the mastered audio of the published reel. By construction a deterministic token-boundary scan; below 100% means the scan is broken. The single highest-stakes catch in the namespace. |
| 4 | **Marker-in-timeline + loudness-target-in-spec** | **100%** of `audio_ready` specs have every mix/SFX/duck marker `0 ≤ at_ms ≤ total_timeline_ms` AND the loudness target == the platform const (−14 LUFS IG/TT primary; −16 LUFS YT flagged; true-peak ceiling −1.0 dBTP) | Fixture + runbook: `audio_conform_check.all_markers_in_timeline` + `loudness_target_in_spec` audited | An accent past the timeline is an unplaceable directive — the audio app cannot land it. A loudness target off the platform const publishes a reel that the platform re-normalizes (audible pumping). The math is deterministic (compare `at_ms` to `total_timeline_ms`; compare target to the platform const); 100% is structural. Over-range → valid `fail` (`audio_marker_out_of_range`); off-const → `loudness_target_out_of_spec`. |
| 5 | **Audio-asset resolution** | **100%** of `audio_ready` specs bind every VO-polish + music-bed + SFX directive to a resolved Ingest `asset_bundle` handle (voice track + music bed both resolve) | Fixture + runbook: `audio_conform_check.vo_track_resolved` / `music_bed_resolved` audited | A mix directive over an unresolved asset is a spec over silence. The two distinct asset classes route back with distinct diagnostics (voice → `vo_track_missing`; music → `audio_asset_unresolved`) — both to Ingest, the resolution owner. 100% resolution-or-fail is structural; an unresolved asset is a valid `fail`, never an `audio_ready` escape. |
| 6 | **False-audio-ready rate** | **0%** (ZERO tolerance — D3/D10) | Across the full fixture corpus + runbook: no `audio_ready` verdict on any reel seeded with any conform/fidelity/loudness/firewall defect | A defective audio spec reaching the audio app burns a finish cycle, or worse, a mastered leak (the firewall class has no post-hoc fix once the audio is published). Bias all ambiguity toward `fail` (Hard Rule #13). The expensive failure direction is the one we never accept. |
| 7 | **False-fail rate** | **≤ 5%** | Clean fixtures (TC-01/TC-02 class): proportion incorrectly failed | Over-flagging a borderline marker to `fail` is the acceptable failure direction — a false `fail` costs one re-route (~$0); a false `audio_ready` costs a finish cycle or a mastered leak. The ≤5% ceiling is **tighter than Edit Director's ≤8%** because Sound carries **NO subjective surface** — every check is binary (a marker is in range or it isn't; a target is the platform const or it isn't; the VO transcript is byte-faithful or it isn't), so there is no correct-conservatism band to absorb (the looser 8% existed only to absorb Edit Director's one `revise` judgment surface). Sound ties Editor / Ingest's ≤5% — the deterministic-executor ceiling. *(Surfaced: partial 1 §14.2 previewed ≤8% carried from the Editor template; the tightening to ≤5% follows directly from Sound's two-verdict determinism (D3) — flagged for operator confirm at the Day 78 LOCK candidate. Donna recommends ≤5%.)* |
| 8 | **Latency** | **p50 ≤ 22s · p95 ≤ 70s** per reel | Wall-clock per runbook case + fixture run | Audio-conform reasoning + spec authoring, no engine wait, no DSP, no waveform decode I/O. **Lighter than Editor's p50 25s / p95 75s** — specifying mix/level/loudness directives over an already-conformed EDL is less generative than authoring the frame-accurate timeline from a plan. Sound must never be the pipeline's bottleneck. |
| 9 | **Cost** | **$0.00 engine + $0.00 DSP — structurally guaranteed** | Audit: zero engine calls, zero DSP dispatch, zero waveform decode, `audio_processed: false` on every emission | Hard Rules #3/#12. Cost here is not a budget to manage but an invariant to attest. Any non-zero engine/DSP figure = a Hard Rule violation, not an overrun. Ties Ingest / QC Pre-flight / Edit Director / Editor for lowest in the fleet. |

**Self-QC yield (carried metric note):** ≥90% of emissions pass the 11-check self-QC list (§6) on attempt 1; the 2-strike retry consumed in ≤10% of runs; `sound_agent_failed` slot-11 halt rate <2%. The retry exists for resilience, not as a crutch — high retry consumption means the audio-spec constructor is sloppy; a high slot-11 rate means the agent design is defective. (Folded into category 1/6 measurement; broken out here for parity with Editor §8.9.)

**Measurement context (v1.0):** All targets are adjudicated against the §9 fixture portfolio + the LLM-test runbook corpus (operator-executed, paste-and-run, $0). No live-pipeline telemetry exists until the orchestrator ships — these are design-acceptance targets, re-baselined when runtime telemetry lands (v1.1).

**Targets NOT carried (deliberate, surfaced):** No audio-render-quality / true-LUFS metric (the human mixes in v1.0; the Week 4–5 automation owns render + measurement QC — Sound SPECS the target, it never measures the waveform), no cut-conform metric (Editor's domain — Sound TRUSTS the `edl_ready` verdict; re-conform is banned, Hard Rule #11), no asset-validity metric (Ingest's jurisdiction — re-validation ban), no cost-ceiling adherence metric (QC Pre-flight's authority), no creative/brand-quality score (Edit Director's jurisdiction — Sound TRUSTS the directed mix intent in the EDL). Sound's scoreboard measures exactly its own job: finish the EDL's audio into an EDL-faithful, loudness-correct, brand-faithful, firewall-clean audio spec; catch every fidelity deviation and every VO-transcript leak; over-flag conservatively; stay fast; stay free.

---

## §9 — 5 Test Fixtures (LOCKED-as-drafted Day 76)

Pattern source: Editor §9 / Edit Director §9 / Ingest §9 / QC Pre-flight §9. Fixture contract: each = **(input.json, expected_output.json, expected_verdict, expected_code_or_null, scenario_description)**. Fixtures live at `skills/sound-agent/tests/` (authored on the SKILL-bundle day; this section is their binding specification). All fixtures use the canonical REINVENTED brand-anchor (Cross-SPEC fixture canon) and platform-relative `ars://` URIs. **5 of the 9 LOCKED codes are exercised behaviorally; the remaining 4 (`upstream_edl_not_ready`, `upstream_not_success`, `audio_asset_unresolved` [music-bed variant], `loudness_target_out_of_spec`, `audio_lineage_failure`) + slot-11 + the `spec_fidelity_breach` hash-tamper variant are exercised schema-only** (enum-presence validation) or in the runbook's adversarial case, mirroring the fleet's fixture-economy precedent. The behavioral 5 are chosen to cover the two highest-stakes Sound-original surfaces (the mode-blind finish-convergence proof, the audio-domain firewall) plus the two PASS-side anchors and the two principal route-back targets (Editor, Ingest).

### TC-01 — Clean Mode-A-origin Pro reel → AUDIO_READY (full audio spec)

- **Scenario:** An Editor-passed (verdict `edl_ready`) Pro reel whose EDL originated from a Mode-A (human footage) production chain: a complete `events[]` (6 cut beats), a `music_event` at `at_ms: 0`, a `music_swell_map[]` length 2, `caption_events[]` present, `total_timeline_ms: 65000`, a resolved Ingest `asset_bundle.audio[]` (voice track present) + `asset_bundle.music_bed` (resolvable), a byte-faithful `vo_transcript[]`, firewall-clean upstream copy, a 9-tuple inbound `parent_chain`, `edl_evidence_hash` present.
- **Expected verdict:** `audio_ready` · **Expected code:** `null`
- **Asserts:** `successAudioSpec` validates; `audio_spec` carries `loudness_target {primary: "-14 LUFS (IG/TT)", true_peak_ceiling_dbtp: -1.0}`; `vo_polish {level_lufs_target, de_ess, breath_trim, voice_cadence}` authored to the brand voice cadence; `music_bed {asset_uri, at_ms: 0, base_level_db, duck_under_vo_db}` bound to the resolved bed; `duck_envelope[]` covering the VO spans with swell moves mapped from the EDL `music_swell_map` (each `from_ms`/`to_ms` inside the timeline); `sfx_accents[]` each `at_ms ≤ total_timeline_ms`; `audio_conform_check {vo_track_resolved: true, music_bed_resolved: true, all_markers_in_timeline: true, loudness_target_in_spec: true, total_timeline_ms: 65000, duration_in_band: true}`; all 5 `spec_fidelity_check` booleans `true` (`music_event_matches_edl`, `swell_markers_match_edl`, `timeline_duration_matches_edl`, `vo_transcript_byte_faithful`, `edl_evidence_hash_verified`); `audio_firewall_pass_11 {status: "pass", hits: 0}` with `passthrough_transcript_fields_scanned` matching the VO-transcript census; `mode_blind_confirm {production_mode_read: false, consumed: "mode_agnostic_edl"}`; `finish_target {audio_processed: false, finish_mode: "human_in_the_loop"}`; `route_back_to: null`; `handoff_targets: ["motion-agent"]`; `human_review_required: true`; `audio_spec_evidence_hash` matches `^[a-f0-9]{64}$`; `parent_chain` extended to a 10-tuple additively.

### TC-02 — Clean Mode-C-origin Enterprise reel → AUDIO_READY (mode-blind finish-convergence proof)

- **Scenario:** An Editor-passed Enterprise reel whose EDL originated from a Mode-C (replicated hot-path) production chain: an 8-beat `events[]`, the richer Enterprise envelope (3 swells, `loudness_variants_planned: 2`), the resolved larger asset bundle. The ONLY input difference from TC-01 is `metadata.production_mode == "C"` and the richer envelope.
- **Expected verdict:** `audio_ready` · **Expected code:** `null`
- **Asserts:** The authored audio spec is **byte-shape-identical** to TC-01's downstream of the `tier_richness_echo` block — the loudness-target math, VO-polish directives, music-bed mix + duck-envelope authoring, SFX placement, firewall pass, and `mode_blind_confirm` are produced by an IDENTICAL executor code path despite the different origin mode (this pair IS the **mode-blind finish-convergence proof** — the Sound analog of Editor's TC-01/TC-02 convergence pair, now proven THREE stages deep: Edit Director → Editor → Sound). `mode_blind_confirm.production_mode_read: false` (the agent never consulted the origin mode); no mode-conditional field leaks into the audio spec; `tier_richness_echo` honors the Enterprise envelope (`loudness_variants_planned: 2`) while `loudness_variants_specced: 1` (v1.0 specs the primary −14 LUFS master only, flags the −16 LUFS YT variant) and EVERY finish rule (loudness const, brand voice cadence, marker-in-timeline, `audio_processed: false`) is identical to the Pilot/Pro path. **This fixture is the convergence payoff carried into the audio-executor seam — the finish behavior does not scale by tier and does not branch on mode.**

### TC-03 — SFX/duck marker exceeds timeline → FAIL + route to Editor

- **Scenario:** An Editor-passed Pro reel where one SFX-accent (or duck-envelope) marker `at_ms` exceeds the EDL's `total_timeline_ms` (e.g. a 67000ms accent on a 65000ms timeline — the EDL's swell map points past the conformed cut). Every other gate is clean. Sound cannot place an accent past the timeline.
- **Expected verdict:** `fail` · **Expected code:** `audio_marker_out_of_range`
- **Asserts:** `errorEnvelope` with `failed_check_id: 5`; `audio_conform_check.all_markers_in_timeline: false` with all other sub-statuses still explicitly computed (no short-circuit nulls); `detail` names the offending marker + the timeline bound (`{at_ms, total_timeline_ms}`); `route_back_to: "editor-agent"` (the timeline owner per the §6.3 route map — a marker-out-of-range is a timeline/EDL defect); verdict is `fail` (soft-recoverable: re-place the marker in the EDL), NOT a halt; `human_review_required: true`. **The finish is defensive — Sound cannot land an accent past the real timeline even if the EDL marked it; the marker is re-routed upstream, never silently clamped.**

### TC-04 — Voice track does not resolve → FAIL + route to Ingest

- **Scenario:** An Editor-passed reel where the `asset_bundle.audio[]` voice track does not resolve against the Ingest bundle (the audio handle is absent from the validated bundle — an upstream binding gap). Every other gate is clean. Sound cannot spec a VO-polish pass over a missing track.
- **Expected verdict:** `fail` · **Expected code:** `vo_track_missing`
- **Asserts:** `failed_check_id: 3` (resolution branch); `audio_conform_check {vo_track_resolved: false, music_bed_resolved: true}` internally consistent (no phantom resolution — the music bed still resolves; only the voice track is missing); `route_back_to: "ingest-agent"` (the asset-bundle owner per the §6.3 route map); `detail` names the unresolvable voice-track URI + the distinct recovery path (`"re-confirm the Ingest asset_bundle.audio[] voice-track asset_uri OR re-run Ingest"`); verdict is `fail` NOT `revise` (an unresolvable track is a hard binding gap, not a creative tension — and Sound has no `revise` slot); `human_review_required: true`. **The SPLIT-code proof:** `vo_track_missing` (this fixture) and `audio_asset_unresolved` (the music-bed variant, exercised as the §9.1 runbook probe) both route to Ingest but carry DISTINCT recovery diagnostics — the divergence from Editor folding all resolution to a single `asset_unresolved`. The audio domain's two distinct asset classes justify the split (D8).

### TC-05 — Audio-domain firewall breach (banned token in the passthrough VO transcript) → hard FAIL (the 11th-pass last audio checkpoint · GATING)

- **Scenario:** A Mode-B-origin reel, all upstream content clean through the Editor 10th (commit) firewall pass — but the passthrough `vo_transcript[]` the audio finish touches contains a spoken line reading `built with sln and holdco group` (firewall entries #4 + #1 tokens). The tokens are in the SPOKEN audio Sound finishes — the last audio surface before Motion.
- **Expected verdict:** `fail` · **Expected code:** `audio_firewall_breach`
- **Asserts:** `failed_check_id: 8`; `audio_firewall_pass_11 {status: "breach", passthrough_transcript_fields_scanned: N, hits: 2}` with `passthrough_transcript_fields_scanned` matching the true VO-transcript census (every `vo_transcript[].text` entry); forensic `detail` names BOTH leaking transcript fields + the rule each violated; the catch occurs at the AUDIO-finish layer — the moment the spoken content enters the mastered mix, the last net before the audio is published; entity firewall list applied verbatim (11 entries, token-boundary, case-insensitive). **This fixture is the 11th pass's existence proof** — a spoken-word leak that Editor's commit-pass (which scanned caption/lower-third/end-card TEXT, not the VO transcript) does not cover, caught before the audio is mastered. **The single highest-stakes code in the namespace — a miss here would be burned into a published reel's audio, with no post-hoc fix. GATING fixture: a runbook run that does not catch TC-05 fails the LOCK gate.**

### 9.1 Fixture-economy rationale (surfaced)

The unexercised codes are all either **deterministic entry/forensic halts** (`upstream_edl_not_ready`, `upstream_not_success`, `audio_lineage_failure` — single equality/shape assertions, behaviorally trivial, schema-enforced, identical in mechanism to the fleet's proven entry-gate fixtures) or **substance codes whose mechanic is fully covered by a sibling behavioral fixture** (`audio_asset_unresolved` [music-bed] shares TC-04's resolution machinery — the named optional runbook probe, chosen precisely to demonstrate the SPLIT-code distinct-diagnostic path; `loudness_target_out_of_spec` is a deterministic target-vs-const equality assertion; the `spec_fidelity_breach` hash-tamper variant shares TC-01's `edl_evidence_hash`-verify machinery). Spending fixture slots on them would displace the two clean-AUDIO_READY convergence proofs (TC-01/TC-02) and the three highest-stakes Sound-original surfaces — the two principal route-backs (TC-03 → Editor, TC-04 → Ingest) and TC-05 (the audio-domain firewall, the last audio line before Motion) — that no other test can provide.

**There is NO `revise` verdict to exercise** — Sound's two-verdict determinism (D3) means the only outcomes are `audio_ready` and `fail`, both covered. This is the divergence from Edit Director's §9, which reserved a runbook adversarial case for its one `revise` judgment surface; Sound has none (it inherits Editor's posture). Slot-11 (`sound_agent_failed`) is definitionally un-fixturable from outside (it requires inducing the agent to build a malformed audio spec twice); the runbook's adversarial case covers its semantics. The `audio_asset_unresolved` music-bed variant and the `spec_fidelity_breach` swell-marker-deviation variant are the two optional runbook probes. Same economy Editor ratified at Day 68, Edit Director at Day 60, Ingest at Day 52, QC Pre-flight at Day 43.

---

## §11 — Cost Model (LOCKED-as-drafted Day 76)

### 11.1 Zero-engine, zero-DSP snapshot (v1.0)

| Cost component | Per-reel v1.0 | Mechanism |
|----------------|---------------|-----------|
| Generative engine calls | **$0.00** | None — structurally banned (Hard Rule #3) |
| Audio DSP / mix render / LUFS normalization / SFX render / encode | **$0.00** | None in v1.0 — audio-spec authoring only; `audio_processed: const false`. The HUMAN runs the mix + loudness pass into the v2.mp4 (Blueprint Week-2 posture); full DSP automation is Week 4–5 (v1.1). |
| Byte-level audio decode (waveform / loudness measurement / true-peak) | **$0.00** | None in v1.0 — declared-transcript + platform-const loudness targets only (Hard Rules #3/#12); live LUFS measurement + true-peak limiting deferred to v1.1 |
| LLM reasoning (audio-conform adjudication + spec authoring) | **≈ $0.02–0.07** | One model pass over the EDL + resolved asset bundle + audio-spec assembly; bounded by the p95 70s latency envelope. **Comparable to or lighter than Editor's $0.02–0.08** — specifying mix/level/loudness directives over an already-conformed EDL is less generative than conforming the timeline itself. |
| Native compute / storage | **$0.00** | No fetch, no transcode, no asset movement, no waveform decode — Sound reads the EDL + bundle and emits one JSON audio spec |
| **Total `cost_incurred_usd`** | **≈ $0.00 (reported to 2dp)** | Carried in `metadata` per Cross-SPEC §3.9 |

Sound holds **no cost ceiling and no ledger authority** (Hard Rule #11 — QC Pre-flight's jurisdiction). The tier ceilings are upstream facts, enforced four gates back; restated for traceability only, NOT re-litigated. **Explicit note (outline §11 / Open Question 1):** the actual audio-render / DSP compute spend lands in v1.1 Week 4–5 automation — **v1.0 is $0 by construction (the human mixes)**.

### 11.2 Faithful-finish value model (the economic justification)

Sound produces no margin directly. Its value is **platform-loudness-validated, brand-faithful, first-pass audio finish + downstream-cost prevention**, quantified across the defect classes it uniquely prevents:

| Prevented failure | Without Sound | Cost of the miss | Sound catch cost |
|-------------------|---------------|------------------|-------------------|
| **An ad-hoc / unfaithful mix reaches the audio app (or renderer)** | The mixer improvises the levels, ducking, and loudness per reel; the directed mix intent is not specified faithfully; the finish varies from the cut | Inconsistent audio at scale + re-mix churn; the directed-finish promise erodes | ≈ $0.00 + ≤70s |
| **A loudness target off the platform const reaches the master** | The reel publishes at the wrong integrated loudness; the platform re-normalizes it (audible pumping / level jumps) — discovered only after publish | 1 wasted finish cycle ≈ 1–3 operator-hours + a re-master + a re-publish; platform-algorithm penalty | ≈ $0.00 + ≤70s |
| **An entity leak in the passthrough VO transcript reaches the mastered audio** | A banned token that survived Editor's commit pass (which scanned TEXT, not the VO transcript) is finished into the mastered mix and published | Brand-safety incident on a PUBLISHED reel's AUDIO — reputational, not monetary; the one failure class with no post-hoc fix once burned into the master | ≈ $0.00 + ≤70s (11th pass) |
| **A directed cut is silently re-finished (a swell moved, the mix re-interpreted)** | The agent "improves" the EDL's audio without a human; the published mix diverges from the directed cut, invisibly | A reel whose audio does not match the approved direction — silent, compounding, undetectable post-publish | ≈ $0.00 (faithful finish or `fail` back) |

**The asymmetry is the whole argument:** every defect Sound can catch costs effectively nothing to catch and materially more to miss — and there is no judgment slot to mis-tune because the executor is fully deterministic (the subjective surface lives upstream at Edit Director). An audio-finish gate with a $0 toll, a 100%-fidelity + 100%-firewall + 100%-loudness-in-spec mandate, and ZERO false-audio-ready tolerance is pure option value — which is why the universal-tier-FLAT table opens it to every reel at every tier with no ceiling and no per-tier scaling. **The audio-render compute that does cost money lands in v1.1; v1.0's value is catching every conform/fidelity/loudness/firewall defect for free, before a single waveform is processed.** ROI formalization against live defect telemetry is a v1.1 task (no real corpus exists pre-orchestrator).

---

## §12 — Verdict Math (LOCKED-as-drafted Day 76)

### 12.1 The ∧-of-gates composition (NO judgment slot — fully deterministic)

Deterministic boolean composition over declared evidence — **no thresholds, no weights, no scores, and NO subjective branch.** This is the defining inheritance from Editor's §12 (which carved out zero judgment slots): Sound is a faithful executor, so the success-side is a pure conjunction with zero judgment surfaces.

```
AUDIO_READY = (editor_precondition_met)          # Check 1  — edl verdict == "edl_ready" ∧ output_type == "successEdl"
            ∧ (upstream_success)                  # Check 1  — no errorEnvelope branch consumed
            ∧ (edl_evidence_hash_verified)        # Check 3  — SHA-256 recomputes (EDL not tampered post-conform)
            ∧ (vo_track_resolved)                 # Check 3  — the asset_bundle.audio[] voice track resolves
            ∧ (music_bed_resolved)                # Check 3  — the music_event.asset_uri resolves against the bundle
            ∧ (all_markers_in_timeline)           # Check 4  — every SFX/duck/swell marker 0 ≤ at_ms ≤ total_timeline_ms
            ∧ (loudness_target_in_spec)           # Check 5  — target == platform const (−14 IG/TT · −16 YT); tp ≤ −1.0 dBTP
            ∧ (duration_in_band)                  # Check 9  — 45000 ≤ total_timeline_ms ≤ 75000 (re-assert from EDL)
            ∧ (spec_fidelity_edl_faithful)        # Check 9  — music event ∧ swell markers ∧ timeline duration ∧ VO byte-faithful match EDL
            ∧ (audio_firewall_clean)              # Check 8  — 11th-pass VO-transcript hits == 0
            ∧ (mode_blind)                        # Check 7  — production_mode_read == false
            ∧ (lineage_intact)                    # Check 10 — well-formed inbound 9-tuple + valid 10-tuple extension
```

### 12.2 Non-ready routing (the verdict function — TWO outcomes only)

Any single ∧-term false → the verdict function routes per the §6.3 / §3.2 map. **There is NO `revise` branch — every non-ready outcome is a halt or a fail.** This is the two-verdict model (D3):

```
# Halts (entry / forensic / construction gates)
if ¬editor_precondition_met    → halt  upstream_edl_not_ready
if ¬upstream_success           → halt  upstream_not_success
if ¬lineage_intact             → halt  audio_lineage_failure          (forensic)
if ¬mode_blind                 → halt  sound_agent_failed             (slot-11 — agent read production_mode)

# Fails (substance adjudications)
if ¬vo_track_resolved          → fail  vo_track_missing               (route_back: ingest-agent)
if ¬music_bed_resolved         → fail  audio_asset_unresolved         (route_back: ingest-agent)
if ¬all_markers_in_timeline    → fail  audio_marker_out_of_range      (route_back: editor-agent)
if ¬loudness_target_in_spec    → fail  loudness_target_out_of_spec    (forensic log + target named)
if ¬edl_evidence_hash_verified → fail  spec_fidelity_breach           (tampered EDL — route_back: editor-agent)
if ¬spec_fidelity_edl_faithful → fail  spec_fidelity_breach           (forensic log + deviating field named)
if ¬audio_firewall_clean       → fail  audio_firewall_breach          (forensic log + transcript field named)
```

**Precedence:** halts (entry/forensic/mode gates) adjudicate before fails; among fails, the FIRST failing check in §6.2 tier order names the headline `failure_code`, with all computed evidence still emitted (no short-circuit nulls — every sub-status explicitly dispositioned regardless of the headline). **There is no `revise` precedence rung — the verdict space is exactly `{audio_ready, fail}` with halts being a fail sub-class that does not route back for re-work.**

### 12.3 Properties (why this is the right math for a faithful executor)

1. **Fully deterministic** — same inputs, same verdict, every run, for EVERY term. There is no soft surface, no gradient, no judgment slot. The LLM is constructing + attesting, never judging. This is the strongest determinism posture in the fleet (Ingest/Editor-class, transplanted to the audio-executor seam).
2. **Monotone** — adding a defect can never improve the verdict. There is no compensatory scoring where a clean loudness target offsets a banned-token VO transcript or an out-of-range SFX marker.
3. **Zero-false-audio-ready by construction** — `audio_ready` requires EVERY term true; ambiguity biases to `fail` (Hard Rule #13). The 0% false-audio-ready target (§8.6) is a property of the composition, not a tuned threshold.
4. **NO judgment slot — inherited from Editor** — where Edit Director isolated exactly one `revise` branch for a soft brand-rule tension, Sound has ZERO (as Editor does). A `revise` here would mean second-guessing a locked cut — exactly the conform/finish override the boundary forbids (D3). Human deferral lives entirely in `human_review_required: true` + `finish_mode: "human_in_the_loop"` + `audio_processed: false` on EVERY emission (recommend-don't-process), not in a verdict branch.
5. **Auditable** — the emitted audio spec carries the evidence for every term (§10 per-check evidence rows), so any verdict is recomputable by a human from the audio spec alone. Recommend-don't-process depends on exactly this recomputability.

**Divergence from Edit Director's ∧-plus-revise (surfaced):** Edit Director's domain is partly creative — most deterministic but with ONE genuine judgment surface, so it carried `revise` exactly where QC Pre-flight carried `hold`. Sound's domain is **fully deterministic** (a marker is in range or it isn't; a loudness target is the platform const or it isn't; the VO transcript is byte-faithful or it isn't; the firewall is clean or it isn't) — so it carries NEITHER. Sound is `audio_ready | fail`, full stop — the same binary determinism Editor + Ingest hold, transplanted to the audio-executor seam. The judgment slot belongs upstream where the creativity is; the executor downstream is deterministic by design.

---

## §13 — Critical Decisions (Day 76 walk — 13 LOCKED-as-drafted · 2 carried open for operator)

Target was 10–14 LOCKED (outline §13). The Day 76 walk lands **13 LOCKED-as-drafted** (within target), with **2 carried open** — both operator-gated, both drafted to Donna's recommended default so the SPEC is buildable while the gates close. **Per the process-integrity attestation, Donna does NOT ratify PRELIMINARY/critical-decision items — D7 and D15 are surfaced, not advanced.** The 14-item outline scaffold maps below, with the Motion-handoff target (Open Question 4) added as D15.

| # | Decision | Status | Resolution |
|---|----------|--------|------------|
| D1 | Audio-spec-authoring vs DSP scope — v1.0 = **audio-conform-spec authoring ONLY**; actual mix/loudness DSP is human-in-the-loop at launch (Blueprint §9), automation Week 4–5 | **LOCKED-as-drafted Day 74** | Resolves outline Open Question 1 per recommendation: the audio spec is the buildable, highest-leverage, $0 slice; the DSP automation lands in the Week 4–5 window the Blueprint already scopes. `audio_processed: const false` is the honesty contract (the direct analog of Editor's `render_dispatched: const false`). |
| D2 | Faithful-executor, zero mix re-interpretation — Sound specs the EDL's audio order/events/timing faithfully; it never re-cuts the timeline, re-authors copy, or re-orders events | **LOCKED-as-drafted Day 74** | Hard Rule #2. Editor conformed the cut; Sound finishes the audio on it. A re-interpretation is an unauthorized override → `spec_fidelity_breach`. The conform/finish executor boundary. |
| D3 | **Two-verdict (NO `revise`)** — Sound is deterministic; the subjective slot lives upstream at Edit Director. `audio_ready \| fail` only | **LOCKED-as-drafted Day 74** | Resolves outline Open Question 2 per recommendation. Inherits Editor's two-verdict posture. A `revise` here would second-guess a locked cut — the conform/finish override the boundary forbids. §12 makes it structural; §8.7 tightens the false-fail ceiling to ≤5% as a consequence. Human deferral lives in `human_review_required: true`, not a verdict branch. |
| D4 | Mode-blind by inheritance — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested | **LOCKED-as-drafted Day 74** | The THIRD contractually mode-blind agent — the live, machine-checkable proof that Ingest's mode-convergence seam holds THREE stages deep (Edit Director → Editor → Sound). Check #7 + TC-01/TC-02 finish-convergence proof. |
| D5 | Editor precondition absolute — Sound runs only on a `successEdl`/`edl_ready` reel; else halts `upstream_edl_not_ready` | **LOCKED-as-drafted Day 74** | Sound never finishes an unlocked cut, and does NOT auto-resolve a failed EDL (the fix belongs upstream). Hard Rule #4. Check #1 runs FIRST. |
| D6 | Tier-FLAT behavior — all 4 tiers reach Sound; the EDL carries the tier envelope, Sound finishes it identically (no own tier scaling) | **LOCKED-as-drafted Day 74** | The same discipline as Editor + Ingest (unlike Edit Director, the only tier-SENSITIVE agent in the post tail). An audio finish is faithful or it isn't, regardless of tier; the richness (swell count, SFX accents) already lives in the EDL Sound receives. §10 tier-flatness matrix. |
| D7 | **10-tuple parent_chain** — inherits Editor 9-tuple + appends `audio_spec_id` (UUIDv7) | **QUINTUPLY-DEFERRED — operator-gated** | Held additively (`minItems: 5`, `prefixItems` 0–9, `maxItems: 10`, `items: false`) pending the Cross-SPEC §3.9 ratification AND the Editor 9-tuple LOCK AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it. `TODO@cross-spec-3.9-ratification` flip note embedded for the schema author. Sound is the FIFTH forcing function for the amendment. **NOT advanced tonight.** |
| D8 | errorEnvelope code count → **9 LOCKED + slot-11** | **RESOLVED Day 75 → LOCKED-as-drafted** | Settled within the 7–9 target. `vo_track_missing` and `audio_asset_unresolved` each kept SPLIT (the OPPOSITE of Editor folding all resolution to a single `asset_unresolved`) because the audio domain carries TWO distinct asset classes (voice track + music bed) whose recovery diagnostics differ even though both route to Ingest. Namespace-cardinality rationale at §6.3. |
| D9 | Self-QC check count → **11** | **RESOLVED Day 75 → LOCKED-as-drafted** | Within the 10–12 target; 4-tier ordering (entry / substance / forensic / construction). The 11th defense-in-depth firewall pass (audio-domain VO-transcript passthrough). |
| D10 | Spec-fidelity = ZERO tolerance — a deviated music event / swell marker / timeline duration, a byte-unfaithful VO transcript, or a failed `edl_evidence_hash` must NEVER survive to `audio_ready`; hash machine-verified | **LOCKED-as-drafted Day 74** | §12.3 makes it structural; §8.2 makes it measured (100% catch). A fidelity deviation → `spec_fidelity_breach` (fail), never `audio_ready`. The byte-faithful executor invariant. |
| D11 | Audio-domain firewall (11th pass) — Sound re-scans the passthrough VO transcript at the audio-finish layer, the last AUDIO checkpoint before Motion typography (NOT a new authorship surface) | **LOCKED-as-drafted Day 74** | The 11th firewall pass — a passthrough-integrity re-scan of the SPOKEN content the finish touches. Editor's 10th pass scanned committed caption/lower-third/end-card TEXT; Sound scans the VO TRANSCRIPT — a distinct surface Editor's pass does not cover. §6.5 list applied verbatim (11 entries). TC-05 is its existence proof (GATING). |
| D12 | No DSP, no engine, no decode — NO generative engine, NO audio DSP, NO waveform decode, NO LUFS measurement in v1.0; declared-transcript + platform-const loudness targets only; `audio_processed: const false`, `cost_incurred_usd ~$0` | **LOCKED-as-drafted Day 74** | Hard Rules #3/#12. Resolves outline Open Question 6 per recommendation (declared-transcript + platform-const targets ratified for v1.0; live LUFS measurement needs decode → v1.1). The forged-provenance framing ("an audio spec claiming a mix it never processed") is the defining negative constraint. Ties Ingest / QC Pre-flight / Edit Director / Editor for $0. |
| D13 | Recommend-don't-process — `human_review_required: true` + `finish_mode: "human_in_the_loop"` + `audio_processed: false` on every emission; verdict is an audio-spec RECOMMENDATION, never a ratified "processed" or "approved-for-Motion" state | **LOCKED-as-drafted Day 74** | Hard Rule #13. The operator (or the Week 4–5 automation) mixes; the agent never marks a reel processed. Lever-3 default. An `audio_ready` verdict means "ready for the human's finish-into-v2 decision," not "mixed." |
| D14 | Multi-loudness-master scope — v1.0 specs the primary −14 LUFS IG/TT master + echoes the `loudness_variants_planned` count; the −16 LUFS YT variant master deferred to v1.1 | **LOCKED-as-drafted Day 76** | Resolves outline Open Question 5 (loudness-variant portion) per recommendation: the −16 LUFS YT master is a derived re-conform, lower-leverage than the primary. Authoring-level scope-narrowing inside the pre-approved recommendation (Donna-resolvable, same class as Editor's D14 variant-fold). `variant_masters[]` reserved in the §10 field map. *(DAW-session-export portion of Open Question 5 also resolved-as-deferred: v1.0 emits the JSON audio spec + a human-readable mix cue-sheet view; native Pro Tools / Audition session export lands with the DSP automation, v1.1.)* |
| D15 | **Motion handoff target** — v1.0 emits the audio spec + v2-edit handle to the **Drive `/reels/[reel_id]/` conform queue (holding store)**; direct agent-to-agent handoff activates when Motion (Agent #12 candidate, position 13) LOCKs | **PRELIMINARY — drafted to recommended default · operator ratification pending** | Outline Open Question 4. Donna recommends the holding store: Motion does not exist yet, and an audio spec emitted into a void is an audit-trail break. `handoff_targets: ["motion-agent"]` names the LOGICAL target; the PHYSICAL v1.0 destination is the Drive conform queue (per Blueprint §7 I/O — mirrors the Editor→Drive-conform-queue and Edit Director→Notion-Edit-Plan holding-store decisions). **Operator may override on this walk's review.** Directly tied to Editor Day 69 Item 8 (D15-of-Editor = the Sound handoff target, which Sound's downstream Motion handoff now resolves jointly with). |

**Decision-walk integrity note:** D8/D9 were PRELIMINARY at Day 74, resolved by the Day 75 partial 1 authoring exactly as the outline's recommended defaults, and are LOCKED-as-drafted here; D14 is a Donna-resolvable scope-narrowing inside the pre-approved recommendation (same class as Editor's D14 variant-fold). D7 and D15 are *operator-only* (a Cross-SPEC amendment ratification + a quintuply-gated lineage flip; and a pipeline-topology commitment) and remain open. This is the same Donna-resolvable vs operator-only line the Editor Day 68, Edit Director Day 60, Ingest Day 52, and QC Pre-flight Day 43 walks drew.

---

## §15 — Change Log + Version History (LOCKED-as-drafted Day 76)

| Version tag | Day | Date | Event |
|-------------|-----|------|-------|
| v1.0-draft-day-74 | 74 | Thu Jul 2 | Outline §0–§5 SHIPPED (`ARS-2026-07-02-Day-74-Sound-Agent-SPEC-Outline.md`) — open questions parked |
| v1.0-draft-day-75 | 75 | Fri Jul 3 | Body partial 1: §6/§7/§10/§14 LOCKED-as-drafted; namespace settled 9+slot-11; self-QC settled 11; **2-verdict model with NO `revise` settled**; `vo_track_missing` + `audio_asset_unresolved` SPLIT by distinct recovery diagnostic (opposite of Editor's fold) |
| v1.0-draft-day-76 | 76 | Sat Jul 4 | **Body partial 2 (this document): §8/§9/§11/§12/§15/§16 LOCKED-as-drafted; §13 walk = 13 LOCKED + D7/D15 carried open. SPEC body §0–§16 COMPLETE.** False-fail ceiling tightened to ≤5% (deterministic-executor consequence of D3 — flagged for operator confirm at LOCK candidate). |
| v1.0-LOCK-CANDIDATE | 78+ | TBD | Assembly of the full SPEC + cross-SPEC §3 full audit + 15-decision walk staged for operator (hard-gated: 6 predecessor LOCKs + §3.9 ratification) |
| v1.0-schemas | TBD | TBD | `input.schema.json` + `output.schema.json` per §10 authoring notes (the 10-tuple additive hold + the 2-verdict enum + the SPLIT 9-code + slot-11 enum + brand/loudness `const`s) |
| v1.0-SKILL | TBD | TBD | `skills/sound-agent/` bundle + §9 fixtures at `tests/` |
| v1.0-runbook | TBD | TBD | LLM-test runbook (operator paste-and-run, 5 cases + the `audio_asset_unresolved`-music-bed + `spec_fidelity_breach`-swell + slot-11 adversarial probes) |
| v1.0-LOCKED | TBD | TBD | **Operator LOCK ceremony** — tag flip + Notion + chip (operator-only) |

**Parked candidates (v1.1+ register):** `variant_masters[]` −16 LUFS YT master activation (D14 v1.1 condition), live LUFS measurement + true-peak limiting (needs byte-level audio decode + a loudness meter), waveform-accurate sidechain ducking render (needs DSP), SFX-library synthesis / actual SFX render (Sound specs the placement; the app inserts the asset), `finish_target.v2_edit_uri` active-write (the Week 4–5 DSP automation), `audio_spec.daw_session_export` (Pro Tools / Audition session adapter), direct Motion handoff (D15 activation condition), live-telemetry re-baseline of §8 targets.

---

## §16 — Metadata Block Schema (LOCKED-as-drafted Day 76)

Cross-SPEC §3.9 canonical fields + **6 Sound additions**. Pattern source: Editor §16 / Edit Director §16 / Ingest §16 / QC Pre-flight §16. This is the binding contract for the schemas-day `metadata` object:

```
"metadata": {
  // ---- Cross-SPEC §3.9 canonical (inherited verbatim) ----
  "agent_id":            "sound-agent",                   // const
  "agent_version":       "1.0",                           // semver string
  "production_mode":     "A" | "B" | "C",                 // PRESENT for audit lineage; NOT read as a branch (Hard Rule #7)
  "brand_id":            "REINVENTED",                    // v1.0 expected value
  "parent_chain":        [ ... ],                         // see addition 1
  "cost_incurred_usd":   0.00,                            // ≈ $0 — conform reasoning + audio-spec authoring only
  "human_review_required": true,                          // const true (Hard Rule #13 — recommend-don't-process)
  "timestamp_utc":       "<ISO-8601>",

  // ---- Sound additions (6) ----
  "audio_spec_class":          "primary_master_-14lufs",  // 1. enum: ["primary_master_-14lufs"] v1.0 · "variant_master_-16lufs" reserved v1.1+
  "audio_spec_evidence_hash":  "<sha256-hex-64>",         // 2. SHA-256 over the audio_spec + audio_conform_check + spec_fidelity_check block (^[a-f0-9]{64}$)
  "audio_processed":           false,                     // 3. const false v1.0 (authors a spec, touches no waveform; the human mixes)
  "finish_mode":               "human_in_the_loop",       // 4. enum: ["human_in_the_loop"] v1.0 · "automated" reserved v1.1 Week 4–5
  "runtime_environment_class": "dev"|"staging"|"production", // 5. inherit AI Video Gen §16
  "audio_spec_id":             "<UUIDv7>"                 // 6. this agent's emitted identity (also parent_chain[9])
}
```

**Addition 1 — `parent_chain` (the quintuply-deferred 10-tuple):** `prefixItems` positions 0–9 = `[brief_id, script_id, storyboard_id, production_plan_id|rendered_shots_set_id, replication_set_id, preflight_report_id, asset_manifest_id, edit_plan_id, edl_id, audio_spec_id]` · `minItems: 5` · `maxItems: 10` · `items: false`. Accepts the 5-tuple (pre-ratification), the 6-tuple (QC Pre-flight extension pending its LOCK), the 7-tuple (Ingest extension pending its LOCK), the 8-tuple (Edit Director extension pending its LOCK), the 9-tuple (Editor extension pending its LOCK), and the 10-tuple (this agent's append). Rejects a 4-tuple. `TODO@cross-spec-3.9-ratification` flips `minItems` to 10 ONLY after all five gates close (D7). The schema author copies this constraint verbatim per §10.

**Mode-blind + finish-target self-attestation blocks (the §16 companions — NOT in `metadata` but in the success payload root):** `mode_blind_confirm: {production_mode_read: false (const), consumed: "mode_agnostic_edl" (const)}` and `finish_target: {audio_processed: false (const), finish_mode: "human_in_the_loop" (const), v2_edit_uri: "<reserved — written by the human finish>"}`. Encoded at the schema layer as the machine-checkable convergence + no-DSP guarantees (§10). This is the structural parallel to Editor's §16: Sound carries the SAME mode-blind attestation (the THIRD agent to do so — convergence three stages deep) PLUS the finish-target block that makes the no-DSP / human-in-the-loop posture machine-checkable at the audio-executor seam (the direct analog of Editor's `render_target` block — and v1.0 keeps `audio_processed` `false`).

**Schema-day cross-references:** `output_type` oneOf split (`successAudioSpec` | `errorEnvelope`), the 9-code + slot-11 `failure_code` enum (`vo_track_missing` + `audio_asset_unresolved` each SPLIT, NOT folded — per D8), the **`verdict` enum WITHOUT `revise` (`["audio_ready", "fail"]` — exactly two values, inherited from Editor; the executor is deterministic, the success-side has no judgment branch)**, the `ars://` URI pattern, `audio_spec.loudness_target.primary const "-14 LUFS (IG/TT)"` + `true_peak_ceiling_dbtp const -1.0`, `music_event.at_ms` + swell-marker timeline-bounds, `audio_processed const false`, `finish_mode const "human_in_the_loop"`, `mode_blind_confirm.production_mode_read const false`, and `audio_conform_check` + `spec_fidelity_check` sub-booleans all required-on-success — all per §10, restated here as the single checklist the schema author works from.

---

## Day 77+ runway (next forward deliverable)

**Day 77 (Sun Jul 5) = REST DAY — no build** (pre-stage the v1.0 LOCK-candidate scaffold only, per the Day 21/28/35/42/49/56/63/70 Rest Day-compounding pattern). **Next build deliverable: Sound Agent v1.0 LOCK CANDIDATE assembly (Day 78, Mon Jul 6)** — merge outline (Day 74) + partial 1 (Day 75) + partial 2 (this document) into the single LOCK-candidate document, run the FULL Cross-SPEC §3 audit (11 dimensions, LOCK-grade), final bipartite-coverage proof (11 checks × 9 codes + slot-11), the full verdict math, and stage the 15-decision §13 walk for the operator. Then schemas (Day 79+) → SKILL bundle → runbook → v1.0 LOCK per the §15 lifecycle. The LOCK itself remains hard-gated on the six predecessor ceremonies + the §3.9 ratification (all operator-pending — see partial 1 §14.4–14.7). The **Editor 9-tuple LOCK is the direct 10-tuple dependency**.

---

## Mirror status

- Source: `ars/ARS-2026-07-04-Day-76-Sound-Agent-SPEC-Body-Partial-2.md` (this document) + `ars/build-log-2026-07-04.md`
- Mirror destination: `/outputs/ars/` (both files)
- Mirror verification: in this session's mirror step.

---

## Process integrity (Day 76)

- ✅ **No LLM dispatched. No engine, no render, no audio DSP, no byte-decode, no LUFS measurement, no network, ZERO $ spent.** Validation was structural (pattern parity vs Editor Day 68 partial 2 + §12 composition audit + fixture-spec consistency + bipartite-coverage re-confirm), not a model run.
- ✅ **No operator-impersonation.** All SIX predecessor LOCK ceremonies (AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor) confirmed STILL-PENDING via on-disk file-state (version tags unflipped). D7 NOT ratified (10-tuple held additively at `minItems: 5`). D15 NOT ratified (drafted to recommended default, explicitly PRELIMINARY). No runbook executed, no version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.
- ✅ **No fake-advance.** §13 distinguishes Donna-resolvable settlements (D8/D9/D14 — inside pre-approved target ranges) from operator-only ratifications (D7/D15 — carried open). The partial is LOCKED-as-drafted, not LOCKED. The SPEC body is complete (§0–§16); the v1.0 LOCK is a future operator ceremony. The §8.7 false-fail tightening to ≤5% is surfaced as a flag-for-confirm, not silently committed over the partial-1 ≤8% preview.
- ✅ **All prior canon read-only.** Partial 1, outline, Blueprint, Cross-SPEC review, Brand-Voice Intake, all predecessor SPECs/schemas/SKILLs/runbooks — untouched.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. HC/NPOX tokens appear only as the §6.5 firewall BLOCK-list (referenced in the TC-05 fixture as the seeded-leak test surface, not restated as a cross-entity reference). REINVENTED = pilot brand inside fixtures per Cross-SPEC canon.
- ✅ **Rest Day honored.** Tonight is Saturday (Day 76, Pacific). Next Rest Day: Day 77 (Sun Jul 5) — LOCK-candidate scaffold pre-stage only, no SPEC content.
- ✅ **No scope expansion.** One forward deliverable (this partial 2) + build log + mirror + Notion status update + standing housekeeping + status-ping attempt. Nothing extra acted on.

---

*Day 76 ships clean ON the outline calendar. The Sound Agent v1.0 SPEC body is COMPLETE — §0–§16 all authored across the outline (Day 74), partial 1 (Day 75), and this partial 2 (Day 76). 13 of 15 critical decisions LOCKED-as-drafted; D7 (10-tuple — quintuply-gated) and D15 (Motion handoff — drafted to the Drive conform-queue holding-store default) remain operator-gated. Next forward deliverable: v1.0 LOCK CANDIDATE assembly (Day 78, after the Day 77 Rest Day). Sound is Agent #11 of 17 — the 11th defense-in-depth firewall (the AUDIO-domain VO-transcript passthrough re-scan, the last audio checkpoint before Motion), the second executor agent in the post tail, and the third contractually mode-blind agent (the continued proof that Ingest's mode-convergence seam holds three stages deep). This partial LOCKs the performance scoreboard (100% fidelity + 100% audio-firewall catch + 100% loudness-in-spec + 0% false-audio-ready + ≤5% false-fail — tightened from the partial-1 ≤8% preview as a consequence of two-verdict determinism), the 5-fixture portfolio (the mode-blind finish-convergence proof + the two principal route-backs + the GATING audio-firewall fixture + the SPLIT-code proof at TC-04), the zero-engine/zero-DSP cost model, the fully-deterministic verdict math (NO `revise` branch — the executor divergence inherited from Editor), and the metadata block schema (6 Sound additions incl. the finish-target self-attestation). Operator pickup unchanged: (1) the six predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight + Ingest + Edit Director + Editor — the Editor 9-tuple is the direct 10-tuple dependency); (2) execute the six pending runbooks (Day 27 / 36 / 47 / 57 / 65 / 73); (3) ratify the Cross-SPEC §3.9 n-tuple amendment (Sound is the fifth forcing function); (4) ratify D15 (Motion handoff target) on this walk; (5) confirm the §8.7 false-fail ≤5% tightening. Day 77 (Jul 5) = next Rest Day.*
