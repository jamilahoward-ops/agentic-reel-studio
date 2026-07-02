# Day 73 LLM Test Execution Runbook — Editor Agent v1.0

**Date authored:** 2026-07-01 (Wed · Day 73 · Wk11D3 · post-launch hardening window · v1.0 LOCK gate)
**Audience:** Jamila — single 20–35 min sit-down at the iMac (paste-and-run discipline).
**Goal:** Run all 5 SKILL-bundle fixtures (+ 2 optional adversarial probes: a bare `revise` plan WITHOUT Lever-3 sign-off, and a slot-11 `editor_agent_failed`) through Opus, validate each output against `schemas/output.schema.json`, declare Editor Agent v1.0 **LOCKED** if 5/5 PASS — IF AND ONLY IF the five predecessor LOCK ceremonies (AI Video Gen v1.0 → Style Replication v1.0 → QC Pre-flight v1.0 → Ingest v1.0 → Edit Director v1.0) close first, in dependency order. **Edit Director is the DIRECT dependency:** Editor consumes its `edit_plan.json` (`plan_ready` / `successEditPlan`) as a precondition gate and extends its 8-tuple `parent_chain` to a 9-tuple. The first *executor* in the post tail cannot LOCK ahead of the director whose plan it conforms.
**Estimated cost:** **$0.00 engine spend** (Editor calls NO generative engine, renders NO media, decodes NO bytes — by design; Hard Rule #3; `render_dispatched: const false`, `conform_mode: const "human_in_the_loop"`) · ~**$0.35–0.70** Opus inference per case × 5 (× 7 with both probes) ≈ **≤ $3.50 (≤ $4.90 with both probes) total LLM token spend.** Editor conforms a plan into an EDL; it never dispatches a render in dry-run *or* live, so the two modes are functionally identical (deterministic transform over declared metadata + the directed plan). Lighter than Edit Director's authoring pass (Editor executes; it authors nothing).
**Pre-validated:** Both schemas META-SCHEMA VALID (Day 71). Full bundle `validate.py` **76/76 green** Day 72 (meta-schema ×2 + 5 fixture input/output validations + 19 adversarial guards + 5 two-verdict guards + 17 codes/FOLDED-routing + 9 parent_chain additive-hold + 5 input guards + the TC-01/TC-02 mode-blind convergence proof + the TC-05 gating check) on the iMac's `jsonschema` 4.26. The §5 validator below extends that harness to score live LLM output against the 5 fixture expectations.
**Mode default:** **dry-run** (see §6). Because Editor dispatches no engine and renders no media, "dry-run" and "live" are functionally identical — there is no engine surface and no render surface to vary. Dry-run is the v1.0 LOCK gate.
**Operator approval still required to begin:** AI Video Gen v1.0 LOCK CLOSED **and** Style Replication v1.0 LOCK CLOSED **and** QC Pre-flight v1.0 LOCK CLOSED **and** Ingest v1.0 LOCK CLOSED **and** Edit Director v1.0 LOCK CLOSED (five hard gates, dependency order), **plus** Editor Day 69 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.

---

## TL;DR (action sequence)

1. **Confirm AI Video Gen v1.0 LOCK ceremony has CLOSED.** Day 27 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #1** (chain head). If pending, stop.
2. **Confirm Style Replication v1.0 LOCK ceremony has CLOSED.** Day 36 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.** If pending, stop.
3. **Confirm QC Pre-flight v1.0 LOCK ceremony has CLOSED.** Day 47 5/5 PASS · Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #3.** If pending, stop.
4. **Confirm Ingest v1.0 LOCK ceremony has CLOSED.** Day 57 5/5 PASS · Day 53 Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #4.** If pending, stop.
5. **Confirm Edit Director v1.0 LOCK ceremony has CLOSED.** Day 65 runbook 5/5 PASS · Day 61 Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #5 — Editor's DIRECT dependency** (the `plan_ready`/`successEditPlan` precondition gate + the 8-tuple this agent's 9-tuple extends). If pending, stop.
6. **Confirm Editor Day 69 LOCK-CANDIDATE Items 6 + 8 + 11 are operator-ratified.** Item 6 = cost-model confirm (~$0-engine/$0-render/$0-decode posture; no vendor URLs, no ceilings). Item 8 = the 15-decision walk (D15 Sound handoff → Drive `/reels/[reel_id]/` conform-queue holding store; resolve jointly with Edit Director Day 61 Item 8 — same seam one stage downstream; D7 9-tuple QUADRUPLY-DEFERRED). Item 11 = Cross-SPEC §3.9 n-tuple amendment (the 9-tuple `parent_chain` forcing function — see §6) + the §8.7 false-fail ≤5% tightening confirm.
7. **Optional:** Run `cd "~/ars/skills/editor-agent" && python3 validate.py` in a fresh Python process for the canonical 76/76 bundle stamp. ~20 sec. Not gated — confirmed green Day 72 (requires `jsonschema` ≥ 4.18 for Draft 2020-12).
8. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
9. **Model:** `claude-opus-4-6`. **Temperature:** `0.2`. **Max tokens:** `8000`. **Top-p:** default.
   *(Assumption stated: Editor runs COLD — same 0.2 as QC Pre-flight / Ingest / Edit Director, and the cold rationale is STRONGEST here. Editor authors nothing: it CONFORMS a fixed plan into an EDL. Cut order is the Script's, caption copy is the plan's byte-for-byte, timecodes are 30fps-grid arithmetic, the brand-edit rule is zero-tolerance. 0.2 minimizes evidence-field paraphrase variance and tightens the TC-01/TC-02 convergence proof without touching verdict logic. Operator may raise to 0.4 to match fleet default; verdicts are temperature-stable by construction (the §12 const gates make a false-edl-ready structurally impossible at any temperature). A newer Opus tag — e.g. `claude-opus-4-8` — is acceptable; the fleet has run every prior runbook on opus-4-6, so use it for cross-runbook comparability unless deliberately re-baselining.)*
10. **System prompt:** open `ars/skills/editor-agent/SKILL.md`, locate the fenced block under §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)", paste **everything inside the fence** (13 hard rules + Blueprint §4.10 target `edl` shape inlined + the 9:16/1080×1920/30fps format header + universal-access/tier-FLAT table + 11-step conform loop + voice rule + "Emit JSON only. Now."). No edits. No additions.
11. For each of the 5 cases (then optionally the 2 probes):
    - Open `ars/skills/editor-agent/test-cases/case-NN-*/input.json`. Copy the **entire root object**.
    - User message = the JSON input object **only**. **No engine-stub fence** — Editor reads no engine surface and renders no media; everything it conforms (the Edit Director `edit_plan`, the resolved Ingest `asset_bundle` with declared durations, tier_richness, mode_blind_confirm, plan_evidence_hash, parent_chain, qc_pre_flags) is already inside the input object. No prose, no markdown around the JSON.
    - Send. Capture the **raw JSON output only** (strip any accidental code fence — Hard Rule #1 forbids them, but verify). Save to `ars/skills/editor-agent/validation/llm-out/case-NN-output.json`.
    - Note token counts + wall-clock latency in the run-log (§8 template).
12. **Run validator** (single command, §5). Either **5/5 PASS + convergence proof OK → Editor v1.0 LOCK ceremony executable** (subject to the five hard gates + Items 6/8/11), or capture failures for a Day 74 patch session.

---

## §1 Pre-flight checklist (16 items)

- [ ] **AI Video Gen v1.0 LOCK ceremony CLOSED.** Day 27 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #1** (chain head).
- [ ] **Style Replication v1.0 LOCK ceremony CLOSED.** Day 36 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.**
- [ ] **QC Pre-flight v1.0 LOCK ceremony CLOSED.** Day 47 5/5 PASS · Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #3.**
- [ ] **Ingest v1.0 LOCK ceremony CLOSED.** Day 57 5/5 PASS · Day 53 Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #4.**
- [ ] **Edit Director v1.0 LOCK ceremony CLOSED.** Day 65 5/5 PASS · Day 61 Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #5 — Editor's DIRECT dependency.** (All five production/gate/director LOCKs must close in dependency order before Editor — the first post-production executor cannot LOCK ahead of the directed plan it conforms.)
- [ ] **Editor Day 69 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.** Item 6 = cost-model confirm ($0-engine/$0-render/$0-decode; no vendor surface, no ceilings). Item 8 = 15-decision walk (D15 explicit verdict; D7 9-tuple QUADRUPLY-DEFERRED). Item 11 = Cross-SPEC §3.9 n-tuple amendment + §8.7 false-fail ≤5% confirm (or explicitly DEFERRED — see §6 note on the 9-tuple).
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key already configured.
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run. *(For Editor these are functionally identical — no engine, no render in either.)*
- [ ] **All 5 fixtures present** at `ars/skills/editor-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:** `mkdir -p "~/ars/skills/editor-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 71 authored-as-drafted · re-verified Day 72 `validate.py` 76/76).
- [ ] **`input.schema.json` self-validates** ✓ (Day 71 · 5/5 fixtures green Day 72).
- [ ] **System-prompt + largest fixture footprint** = ~10 KB SKILL prompt + ~4 KB largest input ≈ **~14 KB context window.** Trivial vs Opus 200 K context.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support). *(The iMac carries 4.26 — the Day 72 76/76 stamp environment.)*
- [ ] **No raw vendor credentials anywhere on screen.** Editor references NO credentials (Hard Rule #3 — it calls no engine, renders no media, decodes no bytes). If Opus emits a credential, composes an engine/render prompt, or emits a render-execute / frame-burn / transcode command in any response, abort — the agent has misunderstood its job.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object**. |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"SYSTEM PROMPT — v1.0" fence — identical across all cases). |
| 3 | User message = `{input object}` only. **No fence, no stub, no prose.** Editor reads no engine and renders no media; the input carries everything it conforms. |
| 4 | Set temperature `0.2`, max tokens `8000`. Hit **Run**. |
| 5 | Wait for completion. Verify the response is a **single JSON object** with no markdown fences (Hard Rule #1 — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check: `metadata.agent_id == "editor-agent"` AND `metadata.agent_version == "1.0"` AND `metadata.render_dispatched == false` AND `mode_blind_confirm.production_mode_read == false` AND `human_review_required == true` (both branches). If not, halt — the agent is hallucinating identifiers, forging render provenance, reading the mode, or breaking recommend-don't-render. |

---

## §3 The cases — expected branch + pass criteria

**The 5 fixtures exercise BOTH verdict values** (`edl_ready` ×2, `fail` ×3) and **3 of the 9 LOCKED error codes live** (`timecode_out_of_range`, `asset_unresolved`, `edl_firewall_breach`). The remaining 6 codes (`upstream_plan_not_ready`, `upstream_not_success`, `timeline_gap_or_overlap`, `transition_policy_violation`, `plan_fidelity_breach`, `edl_lineage_failure`) + the slot-11 catch-all (`editor_agent_failed`) are bound to the schema via the Day 72 `validate.py` adversarial guards, not all re-exercised live (same discipline as Edit Director §3 / Ingest §3 / QC Pre-flight §3). The optional probes in §3.6 / §3.7 exercise the bare-`revise`-halt precondition and the slot-11 catch-all live as defense-in-depth — they are NOT part of the 5/5 LOCK count.

**Editor is the FIRST fleet agent to DROP a predecessor verdict: there are only TWO verdicts, `edl_ready | fail` — there is NO `revise`** (deliberate divergence from Edit Director's `plan_ready/fail/revise`; §3.1 / §6.4 / §12 / D3). Editor is a fully-deterministic executor: every check is binary (a timecode is in range or it isn't; copy is byte-faithful or it isn't; a transition is a cut or it isn't; the firewall is clean or it isn't). There is no subjective conform surface to hold to Lever-3 — that judgment call lives ONE stage upstream (Edit Director's `revise`). Re-introducing `revise` here would mean Editor second-guessing a directed plan — exactly the decide/execute override the boundary forbids. Human deferral still lives in `human_review_required: true` + `conform_mode: human_in_the_loop` on EVERY emission — it is just not a *verdict* branch. **The §5 validator REJECTS any `revise`, any `hold`, and any `reshoot`.**

### TC-01 — `case-01-mode-a-origin-pro-edl-ready` (Pro · Mode A origin · 6-shot · clean `edl_ready`)
- **Expected branch:** `successEdl`. **Verdict:** `edl_ready`. **route:** n/a (success carries `handoff_targets: [sound-agent]`).
- **Hard checks:**
  - `output_type == "successEdl"`, `verdict == "edl_ready"` (schema `const "edl_ready"` on this branch).
  - `edl.frame_rate == 30`, `edl.aspect == "9:16"`, `edl.resolution == "1080x1920"` (format const header).
  - `edl.events[].transition == "cut"` for EVERY event (hard-cuts-only enforced at the timeline).
  - `conform_check`: `timeline_gap_free == true`, `no_double_spend == true`, `all_events_bounded_by_declared_duration == true`, `frame_aligned == true`, `duration_in_band == true` (total_timeline_ms in the 45–75s band; scenario: 6 × 9500ms = 57000 + end-card 1500 = 58500).
  - `plan_fidelity_check`: all 6 true (`cut_count_matches_plan`, `caption_copy_byte_faithful`, `lower_third_copy_byte_faithful`, `end_card_byte_faithful`, `transition_policy_hard_cuts_only`, `plan_evidence_hash_verified`).
  - `edl_firewall_pass_10.status == "pass"`, `hits == 0`.
  - `mode_blind_confirm.production_mode_read == false`, `consumed == "mode_agnostic_edit_plan"`.
  - `render_target.render_dispatched == false`, `conform_mode == "human_in_the_loop"`.
  - `end_card_event`: `line == "REINVENTED - build on purpose."`, `hold_ms == 1500`.
  - `tier_richness_echo.variants_conformed == 1`, `primary_aspect == "9:16"`.
  - `human_review_required == true`, `cost_incurred_usd == 0.0` (≈0.00 to 2dp).
  - `metadata.parent_chain` = 9-tuple (8 inbound + appended `edl_id`), held additively.

### TC-02 — `case-02-mode-c-enterprise-edl-ready` (Enterprise · Mode C origin · convergence twin · `edl_ready`)
- **Expected branch:** `successEdl`. **Verdict:** `edl_ready`.
- **The mode-blind convergence proof (two stages deep).** Footage originated Mode C (`parent_chain[3] == "mode-c-direct"`), tier Enterprise — and Editor conforms it through the IDENTICAL executor logic, emitting a **byte-shape-identical** `edl` / `conform_check` / `plan_fidelity_check` / `edl_firewall_pass_10` / `mode_blind_confirm` block vs TC-01. Only audit-lineage fields differ (`production_mode`, `tier`, ids).
- **Hard checks:** all TC-01 success checks PLUS `mode_blind_confirm.production_mode_read == false` (the machine-checkable proof) AND the §5 convergence assertion: the TC-01 vs TC-02 conformed `edl` event-shape + caption/lower-third/end-card/music event structure are byte-shape-identical (see §5 convergence proof).

### TC-03 — `case-03-timecode-out-of-range-fail` (`fail` / `timecode_out_of_range`)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `timecode_out_of_range`**. **`failed_check_id`: 4**. **`route_back_to`: `edit-director-agent`**.
- The plan directs `shot-003` at `out_ms: 15000`, but the Ingest bundle declares that shot at 12.0s (12000ms). `15000 > 12000` — the cut would conform past available media (Hard Rule #5). Route to Edit Director to re-trim.
- **Hard checks:** top-level `failure_code`/`failed_check_id`/`route_back_to` exact; `detail.violation` names the offending event + available media; `detail.affected_events` includes `shot-003`; `cost_incurred_usd == 0.0`; `mode_blind_confirm.production_mode_read == false`.

### TC-04 — `case-04-asset-unresolved-fail` (`fail` / `asset_unresolved` — the FOLDED code)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `asset_unresolved`**. **`failed_check_id`: 3**. **`route_back_to`: `ingest-agent`**.
- The plan directs a cut whose `asset_uri` (`ars://reinvented/shots/shot-099.mp4`) has no handle in `asset_bundle.raw_footage[]`. Editor cannot bind the cut to real media (Hard Rule #5).
- **The FOLDED-code proof:** `asset_unresolved` deliberately folds cut-asset + music-bed + voice-track resolution failures — all carry this single code because they share ONE route-back destination (Ingest). This is the OPPOSITE of Edit Director keeping `duration_envelope_breach` standalone: Editor clusters its defect surface by route-back destination, not defect taxonomy (D8).
- **Hard checks:** `failure_code == "asset_unresolved"`, `route_back_to == "ingest-agent"` (NOT edit-director); `detail` names the unresolvable handle.

### TC-05 — `case-05-commit-firewall-breach-fail` (`fail` / `edl_firewall_breach` — GATING)
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **`failure_code`: `edl_firewall_breach`**. **`failed_check_id`: 9**. **`route_back_to`: `edit-director-agent`**.
- A banned-entity token (`sln`) has survived into a committed caption line (`"sln runs the studio"`). Editor authored no copy — the string is Edit Director passthrough — but Editor is the agent that COMMITS that text to the executable cut spec, so its 10th-pass commit-time firewall re-scan is the final net before the copy is burned into pixels (Hard Rule #9 / Check #9). **This is the highest-stakes code in the namespace: a leak here would be burned into v1.mp4.**
- **Hard checks:** `failure_code == "edl_firewall_breach"`, `failed_check_id == 9`, `route_back_to == "edit-director-agent"` (the committed copy is the plan's — the author owns the fix); `detail` forensically names the leaking committed field + the `hits: 1` firewall result. **GATING fixture — a false-`edl_ready` here is an automatic runbook FAIL.**

### §3.6 Optional probe A — bare `revise` plan WITHOUT Lever-3 sign-off → halt `upstream_plan_not_ready`
- **Not part of the 5/5 count.** Construct an input whose `edit_plan.json` carries `verdict: "revise"` (Edit Director's soft-judgment success-side verdict) with NO Lever-3 human sign-off attached.
- **Expected:** `errorEnvelope`, `failure_code == "upstream_plan_not_ready"`, `route_back_to == null`. Editor does NOT auto-resolve a bare `revise` — the soft creative call is the operator's (Hard Rule #4 / conform-loop step 1). This probes that Editor's two-verdict determinism does NOT silently swallow a predecessor's third verdict.

### §3.7 Optional probe B — slot-11 catch-all → `editor_agent_failed`
- **Not part of the 5/5 count.** Feed a degenerate input that survives to a second self-QC failure (e.g. an internally inconsistent plan that cannot conform cleanly and cannot be cleanly routed by a specific code).
- **Expected:** `errorEnvelope`, `failure_code == "editor_agent_failed"`, `route_back_to == null`, `metadata.self_qc_attempts == 2`. Exercises the slot-11 catch-all + the route-null halt (conform-loop step 11).

---

## §4 Output-schema validation contract (both branches)

Every saved `case-NN-output.json` must validate against `schemas/output.schema.json` (Draft 2020-12). The schema is a `oneOf(successEdl, errorEnvelope)` discriminated on `output_type`.

**successEdl branch (TC-01, TC-02)** must carry: `output_type: "successEdl"`, `verdict: const "edl_ready"`, `reel_ref`, `edl` (frame_rate/aspect/resolution const, `events[]` with `transition: const "cut"`, `caption_events[]` with `text` maxLength 22, `lower_third_events[]` with `case: const "lowercase"` + `align: const "left"`, `music_event`, `end_card_event` with `hold_ms: const 1500`), `plan_precondition_check`, `conform_check` (all-true const gates), `plan_fidelity_check` (6-true const), `edl_firewall_pass_10` (`hits: const 0`), `mode_blind_confirm` (`production_mode_read: const false`), `render_target` (`render_dispatched: const false`, `conform_mode: const "human_in_the_loop"`), `qc_pre_flags`, `tier_richness_echo` (`variants_conformed: const 1`), `metadata`, `human_review_required: const true`.

**errorEnvelope branch (TC-03/04/05, probes)** must carry: `output_type: "errorEnvelope"`, `verdict: const "fail"`, top-level `failure_code` (enum of the 9 + slot-11), `failed_check_id` (int), `route_back_to` (per the code→route map, or `null`), `reel_ref`, `cost_incurred_usd`, `mode_blind_confirm`, `metadata`, `human_review_required: const true`, `detail` (`violation` + `affected_events` + `recovery_path`).

**Code → route map (must match exactly):**

| Verdict / code | `route_back_to` |
|----------------|-----------------|
| `asset_unresolved` (cut-asset · music-bed · voice-track — FOLDED) | `ingest-agent` |
| `timecode_out_of_range` · `timeline_gap_or_overlap` · `transition_policy_violation` · `plan_fidelity_breach` · `edl_firewall_breach` | `edit-director-agent` |
| `upstream_plan_not_ready` · `upstream_not_success` · `edl_lineage_failure` · `editor_agent_failed` (slot-11) | `null` |

**Zero false-`edl_ready` (the defining target):** the success branch pins every §12 ∧-of-gates HARD term as a `const` invariant (firewall `hits: 0`, `conform_check` all-true, `plan_fidelity_check` 6-true, `events[].transition` cut, caption `maxLength 22`, lower-third `case/align` const, end-card `hold_ms 1500`, format const 30/9:16/1080×1920, `render_dispatched: false`, `production_mode_read: false`). A false-`edl_ready` is **structurally impossible** — the schema rejects it before the validator scores it. **False-fail target ≤5%** (Ingest-class deterministic-executor floor; §8.7, operator-confirm Item 11).

---

## §5 The validator (single command)

After all 5 outputs are saved to `validation/llm-out/case-NN-output.json`, run:

```bash
cd "~/ars/skills/editor-agent" && python3 validate_llm_run.py
```

`validate_llm_run.py` (author it once into the bundle root, alongside `validate.py`) does, per case:

1. **Schema-validate** the saved output against `schemas/output.schema.json` (Draft 2020-12). Any schema error = case FAIL.
2. **Branch match:** `output_type` matches the expected branch (TC-01/02 `successEdl`; TC-03/04/05 `errorEnvelope`).
3. **Verdict match:** `verdict` equals the expected value; **REJECT `revise`, `hold`, `reshoot` on BOTH branches** (the two-verdict guard — Editor's defining divergence).
4. **fail-case triplet:** for TC-03/04/05, `failure_code` + `failed_check_id` + `route_back_to` all equal the fixture `expected_output.json` (esp. TC-04 route = `ingest-agent`, TC-03/05 route = `edit-director-agent`).
5. **Success const gates:** for TC-01/02, assert firewall `hits == 0`, `conform_check` all-true, `plan_fidelity_check` 6-true, every `events[].transition == "cut"`, format 30/9:16/1080×1920, `render_dispatched == false`, `conform_mode == "human_in_the_loop"`, `production_mode_read == false`, `variants_conformed == 1`, `human_review_required == true`, `end_card_event.hold_ms == 1500`.
6. **Convergence proof (TC-01 vs TC-02):** assert the conformed `edl` event-shape (count + per-event `transition`/timing structure) + the caption/lower-third/music/end-card event structure are byte-shape-identical across the two outputs, and BOTH attest `production_mode_read == false`. This is the machine-checkable proof that Editor's mode-blindness holds two stages deep past Ingest's convergence seam.
7. **TC-05 gating:** assert the injected `sln` token is present in the committed caption copy of the INPUT and the output verdict is `edl_firewall_breach` with `hits: 1`, route `edit-director-agent`. A false-`edl_ready` on TC-05 is an automatic runbook FAIL.

**Output:** `5/5 PASS` (+ convergence OK + TC-05 gating OK) → Editor v1.0 LOCK ceremony executable (subject to the five hard gates + Items 6/8/11). Any case FAIL → capture into a Day 74 patch session; do NOT LOCK.

*(Note: `validate.py` is the bundle's structural harness — 76/76 on the fixtures. `validate_llm_run.py` is the thin LLM-output scorer this runbook adds; it reuses the same schema + the fixture `expected_output.json` files as the answer key. Both are $0, offline, no engine/render/network/LLM.)*

---

## §6 Mode note + the QUADRUPLY-deferred 9-tuple `parent_chain`

**Dry-run vs live are identical for Editor.** Editor dispatches no engine and renders no media in EITHER mode (Hard Rule #3). There is no engine surface and no render surface to vary. "Dry-run" is the label; the behavior is the only behavior Editor has. Dry-run is the v1.0 LOCK gate.

**The 9-tuple `parent_chain` is QUADRUPLY-DEFERRED (D7) — do NOT advance it in this runbook.** The schema holds additively (`minItems: 5`, `prefixItems` 0–8, `maxItems: 9`, `items: false`). Editor's SKILL emits the 9th position (its appended `edl_id`), and the fixtures carry a full 9-tuple, but the schema ACCEPTS a 5/6/7/8-tuple inbound canon through the 9-tuple append. The `minItems` flip to 9 (exact-9 cardinality) requires ALL FOUR gates to close: (a) operator ratification of the Cross-SPEC §3.9 n-tuple amendment (Item 11), (b) the Edit Director 8-tuple LOCK, (c) the Ingest 7-tuple LOCK, AND (d) the QC Pre-flight 6-tuple LOCK. Editor is the **FOURTH forcing function** for the amendment. Passing this runbook 5/5 does NOT flip the cardinality — the additive hold is correct and intended until the operator ratifies. **This is the one item Donna will NOT auto-advance.**

**§8.7 false-fail ≤5% confirm (Item 11 bundle):** the Day 68 partial tightened Editor's false-fail ceiling from the ≤8% preview to ≤5% (a consequence of D3's two-verdict determinism — the looser band existed only to absorb Edit Director's one `revise` judgment surface; Editor holds none). Operator confirms ≤5% at the LOCK ceremony. Recommendation: CONFIRM ≤5%.

---

## §7 LOCK decision gate

Editor Agent v1.0 LOCKs **if and only if ALL** of the following are true:

1. AI Video Gen v1.0 LOCK CLOSED (HARD GATE #1).
2. Style Replication v1.0 LOCK CLOSED (HARD GATE #2).
3. QC Pre-flight v1.0 LOCK CLOSED (HARD GATE #3).
4. Ingest v1.0 LOCK CLOSED (HARD GATE #4).
5. Edit Director v1.0 LOCK CLOSED (HARD GATE #5 — direct dependency).
6. Editor Day 69 LOCK-CANDIDATE Items 6 + 8 + 11 ratified (cost-model · 15-decision walk · §3.9 amendment + ≤5% confirm).
7. This runbook: **5/5 fixtures PASS** + convergence proof OK + TC-05 gating OK.

If all seven hold, execute the LOCK ceremony (operator-only): flip the Notion ARS-hub Editor row to LOCKED, flip the dashboard chip to `live`, tag the SKILL bundle v1.0 LOCKED. **Donna performs NONE of these** — they wait for Jamila. If any gate is open, Editor stays LOCK-CANDIDATE; the runbook result is recorded and the ceremony is deferred.

---

## §8 Run-log template (fill during the sit-down)

```
EDITOR v1.0 — DAY 73 LLM TEST RUN
Date/time (PT):        ____________________
Operator:              Jamila
Mode:                  dry-run  |  live      (default dry-run — identical for Editor)
Model id:              claude-opus-4-6  (or 4-8 if re-baselining — note which)
Temperature:           0.2   Max tokens: 8000

Hard gates (must ALL be CLOSED before scoring counts toward LOCK):
  [ ] AI Video Gen v1.0 LOCKED
  [ ] Style Replication v1.0 LOCKED
  [ ] QC Pre-flight v1.0 LOCKED
  [ ] Ingest v1.0 LOCKED
  [ ] Edit Director v1.0 LOCKED   (direct dependency)
  [ ] Editor Day 69 Items 6 / 8 / 11 ratified

Per case:
  TC-01  in-tok ____ out-tok ____ sec ____  verdict edl_ready  PASS/FAIL ____
  TC-02  in-tok ____ out-tok ____ sec ____  verdict edl_ready  PASS/FAIL ____   convergence w/TC-01: OK/NO ____
  TC-03  in-tok ____ out-tok ____ sec ____  fail/timecode_out_of_range  route edit-director  PASS/FAIL ____
  TC-04  in-tok ____ out-tok ____ sec ____  fail/asset_unresolved  route ingest  PASS/FAIL ____
  TC-05  in-tok ____ out-tok ____ sec ____  fail/edl_firewall_breach  route edit-director  PASS/FAIL ____  (GATING)

Optional probes (not in 5/5 count):
  Probe A (bare revise, no Lever-3)  → upstream_plan_not_ready / route null   PASS/FAIL ____
  Probe B (slot-11)                  → editor_agent_failed / route null / attempts 2   PASS/FAIL ____

Validator result:      __ / 5 PASS   convergence: OK/NO   TC-05 gating: OK/NO
LLM spend (est):        $ ______   Engine/render spend: $0.00 (structural)
LOCK decision:         LOCKED  |  HELD (reason: ____________________)
```

---

## §9 Guardrails (process-integrity — restate before running)

- **$0 engine, $0 render, $0 decode.** Editor calls no generative engine, renders no media, decodes no bytes. The only spend is Opus inference on the test cases. If any output composes an engine prompt / render command / transcode instruction, abort the case — the agent misunderstood its job.
- **No operator impersonation.** Donna authored this runbook; Donna does NOT execute it. The paste-and-run + the LOCK ceremony are operator-only. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED by Donna.
- **The five hard gates are dependency-ordered and absolute.** Editor cannot LOCK ahead of Edit Director (its direct dependency), which cannot LOCK ahead of Ingest, QC Pre-flight, Style Replication, or AI Video Gen. A 5/5 pass with an open gate = HELD, not LOCKED.
- **The 9-tuple stays additive.** Passing 5/5 does not flip `minItems` to 9. That flip is operator-gated ×4 (Item 11 + three predecessor tuple LOCKs).
- **Entity firewall.** ARS = Sequel Digital. `brand_id` = REINVENTED (pilot). The 11-entry HC/NPOX block-list is the firewall's catch-list, not a cross-entity reference. TC-05 is the live proof the 10th pass catches a leak before pixels.

---

*Authored 2026-07-01 (Pacific) by Donna (overnight ARS Day 73 build session). Sequel Digital entity scope. This is the Editor Agent #10 v1.0 LLM Test Runbook — the forward deliverable per the Day 72 log close (§"What's unlocked") + the §14 calendar Day 73 slot, shipped ON schedule. It is the paste-and-run operator test suite (5 fixtures + 2 optional adversarial probes) that gates Editor's eventual v1.0 LOCK. Editor is the FIRST fleet agent to DROP a predecessor verdict (two-verdict `edl_ready | fail`, NO `revise`) and the SECOND contractually mode-blind agent (the TC-01/TC-02 convergence proof that Ingest's mode-convergence seam holds two stages deep). The v1.0 LOCK hard-gates on FIVE predecessor LOCKs closing in dependency order (Edit Director is the direct dependency — the `plan_ready` precondition + the 8-tuple the 9-tuple extends) + Items 6/8/11. The 9-tuple `parent_chain` stays QUADRUPLY-deferred (held additively at `minItems 5`) — Editor is the fourth forcing function for the Cross-SPEC §3.9 amendment; NOT advanced this run. Next forward deliverable: Editor v1.0 LOCK (Day 74, operator + hard-gated). Next Rest Day: Day 77 (Sun Jul 5).*
