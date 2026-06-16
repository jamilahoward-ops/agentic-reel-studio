# Day 57 LLM Test Execution Runbook — Ingest Agent v1.0

**Date authored:** 2026-06-15 (Mon · Day 57 · Wk9D1 · post-launch hardening window · v1.0 LOCK gate)
**Audience:** Jamila — single 20–35 min sit-down at the iMac (paste-and-run discipline).
**Goal:** Run all 5 SKILL-bundle fixtures (+ 1 optional adversarial slot-11 probe) through Opus 4.6, validate each output against `schemas/output.schema.json`, declare Ingest Agent v1.0 **LOCKED** if 5/5 PASS — IF AND ONLY IF the three predecessor LOCK ceremonies (AI Video Gen v1.0 → Style Replication v1.0 → QC Pre-flight v1.0) close first, in dependency order. QC Pre-flight is the **direct** dependency: Ingest consumes its `preflight_report.json` as a precondition gate and extends its 6-tuple `parent_chain`. The terminal post-production gateway cannot LOCK ahead of the gate it depends on.
**Estimated cost:** **$0.00 engine spend** (Ingest calls NO generative engine and runs NO byte-level decode, by design — Hard Rule #2) · ~**$0.40–$0.70** Opus 4.6 inference per case × 5 (× 6 with the slot-11 probe) ≈ **≤ $3.50 ($4.20 with probe) total LLM token spend.** Ties QC Pre-flight as the **cheapest runbook in the fleet** — no render dispatch in either dry-run *or* live, because the agent never touches an engine and never decodes a byte.
**Pre-validated:** Both schemas META-SCHEMA VALID (Day 54). Full bundle `validate.py` **47/47 green** Day 55 (meta-schema ×2 + 10 fixture validations + adversarial guards + parent_chain backward-compat + input source/floor/uri guards + TC-01/TC-02 byte-shape convergence proof). The §5 validator below extends that harness to score live LLM output against the 5 fixture expectations.
**Mode default:** **dry-run** (see §6). Because Ingest dispatches no engine *and* no byte-probe, "dry-run" and "live" are functionally identical (both reasoning-only over declared metadata). There is no engine surface and no decode surface to vary. Dry-run is the v1.0 LOCK gate.
**Operator approval still required to begin:** AI Video Gen v1.0 LOCK CLOSED **and** Style Replication v1.0 LOCK CLOSED **and** QC Pre-flight v1.0 LOCK CLOSED (three hard gates, dependency order), **plus** Ingest Day 53 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.

---

## TL;DR (action sequence)

1. **Confirm AI Video Gen v1.0 LOCK ceremony has CLOSED.** Day 27 5/5 PASS verdict in · Notion row "ARS · AI Video Gen Agent v1.0 LOCK" LOCKED · dashboard chip `live`. **HARD GATE #1** (chain head). If pending, stop.
2. **Confirm Style Replication v1.0 LOCK ceremony has CLOSED.** Day 36 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.** If pending, stop.
3. **Confirm QC Pre-flight v1.0 LOCK ceremony has CLOSED.** Day 47 runbook 5/5 PASS · Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #3 — Ingest's DIRECT dependency** (precondition gate + the 6-tuple Ingest's 7-tuple extends). If pending, stop.
4. **Confirm Ingest Day 53 LOCK-CANDIDATE Items 6 + 8 + 11 are operator-ratified.** Item 6 = cost-model confirm (lightest in fleet history — no vendor URLs, no ceilings owned; `cost_incurred_usd ≈ $0.00`). Item 8 = the 15-decisions walk (D15 Edit-Director handoff → Notion holding store needs an explicit verdict). Item 11 = Cross-SPEC §3.9 n-tuple amendment (the `parent_chain` forcing function — see §6).
5. **Optional:** Run `cd "~/ars/skills/ingest-agent" && python3 validate.py` in a fresh Python process for the canonical 47/47 bundle stamp. ~20 sec. Not gated — confirmed green Day 55.
6. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
7. **Model:** `claude-opus-4-6`. **Temperature:** `0.2`. **Max tokens:** `8000`. **Top-p:** default.
   *(Assumption stated: Ingest runs colder than the production agents' 0.4 — same rationale as QC Pre-flight. It is a deterministic adjudication gateway: it composes nothing creative; it walks a fixed 11-step loop over declared metadata and emits a verdict. A file is present or absent; a declared spec matches or it doesn't. Lower temperature reduces evidence-field paraphrase variance without touching the verdict logic. Operator may raise to 0.4 to match fleet default; verdicts are temperature-stable by construction.)*
8. **System prompt:** open `ars/skills/ingest-agent/SKILL.md`, locate the fenced block under §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)", paste **everything inside the fence** (12 hard rules + Blueprint §4.8 target manifest shape inlined + universal-tier table + 11-step ingest loop + voice rule + "Emit JSON only. Now."). No edits. No additions.
9. For each of the 5 cases (then optionally the slot-11 probe):
   - Open `ars/skills/ingest-agent/test-cases/case-NN-*/input.json`. Copy the **entire root object**.
   - User message = the JSON input object **only**. **No engine-stub fence** — Ingest reads no engine surface and no byte surface; everything it adjudicates (the preflight report, the polymorphic source set, storyboard shot list, production plan, declared specs, parent_chain, qc_pre_flags) is already inside the input object. No prose, no markdown around the JSON.
   - Send. Capture the **raw JSON output only** (strip any accidental code fence — Hard Rule #1 forbids them, but verify). Save to `ars/skills/ingest-agent/validation/llm-out/case-NN-output.json`.
   - Note token counts + wall-clock latency in the run-log (§8 template).
10. **Run validator** (single command, §5). Either **5/5 PASS → Ingest v1.0 LOCK ceremony executable** (subject to the three hard gates + Items 6/8/11), or capture failures for a Day 58 patch session.

---

## §1 Pre-flight checklist (14 items)

- [ ] **AI Video Gen v1.0 LOCK ceremony CLOSED.** Day 27 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #1** (chain head).
- [ ] **Style Replication v1.0 LOCK ceremony CLOSED.** Day 36 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.**
- [ ] **QC Pre-flight v1.0 LOCK ceremony CLOSED.** Day 47 5/5 PASS · Items 6/8/11 ratified · Notion row LOCKED · dashboard chip `live`. **HARD GATE #3 — Ingest's DIRECT dependency.** (All three production/gate LOCKs must close in dependency order before Ingest — the post-production gateway cannot LOCK ahead of the precondition gate it consumes.)
- [ ] **Ingest Day 53 LOCK-CANDIDATE Items 6 + 8 + 11 ratified.** Item 6 = cost-model confirm. Item 8 = 15-decisions walk (D15 explicit verdict). Item 11 = Cross-SPEC §3.9 n-tuple amendment (or explicitly DEFERRED — see §6 note on the 7-tuple).
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key already configured.
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run. *(For Ingest these are functionally identical — no engine, no byte-probe in either.)*
- [ ] **All 5 fixtures present** at `ars/skills/ingest-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:** `mkdir -p "~/ars/skills/ingest-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 54 LOCKED-as-drafted · re-verified Day 55 `validate.py`).
- [ ] **`input.schema.json` self-validates** ✓ (Day 54 · 5/5 fixtures green Day 55).
- [ ] **System-prompt + largest fixture footprint** = ~8 KB SKILL prompt + ~3.5 KB largest input ≈ **~12 KB context window.** Trivial vs Opus 4.6 200 K context.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support).
- [ ] **No raw vendor credentials anywhere on screen.** Ingest references NO credentials (Hard Rule #2 — it calls no engine, runs no decode). If Opus emits a credential, composes an engine prompt, or emits a decode/ffprobe command in any response, abort — the agent has misunderstood its job.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object**. |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"SYSTEM PROMPT — v1.0" fence — identical across all cases). |
| 3 | User message = `{input object}` only. **No fence, no stub, no prose.** Ingest reads no engine and no byte surface; the input carries everything it adjudicates. |
| 4 | Set temperature `0.2`, max tokens `8000`. Hit **Run**. |
| 5 | Wait for completion. Verify the response is a **single JSON object** with no markdown fences (Hard Rule #1 — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check: `metadata.agent_id == "ingest-agent"` AND `metadata.agent_version == "1.0"` AND `metadata.byte_probe_performed == false` AND `human_review_required == true`. If not, halt — agent is hallucinating identifiers, forging probe provenance, or breaking recommend-don't-clear. |

---

## §3 The cases — expected branch + pass criteria

**The 5 fixtures exercise all 3 verdict values** (`pass` ×2, `fail` ×2, `reshoot` ×1) and **3 of the 8 LOCKED error codes live** (`asset_firewall_breach`, `asset_spec_violation`, `missing_shot_coverage`). The remaining 5 codes (`upstream_qc_not_passed`, `upstream_not_success`, `asset_uri_integrity_failure`, `audio_sync_failure`, `manifest_lineage_failure`) + the folded `duration_envelope_breach` (→ `asset_spec_violation` subtype) + the slot-11 catch-all (`ingest_agent_failed`) are bound to the schema via the Day 55 `validate.py` adversarial guards, not all re-exercised live (same discipline as QC Pre-flight §3 / Style Replication §9). The optional slot-11 probe in §3.6 exercises the catch-all live as a defense-in-depth extra — it is NOT part of the 5/5 LOCK count.

**There is NO `hold` verdict** (deliberate divergence from QC Pre-flight — §6.4 / Decision #3). Ingest's domain is deterministic: a file is present or absent, a declared spec matches or it doesn't. Human deferral lives in `human_review_required: const true` on **every** emission (recommend-don't-clear, Hard Rule #12), not in a verdict value. The §5 validator REJECTS any `hold`.

### TC-01 — `case-01-mode-b-pro-clean-pass` (Pro · Mode B · 6-shot · clean PASS + Mode B source: replicated + rendered)
- **Expected branch:** `successAssetManifest`. **Verdict:** `pass`. **route:** n/a (success carries `handoff_targets`).
- **Hard checks:**
  - `output_type == "successAssetManifest"`, `verdict == "pass"` (schema `const "pass"` on this branch).
  - `metadata.tier == "pro"`, `metadata.production_mode == "B"`, `metadata.lever_state == "lever-3"`.
  - **AND-of-8-gates (false-pass STRUCTURALLY impossible — Decision #10, schema `const`; assert anyway, defense-in-depth):**
    - `asset_firewall_pass_8.status == "pass"` AND `hits == 0` AND `filenames_scanned > 0` AND `metadata_fields_scanned > 0`.
    - `asset_uri_integrity.non_relative == 0` AND `dangling == 0` AND `uris_checked > 0`.
    - `spec_check.aspect_ok / frame_rate_ok / resolution_ok / container_codec_ok / audio_present_ok / audio_sync_declared_ok` **all `true`**.
    - `spec_check.missing_shots == []`.
    - `coverage_check.coverage_complete == true` AND `shots_required == shots_covered == 6`.
  - **Canonical asset_bundle shape (Blueprint §4.8 — mode-agnostic):** `asset_bundle.raw_footage[]` each carries `{shot_ref, asset_uri (ars://…), duration_sec, source}`; `audio[]` present; `assets_pulled[]` present; `music_bed` is an `ars://…` URI.
  - **Every `asset_uri` matches `^ars://`** (Hard Rule #5/#8 — platform-relative; no absolute URL anywhere in the bundle).
  - `mode_convergence.ingested_mode == "B"` AND `normalized_to == "mode_agnostic_manifest"`.
  - `qc_precondition_check.verdict_observed == "pass"` (or `lever3_signoff_present == true` — schema `anyOf`).
  - `handoff_targets == ["edit-director-agent"]` (Step 10 success path).
  - `qc_pre_flags[]` ≥ 4 entries, every element snake_case (`^[a-z][a-z0-9_]{0,63}$`).
  - `cost_incurred_usd == 0.0` (top-level AND `metadata.cost_incurred_usd`; Hard Rule #2 — $0 effective cost).
  - `metadata.byte_probe_performed == false` (schema `const false` — declared-spec honesty contract; a `true` is forged provenance).
  - `metadata.asset_manifest_class == "pre_edit"`.
- **Lineage:** `metadata.parent_chain` is a **7-tuple** held additively: `[brief-…, script-…, storyboard-…, ai-video-gen-…, <uuid replication_set_id>, preflight-…, <uuid asset_manifest_id>]`. (Schema holds `minItems 5, prefixItems 0–6, maxItems 7`; a 5- or 6-tuple is also accepted; a 4-tuple is rejected. The validator accepts 5/6/7.)
- **Tamper-evidence:** `metadata.manifest_evidence_hash` matches `^[a-f0-9]{64}$`. *(The validator checks SHAPE, not value — Opus cannot deterministically reproduce the fixture's hash; the agent computes it honestly over its own evidence + spec_check block.)*
- **Recommend-don't-clear:** top-level `human_review_required == true` AND `metadata.human_review_required == true` (schema `const true`). Zero clearance language (`cleared`, `cleared for edit`, `approved for edit`, `approved`, `published`) anywhere in any string.
- **Entity firewall + banned-vocab walk:** zero hits of the 10-entry canonical list (`holdco group`, `4821 main`/`4821`, `site-c-brand`/`6315`, `sln`/`salonb`/`shear & cuts`, `retail supply`, `principal holdco`/`principal`, `npox`, `nonprofit leader a`, `partner brand`, `holdcogroup.com`) and zero banned-vocab (`babe`, `boss babe`, `girl boss`, `she-eo`, `mompreneur`) across every emitted string. (REINVENTED IS allowed — pilot brand per Cross-SPEC canon.)

### TC-02 — `case-02-mode-c-enterprise-clean-pass` (Enterprise · Mode C · clean PASS · the mode-convergence proof)
- **Expected branch:** `successAssetManifest`. **Verdict:** `pass`.
- **Hard checks (delta vs TC-01):**
  - `metadata.tier == "enterprise"`, `metadata.production_mode == "C"`.
  - `mode_convergence.ingested_mode == "C"` (Mode C: single-source, no AI Video Gen `rendered_shots`).
  - **Lineage position [3] == `"mode-c-direct"`** (no AI Video Gen stage in a Mode C chain).
  - **THE CONVERGENCE PROOF — the fixture's whole point:** `asset_bundle`, `spec_check`, and `coverage_check` are **byte-shape identical to TC-01** despite a different ingested mode. From Ingest onward, post-production is mode-agnostic; Edit Director and every downstream agent are contractually mode-blind. A regression that leaked the ingested mode into the bundle shape would break that contract. *(The §5 validator asserts this directly: it canonicalizes both bundles — replacing the per-case `asset_manifest_id` — and requires byte-equality of `asset_bundle` + `spec_check` + `coverage_check`.)*
  - All other TC-01 success checks apply (AND-of-8-gates, `^ars://` URIs, `handoff_targets`, recommend-don't-clear, `byte_probe_performed: false`, manifest_evidence_hash shape, 7-tuple lineage).

### TC-03 — `case-03-mode-a-coverage-gap-reshoot` → `errorEnvelope` `missing_shot_coverage` · **THE MODE-A-EXCLUSIVE RESHOOT**
- **Expected branch:** `errorEnvelope`. **Verdict:** `reshoot`. **route_back_to:** `production-coord-agent`.
- **This fixture exercises the only verdict-routing-mode-dependent path in the agent.** `reshoot` is Mode-A-exclusive (live source footage; AI output is re-genned, never re-shot — Decision #3). The schema `if/then` guard binds it: a `reshoot` verdict MUST carry `route_back_to: const "production-coord-agent"` AND `failure_code: const "missing_shot_coverage"`. The take-substitution ladder is exhausted (shot-004: only take declares 0s, fails the spec band, no other take present) → escalate to reshoot.
- **Hard checks:**
  - `output_type == "errorEnvelope"`, `verdict == "reshoot"`.
  - `failure_code == "missing_shot_coverage"`.
  - `failed_check_id == 6` (Step 6 / coverage check).
  - `route_back_to == "production-coord-agent"` (the live-footage owner — NOT `style-replication-agent`; Mode A is re-shot).
  - `attempts == 1` (a real coverage gap is a valid verdict on first construction — NOT a self-QC regenerate loop).
  - `metadata.production_mode == "A"`.
  - `detail.affected_shot == "shot-004"`.
  - `detail.subtype == "coverage_gap"`.
  - `detail.ladder_attempt` present (names the take-substitution ladder exhaustion).
  - `detail.recovery_path` present (re-shoot + route-to-ProdCoord + "live footage re-shot, never re-genned" language).
  - `human_review_required == true` (top-level AND metadata) — even a clear coverage gap is a recommendation, never an autonomous quarantine.
- **Lineage delta:** position [3] == `productionplan-…` (Mode A chain — ProdCoord shoot packet, no AI Video Gen / no Style Replication render stage at position 3).
- **Negative checks:** NO `asset_bundle`, NO `spec_check`, NO `coverage_check` success-shape, NO `handoff_targets`, NO `mode_convergence` on the error branch (those are success-only fields).

### TC-04 — `case-04-asset-spec-violation` → `errorEnvelope` `asset_spec_violation`
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **route_back_to:** `style-replication-agent`.
- **Hard checks:**
  - `failure_code == "asset_spec_violation"`, `failed_check_id == 5` (Step 5 / declared-spec validation), `attempts == 1`.
  - `verdict == "fail"` (NOT `reshoot` — Mode B AI output is re-replicated/re-genned, never re-shot).
  - `route_back_to == "style-replication-agent"` (the agent that produced the deliverable aspect).
  - `detail.affected_shot == "shot-003"`.
  - `detail.subtype == "aspect_ratio"`.
  - `detail.violation` names the mismatch (`declared aspect 16:9 vs 9:16 plan target`). *(This is a field where a spec value legitimately appears for forensics — it carries no firewall token, so no exclusion is needed; but the §5 validator excludes the whole error-branch `detail` object from the firewall walk regardless, see TC-05.)*
  - `detail.recovery_path` present (re-replicate at 9:16 + route + "fixable without re-shooting" language).
  - `human_review_required == true` (both).
- **Negative checks:** NO success-only fields; NO `handoff_targets`.

### TC-05 — `case-05-asset-firewall-breach` → `errorEnvelope` `asset_firewall_breach` · **GATING FIXTURE (the 8th-pass asset-layer catch)**
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **route_back_to:** `style-replication-agent`.
- **This is the most important fixture in the portfolio — Ingest's reason to exist.** The reel CONTENT is fully clean; all 7 prior content passes would pass it. The breach rides the **asset layer** that no prior pass ever inspected: a filename (`sln_cuts_promo_take2.mp4` → token `sln`) and a sidecar caption-metadata field (`contact us at holdcogroup.com for booking` → token `holdcogroup.com`). Ingest is the 8th and first asset-layer firewall. **A v1.0 LOCK is BLOCKED if TC-05 does not catch both injected tokens.**
- **Hard checks:**
  - `output_type == "errorEnvelope"`, `verdict == "fail"`.
  - `failure_code == "asset_firewall_breach"`.
  - `failed_check_id == 4` (Step 4 / asset-layer firewall pass).
  - `route_back_to == "style-replication-agent"` (the leaking upstream stage).
  - `attempts == 1`.
  - `detail.hits == 2` (both tokens caught — a single-hit catch is an UNDER-report and must FAIL the gate).
  - `detail.assets` is a list naming BOTH offending assets + the token each carried (the filename `sln` hit AND the sidecar-caption `holdcogroup.com` hit). *(This is the forensic field where banned tokens legitimately appear — the breach report quoting the offenders. The §5 validator EXCLUDES the entire error-branch `detail` object from its firewall walk; every OTHER emitted string must be clean.)*
  - `detail.upstream_stage == "style-replication-agent"`.
  - `detail.recovery_path` present (strip tokens + re-emit + "8th-pass asset-layer catch" language).
  - `human_review_required == true` (both).
- **Negative checks:** NO success-only fields; NO `handoff_targets`.

### §3.6 — OPTIONAL adversarial probe: slot-11 `ingest_agent_failed` (NOT part of the 5/5 LOCK count)
- **Purpose:** exercise the self-QC 2-strike exhaustion catch-all live (the Day 55 build-log "adversarial slot-11 case"). The schema already guards it (Day 55 `validate.py`: `attempts: const 2` + `route_back_to: const null` + `verdict: const fail` accepted; `attempts==1` rejected; non-null route rejected). This probe confirms the LIVE agent reaches the slot honestly under a genuinely irreconcilable input rather than fabricating a verdict.
- **How to run:** take `test-cases/case-04-asset-spec-violation/input.json`, then **corrupt the declared spec into self-contradiction** — e.g. set `production_plan.platform_target.aspect` to a value present nowhere in any platform variant AND remove the storyboard `shot_list` `shot_ref` for one covered asset, so neither a clean spec match nor a clean coverage map can be constructed. Save as `validation/llm-out/probe-slot11-input.json`. Run with the same system prompt + settings.
- **Expected:** `errorEnvelope`, `failure_code == "ingest_agent_failed"`, `attempts == 2`, `route_back_to == null`, `verdict == "fail"`, `human_review_required == true`. The agent must NOT emit a `pass` and must NOT route-back to an upstream agent (no upstream is at fault for a self-QC exhaustion).
- **Scoring:** PASS/FAIL recorded separately in §9 as an adversarial note. A failure here does NOT block the LOCK on its own (the schema guard already proves the slot is reachable + well-formed), but a *malformed* slot-11 (e.g. `attempts==1`, or a non-null route, or a `pass`) is a **red flag** warranting a Day 58 patch review before ceremony.

### Cross-fixture invariants (apply to all 5 + the probe)
- `metadata.agent_id == "ingest-agent"` on every output (success or error).
- `metadata.agent_version == "1.0"` on every output.
- `metadata.asset_manifest_class == "pre_edit"` on every output.
- `metadata.byte_probe_performed == false` on every output (schema `const false` — the declared-spec honesty contract; a `true` anywhere is forged provenance and a hard FAIL).
- `metadata.runtime_environment_class == "staging"` for dry-run runs.
- `metadata.manifest_evidence_hash` matches `^[a-f0-9]{64}$` on every output (tamper-evident; shape-checked, not value-checked).
- `metadata.parent_chain` is a well-formed 5-, 6-, or 7-tuple (positions [0]=`brief-`, [1]=`script-`, [2]=`storyboard-`, [3]=`ai-video-gen-…`|`mode-c-direct`|`productionplan-…`, [4]=UUID; optional [5]=`preflight-…`, optional [6]=UUID `asset_manifest_id`). A 4-tuple is rejected.
- `reel_ref.asset_manifest_id` is a UUID and equals `metadata.asset_manifest_id` (and, on the 7-tuple, equals `parent_chain[6]`).
- top-level `human_review_required == true` AND `metadata.human_review_required == true` on every output (recommend-don't-clear, schema `const true`).
- `cost_incurred_usd == 0.0` (top-level) on every output (Hard Rule #2 / #10 — Ingest carries no cost ceiling and litigates no cost).
- Zero entity-firewall hits + zero banned-vocab (token-boundary, case-insensitive) across every emitted string, with one legitimate-naming exclusion: the error branch's `detail` object (TC-04's `detail.violation` quotes a spec value; TC-05's `detail.assets` + `detail.recovery_path` quote the offending tokens for forensics). The `detail.hits` count is asserted independently.
- Zero clearance language (`cleared`, `cleared for edit`, `approved for edit`, `approved`, `published`) anywhere.
- **NO `hold` verdict** on any output (deliberate divergence — §6.4 / Decision #3).

---

## §4 Why there is NO engine-stub block (the no-engine / no-byte-probe difference)

The production agents' runbooks (Day 11 Script, Day 19 Production Coord, Day 27 AI Video Gen, Day 36 Style Replication) appended an `<engine_dry_run_mode>` fence to the user message, because those agents dispatch generative engines and the dry-run fence replaces the engine surface with stubbed responses. The Day 47 QC Pre-flight runbook dropped that block — QC Pre-flight dispatches no engine.

**Ingest goes one step further: no engine AND no byte-level decode** (Hard Rule #2 — "no render, no transcode, no ffprobe, no MediaInfo, no API dispatch … you adjudicate DECLARED asset metadata only … set `byte_probe_performed: false` in every manifest"). Everything the agent adjudicates is already inside the input object:

- `preflight_report` — the QC precondition gate (Step 1; verdict must be `pass` or carry Lever-3 sign-off).
- The **polymorphic source** — EITHER a Mode A `footage_upload_manifest` OR the production-tier set (`replicated_shots` from Style Replication, optionally `rendered_shots` from AI Video Gen for Mode B). The schema's `oneOf` enforces exactly one source branch.
- `storyboard_ref.shot_list[]` — the coverage reference (Step 6).
- `production_plan` (Mode B/C) / ProdCoord `format_spec` (Mode A) — the declared-spec target (Step 5).
- Each asset's `declared_spec` (aspect / fps / resolution / container / codec) + `duration_sec` — the spec + duration-envelope surface (Steps 5, 8).
- Filenames, embedded asset-metadata fields, sidecar caption/SRT files — the **asset-layer firewall surface** (Step 4 — the NEW surface).
- `metadata.parent_chain` + `accumulated qc_pre_flags[]` — lineage + the 6-agent floor record.

There is nothing to stub and nothing to decode. The user message is the **bare input object**. The agent reasons over it, runs the 11-step ingest loop, and emits one of two branches. `byte_probe_performed: const false` is the honesty contract: the agent never claims a probe it did not run. This is what makes Ingest tie QC Pre-flight as the cheapest gate in the fleet — and the only two where "live" and "dry-run" are functionally identical.

**Runtime-computed fields (hash, timestamps, latency, UUIDs):** `manifest_evidence_hash` is a SHA-256 the agent computes honestly over its own evidence + spec_check block; `timestamp_utc` + `latency_ms` are runtime telemetry; `asset_manifest_id` is a fresh UUIDv7. In a Workbench run these will NOT match the fixture's frozen values, and that is correct. The §5 validator checks `manifest_evidence_hash` for SHAPE (`^[a-f0-9]{64}$`) only, and does not assert timestamp/latency/UUID values against the fixture. For the TC-01/TC-02 convergence proof it canonicalizes the per-case `asset_manifest_id` out before byte-comparing. Do not flag a hash/timestamp/UUID mismatch against the fixture as a failure — only a malformed shape, or a broken convergence equality, is a failure.

---

## §5 Post-run validator (paste-and-run)

After saving all 5 outputs to `validation/llm-out/case-NN-output.json`:

```bash
cd "~/ars/skills/ingest-agent"

python3 << 'PYEOF'
import json, re, sys
from jsonschema import Draft202012Validator
from pathlib import Path

ROOT = Path(".")
OUT_SCHEMA = json.loads((ROOT / "schemas" / "output.schema.json").read_text())
v = Draft202012Validator(OUT_SCHEMA)

# 10-entry canonical entity firewall list (token-boundary, case-insensitive)
FIREWALL = ["holdco group","hc","4821 main","4821","site-c-brand","6315",
            "sln","sln cuts","sln shear","salonb","shear & cuts","retail supply",
            "principal holdco","principal","npox","community nonprofit","nonprofit leader a",
            "partner brand","holdcogroup.com"]
BANNED   = ["babe","boss babe","girl boss","girlboss","she-eo","mompreneur"]
CLEARANCE = ["cleared for edit","cleared","approved for edit","approved","published"]

UUID_RE   = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
SNAKE_RE  = re.compile(r"^[a-z][a-z0-9_]{0,63}$")
ARS_RE    = re.compile(r"^ars://")

def word_hit(term, text):
    # token-boundary, case-insensitive — "hc" never matches inside "image"
    return re.search(r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])", text) is not None

EXPECT = {
  "case-01-mode-b-pro-clean-pass": {
    "branch": "successAssetManifest", "verdict": "pass",
    "tier": "pro", "mode": "B", "shots": 6, "ingested_mode": "B",
  },
  "case-02-mode-c-enterprise-clean-pass": {
    "branch": "successAssetManifest", "verdict": "pass",
    "tier": "enterprise", "mode": "C", "shots": 6, "ingested_mode": "C",
    "lineage_pos3": "mode-c-direct", "convergence_twin": "case-01-mode-b-pro-clean-pass",
  },
  "case-03-mode-a-coverage-gap-reshoot": {
    "branch": "errorEnvelope", "verdict": "reshoot",
    "failure_code": "missing_shot_coverage", "failed_check_id": 6,
    "route_back_to": "production-coord-agent", "attempts": 1,
    "mode": "A", "affected_shot": "shot-004", "subtype": "coverage_gap",
  },
  "case-04-asset-spec-violation": {
    "branch": "errorEnvelope", "verdict": "fail",
    "failure_code": "asset_spec_violation", "failed_check_id": 5,
    "route_back_to": "style-replication-agent", "attempts": 1,
    "affected_shot": "shot-003", "subtype": "aspect_ratio",
  },
  "case-05-asset-firewall-breach": {
    "branch": "errorEnvelope", "verdict": "fail",
    "failure_code": "asset_firewall_breach", "failed_check_id": 4,
    "route_back_to": "style-replication-agent", "attempts": 1,
    "min_hits": 2, "upstream_stage": "style-replication-agent",
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

def all_asset_uris(out):
    uris = []
    ab = out.get("asset_bundle", {}) or {}
    for rf in ab.get("raw_footage", []) or []:
        if isinstance(rf, dict) and "asset_uri" in rf: uris.append(rf["asset_uri"])
    for a in ab.get("audio", []) or []:
        if isinstance(a, dict) and "asset_uri" in a: uris.append(a["asset_uri"])
        elif isinstance(a, str): uris.append(a)
    if isinstance(ab.get("music_bed"), str): uris.append(ab["music_bed"])
    return uris

def canon_bundle(out):
    # canonicalize per-case identifiers out of the convergence-checked subtree
    import copy
    sub = {k: copy.deepcopy(out.get(k)) for k in ("asset_bundle","spec_check","coverage_check")}
    return json.dumps(sub, sort_keys=True)

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

    # ---- universal metadata + recommend-don't-clear + no-probe ----
    if out.get("verdict") != exp["verdict"]:
        fails.append(f"verdict={out.get('verdict')!r}, expected {exp['verdict']!r}")
    if out.get("verdict") == "hold":
        fails.append("HOLD verdict emitted — forbidden for Ingest (no hold)")
    if meta.get("agent_id") != "ingest-agent":
        fails.append(f"metadata.agent_id={meta.get('agent_id')!r}")
    if meta.get("agent_version") != "1.0":
        fails.append(f"metadata.agent_version={meta.get('agent_version')!r}")
    if meta.get("asset_manifest_class") != "pre_edit":
        fails.append(f"metadata.asset_manifest_class={meta.get('asset_manifest_class')!r}")
    if meta.get("byte_probe_performed") is not False:
        fails.append(f"metadata.byte_probe_performed={meta.get('byte_probe_performed')!r}, expected false (forged-provenance guard)")
    if out.get("human_review_required") is not True:
        fails.append(f"top-level human_review_required={out.get('human_review_required')!r}, expected true")
    if meta.get("human_review_required") is not True:
        fails.append(f"metadata.human_review_required={meta.get('human_review_required')!r}, expected true")
    if (out.get("cost_incurred_usd") or 0) != 0.0:
        fails.append(f"cost_incurred_usd={out.get('cost_incurred_usd')!r}, expected 0.0")
    veh = meta.get("manifest_evidence_hash")
    if not (isinstance(veh, str) and SHA256_RE.match(veh)):
        fails.append(f"metadata.manifest_evidence_hash bad shape: {veh!r}")
    if "mode" in exp and meta.get("production_mode") != exp["mode"]:
        fails.append(f"metadata.production_mode={meta.get('production_mode')!r}, expected {exp['mode']!r}")

    # ---- parent_chain shape (5/6/7-tuple) ----
    pc = meta.get("parent_chain")
    if not (isinstance(pc, list) and len(pc) in (5, 6, 7)):
        fails.append(f"parent_chain not a 5/6/7-tuple: {pc!r}")
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
        if len(pc) == 7 and not UUID_RE.match(str(pc[6])):
            fails.append(f"parent_chain[6] not a UUID: {pc[6]!r}")
    if "lineage_pos3" in exp and isinstance(pc, list) and len(pc) >= 4 and pc[3] != exp["lineage_pos3"]:
        fails.append(f"parent_chain[3]={pc[3]!r}, expected {exp['lineage_pos3']!r}")

    # ---- reel_ref.asset_manifest_id == metadata.asset_manifest_id ----
    rr = out.get("reel_ref", {}) or {}
    rid = rr.get("asset_manifest_id")
    if not (isinstance(rid, str) and UUID_RE.match(rid)):
        fails.append(f"reel_ref.asset_manifest_id not a UUID: {rid!r}")
    elif meta.get("asset_manifest_id") != rid:
        fails.append(f"asset_manifest_id mismatch reel_ref={rid!r} vs metadata={meta.get('asset_manifest_id')!r}")
    elif isinstance(pc, list) and len(pc) == 7 and pc[6] != rid:
        fails.append(f"parent_chain[6]={pc[6]!r} != asset_manifest_id {rid!r}")

    # ---- firewall / banned-vocab / clearance walk (error-branch detail excluded) ----
    walk_obj = json.loads(json.dumps(out))  # deep copy
    if branch == "errorEnvelope":
        walk_obj.pop("detail", None)   # forensic field legitimately quotes tokens
    strings = []; collect_strings(walk_obj, strings)
    joined = "\n".join(strings).lower()
    for t in FIREWALL:
        if word_hit(t, joined): fails.append(f"entity_firewall_leak: {t!r}")
    for t in BANNED:
        if word_hit(t, joined): fails.append(f"banned_vocab_leak: {t!r}")
    for t in CLEARANCE:
        if word_hit(t, joined): fails.append(f"clearance_language_leak: {t!r}")

    if branch == "successAssetManifest":
        if meta.get("tier") != exp["tier"]:
            fails.append(f"metadata.tier={meta.get('tier')!r}, expected {exp['tier']!r}")
        # AND-of-8-gates (false-pass guard)
        afw = out.get("asset_firewall_pass_8", {}) or {}
        if afw.get("status") != "pass" or afw.get("hits") != 0:
            fails.append(f"asset_firewall_pass_8={afw!r} (need status pass, hits 0)")
        if (afw.get("filenames_scanned") or 0) < 1 or (afw.get("metadata_fields_scanned") or 0) < 1:
            fails.append(f"asset_firewall_pass_8 scan counts not >0: {afw!r}")
        aui = out.get("asset_uri_integrity", {}) or {}
        if aui.get("non_relative") != 0 or aui.get("dangling") != 0 or (aui.get("uris_checked") or 0) < 1:
            fails.append(f"asset_uri_integrity={aui!r} (need non_relative 0, dangling 0, uris_checked>0)")
        sc = out.get("spec_check", {}) or {}
        for k in ("aspect_ok","frame_rate_ok","resolution_ok","container_codec_ok","audio_present_ok","audio_sync_declared_ok"):
            if sc.get(k) is not True: fails.append(f"spec_check.{k}={sc.get(k)!r}, expected true (false-pass guard)")
        if sc.get("missing_shots") != []:
            fails.append(f"spec_check.missing_shots={sc.get('missing_shots')!r}, expected []")
        cov = out.get("coverage_check", {}) or {}
        if cov.get("coverage_complete") is not True:
            fails.append(f"coverage_check.coverage_complete={cov.get('coverage_complete')!r}, expected true")
        if cov.get("shots_required") != exp["shots"] or cov.get("shots_covered") != exp["shots"]:
            fails.append(f"coverage counts={cov!r}, expected {exp['shots']}/{exp['shots']}")
        # canonical bundle shape + ars:// URIs
        ab = out.get("asset_bundle", {}) or {}
        if not isinstance(ab.get("raw_footage"), list) or not ab["raw_footage"]:
            fails.append("asset_bundle.raw_footage missing/empty")
        else:
            for i, rf in enumerate(ab["raw_footage"]):
                for key in ("shot_ref","asset_uri","duration_sec","source"):
                    if key not in rf: fails.append(f"raw_footage[{i}] missing {key}")
        for u in all_asset_uris(out):
            if not ARS_RE.match(str(u)): fails.append(f"non-ars:// asset_uri: {u!r}")
        # mode convergence
        mc = out.get("mode_convergence", {}) or {}
        if mc.get("ingested_mode") != exp["ingested_mode"]:
            fails.append(f"mode_convergence.ingested_mode={mc.get('ingested_mode')!r}, expected {exp['ingested_mode']!r}")
        if mc.get("normalized_to") != "mode_agnostic_manifest":
            fails.append(f"mode_convergence.normalized_to={mc.get('normalized_to')!r}")
        # qc precondition
        qp = out.get("qc_precondition_check", {}) or {}
        if not (qp.get("verdict_observed") == "pass" or qp.get("lever3_signoff_present") is True):
            fails.append(f"qc_precondition_check not satisfied: {qp!r}")
        # handoff
        if out.get("handoff_targets") != ["edit-director-agent"]:
            fails.append(f"handoff_targets={out.get('handoff_targets')!r}")
        # qc_pre_flags
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
        if "affected_shot" in exp and detail.get("affected_shot") != exp["affected_shot"]:
            fails.append(f"detail.affected_shot={detail.get('affected_shot')!r}, expected {exp['affected_shot']!r}")
        if "subtype" in exp and detail.get("subtype") != exp["subtype"]:
            fails.append(f"detail.subtype={detail.get('subtype')!r}, expected {exp['subtype']!r}")
        if exp["failure_code"] == "asset_firewall_breach":
            if (detail.get("hits") or 0) < exp["min_hits"]:
                fails.append(f"detail.hits={detail.get('hits')}, expected >= {exp['min_hits']} (under-report = FAIL)")
            if detail.get("upstream_stage") != exp["upstream_stage"]:
                fails.append(f"detail.upstream_stage={detail.get('upstream_stage')!r}, expected {exp['upstream_stage']!r}")
        # reshoot if/then (schema-guarded; assert anyway)
        if exp["verdict"] == "reshoot":
            if out.get("route_back_to") != "production-coord-agent" or out.get("failure_code") != "missing_shot_coverage":
                fails.append("reshoot if/then guard broken (need route production-coord-agent + missing_shot_coverage)")
        # negative checks: no success-only fields on error branch
        for forbidden in ("asset_bundle","spec_check","coverage_check","handoff_targets","mode_convergence",
                          "asset_firewall_pass_8","asset_uri_integrity","qc_precondition_check"):
            if forbidden in out:
                fails.append(f"success-only field {forbidden!r} present on error branch")

    results.append((case_id, "PASS" if not fails else "FAIL", "all checks green" if not fails else " || ".join(fails[:8])))

# ---- TC-01/TC-02 mode-convergence proof (byte-shape identical bundle) ----
conv_note = ""
a = outputs.get("case-01-mode-b-pro-clean-pass")
b = outputs.get("case-02-mode-c-enterprise-clean-pass")
if a and b and a.get("output_type") == "successAssetManifest" and b.get("output_type") == "successAssetManifest":
    if canon_bundle(a) == canon_bundle(b):
        conv_note = "CONVERGENCE PROOF OK — TC-01/TC-02 asset_bundle+spec_check+coverage_check byte-identical."
    else:
        conv_note = "CONVERGENCE PROOF FAIL — TC-01/TC-02 bundles diverge (mode leaked into post-convergence shape)."
        # demote both to FAIL if they were PASS
        results = [(cid, ("FAIL" if cid in ("case-01-mode-b-pro-clean-pass","case-02-mode-c-enterprise-clean-pass") and st=="PASS" else st),
                    (note if not (cid in ("case-01-mode-b-pro-clean-pass","case-02-mode-c-enterprise-clean-pass")) else (note + " || convergence proof failed")))
                   for cid, st, note in results]
else:
    conv_note = "CONVERGENCE PROOF SKIPPED — one or both pass cases missing/non-success."

print()
print("=" * 90)
print("Day 57 LLM Test Runbook — Ingest Agent v1.0 — VALIDATOR RESULTS")
print("=" * 90)
pass_n = 0
for case_id, status, note in results:
    icon = "PASS " if status == "PASS" else "FAIL "
    print(f"  {icon} {case_id:42s} :: {status:14s} {note[:200]}")
    if status == "PASS": pass_n += 1
print("-" * 90)
print(f"  {conv_note}")
print("-" * 90)
print(f"  Aggregate: {pass_n}/{len(results)} PASS")
if pass_n == len(results) and "OK" in conv_note:
    print("  >> Ingest v1.0 LOCK GATE = OPEN.")
    print("  >> HARD GATES: requires AI Video Gen + Style Replication + QC Pre-flight v1.0 LOCKs CLOSED first (dependency order).")
    print("  >> Ceremony: flip v1.0-LOCK-CANDIDATE-day-53 -> v1.0-LOCKED in SKILL.md frontmatter + Notion + dashboard chip.")
else:
    held = len(results) - pass_n
    print(f"  >> Ingest v1.0 LOCK GATE = HELD. {held} failure(s) and/or convergence break require patch.")
    print(f"  >> Patch protocol: SKILL.md system prompt ONLY (schemas LOCKED Day 54; no schema edits without a v1.0.x bump).")
print("=" * 90)
sys.exit(0 if (pass_n == len(results) and "OK" in conv_note) else 1)
PYEOF
```

Save the printed output: append ` > validation/llm-out/run-results-2026-06-15.txt 2>&1` to the bash command above, OR screenshot it.

**Slot-11 probe (optional, §3.6):** save its output to `validation/llm-out/probe-slot11-output.json` and spot-check by hand: `failure_code == "ingest_agent_failed"`, `attempts == 2`, `route_back_to == null`, `verdict == "fail"`, `human_review_required == true`. It is NOT scored by the validator above (which loops the 5 LOCK fixtures) — record the result in §9.

---

## §6 Open Question #57 resolution — dry-run vs live + the 7-tuple

**Decision:** **dry-run mode is the v1.0 LOCK gate** — and for Ingest, dry-run and live are functionally identical.

**Why:**
- Ingest is one of only two agents in the fleet that dispatch **no generative engine at all** (with QC Pre-flight) — and the ONLY one that also runs **no byte-level decode** (Hard Rule #2). There is no render call, no transcode, no `ffprobe`, no `MediaInfo`, no vendor API. "Live mode" for the production agents means real engine spend on non-deterministic outputs; for Ingest there is no such surface, and no decode surface either.
- v1.0 LOCK proves the agent's **reasoning + schema compliance + asset-layer firewall coverage (8th pass) + declared-spec validation + storyboard-coverage math + mode-convergence normalization + verdict-route correctness + recommend-don't-clear discipline + the byte-probe honesty contract.** None require any engine call or any byte decode. They require Opus 4.6 to consume the declared-metadata payload and emit a schema-valid, contract-compliant manifest.
- Cost: dry-run = ~$3.50 in Opus tokens (≤ $4.20 with the slot-11 probe). There is no meaningfully different "live" number — the agent spends $0.00 of engine money and $0.00 of probe money in every mode.

**The 7-tuple `parent_chain` (Decision D6 / Item 11 — DOUBLY-DEFERRED, surfaced not advanced):** the schema holds `parent_chain` at `minItems 5, prefixItems 0–6, maxItems 7`. The SKILL emits the 7th `asset_manifest_id` position; all 5 fixtures carry the 7-tuple; the schema accepts the 5-tuple inbound canon, the 6-tuple QC extension preview, AND the 7-tuple Ingest append. Flipping the floor to exact-7 requires **BOTH** the Cross-SPEC §3.9 n-tuple amendment ratifying **AND** the QC Pre-flight 6-tuple LOCKing — two operator-only gates (Item 11). Donna recommends RATIFY-AS-DRAFTED but does NOT advance it. The §5 validator accepts 5-, 6-, and 7-tuples by design, so this runbook does NOT depend on the amendment landing first. This is purely an operator decision, not a test-gate dependency.

---

## §7 Promotion rule LOCKED

5/5 PASS **+ the TC-01/TC-02 convergence proof OK** + **AI Video Gen v1.0 LOCK CLOSED** + **Style Replication v1.0 LOCK CLOSED** + **QC Pre-flight v1.0 LOCK CLOSED** + Day 53 LOCK-CANDIDATE Items 6 + 8 + 11 ratified → ceremony flips version tag `v1.0-LOCK-CANDIDATE-day-53` → `v1.0-LOCKED` in `skills/ingest-agent/SKILL.md` frontmatter `status:` field AND the Notion ARS hub row AND the dashboard `agentic-reel-studio` Ingest chip `spec` (yellow) → `live` (green). The Day 57 evidence trail (5 LLM outputs + validator results + this runbook) is the canonical justification for the LOCK ceremony.

| Unlocked post-LOCK | Why |
|--------------------|-----|
| **The post-production gateway goes LIVE** — every reel, every tier, every mode now hits a real asset-readiness checkpoint before Edit Director | Ingest is the 8th defense-in-depth firewall + the FIRST asset-layer scan + the mode-convergence seam |
| **8th of 17 SKILL bundles confirmed LIVE at v1.0** | Joins Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight — pipeline has 8 of 17 agents LOCKED at v1.0 |
| **Post-production goes mode-blind** | The TC-01/TC-02 convergence proof empirically demonstrates Edit Director + every downstream agent receive ONE manifest shape regardless of ingest mode |
| **Cross-SPEC §3.9 n-tuple amendment has its second forcing function** (if Item 11 ratified) | Ingest is the agent that appends the 7th `asset_manifest_id`; its LOCK + QC's 6-tuple LOCK are the natural moment to flip the schema floor to exact-7 fleet-wide |
| **Agent #9 of 17 SPEC outline kickoff** | Edit Director — Donna recommendation at ceremony close; operator confirms the specific next-agent schedule |

---

## §8 Run-log template (fill in after each case)

Copy this block 5× (6× with the probe) into `validation/llm-out/run-log-2026-06-15.md`.

```
## Case: case-NN-<slug>

- **Run timestamp (UTC):** 2026-06-15THH:MM:SSZ
- **Mode:** dry-run | live   (functionally identical for Ingest — no engine, no byte-probe)
- **Model:** claude-opus-4-6
- **Temperature:** 0.2
- **Max tokens:** 8000
- **Input tokens:** ____
- **Output tokens:** ____
- **Wall-clock seconds:** ____
- **Output file:** validation/llm-out/case-NN-<slug>-output.json
- **Output size (bytes):** ____
- **Branch emitted:** successAssetManifest | errorEnvelope
- **Verdict:** pass | fail | reshoot   (NEVER hold — Ingest has no hold)
- **failure_code (if error):** ____
- **route_back_to:** ____
- **byte_probe_performed (must be false):** ____
- **manifest_evidence_hash (64-hex shape OK?):** ____
- **parent_chain length (5/6/7):** ____
- **human_review_required (must be true):** ____
- **Validator result (from §5):** PASS | FAIL
- **If FAIL — first failure note:** ____________________
- **Spot-check notes (free-text ≤200 chars):** ____________________
```

---

## §9 Aggregate scoring sheet

| Case | Verdict expected | Branch expected | Verdict emitted | Validator | Notes |
|------|------------------|-----------------|-----------------|-----------|-------|
| TC-01 case-01-mode-b-pro-clean-pass | pass | successAssetManifest | _____ | _____ | _____ |
| TC-02 case-02-mode-c-enterprise-clean-pass | pass | successAssetManifest (convergence twin) | _____ | _____ | _____ |
| TC-03 case-03-mode-a-coverage-gap-reshoot | reshoot | errorEnvelope (missing_shot_coverage → production-coord-agent) | _____ | _____ | _____ |
| TC-04 case-04-asset-spec-violation | fail | errorEnvelope (asset_spec_violation → style-replication-agent) | _____ | _____ | _____ |
| TC-05 case-05-asset-firewall-breach | fail | errorEnvelope (asset_firewall_breach) **GATING** | _____ | _____ | _____ |
| — convergence proof (TC-01 ≡ TC-02 bundle) | byte-identical | — | _____ | _____ | _____ |
| (opt) probe-slot11 | fail | errorEnvelope (ingest_agent_failed, attempts 2, route null) | _____ | _____ | _____ |

**Aggregate:** ___ / 5 PASS  ·  convergence proof: ___  ·  slot-11 probe: ___ (advisory)

**Ingest v1.0 LOCK gate decision (ceremony executable IF):**
- [ ] **5/5 PASS** AND
- [ ] **TC-01/TC-02 convergence proof OK** (byte-shape identical bundle) AND
- [ ] **AI Video Gen v1.0 LOCK ceremony CLOSED first** (hard gate #1, chain head) AND
- [ ] **Style Replication v1.0 LOCK ceremony CLOSED first** (hard gate #2) AND
- [ ] **QC Pre-flight v1.0 LOCK ceremony CLOSED first** (hard gate #3 — direct dependency) AND
- [ ] **Day 53 LOCK-CANDIDATE Items 6 + 8 + 11 ratified** AND
- [ ] **Validator output saved to `validation/llm-out/run-results-2026-06-15.txt`** AND
- [ ] **All 5 LLM output JSONs preserved in `validation/llm-out/`**

→ flip SKILL.md `status:` to `v1.0 LOCKED`. Mark Notion ARS hub row LOCKED. Update dashboard `agentic-reel-studio` Ingest chip → `live` (green). Schedule Agent #9 (Edit Director) SPEC outline kickoff.

- [ ] **<5/5 PASS** → log failure(s) + patch the offending system-prompt clause(s) in SKILL.md (only — schemas LOCKED Day 54). Re-run failed cases Day 58. Do NOT promote until 5/5. **TC-05 is a special case: if the GATING fixture fails to catch BOTH injected asset-layer tokens (`detail.hits` < 2), the LOCK is hard-blocked regardless of the other four** — the agent's reason to exist (the 8th-pass asset-layer firewall) did not fire.

---

## §10 Guardrails (do not skip — process integrity attestation)

- ✅ **No engine dispatch + no byte decode, in any mode.** Ingest calls no engine and runs no byte-level decode by design (Hard Rule #2). There is no live mode to misfire. If Opus composes an engine prompt, requests a credential, or emits an `ffprobe`/`MediaInfo`/decode command in any response, abort — Rule #2 violation. `byte_probe_performed: const false` is enforced by the validator.
- ✅ **No credentials anywhere.** The agent references none. ZERO $ engine spend, ZERO $ probe spend; ≤ $3.50 (≤ $4.20 with probe) Opus tokens total.
- ✅ **No schema edits.** Day 54 schemas are LOCKED-as-drafted. Any drift between agent output and schema is an agent issue, not a schema issue. The 7-tuple stays held additively (`minItems 5`) — NOT flipped to exact-7 (Decision D6 doubly-deferred).
- ✅ **No silent v1.0 promotion on partial PASS.** 4/5 PASS = LOCK held. The contract is 5/5 + convergence-proof-OK or nothing. TC-05 under-reporting = hard-block.
- ✅ **No external comms triggered by this runbook.** Validator output is internal evidence. No client emails, no investor pings, no social posts.
- ✅ **No operator-impersonation.** This runbook does NOT close any of the three predecessor LOCK ceremonies, does NOT ratify Items 6/8/11, does NOT commit the Cross-SPEC §3.9 amendment, does NOT flip any version tag or dashboard chip. All operator-only and remain PENDING until the operator acts.
- ✅ **No fake-advance.** No LLM Test Runbook executed by Donna — this document is the paste-and-run artifact for the operator's sit-down. The validator is schema + fixture-expectation checking, not an LLM run.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. The HC/NPOX tokens in the §5 FIREWALL list are the firewall's BLOCK-list (so the gate rejects them) — not a cross-entity reference. The `sln` + `holdcogroup.com` tokens in TC-05 are the gating fixture's asset-layer catch surface. REINVENTED is the pilot brand inside the fixtures.
- ✅ **Rest Day honored** — this Day 57 build runs Monday Jun 15; the next Sunday (Jun 21) is docs-prep only.

---

## §11 Carry-over visibility block (Notion + dashboard + operator items)

**Operator-only action items (DO NOT advance silently):**

1. **Close AI Video Gen v1.0 LOCK ceremony** (HARD GATE #1 — chain head): Day 27 LLM Test 5/5 (or re-run) · version tag flip + Notion + dashboard chip `live`.
2. **Close Style Replication v1.0 LOCK ceremony** (HARD GATE #2): Day 36 LLM Test 5/5 (runbook paste-and-run ready) · version tag flip + Notion + dashboard chip `live`.
3. **Close QC Pre-flight v1.0 LOCK ceremony** (HARD GATE #3 — Ingest's DIRECT dependency): Day 47 LLM Test 5/5 (runbook paste-and-run ready) · Items 6/8/11 ratified · version tag flip + Notion + dashboard chip `live`.
   - **Order note:** dependency order is AI Video Gen → Style Replication → QC Pre-flight → Ingest. All four LOCKs pending.
4. **Ingest Day 53 LOCK-CANDIDATE Items 6 + 8 + 11** (~15–30 min · 3 independent actions, any order):
   - Item 6 — cost-model confirm (lightest in fleet history — `cost_incurred_usd ≈ $0.00`, no vendor URLs, no ceilings owned). Donna recommends RATIFY.
   - Item 8 — 15-decisions walk; explicit verdict on D15 (Edit-Director handoff → Notion holding store). Donna recommends RATIFY (D6 doubly-deferred).
   - Item 11 — Cross-SPEC §3.9 n-tuple amendment (the 7-tuple `parent_chain` forcing function). Donna recommends RATIFY-AS-DRAFTED. NOT a test-gate dependency (validator accepts 5/6/7-tuples).
5. **Day 57 main session — execute this runbook** (20–35 min). Opus Workbench paste-and-run for all 5 cases (+ optional slot-11 probe). Save outputs + run §5 validator + record PASS/FAIL aggregate.
6. **LOCK ceremony** — IF 5/5 PASS + convergence-proof-OK + all three predecessor LOCKs CLOSED + Items 6/8/11 ratified → flip version tag + Notion + dashboard chip. Then schedule Agent #9 (Edit Director) SPEC outline.

**Dashboard `agentic-reel-studio` updates queued for Day 57 close (Donna executes via `mcp__cowork__update_artifact` if the artifact exists):**
- "Today's Output" → "Day 57 Ingest v1.0 LLM Test Runbook authored (~12 sections · paste-and-run · no-engine/no-byte-probe gate · 5 fixtures + slot-11 probe + convergence proof)"
- Ingest chip stays `spec` (yellow) until the ceremony closes — chip flip is part of the LOCK ceremony, NOT this runbook.

---

## §12 Files produced by this runbook (post-run)

After the operator's Day 57 sit-down completes (regardless of pass/fail outcome):

- `validation/llm-out/case-NN-<slug>-output.json` × 5 — raw Opus output per case
- `validation/llm-out/probe-slot11-output.json` — (optional) the slot-11 adversarial probe output
- `validation/llm-out/run-log-2026-06-15.md` — run-log template filled in × 5 (6 with probe)
- `validation/llm-out/run-results-2026-06-15.txt` — captured §5 validator output
- (On 5/5 PASS + convergence-OK + all three predecessor LOCKs closed + Items 6/8/11 ratified) ceremony: update `skills/ingest-agent/SKILL.md` frontmatter `status:` field
- (On same) ceremony: update Notion ARS hub row → LOCKED
- (On same) ceremony: update dashboard `agentic-reel-studio` Ingest chip → `live` (green)

---

## Sources consulted in authoring this runbook

- `ars/skills/ingest-agent/SKILL.md` (Day 55 — system prompt verbatim · 12 hard rules · 11-step loop · §4.8 target manifest shape · verdict↔route map · 8-code/slot-11)
- `ars/skills/ingest-agent/schemas/{input,output}.schema.json` (Day 54 LOCKED-as-drafted · META-SCHEMA VALID · AND-of-8-gates const · no-hold · reshoot if/then · slot-11 · 5/6/7-tuple)
- `ars/skills/ingest-agent/test-cases/case-NN-*/{scenario.md,input.json,expected_output.json}` × 5 (Day 55 fixture canon)
- `ars/skills/ingest-agent/validate.py` (Day 55 — 47/47 harness; the §5 validator extends it to score live LLM output + the convergence proof)
- `ars/skills/ingest-agent/README.md` (Day 55 invocation guide)
- `ars/ARS-2026-06-11-Day-53-Ingest-Agent-v1-LOCK-CANDIDATE.md` (Day 53 LOCK candidate · 15 decisions · Items 6/8/11)
- `ars/ARS-2026-06-09-Day-51-Ingest-Agent-SPEC-Body-Partial-1.md` (§6.3 8-code/slot-11 · §7.1 system prompt source · canonical firewall list)
- `ars/ARS-2026-06-05-Day-47-QC-Preflight-LLM-Test-Runbook.md` (structural pattern source — this runbook is the Ingest analog: same no-engine discipline, plus the no-byte-probe contract, the no-hold divergence, the reshoot if/then, and the mode-convergence proof)
- `ars/build-log-2026-06-13.md` (Day 55 log — names the LLM Test Runbook as the next forward deliverable; lists the three hard gates + the slot-11 adversarial case)

---

*Day 57 runbook authored ahead of the iMac sit-down so the operator can paste-and-run without re-deriving any step. Ingest ties QC Pre-flight as the cheapest LOCK gate in the fleet — it dispatches NO engine and (uniquely) runs NO byte-level decode, so there is no engine-stub block and no live-vs-dry-run cost delta — total spend ≤ $3.50 Opus tokens (≤ $4.20 with the slot-11 probe), $0.00 engine, $0.00 probe. Dry-run is the v1.0 LOCK gate. 5/5 PASS + the TC-01/TC-02 mode-convergence proof + AI Video Gen LOCK + Style Replication LOCK + QC Pre-flight LOCK closed + Day 53 Items 6/8/11 ratified = Ingest v1.0 LOCKED ceremony executable. TC-05 is the gating fixture — if the 8th-pass asset-layer firewall fails to catch BOTH injected tokens (`sln` filename + `holdcogroup.com` sidecar caption, `detail.hits` < 2), the LOCK is hard-blocked regardless of the other four — the agent's reason to exist did not fire. Recommend-don't-clear is schema-enforced (`human_review_required: const true` + `byte_probe_performed: const false` on every branch); there is NO `hold` verdict (deliberate divergence — Ingest's domain is deterministic). False-pass is structurally impossible (AND-of-8-gates const). Entity boundary respected (Sequel Digital ARS; REINVENTED as pilot brand inside fixtures; HC/NPOX tokens are the firewall block-list). The 7-tuple parent_chain (Item 11 / Decision D6) remains DOUBLY-DEFERRED and is NOT a test-gate dependency — the validator accepts 5-, 6-, and 7-tuples. No operator-only action was advanced or impersonated.*
