# Script Agent — README (v1.0)

Human-readable invocation guide for the ARS Script Agent skill.

## What this is

The Script Agent is the third pre-production agent in ARS. It converts a `brief.json` (from Brief Agent v1.0) into a canonical `script.json` that downstream agents (Storyboard, Production Coord, Edit) consume directly.

This folder is the **deployable skill canon**. Files are versioned at v1.0 as of April 29, 2026.

## How to invoke (operator workflow)

1. Choose a test case or build a fresh input that conforms to `schemas/input.schema.json`. The `brief` field MUST be either a Brief Agent successBrief or errorEnvelope.
2. Open Claude Opus 4.6 (the locked v1.0 model).
3. Set the system prompt to the v1.0 system prompt block in `SKILL.md` §System prompt.
4. Set the user message to the contents of `prompts/user-template.txt` with `{input_json}` substituted.
5. Capture the model's output. It must be a single valid JSON object (no markdown).
6. Validate the output against `schemas/output.schema.json` using the validator script (below).
7. If valid + Lever 3 + qc_score ≥ 0.7 + zero qc_warnings → auto-promote to Storyboard Agent. Otherwise route to Jamila for review before passing.

## How to run the 5 test cases

```bash
cd "Sequel Digital/ARS/skills/script-agent"
python3 -c "
import json, glob
from jsonschema import Draft202012Validator
schema = json.load(open('schemas/input.schema.json'))
v = Draft202012Validator(schema)
for p in sorted(glob.glob('test-cases/case-*.json')):
    case = json.load(open(p))
    errs = list(v.iter_errors(case['input']))
    print(p, 'PASS' if not errs else f'FAIL: {[e.message for e in errs[:2]]}')
"
```

(Already run on Wed Apr 29 — 5 of 5 INPUTS validated. Output validation runs after the LLM produces script.json — see `test-cases/results/`.)

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | System prompt, 9-step process, IO contract, 12-check QC, lever behavior, tier table |
| `prompts/user-template.txt` | Wraps the input JSON into the canonical user message |
| `schemas/input.schema.json` | jsonschema Draft 2020-12 — input validation (accepts both Brief success and error variants) |
| `schemas/output.schema.json` | jsonschema Draft 2020-12 — output validation (success + error envelope) |
| `test-cases/case-01-*.json` | Pilot tier · story format · happy path |
| `test-cases/case-02-*.json` | Starter tier · listicle · prior_scripts opener-diversification |
| `test-cases/case-03-*.json` | Brief was errorEnvelope — expect `brief_not_success` |
| `test-cases/case-04-*.json` | Tier mismatch — Mode C requested on Pilot tier — expect `tier_constraint_violation` |
| `test-cases/case-05-*.json` | Hostile — operator forces "hustle" via swap_words — expect rewrite + qc_warning |

## Status checklist (Wed Apr 29 build — Day 10)

- [x] Skill folder structure stood up
- [x] SKILL.md dropped from spec §8 (system prompt v1.0 LOCKED)
- [x] input.schema.json built and validates as Draft 2020-12
- [x] output.schema.json built and validates as Draft 2020-12 (success + errorEnvelope)
- [x] 5 test-case fixtures authored
- [x] All 5 test-case INPUTS validate against input.schema.json (5/5 pass)
- [x] user-template.txt authored
- [x] README.md authored
- [ ] LLM output runs against schema — pending Thu Apr 30 live execution
- [ ] v1.0 LOCKED status declared after 5 of 5 outputs pass — pending Thu Apr 30 live execution

## Critical rules baked into v1.0

1. **JSON only** output. Single object. Schema-validated.
2. **Entity firewall** — REINVENTED scripts may NEVER reference Holdco Group, 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A. Hard reject with errorEnvelope.
3. **Hook integrity** — `lines[0].spoken` AND `hook_block.spoken_line` are VERBATIM copies of `brief.hook.first_3_seconds`. Script Agent is forbidden to "improve" the hook.
4. **Banned hustle vocabulary** — the 8 terms from Brand Voice Intake §6.2 are absence-checked across every spoken line, on_screen_text, and broll description (verbatim + conjugates).
5. **No buildings rule** — every b-roll cue declares interior or black-card framing only.
6. **Tier honoring** — lines / b-roll / variants / voice takes / music swells stay inside the tier cap embedded in the system prompt.
7. **Mode authorization** — A any tier · B Pro+ · C Enterprise only. Defense in depth.
8. **CTA in final 6 seconds.** Last line ends ≤ duration_target + 1s. Sum of line durations ≤ duration_target × 1.05.
9. **Captions burn-in MANDATORY** at Pilot/Starter tier (every variant).
10. **Lever 3 default** — auto-promote when qc_score_predicted ≥ 0.7 AND zero qc_warnings. Otherwise human review.
11. **Self-QC** — 12-check list runs before emit. Failures regenerate once, then escalate.
12. **swap_words collision rejection** — operator-supplied swaps cannot push banned terms IN.

## Next builds (Week 2 → Week 3)

After Script Agent v1.0 locks (target: Thu 4/30 after 5 live test runs):

1. **Storyboard Agent SPEC** — consumes script.json, emits storyboard.json (Fri Apr 30 / Sat May 1)
2. **Storyboard Agent SKILL bundle** (Sat May 2 — Rest Day spec only, build Sun delayed to Mon)
3. **Trend Hunter** — replaces manual topic_signal feed (Week 3)

Per Orchestration Blueprint §5 sequence.

---

*Build: April 29, 2026 (Day 10 — Wed · Week 2 Day 3)*
*Spec source: `ars/ARS-2026-04-28-Script-Agent-v1-Spec.md`*
*Mirror: `/outputs/ars/skills/script-agent/` (canonical copy)*
