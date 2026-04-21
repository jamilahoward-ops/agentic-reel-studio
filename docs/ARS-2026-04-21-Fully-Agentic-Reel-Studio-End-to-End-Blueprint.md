# Fully-Agentic Reel Studio — End-to-End Blueprint

> Exported from the Notion concept page (last edited 2026-04-21). This is the original concept document that preceded the canon
> [Agent Orchestration Blueprint](ARS-2026-04-24-Agent-Orchestration-Blueprint.md). Redactions for the public repo: the per-brand
> pricing / cost-comparison section and the internal entity-application table were removed; brand-specific examples were generalized.
> Agent numbering here is the concept-stage numbering; the orchestration blueprint supersedes it.

*One human holds the camera (or nothing at all). Claude agents run every other link in the chain.*

---

## TL;DR

- **Concept:** Replace a 15-person Apple-tier Reel team with ~16 Claude Cowork agents + optional human videographer + AI video generation stack + URL-based style replication.
- **Human involvement:** 0 to 60 min per Reel (filming only, if needed at all).
- **Output target:** 30+ Reels/month per brand vs. traditional 4-8.
- **Unlock:** Scales across multiple brands without adding headcount.

---

## The Three Production Modes

**Mode A — Live Footage**
Human videographer shoots on iPhone/Sony → Claude takes over everything else.

**Mode B — 100% AI-Generated (no footage required)**
For brands with no existing footage, no talent, or pure concept-driven content. AI video models generate everything.

**Mode C — Style Replication (drop a URL)**
Paste any YouTube / TikTok / IG / web video URL. System reverse-engineers the style and produces a branded version. Works with Mode A or Mode B as the execution layer.

*Every agent pipeline below supports all three modes.*

---

# THE FULL AGENT PIPELINE

## PHASE 0 — OPTIONAL STYLE SEEDING *(Mode C only)*

### Agent 0: Style Replication Agent

- **Input:** A video URL (YouTube, TikTok, Instagram, Vimeo, any web video)
- **Does:**
  - Downloads/streams the reference video
  - Runs multimodal analysis across these dimensions:
    - **Composition:** framing, rule-of-thirds, negative space, subject placement
    - **Camera work:** angles (low/high/eye-level), movement (static, dolly, handheld, drone, whip pan), lens feel (wide, macro, tele)
    - **Color science:** color grade, LUT approximation, dominant palette, contrast ratio, saturation, temperature
    - **Edit rhythm:** cut pace (cuts per sec), transition style, jump cuts, match cuts
    - **Typography:** on-screen text style, font weight, placement, animation style
    - **Audio profile:** genre, tempo/BPM, voice treatment, SFX density
    - **Lighting:** key/fill/rim setup, hard vs. soft, practical vs. cinematic
    - **Format:** aspect ratio, duration, hook style, pacing arc
    - **Narrative:** structure, tension points, reveal moments, CTA style
  - Outputs a structured Style Profile (JSON)
- **Merges with:** Brand Library (colors, fonts, logo, tone, voice, talent restrictions)
- **Output:** Combined Style + Brand Directive
- **Hands to:** Brief Agent (feeds into script, storyboard, edit decisions)

**Why this changes the game:** Instead of briefing "make a luxury reel," you say *"make it like this"* and drop the URL. System captures the magic you couldn't articulate.

---

## PHASE 1 — PRE-PRODUCTION *(all AI · ~1-2 hours)*

### Agent 1: Strategy Agent
- **Input:** Brand goals, content calendar, trend data, competitor scan, analytics feedback loop
- **Does:** Picks topic, angle, goal (awareness / conversion / community), target KPI
- **Output:** Content brief → **Hands to:** Brief Agent

### Agent 2: Brief Agent
- **Input:** Strategy output + Style Profile (if Mode C)
- **Does:** Structures creative brief — hook, beats, CTA, format, duration, platform specs
- **Output:** Creative brief document → **Hands to:** Script Agent

### Agent 3: Script + Copy Agent
- **Input:** Creative brief
- **Does:** Writes 3-sec hook, voiceover script, on-screen text, 3 caption variants, hashtags, alt text
- **Output:** Script doc + caption pack → **Hands to:** Storyboard Agent

### Agent 4: Storyboard Agent
- **Input:** Script + brief + Style Profile (if Mode C)
- **Does:** Generates shot list, visual references (Midjourney/Flux), wardrobe/styling, locations OR AI scene prompts (Mode B)
- **Output:** Shot list + reference deck + AI prompts → **Hands to:** Production Coordinator

### Agent 5: Production Coordinator Agent
- **Mode A:** Call sheet, schedule, talent notes, location confirm → human videographer
- **Mode B:** Passes shot list + AI prompts → AI Video Generation Agent
- **Output:** Call sheet OR Generation queue

---

## PHASE 2 — PRODUCTION

### MODE A: Human Videographer *(~1-2 hours)*
- Shoots per shot list on iPhone / Sony
- Uploads raw footage to Dropbox/Drive
- **Trigger:** File upload auto-kicks Ingest Agent

### MODE B: AI Video Generation Agent *(~30-90 min)*
- **Input:** Shot list + AI prompts + reference images + Style Profile
- **Does:** Orchestrates multiple AI video models based on shot needs
- **Model stack (candidates):** Higgsfield (camera movement, motion control) · Runway Gen-3/Gen-4 · Sora · Veo 3 · Kling AI · Luma Dream Machine · HeyGen (avatars / talking heads) · Hedra / D-ID · ElevenLabs (VO + dubbing) · Midjourney / Flux (stills for image-to-video)
- **Output:** Raw AI-generated footage + assets → Ingest Agent

---

## PHASE 3 — POST-PRODUCTION *(all AI · ~1-2 hours)*

- **Agent 7: Ingest Agent** — organizes clips, transcribes audio (Whisper), tags shots, flags best takes
- **Agent 8: Edit Director Agent** — reviews takes, selects best, builds paper edit, times to script/beat/Style Profile
- **Agent 9: Editor Agent** — executes cut via CapCut / Descript / Runway APIs; matches reference pace if Mode C
- **Agent 10: Sound + Music Agent** — selects trending or style-matched audio, licensing check, ElevenLabs VO, SFX
- **Agent 11: Motion + Graphics Agent** — on-screen text, captions, kinetic typography, brand lower-thirds
- **Agent 12: QC Agent** — brand standards, accessibility (captions/contrast/alt), legal (music rights, trademarks, likeness), platform specs. ✅ Approved → Localization | ❌ Kickback with notes

---

## PHASE 4 — DISTRIBUTION *(all AI · ~30 min)*

- **Agent 13: Localization Agent** — translates captions + dubs for priority markets; adapts hooks culturally
- **Agent 14: Publishing Agent** — schedules across IG Reels / TikTok / YT Shorts / LinkedIn / Facebook via Ayrshare/Later; A/B tests thumbnails, hooks, captions

---

## PHASE 5 — LEARNING LOOP *(continuous)*

- **Agent 15: Community Agent** — replies to comments, DMs, flags sentiment, escalates VIPs/leads to human
- **Agent 16: Analytics Agent** — pulls performance at 24h / 7d / 30d (views, watch time, completion, saves, shares, follows, profile visits, conversions). **Feeds back to Strategy Agent.**

---

# THE TRIGGER SYSTEM

1. **Scheduled Trigger** — calendar-based (weekly batch, Strategy Agent auto-runs)
2. **Event Trigger** — product launch, press win, trending moment, competitor move detected
3. **Manual Trigger** — *"Make a Reel about X"* — starts at Brief Agent
4. **Performance Trigger** — Analytics spots a top performer → auto-orders variations/sequels
5. **URL Trigger (Mode C)** — *"Make one like this for [brand]"* — kicks off Style Replication Agent

---

# THE LEARNING MECHANICS

- **Shared memory layer** (vector DB) — every agent writes learnings
- **Performance scoring** — which hooks/edits/audio/models/styles drove results
- **Brand voice training** — sharper every post
- **Failure tracking** — QC kickbacks train earlier agents to stop repeating mistakes
- **Model preference learning** — which AI video model performs best for each shot type
- **Style library** — every Mode C reference is saved; most-replicated styles become templates

---

# END-TO-END TIMELINE (one Reel, planning estimate)

| Phase | Who | Time | Output |
|---|---|---|---|
| Style Seeding (Mode C only) | Agent 0 | 10 min | Style Profile |
| Strategy → Brief | Agents 1-2 | 15 min | Creative brief |
| Script + Storyboard | Agents 3-4 | 30 min | Script + refs |
| Production coordination | Agent 5 | 15 min | Call sheet or AI queue |
| Filming (Mode A) | Human | 30-90 min | Raw footage |
| AI Generation (Mode B) | Agent 6 | 30-90 min | AI footage |
| Ingest → Edit Director | Agents 7-8 | 20 min | Paper edit |
| Editor → Sound → Motion | Agents 9-11 | 45 min | Finished cut |
| QC | Agent 12 | 10 min | Approved file |
| Localization → Publish | Agents 13-14 | 20 min | Live across platforms |
| **TOTAL (Mode A)** | | **~3.5-4.5 hrs** | Posted Reel |
| **TOTAL (Mode B)** | | **~3-4 hrs** | Posted Reel |
| **TOTAL (Mode C)** | | **+10 min** | Style-matched Reel |
| Community + Analytics | Agents 15-16 | Ongoing | Feedback loop |

---

# BUILD ROADMAP (concept-stage)

1. **Stage 1 — Front-end prototype:** Strategy + Brief + Copy agents as one workflow. Brief-to-script in 15 min.
2. **Stage 2 — Pre-production pipeline:** Storyboard + Production Coordinator; image-gen integration.
3. **Stage 3 — Post-production agents:** Ingest → Edit Director → Editor → Sound → Motion → QC.
4. **Stage 4 — Distribution + learning:** Localization, Publishing, Community, Analytics; wire the feedback loop.
5. **Stage 5 — AI video layer (Mode B).**
6. **Stage 6 — Style replication layer (Mode C).**
7. **Stage 7 — Multi-brand scale:** brand-specific memory instances, parallel pipelines.

**Governance rule:** Human reviews everything until the system hits 90%+ approval rate. Then move to exception-only review.

---

# SUCCESS METRICS

- **Speed:** time from brief to posted Reel
- **Volume:** Reels published per month per brand
- **Cost per Reel:** declining trajectory
- **Performance:** engagement rate vs. pre-agent baseline
- **Human time per Reel:** should trend toward zero
- **QC kickback rate:** should decline monthly
- **Style Profile library size:** growing catalog of proven reference styles
