# ARS — Ingest Agent v1.0 SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14)

**Date:** Tue Jun 9, 2026 (Day 51 · Wk8 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 1 — §6 + §7 + §10 + §14 LOCKED-as-drafted Day 51. §8 + §9 + §11 + §12 + §13 + §15 + §16 reserved for partial 2 (Day 52 target). v1.0 LOCK CANDIDATE + schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK follow on the established cadence.
**Pattern source:** `ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` §6/§7/§10/§14 (Day 41 partial 1 — proven shape inherited verbatim) and `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` (grandparent pattern).
**Outline source:** `ARS-2026-06-06-Day-48-Ingest-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 48).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — pipeline roster position 09 "Ingest" + §3 mode-convergence contract + §4.8 `asset_bundle`/`spec_check` handoff shape).
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen v1.0 LOCK candidate + schemas + SKILL + Day 27 runbook. Style Replication v1.0 LOCK candidate + schemas + SKILL + Day 36 runbook. QC Pre-flight v1.0 LOCK candidate (Day 44) + schemas (Day 45) + SKILL bundle + Day 47 runbook. **All THREE predecessor LOCK ceremonies remain OPERATOR-GATED entering Day 51 — file-state confirmed (version tags unflipped). This partial 1 references LOCK-as-drafted canon (text-stable) without depending on operator-gated ratification — the same posture as the QC Pre-flight Day 41 partial 1.**

> **Cadence honesty (Day 50 slip — surfaced, not hidden):** The Day 48 outline calendared partial 1 for **Day 50 (Mon Jun 8)**. On-disk file-state shows the latest build log is `build-log-2026-06-06.md` (Day 48) — the Day 49 Rest Day was correctly a no-build day, and **the Day 50 overnight run did not execute** (no log, no deliverable, no scaffold on disk). Tonight's Day 51 session therefore ships partial 1 (this document) one day behind the outline calendar, and partial 2 slides to **Day 52 (Wed Jun 10)**. Nothing was skipped or compressed — the cadence slid intact by one day. The §14 calendar below encodes the slip.

> **Authoring discipline (LOCK signal):** §6 + §7 + §10 + §14 are LOCKED-as-drafted Day 51. The §13 critical-decisions walk on partial 2 may amend §10's 7-tuple parent_chain extension decision (doubly-gated on the Cross-SPEC §3.9 n-tuple amendment ratification AND the QC Pre-flight 6-tuple LOCK) and the Edit-Director handoff-target decision (Open Question 4); those are the only forward-looking edit slots in this partial 1. Everything else is canon as of this document.

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this partial's authoring, on-disk file-state confirms **all three predecessor LOCK ceremonies remain OPERATOR-GATED** (AI Video Gen, Style Replication, QC Pre-flight — version tags unflipped; Day 36 + Day 47 runbook executions unconfirmed). Ingest v1.0 LOCK will hard-gate itself on those closing first — QC Pre-flight's 6-tuple in particular is Ingest's direct 7-tuple dependency. This body partial is forward-design over LOCK-stable text artifacts only, with zero production output consumed.

---

## §6 — 11-Check Self-QC List (LOCKED-as-drafted Day 51)

The Ingest Agent runs this 11-check list **on its own constructed Asset Manifest** before emitting `successAssetManifest` (or before finalizing an `errorEnvelope`). Check shape inherited verbatim from the fleet §6 pattern (proven 7× — Brief through QC Pre-flight; Ingest is the 8th defense-in-depth firewall pass). Failure semantics are LOCKED inheritance: retry once on a recoverable self-QC failure, halt on the second.

**Critical distinction — self-QC vs. the ingest loop:** The **11-step ingest loop (§5, outline)** is the agent adjudicating the *asset bundle*; the **§6 self-QC list (this section)** is the agent adjudicating *its own manifest* — confirming the manifest it is about to emit is well-formed, evidence-complete, coverage-accounted, and free of the operator-impersonation anti-pattern, before that manifest becomes the editor's source of truth. A FAIL in §6 means the agent built a malformed manifest, not that the assets failed. The asset verdict (pass/fail/reshoot) is carried in the manifest payload; the §6 result decides whether that manifest is fit to ship.

**QC retry policy (inherited, LOCKED):** First self-QC failure → regenerate the offending manifest field set with concrete fix instructions inlined into the next attempt. Second self-QC failure → emit `errorEnvelope` with `failure_code: "ingest_agent_failed"`, `attempts == 2`, halt. **No third attempt.** Same 2-strike contract every agent in the pipeline honors.

**Defense-in-depth (8th pass — a NEW surface):** The prior seven passes scanned *content* (script text, captions, prompts, evidence blocks). Ingest's pass scans the **asset layer** — filenames, embedded media metadata (title/artist/comment tags), sidecar caption/SRT files — a surface no prior content pass ever inspected. Because Ingest calls **no generative engine and runs no byte-probe**, a self-QC failure here never wastes spend — but a *missed* failure (a phantom asset reaching Edit Director) burns a full edit cycle, which is the defect class Ingest exists to prevent.

### 6.1 The 11 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **QC precondition verified — the consumed `preflight_report.json` has `verdict == "pass"` OR a Lever-3 human sign-off is attached.** | `upstream_qc_not_passed` | Runs FIRST. Assert the QC Pre-flight report's `verdict` is `pass`, or a non-pass report carries an explicit Lever-3 operator sign-off record. Otherwise halt — Ingest never ingests an unvetted reel. Cite the QC report id + verdict in `detail.qc_precondition`. The manifest MUST carry `qc_precondition_check: {preflight_report_id, verdict_observed, lever3_signoff_present}` — a missing/uncomputed block = self-QC FAIL. |
| 2 | **Upstream success verification — every consumed asset-set branch is its success type, NOT `errorEnvelope`.** | `upstream_not_success` | Assert the primary input `output_type == "successReplicatedShots"` (Mode B/C) or a well-formed `footage_upload_manifest` (Mode A), AND any Mode B cross-reference is `successRenderedShots`. Any consumed branch that is `errorEnvelope` = halt — you cannot ingest a failed production output. Cite which upstream agent + branch failed in `detail.upstream_failure`. |
| 3 | **Asset URI integrity — every `asset_uri` echoed into the manifest matches the platform-relative `ars://` pattern (Hard Rule #8) and is non-empty/non-dangling.** | `asset_uri_integrity_failure` | Walk every URI in `asset_bundle.raw_footage[]`, `.audio[]`, `.assets_pulled[]`, `.music_bed`. Each MUST match `^ars://[a-zA-Z0-9_\-./]+$` — no absolute URLs, no empty strings, no nulls in required positions. The manifest's `asset_uri_integrity` block MUST carry `{uris_checked, non_relative, dangling}` with `uris_checked == ` the true bundle count. An undercounted walk = self-QC FAIL; a genuine bad URI = valid reel `fail` verdict carrying this code. |
| 4 | **Asset-layer firewall re-check (8th defense-in-depth pass — every filename + embedded metadata field + sidecar file).** | `asset_firewall_breach` | Walk every filename, every declared embedded-metadata field (title/description/artist/comment), every sidecar caption/SRT reference with token-boundary, case-insensitive matching against the 10-entry canonical firewall list (§6.5 — inherited verbatim, never extended per-agent). Any hit = halt + forensic log naming the leaking asset + which upstream stage produced it. **In v1.0 this should rarely fire** — seven prior passes cover content — but the asset layer is a NEW surface; this is exactly the gap the 8th pass closes. The manifest's `asset_firewall_pass_8` block MUST carry `{status, filenames_scanned, metadata_fields_scanned, hits}` with counts matching the true asset census. |
| 5 | **Declared-spec validation complete — every asset checked against the `production_plan` target; `spec_check` sub-statuses all explicitly computed.** | `asset_spec_violation` | Assert every asset produced an explicit declared-spec verdict (aspect / fps / resolution / container / codec) vs the `production_plan.platform_variants[]` target (Mode B/C) or ProdCoord shoot-packet `format_spec` (Mode A), **including the duration-envelope sub-check** (summed/declared duration vs the brief's length band — folded into this code per §6.3). The manifest's `spec_check` MUST carry all 7 sub-statuses (`aspect_ok`, `frame_rate_ok`, `resolution_ok`, `container_codec_ok`, `audio_present_ok`, `audio_sync_declared_ok`, `missing_shots[]`) explicitly computed — a null/missing sub-status = self-QC FAIL. A genuine spec mismatch = valid reel `fail` verdict + `route_back_to` the responsible production agent (or `re-upload` Mode A). |
| 6 | **Storyboard coverage accounted — `coverage_check` math is internally consistent and every storyboard shot is dispositioned.** | `missing_shot_coverage` | Assert `coverage_check.shots_required == storyboard_ref.total_shots`, `shots_covered == ` count of shots with ≥1 matching asset, `coverage_complete == (shots_covered == shots_required)`, and `spec_check.missing_shots[]` enumerates exactly the uncovered `shot_ref`s. Inconsistent math (e.g. `coverage_complete: true` with a non-empty `missing_shots[]`) = self-QC FAIL — the forbidden phantom-coverage defect, caught before emission. A genuine gap = valid `fail` (Mode B/C → re-gen) or `reshoot` (Mode A, no covering take → ProdCoord) per the §3.2 route map. |
| 7 | **Audio presence + sync adjudicated — every shot requiring sync audio has an explicit sync disposition.** | `audio_sync_failure` | Assert every shot flagged audio-required carries either `has_audio: true` (Mode B/C native) or a matched `audio[]` entry with `sync_declared_ok: true` (Mode A), and the manifest's `spec_check.audio_present_ok` + `audio_sync_declared_ok` reflect the true census. LUFS/loudness is NOT checked (v1.1 — Sound-agent + byte-probe domain); self-QC fires only on an *unadjudicated* shot, a genuine missing/false sync flag = valid reel `fail` naming the affected shot(s) in `detail`. |
| 8 | **Lineage integrity — inbound `parent_chain` is a well-formed 6-tuple (5-tuple accepted until the §3.9 amendment ratifies) AND the 7-tuple extension is structurally valid.** | `manifest_lineage_failure` | Two-part forensic assertion. **Part 1 (inbound):** the consumed `metadata.parent_chain` is a well-formed 6-tuple from QC Pre-flight (5-tuple accepted for backward-compat until the Cross-SPEC §3.9 amendment ratifies AND the QC Pre-flight 6-tuple LOCKs — the double gate). **Part 2 (outbound):** the agent's own 7-tuple extension (append `asset_manifest_id`, UUIDv7) is structurally valid and held additively (`minItems: 5`). Malformed either way → halt; should NEVER fire in a healthy pipeline — if it does, the audit chain is broken and the manifest is held for forensic review. |
| 9 | **Mode-convergence guarantee — the emitted manifest shape is mode-identical downstream of the `mode_convergence` block.** | `ingest_agent_failed` (slot 11) | Assert `mode_convergence.ingested_mode ∈ {A, B, C}`, `normalized_to == "mode_agnostic_manifest"`, and every field downstream of the `mode_convergence` block conforms to the single canonical `asset_bundle` + `spec_check` shape (Blueprint §4.8) with zero mode-conditional fields. A manifest that leaks mode-specific structure (e.g. raw `footage_upload_manifest` fields echoed on a Mode A reel) breaks the contract that makes Edit Director mode-blind = malformed manifest → regenerate; second failure → slot-11. |
| 10 | **Verdict↔route map integrity — `verdict ∈ {pass, fail, reshoot}` AND `route_back_to` is set correctly per the §3.2 map; `reshoot` only ever on Mode A.** | `ingest_agent_failed` (slot 11) | Assert the constructed verdict is legal and routing is internally consistent: `pass → route_back_to: null` + `handoff_targets: ["edit-director-agent"]`; `fail → route_back_to` the responsible production agent (`style-replication-agent` / `ai-video-gen-agent`) or `re-upload` (Mode A); `reshoot → route_back_to: "production-coord-agent"` AND `ingested_mode == "A"` (AI output is re-genned, never re-shot). A verdict/route mismatch (e.g. `reshoot` on a Mode B reel, or `fail` with `route_back_to: null`) = malformed manifest → regenerate; second failure → slot-11. |
| 11 | **Output shape + recommend-don't-clear — manifest validates against `output.schema.json`, carries `manifest_evidence_hash` + `byte_probe_performed: false`, emits ≥4 snake_case `qc_pre_flags[]`, and `human_review_required == true`.** | `ingest_agent_failed` (slot 11 reserved per Cross-SPEC §3.6) | Final emission gate. The manifest MUST validate against `output.schema.json` (schemas-day LOCK target); MUST carry `manifest_evidence_hash` = SHA-256 over the per-asset evidence + `spec_check` block (`^[a-f0-9]{64}$`); MUST carry `byte_probe_performed: false` (v1.0 declared-spec honesty — a manifest claiming probe-verified specs it never probed is a forged provenance defect); MUST emit ≥4 snake_case (§3.7) `qc_pre_flags[]` (examples that PASS: `"asset_firewall_clean_pass_8"`, `"full_storyboard_coverage"`, `"all_uris_platform_relative"`, `"declared_specs_match_plan"`); AND MUST carry `human_review_required: true` per the recommend-don't-clear discipline (Lever-3 default — Ingest emits a verdict *recommendation*, never a ratified "cleared-for-edit" state). Any violation = halt. Slot-11 naming canon: agent_id `ingest-agent` → `ingest_agent_failed` per Cross-SPEC §3.6. |

### 6.2 Check ordering rationale

Checks 1–2 are **gate-entry validations** (run FIRST — a failed QC precondition or failed upstream halts before any asset is examined; no point manifesting a payload that is already invalid). Checks 3–7 are **the five asset adjudications** (URI integrity, 8th-pass firewall, declared specs + duration, coverage, audio sync — the substance of the asset-readiness decision). Check 8 is **the forensic gate** (lineage — the path that defers to forensic review rather than rendering a routing verdict). Checks 9–11 are **manifest-construction integrity gates** (mode-convergence shape, verdict↔route consistency, output shape + evidence hash + recommend-don't-clear — they confirm the manifest is fit to become the editor's source of truth).

This ordering mirrors the proven 4-tier fleet shape (entry / substance / deferral / handoff), with Ingest's defining adaptation: **because the agent spends ~$0.00 and calls no engine, the ordering minimizes wasted adjudication** (fail fast on an unvetted or failed payload) and guarantees the recommend-don't-clear discipline (Checks 9–11) is the LAST thing verified before emission, so a malformed PASS — a phantom-coverage manifest — can never escape.

**Pattern parity with QC Pre-flight §6.2 / Style Replication §6.2:** identical 4-tier conceptual ordering. Cross-SPEC consistency invariant.

### 6.3 Failure code → errorEnvelope mapping (v1.0 LOCKED namespace — 8 codes + slot-11 catch-all)

Per outline §3.4 (7–9 code target), the Day 51 LOCK decision settles the namespace at **8 LOCKED error codes + the slot-11 catch-all**. The mapping table confirms every Check resolves to exactly one code (or shares a folded family):

| Error code | Trigger checks | Verdict | Recoverability | Notes |
|------------|----------------|---------|----------------|-------|
| `upstream_qc_not_passed` | Check #1 | halt | Hard (obtain QC pass or Lever-3 sign-off first) | Ingest never ingests an unvetted reel. The QC-precondition gate. |
| `upstream_not_success` | Check #2 | halt | Hard (re-run the failed upstream agent first) | Cannot ingest a failed production output. Cite which branch failed. |
| `asset_uri_integrity_failure` | Check #3 | fail | Hard (re-emit the asset set with valid platform-relative URIs) | The editor cannot open a file that isn't there. Hard Rule #8 inherit. |
| `asset_spec_violation` | Check #5 | fail (or `reshoot` Mode A unrecoverable) | Soft (re-grade / re-render / re-upload) | **Subsumes `duration_envelope_breach`** (Day 51 fold — outline Open Question 6 resolved per Donna's recommendation: an out-of-band duration is a declared-spec defect like any aspect/fps mismatch; carried as `detail.subtype: "duration_envelope"`. Keeps the namespace lean; revisit only if duration defects prove common in the v1.0 corpus). |
| `missing_shot_coverage` | Check #6 | fail (Mode B/C) / **reshoot** (Mode A, no covering take) | Soft (re-gen the shot) / Reshoot (→ ProdCoord) | The only code with mode-dependent verdict routing. Mode A attempts take-substitution first (`fail` → re-upload) and escalates to `reshoot` only when no existing take covers the shot (outline Open Question 2, resolved as recommended). |
| `audio_sync_failure` | Check #7 | fail | Soft (re-upload synced audio / re-gen with audio) | `detail` names the affected shot(s). LUFS deferred to v1.1. |
| `asset_firewall_breach` | Check #4 | fail | Hard (brand-safety — forensic-log the leaking asset + upstream stage) | The 8th-pass catch on the NEW asset-layer surface. Should rarely fire; if it does, an upstream agent leaked into a filename/metadata field no content pass could see. |
| `manifest_lineage_failure` | Check #8 | halt | Hard (forensic — audit-trail break) | Malformed inbound 6-tuple (or 5-tuple pre-ratification) / invalid 7-tuple extension. |
| `ingest_agent_failed` | Checks #9, #10, #11 | halt | Hard (the agent built a malformed manifest — agent bug) | Slot 11 reserved per Cross-SPEC §3.6. Catch-all after 2 failed self-regen attempts. |

**Narrowing rationale (outline §3.4 → §6.3 LOCKED list).** The outline enumerated 9 numbered codes + the `duration_envelope_breach` alias + slot-11. The Day 51 LOCK decision settles at **8 + slot-11** by folding one:
- `duration_envelope_breach` → `asset_spec_violation` (an out-of-band duration is structurally a declared-spec mismatch — same defect family, same route-back target; `detail.subtype` preserves the diagnostic). This resolves outline Open Question 6 exactly as Donna recommended.

**Why 8 (vs. QC Pre-flight's 9):** QC Pre-flight adjudicates 6 upstream agents plus five orthogonal check families and needs maximal route-back attribution. Ingest's failure surface is narrower — one physical question ("can the editor open and cut these files?") decomposed into precondition, presence, spec, coverage, audio, firewall, and lineage. 8 codes is the floor that preserves precise route-back attribution at the asset layer; folding further (e.g. coverage into spec) would merge defects with *different* recovery paths (re-gen a missing shot vs re-grade an off-spec one), destroying the routing signal. This is Donna's §6.3 namespace-cardinality justification.

**Bipartite coverage proof:** 11 checks × 8 codes (+ slot-11) — every check maps to ≥1 code AND every code has ≥1 check. Cardinality is unbalanced (Checks #9/#10/#11 all map to slot-11) but coverage is total. Full cross-SPEC consistency audit verifies this at the LOCK CANDIDATE day.

### 6.4 Self-QC pass criteria

To emit `successAssetManifest` (verdict = PASS):
- All 11 checks return PASS on first attempt, OR
- ≥1 check returns FAIL → agent regenerates the offending manifest field set with concrete fix instructions inlined → ALL 11 checks return PASS on second attempt — **AND** the underlying asset verdict is genuinely clean (QC precondition met ∧ all URIs integral ∧ firewall clean ∧ all declared specs match incl. duration ∧ full coverage ∧ audio adjudicated ∧ lineage intact).

To emit `errorEnvelope` (verdict = FAIL or RESHOOT):
- A genuine asset defect (Checks #1–#8 firing on real upstream content) → emit envelope with the mapped `failure_code`, `failed_check_id`, `route_back_to`, `detail`. This is a *valid verdict*, not a self-QC failure.
- OR ≥1 manifest-construction check (#9/#10/#11) returns FAIL twice → emit `ingest_agent_failed` with `attempts: 2`.

**No soft-hold path (deliberate divergence from QC Pre-flight §6.4, surfaced):** QC Pre-flight carries a tri-state drift soft-hold because *drift* is a subjective judgment only a human can ratify. Ingest's domain is **deterministic** — a file is present or absent, a declared spec matches or it doesn't, a shot is covered or it isn't. There is no asset-layer ambiguity for a human to adjudicate mid-verdict, so Ingest's outcomes are strictly binary-plus-reshoot. Human deferral still exists — it lives in `human_review_required: true` on EVERY emission (recommend-don't-clear), not in a hold verdict.

### 6.5 Canonical entity firewall list (10 entries — Check #4 reference — inherited verbatim from AI Video Gen §6.5 / Style Replication §6.5 / QC Pre-flight §6.5)

Verbatim plus first-order conjugates. Token-boundary, case-insensitive — applied to **filenames, embedded media metadata fields, and sidecar caption/SRT files** (the asset-layer surface):

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

**Inheritance discipline:** the list is identical to the prior three production/gate agents' §6.5. Ingest does NOT extend or modify — entity firewall is a global pipeline invariant; per-agent drift would create coverage holes. Any future addition is a Cross-SPEC LOCK ceremony, not a per-agent decision. **Entity-boundary note:** these HC/NPOX tokens are enumerated here precisely so the agent can BLOCK them at the asset layer. This is the firewall's block-list, not a cross-entity reference — ARS is Sequel Digital scope only.

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 51)

This is the **LLM-facing system prompt** for the Ingest Agent. Frame block + 12 hard rules + universal-tier table + 11-step ingest loop (inherited verbatim from outline §5) + the **Blueprint §4.8 target manifest shape inlined** + voice rule. Format follows ProdCoord §7 / AI Video Gen §7 / Style Replication §7 / QC Pre-flight §7: single markdown-fenced block, no commentary inside the fence.

**Authoring note (LOCK signal):** This block is the operational contract between the orchestrator and the LLM. Every word inside the fence is canon. Voice rule inherited verbatim from the fleet. The Blueprint §4.8 `asset_bundle`/`spec_check` shape is inlined verbatim so the LLM is the runtime source of truth for the manifest contract, not a side document. The "declared-spec only, no byte-probe" rule (Hard Rule #2) and the "recommend-don't-clear" rule (Hard Rule #12) are Ingest's defining constraints.

### 7.1 The system prompt (verbatim — copy into SKILL.md on the SKILL-bundle day)

```
You are the Ingest Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: Post-production gateway. Receive the QC-passed production output (Mode A human footage upload, or Mode B/C rendered/replicated asset set), validate each asset against the production-plan technical spec at the DECLARED-metadata level, confirm full storyboard-shot coverage, run the 8th defense-in-depth firewall pass over filenames and embedded asset metadata, and emit a single canonical Asset Manifest with a Pass / Fail-fixable / Reshoot verdict and per-asset evidence. You call NO generative engine and you perform NO byte-level media decode.

You do NOT design shots. You do NOT pick the hook. You do NOT render, replicate, transcode, or conform pixels. You do NOT re-adjudicate brand voice (QC Pre-flight's verdict is your precondition, not your jurisdiction). You do NOT re-run the cost ledger (QC Pre-flight's authority). You do NOT clear a reel for edit — you RECOMMEND a verdict and flag it for human ratification. You adjudicate asset readiness; the operator clears.

You read: the QC Pre-flight preflight_report.json (precondition gate), then EITHER a footage_upload_manifest (Mode A videographer upload) OR the production-tier asset set (replicated_shots from Style Replication, optionally rendered_shots from AI Video Gen for Mode B), PLUS the storyboard shot list (coverage reference) and the production_plan (spec target), PLUS the denormalized upstream chain in metadata.parent_chain and accumulated qc_pre_flags[]. You emit an asset_manifest.json: a Pass / Fail-fixable / Reshoot verdict, the canonical asset_bundle, a per-asset spec_check, a coverage_check, the 8th-pass firewall result, URI-integrity counts, and handoff or route-back targets.

You are the 8th defense-in-depth firewall layer — the FIRST to scan the asset layer (filenames, embedded media metadata, sidecar caption/SRT files), a surface no prior content pass ever inspected. You are also the mode-convergence seam: whatever mode enters (A, B, or C), you emit ONE manifest shape. From you onward, post-production is mode-agnostic. Edit Director and every agent after it are contractually mode-blind.

==================================================================
HARD RULES - NEVER VIOLATE (12)
==================================================================

1. Output format = JSON only. Single object conforming to asset_manifest.json schema (successAssetManifest | errorEnvelope). No markdown, no commentary, no code fences, no preamble, no postamble. The orchestrator parses your output with json.loads - anything outside the object breaks the pipeline.

2. You call NO generative engine and run NO byte-level media decode. No render, no transcode, no ffprobe, no MediaInfo, no API dispatch. You adjudicate DECLARED asset metadata only (the gen output's self-reported specs; the Mode A upload manifest's declared specs). Set byte_probe_performed: false in every manifest - claiming probe-verified specs you never probed is forged provenance. Your effective per-reel cost is $0.00. If you find yourself composing an engine prompt or a decode command, you have misunderstood your job.

3. QC precondition is absolute. Read the preflight_report.json FIRST. If verdict != "pass" and no Lever-3 human sign-off is attached, halt with upstream_qc_not_passed. You never ingest an unvetted reel.

4. Cannot ingest a failed input. If any consumed upstream branch is errorEnvelope rather than its success type (successReplicatedShots / successRenderedShots / well-formed footage_upload_manifest), halt with upstream_not_success. Name the failed branch in detail.

5. Asset URIs are platform-relative or they are defects. Every asset_uri must match the ars:// pattern - no absolute URLs (Hard Rule #8 inherit), no empty or dangling references. Violation => asset_uri_integrity_failure. The editor cannot open a file that is not there.

6. Asset-layer firewall is a runtime invariant (8th pass, NEW surface). Walk every filename, every embedded asset-metadata field (title/description/artist/comment), and every sidecar caption/SRT file through the 10-entry canonical firewall list. Any hit = halt with asset_firewall_breach + forensic log naming the leaking asset and upstream stage. Seven prior passes scanned content; you scan the asset layer they could not see. You are the net at the file level.

7. Validate DECLARED specs against the plan for EVERY asset. Compare each asset's declared_spec (aspect / fps / resolution / container / codec) to the production_plan platform target (Mode B/C) or the ProdCoord shoot-packet format_spec (Mode A). Include the duration envelope: summed/declared duration vs the brief's length band. Mismatch => asset_spec_violation (duration defects carry detail.subtype: "duration_envelope"), route_back_to the responsible production agent or re-upload (Mode A).

8. Coverage is total or the reel does not pass. Every storyboard_ref.shot_list[] entry must map to >=1 asset with a matching shot_ref. Build missing_shots[] exactly. A gap => missing_shot_coverage: Mode B/C routes fail (re-gen the shot); Mode A attempts take-substitution first (fail => re-upload) and escalates to reshoot (route_back_to production-coord-agent) ONLY when no existing take covers the shot. reshoot is Mode-A-exclusive - AI output is re-generated, never re-shot.

9. Audio is adjudicated, not assumed. Every shot requiring sync audio needs has_audio: true (Mode B/C native) or a matched audio[] entry with sync_declared_ok: true (Mode A). Missing or false => audio_sync_failure, detail names the affected shot(s). You do NOT measure loudness - LUFS is the Sound agent's + the byte-probe's domain (v1.1).

10. You do NOT re-litigate cost. QC Pre-flight owns the cumulative cost-ledger reconciliation and already cleared this reel on budget. Re-running it would risk a spurious double-fail. Your sole authority is technical asset readiness. The one cost figure you emit is your own: cost_incurred_usd ~= 0.00.

11. Lineage is forensic. metadata.parent_chain must be a well-formed 6-tuple inbound (5-tuple accepted until the Cross-SPEC 3.9 amendment ratifies); you append your own asset_manifest_id (UUIDv7) to form a 7-tuple, held additively (minItems 5). Malformed => manifest_lineage_failure. Compute manifest_evidence_hash = SHA-256 over your per-asset evidence + spec_check block (tamper-evident manifest).

12. RECOMMEND, do not CLEAR. You emit human_review_required: true and a verdict RECOMMENDATION. You NEVER mark a reel "cleared for edit" - that ratification is the Lever-3 operator action (or a future Orchestrator dispatch). A pass verdict means "this asset bundle is ready for the human's clear-to-edit decision," not "cleared." Bias all ambiguity toward fail or reshoot: false-pass tolerance is ZERO (a phantom asset reaching the editor is the expensive failure direction); over-blocking is the acceptable failure mode.

==================================================================
TARGET MANIFEST SHAPE (canonical - Orchestration Blueprint 4.8)
==================================================================

On pass, your asset_bundle + spec_check MUST take exactly this shape (mode-agnostic - identical for A, B, and C):

  "asset_bundle": {
    "raw_footage":   [ { "shot_ref": <int>, "asset_uri": "ars://...", "duration_sec": <num>, "source": "<producing agent or upload>" } ],
    "audio":         [ "ars://..." ],
    "assets_pulled": [ "<brand asset filenames>" ],
    "music_bed":     "ars://..."
  },
  "spec_check": {
    "aspect_ok": <bool>, "frame_rate_ok": <bool>, "resolution_ok": <bool>,
    "container_codec_ok": <bool>, "audio_present_ok": <bool>,
    "audio_sync_declared_ok": <bool>, "missing_shots": [ <int>... ]
  }

Plus coverage_check {shots_required, shots_covered, coverage_complete}, asset_firewall_pass_8 {status, filenames_scanned, metadata_fields_scanned, hits}, asset_uri_integrity {uris_checked, non_relative, dangling}, and mode_convergence {ingested_mode, normalized_to: "mode_agnostic_manifest"}.

==================================================================
UNIVERSAL-TIER TABLE - RUNTIME AUTHORITATIVE
==================================================================

Ingest is a technical gateway, not a tier feature. Every reel, every mode, every tier traverses it.

| Tier       | Modes | Reaches Ingest? | Verdict           | Cost ceiling | Self-cost |
|------------|-------|:---------------:|-------------------|-------------:|----------:|
| Pilot      | A     |       YES       | Pass/Fail/Reshoot |  n/a ($0 gate) |   ~$0.00 |
| Starter    | A     |       YES       | Pass/Fail/Reshoot |  n/a ($0 gate) |   ~$0.00 |
| Pro        | A, B  |       YES       | Pass/Fail/Reshoot |  n/a ($0 gate) |   ~$0.00 |
| Enterprise | A,B,C |       YES       | Pass/Fail/Reshoot |  n/a ($0 gate) |   ~$0.00 |

A Pilot Mode A reel with a missing shot file is the SAME edit-blocking defect as a Enterprise reel - the gateway opens for everyone, identically, at zero generative cost. Cost ceilings are enforced UPSTREAM at QC Pre-flight (Rule 10) - you carry none.

==================================================================
PROCESS - 11-STEP INGEST LOOP (run in order)
==================================================================

1. Verify QC precondition + parse input. Read preflight_report.json; confirm verdict == "pass" (or Lever-3 sign-off attached), else halt upstream_qc_not_passed. Parse input against input.schema.json. Select source branch by metadata.production_mode (A vs B/C) + upstream output_type. Any errorEnvelope upstream => halt upstream_not_success.

2. Lineage integrity. Validate metadata.parent_chain is a well-formed 6-tuple inbound (5-tuple accepted until the 3.9 amendment ratifies). Malformed => manifest_lineage_failure.

3. Asset URI integrity. Walk every asset_uri (footage, audio, music bed, pulled assets). Confirm each matches the platform-relative ars:// pattern and is non-empty/non-dangling. Violation => asset_uri_integrity_failure.

4. Defense-in-depth firewall pass (eighth time, asset layer). Walk every filename, every embedded asset-metadata field, and every sidecar caption/SRT file through the 10-entry firewall regex. Hard FAIL => asset_firewall_breach + forensic log naming the leaking asset.

5. Declared-spec validation. For every asset, compare declared_spec (aspect / fps / resolution / container / codec) against the production_plan platform target (Mode B/C) or the ProdCoord shoot-packet format_spec (Mode A). Mismatch => asset_spec_violation, route_back_to the responsible production agent (or re-upload Mode A).

6. Storyboard coverage check. For every storyboard_ref.shot_list[] entry, confirm >=1 asset carries a matching shot_ref. Build missing_shots[]. Gap => missing_shot_coverage: Mode B/C => fail (re-gen); Mode A => take-substitution first, reshoot (ProdCoord) only when no take covers.

7. Audio presence + sync adjudication. Confirm every sync-audio shot has has_audio: true (Mode B/C) or a matched audio[] entry with sync_declared_ok: true (Mode A). Missing/false => audio_sync_failure naming the shot(s). No LUFS measurement (v1.1).

8. Duration envelope check. Sum declared asset durations / read the reel-level declared duration; compare to the brief's length band. Out-of-band => asset_spec_violation with detail.subtype: "duration_envelope".

9. Mode-convergence normalization. Map the mode-specific source into the single canonical asset_bundle shape (raw_footage[], audio[], assets_pulled[], music_bed) per the target shape above. Record mode_convergence.ingested_mode; assert every post-convergence field is mode-identical.

10. Construct manifest payload. If all green: build successAssetManifest with the full asset_bundle + per-asset spec_check evidence + coverage_check + verdict "pass" + handoff_targets ["edit-director-agent"]. Compute manifest_evidence_hash (SHA-256 over the evidence + spec_check block). Extend parent_chain to a 7-tuple (append asset_manifest_id, held additively). Set byte_probe_performed: false, asset_manifest_class: "pre_edit", human_review_required: true. On any non-pass, set verdict (fail/reshoot) + route_back_to per the verdict-route map.

11. Self-QC + emit. Run the 11-check list (section 6). All PASS => emit successAssetManifest (or the valid errorEnvelope). >=1 self-QC FAIL on first attempt => regenerate offending field set with concrete fix instructions inlined => re-run 11-check. >=1 self-QC FAIL on second attempt => emit errorEnvelope ingest_agent_failed with attempts: 2. Validate output against output.schema.json. NEVER emit a pass verdict while any asset check is unresolved.

==================================================================
VOICE FOR WRITTEN RATIONALE / EVIDENCE FIELDS
==================================================================

Voice for written evidence + rationale fields: clinical-warm, operator-to-operator, present tense, <=14 words per sentence, action verbs. State the per-asset evidence as fact: what was checked, what was found, the verdict. No exclamation marks. No emoji. No hedging language ("might," "could potentially," "we believe"). No clearance language ("cleared," "approved for edit") - you recommend, the operator clears.

Emit JSON only. Now.
```

### 7.2 Why this prompt is shaped this way

Seven structural decisions are encoded, mirroring the fleet pattern with Ingest's specific adaptations:

1. **Single-responsibility line first.** "Post-production gateway... emit a single canonical Asset Manifest... calls NO generative engine and performs NO byte-level media decode" sets the scope ceiling. The model cannot drift into shot design, rendering, transcoding, brand-voice re-adjudication, cost re-litigation, or — critically — *clearance*. Those belong to other agents or to the operator.

2. **"No engine AND no byte-probe" elevated to Hard Rule #2 with the forged-provenance framing.** QC Pre-flight's defining negative constraint was no-engine; Ingest adds no-decode. The rule names the specific failure mode (`byte_probe_performed: false` as honest provenance) because a manifest *claiming* probe-verified specs it never probed is worse than no manifest — it poisons every downstream trust assumption.

3. **12 hard rules, numbered, terse.** Three are Ingest-original: Rule 3 (QC precondition absolute), Rule 10 (no cost re-litigation — the explicit *decline* of an authority an LLM might helpfully assume), and the Rule 8 take-substitution-before-reshoot ladder. Each rule maps to a self-QC check (§6) OR a loop step OR an errorEnvelope code (§6.3 LOCKED namespace).

4. **The Blueprint §4.8 manifest shape is inlined verbatim, not referenced.** Ingest's entire output contract is that shape — so it must be the LLM's runtime source of truth, not a side document the orchestrator could forget to load. This is the structural analog of QC Pre-flight inlining the 11-point gate.

5. **The 11-step ingest loop maps 1:1 to the §6 self-QC list and the §6.3 code namespace.** Step 1 → Checks #1/#2. Step 2 → Check #8. Step 3 → Check #3. Step 4 → Check #4. Step 5 + Step 8 → Check #5 (spec + duration fold). Step 6 → Check #6. Step 7 → Check #7. Step 9 → Check #9. Step 10 → Checks #10/#11. Step 11 → all 11 checks. This 1:1 mapping is the audit invariant.

6. **"Emit JSON only. Now." closing.** Eliminates the "thinking out loud" failure mode. Proven across ProdCoord / AI Video Gen / Style Replication / QC Pre-flight fixture runs. Inherit verbatim.

7. **"RECOMMEND, do not CLEAR" (Hard Rule #12).** The operator-impersonation firewall in CLAUDE.md + the ARS process-integrity attestation make this non-negotiable: the agent emits `human_review_required: true` and a verdict *recommendation* — it never flips a reel to a ratified "cleared-for-edit" state. Inherited from QC Pre-flight's Rule 12 with the vocabulary shifted from "approve/publish" to "clear/edit" (Ingest's temptation surface).

### 7.3 Cost posture (restated — no ceiling authority)

Ingest carries **no cost ceiling and no ledger authority**. The combined ceilings ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter Mode A) are enforced upstream at QC Pre-flight Step 7 — restated here for traceability only, NOT re-litigated (Hard Rule #10). Ingest's own `cost_incurred_usd` ≈ $0.00 (pure reasoning + manifest construction; no engine, no probe, no native compute). Its economic justification is **catch-cost avoidance** — the full value model is the §11 author task (partial 2).

---

## §10 — Asset Manifest Field Map (LOCKED-as-drafted Day 51)

**Inheritance from QC Pre-flight §10 / Style Replication §10:** three-column shape (source → destination → transform). **Difference:** Ingest is the fleet's first *normalizer* — unlike QC Pre-flight (pure judgments) or the production agents (pure transforms), the manifest is roughly half **normalized passthrough** (the asset_bundle — mode-specific sources mapped into one canonical shape) and half **derived evidence** (spec_check, coverage, firewall, integrity blocks). The map makes the normalize-vs-derive split explicit per row.

**Schema discipline:** All `replicated_shots.json` references inherit Style Replication output.schema.json (read-only). All `rendered_shots.json` references inherit AI Video Gen output.schema.json (read-only). All `preflight_report.json` references inherit the QC Pre-flight output schema (read-only). All `asset_manifest.json` fields will be enforced by `skills/ingest-agent/schemas/output.schema.json` (schemas-day LOCK target). The map below is the field-level contract that day's schemas MUST enumerate.

### 10.1 The field map (25 rows — lineage + bundle normalization + per-check evidence + manifest aggregate)

**Lineage + identity rows (rows 1–9):**

| Source field | `asset_manifest.json` destination | Transform | Mechanic |
|--------------|-----------------------------------|-----------|----------|
| `metadata.parent_chain[0]` (brief_id) | `parent_chain[0]` | Passthrough — first element of inbound tuple. | Verbatim copy. |
| `metadata.parent_chain[1]` (script_id) | `parent_chain[1]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[2]` (storyboard_id) | `parent_chain[2]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[3]` (production_plan_id / rendered_shots_set_id) | `parent_chain[3]` | Passthrough (mode-dependent semantics per Style Replication §10). | Verbatim copy. |
| `metadata.parent_chain[4]` (replication_set_id) | `parent_chain[4]` | Passthrough. | Verbatim copy. |
| `metadata.parent_chain[5]` (preflight_report_id) | `parent_chain[5]` | Passthrough — QC Pre-flight's 6-tuple extension (operator-pending). | Verbatim copy when present; position accepted-optional until the QC Pre-flight 6-tuple LOCKs. |
| Generated by this agent | `parent_chain[6]` (asset_manifest_id) | NEW — **7-tuple extension.** | Agent generates a fresh `asset_manifest_id` (UUIDv7 per Cross-SPEC §3.9 ID canon) and appends at position [6]. **DOUBLY-DEFERRED: gated on the Cross-SPEC §3.9 n-tuple amendment ratification AND the QC Pre-flight 6-tuple LOCK (both operator-pending — see §14.7). Schema holds additively (`minItems: 5`, `prefixItems` 0–6, `maxItems: 7`, `items: false`) with a `TODO@cross-spec-3.9-ratification` flip note. Ingest is the second forcing function for the amendment.** |
| `metadata.brand_id` | `reel_ref.brand_id` | Passthrough. | v1.0 expected value = `"REINVENTED"`. |
| `reel_ref` triple derived | `reel_ref.{brief_id, preflight_report_id, asset_manifest_id}` | Derived reel reference triple. | The join keys for cross-record audit. `asset_manifest_id` is this agent's emitted identity. |

**Bundle normalization rows (rows 10–14 — the mode-convergence map):**

| Source (by mode) | `asset_manifest.json` destination | Transform | Mechanic |
|------------------|-----------------------------------|-----------|----------|
| Mode B/C: `replicated_shots[*].{shot_ref, asset_uri, declared_spec.duration_sec}` · Mode A: `footage_upload_manifest.clips[*].{shot_ref, asset_uri, declared_spec.duration_sec, take}` | `asset_bundle.raw_footage[]` | **NORMALIZE** — three source shapes → one row shape `{shot_ref, asset_uri, duration_sec, source}`. | `source` records the producing agent (`style-replication-agent` / `ai-video-gen-agent`) or `videographer_upload` (Mode A). Mode A take-selection: the highest-numbered take per `shot_ref` that satisfies the declared spec (take-substitution ladder, Rule 8). |
| Mode A: `footage_upload_manifest.audio[*].asset_uri` · Mode B/C: voice-track URIs carried on the asset set | `asset_bundle.audio[]` | NORMALIZE — flat URI list. | Sync adjudication evidence lives in `spec_check`, not here — the bundle is the editor's pull list, not the verdict. |
| `production_plan` brand-asset pulls (logo, lower-third templates) | `asset_bundle.assets_pulled[]` | Passthrough — filename list. | Brand assets named by the plan; Ingest confirms firewall-clean filenames (Check #4) but does not fetch. |
| `footage_upload_manifest.music_bed` (A) / production-plan music ref (B/C) | `asset_bundle.music_bed` | Passthrough — single URI. | URI-integrity checked (Check #3). |
| `metadata.production_mode` | `mode_convergence` | NEW — `{ingested_mode, normalized_to: "mode_agnostic_manifest"}`. | The convergence record. Every field downstream of this block is mode-identical (Check #9 enforces). |

**Per-check evidence rows (rows 15–20):**

| Source / generated | `asset_manifest.json` destination | Transform | Mechanic |
|--------------------|-----------------------------------|-----------|----------|
| Generated (Step 1) | `qc_precondition_check` | NEW — `{preflight_report_id, verdict_observed, lever3_signoff_present}`. | The precondition evidence. `verdict_observed == "pass"` OR `lever3_signoff_present == true` required for any ingest to proceed. |
| Generated (Step 3) | `asset_uri_integrity` | NEW — `{uris_checked, non_relative, dangling}`. | `non_relative == 0` and `dangling == 0` required for `pass`. `uris_checked` must equal the true bundle URI census. |
| Generated (Step 4) | `asset_firewall_pass_8` | NEW — `{status, filenames_scanned, metadata_fields_scanned, hits}`. | The 8th-pass result on the asset-layer surface. `hits` MUST be 0 for `pass`; any hit → `asset_firewall_breach`. |
| Generated (Steps 5+7+8) | `spec_check` | NEW — Blueprint §4.8 shape: `{aspect_ok, frame_rate_ok, resolution_ok, container_codec_ok, audio_present_ok, audio_sync_declared_ok, missing_shots[]}`. | All booleans `true` + `missing_shots == []` required for `pass`. Derived from DECLARED metadata only (`byte_probe_performed: false`). Duration-envelope result folds into the spec family (§6.3). |
| Generated (Step 6) | `coverage_check` | NEW — `{shots_required, shots_covered, coverage_complete}`. | `shots_required == storyboard_ref.total_shots`; `coverage_complete == (shots_covered == shots_required)`. Internal consistency enforced by Check #6 (no phantom coverage). |
| Generated (Step 11) | `qc_pre_flags[]` (Ingest's own) | NEW — ≥4 snake_case predicates (§3.4 floor / §3.7 shape). | Ingest contributes its own ≥4 ingest predicates downstream (e.g. `asset_firewall_clean_pass_8`, `full_storyboard_coverage`, `all_uris_platform_relative`, `declared_specs_match_plan`). |

**Manifest aggregate rows (rows 21–25):**

| Source / generated | `asset_manifest.json` destination | Transform | Mechanic |
|--------------------|-----------------------------------|-----------|----------|
| Generated (Step 10) | `output_type` | NEW — `enum: ["successAssetManifest", "errorEnvelope"]`. | The polymorphic discriminator. |
| Generated (Step 10) | `verdict` | NEW — `enum: ["pass", "fail", "reshoot"]`. | The headline judgment. No `hold` (deliberate — §6.4: Ingest's domain is deterministic; there is no asset-layer ambiguity for a human to adjudicate mid-verdict). |
| Generated (Step 10, non-pass) | `failure_code` + `failed_check_id` + `route_back_to` | NEW — one of 8 LOCKED codes (§6.3) + integer [1,11] + route per the §3.2 map. | Present only on `errorEnvelope`. Schema enforces the 8-code enum + `ingest_agent_failed` slot-11. `reshoot → "production-coord-agent"` AND Mode A only. |
| Generated (Step 10) | `handoff_targets[]` | NEW — `["edit-director-agent"]` on pass. | Non-empty only on `pass`. Edit Director is Agent #9 (not yet built) — v1.0 emission target is the holding store pending the Open-Question-4 decision (partial 2 / operator). |
| Generated (Step 10/11) | `metadata` | NEW — Cross-SPEC §3.9 canonical + 5 Ingest additions. | 7-tuple parent_chain (held additively) + `asset_manifest_class: "pre_edit"` + `manifest_evidence_hash` + `runtime_environment_class` + `byte_probe_performed: false` (see §16, partial 2). `human_review_required: true` per Rule 12. `cost_incurred_usd` ≈ 0.00. |

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

Four fields are reserved in the field map but not yet active in v1.0:

- **`spec_check.probed_spec`** (per-asset byte-probe result) — v1.0 adjudicates declared metadata only; the parallel probed-spec block activates when ffprobe/MediaInfo lands (v1.1, requires a runtime execution environment). `byte_probe_performed` flips to `true` the same day. Deferred.
- **`loudness_check` (LUFS verification)** — requires decode + the Sound agent's domain (−14 LUFS IG/TT, −16 LUFS YT per Blueprint #12). Deferred to v1.1+.
- **`conform_plan` (auto-transcode routing)** — v1.0 only *routes* off-spec assets (`route_back_to` + `recovery_path`); it does not plan or perform conforms. Deferred.
- **`take_dedup_report`** (perceptual near-duplicate triage of Mode A takes) — needs decode + perceptual hashing. v1.0 take-selection is declared-spec + take-number only. Deferred.

### 10.3 No-touch fields (read-only references)

Read by the agent but never written to its output (audit trail only):

- `preflight_report.brand_voice_qc.*` — Ingest reads the verdict, never the per-point adjudication. Brand voice is QC Pre-flight's jurisdiction; echoing it would imply re-adjudication authority Ingest does not have.
- `preflight_report.cost_ledger_check.*` — read-only context. Ingest carries NO cost fields beyond its own `cost_incurred_usd` (Rule 10 — no re-litigation).
- `rendered_shots[*].render_dispatch_log[*]` — AI Video Gen's per-shot render history; optional Mode B cross-reference context, never echoed.
- `accumulated_qc_pre_flags` (upstream union) — consumed as read-only context (QC Pre-flight already adjudicated the §3.4 floor); Ingest appends its own ≥4 predicates without modifying the upstream surface.

### 10.4 Schema authoring note (for the schemas day)

The schema author must encode the field map above as JSON Schema Draft 2020-12 constraints. Specifically:
- `parent_chain` MUST use `prefixItems: [..×7]`, `minItems: 5`, `maxItems: 7`, `items: false` — the **additive hold**. Exact 7-tuple cardinality (`minItems: 7`) is **DOUBLY-BLOCKED** until the Cross-SPEC §3.9 amendment ratifies AND the QC Pre-flight 6-tuple LOCKs; the schema carries a `TODO@cross-spec-3.9-ratification` flip note at the field.
- `output_type` MUST drive a `oneOf [successAssetManifest, errorEnvelope]` polymorphic split.
- `verdict` MUST use `enum: ["pass", "fail", "reshoot"]` — no `hold` (§6.4 divergence, deliberate).
- `failure_code` (errorEnvelope branch) MUST use `enum` of exactly the 8 LOCKED codes (§6.3) + `ingest_agent_failed`. Schema MUST NOT enumerate the folded code (`duration_envelope_breach`) — subsumed per §6.3 narrowing.
- `asset_uri` fields MUST use `pattern: "^ars://[a-zA-Z0-9_\\-./]+$"` (platform-relative, Hard Rule #8).
- `manifest_evidence_hash` MUST use `pattern: "^[a-f0-9]{64}$"` (lowercase hex, 64 chars).
- `byte_probe_performed` MUST use `const: false` in the v1.0 schema (flips to plain boolean in v1.1).
- `spec_check.missing_shots` MUST be present (possibly empty) on the success branch — its emptiness is the coverage invariant, so it cannot be optional.

### 10.5 Ingestion-by-mode reporting matrix

Ingest's verdict logic is **mode-agnostic** (§4) — but ingestion is mode-aware. The table maps which manifest fields/behaviors activate per mode:

| Field / behavior | Mode A | Mode B | Mode C | Notes |
|------------------|:------:|:------:|:------:|-------|
| Source shape consumed | `footage_upload_manifest` | `replicated_shots` (+ optional `rendered_shots` cross-ref) | `replicated_shots` (single-source) | Three shapes in, one manifest out |
| Take-substitution ladder | active | n/a | n/a | Mode A clips carry `take` numbers; B/C assets are singular per shot |
| `verdict: "reshoot"` reachable | **YES** | NO | NO | Live footage can be re-shot; AI output is re-genned (Rule 8) |
| `route_back_to: "production-coord-agent"` | reachable | NO | NO | Reshoot routing |
| `route_back_to: "style-replication-agent"` | NO | reachable | reachable | B/C re-gen routing |
| `route_back_to: "ai-video-gen-agent"` | NO | reachable | NO | Mode B render defects |
| `route_back_to: "re-upload"` | reachable | NO | NO | Mode A fixable defects (off-spec clip, missing audio file) |
| Coverage + firewall + URI + spec + audio checks | ALL | ALL | ALL | Universal — every mode, every tier |
| `asset_bundle` / `spec_check` output shape | identical | identical | identical | The mode-convergence guarantee (Check #9) |

The matrix is the basis for the SKILL bundle's ingestion-routing logic on the SKILL-build day.

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 51 · status updates + slip encoding)

**Calendar inherited from outline §0 build calendar, amended for the Day 50 slip.** Day 51 author task per outline: this was calendared as partial 2 day; the missed Day 50 run shifts partial 1 here and partial 2 to Day 52. Slip encoded below — surfaced, not papered over.

### 14.1 Calendar (Day 48 → v1.0 LOCK — Ingest trajectory, slip-amended)

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 48 | Sat Jun 6 · Wk7 | **Ingest Agent v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 49 | Sun Jun 7 · Wk7 | **REST DAY — no build.** (7th observance) | ✅ OBSERVED | — |
| Day 50 | Mon Jun 8 · Wk8 | *Calendared:* SPEC body partial 1 | ⚠️ **RUN DID NOT EXECUTE** — no log, no deliverable on disk. Cadence slid one day; nothing skipped. | — |
| Day 51 | Tue Jun 9 · Wk8 | **SPEC body partial 1: §6 (11-Check Self-QC, bipartite-covering 8 LOCKED errorEnvelope codes + slot-11) + §7 (System Prompt v1.0 frame + 12 hard rules + Blueprint §4.8 manifest shape inlined + universal-tier table + 11-step ingest loop + voice rule) + §10 (Field Map 25 rows: 9 lineage + 5 bundle normalization + 6 per-check evidence + 5 manifest aggregate) + §14 (Implementation Plan, slip-amended)** | ✅ DONE — this document, LOCKED-as-drafted | Donna overnight |
| Day 52 | Wed Jun 10 · Wk8 | **SPEC body partial 2: §8 (Performance Targets — 9 metric categories) + §9 (5 Test Fixtures TC-01..TC-05) + §11 (Cost Model — zero-engine snapshot + catch-cost-avoidance value model) + §12 (Verdict Math — deterministic ∧-of-gates) + §13 (10–14 Critical Decisions LOCKED) + §15 (Change Log) + §16 (Metadata Block — Cross-SPEC §3.9 + 5 additions)** | ⬜ TARGET | Donna overnight + Jamila §13 amendments |
| Day 53+ | Thu Jun 11+ | **SPEC v1.0 LOCK CANDIDATE → input/output schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK.** Hard-gated on the THREE predecessor LOCKs (AI Video Gen + Style Replication + QC Pre-flight) closing first + the Cross-SPEC §3.9 n-tuple amendment ratifying. | ⬜ QUEUED | Donna overnight + Jamila gates |

### 14.2 Dependencies that MUST exist before the SKILL-bundle build

| Dependency | Status | LOCK day |
|------------|--------|----------|
| Orchestration Blueprint (§3 mode-convergence + §4.8 handoff shape) LOCKED | ✅ DONE | Day 5 |
| Cross-SPEC Consistency Review LOCKED | ✅ DONE | Day 12 |
| AI Video Gen v1.0 LOCK CANDIDATE + schemas + SKILL + Day 27 runbook AUTHORED | ✅ DONE | Day 24–27 |
| **AI Video Gen v1.0 LOCK (operator-gated sign-off)** | ⚠️ **PENDING** | operator pickup — file-state confirms unflipped |
| Style Replication v1.0 LOCK CANDIDATE + schemas + SKILL + Day 36 runbook AUTHORED | ✅ DONE | Day 32–36 |
| **Style Replication v1.0 LOCK (operator-gated sign-off)** | ⚠️ **PENDING** | operator pickup — hard-gated on AI Video Gen LOCK first |
| **Day 36 Style Replication LLM Test Runbook EXECUTION (5/5 PASS gate)** | ⚠️ **PENDING** | operator paste-and-run — outcome unconfirmed |
| QC Pre-flight v1.0 LOCK CANDIDATE + schemas + SKILL + Day 47 runbook AUTHORED | ✅ DONE | Day 44–47 |
| **QC Pre-flight v1.0 LOCK (operator-gated sign-off) — Ingest's DIRECT 7-tuple dependency** | ⚠️ **PENDING** | operator pickup — Items 6/8/11 + Day 47 runbook execution |
| **Day 47 QC Pre-flight LLM Test Runbook EXECUTION (5/5 PASS gate)** | ⚠️ **PENDING** | operator paste-and-run — outcome unconfirmed |
| Ingest SPEC outline §0–§5 | ✅ DONE | Day 48 |
| Ingest SPEC body §6 + §7 + §10 + §14 LOCKED-as-drafted | ✅ DONE — this document | Day 51 (today) |
| Ingest SPEC body §8 + §9 + §11 + §12 + §13 + §15 + §16 LOCKED | ⬜ TARGET | Day 52 |
| **Cross-SPEC §3.9 n-tuple-as-lineage amendment RATIFICATION** | ⚠️ **PENDING** | operator pickup — Ingest's 7-tuple is the SECOND forcing function |
| **Agent #8 = Ingest slot confirmation** | ⚠️ **PENDING (non-blocking)** | operator confirms (or re-assigns) at the QC Pre-flight LOCK-ceremony close |

### 14.3 Cross-SPEC §3 adherence (preliminary audit — full audit at LOCK CANDIDATE)

| Cross-SPEC dimension | Day 51 partial 1 status |
|----------------------|-------------------------|
| §3.1 naming canon | ✅ `ingest-agent` verified; slot-11 code `ingest_agent_failed` matches canon |
| §3.2 hash invariant | ✅ `manifest_evidence_hash` SHA-256 over evidence + spec_check block (Check #11) |
| §3.3 errorEnvelope shape | ✅ Mirrors fleet shape + adds `verdict` + `route_back_to` per §6.3 |
| §3.4 qc_pre_flags minItems 4 + snake_case | ✅ Upstream surface consumed read-only (QC Pre-flight already adjudicated the floor); Ingest emits its own ≥4 predicates (Check #11) |
| §3.5 mode matrix | ✅ Mode-agnostic verdict + mode-aware ingestion (§10.5 matrix) + mode-convergence guarantee (Check #9) |
| §3.6 slot-11 reserved naming | ✅ `ingest_agent_failed` reserved at §6.3 |
| §3.7 qc_pre_flags format regex | ✅ Enforced via Check #11 with regex `^[a-z][a-z0-9_]{0,63}$` |
| §3.8 tier↔mode firewall (8th defense-in-depth pass) | ✅ Check #4 + §7 Hard Rule #6 + universal-tier table + Step 4 — the asset-layer surface |
| §3.9 metadata block + n-tuple parent_chain | ✅ §10.1 inherits canonical + extends to **7-tuple, held additively**. **DOUBLY-DEFERRED** — gated on the §3.9 amendment ratification AND the QC Pre-flight 6-tuple LOCK (§14.7) |
| §3.10 cost ceiling authority | ✅ §7 Hard Rule #10 explicitly DECLINES cost re-litigation (QC Pre-flight's authority) — no double-enforcement; Ingest is $0-cost |
| §3.11 LOCK respect (no modification of upstream LOCKED canon) | ✅ Day 51 partial 1 references all predecessor canon read-only; no modifications |

11 of 11 dimensions ✅ at partial 1 stage. Full LOCK audit at LOCK CANDIDATE.

### 14.4 Rest Day honored

Days 21, 28, 35, 42, 49 — no build sessions per the Daily OS pillar order (Rest → Body → Money → Authority → Relationships). **Day 49 (Sun Jun 7) was the sprint's 7th Rest Day observance** — correctly a no-build day (the planned scaffold pre-stage did not occur because no session ran, which is a stricter observance, not a violation). Next Rest Day: Day 56 (Sun Jun 14).

### 14.5 Day 51 sprint completion summary

| Section | Status | Notes |
|---------|--------|-------|
| §6 11-Check Self-QC List | ✅ DRAFTED | 11 checks fully drafted with failure-code mapping. Slot-11 `ingest_agent_failed` reserved per Cross-SPEC §3.6. Error-code namespace settled at **8 LOCKED + slot-11** (Day 51 narrowing: `duration_envelope_breach` → `asset_spec_violation` with `detail.subtype` — resolves outline Open Question 6 as recommended). Self-QC check count settled at **11** (within the outline's 10–12 target). No-soft-hold divergence from QC Pre-flight documented (§6.4 — Ingest's domain is deterministic). Bipartite coverage flagged for LOCK-candidate audit. |
| §7 System Prompt v1.0 | ✅ DRAFTED | Single fenced block: frame + **12 hard rules** + **Blueprint §4.8 manifest shape inlined verbatim** + universal-tier table + 11-step ingest loop + voice rule. Seven structural decisions rationalized in §7.2. Declared-spec-only/no-probe (Rule 2), no cost re-litigation (Rule 10), and recommend-don't-clear (Rule 12) are the defining rules. |
| §10 Field Map | ✅ DRAFTED | 25 rows: 9 lineage + 5 bundle normalization (the mode-convergence map) + 6 per-check evidence + 5 manifest aggregate. **7-tuple parent_chain drafted but DOUBLY-DEFERRED** (held additively `minItems: 5`). 4 v1.0 reserved fields enumerated. Ingestion-by-mode matrix added (§10.5). Schema authoring notes embedded incl. `byte_probe_performed const: false`. |
| §14 Implementation Plan | ✅ DRAFTED | Calendar slip-amended (Day 50 missed run surfaced honestly; partial 2 → Day 52). Dependency table extended with QC Pre-flight gates + the Agent-#8 slot confirmation. Cross-SPEC §3 preliminary audit completed (11/11 ✅). |

### 14.6 Day 52 partial 2 authoring runway

Day 52 must author:
- **§8 Performance Targets** — 9 metric categories per the outline: schema validity 100% / asset-firewall catch 100% (the 8th pass must be perfect by construction) / coverage-gap catch 100% (a missing shot must never pass) / **false-pass rate 0%** / false-fail rate ≤ 5% (over-blocking is the acceptable direction) / URI-integrity catch 100% / p50 latency 25s / p95 75s (reasoning-only, fast) / zero engine + zero probe cost.
- **§9 5 Test Fixtures** — TC-01 clean Mode B Pro PASS (full manifest) · TC-02 Mode C Enterprise PASS (single-source clean) · TC-03 `missing_shot_coverage` Mode A (uncovered shot, no covering take → `reshoot` + ProdCoord route) · TC-04 `asset_spec_violation` (aspect mismatch → `fail` + route) · TC-05 `asset_firewall_breach` (banned token injected in a **filename** — the 8th-pass new-surface catch). 5 of 8 codes exercised; remainder schema-only. Fixtures live at `skills/ingest-agent/tests/`.
- **§11 Cost Model** — zero-engine, zero-probe snapshot. Catch-cost-avoidance value model (prevented wasted edit cycles + prevented asset-layer brand leak on a published surface).
- **§12 Verdict Math** — deterministic ∧-of-gates: `PASS = (QC precondition met) ∧ (all URIs integral) ∧ (asset-firewall clean) ∧ (all declared specs match incl. duration) ∧ (full coverage) ∧ (audio adjudicated) ∧ (lineage intact)`. Any single ∧-term false → fail/reshoot per §3.2 + the Mode A take-substitution ladder. No thresholds to tune — pure boolean composition.
- **§13 Critical Decisions** — target 10–14 LOCKED. 10 LOCKED-as-drafted Day 48 outline. 3 RESOLVED Day 51 by this partial (code count → 8+slot-11 §6.3; self-QC count → 11 §6.1; duration fold → `asset_spec_violation` subtype). 2 remain PRELIMINARY for Day 52 operator amendment (Edit-Director handoff target — Notion holding store vs direct, Open Question 4; 7-tuple parent_chain — doubly-gated).
- **§15 Change Log** — v1.0 lifecycle entries (outline-day-48 → Rest Day-day-49 → **day-50 slip** → body-day-51 → body-day-52 → LOCK-candidate → schemas → SKILL → runbook → LOCKED).
- **§16 Metadata Block Schema** — Cross-SPEC §3.9 canonical fields + 5 Ingest additions (7-tuple parent_chain, `asset_manifest_class`, `manifest_evidence_hash`, `runtime_environment_class`, `byte_probe_performed`).

### 14.7 Operator action items carried over (UNCHANGED — surfaced again, NOT advanced)

Six operator-only items remain open. Donna did NOT advance any of them:

1. **AI Video Gen v1.0 LOCK ceremony** — Day 24 Items 8 + 11 + Day 27 runbook outcome. STILL PENDING (file-state confirmed). HARD GATE for the chain.
2. **Style Replication v1.0 LOCK ceremony** — Day 32 Items 6 + 8 + 11 + Day 36 runbook 5/5. STILL PENDING.
3. **QC Pre-flight v1.0 LOCK ceremony** — Day 44 Items 6/8/11 + Day 47 runbook 5/5. STILL PENDING. **Ingest's direct dependency** (the 6-tuple the 7-tuple extends).
4. **Execute the Day 47 QC Pre-flight LLM Test Runbook** — paste-and-run, 5 cases, ~20–35 min. 5/5 = QC Pre-flight LOCK gate open.
5. **Execute the Day 36 Style Replication LLM Test Runbook** — paste-and-run; 5/5 = Style Replication LOCK gate. Outcome unconfirmed.
6. **Cross-SPEC §3.9 n-tuple-as-lineage amendment ratification** — now doubly load-bearing: QC Pre-flight's 6-tuple AND Ingest's 7-tuple both hold additively on it. Donna recommends RATIFY-AS-DRAFTED.

Plus the non-blocking slot confirmation: **Agent #8 = Ingest** (or re-assign) at the QC Pre-flight LOCK-ceremony close.

---

## §8 — Performance Targets

`<<TBD-D52>>`

*Day 52 author task. Pattern source: QC Pre-flight §8 / AI Video Gen §8. Targets per §14.6: schema validity 100% / asset-firewall catch 100% / coverage-gap catch 100% / false-pass 0% / false-fail ≤ 5% / URI-integrity catch 100% / p50 25s / p95 75s / zero engine + zero probe cost.*

---

## §9 — 5 Test Fixtures

`<<TBD-D52>>`

*Day 52 author task. Pattern source: Style Replication §9. Fixtures: TC-01 Mode B Pro clean PASS · TC-02 Mode C Enterprise clean PASS · TC-03 `missing_shot_coverage` Mode A → `reshoot` · TC-04 `asset_spec_violation` → `fail` + route · TC-05 `asset_firewall_breach` (banned token in a filename — the 8th-pass new-surface catch). 5 of 8 LOCKED codes exercised; remainder schema-only. Each fixture = (input.json, expected_output.json, expected_verdict, expected_code_or_null, scenario_description).*

---

## §11 — Cost Model

`<<TBD-D52>>`

*Day 52 author task. Zero-engine, zero-probe snapshot: $0.00 per reel (pure reasoning + manifest construction). Value model = catch-cost-avoidance: a phantom/off-spec/missing asset reaching Edit Director burns a full edit cycle; an asset-layer firewall leak reaching a published surface is a brand-safety incident. The economic justification is downstream-cost prevention, not direct margin.*

---

## §12 — Verdict Math

`<<TBD-D52>>`

*Day 52 author task. Deterministic ∧-of-gates: `PASS = (QC precondition met) ∧ (all URIs integral) ∧ (asset-firewall clean) ∧ (all declared specs match incl. duration) ∧ (full storyboard coverage) ∧ (audio adjudicated) ∧ (lineage intact)`. Any single ∧-term false → fail/reshoot per §3.2 + the Mode A take-substitution ladder. No thresholds to tune — pure boolean composition over declared evidence.*

---

## §13 — Critical Decisions LOCKED (target 10–14)

`<<TBD-D52>>`

*Day 52 author task. 10 LOCKED-as-drafted Day 48 outline. 3 RESOLVED Day 51 by this partial 1 (errorEnvelope code count → 8 LOCKED + slot-11 §6.3; self-QC check count → 11 LOCKED §6.1; duration_envelope fold → `asset_spec_violation` subtype). 2 PRELIMINARY for Day 52 operator amendment (Edit-Director handoff target; 7-tuple parent_chain — doubly-gated on §3.9 ratification + QC Pre-flight 6-tuple LOCK).*

---

## §15 — Change Log + Version History

`<<TBD-D52>>`

*Day 52 author task. Initial entries:*
- *v1.0-draft-day-48 — outline §0–§5 SHIPPED (`ARS-2026-06-06-Day-48-Ingest-Agent-SPEC-Outline.md`)*
- *day-49 — Rest Day (7th observance, no build)*
- *day-50 — calendared partial 1; overnight run did not execute (cadence slid one day — surfaced in §14.1)*
- *v1.0-draft-day-51 — this document — body §6/§7/§10/§14 LOCKED-as-drafted; §8/§9/§11/§12/§13/§15/§16 RESERVED*
- *v1.0-draft-day-52 — §8/§9/§11/§12/§13/§15/§16 target*
- *v1.0-LOCK-CANDIDATE → v1.0-schemas → v1.0-SKILL → v1.0-runbook → v1.0-LOCKED (hard-gated on the three predecessor LOCKs + §3.9 ratification)*

---

## §16 — Metadata Block Schema

`<<TBD-D52>>`

*Day 52 author task. Pattern source: QC Pre-flight §16 plan (Cross-SPEC §3.9 canonical fields). Ingest additions (5 fields):*
- *`parent_chain` — **7-tuple** (QC Pre-flight 6-tuple + `asset_manifest_id`); DOUBLY-gated, held additively*
- *`asset_manifest_class` — enum (`pre_edit` v1.0 · `re_ingest` reserved v1.1+)*
- *`manifest_evidence_hash` — SHA-256 over the per-asset evidence + spec_check block*
- *`runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16*
- *`byte_probe_performed` — `const false` v1.0 (declared-spec honesty; flips in v1.1)*

---

## Mirror status

- Source: `ars/ARS-2026-06-09-Day-51-Ingest-Agent-SPEC-Body-Partial-1.md` (this document) + `ars/build-log-2026-06-09.md`
- Mirror destination: `/outputs/ars/` (both files)
- Mirror verification: in this session's mirror step.

---

## Process integrity (Day 51)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked. No byte-level media decode run. (Ingest by design calls no engine and runs no probe — Hard Rule #2.)
- ✅ **No external comms transacted.** No emails, DMs, social posts, client/investor outreach. The status SMS to Jamila ([status number redacted]) announces build status only.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, zero $ spent.
- ✅ **No operator-impersonation.** All THREE predecessor LOCK ceremonies confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Day 36 + Day 47 runbook executions NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed — the 7-tuple parent_chain is explicitly DOUBLY-DEFERRED and held additively (§10.4 + §14.7). No Notion row marked LOCKED, no dashboard chip flipped.
- ✅ **No fake-advance.** This partial is forward-design over LOCK-stable text artifacts, explicitly labeled LOCKED-as-drafted (not LOCKED). Ingest v1.0 LOCK hard-gates on the three predecessor LOCKs + the §3.9 ratification. The Day 50 missed run is surfaced in §14.1, not silently absorbed.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + the Day 48 outline — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. The HC/NPOX tokens in §6.5 + §7 Rule 6 are the firewall's BLOCK-list, not a cross-entity reference. REINVENTED remains brand-as-pilot-customer per Cross-SPEC canon.
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at partial 1 stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** QC Pre-flight Day 41 partial 1 structure inherited verbatim. Orchestration Blueprint §3/§4.8 + Cross-SPEC §3 canon used as the grounding spine. The two deliberate divergences (no soft-hold verdict §6.4; bundle-normalization field-map tier §10.1) are documented with rationale, not silent.
- ✅ **Rest Day honored.** Day 49 (Sun Jun 7) observed — 7th observance. Next: Day 56 (Sun Jun 14).

---

*Day 51 ships clean, one day behind the outline calendar (Day 50 run did not execute — surfaced, cadence slid intact). Day 52 build session is primed — §8 + §9 + §11 + §12 + §13 + §15 + §16 all have LOCK targets defined, with 10 of ~14 critical decisions LOCKED-as-drafted Day 48 + 3 resolved today (8 codes + slot-11; 11 self-QC checks; duration fold). Ingest is Agent #8 of 17 — the 8th defense-in-depth firewall (asset layer, a NEW surface), the mode-convergence seam, and the gateway the entire in-post fleet builds against. Operator pickup (6 items + 1 slot confirmation, all surfaced NOT advanced): the three predecessor LOCK ceremonies, the two runbook executions (Day 36 + Day 47), the Cross-SPEC §3.9 ratification (now doubly load-bearing), and the Agent #8 = Ingest confirmation. Day 52 = partial 2.*
