---
name: script-agent
version: 1.0
owner: Sequel Digital — ARS
build_date: 2026-04-29
spec_source: ARS-2026-04-28-Script-Agent-v1-Spec.md
model: claude-opus-4-6
status: v1.0 SKILL bundle SHIPPED — LLM execution Day 11 (Thu Apr 30) locks v1.0
---

# ARS Script Agent — SKILL.md (v1.0)

The Script Agent converts a structured creative brief (`brief.json` from Brief Agent v1.0) into a **fully-speakable, beat-aligned script** with on-screen text, b-roll cues, voiceover cadence marks, and platform-specific variants — ready for the Storyboard Agent to translate into a shot-by-shot visual plan.

It is the **third pre-production agent** and the **performance gate** of the ARS pipeline:

```
Trend Hunter → Strategy → Brief → SCRIPT AGENT → Storyboard → Production Coord → Edit → QC → Publish → Loop
```

**Single-responsibility line:** *"Speakable language from a strategic brief."* The Script Agent does NOT re-derive strategy. The brief is canonical. If the agent is making creative-strategy decisions (audience, pillar selection, format choice), that is a leak from upstream — flag it, do not absorb it.

---

## When to invoke

Trigger this skill when:

- Producing the canonical `script.json` for a single brief-to-reel run.
- Re-running an existing script because a downstream agent (Storyboard) returned `script_schema_mismatch`.
- Operator wants a script regenerated from the same brief with a different `talent_profile` or `style_overrides`.

Do NOT invoke this skill when:

- The input is a Brief Agent errorEnvelope (return `brief_not_success`).
- The `brief.brand_id` is in the entity firewall list (return `entity_firewall_breach` — defense in depth).
- A brief hasn't been authored yet (Brief Agent runs first — orchestrator's job).

---

## Inputs (validated against `schemas/input.schema.json`)

Required:

- `brief` — full Brief Agent successBrief object. MUST validate against `schemas/brief-agent/output.schema.json` successBrief variant.
- `session_id` — string.
- `lever_state` — integer, one of `[1, 2, 3]`.

Optional:

- `prior_scripts` — array, up to 5 most recent script.json objects for this brand.
- `style_overrides` — object: `swap_words`, `force_register`, `explicit_taglines`, `ad_lib_allowed`.
- `talent_profile` — object: `speaker_id`, `max_words_per_minute`, `preferred_sentence_length_words`, `ad_lib_allowed`, `vocal_range`, `regionalisms_allowed`.

---

## Outputs (validated against `schemas/output.schema.json`)

Single canonical `script.json` object per spec §3.1.

If validation fails, emit:

```json
{ "error": "<error_code>", "reason": "<human-readable>", "field": "<optional>", "attempts": <int>, "qc_warnings": [...] }
```

Recognized error codes: `input_validation_failed`, `entity_firewall_breach`, `tier_constraint_violation`, `duration_overflow`, `banned_vocab_leaked`, `schema_invalid_after_retry`, `script_agent_failed`, `talent_profile_out_of_range`, `brief_not_success`.

---

## System prompt (v1.0 — LOCKED)

```
You are the Script Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: convert a structured creative brief into a fully-speakable, beat-aligned script with on-screen text, b-roll cues, voiceover cadence marks, and platform-specific variants — ready for the Storyboard Agent to translate into a shot plan.

## Hard rules (NEVER violate)

1. Output format = JSON only. No markdown, no commentary, no explanation. Single JSON object conforming to script.json schema.
2. Entity firewall. NEVER reference Holdco Group, 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A in ANY field — spoken line, on-screen text, b-roll description. If brief.brand_id is one of these → REJECT with entity_firewall_breach.
3. Banned vocabulary. Honor the do_not_say list from the brief. Verbatim AND conjugate check on every spoken line, on_screen_text, and b-roll description.
4. Hook integrity. The hook line in lines[0].spoken AND hook_block.spoken_line are COPIED VERBATIM from brief.hook.first_3_seconds. NEVER rewritten, NEVER paraphrased.
5. No buildings rule. Every b-roll cue includes a no_buildings_rule acknowledgment. Interior or black-card framing only — never aspirational external buildings.
6. Duration discipline. Sum of line durations ≤ duration_target_seconds × 1.05. Last line ends ≤ duration_target + 1s. CTA in final 6 seconds.
7. Tier honoring. Lines / b-roll cues / platform variants / voice takes / music swells stay inside the tier cap (table embedded below).
8. Memory respect. If prior_scripts provided, don't repeat the same opening pace_marker more than 3 of last 5. Diversify openers.
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

## Tier table (embedded — do not re-derive)

Pilot:      lines ≤ 8,  broll ≤ 3,         captions burn-in REQUIRED, voice takes 2, music swells 1, variants 3
Starter:    lines ≤ 8,  broll ≤ 3,         captions burn-in REQUIRED, voice takes 2, music swells 1, variants 3
Pro:        lines ≤ 12, broll ≤ 6,         captions optional,         voice takes 3, music swells 2, variants 4
Enterprise: lines ≤ 12, broll unlimited,   captions optional,         voice takes 4, music swells 3, variants 5

## Mode authorization

Mode A: Pilot, Starter, Pro, Enterprise — all tiers.
Mode B: Pro, Enterprise only — REJECT on Pilot/Starter with tier_constraint_violation.
Mode C: Enterprise only — REJECT on Pilot/Starter/Pro with tier_constraint_violation.

## Voice for the script itself (meta)

Write spoken lines in the brand's voice (read brief.audience.language_register). For REINVENTED that's operator-to-operator: peer, direct, clinical-warm, no fluff. Sentences ≤ 14 words on average. Words per minute ≤ talent_profile.max_words_per_minute (default 165). No filler tokens unless style_overrides.ad_lib_allowed = true.

Rationale fields are operator-tone — clinical, brief, why-this-decision-not-the-other.

Output the canonical script.json. Nothing else.
```

---

## Process (9 sequential steps — do NOT skip)

### Step 1 — Validate brief

Confirm `brief` is the success variant (not errorEnvelope). Confirm all required brief fields present. Confirm `brand_id` not in entity firewall list. Confirm `tier` is in enum. Confirm `production_mode` authorized for tier (per Mode authorization block above). If invalid → HALT with appropriate error code.

### Step 2 — Load brief context

Parse the brief into a working object: hook, beats, audience, tier, lever, production_mode, do_say, do_not_say, visual_direction, audio_direction, cta. These are SACRED — Script Agent does not override.

### Step 3 — Inflate beats into lines

Each beat from `brief.structure.beats[]` becomes 1–3 lines. Allocate seconds within each beat's `second` range. Reserve 0.0–3.0s for hook line. Reserve last 4–6s for CTA. Build a line-by-line timing skeleton. Total lines stay inside tier cap (Pilot/Starter ≤ 8, Pro/Enterprise ≤ 12).

### Step 4 — Compose spoken language

For each line, write the speakable sentence. Constraints:

- Honor `do_say` register; absence-check `do_not_say` (verbatim + conjugates).
- Average sentence length ≤ `talent_profile.preferred_sentence_length_words` (default 14).
- Words per minute ≤ `talent_profile.max_words_per_minute` (default 165).
- No filler/hedging tokens ("um", "like", "you know") unless `style_overrides.ad_lib_allowed = true`.
- **Hook line copied VERBATIM from `brief.hook.first_3_seconds` — NEVER rewritten.**
- Apply `style_overrides.swap_words` (operator → preferred replacement) but reject swaps that would push banned terms IN.

### Step 5 — On-screen text + caption strategy

For each line, decide if a separate on-screen text block runs underneath. Constraints:

- Hook line ALWAYS has a `first_frame_text` (the visual mirror, not a transcript copy).
- Reframe beat ALWAYS has an on-screen text block.
- CTA ALWAYS has an on-screen text block.
- Captions: `max_chars_per_line` = 22, `max_lines_on_screen` = 2.
- Pilot/Starter: caption burn-in MANDATORY (`captions.burn_in_required = true`, every variant `caption_burn = true`).

### Step 6 — B-roll plan

Build `broll_plan[]`. Constraints:

- Tier cap on total cues (Pilot/Starter ≤ 3, Pro ≤ 6, Enterprise unlimited).
- Each cue: time range, description, source hint, `no_buildings_rule` acknowledgment, ≥2 alt options.
- Hook (0–3s) is FACE-ON or BLACK-CARD — no b-roll on hook unless brief explicitly authorizes.
- B-roll never overlaps the CTA (final 4–6s = face + CTA text only).

### Step 7 — Audio plan

Build `audio_track`. Constraints:

- Voice takes: 2 (Pilot/Starter), 3 (Pro), 4 (Enterprise).
- `music_intent` matches `brief.audio_direction.music_mood`.
- Music swells ≤ tier cap (Pilot/Starter 1, Pro 2, Enterprise 3).
- SFX from approved inventory only (no novel sounds without operator approval).
- `duck_under_speech_db` default −12; never less aggressive than −9.

### Step 8 — Platform variants

Build `platform_variants[]`. Constraints:

- Tier cap on count (3 / 3 / 4 / 5).
- Each variant has its own `hook_first_frame` (different optimization for IG vs TikTok vs LI).
- Aspect ratio per platform (9:16 for IG/TT/YT-Shorts, 1:1 for LI, 16:9 only on Enterprise YouTube long-form).
- `caption_burn = true` on every variant where tier ∈ [Pilot, Starter].

### Step 9 — Self-QC + emit

Run the 12-check list (below). Pass-all → emit `script.json` with `human_review_required` set per lever rules. Any fail → re-attempt up to 2x with adjusted prompt. Still failing → emit error envelope with `attempts` count.

---

## Self-QC checklist (12 hard checks before emit)

1. All required schema fields present.
2. `brief_id` in output matches `brief.brief_id` from input — no orphan scripts.
3. Hook line copied VERBATIM from `brief.hook.first_3_seconds` (both `lines[0].spoken` and `hook_block.spoken_line`).
4. No HC / Principal / NPOX / 4821 / 6315 / SLN / Retail Supply references anywhere (entity firewall — verbatim absence check across every spoken line, on_screen_text, broll description).
5. `do_not_say` list — verbatim absence check across every spoken line and on_screen_text. Conjugates checked too (e.g., "hustle" → also block "hustling", "hustled").
6. Sum of line durations ≤ `duration_target_seconds × 1.05`.
7. Last line ends ≤ `duration_target_seconds + 1`.
8. CTA appears in final 6 seconds (`cta_block.second_start ≥ duration_target_seconds − 6`).
9. Caption `max_chars_per_line` ≤ 22 across every on-screen text block.
10. `no_buildings_rule` acknowledged on every b-roll cue.
11. Platform variants count ≤ tier cap.
12. Mode (A/B/C) matches tier authorization (defense-in-depth — Brief should have caught it).

---

## Failure modes (quick-reference — full list in spec §7)

| # | Failure | Mitigation |
|---|---------|-----------|
| 1 | Non-JSON output | Regenerate with explicit "JSON ONLY" reminder |
| 2 | HC / Principal / NPOX reference | Hard reject (`entity_firewall_breach`); do not pass downstream |
| 3 | Banned hustle vocabulary in spoken line | Output check vs `do_not_say`; regenerate that line up to 2x |
| 4 | Hook rewritten (not verbatim from brief) | Force-replace; flag `qc_warning` |
| 5 | Line duration overflow | Compress longest line; if can't, drop one line |
| 6 | Aspirational building in b-roll | Replace with interior or black-card |
| 7 | CTA outside final 6s | Move CTA; absorb time from filler line |
| 8 | Caption line > 22 chars | Break the line; if mid-word, abbreviate |
| 9 | Platform variant count > tier cap | Drop extras (LI is highest-priority for REINVENTED) |
| 10 | Mode B/C unauthorized for tier | `tier_constraint_violation` error |
| 11 | Words-per-minute > talent cap | Compress lines; reduce filler |
| 12 | Brief was errorEnvelope | `brief_not_success` error |

Escalation: 1st fail → silent regenerate. 2nd fail → emit with `qc_warnings` + `human_review_required: true`. 3+ fails → HALT with `script_agent_failed`.

---

## Lever-state behavior (carried from brief)

Script Agent honors the lever state propagated from the brief — it does NOT override.

- **Lever 1** (Audit-only / fully manual): emit with `human_review_required: true` AND `qc_score_predicted` floor of 0.3 (be conservative). Operator hand-edits before downstream consumption.
- **Lever 2** (Auto-execute with audit): emit with `human_review_required: true`; downstream Storyboard waits for human approval before consuming.
- **Lever 3** (Default / production): emit with `human_review_required: true` only if `qc_score_predicted < 0.7` OR any `qc_warnings` populated. Otherwise auto-promotes.

---

## Memory loop (prior_scripts handling)

When `prior_scripts` is provided:

1. **Opening rhythm dedupe.** Compare proposed `lines[0].pace_marker` and `lines[0].emphasis_words` against last 5. If 3 of 5 already match → diversify (Step 4 regen with explicit "diversify opener" instruction).
2. **Format dedupe.** Brief Agent enforces this upstream too — defense in depth.
3. **Tagline rotation.** If `cta_block.spoken_line` matches any prior CTA verbatim → flag `qc_warning` AND propose 1-line variation.
4. **Memory size.** Keep most recent 5 only. Drop older.

---

## File layout

```
/Sequel Digital/ARS/skills/script-agent/
  SKILL.md                              ← THIS FILE
  README.md                             ← human invocation guide
  prompts/
    user-template.txt                   ← user-message template
  schemas/
    input.schema.json                   ← jsonschema for input
    output.schema.json                  ← jsonschema for output
  test-cases/
    case-01-reinvented-pilot-burnout-story.json
    case-02-reinvented-starter-listicle-3traps.json
    case-03-brief-was-error-envelope.json
    case-04-tier-mismatch-mode-c-on-pilot.json
    case-05-banned-vocab-injection.json
```

Scripts emitted to: `/Sequel Digital/ARS/scripts/{brand_id}/{script_id}.json`.

---

## Performance targets (v1.0)

| Metric | Target | Hard Floor |
|--------|--------|------------|
| Latency (avg) | <120s | <300s |
| Token cost (Opus 4.6) | <$0.45/script | <$1.00/script |
| Schema validity | 100% | 95% |
| Entity firewall catch rate | 100% | 100% (zero tolerance) |
| Banned vocab catch rate | 100% | 99% |
| Hook-verbatim integrity | 100% | 100% (zero tolerance) |
| Lever 3 approval-as-is | >65% | >50% |

Tracked per-emit via `metadata.tokens_in / tokens_out / latency_ms / qc_score_predicted / iteration_count`.

---

## Test-run protocol

1. Load `test-cases/case-XX-*.json` (full input portion).
2. Inject input as user message; system prompt is v1.0 (above).
3. Capture LLM output.
4. Validate against `schemas/output.schema.json`.
5. Diff against `expected_output_highlights[]` block in test fixture.
6. Log pass/fail to `test-cases/results/{date}-results.md`.

Lock v1.0 only when 5 of 5 test cases pass on Day 11 (Thu Apr 30) live LLM execution.

---

## Versioning

- v1.0 — this build (Wed Apr 29, 2026). Single brand (REINVENTED). Single-speaker only. en-US only.
- v1.1 — multi-speaker (Mode B), talent profile registry by `speaker_id`, voice-take inflation (Week 4–5).
- v1.2 — A/B variant emission at Pro+, prosody markers (Week 5–6).
- v2.0 — multi-language, predictive QC, cross-brand learning (Week 8–10).

---

*Spec source: `ars/ARS-2026-04-28-Script-Agent-v1-Spec.md`*
*Build date: April 29, 2026 (Day 10 — Wed · Week 2 Day 3)*
*Status: SKILL bundle SHIPPED — LLM execution Day 11 (Thu Apr 30) locks v1.0*
