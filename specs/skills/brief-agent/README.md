# Brief Agent — README (v1.0)

Human-readable invocation guide for the ARS Brief Agent skill.

## What this is

The Brief Agent is the second pre-production agent in ARS. It converts a topic + brand context into a canonical `brief.json` that downstream agents (Script, Storyboard, Production Coord) consume directly.

This folder is the **deployable skill canon**. Files are versioned at v1.0 as of April 27, 2026.

## How to invoke (operator workflow)

1. Choose a test case or build a fresh input that conforms to `schemas/input.schema.json`.
2. Open Claude Opus 4.6 (the locked v1.0 model).
3. Set the system prompt to the v1.0 system prompt block in `SKILL.md` §System prompt.
4. Set the user message to the contents of `prompts/user-template.txt` with `{input_json}` substituted.
5. Capture the model's output. It must be a single valid JSON object (no markdown).
6. Validate the output against `schemas/output.schema.json` using the validator script (below).
7. If valid + Lever 3, route to Jamila for review before passing to Script Agent.

## How to run the 5 test cases

```bash
# From repo root:
cd "Sequel Digital/ARS/skills/brief-agent"
python3 -c "
import json
from jsonschema import Draft202012Validator
schema = json.load(open('schemas/input.schema.json'))
v = Draft202012Validator(schema)
for p in sorted(__import__('glob').glob('test-cases/case-*.json')):
    case = json.load(open(p))
    errs = list(v.iter_errors(case['input']))
    print(p, 'PASS' if not errs else f'FAIL: {[e.message for e in errs[:2]]}')
"
```

(Already run on Mon Apr 27 — 5 of 5 INPUTS validated. Output validation runs after the LLM produces brief.json — see `test-cases/results/`.)

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | System prompt, 9-step process, IO contract, QC checklist, lever behavior |
| `prompts/user-template.txt` | Wraps the input JSON into the canonical user message |
| `schemas/input.schema.json` | jsonschema Draft 2020-12 — input validation |
| `schemas/output.schema.json` | jsonschema Draft 2020-12 — output validation (success + error variants) |
| `test-cases/case-01-*.json` | Pilot tier · story format · happy path |
| `test-cases/case-02-*.json` | Starter tier · listicle (forced by prior_briefs diversification) |
| `test-cases/case-03-*.json` | Entity firewall breach (HC topic on REINVENTED brand) |
| `test-cases/case-04-*.json` | Tier mismatch (Mode B requested on Pilot tier) |
| `test-cases/case-05-*.json` | Low-confidence topic (< 0.5) |

## Status checklist (Mon Apr 27 build)

- [x] Skill folder structure stood up
- [x] SKILL.md dropped from spec §5.1 (system prompt v1.0 LOCKED)
- [x] input.schema.json built and validates as Draft 2020-12
- [x] output.schema.json built and validates as Draft 2020-12 (success + error envelope)
- [x] 5 test-case fixtures authored
- [x] All 5 test-case INPUTS validate against input.schema.json
- [ ] LLM output runs against schema — pending live execution
- [ ] v1.0 LOCKED status declared after 5 of 5 outputs pass — pending live execution

## Critical rules baked into v1.0

1. **JSON only** output. Single object. Schema-validated.
2. **Entity firewall** — REINVENTED brand briefs may NEVER reference Holdco Group, 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A. Hard reject with errorEnvelope.
3. **Banned hustle vocabulary** — the 8 terms from Brand Voice Intake §6.2 (`girlboss`, `hustle`, `grind`, `boss babe`, `millionaire mindset`, `8-figure`, `luxury`, `elevate`) MUST appear verbatim in `do_not_say`.
4. **No buildings rule** — visual direction NEVER specifies aspirational external buildings.
5. **Tier honoring** — Pilot/Starter = Mode A only. Pro = Mode A + B. Enterprise = Mode A + B + C.
6. **Format diversification** — single format capped at 3 of last 5 briefs.
7. **Lever 3 default** — `human_review_required: true` for every brief during the first 30 reels.
8. **Self-QC** — 8-check list runs before emit. Failures regenerate once, then escalate.

## Next builds (Week 2 → Week 3)

After Brief Agent v1.0 locks (target: Tue 4/28 after first live test runs):

1. **Script Agent** — consumes brief.json, emits script.json (Week 2 Day 3–4)
2. **Trend Hunter** — replaces manual topic_signal feed (Week 3)
3. **Strategy Agent** — sits between Trend Hunter and Brief Agent (Week 3)

Per Orchestration Blueprint §5 sequence.

---

*Build: April 27, 2026 (Day 8 — Mon · Week 2 Day 1)*
*Spec source: `ars/ARS-2026-04-26-Brief-Agent-v1-Spec.md`*
*Mirror: `/outputs/ars/skills/brief-agent/` (canonical copy)*
