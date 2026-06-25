# ARS — Editor Agent v1.0 SPEC OUTLINE (§0–§5)

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Authored:** Day 66 · Wed Jun 24, 2026 (Pacific) · overnight build session (Donna)
**Deliverable class:** Forward SPEC outline §0–§5 (the head-start design for Agent #10 of 17)
**Status:** OUTLINE ONLY — no LOCK, no schema, no SKILL bundle. Body partials author Days 67 + 68 per the calendar in §0.
**Pattern source:** Edit Director Day 58 outline (`ARS-2026-06-16-Day-58-Edit-Director-Agent-SPEC-Outline.md`) — section structure inherited verbatim. Orchestration Blueprint §1.2 (Agent 11 row: *"Executes the cut per Edit Director's plan. Outputs v1 edit."*), §2 swim-lane, §4.9 (Edit-Director→Editor payload), §4.10 (Editor→Sound payload), §6 dispatch table (row 11: *"On Edit Director handoff · Per reel · Edit plan + assets"*), §7 read/write contract (Editor reads *Edit Plan + raw assets*, writes *Drive `/reels/[reel_id]/v1.mp4`*), §9 build-checklist (*"11 Editor — Human-in-the-loop for Week 2 (agent drafts EDL, human executes in editor app). Full automation Week 4–5."*) used as the grounding spine. Brand-edit rules grounded in `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7–§11.

> **Agent-selection note (Donna, surfaced not hidden):** The Day 65 Edit Director LLM-Test-Runbook close named the next forward deliverable as **"Editor Agent #10 SPEC outline (position 11 in the pipeline; the FIRST agent that actually renders/cuts pixels — it consumes Edit Director's `plan_ready` Edit Plan)."** That selection is followed here. The Edit Director v1.0 LOCK ceremony itself is **operator-only** (it joins AI Video Gen / Style Replication / QC Pre-flight / Ingest in the pending-LOCK queue) — Donna does NOT advance it. This outline is the forward-design head-start, authored on the same forward-looking basis the Ingest, QC Pre-flight, Style Replication, and Edit Director outlines were while their LOCK ceremonies remained operator-gated. Rationale for Editor as the #10 build: (1) **strict dependency order** — Editor is the immediate runtime stage downstream of Edit Director (Blueprint §6: *"On Edit Director handoff"*), consuming the `successEditPlan` Edit Director authors; (2) **fleet-unblock** — nothing downstream (Sound → Motion → full QC) can run without a conformed v1 edit; Editor is the gate that turns a *plan* into an *executable cut*; (3) **the inflection the whole fleet was built toward** — Editor is the FIRST agent whose output is destined for a **media file** (`v1.mp4`), the agent where eight upstream stages of validated planning finally meet the timeline; its outline establishes the *executor* pattern (the EDL/conform seam) the rest of the render tail (Sound/Motion) inherits; (4) **second mode-blind agent** — it inherits Edit Director's mode-agnostic lineage, the continued proof that Ingest's convergence seam holds two stages deep. Operator may re-assign the #10 slot at the LOCK-ceremony close.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 10 — Post-production assembly layer (edit plan → conformed cut) |
| Agent index | **#10 of 17** (build sequence — continues the Edit Director Day 58 "agent #9 of 17" framing) |
| Runtime pipeline position | **11 — Editor** (executes the cut per Edit Director's plan: conforms the cut_order to a frame-accurate EDL/timeline, lays caption + lower-third + end-card events, places the music bed, emits the v1 edit); receives the Edit Plan + raw assets from Edit Director, hands the v1 edit + EDL to Sound |
| Pipeline tier | POST-PRODUCTION ASSEMBLY (first *executor* agent in the post tail; the first agent whose output is destined for a media file — the v1.mp4) |
| Mode coverage | **Mode-blind by inheritance** — consumes the mode-convergent Edit Plan (itself authored from the mode-agnostic Asset Manifest); never sees `production_mode` as a branch discriminator. The **SECOND** contractually mode-blind agent (Edit Director was the first); the continued live proof that Ingest's convergence seam holds two stages deep. |
| Predecessor SPEC (gate) | `ARS-2026-06-19-Day-61-Edit-Director-Agent-v1-LOCK-CANDIDATE.md` (Day 61 LOCK candidate — operator-gated). Editor runs only on an Edit-Director-passed (`successEditPlan`, verdict `plan_ready`, or a `revise` plan with Lever-3 sign-off attached) reel. |
| Predecessor schemas | `ARS-2026-06-20-Edit-Director-output.schema.json` (Day 62) — the `edit_plan` block (`cut_order` + `caption_lines` + `lower_thirds` + `transitions` + `music_bed` + `music_swell_map` + `end_card`) consumed as the primary INPUT. Plus the Ingest `output.schema.json` (Day 54) `asset_bundle` (the raw `asset_uri`s the EDL references) consumed as the media-resolution input. |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape (§3.3/§3.8), metadata block + n-tuple parent_chain (§3.9) all inherited |
| Brand-edit canon | `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (visual identity / motion / lower-thirds), §8 (reel format specs: 9:16 · 1080×1920 · 30fps), §11 (caption spec) — the format + brand-event rules the EDL must conform to byte-faithfully |
| Defense-in-depth layer | **10th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → **Editor**) — the **commit-time** firewall: it is the agent that COMMITS the authored text (captions, lower-thirds, end-card) to the executable cut spec, so it re-scans that text one final time before it can hit a renderer. NOT a new authorship surface (Editor authors no copy — all text is Edit Director passthrough); it is a **passthrough-integrity + commit-time** re-scan (the last text checkpoint before pixels). |
| Lever inheritance | Reads `lever_state` from upstream `metadata`; emits `human_review_required: true` per Lever-3 default AND per the v1.0 human-in-the-loop conform posture (Blueprint §9). The EDL is a *draft a human executes* in v1.0 — Editor never marks a cut "rendered" or "approved"; the operator (or Week 4–5 automation) conforms. |
| Pricing tier authority | **ALL tiers** — Pilot · Starter · Pro · Enterprise. Every reel needs a conform. **Tier-FLAT in its own logic** (unlike Edit Director, which is tier-sensitive in richness): Editor faithfully conforms whatever richness the Edit Plan specifies — it does not scale its own behavior by tier (it inherits the plan's tier envelope and executes it). The `tier_richness` block is read for variant-count awareness only; v1.0 conforms the primary 9:16 (variant EDLs deferred to v1.1). |
| Cost authority class | **Near-zero (ties Ingest / QC Pre-flight / Edit Director for lowest in fleet) IN v1.0** — pure reasoning + EDL/conform-spec authoring over the Edit Plan + asset bundle. **No generative engine calls, no media render, no byte-level decode in v1.0** — Editor v1.0 drafts the EDL; the human executes the conform in the editor app (Blueprint §9 Week-2 posture); full render automation is Week 4–5 (v1.1). Effective per-reel cost ≈ $0.00. `render_dispatched: const false` in v1.0 — the render flips relevance at Editor, but in v1.0 it is the HUMAN who renders, not the agent. |

**Build calendar (Week 10 — Editor trajectory, mirrors the proven 8-day agent-build cadence):**
- **Day 66** (today, Wed Jun 24 · Wk10) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 67 (Thu Jun 25 · Wk10) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 68 (Fri Jun 26 · Wk10) — SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16
- Day 69+ (TBD) — LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK (pattern: Edit Director Day 61–65 / Ingest Day 53–57)
- Day 70 (Sun Jun 28 · Wk10) — **REST DAY** (no build; pre-stage next scaffold only, per the Day 21/28/35/42/49/56/63 Rest Day-compounding pattern)

> **Rest Day honesty:** This Day-66 build runs Wednesday (Pacific) — building is allowed. The next Rest Day is Day 70 (Sun Jun 28 Pacific) per the Day 65 log close. The UTC clock may have rolled past midnight at author time, but the sprint labels by Jamila's Pacific date (Wed Jun 24) — the same convention noted in prior logs.

> **Sequencing honesty:** The 42-day sprint's headline deliverable — the Mode B Pro single-reel **commercial demo** (Day 42 target, now past) — shipped on the six launch-critical production agents threaded through the QC Pre-flight gate. Editor is the third *post-production* agent (after Ingest + Edit Director); its v1.0 build proceeds inside the **post-launch hardening window** and does **not** gate the launch demo. This outline is the forward-design head-start so the render tail is buildable in dependency order once the production-tier + Ingest + Edit Director LOCKs close.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Editor Agent** is the **executor of post-production** — the moment a reel stops being a *directed plan* and becomes an *assembled cut*: the cut_order resolved to frame-accurate timeline events, the captions and lower-thirds laid against the real media, the music bed placed, the end-card committed — a single conformable Edit Decision List (EDL) the editor app (human in Week 2, automation in Week 4–5) executes into the v1 edit file. It is the first agent in the fleet whose job is to **execute** rather than to **decide** or **validate**, and the first whose output is destined for a **media file**.

Where the nine upstream agents authored intent, adjudicated correctness, and directed the assembly, Editor *conforms*:
- Brief / Script / Storyboard = intent + content authoring (what the reel SAYS and how it's shot)
- Production Coord = logistics (mode, vendor, budget)
- AI Video Gen / Style Replication = render + brand-finish (the pixels exist)
- QC Pre-flight = ship-safety (the reel is brand-safe + format-correct)
- Ingest = asset-readiness (the files are present, valid, in-sync — one mode-agnostic Asset Manifest)
- Edit Director = edit-plan authoring (the directed cut: order, pacing, captions, lower-thirds, music, transitions, end-card)

The Editor Agent picks up at the Edit Plan and conforms the cut:
- **Editor Agent = cut conform ("Given a `plan_ready` Edit Plan and the resolved raw asset bundle, produce a single frame-accurate, gap-free, brand-faithful EDL — every cut event mapped to a real `asset_uri` with in/out timecodes inside the declared media duration, every caption/lower-third/end-card event time-placed exactly as the plan directs, the music bed conformed, the hard-cuts-only transition policy enforced at the timeline layer — that the editor app executes beat-for-beat into the v1 edit, with NO creative re-interpretation of the plan.")**

**Single-responsibility line (LOCKED on intent):**
> *"Post-production executor. Receives the Edit-Director-passed Edit Plan (`successEditPlan`, verdict `plan_ready`, or a `revise` plan with Lever-3 sign-off) plus the resolved raw asset bundle, and conforms one canonical EDL — frame-accurate cut events (`asset_uri` + in/out timecodes bounded by declared media duration, gap-free, no double-spend), caption/lower-third/end-card event placements (timing + content faithful to the plan, NOT re-authored), music-bed placement, and the hard-cuts-only transition policy enforced at the timeline — that the editor app executes into the v1 edit file. Authors the EDL only; renders NO pixels and conforms NO media in v1.0 (the human/automation executes the render); calls no generative engine. Faithfully executes the plan — it makes NO creative decisions, re-authors NO copy, re-orders NO cuts. Emits a recommendation (`human_review_required`) — never a ratified 'rendered' or 'approved' state."*

**Why this agent's reason-to-exist is the execute/decide boundary (Blueprint §1.2):** Edit Director *decides* the cut; Editor *executes* it. The separation is the same production-discipline boundary every editorial pipeline draws between the director's intent and the editor's conform: the director must not be re-litigating cuts on the timeline, and the editor must not be overriding the director's plan. **This is Donna's design thesis for building Editor as Agent #10: it is the first faithful-executor agent, and the structural proof that the plan→cut handoff is clean — if Editor can produce a complete, conformable EDL from the plan alone, with zero creative re-interpretation, the plan was buildable and the executor seam holds.** A `plan_unbuildable` outcome (a cut event that cannot map to a real asset, a timecode that exceeds the declared duration) is the signal that the plan or the manifest was wrong — and it routes back, it never silently "fixes" the plan.

**Pipeline position (per Orchestration Blueprint §2 swim lane):**
```
... → EDIT DIRECTOR (edit-plan authoring) →
   [successEditPlan · verdict = plan_ready]
        │
        ▼  [Edit Plan: cut_order + pacing + captions + lower_thirds + music_bed + transitions + end_card]
   EDITOR (cut conform → EDL)
        │
        ▼  [EDL + v1 edit: frame-accurate timeline · conform manifest · Drive /reels/[reel_id]/v1.mp4]
   12 Sound → 13 Motion → 14 QC (full)
        │
   [edl_unbuildable] → route back to Edit Director (plan defect) or Ingest (asset gap)
```

**Why an executor agent distinct from the upstream creative agents (the boundary question):** Edit Director already authored the cut_order + caption copy + lower-third schedule + music swell map — so what does Editor add? A clean separation across the *decide→execute* boundary:
1. **Edit Director authors the PLAN-TO-CUT** — the directed assembly: which shots, in what order, with what timing, captions, music, transitions. It produces a *plan*, not a *timeline*. It works in plan-space (millisecond intentions against declared durations), not media-space.
2. **Editor authors the CONFORM** — given the plan and the *resolved* assets, the concrete EDL: every cut event bound to a real `asset_uri`, every in/out timecode validated against the asset's *declared* media duration (not just the plan's intended out_ms), every text event placed on the timeline, the music bed conformed, the transition policy enforced at the cut-list layer. It produces the executable artifact the editor app runs.
3. **The two phases catch different problems.** Edit Director can direct a 5000ms cut of shot-003; only Editor, resolving the real asset, can discover that shot-003's declared media is only 4200ms and the plan's out_ms exceeds the available media — and route back rather than render a black-frame gap. Editor does NOT re-direct (it trusts the plan's order, pacing, and copy); it *conforms the directed plan against the resolved media* and surfaces any mismatch.

The actual pixel render (executing the EDL into the v1.mp4, frame-accurate trims, the timeline conform in the editor app) is, in v1.0, a **human** action (Blueprint §9: *"Human-in-the-loop for Week 2 — agent drafts EDL, human executes in editor app"*); full render automation is targeted Week 4–5 (v1.1). v1.0 Editor authors the *EDL + conform manifest*; it produces no media file itself. **`render_dispatched` finally becomes the relevant field at this agent (Edit Director's schema flagged that it "flips relevance at Editor, position 11") — and in v1.0 it is STILL `const false`, because Editor drafts the EDL and the human conforms.** This is the human-in-the-loop seam, made explicit and honest.

**Hand-off contract enforced:**
- **PRECONDITION:** Editor reads the Edit Director `edit_plan.json`. If `output_type != "successEditPlan"` OR `verdict not in {plan_ready}` (and no Lever-3 human sign-off is attached to a `revise` plan) → halt with `upstream_plan_not_ready`. Editor never conforms a reel whose plan did not pass Edit Director. A `fail` (errorEnvelope) plan → halt `upstream_not_success`.
- **INPUT contract:**
  - The Edit Director `successEditPlan` — `edit_plan` (`cut_order[]` with `shot_ref` + `asset_uri` + `in_ms`/`out_ms`, `caption_lines[]`, `lower_thirds[]`, `transitions` const, `music_bed`, `music_swell_map[]`, `end_card`), `tier_richness`, `mode_blind_confirm`, the `plan_evidence_hash`.
  - The **resolved raw asset bundle** (the Ingest `asset_bundle.raw_footage[]` `asset_uri` + `duration_sec` per shot) — the media-resolution reference the EDL's timecodes validate against.
  - The **denormalized upstream chain** in `metadata.parent_chain` (8-tuple inbound from Edit Director, triply-deferred) + accumulated `qc_pre_flags[]`.
- **OUTPUT contract:** Emits `edl.json` per §3 (polymorphic: `successEdl | errorEnvelope`). Sound reads the EDL + the v1 edit handle (Blueprint §4.10: *"v1 edit file + EDL"*) and adds VO polish, music-bed finalize, SFX, loudness — without re-deriving the cut.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| EDL authoring (cut events: `asset_uri` + in/out timecodes, gap-free, no double-spend, bounded by declared media duration) | Actual pixel render / timeline conform into v1.mp4 — human-in-the-loop in v1.0 (Blueprint §9); automation Week 4–5 |
| Frame-rounding of plan ms → frame boundaries (30fps grid; declared-duration math) | Sub-frame / audio-waveform-accurate trim — needs byte-level media decode |
| Caption/lower-third/end-card event placement (timing + content faithful to the plan) | Live caption-burn render + font rasterization — Motion domain (position 13) |
| Music-bed placement on the timeline (single bed + swell-map markers) | Loudness/LUFS normalization (−14 IG/TT, −16 YT) — Sound domain (position 12), needs decode |
| Hard-cuts-only transition enforcement at the EDL layer (zero dissolve/wipe/zoom events emitted) | Speed-ramp / morph-cut authoring (forbidden by brand rule regardless) |
| Commit-time firewall re-scan (10th pass) over the passthrough caption/lower-third/end-card text | New-text authorship (Editor authors NO copy — nothing to firewall but the passthrough integrity) |
| Conform manifest (the asset→timeline map + frame-rate/aspect target + duration check) | Multi-variant conform (1:1 LinkedIn EDL auto-gen) — v1.1 (v1.0 conforms the primary 9:16, flags variants) |
| Plan-fidelity check (EDL byte-faithful to the plan: order, copy, timing intentions) | A/B alternate-cut conform |
| 9-tuple parent_chain extension (inherits Edit Director 8-tuple + appends `edl_id`) | EDL-to-NLE-project export (Premiere/Resolve XML) — v1.1 conform-format adapters |
| EDL construction (CMX3600-faithful event list + JSON conform spec) + EDL recommendation | Render-farm dispatch / encode-ladder (the actual compute spend) — v1.1 automation |

**Pricing tier table (Editor is universal-access AND tier-flat in its own logic — defense-in-depth pass 10):**

| Tier | Reaches Editor? | Editor's own behavior | Cost | Conform note |
|------|-----------------|-----------------------|------|--------------|
| Pilot — Founding 5 | **YES** | Faithfully conform the plan (tier-flat executor) | ~$0.00 | conforms the plan's mandatory burn-in captions |
| Starter — Operator | **YES** | Faithfully conform the plan (tier-flat executor) | ~$0.00 | conforms the plan's mandatory burn-in captions |
| Pro — Studio | **YES** | Faithfully conform the plan (tier-flat executor) | ~$0.00 | conforms the plan's richer cut + swell map |
| Enterprise — Agency | **YES** | Faithfully conform the plan (tier-flat executor) | ~$0.00 | conforms the plan's richest cut; flags variant EDLs |

Editor adds **zero** generative cost to every tier envelope in v1.0. Its economic value is **faithful, frame-accurate, brand-faithful conform** — every reel's cut is assembled exactly as directed, every timecode validated against real media before an editor (or a renderer) burns a cycle, and a plan/asset mismatch is caught *before* the render rather than discovered in the v1 review.

---

## §2. Inputs

Editor has **one canonical responsibility** (conform the EDL) reached from **one** primary input shape — the mode-convergent Edit Plan. Like Edit Director (and unlike every production-tier agent), there is **no mode branch** and no source-polymorphism: this is the second agent whose input is structurally mode-blind. (It reads `tier_richness` for variant-count awareness only — it does not scale its own conform logic by tier.)

### §2.1 Precondition input — Edit Director Edit Plan verdict (gate)

**Always read first.** The Edit Director `edit_plan.json`:
```json
{
  "output_type": "successEditPlan",
  "verdict": "plan_ready",
  "reel_ref": { "edit_plan_id": "<uuid>", "asset_manifest_id": "<uuid>" },
  "edit_plan": { "cut_order": [ /* ... */ ], "end_card": { /* ... */ } },
  "brand_edit_check": { "hard_cuts_only": true, "end_card_present": true },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_manifest" },
  "human_review_required": true,
  "metadata": { /* 8-tuple parent_chain inbound, held additively */ }
}
```
**Hard validation:** `output_type == "successEditPlan"` AND `verdict == "plan_ready"` (OR `verdict == "revise"` with a Lever-3 sign-off attached). Otherwise → halt with `upstream_plan_not_ready`. A consumed `errorEnvelope` plan → halt `upstream_not_success`. Editor does not conform a reel whose plan failed Edit Director, and does NOT auto-resolve a `revise` plan (the soft creative call is the operator's — Editor inherits Edit Director's recommend-don't-approve discipline).

### §2.2 Primary input — Edit Plan block (the directed cut to conform)

**Required input fields (preliminary — full schema on the Day 67/68 partials):**
```json
{
  "edit_plan": {
    "cut_order": [
      { "shot_ref": "shot-001", "asset_uri": "ars://reels/REINVENTED-2026-W26-001/raw/shot_1.mp4", "in_ms": 0, "out_ms": 3000, "frame_language": "held-object-close-up" }
    ],
    "pacing_bpm": 120,
    "caption_style": "burn-in, lowercase sans, one line at a time, <=22 chars/line, ivory on ink",
    "caption_lines": [ { "at_ms": 0, "text": "your calendar doesn't lie", "line": 1 } ],
    "lower_thirds": [ { "at_ms": 25000, "content": "the operator's stack", "case": "lowercase", "align": "left", "style": "lt_authority_v3" } ],
    "transitions": "hard cuts only — zero fades, zero wipes, zero zooms (brand rule)",
    "music_bed": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav",
    "music_swell_map": [ { "at_ms": 48000, "type": "emphasis_swell" } ],
    "end_card": { "at_ms": 63500, "line": "REINVENTED — build on purpose.", "hold_ms": 1500, "doubles_as_thumbnail": true }
  },
  "tier_richness": { "tier": "pro", "cut_beats": 11, "variants_planned": 4 },
  "metadata": { /* Cross-SPEC §3.9 — tier, lever_state, brand_id, session_id, parent_chain (8-tuple inbound), qc_pre_flags surface */ }
}
```

**Hard validations on primary input (defense-in-depth pass 10):**
1. Upstream `output_type` is `successEditPlan`, NOT `errorEnvelope`. (errorEnvelope → `upstream_not_success`.)
2. `verdict == "plan_ready"` (or `revise` + Lever-3 sign-off). A bare `revise` with no sign-off → `upstream_plan_not_ready` (defensive — Editor cannot conform a held creative call).
3. Every `cut_order[].asset_uri` resolves against the Ingest `asset_bundle.raw_footage[]` (so each cut event binds to a real media handle). Unresolvable → `asset_unresolved`.
4. Every `cut_order[]` `out_ms` is `<= ` the resolved shot's declared `duration_sec * 1000` AND `out_ms > in_ms` (no over-spend past available media, no zero/negative duration). Violation → `timecode_out_of_range`.
5. `asset_uri`s remain platform-relative `ars://...` (Hard Rule #8 inherit — Editor echoes them into EDL events; it must not introduce an absolute URL). Violation → `asset_uri_integrity_failure`.
6. `metadata.parent_chain` is a well-formed 8-tuple inbound (5/6/7/8-tuple accepted additively — see §3.3). Malformed → `edl_lineage_failure`.

### §2.3 Media-resolution input — Ingest asset bundle (declared durations)

**Denormalized, read as the timecode-validation reference (not re-authored).** Editor reads:
```json
{
  "asset_bundle": {
    "raw_footage": [
      { "shot_ref": "shot-001", "asset_uri": "ars://reels/.../raw/shot_1.mp4", "duration_sec": 3, "source": "style-replication-agent" }
    ],
    "audio": ["ars://reels/.../raw/voice_track.wav"],
    "music_bed": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav"
  }
}
```
Used to validate every EDL cut event against the real declared media duration (the check Edit Director could not fully make in plan-space), to resolve `asset_uri` → media handle, and to confirm the music bed + voice track exist for the conform manifest. **Editor consumes these as fixed resolution facts — it validates the plan's timecodes against them; it does NOT re-decode media (no byte-level read — declared durations only, the same declared-spec posture as Ingest and Edit Director).**

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block: `tier`, `lever_state`, `brand_id`, `session_id`. Editor reads `tier_richness` for variant-count awareness (does v1.0 flag that this tier expects N variant EDLs? — yes, it flags the count; it conforms only the primary 9:16) and sets the EDL's `human_review_required: true` per Lever-3 default AND the v1.0 human-in-the-loop conform posture. It does **not** re-run cost, asset validation, or creative direction — those are QC Pre-flight's, Ingest's, and Edit Director's authorities respectively; Editor trusts the passed verdicts and the `plan_evidence_hash`.

---

## §3. Outputs (skeleton)

Editor emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 / QC Pre-flight Day 40 / Ingest Day 48 / Edit Director Day 58 output pattern (`oneOf [success branch, errorEnvelope]`).

### §3.1 successEdl branch (EDL conformed)

```json
{
  "output_type": "successEdl",
  "verdict": "edl_ready",
  "reel_ref": {
    "brand_id": "REINVENTED",
    "edit_plan_id": "<uuid>",
    "edl_id": "<uuid>"
  },
  "edl": {
    "frame_rate": 30,
    "aspect": "9:16",
    "resolution": "1080x1920",
    "events": [
      { "event": 1, "shot_ref": "shot-001", "asset_uri": "ars://reels/.../raw/shot_1.mp4", "src_in_ms": 0, "src_out_ms": 3000, "rec_in_ms": 0, "rec_out_ms": 3000, "transition": "cut" }
    ],
    "caption_events": [ { "at_ms": 0, "text": "your calendar doesn't lie", "line": 1 } ],
    "lower_third_events": [ { "at_ms": 25000, "content": "the operator's stack", "case": "lowercase", "align": "left" } ],
    "music_event": { "asset_uri": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav", "at_ms": 0 },
    "end_card_event": { "at_ms": 63500, "line": "REINVENTED — build on purpose.", "hold_ms": 1500 }
  },
  "conform_check": {
    "timeline_gap_free": true,
    "no_double_spend": true,
    "all_events_bounded_by_declared_duration": true,
    "frame_aligned": true,
    "total_timeline_ms": 65000,
    "duration_in_band": true
  },
  "plan_fidelity_check": {
    "cut_count_matches_plan": true,
    "caption_copy_byte_faithful": true,
    "lower_third_copy_byte_faithful": true,
    "end_card_byte_faithful": true,
    "transition_policy_hard_cuts_only": true,
    "plan_evidence_hash_verified": true
  },
  "edl_firewall_pass_10": { "status": "pass", "passthrough_text_fields_scanned": 14, "hits": 0 },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_edit_plan" },
  "render_target": { "render_dispatched": false, "conform_mode": "human_in_the_loop", "v1_edit_uri": "ars://reels/.../v1.mp4 (reserved — written by the human conform)" },
  "tier_richness_echo": { "tier": "pro", "variants_planned": 4, "variants_conformed": 1, "primary_aspect": "9:16" },
  "handoff_targets": ["sound-agent"],
  "metadata": { /* Cross-SPEC §3.9 with Editor additions per §3.3 — 9-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (EDL not buildable)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "timecode_out_of_range",
  "failed_check_id": 4,
  "attempts": 1,
  "route_back_to": "edit-director-agent",
  "reel_ref": { "edl_id": "<uuid>" },
  "cost_incurred_usd": 0.00,
  "detail": {
    "violation": "cut_order event 3 (shot-003) out_ms 5000 exceeds the resolved declared media duration 4200ms",
    "affected_events": [3],
    "recovery_path": "re-direct the cut to <=4200ms in the Edit Plan OR re-confirm the Ingest declared duration for shot-003"
  },
  "metadata": { /* Cross-SPEC §3.9 — 9-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `edl_ready` | EDL conformed + plan-faithful + brand-faithful; cleared into Sound (held in the human conform queue in v1.0) | `null` (forward to Sound) | All conform + fidelity + firewall checks green |
| `fail` | EDL unbuildable from current inputs | `edit-director-agent` (plan defect: timecode out of range, transition demand, fidelity break) OR `ingest-agent` (asset gap: unresolvable `asset_uri`) | A conform/resolution defect that the plan or the manifest must fix |

> **Defining divergence (surfaced):** Editor carries **2 verdicts** (`edl_ready | fail`) — it deliberately does NOT inherit Edit Director's success-side third `revise` verdict. Editor is a **faithful executor**, not a creative authority: there is no subjective conform surface for it to hold to Lever-3. A soft creative tension lives ONE stage upstream (Edit Director's `revise`); by the time a plan reaches Editor it is already `plan_ready` (or a Lever-3-signed-off `revise`). Editor either conforms it faithfully (`edl_ready`) or finds a hard plan/asset mismatch (`fail`). Re-introducing `revise` here would mean Editor was second-guessing a directed plan — exactly the override the decide/execute boundary forbids. (Mirror of the Ingest posture: a technical executor is deterministic; the judgment slot lives where the creativity lives.)

### §3.3 Metadata block additions (Editor-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **9-tuple** (inherits Edit Director's 8-tuple lineage + appends own `edl_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (DRAFTED Day 31 §16.3; **ratification still operator-pending**). **Triply-deferred** like Edit Director's, now a **fourth** forcing function: the 9-tuple depends on the §3.9 amendment ratification AND the Edit Director 8-tuple LOCK (which depends on the Ingest 7-tuple LOCK, behind the QC Pre-flight 6-tuple LOCK). Encoded additively (`minItems: 5`, `prefixItems` positions 0–8, `maxItems: 9`, `items: false`) so it accepts the 5/6/7/8/9-tuple while rejecting a 4-tuple. A `TODO@cross-spec-3.9-ratification` flips `minItems` to 9 only after the chain of gates closes. — see §5 + Open Questions.
- `edl_class` — enum (`primary_9x16` for v1.0 · `variant_cutdown` reserved for v1.1 multi-variant conform).
- `edl_evidence_hash` — SHA-256 over the `edl` + `conform_check` + `plan_fidelity_check` block (forensic, tamper-evident conform).
- `render_dispatched` — `const false` in v1.0 (Editor authors the EDL; the human/automation renders. This is the field Edit Director's schema named as "flips relevance at Editor" — and v1.0 keeps it `false`, the honest declaration that no media was produced by the agent). Flips to a real value only when Week 4–5 render automation ships (v1.1).
- `conform_mode` — enum (`human_in_the_loop` for v1.0 · `automated` reserved for v1.1 Week 4–5). The explicit human-in-the-loop attestation.
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.

### §3.4 errorEnvelope code namespace (target 7–9 LOCKED on Day 67/68 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `upstream_plan_not_ready` | Edit Director `verdict not in {plan_ready}` / not `successEditPlan` with no Lever-3 sign-off on a `revise` | 1 | Halt — Editor never conforms an un-directed reel. |
| `upstream_not_success` | the consumed Edit Plan is `errorEnvelope` | 2 | Halt — cannot conform a failed direction output. |
| `asset_unresolved` | a `cut_order[].asset_uri` does not resolve against the Ingest `asset_bundle` | 3 | Hard FAIL — cannot bind a cut event to media; route back to Ingest. |
| `timecode_out_of_range` | a cut event `out_ms` exceeds the resolved declared media duration, or `out_ms <= in_ms` | 4 | Hard FAIL — cannot conform a cut past available media; route back to Edit Director (re-trim). |
| `timeline_gap_or_overlap` | conformed events leave a timeline gap or double-spend the same source span | 5 | Hard FAIL — the EDL is not gap-free / no-double-spend; route back to Edit Director. |
| `transition_policy_violation` | the plan demands (or the conform would require) a non-cut transition event | 6 | Hard FAIL — hard-cuts-only enforced at the EDL layer; `detail` names the event. |
| `plan_fidelity_breach` | conformed copy/order/timing deviates from the plan, or `plan_evidence_hash` does not verify | 7 | Hard FAIL — Editor must conform the plan faithfully; a deviation = an unauthorized creative override. |
| `edl_firewall_breach` | a banned-entity token appears in a passthrough caption / lower-third / end-card at commit time (10th pass) | 8 | Hard FAIL — last text checkpoint before pixels; forensic-log the field. |
| `edl_lineage_failure` | malformed parent_chain / broken n-tuple lineage | 9 | Forensic — audit-trail break. |
| `editor_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 67/68 LOCK:** 7–9 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping.

---

## §4. Tier Constraints & Mode Coverage

**Per-tier gate access (Editor is universal-access AND tier-FLAT in its own logic — restated for defense-in-depth pass 10):**

| Tier | Reaches Editor? | Editor's own conform behavior | Variants conformed (v1.0) | Cost |
|------|-----------------|-------------------------------|---------------------------|------|
| Pilot | **YES** | Faithful conform of the plan | 1 (primary 9:16) | ~$0.00 |
| Starter | **YES** | Faithful conform of the plan | 1 (primary 9:16) | ~$0.00 |
| Pro | **YES** | Faithful conform of the plan | 1 (primary 9:16; flags 4) | ~$0.00 |
| Enterprise | **YES** | Faithful conform of the plan | 1 (primary 9:16; flags 5) | ~$0.00 |

**Why universal access + tier-FLAT behavior (the difference from Edit Director's tier-sensitive richness):** Edit Director is the *creative authority* whose output richness is a sold tier feature, so its plan scales by tier. Editor is the *executor* — a conform is faithful or it isn't, regardless of tier. A Pilot 8-beat plan and an Enterprise 12-beat plan are conformed by the identical executor logic; the richness already lives in the plan Editor receives. **The plan carries the tier envelope; Editor faithfully executes whatever envelope arrives.** v1.0 conforms the primary 9:16 for every tier and flags the `variants_planned` count (the 1:1 LinkedIn cutdown EDL is a derived v1.1 conform). This is the same tier-flat discipline Ingest holds — a technical executor does not re-litigate the tier ladder.

**No cost-ledger / no asset-validation / no creative authority (the inherited discipline, tripled):** Editor does **NOT** re-run the cost ledger (QC Pre-flight's authority), re-validate assets (Ingest's authority), OR re-direct the cut (Edit Director's authority). It is three gates downstream of cost enforcement, two gates downstream of asset validation, and one gate downstream of creative direction; re-litigating any of them would be redundant and risk a double-fail on a reel already cleared. Editor's authority is **faithful conform**, full stop.

**Mode coverage (mode-BLIND by inheritance — the convergence payoff, two stages deep):**

| Mode | What Editor sees | Mode-specific note |
|------|------------------|--------------------|
| A (human footage origin) | The SAME mode-agnostic Edit Plan | Editor cannot tell, and does not need to know, that these shots came from a videographer. `production_mode` is NOT read as a branch. |
| B (rendered + replicated origin) | The SAME mode-agnostic Edit Plan | Identical conform path. |
| C (replicated hot-path origin) | The SAME mode-agnostic Edit Plan | Identical conform path. |

**Mode-blind guarantee (the core §4 contract):** Editor asserts `mode_blind_confirm.production_mode_read == false` in every output — a self-attestation that it conformed the EDL without consulting the origin mode. This is the SECOND machine-checkable proof that Ingest's mode-convergence seam holds — now two stages downstream. **Editor is the second agent in the 17-agent fleet for which the mode columns of this table are identical; that identity, carried through both the director AND the executor, is the structural evidence that the post-production tail is genuinely mode-agnostic end-to-end.** If Editor ever NEEDED to branch on mode to conform a cut, the convergence contract would be broken upstream. By construction it never does.

---

## §5. Process Steps (System Prompt Skeleton — Day 67 §7 will LOCK)

The agent runs an **11-step conform loop** per invocation (mirrors the AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director 11-step process pattern). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope.

**Step 1 — Verify Edit Director precondition + parse input**
- Read the Edit Director `edit_plan.json`. Confirm `output_type == "successEditPlan"` AND `verdict == "plan_ready"` (or `revise` + Lever-3 sign-off attached). Otherwise → halt with `upstream_plan_not_ready`.
- Parse input JSON against `input.schema.json` (Day 67/68 LOCKED). There is NO mode branch — assert the plan is the mode-agnostic shape.
- Confirm the consumed plan is the success branch. Any `errorEnvelope` upstream → halt with `upstream_not_success`.

**Step 2 — Lineage integrity**
- Validate `metadata.parent_chain` is a well-formed 8-tuple inbound (5/6/7-tuple accepted additively until the §3.9 amendment + the Edit Director 8-tuple LOCK). Malformed → `edl_lineage_failure`.

**Step 3 — Plan-evidence + asset resolution**
- Verify the `plan_evidence_hash` (SHA-256 over the plan's `edit_plan` + `brand_edit_check`) recomputes — the plan was not tampered post-direction. Mismatch → `plan_fidelity_breach`.
- Resolve every `cut_order[].asset_uri` against the Ingest `asset_bundle.raw_footage[]`. Unresolvable → `asset_unresolved` (route back to Ingest).

**Step 4 — Timecode + timeline conform**
- For each cut event: round the plan's `in_ms`/`out_ms` to the 30fps frame grid; validate `out_ms <= declared_duration_ms` AND `out_ms > in_ms`. Over-range → `timecode_out_of_range` (route back to Edit Director).
- Lay events end-to-end on the record timeline; confirm gap-free + no source double-spend. A gap/overlap → `timeline_gap_or_overlap`.

**Step 5 — Transition-policy enforcement (EDL layer)**
- Emit every event boundary as a hard `cut`. If the plan's `transitions` is anything but the hard-cuts-only const, or any conform would require a dissolve/wipe/zoom event → `transition_policy_violation`. (Brand rule enforced at the timeline, not just the prompt.)

**Step 6 — Caption / lower-third / end-card event placement**
- Place each `caption_lines[]`, `lower_thirds[]`, and the `end_card` as timed timeline events, content **byte-faithful to the plan** (NO re-authoring — Editor copies the plan's text exactly). Preserve the plan's `case: lowercase` / `align: left` / `<=22` caption rules as already-validated facts (re-assert, do not re-derive).

**Step 7 — Music-bed placement**
- Place the single `music_bed` as a timeline audio event at t0; mark the `music_swell_map[]` positions as conform markers (Sound finalizes loudness + mix — NOT Editor). Confirm the bed + voice track resolve in the asset bundle.

**Step 8 — Defense-in-depth firewall pass (tenth time, COMMIT-time passthrough layer)**
- Re-run the canonical entity-firewall regex (Cross-SPEC §3 drift #10): `Holdco | Principal | NPOX | 4821 | 6315 | SLN | Retail Supply | Nonprofit Leader A | Community Nonprofit | Nonprofit Leader B | Nonprofit Leader C` over every conformed `caption_events[].text`, `lower_third_events[].content`, and the `end_card_event.line`.
- Hard FAIL → `edl_firewall_breach` + forensic log naming the field. **This is the COMMIT-time checkpoint:** Editor authors no new copy (Edit Director already firewall-scanned at the 9th pass), but Editor is the agent that COMMITS that text to the executable cut spec — so a final firewall re-scan before the EDL can reach a renderer is the highest-stakes, last-line catch (a leak that survives here burns into pixels).

**Step 9 — Plan-fidelity + conform check**
- Run `plan_fidelity_check`: cut count matches the plan, caption/lower-third/end-card copy byte-faithful, transition policy hard-cuts-only, `plan_evidence_hash` verified. Any deviation → `plan_fidelity_breach` (an unauthorized override).
- Run `conform_check`: timeline gap-free, no double-spend, all events bounded by declared duration, frame-aligned, total timeline in the 45–75s band (re-assert from the plan's directed duration). Out-of-band → routed as `timecode_out_of_range`/`timeline_gap_or_overlap` per the offending cause.

**Step 10 — Construct EDL payload**
- If all green: build `successEdl` per §3.1 with the full `edl` (events + caption/lower-third/music/end-card events) + `conform_check` + `plan_fidelity_check` + `verdict: "edl_ready"` + `handoff_targets: ["sound-agent"]`.
- Compute `edl_evidence_hash` (SHA-256 over the edl + conform_check + plan_fidelity_check block — tamper-evident).
- Extend `parent_chain` to a **9-tuple** (append `edl_id`), held additively per §3.3.
- Set `render_dispatched: false` (v1.0 honesty — the human conforms), `conform_mode: "human_in_the_loop"`, `edl_class: "primary_9x16"`, `mode_blind_confirm.production_mode_read: false`, `human_review_required: true`.

**Step 11 — Emit + handoff**
- Validate output payload against `output.schema.json` (Day 67/68 LOCKED). Hard FAIL → forensic log + halt (output should always validate; failure here = agent bug).
- Emit JSON to stdout (paste-and-run runbook) OR persist the EDL to the platform path / the Drive `/reels/[reel_id]/` conform queue per runtime environment (Blueprint §7 I/O: Editor writes `Drive/reels/[reel_id]/v1.mp4` — in v1.0 the EDL goes to the human conform queue, the human writes the v1.mp4).
- On `fail`, set `route_back_to` per the §3.2 verdict↔route map so the Orchestrator can re-enter the pipeline at the correct agent (Edit Director for a plan defect, Ingest for an asset gap).

**Anti-patterns Step 11 prevents (Lock-time discipline mirror from Edit Director / Ingest §11):**
- No markdown fences around output JSON.
- No `print()` statements before the output JSON block.
- No engine credentials referenced; **no media render dispatched** (v1.0 authors an EDL only — `render_dispatched` is `const false`; the human/automation conforms).
- No absolute URLs in any EDL `asset_uri` echoed from the plan (Hard Rule #8 inherit).
- No `edl_ready` verdict emitted while any conform, fidelity, or firewall check is unresolved (must be `fail`).
- No reading of `production_mode` as a branch discriminator (mode-blind by construction — `mode_blind_confirm.production_mode_read` must be `false`).
- **No creative re-interpretation:** Editor copies the plan's copy/order/timing exactly; it does NOT re-author a caption, re-order a cut, or "improve" the plan. A plan it disagrees with is conformed faithfully or failed to Edit Director — never silently rewritten.
- **No operator/render impersonation:** Editor emits `human_review_required: true` + an EDL *recommendation* + `render_dispatched: false`; it does NOT mark a reel "rendered" or "approved for Sound" as a ratified state — that is the human conform (v1.0) or the Week 4–5 automation (v1.1).

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 67 + 68)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 67 partial 1. Pattern source: Edit Director §6 / Ingest §6. Target 10–12 checks bipartite-covering the 7–9 errorEnvelope codes. Slot 11 reserved for `editor_agent_failed` per Cross-SPEC §3.6 slot-naming canon. Checks span: precondition + plan-evidence verify · lineage · asset resolution · timecode-in-range · timeline gap-free/no-double-spend · transition hard-cuts-only · caption/lower-third/end-card fidelity · music-bed resolve · commit-time firewall · mode-blind self-attestation · plan-fidelity (`plan_evidence_hash`).
- **§7 System Prompt v1.0** — Day 67 partial 1. Frame + hard rules + universal-tier-FLAT table + 11-step conform loop verbatim from §5 + the Blueprint §4.10 EDL/v1-edit target shape inlined + the REINVENTED format spec (§8: 9:16 · 1080×1920 · 30fps) + brand-event rules (§7/§11) as the enforced conform surface. ~12–14 KB target. Hard Rules mirror Edit Director with Editor-specific tightening on "conform-faithfully-never-re-author," "author-an-EDL-never-render," and "human-conforms (render_dispatched const false)" discipline.
- **§8 Performance Targets** — Day 68 partial 2. 9 metric categories. Schema validity 100% / plan-fidelity 100% (a conformed copy/order deviation must never survive) / commit-time firewall catch 100% / timecode-in-range 100% / gap-free 100% / false-edl-ready rate 0% target / false-fail rate ≤ 8% (over-flagging a borderline timecode to `fail` is the acceptable failure direction) / p50 latency 25s / p95 75s (conform reasoning — lighter than Edit Director's authoring) / zero engine + zero render cost.
- **§9 Test Fixtures** — Day 68 partial 2. 5-fixture portfolio: TC-01 clean Mode-origin-A→plan Pro `edl_ready` (full EDL) · TC-02 Mode-origin-C Enterprise `edl_ready` (proves mode-blind: byte-identical conform path to TC-01 despite different origin — the **mode-blind conform-convergence proof**, the Editor analog of Edit Director's authoring-convergence proof) · TC-03 `timecode_out_of_range` → fail + route to Edit Director (a cut out_ms exceeds declared media) · TC-04 `asset_unresolved` → fail + route to Ingest (a cut_order asset_uri not in the bundle) · TC-05 `edl_firewall_breach` (a banned token present in a passthrough lower-third reaching commit — the 10th-pass last-line catch; GATING fixture). 5 of 7–9 codes exercised; remainder in schema-only fixtures. Optional probes: the `plan_fidelity_breach` (a tampered `plan_evidence_hash`) + the slot-11 `editor_agent_failed` catch-all.
- **§10 Field Map** — Day 67 partial 1. ~26 rows · passthrough vs transform vs derived. Plan→EDL-event map (transform: ms intentions → frame-aligned timecodes) + plan-copy→caption/lower-third/end-card event map (passthrough, byte-faithful) + asset-bundle→resolution map + derived conform/fidelity-check map.
- **§11 Cost Model** — Day 68 partial 2. Zero engine + zero render snapshot (conform reasoning + EDL authoring only; the human/automation renders in v1.0/Week 4–5). Faithful-conform value model (economic justification = a frame-validated, brand-faithful cut on the first pass, no wasted editor cycles, no plan/asset mismatch discovered at v1 review). Explicit note: the actual render compute spend lands in v1.1 Week 4–5 automation — v1.0 is $0 by construction.
- **§12 Verdict Math** — Day 68 partial 2. EDL_READY = (Edit Director precondition met) ∧ (plan_evidence_hash verified) ∧ (all assets resolved) ∧ (all timecodes in range) ∧ (timeline gap-free + no double-spend) ∧ (transitions hard-cuts-only) ∧ (all events frame-aligned) ∧ (duration in band) ∧ (plan-fidelity byte-faithful) ∧ (commit-time firewall clean). Any single ∧-term false → fail per §3.2 (NO `revise` branch — deterministic executor). Fully deterministic — Editor has zero judgment slots (the defining divergence from Edit Director's one `revise` slot).
- **§13 Critical Decisions LOCKED** — Day 68 partial 2. Target 10–14 LOCKED decisions. Pre-scaffolded list:
  1. EDL-authoring vs render scope — v1.0 = EDL/conform-spec authoring ONLY; actual pixel render is human-in-the-loop at launch (Blueprint §9), automation Week 4–5. `render_dispatched: const false`. [LOCKED-as-drafted Day 66]
  2. Faithful-executor, zero creative re-interpretation — Editor conforms the plan's order/copy/timing byte-faithfully; it never re-authors, re-orders, or "improves" the plan. [LOCKED-as-drafted Day 66]
  3. Two-verdict (NO `revise`) — Editor is deterministic; the subjective slot lives upstream at Edit Director. `edl_ready | fail` only. [LOCKED-as-drafted Day 66]
  4. Mode-blind by inheritance — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested (the second mode-blind agent). [LOCKED-as-drafted Day 66]
  5. Plan-ready precondition — Editor runs only on a `successEditPlan`/`plan_ready` (or Lever-3-signed `revise`) reel; otherwise halts `upstream_plan_not_ready`. [LOCKED-as-drafted Day 66]
  6. Tier-FLAT behavior — all 4 tiers reach Editor; the plan carries the tier envelope, Editor conforms it identically (no own tier scaling). [LOCKED-as-drafted Day 66]
  7. 9-tuple parent_chain — inherits Edit Director 8-tuple + appends `edl_id`; QUADRUPLY-deferred (depends on §3.9 amendment ratification AND the Edit Director 8-tuple LOCK behind the Ingest 7-tuple behind the QC 6-tuple). [DEFERRED — held additively at `minItems: 5`]
  8. errorEnvelope code count — 7–9 target. [PRELIMINARY · operator amend Day 68]
  9. Self-QC check count — 10–12. [PRELIMINARY · operator amend Day 68]
  10. Plan-fidelity = ZERO tolerance — a conformed copy/order/timing deviation, a non-cut transition event, or a missing/altered end-card must NEVER survive to `edl_ready`; `plan_evidence_hash` machine-verified. [LOCKED-as-drafted Day 66]
  11. Commit-time firewall (10th pass) — Editor re-scans the passthrough caption/lower-third/end-card text at commit time, the last checkpoint before pixels (not a new authorship surface). [LOCKED-as-drafted Day 66]
  12. No render, no engine, no decode — NO generative engine, NO media render, NO byte-level decode in v1.0; declared-duration math only; `render_dispatched: const false`, `cost_incurred_usd ~$0`. [LOCKED-as-drafted Day 66]
  13. Conform-faithful handoff to Sound — Editor hands the EDL + v1-edit handle to Sound (Blueprint §4.10); the EDL goes to the human conform queue until Week 4–5 automation. [LOCKED-as-drafted Day 66]
  14. Multi-variant scope — v1.0 conforms the primary 9:16 EDL + echoes the `variants_planned` count; auto-cutdown EDL generation (1:1 LinkedIn) deferred to v1.1. [PRELIMINARY · operator amend Day 68]
- **§14 Calendar status updates** — Day 67 partial 1. Day 66 ✓ → trajectory populated.
- **§15 Change Log** — Day 68 partial 2. v1.0 lifecycle entries (outline-day-66 → body-day-67 → body-day-68 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 68 partial 2. Cross-SPEC §3.9 canonical fields + 6 Editor additions (9-tuple parent_chain, edl_class, edl_evidence_hash, render_dispatched const false, conform_mode, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `editor-agent` (kebab-case, matches the fleet pattern + Blueprint §4.10 handoff target) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `edl_evidence_hash` SHA-256 over the edl + conform_check + plan_fidelity_check block; `plan_evidence_hash` re-verified (inherits Edit Director's anchor) |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ Editor consumes the accumulated surface as read-only context; it contributes its own conform predicates downstream |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-BLIND table — the second agent for which the mode columns are identical (the convergence payoff, two stages deep) |
| §3.6 Slot 11 naming canon | ✅ Reserved `editor_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Consumed shapes respected; Editor's own predicates snake_case |
| §3.8 Tier↔mode firewall (10th defense-in-depth) | ✅ Step 8 COMMIT-time passthrough firewall (last checkpoint before pixels) + §4 universal-tier-FLAT table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 9-tuple, held additively. **Quadruply-deferred** — gated on the §3.9 amendment ratification AND the Edit Director 8-tuple LOCK (behind the Ingest 7-tuple, behind the QC 6-tuple). |
| §3.10 Cost ceiling authority | ✅ §4 explicitly DECLINES to re-litigate cost (QC Pre-flight's authority), re-validate assets (Ingest's authority), OR re-direct the cut (Edit Director's authority) — no triple-enforcement; Editor is $0-cost in v1.0 |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 66 outline — 6 parked for operator amendment)

1. **EDL-only vs partial-render scope** — v1.0 authors the EDL + conform manifest; the actual pixel conform into v1.mp4 is human-in-the-loop at launch (Blueprint §9), automation Week 4–5. Confirm v1.0 stops at the EDL and dispatches NO render (`render_dispatched: const false`). *(Donna recommends: confirm EDL-only for v1.0 — the EDL is the buildable, highest-leverage, $0 slice; the render automation lands in the Week 4–5 window the Blueprint already scopes, and keeps the zero-dollar invariant intact.)*
2. **Two-verdict (no `revise`)** — should Editor stay deterministic (`edl_ready | fail`), or inherit Edit Director's success-side `revise` for some borderline conform tension? *(Donna recommends: keep two-verdict — Editor is a faithful executor with no subjective surface; a `revise` here would mean second-guessing a directed plan, exactly the decide/execute override the boundary forbids. The judgment slot belongs upstream where the creativity is.)*
3. **9-tuple parent_chain** — quadruply-gated in effect (depends on the §3.9 amendment AND the Edit Director 8-tuple LOCK AND the Ingest 7-tuple AND the QC 6-tuple behind it). Editor is the first 9-tuple consumer — a fourth forcing function. *(Donna recommends: RATIFY the §3.9 amendment AS-DRAFTED so all 17 agents inherit n-tuple lineage; Editor holds additively until the chain closes.)*
4. **Sound handoff readiness** — Editor hands to a not-yet-built Sound (Agent #11 candidate, position 12). Should v1.0 emit the EDL + v1-edit handle to a holding store (the Drive `/reels/[reel_id]/` conform queue, per Blueprint §7 I/O) until Sound ships, or assume direct handoff? *(Donna recommends: emit to the Drive conform queue in v1.0; direct agent-to-agent handoff activates when Sound LOCKs — mirrors the Edit Director→Notion-Edit-Plan and Ingest→Notion-Asset-Manifest holding-store decisions.)*
5. **EDL format** — v1.0 emits a JSON EDL (schema-validatable) + a CMX3600-faithful event view; should a native NLE project export (Premiere/Resolve XML) be in v1.0 or deferred? *(Donna recommends: defer NLE-XML export to v1.1 — the JSON EDL is the canonical, validatable artifact; the editor app conforms from it in v1.0 (human), and the XML adapter is a derived conform-format convenience that lands with the render automation.)*
6. **Frame-rounding basis** — cut timecodes are frame-rounded to the declared 30fps grid from the plan's ms intentions, with NO byte-level media decode in v1.0; is declared-duration + 30fps-grid rounding an acceptable conform basis? *(Donna recommends: ratify declared-duration + 30fps-grid rounding for v1.0 — sub-frame / waveform-accurate conform needs decode (v1.1), the same declared-spec-only posture as Ingest and Edit Director.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (full Editor trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 66 | Wed Jun 24 | **SPEC outline §0–§5** [SHIPPING NOW] | Edit Director Day 58 outline |
| 67 | Thu Jun 25 | SPEC body partial 1: §6 + §7 + §10 + §14 | Edit Director Day 59 / Ingest Day 51 |
| 68 | Fri Jun 26 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | Edit Director Day 60 / Ingest Day 52 |
| 69+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | Edit Director Day 61–65 / Ingest Day 53–57 |
| 70 | Sun Jun 28 | **REST DAY** — no build (pre-stage next scaffold only) | Day 21/28/35/42/49/56/63 Rest Day compounding |

**Sprint context:** Editor is **Agent #10** — the third post-production agent and the first *executor* agent in the post tail, the 10th defense-in-depth firewall (commit-time passthrough layer) and the **second contractually mode-blind agent** (the continued proof of Ingest's convergence seam, two stages deep). It is the inflection the whole fleet was built toward — the first agent whose output is destined for a media file (the v1.mp4) — yet in v1.0 it produces NO media: it drafts the EDL the human conforms (Week 4–5 automation deferred), keeping the zero-dollar / no-render invariant intact. The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) shipped on the six production agents through the QC Pre-flight gate; Editor v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the Ingest, QC Pre-flight, Style Replication, and Edit Director outlines were (while their LOCK ceremonies remain operator-gated).

---

## Files produced today (Day 66)

- `ars/ARS-2026-06-24-Day-66-Editor-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-06-24.md` — Day 66 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 66)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked. No media render, no byte-level decode. (Editor by design authors an EDL and renders no pixels in v1.0 — the human conforms; full automation is the Week 4–5 v1.1 scope.)
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no client/investor outreach. The end-of-run status iMessage to Jamila ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business. (Notification-channel status carried — see build log.)
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, no render compute, zero $ spent.
- ✅ **No operator-impersonation.** AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director LOCK ceremonies NOT assumed — all five confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Edit Director Day 61 Items 6/8/11 + the Day 65 runbook execution NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. Editor v1.0 LOCK will hard-gate itself on the upstream LOCKs (especially the Edit Director 8-tuple) being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 8 enumerates HC/NPOX tokens precisely so the agent can BLOCK them at the commit-time layer — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Edit Director Day 58 outline structure inherited verbatim. Orchestration Blueprint §1.2 / §2 / §4.9 / §4.10 / §6 / §7 / §9 (Agent 11 Editor definition) + Cross-SPEC §3 canon + Brand-Voice Intake §7–§11 used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-66 build runs Wednesday (Pacific). Next Rest Day: Day 70 (Sun Jun 28 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 66 ships clean. Day 67 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). Editor is Agent #10 of 17 — the 10th defense-in-depth firewall (commit-time passthrough layer) and the first executor agent in the post tail, the second contractually mode-blind agent and therefore the continued proof that Ingest's mode-convergence seam holds two stages deep. It is the inflection the whole fleet was built toward (first output destined for a media file) — yet v1.0 produces no media, authoring the EDL the human conforms (render automation deferred to Week 4–5), keeping the zero-dollar / no-render invariant intact. Operator pickup: (1) the five predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight + Ingest + Edit Director) remain pending and gate Editor's eventual v1.0 LOCK — the Edit Director 8-tuple in particular is Editor's direct 9-tuple dependency; (2) review the §13 critical-decisions list + ratify the Cross-SPEC §3.9 n-tuple amendment so the n-tuple parent_chain is canon (Editor is now the fourth forcing function); (3) confirm the Agent #10 = Editor selection (or re-assign the slot) at the Edit Director LOCK-ceremony close.*
