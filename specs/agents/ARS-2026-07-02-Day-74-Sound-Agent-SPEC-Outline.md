# ARS — Sound Agent v1.0 SPEC OUTLINE (§0–§5)

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Authored:** Day 74 · Thu Jul 2, 2026 (Pacific) · overnight build session (Donna)
**Deliverable class:** Forward SPEC outline §0–§5 (the head-start design for Agent #11 of 17)
**Status:** OUTLINE ONLY — no LOCK, no schema, no SKILL bundle. Body partials author Days 75 + 76 per the calendar in §0.
**Pattern source:** Editor Day 66 outline (`ARS-2026-06-24-Day-66-Editor-Agent-SPEC-Outline.md`) — section structure inherited verbatim. Orchestration Blueprint §1.2 (Agent 12 row: *"Sound — VO polish, music bed mix, SFX accents, loudness normalization (−14 LUFS for IG/TT, −16 LUFS for YT)."*), §2 swim-lane (position 12 between Editor and Motion), §4.10 (Editor→Sound payload: *"v1 edit file + EDL. Sound adds VO polish, music bed, SFX accents, loudness pass."*), §4.11 (Sound→Motion payload: *"v2 edit with finalized audio."*), §6 dispatch table (row 12: *"On Editor v1 · Per reel · v1 edit"*), §7 read/write contract (Sound reads *v1 edit*, writes *Drive `/reels/[reel_id]/v2.mp4`*), §9 build-checklist used as the grounding spine. Brand-audio rules grounded in `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7–§11 (voice / motion / caption cadence) and the loudness targets in Blueprint §1.2 + §4.12.

> **Agent-selection note (Donna, surfaced not hidden):** The Day 73 Editor LLM-Test-Runbook close named the next NEW agent to spec as **"Sound (#11) — its SPEC outline is the Day 75+ forward slot after the Editor LOCK ceremony window."** Today (Day 74, Thu Jul 2) the §14 calendar slot names **Editor v1.0 LOCK** — but that ceremony is **operator-only** (it joins AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director in the pending-LOCK queue; Donna executes NONE of it and did not tonight). With the only calendar-named Day-74 item being an operator-gated ceremony Donna cannot perform, the buildable forward deliverable is the **Sound #11 SPEC outline**, pulled one slot forward into Day 74. This is the identical forward-looking basis on which the Ingest, QC Pre-flight, Style Replication, Edit Director, and Editor outlines were each authored while their predecessor LOCK ceremonies remained operator-gated — never a fake-advance of the ceremony, always the next buildable design head-start. Surfaced here, not silently reconciled. Rationale for Sound as the #11 build: (1) **strict dependency order** — Sound is the immediate runtime stage downstream of Editor (Blueprint §6: *"On Editor v1"*), consuming the `successEdl` / v1-edit handle Editor authors; (2) **fleet-unblock** — nothing downstream (Motion → full QC) can run without a finalized-audio v2 edit; Sound is the gate that turns a silent conformed cut into a mixed, loudness-normalized reel; (3) **the render-tail executor pattern continues** — Sound inherits Editor's *author-the-spec-not-the-media* seam (it authors an audio conform spec; the human/automation processes the audio), keeping the zero-dollar / no-decode invariant intact one stage deeper; (4) **third mode-blind agent** — it inherits Editor's mode-agnostic lineage, the continued proof that Ingest's convergence seam holds THREE stages deep. Operator may re-assign the #11 slot at the Editor LOCK-ceremony close.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 11 — Post-production finishing layer (conformed cut → finalized audio) |
| Agent index | **#11 of 17** (build sequence — continues the Editor Day 66 "agent #10 of 17" framing) |
| Runtime pipeline position | **12 — Sound** (finishes the audio per the v1 edit + EDL: VO polish directives, music-bed mix levels, SFX accent placements, loudness normalization to platform target; emits the audio conform spec + the v2-edit target); receives the v1 edit + EDL from Editor, hands the v2 edit + finalized-audio spec to Motion |
| Pipeline tier | POST-PRODUCTION FINISHING (second *executor* agent in the post tail; the first agent whose domain is **audio** — VO / music / SFX / loudness) |
| Mode coverage | **Mode-blind by inheritance** — consumes the mode-convergent EDL + v1 edit (themselves authored from the mode-agnostic Asset Manifest → mode-agnostic Edit Plan); never sees `production_mode` as a branch discriminator. The **THIRD** contractually mode-blind agent (Edit Director first, Editor second); the continued live proof that Ingest's convergence seam holds three stages deep. |
| Predecessor SPEC (gate) | `ARS-2026-06-27-Day-69-Editor-Agent-v1-LOCK-CANDIDATE.md` (Day 69 LOCK candidate — operator-gated). Sound runs only on an Editor-passed (`successEdl`, verdict `edl_ready`) reel. |
| Predecessor schemas | `ARS-2026-06-29-Editor-output.schema.json` (Day 71) — the `edl` block (`events` + `caption_events` + `lower_third_events` + `music_event` + `end_card_event`) + the `v1_edit_uri` handle consumed as the primary INPUT. Plus the Ingest `output.schema.json` (Day 54) `asset_bundle` (the `audio` voice track + the `music_bed` `asset_uri`) consumed as the audio-resolution input. |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape (§3.3/§3.8), metadata block + n-tuple parent_chain (§3.9) all inherited |
| Brand-audio canon | `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (voice / tone), §8 (reel format specs: 9:16 · 1080×1920 · 30fps), §11 (caption ↔ VO cadence) + Blueprint §1.2 / §4.12 loudness targets (**−14 LUFS IG/TT · −16 LUFS YT**) — the audio-finishing rules the conform spec must specify faithfully |
| Defense-in-depth layer | **11th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → Editor → **Sound**) — the **audio-domain passthrough** firewall: it re-scans the declared VO transcript / any spoken-word metadata the audio finishing touches for banned-entity tokens (the last AUDIO checkpoint before Motion typography). NOT a new authorship surface (Sound authors no copy — the VO transcript is Script/Editor passthrough); it is a **passthrough-integrity re-scan** over the declared transcript (no waveform analysis in v1.0 — declared transcript only). |
| Lever inheritance | Reads `lever_state` from upstream `metadata`; emits `human_review_required: true` per Lever-3 default AND per the v1.0 human-in-the-loop finishing posture (Blueprint §9). The audio conform spec is a *spec a human executes* in v1.0 — Sound never marks audio "processed" or "normalized"; the operator (or Week 4–5 automation) runs the DSP. |
| Pricing tier authority | **ALL tiers** — Pilot · Starter · Pro · Enterprise. Every reel needs an audio finish. **Tier-FLAT in its own logic** (like Editor, unlike Edit Director): Sound faithfully specifies whatever audio the EDL's music/VO events declare — it does not scale its own behavior by tier (it inherits the plan's tier envelope and specs it). The `tier_richness` block is read for variant/platform-target awareness only; v1.0 specs the primary IG/TT −14 LUFS target (flags the YT −16 variant). |
| Cost authority class | **Near-zero (ties Ingest / QC Pre-flight / Edit Director / Editor for lowest in fleet) IN v1.0** — pure reasoning + audio-conform-spec authoring over the EDL + asset bundle. **No generative engine calls, no audio DSP, no byte-level audio decode / waveform analysis in v1.0** — Sound v1.0 drafts the audio finishing spec (VO polish directives + mix levels + SFX placements + loudness targets); the human executes the DSP in the audio app (Blueprint §9 Week-2 posture); full audio automation is Week 4–5 (v1.1). Effective per-reel cost ≈ $0.00. `audio_processed: const false` in v1.0 — Sound specifies the finish, the HUMAN runs it. |

**Build calendar (Week 11 — Sound trajectory, mirrors the proven 8-day agent-build cadence):**
- **Day 74** (today, Thu Jul 2 · Wk11) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 75 (Fri Jul 3 · Wk11) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 76 (Sat Jul 4 · Wk11) — SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16
- Day 77 (Sun Jul 5 · Wk11) — **REST DAY** (no build; pre-stage next scaffold only, per the Day 21/28/35/42/49/56/63/70 Rest Day-compounding pattern)
- Day 78+ (TBD) — LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK (pattern: Editor Day 69–73 / Edit Director Day 61–65)

> **Rest Day honesty:** This Day-74 build runs Thursday (Pacific) — building is allowed. The next Rest Day is Day 77 (Sun Jul 5 Pacific) per the Day 73 log close. The UTC clock may have rolled past midnight at author time, but the sprint labels by Jamila's Pacific date (Thu Jul 2) — the same convention noted in prior logs.

> **Sequencing honesty:** The 42-day sprint's headline deliverable — the Mode B Pro single-reel **commercial demo** (Day 42 target, now past) — shipped on the six launch-critical production agents threaded through the QC Pre-flight gate. Sound is the fourth *post-production* agent (after Ingest + Edit Director + Editor); its v1.0 build proceeds inside the **post-launch hardening window** and does **not** gate the launch demo. This outline is the forward-design head-start so the render/finishing tail is buildable in dependency order once the production-tier + Ingest + Edit Director + Editor LOCKs close.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Sound Agent** is the **audio finisher of post-production** — the moment a reel stops being a *silent conformed cut* and becomes a *mixed, loudness-normalized reel*: the voice track leveled and de-essed to spec, the music bed placed and ducked under the VO, the SFX accents landed on the cut points the EDL marked, and the whole mix normalized to the platform loudness target — a single executable audio conform spec the audio app (human in Week 2, automation in Week 4–5) applies to produce the v2 edit. It is the second *executor* agent in the fleet (after Editor), and the first whose domain is **sound** rather than the timeline or the frame.

Where the ten upstream agents authored intent, adjudicated correctness, directed the assembly, and conformed the cut, Sound *finishes the audio*:
- Brief / Script / Storyboard = intent + content authoring (what the reel SAYS and how it's shot)
- Production Coord = logistics (mode, vendor, budget)
- AI Video Gen / Style Replication = render + brand-finish (the pixels exist)
- QC Pre-flight = ship-safety (the reel is brand-safe + format-correct)
- Ingest = asset-readiness (the files are present, valid, in-sync — one mode-agnostic Asset Manifest)
- Edit Director = edit-plan authoring (the directed cut: order, pacing, captions, lower-thirds, music, transitions, end-card)
- Editor = cut conform (the frame-accurate EDL bound to real media — the executable timeline)

The Sound Agent picks up at the EDL + v1 edit and finishes the audio:
- **Sound Agent = audio finish ("Given an `edl_ready` EDL, the v1-edit handle, and the resolved audio bundle — voice track + music bed — produce a single executable audio conform spec: the VO polish directives (level, de-ess, breath-trim to the brand voice cadence), the music-bed mix levels + ducking envelope under the VO, the SFX accents placed on the EDL's cut/swell markers, and the loudness normalization target (−14 LUFS IG/TT primary, −16 LUFS YT flagged) — that the audio app applies beat-for-beat into the v2 edit, with NO re-cutting of the timeline and NO creative re-interpretation of the mix intent.")**

**Single-responsibility line (LOCKED on intent):**
> *"Post-production audio finisher. Receives the Editor-passed EDL (`successEdl`, verdict `edl_ready`) plus the v1-edit handle and the resolved audio bundle (voice track + music bed), and authors one canonical audio conform spec — VO polish directives (level/de-ess/breath to the brand voice cadence), music-bed mix + ducking envelope under the VO, SFX accent placements bounded by the EDL timeline, and the platform loudness-normalization target — that the audio app applies into the v2 edit. Authors the audio spec only; runs NO audio DSP, decodes NO waveform, and normalizes NO loudness in v1.0 (the human/automation executes the finish); calls no generative engine. Faithfully specifies the EDL's audio intent — it re-cuts NO timeline, re-authors NO copy, re-orders NO events. Emits a recommendation (`human_review_required`) — never a ratified 'processed' or 'normalized' state."*

**Why this agent's reason-to-exist is the cut/finish boundary (Blueprint §1.2):** Editor *conforms* the cut; Sound *finishes* the audio on that cut. The separation is the same production-discipline boundary every editorial pipeline draws between picture lock and audio post: the editor must not be re-mixing on the timeline, and the sound mixer must not be re-cutting picture. **This is Donna's design thesis for building Sound as Agent #11: it is the second faithful-executor agent, and the structural proof that the render-tail executor pattern generalizes from the timeline domain (Editor) to the audio domain — if Sound can produce a complete, executable audio conform spec from the EDL alone, with zero timeline re-cutting, the cut was locked and the finishing seam holds.** An `audio_unbuildable` outcome (a music/VO asset that cannot resolve, an SFX marker past the timeline, a loudness target out of the platform spec) is the signal that the EDL or the manifest was wrong — and it routes back, it never silently "fixes" the cut.

**Pipeline position (per Orchestration Blueprint §2 swim lane):**
```
... → EDITOR (cut conform → EDL) →
   [successEdl · verdict = edl_ready]
        │
        ▼  [EDL + v1 edit: frame-accurate timeline · music_event · Drive /reels/[reel_id]/v1.mp4]
   SOUND (audio finish → audio conform spec)
        │
        ▼  [audio spec + v2 edit: VO polish · music mix + duck · SFX accents · −14/−16 LUFS · Drive /reels/[reel_id]/v2.mp4]
   13 Motion → 14 QC (full)
        │
   [audio_unbuildable] → route back to Editor (timeline/EDL defect) or Ingest (audio asset gap)
```

**Why a finisher agent distinct from the upstream executor (the boundary question):** Editor already placed the `music_event` at t0 and marked the `music_swell_map` positions — so what does Sound add? A clean separation across the *conform→finish* boundary:
1. **Editor authors the TIMELINE** — the frame-accurate EDL: which media, in what order, with what cuts, and *where* the music bed and swell markers sit. It produces a *silent-picture conform*, not a *mix*. It works in timeline-space (frame-aligned event boundaries), not audio-space.
2. **Sound authors the MIX SPEC** — given the EDL and the *resolved* audio assets, the concrete audio conform: the VO leveled + de-essed to the brand voice cadence, the music bed set to a mix level and ducked under the VO, the SFX accents landed on the swell markers, and the whole normalized to the platform loudness target. It produces the executable audio artifact the audio app runs.
3. **The two phases catch different problems.** Editor can mark a music swell at 48000ms; only Sound, resolving the real audio and reasoning over the VO track, can specify that the bed must duck −6 dB under the VO from 0–30000ms and swell +3 dB into the 48000ms emphasis — and, resolving the bundle, discover that the voice track is missing and route back rather than spec a mix over silence. Sound does NOT re-cut (it trusts the EDL's order, timing, and events); it *finishes the audio against the resolved assets* and surfaces any mismatch.

The actual DSP (leveling, de-essing, ducking, SFX rendering, LUFS normalization into the v2.mp4) is, in v1.0, a **human** action (Blueprint §9: *"Human-in-the-loop for Week 2 — agent drafts the finishing spec, human executes in the audio app"*); full audio automation is targeted Week 4–5 (v1.1). v1.0 Sound authors the *audio conform spec*; it produces no media file itself. **`audio_processed` is the new honesty field at this agent — `const false` in v1.0, the explicit declaration that no waveform was touched by the agent.** This is the human-in-the-loop seam, made explicit and honest — the direct analog of Editor's `render_dispatched: const false`.

**Hand-off contract enforced:**
- **PRECONDITION:** Sound reads the Editor `edl.json`. If `output_type != "successEdl"` OR `verdict not in {edl_ready}` → halt with `upstream_edl_not_ready`. Sound never finishes a reel whose cut did not pass Editor. A `fail` (errorEnvelope) EDL → halt `upstream_not_success`.
- **INPUT contract:**
  - The Editor `successEdl` — `edl` (`events[]`, `caption_events[]`, `lower_third_events[]`, `music_event`, `end_card_event`, `frame_rate`, `total_timeline_ms`), `render_target.v1_edit_uri`, `tier_richness_echo`, `mode_blind_confirm`, the `edl_evidence_hash`.
  - The **resolved audio bundle** (the Ingest `asset_bundle.audio[]` voice track + `asset_bundle.music_bed` `asset_uri`) — the audio-resolution reference the mix spec's directives validate against.
  - The **denormalized upstream chain** in `metadata.parent_chain` (9-tuple inbound from Editor, quadruply-deferred) + accumulated `qc_pre_flags[]`.
- **OUTPUT contract:** Emits `audio_spec.json` per §3 (polymorphic: `successAudioSpec | errorEnvelope`). Motion reads the v2 edit + the finalized-audio spec (Blueprint §4.11: *"v2 edit with finalized audio"*) and adds typography / overlays / motion tokens — without re-deriving the mix.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| Audio conform spec authoring (VO polish directives + music-mix levels + SFX placements + loudness target) | Actual audio DSP / mix render into v2.mp4 — human-in-the-loop in v1.0 (Blueprint §9); automation Week 4–5 |
| Loudness-target specification (−14 LUFS IG/TT primary; −16 LUFS YT flagged) as a declared conform target | Live LUFS measurement + true-peak limiting — needs byte-level audio decode + a loudness meter |
| Music-bed mix-level + ducking-envelope specification (bed level, −dB duck under VO, swell markers → gain moves) | Waveform-accurate automatic ducking (sidechain compression render) — needs DSP |
| SFX accent placement (accent events time-bound to the EDL cut/swell markers) | SFX library synthesis / actual SFX rendering — Sound specs the placement; the audio app inserts the asset |
| VO polish directive spec (level, de-ess, breath-trim to the brand voice cadence — declared, not applied) | De-esser / EQ / compressor DSP render — needs waveform processing |
| Audio-domain firewall re-scan (11th pass) over the declared VO transcript passthrough | New-copy authorship (Sound authors NO copy — nothing to firewall but the passthrough transcript integrity) |
| Audio conform manifest (the asset→track map + platform loudness target + timeline-duration check) | Multi-platform loudness variants render (−14 + −16 both mastered) — v1.1 (v1.0 specs the primary −14, flags −16) |
| Spec-fidelity check (audio spec faithful to the EDL: timeline duration, music event, swell markers) | A/B alternate-mix conform |
| 10-tuple parent_chain extension (inherits Editor 9-tuple + appends `audio_spec_id`) | Audio-spec-to-DAW-session export (Pro Tools / Audition session) — v1.1 finishing-format adapters |
| Audio spec construction (declarative mix/level/loudness JSON) + audio recommendation | Render-farm / encode dispatch (the actual compute spend) — v1.1 automation |

**Pricing tier table (Sound is universal-access AND tier-flat in its own logic — defense-in-depth pass 11):**

| Tier | Reaches Sound? | Sound's own behavior | Cost | Finish note |
|------|-----------------|-----------------------|------|-------------|
| Pilot — Founding 5 | **YES** | Faithfully spec the EDL's audio (tier-flat executor) | ~$0.00 | specs VO level + bed + −14 LUFS |
| Starter — Operator | **YES** | Faithfully spec the EDL's audio (tier-flat executor) | ~$0.00 | specs VO level + bed + −14 LUFS |
| Pro — Studio | **YES** | Faithfully spec the EDL's audio (tier-flat executor) | ~$0.00 | specs the richer swell map + SFX accents |
| Enterprise — Agency | **YES** | Faithfully spec the EDL's audio (tier-flat executor) | ~$0.00 | specs the richest mix; flags −16 LUFS YT variant |

Sound adds **zero** generative cost to every tier envelope in v1.0. Its economic value is **faithful, platform-correct, brand-faithful audio finish** — every reel's mix is specified exactly as the cut directs, every loudness target set to the platform spec before a mixer (or a renderer) burns a cycle, and an EDL/asset mismatch is caught *before* the mix rather than discovered in the v2 review.

---

## §2. Inputs

Sound has **one canonical responsibility** (author the audio conform spec) reached from **one** primary input shape — the mode-convergent EDL. Like Editor (and unlike every production-tier agent), there is **no mode branch** and no source-polymorphism: this is the third agent whose input is structurally mode-blind. (It reads `tier_richness_echo` for variant/platform-target awareness only — it does not scale its own finishing logic by tier.)

### §2.1 Precondition input — Editor EDL verdict (gate)

**Always read first.** The Editor `edl.json`:
```json
{
  "output_type": "successEdl",
  "verdict": "edl_ready",
  "reel_ref": { "edl_id": "<uuid>", "edit_plan_id": "<uuid>" },
  "edl": { "events": [ /* ... */ ], "music_event": { /* ... */ }, "total_timeline_ms": 65000 },
  "conform_check": { "timeline_gap_free": true, "duration_in_band": true },
  "render_target": { "render_dispatched": false, "v1_edit_uri": "ars://reels/.../v1.mp4" },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_edit_plan" },
  "human_review_required": true,
  "metadata": { /* 9-tuple parent_chain inbound, held additively */ }
}
```
**Hard validation:** `output_type == "successEdl"` AND `verdict == "edl_ready"`. Otherwise → halt with `upstream_edl_not_ready`. A consumed `errorEnvelope` EDL → halt `upstream_not_success`. Sound does not finish a reel whose cut failed Editor, and does NOT auto-resolve a failed EDL (the fix belongs upstream — Sound inherits the recommend-don't-override discipline).

### §2.2 Primary input — EDL block (the conformed cut to finish)

**Required input fields (preliminary — full schema on the Day 75/76 partials):**
```json
{
  "edl": {
    "frame_rate": 30,
    "total_timeline_ms": 65000,
    "events": [ { "event": 1, "shot_ref": "shot-001", "rec_in_ms": 0, "rec_out_ms": 3000, "transition": "cut" } ],
    "music_event": { "asset_uri": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav", "at_ms": 0 },
    "music_swell_map": [ { "at_ms": 48000, "type": "emphasis_swell" } ],
    "caption_events": [ { "at_ms": 0, "text": "your calendar doesn't lie", "line": 1 } ]
  },
  "vo_transcript": [ { "at_ms": 0, "text": "your calendar doesn't lie" } ],
  "tier_richness_echo": { "tier": "pro", "variants_planned": 4, "primary_aspect": "9:16" },
  "metadata": { /* Cross-SPEC §3.9 — tier, lever_state, brand_id, session_id, parent_chain (9-tuple inbound), qc_pre_flags surface */ }
}
```

**Hard validations on primary input (defense-in-depth pass 11):**
1. Upstream `output_type` is `successEdl`, NOT `errorEnvelope`. (errorEnvelope → `upstream_not_success`.)
2. `verdict == "edl_ready"`. Any other verdict → `upstream_edl_not_ready` (defensive — Sound cannot finish an unlocked cut).
3. The `music_event.asset_uri` AND every voice track in the audio bundle resolve against the Ingest `asset_bundle` (so each audio directive binds to a real media handle). Unresolvable → `audio_asset_unresolved`.
4. Every SFX accent / mix directive time (`at_ms`) is `<=` the EDL's `total_timeline_ms` AND `>= 0` (no accent past the timeline, no negative time). Violation → `audio_marker_out_of_range`.
5. `asset_uri`s remain platform-relative `ars://...` (Hard Rule #8 inherit — Sound echoes them into audio-spec directives; it must not introduce an absolute URL). Violation → `asset_uri_integrity_failure`.
6. `metadata.parent_chain` is a well-formed 9-tuple inbound (5/6/7/8/9-tuple accepted additively — see §3.3). Malformed → `audio_lineage_failure`.

### §2.3 Audio-resolution input — Ingest asset bundle (voice + music)

**Denormalized, read as the audio-resolution reference (not re-authored).** Sound reads:
```json
{
  "asset_bundle": {
    "audio": ["ars://reels/.../raw/voice_track.wav"],
    "music_bed": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav"
  }
}
```
Used to resolve the voice track + music bed `asset_uri` → media handle, to confirm both exist for the audio conform manifest, and to bind every mix/level/SFX directive to a real audio asset. **Sound consumes these as fixed resolution facts — it specifies directives against them; it does NOT decode the waveform (no byte-level read, no loudness measurement — declared assets only, the same declared-spec posture as Ingest, Edit Director, and Editor).**

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block: `tier`, `lever_state`, `brand_id`, `session_id`. Sound reads `tier_richness_echo` for platform-target awareness (does this tier expect the −16 LUFS YT variant flagged? — yes, it flags it; it specs only the primary −14 LUFS IG/TT master) and sets the spec's `human_review_required: true` per Lever-3 default AND the v1.0 human-in-the-loop finishing posture. It does **not** re-run cost, asset validation, cut conform, or creative direction — those are QC Pre-flight's, Ingest's, Editor's, and Edit Director's authorities respectively; Sound trusts the passed verdicts and the `edl_evidence_hash`.

---

## §3. Outputs (skeleton)

Sound emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 / QC Pre-flight Day 40 / Ingest Day 48 / Edit Director Day 58 / Editor Day 66 output pattern (`oneOf [success branch, errorEnvelope]`).

### §3.1 successAudioSpec branch (audio finish specified)

```json
{
  "output_type": "successAudioSpec",
  "verdict": "audio_ready",
  "reel_ref": {
    "brand_id": "REINVENTED",
    "edl_id": "<uuid>",
    "audio_spec_id": "<uuid>"
  },
  "audio_spec": {
    "loudness_target": { "primary": "-14 LUFS (IG/TT)", "true_peak_ceiling_dbtp": -1.0 },
    "vo_polish": { "level_lufs_target": -16, "de_ess": true, "breath_trim": true, "voice_cadence": "brand_voice_v3" },
    "music_bed": { "asset_uri": "ars://reels/.../assets/ambient_piano_slow_120bpm.wav", "at_ms": 0, "base_level_db": -18, "duck_under_vo_db": -6 },
    "duck_envelope": [ { "from_ms": 0, "to_ms": 30000, "duck_db": -6 }, { "from_ms": 48000, "to_ms": 50000, "swell_db": 3 } ],
    "sfx_accents": [ { "at_ms": 48000, "type": "emphasis_swell_accent", "level_db": -12 } ]
  },
  "audio_conform_check": {
    "vo_track_resolved": true,
    "music_bed_resolved": true,
    "all_markers_in_timeline": true,
    "loudness_target_in_spec": true,
    "total_timeline_ms": 65000,
    "duration_in_band": true
  },
  "spec_fidelity_check": {
    "music_event_matches_edl": true,
    "swell_markers_match_edl": true,
    "timeline_duration_matches_edl": true,
    "vo_transcript_byte_faithful": true,
    "edl_evidence_hash_verified": true
  },
  "audio_firewall_pass_11": { "status": "pass", "passthrough_transcript_fields_scanned": 6, "hits": 0 },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_edl" },
  "finish_target": { "audio_processed": false, "finish_mode": "human_in_the_loop", "v2_edit_uri": "ars://reels/.../v2.mp4 (reserved — written by the human finish)" },
  "tier_richness_echo": { "tier": "pro", "loudness_variants_planned": 2, "loudness_variants_specced": 1, "primary_target": "-14 LUFS (IG/TT)" },
  "handoff_targets": ["motion-agent"],
  "metadata": { /* Cross-SPEC §3.9 with Sound additions per §3.3 — 10-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (audio not buildable)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "vo_track_missing",
  "failed_check_id": 3,
  "attempts": 1,
  "route_back_to": "ingest-agent",
  "reel_ref": { "audio_spec_id": "<uuid>" },
  "cost_incurred_usd": 0.00,
  "detail": {
    "violation": "the asset_bundle.audio[] voice track does not resolve — cannot spec a VO polish pass over a missing track",
    "affected_assets": ["voice_track.wav"],
    "recovery_path": "re-confirm the Ingest asset_bundle.audio[] voice-track asset_uri OR re-run Ingest to resolve the voice track"
  },
  "metadata": { /* Cross-SPEC §3.9 — 10-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `audio_ready` | Audio spec authored + EDL-faithful + brand-faithful + loudness-in-spec; cleared into Motion (held in the human finish queue in v1.0) | `null` (forward to Motion) | All conform + fidelity + firewall checks green |
| `fail` | Audio spec unbuildable from current inputs | `editor-agent` (timeline/EDL defect: marker out of range, spec-fidelity break) OR `ingest-agent` (audio asset gap: unresolvable voice/music `asset_uri`) | A finish/resolution defect that the EDL or the manifest must fix |

> **Defining divergence (surfaced):** Sound carries **2 verdicts** (`audio_ready | fail`) — it inherits Editor's deterministic two-verdict posture and deliberately does NOT introduce a third `revise`/creative verdict. Sound is a **faithful executor**, not a creative authority: loudness targets are platform constants (−14/−16 LUFS), the VO cadence is a brand-voice const, and the music/SFX placements are directed by the EDL. There is no subjective conform surface for it to hold to Lever-3. The soft creative tension lives upstream (Edit Director's `revise`); by the time a reel reaches Sound the cut is already `edl_ready`. Sound either specs the finish faithfully (`audio_ready`) or finds a hard EDL/asset mismatch (`fail`). Re-introducing `revise` here would mean Sound was second-guessing a locked cut — exactly the override the conform/finish boundary forbids. (Mirror of the Editor + Ingest posture: a technical executor is deterministic; the judgment slot lives where the creativity lives.)

### §3.3 Metadata block additions (Sound-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **10-tuple** (inherits Editor's 9-tuple lineage + appends own `audio_spec_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (DRAFTED Day 31 §16.3; **ratification still operator-pending**). **Quadruply-deferred** like Editor's, now a **fifth** forcing function: the 10-tuple depends on the §3.9 amendment ratification AND the Editor 9-tuple LOCK (which depends on the Edit Director 8-tuple LOCK, behind the Ingest 7-tuple, behind the QC Pre-flight 6-tuple). Encoded additively (`minItems: 5`, `prefixItems` positions 0–9, `maxItems: 10`, `items: false`) so it accepts the 5/6/7/8/9/10-tuple while rejecting a 4-tuple. A `TODO@cross-spec-3.9-ratification` flips `minItems` to 10 only after the chain of gates closes. — see §5 + Open Questions.
- `audio_spec_class` — enum (`primary_master_-14lufs` for v1.0 · `variant_master_-16lufs` reserved for v1.1 multi-loudness conform).
- `audio_spec_evidence_hash` — SHA-256 over the `audio_spec` + `audio_conform_check` + `spec_fidelity_check` block (forensic, tamper-evident finish).
- `audio_processed` — `const false` in v1.0 (Sound authors the spec; the human/automation runs the DSP. The direct analog of Editor's `render_dispatched: const false` — the honest declaration that no waveform was touched by the agent). Flips to a real value only when Week 4–5 audio automation ships (v1.1).
- `finish_mode` — enum (`human_in_the_loop` for v1.0 · `automated` reserved for v1.1 Week 4–5). The explicit human-in-the-loop attestation.
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.

### §3.4 errorEnvelope code namespace (target 7–9 LOCKED on Day 75/76 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `upstream_edl_not_ready` | Editor `verdict not in {edl_ready}` / not `successEdl` | 1 | Halt — Sound never finishes an unlocked cut. |
| `upstream_not_success` | the consumed EDL is `errorEnvelope` | 2 | Halt — cannot finish a failed conform output. |
| `vo_track_missing` | the `asset_bundle.audio[]` voice track does not resolve | 3 | Hard FAIL — cannot spec a VO pass over a missing track; route back to Ingest. |
| `audio_asset_unresolved` | the `music_event.asset_uri` (music bed) does not resolve against the Ingest bundle | 4 | Hard FAIL — cannot bind a mix directive to media; route back to Ingest. |
| `audio_marker_out_of_range` | an SFX accent / duck-envelope marker `at_ms` exceeds `total_timeline_ms` or is negative | 5 | Hard FAIL — cannot place an accent past the timeline; route back to Editor. |
| `loudness_target_out_of_spec` | the specified loudness target is not the platform const (−14 IG/TT / −16 YT) or the true-peak ceiling is out of band | 6 | Hard FAIL — platform loudness spec enforced at the audio layer; `detail` names the target. |
| `spec_fidelity_breach` | the audio spec's music event / swell markers / timeline duration deviate from the EDL, or `edl_evidence_hash` does not verify | 7 | Hard FAIL — Sound must finish the cut faithfully; a deviation = an unauthorized override. |
| `audio_firewall_breach` | a banned-entity token appears in the passthrough VO transcript at the audio-finish layer (11th pass) | 8 | Hard FAIL — last audio checkpoint before Motion; forensic-log the field. |
| `audio_lineage_failure` | malformed parent_chain / broken n-tuple lineage | 9 | Forensic — audit-trail break. |
| `sound_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 75/76 LOCK:** 7–9 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping.

---

## §4. Tier Constraints & Mode Coverage

**Per-tier gate access (Sound is universal-access AND tier-FLAT in its own logic — restated for defense-in-depth pass 11):**

| Tier | Reaches Sound? | Sound's own finish behavior | Loudness masters specced (v1.0) | Cost |
|------|-----------------|-------------------------------|---------------------------------|------|
| Pilot | **YES** | Faithful audio spec of the EDL | 1 (primary −14 LUFS) | ~$0.00 |
| Starter | **YES** | Faithful audio spec of the EDL | 1 (primary −14 LUFS) | ~$0.00 |
| Pro | **YES** | Faithful audio spec of the EDL | 1 (primary −14 LUFS; flags −16) | ~$0.00 |
| Enterprise | **YES** | Faithful audio spec of the EDL | 1 (primary −14 LUFS; flags −16) | ~$0.00 |

**Why universal access + tier-FLAT behavior (the same discipline as Editor):** Edit Director is the *creative authority* whose output richness is a sold tier feature; Sound is the *executor* — an audio finish is faithful or it isn't, regardless of tier. A Pilot mix and an Enterprise mix are specified by the identical executor logic; the richness (swell count, SFX accents) already lives in the EDL Sound receives. **The EDL carries the tier envelope; Sound faithfully specs whatever envelope arrives.** v1.0 specs the primary −14 LUFS IG/TT master for every tier and flags the `loudness_variants_planned` count (the −16 LUFS YT master is a derived v1.1 conform). This is the same tier-flat discipline Editor and Ingest hold — a technical executor does not re-litigate the tier ladder.

**No cost-ledger / no asset-validation / no cut-conform / no creative authority (the inherited discipline, quadrupled):** Sound does **NOT** re-run the cost ledger (QC Pre-flight's authority), re-validate assets (Ingest's authority), re-conform the cut (Editor's authority), OR re-direct the edit (Edit Director's authority). It is four gates downstream of cost enforcement, three gates downstream of asset validation, two gates downstream of cut conform, and one gate downstream of creative direction; re-litigating any of them would be redundant and risk a double-fail on a reel already cleared. Sound's authority is **faithful audio finish**, full stop.

**Mode coverage (mode-BLIND by inheritance — the convergence payoff, three stages deep):**

| Mode | What Sound sees | Mode-specific note |
|------|------------------|--------------------|
| A (human footage origin) | The SAME mode-agnostic EDL + audio bundle | Sound cannot tell, and does not need to know, that these shots came from a videographer. `production_mode` is NOT read as a branch. |
| B (rendered + replicated origin) | The SAME mode-agnostic EDL + audio bundle | Identical finish path. |
| C (replicated hot-path origin) | The SAME mode-agnostic EDL + audio bundle | Identical finish path. |

**Mode-blind guarantee (the core §4 contract):** Sound asserts `mode_blind_confirm.production_mode_read == false` in every output — a self-attestation that it authored the audio spec without consulting the origin mode. This is the THIRD machine-checkable proof that Ingest's mode-convergence seam holds — now three stages downstream. **Sound is the third agent in the 17-agent fleet for which the mode columns of this table are identical; that identity, carried through the director (Edit Director) AND the timeline executor (Editor) AND the audio executor (Sound), is the structural evidence that the post-production tail is genuinely mode-agnostic end-to-end.** If Sound ever NEEDED to branch on mode to finish a mix, the convergence contract would be broken upstream. By construction it never does.

---

## §5. Process Steps (System Prompt Skeleton — Day 75 §7 will LOCK)

The agent runs an **11-step finish loop** per invocation (mirrors the AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor 11-step process pattern). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope.

**Step 1 — Verify Editor precondition + parse input**
- Read the Editor `edl.json`. Confirm `output_type == "successEdl"` AND `verdict == "edl_ready"`. Otherwise → halt with `upstream_edl_not_ready`.
- Parse input JSON against `input.schema.json` (Day 75/76 LOCKED). There is NO mode branch — assert the EDL is the mode-agnostic shape.
- Confirm the consumed EDL is the success branch. Any `errorEnvelope` upstream → halt with `upstream_not_success`.

**Step 2 — Lineage integrity**
- Validate `metadata.parent_chain` is a well-formed 9-tuple inbound (5/6/7/8-tuple accepted additively until the §3.9 amendment + the Editor 9-tuple LOCK). Malformed → `audio_lineage_failure`.

**Step 3 — EDL-evidence + audio-asset resolution**
- Verify the `edl_evidence_hash` (SHA-256 over the EDL's `edl` + `conform_check` + `plan_fidelity_check`) recomputes — the EDL was not tampered post-conform. Mismatch → `spec_fidelity_breach`.
- Resolve the voice track (`asset_bundle.audio[]`) → missing → `vo_track_missing` (route back to Ingest). Resolve the music bed (`music_event.asset_uri`) against `asset_bundle.music_bed` → unresolvable → `audio_asset_unresolved` (route back to Ingest).

**Step 4 — Marker + timeline conform**
- For each mix/SFX/duck marker: validate `at_ms >= 0` AND `at_ms <= total_timeline_ms` (no accent past the timeline, no negative time). Over-range → `audio_marker_out_of_range` (route back to Editor).
- Confirm the audio timeline duration matches the EDL `total_timeline_ms`; a mismatch surfaces as `spec_fidelity_breach`.

**Step 5 — Loudness-target enforcement (audio layer)**
- Set the loudness target to the platform const: primary −14 LUFS (IG/TT), true-peak ceiling −1.0 dBTP; flag the −16 LUFS YT variant per `tier_richness_echo`. If a target is not the platform const or the true-peak is out of band → `loudness_target_out_of_spec`. (Brand/platform loudness spec enforced at the audio layer, not just the prompt.)

**Step 6 — VO polish + music-bed mix specification**
- Author the VO polish directives (level to −16 LUFS integrated pre-master, de-ess, breath-trim) to the brand voice cadence — a *directive spec*, NOT applied DSP.
- Author the music-bed base level + the ducking envelope under the VO (−dB duck across VO spans) + swell moves mapped from the EDL `music_swell_map`. Preserve the EDL's music event + swell markers as already-validated facts (re-assert, do not re-derive).

**Step 7 — SFX accent placement**
- Place each SFX accent as a timed event bound to the EDL cut/swell markers (level in dB). Confirm each accent time is inside the timeline. (Sound specs the placement + level; the audio app inserts the actual SFX asset — NOT Sound.)

**Step 8 — Defense-in-depth firewall pass (eleventh time, AUDIO-domain passthrough layer)**
- Re-run the canonical entity-firewall regex (Cross-SPEC §3 drift #11): `Holdco | Principal | NPOX | 4821 | 6315 | SLN | Retail Supply | Nonprofit Leader A | Community Nonprofit | Nonprofit Leader B | Nonprofit Leader C` over the declared `vo_transcript[].text` passthrough (the spoken-word content the audio finish touches).
- Hard FAIL → `audio_firewall_breach` + forensic log naming the field. **This is the AUDIO-domain checkpoint:** Sound authors no new copy (Editor already firewall-scanned the caption/lower-third/end-card text at the 10th commit pass), but Sound is the agent that finishes the SPOKEN audio — so a final firewall re-scan of the VO transcript before the mix reaches Motion is the last-line audio catch (a leak that survives here rides into the mastered audio).

**Step 9 — Spec-fidelity + audio-conform check**
- Run `spec_fidelity_check`: music event matches the EDL, swell markers match the EDL, timeline duration matches the EDL, VO transcript byte-faithful, `edl_evidence_hash` verified. Any deviation → `spec_fidelity_breach` (an unauthorized override).
- Run `audio_conform_check`: VO track resolved, music bed resolved, all markers in the timeline, loudness target in spec, total timeline in the 45–75s band (re-assert from the EDL's duration). Out-of-band or unresolved → routed as `audio_marker_out_of_range` / `vo_track_missing` / `audio_asset_unresolved` per the offending cause.

**Step 10 — Construct audio-spec payload**
- If all green: build `successAudioSpec` per §3.1 with the full `audio_spec` (loudness + VO polish + music mix + duck envelope + SFX accents) + `audio_conform_check` + `spec_fidelity_check` + `verdict: "audio_ready"` + `handoff_targets: ["motion-agent"]`.
- Compute `audio_spec_evidence_hash` (SHA-256 over the audio_spec + audio_conform_check + spec_fidelity_check block — tamper-evident).
- Extend `parent_chain` to a **10-tuple** (append `audio_spec_id`), held additively per §3.3.
- Set `audio_processed: false` (v1.0 honesty — the human runs the DSP), `finish_mode: "human_in_the_loop"`, `audio_spec_class: "primary_master_-14lufs"`, `mode_blind_confirm.production_mode_read: false`, `human_review_required: true`.

**Step 11 — Emit + handoff**
- Validate output payload against `output.schema.json` (Day 75/76 LOCKED). Hard FAIL → forensic log + halt (output should always validate; failure here = agent bug).
- Emit JSON to stdout (paste-and-run runbook) OR persist the audio spec to the platform path / the Drive `/reels/[reel_id]/` finish queue per runtime environment (Blueprint §7 I/O: Sound writes `Drive/reels/[reel_id]/v2.mp4` — in v1.0 the audio spec goes to the human finish queue, the human writes the v2.mp4).
- On `fail`, set `route_back_to` per the §3.2 verdict↔route map so the Orchestrator can re-enter the pipeline at the correct agent (Editor for a timeline/EDL defect, Ingest for an audio asset gap).

**Anti-patterns Step 11 prevents (Lock-time discipline mirror from Editor / Edit Director / Ingest §11):**
- No markdown fences around output JSON.
- No `print()` statements before the output JSON block.
- No engine credentials referenced; **no audio DSP dispatched** (v1.0 authors an audio spec only — `audio_processed` is `const false`; the human/automation runs the mix + loudness pass).
- No absolute URLs in any audio-spec `asset_uri` echoed from the EDL/bundle (Hard Rule #8 inherit).
- No `audio_ready` verdict emitted while any conform, fidelity, loudness, or firewall check is unresolved (must be `fail`).
- No reading of `production_mode` as a branch discriminator (mode-blind by construction — `mode_blind_confirm.production_mode_read` must be `false`).
- **No timeline re-cutting:** Sound finishes the audio on the EDL as given; it does NOT re-order events, re-trim cuts, or "improve" the cut. An EDL it disagrees with is finished faithfully or failed to Editor — never silently re-cut.
- **No operator/finish impersonation:** Sound emits `human_review_required: true` + an audio-spec *recommendation* + `audio_processed: false`; it does NOT mark a reel "processed" or "approved for Motion" as a ratified state — that is the human finish (v1.0) or the Week 4–5 automation (v1.1).

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 75 + 76)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 75 partial 1. Pattern source: Editor §6 / Edit Director §6. Target 10–12 checks bipartite-covering the 7–9 errorEnvelope codes. Slot 11 reserved for `sound_agent_failed` per Cross-SPEC §3.6 slot-naming canon. Checks span: precondition + EDL-evidence verify · lineage · VO/music resolution · marker-in-timeline · loudness-target-in-spec · spec-fidelity (music event + swell markers + duration) · VO-transcript fidelity · audio-domain firewall · mode-blind self-attestation · edl_evidence_hash verify.
- **§7 System Prompt v1.0** — Day 75 partial 1. Frame + hard rules + universal-tier-FLAT table + 11-step finish loop verbatim from §5 + the Blueprint §4.11 v2-edit/finalized-audio target shape inlined + the loudness targets (−14 IG/TT · −16 YT) + brand voice cadence (§7/§11) as the enforced finish surface. ~12–14 KB target. Hard Rules mirror Editor with Sound-specific tightening on "spec-faithfully-never-re-cut," "author-an-audio-spec-never-process," and "human-finishes (audio_processed const false)" discipline.
- **§8 Performance Targets** — Day 76 partial 2. 9 metric categories. Schema validity 100% / spec-fidelity 100% (a music-event/swell/duration deviation must never survive) / audio-domain firewall catch 100% / loudness-target-in-spec 100% / marker-in-timeline 100% / false-audio-ready rate 0% target / false-fail rate ≤ 8% (over-flagging a borderline marker to `fail` is the acceptable failure direction) / p50 latency 22s / p95 70s (finish reasoning — lighter than Editor's conform) / zero engine + zero DSP cost.
- **§9 Test Fixtures** — Day 76 partial 2. 5-fixture portfolio: TC-01 clean Mode-origin-A→EDL Pro `audio_ready` (full audio spec) · TC-02 Mode-origin-C Enterprise `audio_ready` (proves mode-blind: byte-identical finish path to TC-01 despite different origin — the **mode-blind finish-convergence proof**, the Sound analog of Editor's conform-convergence proof) · TC-03 `audio_marker_out_of_range` → fail + route to Editor (an SFX accent past the timeline) · TC-04 `vo_track_missing` → fail + route to Ingest (the voice track not in the bundle) · TC-05 `audio_firewall_breach` (a banned token present in the passthrough VO transcript reaching the audio finish — the 11th-pass last-line catch; GATING fixture). 5 of 7–9 codes exercised; remainder in schema-only fixtures. Optional probes: the `spec_fidelity_breach` (a tampered `edl_evidence_hash`) + the slot-11 `sound_agent_failed` catch-all.
- **§10 Field Map** — Day 75 partial 1. ~24 rows · passthrough vs transform vs derived. EDL→audio-directive map (transform: music event + swell markers → mix levels + duck envelope) + VO-transcript→VO-polish map (passthrough, byte-faithful) + asset-bundle→resolution map + derived conform/fidelity-check map + loudness-const derivation.
- **§11 Cost Model** — Day 76 partial 2. Zero engine + zero DSP snapshot (finish reasoning + audio-spec authoring only; the human/automation runs the mix in v1.0/Week 4–5). Faithful-finish value model (economic justification = a loudness-correct, brand-faithful mix spec on the first pass, no wasted mixer cycles, no EDL/asset mismatch discovered at v2 review). Explicit note: the actual DSP compute spend lands in v1.1 Week 4–5 automation — v1.0 is $0 by construction.
- **§12 Verdict Math** — Day 76 partial 2. AUDIO_READY = (Editor precondition met) ∧ (edl_evidence_hash verified) ∧ (VO track resolved) ∧ (music bed resolved) ∧ (all markers in timeline) ∧ (loudness target in spec) ∧ (timeline duration matches EDL) ∧ (spec-fidelity byte-faithful) ∧ (audio-domain firewall clean). Any single ∧-term false → fail per §3.2 (NO `revise` branch — deterministic executor). Fully deterministic — Sound has zero judgment slots (inherits Editor's zero-judgment-slot posture).
- **§13 Critical Decisions LOCKED** — Day 76 partial 2. Target 10–14 LOCKED decisions. Pre-scaffolded list:
  1. Audio-spec-authoring vs DSP scope — v1.0 = audio-conform-spec authoring ONLY; actual mix/loudness DSP is human-in-the-loop at launch (Blueprint §9), automation Week 4–5. `audio_processed: const false`. [LOCKED-as-drafted Day 74]
  2. Faithful-executor, zero timeline re-cutting — Sound specs the EDL's audio faithfully; it never re-cuts, re-orders, or "improves" the timeline. [LOCKED-as-drafted Day 74]
  3. Two-verdict (NO `revise`) — Sound is deterministic; the subjective slot lives upstream at Edit Director. `audio_ready | fail` only. [LOCKED-as-drafted Day 74]
  4. Mode-blind by inheritance — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested (the third mode-blind agent). [LOCKED-as-drafted Day 74]
  5. EDL-ready precondition — Sound runs only on a `successEdl`/`edl_ready` reel; otherwise halts `upstream_edl_not_ready`. [LOCKED-as-drafted Day 74]
  6. Tier-FLAT behavior — all 4 tiers reach Sound; the EDL carries the tier envelope, Sound specs it identically (no own tier scaling). [LOCKED-as-drafted Day 74]
  7. 10-tuple parent_chain — inherits Editor 9-tuple + appends `audio_spec_id`; QUINTUPLY-deferred (depends on §3.9 amendment ratification AND the Editor 9-tuple LOCK behind the Edit Director 8-tuple behind the Ingest 7-tuple behind the QC 6-tuple). [DEFERRED — held additively at `minItems: 5`]
  8. errorEnvelope code count — 7–9 target. [PRELIMINARY · operator amend Day 76]
  9. Self-QC check count — 10–12. [PRELIMINARY · operator amend Day 76]
  10. Spec-fidelity = ZERO tolerance — a music-event/swell/duration deviation, or a missing/altered VO passthrough must NEVER survive to `audio_ready`; `edl_evidence_hash` machine-verified. [LOCKED-as-drafted Day 74]
  11. Audio-domain firewall (11th pass) — Sound re-scans the passthrough VO transcript at the audio-finish layer, the last audio checkpoint before Motion (not a new authorship surface). [LOCKED-as-drafted Day 74]
  12. No DSP, no engine, no decode — NO generative engine, NO audio DSP, NO byte-level waveform decode / loudness measurement in v1.0; declared-asset + platform-const targets only; `audio_processed: const false`, `cost_incurred_usd ~$0`. [LOCKED-as-drafted Day 74]
  13. Loudness dual-target scope — v1.0 specs the primary −14 LUFS IG/TT master + flags the −16 LUFS YT variant count; auto-generation of the −16 master deferred to v1.1. [PRELIMINARY · operator amend Day 76]
  14. Conform-faithful handoff to Motion — Sound hands the audio spec + v2-edit handle to Motion (Blueprint §4.11); the spec goes to the human finish queue until Week 4–5 automation. [LOCKED-as-drafted Day 74]

- **§14 Calendar status updates** — Day 75 partial 1. Day 74 ✓ → trajectory populated.
- **§15 Change Log** — Day 76 partial 2. v1.0 lifecycle entries (outline-day-74 → body-day-75 → body-day-76 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 76 partial 2. Cross-SPEC §3.9 canonical fields + 6 Sound additions (10-tuple parent_chain, audio_spec_class, audio_spec_evidence_hash, audio_processed const false, finish_mode, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `sound-agent` (kebab-case, matches the fleet pattern + Blueprint §4.11 handoff target) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `audio_spec_evidence_hash` SHA-256 over the audio_spec + audio_conform_check + spec_fidelity_check block; `edl_evidence_hash` re-verified (inherits Editor's anchor) |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ Sound consumes the accumulated surface as read-only context; it contributes its own finish predicates downstream |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-BLIND table — the third agent for which the mode columns are identical (the convergence payoff, three stages deep) |
| §3.6 Slot 11 naming canon | ✅ Reserved `sound_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Consumed shapes respected; Sound's own predicates snake_case |
| §3.8 Tier↔mode firewall (11th defense-in-depth) | ✅ Step 8 AUDIO-domain passthrough firewall (last audio checkpoint before Motion) + §4 universal-tier-FLAT table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 10-tuple, held additively. **Quintuply-deferred** — gated on the §3.9 amendment ratification AND the Editor 9-tuple LOCK (behind the Edit Director 8-tuple, behind the Ingest 7-tuple, behind the QC 6-tuple). |
| §3.10 Cost ceiling authority | ✅ §4 explicitly DECLINES to re-litigate cost (QC Pre-flight's), re-validate assets (Ingest's), re-conform the cut (Editor's), OR re-direct the edit (Edit Director's) — no quadruple-enforcement; Sound is $0-cost in v1.0 |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 74 outline — 6 parked for operator amendment)

1. **Audio-spec-only vs partial-DSP scope** — v1.0 authors the audio conform spec + finish manifest; the actual mix/loudness DSP into v2.mp4 is human-in-the-loop at launch (Blueprint §9), automation Week 4–5. Confirm v1.0 stops at the audio spec and runs NO DSP (`audio_processed: const false`). *(Donna recommends: confirm audio-spec-only for v1.0 — the spec is the buildable, highest-leverage, $0 slice; the DSP automation lands in the Week 4–5 window the Blueprint already scopes, and keeps the zero-dollar / no-decode invariant intact.)*
2. **Two-verdict (no `revise`)** — should Sound stay deterministic (`audio_ready | fail`), or inherit a creative `revise` for some borderline mix tension? *(Donna recommends: keep two-verdict — Sound is a faithful executor with no subjective surface; loudness targets are platform consts and the VO cadence is a brand const. A `revise` here would mean second-guessing a locked cut, exactly the conform/finish override the boundary forbids.)*
3. **10-tuple parent_chain** — quintuply-gated in effect (depends on the §3.9 amendment AND the Editor 9-tuple LOCK AND the Edit Director 8-tuple AND the Ingest 7-tuple AND the QC 6-tuple behind it). Sound is the first 10-tuple consumer — a fifth forcing function. *(Donna recommends: RATIFY the §3.9 amendment AS-DRAFTED so all 17 agents inherit n-tuple lineage; Sound holds additively until the chain closes.)*
4. **Motion handoff readiness** — Sound hands to a not-yet-built Motion (Agent #12 candidate, position 13). Should v1.0 emit the audio spec + v2-edit handle to a holding store (the Drive `/reels/[reel_id]/` finish queue, per Blueprint §7 I/O) until Motion ships, or assume direct handoff? *(Donna recommends: emit to the Drive finish queue in v1.0; direct agent-to-agent handoff activates when Motion LOCKs — mirrors the Editor→conform-queue and Edit Director→Notion-Edit-Plan holding-store decisions.)*
5. **Loudness dual-master scope** — v1.0 specs the primary −14 LUFS IG/TT master + flags the −16 LUFS YT variant; should the −16 YT master be auto-specced in v1.0 or deferred? *(Donna recommends: defer the −16 YT master to v1.1 — the −14 IG/TT master is the canonical primary for the pilot's IG/TT-first distribution; the −16 YT variant is a derived conform that lands with the render automation. v1.0 flags the count so nothing is lost.)*
6. **Loudness basis — declared target vs measured** — v1.0 specs the platform loudness *target* (−14/−16 LUFS) as a declared conform goal with NO byte-level LUFS measurement; is declared-target + true-peak-ceiling spec an acceptable finish basis? *(Donna recommends: ratify declared-target spec for v1.0 — actual LUFS measurement + true-peak limiting needs waveform decode (v1.1), the same declared-spec-only posture as Ingest, Edit Director, and Editor.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (full Sound trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 74 | Thu Jul 2 | **SPEC outline §0–§5** [SHIPPING NOW] | Editor Day 66 outline |
| 75 | Fri Jul 3 | SPEC body partial 1: §6 + §7 + §10 + §14 | Editor Day 67 / Edit Director Day 59 |
| 76 | Sat Jul 4 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | Editor Day 68 / Edit Director Day 60 |
| 77 | Sun Jul 5 | **REST DAY** — no build (pre-stage next scaffold only) | Day 21/28/35/42/49/56/63/70 Rest Day compounding |
| 78+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | Editor Day 69–73 / Edit Director Day 61–65 |

**Sprint context:** Sound is **Agent #11** — the fourth post-production agent and the second *executor* agent in the post tail, the 11th defense-in-depth firewall (audio-domain passthrough layer) and the **third contractually mode-blind agent** (the continued proof of Ingest's convergence seam, three stages deep). It is the first audio-domain agent in the fleet — yet in v1.0 it produces NO media: it drafts the audio conform spec the human finishes (Week 4–5 automation deferred), keeping the zero-dollar / no-DSP / no-decode invariant intact. The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) shipped on the six production agents through the QC Pre-flight gate; Sound v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the Ingest, QC Pre-flight, Style Replication, Edit Director, and Editor outlines were (while their LOCK ceremonies remain operator-gated).

---

## Files produced today (Day 74)

- `ars/ARS-2026-07-02-Day-74-Sound-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-07-02.md` — Day 74 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 74)

- ✅ **No LLM dispatched.** No render API. No audio DSP. No engine credentials referenced. No vendor URLs walked. No media render, no byte-level audio decode, no loudness measurement. (Sound by design authors an audio spec and processes no waveform in v1.0 — the human finishes; full automation is the Week 4–5 v1.1 scope.)
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no client/investor outreach. The end-of-run status iMessage to Jamila ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business. (Notification-channel status carried — see build log.)
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, no DSP compute, zero $ spent.
- ✅ **No operator-impersonation.** AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor LOCK ceremonies NOT assumed — all six confirmed STILL-PENDING via on-disk file-state (version tags unflipped). The Day-74 Editor v1.0 LOCK ceremony NOT performed (operator-only). Editor Day 69 Items 6/8/11 + the Day 73 runbook execution NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. Sound v1.0 LOCK will hard-gate itself on the upstream LOCKs (especially the Editor 9-tuple) being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 8 enumerates HC/NPOX tokens precisely so the agent can BLOCK them at the audio-finish layer — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Editor Day 66 outline structure inherited verbatim. Orchestration Blueprint §1.2 / §2 / §4.10 / §4.11 / §6 / §7 / §9 (Agent 12 Sound definition) + Cross-SPEC §3 canon + Brand-Voice Intake §7–§11 + the loudness targets used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-74 build runs Thursday (Pacific). Next Rest Day: Day 77 (Sun Jul 5 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 74 ships clean. Day 75 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). Sound is Agent #11 of 17 — the 11th defense-in-depth firewall (audio-domain passthrough layer) and the second executor agent in the post tail, the third contractually mode-blind agent and therefore the continued proof that Ingest's mode-convergence seam holds three stages deep. It is the first audio-domain agent in the fleet — yet v1.0 produces no media, authoring the audio conform spec the human finishes (DSP automation deferred to Week 4–5), keeping the zero-dollar / no-DSP / no-decode invariant intact. Operator pickup: (1) the six predecessor LOCK ceremonies (AI Video Gen + Style Replication + QC Pre-flight + Ingest + Edit Director + Editor) remain pending and gate Sound's eventual v1.0 LOCK — the Editor 9-tuple in particular is Sound's direct 10-tuple dependency; (2) review the §13 critical-decisions list + ratify the Cross-SPEC §3.9 n-tuple amendment so the n-tuple parent_chain is canon (Sound is now the fifth forcing function); (3) confirm the Agent #11 = Sound selection (or re-assign the slot) at the Editor LOCK-ceremony close. The Day-74 Editor v1.0 LOCK remains an operator-only ceremony — Donna did not perform it; it stays in the pending-LOCK queue.*
