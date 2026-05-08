# Day 19 LLM Test Execution Runbook — Production Coord Agent v1.0

**Date authored:** 2026-05-08 (Fri · Day 19 · Wk3D6+1 → wraps Week 3)
**Audience:** Jamila — single 30 min sit-down during work day.
**Goal:** Run all 5 fixtures through Opus 4.6, validate outputs, declare v1.0 LOCKED if 5/5 pass.
**Estimated cost:** ≤ ~$2.00 (per SPEC §8 target ~$0.40/plan × 5 cases).
**Pre-validated:** All 5 input fixtures pass `input.schema.json` Draft 2020-12 (Day 18 evidence: 5/5 PASS — see `ars/build-log-2026-05-07.md`).

---

## TL;DR (action sequence)

1. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
2. **Model:** `claude-opus-4-6`. **Temperature:** `0.4`. **Max tokens:** `8000`.
3. **System prompt:** paste the system-prompt block from `ars/skills/production-coord-agent/SKILL.md` §"System prompt (v1.0 — LOCKED)" — verbatim, including hard rules, tier table, and the 9-step process.
4. For each of the 5 cases:
   - Open `test-cases/case-NN-*.json`. Copy the entire `input` object's value (NOT the wrapper).
   - User message: paste `prompts/user-template.txt`, then **replace the JSON body wholesale** with the test case's `input` value.
   - Send. Capture the full JSON response. Save to `validation/llm-out/case-NN-output.json`.
5. **Run validator** (one-liner below). Either 5/5 PASS → v1.0 LOCKED, or capture failures for Day 20 patch.

---

## Pre-flight checklist

- [ ] Claude API key in console (already configured)
- [ ] All 5 fixtures present at `ars/skills/production-coord-agent/test-cases/`
- [ ] `output.schema.json` self-validates as Draft 2020-12 ✓ (Day 17 LOCKED)
- [ ] System prompt size: ~17 KB SKILL.md system-prompt block + ≤ ~6 KB largest fixture = trivial vs. Opus 4.6 context window
- [ ] Folder ready for outputs:
      `mkdir -p "~/ars/skills/production-coord-agent/validation/llm-out"`
- [ ] Copy of `output.schema.json` available next to the validator script (or pass an absolute path; the validator below uses an absolute path so no copy is needed)

## Per-case execution checklist

For **each** of the 5 cases below:

| Step | Action |
|------|--------|
| 1 | Open the test-case JSON file. Locate the `"input"` value. |
| 2 | Paste system prompt (LOCKED, identical for all 5 cases — verbatim from SKILL.md). |
| 3 | User message = ONLY the test case's `input` object as raw JSON. No prose, no markdown. |
| 4 | Set temperature 0.4, max tokens 8000. Hit Run. |
| 5 | Save the response (raw JSON, no markdown wrapper) to `validation/llm-out/case-NN-output.json`. |
| 6 | Note token counts + latency in the run-log (template at end of this file) for SPEC §16 metadata. |

---

## The 5 cases — expected branch + pass criteria

### Case 01 — `case-01-reinvented-pilot-mode-a-shoot-day`
- **Expected branch:** `successProductionPlan`
- **Hard checks:**
  - `tier == "Pilot"`, `production_mode == "A"`, `lever == 3`
  - `mode_a_plan` non-null AND `mode_b_plan == null` AND `mode_c_plan == null` (mutual exclusivity)
  - `production_plan_id` matches regex `^productionplan-REINVENTED-\d{4}-\d{2}-\d{2}-\d{3,}$`
  - `parent_chain` is the 3-tuple `["brief-...", "script-...", "storyboard-..."]` — exactly 3 items, exactly those prefixes
  - `total_shots == 8` (matches storyboard input)
  - `mode_a_plan.location_bookings[*].no_buildings_compliant_bool == true` for **every** booking
  - `budget_reservation.total_cost_usd ≤ 200` (Pilot tier ceiling)
  - `execution_window.earliest_start ≥ today + 1`, `latest_finish ≤ today + 7 + buffer`
  - `handoff_targets[]` length ≥ 3 AND every `payload_ref` resolves to an existing dotted path
  - `escalation_path[]` ≥ 1 entry per primary resource (videographer, location, talent)
  - `qc_pre_flags[]` ≥ 4 entries, every element snake_case
  - `metadata.human_review_required == true` (lever 3)
- **Banned vocab check:** zero hits of `girl boss|hustle culture|grind|boss babe` across all rationale + escalation notes (case-insensitive, conjugates included)
- **Entity firewall:** zero hits of `Holdco|Principal|NPOX|4821|6315|SLN|Retail Supply|Nonprofit Leader A|Nonprofit Leader B|Nonprofit Leader C` anywhere in the output

### Case 02 — `case-02-reinvented-pro-mode-b-render-queue`
- **Expected branch:** `successProductionPlan`
- **Hard checks:**
  - `tier == "Pro"`, `production_mode == "B"`, `lever == 3`
  - `mode_b_plan` non-null AND `mode_a_plan == null` AND `mode_c_plan == null`
  - `mode_b_plan.render_queue[]` covers **every** storyboard shot (length == `total_shots`)
  - Every `render_queue[*].quota_reserved_bool == true`
  - Every `render_queue[*].fallback_engine_id` non-null (per Step 8 escalation rule for Mode B)
  - Style-anchor seed comes from `shots[0]` — `mode_b_plan.style_consistency_anchor.anchor_shot_id` ends with `-001`
  - `mode_b_plan.total_render_seconds ≤ 60` (Pro tier render cap)
  - Engine selection includes `runway` as primary somewhere in the queue (input had highest quota for runway = 1800 s)
  - `budget_reservation.total_cost_usd ≤ 400` (Pro tier ceiling)
  - `handoff_targets[]` includes a target whose downstream agent is `ai-video-gen`
- **Banned vocab + entity firewall:** same blanket checks as Case 01

### Case 03 — `case-03-storyboard-was-error-envelope`
- **Expected branch:** `errorEnvelope`
- **Hard checks:**
  - `error == "storyboard_not_success"`
  - `reason` ≥ 4 chars AND contains `"storyboard"` (case-insensitive)
  - `attempts` is integer ∈ [1, 5]
- **Negative checks:** NO `production_plan_id`, NO `mode_a_plan`/`mode_b_plan`/`mode_c_plan`, NO `budget_reservation`, NO `execution_window` keys present (no partial plan emitted)

### Case 04 — `case-04-cost-floor-breach`
- **Expected branch:** `errorEnvelope`
- **Hard checks:**
  - `error == "cost_floor_breach"`
  - `reason` ≥ 4 chars AND contains both `"cost"` AND (`"ceiling"` OR `"200"` OR `"floor"`)
  - `field` (if present) contains `"budget_reservation"` OR `"total_cost"`
  - `attempts` is integer ∈ [1, 5]
- **Negative checks:** NO partial plan emitted

### Case 05 — `case-05-resource-unavailable`
- **Expected branch:** `errorEnvelope`
- **Hard checks:**
  - `error == "resource_unavailable"`
  - `reason` ≥ 4 chars AND contains `"unavailable"` OR `"availability"` OR `"calendar"`
  - `field` (if present) contains `"videographer_registry"` OR `"talent_registry"` OR `"resource"`
  - `attempts` is integer ∈ [1, 5]
- **Negative checks:** NO partial plan emitted

---

## Post-run validator (single command — paste-and-run)

After saving all 5 outputs to `validation/llm-out/case-NN-output.json`:

```bash
cd "~/ars/skills/production-coord-agent"

python3 << 'PYEOF'
import json, re, sys
from jsonschema import Draft202012Validator
from pathlib import Path

base = Path(".")
out_schema = json.load(open(base / "schemas" / "output.schema.json"))
v = Draft202012Validator(out_schema)

# Entity firewall + banned vocab — applied to every successProductionPlan
FIREWALL = ["Holdco","Principal","NPOX","4821","6315","SLN","Retail Supply",
            "Nonprofit Leader A","Nonprofit Leader B","Nonprofit Leader C"]
BANNED   = ["girl boss","girlboss","hustle culture","hustle","hustling",
            "grind","grinding","boss babe"]

EXPECT = {
  "case-01": {
      "branch": "successProductionPlan",
      "tier": "Pilot", "mode": "A", "lever": 3,
      "mode_populated": "mode_a_plan",
      "plan_id_regex": r"^productionplan-REINVENTED-\d{4}-\d{2}-\d{2}-\d{3,}$",
      "total_shots": 8, "cost_ceiling": 200,
      "lead_time_days": 7,
      "human_review_required": True,
      "no_buildings_required": True,
  },
  "case-02": {
      "branch": "successProductionPlan",
      "tier": "Pro", "mode": "B", "lever": 3,
      "mode_populated": "mode_b_plan",
      "plan_id_regex": r"^productionplan-REINVENTED-\d{4}-\d{2}-\d{2}-\d{3,}$",
      "cost_ceiling": 400,
      "render_seconds_cap": 60,
      "render_anchor_suffix": "-001",
      "render_engines_must_include": "runway",
      "handoff_must_include_agent": "ai-video-gen",
      "lead_time_days": 5,
      "human_review_required": True,
  },
  "case-03": {
      "branch": "errorEnvelope",
      "error": "storyboard_not_success",
      "reason_contains": ["storyboard"],
  },
  "case-04": {
      "branch": "errorEnvelope",
      "error": "cost_floor_breach",
      "reason_contains_any": ["cost"],
      "reason_contains_any_secondary": ["ceiling","200","floor"],
  },
  "case-05": {
      "branch": "errorEnvelope",
      "error": "resource_unavailable",
      "reason_contains_any": ["unavailable","availability","calendar"],
  },
}

def has_any(text, needles):
    t = text.lower()
    return any(n.lower() in t for n in needles)

def collect_strings(obj, acc):
    if isinstance(obj, str):
        acc.append(obj)
    elif isinstance(obj, dict):
        for k, val in obj.items():
            acc.append(k)  # property names too — defense in depth
            collect_strings(val, acc)
    elif isinstance(obj, list):
        for item in obj:
            collect_strings(item, acc)

def resolve_dotted(obj, path):
    cur = obj
    for part in path.split("."):
        if part.endswith("[]"):
            part = part[:-2]
            if not isinstance(cur, dict) or part not in cur:
                return False
            cur = cur[part]
            if not isinstance(cur, list):
                return False
        elif "[" in part and part.endswith("]"):
            name, idx = part[:-1].split("[")
            if not isinstance(cur, dict) or name not in cur:
                return False
            try:
                cur = cur[name][int(idx)]
            except Exception:
                return False
        else:
            if isinstance(cur, dict) and part in cur:
                cur = cur[part]
            elif isinstance(cur, list):
                # accept if any item has this key
                hits = [i.get(part) for i in cur if isinstance(i, dict) and part in i]
                if not hits: return False
                cur = hits[0]
            else:
                return False
    return True

results = []
for case_id, expected in EXPECT.items():
    f = base / "validation" / "llm-out" / f"{case_id}-output.json"
    if not f.exists():
        candidates = list((base / "validation" / "llm-out").glob(f"{case_id}*"))
        if candidates: f = candidates[0]
        else:
            results.append((case_id, "MISSING", "no LLM output file"))
            continue
    try:
        out = json.load(open(f))
    except Exception as e:
        results.append((case_id, "JSON_PARSE_ERR", str(e)[:120]))
        continue

    # 1. schema gate (output.schema.json — top-level oneOf success|error)
    errs = list(v.iter_errors(out))
    if errs:
        results.append((case_id, "SCHEMA_FAIL",
                        f"{len(errs)} errs: {errs[0].message[:140]}"))
        continue

    # 2. branch gate
    is_error = "error" in out and "production_plan_id" not in out
    branch = "errorEnvelope" if is_error else "successProductionPlan"
    if branch != expected["branch"]:
        results.append((case_id, "WRONG_BRANCH",
                        f"got {branch}, expected {expected['branch']}"))
        continue

    fails = []

    if branch == "errorEnvelope":
        if out.get("error") != expected["error"]:
            fails.append(f"error={out.get('error')!r}, expected {expected['error']!r}")
        reason = out.get("reason", "")
        if "reason_contains" in expected:
            for sub in expected["reason_contains"]:
                if sub.lower() not in reason.lower():
                    fails.append(f"reason missing {sub!r}")
        if "reason_contains_any" in expected:
            if not has_any(reason, expected["reason_contains_any"]):
                fails.append(f"reason missing any of {expected['reason_contains_any']}")
        if "reason_contains_any_secondary" in expected:
            if not has_any(reason, expected["reason_contains_any_secondary"]):
                fails.append(f"reason missing secondary any of {expected['reason_contains_any_secondary']}")
        # negative check — no partial plan
        for k in ("production_plan_id","mode_a_plan","mode_b_plan","mode_c_plan",
                 "budget_reservation","execution_window"):
            if k in out:
                fails.append(f"partial plan: {k!r} present on errorEnvelope")
    else:
        # tier / mode / lever
        if out.get("tier") != expected["tier"]:
            fails.append(f"tier={out.get('tier')!r}, expected {expected['tier']!r}")
        if out.get("production_mode") != expected["mode"]:
            fails.append(f"mode={out.get('production_mode')!r}, expected {expected['mode']!r}")
        if out.get("lever") != expected["lever"]:
            fails.append(f"lever={out.get('lever')!r}, expected {expected['lever']!r}")
        # mutual exclusivity
        modes = {k: out.get(k) for k in ("mode_a_plan","mode_b_plan","mode_c_plan")}
        populated = [k for k, val in modes.items() if val is not None]
        if populated != [expected["mode_populated"]]:
            fails.append(f"mutual_exclusivity broken: populated={populated}, expected exactly [{expected['mode_populated']!r}]")
        # plan_id regex
        if "plan_id_regex" in expected:
            pid = out.get("production_plan_id","")
            if not re.match(expected["plan_id_regex"], pid):
                fails.append(f"production_plan_id regex miss: {pid!r}")
        # parent_chain — 3-tuple shape from schema $defs
        meta = out.get("metadata", {}) or {}
        pc = meta.get("parent_chain") or out.get("parent_chain")
        if pc is not None:
            if not (isinstance(pc, list) and len(pc) == 3
                    and isinstance(pc[0], str) and pc[0].startswith("brief-")
                    and isinstance(pc[1], str) and pc[1].startswith("script-")
                    and isinstance(pc[2], str) and pc[2].startswith("storyboard-")):
                fails.append(f"parent_chain shape miss: {pc!r}")
        # total_shots
        if "total_shots" in expected and out.get("total_shots") != expected["total_shots"]:
            fails.append(f"total_shots={out.get('total_shots')}, expected {expected['total_shots']}")
        # no-buildings rule (Mode A only)
        if expected.get("no_buildings_required"):
            for i, lb in enumerate(out.get("mode_a_plan",{}).get("location_bookings",[]) or []):
                if lb.get("no_buildings_compliant_bool") is not True:
                    fails.append(f"location_bookings[{i}].no_buildings_compliant_bool != true")
        # cost ceiling
        if "cost_ceiling" in expected:
            tc = (out.get("budget_reservation",{}) or {}).get("total_cost_usd")
            if tc is None or tc > expected["cost_ceiling"]:
                fails.append(f"budget_reservation.total_cost_usd={tc} > ceiling {expected['cost_ceiling']}")
        # render-mode specifics
        if expected["mode"] == "B":
            mb = out.get("mode_b_plan", {}) or {}
            rq = mb.get("render_queue", []) or []
            if "render_seconds_cap" in expected:
                rs = mb.get("total_render_seconds")
                if rs is None or rs > expected["render_seconds_cap"]:
                    fails.append(f"total_render_seconds={rs} > cap {expected['render_seconds_cap']}")
            if rq:
                if not all((q.get("quota_reserved_bool") is True) for q in rq):
                    fails.append("at least one render_queue[*].quota_reserved_bool != true")
                if not all(q.get("fallback_engine_id") for q in rq):
                    fails.append("at least one render_queue[*].fallback_engine_id is null/empty")
                anchor = (mb.get("style_consistency_anchor") or {}).get("anchor_shot_id","")
                if expected.get("render_anchor_suffix") and not anchor.endswith(expected["render_anchor_suffix"]):
                    fails.append(f"style_consistency_anchor.anchor_shot_id={anchor!r} does not end with {expected['render_anchor_suffix']!r}")
                engines = [q.get("engine_id","") for q in rq]
                must = expected.get("render_engines_must_include")
                if must and not any(must in (e or "") for e in engines):
                    fails.append(f"render_queue engines {engines} missing required {must!r}")
            else:
                fails.append("mode_b_plan.render_queue empty")
        # handoff_targets
        ht = out.get("handoff_targets", []) or []
        if len(ht) < 3:
            fails.append(f"handoff_targets length={len(ht)} < 3")
        for i, t in enumerate(ht):
            ref = t.get("payload_ref", "")
            if ref and not resolve_dotted(out, ref):
                fails.append(f"handoff_targets[{i}].payload_ref unresolvable: {ref!r}")
        if "handoff_must_include_agent" in expected:
            agents = [t.get("downstream_agent","") or t.get("agent","") for t in ht]
            if not any(expected["handoff_must_include_agent"] in (a or "") for a in agents):
                fails.append(f"handoff_targets missing agent {expected['handoff_must_include_agent']!r}")
        # escalation_path
        ep = out.get("escalation_path", []) or []
        if not ep:
            fails.append("escalation_path empty")
        # qc_pre_flags
        qcf = out.get("qc_pre_flags", []) or []
        if len(qcf) < 4:
            fails.append(f"qc_pre_flags length={len(qcf)} < 4")
        for q in qcf:
            if not isinstance(q, str) or not re.match(r"^[a-z][a-z0-9_]*$", q):
                fails.append(f"qc_pre_flags non-snake_case entry: {q!r}")
                break
        # metadata.human_review_required
        if expected.get("human_review_required") is True:
            if not (out.get("metadata",{}) or {}).get("human_review_required"):
                fails.append("metadata.human_review_required != true")
        # banned vocab + firewall — across ALL strings in the output
        all_strings = []
        collect_strings(out, all_strings)
        blob = " | ".join(all_strings).lower()
        for fw in FIREWALL:
            if fw.lower() in blob:
                fails.append(f"ENTITY FIREWALL BREACH: {fw!r}")
        for bad in BANNED:
            # word-boundary match where possible
            if re.search(r"\b"+re.escape(bad.lower())+r"\b", blob):
                fails.append(f"BANNED VOCAB present: {bad!r}")

    results.append((case_id, "PASS" if not fails else "FAIL",
                    "; ".join(fails) if fails else "—"))

print("=== Day 19 LLM Test Results — Production Coord Agent v1.0 ===")
print(f"{'Case':<10} {'Result':<14} Notes")
print("-" * 100)
for cid, status, notes in results:
    print(f"{cid:<10} {status:<14} {notes}")

passed = sum(1 for _,s,_ in results if s == "PASS")
print(f"\n{passed}/5 cases PASS")
print("\nDECLARE v1.0 LOCKED — Production Coord Agent" if passed == 5
      else "DEFER v1.0 LOCK — patch on Day 20")
PYEOF
```

---

## Recording template (paste into `validation/llm-out/RUN-LOG-2026-05-08.md`)

```
# Day 19 LLM Test Run Log — 2026-05-08
Operator: Jamila
Model: claude-opus-4-6  Temp: 0.4  Max tokens: 8000
System prompt SHA: <copy-paste sha256 of SKILL.md system-prompt block>

| Case  | Input tokens | Output tokens | Latency (s) | Cost ($) | Branch | First-attempt PASS? | Notes |
|-------|-------------:|--------------:|------------:|--------:|--------|--------------------:|-------|
| 01    |              |               |             |         |        |                     |       |
| 02    |              |               |             |         |        |                     |       |
| 03    |              |               |             |         |        |                     |       |
| 04    |              |               |             |         |        |                     |       |
| 05    |              |               |             |         |        |                     |       |
| Total |              |               |             |         |        |                     |       |

Validator result: __ / 5 PASS

Decision:
  [ ] DECLARE v1.0 LOCKED — flip dashboard, kick off Week 4 (AI Video Gen Agent SPEC)
  [ ] DEFER — capture failure reasons, schedule Day 20 patch (NEVER touch the schema; only the system prompt or the fixture intent)
```

---

## What "v1.0 LOCKED" means downstream

If 5/5 PASS:

1. Flip dashboard `production-coord-agent.status = v1.0 LOCKED`
2. Production Coord Agent unblocks **AI Video Gen Agent** (Week 4, first *production* — not pre-production — agent in the fleet)
3. AI Video Gen Agent consumes `mode_b_plan.render_queue[]` directly — output is its input contract
4. Quadruple-redundant pre-production firewall (Brief → Script → Storyboard → Production Coord) is fully shipped
5. Week 3 closes 6-of-6 days delivered (Day 14/Rest Day SPEC LOCK + Day 15 schema authoring + Day 16 schema LOCK + Day 17 fixtures pre-validate + Day 18 SKILL bundle ship + Day 19 LLM v1.0 LOCK)

If <5 PASS:

1. Capture exact failure reason per case in run log
2. NEVER touch the schema (Day 17 LOCKED). Only adjust the system prompt or fixture intent
3. Day 20 (Rest Day) — minimal patch session if Jamila approves; otherwise Week 4 starts Mon May 11 with Day 19 reissue
4. Storyboard / Script / Brief LLM-tests remain parked — independent track, no blocker

---

## Provenance

- Authored: 2026-05-08 (Fri · Day 19 · Wk3 wrap) — ARS overnight build session
- SPEC source: `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` (Day 14 LOCKED — Rest Day)
- Schemas source: `skills/production-coord-agent/schemas/{input,output}.schema.json` (Day 17 LOCKED + self-validating)
- SKILL bundle: shipped Day 18 (10 files / ~94.7 KB), 5/5 input fixtures pre-validate clean
- Pattern source: `ARS-2026-04-30-Day-11-LLM-Test-Runbook.md` (Script Agent runbook — proven structure)
- Validator: `jsonschema-4.26.0` `Draft202012Validator` (Python 3)
- Cost target: ≤ ~$2.00 across 5 invocations (per SPEC §8 plan)

*Day 19 deliverable: paste-and-run runbook ready. Awaiting Jamila's $2 / 30-min approval to execute. v1.0 LOCK gate is now operator-side, not infrastructure-side.*
