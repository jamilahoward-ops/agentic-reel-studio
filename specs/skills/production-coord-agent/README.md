# Production Coord Agent — README (v1.0)

Human invocation guide for the **fourth pre-production agent** in the Agentic Reel Studio pipeline.

> **Built:** Thu May 7, 2026 (Day 18 · Wk3D6) · Sequel Digital — ARS
> **SPEC:** `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` (LOCKED Day 14 Rest Day)
> **Schemas:** Day 17 (May 6) LOCKED + self-validating (Draft 2020-12)
> **LLM lock target:** Day 19 (Fri May 8) — 5-case test pass

---

## What this skill does

Converts a frame-aligned `storyboard.json` from the Storyboard Agent into a **mode-specific, execution-ready `production_plan.json`** that downstream production agents (or a human videographer for Mode A) can act against without further coordination.

Single-responsibility line: *"Resource binding for an executable storyboard."*

---

## Pipeline position

```
Trend Hunter → Strategy → Brief → Script → Storyboard → PRODUCTION COORD → AI Video Gen / Style Replication / Live Shoot → Edit → QC → Publish → Loop
```

Production Coord is the **execution gate** and the **4th defense-in-depth firewall** (Brief sets, Script re-validates, Storyboard re-validates, Production Coord re-validates entity / banned-vocab / no-buildings / tier↔mode).

---

## When to invoke

- A storyboard is ready and you need to bind concrete resources before downstream production runs.
- A previous plan was rejected by a downstream agent (`production_plan_schema_mismatch`) — re-run with refreshed registries.
- An operator wants to refresh a plan against the same storyboard with new availability data.

**Do NOT invoke when** the upstream Storyboard Agent emitted an errorEnvelope — the agent will halt at Step 1 with `storyboard_not_success` and synthesize nothing.

---

## Inputs (required + optional)

**Required:**

```
storyboard         storyboard-agent successStoryboard OR errorEnvelope
brief              brief-agent successBrief (denormalized passthrough)
script             script-agent successScript (denormalized passthrough)
session_id         "ars-YYYY-MM-DD-NNN"
lever_state        1 | 2 | 3
production_mode    "A" | "B" | "C"
```

**Mode A optional:** `videographer_registry`, `talent_registry`, `location_registry`, `equipment_inventory`, `weather_api_handle`.

**Mode B optional:** `ai_render_quotas`, `style_token_lib`, `cost_floor_per_reel`.

**Mode C optional:** `mode_c_reference_cache`, `style_match_thresholds`.

**Any-mode optional:** `prior_production_plans` (last 5), `escalation_contacts`.

Full validation rules in `schemas/input.schema.json` (Draft 2020-12).

---

## Outputs

Single `production_plan.json` object. Polymorphic top-level:

- **successProductionPlan** — full plan with one of `mode_a_plan` / `mode_b_plan` / `mode_c_plan` populated, others `null`.
- **errorEnvelope** — `{ error, reason, field, attempts, qc_warnings }`.

Mutual exclusivity is enforced in the output schema via `allOf → oneOf` 3-branch (Mode A / B / C).

11 error codes:

```
input_validation_failed       entity_firewall_breach
tier_constraint_violation     storyboard_not_success
schema_invalid_after_retry    production_coord_agent_failed
resource_unavailable          render_quota_exhausted
reference_unreachable         weather_window_violation
cost_floor_breach
```

---

## Quick-start invocation

1. **Confirm prerequisites:**
   - Storyboard Agent v1.0 SKILL bundle is live and produced a `successStoryboard`.
   - Brief + Script Agents emitted successful predecessors (passthroughs available).
   - Tier↔mode pair is authorized (Pilot/Starter = A only, Pro = A or B, Enterprise = A or B or C).

2. **Build the input object** using `prompts/user-template.txt`. Every required field present, registries scoped to the chosen mode.

3. **Validate input** before LLM execution (saves Opus tokens):

   ```bash
   python3 -c "
   import json
   from jsonschema import Draft202012Validator
   schema = json.load(open('schemas/input.schema.json'))
   data = json.load(open('test-cases/case-01-reinvented-pilot-mode-a-shoot-day.json'))['input']
   Draft202012Validator(schema).validate(data)
   print('OK')
   "
   ```

4. **Invoke the agent** with the system prompt from `SKILL.md` (verbatim — do NOT paraphrase) and the input as a JSON-only user message.

5. **Validate the output** against `schemas/output.schema.json`. Reject any output that fails self-validation.

6. **Route per `handoff_targets[]`** to AI Video Gen / Style Replication / Live Shoot / Edit / QC.

---

## File map

```
production-coord-agent/
  SKILL.md                              ← system prompt verbatim (run this)
  README.md                             ← THIS FILE
  prompts/
    user-template.txt                   ← user-message template (fill + paste)
  schemas/
    input.schema.json                   ← Day 17 LOCKED self-validating
    output.schema.json                  ← Day 17 LOCKED self-validating
  test-cases/
    case-01-reinvented-pilot-mode-a-shoot-day.json    ← happy Mode A
    case-02-reinvented-pro-mode-b-render-queue.json   ← happy Mode B
    case-03-storyboard-was-error-envelope.json        ← storyboard_not_success
    case-04-cost-floor-breach.json                    ← cost_floor_breach
    case-05-resource-unavailable.json                 ← resource_unavailable
```

---

## 5 test fixtures (Day 18)

| # | Tier | Mode | Branch | Expected error |
|---|------|------|--------|----------------|
| 1 | Pilot | A | success | n/a — happy path |
| 2 | Pro | B | success | n/a — happy path |
| 3 | n/a | n/a | error | `storyboard_not_success` |
| 4 | Pilot | A | error | `cost_floor_breach` |
| 5 | Pilot | A | error | `resource_unavailable` |

All 5 input objects validate against `schemas/input.schema.json` before LLM execution. Fixtures run on Day 19 (Fri May 8) for v1.0 LOCK.

---

## Common gotchas

- **Polymorphic storyboard accept.** If `storyboard.error` is present, agent halts immediately with `storyboard_not_success` — do NOT attempt to read `storyboard.shots`.
- **Mutual exclusivity (Mode A/B/C).** Exactly one mode plan non-null. Output schema rejects mismatch via `allOf → oneOf` 3-branch.
- **Tier↔mode is 4th defense-in-depth pass.** Pilot/Starter Mode B/C → reject. Pro Mode C → reject. Defense-in-depth is the point.
- **No-buildings rule (Mode A).** Every `location_bookings[*].no_buildings_compliant_bool` MUST be `true`. Brand visual rule per CLAUDE.md 4/22/26.
- **Cost ceiling = agent operating budget.** Pricing Model 4/25 §6 cost-of-goods floors are the CFO lens. SPEC §4 ceilings are the agent's "do not exceed" budget signal. Both valid lenses on the same plan.
- **No external API calls in v1.0.** Weather and Notion registries are pass-in. v1.1 may wire MCP wrappers.

---

## What's next (Day 19 — Fri May 8)

- Run all 5 test fixtures against Opus 4.6 with the v1.0 system prompt.
- Validate every output against `schemas/output.schema.json`.
- Lock v1.0 if 5/5 pass; otherwise iterate prompt + re-run.
- Add fixture #6+ if any new failure modes surface.

Day 20 (Sat May 9) = Production Coord v1.0 LOCK + Week 3 wrap → Week 4 = AI Video Gen Agent SPEC start.

---

## Provenance

- Authored 2026-05-07 (Day 18 · Wk3D6) — Sequel Digital ARS overnight build session
- SPEC LOCKED 2026-05-03 (Day 14 Rest Day)
- Schemas LOCKED 2026-05-06 (Day 17)
- Mirrors: Brief Agent README, Script Agent README, Storyboard Agent README — same shape
- No external comms. No financial commitments. Zero entity-boundary violations.
