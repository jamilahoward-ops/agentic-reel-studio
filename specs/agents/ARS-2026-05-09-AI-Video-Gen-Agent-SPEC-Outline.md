# ARS — AI Video Gen Agent v1.0 SPEC OUTLINE (§0–§5)

**Date:** May 9, 2026 (Sat · Day 20 · Wk4D1 — Week 4 kickoff)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** OUTLINE ONLY — sections §0–§5 drafted (purpose, scope, inputs, outputs skeleton, tier constraints, hard rules / process). Full SPEC body §6–§16 + LOCK target Day 24 (Wed May 13). SKILL bundle Day 25–26. LLM-test runbook Day 27.
**Pattern source:** `ARS-2026-05-01-Production-Coord-Agent-SPEC-Outline.md` (Day 12 outline — proven 17-section shape inherited verbatim).
**Predecessor agent:** Production Coord Agent (consumes `production_plan.json` `mode_b_plan` branch as canonical input).
**Successor agents:** Edit Director (all modes), QC Agent (post-render gate), Style Replication Agent (Mode C; reads anchor frames from this agent's output).

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 4 — Production layer kickoff (Mode B authorization gate) |
| Agent index | #5 of 17 (per Orchestration Blueprint Day 5) |
| Pipeline tier | PRODUCTION (first of two — AI Video Gen + Style Replication) |
| Mode coverage | **Mode B exclusive** — Mode A = live shoot (no agent), Mode C = Style Replication Agent |
| Predecessor SPEC | `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` (Day 14 LOCKED) |
| Predecessor schemas | `skills/production-coord-agent/schemas/output.schema.json` Day 17 LOCKED |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape, qc_pre_flags format, metadata block all inherited |
| Defense-in-depth layer | **5th** firewall pass (Brief→Script→Storyboard→ProdCoord→AIVideoGen) |
| Lever inheritance | Reads `lever_state` from prior layers; emits `human_review_required` per Lever 3 default until Day 30+ |
| Pricing tier authority | Pro tier (Mode B unlocked) + Enterprise tier (Mode A+B+C) — Pilot/Starter NEVER reach this agent |

**Build calendar:**
- Day 20 (today, Sat May 9 · Wk4D1) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 21 (Sun May 10 · Rest Day) — no build
- Day 22 (Mon May 11 · Wk4D2) — SPEC body §6–§10 (system prompt v1.0 + 12-check QC list + tier constraints reconciled)
- Day 23 (Tue May 12 · Wk4D3) — SPEC body §11–§16 (engine assignment heuristics + cost model + performance targets + test fixtures + change log)
- Day 24 (Wed May 13 · Wk4D4) — SPEC LOCK
- Day 25 (Thu May 14 · Wk4D5) — input.schema.json + output.schema.json (Draft 2020-12, mutual-exclusivity if applicable)
- Day 26 (Fri May 15 · Wk4D6) — SKILL bundle (10 files: SKILL.md, README, user-template, 2 schemas, 5 test fixtures) — 5/5 inputs validate clean
- Day 27 (Sat May 16 · Wk5D1) — LLM Test Runbook (paste-and-run, pattern from Day 11/19)
- Day 28+ — operator-gated LLM LOCK; Mode B production gate goes live

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **AI Video Gen Agent** is the first production-tier agent in ARS. It is the **render gate** of the pipeline — the moment the spec stops being JSON and starts being pixels.

Pre-production gates already passed:
- Brief Agent = strategy gate ("Is this the right reel?")
- Script Agent = performance gate ("Is the language going to land?")
- Storyboard Agent = production gate ("Can we shoot/render this in budget, in tier, on-brand?")
- Production Coord Agent = execution gate ("Have we secured everything needed to actually make it happen?")
- **AI Video Gen Agent = render gate ("Did the pixels come out matching the brief, on-budget, with style consistency, with no firewall breach in the prompt?")**

It converts a `production_plan.json` `mode_b_plan` branch into a **rendered shot set** (`rendered_shots.json` + asset URIs):
- Per-shot render dispatch to the assigned engine (Runway / Pika / Luma / Flux / Kling / Higgsfield / HeyGen for talent shots)
- Style consistency anchor binding (anchor seed → downstream-shot seed inheritance per ProdCoord SPEC §13 #3)
- Render budget enforcement (NEVER exceed `mode_b_plan.total_render_cost_usd_estimated` more than 10%)
- Post-render QC seed handoff to QC Agent
- Negative-prompt firewall (entity / banned-vocab / no-buildings list passed into every prompt to every engine)
- Failure-cascade handling (if engine N fails, fall back to `fallback_engine_id` per ProdCoord plan; track attempts; emit `render_quota_exhausted` if all options burn)

**Single-responsibility line:** *"Pixel binding for an executable render queue."*

**Pipeline position (per Orchestration Blueprint §5):**
```
Trend Hunter → Strategy → Brief → Script → Storyboard → Production Coord →
   ├── (Mode A) Live shoot — no agent, human videographer + crew
   ├── (Mode B) AI VIDEO GEN ← THIS AGENT
   └── (Mode C) Style Replication
→ Edit Director → Editor → Sound → Motion → QC → Localization → Publishing → Loop
```

**Why the AI Video Gen Agent matters:** Mode B is the highest-margin production mode in ARS (no human shoot crew, no location, no talent day-rate). It is also the highest-risk: a hallucinated frame, a prompt drift to off-brand visuals, a banned-vocab leak baked into rendered text overlay, or a $400 over-budget render run can each kill the unit economics. This agent enforces the Mode B production envelope at runtime — engine routing, seed inheritance, cost ceiling, prompt firewall, render quota reservation true-up, and handoff payload integrity. It is the **first agent in the pipeline that touches a paid external API at runtime** (every prior agent is pure JSON transformation). Therefore it carries cost authority that no prior agent does.

**Hand-off contract enforced:**
- INPUT contract: AI Video Gen reads `production_plan.json` per Production Coord Agent v1.0 output schema, specifically requires `production_mode == "B"` AND `mode_b_plan != null`. Re-validates tier↔mode + entity firewall (defense-in-depth, **fifth time**). Halts with `not_mode_b` errorEnvelope if branch is wrong.
- OUTPUT contract: emits `rendered_shots.json` per §3 of this spec. Downstream production agents (Edit Director, QC, Style Replication for Mode C anchor seeds) read this without re-deriving from production_plan.

**v1.0 boundary (in-scope vs. deferred):**
| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| Engine routing (6 named engines + HeyGen for talent) | Auto-engine selection by historical hit rate |
| Style consistency anchor (one anchor seed → all child shots inherit) | Multi-anchor rotation for hero/secondary/tertiary visual themes |
| Render quota reservation + drawdown | Live quota negotiation across vendor accounts |
| Cost ceiling enforcement (hard reject at >110% of plan) | Cost-aware engine swap mid-queue |
| Negative-prompt firewall composition | Vector-similarity audit of rendered frames vs. firewall list |
| Single-attempt render + 1 retry on transient failure | Multi-attempt with quality grading between attempts |
| Per-shot QC seed (basic: face count, motion blur estimate, brand-color presence) | Full QC offload to QC Agent — v1.0 emits seed only |
| HeyGen talent integration (Jamila clone v2 — REINVENTED) | Multi-talent v1.1+ |
| Lever 3 only (every render reviewed by human via QC Agent) | Lever 2 sampled approval after 30-reel threshold |

---

## §2. Inputs (TO DRAFT Day 22)

**Required:**
- `production_plan` — full Production Coord Agent successProductionPlan object. MUST validate against `schemas/production-coord-agent/output.schema.json` successProductionPlan variant. Polymorphic accept (success or errorEnvelope); halt with `production_plan_not_success` if errorEnvelope.
- `production_plan.production_mode` MUST equal `"B"`. Halt with `not_mode_b` errorEnvelope otherwise.
- `production_plan.mode_b_plan` MUST be non-null. Halt with `not_mode_b` errorEnvelope otherwise.
- `brief` + `script` + `storyboard` — pass-through references for tier+brand+do_not_say + entity firewall (denormalized for self-containment, 5th defense-in-depth layer).
- `session_id` — string matching `^ars-\d{4}-\d{2}-\d{2}-\d{3,}$`.
- `lever_state` — int 1..3.

**Required (engine credentials handle):**
- `engine_quota_handles` — opaque object {runway: handle_id, pika: handle_id, luma: handle_id, flux: handle_id, kling: handle_id, higgsfield: handle_id, heygen: handle_id}. Agent does NOT read raw API keys; it asks the platform layer (Sequel Digital orchestrator) to reserve and execute against each handle. **Hard rule: agent MUST NOT emit any credential value in any output field.**

**Optional:**
- `style_token_lib` — REINVENTED-specific style tokens cached for prompt-seeding (purple/gold palette, Alux-style framing language, anchor frames from past reels).
- `negative_prompt_template` — base negative prompt prefix shared across engines (firewall + banned vocab + brand-anti-patterns).
- `prior_render_telemetry` — last 10 reels' per-engine hit rate / drift rate / cost variance — informs v1.1 engine swap heuristics; v1.0 ignored.
- `prompt_compose_strategy` — enum {literal_passthrough, augmented, fully_rewritten}. v1.0 = `augmented` only (engine prompt = ProdCoord's `prompt_seed` + style_token + negative_prompt_template). Other values reserved for v1.1+.
- `cost_overrun_buffer_pct` — int 0..15. Default 10. Hard reject if `total_actual_cost_usd > total_estimated_cost_usd * (1 + buffer/100)`.

**Validation rules (TO ENUMERATE Day 22):**
- ProdCoord plan's tier↔mode mapping re-validated (defense-in-depth fifth re-check).
- Every shot in `mode_b_plan.render_queue[]` MUST have `quota_reserved_bool == true`. Else → `quota_not_reserved` errorEnvelope (this is Production Coord's responsibility — AI Video Gen does not re-reserve).
- Style consistency anchor MUST resolve: `mode_b_plan.style_consistency_anchor.anchor_shot_id` MUST equal `mode_b_plan.render_queue[0].shot_id`. Else → `anchor_misalignment` errorEnvelope.
- Tier authorization: `production_plan.tier` MUST be in {Pro, Enterprise}. Else → `tier_constraint_violation` errorEnvelope (Pilot/Starter are Mode A only — defense-in-depth, this should already be caught upstream but we re-check).
- HeyGen talent shots: every shot with `engine_id == "heygen"` MUST have a `talent_id` populated AND that talent must equal `"jamila-howard-reinvented-v2"` for v1.0. Multi-talent deferred.
- Negative prompt presence: every render dispatch MUST attach the composed negative prompt (firewall + banned + brand-anti). Self-QC step #11 verifies.

---

## §3. Outputs — `rendered_shots.json` (TO DRAFT Day 22 + LOCK Day 25 in schema)

Single canonical output. Polymorphic: successRenderedShots OR errorEnvelope (per Cross-Spec canon §3.8).

### 3.1 successRenderedShots schema (high-level skeleton)

```
rendered_shots.json
├── render_set_id               string  pattern: ^renderset-REINVENTED-\d{4}-\d{2}-\d{2}-\d{3,}$
├── parent_chain                array   prefixItems: [brief_id, script_id, storyboard_id, production_plan_id]
│                                       items: false   (4-tuple LOCKED for Mode B; Mode A would be 3-tuple via Live Shoot, no AI Video Gen layer)
├── production_plan_id          string  pattern: ^productionplan-...
├── brand_id                    string
├── tier                        enum: Pro|Enterprise   (Pilot/Starter rejected upstream — re-asserted here)
├── lever                       int 1..3
├── production_mode             const: "B"
├── created_at                  ISO datetime
├── session_id                  string
├── status                      enum: ready_for_edit|partial_with_warnings|blocked
├── total_shots                 int       (mirrors production_plan.total_shots)
├── total_rendered_shots        int       (MUST equal total_shots for status=ready_for_edit)
│
├── rendered_shots              array of object   // see §3.2 — per-shot output record
├── style_consistency_anchor    object             // see §3.3 — anchor frame + downstream propagation log
├── render_telemetry            object             // see §3.4 — cost true-up, latency, retry log
├── handoff_targets             array              // [{ agent: "edit-director|qc|style-replication", payload_ref: "..." }]
├── escalation_path             array              // ordered fallback contacts/engines if any shot failed
├── qc_pre_flags                array (≥ 4)        // snake_case predicates per Cross-Spec §3.7
├── qc_warnings                 array              // soft warnings — partial frames, suspected drift
├── rationale                   object             // why this engine for this shot, why this anchor, retry decisions
└── metadata                    object             // canonical metadata block per Cross-Spec §3.9
```

### 3.2 rendered_shots[] record (per-shot output)

```
rendered_shots[i]
├── shot_id                     string   (mirrors production_plan.mode_b_plan.render_queue[i].shot_id)
├── shot_index                  int      (1-indexed position in storyboard order)
├── engine_id                   enum: runway|pika|luma|flux|kling|higgsfield|heygen
├── model_id                    string   (e.g., "runway-gen3-alpha-turbo", "heygen-v3-clone")
├── prompt_compiled             string   // final composed prompt — passthrough seed + style_token + brand inheritance
├── negative_prompt_compiled    string   // firewall + banned + brand-anti — VERIFIED NON-NULL
├── seed_value                  int      // anchor seed (shot_index==1) OR inherited (shot_index>1)
├── seed_inheritance_source     string OR null   // null for anchor; "rendered_shots[0].seed_value" for inheritors
├── duration_s                  number
├── aspect                      enum: 9:16|1:1|4:5|16:9
├── resolution                  string   (e.g., "1080x1920", "4K-upscaled")
├── render_seconds_actual       number
├── render_cost_usd_actual      number
├── attempts                    int 1..3
├── render_status               enum: rendered|partial|failed
├── asset_uri                   string   // platform-relative URI; agent NEVER emits absolute external URL with credentials
├── asset_checksum              string   // SHA-256 of rendered output
├── post_render_qc_seed         object   // see §3.5 — basic-pass QC signals
├── retry_log                   array    // [{attempt, engine_id, fail_reason, fallback_engine_id_used}]
└── rationale                   string   // one-sentence why-this-engine-for-this-shot
```

### 3.3 style_consistency_anchor (audit object)

```
style_consistency_anchor
├── anchor_shot_id              string   (== rendered_shots[0].shot_id)
├── anchor_seed                 int
├── anchor_engine_id            string
├── anchor_model_id             string
├── inheritor_shots             array of {shot_id, seed_value, inheritance_match_score_0_1}
├── drift_threshold             number 0..1   (default 0.85 — below = qc_warnings populated)
└── propagation_strategy        enum: literal_seed_inherit|seed_plus_style_token   (v1.0 = literal_seed_inherit)
```

### 3.4 render_telemetry (cost true-up + latency)

```
render_telemetry
├── total_render_seconds_actual    number
├── total_render_cost_usd_actual   number
├── budget_estimate_usd            number   (mirrors production_plan.mode_b_plan.total_render_cost_usd_estimated)
├── budget_variance_pct            number   (actual / estimate - 1) * 100
├── budget_variance_within_tolerance_bool   boolean   (TRUE if abs(variance) ≤ cost_overrun_buffer_pct)
├── per_engine_minutes             object   {runway: number, pika: number, luma: number, flux: number, kling: number, higgsfield: number, heygen: number}
├── per_engine_cost_usd            object   (same keys)
├── retry_count_total              int
├── failure_count_total            int
├── start_timestamp                ISO datetime
├── end_timestamp                  ISO datetime
└── total_wall_clock_minutes       number
```

### 3.5 post_render_qc_seed (per-shot basic signals — full QC by QC Agent)

```
post_render_qc_seed
├── frame_count                       int
├── black_frame_count                 int       // hard fail if > 5% of frames
├── face_present_bool                 boolean   // expected for HeyGen talent shots
├── face_count_estimated              int
├── motion_blur_score_0_1             number    // 1.0 = clean, 0.0 = unusable
├── brand_color_presence_bool         boolean   // purple/gold detected in dominant palette
├── on_brand_palette_match_score_0_1  number
├── suspected_drift_bool              boolean   // TRUE if anchor inheritance score < drift_threshold
├── suspected_text_overlay_bool       boolean   // TRUE if text rendered — flag for banned-vocab walk by QC
└── qc_seed_notes                     string    // human-readable handoff note for QC Agent
```

### 3.6 errorEnvelope

Per Cross-Spec canon §3.8. Codes (TBD Day 22 — initial 13):

- `input_validation_failed`
- `entity_firewall_breach` (defense-in-depth, **5th** re-check)
- `tier_constraint_violation` (Pilot/Starter reached Mode B — should never happen; defense-in-depth)
- `production_plan_not_success` (predecessor errorEnvelope variant)
- `not_mode_b` (production_mode != "B" or mode_b_plan is null)
- `quota_not_reserved` (any render_queue[i].quota_reserved_bool != true)
- `anchor_misalignment` (style_consistency_anchor.anchor_shot_id != render_queue[0].shot_id)
- `render_quota_exhausted` (engine + fallback_engine both burned)
- `cost_overrun` (total_actual > estimate * (1 + buffer))
- `engine_failure_unrecoverable` (3 attempts all fail across engine + fallback)
- `negative_prompt_missing` (any render dispatched without composed negative prompt — should be impossible; defense-in-depth)
- `talent_unauthorized` (HeyGen shot with talent_id != "jamila-howard-reinvented-v2" in v1.0)
- `schema_invalid_after_retry`
- `ai_video_gen_agent_failed`

---

## §4. Tier Constraints (TO RECONCILE Day 22 against Pricing Model 4/25 + ProdCoord §4)

| Tier | Mode B authorized | Render budget per reel | Render seconds per reel cap | Engines accessible | Talent (HeyGen) | Anchor strategy |
|------|:-----------------:|:----------------------:|:---------------------------:|--------------------|:---------------:|----------------|
| Pilot | NO | n/a | n/a | n/a | n/a | n/a |
| Starter | NO | n/a | n/a | n/a | n/a | n/a |
| Pro | YES | $400 cap (5× margin floor) | 60s | Runway, Pika, Luma, Flux, Kling, Higgsfield, HeyGen | Jamila v2 only | literal_seed_inherit |
| Enterprise | YES | $750 cap (5× margin floor) | 90s | All Pro + premium tiers (Runway Gen3 Turbo, HeyGen v3 polish) | Jamila v2 only v1.0 / multi-talent v1.1+ | literal_seed_inherit |

**Cost ceiling re-assertion:** AI Video Gen agent enforces tier ceiling AT RUNTIME. ProdCoord's estimate is the budget; AI Video Gen's actual is the bill. Hard reject at >110% of estimate per `cost_overrun_buffer_pct`.

**These numbers inherit from ProdCoord SPEC §4 (Day 14 LOCKED).** Day 22 reconciliation pass confirms exact-match.

---

## §5. 11-Step Process (mirrors prior agent shape)

1. **Validate input shape.** Parse `production_plan.json` against `input.schema.json`. If errorEnvelope variant → `production_plan_not_success`. If `production_mode != "B"` OR `mode_b_plan == null` → `not_mode_b`.
2. **Defense-in-depth firewall + tier+mode revalidation** (5th time across the pipeline).
3. **Load context** — production_plan.mode_b_plan.render_queue, production_plan.mode_b_plan.style_consistency_anchor, brief.do_not_say, storyboard.shoot_logistics passthrough, all engine_quota_handles, style_token_lib, negative_prompt_template.
4. **Compose negative prompt template.** Concatenate: entity firewall list (10 canonical entries) + brief.do_not_say + brand-anti-patterns + no-buildings string. ASSERT non-empty. This template is attached to every render dispatch.
5. **Anchor render (shot_index=1).** Dispatch to assigned engine with `prompt_compiled = prompt_seed + style_token + brand_inheritance`. Capture `anchor_seed`. If primary engine fails 1× retry → fallback engine. If both fail → `engine_failure_unrecoverable` for that shot, halt agent (anchor failure is fatal — downstream shots cannot inherit).
6. **Inheritor renders (shot_index>1).** For each remaining `render_queue[i]`, dispatch to its assigned engine with `seed_value = anchor_seed` (literal inheritance v1.0). Composed prompt + composed negative prompt attached. Same 1× retry + fallback policy. Failure of an inheritor shot does NOT halt agent — emits partial set with `status=partial_with_warnings`.
7. **Per-shot QC seed.** For each rendered asset, run basic-pass QC: frame_count, black_frame_count, face_present_bool (expected for HeyGen), motion_blur_score, brand_color_presence_bool, on_brand_palette_match_score, suspected_drift_bool (anchor inheritance score < threshold), suspected_text_overlay_bool. Store in `post_render_qc_seed`.
8. **Render telemetry true-up.** Sum actuals: total_render_seconds_actual, total_render_cost_usd_actual, per_engine_minutes, per_engine_cost_usd, retry/failure counts. Compute `budget_variance_pct`. ASSERT `abs(variance) ≤ cost_overrun_buffer_pct`. Else → `cost_overrun` errorEnvelope.
9. **Compose handoff_targets[].** Targets:
   - Edit Director (always — mode_a/b/c all flow through Edit)
   - QC Agent (always — runs after Edit; receives post_render_qc_seed for context)
   - Style Replication Agent (only if downstream Mode C reels in same session reference this anchor — v1.1+ feature; v1.0 emits empty hint)
10. **Build escalation_path.** For each shot where retries occurred OR any QC seed flagged drift, list operator-on-call + engine vendor support contact + "human review at Edit step required" flag.
11. **Self-QC + emit.** Run 12-check QC list (§6 to be drafted Day 22). Pass → emit successRenderedShots. Fail twice → emit errorEnvelope with `attempts` count.

---

## §6–§16 — TO DRAFT Days 22–23

| § | Topic | Day target |
|---|-------|-----------|
| §6 | 12-check Self-QC list | Day 22 |
| §7 | System Prompt v1.0 (LLM-facing — locks voice + hard rules + tier table + 11-step process) | Day 22 |
| §8 | Performance Targets (latency, cost, schema validity, firewall catch rate, anchor drift rate, render success rate) | Day 23 |
| §9 | Test Cases (5 fixtures — Pro Mode B happy path, Enterprise Mode B happy path, anchor failure, cost overrun, engine cascade failure) | Day 23 |
| §10 | Engine Assignment Heuristics (which engine for which shot type — talking head vs. b-roll vs. motion graphics seed) | Day 22 |
| §11 | Cost Model (per-engine $/sec lookup table — sourced from vendor pricing canon TBD) | Day 23 |
| §12 | Style Consistency Math (drift threshold derivation, inheritance scoring algorithm) | Day 23 |
| §13 | 17 Critical Decisions (mirrors ProdCoord SPEC §13 — naming, anchor strategy, cost ceiling, retry policy, failure cascades, etc.) | Day 23 |
| §14 | Hard Rules (NEVER list — entity firewall, banned vocab, no-credential leak, no-aspirational-output, no-cost-overshoot, no Pilot/Starter execution) | Day 22 |
| §15 | Change Log + Version History | Day 23 |
| §16 | Metadata block schema (canonical per Cross-Spec §3.9) | Day 23 |

---

## OPEN QUESTIONS (parking — non-blocking through Day 26 SKILL bundle)

1. **Multi-talent v1.1 timing** — do we need multi-talent (Sequel Digital external clients with their own brand spokespeople) before commercial launch Day 42, or can v1.0 ship REINVENTED-only and v1.1 lands Week 7+ as a paid-client trigger?
2. **Cost overrun buffer pct default** — 10% (current default) or 15%? Tighter buffer = more frequent `cost_overrun` errorEnvelope = more re-runs; looser = margin risk. ProdCoord §4 cost ceiling is hard, but render variance is real. Need real telemetry from first 5 Mode B reels to calibrate.
3. **Engine selection authority** — in v1.0, ProdCoord assigns engine per shot (`render_queue[i].engine_id`). AI Video Gen executes that assignment. In v1.1+, should AI Video Gen be allowed to override ProdCoord's assignment if telemetry says Engine X is hitting better lately? Adds complexity; defers to v1.1.
4. **HeyGen talent handle binding** — `"jamila-howard-reinvented-v2"` is the v1.0 hardcode. When v2 polish lands (per Roadmap Week 4 deliverable: "Jamila AI twin v2 — HeyGen polish, voice consistency, blink/hand naturalism pass"), do we version the handle to `v3` and force a re-render of all prior reels? Most likely answer: no, v2 is a frozen brand asset; v3 is a new SKU.
5. **Fallback engine authority** — ProdCoord assigns `fallback_engine_id` per shot. AI Video Gen v1.0 honors that. In v1.1+, should AI Video Gen pick a different fallback if it has better real-time telemetry? Defer.
6. **Asset URI scheme** — platform-relative (`ars://renderset/REINVENTED/2026-05-09-001/shot-003.mp4`) or absolute Sequel Digital CDN URL? v1.0 = platform-relative (avoid credential / signed-URL leakage in JSON output). Absolute URL only at Edit→Publishing handoff stage.
7. **Drift threshold default** — 0.85 (current). Below = QC warning surfaced. Need real anchor-inheritance scoring data from first 10 Mode B reels to calibrate. Day 27 LLM-test runbook will surface initial empirical scores.
8. **Negative-prompt template canon location** — does the negative-prompt template live in this agent's SKILL bundle (per-agent ownership) or in a shared `firewall-template/` module that all production-tier agents import? v1.0 = embedded in this agent's SKILL.md (faster ship). v1.1+ refactor opportunity.
9. **Render queue parallelism** — sequential render of all shots, or parallel dispatch with anchor-first dependency? v1.0 = anchor-first sequential (anchor must complete before inheritors dispatch); inheritors can parallelize. Performance target Day 23 §8.
10. **Lever 2 graduation timing** — at what Mode B reel count does AI Video Gen become Lever 2 eligible (sampled approval)? Inherits from global lever framework (30/90 thresholds) but Mode B-specific gating may be tighter due to render cost. Defer to post-Day 30.

---

## ENTITY SEPARATION (CRITICAL — re-asserted)

AI Video Gen Agent runs under **Sequel Digital Solutions umbrella**. Principal and Holdco Group have ZERO involvement.

**Defense-in-depth firewall list (5th re-check at this layer):**
- Holdco Group / Holdco Group Inc. / HC (and conjugates)
- 4821 Main / 4821 / Main flagship
- SITE-C-BRAND / 6315 / 6315
- SLN / SLN Group / SLN Cuts / SLN Shear / SLN Salon / SalonB / Shear & Cuts
- Retail Supply / Retail Supply Co
- Principal Holdco / Principal
- NPOX / Community Nonprofit Org / Nonprofit Leader A / Nonprofit Leader B / Nonprofit Leader C
- Partner Brand

**Banned vocab inheritance:** brief.do_not_say verbatim AND conjugates. Negative prompt template attaches all of the above + brief.do_not_say to every render dispatch. Self-QC step #11 verifies. Schema validator full-tree string walk verifies on output.

**No-buildings rule:** inherited from Storyboard / ProdCoord — Mode B can render exterior or interior environments AS LONG AS no recognizable real-world buildings are generated. Negative prompt includes "real-world buildings, identifiable architecture, recognizable landmarks." QC seed flag `suspected_buildings_bool` to be added Day 22 to `post_render_qc_seed`.

---

## DEFENSE-IN-DEPTH STATUS — 5th LAYER LIVE (when SPEC LOCKS Day 24)

| Layer | Agent | Defense-in-depth |
|-------|-------|------------------|
| 1 | Brief | Sets do_not_say, entity firewall first instance |
| 2 | Script | Re-validates firewall + banned vocab in script content |
| 3 | Storyboard | Re-validates firewall + tier↔mode + no-buildings |
| 4 | Production Coord | Re-validates firewall + tier↔mode + no-buildings + cost ceiling |
| **5** | **AI Video Gen** | **Re-validates firewall + tier↔mode + no-buildings + cost ceiling AT RUNTIME against actual cost + injects negative prompt into every external render API call** |

Quintuple-redundant pre-production-into-production firewall ACHIEVED at LOCK Day 24.

---

## PROCESS INTEGRITY (Day 20 build session)

- Outline only — no LLM dispatched, no render API touched, no engine credentials referenced
- No external comms (no emails sent, no DMs, no posts)
- No financial commitments (no engine subscriptions, no quota purchases)
- Pattern source: ProdCoord outline Day 12 — structure inherited 1:1 (operator muscle memory)
- Predecessor SPEC referenced for input contract; predecessor schema NOT touched
- Build log written same day (`build-log-2026-05-09.md`)
- Mirror copy to `/outputs/ars/` complete

---

## PROVENANCE

- Authored: 2026-05-09 (Sat · Day 20 · Wk4D1) — ARS overnight build session
- Deliverable file: `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (Desktop/ARS/ + outputs/ars/)
- Pattern source: `ARS-2026-05-01-Production-Coord-Agent-SPEC-Outline.md` (Day 12 outline — proven structure)
- Predecessor SPEC: `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` (Day 14 LOCKED)
- Predecessor schema: `skills/production-coord-agent/schemas/output.schema.json` (Day 17 LOCKED)
- Cross-spec canon: `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — naming, errorEnvelope, qc_pre_flags, metadata)
- Milestone plan reference: `ARS-2026-04-22-Week-1-Milestone-Plan.md` Week 4 ship targets

*Day 20 closes Week 4 Day 1 with AI Video Gen Agent SPEC outline §0–§5 SHIPPED. Body §6–§16 + LOCK target Day 24 (Wed May 13). SKILL bundle Day 25–26. LLM-test runbook Day 27.*
