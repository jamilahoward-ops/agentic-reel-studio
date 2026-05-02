# Storyboard Agent — README (v1.0)

Human-readable invocation guide for the ARS Storyboard Agent skill.

## What this is

The Storyboard Agent is the **fourth pre-production agent** in ARS and the **production gate**. It converts a `script.json` (from Script Agent v1.0) into a canonical `storyboard.json` that downstream agents (Production Coord, Edit, QC) consume directly.

This folder is the **deployable skill canon**. Files are versioned at v1.0 as of May 2, 2026 (Day 13 — Wk3D1).

## Canonical naming (per Cross-SPEC Consistency Review §3)

This SKILL bundle authors against the canonical names from `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` §3, NOT the drifted SPEC examples. Three reconciliations applied:

1. `storyboard_id` regex pattern uses full `storyboard-` prefix — NOT `sb-` (drift #4 fixed here).
2. Top-level `platform_variants` array name — NOT `platform_render_specs` (drift #2 fixed here).
3. errorEnvelope enumerates the canonical 9-code namespace from Cross-SPEC §3.8.

The system prompt in `SKILL.md` is copied verbatim from Storyboard SPEC §8 (already LOCKED).

## How to invoke (operator workflow)

1. Choose a test case or build a fresh input that conforms to `schemas/input.schema.json`. The `script` field MUST be either a Script Agent successScript or errorEnvelope.
2. Open Claude Opus 4.6 (the locked v1.0 model).
3. Set the system prompt to the v1.0 system prompt block in `SKILL.md` §System prompt.
4. Set the user message to the contents of `prompts/user-template.txt` with `{input_json}` substituted.
5. Capture the model's output. It must be a single valid JSON object (no markdown).
6. Validate the output against `schemas/output.schema.json` using the validator script (below).
7. If valid + Lever 3 + qc_score ≥ 0.7 + zero qc_warnings → auto-promote to Production Coord Agent. Otherwise route to Jamila for review before passing.

## How to run the 5 test cases (input validation)

```bash
cd "Sequel Digital/ARS/skills/storyboard-agent"
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

(Run on Sat May 2 — must pass 5/5 before Day 14/15 LLM execution.)

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | System prompt, 9-step process, IO contract, 12-check QC, lever behavior, tier table |
| `prompts/user-template.txt` | Wraps the input JSON into the canonical user message |
| `schemas/input.schema.json` | jsonschema Draft 2020-12 — input validation (accepts both Script success and error variants) |
| `schemas/output.schema.json` | jsonschema Draft 2020-12 — output validation (success + 9-code errorEnvelope) |
| `test-cases/case-01-*.json` | Pilot tier · story format · Mode A · happy path |
| `test-cases/case-02-*.json` | Starter tier · listicle · Mode A · counter motion overlays + opener-rotation enforcement via prior_storyboards |
| `test-cases/case-03-*.json` | Script was errorEnvelope — expect `script_not_success` |
| `test-cases/case-04-*.json` | Defense-in-depth — Mode B requested on Pilot tier — expect `tier_constraint_violation` |
| `test-cases/case-05-*.json` | Defense-in-depth — Mode C requested on Pro tier (Enterprise-only) — expect `tier_constraint_violation` |

## Status checklist (Sat May 2 build — Day 13 — Wk3D1)

- [x] Skill folder structure stood up
- [x] SKILL.md dropped from spec §8 (system prompt v1.0 LOCKED, verbatim)
- [x] input.schema.json built (Draft 2020-12)
- [x] output.schema.json built (Draft 2020-12, success + canonical 9-code errorEnvelope)
- [x] storyboard_id pattern uses full prefix per Cross-SPEC canon
- [x] Top-level platform_variants per Cross-SPEC canon
- [x] 5 test-case fixtures authored
- [x] user-template.txt authored
- [x] README.md authored
- [ ] All 5 test-case INPUTS validate against input.schema.json — pending build-log validation step
- [ ] LLM output runs against schema — pending Day 14/15 live execution
- [ ] v1.0 LOCKED status declared after 5 of 5 outputs pass

## Critical rules baked into v1.0

1. **JSON only** output. Single object. Schema-validated.
2. **Entity firewall** — REINVENTED storyboards may NEVER reference Holdco Group, 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A. Hard reject with errorEnvelope.
3. **Verbatim hook delivery** — the shot covering `lines[0]` MUST set `audio_pillar` to `voice-only` or `hybrid`. Hook is delivered, not replaced by an inserted card alone.
4. **Banned hustle vocabulary** — inherited from `brief.do_not_say`; absence-checked across every `shot.action`, motion_design text, overlay_assets text (verbatim + conjugates).
5. **No-buildings rule per shot** — every `shot.setting.no_buildings_rule` populated, ≥6 chars, declares interior/black-card/closed-set framing only.
6. **Tier honoring** — shot count, complexity, locations, talent, aspects, and (Mode B) render seconds all bounded.
7. **Mode authorization defense-in-depth** — Pilot/Starter = A only · Pro = A+B · Enterprise = A+B+C. Storyboard is the third independent rejection.
8. **Caption burn parity** — every shot inherits `script.captions.burn_in_required`. No per-shot drift below Enterprise.
9. **Duration math ±5%** — strict. Sum of shot durations within ±5% of `script.duration_target_seconds`. Per-shot duration ∈ [0.4, 15].
10. **Color grade brand-locked v1.0** — REINVENTED palette only.
11. **Memory loop best-effort** — `prior_storyboards` violations emit `qc_warnings`, not errorEnvelope.
12. **2-retry max** — Self-QC failures regenerate twice. Still failing → errorEnvelope. No 3rd attempt.

## Next builds (Week 3)

After Storyboard Agent v1.0 locks:

1. **Production Coord Agent SPEC** — Day 15 (Mon May 4). Outline already shipped 5/1 — Day 15 = fill-in-the-blanks.
2. **Production Coord Agent SKILL bundle** — Day 18 (Thu May 7).
3. **Production Coord LLM execution + LOCK** — Day 19 (Fri May 8).

Per Orchestration Blueprint §5 sequence + Storyboard SPEC §16 hand-off preview.

---

*Build: May 2, 2026 (Day 13 — Sat · Week 3 Day 1)*
*Spec source: `ars/ARS-2026-04-30-Storyboard-Agent-v1-Spec.md`*
*Canon source: `ars/ARS-2026-05-01-Cross-Spec-Consistency-Review.md`*
*Mirror: `/outputs/ars/skills/storyboard-agent/` (canonical copy)*
