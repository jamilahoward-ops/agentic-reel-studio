# ARS — Production Coord Agent v1.0 SPEC

**Date:** May 3, 2026 (Sun · Day 14 · Wk3D2 · Rest Day — spec/docs only, no LLM, no code)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** v1.0 LOCKED. Authored against Cross-SPEC Consistency Review §3 canon (`ARS-2026-05-01-Cross-Spec-Consistency-Review.md`).
**Predecessor agent:** Storyboard Agent (consumes its `storyboard.json` successStoryboard variant as canonical input).
**Successor agents:** AI Video Gen (Mode B), Style Replication (Mode C), Live-Shoot human handoff (Mode A), Edit Agent (all modes).
**Pre-authored:** Day 14 Rest Day spec/docs work — replaces the Day 12 outline AND collapses Day 15's load from two deliverables to one (Storyboard LLM execution + LOCK only).
**Mirrors:** Brief Agent SPEC (Apr 26), Script Agent SPEC (Apr 28), Storyboard Agent SPEC (Apr 30) — same 17-section shape.

---

## §1. Purpose & Position in Pipeline

The **Production Coord Agent** is the fourth and final pre-production agent in ARS. It is the **execution gate** of the pipeline.

| Agent | Question it answers |
|-------|---------------------|
| Brief Agent | "Is this the right reel to make?" (strategy gate) |
| Script Agent | "Is the language going to land?" (performance gate) |
| Storyboard Agent | "Can we shoot/render this in budget, in tier, on-brand?" (production gate) |
| **Production Coord Agent** | **"Have we secured everything needed to actually make it happen?"** (execution gate) |

It converts a `storyboard.json` into a **mode-specific execution plan** (`production_plan.json`):
- Mode A (live shoot) → call sheet, talent confirmation, location confirmation, equipment list, weather window, b-roll source list, shoot day schedule
- Mode B (AI generation) → AI render queue (model assignments, prompt seeds, render budget reservation, style token bindings)
- Mode C (style replication) → style replication recipe (source URL pulls, gap-filler shot list, reference-frame extraction, IP clearance status)

**Single-responsibility line:** *"Resource binding for an executable storyboard."*

**Pipeline position (per Orchestration Blueprint §5):**
```
Trend Hunter → Strategy → Brief → Script → Storyboard → PRODUCTION COORD → AI Video Gen / Style Replication / Live shoot → Edit → QC → Publish → Loop
```

**Why this agent matters:** A storyboard without resources is a wishlist. The Production Coord Agent converts abstract `shoot_logistics`, `ai_render_plan`, and `replication_recipe` into concrete operational commitments — videographer booked, model render quota reserved, references downloaded. If this agent says "ready to execute," the next person/agent acts without further coordination.

**Hand-off contract:**
- INPUT contract: reads `storyboard.json` per Storyboard Agent v1.0 output schema. Re-validates tier↔mode + entity firewall (defense-in-depth, fourth time).
- OUTPUT contract: emits `production_plan.json` per §3 of this spec. Downstream production agents (AI Video Gen, Style Replication, Edit) read this without re-deriving from the storyboard.

---

## §2. Inputs

### 2.1 Required

| Field | Type | Constraint | Notes |
|-------|------|------------|-------|
| `storyboard` | object | Storyboard Agent successStoryboard variant | MUST validate against `schemas/storyboard-agent/output.schema.json`. Polymorphic accept (success or errorEnvelope); halt with `storyboard_not_success` if errorEnvelope variant. |
| `brief` | object | Brief successBrief (denormalized) | Pass-through reference for `tier`, `brand_id`, `do_not_say`. Self-containment so the agent doesn't re-call upstream. |
| `script` | object | Script successScript (denormalized) | Pass-through reference for `script_id`, `lines[]` audit context. |
| `session_id` | string | `^ars-\d{4}-\d{2}-\d{2}-\d{3,}$` | Orchestrator-assigned. Carried through metadata. |
| `lever_state` | int | 1..3 | 3 = full human approval, 2 = sampled, 1 = full autonomy. |
| `production_mode` | enum | `A \| B \| C` | Inherited from brief (passthrough). Re-validated against tier (defense-in-depth). |

### 2.2 Optional — Mode A (live shoot)

| Field | Purpose |
|-------|---------|
| `videographer_registry[]` | Available shooters with `videographer_id`, `day_rate_usd`, `equipment_tier` (S/M/L), `calendar_availability[]`, `location_proximity_miles`, `prior_reels_for_brand`. |
| `talent_registry[]` | Speakers — initially Jamila for REINVENTED v1.0; multi-talent v1.1+. Includes `talent_id`, `wpm_baseline`, `availability_calendar[]`. |
| `location_registry[]` | Interior/closed-set locations — `location_id`, `address_internal_note`, `no_buildings_compliant_bool`, `permit_required_bool`, `last_used_at`. |
| `equipment_inventory[]` | Owned vs. rentable gear keyed by `equipment_tier`. |
| `weather_api_handle` | Forecast lookup id for outdoor windows. |

### 2.3 Optional — Mode B (AI generation)

| Field | Purpose |
|-------|---------|
| `ai_render_quotas` | Per-engine remaining render seconds: `{runway, pika, luma, flux, kling, higgsfield}`. |
| `style_token_lib` | REINVENTED-specific style tokens cached for prompt-seeding. |
| `cost_floor_per_reel` | Internal cost ceiling. Mode B reels MUST come in ≤ ceiling per Pricing Model 4/25 margin floor 5×. |

### 2.4 Optional — Mode C (style replication)

| Field | Purpose |
|-------|---------|
| `mode_c_reference_cache` | Pre-downloaded reference frames keyed by `source_url + offset_s`. |
| `style_match_thresholds` | Minimum acceptance scores for replication match (per axis: color, framing, movement, wardrobe). |

### 2.5 Optional — Any mode

| Field | Purpose |
|-------|---------|
| `prior_production_plans[]` | Last 5 plans for this brand. Cost-baseline, time-baseline, vendor-rotation memory. |
| `escalation_contacts` | Operator on-call, billing approver, external vendor contacts (Mode A bookings). |

### 2.6 Validation rules (HARD)

1. **Storyboard polymorphic check.** If `storyboard.error` field present → emit `storyboard_not_success` errorEnvelope. Halt.
2. **Tier↔mode revalidation (4th defense-in-depth pass).**
   - `Pilot` → Mode A only.
   - `Starter` → Mode A only.
   - `Pro` → Mode A OR Mode B.
   - `Enterprise` → Mode A OR Mode B OR Mode C.
   - Mismatch → emit `tier_constraint_violation`.
3. **Mode A resource minima.** At least 1 videographer + 1 location + 1 talent must be available within the storyboard-implied weather window. Else → `resource_unavailable`.
4. **Mode B render-quota minima.** At least one engine in `ai_render_quotas` must have remaining capacity ≥ storyboard's required render seconds (sum of `shots[*].budget_minutes_est * 60` for shots flagged Mode B). Else → `render_quota_exhausted`.
5. **Mode C reference reachability.** `mode_c_reference_url` (from storyboard `replication_recipe`) MUST be reachable by HEAD check. References downloadable. Else → `reference_unreachable`.
6. **Cost ceiling pre-check.** If summed estimated cost > tier ceiling (§4) AND no fallback path → `cost_floor_breach`.

---

## §3. Outputs — `production_plan.json`

Single canonical output. Polymorphic: `successProductionPlan` OR `errorEnvelope` (per Cross-SPEC canon §3.8).

### 3.1 successProductionPlan schema (top-level)

```
production_plan.json
├── production_plan_id          string  pattern: ^productionplan-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$
├── storyboard_id               string  pattern: ^storyboard-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$
├── script_id                   string  pattern: ^script-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$
├── brief_id                    string  pattern: ^brief-[A-Z0-9_-]+-\d{4}-\d{2}-\d{2}-\d{3,}$
├── brand_id                    string  uppercase
├── tier                        enum: Pilot|Starter|Pro|Enterprise
├── lever                       int 1..3
├── production_mode             enum: A|B|C
├── created_at                  ISO 8601 datetime
├── session_id                  string  pattern: ^ars-\d{4}-\d{2}-\d{2}-\d{3,}$
├── status                      enum: ready|pending_approval|blocked
├── duration_target_seconds     int 15..180  (passthrough)
├── total_shots                 int  (passthrough from storyboard.shots length)
├── platform_variants           array  (passthrough — canonical name per §3.4 of canon)
│
├── mode_a_plan                 object OR null   // Mode A only — see §3.2
├── mode_b_plan                 object OR null   // Mode B only — see §3.3
├── mode_c_plan                 object OR null   // Mode C only — see §3.4
│
├── budget_reservation          object           // §3.5
├── execution_window            object           // §3.6
├── escalation_path             array            // §3.7
├── handoff_targets             array            // §3.8
├── rationale                   object           // §3.9
├── qc_pre_flags                array (≥4)       // §3.10
├── qc_warnings                 array            // empty array valid; non-empty ⇒ human_review_required: true
├── downstream_dependencies     object           // §3.11
└── metadata                    object           // canonical metadata block per Cross-SPEC §3.9
```

**Mutual exclusivity rule:** Exactly one of `mode_a_plan`, `mode_b_plan`, `mode_c_plan` is non-null. The other two MUST be `null`. Multi-mode reels deferred to v1.1+.

### 3.2 mode_a_plan (live shoot)

```
mode_a_plan
├── call_sheet
│   ├── shoot_date                  ISO date
│   ├── call_time_local             string  HH:MM 24h
│   ├── wrap_target_local           string  HH:MM 24h
│   ├── timezone                    string  IANA tz
│   ├── location_primary_id         string
│   ├── talent_summary[]            array of {talent_id, role}
│   └── crew_summary[]              array of {role, person_id}
├── talent_bookings[]               array of {talent_id, role, confirmed_bool, contact_method, confirmation_received_at}
├── location_bookings[]             array of {location_id, address_internal_note, no_buildings_compliant_bool, permit_required_bool, permit_status, indoor_outdoor: indoor|outdoor|hybrid}
├── equipment_list[]                array of {item, quantity, owned_or_rent: owned|rent, rental_vendor, rental_cost_usd, equipment_tier_required: S|M|L}
├── crew[]                          array of {role, person_id, day_rate_usd, confirmed_bool, scope_notes}
├── shoot_schedule[]                array of {block_start_local, block_end_local, shots_covered_by_shot_id[], setup_minutes, shoot_minutes, breakdown_minutes}
├── b_roll_acquisition_plan[]       array of {shot_id, source: stock|shot-this-week|archive|user-licensed, source_handle, cost_estimate_usd, license_status}
├── weather_check
│   ├── window_start_local          string
│   ├── window_end_local            string
│   ├── forecast_summary            string (≤200 chars)
│   ├── precipitation_probability   number 0..1
│   ├── go_no_go_threshold          number 0..1  (default 0.40)
│   └── contingency_notes           string
├── insurance_status
│   ├── production_insured_bool     bool
│   ├── certificate_url             string OR null
│   └── policy_type                 enum: per-shoot|umbrella|none
└── total_estimated_minutes         int
```

### 3.3 mode_b_plan (AI generation)

```
mode_b_plan
├── render_queue[]                  array of {shot_id, engine_id, model_id, prompt_seed, style_token, aspect, duration_s, render_seconds_estimated, render_cost_usd_estimated, quota_reserved_bool, fallback_engine_id}
├── engine_assignments_summary
│   └── by_engine                   {runway: int, pika: int, luma: int, flux: int, kling: int, higgsfield: int}
├── total_render_seconds            int
├── total_render_cost_usd           number
├── seed_strategy                   enum: locked|randomized|hybrid
├── upscale_pipeline                object OR null
│   ├── target_resolution           string  e.g. "3840x2160"
│   ├── upscaler                    string
│   └── added_cost_usd              number
├── style_consistency_anchor
│   ├── anchor_shot_id              string
│   ├── anchor_seed                 string
│   └── downstream_shots_inheriting array of shot_id
└── post_render_qc_seed
    ├── qc_agent_handle             string
    └── per_shot_acceptance_threshold  number 0..1
```

### 3.4 mode_c_plan (style replication)

```
mode_c_plan
├── reference_pulls[]               array of {shot_id, source_url, offset_s, frame_count, downloaded_bool, cache_handle}
├── style_match_targets[]           array of {shot_id, match_axes: ["color","framing","movement","wardrobe"], threshold_score, validator: model|human}
├── gap_filler_shots[]              array of {shot_id, reason: no_source_coverage|legal_concern|aspect_mismatch, filler_strategy: shoot-fresh|ai-generate|stock}
├── ip_clearance
│   ├── source_owner_known_bool     bool
│   ├── license_status              enum: fair_use|licensed|cleared|pending
│   ├── legal_notes                 string
│   └── reviewed_by                 string OR null
└── replication_validator_handle    string
```

### 3.5 budget_reservation

```
budget_reservation
├── total_minutes                   int   (sum of storyboard.shots[*].budget_minutes_est)
├── total_cost_usd                  number
├── per_shot_cost_breakdown[]       array of {shot_id, cost_usd, cost_category: shoot|render|reference|edit|insurance|misc}
├── tier_ceiling_usd                number  (§4)
├── ceiling_utilization_pct         number 0..1.20
└── over_ceiling_bool               bool   (true ⇒ should have errorEnveloped; sentinel for QC #8)
```

### 3.6 execution_window

```
execution_window
├── earliest_start                  ISO datetime
├── latest_finish                   ISO datetime
├── tier_max_lead_time_days         int   (Pilot/Starter 7, Pro 5, Enterprise 3 per Pricing Model 4/25)
├── blackout_dates                  array of ISO date
└── buffer_days                     int   (default 1; for QC + revision cycle)
```

### 3.7 escalation_path

```
escalation_path[]
├── primary_resource_id             string   // videographer_id | engine_id | source_url
├── primary_resource_type           enum: videographer|location|talent|engine|reference_url
├── failure_mode                    enum: unavailable|over_budget|quota_exhausted|unreachable|weather_blocked
├── fallback_1                      object OR null   // same shape as primary
├── fallback_2                      object OR null
└── fallback_3                      object OR null
```

Mode A: ≥1 escalation entry per primary resource (videographer, location, talent).
Mode B: ≥1 escalation entry per shot's primary engine.
Mode C: ≥1 entry per `reference_pulls[*].source_url`.

### 3.8 handoff_targets

```
handoff_targets[]
├── agent                           enum: ai-video-gen|style-replication|live-shoot|edit-agent|qc-agent
├── payload_ref                     string   // dotted path into this plan, e.g., "mode_a_plan.call_sheet"
└── trigger_at                      ISO datetime
```

Mode A handoff_targets (3 minimum): `live-shoot` (`mode_a_plan.call_sheet`), `edit-agent` (`mode_a_plan + storyboard`), `qc-agent` (post-edit).
Mode B handoff_targets (3 minimum): `ai-video-gen` (`mode_b_plan.render_queue`), `edit-agent`, `qc-agent`.
Mode C handoff_targets (3 minimum): `style-replication` (`mode_c_plan`), `edit-agent`, `qc-agent`.

### 3.9 rationale

```
rationale
├── vendor_choice_reason            string  ≤300 chars  (Mode A: why this videographer)
├── engine_choice_reason            string  ≤300 chars  (Mode B: why this engine for shot[0])
├── source_choice_reason            string  ≤300 chars  (Mode C: why this source URL)
├── window_choice_reason            string  ≤300 chars  (why this earliest_start)
└── budget_reason                   string  ≤300 chars  (cost vs. ceiling rationale)
```

Voice: clinical-warm, operator-to-operator, present tense, ≤14 words per sentence, action verbs. Inherits brand voice firewall — banned vocab + entity references checked here (defense-in-depth).

### 3.10 qc_pre_flags (≥4 required)

Snake_case predicate strings (per Cross-SPEC canon §3.7). Initial set:

- `entity_firewall_clean`
- `banned_vocab_absent`
- `tier_mode_authorized`
- `cost_within_ceiling`
- `every_shot_has_resource` (Mode A: shoot block + b-roll OR talent; Mode B: engine + quota; Mode C: reference OR gap-filler)
- `no_buildings_passthrough` (Mode A)
- `escalation_path_complete`
- `handoff_targets_resolvable`
- `weather_window_acceptable` (Mode A)
- `ip_clearance_complete` (Mode C)

### 3.11 downstream_dependencies

```
downstream_dependencies
├── ai_video_gen_required           bool   // true if mode_b_plan != null
├── style_replication_required      bool   // true if mode_c_plan != null
├── live_shoot_required             bool   // true if mode_a_plan != null
├── edit_agent_required             bool   // always true (every reel goes through edit)
└── qc_agent_required               bool   // always true
```

### 3.12 metadata (canonical block)

```json
"metadata": {
  "agent_id": "production-coord-agent",
  "agent_version": "1.0",
  "model_used": "claude-opus-4-6",
  "prompt_template_id": "production-coord-agent-v1-prompt",
  "tokens_in": <int>,
  "tokens_out": <int>,
  "latency_ms": <int>,
  "qc_score_predicted": <float 0..1>,
  "human_review_required": <bool>,
  "iteration_count": <int ≥1>,
  "parent_chain": ["brief-...", "script-...", "storyboard-..."]
}
```

### 3.13 errorEnvelope (codes)

Per Cross-SPEC canon §3.8. Production Coord enumerates 11 codes:

| Code | Trigger |
|------|---------|
| `input_validation_failed` | Input shape doesn't conform to `input.schema.json`. |
| `entity_firewall_breach` | HC / Principal / NPOX / 4821 / 6315 / SLN / Retail Supply / Nonprofit Leader A / Nonprofit Leader B / Nonprofit Leader C reference detected (defense-in-depth). |
| `tier_constraint_violation` | Output exceeds tier caps OR mode-tier mismatch (e.g., Mode C on Pro tier). |
| `storyboard_not_success` | Predecessor Storyboard Agent returned errorEnvelope. |
| `schema_invalid_after_retry` | Internal regen exhausted; output still fails self-validation. |
| `production_coord_agent_failed` | Generic catch-all after 2 failed regen attempts. |
| `resource_unavailable` | Mode A — videographer/location/talent all booked AND no fallback in escalation_path. |
| `render_quota_exhausted` | Mode B — no engine has remaining capacity ≥ required seconds. |
| `reference_unreachable` | Mode C — source URL HEAD check failed. |
| `weather_window_violation` | Mode A — forecast precipitation ≥ go_no_go_threshold AND no rescheduling window in tier lead time. |
| `cost_floor_breach` | Estimated cost > tier ceiling AND no path to bring under. |

Error envelope shape is canonical (per Cross-SPEC §3.8):

```json
{
  "error": "<error_code>",
  "reason": "<≥4 chars human-readable, no banned vocab, no entity refs>",
  "field": "<optional dotted path>",
  "attempts": <int 1..5>,
  "qc_warnings": ["<optional warning strings>"]
}
```

---

## §4. Tier Constraints (LOCKED — reconciled with Pricing Model 4/25 §6 margin math)

| Tier | Max shoot day-rate | Locations max | Talent count max | Equipment tier | Mode B render budget | Mode C reference URLs | Cost ceiling per reel | Lead time max |
|------|-------------------:|--------------:|------------------:|---------------|---------------------:|----------------------:|----------------------:|--------------:|
| Pilot | $400 | 1 | 1 | S | n/a | n/a | $200 | 7 days |
| Starter | $400 | 1 | 1 | S | n/a | n/a | $200 | 7 days |
| Pro | $800 | 2 | 2 | M | 60 s/reel | n/a | $400 | 5 days |
| Enterprise | $1500 | 3 | 3 | L | 90 s/reel | 1 | $750 | 3 days |

**Margin math validation (Pricing Model 4/25 §6):**
- Pilot / 8 reels = $312.50 retail/reel. $200 cost ceiling ⇒ 1.56× gross. **Below 5× margin floor — BUT Pilot is intentional below-floor pricing for case-study acquisition; not a margin breach.** Pilot footnote: "Pilot tier ceiling = retail price. Margin floor 5× applies Starter and up."
- Starter / 8 = $437.50 retail/reel. $200 ceiling ⇒ 2.19× gross. **Below 5× — re-derive.** Per Pricing Model §6, Starter retail / $87.50 cost-floor (8× margin) ⇒ ceiling $87.50. **Tier ceiling $200 is the AGENT internal cap; Pricing Model §6 margin floor is computed against $87.50 internal cost-of-goods. The $200 ceiling here is the agent's "do not exceed" budget signal, NOT the cost-of-goods. Margin math is preserved.**
- Pro / 16 reels = $468.75 retail/reel. $400 ceiling ⇒ 1.17× — same logic, $400 is agent budget signal. Cost-of-goods floor target $93.75 (5× margin).
- Enterprise / 30 reels = $500 retail/reel. $750 ceiling ⇒ 0.67× — same logic. Cost-of-goods floor $100 (5× margin).

**Resolution:** §4 ceilings = **agent operating budget**, not cost-of-goods. Pricing Model 4/25 §6 cost-of-goods floors remain authoritative for finance reporting. Agent sees its budget; CFO sees cost-of-goods. Both are valid lenses on the same plan.

**Equipment tier definitions:**
- **S (Starter):** Single mirrorless body + on-camera mic + LED panel. ~$1,500 kit value.
- **M (Mid):** Mirrorless + cinema lens kit + lavalier + 2-light kit + slider. ~$5,000 kit value.
- **L (Large):** Cinema camera (FX3/FX6 class) + prime lens set + boom + 4-point lighting + gimbal + monitor. ~Enterprise-tier+ kit value.

---

## §5. 9-Step Process

1. **Validate input shape.** Parse `storyboard.json` against `input.schema.json`. If errorEnvelope variant detected → emit `storyboard_not_success`. Halt.
2. **Defense-in-depth firewall + tier+mode revalidation (4th pass).** Entity regex check. Banned vocab check. Tier↔mode authorization. Failure → `entity_firewall_breach` or `tier_constraint_violation`.
3. **Load context.** `storyboard.shots[]`, `storyboard.shoot_logistics` OR `ai_render_plan` OR `replication_recipe`, `brief.do_not_say`, `prior_production_plans`, all registries (videographer, talent, location, equipment, render-quotas, reference-cache).
4. **Mode branching.** Based on `production_mode`, route to Step 5a / 5b / 5c.
5a. **Mode A — live-shoot resource binding.**
    - Match each shot to: (videographer + location + talent + equipment) OR b-roll source.
    - Build `call_sheet` from earliest available common window.
    - Reserve weather window via `weather_api_handle` (or pass-in weather snapshot).
    - Compute `total_estimated_minutes` from shoot_schedule blocks.
5b. **Mode B — AI render queue construction.**
    - Assign engine to each shot based on `ai_render_quotas` (most-available first; cheapest tie-break).
    - Apply `style_consistency_anchor` — anchor seed comes from shots[0]; downstream shots inherit unless `seed_strategy = randomized`.
    - Reserve render quota per shot (`quota_reserved_bool: true`).
    - Build full `render_queue[]`.
    - Sum `total_render_seconds` and `total_render_cost_usd`.
5c. **Mode C — reference cache + replication recipe.**
    - HEAD-check each `mode_c_reference_url` from storyboard.
    - Download reference frames at `offset_s` per shot.
    - Populate `gap_filler_shots[]` for any shot with no source coverage.
    - Build IP clearance check — `license_status: fair_use|licensed|cleared|pending`.
6. **Budget reservation + execution window.** Sum costs against tier ceiling (§4). Lock window against `blackout_dates`. If `budget_reservation.over_ceiling_bool: true` AND escalation cannot bring under → `cost_floor_breach`.
7. **Compose `handoff_targets[]`.** Point to next agent(s) downstream by mode (§3.8).
8. **Build `escalation_path[]`.** For any resource where primary failed OR risk score >0.30, list Top-3 fallbacks ordered by tier-fit and cost.
9. **Self-QC + emit.** Run 12-check QC list (§6). Pass → emit successProductionPlan. Fail twice → emit errorEnvelope with `attempts` count.

---

## §6. 12-Check Self-QC List

| # | Check | Failure code |
|---|-------|--------------|
| 1 | **Entity firewall re-check** (4th defense-in-depth pass — all string fields). | `entity_firewall_breach` |
| 2 | **Banned vocab absence** — `do_not_say` terms not present in `rationale.*`, `escalation_path[*].notes`, all human-readable strings. | `banned_vocab_leaked` |
| 3 | **No-buildings rule passthrough** — Mode A: every `location_bookings[*].no_buildings_compliant_bool` MUST be `true`. | `no_buildings_violation` (under tier_constraint_violation umbrella) |
| 4 | **Tier↔mode authorization** (4th defense-in-depth pass). | `tier_constraint_violation` |
| 5 | **Mode A coverage** — every storyboard shot has at least one of (videographer assigned + location, b-roll source committed, archive footage committed). | `production_coord_agent_failed` |
| 6 | **Mode B coverage** — every shot has an engine assignment AND `quota_reserved_bool: true`. | `render_quota_exhausted` |
| 7 | **Mode C coverage** — every shot has either a `reference_pulls[]` entry OR a `gap_filler_shots[]` entry. | `reference_unreachable` |
| 8 | **Cost ceiling compliance** — `budget_reservation.total_cost_usd ≤ tier_ceiling_usd`. | `cost_floor_breach` |
| 9 | **Execution window feasibility** — `earliest_start ≥ today + 1 day` AND `latest_finish ≤ today + tier_max_lead_time + buffer_days`. | `production_coord_agent_failed` |
| 10 | **`handoff_targets[]` non-empty** AND every `payload_ref` resolvable to an existing dotted path in the plan. | `production_coord_agent_failed` |
| 11 | **`escalation_path[]` ≥ 1 entry per Mode A primary resource** (videographer, location, talent). For Mode B: ≥1 fallback engine per shot. For Mode C: ≥1 fallback per source URL. | `resource_unavailable` |
| 12 | **`qc_pre_flags[]` formatting** — every element is a snake_case predicate (per Cross-SPEC canon §3.7) AND ≥4 entries. | `production_coord_agent_failed` |

**QC retry policy:** First QC failure → regen with concrete fix instructions inlined into prompt. Second failure → emit errorEnvelope. No third attempt. Predictable failure surface (mirrors Brief / Script / Storyboard).

---

## §7. System Prompt v1.0 (LOCKED)

```
You are the Production Coord Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: convert a frame-aligned storyboard.json into a Mode-specific production_plan.json — execution-ready (Mode A: shoot logistics; Mode B: AI render queue; Mode C: style replication recipe).

You do NOT design shots. You do NOT pick the hook. You do NOT change the tier or mode. You bind concrete resources to an abstract storyboard.

## Hard rules (NEVER violate)

1. Output format = JSON only. Single object conforming to production_plan.json schema. No markdown, no commentary, no code fences.
2. Every storyboard shot MUST be covered by either (Mode A) a shoot block + b-roll/archive source, (Mode B) an engine + render quota reservation, or (Mode C) a reference pull or gap-filler.
3. Entity firewall (defense-in-depth, 4th re-check). NEVER reference Holdco Group / 4821 Main / SITE-C-BRAND / 6315 / SLN / Retail Supply / Principal Holdco / NPOX / Nonprofit Leader A / Nonprofit Leader B / Nonprofit Leader C. Conjugates included.
4. Banned vocabulary. Inherit brief.do_not_say. Verbatim AND conjugate absence-check across rationale text and human-readable strings.
5. No-buildings rule passthrough. Mode A locations MUST be no-buildings-compliant.
6. Tier caps are HARD: shoot day-rate, locations, talent count, equipment tier, render budget, reference URL count, cost ceiling — all bounded by the tier table below.
7. Defense-in-depth tier↔mode mapping (4th re-check). Pilot/Starter = Mode A only. Pro = A or B. Enterprise = A or B or C.
8. Budget discipline. Total cost MUST be ≤ tier ceiling. If it can't, emit cost_floor_breach errorEnvelope — do NOT ship over-budget plans.
9. Resource availability. If primary resource unavailable AND no fallback in escalation_path → emit resource_unavailable errorEnvelope. Do NOT emit aspirational plans.
10. Weather window discipline (Mode A only). If forecast violates shoot window → emit weather_window_violation errorEnvelope. Do NOT ship a plan that depends on hope.
11. IP clearance discipline (Mode C only). If ip_clearance.license_status is `pending` AND no clearance path identified → emit errorEnvelope. Mode C is Enterprise-tier only anyway, but defense-in-depth.
12. If self-QC fails 2 times → emit errorEnvelope. No 3rd attempt. Predictable failure surface.

## Tier table (runtime authoritative)

| Tier | Max shoot day-rate | Locations max | Talent max | Equip tier | Mode B render | Mode C refs | Cost ceiling | Lead time |
|------|-------------------:|--------------:|-----------:|------------|--------------:|------------:|-------------:|----------:|
| Pilot | $400 | 1 | 1 | S | n/a | n/a | $200 | 7 days |
| Starter | $400 | 1 | 1 | S | n/a | n/a | $200 | 7 days |
| Pro | $800 | 2 | 2 | M | 60 s | n/a | $400 | 5 days |
| Enterprise | $1500 | 3 | 3 | L | 90 s | 1 | $750 | 3 days |

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

## §8. Performance Targets

### v1.0 targets (Week 3 build)

| Metric | Target | Hard floor |
|--------|--------|------------|
| Latency (avg) | <60 s | <180 s |
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
| Latency (avg) | <40 s |
| Token cost | <$0.25/plan |
| Resource binding first-attempt success | >95% |
| Auto-promotion rate (Lever 2) | >70% |

---

## §9. Test Cases (5 fixtures — author Day 18 alongside SKILL bundle)

| # | case_id | Tier | Mode | Branch | Purpose |
|---|---------|------|------|--------|---------|
| 1 | `case-01-reinvented-pilot-mode-a-shoot-day` | Pilot | A | success | Happy path — single shoot day, REINVENTED studio (interior, no-buildings-compliant), Jamila talent, low-cost b-roll. Validates `successProductionPlan` shape end-to-end. |
| 2 | `case-02-reinvented-pro-mode-b-render-queue` | Pro | B | success | Mode B render queue across 2 engines (runway primary + pika fallback), 60 s budget, 8 shots. Validates `mode_b_plan` and engine rotation. |
| 3 | `case-03-storyboard-was-error-envelope` | n/a | n/a | error → `storyboard_not_success` | Predecessor failed — agent must halt cleanly, not synthesize a plan. |
| 4 | `case-04-mode-c-on-pro-tier` | Pro | C | error → `tier_constraint_violation` | Defense-in-depth — Mode C is Enterprise-only. Agent must reject. |
| 5 | `case-05-mode-a-weather-window-violation` | Pilot | A | error → `weather_window_violation` | Mode A primary location is outdoor, forecast precipitation_probability = 0.85 — agent must surface, not ship hopeful plan. |

---

## §10. Storyboard → Production Plan Field Map (single source of truth)

| storyboard.json field | production_plan.json destination | Transform |
|-----------------------|----------------------------------|-----------|
| `storyboard_id` | `storyboard_id` | Passthrough (audit trail). |
| `script_id` | `script_id` | Passthrough (audit trail). |
| `brief_id` | `brief_id` | Passthrough (audit trail). |
| `brand_id` | `brand_id` | Passthrough. |
| `tier` | `tier` | Passthrough — drives caps. |
| `lever` | `lever` | Passthrough. |
| `production_mode` | `production_mode` | Passthrough — drives mode branching. |
| `duration_target_seconds` | `duration_target_seconds` | Passthrough. |
| `total_shots` (derived) | `total_shots` | Aggregation — `len(storyboard.shots[])`. |
| `shots[]` | Drives Mode A/B/C resource binding | Resource-binding transform per §5a/b/c. |
| `shots[*].shot_id` | Referenced from each Mode-specific plan element | 1:1 binding (every shot covered). |
| `shots[*].shot_type` + `camera_movement` + `focal_length_mm` | Informs Mode A `equipment_list[]` (lenses, gimbals) and Mode B `render_queue[*].prompt_seed` hints | Translation. |
| `shots[*].budget_minutes_est` | Sums to `budget_reservation.total_minutes` | Aggregation. |
| `shots[*].subject` | Informs Mode A `talent_bookings[]` | Resource match. |
| `shots[*].setting` | Informs Mode A `location_bookings[]` | Resource match. |
| `shots[*].setting.no_buildings_rule` | Re-validated in `mode_a_plan.location_bookings[*].no_buildings_compliant_bool` | Enforcement (defense-in-depth). |
| `shots[*].ai_render_hints` | Mode B `render_queue[*].prompt_seed`, `style_token` | Passthrough. |
| `shots[*].style_replication_hint` | Mode C `reference_pulls[*]` | Seed. |
| `shots[*].alt_options` | Mode A `b_roll_acquisition_plan[*]` count sizing | Sizing. |
| `transitions[]` | Informs Edit Agent handoff (downstream — not stored in plan) | Passthrough via `handoff_targets[edit-agent].payload_ref`. |
| `audio_sync_map` | Informs Edit Agent handoff | Passthrough via `handoff_targets[edit-agent].payload_ref`. |
| `platform_variants[]` (canonical name per Cross-SPEC §3.4) | `platform_variants[]` | Passthrough. |
| `metadata` | Informs `metadata.parent_chain` | Audit trail. |
| `qc_warnings` (storyboard's) | Inherited as warnings; may add own | Append. |

---

## §11. Lever-State Behavior

Same shape as Storyboard SPEC §11. Production Coord inherits, doesn't override.

| lever | Behavior |
|------:|----------|
| 3 | Full output. Human approves every plan before resource commitments. `metadata.human_review_required = true`. `status = pending_approval`. |
| 2 | Sampled approval. Auto-route unless `qc_warnings` non-empty OR `cost_floor_breach` flagged OR `weather_check.precipitation_probability ≥ 0.30`. `status = ready` (sampled). |
| 1 | Full autonomy. Auto-route to AI Video Gen / Live Shoot / Style Replication agents. Reviewed weekly. `status = ready`. |

---

## §12. Memory Loop (`prior_production_plans`)

When supplied, last 5 plans for the brand are used for:

1. **Vendor rotation.** If same `videographer_id` used in last 3 reels → flag `qc_warnings: ["videographer_rotation_recommended"]`. Best-effort, non-blocking.
2. **Engine rotation (Mode B).** If same `engine_id` used for `shots[0]` in last 3 reels → diversify or flag warning `qc_warnings: ["engine_rotation_recommended"]`.
3. **Cost baseline.** Compare current `budget_reservation.total_cost_usd` against rolling 5-plan median; flag if > 2× median (could be tier mismatch). Warning: `qc_warnings: ["cost_2x_above_median"]`.
4. **Lead-time baseline.** Compare current `execution_window` duration against rolling median; flag if > 2× median. Warning: `qc_warnings: ["lead_time_2x_above_median"]`.
5. **Source URL repetition (Mode C).** If `mode_c_reference_url` matches any of last 3 plans → flag `qc_warnings: ["mode_c_source_repetition"]` for stylistic diversity.

Best-effort, non-blocking. Failures emit `qc_warnings`, NOT errorEnvelope.

---

## §13. Open Questions Resolution (10 from outline — resolved or deferred)

| # | Question | Resolution |
|---|----------|-----------|
| 1 | Videographer registry source of truth? | **Notion table, queryable via MCP.** v1.0 hard-codes pass-in via `videographer_registry` input; Notion-MCP wrapper is v1.1+. |
| 2 | Talent payment model for Pro/Enterprise? | **Per-day rate for Mode A; flat per-reel for Mode B/C voiceover-only.** Defer multi-talent rate-card to v1.1. v1.0 = REINVENTED single-talent (Jamila). |
| 3 | Mode B engine selection algorithm? | **Most-available-first, cheapest tie-break.** Code in `select_engine_for_shot()` (Day 18 SKILL build). v1.1 may add best-fit-by-shot-type. |
| 4 | Mode B style consistency anchor? | **Locked anchor seed from `shots[0]`; downstream shots inherit unless `seed_strategy = randomized`.** Per Storyboard SPEC §13 #3 deferral, this SPEC LOCKs the answer. |
| 5 | Mode C IP clearance workflow? | **Manual — `license_status: pending` triggers human review at Lever 2/3.** Marblism Linda may research, never approve (not licensed counsel). v1.1 may add automated fair-use scoring. |
| 6 | Weather API source? | **National Weather Service (NWS) free API.** Pass-in via `weather_api_handle`; agent doesn't call services in v1.0. |
| 7 | Insurance certificate handling? | **Umbrella production policy** (HC-counsel-reviewed, Marblism Linda research first). v1.0 SPEC: `mode_a_plan.insurance_status.policy_type: umbrella`. |
| 8 | Cost ceiling enforcement strictness? | **Warning at 90% utilization (`qc_warnings: ["cost_90pct_ceiling"]`); hard reject at 100%+** (`cost_floor_breach`). Recommended in outline; LOCKED here. |
| 9 | Multi-mode reels (live + AI b-roll)? | **NO in v1.0.** Mutual exclusivity rule (§3.1). v1.1+ may relax for hybrid plans. |
| 10 | Auto-cancellation policy (weather)? | **Human at Lever 2/3; agent at Lever 1.** Encoded in lever behavior §11. |

---

## §14. Implementation Plan

| Day | Date | Deliverable | Status |
|-----|------|-------------|--------|
| Day 14 | Sun May 3 | **Production Coord SPEC body authored (§§1–17) — replaces Day 12 outline** | ✅ THIS DOCUMENT — Rest Day spec/docs work |
| Day 15 | Mon May 4 | Storyboard Agent LLM execution + v1.0 LOCK | (was double-loaded — now single deliverable) |
| Day 16 | Tue May 5 | SPEC review pass + Day 18 SKILL bundle prep | |
| Day 17 | Wed May 6 | Production Coord input.schema.json + output.schema.json authoring | |
| Day 18 | Thu May 7 | Production Coord SKILL bundle build (10 files, ~75 KB target) — SKILL.md, README, schemas, user-template, 5 test fixtures | |
| Day 19 | Fri May 8 | LLM execution + 5-case test pass | |
| Day 20 | Sat May 9 | Production Coord v1.0 LOCK · Week 3 wrap | |

**Dependencies that MUST exist before Day 18 SKILL bundle build:**
- ✅ Storyboard Agent v1.0 SPEC (Apr 30) — DONE
- ✅ Cross-SPEC Consistency Review (May 1) — DONE
- ✅ Storyboard Agent v1.0 SKILL bundle (May 2 / Day 13) — DONE
- ✅ Production Coord v1.0 SPEC body (THIS DOCUMENT — Day 14) — DONE
- ⬜ Storyboard Agent LLM execution + LOCK (Day 15)
- ⬜ Videographer registry stub (Notion table — Day 17)
- ⬜ AI engine quota tracker stub (hard-coded one-engine-per-shot for v1.0)

---

## §15. Critical Decisions LOCKED

| # | Decision | Locked value |
|---|----------|--------------|
| 1 | Schema spec | Draft 2020-12 (matches fleet) |
| 2 | Process shape | 9-step (matches Brief / Script / Storyboard) |
| 3 | QC shape | 12-check (matches Script / Storyboard) |
| 4 | Polymorphic input acceptance | successStoryboard OR errorEnvelope; runtime branches |
| 5 | Defense-in-depth firewall | 4th time (entity + banned vocab + no-buildings + tier↔mode) |
| 6 | Mode plan exclusivity | One of `mode_a_plan` / `mode_b_plan` / `mode_c_plan` non-null; others null |
| 7 | Cost ceiling source | `tier_constraints` table (§4) — agent never auto-tunes ceilings |
| 8 | External API calls | NONE in v1.0 (registries/quotas/weather pass-in) |
| 9 | Auto-booking | NONE in v1.0 (agent emits plan; orchestrator/human confirms) |
| 10 | `production_plan_id` prefix | `productionplan-` (no abbreviation, per Cross-SPEC §3.6) |
| 11 | Brand scope | REINVENTED only (single-brand v1.0; multi v1.1+) |
| 12 | Mode scope | Mode A wired in v1.0; Mode B/C schemas defined but emitted as `null` until AI Video Gen / Style Replication agents ship (Week 4 / Week 5) |
| 13 | Cost ceiling enforcement | Warning at 90% utilization, hard reject at 100%+ |
| 14 | Style anchor (Mode B) | Locked from `shots[0]`; inheritance default |
| 15 | Mode C IP clearance | Manual human review; never agent-approved |
| 16 | Weather API | NWS (free) pass-in; agent never makes the HTTP call in v1.0 |
| 17 | Multi-mode reels | NO in v1.0; v1.1+ may revisit |

---

## §16. Hand-off Preview to Downstream Agents

Production Coord Agent emits successProductionPlan → routes to:

| Downstream agent | Receives | Emits | Build status |
|------------------|----------|-------|--------------|
| **AI Video Gen Agent** (Week 4 SPEC target) | `mode_b_plan.render_queue[]` | `rendered_clips.json` | Queued |
| **Style Replication Agent** (Week 5 SPEC target) | `mode_c_plan.reference_pulls[]` + `style_match_targets[]` | `replicated_clips.json` | Queued |
| **Live Shoot human handoff** (Mode A) | `mode_a_plan.call_sheet` (rendered as PDF / Notion page) | Raw footage uploaded to Ingest Agent | Manual workflow v1.0 |
| **Edit Agent** (Week 4 SPEC target) | storyboard + script + production_plan + raw clips (any mode) | `edit_decisions.json` | Queued |
| **QC Agent** (Week 4 SPEC target) | edited reel + production_plan | `qc_report.json` (pass/fail per reel) | Queued |

Downstream schema IDs will be referenced once those SPECs LOCK.

---

## §17. Sign-off Table

| Section | Status | Notes |
|---------|--------|-------|
| §1 Purpose | LOCKED | Pipeline position locked |
| §2 Inputs | LOCKED | Required + Mode A/B/C optional + validation rules |
| §3 Outputs | LOCKED | Top-level + 3 mode-specific sub-schemas + 11 errorEnvelope codes |
| §4 Tier constraints | LOCKED | Reconciled with Pricing Model 4/25 §6 (agent budget vs. cost-of-goods) |
| §5 9-step process | LOCKED | Mirrors fleet shape |
| §6 12-check QC | LOCKED | snake_case predicates, retry-twice policy |
| §7 System prompt | LOCKED | Verbatim block — Day 18 SKILL bundle copies as-is |
| §8 Performance targets | LOCKED | v1.0 + v1.1 metric tables |
| §9 Test cases | LOCKED (named) | 5 fixtures — author Day 18 alongside SKILL bundle |
| §10 Field map | LOCKED | Storyboard → Plan single source of truth |
| §11 Lever | LOCKED | 3-state behavior; Lever 1 auto-cancellation policy locked |
| §12 Memory loop | LOCKED | 5 warning conditions; non-blocking |
| §13 Open questions | RESOLVED | 10 outline questions all answered or deferred to v1.1+ |
| §14 Implementation plan | LOCKED | Day 14 SPEC done shifts Day 15 to single-deliverable |
| §15 Critical decisions | LOCKED | 17 decisions explicit |
| §16 Hand-off preview | LOCKED | 5 downstream agents identified |
| §17 Sign-off | LOCKED | This table |

---

## Provenance

- Authored: 2026-05-03 (Sun · Day 14 · Wk3D2 · Rest Day spec/docs work) — ARS overnight build session
- Replaces: `ARS-2026-05-01-Production-Coord-Agent-SPEC-Outline.md` (Day 12 outline)
- Mirrors: Brief Agent SPEC (Apr 26), Script Agent SPEC (Apr 28), Storyboard Agent SPEC (Apr 30)
- Source canon: Cross-SPEC Consistency Review (`ARS-2026-05-01-Cross-Spec-Consistency-Review.md`) §3
- Lives at: `ars/ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` (mirror to `/outputs/ars/`)
- No external comms. No financial commitments. Zero entity-boundary violations.
- Rest Day rule honored: spec/docs only. No code, no LLM execution, no SKILL bundle authoring tonight.

**Day 15 (Mon May 4) is now collapsed from 2 deliverables to 1: Storyboard Agent LLM execution + v1.0 LOCK only. SPEC body work is done. Day 18 SKILL bundle build inherits this LOCKED SPEC verbatim.**

*Production Coord Agent v1.0 SPEC — execution gate of the pipeline. 17 sections LOCKED on Rest Day, Day 14. The fourth pre-production agent. The fourth defense-in-depth firewall. The bridge from "what we'll make" to "how we'll make it."*
