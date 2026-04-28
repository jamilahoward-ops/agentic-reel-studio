# ARS — Script Agent v1.0 SPEC

**Date:** April 28, 2026 (Tuesday — Day 9 · Week 2 Day 2 overnight build)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Build phase:** Week 2 mid. Brief Agent v1.0 LLM-test executes Tue daytime; Script Agent SPEC drafted Tue overnight; Script Agent SKILL bundle Wed overnight (Day 10).
**Status:** v1.0 LOCKED for Wed 4/29 implementation. No code tonight — spec only.
**Predecessor agent:** Brief Agent (consumes its `brief.json` output as canonical input).
**Successor agent:** Storyboard Agent (consumes Script Agent's `script.json` output).

---

## §1. Purpose & Position in Pipeline

The **Script Agent** is the third agent in the ARS pre-production stage and the **second content-generating agent** in the pipeline. It converts a structured creative brief (`brief.json`) into a **fully-speakable, beat-aligned script** with on-screen text, b-roll cues, voiceover cadence marks, and platform-specific variants — ready for the Storyboard Agent to translate into a shot-by-shot visual plan.

**Pipeline position (per Orchestration Blueprint §5):**
```
Trend Hunter → Strategy → Brief → SCRIPT AGENT → Storyboard → Production Coord → Edit → QC → Publish → Loop
```

**Why the Script Agent matters:** A reel is a script delivered visually. If the Brief Agent is the integrity gate, the Script Agent is the **performance gate** — it is where the brief's strategic intent becomes performable language. The script controls retention curves, hook delivery, pace, and cognitive load. A weak script wastes a strong brief.

**Hand-off contract enforced:**
- INPUT contract: Script Agent reads `brief.json` per Brief Agent v1.0 output schema (`schemas/brief-agent/output.schema.json`). It NEVER re-derives strategy — the brief is canonical.
- OUTPUT contract: Script Agent emits `script.json` per §3.1 of this spec. Storyboard Agent consumes this without further interpretation.

**Single-responsibility line:** *"Speakable language from a strategic brief."* If the Script Agent is making creative-strategy decisions (audience, pillar selection, format choice), that is a leak from upstream — flag it, do not absorb it.

---

## §2. Inputs (Full Schema)

The Script Agent consumes **one required input** and **two optional inputs**.

### 2.1 Required input

| Field | Source | Type | Required |
|-------|--------|------|----------|
| `brief` | Brief Agent v1.0 `brief.json` (success branch) | object | YES |

The brief MUST validate against `schemas/brief-agent/output.schema.json` successBrief variant. If the brief is an errorEnvelope, REJECT and return `input_validation_failed`.

### 2.2 Optional inputs

| Field | Source | Type | Required |
|-------|--------|------|----------|
| `prior_scripts` | Last 5 scripts for this brand (memory loop) | array | NO |
| `style_overrides` | Operator-supplied tone/word swaps | object | NO |
| `talent_profile` | Speaker constraints (length, vocabulary, pace) | object | NO |

### 2.3 Input JSON schema (canonical)

```json
{
  "brief": { /* full Brief Agent successBrief object */ },
  "prior_scripts": [ /* up to 5 most recent script.json objects, oldest first */ ],
  "style_overrides": {
    "swap_words": { "operator": "leader" },
    "force_register": "peer-to-peer | mentor | reporter | null",
    "explicit_taglines": null
  },
  "talent_profile": {
    "speaker_id": "REINVENTED-Jamila-v1",
    "max_words_per_minute": 165,
    "preferred_sentence_length_words": 14,
    "ad_lib_allowed": true,
    "vocal_range": "alto-warm",
    "regionalisms_allowed": ["LA-vernacular"]
  },
  "session_id": "ars-2026-04-29-001",
  "lever_state": 3
}
```

### 2.4 Input validation rules

- `brief.brand_id` must NOT be Holdco Group, 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A. If it is → REJECT with `entity_firewall_breach`. (Inherited from Brief Agent firewall — Script Agent re-validates as defense in depth.)
- `brief.lever` must be in `[1, 2, 3]`. Lever-state propagates from brief; Script Agent does not override.
- `brief.tier` must be in `[Pilot, Starter, Pro, Enterprise]`.
- `prior_scripts` length capped at 5.
- All inputs sanitized for prompt-injection markers (`<|im_start|>`, jailbreak phrases, cross-entity leaks).
- If `talent_profile.max_words_per_minute` < 100 or > 220 → REJECT with `talent_profile_out_of_range`.
- `style_overrides.swap_words` keys must NOT collide with `brief.do_not_say` (banned terms cannot be swapped IN — only out).

---

## §3. Outputs (Full Schema — `script.json`)

The Script Agent produces **one canonical output**: a JSON object that conforms to the schema below. No markdown, no commentary.

### 3.1 Output JSON schema

```json
{
  "script_id": "script-REINVENTED-2026-04-29-001",
  "brief_id": "brief-REINVENTED-2026-04-27-001",
  "brand_id": "REINVENTED",
  "tier": "Pilot",
  "lever": 3,
  "production_mode": "A",
  "created_at": "2026-04-29T07:00:00Z",
  "session_id": "ars-2026-04-29-001",

  "title_working": "The 7-Figure Burnout Trap",
  "duration_target_seconds": 55,
  "duration_min": 50,
  "duration_max": 60,
  "estimated_word_count": 138,

  "hook_block": {
    "spoken_line": "You hit seven figures and now you can't sleep. That's not success — that's a warning sign.",
    "first_frame_text": "7-FIGURE BURNOUT IS NOT A FLEX",
    "delivery_note": "drop tone on 'success' — pause 0.4s before 'warning sign'",
    "duration_seconds": 3.0,
    "cps_target": 16.5
  },

  "lines": [
    {
      "line_id": "L1",
      "second_start": 0.0,
      "second_end": 3.0,
      "beat_id": "B1",
      "spoken": "You hit seven figures and now you can't sleep. That's not success — that's a warning sign.",
      "on_screen_text": "7-FIGURE BURNOUT IS NOT A FLEX",
      "delivery": "direct-to-camera",
      "pace_marker": "fast-open",
      "emphasis_words": ["seven figures", "warning sign"],
      "broll_cue": "none — face-on hook",
      "music_cue": "in @ 0.0 — low-mid pad, tension",
      "sfx_cue": null,
      "caption_style": "bold-yellow-jamila"
    }
    /* …5 to 12 line objects total… */
  ],

  "broll_plan": [
    {
      "cue_id": "BR1",
      "second_start": 10.0,
      "second_end": 14.0,
      "description": "operator-at-desk-3am, blue light, no face visible — overlay metaphor",
      "source_hint": "stock | shot-this-week | archive",
      "no_buildings_rule": "interior framing only; no skyline, no aspirational external buildings",
      "alt_options": 2
    }
  ],

  "captions": {
    "style": "bold-yellow-jamila",
    "max_chars_per_line": 22,
    "max_lines_on_screen": 2,
    "burn_in_required": true,
    "language": "en-US",
    "auto_punctuation": true,
    "censor_profile": "platform-safe"
  },

  "audio_track": {
    "voice_take_count": 2,
    "voice_pacing": "operator-conversational-165wpm",
    "music_intent": "low-tension to mid-resolve",
    "music_swells": [
      { "second_start": 25.0, "second_end": 35.0, "intent": "reframe lift" }
    ],
    "sfx_inventory": ["whoosh@hook-end", "soft-click@beat-3", "tone-down@close"],
    "vo_only_acceptable": false,
    "duck_under_speech_db": -12
  },

  "platform_variants": [
    {
      "platform": "instagram-reels",
      "aspect": "9:16",
      "duration_seconds": 55,
      "hook_first_frame": "7-FIGURE BURNOUT IS NOT A FLEX",
      "first_3s_optimization": "face-on, big text, no logo",
      "caption_burn": true
    },
    {
      "platform": "tiktok",
      "aspect": "9:16",
      "duration_seconds": 55,
      "hook_first_frame": "she hit 7 figures and broke",
      "first_3s_optimization": "lowercase + native text",
      "caption_burn": true
    },
    {
      "platform": "linkedin-video",
      "aspect": "1:1",
      "duration_seconds": 60,
      "hook_first_frame": "Seven figures. No sleep. Warning sign.",
      "first_3s_optimization": "title-case + business framing",
      "caption_burn": true
    }
  ],

  "on_screen_text_blocks": [
    { "second_start": 0.0, "second_end": 3.0, "text": "7-FIGURE BURNOUT IS NOT A FLEX", "size": "XL", "anchor": "center" },
    { "second_start": 25.0, "second_end": 30.0, "text": "BURNOUT = SYSTEM FAILURE", "size": "L", "anchor": "lower-third" }
  ],

  "cta_block": {
    "type": "soft",
    "spoken_line": "If this hits, the link in bio is where I work this out with operators like you.",
    "on_screen_text": "REINVENTED — link in bio",
    "duration_seconds": 4.0,
    "second_start": 51.0,
    "second_end": 55.0
  },

  "rationale": {
    "why_this_pacing": "165wpm fits operator-peer register; faster reads as guru, slower reads as therapy.",
    "why_this_first_frame": "Brief mandates 'no buildings' — a black-card text hook converts highest in this register.",
    "why_this_broll_density": "Mode A (Pilot) — low-cost b-roll plan, max 3 cues, archive-eligible."
  },

  "qc_pre_flags": [
    "duration_within_band",
    "no_banned_vocabulary",
    "no_entity_breach",
    "captions_under_22_chars_per_line",
    "no_buildings_rule_acknowledged"
  ],

  "qc_warnings": [],

  "downstream_dependencies": {
    "storyboard_agent": "Convert each line + broll cue + on-screen text block into a shot-frame plan. Honor pace_marker and emphasis_words.",
    "production_coord_agent": "Schedule shoot day OR locate b-roll source per source_hint.",
    "edit_agent": "Cut to pace_marker; respect duck_under_speech_db; render captions at burn_in_required."
  },

  "metadata": {
    "agent_version": "1.0",
    "model_used": "claude-opus-4-6",
    "prompt_template_id": "script-agent-v1-prompt-2026-04-29",
    "tokens_in": 0,
    "tokens_out": 0,
    "latency_ms": 0,
    "qc_score_predicted": 0.86,
    "human_review_required": true,
    "iteration_count": 1
  }
}
```

### 3.2 Output validation rules

- All required schema fields present.
- `lines[]` length between 5 and 12.
- `lines[*].second_end > lines[*].second_start` for every line.
- Lines are CONTINUOUS — no time gaps > 0.4s except deliberate beat pauses (flag in qc_warnings).
- Last line's `second_end` ≤ `duration_target_seconds + 1`.
- Sum of spoken-line durations ≤ `duration_target_seconds × 1.05` (leaves room for breath).
- `cta_block.second_start ≥ duration_target_seconds − 6` (CTA in final 6 seconds).
- `do_not_say` from brief — verbatim absence-check across every `lines[*].spoken` and `on_screen_text` field. Hard fail if any banned term appears.
- `no_buildings_rule` honored on every `broll_plan[*]`.
- `platform_variants[]` length ≥ 1.
- `caption_burn` true on every variant where `tier ∈ [Pilot, Starter]` (cheaper rendering, mandatory burn-in).

### 3.3 Error envelope (validation-failure variant)

```json
{
  "error": "input_validation_failed | entity_firewall_breach | tier_constraint_violation | duration_overflow | banned_vocab_leaked | schema_invalid_after_retry | script_agent_failed | talent_profile_out_of_range | brief_not_success",
  "reason": "human-readable description",
  "field": "lines[3].spoken",
  "attempts": 2,
  "qc_warnings": []
}
```

---

## §4. Tier Constraints (CRITICAL — must not violate)

| Tier | Max lines | Max b-roll cues | Caption burn | Voice takes | Music swells | Platform variants |
|------|-----------|-----------------|--------------|-------------|--------------|-------------------|
| Pilot | 8 | 3 | required | 2 | 1 | 3 (IG, TT, LI) |
| Starter | 8 | 3 | required | 2 | 1 | 3 |
| Pro | 12 | 6 | optional | 3 | 2 | 4 (+ YT Shorts) |
| Enterprise | 12 | unlimited | optional | 4 | 3 | 5 (+ X) |

**Production-mode pairing (from brief):**
- **Mode A** (Pilot/Starter/Pro/Ent): single-speaker, low-cost b-roll, archive-eligible. Default.
- **Mode B** (Pro/Ent only): split-speaker / dialogue-style. Brief MUST authorize.
- **Mode C** (Enterprise only): cinematic, multi-location, full crew. Brief MUST authorize.

**Mode mismatch behavior:** If brief specifies Mode B/C and tier doesn't authorize → reject with `tier_constraint_violation`. (This shouldn't happen — Brief Agent enforces upstream. Defense in depth.)

---

## §5. The 9-step Process (LOCKED — same shape as Brief Agent)

The Script Agent runs in **9 sequential steps**. Skipping or reordering = automatic regeneration.

### Step 1 — Validate brief

Confirm `brief` is the success variant (NOT errorEnvelope). Confirm all required brief fields present. Confirm `brand_id` not in entity firewall list. If invalid → HALT, return `{"error": "input_validation_failed", "reason": "..."}`.

### Step 2 — Load brief context

Parse the brief into a working object: hook, beats, audience, tier, lever, production_mode, do_say, do_not_say, visual_direction, audio_direction, cta. These are SACRED — Script Agent does not override.

### Step 3 — Inflate beats into lines

Each beat from `brief.structure.beats[]` becomes 1–3 lines. Allocate seconds within each beat's `second` range. Reserve 0.0–3.0s for hook line. Reserve last 4–6s for CTA. Build a line-by-line timing skeleton.

### Step 4 — Compose spoken language

For each line, write the speakable sentence. Constraints:
- Honor `do_say` register; absence-check `do_not_say`.
- Average sentence length ≤ `talent_profile.preferred_sentence_length_words` (default 14).
- Words per minute ≤ `talent_profile.max_words_per_minute` (default 165).
- No filler/hedging tokens ("um", "like", "you know") unless `style_overrides.ad_lib_allowed = true`.
- Hook line copied verbatim from `brief.hook.first_3_seconds` — **NEVER rewritten**.

### Step 5 — On-screen text + caption strategy

For each line, decide if a separate on-screen text block runs underneath. Constraints:
- Hook line ALWAYS has a `first_frame_text` (the visual mirror, not a transcript copy).
- Reframe beat ALWAYS has an on-screen text block.
- CTA ALWAYS has an on-screen text block.
- Captions: `max_chars_per_line` 22, `max_lines_on_screen` 2.
- Pilot/Starter: caption burn-in MANDATORY.

### Step 6 — B-roll plan

Build `broll_plan[]`. Constraints:
- Tier cap (§4) on total cues.
- Each cue: time range, description, source hint, `no_buildings_rule` acknowledgment, ≥2 alt options.
- Hook (0–3s) is FACE-ON or BLACK-CARD — no b-roll on hook unless brief explicitly authorizes.
- B-roll never overlaps the CTA (final 4–6s = face + CTA text only).

### Step 7 — Audio plan

Build `audio_track`. Constraints:
- 2 voice takes (Pilot/Starter), 3 (Pro), 4 (Ent).
- Music intent matches `brief.audio_direction.music_mood`.
- Music swells ≤ tier cap.
- SFX from approved inventory (no novel sounds without operator approval).
- Duck-under-speech default −12dB; never less aggressive than −9dB.

### Step 8 — Platform variants

Build `platform_variants[]`. Constraints:
- Tier cap on count.
- Each variant has its own first-frame text (different optimization for IG vs TikTok vs LI).
- Aspect ratio per platform (9:16 for IG/TT, 1:1 for LI, 9:16 for YT Shorts, 16:9 only on Enterprise YouTube long-form variant).
- Caption burn flag per platform per tier rule.

### Step 9 — Self-QC + emit

Run the 12-check list (§6). Pass-all → emit `script.json` with `human_review_required: true` (Lever 3 default). Any fail → re-attempt up to 2x with adjusted prompt. Still failing → emit error envelope with `attempts` count.

---

## §6. Self-QC Checklist (12 hard checks before emit)

1. All required schema fields present.
2. `brief_id` in output matches `brief.brief_id` from input — no orphan scripts.
3. Hook line copied VERBATIM from `brief.hook.first_3_seconds`.
4. No HC / Principal / NPOX / 4821 / 6315 / SLN / Retail Supply references anywhere (entity firewall — verbatim absence check across every spoken line, on_screen_text, and broll description).
5. `do_not_say` list — verbatim absence check across every spoken line and on_screen_text. Conjugates checked too (e.g., "hustle" → also block "hustling", "hustled").
6. Sum of line durations ≤ `duration_target_seconds × 1.05`.
7. Last line ends ≤ `duration_target_seconds + 1`.
8. CTA appears in final 6 seconds.
9. Caption `max_chars_per_line` ≤ 22 across every on-screen text block.
10. `no_buildings_rule` acknowledged on every b-roll cue.
11. Platform variants count ≤ tier cap.
12. Mode (A/B/C) matches tier authorization (defense-in-depth — Brief should have caught it).

---

## §7. Failure Modes (Quick-reference — Full List)

| # | Failure | Detection | Mitigation |
|---|---------|-----------|------------|
| 1 | Non-JSON output | Parse fails | Regenerate with explicit "JSON ONLY" reminder |
| 2 | HC / Principal / NPOX reference | Verbatim scan | Hard reject + log; do not pass downstream |
| 3 | Banned hustle vocabulary in spoken line | do_not_say scan | Output check; regenerate that line up to 2x |
| 4 | Hook rewritten (not verbatim from brief) | String compare | Force-replace; flag qc_warning |
| 5 | Line duration overflow | Time-math sum | Compress longest line; if can't, drop one line |
| 6 | Aspirational building in b-roll | no_buildings_rule scan | Replace with interior or black-card |
| 7 | CTA outside final 6s | second_start check | Move CTA; absorb time from filler line |
| 8 | Caption line > 22 chars | char count | Break the line; if mid-word, abbreviate |
| 9 | Platform variant count > tier cap | array length | Drop extras (LI is highest-priority for REINVENTED) |
| 10 | Mode B/C unauthorized for tier | tier table | tier_constraint_violation error |
| 11 | Words-per-minute > talent cap | word count / duration | Compress lines; reduce filler |
| 12 | Brief was errorEnvelope | shape check | brief_not_success error |

---

## §8. System Prompt (v1.0 — LOCKED draft for Wed implementation)

```
You are the Script Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: convert a structured creative brief into a fully-speakable, beat-aligned script with on-screen text, b-roll cues, voiceover cadence marks, and platform-specific variants — ready for the Storyboard Agent to translate into a shot plan.

## Hard rules (NEVER violate)

1. Output format = JSON only. No markdown, no commentary, no explanation. Single JSON object conforming to script.json schema.
2. Entity firewall. NEVER reference Holdco Group, 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A in ANY field — spoken line, on-screen text, b-roll description. If brief.brand_id is one of these → REJECT with entity_firewall_breach.
3. Banned vocabulary. Honor the do_not_say list from the brief. Verbatim AND conjugate check on every spoken line, on_screen_text, and b-roll description.
4. Hook integrity. The hook line in lines[0].spoken is COPIED VERBATIM from brief.hook.first_3_seconds. NEVER rewritten, NEVER paraphrased.
5. No buildings rule. Every b-roll cue includes a no_buildings_rule acknowledgment. Interior or black-card framing only — never aspirational external buildings.
6. Duration discipline. Sum of line durations ≤ duration_target_seconds × 1.05. Last line ends ≤ duration_target + 1s. CTA in final 6 seconds.
7. Tier honoring. Lines / b-roll cues / platform variants / voice takes / music swells stay inside the tier cap (see §4 tier table — embedded below).
8. Memory respect. If prior_scripts provided, don't repeat the same opening rhythm more than 3 of last 5. Diversify openers.
9. Self-QC before emit. Run the 12-check list internally. If anything fails, regenerate that line / cue once. If still failing, emit error envelope with attempts count.

## Process (run in order)

1. Validate brief (success variant, all required fields).
2. Load brief context (hook, beats, audience, tier, lever, mode, do_say, do_not_say, visual, audio, cta).
3. Inflate beats into lines (1–3 lines per beat).
4. Compose spoken language (honor do_say register; absence-check do_not_say).
5. Build on-screen text + caption strategy.
6. Build b-roll plan (≤ tier cap; no buildings).
7. Build audio plan (voice takes, music swells, sfx, duck).
8. Build platform variants (per tier cap, each with own first-frame text).
9. Self-QC + emit.

## Tier table (embed)

Pilot:    lines ≤ 8, broll ≤ 3, captions burn-in REQUIRED, voice takes 2, music swells 1, variants 3
Starter:  lines ≤ 8, broll ≤ 3, captions burn-in REQUIRED, voice takes 2, music swells 1, variants 3
Pro:      lines ≤ 12, broll ≤ 6, captions optional, voice takes 3, music swells 2, variants 4
Enterprise: lines ≤ 12, broll unlimited, captions optional, voice takes 4, music swells 3, variants 5

## Voice for the script itself (meta)

Write spoken lines in the brand's voice (read brief.audience.language_register). For REINVENTED that's operator-to-operator: peer, direct, clinical-warm, no fluff. Sentences ≤ 14 words on average. No filler tokens unless style_overrides.ad_lib_allowed = true.

Rationale fields are operator-tone — clinical, brief, why-this-decision-not-the-other.

Output the canonical script.json. Nothing else.
```

---

## §9. Test-Case Plan (5 fixtures, mirroring Brief Agent test pattern)

To be authored alongside the SKILL bundle on Wed Apr 29 (Day 10).

| # | Test name | Tier | Mode | Purpose |
|---|-----------|------|------|---------|
| 1 | reinvented-pilot-burnout-story | Pilot | A | Happy path — story format, 55s, full QC pass |
| 2 | reinvented-starter-listicle-3traps | Starter | A | Listicle format, hook diversification check |
| 3 | brief-was-error-envelope | n/a | n/a | Reject branch — input is errorEnvelope; expect `brief_not_success` |
| 4 | tier-mismatch-mode-c-on-pilot | Pilot | C | Reject branch — expect `tier_constraint_violation` |
| 5 | banned-vocab-injection | Pilot | A | Hostile — operator forces "hustle" via style_overrides; expect rewrite + qc_warning |

Each fixture:
- Lives in `ars/skills/script-agent/test-cases/case-0X-*.json`
- Includes `expected_output_highlights[]` (key fields the validator diff-checks)
- Inputs validated against `schemas/input.schema.json` BEFORE LLM execution

---

## §10. Brief → Script Field-Mapping Reference

This table is the **single source of truth** for how every brief field flows into script. Implementers do not derive this from prose — they implement directly against it.

| brief.json field | script.json destination | Transform |
|------------------|-------------------------|-----------|
| `brief_id` | `brief_id` | passthrough (audit trail) |
| `brand_id` | `brand_id` | passthrough |
| `tier` | `tier` | passthrough (drives §4 caps) |
| `lever` | `lever` | passthrough |
| `production_mode` | `production_mode` | passthrough |
| `title_working` | `title_working` | passthrough |
| `hook.first_3_seconds` | `hook_block.spoken_line` AND `lines[0].spoken` | VERBATIM copy — both fields |
| `hook.alt_hooks[]` | (used internally for platform_variants[*].hook_first_frame derivation) | reformat per platform |
| `hook.delivery` | `lines[0].delivery` | passthrough |
| `hook.tone` | `audio_track.voice_pacing` (partial) | mapping |
| `core_promise` | `rationale.why_this_pacing` (partial) | mapping |
| `audience.language_register` | governs §4 sentence-length default | constraint |
| `structure.beats[]` | `lines[]` | each beat → 1–3 lines (Step 3) |
| `structure.duration_target_seconds` | `duration_target_seconds` | passthrough |
| `structure.duration_min` / `_max` | `duration_min` / `duration_max` | passthrough |
| `messaging_pillars_used[]` | `rationale` (informational) | passthrough |
| `do_say[]` | language constraint during Step 4 | enforced |
| `do_not_say[]` | absence-check during Step 4 + QC | enforced (verbatim + conjugate) |
| `visual_direction.shot_list_hint[]` | `broll_plan[*].description` seeds | translation |
| `visual_direction.no_buildings_rule` | `broll_plan[*].no_buildings_rule` | passthrough |
| `audio_direction.music_mood` | `audio_track.music_intent` | passthrough |
| `audio_direction.captions` | `captions.style` | passthrough |
| `cta.copy` | `cta_block.spoken_line` (may polish for cadence) | minor edit allowed |
| `cta.placement` | `cta_block.second_start/end` | scheduling |
| `platform_targets[]` | `platform_variants[]` | per-platform variant build |
| `qc_pre_flags[]` | `qc_pre_flags[]` | merge with script-side flags |
| `metadata.session_id` | `session_id` | passthrough |

---

## §11. Lever-State Behavior (carried from brief)

Script Agent honors the lever state propagated from the brief — it does NOT override.

- **Lever 1** (Audit-only / fully manual): Script Agent emits but `human_review_required = true` AND `metadata.qc_score_predicted` floor of 0.3 (be conservative). Operator hand-edits before downstream consumption.
- **Lever 2** (Auto-execute with audit): Script Agent emits with `human_review_required = true`, downstream Storyboard waits for human approval before consuming.
- **Lever 3** (Default / production): Script Agent emits with `human_review_required = true` only if `qc_score_predicted < 0.7` OR any `qc_warnings` populated. Otherwise auto-promotes.

Lever overrides don't happen here. If an operator needs a different lever, that is a workflow-orchestrator concern, not a Script Agent concern.

---

## §12. Memory Loop (prior_scripts handling)

When `prior_scripts` is provided:

1. **Opening rhythm dedupe.** Compare `lines[0].pace_marker` and `lines[0].emphasis_words` against last 5. If 3 of 5 already match the proposed opener → diversify (Step 4 regen with explicit "diversify opener" instruction).
2. **Format dedupe.** Track `structure.format` (from brief). Brief Agent enforces this upstream too — defense in depth.
3. **Tagline rotation.** If `cta_block.spoken_line` matches any prior CTA verbatim → flag qc_warning AND propose 1-line variation. (Brand consistency vs. fatigue tradeoff.)
4. **Memory size.** Keep most recent 5 only. Drop older.

---

## §13. Open Questions (Parked — non-blocking through Week 5)

These are intentionally NOT resolved in v1.0. They are listed so future iterations remember the deferred decisions.

1. **Multi-speaker scripts (Mode B).** v1.0 supports single-speaker only. Mode B is documented in tier table but speaker assignment is unimplemented — Pro tier first reel is single-speaker until v1.1.
2. **Prosody markers.** v1.0 emits `delivery_note` strings ("drop tone on…"). v1.1 may emit SSML or formal prosody markers if voice-clone (HeyGen / ElevenLabs) integration justifies it.
3. **Live caption sync.** v1.0 specifies caption style + char limits but not frame-accurate timing — that is Edit Agent's job. Revisit if captions drift in early production runs.
4. **A/B variant generation.** v1.0 emits one canonical script per call. v1.2 may emit 2 variants for A/B testing on platform variants. Held until performance data exists to justify cost.
5. **Talent profile registry.** v1.0 accepts inline `talent_profile`. v1.1 — registry lookup by `speaker_id`.
6. **Off-brand topic refusal.** Currently the brief filters this. Should Script Agent re-validate with a topic-vs-pillar score? Defense in depth vs. cost. Held until Week 5 retro.
7. **Translation / localization.** v1.0 = en-US only. International is Q3 concern.
8. **Long-form mode.** YouTube long-form (>3min) is Enterprise-only and v1.3+. Not in scope.
9. **Voice-take inflation.** v1.0 specifies count, not the actual variant lines. v1.1 emits the second / third take inline so voice-clone executes without re-inferring.

---

## §14. Implementation Plan (Wed Apr 29 — Day 10 overnight build)

Mirror the Brief Agent skill bundle pattern exactly:

```
ars/skills/script-agent/
├── SKILL.md                          (system prompt + process + tier table + QC list)
├── README.md                         (operator invocation guide)
├── prompts/
│   └── user-template.txt             (canonical user message wrapper)
├── schemas/
│   ├── input.schema.json             (validates Script Agent input shape)
│   └── output.schema.json            (validates script.json — success + error envelope)
└── test-cases/
    ├── case-01-reinvented-pilot-burnout-story.json
    ├── case-02-reinvented-starter-listicle-3traps.json
    ├── case-03-brief-was-error-envelope.json
    ├── case-04-tier-mismatch-mode-c-on-pilot.json
    └── case-05-banned-vocab-injection.json
```

**Execution order on Day 10:**
1. Build `schemas/input.schema.json` (Draft 2020-12).
2. Build `schemas/output.schema.json` (success + errorEnvelope).
3. Validate both schemas as Draft 2020-12.
4. Author `SKILL.md` (system prompt + 9-step process + tier table + 12-check QC).
5. Author `prompts/user-template.txt`.
6. Author 5 test fixtures.
7. Validate all 5 input fixtures against `input.schema.json` — must pass 5/5.
8. Author `README.md`.
9. Mirror to `/outputs/ars/skills/script-agent/`.
10. Update dashboard.

**Day 11 (Thu Apr 30):** Run 5 test cases through Opus 4.6 → validate outputs against `output.schema.json` → if 5/5 pass, lock v1.0. Storyboard Agent SPEC kicks off Day 12 (Fri).

---

## §15. Critical Decisions Locked in This Spec

These are the choices that future iterations should NOT re-litigate without an explicit retro:

1. **Hook line is verbatim copy from brief.** Not paraphrase. Script Agent does not "improve" the hook — that is Brief Agent's territory.
2. **Default words-per-minute = 165.** Operator-to-operator pacing. Slower reads as guru.
3. **Default sentence length = 14 words.** Caption-line-friendly.
4. **Pilot/Starter caption burn-in = MANDATORY.** Cheaper rendering pipeline + accessibility.
5. **B-roll never overlaps CTA.** Final 4–6s = face + CTA text only — preserves intent.
6. **Single-speaker only in v1.0.** Multi-speaker (Mode B) deferred to v1.1.
7. **3 platform variants minimum (IG, TikTok, LinkedIn).** REINVENTED's distribution canon.
8. **Lever 3 default human review at qc_score < 0.7.** Otherwise auto-promote — Jamila's hands stay off most of the loop.
9. **Schema is Draft 2020-12.** Same as Brief Agent — single schema canon across the agent fleet.
10. **Language is en-US only in v1.0.**
11. **Defense in depth on entity firewall.** Brief Agent enforces it upstream; Script Agent re-validates. Three agents will eventually validate this — that is intended.
12. **`brief_id` in script.json.** Audit trail mandatory — every script traces back to a brief.

---

## §16. Hand-off to Storyboard Agent (preview — out of scope this spec)

The Script Agent's `script.json` becomes the input to the Storyboard Agent (Spec target: Day 12 Fri Apr 30 / Sat May 1). Preview of Storyboard Agent's expected reads:

- `lines[]` → frame-by-frame shot plan
- `broll_plan[]` → asset acquisition list
- `on_screen_text_blocks[]` → motion graphic spec
- `platform_variants[]` → render output matrix
- `pace_marker` per line → cut rhythm

Storyboard Agent SPEC will be authored on Day 12 (Friday overnight build). It will reference this spec as its canonical input contract.

---

## §17. Sign-off & Status

| Item | Status |
|------|--------|
| §1 Purpose & Pipeline Position | LOCKED |
| §2 Inputs | LOCKED |
| §3 Outputs | LOCKED |
| §4 Tier Constraints | LOCKED |
| §5 9-step Process | LOCKED |
| §6 Self-QC Checklist (12 checks) | LOCKED |
| §7 Failure Modes | LOCKED |
| §8 System Prompt v1.0 | LOCKED |
| §9 Test-Case Plan | DRAFT — fixtures authored Day 10 |
| §10 Brief → Script Field Map | LOCKED |
| §11 Lever Behavior | LOCKED |
| §12 Memory Loop | LOCKED |
| §13 Open Questions | PARKED (non-blocking) |
| §14 Implementation Plan | LOCKED for Day 10 |
| §15 Critical Decisions | LOCKED |
| §16 Storyboard Hand-off Preview | INFORMATIONAL |
| §17 Sign-off | DONE |

**Implementation greenlight:** Wednesday Apr 29 (Day 10) overnight build executes against this spec. Implementation is fill-in-the-blanks — every decision is pre-made.

---

*Spec authored: Tuesday Apr 28, 2026 (Day 9 · Week 2 Day 2 overnight build session, ~70 min)*
*Owner: Jamila Howard — Sequel Digital — ARS productized build*
*Predecessor: ARS-2026-04-26-Brief-Agent-v1-Spec.md*
*Successor: ARS-2026-05-01-Storyboard-Agent-v1-Spec.md (target)*
*Entity scope: Sequel Digital. Zero HC / Principal / NPOX references.*
