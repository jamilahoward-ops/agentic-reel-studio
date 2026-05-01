# ARS — Production Coord Agent v1.0 SPEC OUTLINE

**Date:** May 1, 2026 (Fri · Day 12 · Wk2D6 · Rest Day-adjacent — outline only, no LLM, no code)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Build phase:** Week 2 wrap. Full SPEC drafts on Day 15 (Mon May 4); SKILL bundle on Day 18 (Thu May 7); LLM execution Day 19; v1.0 LOCK Day 20.
**Status:** OUTLINE ONLY — section skeleton + open questions. Full SPEC body authored Day 15 against this skeleton + the Cross-Spec Consistency canon (`ARS-2026-05-01-Cross-Spec-Consistency-Review.md` §3).
**Predecessor agent:** Storyboard Agent (consumes its `storyboard.json` output as canonical input).
**Successor agents:** AI Video Gen (Mode B), Style Replication (Mode C), Edit Agent (all modes).

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Production Coord Agent** is the fourth and final pre-production agent in ARS. It is the **execution gate** of the pipeline:
- Brief Agent = strategy gate ("Is this the right reel?")
- Script Agent = performance gate ("Is the language going to land?")
- Storyboard Agent = production gate ("Can we shoot/render this in budget, in tier, on-brand?")
- **Production Coord Agent = execution gate ("Have we secured everything needed to actually make it happen?")**

It converts a `storyboard.json` into a **Mode-specific execution plan** (`production_plan.json`):
- Mode A (live shoot) → call sheet, talent confirmation, location confirmation, equipment list, weather window, b-roll source list, shoot day schedule
- Mode B (AI generation) → AI render queue (model assignments, prompt seeds, render budget reservation, style token bindings)
- Mode C (style replication) → style replication recipe (source URL pulls, gap-filler shot list, reference-frame extraction)

**Single-responsibility line:** *"Resource binding for an executable storyboard."*

**Pipeline position (per Orchestration Blueprint §5):**
```
Trend Hunter → Strategy → Brief → Script → Storyboard → PRODUCTION COORD → AI Video Gen / Style Replication / Live shoot → Edit → QC → Publish → Loop
```

**Why the Production Coord Agent matters:** A storyboard without resources is a wishlist. The Production Coord Agent is where the abstract `shoot_logistics`, `ai_render_plan`, and `replication_recipe` from the storyboard become concrete operational commitments — videographer booked, model render quota reserved, references downloaded. If this agent says "ready to execute," the next person/agent can act without further coordination.

**Hand-off contract enforced:**
- INPUT contract: Production Coord reads `storyboard.json` per Storyboard Agent v1.0 output schema. Re-validates tier↔mode + entity firewall (defense-in-depth, fourth time).
- OUTPUT contract: emits `production_plan.json` per §3 of this spec. Downstream production agents (AI Video Gen, Style Replication, Edit) read this without re-deriving from storyboard.

---

## §2. Inputs (TO DRAFT Day 15)

**Required:**
- `storyboard` — full Storyboard Agent successStoryboard object. MUST validate against `schemas/storyboard-agent/output.schema.json` successStoryboard variant. Polymorphic accept (success or errorEnvelope); halt with `storyboard_not_success` if errorEnvelope.
- `brief` + `script` — pass-through references for tier+brand+do_not_say (denormalized for self-containment).
- `session_id` — string matching `^ars-\d{4}-\d{2}-\d{2}-\d{3,}$`.
- `lever_state` — int 1..3.

**Optional (Mode A):**
- `videographer_registry` — array of available shooters with rates, equipment tier, calendar availability, location proximity, prior reels.
- `talent_registry` — speakers (initially: Jamila for REINVENTED v1.0; multi-talent v1.1+).
- `location_registry` — interior / closed-set locations available (no buildings rule applies).
- `equipment_inventory` — owned vs. rentable gear keyed by `equipment_tier` (S/M/L).
- `weather_api_handle` — weather forecast lookup id for outdoor windows.

**Optional (Mode B):**
- `ai_render_quotas` — per-engine remaining render seconds (runway / pika / luma / flux / kling / higgsfield).
- `style_token_lib` — REINVENTED-specific style tokens cached for prompt-seeding.
- `cost_floor_per_reel` — internal cost ceiling. Mode B reels must come in ≤ cost ceiling (per Pricing Model 4/25 margin floor 5x gross).

**Optional (Mode C):**
- `mode_c_reference_cache` — pre-downloaded reference frames keyed by source_url + offset_s.
- `style_match_thresholds` — minimum acceptance scores for replication match.

**Optional (any mode):**
- `prior_production_plans` — last 5 plans for this brand (cost-baseline, time-baseline, vendor preference rotation).
- `escalation_contacts` — operator on-call, billing approver, external vendor contacts (for Mode A bookings).

**Validation rules (TO ENUMERATE Day 15):**
- Storyboard's tier↔mode mapping re-validated (defense-in-depth fourth re-check).
- For Mode A: at minimum 1 videographer + 1 location + 1 talent must be available within `weather_window`. Else → `resource_unavailable` errorEnvelope.
- For Mode B: at least one engine in `ai_render_quotas` must have remaining capacity ≥ storyboard's required render seconds. Else → `render_quota_exhausted` errorEnvelope.
- For Mode C: `mode_c_reference_url` must be reachable (HEAD check); references downloadable. Else → `reference_unreachable` errorEnvelope.

---

## §3. Outputs — `production_plan.json` (TO DRAFT Day 15)

Single canonical output. Polymorphic: successProductionPlan OR errorEnvelope (per Cross-Spec canon §3.8).

### 3.1 successProductionPlan schema (high-level skeleton)

```
production_plan.json
├── production_plan_id          string  pattern: ^productionplan-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$
├── storyboard_id               string  pattern: ^storyboard-...
├── script_id                   string  pattern: ^script-...
├── brief_id                    string  pattern: ^brief-...
├── brand_id                    string
├── tier                        enum: Pilot|Starter|Pro|Enterprise
├── lever                       int 1..3
├── production_mode             enum: A|B|C
├── created_at                  ISO datetime
├── session_id                  string
├── status                      enum: ready|pending_approval|blocked
├── duration_target_seconds     int 15..180
├── total_shots                 int (passthrough from storyboard)
├── platform_variants           array (passthrough from storyboard)
│
├── mode_a_plan                 object OR null     // Mode A only — see §3.2
├── mode_b_plan                 object OR null     // Mode B only — see §3.3
├── mode_c_plan                 object OR null     // Mode C only — see §3.4
│
├── budget_reservation          object             // total_minutes, total_cost_usd, per_shot_cost_breakdown
├── execution_window            object             // earliest_start, latest_finish, blackout_dates
├── escalation_path             array              // ordered fallback contacts if primary resource unavailable
├── handoff_targets             array              // [{ agent: "ai-video-gen|style-replication|live-shoot|edit", payload_ref: "..." }]
├── rationale                   object             // why this vendor, why this engine, why this window
├── qc_pre_flags                array (≥4)
├── qc_warnings                 array
├── downstream_dependencies     object             // ai_video_gen, style_replication, edit_agent
└── metadata                    object             // canonical metadata block per Cross-Spec §3.9
```

### 3.2 mode_a_plan (live shoot)

```
mode_a_plan
├── call_sheet                  object {shoot_date, call_time_local, wrap_target, location, talent, crew}
├── talent_bookings             array of {talent_id, role, confirmed_bool, contact_method}
├── location_bookings           array of {location_id, address_internal_note, no_buildings_compliant_bool, permit_required_bool, permit_status}
├── equipment_list              array of {item, owned_or_rent, rental_vendor, rental_cost_usd}
├── crew                        array of {role, person_id, day_rate_usd, confirmed_bool}
├── shoot_schedule              array of {block_start, block_end, shots_covered_by_shot_id[], setup_minutes, shoot_minutes, breakdown_minutes}
├── b_roll_acquisition_plan     array of {shot_id, source: "stock|shot-this-week|archive", source_handle, cost_estimate_usd}
├── weather_check               object {window, forecast_summary, contingency_notes}
├── insurance_status            object {production_insured_bool, certificate_url}
└── total_estimated_minutes     int
```

### 3.3 mode_b_plan (AI generation)

```
mode_b_plan
├── render_queue                array of {shot_id, engine_id, model_id, prompt_seed, style_token, aspect, duration_s, render_seconds_estimated, render_cost_usd_estimated, quota_reserved_bool}
├── engine_assignments_summary  object {by_engine: {runway: int, pika: int, luma: int, flux: int, kling: int, higgsfield: int}}
├── total_render_seconds        int
├── total_render_cost_usd       number
├── seed_strategy               enum: locked|randomized|hybrid    // ref Storyboard SPEC §13 #3
├── upscale_pipeline            object OR null                    // optional 4K/HQ upscale stage
├── style_consistency_anchor    object {anchor_shot_id, anchor_seed, downstream_shots_inheriting[]}
└── post_render_qc_seed         object                            // hands off to QC Agent
```

### 3.4 mode_c_plan (style replication)

```
mode_c_plan
├── reference_pulls             array of {shot_id, source_url, offset_s, frame_count, downloaded_bool, cache_handle}
├── style_match_targets         array of {shot_id, match_axes: ["color","framing","movement","wardrobe"], threshold_score, validator: "model|human"}
├── gap_filler_shots            array of {shot_id, reason: "no source coverage|legal_concern|aspect_mismatch", filler_strategy}
├── ip_clearance                object {source_owner_known_bool, license_status: "fair_use|licensed|cleared|pending", legal_notes}
└── replication_validator_handle string                            // hands off to Style Replication Agent
```

### 3.5 errorEnvelope

Per Cross-Spec canon §3.8. Codes (TBD Day 15 — initial 11):

- `input_validation_failed`
- `entity_firewall_breach` (defense-in-depth, fourth re-check)
- `tier_constraint_violation`
- `storyboard_not_success` (predecessor errorEnvelope)
- `schema_invalid_after_retry`
- `production_coord_agent_failed`
- `resource_unavailable` (Mode A — videographer/location/talent all booked)
- `render_quota_exhausted` (Mode B — no engine has capacity)
- `reference_unreachable` (Mode C — source URL HEAD check failed)
- `weather_window_violation` (Mode A — forecast says shoot window unshootable)
- `cost_floor_breach` (any mode — estimated cost > tier floor)

---

## §4. Tier Constraints (TO DRAFT Day 15)

| Tier | Max shoot day-rate | Locations max | Talent count max | Equipment tier | Mode B render budget | Mode C reference URLs | Cost ceiling per reel |
|------|-------------------:|--------------:|------------------:|---------------|---------------------:|----------------------:|----------------------:|
| Pilot | $400 | 1 | 1 | S | n/a | n/a | $200 (margin floor 5×) |
| Starter | $400 | 1 | 1 | S | n/a | n/a | $200 |
| Pro | $800 | 2 | 2 | M | 60s/reel | n/a | $400 |
| Enterprise | $1500 | 3 | 3 | L | 90s/reel | 1 | $750 |

**These are placeholder numbers — Day 15 SPEC reconciles against Pricing Model 4/25 §6 (margin math) before LOCK.**

---

## §5. 9-Step Process (mirrors Brief / Script / Storyboard shape)

1. **Validate input shape.** Parse `storyboard.json` against `input.schema.json`. If errorEnvelope variant → `storyboard_not_success`.
2. **Defense-in-depth firewall + tier+mode revalidation** (4th time across the pipeline).
3. **Load context** — storyboard.shots, storyboard.shoot_logistics OR ai_render_plan OR replication_recipe, brief.do_not_say, prior_production_plans, all registries.
4. **Mode branching** — based on `production_mode`, route to Step 5a / 5b / 5c.
5a. **Mode A: live-shoot resource binding** — match shots to videographer + location + talent + equipment; build call sheet; reserve weather window.
5b. **Mode B: AI render queue construction** — assign engines to shots based on `ai_render_quotas` + style consistency anchor + cost; reserve render quota; build render queue.
5c. **Mode C: reference cache + replication recipe** — HEAD-check source URLs; download reference frames; populate gap-filler list; build IP clearance check.
6. **Budget reservation + execution window** — sum costs against tier ceiling; lock window against blackout dates; emit `cost_floor_breach` if over.
7. **Compose handoff_targets[]** — point to next agent(s) downstream by mode.
8. **Build escalation path** — for any resource where primary failed, list the Top-3 fallbacks ordered by tier-fit and cost.
9. **Self-QC + emit** — run 12-check QC list; pass → emit successProductionPlan; fail twice → emit errorEnvelope with `attempts` count.

---

## §6. 12-Check Self-QC List (TO DRAFT Day 15)

Initial 12 candidates:
1. Entity firewall re-check (4th defense-in-depth pass).
2. Banned vocab absence in `rationale.*`, `escalation_path[*].notes`, all human-readable strings.
3. No-buildings rule passthrough — Mode A `location_bookings[*].no_buildings_compliant_bool` MUST be `true` for every location.
4. Tier↔mode authorization (defense-in-depth, 4th time).
5. Mode A: every storyboard shot has at least one of (videographer assigned, b-roll source committed).
6. Mode B: every storyboard shot has an engine assignment + reserved render quota.
7. Mode C: every storyboard shot has either a reference pull OR a gap-filler entry.
8. Cost ceiling: `budget_reservation.total_cost_usd` ≤ tier ceiling (§4).
9. Execution window: `earliest_start ≥ today + 1 day` AND `latest_finish ≤ today + tier_max_lead_time`.
10. `handoff_targets[]` non-empty AND every `payload_ref` resolvable.
11. `escalation_path[]` ≥ 1 entry per Mode A primary resource.
12. Every `qc_pre_flags[]` element is a snake_case predicate (per Cross-Spec canon §3.7).

---

## §7. System Prompt v1.0 (TO LOCK Day 15)

Skeleton (matches Brief / Script / Storyboard shape):

```
You are the Production Coord Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: convert a frame-aligned storyboard.json into a Mode-specific production_plan.json — execution-ready (Mode A: shoot logistics; Mode B: AI render queue; Mode C: style replication recipe).

You do NOT design shots. You do NOT pick the hook. You do NOT change the tier or mode. You bind concrete resources to an abstract storyboard.

## Hard rules (NEVER violate)

1. Output format = JSON only. Single object conforming to production_plan.json schema. No markdown, no commentary, no code fences.
2. Every storyboard shot MUST be covered by either (Mode A) a shoot block + b-roll source, (Mode B) an engine + render quota reservation, or (Mode C) a reference pull or gap-filler.
3. Entity firewall (defense-in-depth, 4th re-check). NEVER reference Holdco Group / 4821 Main / SITE-C-BRAND / 6315 / SLN / Retail Supply / Principal Holdco / NPOX / Nonprofit Leader A / Nonprofit Leader B / Nonprofit Leader C. Conjugates included.
4. Banned vocabulary. Inherit brief.do_not_say. Verbatim AND conjugate absence-check across rationale text and human-readable strings.
5. No-buildings rule passthrough. Mode A locations MUST be no-buildings-compliant.
6. Tier caps are HARD: shoot day-rate, locations, talent count, equipment tier, render budget, reference URL count, cost ceiling — all bounded by §4 tier table.
7. Defense-in-depth tier↔mode mapping (4th re-check). Pilot/Starter = Mode A only. Pro = A+B. Enterprise = A+B+C.
8. Budget discipline. Total cost MUST be ≤ tier ceiling. If it can't, emit cost_floor_breach errorEnvelope — do NOT ship over-budget plans.
9. Resource availability. If primary resource unavailable AND no fallback in escalation_path → emit resource_unavailable errorEnvelope. Do NOT emit aspirational plans.
10. Weather window discipline (Mode A only). If forecast violates shoot window → emit weather_window_violation errorEnvelope. Do NOT ship a plan that depends on hope.
11. IP clearance discipline (Mode C only). If `ip_clearance.license_status` is `pending` AND tier is Pilot/Starter → emit errorEnvelope. Mode C is Enterprise-tier only anyway, but defense-in-depth.
12. If self-QC fails 2 times → emit errorEnvelope. No 3rd attempt. Predictable failure surface.

## Tier table (runtime authoritative)

[INSERT §4 TABLE HERE — Day 15]

## Process (9 steps)

1. Validate input.
2. Defense-in-depth firewall + tier+mode revalidation.
3. Load context (storyboard, brief.do_not_say, prior_production_plans, registries).
4. Branch on production_mode.
5a/b/c. Mode-specific resource binding.
6. Budget reservation + execution window.
7. Compose handoff_targets.
8. Build escalation_path.
9. Self-QC (12 checks). Pass → successProductionPlan. Fail twice → errorEnvelope.

Voice for written rationale fields: clinical-warm, operator-to-operator, present tense, ≤14 words per sentence, action verbs.

Emit JSON only. Now.
```

---

## §8. Performance Targets (TO DRAFT Day 15)

### v1.0 targets (Week 3 build)

| Metric | Target | Hard floor |
|--------|--------|------------|
| Latency (avg) | <60s | <180s |
| Token cost (Opus 4.6) | <$0.40/plan | <$1.00/plan |
| Schema validity rate | 100% | 95% |
| Entity firewall catch rate | 100% | 100% (zero tolerance) |
| Resource binding success rate (Mode A) | >85% on first attempt | >70% |
| Render quota reservation success rate (Mode B) | >95% | >90% |
| Reference pull success rate (Mode C) | >90% | >80% |
| Cost ceiling compliance | 100% | 100% |
| Execution window feasibility (within tier lead time) | >90% | >75% |

### v1.1 targets (Week 5+)

| Metric | Target |
|--------|--------|
| Latency (avg) | <40s |
| Token cost | <$0.25/plan |
| Resource binding first-attempt success | >95% |
| Auto-promotion rate (Lever 2) | >70% |

---

## §9. Test Cases (5 fixtures — author Day 18 alongside SKILL bundle)

| # | case_id | Tier | Mode | Branch | Purpose |
|---|---------|------|------|--------|---------|
| 1 | case-01-reinvented-pilot-mode-a-shoot-day | Pilot | A | success | Happy path — single shoot day, REINVENTED studio, Jamila talent, low-cost b-roll |
| 2 | case-02-reinvented-pro-mode-b-render-queue | Pro | B | success | Mode B render queue across 2 engines (runway primary + pika fallback), 60s budget |
| 3 | case-03-storyboard-was-error-envelope | n/a | n/a | error→storyboard_not_success | Reject — upstream Storyboard Agent failed |
| 4 | case-04-mode-c-on-pro-tier | Pro | C | error→tier_constraint_violation | Defense-in-depth — Mode C is Enterprise-only |
| 5 | case-05-mode-a-weather-window-violation | Pilot | A | error→weather_window_violation | Mode A primary location is outdoor, forecast says rain — agent must surface, not ship hopeful plan |

---

## §10. Storyboard → Production Plan Field Map (TO DRAFT Day 15 — single source of truth)

Skeleton — Day 15 fills in every row:

| storyboard.json field | production_plan.json destination | Transform |
|-----------------------|-----------------------------------|-----------|
| `storyboard_id` | `storyboard_id` | passthrough (audit trail) |
| `script_id` / `brief_id` | passthrough | audit trail |
| `brand_id` | `brand_id` | passthrough |
| `tier` / `lever` / `production_mode` | passthrough | drives caps |
| `duration_target_seconds` | `duration_target_seconds` | passthrough |
| `shots[]` | input to Mode A/B/C planning | resource binding |
| `shots[*].shot_id` | referenced from Mode-specific plan element | 1:1 binding |
| `shots[*].shot_type` + `camera_movement` + `focal_length_mm` | informs Mode A equipment list / Mode B render hints | translation |
| `shots[*].budget_minutes_est` | sums to `budget_reservation.total_minutes` | aggregation |
| `shots[*].subject` + `setting` | informs Mode A talent/location bookings | resource match |
| `shots[*].setting.no_buildings_rule` | re-validated in Mode A `location_bookings[*].no_buildings_compliant_bool` | enforcement |
| `shots[*].ai_render_hints` | Mode B `render_queue[*].prompt_seed`, `style_token` | passthrough |
| `shots[*].style_replication_hint` | Mode C `reference_pulls[*]` | seed |
| `shots[*].alt_options` | Mode A b-roll alt count | sizing |
| `transitions[]` | informs Edit Agent handoff | passthrough |
| `audio_sync_map` | informs Edit Agent handoff | passthrough |
| `platform_render_specs[]` (canonical: `platform_variants[]`) | `platform_variants[]` | passthrough |
| `metadata` | informs `metadata.parent_chain` | audit trail |

---

## §11. Lever-State Behavior (carried from storyboard; no override)

Same shape as Storyboard SPEC §11. Production Coord inherits, doesn't override.

| lever | Behavior |
|------:|----------|
| 3 | Full output. Human approves every plan before resource commitments. `human_review_required = true`. |
| 2 | Sampled approval. Auto-route unless `qc_warnings` non-empty OR `cost_floor_breach` flagged. |
| 1 | Full autonomy. Auto-route to AI Video Gen / Live Shoot / Style Replication agents. Reviewed weekly. |

---

## §12. Memory Loop (`prior_production_plans`)

When supplied, last 5 plans for the brand are used for:
1. **Vendor rotation.** If same videographer used in last 3 reels → flag `qc_warnings: ["videographer_rotation_recommended"]`. Best-effort, non-blocking.
2. **Engine rotation (Mode B).** If same engine used for shots[0] in last 3 reels → diversify or flag warning.
3. **Cost baseline.** Compare current `budget_reservation.total_cost_usd` against rolling 5-plan median; flag if >2× median (could be tier mismatch).
4. **Lead-time baseline.** Compare current `execution_window` against rolling median; flag if >2× median.

Best-effort, non-blocking. Failures emit qc_warnings, NOT errorEnvelope.

---

## §13. Open Questions (10 — to expand Day 15)

These are Day 12 outline-stage questions. Day 15 SPEC may add more.

1. **Videographer registry source of truth.** Notion table? Airtable? Inline JSON in repo? (Recommend: Notion, queryable via MCP.)
2. **Talent payment model for Pro/Enterprise.** Per-day rate vs. per-reel rate vs. retainer? (Pricing Model 4/25 didn't specify.)
3. **Mode B engine selection algorithm.** Cheapest first? Best-fit by shot type? Round-robin for diversity? (Defer to Week 4 once we have actual quota numbers.)
4. **Mode B style consistency anchor.** Should every reel use the same anchor seed across shots, or per-shot independent seeds? (Storyboard SPEC §13 #3 parked this.)
5. **Mode C IP clearance workflow.** Manual legal review (Linda/Marblism) for every reel, or automated fair-use scoring + escalation? (Defer; Linda agent isn't licensed counsel.)
6. **Weather API source.** OpenWeather / National Weather Service / paid forecasting? (Defer to Day 18 build; default to NWS for free.)
7. **Insurance certificate handling.** Per-shoot certs or umbrella production policy? (Recommend: umbrella, HC-counsel-reviewed; Marblism Linda research first.)
8. **Cost ceiling enforcement strictness.** Hard reject if 1¢ over, or warning at 90% / hard reject at 110%? (Recommend: warning at 90%, hard reject at 100%.)
9. **Multi-mode reels.** Can one reel mix Mode A live + Mode B AI b-roll? (Storyboard implies yes; Production Coord SPEC needs to decide.)
10. **Auto-cancellation policy.** If shoot day weather goes bad <24h before, who decides cancel vs. push? Agent or human? (Recommend: human at Lever 2/3; agent at Lever 1.)

---

## §14. Implementation Plan

| Day | Date | Deliverable |
|-----|------|-------------|
| Day 15 | Mon May 4 | Full SPEC body authored (§§1–17) — replaces this outline |
| Day 16 | Tue May 5 | SPEC review pass + LLM execution prep for Storyboard Agent (Day 13 SKILL ships first) |
| Day 17 | Wed May 6 | Storyboard Agent v1.0 LOCK + Production Coord input schema authoring |
| Day 18 | Thu May 7 | Production Coord SKILL bundle build (10 files, ~75 KB target) |
| Day 19 | Fri May 8 | LLM execution + 5-case test pass |
| Day 20 | Sat May 9 | Production Coord v1.0 LOCK · Week 3 wrap |

**Dependencies that must exist BEFORE Day 18 SKILL bundle build:**
- ✅ Storyboard Agent v1.0 SPEC (Apr 30) — DONE
- ✅ Cross-Spec Consistency Review (May 1) — DONE
- ⬜ Storyboard Agent v1.0 SKILL bundle (Day 13 — Sat May 2)
- ⬜ Storyboard Agent LLM execution + LOCK (Day 15 — Mon May 4)
- ⬜ Production Coord v1.0 SPEC body (Day 15)
- ⬜ Videographer registry (deferred — manual Notion table will do for v1.0)
- ⬜ AI engine quota tracker (deferred — for v1.0, hard-code one engine per Mode B shot)

---

## §15. Critical Decisions to LOCK on Day 15

These shape the v1.0 footprint. List as discussion items for Day 15 authoring session:

1. **Schema is Draft 2020-12** — same as fleet (LOCKED by precedent).
2. **9-step process** — same shape as Brief / Script / Storyboard (LOCKED by precedent).
3. **12-check QC** — same shape as Script / Storyboard (LOCKED by precedent).
4. **Polymorphic input acceptance** — accept successStoryboard or errorEnvelope; runtime branches (LOCKED by precedent).
5. **Defense-in-depth firewall (4th time)** — entity + banned vocab + no-buildings + tier↔mode (LOCKED by precedent).
6. **Mode-specific output sub-schemas** — `mode_a_plan` / `mode_b_plan` / `mode_c_plan` are mutually exclusive (one per plan).
7. **Cost ceiling is HARD-coded by tier in §4** — agent never auto-tunes ceilings (CFO/Bookkeeper concern, not agent concern).
8. **No external API calls in v1.0.** Weather, vendor registry, render quotas are passed in as inputs. Agent doesn't call services. v1.1+ may add MCP wrappers.
9. **No auto-booking in v1.0.** Agent EMITS the plan; human (Lever 3) or orchestrator (Lever 2/1) confirms bookings out-of-band. Reduces blast radius on agent failure.
10. **`production_plan_id` prefix = `productionplan-`** (no abbreviation, per Cross-Spec canon §3.6).
11. **Single-brand v1.0** — REINVENTED only. Multi-brand v1.1+.
12. **Mode A only for v1.0** — Mode B is Week 4 build (SKILL bundle wires Mode B once AI Video Gen Agent ships); Mode C is Week 5. v1.0 SPEC includes Mode B/C schemas but agent emits `mode_b_plan = null` / `mode_c_plan = null` until those agents are LIVE.

---

## §16. Hand-off Preview to Downstream Agents

Production Coord Agent emits successProductionPlan → routes to:

- **AI Video Gen Agent** (Week 4 SPEC target) — receives `mode_b_plan.render_queue[]`; assigns to engine MCPs; emits `rendered_clips.json`.
- **Style Replication Agent** (Week 5 SPEC target) — receives `mode_c_plan.reference_pulls[]` + `style_match_targets[]`; emits `replicated_clips.json`.
- **Live Shoot human handoff** (Mode A) — `mode_a_plan` becomes the call sheet PDF / Notion page; videographer executes; raw footage uploaded to Ingest Agent.
- **Edit Agent** (Week 4 SPEC target) — receives storyboard + script + production_plan + raw clips (any mode); emits `edit_decisions.json`.

Production Coord SPEC §16 will reference each downstream schema once they exist.

---

## §17. Sign-off Table (Outline-Only Status — to-update Day 15)

| Section | Outline Status | Day 15 LOCK Target |
|---------|----------------|---------------------|
| §1 Purpose | INTENT-LOCKED | LOCKED |
| §2 Inputs | OUTLINED | LOCKED |
| §3 Outputs | OUTLINED | LOCKED |
| §4 Tier constraints | DRAFT (placeholder $) | LOCKED |
| §5 9-step process | OUTLINED | LOCKED |
| §6 12-check QC | OUTLINED | LOCKED |
| §7 System prompt | SKELETON | LOCKED |
| §8 Performance targets | OUTLINED | LOCKED |
| §9 Test cases | NAMED | DRAFT (5 fixtures author Day 18) |
| §10 Field map | SKELETON | LOCKED |
| §11 Lever | OUTLINED | LOCKED |
| §12 Memory loop | OUTLINED | LOCKED |
| §13 Open questions | 10 listed | EXPAND or RESOLVE Day 15 |
| §14 Implementation plan | LOCKED | (this won't change) |
| §15 Critical decisions | LISTED | LOCKED |
| §16 Hand-off preview | LOCKED | LOCKED |
| §17 Sign-off | THIS TABLE | LOCKED |

**Outline status: 17 of 17 sections sketched. Day 15 SPEC body authoring = fill-in-the-blanks against this skeleton.**

---

## Provenance

- Authored: 2026-05-01 (Fri · Day 12 · Wk2D6) — ARS overnight build session, stretch goal
- Mirrors: Brief Agent SPEC (Apr 26), Script Agent SPEC (Apr 28), Storyboard Agent SPEC (Apr 30) — same 17-section shape
- Source canon: Cross-Spec Consistency Review (`ARS-2026-05-01-Cross-Spec-Consistency-Review.md`) §3 (canonical naming map)
- Lives at: `/outputs/ars/ARS-2026-05-01-Production-Coord-Agent-SPEC-Outline.md` (mirror to `ars/`)
- No external comms. No financial commitments. Zero entity-boundary violations.

*Production Coord Agent v1.0 SPEC OUTLINE — execution gate of the pipeline. Day 15 authoring expands this skeleton into a LOCKED SPEC. Friday's freed time used for forward planning so Day 15 starts with a full skeleton already in hand.*
