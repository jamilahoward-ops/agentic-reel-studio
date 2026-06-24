# Day 65 LLM Test Execution Runbook — Edit Director Agent v1.0

**Date authored:** 2026-06-23 (Tue · Day 65 · Wk9D3 · post-launch hardening window · v1.0 LOCK gate)
**Audience:** Jamila — single 20–35 min sit-down at the iMac (paste-and-run discipline).
**Goal:** Run all 5 SKILL-bundle fixtures (+ 2 optional adversarial probes: a valid `revise` and a slot-11 `edit_director_agent_failed`) through Opus, validate each output against `schemas/output.schema.json`, declare Edit Director Agent v1.0 **LOCKED** if 5/5 PASS — IF AND ONLY IF the four predecessor LOCK ceremonies (AI Video Gen v1.0 → Style Replication v1.0 → QC Pre-flight v1.0 → Ingest v1.0) close first, in dependency order. **Ingest is the DIRECT dependency:** Edit Director consumes its `asset_manifest.json` (`pass` / `successAssetManifest`) as a precondition gate and extends its 7-tuple `parent_chain` to an 8-tuple. The first creative-authoring agent in the post tail cannot LOCK ahead of the gate it depends on.
**Estimated cost:** **$0.00 engine spend** (Edit Director calls NO generative engine and renders NO media, by design — Hard Rule #2; `render_dispatched: const false`) · ~**$0.45–$0.80** Opus inference per case × 5 (× 7 with both probes) ≈ **≤ $4.00 ($5.60 with both probes) total LLM token spend.** Edit Director authors a plan; it never dispatches a render in dry-run *or* live, so the two modes are functionally identical (reasoning-only over declared metadata + upstream creative intent).
**Pre-validated:** Both schemas META-SCHEMA VALID (Day 62). Full bundle `validate.py` **59/59 green** Day 64 (meta-schema ×2 + 5 fixture input/output validations + 30 adversarial guards + parent_chain additive hold + 3-verdict model + standalone-`duration_envelope_breach` + slot-11 + the TC-01/TC-02 mode-blind convergence proof + the TC-05 gating check). The §5 validator below extends that harness to score live LLM output against the 5 fixture expectations.
**Mode default:** **dry-run** (see §6). Because Edit Director dispatches no engine and renders no media, "dry-run" and "live" are functionally identical — there is no engine surface and no render surface to vary. Dry-run is the v1.0 LOCK gate.
**Operator approval still required to begin:** AI Video Gen v1.0 LOCK CLOSED **and** Style Replication v1.0 LOCK CLOSED **and** QC Pre-flight v1.0 LOCK CLOSED **and** Ingest v1.0 LOCK CLOSED (four hard gates, dependency order), **plus** Edit Director Day 61 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.

---

## TL;DR (action sequence)

1. **Confirm AI Video Gen v1.0 LOCK ceremony has CLOSED.** Day 27 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #1** (chain head). If pending, stop.
2. **Confirm Style Replication v1.0 LOCK ceremony has CLOSED.** Day 36 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.** If pending, stop.
3. **Confirm QC Pre-flight v1.0 LOCK ceremony has CLOSED.** Day 47 runbook 5/5 PASS · Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #3.** If pending, stop.
4. **Confirm Ingest v1.0 LOCK ceremony has CLOSED.** Day 57 runbook 5/5 PASS · Day 53 Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #4 — Edit Director's DIRECT dependency** (the `successAssetManifest`/`pass` precondition gate + the 7-tuple this agent's 8-tuple extends). If pending, stop.
5. **Confirm Edit Director Day 61 LOCK-CANDIDATE Items 6 + 8 + 11 are operator-ratified.** Item 6 = cost-model confirm ($0-engine/$0-render posture; `cost_incurred_usd ≈ 0.04` token-only). Item 8 = the 15-decision walk (D15 Editor-handoff → Notion Edit Plan holding store; resolve jointly with Ingest Day 53 Item 8 — same seam both ends). Item 11 = Cross-SPEC §3.9 n-tuple amendment (the 8-tuple `parent_chain` forcing function — see §6).
6. **Optional:** Run `cd "~/ars/skills/edit-director-agent" && python3 validate.py` in a fresh Python process for the canonical 59/59 bundle stamp. ~20 sec. Not gated — confirmed green Day 64.
7. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
8. **Model:** `claude-opus-4-6`. **Temperature:** `0.2`. **Max tokens:** `8000`. **Top-p:** default.
   *(Assumption stated: Edit Director runs colder than the production agents' 0.4 — same rationale as QC Pre-flight + Ingest. Although it AUTHORS a plan, the authoring is rule-bound, not free-creative: cut order is fixed by the Script structure + Storyboard vocabulary, caption copy is LAID not written, the brand-edit ruleset is zero-tolerance. 0.2 reduces evidence-field + cut-rhythm paraphrase variance and tightens the TC-01/TC-02 convergence proof without touching verdict logic. Operator may raise to 0.4 to match fleet default; verdicts are temperature-stable by construction. A newer Opus tag — e.g. `claude-opus-4-8` — is acceptable; the fleet has run every prior runbook on opus-4-6, so use it for cross-runbook comparability unless deliberately re-baselining.)*
9. **System prompt:** open `ars/skills/edit-director-agent/SKILL.md`, locate the fenced block under §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)", paste **everything inside the fence** (12 hard rules + Blueprint §4.9 target `edit_plan` shape inlined + universal-access/tier-richness table + 11-step direction loop + voice rule + "Emit JSON only. Now."). No edits. No additions.
10. For each of the 5 cases (then optionally the 2 probes):
    - Open `ars/skills/edit-director-agent/test-cases/case-NN-*/input.json`. Copy the **entire root object**.
    - User message = the JSON input object **only**. **No engine-stub fence** — Edit Director reads no engine surface and renders no media; everything it directs (the Ingest Asset Manifest, the denormalized Script beat map + caption strategy, the Storyboard shot vocabulary, the production_plan target, the brief length band, parent_chain, qc_pre_flags) is already inside the input object. No prose, no markdown around the JSON.
    - Send. Capture the **raw JSON output only** (strip any accidental code fence — Hard Rule #1 forbids them, but verify). Save to `ars/skills/edit-director-agent/validation/llm-out/case-NN-output.json`.
    - Note token counts + wall-clock latency in the run-log (§8 template).
11. **Run validator** (single command, §5). Either **5/5 PASS + convergence proof OK → Edit Director v1.0 LOCK ceremony executable** (subject to the four hard gates + Items 6/8/11), or capture failures for a Day 66 patch session.

---

## §1 Pre-flight checklist (15 items)

- [ ] **AI Video Gen v1.0 LOCK ceremony CLOSED.** Day 27 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #1** (chain head).
- [ ] **Style Replication v1.0 LOCK ceremony CLOSED.** Day 36 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.**
- [ ] **QC Pre-flight v1.0 LOCK ceremony CLOSED.** Day 47 5/5 PASS · Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #3.**
- [ ] **Ingest v1.0 LOCK ceremony CLOSED.** Day 57 5/5 PASS · Day 53 Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #4 — Edit Director's DIRECT dependency.** (All four production/gate LOCKs must close in dependency order before Edit Director — the first post-production authoring agent cannot LOCK ahead of the precondition manifest it consumes.)
- [ ] **Edit Director Day 61 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.** Item 6 = cost-model confirm. Item 8 = 15-decision walk (D15 explicit verdict; D6 8-tuple triply-deferred). Item 11 = Cross-SPEC §3.9 n-tuple amendment (or explicitly DEFERRED — see §6 note on the 8-tuple).
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key already configured.
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run. *(For Edit Director these are functionally identical — no engine, no render in either.)*
- [ ] **All 5 fixtures present** at `ars/skills/edit-director-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:** `mkdir -p "~/ars/skills/edit-director-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 62 LOCKED-as-drafted · re-verified Day 64 `validate.py`).
- [ ] **`input.schema.json` self-validates** ✓ (Day 62 · 5/5 fixtures green Day 64).
- [ ] **System-prompt + largest fixture footprint** = ~9 KB SKILL prompt + ~4 KB largest input ≈ **~13 KB context window.** Trivial vs Opus 200 K context.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support).
- [ ] **No raw vendor credentials anywhere on screen.** Edit Director references NO credentials (Hard Rule #2 — it calls no engine, renders no media). If Opus emits a credential, composes an engine/render prompt, or emits an EDL-execute / frame-trim command in any response, abort — the agent has misunderstood its job.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object**. |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"SYSTEM PROMPT — v1.0" fence — identical across all cases). |
| 3 | User message = `{input object}` only. **No fence, no stub, no prose.** Edit Director reads no engine and renders no media; the input carries everything it directs. |
| 4 | Set temperature `0.2`, max tokens `8000`. Hit **Run**. |
| 5 | Wait for completion. Verify the response is a **single JSON object** with no markdown fences (Hard Rule #1 — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check: `metadata.agent_id == "edit-director-agent"` AND `metadata.agent_version == "1.0"` AND `metadata.render_dispatched == false` AND `mode_blind_confirm.production_mode_read == false` (success branch) AND `human_review_required == true`. If not, halt — the agent is hallucinating identifiers, forging render provenance, reading the mode, or breaking recommend-don't-approve. |

---

## §3 The cases — expected branch + pass criteria

**The 5 fixtures exercise all 3 verdict values** (`plan_ready` ×2, `fail` ×3) and **3 of the 9 LOCKED error codes live** (`incomplete_shot_coverage`, `brand_edit_rule_conflict`, `edit_plan_firewall_breach`). The remaining 6 codes (`upstream_ingest_not_passed`, `upstream_not_success`, `beat_map_unmappable`, `cut_order_incomplete`, `caption_spec_violation`, the STANDALONE `duration_envelope_breach`) + `plan_lineage_failure` (forensic halt) + the slot-11 catch-all (`edit_director_agent_failed`) are bound to the schema via the Day 64 `validate.py` adversarial guards, not all re-exercised live (same discipline as Ingest §3 / QC Pre-flight §3). The optional probes in §3.6 / §3.7 exercise the `revise` success-side verdict and the slot-11 catch-all live as defense-in-depth — they are NOT part of the 5/5 LOCK count.

**The third verdict is `revise`, NOT `hold`, and there is NO `reshoot`** (deliberate divergence from Ingest's `pass/fail/reshoot` — §6.4 / SKILL verdict model). Edit Director's soft-judgment slot lives on the **success branch** as `revise` (a `successEditPlan`-shaped payload + `revise_rationale`, `route_back_to: null`), reachable only when every HARD gate is true but a SOFT brand-rule tension needs the operator's creative call. A coverage hole routes back to `ingest-agent`, never to a re-shoot (Edit Director is two gates downstream of live footage). The §5 validator REJECTS any `hold` and any `reshoot`.

### TC-01 — `case-01-mode-a-origin-pro-plan-ready` (Pro · Mode A origin · 6-shot · clean `plan_ready`)
- **Expected branch:** `successEditPlan`. **Verdict:** `plan_ready`. **route:** n/a (success carries `handoff_targets`).
- **Hard checks:**
  - `output_type == "successEditPlan"`, `verdict == "plan_ready"` (schema `const "plan_ready"` on this branch).
  - `metadata.tier == "pro"`, `metadata.production_mode == "A"`, `metadata.edit_plan_class == "primary_9x16"`.
  - **AND-of-11-gates (false-plan-ready STRUCTURALLY impossible — §12 / §8.5, schema `const`; assert anyway, defense-in-depth):**
    - `edit_plan_firewall_pass_9.status == "pass"` AND `hits == 0` AND `authored_text_fields_scanned > 0`.
    - `brand_edit_check` — the 5 HARD booleans `hard_cuts_only`, `lower_thirds_lowercase_left`, `captions_within_char_limit`, `no_reel_level_sales_cta`, `end_card_present` **all `true`**. (The 2 SOFT booleans `one_text_reveal_per_8s`, `one_emotional_beat` must also be `true` on a `plan_ready` — they may only be `false` on a `revise`.)
    - `structure_check.hook_window_ok == true`, `cta_internal_question_ok == true`, `duration_in_band == true`, `total_duration_ms` within the 45000–75000 ms band, `body_beats >= 1`.
    - `coverage_remap.unmapped_shot_refs == []` AND `unmapped_beats == []` AND `shots_required == shots_mapped == 6`.
    - `mode_blind_confirm.production_mode_read == false` AND `consumed == "mode_agnostic_manifest"`.
  - **Canonical `edit_plan` shape (Blueprint §4.9 — mode-agnostic):** keys exactly `cut_order, pacing_bpm, cut_rhythm, caption_style, caption_lines, lower_thirds, transitions, music_bed, music_swell_map, end_card`.
    - `cut_order[]` each carries `{shot_ref, in_ms, out_ms, frame_language}`; `len(cut_order) == 6` and `<= 12` (Pro tier ceiling).
    - `transitions` is the hard-cuts-only string (contains `hard cuts only`; contains NO `fade`/`wipe`/`zoom` as an enabled transition).
    - every `caption_lines[].text` is `<= 22` chars and lowercase; `line` ∈ {1,2}.
    - every `lower_thirds[].content` is lowercase, `case == "lowercase"`, `align == "left"`.
    - `music_bed` matches `^ars://`.
    - `music_swell_map` length `== 2` (the authored swell count for this reel; also the Pro tier ceiling).
    - `end_card.line == "REINVENTED — build on purpose."` (em-dash), `font_class == "serif_display"`, `hold_ms == 1500`, `doubles_as_thumbnail == true`.
  - `tier_richness.tier == "pro"`, `cut_beats <= 12`, `b_roll <= 6`, `music_swells == 2`, `variants_planned == 4`.
  - `ingest_precondition_check.verdict_observed == "pass"` (or `lever3_signoff_present == true` — schema `anyOf`).
  - `handoff_targets == ["editor-agent"]` (Step 10 success path — NOT `edit-director-agent`; Editor is position 11).
  - `qc_pre_flags[]` ≥ 4 entries, every element snake_case (`^[a-z][a-z0-9_]{0,63}$`).
  - `cost_incurred_usd <= 0.04` (top-level AND `metadata.cost_incurred_usd`; Hard Rule #2 — $0 *engine/render* cost, token-only ≈ $0.04).
  - `metadata.render_dispatched == false` (schema `const false` — a plan claiming a render it never dispatched is forged provenance).
- **Lineage:** `metadata.parent_chain` is an **8-tuple** held additively: `[brief-…, script-…, storyboard-…, productionplan-…, <uuid replication_set_id>, preflight-…, <uuid asset_manifest_id>, <uuid edit_plan_id>]`. (Schema holds `minItems 5, prefixItems 0–7, maxItems 8`; a 5/6/7-tuple is also accepted; a 4-tuple and a 9-tuple are rejected. The validator accepts 5/6/7/8.)
- **Tamper-evidence:** `metadata.plan_evidence_hash` matches `^[a-f0-9]{64}$`. *(The validator checks SHAPE, not value — Opus cannot deterministically reproduce the fixture's hash; the agent computes it honestly over its own `edit_plan` + `brand_edit_check` block.)*
- **Recommend-don't-approve:** top-level `human_review_required == true` AND `metadata.human_review_required == true` (schema `const true`). Zero approval language (`approved`, `approved for cut`, `cleared for cut`, `cleared`, `published`) anywhere in any string.
- **Entity firewall + banned-vocab walk:** zero hits of the 11-entry canonical list (`holdco group`/`hc`, `4821 main`/`4821`, `site-c-brand`/`6315`, `sln`/`sln cuts`/`sln shear`/`salonb`/`shear & cuts`, `retail supply`, `principal holdco`/`principal`, `npox`, `nonprofit leader a`, `partner brand`, `holdcogroup.com`, `community nonprofit`) and zero banned-vocab (`babe`, `boss babe`, `girl boss`, `she-eo`, `mompreneur`) across every emitted string. (REINVENTED IS allowed — pilot brand; `end_card.line` legitimately carries it.)

### TC-02 — `case-02-mode-c-enterprise-plan-ready` (Enterprise · Mode C · clean `plan_ready` · THE MODE-BLIND CONVERGENCE PROOF)
- **Expected branch:** `successEditPlan`. **Verdict:** `plan_ready`.
- **Hard checks (delta vs TC-01):**
  - `metadata.tier == "enterprise"`, `metadata.production_mode == "C"`.
  - **Lineage position [3] == `"mode-c-direct"`** (no AI Video Gen / no ProdCoord stage in a Mode C chain).
  - **THE CONVERGENCE PROOF — the fixture's whole point:** the authored `edit_plan`, `coverage_remap`, `structure_check`, `brand_edit_check`, `edit_plan_firewall_pass_9`, and `mode_blind_confirm` blocks are **byte-shape identical to TC-01** despite a different origin mode. Edit Director is the FIRST contractually mode-blind agent: whatever mode produced the footage (A, B, or C), it authors from ONE manifest shape and never branches on origin. A regression that leaked the origin mode into the authored plan would break Ingest's mode-convergence contract end-to-end. *(The §5 validator asserts this directly: it requires byte-equality of those six blocks between TC-01 and TC-02, AND that both attest `production_mode_read: false`, AND that the two `metadata.production_mode` values DIFFER — equal modes would void the proof.)*
  - **NOTE — the strictest live check.** Two independent generations from different-mode inputs must yield the *same authored plan*. Because authoring is rule-bound (not free-creative), this is achievable at temp 0.2; but authored-copy drift (a caption reworded, a swell moved 100 ms) is the **primary live-run risk** and will fail the convergence proof even when both cases independently pass every other check. If the proof fails but both cases are otherwise green, re-run BOTH at temp 0.2 (or 0.0) before declaring a patch — variance, not a contract break, is the likely cause. A *structural* divergence (different cut count, a mode-branched field) IS a contract break and warrants a Day 66 patch.
  - All other TC-01 success checks apply (AND-of-11-gates, `^ars://` `music_bed`, `handoff_targets == ["editor-agent"]`, recommend-don't-approve, `render_dispatched: false`, `plan_evidence_hash` shape, 8-tuple lineage). **`tier_richness` legitimately DIFFERS from TC-01** — at Enterprise `tier_richness.music_swells == 3`, `variants_planned == 5`, `b_roll == 9` (the declared tier ceiling) — because `tier_richness` is excluded from the converged block set. But the **authored** `edit_plan.music_swell_map` length stays `== 2` (byte-identical to TC-01) — the authored plan converges even though the tier ceiling does not. Validate the declared ceiling via `tier_richness` and the authored count via `edit_plan` separately.

### TC-03 — `case-03-coverage-gap-fail` → `errorEnvelope` `incomplete_shot_coverage` · route to **Ingest**
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **route_back_to:** `ingest-agent`.
- **This fixture exercises the defensive coverage re-confirm (Step 3 / Check #3).** Edit Director re-verifies `coverage_complete == true` and `missing_shots == []` even though Ingest already cleared it — a coverage hole that survived to the authoring layer routes back to **Ingest** (the asset-side owner), NOT to a re-shoot. `incomplete_shot_coverage` is the asset-side coverage code.
- **Hard checks:**
  - `output_type == "errorEnvelope"`, `verdict == "fail"`.
  - `failure_code == "incomplete_shot_coverage"`.
  - `failed_check_id == 3` (Step 3 / coverage + mappability confirm).
  - `route_back_to == "ingest-agent"` (the asset-side owner — NOT `production-coord-agent`, NOT a reshoot).
  - `attempts == 1` (a real coverage gap is a valid verdict on first construction — NOT a self-QC regenerate loop).
  - `metadata.production_mode == "A"`.
  - `detail.unmapped_beats` present and non-empty (names the beat(s) with no covering shot).
  - `detail.violation` present (names the coverage hole).
  - `detail.recovery_path` present (re-confirm coverage at Ingest + route-to-Ingest language).
  - `human_review_required == true` (top-level AND metadata) — even a clear coverage gap is a recommendation, never an autonomous quarantine.
- **Lineage:** 8-tuple, position [3] == `productionplan-…` (Mode A chain).
- **Negative checks:** NO `edit_plan`, NO `structure_check`, NO `brand_edit_check`, NO `coverage_remap` success-shape, NO `edit_plan_firewall_pass_9`, NO `mode_blind_confirm`, NO `tier_richness`, NO `handoff_targets` on the error branch (those are success-only fields).

### TC-04 — `case-04-brand-edit-rule-conflict` → `errorEnvelope` `brand_edit_rule_conflict` · route to **Production Coord** · **HARD fail, NOT `revise`**
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **route_back_to:** `production-coord-agent`.
- **This fixture proves the hard/soft brand-rule split.** The input demands a transition the brand ruleset forbids absolutely (a fade — "hard cuts ONLY, zero fades"). A HARD brand-rule that cannot be satisfied is `brand_edit_rule_conflict` (`fail`) — it is **NOT** a `revise` (the soft-tension verdict). A fade can NEVER survive to `plan_ready`. This is the discriminator between the two soft/hard paths: a soft creative tension → `revise` (success branch); a hard-rule violation → `fail` (error branch).
- **Hard checks:**
  - `output_type == "errorEnvelope"`, `verdict == "fail"` (NOT `revise` — a hard-rule conflict is never deferred to the operator as a soft call).
  - `failure_code == "brand_edit_rule_conflict"`.
  - `failed_check_id == 7` (Step 8 brand check / the §7 hard-rule gate — fixture binds id 7).
  - `route_back_to == "production-coord-agent"` (the upstream owner of the conflicting creative directive).
  - `attempts == 1`.
  - `detail.rule_violated` present (names the hard rule — the hard-cuts-only / no-fades rule).
  - `detail.brand_edit_check` present (the failing check block, showing `hard_cuts_only: false`).
  - `detail.violation` present; `detail.recovery_path` present (re-direct without the fade + route language).
  - `human_review_required == true` (both).
- **Negative checks:** NO success-only fields; NO `handoff_targets`. **Crucially: `verdict != "revise"`** — if the agent emits `revise` for a hard-rule conflict it has misclassified the soft/hard split → FAIL.

### TC-05 — `case-05-authored-text-firewall-breach` → `errorEnvelope` `edit_plan_firewall_breach` · route **null** · **GATING FIXTURE (the 9th-pass self-authored catch)**
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **route_back_to:** `null`.
- **This is the most important fixture in the portfolio — Edit Director's reason to exist as the 9th firewall.** Eight prior passes scanned text the pipeline RECEIVED; Edit Director is the first to scan text it WRITES ITSELF. The input's upstream content is clean; the breach is created when the agent AUTHORS reel-facing copy (lower-thirds) from a Script `on_screen_text` block that carries injected entity tokens (`built for operators like sln` → token `sln`; `see holdcogroup.com` → token `holdcogroup.com`). The 9th-pass firewall (Step 9, AFTER authoring) must catch both. **A v1.0 LOCK is BLOCKED if TC-05 does not catch both injected tokens.** Because the leak is self-authored, there is no upstream stage to route back to — `route_back_to: null`.
- **Hard checks:**
  - `output_type == "errorEnvelope"`, `verdict == "fail"`.
  - `failure_code == "edit_plan_firewall_breach"`.
  - `failed_check_id == 4` (the firewall pass — Check #4 in the §6 self-QC numbering / Step 9 in the loop).
  - `route_back_to == null` (the leak is self-authored — no upstream is at fault; do NOT route to `style-replication-agent` or `ingest-agent`).
  - `attempts == 1`.
  - `detail.edit_plan_firewall_pass_9.status == "breach"` AND `detail.edit_plan_firewall_pass_9.hits == 2` (both tokens caught — a single-hit catch is an UNDER-report and must FAIL the gate).
  - `detail.authored_fields` is a list naming BOTH offending authored fields + the token each carried (the `sln` hit AND the `holdcogroup.com` hit). *(This is the forensic field where banned tokens legitimately appear — the breach report quoting the offenders. The §5 validator EXCLUDES the entire error-branch `detail` object from its firewall walk; every OTHER emitted string must be clean.)*
  - `detail.violation` present; `detail.recovery_path` present (strip tokens + re-author within brand-safe copy + "9th-pass authored-text catch" language).
  - `metadata.production_mode == "B"`.
  - `human_review_required == true` (both).
- **Negative checks:** NO success-only fields; NO `handoff_targets`.

### §3.6 — OPTIONAL adversarial probe A: the `revise` success-side verdict (NOT part of the 5/5 LOCK count)
- **Purpose:** exercise the **first fleet success-side third verdict** live. The 5 LOCK fixtures cover `plan_ready` ×2 and `fail` ×3 but do not exercise `revise` live (the Day 64 `validate.py` guards it at the schema layer). This probe confirms the LIVE agent produces a well-formed `revise` — a `successEditPlan`-shaped payload with a SOFT brand bool false + a `revise_rationale` + `route_back_to: null` — rather than collapsing it to a `fail` or silently overriding the soft rule.
- **How to run:** take `test-cases/case-01-mode-a-origin-pro-plan-ready/input.json`, then **introduce a SOFT-rule tension** that cannot be auto-resolved without a creative call — e.g. craft the Script beat map so two emotional beats legitimately compete (forcing the `one_emotional_beat` soft rule into tension) OR pack a text reveal slightly inside the 8-second ceiling such that honoring it costs a beat. Do NOT introduce a HARD-rule violation (that would correctly route to `fail`). Save as `validation/llm-out/probe-revise-input.json`. Run with the same system prompt + settings.
- **Expected:** `output_type == "successEditPlan"`, `verdict == "revise"`, `route_back_to == null`, a non-empty `revise_rationale`, exactly ONE of the two SOFT booleans (`one_text_reveal_per_8s` / `one_emotional_beat`) `false` while ALL 5 HARD `brand_edit_check` booleans remain `true`, the firewall still `pass`/`hits 0`, `mode_blind_confirm.production_mode_read: false`, `human_review_required: true`. The agent must NOT emit `plan_ready` (a soft tension is unresolved) and must NOT emit `fail` (no hard rule is violated).
- **Scoring:** PASS/FAIL recorded separately in §9 as an adversarial note. A failure here does NOT block the LOCK on its own (the schema guard already proves `revise` is reachable + well-formed), but a *malformed* `revise` (a HARD bool false, a missing rationale, a non-null route, or a misclassification to `fail`/`plan_ready`) is a **red flag** warranting a Day 66 review before ceremony.

### §3.7 — OPTIONAL adversarial probe B: slot-11 `edit_director_agent_failed` (NOT part of the 5/5 LOCK count)
- **Purpose:** exercise the self-QC 2-strike exhaustion catch-all live. The schema already guards it (Day 64 `validate.py`: `attempts: const 2` + `route_back_to: const null` + `verdict: const fail` accepted; `attempts==1` rejected; non-null route rejected). This probe confirms the LIVE agent reaches the slot honestly under a genuinely irreconcilable input rather than fabricating a verdict.
- **How to run:** take `test-cases/case-01-mode-a-origin-pro-plan-ready/input.json`, then **corrupt the inputs into self-contradiction** — e.g. declare a shot duration that makes the 45–75 s band unreachable no matter how the cut is trimmed AND remove a Storyboard `frame_language` for a covered shot, so neither a clean cut-order nor a clean structure_check can be constructed. Save as `validation/llm-out/probe-slot11-input.json`. Run with the same system prompt + settings.
- **Expected:** `errorEnvelope`, `failure_code == "edit_director_agent_failed"`, `attempts == 2`, `route_back_to == null`, `verdict == "fail"`, `human_review_required == true`. The agent must NOT emit a `plan_ready`/`revise` and must NOT route-back to an upstream agent (no upstream is at fault for a self-QC exhaustion).
- **Scoring:** PASS/FAIL recorded separately in §9. A failure here does NOT block the LOCK on its own (the schema guard already proves the slot is reachable + well-formed), but a *malformed* slot-11 (e.g. `attempts==1`, a non-null route, or a `plan_ready`) is a **red flag** warranting a Day 66 patch review before ceremony.

### Cross-fixture invariants (apply to all 5 + the probes)
- `metadata.agent_id == "edit-director-agent"` on every output (success or error).
- `metadata.agent_version == "1.0"` on every output.
- `metadata.edit_plan_class == "primary_9x16"` on every output.
- `metadata.render_dispatched == false` on every output (schema `const false` — the no-render honesty contract; a `true` anywhere is forged provenance and a hard FAIL).
- `metadata.runtime_environment_class == "staging"` for dry-run runs.
- `metadata.plan_evidence_hash` matches `^[a-f0-9]{64}$` on every output (tamper-evident; shape-checked, not value-checked).
- `metadata.parent_chain` is a well-formed 5-, 6-, 7-, or 8-tuple (positions [0]=`brief-`, [1]=`script-`, [2]=`storyboard-`, [3]=`productionplan-…`|`mode-c-direct`|`ai-video-gen-…`, [4]=UUID; optional [5]=`preflight-…`, optional [6]=UUID `asset_manifest_id`, optional [7]=UUID `edit_plan_id`). A 4-tuple and a 9-tuple are rejected.
- `reel_ref.edit_plan_id` is a UUID and equals `metadata.edit_plan_id` (and, on the 8-tuple, equals `parent_chain[7]`); `reel_ref.asset_manifest_id` equals `metadata` / `parent_chain[6]` where present.
- top-level `human_review_required == true` AND `metadata.human_review_required == true` on every output (recommend-don't-approve, schema `const true`).
- `cost_incurred_usd <= 0.04` (top-level) on every output (Hard Rule #2 / #10 — Edit Director carries no engine/render cost; its only cost is its own token spend ≈ $0.04).
- On the **success branch**, `mode_blind_confirm.production_mode_read == false` (schema `const false` — the mode-blind contract; a `true` is a convergence break and a hard FAIL).
- Zero entity-firewall hits + zero banned-vocab (token-boundary, case-insensitive) across every emitted string, with one legitimate-naming exclusion: the error branch's `detail` object (TC-05's `detail.authored_fields` + `detail.recovery_path` quote the offending tokens for forensics). The `detail.…hits` count is asserted independently. (REINVENTED IS allowed — pilot brand.)
- Zero approval language (`approved`, `approved for cut`, `cleared for cut`, `cleared`, `published`) anywhere.
- **NO `hold` verdict and NO `reshoot` verdict** on any output (deliberate divergences from Ingest — §6.4 / SKILL verdict model).

---

## §4 Why there is NO engine-stub block (the no-engine / no-render difference)

The production agents' runbooks (Day 11 Script, Day 19 Production Coord, Day 27 AI Video Gen, Day 36 Style Replication) appended an `<engine_dry_run_mode>` fence to the user message, because those agents dispatch generative engines and the dry-run fence replaces the engine surface with stubbed responses. The Day 47 QC Pre-flight and Day 57 Ingest runbooks dropped that block — neither dispatches an engine.

**Edit Director is the same: no engine AND no media render** (Hard Rule #2 — "no render, no transcode, no conform, no EDL execution, no frame-accurate trim, no API dispatch … you produce in_ms/out_ms cut points against DECLARED shot durations — you do not touch pixels … set `render_dispatched: false` in every plan"). Everything the agent directs is already inside the input object:

- `asset_manifest` — the Ingest precondition gate (Step 1; verdict must be `pass`/`successAssetManifest` or carry Lever-3 sign-off).
- The **mode-agnostic `asset_bundle`** — `raw_footage[]` (with `shot_ref` + `duration_sec`), `audio[]`, `assets_pulled[]`, `music_bed`. There is NO mode branch — the manifest shape is identical for A/B/C (the convergence contract).
- The denormalized **Script beat map** (audio_track, captions, pace_markers, on_screen_text, structure, cta) + **Storyboard shot vocabulary** (frame_language per shot) — the creative intent Edit Director LAYS onto the cut (Steps 4–6).
- `production_plan` platform/format target + the brief length band — the structure/duration surface (Step 8).
- `metadata.parent_chain` (7-tuple inbound) + accumulated `qc_pre_flags[]` — lineage + the 6-agent floor record.

There is nothing to stub and nothing to render. The user message is the **bare input object**. The agent reasons over it, runs the 11-step direction loop, and emits one of two branches (`successEditPlan` with `plan_ready`/`revise`, or `errorEnvelope`). `render_dispatched: const false` is the honesty contract: the agent never claims a render it did not dispatch (that is Editor's job, position 11). This is what keeps Edit Director at $0 engine/render spend — its only cost is its own ≈$0.04 token inference.

**Runtime-computed fields (hash, timestamps, latency, UUIDs):** `plan_evidence_hash` is a SHA-256 the agent computes honestly over its own `edit_plan` + `brand_edit_check` block; `timestamp_utc` + `latency_ms` are runtime telemetry; `edit_plan_id` / `asset_manifest_id` are UUIDs. In a Workbench run these will NOT match the fixture's frozen values, and that is correct. The §5 validator checks `plan_evidence_hash` for SHAPE (`^[a-f0-9]{64}$`) only, and does not assert timestamp/latency/UUID values against the fixture. For the TC-01/TC-02 convergence proof it compares only the six authored blocks (`edit_plan`, `coverage_remap`, `structure_check`, `brand_edit_check`, `edit_plan_firewall_pass_9`, `mode_blind_confirm`) — none of which carries a per-case UUID — so no canonicalization is needed there. Do not flag a hash/timestamp/UUID mismatch against the fixture as a failure — only a malformed shape, or a broken convergence equality, is a failure.

---

## §5 Post-run validator (paste-and-run)

After saving all 5 outputs to `validation/llm-out/case-NN-output.json`:

```bash
cd "~/ars/skills/edit-director-agent"

python3 << 'PYEOF'
import json, re, sys, copy
from jsonschema import Draft202012Validator
from pathlib import Path

ROOT = Path(".")
OUT_SCHEMA = json.loads((ROOT / "schemas" / "output.schema.json").read_text())
v = Draft202012Validator(OUT_SCHEMA)

# 11-entry canonical entity firewall list (token-boundary, case-insensitive)
FIREWALL = ["holdco group","hc","4821 main","4821","site-c-brand","6315",
            "sln","sln cuts","sln shear","sln salon","salonb","shear & cuts",
            "retail supply","principal holdco","principal","npox","community nonprofit",
            "nonprofit leader a","partner brand","holdcogroup.com"]
BANNED    = ["babe","boss babe","girl boss","girlboss","she-eo","mompreneur"]
APPROVAL  = ["approved for cut","cleared for cut","approved","cleared","published"]

UUID_RE   = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
SNAKE_RE  = re.compile(r"^[a-z][a-z0-9_]{0,63}$")
ARS_RE    = re.compile(r"^ars://")
DUR_LO, DUR_HI = 45000, 75000

def word_hit(term, text):
    # token-boundary, case-insensitive — "hc" never matches inside "image"
    return re.search(r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])", text) is not None

EXPECT = {
  "case-01-mode-a-origin-pro-plan-ready": {
    # music_swells = the tier_richness DECLARED ceiling (Pro=2); authored_swells = the actual
    # edit_plan.music_swell_map length (pinned equal across the convergence twins by design).
    "branch": "successEditPlan", "verdict": "plan_ready",
    "tier": "pro", "mode": "A", "shots": 6, "music_swells": 2, "variants": 4, "authored_swells": 2,
  },
  "case-02-mode-c-enterprise-plan-ready": {
    # tier_richness declares Enterprise (music_swells 3 / variants 5) — but the AUTHORED edit_plan is
    # byte-identical to TC-01 (authored_swells 2): tier_richness is excluded from the converged block
    # set, so the tier ceiling differs while the authored plan does not. This is the convergence proof.
    "branch": "successEditPlan", "verdict": "plan_ready",
    "tier": "enterprise", "mode": "C", "shots": 6, "music_swells": 3, "variants": 5, "authored_swells": 2,
    "lineage_pos3": "mode-c-direct", "convergence_twin": "case-01-mode-a-origin-pro-plan-ready",
  },
  "case-03-coverage-gap-fail": {
    "branch": "errorEnvelope", "verdict": "fail",
    "failure_code": "incomplete_shot_coverage", "failed_check_id": 3,
    "route_back_to": "ingest-agent", "attempts": 1, "mode": "A",
  },
  "case-04-brand-edit-rule-conflict": {
    "branch": "errorEnvelope", "verdict": "fail",
    "failure_code": "brand_edit_rule_conflict", "failed_check_id": 7,
    "route_back_to": "production-coord-agent", "attempts": 1,
  },
  "case-05-authored-text-firewall-breach": {
    "branch": "errorEnvelope", "verdict": "fail",
    "failure_code": "edit_plan_firewall_breach", "failed_check_id": 4,
    "route_back_to": None, "attempts": 1, "min_hits": 2, "mode": "B",
  },
}

def collect_strings(obj, acc):
    if isinstance(obj, str):
        acc.append(obj)
    elif isinstance(obj, dict):
        for k, val in obj.items():
            acc.append(k); collect_strings(val, acc)
    elif isinstance(obj, list):
        for item in obj: collect_strings(item, acc)

outputs = {}
results = []
for case_id, exp in EXPECT.items():
    f = ROOT / "validation" / "llm-out" / f"{case_id}-output.json"
    if not f.exists():
        results.append((case_id, "MISSING", "no LLM output file")); continue
    try:
        out = json.loads(f.read_text())
    except Exception as e:
        results.append((case_id, "JSON_PARSE_ERR", str(e)[:160])); continue
    outputs[case_id] = out

    # 1. schema gate
    errs = list(v.iter_errors(out))
    if errs:
        results.append((case_id, "SCHEMA_FAIL", f"{len(errs)} errs · first: {errs[0].message[:150]}")); continue

    # 2. branch detection
    branch = out.get("output_type")
    if branch != exp["branch"]:
        results.append((case_id, "WRONG_BRANCH", f"got {branch!r}, expected {exp['branch']!r}")); continue

    fails = []
    meta = out.get("metadata", {}) or {}

    # ---- universal metadata + recommend-don't-approve + no-render ----
    if out.get("verdict") != exp["verdict"]:
        fails.append(f"verdict={out.get('verdict')!r}, expected {exp['verdict']!r}")
    if out.get("verdict") in ("hold", "reshoot"):
        fails.append(f"{out.get('verdict')!r} verdict emitted — forbidden for Edit Director")
    if meta.get("agent_id") != "edit-director-agent":
        fails.append(f"metadata.agent_id={meta.get('agent_id')!r}")
    if meta.get("agent_version") != "1.0":
        fails.append(f"metadata.agent_version={meta.get('agent_version')!r}")
    if meta.get("edit_plan_class") != "primary_9x16":
        fails.append(f"metadata.edit_plan_class={meta.get('edit_plan_class')!r}")
    if meta.get("render_dispatched") is not False:
        fails.append(f"metadata.render_dispatched={meta.get('render_dispatched')!r}, expected false (forged-provenance guard)")
    if out.get("human_review_required") is not True:
        fails.append(f"top-level human_review_required={out.get('human_review_required')!r}, expected true")
    if meta.get("human_review_required") is not True:
        fails.append(f"metadata.human_review_required={meta.get('human_review_required')!r}, expected true")
    if (out.get("cost_incurred_usd") or 0) > 0.04:
        fails.append(f"cost_incurred_usd={out.get('cost_incurred_usd')!r}, expected <= 0.04")
    peh = meta.get("plan_evidence_hash")
    if not (isinstance(peh, str) and SHA256_RE.match(peh)):
        fails.append(f"metadata.plan_evidence_hash bad shape: {peh!r}")
    if "mode" in exp and meta.get("production_mode") != exp["mode"]:
        fails.append(f"metadata.production_mode={meta.get('production_mode')!r}, expected {exp['mode']!r}")

    # ---- parent_chain shape (5/6/7/8-tuple, additive hold) ----
    pc = meta.get("parent_chain")
    if not (isinstance(pc, list) and len(pc) in (5, 6, 7, 8)):
        fails.append(f"parent_chain not a 5/6/7/8-tuple: {pc!r}")
    else:
        if not str(pc[0]).startswith("brief-"):      fails.append(f"parent_chain[0]={pc[0]!r}")
        if not str(pc[1]).startswith("script-"):     fails.append(f"parent_chain[1]={pc[1]!r}")
        if not str(pc[2]).startswith("storyboard-"): fails.append(f"parent_chain[2]={pc[2]!r}")
        if not (str(pc[3]).startswith("ai-video-gen-") or pc[3] == "mode-c-direct"
                or str(pc[3]).startswith("productionplan-")):
            fails.append(f"parent_chain[3]={pc[3]!r}")
        if not UUID_RE.match(str(pc[4])):            fails.append(f"parent_chain[4] not a UUID: {pc[4]!r}")
        if len(pc) >= 6 and not str(pc[5]).startswith("preflight-"):
            fails.append(f"parent_chain[5]={pc[5]!r}, expected preflight-…")
        if len(pc) >= 7 and not UUID_RE.match(str(pc[6])):
            fails.append(f"parent_chain[6] not a UUID: {pc[6]!r}")
        if len(pc) == 8 and not UUID_RE.match(str(pc[7])):
            fails.append(f"parent_chain[7] not a UUID: {pc[7]!r}")
    if "lineage_pos3" in exp and isinstance(pc, list) and len(pc) >= 4 and pc[3] != exp["lineage_pos3"]:
        fails.append(f"parent_chain[3]={pc[3]!r}, expected {exp['lineage_pos3']!r}")

    # ---- reel_ref.edit_plan_id == metadata.edit_plan_id (== parent_chain[7] on 8-tuple) ----
    rr = out.get("reel_ref", {}) or {}
    eid = rr.get("edit_plan_id")
    if not (isinstance(eid, str) and UUID_RE.match(eid)):
        fails.append(f"reel_ref.edit_plan_id not a UUID: {eid!r}")
    elif meta.get("edit_plan_id") != eid:
        fails.append(f"edit_plan_id mismatch reel_ref={eid!r} vs metadata={meta.get('edit_plan_id')!r}")
    elif isinstance(pc, list) and len(pc) == 8 and pc[7] != eid:
        fails.append(f"parent_chain[7]={pc[7]!r} != edit_plan_id {eid!r}")

    # ---- firewall / banned-vocab / approval walk (error-branch detail excluded) ----
    walk_obj = json.loads(json.dumps(out))  # deep copy
    if branch == "errorEnvelope":
        walk_obj.pop("detail", None)   # forensic field legitimately quotes tokens
    strings = []; collect_strings(walk_obj, strings)
    joined = "\n".join(strings).lower()
    for t in FIREWALL:
        if word_hit(t, joined): fails.append(f"entity_firewall_leak: {t!r}")
    for t in BANNED:
        if word_hit(t, joined): fails.append(f"banned_vocab_leak: {t!r}")
    for t in APPROVAL:
        if word_hit(t, joined): fails.append(f"approval_language_leak: {t!r}")

    if branch == "successEditPlan":
        if meta.get("tier") != exp["tier"]:
            fails.append(f"metadata.tier={meta.get('tier')!r}, expected {exp['tier']!r}")
        # AND-of-11-gates (false-plan-ready guard) -----------------------------
        fw = out.get("edit_plan_firewall_pass_9", {}) or {}
        if fw.get("status") != "pass" or fw.get("hits") != 0:
            fails.append(f"edit_plan_firewall_pass_9={fw!r} (need status pass, hits 0)")
        if (fw.get("authored_text_fields_scanned") or 0) < 1:
            fails.append(f"firewall authored_text_fields_scanned not >0: {fw!r}")
        bec = out.get("brand_edit_check", {}) or {}
        for k in ("hard_cuts_only","one_text_reveal_per_8s","one_emotional_beat",
                  "lower_thirds_lowercase_left","captions_within_char_limit",
                  "no_reel_level_sales_cta","end_card_present"):
            if bec.get(k) is not True:
                fails.append(f"brand_edit_check.{k}={bec.get(k)!r}, expected true on plan_ready")
        sc = out.get("structure_check", {}) or {}
        if sc.get("hook_window_ok") is not True: fails.append("structure_check.hook_window_ok != true")
        if sc.get("cta_internal_question_ok") is not True: fails.append("structure_check.cta_internal_question_ok != true")
        if sc.get("duration_in_band") is not True: fails.append("structure_check.duration_in_band != true")
        tdm = sc.get("total_duration_ms")
        if not (isinstance(tdm,(int,float)) and DUR_LO <= tdm <= DUR_HI):
            fails.append(f"structure_check.total_duration_ms={tdm!r} out of 45000-75000 band")
        if (sc.get("body_beats") or 0) < 1: fails.append(f"structure_check.body_beats={sc.get('body_beats')!r} < 1")
        cr = out.get("coverage_remap", {}) or {}
        if cr.get("unmapped_shot_refs") != [] or cr.get("unmapped_beats") != []:
            fails.append(f"coverage_remap unmapped not empty: {cr!r}")
        if cr.get("shots_required") != exp["shots"] or cr.get("shots_mapped") != exp["shots"]:
            fails.append(f"coverage_remap counts={cr!r}, expected {exp['shots']}/{exp['shots']}")
        mb = out.get("mode_blind_confirm", {}) or {}
        if mb.get("production_mode_read") is not False:
            fails.append(f"mode_blind_confirm.production_mode_read={mb.get('production_mode_read')!r}, expected false (convergence contract)")
        if mb.get("consumed") != "mode_agnostic_manifest":
            fails.append(f"mode_blind_confirm.consumed={mb.get('consumed')!r}")
        # canonical edit_plan shape ------------------------------------------
        ep = out.get("edit_plan", {}) or {}
        EXPECT_KEYS = {"cut_order","pacing_bpm","cut_rhythm","caption_style","caption_lines",
                       "lower_thirds","transitions","music_bed","music_swell_map","end_card"}
        if set(ep.keys()) != EXPECT_KEYS:
            fails.append(f"edit_plan key set != canonical Blueprint 4.9 shape: {sorted(ep.keys())}")
        co = ep.get("cut_order") or []
        if not co or len(co) != exp["shots"]:
            fails.append(f"cut_order len={len(co)}, expected {exp['shots']}")
        if len(co) > 12:
            fails.append(f"cut_order len {len(co)} > 12 tier ceiling")
        for i, c in enumerate(co):
            for key in ("shot_ref","in_ms","out_ms","frame_language"):
                if key not in c: fails.append(f"cut_order[{i}] missing {key}")
        tr = (ep.get("transitions") or "").lower()
        if "hard cuts only" not in tr:
            fails.append(f"transitions not hard-cuts-only: {ep.get('transitions')!r}")
        for bad_t in ("fade","wipe","zoom"):
            # allowed only inside the 'zero fades/zero wipes/zero zooms' negation
            if re.search(r"(?<!zero )" + bad_t, tr) and ("zero " + bad_t) not in tr:
                fails.append(f"transitions enables a {bad_t}: {ep.get('transitions')!r}")
        for j, cl in enumerate(ep.get("caption_lines") or []):
            t = cl.get("text","")
            if len(t) > 22: fails.append(f"caption_lines[{j}] len {len(t)} > 22: {t!r}")
            if t != t.lower(): fails.append(f"caption_lines[{j}] not lowercase: {t!r}")
            if cl.get("line") not in (1,2): fails.append(f"caption_lines[{j}].line={cl.get('line')!r}")
        for j, lt in enumerate(ep.get("lower_thirds") or []):
            if lt.get("case") != "lowercase": fails.append(f"lower_thirds[{j}].case={lt.get('case')!r}")
            if lt.get("align") != "left": fails.append(f"lower_thirds[{j}].align={lt.get('align')!r}")
            c = lt.get("content","")
            if c != c.lower(): fails.append(f"lower_thirds[{j}].content not lowercase: {c!r}")
        if not ARS_RE.match(str(ep.get("music_bed",""))):
            fails.append(f"music_bed not ars://: {ep.get('music_bed')!r}")
        # AUTHORED swell-map length is pinned by the convergence design (equal across the twins),
        # NOT by the tier ceiling — tier_richness.music_swells (declared) is checked separately below.
        if len(ep.get("music_swell_map") or []) != exp["authored_swells"]:
            fails.append(f"edit_plan.music_swell_map len={len(ep.get('music_swell_map') or [])}, expected authored {exp['authored_swells']}")
        ec = ep.get("end_card", {}) or {}
        if "REINVENTED" not in (ec.get("line") or "") or "build on purpose" not in (ec.get("line") or ""):
            fails.append(f"end_card.line wrong copy: {ec.get('line')!r}")
        if ec.get("font_class") != "serif_display": fails.append(f"end_card.font_class={ec.get('font_class')!r}")
        if ec.get("hold_ms") != 1500: fails.append(f"end_card.hold_ms={ec.get('hold_ms')!r}")
        if ec.get("doubles_as_thumbnail") is not True: fails.append("end_card.doubles_as_thumbnail != true")
        # tier_richness ------------------------------------------------------
        tre = out.get("tier_richness", {}) or {}
        if tre.get("tier") != exp["tier"]: fails.append(f"tier_richness.tier={tre.get('tier')!r}")
        if tre.get("music_swells") != exp["music_swells"]: fails.append(f"tier_richness.music_swells={tre.get('music_swells')!r}")
        if tre.get("variants_planned") != exp["variants"]: fails.append(f"tier_richness.variants_planned={tre.get('variants_planned')!r}")
        # ingest precondition ------------------------------------------------
        ip = out.get("ingest_precondition_check", {}) or {}
        if not (ip.get("verdict_observed") == "pass" or ip.get("lever3_signoff_present") is True):
            fails.append(f"ingest_precondition_check not satisfied: {ip!r}")
        # handoff ------------------------------------------------------------
        if out.get("handoff_targets") != ["editor-agent"]:
            fails.append(f"handoff_targets={out.get('handoff_targets')!r}, expected ['editor-agent']")
        # qc_pre_flags -------------------------------------------------------
        qf = out.get("qc_pre_flags") or []
        if len(qf) < 4: fails.append(f"qc_pre_flags count={len(qf)} < 4")
        for j, fl in enumerate(qf):
            if not (isinstance(fl, str) and SNAKE_RE.match(fl)):
                fails.append(f"qc_pre_flags[{j}] not snake_case: {fl!r}")

    else:  # errorEnvelope
        if out.get("failure_code") != exp["failure_code"]:
            fails.append(f"failure_code={out.get('failure_code')!r}, expected {exp['failure_code']!r}")
        if out.get("failed_check_id") != exp["failed_check_id"]:
            fails.append(f"failed_check_id={out.get('failed_check_id')}, expected {exp['failed_check_id']}")
        if out.get("attempts") != exp["attempts"]:
            fails.append(f"attempts={out.get('attempts')}, expected {exp['attempts']}")
        if out.get("route_back_to") != exp["route_back_to"]:
            fails.append(f"route_back_to={out.get('route_back_to')!r}, expected {exp['route_back_to']!r}")
        detail = out.get("detail", {}) or {}
        if not (detail.get("recovery_path") or "").strip():
            fails.append("detail.recovery_path empty/absent")
        if not (detail.get("violation") or "").strip():
            fails.append("detail.violation empty/absent")
        if exp["failure_code"] == "incomplete_shot_coverage":
            if not detail.get("unmapped_beats"):
                fails.append("detail.unmapped_beats empty/absent on coverage-gap fail")
        if exp["failure_code"] == "brand_edit_rule_conflict":
            if not (detail.get("rule_violated") or "").strip():
                fails.append("detail.rule_violated empty/absent")
            bec = detail.get("brand_edit_check", {}) or {}
            if bec.get("hard_cuts_only") is not False:
                fails.append(f"detail.brand_edit_check.hard_cuts_only={bec.get('hard_cuts_only')!r}, expected false")
        if exp["failure_code"] == "edit_plan_firewall_breach":
            fwd = detail.get("edit_plan_firewall_pass_9", {}) or {}
            if fwd.get("status") != "breach":
                fails.append(f"detail firewall status={fwd.get('status')!r}, expected breach")
            if (fwd.get("hits") or 0) < exp["min_hits"]:
                fails.append(f"detail firewall hits={fwd.get('hits')}, expected >= {exp['min_hits']} (under-report = FAIL)")
            if not detail.get("authored_fields"):
                fails.append("detail.authored_fields empty/absent (must name both offending fields)")
        # negative checks: no success-only fields on error branch
        for forbidden in ("edit_plan","structure_check","brand_edit_check","coverage_remap",
                          "edit_plan_firewall_pass_9","mode_blind_confirm","tier_richness",
                          "handoff_targets","ingest_precondition_check"):
            if forbidden in out:
                fails.append(f"success-only field {forbidden!r} present on error branch")

    results.append((case_id, "PASS" if not fails else "FAIL", "all checks green" if not fails else " || ".join(fails[:8])))

# ---- TC-01/TC-02 mode-blind convergence proof (byte-shape-identical authored plan) ----
conv_note = ""
a = outputs.get("case-01-mode-a-origin-pro-plan-ready")
b = outputs.get("case-02-mode-c-enterprise-plan-ready")
CONV_KEYS = ["edit_plan","coverage_remap","structure_check","brand_edit_check",
             "edit_plan_firewall_pass_9","mode_blind_confirm"]
if a and b and a.get("output_type") == "successEditPlan" and b.get("output_type") == "successEditPlan":
    same = all(a.get(k) == b.get(k) for k in CONV_KEYS)
    modes_differ = a.get("metadata",{}).get("production_mode") != b.get("metadata",{}).get("production_mode")
    both_blind = a.get("mode_blind_confirm",{}).get("production_mode_read") is False \
                 and b.get("mode_blind_confirm",{}).get("production_mode_read") is False
    if same and modes_differ and both_blind:
        conv_note = "CONVERGENCE PROOF OK — TC-01(A)/TC-02(C) authored plan byte-shape-identical, modes differ, both mode-blind."
    else:
        reason = []
        if not same: reason.append("authored blocks diverge (mode leaked OR authored-copy drift — re-run at temp 0.2/0.0 before patching)")
        if not modes_differ: reason.append("production_mode equal (proof void)")
        if not both_blind: reason.append("a fixture failed mode-blind self-attestation")
        conv_note = "CONVERGENCE PROOF FAIL — " + " ; ".join(reason)
        results = [(cid, ("FAIL" if cid in ("case-01-mode-a-origin-pro-plan-ready","case-02-mode-c-enterprise-plan-ready") and st=="PASS" else st),
                    (note if cid not in ("case-01-mode-a-origin-pro-plan-ready","case-02-mode-c-enterprise-plan-ready") else (note + " || convergence proof failed")))
                   for cid, st, note in results]
else:
    conv_note = "CONVERGENCE PROOF SKIPPED — one or both plan_ready cases missing/non-success."

print()
print("=" * 92)
print("Day 65 LLM Test Runbook — Edit Director Agent v1.0 — VALIDATOR RESULTS")
print("=" * 92)
pass_n = 0
for case_id, status, note in results:
    icon = "PASS " if status == "PASS" else "FAIL "
    print(f"  {icon} {case_id:44s} :: {status:14s} {note[:200]}")
    if status == "PASS": pass_n += 1
print("-" * 92)
print(f"  {conv_note}")
print("-" * 92)
print(f"  Aggregate: {pass_n}/{len(results)} PASS")
if pass_n == len(results) and "OK" in conv_note:
    print("  >> Edit Director v1.0 LOCK GATE = OPEN.")
    print("  >> HARD GATES: requires AI Video Gen + Style Replication + QC Pre-flight + Ingest v1.0 LOCKs CLOSED first (dependency order).")
    print("  >> Ceremony: flip v1.0-LOCK-CANDIDATE-day-61 -> v1.0-LOCKED in SKILL.md frontmatter + Notion + dashboard chip.")
else:
    held = len(results) - pass_n
    print(f"  >> Edit Director v1.0 LOCK GATE = HELD. {held} failure(s) and/or convergence break require patch.")
    print(f"  >> Patch protocol: SKILL.md system prompt ONLY (schemas LOCKED Day 62; no schema edits without a v1.0.x bump).")
print("=" * 92)
sys.exit(0 if (pass_n == len(results) and "OK" in conv_note) else 1)
PYEOF
```

Save the printed output: append ` > validation/llm-out/run-results-2026-06-23.txt 2>&1` to the bash command above, OR screenshot it.

**Probes (optional, §3.6 / §3.7):** save the `revise` probe to `validation/llm-out/probe-revise-output.json` and the slot-11 probe to `validation/llm-out/probe-slot11-output.json` and spot-check by hand per the expected-field lists above. Neither is scored by the validator (which loops the 5 LOCK fixtures) — record both in §9.

---

## §6 Open Question #65 resolution — dry-run vs live + the 8-tuple

**Decision:** **dry-run mode is the v1.0 LOCK gate** — and for Edit Director, dry-run and live are functionally identical.

**Why:**
- Edit Director dispatches **no generative engine and renders no media** (Hard Rule #2 — joins QC Pre-flight + Ingest as the no-engine agents; like them there is no render call, no transcode, no EDL execution, no frame trim, no vendor API). "Live mode" for the production agents means real engine spend on non-deterministic outputs; for Edit Director there is no such surface — it produces `in_ms`/`out_ms` cut points against DECLARED shot durations.
- v1.0 LOCK proves the agent's **plan-authoring discipline + schema compliance + the 9th-pass authored-text firewall (self-authored surface) + the brand-edit ruleset (zero-tolerance hard rules / soft-tension `revise`) + the structure/duration math + the mode-blind convergence (TC-01/TC-02) + verdict-route correctness + recommend-don't-approve discipline + the no-render honesty contract.** None require any engine call or any render. They require Opus to consume the Asset Manifest + denormalized creative intent and emit a schema-valid, contract-compliant Edit Plan.
- Cost: dry-run = ~$4.00 in Opus tokens (≤ $5.60 with both probes). There is no meaningfully different "live" number — the agent spends $0.00 of engine money and $0.00 of render money in every mode.

**The 8-tuple `parent_chain` (Decision D6 / Item 11 — TRIPLY-DEFERRED, surfaced not advanced):** the schema holds `parent_chain` at `minItems 5, prefixItems 0–7, maxItems 8`. The SKILL emits the 8th `edit_plan_id` position; all 5 fixtures carry the 8-tuple; the schema accepts the 5-tuple inbound canon, the 6-tuple QC preview, the 7-tuple Ingest extension, AND the 8-tuple Edit Director append. Flipping the floor to exact-8 requires **ALL THREE** of: the Cross-SPEC §3.9 n-tuple amendment ratifying **AND** the Ingest 7-tuple LOCKing **AND** the QC Pre-flight 6-tuple LOCKing — operator-only gates (Item 11). Donna recommends RATIFY-AS-DRAFTED but does NOT advance it. The §5 validator accepts 5-, 6-, 7-, and 8-tuples by design, so this runbook does NOT depend on the amendment landing first. This is purely an operator decision, not a test-gate dependency — and it is the **one item Donna will NOT auto-advance** (D6).

---

## §7 Promotion rule LOCKED

5/5 PASS **+ the TC-01/TC-02 convergence proof OK** + **AI Video Gen v1.0 LOCK CLOSED** + **Style Replication v1.0 LOCK CLOSED** + **QC Pre-flight v1.0 LOCK CLOSED** + **Ingest v1.0 LOCK CLOSED** + Day 61 LOCK-CANDIDATE Items 6 + 8 + 11 ratified → ceremony flips version tag `v1.0-LOCK-CANDIDATE-day-61` → `v1.0-LOCKED` in `skills/edit-director-agent/SKILL.md` frontmatter `status:` field AND the Notion ARS hub row AND the dashboard `agentic-reel-studio` Edit Director chip `spec` (yellow) → `live` (green). The Day 65 evidence trail (5 LLM outputs + validator results + this runbook) is the canonical justification for the LOCK ceremony.

**Operator-only — Donna never executes any of the following:** the four predecessor LOCK ceremonies, this Edit Director LOCK ceremony, the paste-and-run execution of this runbook, the Cross-SPEC §3.9 amendment ratification, Items 6/8/11 ratification, or flipping any version tag / dashboard chip. Donna authored this runbook; the operator runs it.

---

## §8 Run-log template (fill one row per case)

| Case | Model id | Temp | Mode (dry/live) | Input tok | Output tok | Wall-clock s | Branch emitted | Verdict | Validator |
|------|----------|------|-----------------|-----------|------------|--------------|----------------|---------|-----------|
| TC-01 | | 0.2 | dry-run | | | | | | |
| TC-02 | | 0.2 | dry-run | | | | | | |
| TC-03 | | 0.2 | dry-run | | | | | | |
| TC-04 | | 0.2 | dry-run | | | | | | |
| TC-05 | | 0.2 | dry-run | | | | | | |
| probe-revise | | 0.2 | dry-run | | | | | | (note only) |
| probe-slot11 | | 0.2 | dry-run | | | | | | (note only) |

---

## §9 Probe results + notes (fill after run)

- **Probe A — `revise` (§3.6):** result PASS / FAIL · note: ______________________________
- **Probe B — slot-11 (§3.7):** result PASS / FAIL · note: ______________________________
- **Convergence proof (TC-01/TC-02):** OK / FAIL · if FAIL, re-run both at temp 0.2/0.0 before patching (authored-copy drift vs structural break): ______________________________
- **Any markdown-fence / preamble violations (Hard Rule #1):** ______________________________
- **Any forged-provenance flags (`render_dispatched: true` / mode read / approval language):** ______________________________

---

*Authored 2026-06-23 (Pacific) by Donna (overnight ARS Day 65 build session). Sequel Digital entity scope. The Edit Director Agent #9 v1.0 LLM Test Runbook is the forward deliverable per the Day 64 log close + the §14 calendar Day 65 slot. It is OPERATOR-GATED: Donna authored the paste-and-run runbook + the §5 validator; the operator executes it at the Workbench and runs the LOCK ceremony. The runbook exercises all 3 verdicts (plan_ready ×2, fail ×3) + 2 optional probes (the first-fleet `revise` success-side verdict + the slot-11 catch-all), with the TC-01/TC-02 mode-blind convergence proof and the TC-05 9th-pass authored-text firewall catch as the two gating checks. $0 engine/render spend; ≤ $4.00 token-only. v1.0 LOCK is HARD-GATED on the four predecessor LOCKs closing in dependency order (AI Video Gen → Style Replication → QC Pre-flight → Ingest), then Edit Director. The 8-tuple parent_chain stays held additively (minItems 5) — the one item NOT auto-advanced (D6).*
