# ARS — Edit Director Agent v1.0 SPEC OUTLINE (§0–§5)

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Authored:** Day 58 · Tue Jun 16, 2026 (Pacific) · overnight build session (Donna)
**Deliverable class:** Forward SPEC outline §0–§5 (the head-start design for Agent #9 of 17)
**Status:** OUTLINE ONLY — no LOCK, no schema, no SKILL bundle. Body partials author Days 59 + 60 per the calendar in §0.
**Pattern source:** Ingest Day 48 outline (`ARS-2026-06-06-Day-48-Ingest-Agent-SPEC-Outline.md`) — section structure inherited verbatim. Orchestration Blueprint §1.2 (Agent 10 row), §2 swim-lane, §4.8 (Ingest→Edit-Director payload), §4.9 (Edit-Director→Editor payload), §7 dispatch + I/O tables, and Cross-SPEC §3 canon used as the grounding spine. Brand-creative rules grounded in `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7–§11.

> **Agent-selection note (Donna, surfaced not hidden):** The Day 57 Ingest LLM-Test-Runbook close named the next forward deliverable as **"Agent #9 (Edit Director) SPEC outline kickoff — the first agent in the mode-blind post-production tail Ingest unlocks."** That selection is followed here. The Ingest v1.0 LOCK ceremony itself is **operator-only** (it joins AI Video Gen / Style Replication / QC Pre-flight in the pending-LOCK queue) — Donna does NOT advance it. This outline is the forward-design head-start, authored on the same forward-looking basis the Ingest, QC Pre-flight, and Style Replication outlines were while their LOCK ceremonies remained operator-gated. Rationale for Edit Director as the #9 build: (1) **strict dependency order** — Edit Director is the immediate runtime stage downstream of Ingest (Blueprint §7: "On Ingest completion"), consuming the Asset Manifest Ingest produces; (2) **convergence payoff** — it is the **first contractually mode-blind agent**, the structural proof that Ingest's mode-convergence contract works; (3) **family pivot is high-value design surface** — Edit Director is the first *creative-authoring* agent in the post tail (it MAKES cut/pacing/caption decisions), not another validation/gate agent, so its outline establishes the authoring-agent pattern the rest of the post fleet (Editor/Sound/Motion) inherits; (4) **fleet-unblock** — nothing downstream (Editor → Sound → Motion → full QC) can run without the Edit Plan. Operator may re-assign the #9 slot at the LOCK-ceremony close.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 9 — Post-production creative layer (asset bundle → edit plan) |
| Agent index | **#9 of 17** (build sequence — continues the Ingest Day 48 "agent #8 of 17" framing) |
| Runtime pipeline position | **10 — Edit Director** (writes the edit plan: cut order, pacing, music bed, caption style, lower-thirds, transitions); receives the Asset Manifest from Ingest, hands the Edit Plan to Editor |
| Pipeline tier | POST-PRODUCTION CREATIVE (first creative-authoring agent in the post tail; first agent built after the post-production gateway) |
| Mode coverage | **Mode-blind by construction** — consumes the single mode-convergent Asset Manifest Ingest emits; never sees `production_mode` as a branch discriminator. The FIRST agent in the fleet that is contractually mode-agnostic (Blueprint §3 "from Ingest onward, post-production is mode-agnostic" — Edit Director is where that promise is first *consumed*). |
| Predecessor SPEC (gate) | `ARS-2026-06-11-Day-53-Ingest-Agent-v1-LOCK-CANDIDATE.md` (Day 53 LOCK candidate — operator-gated). Edit Director runs only on an Ingest-passed (`successAssetManifest`, verdict `pass`) reel. |
| Predecessor schemas | `ARS-2026-06-12-Ingest-output.schema.json` (Day 54) — the `asset_bundle` + `spec_check` + `coverage_check` block consumed as the primary INPUT. Plus the Script Agent `output.schema.json` (Day 9) + Storyboard `output.schema.json` (Day 12) consumed as denormalized creative-intent inputs (beat map, caption strategy, shot vocabulary). |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape (§3.3/§3.8), metadata block + n-tuple parent_chain (§3.9) all inherited |
| Brand-creative canon | `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (visual identity / motion / lower-thirds), §8 (reel format specs / structure), §10 (CTA library — internal-question rule), §11 (caption spec) — the rule surface Edit Director's plan must satisfy |
| Defense-in-depth layer | **9th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → QC Pre-flight → Ingest → **Edit Director**) — the **authored-text** firewall: it is the first agent to firewall-scan text it WRITES ITSELF (lower-thirds copy, caption strings, end-card line), not just text it receives |
| Lever inheritance | Reads `lever_state` from upstream `metadata`; emits `human_review_required` per Lever-3 default. As a creative-decision agent its Edit Plan is a *recommendation* — it never marks a plan "approved for cut"; the operator (or a future Orchestrator dispatch) ratifies before Editor executes. |
| Pricing tier authority | **ALL tiers** — Pilot · Starter · Pro · Enterprise. Every reel needs an edit plan. **Tier-sensitive in plan RICHNESS** (unlike Ingest, which is tier-flat): caption-burn mandatory + 3 variants on Pilot/Starter; captions optional + more b-roll/music-swells/variants on Pro/Enterprise (Script Agent tier ladder inherited). |
| Cost authority class | **Near-zero (ties Ingest / QC Pre-flight for lowest in fleet)** — pure reasoning + plan construction over the Asset Manifest + creative-intent inputs. **No generative engine calls, no media render, no byte-level decode in v1.0** — Edit Director writes a *plan*, it does not cut pixels (that is Editor, position 11). Effective per-reel cost ≈ $0.00. |

**Build calendar (Week 9 — Edit Director trajectory, mirrors the proven 8-day agent-build cadence):**
- **Day 58** (today, Tue Jun 16 · Wk9) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 59 (Wed Jun 17 · Wk9) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 60 (Thu Jun 18 · Wk9) — SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16
- Day 61+ (TBD) — LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK (pattern: Ingest Day 53–57 / QC Pre-flight Day 44–47)
- Day 63 (Sun Jun 21 · Wk9) — **REST DAY** (no build; pre-stage next scaffold only, per the Day 21/28/35/42/49/56 Rest Day-compounding pattern)

> **Rest Day honesty:** This Day-58 build runs Tuesday (Pacific) — building is allowed. The next Rest Day is Day 63 (Sun Jun 21 Pacific) per the Day 57 log close. The UTC clock may have rolled past midnight at author time, but the sprint labels by Jamila's Pacific date (Tue Jun 16) — the same convention noted in prior logs.

> **Sequencing honesty:** The 42-day sprint's headline deliverable — the Mode B Pro single-reel **commercial demo** (Day 42 target, now past) — shipped on the six launch-critical production agents threaded through the QC Pre-flight gate. Edit Director is the second *post-production* agent (after Ingest); its v1.0 build proceeds inside the **post-launch hardening window** and does **not** gate the launch demo. This outline is the forward-design head-start so the in-post fleet is buildable in dependency order once the production-tier + Ingest LOCKs close.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Edit Director Agent** is the **creative brain of post-production** — the moment a reel stops being a *validated bundle of media files* and becomes a *directed edit*: a specific cut order, a specific rhythm, a specific caption and lower-third treatment, a specific musical spine. It is the first agent in the fleet whose job is to **decide** rather than to **validate**, and the first that is contractually **mode-blind**.

Where the eight upstream agents adjudicated whether things were *correct*, Edit Director decides how things should be *assembled*:
- Brief / Script / Storyboard = intent + content authoring (what the reel SAYS and how it's shot)
- Production Coord = logistics (mode, vendor, budget)
- AI Video Gen / Style Replication = render + brand-finish (the pixels exist)
- QC Pre-flight = ship-safety (the reel is brand-safe + format-correct)
- Ingest = asset-readiness (the files are present, valid, in-sync — one mode-agnostic Asset Manifest)

The Edit Director Agent picks up at the manifest and authors the assembly:
- **Edit Director Agent = edit-plan authoring ("Given a complete, valid Asset Manifest and the original Script beat map + Storyboard shot vocabulary, in what ORDER do these shots cut, at what PACING, with what CAPTION and LOWER-THIRD treatment, over what MUSIC bed, with what TRANSITIONS — such that the result honors every REINVENTED brand-edit rule and the script's emotional arc? Emit a single canonical Edit Plan the Editor can execute beat-for-beat.")**

**Single-responsibility line (LOCKED on intent):**
> *"Post-production creative director. Receives the Ingest-passed Asset Manifest (one mode-agnostic asset bundle + spec_check + coverage_check) plus the denormalized Script beat map, caption strategy, and Storyboard shot vocabulary, and authors one canonical Edit Plan — cut order (shot-ref → in/out timecodes), pacing (bpm + cut rhythm), caption style + per-line copy, lower-thirds (timed, branded), music-bed selection + swell map, transition policy, and the mandatory end-card — that honors the REINVENTED brand-edit ruleset (hard-cuts-only, one-text-reveal-per-8s, one-emotional-beat, Alux minimalism, ≤22-char caption lines, internal-question CTA) and the 45–75s structure. Authors no pixels and renders no media; calls no generative engine. Emits a recommendation (human_review_required) — never a ratified 'approved-for-cut' state."*

**Why this agent's reason-to-exist is the mode-convergence payoff (Blueprint §3):** Ingest is the agent that *makes* the pipeline mode-agnostic; Edit Director is the first agent that *depends on* that being true. It reads ONE Asset Manifest shape and never branches on whether the footage was a videographer's `.mov`, a HeyGen render, or a Style-Replication grade pass. **This is Donna's design thesis for building Edit Director as Agent #9: it is the first contractually mode-blind agent, and therefore the live proof that Ingest's convergence seam holds.** If Edit Director can author a complete plan from the manifest alone — with zero mode awareness — the convergence contract is validated end-to-end.

**Pipeline position (per Orchestration Blueprint §2 swim lane):**
```
... → INGEST (asset-readiness gate) →
   [successAssetManifest · verdict = pass]
        │
        ▼  [Asset Manifest: asset_bundle + spec_check + coverage_check]
   EDIT DIRECTOR (edit-plan authoring)
        │
        ▼  [Edit Plan: cut_order + pacing + captions + lower_thirds + music_bed + transitions + end_card]
   11 Editor → 12 Sound → 13 Motion → 14 QC (full)
        │
   [plan_unbuildable] → route back to Ingest (manifest insufficient) or surface to operator (creative-intent conflict)
```

**Why a creative-authoring agent distinct from the upstream creative agents (the boundary question):** Script already authored the beat map + caption copy; Storyboard already authored the shot vocabulary — so what does Edit Director add? A clean separation of concerns across the production→post boundary:
1. **Script + Storyboard author the PLAN-TO-SHOOT** — what to say, how to frame it, the *intended* beats. They run BEFORE the footage exists. They cannot know which takes survived, what the real shot durations are, or which assets Ingest validated.
2. **Edit Director authors the PLAN-TO-CUT** — given the assets that ACTUALLY exist and passed Ingest, the concrete assembly: real in/out timecodes against real declared durations, cut order reconciled to actual coverage, caption timing against the real cut, the lower-third schedule, the music swell map. It runs AFTER the footage is validated.
3. **The two phases catch different problems.** Script/Storyboard can specify a 3-beat arc; only Edit Director, holding the real Asset Manifest, can discover that the available assets total 71s of usable footage for a 60s reel and decide what to trim — and do it while honoring the one-emotional-beat and hard-cuts-only rules. Edit Director does NOT re-author content (it trusts Script's copy + Storyboard's vocabulary); it *directs the assembly of validated assets toward the script's intent*.

The actual cut execution (rendering the v1 edit file, frame-accurate trims, the EDL→timeline conform) is **Editor's** job (position 11) — Week 2 launch posture is human-in-the-loop (agent drafts the EDL, a human executes in the editor app), full automation targeted Week 4–5 per Blueprint §7. v1.0 Edit Director authors the *plan*; it produces no media file.

**Hand-off contract enforced:**
- **PRECONDITION:** Edit Director reads the Ingest `asset_manifest.json`. If `output_type != "successAssetManifest"` OR `verdict != "pass"` (and no Lever-3 human sign-off is attached) → halt with `upstream_ingest_not_passed`. Edit Director never directs a reel whose assets did not pass Ingest.
- **INPUT contract:**
  - The Ingest `successAssetManifest` — `asset_bundle` (`raw_footage[]` with `shot_ref` + `duration_sec`, `audio[]`, `assets_pulled[]`, `music_bed`), `spec_check` (must show `missing_shots: []`), `coverage_check` (`coverage_complete: true`).
  - The denormalized **Script** beat map (`audio_track`, `captions`, `pace_marker`s, `voice_pacing`, on-screen text blocks) + **Storyboard** shot vocabulary (Alux frame language per shot) as creative-intent reference.
  - The **production_plan** platform/format target (aspect, platform_variants[]) + the **brief** length band.
  - The **denormalized upstream chain** in `metadata.parent_chain` (7-tuple inbound from Ingest, doubly-deferred) + accumulated `qc_pre_flags[]`.
- **OUTPUT contract:** Emits `edit_plan.json` per §3 (polymorphic: `successEditPlan | errorEnvelope`). Editor reads the plan's `cut_order` + `pacing` + `caption_style` + `lower_thirds` + `transitions` + `music_bed` (Blueprint §4.9 shape) and executes without re-deriving creative intent.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| Cut-order authoring (shot_ref → in_ms/out_ms against declared durations) | Frame-accurate trim points (sub-frame conform) — needs the real media + a runtime editor |
| Pacing plan (`pacing_bpm` + `cut_rhythm` cue language) | Beat-detected music-sync (audio analysis of the music bed) — needs byte-level decode |
| Caption style + per-line copy timing (from Script's caption strategy, ≤22 char/line, ≤2 lines) | Live frame-accurate caption-burn timing — Editor/Motion domain |
| Lower-thirds schedule (timed, lowercase-sans, left-aligned, branded) | Animated lower-third keyframe authoring — Motion domain (position 13) |
| Music-bed selection + swell map (count per tier) | Loudness/LUFS normalization (−14 IG/TT, −16 YT) — Sound domain (position 12), needs decode |
| Transition policy enforcement (hard-cuts-only; zero fades/wipes/zooms) | Multi-variant auto-cutdown (1:1 LinkedIn cutdown auto-gen) — v1.1 (v1.0 authors the primary 9:16, flags variants) |
| End-card insertion (mandatory "REINVENTED — build on purpose." serif hold) | A/B alternate-cut generation (two directed versions per reel) |
| 9th defense-in-depth firewall pass over AUTHORED text (lower-thirds, captions, end-card) | Auto-music-licensing check (rights clearance on the music bed) |
| 8-tuple parent_chain extension (inherits Ingest 7-tuple + appends `edit_plan_id`) | Real-time collaborative plan editing (operator live-edits the plan) |
| Edit Plan construction (Blueprint §4.9 shape) + plan recommendation | Predictive edit-quality scoring (will this cut retain viewers?) |

**Pricing tier table (Edit Director is universal-access but tier-sensitive in richness — defense-in-depth pass 9):**

| Tier | Reaches Edit Director? | Plan richness ceiling | Cost | Caption rule |
|------|-----------------------|-----------------------|------|--------------|
| Pilot — Founding 5 | **YES** | ≤8 cut beats, ≤3 b-roll, 1 music swell, 3 variants | ~$0.00 | burn-in MANDATORY |
| Starter — Operator | **YES** | ≤8 cut beats, ≤3 b-roll, 1 music swell, 3 variants | ~$0.00 | burn-in MANDATORY |
| Pro — Studio | **YES** | ≤12 cut beats, ≤6 b-roll, 2 music swells, 4 variants | ~$0.00 | captions optional |
| Enterprise — Agency | **YES** | ≤12 cut beats, b-roll unlimited, 3 music swells, 5 variants | ~$0.00 | captions optional |

Edit Director adds **zero** generative cost to every tier envelope. Its economic value is **directed coherence + brand-rule guarantee** — every reel ships with a deliberate, brand-compliant edit instead of an ad-hoc cut, and brand violations are caught *before* an editor burns a cut cycle.

---

## §2. Inputs

Edit Director has **one canonical responsibility** (author the Edit Plan) reached from **one** input shape — the mode-convergent Asset Manifest. Unlike every upstream agent, there is **no mode branch** and no source-polymorphism: this is the first agent whose input is structurally mode-blind. (The only discriminator it reads is `tier`, for plan-richness scaling.)

### §2.1 Precondition input — Ingest Asset Manifest verdict (gate)

**Always read first.** The Ingest `asset_manifest.json`:
```json
{
  "output_type": "successAssetManifest",
  "verdict": "pass",
  "reel_ref": { "asset_manifest_id": "assetmanifest-REINVENTED-2026-06-16-001" },
  "coverage_check": { "coverage_complete": true },
  "spec_check": { "missing_shots": [] },
  "human_review_required": true,
  "metadata": { /* 7-tuple parent_chain inbound, held additively */ }
}
```
**Hard validation:** `output_type == "successAssetManifest"` AND `verdict == "pass"` (or a Lever-3 human sign-off is attached to a non-pass manifest). Otherwise → halt with `upstream_ingest_not_passed`. Edit Director does not direct a reel whose assets failed ingest.

### §2.2 Primary input — Asset Manifest bundle (the assets to direct)

**Required input fields (preliminary — full schema on the Day 59/60 partials):**
```json
{
  "asset_bundle": {
    "raw_footage": [
      { "shot_ref": 1, "asset_uri": "ars://reels/REINVENTED-2026-W25-001/raw/shot_1.mp4", "duration_sec": 3, "source": "style-replication-agent" }
    ],
    "audio": ["ars://reels/.../raw/voice_track.wav"],
    "assets_pulled": ["logo_ivory_gold.png", "lt_authority_v3.mogrt"],
    "music_bed": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav"
  },
  "spec_check": { "missing_shots": [] },
  "coverage_check": { "shots_required": 7, "shots_covered": 7, "coverage_complete": true },
  "metadata": { /* Cross-SPEC §3.9 — tier, lever_state, brand_id, session_id, parent_chain (7-tuple inbound), accumulated qc_pre_flags surface */ }
}
```

**Hard validations on primary input (defense-in-depth pass 9):**
1. Upstream `output_type` is `successAssetManifest`, NOT `errorEnvelope`. (errorEnvelope → `upstream_not_success`.)
2. `coverage_check.coverage_complete == true` AND `spec_check.missing_shots == []` (defensive re-confirm — Ingest guaranteed it, but Edit Director cannot author a cut over a hole). Violation → `incomplete_shot_coverage`.
3. Every `asset_bundle.raw_footage[]` entry carries a `shot_ref` resolvable against the Script/Storyboard beat map (so cut-order can map intent → asset). Unresolvable → `beat_map_unmappable`.
4. `asset_uri`s remain platform-relative `ars://...` (Hard Rule #8 inherit — Edit Director echoes them into `cut_order`; it must not introduce an absolute URL). Violation → `asset_uri_integrity_failure`.
5. `metadata.parent_chain` is a well-formed 7-tuple inbound (5/6/7-tuple accepted additively — see §3.3). Malformed → `plan_lineage_failure`.

### §2.3 Creative-intent inputs — Script beat map + Storyboard vocabulary

**Denormalized, read as reference (not re-authored).** Edit Director reads:
```json
{
  "script_ref": {
    "audio_track": { "voice_pacing": "operator-conversational-165wpm", "pace_markers": [ /* per-beat */ ] },
    "captions": { "style": "burned-in-lowercase-sans", "max_chars_per_line": 22, "max_lines_on_screen": 2 },
    "on_screen_text": [ { "second_start": 25.0, "second_end": 30.0, "text": "...", "size": "L", "anchor": "lower-third" } ],
    "structure": { "hook": "0:00-0:08", "body_beats": 3, "cta": "0:55-1:05" },
    "cta": { "type": "internal_question" }
  },
  "storyboard_ref": { "shot_list": [ { "shot": 1, "frame_language": "held-object-close-up", "duration_sec": 3 } ], "total_shots": 7 }
}
```
Used to drive cut order (honor the hook→3-beat→CTA structure), pacing (`165wpm` → `pacing_bpm` + cut rhythm), caption copy + char limits, lower-third content + timing, and the one-emotional-beat / one-text-reveal-per-8s rhythm rules. **Edit Director consumes these as fixed creative intent — it directs the assembly toward them, it does not rewrite copy or re-frame shots.**

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block: `tier`, `lever_state`, `brand_id`, `session_id`. Edit Director reads `tier` to scale plan richness per §4 (the only tier-sensitive authority in the post tail so far) and sets the plan's `human_review_required` per Lever-3 default. It does **not** re-run cost or asset validation — those are QC Pre-flight's and Ingest's authorities respectively; Edit Director trusts the passed verdicts.

---

## §3. Outputs (skeleton)

Edit Director emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 / QC Pre-flight Day 40 / Ingest Day 48 output pattern (`oneOf [success branch, errorEnvelope]`).

### §3.1 successEditPlan branch (plan authored)

```json
{
  "output_type": "successEditPlan",
  "verdict": "plan_ready",
  "reel_ref": {
    "brief_id": "brief-REINVENTED-2026-06-16-001",
    "asset_manifest_id": "assetmanifest-REINVENTED-2026-06-16-001",
    "edit_plan_id": "editplan-REINVENTED-2026-06-16-001"
  },
  "edit_plan": {
    "cut_order": [
      { "shot_ref": 1, "in_ms": 0, "out_ms": 3000, "frame_language": "held-object-close-up" },
      { "shot_ref": 2, "in_ms": 3000, "out_ms": 8000, "frame_language": "slow-push-in-face" }
    ],
    "pacing_bpm": 120,
    "cut_rhythm": "quarter-note on beats, syncopated on b-roll",
    "caption_style": "burn-in, lowercase sans, one line at a time, <=22 chars/line, ivory on ink",
    "caption_lines": [ { "at_ms": 0, "text": "your calendar doesn't lie", "line": 1 } ],
    "lower_thirds": [ { "at_ms": 25000, "content": "the operator's stack", "style": "lt_authority_v3", "case": "lowercase", "align": "left" } ],
    "transitions": "hard cuts only — zero fades, zero wipes, zero zooms (brand rule)",
    "music_bed": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav",
    "music_swell_map": [ { "at_ms": 48000, "type": "emphasis_swell" } ],
    "end_card": { "at_ms": 63500, "line": "REINVENTED — build on purpose.", "font_class": "serif_display", "hold_ms": 1500, "doubles_as_thumbnail": true }
  },
  "structure_check": { "hook_window_ok": true, "body_beats": 3, "cta_internal_question_ok": true, "total_duration_ms": 65000, "duration_in_band": true },
  "brand_edit_check": {
    "hard_cuts_only": true,
    "one_text_reveal_per_8s": true,
    "one_emotional_beat": true,
    "lower_thirds_lowercase_left": true,
    "captions_within_char_limit": true,
    "no_reel_level_sales_cta": true,
    "end_card_present": true
  },
  "edit_plan_firewall_pass_9": { "status": "pass", "authored_text_fields_scanned": 14, "hits": 0 },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_manifest" },
  "tier_richness": { "tier": "Pro", "cut_beats": 11, "b_roll": 5, "music_swells": 2, "variants_planned": 4 },
  "handoff_targets": ["editor-agent"],
  "metadata": { /* Cross-SPEC §3.9 with Edit-Director additions per §3.3 — 8-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (plan not buildable)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "beat_map_unmappable",
  "failed_check_id": 3,
  "attempts": 1,
  "route_back_to": "ingest-agent",
  "reel_ref": { "edit_plan_id": "editplan-REINVENTED-2026-06-16-001" },
  "cost_incurred_usd": 0.00,
  "detail": {
    "violation": "asset_bundle.raw_footage shot_ref 5 has no resolvable beat in the Script beat map",
    "affected_shots": [5],
    "recovery_path": "re-confirm Ingest coverage_check OR re-sync the Script beat map to the delivered shot set"
  },
  "metadata": { /* Cross-SPEC §3.9 — 8-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `plan_ready` | Edit Plan authored + brand-compliant; cleared into Editor | `null` (forward to Editor) | All structure + brand-edit checks green |
| `fail` | Plan unbuildable from current inputs (recoverable upstream) | `ingest-agent` (asset gap) OR `production-coord-agent` (creative-intent conflict needing a re-plan) | Coverage/lineage/mappability defect, or a brand-rule conflict that cannot be auto-resolved |
| `revise` | Plan authored but a soft brand-rule is in tension; needs operator creative call | `null` (held for Lever-3) | E.g., the only coherent cut needs a 4th body beat vs the one-emotional-beat rule — surface, don't silently override |

### §3.3 Metadata block additions (Edit-Director-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **8-tuple** (inherits Ingest's 7-tuple lineage + appends own `edit_plan_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (DRAFTED Day 31 §16.3; **ratification still operator-pending**). **Doubly-deferred** like Ingest's: the 8-tuple depends on BOTH the §3.9 amendment ratification AND the Ingest 7-tuple LOCK (which itself depends on the QC Pre-flight 6-tuple LOCK). Encoded additively (`minItems: 5`, `prefixItems` positions 0–7, `maxItems: 8`, `items: false`) so it accepts the 5/6/7/8-tuple while rejecting a 4-tuple. A `TODO@cross-spec-3.9-ratification` flips `minItems` to 8 only after the chain of gates closes. — see §5 + Open Questions.
- `edit_plan_class` — enum (`primary_9x16` for v1.0 · `variant_cutdown` reserved for v1.1 multi-variant auto-gen).
- `plan_evidence_hash` — SHA-256 over the `edit_plan` + `brand_edit_check` block (forensic, tamper-evident plan).
- `render_dispatched` — `const false` in v1.0 (Edit Director authors a plan, never renders; flips relevance at Editor, position 11). Honest provenance that no media was produced.
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.

### §3.4 errorEnvelope code namespace (target 7–9 LOCKED on Day 59/60 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `upstream_ingest_not_passed` | Ingest `verdict != pass` / not `successAssetManifest` with no Lever-3 sign-off | 1 | Halt — Edit Director never directs an un-ingested reel. |
| `upstream_not_success` | the consumed Asset Manifest is `errorEnvelope` | 2 | Halt — cannot direct a failed ingest output. |
| `incomplete_shot_coverage` | `coverage_complete != true` OR `missing_shots != []` | 3 | Hard FAIL — cannot author a cut over a hole; route back to Ingest. |
| `beat_map_unmappable` | a delivered shot has no resolvable Script/Storyboard beat (or vice versa) | 4 | Cut-order cannot be derived; route back to Ingest (asset gap) or operator (intent drift). |
| `duration_envelope_breach` | planned `total_duration_ms` outside the brief's 45–75s band | 5 | The cut can't fit the band even after trim; surface trim options. |
| `brand_edit_rule_conflict` | a required edit choice violates a NON-NEGOTIABLE brand rule with no auto-resolution (e.g. only-coherent-cut needs a fade) | 6 | Hard FAIL — brand-edit firewall; `detail` names the rule + the conflict. |
| `caption_spec_violation` | authored caption line cannot meet ≤22 chars / ≤2 lines without losing meaning | 7 | Verdict = fail; `detail` names the offending line. |
| `edit_plan_firewall_breach` | a banned-entity token appears in an AUTHORED lower-third / caption / end-card (9th pass, self-authored surface) | 8 | Hard FAIL — brand-safety on text Edit Director itself wrote; forensic-log the field. |
| `plan_lineage_failure` | malformed parent_chain / broken n-tuple lineage | 9 | Forensic — audit-trail break. |
| `edit_director_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 59/60 LOCK:** 7–9 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping.

---

## §4. Tier Constraints & Mode Coverage

**Per-tier gate access (Edit Director is universal-access, tier-sensitive in richness — restated for defense-in-depth pass 9):**

| Tier | Reaches Edit Director? | Cut beats | B-roll | Music swells | Variants | Caption rule | Cost |
|------|-----------------------|-----------|--------|--------------|----------|--------------|------|
| Pilot | **YES** | ≤8 | ≤3 | 1 | 3 | burn-in MANDATORY | ~$0.00 |
| Starter | **YES** | ≤8 | ≤3 | 1 | 3 | burn-in MANDATORY | ~$0.00 |
| Pro | **YES** | ≤12 | ≤6 | 2 | 4 | optional | ~$0.00 |
| Enterprise | **YES** | ≤12 | unlimited | 3 | 5 | optional | ~$0.00 |

**Why universal access + tier-sensitive richness (the difference from Ingest's tier-flat posture):** Ingest is a *technical gateway* — a file is valid or it isn't, regardless of tier, so its checks are tier-flat. Edit Director is a *creative authority* whose output richness IS a sold tier feature: a Pilot reel gets a clean, disciplined 8-beat cut with mandatory burn-in captions; a Enterprise reel gets a 12-beat cut with unlimited b-roll, 3 music swells, and 5 platform variants. The richness ladder is inherited verbatim from the Script Agent tier table (Day 9) so the edit honors the same envelope the script was written into. **Plan richness scales with tier; brand-rule compliance does NOT** — every tier gets hard-cuts-only, one-emotional-beat, the end-card, and the internal-question CTA.

**No cost-ledger authority (the inherited discipline):** Edit Director does **NOT** re-run the cumulative cost ledger (QC Pre-flight's authority) or re-validate assets (Ingest's authority). It is two gates downstream of cost enforcement and one gate downstream of asset validation; re-litigating either would be redundant and risk a double-fail on a reel already cleared. Edit Director's authority is **creative direction**, full stop.

**Mode coverage (mode-BLIND — the convergence payoff):**

| Mode | What Edit Director sees | Mode-specific note |
|------|--------------------------|--------------------|
| A (human footage origin) | The SAME mode-agnostic Asset Manifest | Edit Director cannot tell, and does not need to know, that these shots came from a videographer. `production_mode` is NOT read as a branch. |
| B (rendered + replicated origin) | The SAME mode-agnostic Asset Manifest | Identical authoring path. |
| C (replicated hot-path origin) | The SAME mode-agnostic Asset Manifest | Identical authoring path. |

**Mode-blind guarantee (the core §4 contract):** Edit Director asserts `mode_blind_confirm.production_mode_read == false` in every output — a self-attestation that it authored the plan without consulting the origin mode. This is the live, machine-checkable proof that Ingest's mode-convergence seam holds: if Edit Director ever NEEDED to branch on mode, the convergence contract would be broken upstream. By construction it never does. **Edit Director is the first agent in the 17-agent fleet for which the mode columns of this table are identical — that identity IS the deliverable Ingest unlocked.**

---

## §5. Process Steps (System Prompt Skeleton — Day 59 §7 will LOCK)

The agent runs an **11-step direction loop** per invocation (mirrors the AI Video Gen / Style Replication / QC Pre-flight / Ingest 11-step process pattern). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope.

**Step 1 — Verify Ingest precondition + parse input**
- Read the Ingest `asset_manifest.json`. Confirm `output_type == "successAssetManifest"` AND `verdict == "pass"` (or Lever-3 sign-off attached). Otherwise → halt with `upstream_ingest_not_passed`.
- Parse input JSON against `input.schema.json` (Day 59/60 LOCKED). There is NO mode branch — assert the manifest is the mode-agnostic shape.
- Confirm the consumed manifest is the success branch. Any `errorEnvelope` upstream → halt with `upstream_not_success`.

**Step 2 — Lineage integrity**
- Validate `metadata.parent_chain` is a well-formed 7-tuple inbound (5/6-tuple accepted additively until the §3.9 amendment + Ingest 7-tuple LOCK). Malformed → `plan_lineage_failure`.

**Step 3 — Coverage + mappability confirm (defensive)**
- Re-confirm `coverage_check.coverage_complete == true` AND `spec_check.missing_shots == []`. Violation → `incomplete_shot_coverage` (route back to Ingest).
- Resolve every `asset_bundle.raw_footage[].shot_ref` against the Script/Storyboard beat map. Unresolvable in either direction → `beat_map_unmappable`.

**Step 4 — Defense-in-depth firewall pass (ninth time, AUTHORED-text layer)**
- This step runs AFTER the plan text is drafted (Steps 5–9) and re-runs over every field Edit Director itself authored: every `lower_thirds[].content`, every `caption_lines[].text`, and the `end_card.line`, with the canonical entity-firewall regex (Cross-SPEC §3 drift #10): `Holdco | Principal | NPOX | 4821 | 6315 | SLN | Retail Supply | Nonprofit Leader A | Community Nonprofit | Nonprofit Leader B | Nonprofit Leader C`.
- Hard FAIL → `edit_plan_firewall_breach` + forensic log naming the authored field. **This is a NEW firewall surface:** Edit Director is the first agent that WRITES copy into the reel (lower-thirds, caption lines, end-card) rather than only passing through upstream text — so it must firewall its OWN authorship, not just inherit the manifest's clean status.

**Step 5 — Cut-order authoring**
- Map the Script's hook→3-beat→CTA structure onto the available `raw_footage[]` shots, honoring Storyboard frame-language per shot. Assign `in_ms`/`out_ms` against each shot's declared `duration_sec`.
- Honor the structure windows: hook 0:00–0:08, body 3 beats, CTA in the 0:55–1:05 band.

**Step 6 — Pacing + rhythm authoring**
- Derive `pacing_bpm` + `cut_rhythm` from the Script `voice_pacing` (165wpm → operator-peer rhythm). Apply the one-text-reveal-per-8s ceiling and the one-emotional-beat rule. Whip-pans/shake/jump-cut-comedy are forbidden (Alux motion canon).

**Step 7 — Caption + lower-third authoring**
- Lay the Script caption copy onto the cut at ≤22 chars/line, ≤2 lines on screen, burned-in lowercase sans (Pilot/Starter mandatory; Pro/Enterprise optional). A line that can't fit without losing meaning → `caption_spec_violation`.
- Schedule lower-thirds: lowercase, left-aligned, subtle underline, NEVER all-caps screamers; content from the Script on-screen-text blocks.

**Step 8 — Music-bed + swell authoring**
- Select the `music_bed` from the Asset Manifest; author the `music_swell_map` (count per tier: 1 Pilot/Starter, 2 Pro, 3 Enterprise). Ambient/cinematic under only — no pop, no trending audio (brand rule). (Loudness/LUFS is Sound's domain — NOT set here.)

**Step 9 — End-card + structure/brand check**
- Insert the mandatory end-card: "REINVENTED — build on purpose." serif display, centered, 1.5s hold, doubles as thumbnail.
- Run `structure_check` (hook window, 3 body beats, internal-question CTA, total duration in the 45–75s band) and `brand_edit_check` (hard-cuts-only, one-text-reveal-per-8s, one-emotional-beat, lower-thirds lowercase-left, captions within char limit, no reel-level sales CTA, end-card present).
- Duration out-of-band after trim → `duration_envelope_breach`. A non-negotiable brand rule that cannot be satisfied → `brand_edit_rule_conflict`. A soft-rule tension needing a creative call → `verdict: revise` (held for Lever-3, NOT silently overridden).

**Step 10 — Construct plan payload**
- If all green: build `successEditPlan` per §3.1 with the full `edit_plan` + `structure_check` + `brand_edit_check` + `verdict: "plan_ready"` + `handoff_targets: ["editor-agent"]`.
- Compute `plan_evidence_hash` (SHA-256 over the edit_plan + brand_edit_check block — tamper-evident).
- Extend `parent_chain` to an **8-tuple** (append `edit_plan_id`), held additively per §3.3.
- Set `render_dispatched: false` (v1.0 honesty), `edit_plan_class: "primary_9x16"`, `mode_blind_confirm.production_mode_read: false`, `human_review_required: true` per Lever-3 default.

**Step 11 — Emit + handoff**
- Validate output payload against `output.schema.json` (Day 59/60 LOCKED). Hard FAIL → forensic log + halt (output should always validate; failure here = agent bug).
- Emit JSON to stdout (paste-and-run runbook) OR persist to platform path / the Notion Edit Plan block per runtime environment (Blueprint §7 I/O: Edit Director writes a Notion Edit Plan block).
- On `fail`, set `route_back_to` per the §3.2 verdict↔route map so the Orchestrator can re-enter the pipeline at the correct agent.

**Anti-patterns Step 11 prevents (Lock-time discipline mirror from Ingest / QC Pre-flight §11):**
- No markdown fences around output JSON.
- No `print()` statements before the output JSON block.
- No engine credentials referenced; no media render dispatched (v1.0 authors a plan only — `render_dispatched` is `const false`).
- No absolute URLs in any `cut_order[].asset_uri` echoed into the plan (Hard Rule #8 inherit).
- No `plan_ready` verdict emitted while any structure or brand-edit check is unresolved (must be `fail` or `revise`).
- No reading of `production_mode` as a branch discriminator (mode-blind by construction — `mode_blind_confirm.production_mode_read` must be `false`).
- **No operator-impersonation:** Edit Director emits `human_review_required: true` and a plan *recommendation*; it does NOT mark a reel "approved for cut" as a ratified state — that is the Lever-3 operator action (or a future Orchestrator auto-dispatch).

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 59 + 60)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 59 partial 1. Pattern source: Ingest §6 / QC Pre-flight §6. Target 10–12 checks bipartite-covering the 7–9 errorEnvelope codes. Slot 11 reserved for `edit_director_agent_failed` per Cross-SPEC §3.6 slot-naming canon. Checks span: coverage confirm · cut-order completeness · duration-in-band · one-text-reveal-per-8s · one-emotional-beat · hard-cuts-only · caption char-limit · lower-third case/align · end-card present · internal-question CTA · authored-text firewall · mode-blind self-attestation.
- **§7 System Prompt v1.0** — Day 59 partial 1. Frame + hard rules + universal-tier-with-richness table + 11-step direction loop verbatim from §5 + the Blueprint §4.9 `edit_plan` target shape inlined + the REINVENTED brand-edit ruleset (§7–§11 of the brand intake) as the enforced rule surface. ~12–14 KB target. Hard Rules mirror Ingest with Edit-Director-specific tightening on "author-a-plan-never-render," "mode-blind," and "recommend-don't-approve" Lever-3 discipline.
- **§8 Performance Targets** — Day 60 partial 2. 9 metric categories. Schema validity 100% / brand-edit-rule catch 100% (a fade/wipe/zoom must never survive) / authored-text firewall catch 100% / duration-in-band 100% / false-plan-ready rate 0% target / false-fail rate ≤ 8% (over-flagging a creative tension to `revise` is the acceptable failure direction) / p50 latency 30s / p95 90s (reasoning + plan authoring) / zero engine cost.
- **§9 Test Fixtures** — Day 60 partial 2. 5-fixture portfolio: TC-01 clean Mode-origin-A→manifest Pro PASS (full plan) · TC-02 Mode-origin-C Enterprise PASS (proves mode-blind: byte-identical authoring path to TC-01 despite different origin) · TC-03 `incomplete_shot_coverage` → fail + route to Ingest · TC-04 `brand_edit_rule_conflict` (a beat that can only resolve with a fade → hard FAIL) · TC-05 `edit_plan_firewall_breach` (banned token authored into a lower-third — the 9th-pass self-authored catch). 5 of 7–9 codes exercised; remainder in schema-only fixtures. TC-01/TC-02 carry the **mode-blind convergence proof** (the Edit-Director analog of Ingest's mode-convergence proof).
- **§10 Field Map** — Day 59 partial 1. ~26 rows · passthrough vs transform vs derived. Manifest→cut_order map + Script→caption/pacing map + Storyboard→frame_language map + derived structure/brand-check map.
- **§11 Cost Model** — Day 60 partial 2. Zero engine snapshot (reasoning + plan authoring only; no render in v1.0). Directed-coherence value model (economic justification = brand-compliant cut on the first pass, no wasted edit cycles, no post-Motion brand-defect surfacing).
- **§12 Verdict Math** — Day 60 partial 2. PLAN_READY = (Ingest precondition met) ∧ (coverage complete) ∧ (beat map fully mappable) ∧ (cut order covers structure) ∧ (duration in band) ∧ (all brand-edit rules satisfied) ∧ (captions within char limit) ∧ (authored-text firewall clean). Any single ∧-term false → fail/revise per §3.2. Soft-rule tension → `revise` (operator creative call), hard-rule violation → `fail`. Deterministic on the hard rules; `revise` is the only judgment slot.
- **§13 Critical Decisions LOCKED** — Day 60 partial 2. Target 10–14 LOCKED decisions. Pre-scaffolded list:
  1. Plan-authoring vs render scope — v1.0 = edit-PLAN authoring ONLY; actual cut execution is Editor (position 11), human-in-the-loop at launch. [LOCKED-as-drafted Day 58]
  2. Universal access + tier-sensitive richness — all 4 tiers reach Edit Director; plan richness scales by tier, brand-rule compliance does not. [LOCKED-as-drafted Day 58]
  3. Mode-blind by construction — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested. [LOCKED-as-drafted Day 58]
  4. Ingest-pass precondition — Edit Director runs only on a `successAssetManifest`/`pass` (or Lever-3 approved) reel; otherwise halts `upstream_ingest_not_passed`. [LOCKED-as-drafted Day 58]
  5. No content re-authoring — Edit Director directs the ASSEMBLY of validated assets; it does NOT rewrite Script copy or re-frame Storyboard shots. [LOCKED-as-drafted Day 58]
  6. 8-tuple parent_chain — inherits Ingest 7-tuple + appends `edit_plan_id`; DOUBLY-deferred (depends on §3.9 amendment ratification AND the Ingest 7-tuple LOCK behind the QC 6-tuple). [DEFERRED — held additively at `minItems: 5`]
  7. errorEnvelope code count — 7–9 target. [PRELIMINARY · operator amend Day 60]
  8. Self-QC check count — 10–12. [PRELIMINARY · operator amend Day 60]
  9. Brand-edit-rule compliance = ZERO tolerance — a fade/wipe/zoom, an all-caps lower-third, a reel-level sales CTA, or a missing end-card must NEVER survive to `plan_ready`. [LOCKED-as-drafted Day 58]
  10. `revise` verdict for soft-rule tension — Edit Director surfaces a creative judgment call to Lever-3 (e.g. a 4th body beat vs one-emotional-beat) rather than silently overriding a brand rule. [LOCKED-as-drafted Day 58]
  11. No render, no engine — NO generative engine calls, NO media render in v1.0; `render_dispatched: const false`. [LOCKED-as-drafted Day 58]
  12. Recommend-don't-approve — Edit Director emits `human_review_required: true` + a plan recommendation; never flips a reel to a ratified "approved-for-cut" state. [LOCKED-as-drafted Day 58]
  13. Authored-text firewall (9th pass) — Edit Director firewall-scans the text it AUTHORS (lower-thirds, captions, end-card), a new surface no prior agent owned. [LOCKED-as-drafted Day 58]
  14. Multi-variant scope — v1.0 authors the primary 9:16 plan + flags variant count; auto-cutdown generation (1:1 LinkedIn) deferred to v1.1. [PRELIMINARY · operator amend Day 60]
- **§14 Calendar status updates** — Day 59 partial 1. Day 58 ✓ → trajectory populated.
- **§15 Change Log** — Day 60 partial 2. v1.0 lifecycle entries (outline-day-58 → body-day-59 → body-day-60 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 60 partial 2. Cross-SPEC §3.9 canonical fields + 5 Edit-Director additions (8-tuple parent_chain, edit_plan_class, plan_evidence_hash, render_dispatched, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `edit-director-agent` (kebab-case, matches the fleet pattern + Blueprint §4.9 handoff target) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `plan_evidence_hash` SHA-256 over the edit_plan + brand_edit_check block |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ Edit Director consumes the accumulated surface as read-only context; it contributes its own brand-edit predicates downstream |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-BLIND table — the first agent for which the mode columns are identical (the convergence payoff) |
| §3.6 Slot 11 naming canon | ✅ Reserved `edit_director_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Consumed shapes respected; Edit Director's own predicates snake_case |
| §3.8 Tier↔mode firewall (9th defense-in-depth) | ✅ Step 4 AUTHORED-text firewall (new surface) + §4 universal-tier-with-richness table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 8-tuple, held additively. **Doubly-deferred** — gated on the §3.9 amendment ratification AND the Ingest 7-tuple LOCK (behind the QC 6-tuple). |
| §3.10 Cost ceiling authority | ✅ §4 explicitly DECLINES to re-litigate cost (QC Pre-flight's authority) or re-validate assets (Ingest's authority) — no double-enforcement; Edit Director is $0-cost |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 58 outline — 6 parked for operator amendment)

1. **Plan-only vs partial-EDL scope** — v1.0 authors the Edit Plan (cut order + creative direction); the executable EDL/timeline conform is Editor's job (human-in-loop at launch). Confirm v1.0 stops at the plan and does NOT emit a machine-conformable EDL. *(Donna recommends: confirm plan-only for v1.0 — the plan is the buildable, highest-leverage slice; the EDL emit lands when Editor automation ships Week 4–5.)*
2. **`revise` verdict existence** — should Edit Director carry a third `revise` verdict for soft-brand-rule creative tension (surface to Lever-3), or collapse everything into `plan_ready`/`fail`? *(Donna recommends: keep `revise` — a creative judgment call (e.g. a 4th emotional beat) is exactly the human-in-the-loop slot Lever-3 exists for; silently overriding a brand rule is the worse failure.)*
3. **8-tuple parent_chain** — triply-gated in effect (depends on the §3.9 amendment AND the Ingest 7-tuple LOCK AND the QC 6-tuple LOCK behind it). Edit Director is the first 8-tuple consumer — a third forcing function. *(Donna recommends: RATIFY the §3.9 amendment AS-DRAFTED so all 17 agents inherit n-tuple lineage; Edit Director holds additively until the chain closes.)*
4. **Editor handoff readiness** — Edit Director hands to a not-yet-built Editor (Agent #10 candidate). Should v1.0 emit the plan to a holding store (the Notion Edit Plan block, per Blueprint §7 I/O) until Editor ships, or assume direct handoff? *(Donna recommends: emit to the Notion Edit Plan block in v1.0; direct agent-to-agent handoff activates when Editor LOCKs — mirrors the Ingest→Notion-Asset-Manifest holding-store decision (Ingest Open Q4).)*
5. **Multi-variant authoring** — v1.0 authors the primary 9:16 plan and flags `variants_planned` count; should the 1:1 LinkedIn cutdown plan be auto-authored in v1.0 or deferred? *(Donna recommends: defer auto-cutdown to v1.1 — author the primary 9:16 + flag the count; a cutdown is a derived re-plan, lower-leverage than the primary.)*
6. **Pacing-bpm derivation** — `pacing_bpm` is derived from the Script `voice_pacing` (165wpm) + the music bed's declared tempo; with no byte-level audio analysis in v1.0, is declared-tempo + wpm-heuristic an acceptable basis? *(Donna recommends: ratify declared-tempo + wpm-heuristic for v1.0 — beat-detected sync needs decode (v1.1), same posture as Ingest's declared-spec-only adjudication.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (full Edit Director trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 58 | Tue Jun 16 | **SPEC outline §0–§5** [SHIPPING NOW] | Ingest Day 48 outline |
| 59 | Wed Jun 17 | SPEC body partial 1: §6 + §7 + §10 + §14 | Ingest Day 51 / QC Pre-flight Day 41 |
| 60 | Thu Jun 18 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | Ingest Day 52 / QC Pre-flight Day 43 |
| 61+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | Ingest Day 53–57 / QC Pre-flight Day 44–47 |
| 63 | Sun Jun 21 | **REST DAY** — no build (pre-stage next scaffold only) | Day 21/28/35/42/49/56 Rest Day compounding |

**Sprint context:** Edit Director is **Agent #9** — the second post-production agent and the first creative-authoring agent in the post tail, the 9th defense-in-depth firewall (authored-text layer) and the **first contractually mode-blind agent** (the live proof of Ingest's convergence seam). The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) shipped on the six production agents through the QC Pre-flight gate; Edit Director v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the Ingest, QC Pre-flight, and Style Replication outlines were (while their LOCK ceremonies remain operator-gated).

---

## Files produced today (Day 58)

- `ars/ARS-2026-06-16-Day-58-Edit-Director-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-06-16.md` — Day 58 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 58)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked. No media render, no byte-level decode. (Edit Director by design authors a plan and renders no pixels in v1.0 — appropriate for a creative-direction agent.)
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no client/investor outreach. The end-of-run status iMessage to Jamila ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business. (Notification-channel status carried — see build log.)
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, zero $ spent.
- ✅ **No operator-impersonation.** AI Video Gen / Style Replication / QC Pre-flight / Ingest LOCK ceremonies NOT assumed — all four confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Ingest Day 53 Items 6/8/11 + the Day 57 runbook execution NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. Edit Director v1.0 LOCK will hard-gate itself on the upstream LOCKs (especially the Ingest 7-tuple) being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 4 enumerates HC/NPOX tokens precisely so the agent can BLOCK them at the authored-text layer — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Ingest Day 48 outline structure inherited verbatim. Orchestration Blueprint §1.2 / §2 / §4.8 / §4.9 / §7 (Agent 10 Edit Director definition) + Cross-SPEC §3 canon + Brand-Voice Intake §7–§11 used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-58 build runs Tuesday (Pacific). Next Rest Day: Day 63 (Sun Jun 21 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 58 ships clean. Day 59 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). Edit Director is Agent #9 of 17 — the 9th defense-in-depth firewall (authored-text layer) and the first creative-authoring agent in the post tail, the first contractually mode-blind agent and therefore the live proof that Ingest's mode-convergence seam holds end-to-end. Operator pickup: (1) the four predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight + Ingest) remain pending and gate Edit Director's eventual v1.0 LOCK — the Ingest 7-tuple in particular is Edit Director's direct 8-tuple dependency; (2) review the §13 critical-decisions list + ratify the Cross-SPEC §3.9 n-tuple amendment so the n-tuple parent_chain is canon; (3) confirm the Agent #9 = Edit Director selection (or re-assign the slot) at the Ingest LOCK-ceremony close.*
