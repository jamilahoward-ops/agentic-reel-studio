# ARS Storyboard Agent v1.0 — SPEC
**Pipeline position:** Trend Hunter → Strategy → Brief → Script → **STORYBOARD** → Production Coord → AI Video Gen / Style Replication / Live shoot → Edit → QC → Publish → Loop

**Authored:** 2026-04-30 (Thu · Day 11 · Wk2D5 — pulled forward from Day 12)
**Source documents:** Brief Agent v1.0 SPEC + SKILL bundle (Apr 26–27), Script Agent v1.0 SPEC + SKILL bundle (Apr 28–29).
**Same shape as:** Brief Agent SPEC, Script Agent SPEC. Easier review.
**Status:** v1.0 SPEC — DRAFT → LOCKED on §§1–8, 10–17 in this session. §9 test fixtures author Day 13 alongside SKILL bundle.

---

## §1 Purpose & pipeline position

The Storyboard Agent converts a beat-aligned **`script.json`** into a **shot-by-shot, frame-aligned `storyboard.json`** that a videographer (Mode A), an AI video generator (Mode B), or a style-replication engine (Mode C) can execute against deterministically.

Single-responsibility line: *"Visual realization of a speakable script."*

The Storyboard Agent is the **production gate** of the pipeline:
- The **Brief Agent** is the strategy gate. (Is this the right reel?)
- The **Script Agent** is the performance gate. (Is the language going to land?)
- The **Storyboard Agent** is the production gate. (Can we actually shoot/render this in budget, in tier, on-brand?)

If the Storyboard Agent emits a successStoryboard, downstream production is unblocked. If it emits an errorEnvelope, no shoot/render is initiated.

---

## §2 Inputs

**Required:**
- `script` — full Script Agent successScript object. MUST validate against `schemas/script-agent/output.schema.json` successScript variant. (PolymorphismFactor: same as Script Agent — accept both successScript and errorEnvelope at the schema layer; halt with `script_not_success` if errorEnvelope.)
- `brief` — pass-through reference for tier+brand+do_not_say (denormalized for self-containment; do not re-derive from script).
- `session_id` — string, ≥4 chars.
- `lever_state` — integer ∈ [1, 2, 3].

**Optional:**
- `prior_storyboards` — array, up to 5 most recent storyboard.json objects for this brand. Used for shot-language dedupe and visual rotation.
- `production_constraints` — object: `available_locations` (array), `available_talent` (array), `equipment_tier` (S/M/L), `budget_minutes` (integer), `weather_window` (date range).
- `mode_b_engine_profile` — object only when production_mode == "B": `model_id` (`runway-gen-3`/`pika-1.5`/`luma-dream-machine`/`flux-pro-1.1`/`kling-1.6`/`higgsfield-genie-v1`), `max_clip_duration_s`, `aspect_ratios_supported`, `style_token_lib`.
- `mode_c_reference_url` — string, URL only when production_mode == "C". Storyboard re-derives shot language from the source URL (style replication).

Validated by `schemas/input.schema.json` (Draft 2020-12). Per spec §2.3 in matching pattern from Script Agent.

---

## §3 Outputs

Single canonical `storyboard.json` object per shot-level contract. `oneOf` polymorphism: successStoryboard OR errorEnvelope.

### 3.1 successStoryboard schema (high-level)

```
storyboard.json
├── storyboard_id              string  pattern: ^sb-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$
├── script_id                  string  pattern: ^script-...
├── brief_id                   string  pattern: ^brief-...
├── brand_id                   string
├── tier                       enum: Pilot|Starter|Pro|Enterprise
├── lever                      int 1..3
├── production_mode            enum: A|B|C
├── created_at                 ISO datetime
├── session_id                 string
├── duration_target_seconds    int 15..180
├── total_shots                int (computed = shots.length)
├── locked_aspect_ratios       array of "9:16"|"1:1"|"16:9"|"4:5"  (≥1, ≤4)
├── shots                      array  minItems: 6  maxItems: 24
│   └── shot_object (see §3.2)
├── transitions                array (between shots, length = shots.length - 1)
├── color_grade                object
├── motion_design              object  // lower-thirds, kinetic text, counters
├── overlay_assets             array   // logos, watermarks, brand marks
├── audio_sync_map             object  // ties shots to script.audio_track timing
├── platform_render_specs      array (one per platform target)
├── shoot_logistics            object  // Mode A only
├── ai_render_plan             object  // Mode B only
├── replication_recipe         object  // Mode C only
├── budget_estimate            object  // shoot minutes / render seconds / asset count
├── rationale                  object  // why this shot count, why these transitions, why this grade
├── qc_pre_flags               array (≥4)
├── qc_warnings                array
├── downstream_dependencies    object  // production_coord_agent, edit_agent, qc_agent
└── metadata                   object  // agent_version, model_used, prompt_template_id, tokens, latency, qc_score, human_review_required, iteration_count
```

### 3.2 shot_object (per shot)

```
shot_object
├── shot_id                    pattern: ^S\d+$
├── line_id_ref                pattern: ^L\d+$       // references script.lines[i].line_id (1:N possible)
├── second_start               number ≥ 0
├── second_end                 number ≥ 0
├── duration_seconds           number 0.4..15
├── shot_type                  enum: ECU|CU|MCU|MS|MLS|LS|XLS|insert|cutaway|aerial|POV|OTS|two-shot
├── camera_movement            enum: static|pan|tilt|dolly-in|dolly-out|truck|crane|handheld|gimbal-orbit|whip-pan|push-in|pull-back
├── focal_length_mm            int  enum: [16, 24, 35, 50, 85, 135] OR null (Mode B/C nullable)
├── lens_aperture              string OR null  // f/1.4..f/16
├── framing_anchor             enum: rule-of-thirds-left|rule-of-thirds-right|centered|negative-space-left|negative-space-right|symmetric
├── subject                    object {who, wardrobe, expression, posture}
├── setting                    object {location_type, palette_hex[], lighting_intent, no_buildings_rule}
├── action                     string  ≥6 chars      // what happens IN the shot
├── on_screen_text_ref         string OR null        // points to script.on_screen_text_blocks[i] by second_start match
├── caption_burn_ref           bool                  // mirrors script.captions.burn_in_required
├── motion_overlay_ref         string OR null        // points to motion_design entry id
├── audio_pillar               enum: voice-only|music-bed|sfx-accent|silence|hybrid
├── duck_under_speech_db_inherit bool               // copy script.audio_track.duck_under_speech_db
├── ai_render_hints            object OR null        // Mode B only — model, seed, style_token, prompt_seed
├── style_replication_hint     object OR null        // Mode C only — source_url offset_s, style_match_target
├── shot_complexity            enum: simple|moderate|complex|hero
├── budget_minutes_est         number ≥ 0            // shoot minutes for Mode A; render seconds for B
├── alt_options                int 0..4              // # of alternate framings to capture
└── qc_per_shot                object {ban_drift_check, no_buildings_check, tier_complexity_check}
```

### 3.3 errorEnvelope (when validation fails)

```json
{
  "error": "<code>",
  "reason": "<≥4 chars>",
  "field": "<optional path>",
  "attempts": <int 1..5>,
  "qc_warnings": ["..."]
}
```

Error codes (9): `input_validation_failed`, `entity_firewall_breach`, `tier_constraint_violation`, `mode_engine_mismatch`, `budget_overflow`, `shot_complexity_mismatch`, `schema_invalid_after_retry`, `script_not_success`, `storyboard_agent_failed`.

---

## §4 Tier constraints (embedded in system prompt at runtime)

| Tier | Shots/reel | Shot complexity allowed | Locations max | Talent count | Aspects | Mode B render seconds cap | Mode C reference URLs |
|------|-----------:|------------------------|--------------:|-------------:|---------|---------------------------:|----------------------:|
| Pilot | 6–8 | simple, moderate | 1 | 1 | 9:16, 1:1, 16:9 (3 max) | n/a | n/a |
| Starter | 6–8 | simple, moderate | 1 | 1 | same | n/a | n/a |
| Pro | 8–14 | simple, moderate, complex | 2 | 2 | 9:16, 1:1, 16:9, 4:5 (4 max) | 60s/reel | n/a |
| Enterprise | 10–24 | all (hero allowed) | 3 | 3 | all | 90s/reel | 1 |

Mode mapping enforcement (defense-in-depth, also enforced at Brief and Script):
- Pilot/Starter: Mode A only
- Pro: Mode A + B
- Enterprise: Mode A + B + C

Same-tier-table copy lives in §8 system prompt for runtime self-containment.

---

## §5 9-Step Process (mirrors Script Agent shape)

**Step 1 — Validate input shape.**
Parse against `input.schema.json`. If fail → emit `input_validation_failed` errorEnvelope, halt.
If `script` is errorEnvelope variant → emit `script_not_success` errorEnvelope, halt.

**Step 2 — Defense-in-depth firewall + tier+mode revalidation.**
Re-check script.brand_id against entity firewall list. Re-check tier↔mode mapping. If mismatched → `entity_firewall_breach` or `tier_constraint_violation` errorEnvelope, halt.

**Step 3 — Load context.**
- script.lines (for shot:line mapping)
- script.broll_plan (for cutaway/insert seeds)
- script.platform_variants (for aspect lock)
- script.audio_track (for audio_pillar / duck inheritance)
- script.captions (for caption_burn_ref)
- script.on_screen_text_blocks (for on_screen_text_ref)
- brief.do_not_say (firewall check on shot.action descriptions)
- brief.visual_direction.no_buildings_rule (REQUIRED in every shot.setting)
- prior_storyboards (rotation/dedupe seed)

**Step 4 — Allocate shots.**
For each script line (5..12), allocate 1..N shots. Total shots must satisfy tier cap (§4). Default allocation: 1.0–1.4 shots per line for monologue/story formats; 1.5–2.2 for listicle (counter beats).

**Step 5 — Compose shot language.**
For each shot, populate: shot_type, camera_movement, focal_length_mm, framing_anchor, subject, setting, action, shot_complexity. Respect prior_storyboards rotation (don't repeat same opening shot_type 3x in a row).

**Step 6 — Apply on-screen + motion overlays.**
Cross-link shots with script.on_screen_text_blocks by `second_start` match. Wire motion_design IDs (lower-thirds, counters, kinetic text). Resolve overlay_assets (brand mark slot, logo lockup).

**Step 7 — Compose transitions + color grade.**
Choose transition type per shot pair (cut/dissolve/whip/match-cut). Respect tier complexity (Pilot/Starter = cut + dissolve only; Pro adds whip + match; Enterprise unlocks all). Apply brand-locked color grade (REINVENTED palette: `#1A1033 / #F8F4FF / #A044FF / #FFD700`).

**Step 8 — Mode-specific plan.**
- Mode A → populate `shoot_logistics` (locations, call sheet, equipment list, weather window).
- Mode B → populate `ai_render_plan` (model assignments per shot, seed seeds, render budget, aspect render passes).
- Mode C → populate `replication_recipe` (source URL offset map, style match targets, gap-filler shots).

**Step 9 — Self-QC + emit.**
Run the 12-check QC list (§6). If pass → emit successStoryboard. If fail → regenerate affected shot(s) up to 2 retries; if still failing → emit errorEnvelope.

---

## §6 12-Check Self-QC List (defense-in-depth firewall)

1. **Entity firewall (re-check).** Zero references to `Holdco|Principal|NPOX|4821|6315|SLN|Retail Supply|Nonprofit Leader A` in any `shot.action`, `shot.subject.who`, `shot.setting.location_type`, or motion_design text. Conjugates included.
2. **Banned vocab (inherit from brief.do_not_say).** Same firewall as Script Agent — verbatim AND conjugate absence-check across all `shot.action`, `motion_design.*.text`, `overlay_assets.*.text`.
3. **No-buildings rule (per-shot).** Every `shot.setting.no_buildings_rule` populated, ≥6 chars, declares interior/black-card/closed-set framing only. NO AI-generated fake buildings. NO stock buildings. Per CLAUDE.md HC Visual Brand Rule (4/22/26) — applies to ALL ARS output, not just HC.
4. **Tier shot count.** `shots.length` inside [tier_min, tier_max] from §4 table.
5. **Tier shot complexity.** Every `shot.shot_complexity` permitted by tier (Pilot/Starter forbid `complex`; only Enterprise allows `hero`).
6. **Aspect cap.** `locked_aspect_ratios.length` ≤ tier-cap.
7. **Mode authorization.** `production_mode` permitted by tier.
8. **Mode B engine match.** If mode==B, `mode_b_engine_profile.model_id` non-null AND ai_render_plan populated AND total render seconds ≤ tier cap.
9. **Mode C reference present.** If mode==C, `mode_c_reference_url` non-null AND replication_recipe populated.
10. **Shot:line coverage.** Every `script.lines[].line_id` referenced by ≥1 shot via `line_id_ref`. No orphaned lines.
11. **Duration math.** `sum(shot.duration_seconds)` ∈ [duration_target × 0.95, duration_target × 1.05]. Each shot duration ∈ [0.4, 15].
12. **Caption burn parity.** `shot.caption_burn_ref` matches `script.captions.burn_in_required` for ALL shots (no per-shot drift unless tier==Enterprise + explicitly authorized).

If any check fails after 2 regen attempts → emit errorEnvelope with the specific error code from §3.3.

---

## §7 Failure modes table (12)

| # | Failure mode | Detection point | Error code |
|---|--------------|-----------------|------------|
| 1 | Input schema invalid | Step 1 | input_validation_failed |
| 2 | Script was errorEnvelope | Step 1 | script_not_success |
| 3 | Entity firewall breach (re-check) | Step 2 + QC #1 | entity_firewall_breach |
| 4 | Tier↔mode mismatch | Step 2 + QC #7 | tier_constraint_violation |
| 5 | Shot count outside tier cap | QC #4 | tier_constraint_violation |
| 6 | Hero shot on non-Enterprise tier | QC #5 | shot_complexity_mismatch |
| 7 | Aspect cap exceeded | QC #6 | tier_constraint_violation |
| 8 | Mode B engine missing/wrong | QC #8 | mode_engine_mismatch |
| 9 | Mode C ref URL missing | QC #9 | mode_engine_mismatch |
| 10 | Orphaned script line (uncovered) | QC #10 | storyboard_agent_failed |
| 11 | Duration overflow | QC #11 | budget_overflow |
| 12 | Schema invalid after 2 retries | Step 9 retry exhaust | schema_invalid_after_retry |

---

## §8 System prompt v1.0 (LOCKED)

```
You are the Storyboard Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: convert a beat-aligned script.json into a shot-by-shot, frame-aligned storyboard.json — production-ready for shoot (Mode A), AI render (Mode B), or style replication (Mode C).

You do NOT write language. You do NOT pick beats. You do NOT change the hook. You do NOT decide tier or mode. You translate the script into a visual plan.

## Hard rules (NEVER violate)

1. Output format = JSON only. No markdown, commentary, or explanation. Single JSON object conforming to storyboard.json schema. No code fences.
2. The script's `lines` are canonical. You may map 1..N shots per line, but every line MUST be covered by ≥1 shot.
3. Verbatim hook protection: the shot covering script.lines[0] MUST set `audio_pillar` to include "voice-only" or "voice+music-bed" — the hook line is delivered, never replaced by an inserted on-screen text card alone.
4. Entity firewall: you may NOT reference Holdco Group, 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A in any shot field. Conjugates included.
5. Banned vocabulary: inherit brief.do_not_say. Verbatim AND conjugate absence-check across every shot.action, motion_design text, and overlay_assets text.
6. No buildings rule (per CLAUDE.md, 4/22/26): every shot.setting.no_buildings_rule must be populated and declare interior/black-card/closed-set framing only. NO AI-generated fake buildings. NO stock buildings. NO aspirational skylines.
7. Tier caps are HARD: shot count, shot complexity, aspects, modes — all bounded by the tier table embedded below.
8. Defense-in-depth: re-validate tier↔mode mapping. Pilot/Starter = Mode A only. Pro = A+B. Enterprise = A+B+C. If brief or script bypassed this — you reject.
9. Captions: every shot.caption_burn_ref MUST equal script.captions.burn_in_required.
10. Duration math: sum of shot durations within ±5% of duration_target_seconds. No shot < 0.4s. No shot > 15s.
11. Rotation: if prior_storyboards shows last 3 reels opened with the same shot_type, do NOT use that shot_type for shots[0]. Flag in qc_warnings.
12. If you regenerate a shot 2 times and still fail QC → emit errorEnvelope. Do NOT ship a non-conformant storyboard.

## Tier table (runtime authoritative)

| Tier | Shots | Complexity | Locations | Talent | Aspects | Mode B s | Mode C URLs |
|------|------|-----------|-----------|-------|---------|----------|------------|
| Pilot | 6–8 | simple, moderate | 1 | 1 | 3 max | n/a | n/a |
| Starter | 6–8 | simple, moderate | 1 | 1 | 3 max | n/a | n/a |
| Pro | 8–14 | + complex | 2 | 2 | 4 max | 60 | n/a |
| Enterprise | 10–24 | + hero | 3 | 3 | all | 90 | 1 |

## Process (9 steps)

1. Validate input. If script is errorEnvelope → halt with script_not_success.
2. Defense-in-depth firewall + tier+mode revalidation.
3. Load context (lines, broll_plan, platform_variants, audio_track, captions, on_screen_text_blocks, brief.do_not_say, brief.visual_direction.no_buildings_rule, prior_storyboards).
4. Allocate shots per line per tier (1.0–1.4× lines for story/monologue; 1.5–2.2× for listicle).
5. Compose shot language (shot_type, camera_movement, focal_length_mm, framing_anchor, subject, setting, action, shot_complexity).
6. Apply on-screen + motion overlays (cross-link by second_start match; wire motion_design + overlay_assets).
7. Compose transitions + color grade (REINVENTED palette: #1A1033 / #F8F4FF / #A044FF / #FFD700).
8. Mode-specific plan (A: shoot_logistics; B: ai_render_plan; C: replication_recipe).
9. Self-QC (12-check list). Pass → emit successStoryboard. Fail twice → emit errorEnvelope.

Voice for written shot.action descriptions: clinical-warm, operator-to-operator, present tense, ≤14 words per sentence, action verbs.

Emit JSON only. Now.
```

(End of system prompt — copy-paste-ready into Day 13 SKILL bundle.)

---

## §9 Test-case plan (5 fixtures — author Day 13)

| # | case_id | Tier | Mode | Branch | Purpose |
|---|---------|------|------|--------|---------|
| 1 | case-01-reinvented-pilot-burnout-storyboard | Pilot | A | success | Happy path — 8 shots covering 6 lines, story format, single shoot day |
| 2 | case-02-reinvented-starter-listicle-counters | Starter | A | success | Listicle — 8 shots with counter motion overlays, validates 1.5x line:shot ratio |
| 3 | case-03-script-was-error-envelope | n/a | n/a | error→script_not_success | Reject — upstream Script Agent failed |
| 4 | case-04-mode-b-on-pilot-tier | Pilot | B | error→tier_constraint_violation | Defense-in-depth — Mode B not allowed on Pilot |
| 5 | case-05-mode-c-style-replication-pro | Pro | C | error→tier_constraint_violation | Mode C requires Enterprise — defense-in-depth |

Day 13 SKILL bundle authors all 5 fixtures + validates against `input.schema.json` (must pass 5/5).

---

## §10 Script → Storyboard Field Map (single source of truth)

| script.json field | storyboard.json destination |
|-------------------|------------------------------|
| script_id | storyboard.script_id |
| brief_id | storyboard.brief_id |
| brand_id | storyboard.brand_id |
| tier | storyboard.tier (verbatim) |
| lever | storyboard.lever (verbatim) |
| production_mode | storyboard.production_mode (verbatim) |
| duration_target_seconds | storyboard.duration_target_seconds |
| hook_block.spoken_line | shots[0].action context (informs framing) |
| hook_block.first_frame_text | overlay_assets[0].text (Frame 1 burn-in) |
| lines[i].line_id | shots[*].line_id_ref (1:N mapping) |
| lines[i].second_start..second_end | bounds shot.second_start..second_end allocations |
| lines[i].pace_marker | informs camera_movement choice (fast-open → push-in / whip-pan candidate) |
| lines[i].emphasis_words | informs shot.shot_type (emphasis often = ECU/CU) |
| broll_plan[i] | seeds shot.shot_type=insert/cutaway with source_hint inherited |
| platform_variants[].aspect | locked_aspect_ratios |
| platform_variants[].hook_first_frame | overlay_assets per-aspect variant |
| on_screen_text_blocks[i] | shot.on_screen_text_ref by second_start match |
| audio_track.voice_pacing | informs shot.duration_seconds within line bounds |
| audio_track.music_swells | audio_sync_map.music_swell_shot_ids |
| audio_track.duck_under_speech_db | shot.duck_under_speech_db_inherit |
| captions.burn_in_required | shot.caption_burn_ref (every shot) |
| cta_block.second_start..second_end | bounds final shots (CTA shots) |
| qc_pre_flags | inherited into storyboard.qc_pre_flags |
| metadata | informs storyboard.metadata.parent_chain |

This map is authoritative. Storyboard Agent never re-derives strategy from the brief — only from the script's translated state.

---

## §11 Lever-state behavior (carried from brief; no override)

| lever_state | Storyboard behavior |
|------------:|---------------------|
| 3 | Full output. Human approves every storyboard. metadata.human_review_required = true. |
| 2 | Sampled approval. metadata.human_review_required = false unless qc_warnings non-empty. |
| 1 | Full autonomy. Storyboard auto-routes to Production Coord. metadata.human_review_required = false. |

Storyboard Agent does NOT override lever. It inherits from the script's lever, which inherited from the brief's lever, which was set by the orchestrator based on the brand's accumulated reels-shipped count (3 → 30 reels → 2; 2 → 90 reels → 1).

---

## §12 Memory loop (prior_storyboards)

When `prior_storyboards` is supplied (up to 5 most recent for the brand):

1. **Opener dedupe.** If the last 3 reels opened with the same `shots[0].shot_type`, do NOT use it for current shots[0]. Add `qc_warnings: ["opener_shot_type_rotation_enforced"]`.
2. **Camera movement rotation.** If 4 of 5 prior used `dolly-in` as primary movement, prefer `static` or `gimbal-orbit` for the current reel's primary movement.
3. **Color grade variance.** If all 5 prior used the same color_grade preset, allow ±5% saturation drift to keep visual feed alive.
4. **Wardrobe rotation (Mode A).** If `shoot_logistics.wardrobe` matches 2 of last 3 → flag as soft warning, prefer alternate.

Memory loop is best-effort, not blocking. Failures emit qc_warnings, not errorEnvelope.

---

## §13 Parked open questions (10 — all non-blocking through Week 5)

1. **Multi-talent storyboard format** — when Pro tier introduces 2-talent shoots, does the schema need `subject` to become `subjects[]` array? (Defer to Week 4 with Mode B planning.)
2. **Aerial shot allowance for Pilot** — currently disallowed by tier complexity rule; should we allow drone B-roll if budget_minutes_est is trivial? (Defer.)
3. **AI render seed determinism (Mode B)** — should `ai_render_hints.seed` be locked across re-runs for reproducibility, or randomized for variety? (Defer to Week 4.)
4. **Style replication legal review (Mode C)** — when source_url is a third-party reel, what's the IP boundary? (Defer to Week 5; Linda/Marblism legal pre-check before Enterprise tier launches.)
5. **Per-platform shot variants** — should the storyboard emit one master shot list with per-platform crop hints, or N parallel storyboards (one per aspect)? (Default v1.0 = master + crop hints. Revisit if QC shows aspect-specific drift.)
6. **Color grade locked vs. brand-rotatable** — REINVENTED palette is locked; when ARS scales to other Sequel clients, does each brand need their own brand-locked palette in the system prompt, or runtime-injected from brief? (Defer to Week 6 multi-brand work.)
7. **Motion design vendor binding** — currently abstract "motion_overlay_ref"; do we lock to a specific tool (After Effects template / Lottie / web-based generator)? (Defer to Edit agent spec, Week 3.)
8. **Caption-burn font locking** — `bold-yellow-jamila` is the Pilot/Starter style; should this become a brand asset registry rather than inline in script.captions.style? (Defer to multi-brand.)
9. **Shot-list export format for videographer (Mode A)** — Notion table? CSV? PDF call sheet? (Defer to Production Coord agent spec, Week 3.)
10. **Hero shot definition** — Enterprise-only "hero" complexity is ambiguous. Codify acceptance criteria (e.g., `budget_minutes_est ≥ 60` AND `alt_options ≥ 3`). (Defer.)

All 10 are tracked in dashboard "Open Questions" card. None block Week 3 SKILL bundle build.

---

## §14 Implementation plan for Day 13 (Sat May 2 — Week 3 Day 1)

**Storyboard Agent SKILL bundle build (~75 min):**

1. `schemas/input.schema.json` (Draft 2020-12) — validate Storyboard Agent input shape
2. `schemas/output.schema.json` (Draft 2020-12) — storyboard.json success + error envelope variants
3. Self-validate both schemas as Draft 2020-12 (must self-validate clean)
4. Author `SKILL.md` (system prompt + 9-step process + tier table + 12-check QC) — copy spec §5/§6/§8 into deployable form
5. Author `prompts/user-template.txt`
6. Author 5 test fixtures (case-01..05) per spec §9
7. Validate all 5 input fixtures against `input.schema.json` — must pass 5/5
8. Author `README.md`
9. Mirror to `/outputs/ars/skills/storyboard-agent/`
10. Update dashboard

**Day 14 (Sun May 3) — Rest Day rule.** Spec/docs only, no code.

**Day 15 (Mon May 4) — LLM execution + Production Coord SPEC kickoff.**

---

## §15 12 Critical Decisions — LOCKED

1. **Output is JSON only.** No prose, no markdown wrappers. Same as Brief, Script.
2. **Polymorphic input acceptance.** Schema accepts both successScript and errorEnvelope; runtime branches on shape.
3. **Shot:line allocation = 1:N.** Multiple shots per line allowed. Every line MUST be covered.
4. **Hook line is delivered, not replaced.** shots[0] audio_pillar must include voice. (Mirrors Script Agent's hook-verbatim rule, applied to delivery.)
5. **No-buildings rule per shot.** Every single shot declares it. Inherited from CLAUDE.md HC Visual Brand Rule (4/22/26) — extended to ALL ARS output.
6. **Tier table embedded in system prompt.** Runtime self-containment, same as Script Agent.
7. **Mode authorization defense-in-depth.** Storyboard re-checks tier↔mode after Brief and Script both checked. Three independent rejections.
8. **Caption burn parity.** Every shot inherits script.captions.burn_in_required. No per-shot drift below Enterprise.
9. **Duration math ±5%.** Strict. Sum of shot durations within ±5% of script.duration_target_seconds. No drift.
10. **Color grade brand-locked v1.0.** REINVENTED palette only. Multi-brand defer to Week 6.
11. **Memory loop = best-effort.** Failures emit qc_warnings, not errorEnvelope. Prior_storyboards never blocks.
12. **2-retry max.** If Self-QC fails twice on same shot → errorEnvelope. No 3rd attempt. Predictable failure surface.

---

## §16 Production Coord hand-off preview (Day 15 spec target)

Storyboard Agent emits successStoryboard → Production Coord Agent picks up:
- Mode A → builds call sheet, books videographer, sources b-roll per source_hint, schedules shoot
- Mode B → routes ai_render_plan to AI Video Gen Agent (one of: runway/pika/luma/flux/kling/higgsfield)
- Mode C → routes replication_recipe to Style Replication Agent

Production Coord SPEC kickoff = Day 15 (Mon May 4). It will reference storyboard.json shape directly from this spec's §3.

---

## §17 Sign-off table

| Section | Status | Notes |
|---------|--------|-------|
| §1 Purpose | LOCKED | Production gate definition |
| §2 Inputs | LOCKED | Polymorphic accept of successScript + errorEnvelope |
| §3 Outputs | LOCKED | successStoryboard + errorEnvelope; shot_object schema fully defined |
| §4 Tier constraints | LOCKED | Same shape as Script Agent §4 |
| §5 9-step process | LOCKED | Mirrors Script Agent exactly |
| §6 12-check QC | LOCKED | Defense-in-depth firewall preserved |
| §7 Failure modes | LOCKED | 12 modes mapped to 9 error codes |
| §8 System prompt | LOCKED | Self-contained, runtime tier table embedded |
| §9 Test cases | DRAFT | 5 fixtures named; author Day 13 |
| §10 Script→Storyboard field map | LOCKED | Single source of truth |
| §11 Lever-state | LOCKED | Inheritance only, no override |
| §12 Memory loop | LOCKED | Best-effort, non-blocking |
| §13 Open questions | PARKED | 10 tracked, all non-blocking through Week 5 |
| §14 Implementation plan | LOCKED | Day 13 SKILL bundle map |
| §15 Critical decisions | LOCKED | 12 decisions |
| §16 Production Coord preview | LOCKED | Day 15 SPEC kickoff |
| §17 Sign-off | THIS TABLE | LOCKED |

**16 of 17 sections LOCKED on Day 11. §9 fixtures author Day 13 alongside SKILL bundle.**

---

## Provenance

- Authored: 2026-04-30 (Thu · Day 11 · Wk2D5) ARS overnight build session
- Pulled forward from originally scheduled Day 12 (Fri May 1) to free Friday for cross-spec consistency review + week-end wrap
- Mirrors: Brief Agent SPEC (Apr 26), Script Agent SPEC (Apr 28)
- Source canon: this file lives at `ars/ARS-2026-04-30-Storyboard-Agent-v1-Spec.md` (mirror at `/outputs/ars/`)
- No external comms sent. No financial commitments made. Zero entity-boundary violations.

*Storyboard Agent v1.0 SPEC — third pre-production agent locked. Pre-production firewall now triple-redundant: Brief (strategy gate) → Script (performance gate) → Storyboard (production gate). Three independent agents will reject any output that touches HC / Principal / NPOX / banned vocab before a single frame is shot or rendered.*
