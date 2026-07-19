# Day 90 LLM Test Execution Runbook — Motion Agent v1.0

**Date authored:** 2026-07-18 (Sat · Day 90 · Wk13D6 · post-launch hardening window · v1.0 LOCK gate — DOUBLE-gated)
**Audience:** Jamila — single 20–35 min sit-down at the iMac (paste-and-run discipline). Runnable by Donna under the 2026-07-07 standing authorization once a live 5/5 exists AND the Sound LOCK has closed (see §7).
**Goal:** Run all 5 SKILL-bundle fixtures (+ 5 optional named adversarial probes) through Opus, validate each output against `schemas/output.schema.json`, and — **only after the Sound v1.0 LOCK closes first** — declare Motion Agent v1.0 **LOCKED** if 5/5 PASS. **Motion's LOCK is the fleet's first DOUBLE-gated LOCK:** predecessors #1–#10 already CLOSED at the Day 79 ceremony (240/240 reproducible `validate.py` evidence, $0), but **Sound #11 — Motion's DIRECT dependency — is still LOCK CANDIDATE, not LOCKED.** Motion reads Sound's `successAudioSpec` / `audio_ready` as its precondition gate and extends Sound's 10-tuple `parent_chain` to an 11-tuple. **The third executor in the post tail cannot finish the graphics on an unlocked audio spec.** So this runbook can be *authored* and *run 5/5* now, but Motion cannot LOCK until the Sound LOCK closes (the ONLY open link in the ten-deep LOCKED chain).
**Estimated cost:** **$0.00 engine spend** (Motion calls NO generative engine, renders NO graphics, composites NO frame, burns in NO text, decodes NO video frame — by design; Hard Rule #3; `motion_processed: const false`, `finish_mode: const "human_in_the_loop"`) · ~**$0.40–0.75** Opus inference per case × 5 (× 10 with all five probes) ≈ **≤ $3.75 (≤ $7.50 with every probe) total LLM token spend.** Motion authors a typography + motion-graphics finish spec over declared text and a declared v2-edit handle; it never composites, rasterizes, or renders a pixel in dry-run *or* live, so the two modes are functionally identical (deterministic transform over the declared EDL typography + the Sound-passed audio spec). Lighter than any authoring pass — Motion executes; it authors zero creative decisions.
**Pre-validated:** Both schemas META-SCHEMA VALID (Day 87). Full bundle `validate.py` **111/111 green** (meta-schema ×2 + 5 fixture input/output validations + adversarial guards + the two TYPE-SYSTEM brand encodings + the 2-verdict guards + the SPLIT/dual-route map + the 11-tuple additive-hold + input guards + the TC-01/TC-02 mode-blind finish-convergence proof [FOUR stages deep] + the TC-05 gating check) — re-confirmed Day 90 on `jsonschema` 4.26.0, and the **full fleet re-ran 434/434 (8 bundles, 0 drift)**. The §5 validator below extends that harness to score live LLM output against the 5 fixture expectations.
**Mode default:** **dry-run** (see §6). Because Motion dispatches no engine and renders no frame, "dry-run" and "live" are functionally identical — there is no engine surface, no compositing surface, and no frame-decode surface to vary. Dry-run is the v1.0 LOCK gate.
**Operator approval still required to begin:** the ten predecessor LOCKs CLOSED (satisfied — Day 79 ceremony; re-confirm the chips are still `live`), **the Sound v1.0 LOCK CLOSED** (the double-gate — NOT yet done; the immediate prior operator action), **plus** Motion Day 86 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.

---

## TL;DR (action sequence)

1. **Confirm the ten predecessor LOCK ceremonies are CLOSED and their dashboard chips still read `live`.** AI Video Gen (#5) · Style Replication (#6) · QC Pre-flight (#7) · Ingest (#8) · Edit Director (#9) · Editor (#10) + the four upstream (#1–#4) — all LOCKED Day 79 (240/240 `validate.py`, $0). If any chip has regressed off `live`, stop and surface it.
2. **Confirm the Sound v1.0 LOCK is CLOSED (the double-gate).** Sound (#11) is Motion's DIRECT dependency — the `audio_ready` / `successAudioSpec` precondition Motion reads + the 10-tuple this agent's 11-tuple extends. As of Day 90 Sound is **LOCK CANDIDATE** (its own 5/5 live run — ~$3.50 Opus — has not been executed under the $0 unattended ceiling). **Motion cannot LOCK until the Sound row reads LOCKED and its chip reads `live`.** If Sound is not LOCKED, this runbook may still be RUN for evidence, but the Motion LOCK is HELD.
3. **Confirm Motion Day 86 LOCK-CANDIDATE Items 6 + 8 + 11 are operator-ratified.** Item 6 = cost-model confirm (~$0 engine / $0 render / $0 compositing / $0 frame-decode; no vendor URLs, no ceilings — recommend RATIFY). Item 8 = the 15-decision walk (incl. D7 the 11-tuple + **D15 the full-QC handoff target** — `handoff_targets: ["qc-agent"]` with the Drive `/reels/[reel_id]/` finish-queue holding-store default until full QC LOCKs; needs an explicit verdict — recommend RATIFY D15 default + D7-as-drafted). Item 11 = Cross-SPEC §3.9 n-tuple amendment (RATIFIED Day 79) + §8.8 false-fail ≤5% confirm (recommend CONFIRM ≤5%).
4. **Optional:** Run `cd "~/ars/skills/motion-agent" && python3 validate.py` in a fresh Python process for the canonical 111/111 bundle stamp. ~25 sec. Not gated — confirmed green Day 89, re-confirmed Day 90 (requires `jsonschema` ≥ 4.18 for Draft 2020-12; the iMac carries 4.26).
5. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
6. **Model:** `claude-opus-4-8` (or `claude-opus-4-6` for cross-runbook comparability — note which; every prior fleet runbook baselined on opus-4-6). **Temperature:** `0.2`. **Max tokens:** `8000`. **Top-p:** default.
   *(Assumption stated: Motion runs COLD — same 0.2 as QC Pre-flight / Ingest / Edit Director / Editor / Sound, and the cold rationale is as strong as Sound's. Motion authors nothing: it FINISHES the typography + motion on a fixed EDL + a finished audio spec. The caption / lower-third / end-card text is Script/Editor passthrough byte-for-byte, the reveal cadence + motion tokens + end-card are brand consts, the timeline arithmetic is 30fps-grid. 0.2 minimizes evidence-field paraphrase variance and tightens the TC-01/TC-02 convergence proof without touching verdict logic. Operator may raise to 0.4 to match fleet default; verdicts are temperature-stable by construction — the §12 `const` gates PLUS the two TYPE-SYSTEM encodings make a false-`motion_ready` structurally impossible at any temperature.)*
7. **System prompt:** open `ars/skills/motion-agent/SKILL.md`, locate the fenced block under §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)", paste **everything inside the fence** (13 hard rules + Blueprint §4.12 target v3-final / motion-self-check shape inlined + the 9:16 / 1080×1920 / 30fps format header + the motion-token set [allowed slow_push_in/static_hold/subtle_parallax · banned whip_pan/shake/meme_transition/trending_transition · 120ms ease-in-out · zero_bounce] + the reveal cadence [one line at a time, ≤1 reveal / 8000ms] + the end-card const + universal-access/tier-FLAT table + 11-step finish loop + voice rule + "Emit JSON only. Now."). No edits. No additions.
8. For each of the 5 cases (then optionally the 5 probes):
    - Open `ars/skills/motion-agent/test-cases/case-NN-*/input.json`. Copy the **entire root object**.
    - User message = the JSON input object **only**. **No engine-stub fence** — Motion reads no engine surface and renders no frame; everything it finishes (the Sound `audio_spec` with `audio_ready` + the `finish_target.v2_edit_uri` + the `audio_spec_evidence_hash`, the EDL typography source [caption_events[] + lower_third_events[] + end_card_event + frame_rate + total_timeline_ms] + `edl_evidence_hash`, tier_richness_echo, mode_blind_confirm, parent_chain, qc_pre_flags) is already inside the input object. No prose, no markdown around the JSON.
    - Send. Capture the **raw JSON output only** (strip any accidental code fence — Hard Rule #1 forbids them, but verify). Save to `ars/skills/motion-agent/validation/llm-out/case-NN-output.json`.
    - Note token counts + wall-clock latency in the run-log (§8 template).
9. **Run validator** (single command, §5). Either **5/5 PASS + convergence proof OK + TC-05 gating OK → Motion v1.0 LOCK ceremony executable IF AND ONLY IF the Sound LOCK has closed** (subject to the three preconditions above), or capture failures for a patch session.

---

## §1 Pre-flight checklist (18 items)

- [ ] **AI Video Gen v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #5.
- [ ] **Style Replication v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #6.
- [ ] **QC Pre-flight v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #7.
- [ ] **Ingest v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #8.
- [ ] **Edit Director v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #9 (a route-back destination for `text_asset_unresolved` / marker / token / typography / fidelity defects — see TC-03).
- [ ] **Editor v1.0 LOCKED** (Day 79) · chip still `live`. Predecessor #10 (the typography-text route-back owner — the SPLIT-to-Editor leg).
- [ ] **Sound v1.0 LOCKED · chip `live`. DIRECT dependency #11 — THE DOUBLE-GATE.** The `audio_ready`/`successAudioSpec` precondition Motion reads + the 10-tuple this agent's 11-tuple extends + the `v2_edit_unresolved` SPLIT-to-Sound route-back owner (TC-04). **As of Day 90 this is the ONE open link — Sound is LOCK CANDIDATE, its own 5/5 live run not yet executed. If this box is unchecked, RUN the runbook for evidence but HOLD the Motion LOCK.**
- [ ] **Motion Day 86 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.** Item 6 = cost-model confirm ($0 engine / render / compositing / frame-decode; no vendor surface, no ceilings). Item 8 = 15-decision walk (D15 the full-QC handoff target `["qc-agent"]` + Drive holding-store default; D7 11-tuple SEXTUPLY-DEFERRED). Item 11 = Cross-SPEC §3.9 n-tuple amendment [RATIFIED Day 79] + §8.8 false-fail ≤5% confirm.
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key already configured.
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run. *(For Motion these are functionally identical — no engine, no render, no compositing in either.)*
- [ ] **All 5 fixtures present** at `ars/skills/motion-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:** `mkdir -p "~/ars/skills/motion-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 87 authored-as-drafted · re-verified Day 89/90 `validate.py` 111/111).
- [ ] **`input.schema.json` self-validates** ✓ (Day 87 · 5/5 fixtures green Day 89/90).
- [ ] **System-prompt + largest fixture footprint** = ~14 KB SKILL prompt + ~5 KB largest input ≈ **~19 KB context window.** Trivial vs Opus 200 K context.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support). *(The iMac carries 4.26 — the 111/111 stamp environment.)*
- [ ] **No raw vendor credentials anywhere on screen.** Motion references NO credentials (Hard Rule #3 — it calls no engine, renders no frame, composites nothing, decodes no video). If Opus emits a credential, composes a compositing graph / render command / keyframe-render / burn-in instruction, or emits a frame-decode instruction in any response, abort — the agent has misunderstood its job.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object**. |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"SYSTEM PROMPT — v1.0" fence — identical across all cases). |
| 3 | User message = `{input object}` only. **No fence, no stub, no prose.** Motion reads no engine and renders no frame; the input carries everything it finishes. |
| 4 | Set temperature `0.2`, max tokens `8000`. Hit **Run**. |
| 5 | Wait for completion. Verify the response is a **single JSON object** with no markdown fences (Hard Rule #1 — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check: `metadata.agent_id == "motion-agent"` AND `metadata.agent_version == "1.0"` AND `finish_target.motion_processed == false` AND `finish_target.finish_mode == "human_in_the_loop"` AND `mode_blind_confirm.production_mode_read == false` AND `human_review_required == true` (both branches). If not, halt — the agent is hallucinating identifiers, forging finish provenance, reading the mode, or breaking recommend-don't-render. |

---

## §3 The cases — expected branch + pass criteria

**The 5 fixtures exercise BOTH verdict values** (`motion_ready` ×2, `fail` ×3) and **3 of the 10 LOCKED error codes live** (`motion_marker_out_of_range`, `v2_edit_unresolved`, `motion_firewall_breach`). The remaining 7 codes (`upstream_audio_not_ready`, `upstream_not_success`, `text_asset_unresolved`, `motion_token_out_of_spec`, `typography_out_of_spec`, `spec_fidelity_breach`, `motion_lineage_failure`) + the slot-11 catch-all (`motion_agent_failed`) are bound to the schema via the Day 89 `validate.py` adversarial guards, not all re-exercised live (same discipline as Sound §3 / Editor §3 / Ingest §3). The optional named probes in §3.6 exercise five of them live as defense-in-depth — they are NOT part of the 5/5 LOCK count.

**Motion is the THIRD fleet agent (after Editor + Sound) to carry only TWO verdicts, `motion_ready | fail` — there is NO `revise`** (deliberate inheritance of Editor's + Sound's determinism; §3.1 / §6.4 / §12 / D3). Motion is a fully-deterministic executor: every check is binary (a handle resolves or it doesn't; a text field is non-empty or it isn't; a marker is in the timeline or it isn't; a token is in the allowed set or it isn't; two reveals are 8s apart or they collide; a lower-third is lowercase-sans or it's an all-caps screamer; the end-card is the brand const or it's a deviation; the text is byte-faithful or it's an override; the firewall is clean or it isn't). There is no subjective finish surface to hold to Lever-3 — that judgment call lives THREE stages upstream (Edit Director's `revise`). Human deferral still lives in `human_review_required: true` + `finish_mode: human_in_the_loop` + `motion_processed: false` on EVERY emission — it is just not a *verdict* branch. **The §5 validator REJECTS any `revise`, any `hold`, and any `reshoot`.**

### TC-01 — `case-01-mode-a-origin-pro-motion-ready` (Pro · Mode A origin · clean `motion_ready`)
- **Expected branch:** `successMotionSpec`. **Verdict:** `motion_ready`. **route:** n/a (success carries `handoff_targets: ["qc-agent"]`).
- **Hard checks:**
  - `output_type == "successMotionSpec"`, `verdict == "motion_ready"` (schema `const "motion_ready"` on this branch).
  - `motion_spec.reveal_cadence`: `one_line_at_a_time == true`, `max_reveals_per_8s == 1`, `brand_cadence == "reinvented_v3"`; no two `caption_reveals[].at_ms` closer than 8000ms.
  - `motion_spec.motion_tokens.applied[]` ⊆ {`slow_push_in`, `static_hold`, `subtle_parallax`} (banned tokens are ENUM-UNREPRESENTABLE — a violation cannot serialize); `ease == "120ms ease-in-out"`, `bounce_policy == "zero_bounce"`.
  - `motion_spec.lower_thirds[]`: every `style == "lowercase_sans_left_underline"`, `all_caps == false` (CONST-FALSE — an all-caps screamer cannot serialize).
  - `motion_spec.end_card`: `text == "REINVENTED - build on purpose."`, `font == "serif"`, `bg == "ivory"`, `hold_ms == 1500` (brand const).
  - `motion_conform_check`: `v2_edit_resolved == true`, `all_text_fields_resolved == true`, `all_markers_in_timeline == true`, `reveal_cadence_in_spec == true`, `motion_tokens_in_brand_set == true`, `duration_in_band == true` (total_timeline_ms in the 45–75s band).
  - `spec_fidelity_check`: all 6 true (`caption_text_byte_faithful`, `lower_third_text_byte_faithful`, `end_card_matches_brand_const`, `timeline_duration_matches_edl`, `audio_spec_evidence_hash_verified`, `edl_evidence_hash_verified`).
  - `motion_firewall_pass_12.status == "pass"`, `hits == 0`.
  - `mode_blind_confirm.production_mode_read == false`, `consumed == "mode_agnostic_v2_edit"`.
  - `finish_target.motion_processed == false`, `finish_mode == "human_in_the_loop"`.
  - every `caption_reveals[].at_ms`, `lower_thirds[].at_ms`, `end_card.at_ms`: `>= 0` AND `<= total_timeline_ms`; every `overlays[]`: `from_ms <= to_ms`, both in `[0, total_timeline_ms]`.
  - `tier_richness_echo.aspect_variants_specced == 1`, `primary_aspect == "9:16"`.
  - `human_review_required == true`, `cost_incurred_usd == 0.0` (≈0.00 to 2dp).
  - `metadata.parent_chain` = 11-tuple (10 inbound + appended `motion_spec_id`), held additively.

### TC-02 — `case-02-mode-c-enterprise-motion-ready` (Enterprise · Mode C origin · convergence twin · `motion_ready`)
- **Expected branch:** `successMotionSpec`. **Verdict:** `motion_ready`.
- **The mode-blind finish-convergence proof (FOUR stages deep — the deepest in the fleet).** Footage originated Mode C (`parent_chain[3] == "mode-c-direct"`), tier Enterprise — and Motion finishes it through the IDENTICAL executor logic, emitting a **byte-shape-identical** `motion_spec` / `motion_conform_check` / `spec_fidelity_check` / `motion_self_check` / `motion_firewall_pass_12` / `mode_blind_confirm` / `finish_target` block vs TC-01. Only audit-lineage fields differ (`production_mode`, `tier`, ids). This is the live proof that Ingest's mode-convergence seam holds FOUR stages deep (Edit Director → Editor → Sound → **Motion**) — **with Motion, the entire post-production tail is proven mode-agnostic end to end.**
- **Authoring note (surfaced, from the Day 89 bundle):** to keep the convergence proof a strict byte-equality (mirroring the LOCKED Sound Day-80 harness), TC-02 holds the typography set identical to TC-01 so the ONE variable under test is the origin mode; the §9 "richer Enterprise envelope" descriptor is honored via `tier_richness_echo.aspect_variants_planned: 2` while `aspect_variants_specced: 1` (v1.0 primary 9:16 master only). This isolates the mode variable and makes the proof a strict deep-equality — the stronger form.
- **Hard checks:** all TC-01 success checks PLUS `mode_blind_confirm.production_mode_read == false` (the machine-checkable proof) AND the §5 convergence assertion: the TC-01 vs TC-02 finished `motion_spec` shape (caption-reveal / reveal-cadence / lower-third / motion-token / overlay / end-card structure) + conform/fidelity/self-check/firewall blocks are byte-shape-identical across the two outputs.

### TC-03 — `case-03-caption-reveal-out-of-range-fail` (`fail` / `motion_marker_out_of_range`)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `motion_marker_out_of_range`**. **`failed_check_id`: 4**. **`route_back_to`: `editor-agent`**.
- A caption reveal (or overlay / lower-third / end-card marker) resolves at an `at_ms` past `edl.total_timeline_ms` (or negative) — a reveal placed off the end of the cut (Hard Rule #6). It is a timeline/EDL defect, so it routes back to Editor to re-conform, not to Sound.
- **Hard checks:** top-level `failure_code`/`failed_check_id`/`route_back_to` exact; `detail.violation` names the offending marker `at_ms` + the `total_timeline_ms` bound; `detail.affected_events` (or equivalent) names the over-range marker; `cost_incurred_usd == 0.0`; `mode_blind_confirm.production_mode_read == false`; `metadata.parent_chain` = 11-tuple (the append fires on fail too).

### TC-04 — `case-04-v2-edit-unresolved-fail` (`fail` / `v2_edit_unresolved` — the SPLIT-to-Sound code)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `v2_edit_unresolved`**. **`failed_check_id`: 3**. **`route_back_to`: `sound-agent`**.
- The `finish_target.v2_edit_uri` (the audio-final picture handle Sound passed) does not resolve — Motion cannot spec a graphics finish over a missing picture (Hard Rule #5).
- **Motion's defining SPLIT-code proof — the split routes to TWO DIFFERENT agents:** `v2_edit_unresolved` (the picture handle → **Sound**) and `text_asset_unresolved` (the typography text → **Editor**) are kept **SEPARATE** because the two input classes have two different owners (the picture comes from Sound; the text comes from Editor). This is even more strongly justified than Sound's split (which routed both halves to one agent, Ingest). This fixture exercises the picture-handle leg (→ Sound); the typography-text leg (`text_asset_unresolved` → Editor) is the §3.6 named probe + the schema-bound adversarial guard in `validate.py`.
- **Hard checks:** `failure_code == "v2_edit_unresolved"`, `route_back_to == "sound-agent"` (NOT editor); `detail` names the unresolvable v2-edit handle; the validator additionally asserts the output is NOT the Editor-routed `text_asset_unresolved` (SPLIT discipline — right leg, right owner).

### TC-05 — `case-05-typography-firewall-breach-fail` (`fail` / `motion_firewall_breach` — GATING)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `motion_firewall_breach`**. **`failed_check_id`: 8**. **`route_back_to`: `null`**.
- Banned-entity tokens have survived into the passthrough on-screen typography — `sln` in a `caption_events[].text` line AND `holdco group` in a `lower_third_events[].text` (HC/NPOX BLOCK-list, `hits: 2`). Motion authored no copy, but it is the agent that turns written text into PIXELS, so its 12th-pass typography-domain re-scan is the LAST visual-text net before the master reaches full QC (Hard Rule #8 / Check #8). **This is the highest-stakes code in the namespace: a leak here would be burned into the delivered picture of v3-final.mp4.** Routes to `null` — a self-contained gating halt (unlike Sound's audio breach, which routed to Editor; Motion's typography breach is the terminal visual-text checkpoint and holds for human review rather than auto-routing).
- **Hard checks:** `failure_code == "motion_firewall_breach"`, `failed_check_id == 8`, `route_back_to == null`; `detail.motion_firewall_pass_12` forensically names the two leaking typography fields with `hits: 2`, `status: "breach"`; `detail.leaking_fields` enumerates the caption + lower-third. **GATING fixture — a false-`motion_ready` here is an automatic runbook FAIL.**

### §3.6 Optional named adversarial probes (five — NOT part of the 5/5 count)
Per the Day 89 log close, the named live probes are defense-in-depth beyond the five fixtures. Each is optional; none count toward the 5/5 LOCK gate.

- **Probe A — the reveal-cadence collision.** Construct an input whose EDL places two caption events < 8000ms apart. **Expected:** `errorEnvelope`, `failure_code == "motion_token_out_of_spec"`, `route_back_to == "editor-agent"`, `detail` names the colliding reveal pair (the sub-8000ms gap). Probes the cadence-min enforcement (Step 5 / Hard Rule #8).
- **Probe B — the end-card text drift.** Feed an EDL `end_card_event.text` that deviates from the brand const (e.g. `"REINVENTED — build with purpose."`). **Expected:** `errorEnvelope`, `failure_code == "typography_out_of_spec"`, `route_back_to == "editor-agent"`, `detail` names the end-card deviation vs the const `"REINVENTED - build on purpose."`. Probes the end-card brand const (Step 7 / Hard Rule #9).
- **Probe C — the caption-text drift.** Feed an output-forcing case where a caption reveal is NOT byte-faithful to the EDL passthrough (a paraphrase / re-case / re-punctuation). **Expected:** `errorEnvelope`, `failure_code == "spec_fidelity_breach"`, `route_back_to == "editor-agent"`, `detail` names the non-byte-faithful caption. Probes the byte-faithful executor invariant (Step 9 / Hard Rule #10).
- **Probe D — the `text_asset_unresolved` → Editor SPLIT leg.** Construct an input with an empty / missing `caption_events[].text` (or lower-third / end-card) string. **Expected:** `errorEnvelope`, `failure_code == "text_asset_unresolved"`, `route_back_to == "editor-agent"` — the OPPOSITE-owner leg of TC-04's picture-handle split. Probes that the split routes text defects to Editor (not Sound). This is the highest-value probe: it completes the SPLIT-to-two-agents proof live.
- **Probe E — the dual-hash-tamper.** Tamper ONE byte of the inbound `audio_spec_evidence_hash` OR the `edl_evidence_hash`. **Expected:** `errorEnvelope`, `failure_code == "spec_fidelity_breach"`, `route_back_to == "editor-agent"`, `metadata.self_qc_attempts` per finish-loop step 11; `detail` names which of the TWO hashes failed to recompute. Probes Motion's distinction as the **first agent to verify TWO upstream evidence hashes** (Step 3 / Hard Rule #12 — the byte-faithful executor invariant, doubled).

*(A slot-11 `motion_agent_failed` / route-null / attempts-2 catch-all probe is also available as an optional sixth probe — a degenerate input that survives to a second self-QC failure — but is fully schema-bound in `validate.py` and not required live.)*

---

## §4 Output-schema validation contract (both branches)

Every saved `case-NN-output.json` must validate against `schemas/output.schema.json` (Draft 2020-12). The schema is a `oneOf(successMotionSpec, errorEnvelope)` discriminated on `output_type`.

**successMotionSpec branch (TC-01, TC-02)** must carry: `output_type: "successMotionSpec"`, `verdict: const "motion_ready"`, `reel_ref`, `motion_spec` (`caption_reveals[]` with byte-faithful `text` + `ease "ease_in_out_120ms"`; `reveal_cadence` `one_line_at_a_time: const true` + `max_reveals_per_8s: const 1`; `lower_thirds[]` `style` const + `all_caps: const false`; `motion_tokens.applied[]` ENUM-restricted to the allowed set + `bounce_policy: const "zero_bounce"`; `overlays[]`; `end_card` brand const `text`/`font`/`bg`/`hold_ms 1500`), `motion_conform_check` (all-true const gates), `spec_fidelity_check` (6-true const), `motion_self_check` (Blueprint §4.12 — `voice_markers_in_captions`, `truth_echoes`, `banned_vocab_hits: const 0`, `motion_tokens_applied: const true`), `motion_firewall_pass_12` (`status: const "pass"`, `hits: const 0`), `mode_blind_confirm` (`production_mode_read: const false`, `consumed: const "mode_agnostic_v2_edit"`), `finish_target` (`motion_processed: const false`, `finish_mode: const "human_in_the_loop"`, `v3_final_uri` reserved), `tier_richness_echo` (`aspect_variants_specced: const 1`, `primary_aspect: const "9:16"`), `metadata`, `handoff_targets: ["qc-agent"]`, `human_review_required: const true`.

**errorEnvelope branch (TC-03/04/05, probes)** must carry: `output_type: "errorEnvelope"`, `verdict: const "fail"`, top-level `failure_code` (enum of the 10 + slot-11), `failed_check_id` (int), `route_back_to` (per the code→route map, or `null`), `reel_ref`, `cost_incurred_usd`, `mode_blind_confirm`, `metadata` (11-tuple `parent_chain` — the append fires on fail too), `human_review_required: const true`, `detail` (`violation` + `recovery_path` + the code-specific forensic block).

**Code → route map (must match exactly) — Motion's defining divergence is the SPLIT to TWO different agents:**

| Verdict / code | `route_back_to` |
|----------------|-----------------|
| `v2_edit_unresolved` (the v2-edit picture handle — SPLIT → Sound) | `sound-agent` |
| `text_asset_unresolved` (the typography text — SPLIT → Editor) · `motion_marker_out_of_range` · `motion_token_out_of_spec` · `typography_out_of_spec` · `spec_fidelity_breach` | `editor-agent` |
| `upstream_audio_not_ready` · `upstream_not_success` · `motion_firewall_breach` · `motion_lineage_failure` · `motion_agent_failed` (slot-11) | `null` |

**Zero false-`motion_ready` (the defining target):** the success branch pins every §12 ∧-of-gates HARD term as a `const` invariant (firewall `status pass` + `hits: 0`, `motion_conform_check` all-true, `spec_fidelity_check` 6-true, `motion_self_check.banned_vocab_hits: 0`, the reveal-cadence + end-card + lower-third-style consts, `motion_processed: false`, `finish_mode: human_in_the_loop`, `production_mode_read: false`, `aspect_variants_specced: 1`) **AND** two invariants pinned in the TYPE SYSTEM (the banned motion tokens are `enum`-excluded on `motion_tokens.applied[]`; the all-caps lower-third is `all_caps: const false`) — so a violating spec **cannot even serialize**. A false-`motion_ready` is **structurally impossible** — the schema rejects it before the validator scores it. **False-fail target ≤5%** (Editor/Sound-class deterministic-executor floor; §8.8, operator-confirm Item 11).

---

## §5 The validator (single command)

After all 5 outputs are saved to `validation/llm-out/case-NN-output.json`, run:

```bash
cd "~/ars/skills/motion-agent" && python3 validate_llm_run.py
```

`validate_llm_run.py` (author it once into the bundle root, alongside `validate.py`) does, per case:

1. **Schema-validate** the saved output against `schemas/output.schema.json` (Draft 2020-12). Any schema error = case FAIL.
2. **Branch match:** `output_type` matches the expected branch (TC-01/02 `successMotionSpec`; TC-03/04/05 `errorEnvelope`).
3. **Verdict match:** `verdict` equals the expected value; **REJECT `revise`, `hold`, `reshoot` on BOTH branches** (the two-verdict guard — Motion's inherited-from-Editor/Sound divergence, carried one stage deeper).
4. **fail-case triplet:** for TC-03/04/05, `failure_code` + `failed_check_id` + `route_back_to` all equal the fixture `expected_output.json` (esp. TC-04 route = `sound-agent` AND code = `v2_edit_unresolved` NOT the Editor-routed `text_asset_unresolved`; TC-03 route = `editor-agent`, check 4; TC-05 route = `null`, check 8, `hits: 2`).
5. **Success const gates:** for TC-01/02, assert firewall `status == "pass"` + `hits == 0`, `motion_conform_check` all-true, `spec_fidelity_check` 6-true, `motion_self_check.banned_vocab_hits == 0` + `motion_tokens_applied == true`, `motion_tokens.applied[]` ⊆ the allowed set (no banned token), every `lower_thirds[].all_caps == false` + `style` const, `end_card` == the brand const (text/font/bg/hold_ms 1500), reveal cadence `max_reveals_per_8s == 1` + no two reveals < 8000ms apart, every marker in `[0, total_timeline_ms]` (overlays `from_ms <= to_ms`), `motion_processed == false`, `finish_mode == "human_in_the_loop"`, `production_mode_read == false`, `aspect_variants_specced == 1` + `primary_aspect == "9:16"`, `human_review_required == true`, `handoff_targets == ["qc-agent"]`.
6. **Convergence proof (TC-01 vs TC-02):** assert the finished `motion_spec` shape (caption-reveal count + per-reveal structure / reveal-cadence / lower-third count + structure / motion-token set / overlay count + structure / end-card) + the conform/fidelity/self-check/firewall blocks are byte-shape-identical across the two outputs, and BOTH attest `production_mode_read == false`. This is the machine-checkable proof that Motion's mode-blindness holds FOUR stages deep past Ingest's convergence seam — the entire post tail proven mode-agnostic end to end.
7. **TC-05 gating:** assert the injected `sln` token (in a passthrough caption) AND `holdco group` (in a passthrough lower-third) are present in the INPUT and the output verdict is `motion_firewall_breach` with `hits: 2`, `status: "breach"`, route `null`. A false-`motion_ready` on TC-05 is an automatic runbook FAIL.

**Output:** `5/5 PASS` (+ convergence OK + TC-05 gating OK) → Motion v1.0 LOCK ceremony executable **IF AND ONLY IF the Sound LOCK has closed first** (subject to the three preconditions in §7). Any case FAIL → capture into a patch session; do NOT LOCK.

*(Note: `validate.py` is the bundle's structural harness — 111/111 on the fixtures. `validate_llm_run.py` is the thin LLM-output scorer this runbook adds; it reuses the same schema + the fixture `expected_output.json` files as the answer key. Both are $0, offline, no engine/render/compositing/frame-decode/network/LLM.)*

---

## §6 Mode note + the SEXTUPLY-deferred 11-tuple `parent_chain`

**Dry-run vs live are identical for Motion.** Motion dispatches no engine and renders no frame in EITHER mode (Hard Rule #3). There is no engine surface, no compositing surface, and no frame-decode surface to vary. "Dry-run" is the label; the behavior is the only behavior Motion has. Dry-run is the v1.0 LOCK gate.

**The 11-tuple `parent_chain` is SEXTUPLY-DEFERRED (D7) — do NOT advance it in this runbook.** The schema holds additively (`minItems: 5`, `prefixItems` 0–10, `maxItems: 11`, `items: false`). Motion's SKILL emits the 11th position (its appended `motion_spec_id`), and the fixtures carry a full 11-tuple, but the schema ACCEPTS a 5/6/7/8/9/10-tuple inbound canon through the 11-tuple append. The `minItems` flip to 11 (exact-11 cardinality) is UNBLOCKED — the Cross-SPEC §3.9 amendment RATIFIED at the Day 79 ceremony, and the Sound 10-tuple + Editor 9-tuple + Edit Director 8-tuple + Ingest 7-tuple + QC Pre-flight 6-tuple all in the additive hold — but it is **deliberately deferred as a separate, individually re-validated hardening migration** (both Motion schemas + the bundle copy carry the `TODO@exact-n-hardening-migration` flip note; a premature flip would false-reject the current fixtures, authored under the additive `minItems:5` floor). Motion is the **SIXTH forcing function** for the amendment. Passing this runbook 5/5 does NOT flip the cardinality. **This is the one item Donna will NOT auto-advance.** Schedule it as its own validated migration once the Sound LOCK closes — not folded into an agent LOCK.

**§8.8 false-fail ≤5% confirm (Item 11 bundle):** Motion inherits Editor's + Sound's ≤5% false-fail ceiling (a consequence of D3's two-verdict determinism — there is no `revise` judgment surface to absorb a looser band). Operator confirms ≤5% at the LOCK ceremony. Recommendation: CONFIRM ≤5%.

---

## §7 LOCK decision gate — DOUBLE-gated

Motion Agent v1.0 LOCKs **if and only if ALL** of the following are true:

1. The ten predecessor v1.0 LOCKs (#1–#10) are CLOSED and their chips read `live` (closed Day 79, 240/240, $0). **Precondition, satisfied — re-confirm the chips only.**
2. **The Sound v1.0 LOCK is CLOSED and its chip reads `live` (the DOUBLE-GATE).** Sound is Motion's direct dependency (the `audio_ready` precondition + the 10-tuple this agent's 11-tuple extends + the `v2_edit_unresolved`-routed owner). **As of Day 90 this is NOT satisfied — Sound is LOCK CANDIDATE, its own 5/5 live run (~$3.50 Opus) not yet executed. This is the ONLY open link in the ten-deep LOCKED chain, and it must close BEFORE the Motion LOCK.**
3. Motion Day 86 LOCK-CANDIDATE Items 6 + 8 + 11 ratified (cost-model · 15-decision walk incl. D15 full-QC handoff · §3.9 amendment [already ratified] + ≤5% confirm). *(All three are Motion-local and ratifiable in advance of the Sound LOCK.)*
4. This runbook: **5/5 fixtures PASS** + convergence proof OK + TC-05 gating OK, on a **real, reproducible** run.

If all four hold, execute the LOCK ceremony: flip the Notion ARS-hub Motion row to LOCKED, flip the dashboard chip to `live`, tag the SKILL bundle v1.0 LOCKED, ratify the as-drafted Motion reviewer Items 6/8/11.

**Standing-authorization note (2026-07-07, re-confirmed 2026-07-09).** Jamila has authorized Donna to run this runbook and execute the Motion LOCK herself once (a) the Sound LOCK has closed AND (b) this runbook validates 5/5 on real reproducible evidence (the same posture as the Day 79 ceremony, which LOCKED #1–#10 on 240/240 reproducible `validate.py` evidence, $0). **What that does NOT permit:** a LOCK without a real 5/5 behind it, and a LOCK ahead of the Sound LOCK. The 5/5 is the live paste-and-run of the 5 fixtures through Opus (§1–§5) — a live inference pass that costs ~$3.75 in LLM tokens. **The unattended overnight build runs under an absolute $0 ceiling** (no LLM dispatch, no vendor spend), so the overnight session **authors** this runbook but does **NOT** execute the live 5/5 and does **NOT** LOCK Motion — locking on the structural `validate.py` stamp alone, the same night the runbook is authored, would be a fake-advance against guardrail "no LOCK without a real 5/5 run behind it." The Motion LOCK is therefore a downstream operator/attended-spend action, sequenced AFTER the Sound LOCK. Until then Motion stays **LOCK CANDIDATE**.

---

## §8 Run-log template (fill during the sit-down)

```
MOTION v1.0 — DAY 90 LLM TEST RUN
Date/time (PT):        ____________________
Operator:              Jamila  (or Donna, attended + spend-authorized)
Mode:                  dry-run  |  live      (default dry-run — identical for Motion)
Model id:              claude-opus-4-8  (or 4-6 for comparability — note which)
Temperature:           0.2   Max tokens: 8000

Preconditions (must ALL hold before a 5/5 counts toward the LOCK):
  [ ] Predecessors #1–#10 v1.0 LOCKED · chips live
  [ ] Sound v1.0 LOCKED · chip live        <-- THE DOUBLE-GATE (Day 90: NOT yet — LOCK CANDIDATE)
  [ ] Motion Day 86 Items 6 / 8 / 11 ratified

Per case:
  TC-01  in-tok ____ out-tok ____ sec ____  verdict motion_ready  PASS/FAIL ____
  TC-02  in-tok ____ out-tok ____ sec ____  verdict motion_ready  PASS/FAIL ____   convergence w/TC-01: OK/NO ____
  TC-03  in-tok ____ out-tok ____ sec ____  fail/motion_marker_out_of_range  chk 4  route editor  PASS/FAIL ____
  TC-04  in-tok ____ out-tok ____ sec ____  fail/v2_edit_unresolved  chk 3  route sound (SPLIT)  PASS/FAIL ____
  TC-05  in-tok ____ out-tok ____ sec ____  fail/motion_firewall_breach  chk 8  route null  hits 2  PASS/FAIL ____  (GATING)

Optional named probes (not in 5/5 count):
  Probe A (reveal-cadence collision)   -> motion_token_out_of_spec / route editor    PASS/FAIL ____
  Probe B (end-card text drift)        -> typography_out_of_spec / route editor       PASS/FAIL ____
  Probe C (caption-text drift)         -> spec_fidelity_breach / route editor         PASS/FAIL ____
  Probe D (text_asset_unresolved SPLIT)-> text_asset_unresolved / route editor        PASS/FAIL ____
  Probe E (dual-hash-tamper)           -> spec_fidelity_breach / route editor         PASS/FAIL ____

Validator result:      __ / 5 PASS   convergence: OK/NO   TC-05 gating: OK/NO
LLM spend (est):        $ ______   Engine/render/compositing/frame-decode spend: $0.00 (structural)
Sound LOCK closed?:     YES / NO   (if NO — Motion LOCK is HELD regardless of 5/5)
LOCK decision:         LOCKED  |  HELD (reason: ____________________)
```

---

## §9 Guardrails (process-integrity — restate before running)

- **$0 engine, $0 render, $0 compositing, $0 frame-decode.** Motion calls no generative engine, renders no frame, composites no graphic, burns in no text, decodes no video frame. The only spend is Opus inference on the test cases. If any output composes a compositing graph / render command / keyframe-render / caption-burn-in / frame-decode instruction, abort the case — the agent misunderstood its job.
- **No operator impersonation by the overnight session.** Donna AUTHORED this runbook; the overnight $0 session does NOT execute it. The live paste-and-run + the LOCK ceremony require inference spend and/or attended execution — see §7. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED by the overnight build.
- **The Motion LOCK is DOUBLE-gated.** The ten predecessor LOCKs are satisfied (Day 79, 240/240, $0), but the Sound LOCK is NOT — it is the ONLY open link. Motion cannot LOCK ahead of Sound (its direct dependency). Even a clean 5/5 HOLDS the Motion LOCK until the Sound row reads LOCKED and its chip reads `live`.
- **The 11-tuple stays additive.** Passing 5/5 does not flip `minItems` to 11. That flip is a separately re-validated hardening migration (the §3.9 amendment is ratified, so it is unblocked but deliberately deferred), scheduled once the Sound LOCK closes.
- **Entity firewall.** ARS = Sequel Digital. `brand_id` = REINVENTED (pilot). The 11-entry HC/NPOX block-list is the firewall's catch-list, not a cross-entity reference. TC-05 is the live proof the 12th (typography-domain) pass catches a leak in the on-screen caption + lower-third — the moment the written word becomes pixels — before the master is delivered.

---

*Authored 2026-07-18 (Pacific) by Donna (overnight ARS Day 90 build session). Sequel Digital entity scope. This is the Motion Agent #12 v1.0 LLM Test Runbook — the forward deliverable per the Day 89 log close (§"What's unlocked") + the established cadence (LOCK candidate Day 86 → schema pair Day 87 → SKILL bundle Day 89 → LLM test runbook Day 90 → LOCK next), shipped one deliverable this night. It is the paste-and-run operator test suite (5 fixtures + 5 optional named adversarial probes) that gates Motion's eventual v1.0 LOCK. Motion is the THIRD fleet agent to carry only two verdicts (`motion_ready | fail`, NO `revise`, inheriting Editor's + Sound's determinism), the THIRD executor in the post tail and the FINAL finisher before full QC, the 12th defense-in-depth firewall (the typography-domain on-screen-text re-scan — the LAST visual-text checkpoint before a master ships), and the FOURTH contractually mode-blind agent (the TC-01/TC-02 finish-convergence proof that Ingest's mode-convergence seam holds FOUR stages deep — with Motion, the entire post-production tail is proven mode-agnostic end to end). Motion's DIRECT dependency is Sound (the `audio_ready`/`successAudioSpec` precondition + the 10-tuple the 11-tuple extends) — **which is still LOCK CANDIDATE, making the Motion LOCK the fleet's first DOUBLE-gated LOCK.** The Motion LOCK requires (a) the Sound LOCK closing first (a real 5/5 live run, ≈$3.50 Opus) AND (b) this runbook running 5/5 (≈$3.75 Opus); the $0 unattended overnight session authors this runbook but executes NEITHER live run and LOCKS nothing. Both are downstream operator/attended-spend actions, sequenced Sound-LOCK-then-Motion-LOCK, per the standing authorization. The 11-tuple `parent_chain` stays SEXTUPLY-deferred (held additively at `minItems 5`) — Motion is the sixth forcing function for the (already-ratified) Cross-SPEC §3.9 amendment; the exact-N flip is a separate hardening migration, NOT advanced this run. Next forward deliverables after this: the Sound v1.0 LOCK, then the Motion v1.0 LOCK (both on real 5/5 runs), then full QC #13 SPEC outline. Fleet validators re-ran 434/434 (8 bundles, 0 drift) this session. Next Rest Day: Day 91 (Sun Jul 19) — observed; next build Day 92 (Mon Jul 20).*
