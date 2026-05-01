# ARS — Cross-SPEC Consistency Review (Brief · Script · Storyboard)

**Date:** May 1, 2026 (Fri · Day 12 · Wk2D6 · Rest Day-adjacent — review work, no code)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Scope:** Compare Brief Agent v1.0 SPEC (Apr 26), Script Agent v1.0 SPEC (Apr 28), Storyboard Agent v1.0 SPEC (Apr 30) for terminology / schema / process drift before Day 13 Storyboard SKILL bundle build and Day 15 Production Coord SPEC kickoff.
**Status:** v1.0 LOCKED — naming map authoritative. 14 drift items found; 4 P0 (fix in v1.1), 6 P1 (track), 4 P2 (cosmetic).
**Source files reviewed:**
- `ars/ARS-2026-04-26-Brief-Agent-v1-Spec.md`
- `ars/ARS-2026-04-28-Script-Agent-v1-Spec.md`
- `ars/ARS-2026-04-30-Storyboard-Agent-v1-Spec.md`

---

## §1 Executive summary

Three SPECs reviewed line-by-line. **Logic and pipeline contract are sound** — every Script field traces cleanly back to a Brief field, every Storyboard field traces back to a Script field, and the defense-in-depth firewall (entity / banned vocab / no-buildings) is consistently re-validated at each agent.

Where they drift is **surface naming** — same concept, three different names. This is normal cumulative drift for SPECs authored on consecutive days without a reconciliation pass. Now is the right time to fix it: before the Storyboard SKILL bundle ships (Day 13) and before Production Coord copies any of these patterns (Day 15).

**Verdict:** No SPEC needs to be re-LOCKED. Drift items are tracked here; the canonical naming map (§3) is the single source of truth Day 13 and Day 15 build against. Brief and Script SPECs get a v1.1 patch in Week 4 to align cosmetic naming. Storyboard SKILL bundle authors against canonical names directly.

---

## §2 Drift inventory (14 items, prioritized)

### P0 — Fix in v1.1 (4 items)

These create real implementation friction or audit-trail gaps.

| # | Drift | Brief | Script | Storyboard | Canonical (proposed) | Rationale |
|---|-------|-------|--------|------------|----------------------|-----------|
| 1 | **Hook field name** | `hook.first_3_seconds` | `hook_block.spoken_line` (and `lines[0].spoken`) | `hook_block.spoken_line` (referenced) | **`hook_block.spoken_line`** with `hook_block.spoken_duration_target_seconds: 3.0` | Brief's "first_3_seconds" hard-codes a duration assumption into the field name. Script/Storyboard correctly decouple. Brief v1.1 renames field; field map already documents the transform. |
| 2 | **Platform list field name** | `platform_targets[]` | `platform_variants[]` | `platform_render_specs[]` | **`platform_variants[]`** | Three names for same array. `platform_targets` (intent) vs. `platform_variants` (executable specs) vs. `platform_render_specs` (rendering specs) — all map 1:1. Pick one. Script's `platform_variants` is most precise. Brief v1.1 renames. Storyboard SKILL bundle uses `platform_variants` not `platform_render_specs`. |
| 3 | **CTA container field name** | `cta` | `cta_block` | `cta_block` (reference only) | **`cta_block`** | Brief uses `cta`; Script/Storyboard use `cta_block`. Brief v1.1 aligns to `cta_block`. Inner field names also drift (Brief.cta.copy → Script.cta_block.spoken_line). Codify the rename map below. |
| 4 | **`storyboard_id` prefix abbreviation** | (n/a) | (n/a — `script_id` uses `script-` prefix) | `sb-` (per regex `^sb-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$`) | **`storyboard-` prefix** (full word, matches `brief-` and `script-`) | Storyboard SPEC §3.1 uses `sb-` abbreviation; Brief and Script use full-word prefixes. Storyboard SKILL bundle should regenerate the regex to `^storyboard-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$` for audit-trail consistency. |

### P1 — Track + reconcile in Week 4 retro (6 items)

These don't block Day 13 build but should be standardized before the agent fleet ships v1.0 publicly.

| # | Drift | Brief | Script | Storyboard | Canonical (proposed) |
|---|-------|-------|--------|------------|----------------------|
| 5 | **`agent_version` value format** | `"brief-agent-v1.0"` (full string with agent name) | `"1.0"` (version only) | not shown in example | **`"1.0"`** + separate `metadata.agent_id: "brief-agent" \| "script-agent" \| "storyboard-agent"`. Splitting these makes version-bumps and fleet-wide queries cleaner. |
| 6 | **`prompt_template_id` format** | `"brief-agent-v1.0-prompt"` (no date) | `"script-agent-v1-prompt-2026-04-29"` (date suffix) | not shown | **`"<agent>-v<version>-prompt"`** (no date in template id; date lives in `metadata.created_at` and the template file's git history). |
| 7 | **Failure mode count + QC check count consistency** | 10 failure modes / 8 QC checks | 12 failure modes / 12 QC checks | 12 failure modes / 12 QC checks | Brief grows to 12 / 12 in v1.1 — `iteration_count`, `qc_warnings` array, and `human_review_required` propagation gap-fill the missing 4 checks. |
| 8 | **`qc_warnings` array on output** | NOT in canonical output (referenced only in §6.2 escalation prose) | Explicit `"qc_warnings": []` in output schema | Explicit `qc_warnings` array in output schema | Brief v1.1 adds `qc_warnings: []` to canonical output schema. Empty array is valid; non-empty triggers `human_review_required: true`. |
| 9 | **`iteration_count` in metadata** | NOT present | Present | Present | Brief v1.1 adds `metadata.iteration_count: int ≥ 1`. Auditable retry count for prompt-engineering iteration. |
| 10 | **Entity-firewall regex pattern (Storyboard QC #1)** | (prose list) | (prose list) | `Holdco\|Principal\|NPOX\|4821\|6315\|SLN\|Retail Supply\|Nonprofit Leader A` | Storyboard SKILL bundle uses canonical regex: `(?i)\\b(Holdco\\s*Group\\|Holdco\\|Principal(\\s*Holdco)?\\|4821(\\s*Main)?\\|SITE-?C-?BRAND\\|6315\\|SLN(\\s*(Group\\|Cuts\\|Shear\\|Salon\\|Shears))?\\|Retail\\s*Supply\\|NPOX\\|Community\\s*Nonprofit\\|Nonprofit\\s*Leader\\s*A\\|Nonprofit\\s*Leader\\s*B\\|Nonprofit\\s*Leader\\s*C)\\b`. Brief and Script SKILL bundles cross-reference this regex from a shared firewall constants file (Day 15+ work). |

### P2 — Cosmetic (4 items, ship as-is)

These don't change behavior; flag in Week 4 cleanup.

| # | Drift | Brief | Script | Storyboard | Action |
|---|-------|-------|--------|------------|--------|
| 11 | Section-header punctuation style | `## §1. Purpose & Position in Pipeline` (period after §1) | `## §1. Purpose & Position in Pipeline` (matches Brief) | `## §1 Purpose & pipeline position` (no period, lowercase variation) | Standardize on Brief/Script form: **`## §<n>. <Title in Title Case>`** in any future SPEC. Storyboard re-formatted in v1.1 doc-pass. No semantic impact. |
| 12 | `brief_id` / `script_id` regex formality | Pattern shown by example only (`brief-REINVENTED-2026-04-27-001`) | Pattern shown by example only | Formal regex in §3.1 (`^sb-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$`) | Brief and Script v1.1 add formal regex to schema. Canonical pattern: **`^<agent_prefix>-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$`**. |
| 13 | `qc_pre_flags` element format | Prose strings ("Verify no HC / Principal / NPOX / 4821 / 6315 reference") | snake_case predicate strings ("duration_within_band", "no_banned_vocabulary") | inherits + extends, ≥4 required | Standardize on **snake_case predicates**. Brief v1.1 reformats to snake_case. Easier programmatic parsing. |
| 14 | `session_id` formal regex | (no regex; example only) | (no regex) | (no regex; "string ≥4 chars") | All three SPECs adopt: **`^ars-\d{4}-\d{2}-\d{2}-\d{3,}$`** in v1.1 schema files. |

---

## §3 Canonical naming map (single source of truth — Day 13+ build authority)

This map supersedes any drift above. Storyboard SKILL bundle and Production Coord SPEC build against this canon.

### 3.1 Top-level identity fields

| Concept | Canonical name | Where set | Where read | Notes |
|---------|----------------|-----------|------------|-------|
| Brief identifier | `brief_id` | Brief Agent | Script, Storyboard, Production Coord, Edit, QC, all downstream | Pattern: `^brief-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$` |
| Script identifier | `script_id` | Script Agent | Storyboard, Production Coord, Edit, QC | Pattern: `^script-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$` |
| Storyboard identifier | `storyboard_id` | Storyboard Agent | Production Coord, Edit, QC | Pattern: `^storyboard-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$` (NOT `sb-`) |
| Brand identifier | `brand_id` | Brief Agent | All downstream | Uppercase string. Currently `REINVENTED`. Multi-brand v1.1+. |
| Tier | `tier` | Brief Agent (passthrough downstream) | All downstream | Enum: `Pilot \| Starter \| Pro \| Enterprise` |
| Lever (state) | `lever` (output) / `lever_state` (input) | Brief Agent (passthrough) | All downstream | Int 1..3 |
| Production mode | `production_mode` | Brief Agent (passthrough) | All downstream | Enum: `A \| B \| C` |
| Session identifier | `session_id` | Orchestrator | All agents | Pattern: `^ars-\d{4}-\d{2}-\d{2}-\d{3,}$` |
| Created-at | `created_at` | Each agent at emit | Audit only | ISO 8601 datetime |

### 3.2 Hook fields (currently drifted — canon below)

| Canonical | Brief writes as | Script reads from | Notes |
|-----------|-----------------|-------------------|-------|
| `hook_block.spoken_line` | (currently `hook.first_3_seconds`) | `hook_block.spoken_line` AND `lines[0].spoken` | Brief v1.1 renames. **Verbatim copy mandatory** (Script Agent NEVER rewrites). |
| `hook_block.spoken_duration_target_seconds` | (new field — Brief v1.1) | informational | Default 3.0; was implicit in old field name. |
| `hook_block.alt_hooks[]` | (currently `hook.alt_hooks`) | distributed to `platform_variants[*].hook_first_frame` | min 2 alt hooks required. |
| `hook_block.delivery` | (currently `hook.delivery`) | `lines[0].delivery` | Enum: `direct-to-camera \| voiceover-over-broll`. |
| `hook_block.tone` | (currently `hook.tone`) | `audio_track.voice_pacing` (partial) | Free-form string. |

### 3.3 CTA fields (canon)

| Canonical | Brief writes as | Script reads/transforms to | Notes |
|-----------|-----------------|----------------------------|-------|
| `cta_block.type` | (currently `cta.type`) | `cta_block.type` | Enum: `soft \| hard \| none` |
| `cta_block.spoken_line` | (currently `cta.copy`) | `cta_block.spoken_line` (minor cadence polish allowed) | The sentence the speaker says. |
| `cta_block.on_screen_text` | (derived from `cta.copy` + brand) | `cta_block.on_screen_text` | Burn-in CTA text. |
| `cta_block.placement` | (currently `cta.placement`) | scheduled into `cta_block.second_start \| _end` | Free-form prose hint. |
| `cta_block.duration_seconds` | implicit (4–6s) | `cta_block.duration_seconds` | Strict: ≥4, ≤6. |
| `cta_block.second_start` | (n/a — Brief doesn't time CTA precisely) | `cta_block.second_start` | Must be ≥ `duration_target − 6`. |
| `cta_block.second_end` | (n/a) | `cta_block.second_end` | Must be ≤ `duration_target + 1`. |

### 3.4 Platform fields (canon — v1.1 rename across all 3 SPECs)

**Pick one name fleet-wide: `platform_variants[]`.** Brief v1.1 renames `platform_targets` → `platform_variants`; Storyboard v1.1 renames `platform_render_specs` → `platform_variants`.

| Canonical | Type | Notes |
|-----------|------|-------|
| `platform_variants[].platform` | enum | `instagram-reels \| tiktok \| linkedin-video \| youtube-shorts \| x-video` |
| `platform_variants[].aspect` | enum | `9:16 \| 1:1 \| 16:9 \| 4:5` |
| `platform_variants[].duration_seconds` | int | Per-platform duration (may differ from `duration_target_seconds` for cropped variants). |
| `platform_variants[].hook_first_frame` | string | Burn-in text first frame per-platform. |
| `platform_variants[].first_3s_optimization` | string | Free-form note (e.g., "lowercase + native text" for TikTok). |
| `platform_variants[].caption_burn` | bool | Inherits `tier ≤ Starter ⇒ true`; Pro/Enterprise optional. |

### 3.5 Time fields (canon — already consistent across SPECs)

| Field | Type | Where used | Notes |
|-------|------|------------|-------|
| `duration_target_seconds` | int | Brief, Script, Storyboard top-level | The target reel duration. |
| `duration_min` / `duration_max` | int | Brief, Script | Tier-derived bounds. Storyboard inherits from Script, doesn't restate. |
| `duration_seconds` | num | Per-line (Script) and per-shot (Storyboard) | Per-element duration. ≥0.4, ≤15 for shots. |
| `second_start` / `second_end` | num | Per-line (Script), per-shot (Storyboard), per-broll (Script), per-on-screen-text (Script), per-music-swell (Script) | Decimal seconds from t=0. |
| `second` (string range) | string | Brief beats only | e.g., `"0–3"` — keep as legacy at beat-level; downstream agents convert to numeric `second_start`/`second_end`. |
| `cps_target` | num | Script `hook_block` | Characters-per-second pacing target. |

### 3.6 ID-reference fields (canon)

| Field | Pattern | Purpose |
|-------|---------|---------|
| `line_id` | `^L\d+$` | Script line identifier (per Script SPEC §3.1). |
| `shot_id` | `^S\d+$` | Storyboard shot identifier (per Storyboard SPEC §3.2). |
| `beat_id` | `^B\d+$` | Brief beat identifier (per Script `lines[*].beat_id`). **Brief v1.1 should formally declare this in `structure.beats[*].beat_id`** (currently implicit). |
| `cue_id` | `^BR\d+$` | B-roll cue identifier (per Script `broll_plan[*]`). |
| `line_id_ref` | `^L\d+$` | Storyboard shot's reference to a script line (1:N mapping). |
| `on_screen_text_ref` | string (matches by `second_start`) | Storyboard shot's reference to an on-screen text block. **v1.2 promote to formal id like `OST<n>`**. |
| `motion_overlay_ref` | string | Storyboard shot's reference to a motion design entry. **v1.2 promote to `MO<n>` id pattern**. |

### 3.7 QC fields (canon)

| Field | Brief v1.0 | Brief v1.1 (proposed) | Script v1.0 | Storyboard v1.0 |
|-------|-----------|------------------------|-------------|------------------|
| `qc_pre_flags[]` | prose strings | snake_case predicate strings | snake_case | snake_case |
| `qc_warnings[]` | NOT in output schema | `[]` (added) | `[]` | `[]` |
| `metadata.qc_score_predicted` | float 0..1 | float 0..1 | float 0..1 | float 0..1 |
| `metadata.human_review_required` | bool | bool | bool | bool |
| `metadata.iteration_count` | NOT present | int ≥1 (added) | int ≥1 | int ≥1 |

### 3.8 Error envelope (canon — applies to all 3 agents)

```json
{
  "error": "<error_code>",
  "reason": "<≥4 chars human-readable>",
  "field": "<optional dotted path>",
  "attempts": <int 1..5>,
  "qc_warnings": ["<optional warning strings>"]
}
```

**Canonical error code namespace** (every agent uses this naming convention):

| Code | Set by | Meaning |
|------|--------|---------|
| `input_validation_failed` | All | Input shape doesn't conform to that agent's `input.schema.json`. |
| `entity_firewall_breach` | All | Banned entity reference detected (defense-in-depth — every agent re-checks). |
| `tier_constraint_violation` | All | Output exceeds tier caps OR mode-tier mismatch. |
| `schema_invalid_after_retry` | All | Internal regen exhausted; output still fails self-validation. |
| `<agent>_agent_failed` | Self | Generic catch-all after 2 failed regen attempts. e.g., `brief_agent_failed`, `script_agent_failed`, `storyboard_agent_failed`. |
| `<predecessor>_not_success` | Successor | Upstream agent returned errorEnvelope; halt downstream. e.g., `brief_not_success` (Script), `script_not_success` (Storyboard). |
| `banned_vocab_leaked` | Script, Storyboard | `do_not_say` term present after retries. |
| `duration_overflow` | Script | Sum of line durations exceeds `duration_target × 1.05`. |
| `budget_overflow` | Storyboard | Sum of shot durations OR Mode B render seconds exceeds tier cap. **Note: `duration_overflow` (Script) and `budget_overflow` (Storyboard) are different — Script measures spoken duration, Storyboard measures shoot/render budget. Keep both.** |
| `talent_profile_out_of_range` | Script | `max_words_per_minute` outside [100, 220]. |
| `mode_engine_mismatch` | Storyboard | Mode B without `mode_b_engine_profile` OR Mode C without `mode_c_reference_url`. |
| `shot_complexity_mismatch` | Storyboard | Shot complexity not authorized for tier (e.g., `hero` on non-Enterprise). |

**Brief v1.1 promotes its inline error references to a formal §3.3 errorEnvelope block** matching this shape. (Brief currently mentions `entity_firewall_breach`, `brief_agent_failed`, `input_validation_failed` — needs full enumeration.)

### 3.9 Metadata block (canon)

```json
"metadata": {
  "agent_id": "brief-agent | script-agent | storyboard-agent",
  "agent_version": "1.0",
  "model_used": "claude-opus-4-6",
  "prompt_template_id": "<agent_id>-v<version>-prompt",
  "tokens_in": <int>,
  "tokens_out": <int>,
  "latency_ms": <int>,
  "qc_score_predicted": <float 0..1>,
  "human_review_required": <bool>,
  "iteration_count": <int ≥1>
}
```

Every agent emits this exact shape. Differences in v1.0 (Brief lacks `agent_id`+`iteration_count`; Brief's `agent_version` includes the agent name; etc.) reconcile in v1.1.

---

## §4 Pipeline contract — verified clean

Despite cosmetic drift, the **handoff contracts are correct end-to-end**:

```
Brief Agent → emits brief.json (successBrief OR errorEnvelope)
           ↓
Script Agent reads brief; emits script.json (successScript OR errorEnvelope)
           ↓
Storyboard Agent reads script + brief (denormalized); emits storyboard.json (successStoryboard OR errorEnvelope)
           ↓
Production Coord Agent reads storyboard; emits production_plan.json (Day 15 SPEC target)
```

**Verified consistent across all 3 SPECs:**
1. ✅ **Polymorphic schema accept.** Each successor schema accepts both success AND errorEnvelope shapes from predecessor; runtime branches on shape.
2. ✅ **Defense-in-depth firewall.** Entity firewall re-checked at every agent (Brief sets, Script re-validates, Storyboard re-validates). Three independent rejections before a shoot/render.
3. ✅ **Verbatim hook protection.** Brief authors → Script copies verbatim → Storyboard preserves delivery (audio_pillar must include voice).
4. ✅ **Tier passthrough + cap enforcement.** Brief sets tier; every downstream re-validates tier constraints (mode authorization, count caps, complexity caps).
5. ✅ **Lever inheritance, no override.** Brief sets lever (from orchestrator); Script and Storyboard inherit and never override.
6. ✅ **No-buildings rule.** Brief declares; Script enforces in `broll_plan[*]`; Storyboard enforces per-shot in `setting.no_buildings_rule`. Triple-redundant.
7. ✅ **`brief_id` audit trail.** Every script.json and storyboard.json carries `brief_id` for upstream lineage.
8. ✅ **Schema canon.** All three use Draft 2020-12. No drift.

**Verdict: pipeline is shippable.** Drift items are cosmetic / v1.1 cleanup, not contract breaks.

---

## §5 Pre-production firewall summary (checked across all 3 SPECs)

| Check | Brief | Script | Storyboard | Defense depth |
|-------|-------|--------|------------|---------------|
| `brand_id` not in HC/NPOX list | ✅ §5.1 hard rule 2 | ✅ §2.4 + §6 check 4 | ✅ §6 check 1 | **3x** |
| `do_not_say` verbatim absence | ✅ §5.1 hard rule 3 | ✅ §6 check 5 | ✅ §6 check 2 | **3x** |
| `do_not_say` conjugate absence | ⚠️ implicit | ✅ §6 check 5 ("conjugates checked too") | ✅ §6 check 2 ("conjugates included") | **2x** (Brief should formalize in v1.1) |
| No-buildings rule | ✅ §5.1 hard rule 4 | ✅ §6 check 10 | ✅ §6 check 3 (per-shot) | **3x** |
| Tier↔mode authorization | ✅ §5.1 hard rule 6 | ✅ §6 check 12 | ✅ §6 check 7 + 8 + 9 | **3x** |
| Duration discipline | ✅ §5.1 hard rule 5 | ✅ §6 checks 6+7 | ✅ §6 check 11 | **3x** |
| Hook integrity (verbatim) | ✅ Brief authors | ✅ §6 check 3 (verbatim from brief) | ✅ §8 hard rule 3 (audio_pillar voice) | **3x** |
| `brief_id` audit trail | (n/a — origin) | ✅ §6 check 2 | ✅ inherited from script | **2x** |
| Caption burn parity | (n/a) | ✅ §3.2 (tier rule) | ✅ §6 check 12 (parity with script) | **2x** |
| Banned-vocab in **on-screen-text** | ✅ §3.2 check (do_not_say) | ✅ §6 check 5 (across `on_screen_text`) | ✅ §6 check 2 (`motion_design.text`, `overlay_assets.text`) | **3x** |

**Triple-redundant on every behavior the brand cares about.** No firewall gap found.

---

## §6 Action items

### 6.1 For Day 13 (Sat May 2 — Storyboard SKILL bundle build)

The SKILL bundle authors against this naming canon, NOT the v1.0 SPEC where it drifts.

- [ ] In `schemas/output.schema.json`: rename `storyboard_id` regex to `^storyboard-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$` (drop `sb-` abbreviation per **drift #4**).
- [ ] In `schemas/output.schema.json`: rename top-level `platform_render_specs` → `platform_variants` (per **drift #2**). Update internal references.
- [ ] In `schemas/output.schema.json`: enumerate the **9 error codes** from §3.8 above (including `script_not_success`).
- [ ] In `SKILL.md`: replace any reference to `sb-` prefix with `storyboard-` prefix.
- [ ] In `SKILL.md`: keep the rest of the system prompt VERBATIM from SPEC §8 (already LOCKED).
- [ ] Test fixtures use the canonical naming (not the drifted SPEC examples). Each fixture's expected output references `storyboard_id` with full prefix and `platform_variants` array name.

### 6.2 For Day 15 (Mon May 4 — Production Coord SPEC kickoff)

Production Coord SPEC inherits this canon by default.

- [ ] §1 Purpose / position formatted to **`## §<n>. <Title in Title Case>`** (matches Brief / Script form).
- [ ] §2 Inputs accepts polymorphic `successStoryboard | errorEnvelope`.
- [ ] §3 Outputs schema uses `production_plan_id` with pattern `^productionplan-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$`.
- [ ] §3 errorEnvelope formalized using §3.8 canon. Add `storyboard_not_success` to the predecessor-not-success namespace.
- [ ] §6 12-check QC mirrors Storyboard SPEC §6 shape.
- [ ] §10 Storyboard→ProductionPlan field map = single source of truth (mirrors Script SPEC §10 / Storyboard SPEC §10).
- [ ] §15 Critical decisions LOCKED list.

### 6.3 Brief Agent v1.1 backfill (Week 4 work)

Non-urgent. Tracked here so it doesn't get lost.

- [ ] Rename `hook.first_3_seconds` → `hook_block.spoken_line` (per **drift #1**).
- [ ] Add `hook_block.spoken_duration_target_seconds` field (default 3.0).
- [ ] Rename `platform_targets[]` → `platform_variants[]` (per **drift #2**).
- [ ] Rename `cta` → `cta_block` (per **drift #3**).
- [ ] Add `qc_warnings: []` to canonical output schema (per **drift #8**).
- [ ] Add `metadata.iteration_count` and `metadata.agent_id` (per **drift #5, #9**).
- [ ] Reformat `qc_pre_flags[]` from prose to snake_case predicates (per **drift #13**).
- [ ] Promote inline error references to formal §3.3 errorEnvelope schema (per §3.8 canon).
- [ ] Grow §6.1 failure mode count from 10 → 12 to match Script/Storyboard.
- [ ] Grow §3.2 self-QC from 8 → 12 checks (gap-fill: `iteration_count`, `qc_warnings` populated correctly, `human_review_required` correctly cascaded, `metadata.agent_id` populated).
- [ ] Add formal regex for `brief_id`, `beat_id`, and `session_id` to `schemas/input.schema.json` and `schemas/output.schema.json`.

### 6.4 Script Agent v1.1 backfill (Week 4 work)

- [ ] Drop date suffix from `prompt_template_id`: `script-agent-v1-prompt-2026-04-29` → `script-agent-v1.0-prompt` (per **drift #6**).
- [ ] Adopt canonical `metadata.agent_id` field; flatten `agent_version` to just `"1.0"` (per **drift #5**).
- [ ] Add formal regex for `script_id` to `schemas/output.schema.json` (per **drift #12**).

### 6.5 Storyboard Agent v1.1 backfill (Week 4 work)

- [ ] Reformat all section headers to `## §<n>. <Title in Title Case>` (per **drift #11**).
- [ ] Storyboard SKILL bundle authored Day 13 already uses canonical names; SPEC document re-LOCKS in v1.1 doc-pass.

---

## §7 Test: pipeline integrity check (synthetic — paper-walk)

To verify the canon is implementation-correct, walk a single brief→script→storyboard chain on paper.

**Input to Brief Agent:**
```json
{
  "brand_id": "REINVENTED",
  "topic_signal": { "topic": "Why operators burn out at 7-figure revenue", "confidence": 0.78 },
  "tier_context": "Pilot",
  "session_id": "ars-2026-05-01-001",
  "lever_state": 3
}
```

**Brief Agent emits (canonical v1.1 shape):**
- `brief_id: "brief-REINVENTED-2026-05-01-001"`
- `tier: "Pilot"`, `lever: 3`, `production_mode: "A"`
- `hook_block: { spoken_line: "...", spoken_duration_target_seconds: 3.0, alt_hooks: [...], delivery: "direct-to-camera", tone: "honest-without-pity" }`
- `platform_variants: [{ platform: "instagram-reels", aspect: "9:16", ... }]`
- `cta_block: { type: "soft", spoken_line: "...", placement: "..." }`
- `metadata: { agent_id: "brief-agent", agent_version: "1.0", iteration_count: 1, ... }`
- `qc_warnings: []`

**Script Agent reads brief; emits canonical script.json:**
- `script_id: "script-REINVENTED-2026-05-01-001"`
- `brief_id: "brief-REINVENTED-2026-05-01-001"` (audit trail)
- `hook_block.spoken_line` = brief.hook_block.spoken_line (verbatim)
- `lines[0].spoken` = brief.hook_block.spoken_line (verbatim)
- `platform_variants` populated per tier cap
- `cta_block.spoken_line` = polished from brief.cta_block.spoken_line
- `metadata: { agent_id: "script-agent", agent_version: "1.0", iteration_count: 1, ... }`

**Storyboard Agent reads script; emits canonical storyboard.json:**
- `storyboard_id: "storyboard-REINVENTED-2026-05-01-001"` (full prefix, NOT `sb-`)
- `script_id` and `brief_id` (audit trail)
- `shots[0].line_id_ref: "L1"` (covers script.lines[0])
- `shots[0].audio_pillar: "voice-only"` OR `"hybrid"` (hook delivery)
- `platform_variants` (NOT `platform_render_specs`) populated per tier cap
- `metadata: { agent_id: "storyboard-agent", agent_version: "1.0", iteration_count: 1, ... }`

**End-state:** Production Coord Agent gets `storyboard.json` with `production_mode: "A"`, builds shoot logistics, hands off to Edit Agent. Audit trail traces: `production_plan_id ← storyboard_id ← script_id ← brief_id ← session_id`.

✅ Walk-through clean. No drift breaks the contract.

---

## §8 Open questions raised by this review (3 — non-blocking)

These didn't exist before the review surfaced them. Tracked here; resolution can wait until Week 4 retro.

1. **Should `metadata.agent_id` and `metadata.agent_version` be JSON-schema enums?** Pros: prevents typos. Cons: every version bump requires schema migration. Recommend: enum on `agent_id` (small fixed set), free string on `agent_version` (semver).
2. **Should `errorEnvelope.attempts` be capped above 5?** Currently 1..5. If a model genuinely needs 6 retries, that's a prompt-engineering signal — but the cap forces the failure to surface. Recommend: keep at 5.
3. **Does `qc_warnings[]` need a typed schema (warning code + reason) instead of free strings?** v1.0 = free strings. v1.2 candidate: structured objects `{ code: enum, message: string, field: string }`. Defer until we have warning-frequency data from v1.0 production.

---

## §9 Deliverable summary

**This document = single source of truth** for ARS pre-production agent terminology. Day 13 SKILL bundle and Day 15 Production Coord SPEC build against §3 (canonical names) and §3.8 (canonical error codes), NOT against the v1.0 SPECs where they drift.

**Quantitative summary:**
- 3 SPECs reviewed: Brief (612 lines), Script (~620 lines), Storyboard (453 lines) — ~1,700 SPEC lines total
- 14 drift items catalogued (4 P0, 6 P1, 4 P2)
- 0 contract-breaking drifts found
- 10 firewall checks verified across all 3 agents (all triple-redundant where applicable)
- 4 backfill SPEC v1.1 patches queued (Week 4 work)
- 1 forward-canonical map (this §3) authored

**Status:** ✅ ARS pre-production agent fleet is shippable in v1.0 form. Cosmetic drift documented. v1.1 cleanup pass scheduled for Week 4. Day 13 Storyboard SKILL bundle and Day 15 Production Coord SPEC build against canonical names from §3.

---

*Authored: 2026-05-01 (Fri · Day 12 · Wk2D6) ARS overnight build session*
*No external comms. No financial commitments. Zero entity-boundary violations.*
*Lives at: `/outputs/ars/ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (mirror to `ars/`)*
