# Day 81 LLM Test Execution Runbook — Sound Agent v1.0

**Date authored:** 2026-07-09 (Thu · Day 81 · Wk12D4 · post-launch hardening window · v1.0 LOCK gate)
**Audience:** Jamila — single 20–35 min sit-down at the iMac (paste-and-run discipline). Runnable by Donna under the 2026-07-07 standing authorization once a live 5/5 exists (see §7).
**Goal:** Run all 5 SKILL-bundle fixtures (+ 2 optional adversarial probes: a bare `fail`/`errorEnvelope` upstream EDL, and a slot-11 `sound_agent_failed`) through Opus, validate each output against `schemas/output.schema.json`, and declare Sound Agent v1.0 **LOCKED** if 5/5 PASS. **The six predecessor LOCKs (#1–#10) already CLOSED at the Day 79 ceremony** (AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → Editor, 240/240 reproducible `validate.py` evidence, $0). So — unlike the Editor Day 73 runbook, which hard-gated on five *open* predecessor LOCKs — Sound's predecessor chain is a satisfied precondition, not an open gate. **Editor is the DIRECT dependency:** Sound reads its `edl.json` (`edl_ready` / `successEdl`) as a precondition gate and extends its 9-tuple `parent_chain` to a 10-tuple. The second *executor* in the post tail cannot finish an unlocked cut.
**Estimated cost:** **$0.00 engine spend** (Sound calls NO generative engine, processes NO waveform, decodes NO audio, measures NO LUFS — by design; Hard Rule #3; `audio_processed: const false`, `finish_mode: const "human_in_the_loop"`) · ~**$0.35–0.70** Opus inference per case × 5 (× 7 with both probes) ≈ **≤ $3.50 (≤ $4.90 with both probes) total LLM token spend.** Sound authors an audio finish spec over declared assets; it never mixes, levels, ducks, or normalizes a waveform in dry-run *or* live, so the two modes are functionally identical (deterministic transform over the declared EDL + resolved audio bundle). Lighter than any authoring pass — Sound executes; it authors zero creative decisions.
**Pre-validated:** Both schemas META-SCHEMA VALID (Day 79). Full bundle `validate.py` **83/83 green** (meta-schema ×2 + 5 fixture input/output validations + adversarial guards + 5 two-verdict guards + SPLIT/fold routing + the 10-tuple additive-hold + input guards + the TC-01/TC-02 mode-blind finish-convergence proof [three stages deep] + the TC-05 gating check) — re-confirmed Day 81 on `jsonschema` 4.26.0 (the iMac stamp of record). The §5 validator below extends that harness to score live LLM output against the 5 fixture expectations.
**Mode default:** **dry-run** (see §6). Because Sound dispatches no engine and processes no audio, "dry-run" and "live" are functionally identical — there is no engine surface, no DSP surface, and no LUFS-measurement surface to vary. Dry-run is the v1.0 LOCK gate.
**Operator approval still required to begin:** the six predecessor LOCKs CLOSED (satisfied — Day 79 ceremony; re-confirm the chips are still `live`), **plus** Sound Day 78 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.

---

## TL;DR (action sequence)

1. **Confirm the six predecessor LOCK ceremonies are CLOSED and their dashboard chips still read `live`.** AI Video Gen (#5) · Style Replication (#6) · QC Pre-flight (#7) · Ingest (#8) · Edit Director (#9) · Editor (#10) — all LOCKED Day 79 (240/240 `validate.py`, $0). **Editor (#10) is Sound's DIRECT dependency** (the `edl_ready`/`successEdl` precondition + the 9-tuple this agent's 10-tuple extends). If any chip has regressed off `live`, stop and surface it.
2. **Confirm Sound Day 78 LOCK-CANDIDATE Items 6 + 8 + 11 are operator-ratified.** Item 6 = cost-model confirm (~$0 engine / $0 DSP / $0 decode / $0 LUFS-measurement; no vendor URLs, no ceilings — recommend RATIFY). Item 8 = the 15-decision walk (incl. D7 10-tuple + D15 Motion→Drive conform-queue holding-store handoff PRELIMINARY — recommend RATIFY D15 default + D7-as-drafted). Item 11 = Cross-SPEC §3.9 n-tuple amendment (RATIFIED Day 79) + §8.7 false-fail ≤5% confirm (recommend CONFIRM ≤5%).
3. **Optional:** Run `cd "~/ars/skills/sound-agent" && python3 validate.py` in a fresh Python process for the canonical 83/83 bundle stamp. ~20 sec. Not gated — confirmed green Day 80, re-confirmed Day 81 (requires `jsonschema` ≥ 4.18 for Draft 2020-12; the iMac carries 4.26).
4. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
5. **Model:** `claude-opus-4-8` (or `claude-opus-4-6` for cross-runbook comparability — note which; every prior fleet runbook baselined on opus-4-6). **Temperature:** `0.2`. **Max tokens:** `8000`. **Top-p:** default.
   *(Assumption stated: Sound runs COLD — same 0.2 as QC Pre-flight / Ingest / Edit Director / Editor, and the cold rationale is as strong as Editor's. Sound authors nothing: it FINISHES the audio on a fixed EDL. The music event + swell markers are the EDL's byte-for-byte, the VO transcript is Script/Editor passthrough, the loudness target is the platform const, the timeline arithmetic is 30fps-grid. 0.2 minimizes evidence-field paraphrase variance and tightens the TC-01/TC-02 convergence proof without touching verdict logic. Operator may raise to 0.4 to match fleet default; verdicts are temperature-stable by construction — the §12 `const` gates make a false-`audio_ready` structurally impossible at any temperature.)*
6. **System prompt:** open `ars/skills/sound-agent/SKILL.md`, locate the fenced block under §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)", paste **everything inside the fence** (13 hard rules + Blueprint §4.11 target audio-spec shape inlined + the 9:16/1080×1920/30fps format header + loudness targets −14 LUFS IG-TT / −16 LUFS YT + universal-access/tier-FLAT table + 11-step finish loop + voice rule + "Emit JSON only. Now."). No edits. No additions.
7. For each of the 5 cases (then optionally the 2 probes):
    - Open `ars/skills/sound-agent/test-cases/case-NN-*/input.json`. Copy the **entire root object**.
    - User message = the JSON input object **only**. **No engine-stub fence** — Sound reads no engine surface and processes no audio; everything it finishes (the Editor `edl` with events + music_event + music_swell_map + total_timeline_ms, the resolved Ingest `asset_bundle.audio[]` voice track + `music_bed`, tier_richness_echo, mode_blind_confirm, edl_evidence_hash, parent_chain, qc_pre_flags) is already inside the input object. No prose, no markdown around the JSON.
    - Send. Capture the **raw JSON output only** (strip any accidental code fence — Hard Rule #1 forbids them, but verify). Save to `ars/skills/sound-agent/validation/llm-out/case-NN-output.json`.
    - Note token counts + wall-clock latency in the run-log (§8 template).
8. **Run validator** (single command, §5). Either **5/5 PASS + convergence proof OK + TC-05 gating OK → Sound v1.0 LOCK ceremony executable** (subject to the two preconditions above), or capture failures for a Day 82 patch session.

---

## §1 Pre-flight checklist (16 items)

- [ ] **AI Video Gen v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #5.
- [ ] **Style Replication v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #6.
- [ ] **QC Pre-flight v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #7.
- [ ] **Ingest v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #8 (a SPLIT route-back destination — see TC-04).
- [ ] **Edit Director v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #9 (a route-back destination for `spec_fidelity_breach` deviations).
- [ ] **Editor v1.0 LOCKED** (Day 79) · chip still `live`. **DIRECT dependency #10** — the `edl_ready`/`successEdl` precondition Sound reads + the 9-tuple this agent's 10-tuple extends. (All six predecessor LOCKs already closed at the Day 79 ceremony on 240/240 reproducible evidence; this runbook re-confirms the chips, it does not re-open the gates.)
- [ ] **Sound Day 78 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.** Item 6 = cost-model confirm ($0 engine / DSP / decode / LUFS-measurement; no vendor surface, no ceilings). Item 8 = 15-decision walk (D15 Motion→Drive conform-queue holding-store default; D7 10-tuple QUINTUPLY-DEFERRED). Item 11 = Cross-SPEC §3.9 n-tuple amendment [RATIFIED Day 79] + §8.7 false-fail ≤5% confirm.
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key already configured.
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run. *(For Sound these are functionally identical — no engine, no DSP in either.)*
- [ ] **All 5 fixtures present** at `ars/skills/sound-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:** `mkdir -p "~/ars/skills/sound-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 79 authored-as-drafted · re-verified Day 80/81 `validate.py` 83/83).
- [ ] **`input.schema.json` self-validates** ✓ (Day 79 · 5/5 fixtures green Day 80/81).
- [ ] **System-prompt + largest fixture footprint** = ~12 KB SKILL prompt + ~4 KB largest input ≈ **~16 KB context window.** Trivial vs Opus 200 K context.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support). *(The iMac carries 4.26 — the 83/83 stamp environment.)*
- [ ] **No raw vendor credentials anywhere on screen.** Sound references NO credentials (Hard Rule #3 — it calls no engine, processes no audio, decodes no waveform, measures no LUFS). If Opus emits a credential, composes a DSP chain / mix render / normalization command, or emits a LUFS-measurement instruction in any response, abort — the agent has misunderstood its job.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object**. |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"SYSTEM PROMPT — v1.0" fence — identical across all cases). |
| 3 | User message = `{input object}` only. **No fence, no stub, no prose.** Sound reads no engine and processes no audio; the input carries everything it finishes. |
| 4 | Set temperature `0.2`, max tokens `8000`. Hit **Run**. |
| 5 | Wait for completion. Verify the response is a **single JSON object** with no markdown fences (Hard Rule #1 — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check: `metadata.agent_id == "sound-agent"` AND `metadata.agent_version == "1.0"` AND `finish_target.audio_processed == false` AND `finish_target.finish_mode == "human_in_the_loop"` AND `mode_blind_confirm.production_mode_read == false` AND `human_review_required == true` (both branches). If not, halt — the agent is hallucinating identifiers, forging finish provenance, reading the mode, or breaking recommend-don't-process. |

---

## §3 The cases — expected branch + pass criteria

**The 5 fixtures exercise BOTH verdict values** (`audio_ready` ×2, `fail` ×3) and **3 of the 9 LOCKED error codes live** (`audio_marker_out_of_range`, `vo_track_missing`, `audio_firewall_breach`). The remaining 6 codes (`upstream_edl_not_ready`, `upstream_not_success`, `audio_asset_unresolved`, `loudness_target_out_of_spec`, `spec_fidelity_breach`, `audio_lineage_failure`) + the slot-11 catch-all (`sound_agent_failed`) are bound to the schema via the Day 80 `validate.py` adversarial guards, not all re-exercised live (same discipline as Editor §3 / Edit Director §3 / Ingest §3). The optional probes in §3.6 / §3.7 exercise the upstream-halt precondition and the slot-11 catch-all live as defense-in-depth — they are NOT part of the 5/5 LOCK count.

**Sound is the SECOND fleet agent (after Editor) to carry only TWO verdicts, `audio_ready | fail` — there is NO `revise`** (deliberate inheritance of Editor's determinism; §3.1 / §6.4 / §12 / D3). Sound is a fully-deterministic executor: every check is binary (an asset resolves or it doesn't; a marker is in the timeline or it isn't; the loudness target is the platform const or it isn't; the VO transcript is byte-faithful or it isn't; the firewall is clean or it isn't). There is no subjective finish surface to hold to Lever-3 — that judgment call lives upstream (Edit Director's `revise`). Human deferral still lives in `human_review_required: true` + `finish_mode: human_in_the_loop` + `audio_processed: false` on EVERY emission — it is just not a *verdict* branch. **The §5 validator REJECTS any `revise`, any `hold`, and any `reshoot`.**

### TC-01 — `case-01-mode-a-origin-pro-audio-ready` (Pro · Mode A origin · clean `audio_ready`)
- **Expected branch:** `successAudioSpec`. **Verdict:** `audio_ready`. **route:** n/a (success carries `handoff_targets: [motion-agent]`).
- **Hard checks:**
  - `output_type == "successAudioSpec"`, `verdict == "audio_ready"` (schema `const "audio_ready"` on this branch).
  - `audio_spec.loudness_target.primary == "-14 LUFS (IG/TT)"`, `audio_spec.loudness_target.true_peak_ceiling_dbtp == -1.0` (platform const).
  - `audio_conform_check`: `vo_track_resolved == true`, `music_bed_resolved == true`, `all_markers_in_timeline == true`, `loudness_target_in_spec == true`, `duration_in_band == true` (total_timeline_ms in the 45–75s band).
  - `spec_fidelity_check`: all 5 true (`music_event_matches_edl`, `swell_markers_match_edl`, `timeline_duration_matches_edl`, `vo_transcript_byte_faithful`, `edl_evidence_hash_verified`).
  - `audio_firewall_pass_11.status == "pass"`, `hits == 0`.
  - `mode_blind_confirm.production_mode_read == false`, `consumed == "mode_agnostic_edl"`.
  - `finish_target.audio_processed == false`, `finish_mode == "human_in_the_loop"`.
  - every `audio_spec.duck_envelope[]` and `audio_spec.sfx_accents[]` marker: `at_ms >= 0` AND `<= total_timeline_ms`; each SFX accent maps to an EDL swell marker (not invented).
  - `tier_richness_echo.loudness_variants_specced == 1`, `primary_target == "-14 LUFS (IG/TT)"`.
  - `human_review_required == true`, `cost_incurred_usd == 0.0` (≈0.00 to 2dp).
  - `metadata.parent_chain` = 10-tuple (9 inbound + appended `audio_spec_id`), held additively.

### TC-02 — `case-02-mode-c-enterprise-audio-ready` (Enterprise · Mode C origin · convergence twin · `audio_ready`)
- **Expected branch:** `successAudioSpec`. **Verdict:** `audio_ready`.
- **The mode-blind finish-convergence proof (THREE stages deep).** Footage originated Mode C (`parent_chain[3] == "mode-c-direct"`), tier Enterprise — and Sound finishes it through the IDENTICAL executor logic, emitting a **byte-shape-identical** `audio_spec` / `audio_conform_check` / `spec_fidelity_check` / `audio_firewall_pass_11` / `mode_blind_confirm` / `finish_target` block vs TC-01. Only audit-lineage fields differ (`production_mode`, `tier`, ids). This is the live proof that Ingest's mode-convergence seam holds three stages deep (Edit Director → Editor → **Sound**).
- **Hard checks:** all TC-01 success checks PLUS `mode_blind_confirm.production_mode_read == false` (the machine-checkable proof) AND the §5 convergence assertion: the TC-01 vs TC-02 finished `audio_spec` shape (loudness / VO-polish / music-bed / duck-envelope / SFX-accent structure) + conform/fidelity/firewall blocks are byte-shape-identical across the two outputs.

### TC-03 — `case-03-audio-marker-out-of-range-fail` (`fail` / `audio_marker_out_of_range`)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `audio_marker_out_of_range`**. **`failed_check_id`: 4**. **`route_back_to`: `editor-agent`**.
- An SFX/duck marker resolves at an `at_ms` past `edl.total_timeline_ms` (or negative) — an accent placed off the end of the cut (Hard Rule #6). It is a timeline/EDL defect, so it routes back to Editor to re-conform, not to Ingest.
- **Hard checks:** top-level `failure_code`/`failed_check_id`/`route_back_to` exact; `detail.violation` names the offending marker `at_ms` + the `total_timeline_ms` bound; `detail.affected_events` names the over-range marker; `cost_incurred_usd == 0.0`; `mode_blind_confirm.production_mode_read == false`.

### TC-04 — `case-04-vo-track-missing-fail` (`fail` / `vo_track_missing` — the SPLIT code)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `vo_track_missing`**. **`failed_check_id`: 3**. **`route_back_to`: `ingest-agent`**.
- The `asset_bundle.audio[]` voice track does not resolve — Sound cannot spec a VO polish pass over a missing track (Hard Rule #5).
- **The SPLIT-code proof:** `vo_track_missing` (the VO voice track) and `audio_asset_unresolved` (the music bed) are kept as **SEPARATE** codes — the deliberate OPPOSITE of Editor folding all resolution into one `asset_unresolved` (D8) — because a missing voice track and an unresolvable music bed demand different operator recovery actions. Both route to Ingest, but they are distinct codes. This fixture exercises the VO-track leg; the music-bed leg (`audio_asset_unresolved`) is the schema-bound adversarial guard in `validate.py`.
- **Hard checks:** `failure_code == "vo_track_missing"`, `route_back_to == "ingest-agent"` (NOT editor); `detail` names the unresolvable voice-track handle; the validator additionally asserts the output is NOT the folded `audio_asset_unresolved` (SPLIT discipline).

### TC-05 — `case-05-audio-firewall-breach-fail` (`fail` / `audio_firewall_breach` — GATING)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `audio_firewall_breach`**. **`failed_check_id`: 8**. **`route_back_to`: `editor-agent`**.
- A banned-entity token (`sln cuts`) has survived into a passthrough `vo_transcript[].text` line — the SPOKEN copy Script authored and Editor committed. Sound authored no copy, but it is the agent that FINISHES the spoken audio, so its 11th-pass audio-domain firewall re-scan is the last net before the mix reaches Motion typography (Hard Rule #8 / Check #8). **This is the highest-stakes code in the namespace: a leak here would be mastered into the finished audio of v2.mp4.** Routes to Editor (the committer owns the copy fix).
- **Hard checks:** `failure_code == "audio_firewall_breach"`, `failed_check_id == 8`, `route_back_to == "editor-agent"`; `detail` forensically names the leaking `vo_transcript` field + the `hits: 1` firewall result. **GATING fixture — a false-`audio_ready` here is an automatic runbook FAIL.**

### §3.6 Optional probe A — upstream EDL not `edl_ready` → halt `upstream_edl_not_ready` / `upstream_not_success`
- **Not part of the 5/5 count.** Construct an input whose `edl.json` carries `verdict: "fail"` / `output_type: "errorEnvelope"` (a failed upstream cut), OR a `successEdl` object whose `verdict != "edl_ready"`.
- **Expected:** `errorEnvelope`, `failure_code == "upstream_edl_not_ready"` (verdict-mismatch case) or `"upstream_not_success"` (consumed errorEnvelope case), `route_back_to == null`. Sound does NOT finish an unlocked cut and does NOT auto-resolve a failed EDL (the fix belongs upstream — Hard Rule #4 / finish-loop step 1). This probes that Sound's precondition gate is a hard halt, not a schema reject (the input is a well-formed object; the halt is runtime).

### §3.7 Optional probe B — slot-11 catch-all → `sound_agent_failed`
- **Not part of the 5/5 count.** Feed a degenerate input that survives to a second self-QC failure (e.g. an internally inconsistent spec that cannot finish cleanly and cannot be cleanly routed by a specific code).
- **Expected:** `errorEnvelope`, `failure_code == "sound_agent_failed"`, `route_back_to == null`, `metadata.self_qc_attempts == 2`. Exercises the slot-11 catch-all + the route-null halt (finish-loop step 11).

---

## §4 Output-schema validation contract (both branches)

Every saved `case-NN-output.json` must validate against `schemas/output.schema.json` (Draft 2020-12). The schema is a `oneOf(successAudioSpec, errorEnvelope)` discriminated on `output_type`.

**successAudioSpec branch (TC-01, TC-02)** must carry: `output_type: "successAudioSpec"`, `verdict: const "audio_ready"`, `reel_ref`, `audio_spec` (`loudness_target.primary` const `"-14 LUFS (IG/TT)"` + `true_peak_ceiling_dbtp` const `-1.0`; `vo_polish`; `music_bed` with `asset_uri` `ars://` pattern + `at_ms`; `duck_envelope[]`; `sfx_accents[]`), `audio_conform_check` (all-true const gates), `spec_fidelity_check` (5-true const), `audio_firewall_pass_11` (`status: const "pass"`, `hits: const 0`), `mode_blind_confirm` (`production_mode_read: const false`, `consumed: const "mode_agnostic_edl"`), `finish_target` (`audio_processed: const false`, `finish_mode: const "human_in_the_loop"`, `v2_edit_uri` reserved), `tier_richness_echo` (`loudness_variants_specced: const 1`), `metadata`, `handoff_targets: [motion-agent]`, `human_review_required: const true`.

**errorEnvelope branch (TC-03/04/05, probes)** must carry: `output_type: "errorEnvelope"`, `verdict: const "fail"`, top-level `failure_code` (enum of the 9 + slot-11), `failed_check_id` (int), `route_back_to` (per the code→route map, or `null`), `reel_ref`, `cost_incurred_usd`, `mode_blind_confirm`, `metadata`, `human_review_required: const true`, `detail` (`violation` + `affected_events` + `recovery_path`).

**Code → route map (must match exactly):**

| Verdict / code | `route_back_to` |
|----------------|-----------------|
| `vo_track_missing` (the VO voice track — SPLIT) · `audio_asset_unresolved` (the music bed — SPLIT) | `ingest-agent` |
| `audio_marker_out_of_range` · `loudness_target_out_of_spec` · `spec_fidelity_breach` · `audio_firewall_breach` | `editor-agent` |
| `upstream_edl_not_ready` · `upstream_not_success` · `audio_lineage_failure` · `sound_agent_failed` (slot-11) | `null` |

**Zero false-`audio_ready` (the defining target):** the success branch pins every §12 ∧-of-gates HARD term as a `const` invariant (firewall `status pass` + `hits: 0`, `audio_conform_check` all-true, `spec_fidelity_check` 5-true, `loudness_target.primary` + `true_peak_ceiling_dbtp -1.0`, `audio_processed: false`, `finish_mode: human_in_the_loop`, `production_mode_read: false`, `loudness_variants_specced: 1`). A false-`audio_ready` is **structurally impossible** — the schema rejects it before the validator scores it. **False-fail target ≤5%** (Editor-class deterministic-executor floor; §8.7, operator-confirm Item 11).

---

## §5 The validator (single command)

After all 5 outputs are saved to `validation/llm-out/case-NN-output.json`, run:

```bash
cd "~/ars/skills/sound-agent" && python3 validate_llm_run.py
```

`validate_llm_run.py` (author it once into the bundle root, alongside `validate.py`) does, per case:

1. **Schema-validate** the saved output against `schemas/output.schema.json` (Draft 2020-12). Any schema error = case FAIL.
2. **Branch match:** `output_type` matches the expected branch (TC-01/02 `successAudioSpec`; TC-03/04/05 `errorEnvelope`).
3. **Verdict match:** `verdict` equals the expected value; **REJECT `revise`, `hold`, `reshoot` on BOTH branches** (the two-verdict guard — Sound's inherited-from-Editor divergence).
4. **fail-case triplet:** for TC-03/04/05, `failure_code` + `failed_check_id` + `route_back_to` all equal the fixture `expected_output.json` (esp. TC-04 route = `ingest-agent` AND code = `vo_track_missing` NOT the folded `audio_asset_unresolved`; TC-03/05 route = `editor-agent`).
5. **Success const gates:** for TC-01/02, assert firewall `status == "pass"` + `hits == 0`, `audio_conform_check` all-true, `spec_fidelity_check` 5-true, `loudness_target.primary == "-14 LUFS (IG/TT)"` + `true_peak_ceiling_dbtp == -1.0`, every `duck_envelope`/`sfx_accents` marker in `[0, total_timeline_ms]`, `audio_processed == false`, `finish_mode == "human_in_the_loop"`, `production_mode_read == false`, `loudness_variants_specced == 1`, `human_review_required == true`, `handoff_targets == ["motion-agent"]`.
6. **Convergence proof (TC-01 vs TC-02):** assert the finished `audio_spec` shape (loudness / VO-polish / music-bed / duck-envelope count + per-marker structure / SFX-accent count + structure) + the conform/fidelity/firewall blocks are byte-shape-identical across the two outputs, and BOTH attest `production_mode_read == false`. This is the machine-checkable proof that Sound's mode-blindness holds three stages deep past Ingest's convergence seam.
7. **TC-05 gating:** assert the injected `sln cuts` token is present in a passthrough `vo_transcript[].text` of the INPUT and the output verdict is `audio_firewall_breach` with `hits: 1`, route `editor-agent`. A false-`audio_ready` on TC-05 is an automatic runbook FAIL.

**Output:** `5/5 PASS` (+ convergence OK + TC-05 gating OK) → Sound v1.0 LOCK ceremony executable (subject to the two preconditions in §7). Any case FAIL → capture into a Day 82 patch session; do NOT LOCK.

*(Note: `validate.py` is the bundle's structural harness — 83/83 on the fixtures. `validate_llm_run.py` is the thin LLM-output scorer this runbook adds; it reuses the same schema + the fixture `expected_output.json` files as the answer key. Both are $0, offline, no engine/DSP/decode/LUFS/network/LLM.)*

---

## §6 Mode note + the QUINTUPLY-deferred 10-tuple `parent_chain`

**Dry-run vs live are identical for Sound.** Sound dispatches no engine and processes no audio in EITHER mode (Hard Rule #3). There is no engine surface, no DSP surface, and no LUFS-measurement surface to vary. "Dry-run" is the label; the behavior is the only behavior Sound has. Dry-run is the v1.0 LOCK gate.

**The 10-tuple `parent_chain` is QUINTUPLY-DEFERRED (D7) — do NOT advance it in this runbook.** The schema holds additively (`minItems: 5`, `prefixItems` 0–9, `maxItems: 10`, `items: false`). Sound's SKILL emits the 10th position (its appended `audio_spec_id`), and the fixtures carry a full 10-tuple, but the schema ACCEPTS a 5/6/7/8/9-tuple inbound canon through the 10-tuple append. The `minItems` flip to 10 (exact-10 cardinality) is now UNBLOCKED — the Cross-SPEC §3.9 amendment RATIFIED at the Day 79 ceremony, and the Editor 9-tuple + Edit Director 8-tuple + Ingest 7-tuple + QC Pre-flight 6-tuple all LOCKED — but it is **deliberately deferred as a separate, individually re-validated hardening migration** (the current fixtures were authored under the additive `minItems:5` floor; a premature flip would false-reject them). Sound is the **FIFTH forcing function** for the amendment. Passing this runbook 5/5 does NOT flip the cardinality. **This is the one item Donna will NOT auto-advance.**

**§8.7 false-fail ≤5% confirm (Item 11 bundle):** Sound inherits Editor's ≤5% false-fail ceiling (a consequence of D3's two-verdict determinism — there is no `revise` judgment surface to absorb a looser band). Operator confirms ≤5% at the LOCK ceremony. Recommendation: CONFIRM ≤5%.

---

## §7 LOCK decision gate

Sound Agent v1.0 LOCKs **if and only if ALL** of the following are true:

1. The six predecessor v1.0 LOCKs are CLOSED and their chips read `live` (AI Video Gen · Style Replication · QC Pre-flight · Ingest · Edit Director · Editor — all closed Day 79; Editor is the direct dependency). **Precondition, satisfied — re-confirm the chips only.**
2. Sound Day 78 LOCK-CANDIDATE Items 6 + 8 + 11 ratified (cost-model · 15-decision walk · §3.9 amendment [already ratified] + ≤5% confirm).
3. This runbook: **5/5 fixtures PASS** + convergence proof OK + TC-05 gating OK, on a **real, reproducible** run.

If all three hold, execute the LOCK ceremony: flip the Notion ARS-hub Sound row to LOCKED, flip the dashboard chip to `live`, tag the SKILL bundle v1.0 LOCKED, ratify the as-drafted Sound reviewer Items 6/8/11.

**Standing-authorization note (2026-07-07, re-confirmed 2026-07-09).** Jamila has authorized Donna to run this runbook and execute the Sound LOCK herself once it validates 5/5 on real reproducible evidence (the same posture as the Day 79 ceremony, which LOCKED #1–#10 on 240/240 reproducible `validate.py` evidence, $0). **What that does NOT permit:** a LOCK without a real 5/5 behind it. The 5/5 is the live paste-and-run of the 5 fixtures through Opus (§1–§5) — a live inference pass that costs ~$3.50 in LLM tokens. **The unattended overnight build runs under an absolute $0 ceiling** (no LLM dispatch, no vendor spend), so the overnight session **authors** this runbook but does **NOT** execute the live 5/5 and does **NOT** LOCK Sound — locking on the structural `validate.py` stamp alone, the same night the runbook is authored, would be a fake-advance against guardrail "no LOCK without a real 5/5 run behind it." The Sound LOCK is therefore the immediate next step, executable (a) by Jamila in the ~20–35 min iMac sit-down, or (b) by Donna in an attended, spend-authorized session once the live 5/5 is captured. Until then Sound stays **LOCK CANDIDATE**.

---

## §8 Run-log template (fill during the sit-down)

```
SOUND v1.0 — DAY 81 LLM TEST RUN
Date/time (PT):        ____________________
Operator:              Jamila  (or Donna, attended + spend-authorized)
Mode:                  dry-run  |  live      (default dry-run — identical for Sound)
Model id:              claude-opus-4-8  (or 4-6 for comparability — note which)
Temperature:           0.2   Max tokens: 8000

Preconditions (must ALL hold before scoring counts toward LOCK):
  [ ] AI Video Gen v1.0 LOCKED · chip live
  [ ] Style Replication v1.0 LOCKED · chip live
  [ ] QC Pre-flight v1.0 LOCKED · chip live
  [ ] Ingest v1.0 LOCKED · chip live
  [ ] Edit Director v1.0 LOCKED · chip live
  [ ] Editor v1.0 LOCKED · chip live   (direct dependency)
  [ ] Sound Day 78 Items 6 / 8 / 11 ratified

Per case:
  TC-01  in-tok ____ out-tok ____ sec ____  verdict audio_ready  PASS/FAIL ____
  TC-02  in-tok ____ out-tok ____ sec ____  verdict audio_ready  PASS/FAIL ____   convergence w/TC-01: OK/NO ____
  TC-03  in-tok ____ out-tok ____ sec ____  fail/audio_marker_out_of_range  route editor  PASS/FAIL ____
  TC-04  in-tok ____ out-tok ____ sec ____  fail/vo_track_missing  route ingest (SPLIT)  PASS/FAIL ____
  TC-05  in-tok ____ out-tok ____ sec ____  fail/audio_firewall_breach  route editor  PASS/FAIL ____  (GATING)

Optional probes (not in 5/5 count):
  Probe A (upstream EDL not edl_ready)  → upstream_edl_not_ready / route null   PASS/FAIL ____
  Probe B (slot-11)                     → sound_agent_failed / route null / attempts 2   PASS/FAIL ____

Validator result:      __ / 5 PASS   convergence: OK/NO   TC-05 gating: OK/NO
LLM spend (est):        $ ______   Engine/DSP/decode/LUFS spend: $0.00 (structural)
LOCK decision:         LOCKED  |  HELD (reason: ____________________)
```

---

## §9 Guardrails (process-integrity — restate before running)

- **$0 engine, $0 DSP, $0 decode, $0 LUFS-measurement.** Sound calls no generative engine, processes no audio, decodes no waveform, measures no loudness. The only spend is Opus inference on the test cases. If any output composes a DSP chain / mix render / normalization command / LUFS-measurement instruction, abort the case — the agent misunderstood its job.
- **No operator impersonation by the overnight session.** Donna AUTHORED this runbook; the overnight $0 session does NOT execute it. The live paste-and-run + the LOCK ceremony require inference spend and/or attended execution — see §7. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED by the overnight build.
- **The predecessor LOCKs are satisfied, not open.** The six predecessor LOCKs closed at the Day 79 ceremony (240/240, $0). This runbook re-confirms the chips; it does not re-open or re-run those gates. Sound cannot LOCK ahead of Editor (its direct dependency), which is already LOCKED — so that ordering constraint is met.
- **The 10-tuple stays additive.** Passing 5/5 does not flip `minItems` to 10. That flip is a separately re-validated hardening migration (the §3.9 amendment is ratified, so it is unblocked but deliberately deferred).
- **Entity firewall.** ARS = Sequel Digital. `brand_id` = REINVENTED (pilot). The 11-entry HC/NPOX block-list is the firewall's catch-list, not a cross-entity reference. TC-05 is the live proof the 11th (audio-domain) pass catches a leak in the spoken VO transcript before the mix is mastered.

---

*Authored 2026-07-09 (Pacific) by Donna (overnight ARS Day 81 build session). Sequel Digital entity scope. This is the Sound Agent #11 v1.0 LLM Test Runbook — the forward deliverable per the Day 80 log close (§"What's unlocked") + the established cadence (LOCK candidate Day 78 → schema pair Day 79 → SKILL bundle Day 80 → LLM test runbook Day 81 → LOCK next), shipped ON schedule, one deliverable this night. It is the paste-and-run operator test suite (5 fixtures + 2 optional adversarial probes) that gates Sound's eventual v1.0 LOCK. Sound is the SECOND fleet agent to carry only two verdicts (`audio_ready | fail`, NO `revise`, inheriting Editor's determinism), the SECOND executor in the post tail, the 11th defense-in-depth firewall (the audio-domain VO-transcript re-scan), and the THIRD contractually mode-blind agent (the TC-01/TC-02 finish-convergence proof that Ingest's mode-convergence seam holds THREE stages deep). Sound's DIRECT dependency is Editor (the `edl_ready`/`successEdl` precondition + the 9-tuple the 10-tuple extends) — already LOCKED Day 79, so the predecessor chain is a satisfied precondition, not an open gate. The Sound LOCK requires a real 5/5 live run (≈$3.50 Opus); the $0 unattended overnight session authors this runbook but does NOT execute the live run and does NOT LOCK — that is the immediate next step, runnable by Jamila in a ~20–35 min sit-down or by Donna in an attended spend-authorized session, per the standing authorization. The 10-tuple `parent_chain` stays QUINTUPLY-deferred (held additively at `minItems 5`) — Sound is the fifth forcing function for the (already-ratified) Cross-SPEC §3.9 amendment; the exact-N flip is a separate hardening migration, NOT advanced this run. Next forward deliverable after this: the Sound v1.0 LOCK (Day 82, on a real 5/5), then Motion #12 SPEC outline. Next Rest Day: Day 84 (Sun Jul 12).*
