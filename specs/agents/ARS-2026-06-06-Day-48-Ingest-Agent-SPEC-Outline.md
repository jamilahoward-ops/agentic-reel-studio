# ARS — Ingest Agent v1.0 SPEC OUTLINE (§0–§5)

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Authored:** Day 48 · Sat Jun 6, 2026 (Pacific) · overnight build session (Donna)
**Deliverable class:** Forward SPEC outline §0–§5 (the head-start design for Agent #8 of 17)
**Status:** OUTLINE ONLY — no LOCK, no schema, no SKILL bundle. Body partials author Days 49 + 51 per the calendar in §0.
**Pattern source:** QC Pre-flight Day 40 outline (`ARS-2026-05-29-Day-40-QC-Preflight-Agent-SPEC-Outline.md`) — structure inherited verbatim. Orchestration Blueprint §1.4 / §4.8 / §7 (Agent 09 Ingest definition) + Cross-SPEC §3 canon used as the grounding spine.

> **Agent-selection note (Donna, surfaced not hidden):** No canon file pre-names the specific "Agent #8 of 17." Per the scheduled-task instruction to make a reasonable choice and note it, Donna selected the **Ingest Agent** (runtime pipeline position **09**) as Agent #8. Rationale: (1) **strict dependency order** — Ingest is the immediate runtime stage downstream of the QC Pre-flight gate (it consumes the QC-passed production output at the production→post boundary); (2) **same agent family** — Ingest is a validation/manifest/gate agent, so the just-completed QC Pre-flight patterns (errorEnvelope shape, defense-in-depth firewall pass, parent_chain lineage, recommend-don't-approve discipline, $0-engine reasoning posture) extend with minimal new surface; (3) **mode-convergence leverage** — per Blueprint §3, "from Ingest onward, post-production is mode-agnostic," so Ingest is the canonical point where Modes A/B/C physically reunify into one asset bundle — a high-value design surface; (4) **fleet-unblock** — Ingest is the hard blocker for the entire in-post fleet (Edit Director → Editor → Sound → Motion); nothing in post can run without the Asset Manifest it produces. Operator may re-assign the #8 slot at the LOCK-ceremony close; this outline is the forward-design head-start, authored on the same forward-looking basis the QC Pre-flight and Style Replication outlines were.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 7 — Post-production gateway layer (production → post handoff, asset side) |
| Agent index | **#8 of 17** (build sequence — Donna selection per the note above; continues the QC Pre-flight Day 40 "agent #7 of 17" framing) |
| Runtime pipeline position | **09 — Ingest** (the post-production gateway); receives footage (Mode A) or raw AI outputs (Mode B/C), validates specs, logs assets, hands metadata to Edit Director |
| Pipeline tier | POST-PRODUCTION GATEWAY (first post-production agent built in the sprint) |
| Mode coverage | **Mode-convergent** — ingests Mode A (graded/raw human footage upload), Mode B (rendered + replicated asset set), Mode C (replicated hot-path asset set); from this agent onward the pipeline is mode-agnostic (Blueprint §3) |
| Predecessor SPEC (gate) | `ARS-2026-06-02-Day-44-QC-Preflight-Agent-v1-LOCK-CANDIDATE.md` (Day 44 LOCK candidate — operator-gated). Ingest runs only on a QC-passed (or Lever-3 human-approved) reel. |
| Predecessor schemas | `skills/style-replication-agent/schemas/output.schema.json` (Day 33) + `skills/ai-video-gen-agent/schemas/output.schema.json` (Day 25) + the QC Pre-flight `output.schema.json` (Day 45) — all consumed as INPUT branches (asset set + verdict precondition) |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape (§3.8), qc_pre_flags minItems-4 floor (§3.4/§3.7), metadata block + n-tuple parent_chain (§3.9) all inherited |
| Defense-in-depth layer | **8th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → QC Pre-flight → **Ingest**) — the asset-layer firewall (filenames, embedded media metadata, sidecar/caption files) |
| Lever inheritance | Reads `lever_state` from upstream `metadata`; emits `human_review_required` per Lever-3 default. As a technical gateway, its verdict is a recommendation — it never marks a reel "cleared for edit"; the operator (or a future Orchestrator dispatch) ratifies. |
| Pricing tier authority | **ALL tiers** — Pilot · Starter · Pro · Enterprise. Every reel, every mode, traverses Ingest on the way into post (Mode A Pilot reels skip the Mode B/C production paths but still ingest their footage). Universal gateway. |
| Cost authority class | **Near-zero (ties QC Pre-flight for lowest in fleet)** — pure reasoning + manifest construction over DECLARED asset specs. **No generative engine calls, no byte-level media probe in v1.0** (ffprobe/MediaInfo deferred to v1.1 — requires a runtime execution environment). Effective per-reel cost ≈ $0.00. |

**Build calendar (Week 7 — Ingest trajectory, mirrors the proven 8-day agent-build cadence):**
- **Day 48** (today, Sat Jun 6 · Wk7) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 49 (Sun Jun 7 · Wk7) — **REST DAY** (no build; pre-stage SPEC body partial-1 scaffold only, per the Day 21/28/35/42 Rest Day-compounding pattern)
- Day 50 (Mon Jun 8 · Wk7) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 51 (Tue Jun 9 · Wk7) — SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16
- Day 52+ (TBD) — LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK (pattern: QC Pre-flight Day 44–47 / Style Replication Day 32–37)

> **Rest Day honesty:** This Day-48 build runs Saturday (Pacific) — building is allowed. Day 49 (Sun Jun 7 Pacific) is the sprint's 7th Rest Day; per the canonical compounding pattern it pre-stages the partial-1 scaffold without advancing build canon. The UTC clock has rolled to Sunday Jun 7 at author time, but the sprint labels by Jamila's Pacific date (Sat Jun 6) — the same convention noted in the Day 47 log's housekeeping.

> **Sequencing honesty:** The 42-day sprint's headline deliverable — the Mode B Pro single-reel **commercial demo** (Day 42 target) — ships on the six launch-critical production agents threaded through the QC Pre-flight gate. Ingest is the first *post-production* agent; its v1.0 build proceeds inside the **post-launch hardening window** and does **not** gate the launch demo. This outline is the forward-design head-start so the post fleet is buildable in dependency order once the production-tier LOCKs close.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Ingest Agent** is the **post-production gateway** of ARS — the moment a reel stops being a *content artifact that passed brand QC* and becomes a *technical asset bundle ready to edit*. It is the eighth automated defense-in-depth firewall pass, and the first agent every tier and every mode funnels through on the way **into** post-production.

Where the upstream gates adjudicate *meaning*, Ingest adjudicates *matter*:
- Brief / Script / Storyboard = intent + content gates
- Production Coord = logistics gate (mode, vendor, budget envelope)
- AI Video Gen / Style Replication = render + brand-finish gates ("Are these the right pixels?")
- QC Pre-flight = ship-safety / brand-correctness gate ("Is the *reel* brand-safe, format-correct, on-budget?")

The Ingest Agent picks up at the convergence point, one layer down:
- **Ingest Agent = asset-readiness gate ("Are the actual media *files* present, valid, spec-conformant, and in-sync? Does every storyboard shot have a usable asset? Is the asset layer firewall-clean (8th pass on filenames + embedded metadata)? Build the canonical Asset Manifest the editor consumes. PASS, FAIL_FIXABLE, or FAIL_RESHOOT?")**

**Single-responsibility line (LOCKED):**
> *"Post-production gateway. Receives the QC-passed production output (Mode A human footage upload, or Mode B/C rendered/replicated asset set), validates each asset against the production-plan technical spec (aspect, frame rate, resolution, codec/container, duration, audio presence/sync) at the DECLARED-metadata level, confirms full storyboard-shot coverage, runs the 8th defense-in-depth firewall pass over filenames and embedded asset metadata, and emits a single canonical Asset Manifest with a Pass / Fail-fixable / Reshoot verdict and per-asset evidence. Calls no generative engine and performs no byte-level media decode in v1.0."*

**Why this agent's reason-to-exist is the mode-convergence contract (Blueprint §3):** Every prior agent forks on mode — Mode A goes to a human shoot, Mode B to AI Video Gen, Mode C to Style Replication's hot path. The Orchestration Blueprint states plainly: *"From Ingest onward, post-production is mode-agnostic."* Ingest is the agent that **makes that true** — it is the funnel where three physically different asset origins (a videographer's `.mov` upload, a HeyGen/Runway render folder, a Style-Replication grade-pass output set) are normalized into **one** Asset Manifest with **one** shape, so that Edit Director (and every agent after it) never has to know how the footage was born. Without Ingest, the in-post fleet would each need three mode branches; with it, they need none. **This is Donna's mode-convergence justification for building Ingest as Agent #8 — it is the structural seam that collapses the pipeline from three production paths back to one post path.**

**Pipeline position (per Orchestration Blueprint §2 swim lane):**
```
... → QC PRE-FLIGHT (ship-safety gate) →
   [PASS / Lever-3 human-approved]
        │
        ▼
   ┌── (Mode A) human videographer upload ───┐
   ├── (Mode B) AI Video Gen + Style Repl set ├─► INGEST (asset-readiness gate)
   └── (Mode C) Style Replication hot-path set ┘        │
                                                        ▼  [Asset Manifest]
                                       10 Edit Director → 11 Editor → 12 Sound → 13 Motion → 14 QC (full)
                                                        │
                            [FAIL_FIXABLE] → re-upload / re-gen the specific defective asset
                            [FAIL_RESHOOT] → route back to Production Coord (Mode A source unusable)
```

**Why an asset-readiness gate distinct from QC Pre-flight (the boundary question):** QC Pre-flight already validates format specs, firewall, and brand voice at the production→post boundary — so what does Ingest add? A clean separation of concerns:
1. **QC Pre-flight adjudicates the *semantic* reel** — is the content brand-correct, is the *declared* format spec right, is the cumulative cost in budget. It answers "should this reel exist?"
2. **Ingest adjudicates the *physical* assets** — do the actual files exist at their `asset_uri`s, is each one's declared technical metadata internally consistent and matched to the plan, does every storyboard shot have coverage, are the filenames/embedded metadata firewall-clean. It answers "can the editor open and cut these files?"
3. **The two gates catch different failure classes.** QC Pre-flight cannot catch a missing shot file, a dangling `asset_uri`, an audio track that never arrived, or a banned token buried in a filename — those are *asset-layer* defects invisible to a content gate. Ingest cannot re-adjudicate brand voice — it trusts the QC verdict it requires as a precondition. Defense-in-depth means each pass owns the failures the prior pass structurally cannot see.

The full byte-level media validation (decode-and-probe: real codec inspection, true frame-rate read, LUFS measurement, color-space verify) is a deliberate **v1.1+** deliverable — it requires a runtime execution environment with ffprobe/MediaInfo, which the no-engine/$0 sprint posture does not provide. v1.0 Ingest adjudicates the **declared** asset metadata (the gen output's self-reported specs; the Mode A upload manifest's declared specs) — the same posture by which QC Pre-flight adjudicates declared `qc_pre_flags` rather than re-rendering.

**Hand-off contract enforced:**
- **PRECONDITION:** Ingest reads the QC Pre-flight `preflight_report.json`. If `verdict != "pass"` AND there is no Lever-3 human sign-off on the report → halt with `upstream_qc_not_passed`. Ingest never ingests an unvetted reel.
- **INPUT contract (polymorphic by source):**
  - **Mode A:** a `footage_upload_manifest` (videographer Drive upload — declared clips, takes, audio, declared specs).
  - **Mode B/C:** the production-tier asset set — `replicated_shots[]` (Style Replication, primary) and/or `rendered_shots[]` (AI Video Gen, Mode B) `asset_uri` list with declared per-asset specs.
  - Plus the **storyboard shot list** (denormalized) as the coverage reference, and the **production_plan** for the platform/format target.
  - Plus the **denormalized upstream chain** in `metadata.parent_chain` (6-tuple inbound from QC Pre-flight, operator-pending) + accumulated `qc_pre_flags[]`.
- **OUTPUT contract:** Emits `asset_manifest.json` per §3 (polymorphic: `successAssetManifest | errorEnvelope`). Edit Director reads the manifest's `asset_bundle` + `spec_check` (Blueprint §4.8 shape) without re-deriving asset validity.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| Asset presence + `asset_uri` integrity check (platform-relative `ars://`, Hard Rule #8; non-dangling) | Byte-level media decode/probe (ffprobe/MediaInfo: true codec, real fps, container deep-read) — needs runtime engine |
| Declared-spec validation vs `production_plan` (aspect / fps / resolution / codec / container) | LUFS / loudness measurement — requires decode + the Sound agent's domain (not built) |
| Storyboard-shot coverage check (every shot has ≥1 usable declared asset; `missing_shots[]`) | Per-frame visual integrity (corrupt-frame / dropped-frame detection) — needs decode |
| Declared audio presence + sync-flag adjudication | Auto-conform / auto-transcode of off-spec assets (v1.0 only *routes*; does not transform) |
| 8th defense-in-depth firewall pass over filenames + embedded metadata + sidecar/caption files | Perceptual de-dup of near-identical takes (Mode A coverage triage) |
| Canonical Asset Manifest construction (Blueprint §4.8 `asset_bundle` + `spec_check`) | Multi-reel batch ingest (v1.0 = one reel per invocation) |
| Mode-convergence normalization (A/B/C → one manifest shape) | Real-time upload-watcher trigger (v1.0 = on-invocation; Drive-watcher is an Orchestrator feature) |
| 7-tuple parent_chain extension (inherits QC Pre-flight 6-tuple + appends `asset_manifest_id`) | Auto-reshoot-cost estimation + ProdCoord auto-rebook |
| Pass / Fail-fixable / Reshoot verdict with per-asset evidence | Color-space / HDR-tag verification — needs decode |

**Pricing tier table (Ingest is universal — restated for defense-in-depth pass 8):**

| Tier | Reaches Ingest? | Ingest cost ceiling | Verdict authority |
|------|-----------------|---------------------|-------------------|
| Pilot — Founding 5 | **YES** (Mode A footage ingests here) | ~$0.00 (reasoning only) | Pass / Fail-fixable / Reshoot |
| Starter — Operator | **YES** | ~$0.00 | Pass / Fail-fixable / Reshoot |
| Pro — Studio | **YES** | ~$0.00 | Pass / Fail-fixable / Reshoot |
| Enterprise — Agency | **YES** | ~$0.00 | Pass / Fail-fixable / Reshoot |

Ingest adds **zero** generative cost to every tier envelope. Its economic value is **catch-cost avoidance** — preventing a missing-shot, dangling-asset, or off-spec file from reaching Edit Director and burning a wasted edit cycle (or, worse, surfacing as a defect after Motion).

---

## §2. Inputs

Ingest has **one canonical responsibility** (normalize the production output into an Asset Manifest) reached via a polymorphic **source** branch. Like QC Pre-flight, Ingest is mode-convergent — `production_mode` is read for branch selection and reporting, but the manifest it emits has one shape regardless of mode. Schema discriminator for the *source shape* is `metadata.production_mode` (A vs B/C) plus the upstream `output_type` of the consumed asset set.

### §2.1 Precondition input — QC Pre-flight verdict (gate)

**Always read first.** The QC Pre-flight `preflight_report.json`:
```json
{
  "output_type": "successPreflightReport",
  "verdict": "pass",
  "reel_ref": { "preflight_report_id": "preflight-REINVENTED-2026-06-06-001" },
  "human_review_required": true,
  "metadata": { /* 6-tuple parent_chain inbound */ }
}
```
**Hard validation:** `verdict == "pass"` (or a Lever-3 human sign-off is attached to a non-pass report). Otherwise → halt with `upstream_qc_not_passed`. Ingest does not ingest a reel that failed brand QC.

### §2.2 Primary input — Mode B/C production-tier asset set (preferred path)

**When invoked:** A QC-passed Mode B or Mode C reel whose pixels were produced by AI Video Gen and/or Style Replication.

**Required input fields (preliminary — full schema on the Day 50/51 partials):**
```json
{
  "replicated_shots": [
    {
      "shot_ref": 1,
      "asset_uri": "ars://reels/REINVENTED-2026-W23-001/raw/shot_1.mp4",
      "declared_spec": { "aspect_ratio": "9:16", "frame_rate": 30, "resolution": "1080x1920", "container": "mp4", "codec": "h264", "duration_sec": 3 },
      "has_audio": true,
      "qc_pre_flags": ["anchor_identity_verified", "drift_within_tolerance", "brand_finish_applied", "cost_within_ceiling"]
    }
  ],
  "rendered_shots": [ /* AI Video Gen successRenderedShots — Mode B forensic cross-reference, optional */ ],
  "production_plan": { /* denormalized ProdCoord output: platform_variants[], tier, format spec target */ },
  "storyboard_ref": { "shot_list": [ { "shot": 1, "duration_sec": 3 } /* ... */ ], "total_shots": 7 },
  "metadata": { /* Cross-SPEC §3.9 — production_mode, agent_id chain, parent_chain (6-tuple inbound), session_id, lever_state, accumulated qc_pre_flags surface */ }
}
```

**Hard validations on primary input (defense-in-depth pass 8):**
1. Upstream asset-set `output_type` is the success branch (`successReplicatedShots` / `successRenderedShots`), NOT `errorEnvelope`. (errorEnvelope → `upstream_not_success`.)
2. Every `asset_uri` matches the platform-relative `ars://...` pattern (Hard Rule #8 — **no absolute URLs**); none dangling/empty. Violation → `asset_uri_integrity_failure`.
3. Every `declared_spec` matches the corresponding `production_plan.platform_variants[]` target (aspect / fps / resolution / container / codec). Mismatch → `asset_spec_violation`.
4. Every `storyboard_ref.shot_list[]` entry maps to ≥1 asset with a matching `shot_ref` (coverage). Gap → `missing_shot_coverage`.
5. `metadata.parent_chain` is a well-formed 6-tuple inbound (lineage integrity — see §3.3). Malformed → `manifest_lineage_failure`.
6. Filenames + embedded metadata + any sidecar caption files are firewall-clean (8th pass — see §5 Step 4).

### §2.3 Secondary input — Mode A human-footage upload manifest

**When invoked:** A QC-passed Mode A reel where a human videographer uploaded raw footage to the Drive shoot folder.

**Required input fields:**
```json
{
  "footage_upload_manifest": {
    "shoot_packet_id": "shootpacket-REINVENTED-2026-W23-001",
    "clips": [
      { "shot_ref": 1, "asset_uri": "ars://reels/REINVENTED-2026-W23-001/raw/shot_1_take_3.mov",
        "declared_spec": { "aspect_ratio": "9:16", "frame_rate": 30, "resolution": "2160x3840", "container": "mov", "codec": "prores422hq", "duration_sec": 18 },
        "take": 3, "has_audio": true }
    ],
    "audio": [ { "asset_uri": "ars://reels/.../raw/lav_take_3.wav", "synced_to_shot_ref": 1, "sync_declared_ok": true } ],
    "music_bed": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav"
  }
}
```

**Hard validations (Mode A only):**
1. Every `storyboard_ref` shot has ≥1 clip with a matching `shot_ref` (coverage). Gap → `missing_shot_coverage` (Mode A gap is the **reshoot-eligible** path — see §3.2).
2. Declared clip spec meets the ProdCoord shoot-packet `format_spec` (e.g. ProRes 422 HQ, 9:16, 4K). Off-spec → `asset_spec_violation`.
3. Every shot needing sync audio has an `audio[]` entry with `sync_declared_ok: true`. Missing/false → `audio_sync_failure`.
4. Filenames + sidecar firewall-clean (8th pass).

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block: `tier`, `lever_state`, `production_mode`, `brand_id`, `session_id`. Ingest re-validates the tier↔mode authorization one final time on the asset side (8th pass) and sets the verdict's `human_review_required` per Lever-3 default. Ingest does **not** re-run the cumulative cost ledger — that is QC Pre-flight's authority; Ingest trusts the passed verdict.

---

## §3. Outputs (skeleton)

Ingest emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 / QC Pre-flight Day 40 output pattern (`oneOf [success branch, errorEnvelope]`).

### §3.1 successAssetManifest branch (verdict = PASS)

```json
{
  "output_type": "successAssetManifest",
  "verdict": "pass",
  "reel_ref": {
    "brief_id": "brief-REINVENTED-2026-06-06-001",
    "preflight_report_id": "preflight-REINVENTED-2026-06-06-001",
    "asset_manifest_id": "assetmanifest-REINVENTED-2026-06-06-001"
  },
  "asset_bundle": {
    "raw_footage": [
      { "shot_ref": 1, "asset_uri": "ars://reels/.../raw/shot_1.mp4", "duration_sec": 3, "source": "style-replication-agent" }
    ],
    "audio": ["ars://reels/.../raw/voice_track.wav"],
    "assets_pulled": ["logo_ivory_gold.png", "lt_authority_v3.mogrt"],
    "music_bed": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav"
  },
  "spec_check": {
    "aspect_ok": true,
    "frame_rate_ok": true,
    "resolution_ok": true,
    "container_codec_ok": true,
    "audio_present_ok": true,
    "audio_sync_declared_ok": true,
    "missing_shots": []
  },
  "coverage_check": { "shots_required": 7, "shots_covered": 7, "coverage_complete": true },
  "asset_firewall_pass_8": { "status": "pass", "filenames_scanned": 12, "metadata_fields_scanned": 96, "hits": 0 },
  "asset_uri_integrity": { "uris_checked": 12, "non_relative": 0, "dangling": 0 },
  "mode_convergence": { "ingested_mode": "C", "normalized_to": "mode_agnostic_manifest" },
  "handoff_targets": ["edit-director-agent"],
  "metadata": { /* Cross-SPEC §3.9 with Ingest additions per §3.3 — 7-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (verdict = FAIL or RESHOOT)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "missing_shot_coverage",
  "failed_check_id": 3,
  "attempts": 1,
  "route_back_to": "style-replication-agent",
  "reel_ref": { "asset_manifest_id": "assetmanifest-REINVENTED-2026-06-06-001" },
  "cost_incurred_usd": 0.00,
  "detail": {
    "violation": "storyboard shot_ref 5 has no asset in replicated_shots[]",
    "affected_shots": [5],
    "recovery_path": "re-run Style Replication grade pass for shot 5 OR drop shot 5 from the storyboard and re-cut the beat map"
  },
  "metadata": { /* Cross-SPEC §3.9 — 7-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `pass` | Asset bundle valid + complete; cleared into post | `null` (forward to Edit Director) | All asset checks green |
| `fail` | Fixable without re-shooting | the responsible upstream agent (`style-replication-agent`, `ai-video-gen-agent`) or `re-upload` | A specific asset is off-spec / missing / dangling and can be re-genned or re-uploaded |
| `reshoot` | Mode A source footage unrecoverable / uncovered | `production-coord-agent` | A Mode A storyboard shot has no usable clip and cannot be re-derived from existing takes |

### §3.3 Metadata block additions (Ingest-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **7-tuple** (inherits QC Pre-flight's 6-tuple lineage + appends own `asset_manifest_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (DRAFTED Day 31 §16.3; **ratification still operator-pending**). **Doubly-deferred:** the 7-tuple depends on BOTH the §3.9 amendment ratification AND the QC Pre-flight 6-tuple LOCK. Encoded additively (`minItems: 5`, `prefixItems` positions 0–6, `maxItems: 7`, `items: false`) so it accepts the 5-tuple, 6-tuple, and 7-tuple while rejecting a 4-tuple. A `TODO@cross-spec-3.9-ratification` flips `minItems` to 7 only after both gates close. — see §5 + Open Questions.
- `asset_manifest_class` — enum (`pre_edit` for v1.0 · `re_ingest` reserved for v1.1 conform/transcode round-trips).
- `manifest_evidence_hash` — SHA-256 over the per-asset evidence + spec_check block (forensic, tamper-evident manifest).
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.
- `byte_probe_performed` — `const false` in v1.0 (declared-spec adjudication only; flips to `true` in v1.1 when ffprobe/MediaInfo runs). Honest provenance of how the spec_check was derived.

### §3.4 errorEnvelope code namespace (target 7–9 LOCKED on Day 50/51 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `upstream_qc_not_passed` | QC Pre-flight `verdict != pass` with no Lever-3 sign-off | 1 | Halt — Ingest never ingests an unvetted reel. |
| `upstream_not_success` | the consumed asset-set branch is `errorEnvelope` | 2 | Halt — cannot ingest a failed production output. |
| `asset_uri_integrity_failure` | an `asset_uri` is non-relative (Hard Rule #8) OR empty/dangling | 3 | Hard FAIL — the editor cannot open a file that isn't there. |
| `asset_spec_violation` | declared aspect/fps/resolution/container/codec ≠ production_plan target | 4 | Verdict = fail; routes to the responsible production agent (or re-upload for Mode A). |
| `missing_shot_coverage` | a storyboard shot has no usable asset | 5 | fail (Mode B/C → re-gen) OR reshoot (Mode A → ProdCoord). |
| `audio_sync_failure` | required sync audio missing OR `sync_declared_ok: false` | 6 | Verdict = fail; `detail` names the affected shot(s). |
| `asset_firewall_breach` | banned-entity token in a filename / embedded metadata / sidecar caption (8th pass) | 7 | Hard FAIL — brand-safety at the asset layer; forensic-log which asset leaked. |
| `manifest_lineage_failure` | malformed parent_chain / broken n-tuple lineage | 8 | Forensic — audit-trail break. |
| `duration_envelope_breach` | summed/declared asset duration outside the brief's length band | (alias 4) | Same family as spec violation; Day 50 LOCK decision: distinct code OR fold into `asset_spec_violation`. |
| `ingest_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 50/51 LOCK:** 7–9 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping.

---

## §4. Tier Constraints & Mode Coverage

**Per-tier gate access (Ingest is universal — restated for defense-in-depth pass 8):**

| Tier | Modes accessible | Reaches Ingest? | Verdict | Cost |
|------|------------------|-----------------|---------|------|
| Pilot | A | **YES** | Pass / Fail-fixable / Reshoot | ~$0.00 |
| Starter | A | **YES** | Pass / Fail-fixable / Reshoot | ~$0.00 |
| Pro | A, B | **YES** | Pass / Fail-fixable / Reshoot | ~$0.00 |
| Enterprise | A, B, C | **YES** | Pass / Fail-fixable / Reshoot | ~$0.00 |

**Why universal access (vs Style Replication's Pro/Enterprise gating):** Style Replication's Mode B/C paths are tier-gated because they are *production capabilities* sold by tier. Ingest is a *technical gateway* — every reel, regardless of tier or how its footage was born, must become a valid asset bundle before an editor can touch it. A Pilot Mode A reel with a missing shot file is the same edit-blocking defect as a Enterprise reel. The gateway opens for everyone, at zero generative cost.

**No tier-sensitive cost authority (the one difference from QC Pre-flight):** QC Pre-flight owns the cumulative cost-ledger reconciliation against the combined tier ceiling. Ingest deliberately does **NOT** re-run that check — it is downstream of the gate that already enforced it, and re-litigating cost at the asset layer would be redundant and would risk a double-fail on a reel QC already cleared on budget. Ingest's authority is **technical asset readiness**, full stop. (Restated for traceability: combined ceilings $450 Pro / $870 Enterprise / ≤$40 Pilot-Starter Mode A are enforced upstream at QC Pre-flight Step 7.)

**Mode coverage (mode-convergent verdict, mode-aware ingestion):**

| Mode | What Ingest checks | Mode-specific note |
|------|--------------------|--------------------|
| A (human footage upload) | Coverage + declared shoot-packet spec + audio sync + filename firewall; `reshoot` route available if a shot is uncovered/unrecoverable | Only mode where `reshoot` is reachable (live footage can be re-shot; AI output is re-genned, not re-shot) |
| B (rendered + replicated) | Coverage + declared gen spec + `asset_uri` integrity + optional AI-Video-Gen cross-reference + filename/metadata firewall | Asset set arrives pre-normalized from the production agents; coverage gap → re-gen, not reshoot |
| C (replicated hot-path) | Coverage + declared replicated-shot spec + `asset_uri` integrity + filename/metadata firewall | Highest-margin mode; manifest is the cleanest (single-source asset set) |

**Mode-convergence guarantee (the core §4 contract):** Whatever mode enters, Ingest emits **one** `successAssetManifest` shape. `mode_convergence.ingested_mode` records the origin for audit; every field downstream of `mode_convergence` is mode-identical. Edit Director and all subsequent in-post agents are contractually mode-blind.

---

## §5. Process Steps (System Prompt Skeleton — Day 50 §7 will LOCK)

The agent runs an **11-step ingest loop** per invocation (mirrors the AI Video Gen / Style Replication / QC Pre-flight 11-step process pattern). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope.

**Step 1 — Verify QC precondition + parse input**
- Read the QC Pre-flight `preflight_report.json`. Confirm `verdict == "pass"` (or Lever-3 sign-off attached). Otherwise → halt with `upstream_qc_not_passed`.
- Parse input JSON against `input.schema.json` (Day 50/51 LOCKED). Select source branch by `metadata.production_mode` (A vs B/C) + upstream `output_type`.
- Confirm consumed asset-set branch is the success branch. Any `errorEnvelope` upstream → halt with `upstream_not_success`.

**Step 2 — Lineage integrity**
- Validate `metadata.parent_chain` is a well-formed 6-tuple inbound (5-tuple accepted for backward-compat until the §3.9 amendment ratifies). Malformed → `manifest_lineage_failure`.

**Step 3 — Asset URI integrity**
- Walk every `asset_uri` (footage, audio, music bed, pulled assets). Confirm each matches the platform-relative `ars://...` pattern (Hard Rule #8 — no absolute URLs) and is non-empty/non-dangling.
- Violation → `asset_uri_integrity_failure`.

**Step 4 — Defense-in-depth firewall pass (eighth time, asset layer)**
- Walk every filename, every embedded asset-metadata field (title/description/artist/comment tags), and every sidecar caption/SRT file with the canonical entity-firewall regex (Cross-SPEC §3 drift #10): `Holdco | Principal | NPOX | 4821 | 6315 | SLN | Retail Supply | Nonprofit Leader A | Community Nonprofit | Nonprofit Leader B | Nonprofit Leader C`.
- Hard FAIL → `asset_firewall_breach` + forensic log naming the leaking asset (in v1.0 this should rarely fire — seven prior passes cover content — but filenames/embedded metadata are a NEW surface the prior content passes never inspected; this is exactly the asset-layer gap Ingest exists to close).

**Step 5 — Declared-spec validation**
- For every asset, compare its `declared_spec` (aspect / fps / resolution / container / codec) against the `production_plan` platform/format target (Mode B/C) or the ProdCoord shoot-packet `format_spec` (Mode A).
- Mismatch → `asset_spec_violation`, `route_back_to` the responsible production agent (or `re-upload` for Mode A).

**Step 6 — Storyboard coverage check**
- For every `storyboard_ref.shot_list[]` entry, confirm ≥1 asset carries a matching `shot_ref`. Build `missing_shots[]`.
- Gap → `missing_shot_coverage`: Mode B/C routes `fail` (re-gen the shot); Mode A routes `reshoot` (→ ProdCoord) when no existing take covers it.

**Step 7 — Audio presence + sync adjudication**
- Confirm every shot requiring sync audio has an `audio[]` entry with `sync_declared_ok: true` (Mode A) or `has_audio: true` (Mode B/C native-voice).
- Missing/false → `audio_sync_failure`, `detail` names the affected shot(s). (Note: LUFS/loudness is NOT checked — that is Sound-agent + byte-probe domain, deferred to v1.1.)

**Step 8 — Duration envelope check**
- Sum declared asset durations / read the reel-level declared duration; compare to the brief's length band (e.g. 45s ±10%).
- Out-of-band → `duration_envelope_breach` (Day 50 LOCK decision: distinct code OR fold into `asset_spec_violation`).

**Step 9 — Mode-convergence normalization**
- Map the mode-specific source (Mode A `footage_upload_manifest` / Mode B/C `replicated_shots[]`+`rendered_shots[]`) into the single canonical `asset_bundle` shape (`raw_footage[]`, `audio[]`, `assets_pulled[]`, `music_bed`) per Blueprint §4.8.
- Record `mode_convergence.ingested_mode`; assert every post-convergence field is mode-identical.

**Step 10 — Construct manifest payload**
- If all green: build `successAssetManifest` per §3.1 with the full `asset_bundle` + per-asset `spec_check` evidence + `coverage_check` + `verdict: "pass"` + `handoff_targets: ["edit-director-agent"]`.
- Compute `manifest_evidence_hash` (SHA-256 over the evidence + spec_check block — tamper-evident).
- Extend `parent_chain` to a **7-tuple** (append `asset_manifest_id`), held additively per §3.3.
- Set `byte_probe_performed: false` (v1.0 honesty), `asset_manifest_class: "pre_edit"`, `human_review_required: true` per Lever-3 default.

**Step 11 — Emit + handoff**
- Validate output payload against `output.schema.json` (Day 50/51 LOCKED). Hard FAIL → forensic log + halt (output should always validate; failure here = agent bug).
- Emit JSON to stdout (paste-and-run runbook) OR persist to platform path per runtime environment.
- On `fail` / `reshoot`, set `route_back_to` per the §3.2 verdict↔route map so the Orchestrator can re-enter the pipeline at the correct agent.

**Anti-patterns Step 11 prevents (Lock-time discipline mirror from QC Pre-flight / Style Replication §11):**
- No markdown fences around output JSON.
- No `print()` statements before the output JSON block.
- No engine credentials referenced; no byte-level media decode invoked (v1.0 calls no engine and runs no ffprobe — `byte_probe_performed` is `const false`).
- No absolute URLs in any `asset_uri` echoed into the manifest (Hard Rule #8 inherit).
- No `pass` verdict emitted while any asset check is unresolved (must be `fail` or `reshoot`).
- **No operator-impersonation:** Ingest emits `human_review_required: true` and a verdict *recommendation*; it does NOT mark a reel "cleared for edit" as a ratified state — that is the Lever-3 operator action (or a future Orchestrator auto-dispatch).

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 50 + 51)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 50 partial 1. Pattern source: QC Pre-flight §6 / Style Replication §6. Target 10–12 checks bipartite-covering the 7–9 errorEnvelope codes. Slot 11 reserved for `ingest_agent_failed` per Cross-SPEC §3.6 slot-naming canon.
- **§7 System Prompt v1.0** — Day 50 partial 1. Frame + hard rules + universal-tier table + 11-step ingest loop verbatim from §5 + the Blueprint §4.8 `asset_bundle`/`spec_check` target shape inlined. ~11–13 KB target. Hard Rules mirror QC Pre-flight with Ingest-specific tightening on the "declared-spec only, no byte-probe" and "recommend-don't-clear" Lever-3 discipline.
- **§8 Performance Targets** — Day 51 partial 2. 9 metric categories. Schema validity 100% / asset-firewall catch 100% (the 8th pass must be perfect by construction) / coverage-gap catch 100% (a missing shot must never pass) / false-pass rate 0% target / false-fail rate ≤ 5% (over-blocking is the acceptable failure direction) / p50 latency 25s / p95 75s (reasoning-only, fast) / zero engine cost.
- **§9 Test Fixtures** — Day 51 partial 2. 5-fixture portfolio: TC-01 clean Mode B Pro PASS (full manifest) · TC-02 Mode C Enterprise PASS (single-source clean) · TC-03 `missing_shot_coverage` Mode A (uncovered shot → `reshoot` + ProdCoord route) · TC-04 `asset_spec_violation` (aspect mismatch → `fail` + route) · TC-05 `asset_firewall_breach` (banned token injected in a filename — the 8th-pass catch). 5 of 7–9 codes exercised; remainder in schema-only fixtures.
- **§10 Field Map** — Day 50 partial 1. ~25 rows · passthrough vs transform vs derived. Per-asset evidence map + reel-level manifest aggregate map + mode-convergence normalization map.
- **§11 Cost Model** — Day 51 partial 2. Zero engine snapshot (reasoning + manifest construction only; no ffprobe in v1.0). Catch-cost-avoidance value model (economic justification = prevented wasted edit cycles, not direct margin).
- **§12 Verdict Math** — Day 51 partial 2. PASS = (QC precondition met) ∧ (all `asset_uri` integral) ∧ (asset-firewall clean) ∧ (all declared specs match) ∧ (full storyboard coverage) ∧ (audio present+sync-declared) ∧ (duration in band). Any single ∧-term false → fail/reshoot per §3.2 + Step-6 mode routing. Deterministic, no thresholds to tune.
- **§13 Critical Decisions LOCKED** — Day 51 partial 2. Target 10–14 LOCKED decisions. Pre-scaffolded list:
  1. Asset-readiness vs full-decode scope — v1.0 = declared-spec adjudication ONLY; byte-level media probe (ffprobe/MediaInfo) deferred to v1.1 once a runtime engine exists. [LOCKED-as-drafted Day 48]
  2. Universal tier access — all 4 tiers traverse Ingest (asset readiness is not a tier feature). [LOCKED-as-drafted Day 48]
  3. Verdict model — Pass / Fail-fixable / Reshoot; `reshoot` is Mode-A-exclusive. [LOCKED-as-drafted Day 48]
  4. QC-pass precondition — Ingest runs only on a QC-passed (or Lever-3 approved) reel; otherwise halts `upstream_qc_not_passed`. [LOCKED-as-drafted Day 48]
  5. No cost re-litigation — Ingest does NOT re-run the cumulative cost ledger (QC Pre-flight's authority). [LOCKED-as-drafted Day 48]
  6. 7-tuple parent_chain — inherits QC Pre-flight 6-tuple + appends `asset_manifest_id`; DOUBLY-deferred (depends on §3.9 amendment ratification AND QC Pre-flight 6-tuple LOCK). [DEFERRED — held additively at `minItems: 5`]
  7. errorEnvelope code count — 7–9 target. [PRELIMINARY · operator amend Day 51]
  8. Self-QC check count — 10–12. [PRELIMINARY · operator amend Day 51]
  9. Mode-convergence guarantee — one manifest shape regardless of mode; downstream agents mode-blind. [LOCKED-as-drafted Day 48]
  10. False-pass tolerance — ZERO (a missing/dangling/off-spec asset must never pass); bias all ambiguity toward fail/reshoot. [LOCKED-as-drafted Day 48]
  11. Engine + probe policy — NO generative engine calls, NO byte-level decode in v1.0; `byte_probe_performed: const false`. [LOCKED-as-drafted Day 48]
  12. Recommend-don't-clear — Ingest emits `human_review_required: true` + verdict recommendation; never flips a reel to a ratified "cleared-for-edit" state. [LOCKED-as-drafted Day 48]
  13. Audio-sync scope — declared sync-flag adjudication only; LUFS/loudness deferred to v1.1 (Sound-agent + decode domain). [LOCKED-as-drafted Day 48]
  14. `duration_envelope_breach` — distinct code vs fold into `asset_spec_violation`. [PRELIMINARY · operator amend Day 51]
- **§14 Calendar status updates** — Day 50 partial 1. Day 48 ✓ → trajectory populated.
- **§15 Change Log** — Day 51 partial 2. v1.0 lifecycle entries (outline-day-48 → Rest Day-day-49 → body-day-50 → body-day-51 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 51 partial 2. Cross-SPEC §3.9 canonical fields + 5 Ingest additions (7-tuple parent_chain, asset_manifest_class, manifest_evidence_hash, runtime_environment_class, byte_probe_performed).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `ingest-agent` (kebab-case, matches the fleet pattern) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `manifest_evidence_hash` SHA-256 over evidence block; optional Mode B AI-Video-Gen cross-reference |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication / QC Pre-flight shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ Ingest consumes the accumulated surface as read-only context (QC Pre-flight already adjudicated the floor); Ingest contributes its own ≥4 ingest predicates downstream |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-convergent verdict + mode-aware ingestion (A/B/C) + mode-convergence guarantee |
| §3.6 Slot 11 naming canon | ✅ Reserved `ingest_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Consumed shapes respected; Ingest's own predicates snake_case |
| §3.8 Tier↔mode firewall (8th defense-in-depth) | ✅ Step 4 asset-layer firewall + §4 universal-tier table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 7-tuple, held additively. **Doubly-deferred** — gated on the §3.9 amendment ratification AND the QC Pre-flight 6-tuple LOCK. |
| §3.10 Cost ceiling authority | ✅ §4 explicitly DECLINES to re-litigate cost (QC Pre-flight's authority) — no double-enforcement; Ingest is $0-cost |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / QC Pre-flight / Cross-SPEC references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 48 outline — 6 parked for operator amendment)

1. **Declared-spec vs byte-probe scope** — v1.0 adjudicates declared asset metadata only; full ffprobe/MediaInfo decode is v1.1. Confirm this is the right buildable slice given the no-engine/$0 sprint posture. *(Donna recommends: confirm declared-spec-only for v1.0 — it is the buildable, highest-leverage slice; byte-probe lands when a runtime engine ships.)*
2. **`reshoot` vs `fail` on a Mode A coverage gap** — when a Mode A shot is uncovered, is it always reshoot, or fail-then-re-upload if other takes might cover it? *(Donna recommends: attempt take-substitution first → `fail` (re-upload), escalate to `reshoot` only when no existing take covers the shot.)*
3. **7-tuple parent_chain** — doubly-deferred (depends on the §3.9 n-tuple amendment AND the QC Pre-flight 6-tuple LOCK, both operator-pending). Ingest is the first 7-tuple consumer — its build is a second forcing function. *(Donna recommends: RATIFY the §3.9 amendment AS-DRAFTED so all 17 agents inherit n-tuple lineage; Ingest holds additively until then.)*
4. **Edit-Director handoff readiness** — Ingest hands to a not-yet-built Edit Director (Agent #9 candidate). Should v1.0 emit the manifest to a holding store (Notion Asset Manifest DB) until Edit Director ships, or assume direct handoff? *(Donna recommends: emit to the Notion Asset Manifest DB in v1.0; direct agent-to-agent handoff activates when Edit Director LOCKs.)*
5. **False-pass tolerance** — confirm ZERO false-pass policy (bias all ambiguity to fail/reshoot). *(Donna recommends: ratify zero-false-pass — a phantom asset reaching the editor is the expensive failure direction.)*
6. **`duration_envelope_breach` codeification** — distinct errorEnvelope code, or folded into `asset_spec_violation`? *(Donna recommends: fold into `asset_spec_violation` with a `detail.subtype` — keeps the code count lean; revisit if duration defects prove common.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (full Ingest trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 48 | Sat Jun 6 | **SPEC outline §0–§5** [SHIPPING NOW] | QC Pre-flight Day 40 outline |
| 49 | Sun Jun 7 | **REST DAY** — no build (pre-stage partial-1 scaffold only) | Day 21/28/35/42 Rest Day compounding |
| 50 | Mon Jun 8 | SPEC body partial 1: §6 + §7 + §10 + §14 | QC Pre-flight Day 41 |
| 51 | Tue Jun 9 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | QC Pre-flight Day 43 |
| 52+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | QC Pre-flight Day 44–47 / Style Replication Day 32–37 |

**Sprint context:** Ingest is **Agent #8** — the first post-production agent, extending the fleet past the seven launch-and-gate agents. The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) ships on the six production agents through the QC Pre-flight gate; Ingest v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the QC Pre-flight and Style Replication outlines were (while prior LOCK ceremonies remain operator-gated).

---

## Files produced today (Day 48)

- `ars/ARS-2026-06-06-Day-48-Ingest-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-06-06.md` — Day 48 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 48)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked. No byte-level media decode (ffprobe/MediaInfo) run. (Ingest by design calls no generative engine and runs no probe in v1.0 — appropriate for a declared-spec asset gateway.)
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no client/investor outreach. The end-of-run status SMS to Jamila (Google Voice [status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business. (SMS provisioning status carried — see build log.)
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, zero $ spent.
- ✅ **No operator-impersonation.** AI Video Gen Day 24 Items 8 + 11 + Day 27 sit-down verdict NOT assumed. Style Replication Day 32 Items 6 + 8 + 11 + Day 36 runbook execution NOT assumed. QC Pre-flight Day 44 Items 6/8/11 + Day 47 runbook execution NOT assumed. All three production/gate LOCK ceremonies confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Cross-SPEC §3.9 amendment NOT silently committed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. Ingest v1.0 LOCK will hard-gate itself on the upstream LOCKs (especially QC Pre-flight's 6-tuple) being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 4 enumerates HC/NPOX tokens precisely so the agent can BLOCK them at the asset layer — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** QC Pre-flight Day 40 outline structure inherited verbatim. Orchestration Blueprint §1.4 / §4.8 / §7 (Agent 09 Ingest definition) + Cross-SPEC §3 canon used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-48 build runs Saturday (Pacific). Day 49 (Sun Jun 7 Pacific) is the 7th Rest Day: docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 48 ships clean. Day 50 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14) after the Day 49 Rest Day scaffold pre-stage. Ingest is Agent #8 of 17 — the 8th defense-in-depth firewall (asset layer) and the first post-production agent, the structural seam that collapses three production modes back to one mode-agnostic post path. Operator pickup: (1) the three predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight) remain pending and gate Ingest's eventual v1.0 LOCK — QC Pre-flight's 6-tuple in particular is Ingest's direct 7-tuple dependency; (2) review the §13 critical-decisions list + ratify the Cross-SPEC §3.9 n-tuple amendment so the n-tuple parent_chain is canon; (3) confirm the Agent #8 = Ingest selection (or re-assign the slot) at the QC Pre-flight LOCK-ceremony close.*
