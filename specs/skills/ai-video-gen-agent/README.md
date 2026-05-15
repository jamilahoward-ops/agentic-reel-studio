# AI Video Gen Agent — README (v1.0)

Human invocation guide for the **fifth pre-production agent** and the **first runtime-cost agent** in the Agentic Reel Studio pipeline.

> **Built:** Fri May 15, 2026 (Day 26 · Wk4D6) · Sequel Digital — ARS
> **SPEC:** `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` (Day 24 LOCK CANDIDATE — operator sign-off Items 8 + 11 still pending)
> **Schemas:** Day 25 (Thu May 14) LOCKED + self-validating (Draft 2020-12) · 6/6 positive · 9/10 negative
> **LLM lock target:** Day 27 (Sat May 16) — paste-and-run runbook · operator-gated · dry-run vs live = Open Question #11

---

## What this skill does

Reads a **Mode B** `production_plan.json` from the Production Coord Agent and emits a `rendered_shots.json` — per-shot render dispatch records, style consistency anchor, render telemetry, post-render QC seed, and handoff targets for Edit Director / QC / Style Replication.

Single-responsibility line: *"Pixel binding for an executable render queue."*

This is the **first agent that spends money** at runtime. Defense-in-depth here is non-negotiable — a leak costs cash AND ships pixels.

---

## Pipeline position

```
Trend Hunter → Strategy → Brief → Script → Storyboard → Production Coord → AI VIDEO GEN → Edit → QC → Publish → Loop
```

AI Video Gen is the **runtime gate** and the **5th defense-in-depth firewall** (Brief sets, Script re-validates, Storyboard re-validates, Production Coord re-validates, AI Video Gen re-validates entity / banned-vocab / no-buildings / tier↔mode).

---

## When to invoke

- A Mode B production plan (Pro or Enterprise tier) is ready and renders need to ship.
- A previous render set was rejected by Edit Director or QC (`rendered_shots_schema_mismatch` or `partial_set_unusable`) — re-run with refreshed quotas.
- An operator wants a render set regenerated against the same plan after a vendor outage / quota replenishment.

**Do NOT invoke when:**
- Upstream Production Coord Agent emitted an errorEnvelope — agent halts at Step 1 with `production_plan_not_success`.
- `production_mode != "B"` OR `mode_b_plan == null` — agent halts with `not_mode_b` (route to Style Replication Agent for Mode C, or human handoff for Mode A live shoot).
- `tier ∈ {Pilot, Starter}` — Pilot/Starter NEVER reach Mode B. Halt with `tier_constraint_violation`.

---

## Inputs (required + optional)

**Required (6 top-level fields):**

```
production_plan         production-coord-agent successProductionPlan (Mode B branch only) OR errorEnvelope
brief                   brief-agent successBrief (denormalized passthrough — do_not_say + entity firewall)
storyboard              storyboard-agent successStoryboard (denormalized passthrough — shoot_logistics)
session_id              "ars-YYYY-MM-DD-NNN"
lever_state             1 | 2 | 3 (v1.0 default = 3)
engine_quota_handles    { engine_id: opaque-handle-string } — opaque platform-layer handles (NEVER raw credentials)
```

**Optional:**

- `style_token_lib[]` — REINVENTED-specific aesthetic tokens (purple/gold palette, Alux framing language). Up to 32 tokens.
- `negative_prompt_template` — pre-composed negative prompt (must be >100 chars). If absent, agent composes from canonical sources (§6.5 firewall + `brief.do_not_say` + brand-anti-patterns + no-buildings string).
- `cost_overrun_buffer_pct` — integer 0..15, default 10. Hard ceiling at 15% — operator cannot widen the gate above v1.0 invariant.
- `runtime_environment_class` — `"dev" | "staging" | "production"`, default `"production"`. Day 27 LLM Test Runbook uses `"staging"`.

Full validation rules in `schemas/input.schema.json` (Draft 2020-12). Mode B exclusivity hard-enforced at the schema layer — Pilot/Starter/Mode A/Mode C inputs reject at parse.

---

## Outputs

Single `rendered_shots.json` object. Polymorphic top-level:

- **successRenderedShots** — full set with `rendered_shots[]`, `style_consistency_anchor`, `render_telemetry`, `qc_pre_flags[]`, `qc_warnings[]`, `escalation_path[]`, `handoff_targets[]`, `parent_chain` 4-tuple, `metadata{}`.
- **errorEnvelope** — `{ status: "blocked", errorEnvelope: { failure_code, failed_check_id, failed_shot_id?, attempts, detail{} } }`.

**17 error codes** (canonical namespace per SPEC §6.3 + §13 Decision #11):

```
input_validation_failed         entity_firewall_breach
tier_constraint_violation       production_plan_not_success
not_mode_b                      quota_not_reserved
anchor_misalignment             render_quota_exhausted
cost_overrun                    engine_failure_unrecoverable
negative_prompt_missing         talent_unauthorized
banned_vocab_leaked             no_buildings_violation
qc_pre_flags_format_violation   ai_video_gen_agent_failed
schema_invalid_after_retry
```

Slot 11 = `ai_video_gen_agent_failed` (renamed from inherited `production_coord_agent_failed` per Cross-SPEC §3.6).

**Schema-layer hard enforcement (Day 25 LOCKED):**
- `negative_prompt_attached_bool: const true` on every dispatch record (Hard Rule #10 baked in)
- `asset_uri` pattern enforces `ars://renderset/...` scheme (Hard Rule #8 baked in)
- `parent_chain` exact 4-tuple via `prefixItems` + `items: false` (Decision #16)
- 17 errorEnvelope codes via `enum` (Decision #11)

---

## Quick-start invocation

1. **Confirm prerequisites:**
   - Production Coord Agent v1.0 SKILL bundle is live and produced a `successProductionPlan` (Mode B branch).
   - Brief + Script + Storyboard + ProdCoord all emitted successful predecessors (passthroughs available).
   - Tier ∈ {Pro, Enterprise} (Pilot/Starter never reach Mode B).
   - `engine_quota_handles` populated for at least the engines referenced in `render_queue[*].engine_id`.

2. **Build the input object** using `prompts/user-template.txt`. Every required field present.

3. **Validate input** before LLM execution (saves Opus tokens AND prevents wasted engine spend):

   ```bash
   python3 -c "
   import json
   from jsonschema import Draft202012Validator
   schema = json.load(open('schemas/input.schema.json'))
   data = json.load(open('test-cases/case-01-pro-happy/input.json'))
   Draft202012Validator(schema).validate(data)
   print('OK')
   "
   ```

   Or run the bundled harness:

   ```bash
   python3 validate.py
   ```

4. **Invoke the agent** with the system prompt from `SKILL.md` (verbatim — do NOT paraphrase) and the input as a JSON-only user message.

5. **Validate the output** against `schemas/output.schema.json`. Reject any output that fails self-validation.

6. **Route per `handoff_targets[]`** to Edit Director / QC / Style Replication.

---

## File map

```
ai-video-gen-agent/
  SKILL.md                              ← system prompt verbatim (run this)
  README.md                             ← THIS FILE
  vendor_pricing_canon.json             ← 8-engine $/sec lookup (RESEARCH-ONLY snapshot)
  negative_prompt_template.md           ← composed negative prompt canon + SHA-256
  prompts/
    user-template.txt                   ← user-message template (fill + paste)
  schemas/
    input.schema.json                   ← Day 25 LOCKED self-validating
    output.schema.json                  ← Day 25 LOCKED self-validating
  test-cases/
    case-01-pro-happy/                  ← TC-01 happy Pro (3-shot · single engine · all renders first attempt)
      input.json
      expected_output.json
      scenario.md
    case-02-enterprise-happy/           ← TC-02 happy Enterprise (5-shot · mixed engines + HeyGen talent)
      input.json
      expected_output.json
      scenario.md
    case-03-anchor-failure/             ← TC-03 anchor render exhausts primary + fallback → engine_failure_unrecoverable
      input.json
      expected_output.json
      scenario.md
    case-04-cost-overrun/               ← TC-04 actual $852 vs $750 Ent ceiling → cost_overrun
      input.json
      expected_output.json
      scenario.md
    case-05-quota-exhausted/            ← TC-05 anchor renders OK, both inheritors burn 4 attempts each → render_quota_exhausted
      input.json
      expected_output.json
      scenario.md
  validate.py                           ← positive harness (5/5 inputs validate clean + 4/4 outputs validate clean)
```

---

## 5 test fixtures (Day 26)

| # | Tier | Branch | Expected error | Coverage |
|---|------|--------|----------------|----------|
| 1 | Pro | success | n/a — happy path | Anchor + 2 inheritors · single engine · all first attempt |
| 2 | Enterprise | success | n/a — happy path | Anchor (Runway Turbo) + 4 inheritors (Pika + HeyGen v3 + Kling + Pika) |
| 3 | Pro | error | `engine_failure_unrecoverable` | Anchor exhausts primary + fallback (4 attempts burned, set blocked) |
| 4 | Enterprise | error | `cost_overrun` | $852 actual vs $750 ceiling × 1.10 = $825 hard ceiling — $27 over |
| 5 | Pro | error | `render_quota_exhausted` | Anchor renders OK, both inheritors burn 4 attempts each across all engines |

All 5 input objects validate against `schemas/input.schema.json` before LLM execution. All 4 outputs (TC-01 success branch + TC-03/04/05 errorEnvelope branch) validate against `schemas/output.schema.json`. Fixtures run on Day 27 (Sat May 16) for v1.0 LOCK.

---

## Common gotchas

- **Mode B exclusivity is parse-time.** Pilot/Starter/Mode A/Mode C inputs REJECT at the schema layer — agent never even reaches Process Step 1. This is intentional defense-in-depth.
- **Polymorphic production_plan accept.** If `production_plan.error` is present, agent halts immediately with `production_plan_not_success` — do NOT attempt to read `mode_b_plan`.
- **Anchor failure is fatal.** If `rendered_shots[0]` (the anchor) fails across primary + 1 retry + fallback + 1 retry → emit `engine_failure_unrecoverable`. Do NOT dispatch inheritors. Operator pays for the failed anchor render (~$15 worst case on Runway Gen3 60s) but avoids N inheritor renders that would all drift.
- **Inheritor failure is partial.** If one or more inheritors fail across all engines → set `status="partial_with_warnings"`, list failed shot IDs in `qc_warnings[]`, continue. Edit Director can decide whether to ship partial or re-queue.
- **Negative prompt is `const: true`.** Schema rejects any `negative_prompt_attached_bool: false` at parse time. There is no way to ship a render without the negative prompt — by design.
- **Asset URIs are `ars://renderset/...`.** Schema pattern rejects absolute external CDN URLs. Orchestrator resolves to signed URLs at Edit Director → Publishing.
- **HeyGen talent is hardcoded `jamila-howard-reinvented-v2` v1.0.** Any other talent value rejects BEFORE the HeyGen API call (no cost incurred). Multi-talent v1.1+ gated on first Sequel Digital external client onboarding.
- **Cost ceiling has zero exceptions.** Pro $400 × 1.10 = $440 hard ceiling. Enterprise $750 × 1.10 = $825 hard ceiling. Even $441 on Pro = halt with `cost_overrun`. No "almost made it."
- **5th defense-in-depth firewall is the point.** Brief, Script, Storyboard, ProdCoord all already validated. Re-checking here is non-negotiable because this is where money gets spent.
- **No external API calls in v1.0 SKILL bundle dry-run.** Day 27 LLM Test Runbook is the gate for first paid engine dispatch — operator-decided dry-run vs live (Open Question #11). v1.0 SKILL bundle authors against schemas + fixtures only.

---

## What's next (Day 27 — Sat May 16)

- Run all 5 test fixtures against Opus 4.6 with the v1.0 system prompt (paste-and-run runbook).
- Validate every output against `schemas/output.schema.json`.
- Lock v1.0 if 5/5 pass; otherwise iterate prompt + re-run.
- Decision Day 27 OR Day 28 (Rest Day review): dry-run only (cost ≈ $0, cached mock engine responses) OR live mode (≤$1,000 worst case for 1 Pro + 1 Enterprise happy-path live render). Operator decision per Open Question #11.

Day 28 (Sun May 17) = Rest Day. Day 29+ = operator-gated v1.0 LLM LOCK + Mode B production gate goes live + Style Replication Agent SPEC outline kickoff (Mode C / Week 5 target).

---

## Provenance

- Authored 2026-05-15 (Day 26 · Wk4D6) — Sequel Digital ARS overnight build session
- SPEC LOCK CANDIDATE 2026-05-13 (Day 24) — operator sign-off Items 8 + 11 pending
- SPEC body 2026-05-11 (Day 22 §6/§7/§10/§14) + 2026-05-12 (Day 23 §8/§9/§11/§12/§13/§15/§16)
- Schemas LOCKED 2026-05-14 (Day 25) — 6/6 positive · 9/10 negative
- Mirrors: Brief Agent README, Script Agent README, Storyboard Agent README, Production Coord Agent README — same shape
- No external comms. No render API. No engine credentials. No financial commitments. Zero entity-boundary violations.
