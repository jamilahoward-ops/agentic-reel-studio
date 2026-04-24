# ARS Agent Orchestration Blueprint — v1.0

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Built by:** Jamila Howard · Overnight Build Session Day 5
**Date locked:** April 24, 2026
**Week 1 deliverable:** 5 of 5 required (this completes the Week 1 set alongside Orchestration Blueprint pending Service Tier + Pricing)
**Read-by:** Every agent in the system. This is the wiring diagram.

---

## 0 · Purpose

One document that tells every agent in the ARS pipeline:
1. **Who they are** (inputs, outputs, scope, blast radius)
2. **Who they talk to** (handoff contracts — JSON in, JSON out)
3. **When they fire** (trigger map)
4. **Where they read/write** (data store contract)
5. **How they fail safely** (retries, escalation, rollback)
6. **Where the human intervenes** (Lever 3 / 2 / 1 checkpoints)
7. **How modes route** (A vs B vs C branching logic)

If any of the 17–18 agents need to know "what am I supposed to do right now," the answer is in this blueprint.

---

## 1 · Agent Roster (Canon Count = 18 specialized + 1 orchestrator)

> **Count note:** Dashboard historically said "14 Claude agents + AI video stack." Actual pipeline has 18 specialized agents + 1 Orchestrator meta-agent. The "14" figure counts only Claude-reasoning agents (excludes 2 video-gen agents which are thin wrappers on HeyGen/Runway/Sora). For this blueprint, 18 is canon. Flag for Jamila to resolve marketing copy later. Non-blocking.

### 1.1 Orchestrator (meta-agent, runs above the pipeline)

| ID | Name | Role |
|---|---|---|
| 00 | **Orchestrator** | Meta-agent. Routes reel intents to the right mode, manages state, enforces Lever, triggers retries, writes the run ledger. Does not touch content — only flow. |

### 1.2 Pre-Production (6 agents)

| ID | Name | One-line responsibility |
|---|---|---|
| 01 | **Trend Hunter** | Scans TikTok/IG/YouTube/X for trending formats, sounds, topics. Outputs weekly Trend Radar. |
| 02 | **Strategy** | Reads Analytics + Trend Radar + Brand Voice. Outputs weekly Reel Plan (5–10 topics, pillar distribution, mode assignment). |
| 03 | **Brief** | Converts a Reel Plan row into a shootable Brief: hook, beats, CTA, format, style, QC targets. Consumes Brand Voice Intake JSON. |
| 04 | **Script** | Writes the Script: hook (≤3s), body (3 beats), CTA. In REINVENTED voice per Brand Voice JSON §§5-6. |
| 05 | **Storyboard** | 6–9 shot list. Alux-style frame language. Maps every script beat to a visual. Specifies motion, light, talent, wardrobe. |
| 06 | **Production Coord** | Bundles Brief + Script + Storyboard into a Shoot Packet (Mode A) or a Gen Packet (Mode B/C). Assigns vendor. Books shoot date. |

### 1.3 Production (2 agents, mode-dependent)

| ID | Name | Fires in |
|---|---|---|
| 07 | **AI Video Gen** | Mode B. Prompts HeyGen (talent), Runway/Sora/Veo (b-roll), ElevenLabs (voice). Composes raw assembly. |
| 08 | **Style Replication** | Mode C. Ingests reference URL(s), extracts style DNA (palette, cut rhythm, motion, type), applies REINVENTED voice on top. |

### 1.4 Post-Production (6 agents)

| ID | Name | One-line responsibility |
|---|---|---|
| 09 | **Ingest** | Receives footage (Mode A) or raw AI outputs (Mode B/C). Validates specs, logs assets, hands metadata to Edit Director. |
| 10 | **Edit Director** | Writes the edit plan: cut order, pacing, music bed, captions style, lower-thirds, transitions. |
| 11 | **Editor** | Executes the cut per Edit Director's plan. Outputs v1 edit. |
| 12 | **Sound** | VO polish, music bed mix, SFX accents, loudness normalization (−14 LUFS for IG/TT, −16 LUFS for YT). |
| 13 | **Motion** | Typography reveals, lower-thirds, subtle parallax/overlays. Applies REINVENTED motion tokens (120ms ease-in-out, zero-bounce policy). |
| 14 | **QC** | Runs the 11-point Brand Voice QC gate + entity firewall + format specs + caption spec. Pass/Fail/Reshoot. |

### 1.5 Distribution (2 agents)

| ID | Name | One-line responsibility |
|---|---|---|
| 15 | **Localization** | Optional. Generates caption variants for cross-platform (IG vs TT vs LI vs Shorts). Handles vertical-to-horizontal crops if needed. |
| 16 | **Publishing** | Pushes to Ayrshare (IG/TT/LI/YT). Handles scheduling, hashtag rotation, thumbnail pick. Logs post URLs. |

### 1.6 Learning Loop (2 agents)

| ID | Name | One-line responsibility |
|---|---|---|
| 17 | **Community** | Listens to comments + DMs post-publish. Surfaces questions, objections, hot leads. Feeds intent signals back to Strategy. |
| 18 | **Analytics** | Pulls metrics 24h / 7d / 28d after publish. Scores against success rubric. Feeds winning patterns to Strategy for next cycle. |

---

## 2 · System-Level Swim Lane (linear view)

```
TRIGGER (Monday 3pm UTC or on-demand)
   │
   ▼
┌──────────────────── PRE-PRODUCTION ────────────────────┐
│                                                         │
│ 01 Trend Hunter  →  02 Strategy  →  03 Brief            │
│                         ▲               │               │
│                         │               ▼               │
│                    18 Analytics    04 Script            │
│                         ▲               │               │
│                         │               ▼               │
│                    17 Community    05 Storyboard        │
│                                         │               │
│                                         ▼               │
│                                06 Production Coord      │
│                                         │               │
└─────────────────────────────────────────┼───────────────┘
                                          │
                        ┌─────────────────┼─────────────────┐
                        │                 │                 │
             ▼ Mode A   ▼ Mode B          ▼ Mode C
      [Human Shooter]  07 AI Video Gen   08 Style Replication
                        │                 │                 │
                        └─────────────────┴────────┬────────┘
                                                   ▼
┌──────────────────── POST-PRODUCTION ───────────────────┐
│ 09 Ingest → 10 Edit Director → 11 Editor               │
│                                    │                   │
│                                    ▼                   │
│                               12 Sound                 │
│                                    │                   │
│                                    ▼                   │
│                               13 Motion                │
│                                    │                   │
│                                    ▼                   │
│                               14 QC ◄── (Lever 3/2/1)  │
│                                    │                   │
└────────────────────────────────────┼───────────────────┘
                                     │
                                     ▼
                     15 Localization (optional)
                                     │
                                     ▼
                               16 Publishing
                                     │
                                     ▼
              17 Community  ←→  18 Analytics  →  feeds 02 Strategy
                              (closes the loop)
```

---

## 3 · Mode Routing Logic (how Brief picks A / B / C)

The Brief Agent writes a `production_mode` field on every Brief. Logic:

```python
# Pseudocode — lives inside Brief Agent
def assign_mode(brief_input, strategy_row, brand_voice_json, capacity_state):
    # Mode C takes priority when a reference is explicitly given
    if strategy_row.reference_url or brief_input.replicate_style_of:
        return "C"  # Style Replication

    # Mode B for anything where Jamila on-camera is not required + AI stack is ready
    if (
        not brief_input.requires_human_on_camera
        and brand_voice_json.visual_identity.ai_video_eligible is True
        and capacity_state.ai_video_budget_remaining > 0
    ):
        return "B"  # AI-generated

    # Default Mode A — live shoot with human videographer
    return "A"
```

Triggers per mode:
- **Mode A** routes `Brief → Production Coord → [shoot packet to human] → 09 Ingest`
- **Mode B** routes `Brief → Production Coord → 07 AI Video Gen → 09 Ingest`
- **Mode C** routes `Brief → Production Coord → 08 Style Replication → 09 Ingest`

From Ingest onward, post-production is mode-agnostic.

---

## 4 · Handoff Contracts (JSON schemas — every agent-to-agent interface)

> All handoffs go through the Orchestrator's run-ledger. Each JSON payload has three top-level keys: `meta` (run id, mode, timestamp, from/to agent), `payload` (the actual work), and `checks` (pre-flight validation results).

### 4.1 Base envelope (wraps every handoff)

```json
{
  "meta": {
    "run_id": "ars-r-00042",
    "brand": "REINVENTED",
    "mode": "A",
    "from_agent": "03-brief",
    "to_agent": "04-script",
    "ts": "2026-04-24T20:00:00Z",
    "lever": 3,
    "attempt": 1
  },
  "payload": { /* agent-specific */ },
  "checks": {
    "schema_valid": true,
    "entity_firewall_pass": true,
    "brand_voice_version": "reinvented-v1.0"
  }
}
```

### 4.2 `01 Trend Hunter → 02 Strategy`

```json
{
  "payload": {
    "trend_radar_week": "2026-W17",
    "trends": [
      {
        "id": "trend-001",
        "format": "talking_head_hook_switch",
        "sound_id": "tiktok-sound-abc123",
        "sound_title": "[sound title]",
        "velocity": "rising|peak|cooling",
        "platform_fit": ["TT", "IG"],
        "topic_cluster": "solopreneur_systems",
        "creators_using": 127,
        "sample_refs": ["https://...", "https://..."],
        "pillar_fit": ["pillar_3_systems"],
        "novelty_score": 0.82
      }
    ]
  }
}
```

### 4.3 `02 Strategy → 03 Brief`

```json
{
  "payload": {
    "reel_plan_week": "2026-W17",
    "plan_rows": [
      {
        "reel_id": "REINV-2026-W17-001",
        "topic": "The operator's morning stack",
        "pillar": "pillar_3_systems",
        "hook_intent": "permission_to_simplify",
        "mode_hint": "A",
        "reference_url": null,
        "requires_human_on_camera": true,
        "target_length_sec": 45,
        "priority": 1,
        "due_publish": "2026-04-29T16:00:00Z"
      }
    ]
  }
}
```

### 4.4 `03 Brief → 04 Script`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "production_mode": "A",
    "brand_voice_ref": "reinvented-v1.0",
    "hook_pattern": "permission_flip",
    "body_structure": "3-beat (setup → tension → payoff)",
    "cta_template": "silent_authority",
    "banned_lexicon_source": "brand-voice-intake §6",
    "length_sec": 45,
    "format": {
      "aspect_ratio": "9:16",
      "frame_rate": 30,
      "captions": "burn-in",
      "talent": "Jamila on-camera"
    },
    "qc_targets": {
      "pillar_fit": "pillar_3_systems",
      "truth_echoes_required": 1,
      "voice_markers_min": 3
    }
  }
}
```

### 4.5 `04 Script → 05 Storyboard`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "script": {
      "hook": {
        "line": "If your morning needs 14 steps, you don't have a system. You have a hostage situation.",
        "duration_sec": 3,
        "delivery_note": "flat, no smile, eye contact"
      },
      "beats": [
        {
          "beat": 1,
          "line": "Everyone sells you a routine. Nobody sells you the cut list.",
          "duration_sec": 5
        },
        {
          "beat": 2,
          "line": "The operator's stack is five things. First meal. First decision. First system touched. First person called. First block closed.",
          "duration_sec": 20
        },
        {
          "beat": 3,
          "line": "Five. Not fourteen. Five moves and you're already ahead of the version of you that wakes up scrolling.",
          "duration_sec": 12
        }
      ],
      "cta": {
        "line": "Save this one.",
        "duration_sec": 3,
        "visual": "static card, gold on ivory"
      }
    },
    "voice_markers_detected": 5,
    "truth_echoes_detected": 2,
    "banned_vocab_flags": []
  }
}
```

### 4.6 `05 Storyboard → 06 Production Coord`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "shot_list": [
      {
        "shot": 1,
        "type": "medium close-up",
        "duration_sec": 3,
        "talent_action": "eye contact, no smile, hook delivery",
        "lighting": "window-left, natural, 5500K",
        "wardrobe": "ivory crewneck, no pattern",
        "location": "home office — neutral wall",
        "coverage": "1 take minimum, 3 preferred"
      }
    ],
    "bin_assets_needed": ["logo_ivory_gold", "lower_third_authority_v3"],
    "music_bed_direction": "ambient_piano_slow_120bpm",
    "total_shots": 7
  }
}
```

### 4.7 `06 Production Coord → 07/08/[human]`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "mode": "A",
    "packet_type": "shoot_packet",
    "vendor": {
      "type": "human_videographer",
      "contact": "[videographer name]",
      "shoot_date": "2026-04-28",
      "deliverable_by": "2026-04-29T00:00:00Z",
      "format_spec": "ProRes 422 HQ, 9:16, 4K"
    },
    "attached": {
      "brief_url": "notion://...",
      "script_url": "notion://...",
      "storyboard_url": "notion://...",
      "wardrobe_note": "ivory crewneck",
      "location_confirmed": true
    }
  }
}
```

### 4.8 `09 Ingest → 10 Edit Director`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "asset_bundle": {
      "raw_footage": [
        {"file": "drive://.../shot_1_take_3.mov", "duration_sec": 18, "shot_ref": 1}
      ],
      "audio": ["drive://.../lav_take_3.wav"],
      "assets_pulled": ["logo_ivory_gold.png", "lt_authority_v3.mogrt"],
      "music_bed": "drive://.../ambient_piano_slow_120bpm.wav"
    },
    "spec_check": {
      "aspect_ok": true,
      "frame_rate_ok": true,
      "audio_sync_ok": true,
      "missing_shots": []
    }
  }
}
```

### 4.9 `10 Edit Director → 11 Editor`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "edit_plan": {
      "cut_order": [
        {"shot_ref": 1, "in_ms": 0, "out_ms": 3000},
        {"shot_ref": 2, "in_ms": 3000, "out_ms": 8000}
      ],
      "pacing_bpm": 120,
      "cut_rhythm": "quarter-note on beats, syncopated on b-roll",
      "caption_style": "burn-in, 48pt, ivory on black box, 80% opacity",
      "lower_thirds": [{"at_ms": 8000, "content": "THE OPERATOR'S STACK", "style": "authority_v3"}],
      "transitions": "hard cuts only — zero fades, zero wipes, zero zooms (brand rule)"
    }
  }
}
```

### 4.10 `11 Editor → 12 Sound`

Payload: v1 edit file + EDL. Sound adds VO polish, music bed, SFX accents, loudness pass.

### 4.11 `12 Sound → 13 Motion`

Payload: v2 edit with finalized audio. Motion adds typography, overlays, motion tokens.

### 4.12 `13 Motion → 14 QC`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "v3_final_file": "drive://.../REINV-W17-001-v3.mp4",
    "duration_sec": 43,
    "format": "9:16 · 1080x1920 · 30fps · -14 LUFS",
    "self_check": {
      "voice_markers_in_captions": 5,
      "truth_echoes": 2,
      "banned_vocab_hits": 0,
      "motion_tokens_applied": true
    }
  }
}
```

### 4.13 `14 QC → Lever Router → 15/16 Publishing`

QC outputs verdict: `PASS` / `FAIL_FIXABLE` / `FAIL_RESHOOT`. Verdict routes:
- **PASS + Lever 3:** → Human approval queue → on approve → 15 Localization
- **PASS + Lever 2:** sampled (see §8) → approval queue OR direct to 15
- **PASS + Lever 1:** → direct to 15
- **FAIL_FIXABLE:** → back to 11 Editor (specific fix note)
- **FAIL_RESHOOT:** → escalate to Jamila + back to 06 Production Coord

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "verdict": "PASS",
    "qc_scorecard": {
      "brand_voice": 10,
      "pillar_fit": "pillar_3_systems · match",
      "entity_firewall": "clean",
      "format_spec": "match",
      "caption_spec": "match",
      "hook_strength": 9,
      "cta_present": true,
      "overall": "PASS — route to Lever"
    }
  }
}
```

### 4.14 `16 Publishing → 17/18 Learning Loop`

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "published_at": "2026-04-29T16:00:00Z",
    "posts": [
      {"platform": "IG", "url": "https://instagram.com/p/...", "post_id": "ig-..."},
      {"platform": "TT", "url": "https://tiktok.com/@.../video/...", "post_id": "tt-..."},
      {"platform": "LI", "url": "https://linkedin.com/posts/...", "post_id": "li-..."}
    ],
    "monitor_windows": ["24h", "7d", "28d"]
  }
}
```

### 4.15 `18 Analytics → 02 Strategy` (closes the loop)

```json
{
  "payload": {
    "reel_id": "REINV-2026-W17-001",
    "metrics_at": "2026-05-06T16:00:00Z",
    "window": "7d",
    "per_platform": {
      "IG": {"views": 18400, "hook_retention_3s": 0.71, "saves": 412, "shares": 89, "dms": 14, "profile_visits": 267},
      "TT": {"views": 42100, "hook_retention_3s": 0.68, "saves": 901, "shares": 210, "completion": 0.41}
    },
    "score_vs_baseline": 1.34,
    "winners": ["permission_flip hook", "five-move structure", "no-smile delivery"],
    "losers": [],
    "feed_forward": "double down permission_flip in W18; no change to pillar mix"
  }
}
```

---

## 5 · Dependency Graph (who blocks whom)

```
01 Trend Hunter  ──┐
                   ├──► 02 Strategy ──► 03 Brief ──► 04 Script ──► 05 Storyboard ──► 06 Production Coord
18 Analytics ──────┤
17 Community ──────┘                                                                 │
                                                                                     │
                                               ┌─────────────────┬───────────────────┤
                                               ▼                 ▼                   ▼
                                           Mode A          07 AI Video Gen   08 Style Replication
                                      (human shoot)          (Mode B)             (Mode C)
                                               │                 │                   │
                                               └─────────────────┼───────────────────┘
                                                                 ▼
09 Ingest ──► 10 Edit Director ──► 11 Editor ──► 12 Sound ──► 13 Motion ──► 14 QC
                                                                              │
                                                           ┌──────────────────┼──────────────────┐
                                                           ▼                  ▼                  ▼
                                                      FAIL_FIXABLE        FAIL_RESHOOT       PASS
                                                      (back to 11)       (back to 06)        │
                                                                                              ▼
                                                                                  Lever Router
                                                                                              │
                                                                                  ┌───────────┼───────────┐
                                                                                  ▼           ▼           ▼
                                                                              Lever 3     Lever 2     Lever 1
                                                                           (100% review) (sampled)    (auto)
                                                                                  │           │           │
                                                                                  └───────────┼───────────┘
                                                                                              ▼
                                                                              15 Localization (opt) ──► 16 Publishing
                                                                                              │
                                                                                  ┌───────────┴───────────┐
                                                                                  ▼                       ▼
                                                                          17 Community           18 Analytics
                                                                                  │                       │
                                                                                  └──────► loops back to 02 Strategy
```

**Hard blockers (upstream must complete before downstream starts):**
- 02 Strategy blocks 03 Brief (no plan = no brief)
- 03 Brief blocks 04 Script and mode routing
- 05 Storyboard blocks 06 Production Coord (no shot list = nothing to shoot)
- 09 Ingest blocks 10–14 (post pipeline needs assets)
- 14 QC blocks 15/16 (no unreviewed reel posts)

**Soft dependencies (can run in parallel after initial burst):**
- 17 Community + 18 Analytics run continuously in background — not blockers
- 01 Trend Hunter runs weekly Monday 3pm UTC — decoupled from reel production
- 15 Localization is optional — can skip for single-platform reels

---

## 6 · Trigger Map (what starts each agent)

| Agent | Trigger | Frequency | Input source |
|---|---|---|---|
| 01 Trend Hunter | Monday 3pm UTC cron | Weekly | Platform APIs + saved search feeds |
| 02 Strategy | Mon 4pm UTC (after Trend Hunter) | Weekly | Trend Radar + Analytics feed-forward + Brand Voice JSON |
| 03 Brief | On Strategy output row + manual trigger (on-demand) | Per reel | Reel Plan row |
| 04 Script | On Brief completion | Per reel | Brief JSON |
| 05 Storyboard | On Script completion | Per reel | Script JSON + Brand Voice visual spec |
| 06 Production Coord | On Storyboard completion | Per reel | Brief + Script + Storyboard bundle |
| 07 AI Video Gen | On Production Coord (mode=B) | Per reel | Gen packet |
| 08 Style Replication | On Production Coord (mode=C) | Per reel | Gen packet + reference URL |
| 09 Ingest | On Mode A shooter upload / Mode B/C gen complete | Per reel | Raw assets |
| 10 Edit Director | On Ingest completion | Per reel | Asset bundle + Brief/Script/Storyboard |
| 11 Editor | On Edit Director handoff | Per reel | Edit plan + assets |
| 12 Sound | On Editor v1 | Per reel | v1 edit |
| 13 Motion | On Sound v2 | Per reel | v2 edit |
| 14 QC | On Motion v3 | Per reel | v3 final |
| Lever Router (orchestrator) | On QC PASS | Per reel | QC verdict + current Lever |
| 15 Localization | On Lever approval (if multi-platform variants needed) | Per reel | Approved final |
| 16 Publishing | On Lever approval (+ Localization if used) | Per reel | Approved final + platform manifest |
| 17 Community | Every 30 min post-publish for 7 days | Continuous | Comment + DM streams |
| 18 Analytics | 24h / 7d / 28d after publish | Windowed | Platform insights APIs |

---

## 7 · Data Store Contract (where each agent reads + writes)

**Canon stores:**
- **Notion** — human-facing records. Reel Plan, Reel Record, Approvals queue, QC scorecards, blocker log.
- **Drive** — media files (raw footage, v1/v2/v3 edits, final mp4s, assets, source projects).
- **JSON run-ledger** (Cowork artifact `ars-run-ledger`, future build) — machine-facing event log. Every handoff envelope written here.
- **Brand Voice JSON** — read-only canon at `ars/ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §16. Referenced by version string (e.g. `reinvented-v1.0`).
- **Ayrshare** — publishing target (Publishing agent writes here).

**Per-agent read/write contract:**

| Agent | Reads | Writes |
|---|---|---|
| 01 Trend Hunter | Platform APIs | Notion: Trend Radar DB |
| 02 Strategy | Trend Radar DB, Analytics feed-forward, Brand Voice JSON | Notion: Reel Plan DB |
| 03 Brief | Reel Plan row, Brand Voice JSON | Notion: Reel Record (brief block) |
| 04 Script | Reel Record brief | Notion: Reel Record (script block) |
| 05 Storyboard | Reel Record script + Brand Voice visual spec | Notion: Reel Record (storyboard block) |
| 06 Production Coord | Full Reel Record | Drive: shoot packet folder, Notion: Vendor assignment |
| 07 AI Video Gen | Gen packet, Brand Voice visual spec | Drive: raw gen output folder |
| 08 Style Replication | Gen packet + ref URL | Drive: raw gen output folder |
| 09 Ingest | Raw assets folder | Notion: Asset Manifest, flag spec failures |
| 10 Edit Director | Asset Manifest + Reel Record | Notion: Edit Plan block |
| 11 Editor | Edit Plan + raw assets | Drive: `/reels/[reel_id]/v1.mp4` |
| 12 Sound | v1 edit | Drive: `/reels/[reel_id]/v2.mp4` |
| 13 Motion | v2 edit | Drive: `/reels/[reel_id]/v3-final.mp4` |
| 14 QC | v3 final + Brand Voice JSON | Notion: QC Scorecard, Verdict |
| 15 Localization | v3 final | Drive: platform variants folder |
| 16 Publishing | Approved final + manifest | Ayrshare, then Notion: Post URLs on Reel Record |
| 17 Community | Comments + DMs streams | Notion: Community Signals DB |
| 18 Analytics | Platform insights APIs | Notion: Reel Metrics block on Reel Record, Feed-forward doc |

**File path conventions (locked):**
```
Drive/Sequel Digital/ARS/
├── brands/
│   └── REINVENTED/
│       ├── brand-voice-v1.0.json           (read-only canon)
│       ├── assets/
│       │   ├── logos/
│       │   ├── motion-tokens/
│       │   └── music-beds/
│       └── reels/
│           └── [reel_id]/
│               ├── brief.json
│               ├── script.json
│               ├── storyboard.json
│               ├── shoot-packet/
│               ├── raw/
│               ├── v1.mp4
│               ├── v2.mp4
│               ├── v3-final.mp4
│               ├── qc-scorecard.json
│               └── published-manifest.json
```

---

## 8 · Lever Router Logic (human intervention gating)

```python
def route_on_pass(reel_id, lever, sample_policy, recent_verdicts):
    # Lever 3 — approve every reel
    if lever == 3:
        return "queue_for_human_approval"

    # Lever 2 — sampled approval
    if lever == 2:
        if sample_policy == "1_in_5":
            if hash(reel_id) % 5 == 0:
                return "queue_for_human_approval"
            else:
                return "auto_publish"
        if sample_policy == "1_in_10":
            if hash(reel_id) % 10 == 0:
                return "queue_for_human_approval"
            else:
                return "auto_publish"
        # Weighted by novelty: new-pattern reels sampled more often
        if sample_policy == "novelty_weighted":
            if reel_id.pattern_is_new(recent_verdicts):
                return "queue_for_human_approval"
            else:
                return "auto_publish"

    # Lever 1 — full autonomy
    if lever == 1:
        return "auto_publish"
```

**Sample policy selection is OPEN QUESTION #2** on dashboard. Default until Jamila picks: `1_in_5`. Write this clearly in the Lever 2 graduation checklist.

**Escalation rules (always run, regardless of Lever):**
- Entity firewall violation → never auto-publish, always human escalation
- Truth echo missing → never auto-publish
- Banned vocab hit → never auto-publish
- QC verdict `FAIL_RESHOOT` → always human escalation (Jamila decides: reshoot or kill)
- Reel metrics score < 0.5× baseline on 24h → Analytics flags to Strategy for pattern review

---

## 9 · Failure + Retry Logic

**Three failure classes:**

| Class | Example | Action |
|---|---|---|
| **Transient** | API timeout, rate limit, tool momentary failure | Exponential backoff: 5s, 30s, 2min, 10min. Max 4 tries. Then escalate. |
| **Content** | QC FAIL_FIXABLE, banned vocab hit, missing voice markers | Route to upstream agent with specific fix note. Max 2 rewrite cycles then escalate. |
| **Structural** | Schema violation, missing upstream artifact, broken dependency | Hard stop. Write to blocker log. Escalate to Jamila immediately via SMS. |

**Retry state kept in run-ledger:**
```json
{
  "run_id": "ars-r-00042",
  "attempts": [
    {"agent": "14-qc", "attempt": 1, "ts": "...", "verdict": "FAIL_FIXABLE", "note": "missing voice marker 'move' in caption"},
    {"agent": "11-editor", "attempt": 1, "ts": "...", "note": "re-cut with voice marker"},
    {"agent": "14-qc", "attempt": 2, "ts": "...", "verdict": "PASS"}
  ]
}
```

---

## 10 · Observability Requirements

Every run must emit:
- **Run start** event (reel_id, mode, lever)
- **Per-agent start + end** events (timestamp, duration, verdict)
- **Handoff envelopes** (logged in run-ledger)
- **Approval events** (who approved, when, what lever)
- **Publish events** (platform + URL)
- **Metrics events** (24h, 7d, 28d)

**Dashboard must show (Week 2 build target for `agentic-reel-studio` artifact):**
- In-flight reels (queue depth per agent)
- Avg cycle time (Brief → Published) per mode
- QC pass rate (first pass / after fix)
- Lever mix this week (% auto vs. approved)
- Top-performing reel pattern (rolling 7d + 28d)
- Blockers count + oldest age

---

## 11 · Brand Firewall (inherited from Brand Voice Intake §6)

**Every agent enforces:**
1. NO mentions of: Holdco Group, Principal, NPOX, 4821 Main, SITE-C-BRAND, Retail Supply, Partner Brand, SLN in output (unless explicit Sequel Digital client engagement with those brands is active and separately encoded).
2. NO internal tool names in reel output: no "Claude," "Cowork," "Marblism," "Lovable," "GHL," "Notion," "Ayrshare," "HeyGen," "Runway," "ElevenLabs."
3. NO "genuinely," "honestly," or "straightforward" (per Jamila user preferences, extended to brand).
4. All output must pass the 11-point QC gate in Brand Voice Intake §13 before any agent downstream of QC touches it.
5. Version pinning: every reel record stores the `brand_voice_version` it was produced against. Post-hoc audits possible.

**QC Agent is the final firewall.** If QC misses, Lever Router double-checks on entity + banned vocab.

---

## 12 · Mode-Specific Implementation Notes

### Mode A — Live Shoot (Week 2 target)

- Human videographer receives Shoot Packet 24–48h pre-shoot
- Jamila = talent
- Wardrobe: brand voice JSON §7 visual identity
- Location: neutral, window-lit preferred
- Coverage: 1 take minimum per shot, 3 preferred
- Audio: lav + boom backup
- Turnaround from shoot to Ingest: < 24h

### Mode B — AI-Generated (Week 4 target)

- HeyGen avatar = Jamila's trained digital twin (v2 target by Week 4 per milestone plan)
- Runway/Sora/Veo for b-roll — prompt library built from Brand Voice visual spec
- ElevenLabs for voice (backup to HeyGen native voice)
- No live shoot required
- Cost per reel ceiling: $TBD (OPEN — see Pricing Model v1 Saturday deliverable)

### Mode C — Style Replication (Week 5 target)

- Input: 1–3 reference reel URLs the client wants replicated
- Style Replication Agent extracts: cut rhythm, palette, type, motion, pacing
- REINVENTED voice + content layered on top (NOT the source's content or voice)
- Output flagged "style-derived from [ref]" in internal notes for legal clarity
- Client signs reference consent in intake

---

## 13 · Week 2 Implementation Checklist (what builds next)

This blueprint unlocks Week 2. Concrete build list:

**Agents to stand up (existing Week 2 milestone):**
- [ ] 02 Strategy — Claude skill + Notion Reel Plan DB writer
- [ ] 03 Brief — Claude skill (consume Brand Voice JSON + Reel Plan row)
- [ ] 04 Script — Claude skill (REINVENTED voice enforced)
- [ ] 05 Storyboard — Claude skill (Alux-style shot language)
- [ ] 06 Production Coord — Notion writer + Drive folder setup + vendor routing
- [ ] 09 Ingest — Drive watcher + spec validator
- [ ] 10 Edit Director — Claude skill (edit plan JSON output)
- [ ] 11 Editor — Human-in-the-loop for Week 2 (agent drafts EDL, human executes in editor app). Full automation Week 4–5.

**Infrastructure:**
- [ ] Notion: Reel Plan DB, Reel Record DB, QC Scorecard DB, Community Signals DB, Reel Metrics block
- [ ] Drive: `/Sequel Digital/ARS/brands/REINVENTED/` tree per §7
- [ ] Run-ledger: Cowork artifact `ars-run-ledger` (JSON-backed)
- [ ] JSON schema validators: one per handoff contract in §4

**Contracts:**
- [ ] Every JSON schema in §4 lint-validated (pydantic or zod)
- [ ] Handoff envelopes logged to run-ledger on every transition

**First reel test (exit criteria):**
- [ ] Brief → Script → Storyboard produces usable output in < 5 min no rework (inherited from Week 1 exit criteria)
- [ ] One Mode A reel runs end-to-end with Lever 3 approval

---

## 14 · Mode Routing Decision Tree (visual reference)

```
                    NEW REEL BRIEF
                         │
                         ▼
             ┌─── replicate_style_of set? ───┐
             │                                │
            YES                               NO
             │                                │
             ▼                                ▼
          MODE C                 ┌──── requires_human_on_camera? ───┐
                                 │                                    │
                                YES                                   NO
                                 │                                    │
                                 ▼                                    ▼
                              MODE A                     ┌─ ai_video_eligible + budget OK? ─┐
                                                         │                                    │
                                                        YES                                   NO
                                                         │                                    │
                                                         ▼                                    ▼
                                                      MODE B                               MODE A
                                                                                         (fallback)
```

---

## 15 · Open Questions (still parked, from Apr 22)

1. **HC brands as paid Sequel Digital clients?** Affects multi-brand memory design (Week 5). Non-blocking through Week 4.
2. **Lever 2 sampling rate?** Default = 1 in 5 until Jamila picks. Non-blocking through Week 3.
3. **Week 6 cold outreach list?** Affects Pricing + Landing Page copy. Non-blocking through Week 5.
4. **Pricing anchor?** Retainer (current default per Competitor Scan) vs. reel-count vs. outcome. Non-blocking until Week 6.

**New Q from this blueprint (non-blocking):**
5. **Agent count for marketing copy** — "14 Claude agents + AI video stack" (current tagline) vs. "17 agents" (dashboard) vs. "18 specialized + 1 orchestrator" (this doc). Recommend: keep "14 Claude agents" in public copy (honest — excludes AI video stack wrappers), keep 18 as internal canon. Flag for Saturday refresh.
6. **Sample policy for Lever 2** — beyond rate, is it random, round-robin, or novelty-weighted? Recommend: novelty-weighted (new pattern = always reviewed, established pattern = 1-in-10 spot-check). Non-blocking.

---

## 16 · Blueprint version + versioning policy

- **v1.0 locked:** April 24, 2026
- **Next review:** May 1, 2026 (end of Week 2) — after first 5 Mode A reels run against this wiring
- **Changes require:** a changelog entry, a bumped version string, and a sweep of all agents that embed schemas (regenerate validators)

**Versioning rules:**
- Patch (v1.0.x) — bug fix / typo / clarification. No agent rebuild.
- Minor (v1.x.0) — new handoff field (additive only). Validator re-gen, no agent rewrite.
- Major (v2.0.0) — schema-breaking. Full migration doc required.

---

## 17 · Handoff Contract Index (quick reference)

| From → To | §4 ref | Key payload fields |
|---|---|---|
| 01 → 02 | 4.2 | trend_radar_week, trends[] |
| 02 → 03 | 4.3 | reel_plan_week, plan_rows[] |
| 03 → 04 | 4.4 | production_mode, hook_pattern, qc_targets |
| 04 → 05 | 4.5 | script{hook,beats,cta}, voice_markers_detected |
| 05 → 06 | 4.6 | shot_list[], bin_assets_needed, music_bed_direction |
| 06 → 07/08/human | 4.7 | packet_type, vendor, attached refs |
| 09 → 10 | 4.8 | asset_bundle, spec_check |
| 10 → 11 | 4.9 | edit_plan{cut_order, pacing_bpm, captions, transitions} |
| 11 → 12 | 4.10 | v1 edit + EDL |
| 12 → 13 | 4.11 | v2 edit |
| 13 → 14 | 4.12 | v3_final_file, self_check |
| 14 → Lever | 4.13 | verdict, qc_scorecard |
| 16 → 17/18 | 4.14 | published_at, posts[], monitor_windows |
| 18 → 02 | 4.15 | per_platform metrics, winners, feed_forward |

---

## 18 · Sign-off

This blueprint is the canon wiring for ARS Week 2 build. Every agent built after 4/24/26 must read this doc first. Changes to interfaces require a version bump and a downstream sweep.

**Next session target:** Service Tier + Pricing Model v1 (closes Week 1 deliverable set).

*— Agentic Reel Studio Daily Build, Day 5 of 42*
