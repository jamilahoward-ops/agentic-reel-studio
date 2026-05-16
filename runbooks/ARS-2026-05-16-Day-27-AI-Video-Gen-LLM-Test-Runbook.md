# Day 27 LLM Test Execution Runbook — AI Video Gen Agent v1.0

**Date authored:** 2026-05-16 (Sat · Day 27 · Wk5D1 · v1.0 LOCK gate)
**Audience:** Jamila — single 30–45 min sit-down at the iMac (paste-and-run discipline).
**Goal:** Run all 5 SKILL bundle fixtures through Opus 4.6 in **dry-run mode**, validate outputs against `schemas/output.schema.json`, declare v1.0 **LOCKED** if 5/5 PASS.
**Estimated cost:** ≈ **$0.00 of engine spend** (dry-run · mock engine responses) · ~**$0.30–$0.80** Opus 4.6 inference per case × 5 ≈ **≤ $4 total LLM token spend**.
**Pre-validated:** 5/5 inputs + 5/5 expected outputs validate clean against Day 25 LOCKED schemas (Day 26 evidence: 11/11 PASS — see `ars/build-log-2026-05-15.md`).
**Mode default:** **dry-run** (Open Question #11 resolution — see §6 below). Operator can flip to **live** post-LOCK as a v1.0.1 confidence pass.
**Operator approval still required to begin:** Day 24 LOCK candidate Items 8 + 11 ratification (the 17-decision walk + this runbook's mode choice).

---

## TL;DR (action sequence)

1. **Confirm operator approval of Day 24 LOCK candidate Items 8 + 11.** If not yet ratified, stop here and walk those decisions first. Day 27 cannot promote v1.0 without them.
2. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
3. **Model:** `claude-opus-4-6`. **Temperature:** `0.3`. **Max tokens:** `12000`. **Top-p:** default.
4. **System prompt:** open `ars/skills/ai-video-gen-agent/SKILL.md`, locate the fenced block under §"System prompt (v1.0 — LOCKED, verbatim from SPEC §7)", paste **everything inside the fence** (13 hard rules + tier table + 11-step process + voice rule + final `Emit JSON only. Now.` line). No edits. No additions.
5. For each of the 5 cases:
   - Open `ars/skills/ai-video-gen-agent/test-cases/case-NN-*/input.json`. Copy the entire root object.
   - In dry-run mode, append the **Engine Stub Block** (§4 below) inside a `<engine_dry_run_mode>` fence at the **end** of the user message — this primes Opus to behave as if the named engines returned the stubbed responses. The agent's prompt body remains untouched; only the simulated engine surface changes.
   - User message = the JSON input object + the dry-run fence. No prose, no markdown around the JSON itself.
   - Send. Capture the **raw JSON output only** (strip any accidental code fence Opus emits — the system prompt forbids them, but verify). Save to `ars/skills/ai-video-gen-agent/validation/llm-out/case-NN-output.json`.
   - Note token counts + wall-clock latency in the run-log (template at end of this file) — feeds SPEC §16 metadata.
6. **Run validator** (single command, §5 below). Either **5/5 PASS → v1.0 LOCKED**, or capture failures for Day 28 (Rest Day rest) → Day 29 patch.

---

## §1 Pre-flight checklist

- [ ] **Operator ratification confirmed** — Day 24 LOCK candidate Items 8 + 11 walked + signed (Notion Action Tracker row "ARS · AI Video Gen Agent v1.0 LOCK" marked LOCKED). If pending, halt and walk decisions first.
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key in console (already configured).
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run.
- [ ] **All 5 fixtures present** at `ars/skills/ai-video-gen-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:**
      `mkdir -p "~/ars/skills/ai-video-gen-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 25 LOCKED · re-verified Day 26).
- [ ] **`input.schema.json` self-validates** ✓ (Day 25 LOCKED · 5/5 fixture pre-validation Day 26).
- [ ] **System-prompt block + largest fixture footprint** = ~22 KB SKILL prompt + ~9 KB largest input (TC-04 Enterprise 5-shot) + ~2 KB dry-run fence = **~33 KB context window**. Trivial vs Opus 4.6 200 K context window.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support).
- [ ] **No raw vendor credentials anywhere on screen.** Engine quota handles in fixtures are opaque placeholders (e.g., `"runway": "rwy-opaque-handle-001"`). Hard Rule #8 — agent never sees real credentials.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).
- [ ] **SHA-256 utility ready** for the negative-prompt verification spot-check: `python3 -c "import hashlib; print(hashlib.sha256(b'sample').hexdigest())"`.

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object** (NOT the file as wrapped JSON — the object itself). |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"System prompt (v1.0 — LOCKED, verbatim from SPEC §7)" fence — identical across all 5 cases). |
| 3 | User message = `{input object}` then a newline then the dry-run engine-stub fence (`<engine_dry_run_mode>...</engine_dry_run_mode>` — §4 below). For live mode: omit the fence (Opus dispatches real engine calls via the orchestrator layer — DO NOT run live in this iMac console session; live mode requires the v1.0.1 orchestrator harness, not Workbench). |
| 4 | Set temperature `0.3`, max tokens `12000`. Hit **Run**. |
| 5 | Wait for completion. Verify response is a **single JSON object** with no markdown fences (system prompt Hard Rule #1 — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check `metadata.session_id` in the output matches the input `session_id`. If not, halt — agent is hallucinating identifiers. |

---

## §3 The 5 cases — expected branch + pass criteria

### TC-01 — `case-01-pro-happy` (Pro · 3-shot · single-engine Runway)
- **Expected branch:** `successRenderedShots`
- **Hard checks:**
  - Top-level keys: `status: "ok"`, `rendered_shots: [3 items]`, `style_consistency_anchor`, `render_telemetry`, `handoff_targets: [≥2]`, `escalation_path: [≥0]`, `metadata` with 4-tuple `parent_chain`.
  - `rendered_shots[*].render_status` ∈ `{"rendered"}` for all 3.
  - `rendered_shots[0].shot_index == 1` AND is the anchor (matches `style_consistency_anchor.anchor_shot_id`).
  - Every `render_dispatch_log[*].negative_prompt_attached_bool == true` (schema-enforced `const`, but verify post-hoc).
  - Every `render_dispatch_log[*].negative_prompt_sha256` matches regex `^[a-f0-9]{64}$`.
  - All `negative_prompt_sha256` values **identical across all 3 dispatches** (bind-once-reuse — Process Step 4).
  - Every `rendered_shots[*].asset_uri` matches `^ars://renderset/REINVENTED/\d{4}-\d{2}-\d{2}/\d{3,}/shot-\d{3}\.[a-z0-9]+$`.
  - `render_telemetry.total_render_cost_usd_actual ≤ 440` (Pro hard ceiling = $400 × 1.10).
  - `render_telemetry.budget_variance_pct ≤ 10` (default `cost_overrun_buffer_pct`).
  - `metadata.parent_chain` is exactly the 4-tuple `["brief-...", "script-...", "storyboard-...", "productionplan-..."]` — every prefix mandatory.
  - `metadata.agent_id == "ai-video-gen-agent"` AND `metadata.agent_version == "v1.0"` AND `metadata.spec_version` contains `"v1.0"`.
  - `handoff_targets[]` includes `{agent: "edit-director", payload_ref: "rendered_shots"}` AND `{agent: "qc", payload_ref: "rendered_shots"}`.
  - `qc_pre_flags[]` ≥ 4 entries, every element snake_case.
  - No `rendered_shots[*].post_render_qc_seed.suspected_buildings_bool == true` anywhere.
- **Banned-vocab check:** zero hits of `girl boss|girlboss|hustle culture|hustle|hustling|grind|grinding|boss babe` across all rationale + prompt_compiled + qc_seed_notes (case-insensitive, conjugates).
- **Entity firewall:** zero hits of `Holdco|Principal|NPOX|4821|6315|SLN|Retail Supply|Nonprofit Leader A|Nonprofit Leader B|Nonprofit Leader C|Partner Brand|holdcogroup\.com` anywhere in the output.

### TC-02 — `case-02-enterprise-happy` (Enterprise · 5-shot · mixed engines + HeyGen talent)
- **Expected branch:** `successRenderedShots`
- **Hard checks (delta vs TC-01):**
  - `rendered_shots[]` length == 5.
  - `render_telemetry.total_render_cost_usd_actual ≤ 825` (Enterprise hard ceiling = $750 × 1.10).
  - `engine_telemetry_summary.per_engine{}` covers **all 4 distinct engines** dispatched (`runway`, `pika`, `heygen`, `kling`).
  - Every shot with `engine_id == "heygen"` has `talent_id == "jamila-howard-reinvented-v2"` (Hard Rule #9).
  - At least one shot uses `model_id == "runway-gen3-alpha-turbo"` (Enterprise-only — Hard Rule #6 + tier table).
  - At least one shot uses `model_id == "heygen-v3-polish"` (Enterprise-only — tier table).
  - `inheritance_match_score_0_1` for every inheritor ≥ 0.85 (drift threshold default — soft warning otherwise).
  - All other TC-01 checks apply (negative_prompt SHA-256 identical across all 5 dispatches · asset_uri pattern · 4-tuple parent_chain · banned-vocab + entity firewall).

### TC-03 — `case-03-anchor-failure` → `errorEnvelope` `engine_failure_unrecoverable`
- **Expected branch:** `errorEnvelope`
- **Top-level shape:** `{ "status": "blocked", "errorEnvelope": { ... }, "metadata": { ... } }`.
- **Hard checks:**
  - `errorEnvelope.failure_code == "engine_failure_unrecoverable"`.
  - `errorEnvelope.failed_check_id == 6` (Check #6 = anchor render success).
  - `errorEnvelope.attempts == 4` (primary engine 2 attempts + fallback engine 2 attempts = 4 max per Hard Rule #12).
  - `errorEnvelope.failed_shot_id == "shot-001"` (anchor).
  - `errorEnvelope.detail.anchor_shot_id == "shot-001"`.
  - `errorEnvelope.detail.engines_burned` is an array of length ≥ 2 (primary + fallback) — must include `"runway"` AND `"pika"`.
  - `errorEnvelope.detail.cost_incurred_usd > 0` (real money was spent on 4 attempts — honest accounting).
  - `errorEnvelope.detail.cost_incurred_usd ≤ 60` (sanity bound: 4 attempts × ~$15 max for 15s anchor on Runway).
- **Negative checks (Hard Rule #11 — anchor fail = whole-set blocked):**
  - NO `rendered_shots[]` array present (inheritors never dispatched).
  - NO `render_telemetry` block populated for inheritor shots (only anchor attempt telemetry, if any).
  - NO `handoff_targets[]` to edit-director or qc (set is blocked, not routed downstream).
  - NO `style_consistency_anchor` populated (anchor never rendered successfully).

### TC-04 — `case-04-cost-overrun` → `errorEnvelope` `cost_overrun`
- **Expected branch:** `errorEnvelope`
- **Hard checks:**
  - `errorEnvelope.failure_code == "cost_overrun"`.
  - `errorEnvelope.failed_check_id == 7` (Check #7 = cost ceiling compliance).
  - `errorEnvelope.attempts == 1` (cost overrun detected once at telemetry true-up — no retry possible per Hard Rule #7).
  - `errorEnvelope.detail.total_render_cost_usd_actual ≈ 852` (±$5 tolerance — engine cost is mocked deterministic).
  - `errorEnvelope.detail.tier_cost_ceiling_usd == 750` (Enterprise).
  - `errorEnvelope.detail.hard_ceiling_usd == 825` (= $750 × 1.10).
  - `errorEnvelope.detail.excess_usd ≈ 27` (±$5 tolerance).
  - `errorEnvelope.detail.excess_pct ≈ 13.6` OR present as `excess_pct_vs_estimate` (relative to estimate, not ceiling — operator semantics from Day 26 fixture).
  - `errorEnvelope.detail.per_engine_overrun_attribution{}` is a non-empty object with at least 3 engine keys (Runway + at least 2 others).
- **Negative checks (Hard Rule #7 — overrun = halt before handoff):**
  - NO `handoff_targets[]` to edit-director or qc.
  - NO `status: "ok"` (must be `"blocked"`).
  - The renders that DID complete are preserved in `errorEnvelope.detail.rendered_assets_for_forensic_review[]` per fixture canon — but they are NOT routed downstream. Verify presence but do NOT route.

### TC-05 — `case-05-quota-exhausted` → `errorEnvelope` `render_quota_exhausted`
- **Expected branch:** `errorEnvelope`
- **Hard checks:**
  - `errorEnvelope.failure_code == "render_quota_exhausted"`.
  - `errorEnvelope.failed_check_id == 5` (Check #5 = Mode B coverage).
  - `errorEnvelope.attempts == 2` (agent regenerated once at outer self-QC layer to confirm no recovery path).
  - `errorEnvelope.detail.anchor_status == "rendered"` (anchor DID complete — preserved per fixture canon).
  - `errorEnvelope.detail.failed_inheritor_shot_ids` is an array of length 2 (`["shot-002", "shot-003"]`).
  - `errorEnvelope.detail.engines_burned` includes all 4 engines touched (`runway` for anchor, `pika`+`luma` for inheritor 1 chain, `kling`+`higgsfield` for inheritor 2 chain) — but `runway` is anchor-only, so the inheritor cascade engines are `pika, luma, kling, higgsfield` — verify ≥ 4 entries.
  - `errorEnvelope.detail.cost_incurred_usd ≈ 198` (±$25 tolerance — 1 anchor + 8 burned inheritor attempts).
- **Negative checks:**
  - NO `handoff_targets[]` to edit-director or qc (set is blocked).
  - `rendered_shots[]` MAY contain the successful anchor render as a forensic artifact in `errorEnvelope.detail.partial_rendered_shots[]` — but the top-level `rendered_shots` array (the routable payload) is absent.

### Cross-fixture invariants (apply to all 5)
- `metadata.runtime_environment_class == "staging"` for dry-run mode runs (set via input `runtime_environment_class: "staging"`).
- `metadata.composed_prompt_template_sha256` populated on success branches (TC-01 + TC-02) and on cost_overrun if any dispatches happened (TC-04). Optional/absent on TC-03 (no anchor render) and TC-05 (anchor rendered, so present).
- `metadata.build_envelope_sha256` populated on every output (LOCK invariant — Cross-SPEC §3.9).
- `metadata.human_review_required == true` for `lever_state == 3` (default v1.0).

---

## §4 Dry-run engine stub block

Append the block below to the **end of the user message**, after the JSON input object. Opus 4.6 reads this as the simulated engine response surface — no real render API is dispatched. Cost ≈ $0 of engine spend.

For **live mode** (post-LOCK confidence pass, v1.0.1), omit this block — but live mode requires the orchestrator harness, NOT this Workbench-based runbook. Do not attempt live mode in this session.

```
<engine_dry_run_mode>
runtime_environment_class: "staging"
spend_cap_usd_total: 0.00
mock_engine_responses:
  runway/runway-gen3-alpha:
    case-01: { success: true, seed: "rwy-seed-tc01-anchor", latency_ms: 18000, usd: 14.25 }
    case-03/anchor: { success: false, error: "quality_below_threshold", latency_ms: 22000, usd: 11.00 }
  runway/runway-gen3-alpha-turbo:
    case-02/anchor: { success: true, seed: "rwy-turbo-seed-tc02-anchor", latency_ms: 9000, usd: 9.00 }
    case-04/anchor: { success: true, seed: "rwy-seed-tc04-anchor", latency_ms: 33000, usd: 28.50 }
  pika/pika-1.5:
    case-01/inheritors: { success: true, latency_ms: 14000, usd: 3.60 each }
    case-02/inheritors: { success: true, latency_ms: 13000, usd: 3.60 each }
    case-03/fallback: { success: false, error: "fallback_failed", latency_ms: 18000, usd: 5.40 }
    case-04/inheritors: { success: true, latency_ms: 14000, usd_actual: 18.00 each (inflated vs canon) }
    case-05/inheritor-1: { success: false, error: "rate_limited_429", latency_ms: 2000, usd: 0.00 }
  luma/luma-dream-machine:
    case-05/inheritor-1-fallback: { success: false, error: "quota_exhausted", latency_ms: 1500, usd: 0.00 }
  flux/flux-1.1:
    case-04/inheritors: { success: true, latency_ms: 16000, usd_actual: 4.00 each }
  kling/kling-1.6:
    case-02/inheritor-4: { success: true, latency_ms: 15000, usd: 6.00 }
    case-04/inheritors: { success: true, latency_ms: 15000, usd_actual: 8.00 each (inflated vs canon) }
    case-05/inheritor-2: { success: false, error: "vendor_outage_503", latency_ms: 10000, usd: 0.00 }
  higgsfield/higgsfield-v1:
    case-05/inheritor-2-fallback: { success: false, error: "rate_limited_429", latency_ms: 2000, usd: 0.00 }
  heygen/heygen-v2-clone: (unused in v1.0 fixtures)
  heygen/heygen-v3-polish:
    case-02/inheritor-2: { success: true, latency_ms: 11000, usd: 2.08, talent_id: "jamila-howard-reinvented-v2" }
    case-04/inheritor-2: { success: true, latency_ms: 11000, usd_actual: 17.00 (inflated vs canon) }
behavior_directive:
  - When invoking an engine, use the matched mock_engine_responses entry to populate render_dispatch_log[*] telemetry (seed, latency_ms, cost_incurred_usd).
  - Compute per_engine_cost_usd + total_render_cost_usd_actual + budget_variance_pct from the matched usd values verbatim.
  - Compute negative_prompt_sha256 honestly (SHA-256 of the composed negative prompt — this is the one piece NOT mocked).
  - Compute composed_prompt_template_sha256 honestly (SHA-256 of the composed positive prompt template scaffold).
  - For TC-03 (anchor failure), exhaust 4 attempts on runway+pika per Hard Rule #12, then emit engine_failure_unrecoverable.
  - For TC-04 (cost overrun), all dispatches succeed but total cost exceeds $825 hard ceiling → emit cost_overrun at Step 8.
  - For TC-05 (quota exhausted), anchor succeeds, both inheritor chains exhaust 4 attempts each → emit render_quota_exhausted at Step 11 Check #5.
  - Treat this block as binding for engine-layer behavior ONLY. All other Hard Rules + Process Steps + Self-QC Checks remain in full force.
</engine_dry_run_mode>
```

**Why this works:** the SKILL system prompt is engine-agnostic at the LLM layer — it composes prompts and reasons about retry policy, cost ceilings, anchor-first sequencing, and 12-check self-QC. The actual engine dispatch is normally handled by the orchestrator. In dry-run mode, the orchestrator's engine surface is replaced by these stubbed responses. Opus 4.6 reasons through the full agent loop using the stubbed engine behavior, producing the same shape of output it would produce against real engines. Validation against `output.schema.json` + the fixture expected_output diff catches any drift.

**Cost discipline:** every `usd:` value in the stub is real-money-honest — it matches what an actual render would cost per `vendor_pricing_canon.json`. The agent's cost ceiling math operates on the same numbers a real run would. TC-04's overrun is engineered: stubs are inflated above canon to push past $825.

---

## §5 Post-run validator (paste-and-run)

After saving all 5 outputs to `validation/llm-out/case-NN-output.json`:

```bash
cd "~/ars/skills/ai-video-gen-agent"

python3 << 'PYEOF'
import json, re, sys, hashlib
from jsonschema import Draft202012Validator
from pathlib import Path

ROOT = Path(".")
OUT_SCHEMA = json.loads((ROOT / "schemas" / "output.schema.json").read_text())
v = Draft202012Validator(OUT_SCHEMA)

FIREWALL = ["Holdco","Principal","NPOX","4821","6315","SLN","Retail Supply",
            "Nonprofit Leader A","Nonprofit Leader B","Nonprofit Leader C","Partner Brand","holdcogroup.com"]
BANNED   = ["girl boss","girlboss","hustle culture","hustle","hustling",
            "grind","grinding","boss babe"]

EXPECT = {
  "case-01-pro-happy": {
    "branch": "success",
    "rendered_count": 3,
    "cost_ceiling_hard": 440.0,    # Pro $400 × 1.10
    "anchor_index": 1,
    "shot_id_anchor": "shot-001",
    "brand_id_prefix_in_asset_uri": "REINVENTED",
    "engines_distinct_count_min": 1,
    "engines_must_include": ["runway"],
  },
  "case-02-enterprise-happy": {
    "branch": "success",
    "rendered_count": 5,
    "cost_ceiling_hard": 825.0,    # Enterprise $750 × 1.10
    "anchor_index": 1,
    "shot_id_anchor": "shot-001",
    "brand_id_prefix_in_asset_uri": "REINVENTED",
    "engines_distinct_count_min": 4,
    "engines_must_include": ["runway","pika","heygen","kling"],
    "model_ids_must_include": ["runway-gen3-alpha-turbo","heygen-v3-polish"],
    "heygen_talent_id_required": "jamila-howard-reinvented-v2",
  },
  "case-03-anchor-failure": {
    "branch": "error",
    "failure_code": "engine_failure_unrecoverable",
    "failed_check_id": 6,
    "attempts": 4,
    "failed_shot_id": "shot-001",
    "detail_engines_burned_must_include": ["runway","pika"],
    "cost_incurred_usd_max": 60.0,
    "no_rendered_shots": True,
    "no_handoff_targets": True,
  },
  "case-04-cost-overrun": {
    "branch": "error",
    "failure_code": "cost_overrun",
    "failed_check_id": 7,
    "attempts": 1,
    "detail_total_render_cost_usd_actual_min": 825.0,
    "detail_tier_cost_ceiling_usd": 750.0,
    "no_handoff_targets": True,
  },
  "case-05-quota-exhausted": {
    "branch": "error",
    "failure_code": "render_quota_exhausted",
    "failed_check_id": 5,
    "attempts": 2,
    "detail_engines_burned_min_count": 4,
    "detail_failed_inheritor_count": 2,
    "no_handoff_targets": True,
  },
}

ASSET_URI_RE = re.compile(r"^ars://renderset/[A-Z][A-Z0-9_-]*/\d{4}-\d{2}-\d{2}/\d{3,}/shot-\d{3}\.[a-z0-9]+$")
SHA256_RE    = re.compile(r"^[a-f0-9]{64}$")
PLAN_PARENT_RE = re.compile(r"^productionplan-")

def collect_strings(obj, acc):
    if isinstance(obj, str):
        acc.append(obj)
    elif isinstance(obj, dict):
        for k, val in obj.items():
            acc.append(k)
            collect_strings(val, acc)
    elif isinstance(obj, list):
        for item in obj:
            collect_strings(item, acc)

def has_any(text, needles):
    t = text.lower()
    return any(n.lower() in t for n in needles)

def get_path(obj, *keys, default=None):
    cur = obj
    for k in keys:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return default
    return cur

results = []
for case_id, expected in EXPECT.items():
    f = ROOT / "validation" / "llm-out" / f"{case_id}-output.json"
    if not f.exists():
        results.append((case_id, "MISSING", "no LLM output file"))
        continue
    try:
        out = json.loads(f.read_text())
    except Exception as e:
        results.append((case_id, "JSON_PARSE_ERR", str(e)[:160]))
        continue

    # 1. schema gate
    errs = list(v.iter_errors(out))
    if errs:
        results.append((case_id, "SCHEMA_FAIL", f"{len(errs)} errs · first: {errs[0].message[:160]}"))
        continue

    # 2. branch detection
    has_envelope = isinstance(out.get("errorEnvelope"), dict)
    has_rendered = isinstance(out.get("rendered_shots"), list)
    branch = "error" if has_envelope else ("success" if has_rendered else "unknown")
    if branch != expected["branch"]:
        results.append((case_id, "WRONG_BRANCH", f"got {branch}, expected {expected['branch']}"))
        continue

    fails = []
    all_strings = []
    collect_strings(out, all_strings)
    joined = "\n".join(s for s in all_strings if isinstance(s, str))

    # Universal firewall + banned-vocab walk (defense-in-depth, also runs on errorEnvelope)
    for f_term in FIREWALL:
        if f_term.lower() in joined.lower():
            fails.append(f"entity_firewall_leak: {f_term!r}")
    for b_term in BANNED:
        if b_term.lower() in joined.lower():
            fails.append(f"banned_vocab_leak: {b_term!r}")

    # parent_chain shape (4-tuple at output) — applies wherever metadata present
    meta = out.get("metadata", {}) or {}
    pc = meta.get("parent_chain")
    if pc is not None:
        if not (isinstance(pc, list) and len(pc) == 4
                and pc[0].startswith("brief-")
                and pc[1].startswith("script-")
                and pc[2].startswith("storyboard-")
                and PLAN_PARENT_RE.match(pc[3])):
            fails.append(f"parent_chain shape miss: {pc!r}")
    if meta.get("agent_id") != "ai-video-gen-agent":
        fails.append(f"metadata.agent_id={meta.get('agent_id')!r}, expected 'ai-video-gen-agent'")
    if not (meta.get("agent_version") or "").startswith("v1.0"):
        fails.append(f"metadata.agent_version={meta.get('agent_version')!r}")

    if branch == "success":
        # rendered_shots length
        rs = out.get("rendered_shots", [])
        if len(rs) != expected["rendered_count"]:
            fails.append(f"rendered_shots len={len(rs)}, expected {expected['rendered_count']}")
        # anchor identity
        anchor = next((s for s in rs if s.get("shot_index") == expected["anchor_index"]), None)
        if not anchor:
            fails.append(f"no anchor shot with shot_index={expected['anchor_index']}")
        elif anchor.get("shot_id") != expected["shot_id_anchor"]:
            fails.append(f"anchor.shot_id={anchor.get('shot_id')!r}, expected {expected['shot_id_anchor']!r}")
        # render_status all rendered
        for i, s in enumerate(rs):
            if s.get("render_status") != "rendered":
                fails.append(f"rendered_shots[{i}].render_status={s.get('render_status')!r}, expected 'rendered'")
            uri = s.get("asset_uri","")
            if not ASSET_URI_RE.match(uri):
                fails.append(f"rendered_shots[{i}].asset_uri pattern fail: {uri!r}")
        # cost ceiling
        rt = out.get("render_telemetry", {}) or {}
        cost = rt.get("total_render_cost_usd_actual")
        if cost is None or cost > expected["cost_ceiling_hard"]:
            fails.append(f"render_telemetry.total_render_cost_usd_actual={cost}, ceiling {expected['cost_ceiling_hard']}")
        # negative_prompt SHA-256 invariant: all dispatches share one hash
        dispatches = []
        for s in rs:
            for d in (s.get("render_dispatch_log") or []):
                dispatches.append(d)
        sha_set = set()
        for d in dispatches:
            if d.get("negative_prompt_attached_bool") is not True:
                fails.append("negative_prompt_attached_bool != true on a dispatch (schema should have blocked!)")
            sha = d.get("negative_prompt_sha256","")
            if not SHA256_RE.match(sha):
                fails.append(f"negative_prompt_sha256 regex fail: {sha!r}")
            else:
                sha_set.add(sha)
        if len(sha_set) > 1:
            fails.append(f"negative_prompt_sha256 NOT identical across dispatches: {len(sha_set)} distinct hashes")
        # engines coverage
        engines_used = {(s.get("engine_id") or "").lower() for s in rs}
        if len(engines_used) < expected.get("engines_distinct_count_min", 0):
            fails.append(f"distinct engines={len(engines_used)} < min {expected['engines_distinct_count_min']}")
        for must in expected.get("engines_must_include", []):
            if not any(must in e for e in engines_used):
                fails.append(f"engines missing required {must!r}; saw {engines_used}")
        for must_model in expected.get("model_ids_must_include", []):
            if not any((s.get("model_id") or "") == must_model for s in rs):
                fails.append(f"model_ids missing required {must_model!r}")
        # HeyGen talent
        if expected.get("heygen_talent_id_required"):
            heygen_shots = [s for s in rs if (s.get("engine_id") or "").lower() == "heygen"]
            for s in heygen_shots:
                if s.get("talent_id") != expected["heygen_talent_id_required"]:
                    fails.append(f"HeyGen shot talent_id={s.get('talent_id')!r}, expected {expected['heygen_talent_id_required']!r}")
        # handoff_targets
        ht = out.get("handoff_targets", []) or []
        agents_referenced = {(t.get("agent") or "").lower() for t in ht}
        for required in ("edit-director","qc"):
            if required not in agents_referenced:
                fails.append(f"handoff_targets missing required agent {required!r}")
        # qc_pre_flags
        qp = out.get("qc_pre_flags") or rt.get("qc_pre_flags") or []
        if len(qp) < 4:
            fails.append(f"qc_pre_flags count={len(qp)} < 4")
        # suspected_buildings
        for i, s in enumerate(rs):
            sb = ((s.get("post_render_qc_seed") or {}).get("suspected_buildings_bool"))
            if sb is True:
                fails.append(f"rendered_shots[{i}].post_render_qc_seed.suspected_buildings_bool == true (Hard Rule #5 violation)")

    else:
        env = out.get("errorEnvelope", {}) or {}
        if env.get("failure_code") != expected["failure_code"]:
            fails.append(f"failure_code={env.get('failure_code')!r}, expected {expected['failure_code']!r}")
        if env.get("failed_check_id") != expected["failed_check_id"]:
            fails.append(f"failed_check_id={env.get('failed_check_id')}, expected {expected['failed_check_id']}")
        if env.get("attempts") != expected["attempts"]:
            fails.append(f"attempts={env.get('attempts')}, expected {expected['attempts']}")
        if "failed_shot_id" in expected:
            if env.get("failed_shot_id") != expected["failed_shot_id"]:
                fails.append(f"failed_shot_id={env.get('failed_shot_id')!r}, expected {expected['failed_shot_id']!r}")
        detail = env.get("detail", {}) or {}
        if "detail_engines_burned_must_include" in expected:
            burned = [str(x).lower() for x in (detail.get("engines_burned") or [])]
            for must in expected["detail_engines_burned_must_include"]:
                if not any(must in b for b in burned):
                    fails.append(f"detail.engines_burned missing {must!r}; saw {burned}")
        if "detail_engines_burned_min_count" in expected:
            burned = detail.get("engines_burned") or []
            if len(burned) < expected["detail_engines_burned_min_count"]:
                fails.append(f"detail.engines_burned count={len(burned)} < {expected['detail_engines_burned_min_count']}")
        if "cost_incurred_usd_max" in expected:
            ci = detail.get("cost_incurred_usd")
            if ci is None or ci > expected["cost_incurred_usd_max"]:
                fails.append(f"detail.cost_incurred_usd={ci} > max {expected['cost_incurred_usd_max']}")
        if "detail_total_render_cost_usd_actual_min" in expected:
            tc = detail.get("total_render_cost_usd_actual")
            if tc is None or tc < expected["detail_total_render_cost_usd_actual_min"]:
                fails.append(f"detail.total_render_cost_usd_actual={tc} < min {expected['detail_total_render_cost_usd_actual_min']}")
        if "detail_tier_cost_ceiling_usd" in expected:
            tcl = detail.get("tier_cost_ceiling_usd")
            if tcl != expected["detail_tier_cost_ceiling_usd"]:
                fails.append(f"detail.tier_cost_ceiling_usd={tcl}, expected {expected['detail_tier_cost_ceiling_usd']}")
        if "detail_failed_inheritor_count" in expected:
            fi = detail.get("failed_inheritor_shot_ids") or []
            if len(fi) != expected["detail_failed_inheritor_count"]:
                fails.append(f"detail.failed_inheritor_shot_ids count={len(fi)}, expected {expected['detail_failed_inheritor_count']}")
        if expected.get("no_rendered_shots") and isinstance(out.get("rendered_shots"), list) and out["rendered_shots"]:
            fails.append("rendered_shots present on error branch (Hard Rule #11 / anchor halt violation)")
        if expected.get("no_handoff_targets"):
            ht = out.get("handoff_targets") or []
            if ht and any(t.get("agent") in ("edit-director","qc") for t in ht):
                fails.append("handoff_targets to edit-director/qc on error branch (should be absent — set is blocked)")
        # top-level status must be "blocked"
        if out.get("status") not in ("blocked", "error"):
            fails.append(f"top-level status={out.get('status')!r}, expected 'blocked'")

    if fails:
        results.append((case_id, "FAIL", " || ".join(fails[:8])))
    else:
        results.append((case_id, "PASS", "all checks green"))

print()
print("=" * 78)
print("Day 27 LLM Test Runbook — AI Video Gen Agent v1.0 — VALIDATOR RESULTS")
print("=" * 78)
pass_n = 0
for case_id, status, note in results:
    icon = "PASS " if status == "PASS" else "FAIL "
    print(f"  {icon} {case_id:30s}  ::  {status:18s}  {note[:200]}")
    if status == "PASS":
        pass_n += 1
print("-" * 78)
print(f"  Aggregate: {pass_n}/{len(results)} PASS")
if pass_n == len(results):
    print("  >> v1.0 LOCK GATE = OPEN. Operator may flip version tag.")
else:
    print(f"  >> v1.0 LOCK GATE = HELD. {len(results) - pass_n} failure(s) require patch.")
print("=" * 78)
sys.exit(0 if pass_n == len(results) else 1)
PYEOF
```

Save the printed validator output as a screenshot OR redirect to a file: append ` > validation/llm-out/run-results-2026-05-16.txt 2>&1` to the bash command above.

---

## §6 Open Question #11 resolution — dry-run vs live

**Decision:** **dry-run mode is the v1.0 LOCK gate.**

**Why:**
- v1.0 LOCK is about proving the agent's **reasoning + schema compliance + cost discipline** loops execute correctly. None of those require real engine API calls — they require Opus 4.6 to consume mocked engine responses and produce schema-valid, contract-compliant outputs.
- Live mode burns real money on engines whose responses are not deterministic. A v1.0 LOCK that depends on non-deterministic engine output is not a LOCK — it's a probability distribution.
- The vendor pricing canon (`vendor_pricing_canon.json`) is RESEARCH-ONLY per Day 24 LOCK candidate Item 3 flag. Live mode would assert canon accuracy against vendor reality — that's a different gate (v1.0.1 confidence pass) and properly gated on the operator URL walkthrough first.
- Cost: dry-run = ~$4 in Opus tokens. Live mode worst case = ≤ $1,000 (1 Pro happy + 1 Enterprise happy live render) and requires the orchestrator harness, not Workbench. Disproportionate cost-to-gate-value for v1.0 LOCK.

**Promotion rule (post-LOCK):**
- Day 27 5/5 PASS + Day 24 LOCK candidate Items 8 + 11 ratified → version tag flips `v1.0-LOCK-CANDIDATE-day-24` → **`v1.0-LOCKED-day-27`** in `skills/ai-video-gen-agent/SKILL.md` frontmatter `status:` field AND in Notion Action Tracker row "ARS · AI Video Gen Agent v1.0 LOCK".
- v1.0.1 confidence pass (live mode, orchestrator harness) is queued for **after** the operator vendor URL walkthrough completes. Scope: 1 Pro happy + 1 Enterprise happy live render. Worst case spend ceiling: $1,000. Operator pre-approves before any live dispatch.

**If 5/5 do NOT pass on Day 27:**
- Day 28 (Sun May 17) is **Rest Day rest** per Future Jamila 2033 directive — no build.
- Day 29 (Mon May 18) = first-pass patch on whichever case(s) failed. Patch SKILL.md system prompt only if needed (schema is LOCKED — no schema changes without a new v1.0.x version). Most failures will be system-prompt clarity issues solvable by tightening 1–2 hard rules' wording.
- Re-run failed cases. If 5/5 PASS on re-run → v1.0 LOCK still ships Day 29 with a `v1.0-LOCKED-day-29-patched-from-day-27` version tag.

---

## §7 What this run unlocks (post-PASS)

| Unlocked | Why |
|----------|-----|
| **Mode B production gate goes LIVE** — operator can ship paid renders on the AI Video Gen Agent | Bundle is the runtime contract; LOCK promotes the contract to production-eligible |
| **Style Replication Agent SPEC outline kickoff (Mode C / Week 5)** | AI Video Gen LOCK clears the last pre-Mode-C dependency — Style Replication inherits from rendered_shots anchor + style_consistency_anchor |
| **Cross-SPEC §3 canon promoted from "outline pattern" to "production pattern"** | All 5 production-side agents now LOCKED (Brief / Script / Storyboard / ProdCoord / AI Video Gen) — the pattern is empirically validated, not theoretical |
| **Week 4 closes with all SPEC deliverables shipped** | Week 5 starts Sunday/Monday with the Mode C / 30-reel Lever-2 graduation gate clear runway |
| **First Sequel Digital paid Mode B reel can be quoted** | Pro tier Starter-tier or Enterprise offers carry contractually defensible delivery promise (agent + schema + LOCKED runbook + validation evidence trail) |

---

## §8 Run-log template (fill in after each case)

Copy this block 5x (one per case) into `validation/llm-out/run-log-2026-05-16.md`.

```
## Case: case-NN-<slug>

- **Run timestamp (UTC):** 2026-05-16THH:MM:SSZ
- **Mode:** dry-run | live
- **Model:** claude-opus-4-6
- **Temperature:** 0.3
- **Max tokens:** 12000
- **Input tokens:** ____
- **Output tokens:** ____
- **Wall-clock seconds:** ____
- **Output file:** validation/llm-out/case-NN-<slug>-output.json
- **Output size (bytes):** ____
- **Branch emitted:** successRenderedShots | errorEnvelope
- **Top-level status:** ok | blocked
- **negative_prompt_sha256 (first dispatch, if applicable):** ____
- **composed_prompt_template_sha256 (if applicable):** ____
- **Validator result (from §5 validator):** PASS | FAIL
- **If FAIL — first failure note:** ____________________
- **Spot-check notes (free-text ≤200 chars):** ____________________
```

---

## §9 Aggregate scoring sheet

After all 5 cases run, fill in:

| Case | Branch expected | Branch emitted | Validator | Notes |
|------|----------------|----------------|-----------|-------|
| TC-01 case-01-pro-happy | successRenderedShots | _____ | _____ | _____ |
| TC-02 case-02-enterprise-happy | successRenderedShots | _____ | _____ | _____ |
| TC-03 case-03-anchor-failure | errorEnvelope (engine_failure_unrecoverable) | _____ | _____ | _____ |
| TC-04 case-04-cost-overrun | errorEnvelope (cost_overrun) | _____ | _____ | _____ |
| TC-05 case-05-quota-exhausted | errorEnvelope (render_quota_exhausted) | _____ | _____ | _____ |

**Aggregate:** ___ / 5 PASS

**v1.0 LOCK gate decision:**
- [ ] **5/5 PASS** → flip SKILL.md `status:` from `SKILL bundle SHIPPED — LLM execution Day 27 (Sat May 16) locks v1.0` to `v1.0 LOCKED — Day 27 (Sat May 16)`. Mark Notion Action Tracker row LOCKED. Schedule Style Replication SPEC outline kickoff for Day 29 (Mon May 18 — Day 28 is Rest Day).
- [ ] **<5/5 PASS** → log failure(s) + patch the offending system-prompt clause(s) in SKILL.md (only — schemas are LOCKED). Re-run failed cases on Day 29 (post-Rest Day). Do NOT promote until 5/5.

---

## §10 Guardrails (do not skip)

- **No live engine dispatch in this Workbench session.** Live mode = orchestrator harness only. Confirm dry-run fence is in every user message.
- **No credentials anywhere.** `engine_quota_handles` values are opaque placeholders. The dry-run fence does not request credentials. If Opus asks for a credential in any response, abort — Hard Rule #8 violation.
- **No schema edits.** Day 25 schemas are LOCKED. Any drift between agent output and schema is an agent issue, not a schema issue.
- **No silent v1.0 promotion on partial PASS.** 4/5 PASS = v1.0 LOCK held. The contract is 5/5 or nothing.
- **No external comms triggered by this runbook.** Validator output is internal evidence. No client emails, no investor pings, no social posts derive from this run.
- **No financial commitments.** Dry-run mode = ~$4 Opus tokens. Live mode (v1.0.1) requires explicit operator approval AND a spend ceiling pre-set.
- **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED ops on this run. (REINVENTED is the brand inside the fixtures — that's brand-as-pilot-customer, not entity ownership.)

---

## §11 Files produced by this runbook

After the run completes (regardless of pass/fail outcome):

- `validation/llm-out/case-NN-<slug>-output.json` × 5 — raw Opus output per case
- `validation/llm-out/run-log-2026-05-16.md` — run-log template filled in × 5
- `validation/llm-out/run-results-2026-05-16.txt` — captured validator script output
- (On 5/5 PASS) Update `skills/ai-video-gen-agent/SKILL.md` frontmatter `status:` field
- (On 5/5 PASS) Update Notion Action Tracker row "ARS · AI Video Gen Agent v1.0 LOCK" → LOCKED

---

## §12 Sources consulted in authoring this runbook

- `ars/skills/ai-video-gen-agent/SKILL.md` (Day 26 LOCKED system prompt verbatim)
- `ars/skills/ai-video-gen-agent/schemas/{input,output}.schema.json` (Day 25 LOCKED)
- `ars/skills/ai-video-gen-agent/vendor_pricing_canon.json` (Day 23/26 RESEARCH-ONLY)
- `ars/skills/ai-video-gen-agent/test-cases/case-NN-*/scenario.md` × 5 (Day 25/26 fixture canon)
- `ars/ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` (Day 24 LOCK candidate)
- `ars/ARS-2026-05-08-Day-19-Production-Coord-LLM-Test-Runbook.md` (Day 19 ProdCoord runbook — structural pattern inheritance)
- `ars/ARS-2026-04-30-Day-11-LLM-Test-Runbook.md` (Day 11 Script Agent runbook — paste-and-run pattern inheritance)
- `ars/build-log-2026-05-15.md` (Day 26 build log — Day 27 runway specification)

---

*Day 27 authored ahead of the iMac sit-down so the operator can paste-and-run without re-deriving any step. Dry-run mode is the v1.0 LOCK gate. Live mode is queued for v1.0.1 post-LOCK confidence pass, gated on the operator vendor URL walkthrough completing first. 5/5 PASS = v1.0 LOCKED + Style Replication SPEC outline kickoff Day 29 (Mon May 18 — Day 28 is Rest Day). Cost discipline maintained: ≤ $4 Opus tokens spend ceiling on this entire LOCK gate.*
