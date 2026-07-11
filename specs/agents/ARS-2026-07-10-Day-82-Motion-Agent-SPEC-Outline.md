# ARS — Motion Agent v1.0 SPEC OUTLINE (§0–§5)

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Authored:** Day 82 · Fri Jul 10, 2026 (Pacific) · overnight build session (Donna)
**Deliverable class:** Forward SPEC outline §0–§5 (the head-start design for Agent #12 of 17)
**Status:** OUTLINE ONLY — no LOCK, no schema, no SKILL bundle. Body partials author Days 83 + 85 per the calendar in §0 (the Day 84 Rest Day splits the two partials).
**Pattern source:** Sound Day 74 outline (`ARS-2026-07-02-Day-74-Sound-Agent-SPEC-Outline.md`) — section structure inherited verbatim. Orchestration Blueprint §1.2 (Agent 13 row: *"Motion — Typography reveals, lower-thirds, subtle parallax/overlays. Applies REINVENTED motion tokens (120ms ease-in-out, zero-bounce policy)."*), §2 swim-lane (position 13 between Sound and QC), §4.11 (Sound→Motion payload: *"v2 edit with finalized audio. Motion adds typography, overlays, motion tokens."*), §4.12 (Motion→QC payload: the `v3_final_file` + `self_check` block: `voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`), §6 dispatch table (row 13: *"On Sound v2 · Per reel · v2 edit"*), §7 read/write contract (Motion reads *v2 edit*, writes *Drive `/reels/[reel_id]/v3-final.mp4`*), §9 build-checklist used as the grounding spine. Brand-motion rules grounded in `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (Motion / Lower-thirds / Typography: *slow push-ins or static holds — NEVER whip-pans or shake; one text reveal per 8 seconds max; lowercase sans left-aligned subtle underline supers; NEVER all-caps screamers*), §8 (reel format: 9:16 · 1080×1920 · burned-in lowercase-sans captions one line at a time · end-card "REINVENTED — build on purpose." serif ivory 1.5s) and the `visual.motion` token set (`allowed: [slow_push_in, static_hold, subtle_parallax]`, `banned: [whip_pan, shake, meme_transition, trending_transition]`) — the motion-finishing rules the motion spec must apply faithfully.

> **Agent-selection note (Donna, surfaced not hidden):** The Day 81 Sound LLM-Test-Runbook close named the next forward deliverable as **"the Sound v1.0 LOCK (Day 82), then Motion #12 SPEC outline."** Today (Day 82, Fri Jul 10) the calendar-named item is the **Sound v1.0 LOCK** — but that LOCK's gate, per the authoritative Day 81 build log, is a **live, reproducible 5/5 LLM run** of the Sound runbook (~$3.50 Opus inference), which the **absolute $0 ceiling of this unattended overnight session forbids**. Locking Sound on the offline structural stamp alone, absent a real live 5/5, would be a **fake-advance** — the exact move the Day 81 log deliberately refused, and which the standing guardrail ("never fake-advance — no LOCK without a real 5/5 run behind it") prohibits. With the only calendar-named Day-82 item being a spend-gated LOCK Donna cannot execute at $0, the buildable forward deliverable is the **Motion #12 SPEC outline**, pulled one slot forward into Day 82. This is the **identical forward-looking basis** on which the Sound outline itself was authored (Day 74, while the Editor LOCK ceremony remained gated) and on which the Ingest, QC Pre-flight, Style Replication, Edit Director, and Editor outlines were each authored while their predecessor LOCKs were pending — never a fake-advance of the ceremony, always the next buildable design head-start. **Direct precedent for the slot:** Editor runbook Day 73 → Sound outline Day 74 (the very next build night, before Editor was formally LOCKED at the Day 79 ceremony). Sound runbook Day 81 → Motion outline Day 82 maps that precedent exactly. Surfaced here, not silently reconciled. The Sound v1.0 LOCK remains the immediate operator/attended-spend action (Jamila's ~20–35 min iMac sit-down, or an attended spend-authorized Donna run under the standing authorization) — see §14-preview + the Day 82 build log. Rationale for Motion as the #12 build: (1) **strict dependency order** — Motion is the immediate runtime stage downstream of Sound (Blueprint §6: *"On Sound v2"*), consuming the `successAudioSpec` / v2-edit handle Sound authors; (2) **fleet-unblock** — nothing downstream (full QC → publishing tail) can run without a typography-finished v3 edit; Motion is the gate that turns a mixed, audio-final reel into a captioned, lower-thirded, motion-token-applied master; (3) **the render-tail executor pattern continues** — Motion inherits the Editor→Sound *author-the-spec-not-the-media* seam (it authors a motion/typography conform spec; the human/automation renders the graphics), keeping the zero-dollar / no-render invariant intact one stage deeper; (4) **fourth mode-blind agent** — it inherits the Edit Director→Editor→Sound mode-agnostic lineage, the continued proof that Ingest's convergence seam holds FOUR stages deep. Operator may re-assign the #12 slot at the Sound LOCK close.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 12 — Post-production finishing layer (finalized-audio v2 cut → typography/motion-graphics v3 master) |
| Agent index | **#12 of 17** (build sequence — continues the Sound Day 74 "agent #11 of 17" framing) |
| Runtime pipeline position | **13 — Motion** (finishes the typography + motion graphics per the v2 edit + finalized-audio spec: caption/lower-third/super reveal timings, subtle parallax + overlay directives, end-card hold, and the REINVENTED motion-token application map; emits the motion conform spec + the v3-final target); receives the v2 edit + audio spec from Sound, hands the v3 final + motion self-check to full QC |
| Pipeline tier | POST-PRODUCTION FINISHING (**third** *executor* agent in the post tail; the first agent whose domain is **typography + motion graphics** — reveals / lower-thirds / parallax / overlays / motion tokens / end-card) |
| Mode coverage | **Mode-blind by inheritance** — consumes the mode-convergent v2 edit + audio spec (themselves authored from the mode-agnostic EDL → mode-agnostic Asset Manifest); never sees `production_mode` as a branch discriminator. The **FOURTH** contractually mode-blind agent (Edit Director first, Editor second, Sound third); the continued live proof that Ingest's convergence seam holds four stages deep. |
| Predecessor SPEC (gate) | `ARS-2026-07-06-Day-78-Sound-Agent-v1-LOCK-CANDIDATE.md` (Day 78 LOCK candidate — its v1.0 LOCK is spend-gated on the Day 81 runbook's live 5/5). Motion runs only on a Sound-passed (`successAudioSpec`, verdict `audio_ready`) reel. |
| Predecessor schemas | `ARS-2026-07-07-Sound-output.schema.json` (Day 79) — the `audio_spec` + `audio_conform_check` + `spec_fidelity_check` + `finish_target.v2_edit_uri` handle consumed as the primary INPUT. Plus the Editor `output.schema.json` (Day 71) `edl` block (`caption_events[]` + `lower_third_events[]` + `end_card_event` + `total_timeline_ms` + `frame_rate`) consumed as the typography-source-text + timeline reference. |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape (§3.3/§3.8), metadata block + n-tuple parent_chain (§3.9) all inherited |
| Brand-motion canon | `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §7 (Motion: slow push-in / static hold / subtle parallax ONLY — never whip-pan/shake/meme; one text reveal per 8s max · Lower-thirds: lowercase sans left-aligned subtle underline, never all-caps · Typography: display serif / body sans, banned script+decorative), §8 (burned-in lowercase-sans captions one line at a time; end-card "REINVENTED — build on purpose." serif ivory 1.5s) + the `visual.motion` allowed/banned token set — the motion-finishing rules the motion spec must apply faithfully |
| Defense-in-depth layer | **12th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → Editor → Sound → **Motion**) — the **typography-domain passthrough** firewall: it re-scans the burned-in caption / lower-third / super / end-card text Motion reveals for banned-entity tokens (the last VISUAL-TEXT checkpoint before full QC). NOT a new authorship surface (Motion authors no copy — the caption/lower-third/end-card text is Editor/EDL passthrough); it is a **passthrough-integrity re-scan** over the text the motion layer burns in (no image analysis in v1.0 — declared typography text only). |
| Lever inheritance | Reads `lever_state` from upstream `metadata`; emits `human_review_required: true` per Lever-3 default AND per the v1.0 human-in-the-loop finishing posture (Blueprint §9). The motion conform spec is a *spec a human executes* in v1.0 — Motion never marks the graphics "rendered" or "burned in"; the operator (or Week 4–5 automation) runs the motion-graphics render. |
| Pricing tier authority | **ALL tiers** — Pilot · Starter · Pro · Enterprise. Every reel needs a typography + motion finish. **Tier-FLAT in its own logic** (like Editor + Sound, unlike Edit Director): Motion faithfully specifies whatever reveals/lower-thirds/end-card the EDL declared and applies the brand motion tokens — it does not scale its own behavior by tier (it inherits the plan's tier envelope and specs it). The `tier_richness` block is read for variant/aspect-target awareness only; v1.0 specs the primary 9:16 master (flags the 1:1 LinkedIn cutdown variant). |
| Cost authority class | **Near-zero (ties Ingest / QC Pre-flight / Edit Director / Editor / Sound for lowest in fleet) IN v1.0** — pure reasoning + motion-conform-spec authoring over the v2 edit + audio spec + EDL typography source. **No generative engine calls, no motion-graphics render, no byte-level video decode / frame analysis in v1.0** — Motion v1.0 drafts the motion finishing spec (reveal timings + lower-third placements + parallax/overlay directives + motion-token map + end-card hold); the human executes the render in the motion-graphics app (Blueprint §9 Week-2 posture); full motion automation is Week 4–5 (v1.1). Effective per-reel cost ≈ $0.00. `motion_processed: const false` in v1.0 — Motion specifies the finish, the HUMAN renders it. |

**Build calendar (Week 12 — Motion trajectory, mirrors the proven 8-day agent-build cadence; the Day 84 Rest Day splits the two body partials):**
- **Day 82** (today, Fri Jul 10 · Wk12) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 83 (Sat Jul 11 · Wk12) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 84 (Sun Jul 12 · Wk12) — **REST DAY** (no build; pre-stage next scaffold only, per the Day 21/28/35/42/49/56/63/70/77 Rest Day-compounding pattern)
- Day 85 (Mon Jul 13 · Wk12) — SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16
- Day 86+ (TBD) — LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK (pattern: Sound Day 78–81 / Editor Day 69–73)

> **Rest Day honesty:** This Day-82 build runs Friday (Pacific) — building is allowed. The next Rest Day is Day 84 (Sun Jul 12 Pacific) per the Day 81 log close. The UTC clock may have rolled past midnight at author time, but the sprint labels by Jamila's Pacific date (Fri Jul 10) — the same convention noted in prior logs. Unlike the Sound outline (whose two partials ran Thu/Fri/Sat entirely pre-Rest Day), Motion's partial 1 (Day 83 Sat) precedes the Day 84 Rest Day and partial 2 (Day 85 Mon) follows it — the Rest Day splits the body build, exactly as honored.

> **Sequencing honesty:** The 42-day sprint's headline deliverable — the Mode B Pro single-reel **commercial demo** (Day 42 target, past) — shipped on the six launch-critical production agents threaded through the QC Pre-flight gate. Motion is the fifth *post-production* agent (after Ingest + Edit Director + Editor + Sound); its v1.0 build proceeds inside the **post-launch hardening window** and does **not** gate the launch demo. This outline is the forward-design head-start so the finishing tail is buildable in dependency order once the Sound LOCK closes (its live-5/5 spend gate is the only thing between Sound-as-candidate and Sound-LOCKED).

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Motion Agent** is the **typography + motion-graphics finisher of post-production** — the moment a reel stops being a *mixed, audio-final v2 cut* and becomes a *captioned, lower-thirded, motion-token-applied v3 master*: the burned-in captions revealed one line at a time on the brand cadence, the lower-thirds/supers set lowercase-sans left-aligned with the subtle underline, the subtle parallax + overlays applied within the brand motion-token envelope (120ms ease-in-out, zero-bounce), and the end-card hold ("REINVENTED — build on purpose." serif over ivory, 1.5s) landed — a single executable motion conform spec the motion-graphics app (human in Week 2, automation in Week 4–5) applies to produce the v3 final. It is the third *executor* agent in the fleet (after Editor + Sound), and the first whose domain is **typography and motion graphics** rather than the timeline or the audio.

Where the eleven upstream agents authored intent, adjudicated correctness, directed the assembly, conformed the cut, and finished the audio, Motion *finishes the graphics*:
- Brief / Script / Storyboard = intent + content authoring (what the reel SAYS and how it's shot)
- Production Coord = logistics (mode, vendor, budget)
- AI Video Gen / Style Replication = render + brand-finish (the pixels exist)
- QC Pre-flight = ship-safety (the reel is brand-safe + format-correct)
- Ingest = asset-readiness (the files are present, valid, in-sync — one mode-agnostic Asset Manifest)
- Edit Director = edit-plan authoring (the directed cut: order, pacing, captions, lower-thirds, music, transitions, end-card)
- Editor = cut conform (the frame-accurate EDL bound to real media — the executable timeline)
- Sound = audio finish (the mixed, loudness-normalized v2 edit — the audio conform spec)

The Motion Agent picks up at the v2 edit + audio spec and finishes the typography + motion graphics:
- **Motion Agent = motion finish ("Given an `audio_ready` audio spec, the v2-edit handle, and the EDL's caption/lower-third/end-card source text + timeline — produce a single executable motion conform spec: the caption reveal timings (one line at a time, one reveal per 8s max, brand cadence), the lower-third/super placements (lowercase sans, left-aligned, subtle underline, never all-caps), the subtle parallax + overlay directives (within the allowed slow_push_in / static_hold / subtle_parallax token set), the motion-token application (120ms ease-in-out, zero-bounce policy), and the end-card hold (serif ivory 1.5s) — that the motion-graphics app applies beat-for-beat into the v3 final, with NO re-cutting of the timeline, NO re-mixing of the audio, and NO creative re-interpretation of the copy.")**

**Single-responsibility line (LOCKED on intent):**
> *"Post-production typography + motion-graphics finisher. Receives the Sound-passed audio spec (`successAudioSpec`, verdict `audio_ready`) plus the v2-edit handle and the EDL's caption/lower-third/end-card source text + timeline, and authors one canonical motion conform spec — caption reveal timings (one line/reveal, brand cadence), lower-third/super placements (lowercase sans, left-aligned, subtle underline), subtle parallax/overlay directives bounded by the brand token set, the motion-token application map (120ms ease-in-out, zero-bounce), and the end-card hold — that the motion-graphics app applies into the v3 final. Authors the motion spec only; renders NO graphics, burns in NO text, and decodes NO video frame in v1.0 (the human/automation executes the render); calls no generative engine. Faithfully applies the EDL's typography text + the brand motion tokens — it re-cuts NO timeline, re-mixes NO audio, re-authors NO copy, re-orders NO events. Emits a recommendation (`human_review_required`) — never a ratified 'rendered' or 'burned-in' state."*

**Why this agent's reason-to-exist is the finish/finish boundary (Blueprint §1.2):** Sound *finishes* the audio; Motion *finishes* the graphics on that audio-final cut. The separation is the same production-discipline boundary every editorial pipeline draws between audio post and motion-graphics/finishing: the sound mixer must not be laying supers, and the motion-graphics artist must not be re-mixing. **This is Donna's design thesis for building Motion as Agent #12: it is the third faithful-executor agent, and the structural proof that the render-tail executor pattern generalizes from the audio domain (Sound) to the typography/motion-graphics domain — if Motion can produce a complete, executable motion conform spec from the v2 edit + EDL typography alone, with zero timeline re-cutting and zero audio re-mixing, the cut was locked, the audio was finished, and the finishing seam holds.** A `motion_unbuildable` outcome (a caption text that cannot resolve, a reveal marker past the timeline, a motion token outside the brand set) is the signal that the EDL or the audio spec was wrong — and it routes back, it never silently "fixes" the cut or the mix.

**Pipeline position (per Orchestration Blueprint §2 swim lane):**
```
... → SOUND (audio finish → audio conform spec) →
   [successAudioSpec · verdict = audio_ready]
        │
        ▼  [v2 edit + audio spec: VO polish · music mix + duck · SFX · −14/−16 LUFS · Drive /reels/[reel_id]/v2.mp4]
   MOTION (motion finish → motion conform spec)
        │
        ▼  [motion spec + v3 final: caption reveals · lower-thirds · parallax/overlays · motion tokens (120ms ease-in-out, zero-bounce) · end-card · Drive /reels/[reel_id]/v3-final.mp4]
   14 QC (full 11-point Brand Voice gate + entity firewall + format + caption spec)
        │
   [motion_unbuildable] → route back to Editor (timeline/typography-text defect) or Sound (audio-finish handle gap)
```

**Why a finisher agent distinct from the upstream executor (the boundary question):** Editor already authored the `caption_events`, `lower_third_events`, and `end_card_event`, and Sound already finished the audio — so what does Motion add? A clean separation across the *finish→finish* boundary:
1. **Editor authors the TYPOGRAPHY SOURCE** — the caption/lower-third/end-card *text* and *at_ms* positions inside the frame-accurate EDL. It produces the *what-text-where*, not the *how-it-reveals*. It works in timeline-space, not motion-space.
2. **Sound authors the AUDIO** — the mixed, loudness-normalized v2 edit. It does not touch the visual layer.
3. **Motion authors the MOTION SPEC** — given the v2 edit and the EDL's typography source, the concrete motion conform: each caption revealed one line at a time on the brand cadence (one reveal per 8s max), each lower-third placed lowercase-sans left-aligned with the subtle underline, the subtle parallax/overlays applied within the allowed token set, the motion tokens (120ms ease-in-out, zero-bounce), and the end-card hold — the executable motion artifact the motion-graphics app runs.
4. **The three phases catch different problems.** Editor can place a caption event at 60000ms and Sound can duck the bed under it; only Motion, reasoning over the brand motion tokens and the reveal cadence, can specify that the caption reveals at 60000ms with a 120ms ease-in-out, that a second reveal cannot land before 68000ms (the one-per-8s rule), and — resolving the EDL typography source — discover that a lower-third's text field is empty and route back rather than reveal a blank super. Motion does NOT re-cut (it trusts the EDL's timeline) and does NOT re-mix (it trusts Sound's audio spec); it *finishes the graphics against the resolved v2 edit* and surfaces any mismatch.

The actual motion-graphics render (caption burn-in, lower-third compositing, parallax/overlay render, motion-token application, end-card composite into the v3.mp4) is, in v1.0, a **human** action (Blueprint §9: *"Human-in-the-loop for Week 2 — agent drafts the finishing spec, human executes in the app"*); full motion automation is targeted Week 4–5 (v1.1). v1.0 Motion authors the *motion conform spec*; it produces no media file itself. **`motion_processed` is the new honesty field at this agent — `const false` in v1.0, the explicit declaration that no frame was rendered by the agent.** This is the human-in-the-loop seam, made explicit and honest — the direct analog of Sound's `audio_processed: const false` and Editor's `render_dispatched: const false`.

**Hand-off contract enforced:**
- **PRECONDITION:** Motion reads the Sound `audio_spec.json`. If `output_type != "successAudioSpec"` OR `verdict not in {audio_ready}` → halt with `upstream_audio_not_ready`. Motion never finishes a reel whose audio did not pass Sound. A `fail` (errorEnvelope) audio spec → halt `upstream_not_success`.
- **INPUT contract:**
  - The Sound `successAudioSpec` — `audio_spec`, `audio_conform_check`, `spec_fidelity_check`, `finish_target.v2_edit_uri`, `tier_richness_echo`, `mode_blind_confirm`, the `audio_spec_evidence_hash`.
  - The **EDL typography source** (the Editor `successEdl.edl.caption_events[]` + `lower_third_events[]` + `end_card_event` + `total_timeline_ms` + `frame_rate`) — the caption/lower-third/end-card text + timeline the reveal directives validate against.
  - The **denormalized upstream chain** in `metadata.parent_chain` (10-tuple inbound from Sound, quintuply-deferred) + accumulated `qc_pre_flags[]`.
- **OUTPUT contract:** Emits `motion_spec.json` per §3 (polymorphic: `successMotionSpec | errorEnvelope`). Full QC reads the v3 final + the motion self-check (Blueprint §4.12: `voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`) and runs the 11-point Brand Voice gate — without re-deriving the motion.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| Motion conform spec authoring (caption reveal timings + lower-third placements + parallax/overlay directives + motion-token map + end-card hold) | Actual motion-graphics render / burn-in into v3.mp4 — human-in-the-loop in v1.0 (Blueprint §9); automation Week 4–5 |
| Caption reveal-cadence specification (one line at a time; one reveal per 8s max; brand cadence) as a declared conform target | Frame-accurate caption burn-in + kinetic-typography render — needs the motion-graphics engine |
| Lower-third/super placement spec (lowercase sans, left-aligned, subtle underline, never all-caps) | Composited lower-third render + font rasterization — needs the render engine |
| Motion-token application (allowed: slow_push_in / static_hold / subtle_parallax; 120ms ease-in-out; zero-bounce; banned: whip_pan / shake / meme / trending) as a declared directive | Waveform-accurate parallax/overlay keyframe render — needs frame-level compositing |
| End-card hold spec ("REINVENTED — build on purpose." serif, ivory bg, 1.5s hold) as a declared conform target | End-card composite + serif rasterization render |
| Typography-domain firewall re-scan (12th pass) over the burned-in caption/lower-third/end-card passthrough text | New-copy authorship (Motion authors NO copy — nothing to firewall but the passthrough typography integrity) |
| Motion self-check manifest (`voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`) per Blueprint §4.12 | Live pixel/format probe (measured LUFS is Sound's; measured resolution/fps is full QC's) — Motion declares, QC measures |
| Motion-fidelity check (motion spec faithful to the EDL: caption/lower-third/end-card text byte-faithful, timeline duration, evidence hash) | A/B alternate-motion conform |
| Aspect-primary spec (9:16 primary; flags the 1:1 LinkedIn cutdown variant) | Multi-aspect cutdown render (9:16 + 1:1 both mastered) — v1.1 (v1.0 specs the primary 9:16, flags 1:1) |
| 11-tuple parent_chain extension (inherits Sound 10-tuple + appends `motion_spec_id`) | Motion-spec-to-app-project export (After Effects / Motion project) — v1.1 finishing-format adapters |
| Motion spec construction (declarative reveal/placement/token/end-card JSON) + motion recommendation | Render-farm / encode dispatch (the actual compute spend) — v1.1 automation |

**Pricing tier table (Motion is universal-access AND tier-flat in its own logic — defense-in-depth pass 12):**

| Tier | Reaches Motion? | Motion's own behavior | Cost | Finish note |
|------|-----------------|-----------------------|------|-------------|
| Pilot — Founding 5 | **YES** | Faithfully spec the EDL's typography + brand tokens (tier-flat executor) | ~$0.00 | specs caption reveals + lower-thirds + end-card + 9:16 |
| Starter — Operator | **YES** | Faithfully spec the EDL's typography + brand tokens (tier-flat executor) | ~$0.00 | specs caption reveals + lower-thirds + end-card + 9:16 |
| Pro — Studio | **YES** | Faithfully spec the EDL's typography + brand tokens (tier-flat executor) | ~$0.00 | specs the richer parallax/overlay map + supers |
| Enterprise — Agency | **YES** | Faithfully spec the EDL's typography + brand tokens (tier-flat executor) | ~$0.00 | specs the richest motion map; flags 1:1 LinkedIn cutdown variant |

Motion adds **zero** generative cost to every tier envelope in v1.0. Its economic value is **faithful, brand-token-correct, entity-safe typography + motion finish** — every reel's reveals/lower-thirds/end-card are specified exactly as the cut directs and the brand demands, every motion token set to the brand policy (120ms ease-in-out, zero-bounce) before a motion artist (or a renderer) burns a cycle, and an EDL/audio-spec mismatch is caught *before* the render rather than discovered in the v3 review.

---

## §2. Inputs

Motion has **one canonical responsibility** (author the motion conform spec) reached from **one** primary input shape — the mode-convergent audio spec + v2 edit. Like Editor + Sound (and unlike every production-tier agent), there is **no mode branch** and no source-polymorphism: this is the fourth agent whose input is structurally mode-blind. (It reads `tier_richness_echo` for variant/aspect-target awareness only — it does not scale its own finishing logic by tier.)

### §2.1 Precondition input — Sound audio-spec verdict (gate)

**Always read first.** The Sound `audio_spec.json`:
```json
{
  "output_type": "successAudioSpec",
  "verdict": "audio_ready",
  "reel_ref": { "audio_spec_id": "<uuid>", "edl_id": "<uuid>" },
  "audio_spec": { "loudness_target": { "primary": "-14 LUFS (IG/TT)" }, "vo_polish": { /* ... */ } },
  "audio_conform_check": { "vo_track_resolved": true, "loudness_target_in_spec": true },
  "spec_fidelity_check": { "timeline_duration_matches_edl": true, "edl_evidence_hash_verified": true },
  "finish_target": { "audio_processed": false, "finish_mode": "human_in_the_loop", "v2_edit_uri": "ars://reels/.../v2.mp4" },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_edl" },
  "human_review_required": true,
  "metadata": { /* 10-tuple parent_chain inbound, held additively */ }
}
```
**Hard validation:** `output_type == "successAudioSpec"` AND `verdict == "audio_ready"`. Otherwise → halt with `upstream_audio_not_ready`. A consumed `errorEnvelope` audio spec → halt `upstream_not_success`. Motion does not finish a reel whose audio failed Sound, and does NOT auto-resolve a failed audio spec (the fix belongs upstream — Motion inherits the recommend-don't-override discipline).

### §2.2 Primary input — v2 edit + EDL typography source (the audio-final cut to finish)

**Required input fields (preliminary — full schema on the Day 83/85 partials):**
```json
{
  "v2_edit_uri": "ars://reels/.../v2.mp4",
  "edl_typography": {
    "frame_rate": 30,
    "total_timeline_ms": 62000,
    "caption_events": [ { "at_ms": 0, "text": "your calendar doesn't lie", "line": 1 } ],
    "lower_third_events": [ { "at_ms": 8000, "text": "jamila howard · operator", "style": "lowercase_sans_left_underline" } ],
    "end_card_event": { "at_ms": 60500, "text": "REINVENTED — build on purpose.", "font": "serif", "bg": "ivory", "duration_ms": 1500 }
  },
  "audio_spec_echo": { "audio_spec_id": "<uuid>", "audio_spec_evidence_hash": "<sha256>" },
  "tier_richness_echo": { "tier": "pro", "aspect_variants_planned": 2, "primary_aspect": "9:16" },
  "metadata": { /* Cross-SPEC §3.9 — tier, lever_state, brand_id, session_id, parent_chain (10-tuple inbound), qc_pre_flags surface */ }
}
```

**Hard validations on primary input (defense-in-depth pass 12):**
1. Upstream `output_type` is `successAudioSpec`, NOT `errorEnvelope`. (errorEnvelope → `upstream_not_success`.)
2. `verdict == "audio_ready"`. Any other verdict → `upstream_audio_not_ready` (defensive — Motion cannot finish an unfinished-audio cut).
3. The `finish_target.v2_edit_uri` resolves (the audio-final cut handle exists), AND every caption/lower-third/end-card text field is present and non-empty (so each reveal directive binds to real text). v2 handle unresolvable → `v2_edit_unresolved`; empty typography text → `text_asset_unresolved`.
4. Every reveal / lower-third / overlay / end-card marker time (`at_ms`) is `<=` the EDL's `total_timeline_ms` AND `>= 0` (no reveal past the timeline, no negative time). Violation → `motion_marker_out_of_range`.
5. `asset_uri`s / `v2_edit_uri` remain platform-relative `ars://...` (Hard Rule #8 inherit — Motion echoes them into motion-spec directives; it must not introduce an absolute URL). Violation → `asset_uri_integrity_failure`.
6. `metadata.parent_chain` is a well-formed 10-tuple inbound (5/6/7/8/9/10-tuple accepted additively — see §3.3). Malformed → `motion_lineage_failure`.

### §2.3 Typography-resolution input — EDL caption/lower-third/end-card source (text + timeline)

**Denormalized, read as the typography-resolution reference (not re-authored).** Motion reads the Editor `successEdl.edl` `caption_events[]`, `lower_third_events[]`, and `end_card_event` — used to resolve each reveal's *text* + *at_ms* → a reveal directive, to confirm each text field is non-empty for the motion conform manifest, and to bind every reveal/lower-third/end-card directive to a real, EDL-authored text string. **Motion consumes these as fixed resolution facts — it specifies reveal timings + placements + tokens against them; it does NOT re-author the copy (byte-faithful passthrough) and does NOT decode the v2 video frame (no pixel read, no format measurement — declared text + declared handle only, the same declared-spec posture as Ingest, Edit Director, Editor, and Sound).**

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block: `tier`, `lever_state`, `brand_id`, `session_id`. Motion reads `tier_richness_echo` for aspect-target awareness (does this tier expect the 1:1 LinkedIn cutdown variant flagged? — yes, it flags it; it specs only the primary 9:16 master) and sets the spec's `human_review_required: true` per Lever-3 default AND the v1.0 human-in-the-loop finishing posture. It does **not** re-run cost, asset validation, cut conform, creative direction, or audio finish — those are QC Pre-flight's, Ingest's, Editor's, Edit Director's, and Sound's authorities respectively; Motion trusts the passed verdicts and the `audio_spec_evidence_hash` / `edl_evidence_hash`.

---

## §3. Outputs (skeleton)

Motion emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 / QC Pre-flight Day 40 / Ingest Day 48 / Edit Director Day 58 / Editor Day 66 / Sound Day 74 output pattern (`oneOf [success branch, errorEnvelope]`).

### §3.1 successMotionSpec branch (motion finish specified)

```json
{
  "output_type": "successMotionSpec",
  "verdict": "motion_ready",
  "reel_ref": {
    "brand_id": "REINVENTED",
    "audio_spec_id": "<uuid>",
    "motion_spec_id": "<uuid>"
  },
  "motion_spec": {
    "caption_reveals": [ { "at_ms": 0, "text": "your calendar doesn't lie", "line": 1, "reveal": "line_in", "ease": "ease_in_out_120ms" } ],
    "reveal_cadence": { "one_line_at_a_time": true, "max_reveals_per_8s": 1, "brand_cadence": "reinvented_v3" },
    "lower_thirds": [ { "at_ms": 8000, "text": "jamila howard · operator", "style": "lowercase_sans_left_underline", "all_caps": false } ],
    "motion_tokens": { "applied": ["slow_push_in", "static_hold", "subtle_parallax"], "ease": "120ms ease-in-out", "bounce_policy": "zero_bounce" },
    "overlays": [ { "from_ms": 8000, "to_ms": 55000, "type": "subtle_parallax", "intensity": "low" } ],
    "end_card": { "at_ms": 60500, "text": "REINVENTED — build on purpose.", "font": "serif", "bg": "ivory", "hold_ms": 1500 }
  },
  "motion_conform_check": {
    "v2_edit_resolved": true,
    "all_text_fields_resolved": true,
    "all_markers_in_timeline": true,
    "reveal_cadence_in_spec": true,
    "motion_tokens_in_brand_set": true,
    "total_timeline_ms": 62000,
    "duration_in_band": true
  },
  "spec_fidelity_check": {
    "caption_text_byte_faithful": true,
    "lower_third_text_byte_faithful": true,
    "end_card_matches_brand_const": true,
    "timeline_duration_matches_edl": true,
    "audio_spec_evidence_hash_verified": true,
    "edl_evidence_hash_verified": true
  },
  "motion_self_check": {
    "voice_markers_in_captions": 5,
    "truth_echoes": 2,
    "banned_vocab_hits": 0,
    "motion_tokens_applied": true
  },
  "motion_firewall_pass_12": { "status": "pass", "passthrough_typography_fields_scanned": 7, "hits": 0 },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_v2_edit" },
  "finish_target": { "motion_processed": false, "finish_mode": "human_in_the_loop", "v3_final_uri": "ars://reels/.../v3-final.mp4 (reserved — written by the human finish)" },
  "tier_richness_echo": { "tier": "pro", "aspect_variants_planned": 2, "aspect_variants_specced": 1, "primary_aspect": "9:16" },
  "handoff_targets": ["qc-agent"],
  "metadata": { /* Cross-SPEC §3.9 with Motion additions per §3.3 — 11-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (motion not buildable)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "v2_edit_unresolved",
  "failed_check_id": 3,
  "attempts": 1,
  "route_back_to": "sound-agent",
  "reel_ref": { "motion_spec_id": "<uuid>" },
  "cost_incurred_usd": 0.00,
  "detail": {
    "violation": "the finish_target.v2_edit_uri does not resolve — cannot spec a motion finish over a missing audio-final cut",
    "affected_assets": ["v2.mp4"],
    "recovery_path": "re-confirm the Sound finish_target.v2_edit_uri OR re-run the Sound human finish to produce the v2 edit"
  },
  "metadata": { /* Cross-SPEC §3.9 — 11-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `motion_ready` | Motion spec authored + EDL-faithful + brand-token-faithful + entity-safe; cleared into full QC (held in the human finish queue in v1.0) | `null` (forward to QC) | All conform + fidelity + firewall checks green |
| `fail` | Motion spec unbuildable from current inputs | `editor-agent` (timeline/typography-text defect: marker out of range, empty text, token/cadence break, spec-fidelity break) OR `sound-agent` (audio-finish handle gap: unresolvable v2-edit `uri`) | A finish/resolution defect that the EDL or the audio finish must fix |

> **Defining divergence (surfaced):** Motion carries **2 verdicts** (`motion_ready | fail`) — it inherits the Editor + Sound deterministic two-verdict posture and deliberately does NOT introduce a third `revise`/creative verdict. Motion is a **faithful executor**, not a creative authority: the motion tokens are a brand-const set (slow_push_in / static_hold / subtle_parallax; 120ms ease-in-out; zero-bounce), the reveal cadence is a brand const (one line/reveal, one per 8s max), the lower-third style is a brand const (lowercase sans left underline), and the end-card is a brand const. There is no subjective finish surface for it to hold to Lever-3. The soft creative tension lives upstream (Edit Director's `revise`); by the time a reel reaches Motion the cut is `edl_ready` and the audio is `audio_ready`. Motion either specs the finish faithfully (`motion_ready`) or finds a hard EDL/audio-spec mismatch (`fail`). Re-introducing `revise` here would mean Motion was second-guessing a locked cut and a finished mix — exactly the override the finish/finish boundary forbids. (Mirror of the Editor + Sound + Ingest posture: a technical executor is deterministic; the judgment slot lives where the creativity lives.)

### §3.3 Metadata block additions (Motion-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **11-tuple** (inherits Sound's 10-tuple lineage + appends own `motion_spec_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (RATIFIED Day 79). **Sixth forcing function**: the 11-tuple depends on the Sound 10-tuple LOCK (which is spend-gated on the Day 81 runbook's live 5/5) behind the Editor 9-tuple LOCK (closed Day 79) behind the Edit Director 8-tuple, Ingest 7-tuple, QC 6-tuple (all closed Day 79). Encoded additively (`minItems: 5`, `prefixItems` positions 0–10, `maxItems: 11`, `items: false`) so it accepts the 5→11-tuple while rejecting a 4-tuple. The exact-N `minItems` flip to 11 is deferred to the same separately-validated hardening migration the Sound 10-tuple flip awaits (the current fixtures were authored under the additive floor). — see §5 + Open Questions.
- `motion_spec_class` — enum (`primary_master_9x16` for v1.0 · `variant_master_1x1` reserved for v1.1 multi-aspect conform).
- `motion_spec_evidence_hash` — SHA-256 over the `motion_spec` + `motion_conform_check` + `spec_fidelity_check` block (forensic, tamper-evident finish).
- `motion_processed` — `const false` in v1.0 (Motion authors the spec; the human/automation runs the render. The direct analog of Sound's `audio_processed: const false` and Editor's `render_dispatched: const false` — the honest declaration that no frame was rendered by the agent). Flips to a real value only when Week 4–5 motion automation ships (v1.1).
- `finish_mode` — enum (`human_in_the_loop` for v1.0 · `automated` reserved for v1.1 Week 4–5). The explicit human-in-the-loop attestation.
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.

### §3.4 errorEnvelope code namespace (target 7–9 LOCKED on Day 83/85 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `upstream_audio_not_ready` | Sound `verdict not in {audio_ready}` / not `successAudioSpec` | 1 | Halt — Motion never finishes an unfinished-audio cut. |
| `upstream_not_success` | the consumed audio spec is `errorEnvelope` | 2 | Halt — cannot finish a failed audio-finish output. |
| `v2_edit_unresolved` | the `finish_target.v2_edit_uri` (audio-final cut) does not resolve | 3 | Hard FAIL — cannot spec a motion finish over a missing v2 edit; route back to Sound. |
| `text_asset_unresolved` | a caption / lower-third / end-card text field is empty or missing from the EDL passthrough | 4 | Hard FAIL — cannot reveal a blank super; route back to Editor. |
| `motion_marker_out_of_range` | a reveal / overlay / lower-third / end-card marker `at_ms` exceeds `total_timeline_ms` or is negative | 5 | Hard FAIL — cannot place a reveal past the timeline; route back to Editor. |
| `motion_token_out_of_spec` | a specified motion token is not in the allowed brand set (uses whip_pan/shake/meme/trending, violates 120ms ease-in-out / zero-bounce, or exceeds one reveal per 8s) | 6 | Hard FAIL — brand motion policy enforced at the motion layer; `detail` names the token. |
| `typography_out_of_spec` | a lower-third is all-caps / not lowercase-sans-left-underline, a caption is not one-line burned-in, or the end-card is not serif-ivory-1.5s | 7 | Hard FAIL — brand typography spec enforced at the motion layer. |
| `spec_fidelity_breach` | the motion spec's caption/lower-third/end-card text or timeline duration deviates from the EDL, or `edl_evidence_hash` / `audio_spec_evidence_hash` does not verify | 8 | Hard FAIL — Motion must finish the cut faithfully; a deviation = an unauthorized override. |
| `motion_firewall_breach` | a banned-entity token appears in the passthrough typography (caption/lower-third/end-card) at the motion-finish layer (12th pass) | 9 | Hard FAIL — last visual-text checkpoint before full QC; forensic-log the field. |
| `motion_lineage_failure` | malformed parent_chain / broken n-tuple lineage | 10 | Forensic — audit-trail break. |
| `motion_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 83/85 LOCK:** 7–9 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping. (Preliminary list carries 9 named + lineage + catch-all; the §13 walk will confirm the SPLIT-vs-fold decision on `v2_edit_unresolved`→Sound vs `text_asset_unresolved`/`motion_marker_out_of_range`→Editor, the direct analog of Sound's `vo_track_missing`/`audio_asset_unresolved`→Ingest SPLIT.)

---

## §4. Tier Constraints & Mode Coverage

**Per-tier gate access (Motion is universal-access AND tier-FLAT in its own logic — restated for defense-in-depth pass 12):**

| Tier | Reaches Motion? | Motion's own finish behavior | Aspect masters specced (v1.0) | Cost |
|------|-----------------|-------------------------------|-------------------------------|------|
| Pilot | **YES** | Faithful motion spec of the EDL typography + brand tokens | 1 (primary 9:16) | ~$0.00 |
| Starter | **YES** | Faithful motion spec of the EDL typography + brand tokens | 1 (primary 9:16) | ~$0.00 |
| Pro | **YES** | Faithful motion spec of the EDL typography + brand tokens | 1 (primary 9:16; flags 1:1) | ~$0.00 |
| Enterprise | **YES** | Faithful motion spec of the EDL typography + brand tokens | 1 (primary 9:16; flags 1:1) | ~$0.00 |

**Why universal access + tier-FLAT behavior (the same discipline as Editor + Sound):** Edit Director is the *creative authority* whose output richness is a sold tier feature; Motion is the *executor* — a typography/motion finish is faithful or it isn't, regardless of tier. A Pilot finish and an Enterprise finish are specified by the identical executor logic; the richness (reveal count, lower-third density, overlay map) already lives in the EDL Motion receives, and the motion tokens are a single brand const set for all tiers. **The EDL carries the tier envelope; Motion faithfully specs whatever envelope arrives and applies the one brand token policy.** v1.0 specs the primary 9:16 master for every tier and flags the `aspect_variants_planned` count (the 1:1 LinkedIn cutdown is a derived v1.1 conform). This is the same tier-flat discipline Editor and Sound hold — a technical executor does not re-litigate the tier ladder.

**No cost-ledger / no asset-validation / no cut-conform / no creative authority / no audio-finish (the inherited discipline, quintupled):** Motion does **NOT** re-run the cost ledger (QC Pre-flight's authority), re-validate assets (Ingest's authority), re-conform the cut (Editor's authority), re-direct the edit (Edit Director's authority), OR re-mix the audio (Sound's authority). It is five gates downstream of cost enforcement, four gates downstream of asset validation, three gates downstream of cut conform, two gates downstream of creative direction, and one gate downstream of audio finish; re-litigating any of them would be redundant and risk a double-fail on a reel already cleared. Motion's authority is **faithful typography + motion-graphics finish**, full stop.

**Mode coverage (mode-BLIND by inheritance — the convergence payoff, four stages deep):**

| Mode | What Motion sees | Mode-specific note |
|------|------------------|--------------------|
| A (human footage origin) | The SAME mode-agnostic v2 edit + EDL typography | Motion cannot tell, and does not need to know, that these shots came from a videographer. `production_mode` is NOT read as a branch. |
| B (rendered + replicated origin) | The SAME mode-agnostic v2 edit + EDL typography | Identical finish path. |
| C (replicated hot-path origin) | The SAME mode-agnostic v2 edit + EDL typography | Identical finish path. |

**Mode-blind guarantee (the core §4 contract):** Motion asserts `mode_blind_confirm.production_mode_read == false` in every output — a self-attestation that it authored the motion spec without consulting the origin mode. This is the FOURTH machine-checkable proof that Ingest's mode-convergence seam holds — now four stages downstream. **Motion is the fourth agent in the 17-agent fleet for which the mode columns of this table are identical; that identity, carried through the director (Edit Director) AND the timeline executor (Editor) AND the audio executor (Sound) AND the motion executor (Motion), is the structural evidence that the post-production tail is genuinely mode-agnostic end-to-end.** If Motion ever NEEDED to branch on mode to finish the graphics, the convergence contract would be broken upstream. By construction it never does.

---

## §5. Process Steps (System Prompt Skeleton — Day 83 §7 will LOCK)

The agent runs an **11-step finish loop** per invocation (mirrors the AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound 11-step process pattern). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope.

**Step 1 — Verify Sound precondition + parse input**
- Read the Sound `audio_spec.json`. Confirm `output_type == "successAudioSpec"` AND `verdict == "audio_ready"`. Otherwise → halt with `upstream_audio_not_ready`.
- Parse input JSON against `input.schema.json` (Day 83/85 LOCKED). There is NO mode branch — assert the v2 edit + EDL typography is the mode-agnostic shape.
- Confirm the consumed audio spec is the success branch. Any `errorEnvelope` upstream → halt with `upstream_not_success`.

**Step 2 — Lineage integrity**
- Validate `metadata.parent_chain` is a well-formed 10-tuple inbound (5/6/7/8/9/10-tuple accepted additively under the ratified §3.9 amendment). Malformed → `motion_lineage_failure`.

**Step 3 — Audio-spec-evidence + typography/handle resolution**
- Verify the `audio_spec_evidence_hash` (SHA-256 over the audio_spec + audio_conform_check + spec_fidelity_check) recomputes — the audio spec was not tampered post-finish. Mismatch → `spec_fidelity_breach`.
- Resolve the v2-edit handle (`finish_target.v2_edit_uri`) → unresolvable → `v2_edit_unresolved` (route back to Sound). Resolve every caption/lower-third/end-card text field (EDL passthrough) → any empty/missing → `text_asset_unresolved` (route back to Editor).

**Step 4 — Marker + timeline conform**
- For each reveal/overlay/lower-third/end-card marker: validate `at_ms >= 0` AND `at_ms <= total_timeline_ms` (no reveal past the timeline, no negative time). Over-range → `motion_marker_out_of_range` (route back to Editor).
- Confirm the motion timeline duration matches the EDL `total_timeline_ms`; a mismatch surfaces as `spec_fidelity_breach`.

**Step 5 — Motion-token + reveal-cadence enforcement (motion layer)**
- Constrain every motion token to the brand allowed set (`slow_push_in` / `static_hold` / `subtle_parallax`); reject any banned token (`whip_pan` / `shake` / `meme_transition` / `trending_transition`). Enforce the 120ms ease-in-out + zero-bounce policy. Enforce one caption line at a time and one reveal per 8s max. Any violation → `motion_token_out_of_spec` (brand motion policy enforced at the motion layer, not just the prompt).

**Step 6 — Caption reveal + lower-third placement specification**
- Author the caption reveal directives (line-in reveal, one line at a time, brand cadence, 120ms ease) preserving the EDL caption text byte-faithful — a *directive spec*, NOT rendered graphics.
- Author the lower-third/super placements (lowercase sans, left-aligned, subtle underline, `all_caps: false`) mapped from the EDL `lower_third_events`. Any all-caps / non-brand style → `typography_out_of_spec`. Preserve the EDL's text as already-validated facts (re-assert, do not re-derive).

**Step 7 — Overlay / parallax + end-card placement**
- Place each subtle parallax/overlay as a timed directive bound to the timeline (intensity low, within the allowed token set). Author the end-card hold ("REINVENTED — build on purpose." serif, ivory bg, 1.5s) per the EDL `end_card_event`; any deviation from the brand end-card const → `typography_out_of_spec`. (Motion specs the placement + tokens; the motion-graphics app renders the actual composite — NOT Motion.)

**Step 8 — Defense-in-depth firewall pass (twelfth time, TYPOGRAPHY-domain passthrough layer)**
- Re-run the canonical entity-firewall regex (Cross-SPEC §3 drift #12): `Holdco | Principal | NPOX | 4821 | 6315 | SLN | Retail Supply | Nonprofit Leader A | Community Nonprofit | Nonprofit Leader B | Nonprofit Leader C` over the declared caption/lower-third/end-card passthrough text (the on-screen typography the motion finish burns in).
- Hard FAIL → `motion_firewall_breach` + forensic log naming the field. **This is the TYPOGRAPHY-domain checkpoint:** Motion authors no new copy (Editor firewall-scanned the caption/lower-third/end-card text at the 10th commit pass; Sound re-scanned the VO transcript at the 11th audio pass), but Motion is the agent that BURNS IN the on-screen text — so a final firewall re-scan of the visible typography before the master reaches full QC is the last-line visual catch (a leak that survives here rides into the burned-in v3 master).

**Step 9 — Spec-fidelity + motion-conform check**
- Run `spec_fidelity_check`: caption text byte-faithful, lower-third text byte-faithful, end-card matches the brand const, timeline duration matches the EDL, `edl_evidence_hash` + `audio_spec_evidence_hash` verified. Any deviation → `spec_fidelity_breach` (an unauthorized override).
- Run `motion_conform_check`: v2 edit resolved, all text fields resolved, all markers in the timeline, reveal cadence in spec, motion tokens in the brand set, total timeline in the 45–75s band (re-assert from the EDL's duration). Out-of-band or unresolved → routed as `motion_marker_out_of_range` / `v2_edit_unresolved` / `text_asset_unresolved` per the offending cause.
- Compute the `motion_self_check` per Blueprint §4.12 (`voice_markers_in_captions`, `truth_echoes` counted from the passthrough caption text; `banned_vocab_hits` from the firewall pass; `motion_tokens_applied: true`).

**Step 10 — Construct motion-spec payload**
- If all green: build `successMotionSpec` per §3.1 with the full `motion_spec` (caption reveals + reveal cadence + lower-thirds + motion tokens + overlays + end-card) + `motion_conform_check` + `spec_fidelity_check` + `motion_self_check` + `verdict: "motion_ready"` + `handoff_targets: ["qc-agent"]`.
- Compute `motion_spec_evidence_hash` (SHA-256 over the motion_spec + motion_conform_check + spec_fidelity_check block — tamper-evident).
- Extend `parent_chain` to an **11-tuple** (append `motion_spec_id`), held additively per §3.3.
- Set `motion_processed: false` (v1.0 honesty — the human runs the render), `finish_mode: "human_in_the_loop"`, `motion_spec_class: "primary_master_9x16"`, `mode_blind_confirm.production_mode_read: false`, `human_review_required: true`.

**Step 11 — Emit + handoff**
- Validate output payload against `output.schema.json` (Day 83/85 LOCKED). Hard FAIL → forensic log + halt (output should always validate; failure here = agent bug).
- Emit JSON to stdout (paste-and-run runbook) OR persist the motion spec to the platform path / the Drive `/reels/[reel_id]/` finish queue per runtime environment (Blueprint §7 I/O: Motion writes `Drive/reels/[reel_id]/v3-final.mp4` — in v1.0 the motion spec goes to the human finish queue, the human writes the v3-final.mp4).
- On `fail`, set `route_back_to` per the §3.2 verdict↔route map so the Orchestrator can re-enter the pipeline at the correct agent (Editor for a timeline/typography-text defect, Sound for an audio-finish handle gap).

**Anti-patterns Step 11 prevents (Lock-time discipline mirror from Editor / Sound / Ingest §11):**
- No markdown fences around output JSON.
- No `print()` statements before the output JSON block.
- No engine credentials referenced; **no motion-graphics render dispatched** (v1.0 authors a motion spec only — `motion_processed` is `const false`; the human/automation runs the render + burn-in pass).
- No absolute URLs in any motion-spec `asset_uri` / `v2_edit_uri` / `v3_final_uri` echoed from the audio spec/EDL (Hard Rule #8 inherit).
- No `motion_ready` verdict emitted while any conform, fidelity, token, typography, or firewall check is unresolved (must be `fail`).
- No reading of `production_mode` as a branch discriminator (mode-blind by construction — `mode_blind_confirm.production_mode_read` must be `false`).
- **No timeline re-cutting or audio re-mixing:** Motion finishes the graphics on the v2 edit as given; it does NOT re-order events, re-trim cuts, re-mix the audio, or "improve" the copy. An EDL/audio spec it disagrees with is finished faithfully or failed upstream — never silently re-cut, re-mixed, or re-written.
- **No operator/finish impersonation:** Motion emits `human_review_required: true` + a motion-spec *recommendation* + `motion_processed: false`; it does NOT mark a reel "rendered" or "approved for QC" as a ratified state — that is the human finish (v1.0) or the Week 4–5 automation (v1.1).

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 83 + 85)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 83 partial 1. Pattern source: Sound §6 / Editor §6. Target 10–12 checks bipartite-covering the 7–9 errorEnvelope codes. Slot 11 reserved for `motion_agent_failed` per Cross-SPEC §3.6 slot-naming canon. Checks span: precondition + audio-spec-evidence verify · lineage · v2-edit/typography resolution · marker-in-timeline · motion-token-in-brand-set · reveal-cadence-in-spec · typography-style-in-spec · spec-fidelity (caption/lower-third/end-card text + duration) · typography-domain firewall · mode-blind self-attestation · evidence-hash verify.
- **§7 System Prompt v1.0** — Day 83 partial 1. Frame + hard rules + universal-tier-FLAT table + 11-step finish loop verbatim from §5 + the Blueprint §4.12 v3-final/self-check target shape inlined + the brand motion tokens (allowed/banned set, 120ms ease-in-out, zero-bounce) + reveal cadence (one line/reveal, one per 8s) + lower-third/end-card brand consts (§7/§8) as the enforced finish surface. ~12–14 KB target. Hard Rules mirror Sound with Motion-specific tightening on "spec-faithfully-never-re-cut/re-mix," "author-a-motion-spec-never-render," and "human-finishes (motion_processed const false)" discipline.
- **§8 Performance Targets** — Day 85 partial 2. 9 metric categories. Schema validity 100% / spec-fidelity 100% (a caption/lower-third/end-card/duration deviation must never survive) / typography-domain firewall catch 100% / motion-token-in-brand-set 100% / reveal-cadence-in-spec 100% / marker-in-timeline 100% / false-motion-ready rate 0% target / false-fail rate ≤ 8% (over-flagging a borderline token to `fail` is the acceptable failure direction) / p50 latency 22s / p95 70s (finish reasoning — comparable to Sound's) / zero engine + zero render cost.
- **§9 Test Fixtures** — Day 85 partial 2. 5-fixture portfolio: TC-01 clean Mode-origin-A→audio-spec Pro `motion_ready` (full motion spec) · TC-02 Mode-origin-C Enterprise `motion_ready` (proves mode-blind: byte-identical finish path to TC-01 despite different origin — the **mode-blind finish-convergence proof**, the Motion analog of Sound's finish-convergence proof, FOUR stages deep) · TC-03 `motion_marker_out_of_range` → fail + route to Editor (a caption reveal past the timeline) · TC-04 `v2_edit_unresolved` → fail + route to Sound (the audio-final cut handle not resolving — the SPLIT-analog to Sound's `vo_track_missing`→Ingest) · TC-05 `motion_firewall_breach` (a banned token present in the passthrough caption/lower-third typography reaching the motion finish — the 12th-pass last-line catch; GATING fixture). 5 of 7–9 codes exercised; remainder in schema-only fixtures. Optional probes: the `typography_out_of_spec` (an all-caps lower-third) + the slot-11 `motion_agent_failed` catch-all.
- **§10 Field Map** — Day 83 partial 1. ~24 rows · passthrough vs transform vs derived. EDL-typography→reveal-directive map (transform: caption/lower-third events → reveal timings + placements) + caption-text→byte-faithful-passthrough map + motion-token→brand-const-derivation map + audio-spec/v2-edit→resolution map + derived conform/fidelity/self-check map.
- **§11 Cost Model** — Day 85 partial 2. Zero engine + zero render snapshot (finish reasoning + motion-spec authoring only; the human/automation runs the render in v1.0/Week 4–5). Faithful-finish value model (economic justification = a brand-token-correct, entity-safe motion spec on the first pass, no wasted motion-artist cycles, no EDL/audio-spec mismatch discovered at v3 review). Explicit note: the actual render compute spend lands in v1.1 Week 4–5 automation — v1.0 is $0 by construction.
- **§12 Verdict Math** — Day 85 partial 2. MOTION_READY = (Sound precondition met) ∧ (audio_spec_evidence_hash verified) ∧ (v2 edit resolved) ∧ (all text fields resolved) ∧ (all markers in timeline) ∧ (motion tokens in brand set) ∧ (reveal cadence in spec) ∧ (typography style in spec) ∧ (timeline duration matches EDL) ∧ (spec-fidelity byte-faithful) ∧ (typography-domain firewall clean). Any single ∧-term false → fail per §3.2 (NO `revise` branch — deterministic executor). Fully deterministic — Motion has zero judgment slots (inherits Editor + Sound zero-judgment-slot posture).
- **§13 Critical Decisions LOCKED** — Day 85 partial 2. Target 10–14 LOCKED decisions. Pre-scaffolded list:
  1. Motion-spec-authoring vs render scope — v1.0 = motion-conform-spec authoring ONLY; actual motion-graphics render/burn-in is human-in-the-loop at launch (Blueprint §9), automation Week 4–5. `motion_processed: const false`. [LOCKED-as-drafted Day 82]
  2. Faithful-executor, zero timeline re-cutting / zero audio re-mixing — Motion specs the EDL's typography + brand tokens faithfully; it never re-cuts, re-mixes, re-orders, or "improves" copy. [LOCKED-as-drafted Day 82]
  3. Two-verdict (NO `revise`) — Motion is deterministic; the subjective slot lives upstream at Edit Director. `motion_ready | fail` only. [LOCKED-as-drafted Day 82]
  4. Mode-blind by inheritance — no `production_mode` branch; `mode_blind_confirm.production_mode_read: false` self-attested (the fourth mode-blind agent). [LOCKED-as-drafted Day 82]
  5. Audio-ready precondition — Motion runs only on a `successAudioSpec`/`audio_ready` reel; otherwise halts `upstream_audio_not_ready`. [LOCKED-as-drafted Day 82]
  6. Tier-FLAT behavior — all 4 tiers reach Motion; the EDL carries the tier envelope, Motion specs it identically + applies one brand token policy (no own tier scaling). [LOCKED-as-drafted Day 82]
  7. 11-tuple parent_chain — inherits Sound 10-tuple + appends `motion_spec_id`; SIXTH forcing function (depends on the Sound 10-tuple LOCK, itself spend-gated on the Day 81 runbook 5/5; the §3.9 amendment is already RATIFIED Day 79). [DEFERRED — held additively at `minItems: 5`]
  8. errorEnvelope code count — 7–9 target; SPLIT-vs-fold on `v2_edit_unresolved`→Sound vs `text_asset_unresolved`/`motion_marker_out_of_range`→Editor. [PRELIMINARY · operator amend Day 85]
  9. Self-QC check count — 10–12. [PRELIMINARY · operator amend Day 85]
  10. Spec-fidelity = ZERO tolerance — a caption/lower-third/end-card text deviation, altered brand end-card, or duration mismatch must NEVER survive to `motion_ready`; `edl_evidence_hash` + `audio_spec_evidence_hash` machine-verified. [LOCKED-as-drafted Day 82]
  11. Typography-domain firewall (12th pass) — Motion re-scans the passthrough caption/lower-third/end-card text at the motion-finish layer, the last visual-text checkpoint before full QC (not a new authorship surface). [LOCKED-as-drafted Day 82]
  12. No render, no engine, no decode — NO generative engine, NO motion-graphics render, NO byte-level video frame decode in v1.0; declared-text + brand-const tokens only; `motion_processed: const false`, `cost_incurred_usd ~$0`. [LOCKED-as-drafted Day 82]
  13. Aspect dual-master scope — v1.0 specs the primary 9:16 master + flags the 1:1 LinkedIn cutdown variant count; auto-generation of the 1:1 master deferred to v1.1. [PRELIMINARY · operator amend Day 85]
  14. Conform-faithful handoff to full QC — Motion hands the motion spec + v3-final handle + `motion_self_check` to full QC (Blueprint §4.12); the spec goes to the human finish queue until Week 4–5 automation. [LOCKED-as-drafted Day 82]

- **§14 Calendar status updates** — Day 83 partial 1. Day 82 ✓ → trajectory populated.
- **§15 Change Log** — Day 85 partial 2. v1.0 lifecycle entries (outline-day-82 → body-day-83 → body-day-85 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 85 partial 2. Cross-SPEC §3.9 canonical fields + 6 Motion additions (11-tuple parent_chain, motion_spec_class, motion_spec_evidence_hash, motion_processed const false, finish_mode, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `motion-agent` (kebab-case, matches the fleet pattern + Blueprint §4.11 handoff target) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `motion_spec_evidence_hash` SHA-256 over the motion_spec + motion_conform_check + spec_fidelity_check block; `edl_evidence_hash` + `audio_spec_evidence_hash` re-verified (inherits the Editor + Sound anchors) |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ Motion consumes the accumulated surface as read-only context; it contributes its own finish predicates + the `motion_self_check` downstream |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-BLIND table — the fourth agent for which the mode columns are identical (the convergence payoff, four stages deep) |
| §3.6 Slot 11 naming canon | ✅ Reserved `motion_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Consumed shapes respected; Motion's own predicates snake_case |
| §3.8 Tier↔mode firewall (12th defense-in-depth) | ✅ Step 8 TYPOGRAPHY-domain passthrough firewall (last visual-text checkpoint before full QC) + §4 universal-tier-FLAT table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 11-tuple, held additively. **Sixth forcing function** — gated on the Sound 10-tuple LOCK (spend-gated on the Day 81 runbook 5/5); the §3.9 amendment itself is RATIFIED (Day 79). |
| §3.10 Cost ceiling authority | ✅ §4 explicitly DECLINES to re-litigate cost (QC Pre-flight's), re-validate assets (Ingest's), re-conform the cut (Editor's), re-direct the edit (Edit Director's), OR re-mix the audio (Sound's) — no quintuple-enforcement; Motion is $0-cost in v1.0 |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 82 outline — 6 parked for operator amendment)

1. **Motion-spec-only vs partial-render scope** — v1.0 authors the motion conform spec + finish manifest; the actual motion-graphics render/burn-in into v3.mp4 is human-in-the-loop at launch (Blueprint §9), automation Week 4–5. Confirm v1.0 stops at the motion spec and runs NO render (`motion_processed: const false`). *(Donna recommends: confirm motion-spec-only for v1.0 — the spec is the buildable, highest-leverage, $0 slice; the render automation lands in the Week 4–5 window the Blueprint already scopes, and keeps the zero-dollar / no-render invariant intact.)*
2. **Two-verdict (no `revise`)** — should Motion stay deterministic (`motion_ready | fail`), or inherit a creative `revise` for some borderline motion tension? *(Donna recommends: keep two-verdict — Motion is a faithful executor with no subjective surface; the motion tokens, reveal cadence, lower-third style, and end-card are all brand consts. A `revise` here would mean second-guessing a locked cut + finished mix, exactly the finish/finish override the boundary forbids.)*
3. **11-tuple parent_chain** — sixth forcing function (depends on the Sound 10-tuple LOCK, itself spend-gated on the Day 81 runbook 5/5; the §3.9 amendment is already RATIFIED Day 79). Motion is the first 11-tuple consumer. *(Donna recommends: hold additively at `minItems: 5` until the Sound 10-tuple LOCKs; the exact-N flip to 11 folds into the same separately-validated hardening migration the Sound 10-tuple flip awaits.)*
4. **QC handoff readiness** — Motion hands to the not-yet-built full QC agent (Agent #13 candidate, position 14). Should v1.0 emit the motion spec + v3-final handle + `motion_self_check` to a holding store (the Drive `/reels/[reel_id]/` finish queue, per Blueprint §7 I/O) until full QC ships, or assume direct handoff? *(Donna recommends: emit to the Drive finish queue in v1.0; direct agent-to-agent handoff activates when full QC LOCKs — mirrors the Sound→Motion-finish-queue and Editor→conform-queue holding-store decisions.)*
5. **Aspect dual-master scope** — v1.0 specs the primary 9:16 master + flags the 1:1 LinkedIn cutdown variant; should the 1:1 master be auto-specced in v1.0 or deferred? *(Donna recommends: defer the 1:1 cutdown to v1.1 — the 9:16 vertical master is the canonical primary for the pilot's IG/TT-first distribution; the 1:1 LinkedIn variant is a derived conform that lands with the render automation. v1.0 flags the count so nothing is lost.)*
6. **Motion-token basis — declared directive vs measured** — v1.0 specs the motion tokens (slow_push_in / static_hold / subtle_parallax; 120ms ease-in-out; zero-bounce) as declared directives with NO frame-level keyframe render; is declared-token + reveal-cadence spec an acceptable finish basis? *(Donna recommends: ratify declared-token spec for v1.0 — actual keyframe render + parallax compositing needs frame-level decode (v1.1), the same declared-spec-only posture as Ingest, Edit Director, Editor, and Sound.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (full Motion trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 82 | Fri Jul 10 | **SPEC outline §0–§5** [SHIPPING NOW] | Sound Day 74 outline |
| 83 | Sat Jul 11 | SPEC body partial 1: §6 + §7 + §10 + §14 | Sound Day 75 / Editor Day 67 |
| 84 | Sun Jul 12 | **REST DAY** — no build (pre-stage next scaffold only) | Day 21/28/35/42/49/56/63/70/77 Rest Day compounding |
| 85 | Mon Jul 13 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | Sound Day 76 / Editor Day 68 |
| 86+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | Sound Day 78–81 / Editor Day 69–73 |

**Sprint context:** Motion is **Agent #12** — the fifth post-production agent and the third *executor* agent in the post tail, the 12th defense-in-depth firewall (typography-domain passthrough layer) and the **fourth contractually mode-blind agent** (the continued proof of Ingest's convergence seam, four stages deep). It is the first typography/motion-graphics-domain agent in the fleet — yet in v1.0 it produces NO media: it drafts the motion conform spec the human finishes (Week 4–5 automation deferred), keeping the zero-dollar / no-render / no-decode invariant intact. The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) shipped on the six production agents through the QC Pre-flight gate; Motion v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the Sound, Ingest, QC Pre-flight, Style Replication, Edit Director, and Editor outlines were (while their predecessor LOCKs remained gated — Sound's LOCK here spend-gated on the Day 81 runbook's live 5/5).

---

## Files produced today (Day 82)

- `ars/ARS-2026-07-10-Day-82-Motion-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-07-10.md` — Day 82 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 82)

- ✅ **No LLM dispatched.** No render API. No motion-graphics render. No engine credentials referenced. No vendor URLs walked. No media render, no byte-level video decode, no frame analysis. (Motion by design authors a motion spec and renders no frame in v1.0 — the human finishes; full automation is the Week 4–5 v1.1 scope.)
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no client/investor outreach. The end-of-run status digest to Jamila's Google Voice self-thread ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, no render compute, zero $ spent. (`jsonschema` re-validation, if run, is a PyPI install with no vendor/engine surface, $0.)
- ✅ **No operator-impersonation.** The Sound v1.0 LOCK ceremony NOT performed — its gate is a live, reproducible 5/5 run of the Day 81 runbook (~$3.50 Opus) that the $0 unattended session cannot execute; locking on the offline stamp alone would be a fake-advance (refused). Sound stays LOCK CANDIDATE. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED for Sound. The §3.9 amendment (ratified Day 79) NOT re-committed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. Motion v1.0 LOCK will hard-gate itself on the upstream LOCKs (especially the Sound 10-tuple) being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 8 enumerates HC/NPOX tokens precisely so the agent can BLOCK them at the motion-finish layer — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Sound Day 74 outline structure inherited verbatim. Orchestration Blueprint §1.2 / §2 / §4.11 / §4.12 / §6 / §7 / §9 (Agent 13 Motion definition) + Cross-SPEC §3 canon + Brand-Voice Intake §7–§8 + the motion-token set used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-82 build runs Friday (Pacific). Next Rest Day: Day 84 (Sun Jul 12 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 82 ships clean. Day 83 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). Motion is Agent #12 of 17 — the 12th defense-in-depth firewall (typography-domain passthrough layer) and the third executor agent in the post tail, the fourth contractually mode-blind agent and therefore the continued proof that Ingest's mode-convergence seam holds four stages deep. It is the first typography/motion-graphics-domain agent in the fleet — yet v1.0 produces no media, authoring the motion conform spec the human finishes (render automation deferred to Week 4–5), keeping the zero-dollar / no-render / no-decode invariant intact. Operator pickup: (1) the Sound v1.0 LOCK remains the immediate forward step — its gate is a live, reproducible 5/5 run of the Day 81 runbook (~$3.50 Opus) that the $0 overnight cannot execute; runnable in Jamila's ~20–35 min iMac sit-down OR an attended, spend-authorized Donna run under the standing authorization; the Sound 10-tuple is Motion's direct 11-tuple dependency; (2) review the §13 critical-decisions list — the §3.9 n-tuple amendment is already RATIFIED (Day 79), so Motion inherits n-tuple lineage cleanly (sixth forcing function, held additively until the Sound 10-tuple LOCKs); (3) confirm the Agent #12 = Motion selection (or re-assign the slot) at the Sound LOCK close. The Sound v1.0 LOCK was NOT performed tonight — locking on the offline stamp alone, absent the live 5/5, would be a fake-advance; it stays in the spend-gated queue.*
