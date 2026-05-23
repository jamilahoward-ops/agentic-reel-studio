# Style Replication Agent — README (v1.0)

Human invocation guide for the **sixth pre-production-into-production agent** and the **second runtime-cost agent** (after AI Video Gen) in the Agentic Reel Studio pipeline.

> **Built:** Sat May 23, 2026 (Day 34 · Wk5D8/Wk6D1) · Sequel Digital — ARS
> **SPEC:** `ARS-2026-05-21-Day-32-Style-Replication-Agent-v1-LOCK-CANDIDATE.md` (operator Items 6/8/11 pending)
> **Schemas:** Day 33 (Fri May 22) LOCKED + META-SCHEMA VALID + 5/5 SMOKE FIXTURES PASS (Draft 2020-12)
> **v1.0 LOCK target:** Day 37 (Tue May 26) — hard-gated on AI Video Gen v1.0 LOCK first

---

## What this skill does

Reads a **Mode A | Mode B | Mode C** input bundle (polymorphic via `oneOf` on `production_mode`) and emits a `replicated_shots` object — per-shot replication record with composite `inheritance_match_score_0_1` vs drift threshold 0.85, replication telemetry, post-replication QC seed, and handoff targets for Edit Director / QC / (optional) Localization.

Single-responsibility line: *"Brand-aesthetic transfer onto rendered or sourced footage. Inherits anchor style from rendered_shots; applies consistent palette, motion grade, framing tokens, and brand finish layer across all inheritor shots without re-renders."*

This is the **second agent that spends money** at runtime. Defense-in-depth here is non-negotiable — a leak costs cash AND ships pixels.

---

## Pipeline position

```
Trend Hunter → Strategy → Brief → Script → Storyboard → Production Coord → AI Video Gen → STYLE REPLICATION → Edit → QC → Publish → Loop
```

Style Replication is the **runtime gate after AI Video Gen** and the **6th defense-in-depth firewall** (Brief sets, Script re-validates, Storyboard re-validates, ProdCoord re-validates, AI Video Gen re-validates, Style Replication re-validates entity / banned-vocab / no-buildings / tier↔mode↔ceiling / drift).

---

## When to invoke

- A Mode B AI Video Gen `rendered_shots` set is ready for inheritor pass + grade pass.
- A Mode A operator+videographer raw shoot manifest is ready for grade pass only.
- A Mode C Enterprise hot-path directive came from ProdCoord with `mode_c_directive.shot_prompts[]` and operator wants to skip per-shot generation.
- A previous replication set was rejected by Edit Director or QC — re-run with refreshed anchor cache.

**Do NOT invoke when:**
- Upstream ProdCoord emitted errorEnvelope — Style Replication halts at Step 1.
- `tier ∈ {Pilot, Starter}` — Pilot/Starter NEVER reach any Style Replication mode. Halt at schema parse.
- `production_mode == "C"` AND `tier != "Enterprise"` — Decision #10 LOCKED Enterprise-only at v1.0. Halt at schema parse.
- `brand_anchor_reference` missing or fields incomplete — halt with `anchor_unavailable`.

---

## Inputs (Mode B Pro happy path — required + optional)

**Required (7 top-level fields per Mode B branch):**

```
production_plan         production-coord-agent successProductionPlan Mode B branch
rendered_shots          ai-video-gen-agent successRenderedShots (denormalized subset — Mode B only)
brief                   brief-agent successBrief (denormalized passthrough — do_not_say + brand_finish_intent)
brand_anchor_reference  brand-anchor-cache lookup record (anchor_id + anchor_sha256 + anchor_locked_date triplet)
session_id              "ars-YYYY-MM-DD-NNN"
lever_state             1 | 2 | 3 (v1.0 default = 3)
engine_quota_handles    { pika_style_tokens, runway_style_reference, clip_native, phash_native, palette_native, grade_pass_native }
```

**Optional:**

- `cost_overrun_buffer_pct` — integer 0..15, default 10. Hard ceiling at 15% — operator cannot widen above v1.0 invariant.
- `runtime_environment_class` — `"dev" | "staging" | "production"`, default `"production"`. Day 36 LLM Test Runbook will use `"staging"`.

**Mode A** swaps `rendered_shots` for `raw_shot_manifest` and trims `engine_quota_handles` to native + grade_pass only.

**Mode C** drops `rendered_shots`, adds `mode_c_directive` (with `shot_prompts[]` + `coverage_envelope_tolerance_pct`) to `production_plan`, and adds `coverage_envelope_native` to `engine_quota_handles`.

Full validation rules in `schemas/input.schema.json` (Draft 2020-12). Mode + tier joint validation hard-enforced at the schema layer — Pilot/Starter and Mode C non-Enterprise inputs reject at parse.

---

## Outputs

Single `replicated_shots` object. Polymorphic top-level:

- **successReplicatedShots** — `status ∈ {ready_for_qc, partial_with_warnings}` with `replicated_shots[]`, `brand_anchor_reference` (re-emitted), `replication_telemetry`, `qc_pre_flags[]`, `qc_warnings[]`, `escalation_path[]`, `handoff_targets[]`, `parent_chain` 5-tuple, `metadata{}`.
- **errorEnvelope** — `{ status: "blocked", errorEnvelope: { failure_code, failed_check_id?, failed_shot_id?, attempts, detail?, successful_shots?, recovery_path? } }`.

**6 error codes** (canonical namespace per SPEC §6.3 + §13 Decision #11 — LOCKED Day 30):

```
anchor_unavailable              brand_finish_layer_missing
style_drift_exceeded            qc_pre_flags_format_violation
cost_overrun                    style_replication_agent_failed
```

Slot 12 = `style_replication_agent_failed` (renamed from inherited `production_coord_agent_failed` per Cross-SPEC §3.6).

**Schema-layer hard enforcement (Day 33 LOCKED):**
- `parent_chain` exact 5-tuple via `prefixItems` + `items: false` + `minItems: 5` + `maxItems: 5` (§16.5 decision #1)
- `mode_c_coverage_match_bool` nullable via `type: ["boolean", "null"]` (§16.5 decision #2)
- `literal_fingerprint_inherit` `anyOf` [full | Mode-A partial | null] with `not: required[anchor_phash_64bit]` on partial (§16.5 decision #3)
- `replication_set_id` `format: "uuid"` (§16.5 decision #4)
- `self_qc_failed_check_id` `oneOf: [null | integer 1..12]` (§16.5 decision #5)
- Backward-compat assertion: 4-tuple parent_chain REJECTED, 6-tuple REJECTED (§16.5 decision #6)

---

## Quick-start invocation

1. **Confirm prerequisites:**
   - AI Video Gen Agent v1.0 SKILL bundle is live and produced a `successRenderedShots` (for Mode B), OR ProdCoord emitted Mode A `raw_shot_manifest`, OR ProdCoord emitted Mode C `mode_c_directive`.
   - Brand-anchor cache has a current entry for the target brand (REINVENTED at v1.0).
   - Tier ∈ {Pro, Enterprise} (Pilot/Starter never reach Style Replication).
   - For Mode C: tier MUST be Enterprise (Decision #10).
   - `engine_quota_handles` populated for at least the engines referenced by the mode (Mode B + C require `pika_style_tokens`; native handles always required).

2. **Build the input object** using `prompts/user-template.txt`. Every required field present per mode branch.

3. **Validate input** BEFORE LLM execution (saves Opus tokens AND prevents wasted engine spend):

   ```bash
   python3 -c "
   import json
   from jsonschema import Draft202012Validator
   schema = json.load(open('schemas/input.schema.json'))
   data = json.load(open('test-cases/case-01-mode-b-pro-happy/input.json'))
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

6. **Route per `handoff_targets[]`** to Edit Director / QC / (optional) Localization.

---

## File map

```
style-replication-agent/
  SKILL.md                              ← system prompt verbatim (run this)
  README.md                             ← THIS FILE
  engine_pricing_canon.json             ← 7-engine $/shot lookup (RESEARCH-ONLY snapshot)
  literal_fingerprint_template.md       ← anyOf encoding canon + 5-layer enforcement chain
  prompts/
    user-template.txt                   ← user-message template (fill + paste) — Mode B Pro skeleton
  schemas/
    input.schema.json                   ← Day 33 LOCKED self-validating (Draft 2020-12)
    output.schema.json                  ← Day 33 LOCKED self-validating (Draft 2020-12)
  test-cases/
    case-01-mode-b-pro-happy/           ← TC-01 happy Mode B Pro (5 shots: anchor + 4 inheritors, all Pika)
      input.json
      expected_output.json
      scenario.md
    case-02-mode-c-enterprise-happy/    ← TC-02 happy Mode C Enterprise (3 shots, hot-path · margin demo -92%)
      input.json
      expected_output.json
      scenario.md
    case-03-anchor-unavailable/         ← TC-03 Mode C cache miss → anchor_unavailable
      input.json
      expected_output.json
      scenario.md
    case-04-cost-overrun/               ← TC-04 Mode B Enterprise 8 shots × 3 fallback → cost_overrun
      input.json
      expected_output.json
      scenario.md
    case-05-style-drift-exceeded/       ← TC-05 Mode B Pro regenerate-then-still-fail → style_drift_exceeded
      input.json
      expected_output.json
      scenario.md
  validate.py                           ← positive harness (5/5 inputs validate clean + 5/5 outputs validate clean + 7/7 engine_pricing_canon lookups)
```

---

## 5 test fixtures (Day 34)

| # | Mode | Tier | Branch | Expected error | Coverage |
|---|------|------|--------|----------------|----------|
| 1 | B | Pro | success | n/a — happy path | Anchor + 4 inheritors · Pika PRIMARY all shots · full 12-check validation matrix |
| 2 | C | Enterprise | success | n/a — happy path | Hot path · 3 shots · margin demo $55 vs $692 Mode B equivalent = **-92% cost** |
| 3 | C | Enterprise | error | `anchor_unavailable` | Cache miss on deprecated anchor → errorEnvelope with `recovery_path` guidance |
| 4 | B | Enterprise | error | `cost_overrun` | 8 shots × 3 fallback cascade pushes past $120 ceiling, halt mid-process with partial work preserved |
| 5 | B | Pro | error | `style_drift_exceeded` | Regenerate-then-still-fail after 2 attempts, Check #6 tri-state FAIL, partial work preserved in `successful_shots[]` |

4 of 6 errorEnvelope codes covered by test fixtures. 2 uncovered (`brand_finish_layer_missing` + `qc_pre_flags_format_violation`) covered by schema-only smoke fixtures at Day 33. Mode A fixture deferred to v1.0.1 (§13 Decision #14).

All 5 input objects validate against `schemas/input.schema.json` before LLM execution. All 5 outputs (TC-01 + TC-02 successReplicatedShots branch · TC-03 + TC-04 + TC-05 errorEnvelope branch) validate against `schemas/output.schema.json`. Fixtures run on Day 36 (Mon May 25) for v1.0 LOCK gate.

---

## Common gotchas

- **Tier × Mode joint validation is parse-time.** Pilot/Starter inputs REJECT at the schema layer. Mode C with `tier == "Pro"` REJECTS at the schema layer (Enterprise-only Decision #10).
- **Polymorphic input is by `production_mode` const.** Mode A bundle requires `raw_shot_manifest`; Mode B requires `rendered_shots`; Mode C requires `mode_c_directive`. Sending the wrong shape rejects at parse before the agent loop runs.
- **Anchor identity = three-way bit equality.** `anchor_id` AND `anchor_sha256` AND `anchor_locked_date` ALL must match the cache. Any single mismatch → `anchor_unavailable`.
- **Drift threshold 0.85 is LOCKED canon.** Identical to AI Video Gen Day 23 §12. Do NOT loosen per fixture.
- **Regenerate ceiling = 2.** Decision #6 LOCKED Day 31. No third attempt under any circumstance. `retry_count` schema max = 2.
- **Cost ceiling × 1.10 = hard halt.** Pro $50 × 1.10 = $55 hard ceiling. Enterprise $120 × 1.10 = $132 hard ceiling. Even $55.01 on Pro = halt with `cost_overrun`. No "almost made it."
- **Mode C is the margin engine.** Bypasses AI Video Gen entirely. Typical Mode C reel costs **~$55 vs $692 Mode B equivalent (-92%)**. This is the agent's economic justification — Lever 1 graduation post-90 reels assumes Mode C carries the cost story.
- **Mode A is intentionally narrow.** Grade pass only on operator+videographer assets. No fingerprint extraction (raw shoot manifest fingerprinting differs — `anchor_phash_64bit` omitted via `not: required` on Mode A partial encoding §16.5 decision #3).
- **Asset URIs are `ars://replicated_shots/...`** (output) and `ars://rendered_shots/...` (input rendered_shots) and `ars://raw_shoots/...` (input Mode A raw_shot_manifest). Schema patterns reject any external CDN URL at parse.
- **`literal_fingerprint_inherit` shape varies by branch.** Mode B + C success: full. Mode A success: partial (omit `anchor_phash_64bit`). errorEnvelope: null. The `anyOf` enforces this.
- **5-tuple parent_chain is the §16.3 amendment.** Cross-SPEC §3.9 generalization to n-tuple-as-lineage for all 17 agents. Schema rejects 4-tuples (legacy AI Video Gen shape) AND 6-tuples (future extensions belong in downstream agent schemas).
- **6th defense-in-depth firewall is the point.** Brief, Script, Storyboard, ProdCoord, AI Video Gen all already validated. Re-checking here is non-negotiable because this is the LAST agent before downstream Edit Director + QC + Publish.
- **No external API calls in v1.0 SKILL bundle dry-run.** Day 36 LLM Test Runbook is the gate for first paid engine dispatch — operator-decided dry-run vs live (Open Q #36 — Donna recommends dry-run for LOCK gate per AI Video Gen #11 precedent). v1.0 SKILL bundle authors against schemas + fixtures only.

---

## What's next (Day 35 — Sun May 25 · Rest Day)

- Future Jamila 2033 directive (Pillar 1: Rest) observed.
- Donna may produce a Day 36 pre-flight scaffold (handoff doc, NOT canon) per Day 28 Rest Day pattern.

## What's next (Day 36 — Mon May 26)

- LLM Test Runbook authoring (mirror AI Video Gen Day 27 pattern).
- Operator sit-down primed: pre-flight checklist → per-case execution → 5 fixture pass criteria → dry-run engine stub block keyed by mode/engine/case → paste-and-run Python validator → aggregate 5/5 PASS verdict for v1.0 LOCK gate.
- Live mode reserved for v1.0.1 (≤$500 spend ceiling vs AI Video Gen's ≤$1K because Style Replication per-shot cost ~1/8th).

## What's next (Day 37 — Tue May 27)

- v1.0 LOCK ceremony.
- **HARD GATE on AI Video Gen v1.0 LOCK first.** Style Replication LOCK ceremony cannot complete without AI Video Gen LOCKED.
- Promotion rule (Day 32 LOCK CANDIDATE §5 LOCKED): `v1.0-LOCK-CANDIDATE-day-32` → `v1.0-LOCKED-day-32-pending-ai-video-gen-LOCK` (Items 6/8/11 ratified) → final flip to `v1.0-LOCKED-day-37` at Day 37 ceremony AFTER AI Video Gen v1.0 LOCK confirmed.

---

## Provenance

- Authored 2026-05-23 (Day 34 · Sat · Wk5D8/Wk6D1) — Sequel Digital ARS overnight build session
- SPEC LOCK CANDIDATE 2026-05-21 (Day 32) — operator sign-off Items 6 + 8 + 11 pending
- SPEC body 2026-05-19 (Day 30 §6/§7/§10/§14) + 2026-05-20 (Day 31 §8/§9/§11/§12/§13/§15/§16)
- SPEC outline 2026-05-18 (Day 29 §0–§5)
- Schemas LOCKED 2026-05-22 (Day 33) — META-SCHEMA VALID + 5/5 SMOKE FIXTURES PASS
- Mirror pattern: AI Video Gen Day 26 SKILL bundle (10-file pattern → 11-file for Style Replication; literal_fingerprint_template.md replaces negative_prompt_template.md as the read-side analog of the same Hard Rule #10 chain)
- No external comms. No render API. No engine credentials. No vendor URL walkthrough. No financial commitments. No operator-impersonation (Day 32 Items 6/8/11 NOT silently advanced; AI Video Gen LOCK status unchanged). Zero entity-boundary violations.
