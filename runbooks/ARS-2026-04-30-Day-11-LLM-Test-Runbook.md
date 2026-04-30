# Day 11 LLM Test Execution Runbook — Script Agent v1.0
**Date authored:** 2026-04-30 (Thu · Day 11 · Wk2D5)
**Audience:** Jamila — single 30 min sit-down during work day.
**Goal:** Run all 5 fixtures through Opus 4.6, validate outputs, declare v1.0 LOCKED if 5/5 pass.
**Pre-validated:** All 5 input fixtures pass `input.schema.json` (Draft 2020-12). See `validation/VALIDATION-REPORT-2026-04-30.md`.

---

## TL;DR (action sequence)

1. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
2. **Model:** `claude-opus-4-6`. **Temperature:** `0.4`. **Max tokens:** `8000`.
3. **System prompt:** paste the 4-section block from `ars/skills/script-agent/SKILL.md` §"System prompt (v1.0 — LOCKED)" (lines ~73–end of fenced block).
4. For each of the 5 cases:
   - Open `test-cases/case-NN-*.json`. Copy the entire `input` object's value.
   - User message: paste `prompts/user-template.txt`, replace `{input_json}` with the input value from the test case.
   - Send. Capture the entire JSON response. Save to `validation/llm-out/case-NN-output.json`.
5. **Run validator** (one-liner below). Either 5/5 PASS → v1.0 LOCKED, or capture failures for Day 12 patch.

---

## Pre-flight checklist

- [ ] Claude API key in console (already configured)
- [ ] All 5 fixtures present at `ars/skills/script-agent/test-cases/`
- [ ] `output.schema.json` self-validates as Draft 2020-12 ✓ (confirmed 4/30)
- [ ] System prompt ≤ context window for Opus 4.6 (~16 KB SKILL.md + ~7 KB largest fixture = trivial)
- [ ] Folder ready for outputs: `mkdir -p ~/Library/Application\ Support/Claude/local-agent-mode-sessions/49211fcf-95ea-4b7b-8362-22f85de2f545/a35c3e2e-2169-41e7-a483-0bb119072d25/local_c23375b7-8963-49e9-adb8-0e65356fb339/outputs/ars/validation/llm-out/`

## Per-case execution checklist

For **each** of the 5 cases below:

| Step | Action |
|------|--------|
| 1 | Open the test-case JSON file. Locate the `"input"` value (NOT the wrapper). |
| 2 | Paste system prompt (locked, identical for all 5 cases). |
| 3 | Paste user-template, replace `{input_json}` with the input value. |
| 4 | Set temperature 0.4, max tokens 8000. Hit Run. |
| 5 | Save the response (raw JSON, no markdown wrapper) to `validation/llm-out/case-NN-output.json`. |
| 6 | Note token counts + latency in the result table below (for spec §16 metadata). |

## The 5 cases — expected branch + pass criteria

### Case 01 — `case-01-reinvented-pilot-burnout-story`
- **Expected branch:** `successScript`
- **Hard checks:** `tier=Pilot`, `production_mode=A`, `lever=3`, `lines.length` ∈ [5, 8], `broll_plan.length` ≤ 3, `platform_variants.length` = 3
- **Verbatim check:** `hook_block.spoken_line` AND `lines[0].spoken` MUST equal `"You hit seven figures and now you can't sleep. That's not success — that's a warning sign."`
- **Banned vocab check:** zero hits of `girlboss|hustle|grind|boss babe|millionaire mindset|8-figure|luxury|elevate` (incl. conjugates) across all `spoken` and `on_screen_text`
- **Entity firewall:** zero hits of `Holdco|Principal|NPOX|4821|6315|SLN|Retail Supply|Nonprofit Leader A`
- **No-buildings rule:** every `broll_plan[i].no_buildings_rule` non-empty, ≥6 chars
- **CTA timing:** `cta_block.second_start` ≥ 49

### Case 02 — `case-02-reinvented-starter-listicle-3traps`
- **Expected branch:** `successScript`
- **Hard checks:** `tier=Starter`, `production_mode=A`, `lever=3`, `lines.length` ∈ [6, 8]
- **Verbatim check:** `hook_block.spoken_line` AND `lines[0].spoken` MUST equal `"Three traps break most operators between six and seven figures. Number two will sting."`
- **Diversification check:** `lines[0].pace_marker` should NOT be `"fast-open"` (prior_scripts shows 2/2 prior were fast-open — system prompt says rotate). If pace_marker IS `fast-open`, downgrade to soft-fail and flag in `qc_warnings`.
- **Banned vocab + entity firewall + no-buildings:** same as Case 01

### Case 03 — `case-03-brief-was-error-envelope`
- **Expected branch:** `errorEnvelope`
- **Hard checks:** `error == "brief_not_success"`, `reason` contains `"brief"` AND `"errorEnvelope"`
- **Negative check:** NO `script_id`, `lines`, `hook_block` keys present (no partial script emitted)

### Case 04 — `case-04-tier-mismatch-mode-c-on-pilot`
- **Expected branch:** `errorEnvelope`
- **Hard checks:** `error == "tier_constraint_violation"`, `reason` contains `"Mode C"` AND (`"Pilot"` OR `"Enterprise"`), `field` contains `"production_mode"`
- **Negative check:** NO partial script emitted

### Case 05 — `case-05-banned-vocab-injection`
- **Expected branch:** `successScript` (with `qc_warnings`)
- **Hard checks:** `hook_block.spoken_line` AND `lines[0].spoken` equal `"Most operators don't need more output. They need a reset."`
- **Banned vocab anywhere:** zero hits of `hustle|hustling|hustled|grind|grinding|grinded` — even though operator tried to inject via `style_overrides.swap_words`
- **Warning check:** `qc_warnings` MUST contain at least one of: `style_override_swap_rejected`, `banned_vocab_swap_rejected`, `swap_words_collision`
- **Human-review flag:** `metadata.human_review_required == true`

---

## Post-run validator (single command)

After saving all 5 outputs to `validation/llm-out/case-NN-output.json`:

```bash
cd "~/Library/Application Support/Claude/local-agent-mode-sessions/49211fcf-95ea-4b7b-8362-22f85de2f545/a35c3e2e-2169-41e7-a483-0bb119072d25/local_c23375b7-8963-49e9-adb8-0e65356fb339/outputs/ars/validation"

python3 << 'PYEOF'
import json, re
from jsonschema import Draft202012Validator
from pathlib import Path

base = Path(".")
out_schema = json.load(open(base / "output.schema.json"))
v = Draft202012Validator(out_schema)

# expectations table — encoded from this runbook
EXPECT = {
  "case-01": {"branch": "successScript", "tier": "Pilot", "mode": "A",
              "verbatim_hook": "You hit seven figures and now you can't sleep. That's not success — that's a warning sign.",
              "lines_min": 5, "lines_max": 8, "broll_max": 3, "variants": 3,
              "banned": ["girlboss","hustle","grind","boss babe","millionaire mindset","8-figure","luxury","elevate"],
              "firewall": ["Holdco","Principal","NPOX","4821","6315","SLN","Retail Supply","Nonprofit Leader A"],
              "cta_start_min": 49},
  "case-02": {"branch": "successScript", "tier": "Starter", "mode": "A",
              "verbatim_hook": "Three traps break most operators between six and seven figures. Number two will sting.",
              "lines_min": 6, "lines_max": 8, "broll_max": 3, "variants": 3,
              "banned": ["girlboss","hustle","grind","boss babe","millionaire mindset","8-figure","luxury","elevate"],
              "firewall": ["Holdco","Principal","NPOX","4821","6315","SLN","Retail Supply","Nonprofit Leader A"],
              "cta_start_min": 49,
              "diversify_pace_not": "fast-open"},
  "case-03": {"branch": "errorEnvelope", "error": "brief_not_success",
              "reason_contains": ["brief", "errorEnvelope"]},
  "case-04": {"branch": "errorEnvelope", "error": "tier_constraint_violation",
              "reason_contains_any_of": [["Mode C", "Pilot"], ["Mode C", "Enterprise"]],
              "field_contains": "production_mode"},
  "case-05": {"branch": "successScript", "tier": "Pilot", "mode": "A",
              "verbatim_hook": "Most operators don't need more output. They need a reset.",
              "lines_min": 5, "lines_max": 8,
              "banned": ["hustle","hustling","hustled","grind","grinding","grinded"],
              "firewall": ["Holdco","Principal","NPOX","4821","6315","SLN","Retail Supply","Nonprofit Leader A"],
              "qc_warnings_any_of": ["style_override_swap_rejected","banned_vocab_swap_rejected","swap_words_collision"],
              "human_review_required": True}
}

results = []
for case_id, expected in EXPECT.items():
    f = base / "llm-out" / f"{case_id}-output.json"
    if not f.exists():
        # try glob fallback
        candidates = list((base / "llm-out").glob(f"{case_id}*"))
        if candidates: f = candidates[0]
        else:
            results.append((case_id, "MISSING", "no LLM output file"))
            continue
    try:
        out = json.load(open(f))
    except Exception as e:
        results.append((case_id, "JSON_PARSE_ERR", str(e)))
        continue

    # 1. schema gate
    errs = list(v.iter_errors(out))
    if errs:
        results.append((case_id, "SCHEMA_FAIL", f"{len(errs)} errs: {errs[0].message[:120]}"))
        continue

    # 2. branch gate
    is_error = "error" in out and "lines" not in out
    branch = "errorEnvelope" if is_error else "successScript"
    if branch != expected["branch"]:
        results.append((case_id, "WRONG_BRANCH", f"got {branch}, expected {expected['branch']}"))
        continue

    # 3. branch-specific checks
    fails = []
    if branch == "errorEnvelope":
        if out.get("error") != expected["error"]:
            fails.append(f"error={out.get('error')!r}, expected {expected['error']!r}")
        if "reason_contains" in expected:
            for sub in expected["reason_contains"]:
                if sub.lower() not in out.get("reason", "").lower():
                    fails.append(f"reason missing {sub!r}")
        if "reason_contains_any_of" in expected:
            ok = False
            r = out.get("reason", "").lower()
            for combo in expected["reason_contains_any_of"]:
                if all(s.lower() in r for s in combo):
                    ok = True; break
            if not ok:
                fails.append(f"reason missing any of {expected['reason_contains_any_of']}")
        if "field_contains" in expected:
            if expected["field_contains"] not in out.get("field", ""):
                fails.append(f"field missing {expected['field_contains']!r}")
        if any(k in out for k in ("script_id","lines","hook_block")):
            fails.append("partial script emitted on error branch")
    else:
        if out.get("tier") != expected["tier"]:
            fails.append(f"tier={out.get('tier')!r}, expected {expected['tier']!r}")
        if out.get("production_mode") != expected["mode"]:
            fails.append(f"mode={out.get('production_mode')!r}, expected {expected['mode']!r}")
        # verbatim hook
        h = out.get("hook_block", {}).get("spoken_line", "")
        if h != expected["verbatim_hook"]:
            fails.append(f"hook_block.spoken_line drift: got {h[:60]!r}")
        l0 = out.get("lines", [{}])[0].get("spoken", "")
        if l0 != expected["verbatim_hook"]:
            fails.append(f"lines[0].spoken drift: got {l0[:60]!r}")
        ln = len(out.get("lines", []))
        if not (expected["lines_min"] <= ln <= expected["lines_max"]):
            fails.append(f"lines.length={ln}, expected [{expected['lines_min']},{expected['lines_max']}]")
        if "broll_max" in expected and len(out.get("broll_plan", [])) > expected["broll_max"]:
            fails.append(f"broll_plan.length={len(out['broll_plan'])} > {expected['broll_max']}")
        if "variants" in expected and len(out.get("platform_variants", [])) != expected["variants"]:
            fails.append(f"platform_variants.length={len(out.get('platform_variants',[]))} != {expected['variants']}")
        # banned vocab + firewall
        all_text = " ".join([l.get("spoken","")+" "+(l.get("on_screen_text","") or "") for l in out.get("lines",[])])
        all_text += " " + h + " " + (out.get("hook_block",{}).get("first_frame_text","") or "")
        all_text_l = all_text.lower()
        for bad in expected.get("banned", []):
            if re.search(r"\b"+re.escape(bad.lower())+r"\b", all_text_l):
                fails.append(f"BANNED VOCAB present: {bad!r}")
        for fw in expected.get("firewall", []):
            if fw.lower() in all_text_l:
                fails.append(f"ENTITY FIREWALL BREACH: {fw!r}")
        if "cta_start_min" in expected:
            if out.get("cta_block",{}).get("second_start", 0) < expected["cta_start_min"]:
                fails.append(f"cta_block.second_start={out['cta_block'].get('second_start')} < {expected['cta_start_min']}")
        if "diversify_pace_not" in expected:
            if out.get("lines",[{}])[0].get("pace_marker") == expected["diversify_pace_not"]:
                fails.append(f"diversification miss: lines[0].pace_marker={expected['diversify_pace_not']!r}")
        if "qc_warnings_any_of" in expected:
            qcw = " ".join(out.get("qc_warnings", []))
            if not any(w in qcw for w in expected["qc_warnings_any_of"]):
                fails.append(f"qc_warnings missing any of {expected['qc_warnings_any_of']}")
        if expected.get("human_review_required") is True:
            if not out.get("metadata",{}).get("human_review_required"):
                fails.append("metadata.human_review_required != true")

    results.append((case_id, "PASS" if not fails else "FAIL", "; ".join(fails) if fails else "—"))

print("=== Day 11 LLM Test Results — Script Agent v1.0 ===")
print(f"{'Case':<10} {'Result':<14} Notes")
print("-" * 80)
for cid, status, notes in results:
    print(f"{cid:<10} {status:<14} {notes}")

passed = sum(1 for _,s,_ in results if s == "PASS")
print(f"\n{passed}/5 cases PASS")
print("\nDECLARE v1.0 LOCKED" if passed == 5 else "DEFER v1.0 LOCK — patch on Day 12")
PYEOF
```

## Recording template (paste into `validation/llm-out/RUN-LOG-YYYY-MM-DD.md`)

```
# Day 11 LLM Test Run Log — YYYY-MM-DD
Operator: Jamila
Model: claude-opus-4-6  Temp: 0.4  Max tokens: 8000

| Case | Tokens In | Tokens Out | Latency (s) | Result |
|------|----------:|-----------:|------------:|--------|
| case-01 | | | | |
| case-02 | | | | |
| case-03 | | | | |
| case-04 | | | | |
| case-05 | | | | |

## Validator output
[paste output from python validator above]

## Decision
[ ] v1.0 LOCKED (5/5 pass)
[ ] DEFER — patches needed on Day 12:
    - ...
```

## If something fails — triage tree

| Failure mode | Most likely cause | Day-12 patch surface |
|--------------|-------------------|----------------------|
| Hook drift (lines[0] != verbatim) | Model "improved" the hook | Strengthen hard rule #2 in system prompt; add example of verbatim copy |
| Banned vocab leak | Conjugate check missed | Tighten user-template reminder; expand banned list with conjugates explicitly |
| Wrong branch on errorEnvelope cases | Model tried to fix Brief Agent's error | Add example errorEnvelope output to system prompt |
| Schema fail (missing field) | Required field omitted | Audit system prompt §3 against output.schema.json — flag missing field name |
| Tier cap exceeded | Tier table not enforced at runtime | Embed tier table in user-template (currently in system prompt only) |
| qc_warnings missing on case-05 | Model silently rejected swap without flagging | Add explicit "WARN if you reject a style_override" rule |

## Cost guardrail

5 cases × ~7 KB input × claude-opus-4-6 ≈ ~35K input tokens + ~25K output tokens total run.
Approx cost: ~$1.50 for the full Day 11 test pass. Well under any threshold.

## Output of this run feeds

- Dashboard "Today's Output" card (Apr 30 → Apr 31 if test deferred)
- Brief Agent LLM-test pending fold (run that one in the same sit-down — same template, same harness, point at brief-agent test cases)
- Day 12 (Fri May 1) Storyboard SPEC will reference ScriptAgent v1.0 LOCKED status

---
*Authored: 2026-04-30 ARS overnight build session*
*Owner: Jamila (work-day execution) · Validator: deterministic Python (no LLM)*
*Pass criteria: 5/5 = v1.0 LOCKED*
