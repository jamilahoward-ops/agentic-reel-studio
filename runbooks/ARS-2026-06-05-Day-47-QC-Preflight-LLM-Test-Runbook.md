# Day 47 LLM Test Execution Runbook — QC Pre-flight Agent v1.0

**Date authored:** 2026-06-05 (Fri · Day 47 · Wk7D4 · post-launch hardening window · v1.0 LOCK gate)
**Audience:** Jamila — single 20–35 min sit-down at the iMac (paste-and-run discipline).
**Goal:** Run all 5 SKILL bundle fixtures through Opus 4.6, validate outputs against `schemas/output.schema.json`, declare QC Pre-flight v1.0 **LOCKED** if 5/5 PASS — IF AND ONLY IF **both** production-tier predecessor LOCK ceremonies (AI Video Gen v1.0 + Style Replication v1.0) close first (HARD GATE per Day 44 LOCK CANDIDATE — QC Pre-flight consumes both as input branches; it cannot be the terminal gate until the agents it gates are themselves LOCKED).
**Estimated cost:** **$0.00 of engine spend** (QC Pre-flight calls NO engine, by design) · ~**$0.40–$0.70** Opus 4.6 inference per case × 5 ≈ **≤ $3.50 total LLM token spend**. This is the **cheapest runbook in the fleet** — there is no render dispatch in either dry-run *or* live, because the agent never touches an engine.
**Pre-validated:** Both schemas META-SCHEMA VALID (Day 45). Full bundle `validate.py` 34/34 green Day 46 (meta-schema ×2 + 10 fixture validations + 14 adversarial guards + parent_chain backward-compat + input guards + TC-03 gating). The §5 validator below extends that harness to score live LLM output against the 5 fixture expectations.
**Mode default:** **dry-run** (Open Question #47 resolution — see §6). Because QC Pre-flight dispatches no engine, "dry-run" and "live" are nearly identical (both reasoning-only); the only difference is the optional native pHash/CLIP drift re-verify (~$0.001/shot), which is NOT exercised by any of the 5 fixtures. Dry-run is the v1.0 LOCK gate.
**Operator approval still required to begin:** AI Video Gen v1.0 LOCK ceremony CLOSED **and** Style Replication v1.0 LOCK ceremony CLOSED (both hard gates), **plus** QC-local Day 44 LOCK CANDIDATE Items 6 + 8 + 11 ratified.

---

## TL;DR (action sequence)

1. **Confirm AI Video Gen v1.0 LOCK ceremony has CLOSED.** Day 24 Items 8 + 11 ratified · Day 27 5/5 PASS verdict in · Notion row "ARS · AI Video Gen Agent v1.0 LOCK" marked LOCKED · dashboard chip flipped to `live`. **HARD GATE #1.** If pending, stop — QC Pre-flight LOCK cannot proceed.
2. **Confirm Style Replication v1.0 LOCK ceremony has CLOSED.** Day 32 Items 6 + 8 + 11 ratified · Day 36 5/5 PASS verdict in · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.** If pending, stop.
3. **Confirm QC Pre-flight Day 44 LOCK CANDIDATE Items 6 + 8 + 11 are operator-ratified.** Item 6 = inherited combined-ceiling confirm ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter Mode A). Item 8 = the 14 critical decisions walk (PRELIMINARY #4 + #13 require explicit verdict). Item 11 = Cross-SPEC §3.9 n-tuple amendment (the 6-tuple `parent_chain` forcing function; schema currently holds `minItems: 5`).
4. **Optional:** Run `cd "~/ars/skills/qc-preflight-agent/" && python3 validate.py` in a fresh Python process for the canonical 34/34 bundle stamp. ~20 sec. Not gated — confirmed green Day 46.
5. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
6. **Model:** `claude-opus-4-6`. **Temperature:** `0.2`. **Max tokens:** `8000`. **Top-p:** default.
   *(Assumption stated: QC Pre-flight runs colder than the production agents' 0.4. It is a deterministic adjudication gate — it composes nothing creative; it walks fixed checklists and emits a verdict. A lower temperature reduces evidence-field paraphrase variance without affecting the verdict logic. Operator may raise to 0.4 to match fleet default; verdicts are temperature-stable.)*
7. **System prompt:** open `ars/skills/qc-preflight-agent/SKILL.md`, locate the fenced block under §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)", paste **everything inside the fence** (12 hard rules + 11-point Brand Voice QC gate inlined + universal-tier table + 11-step verdict loop + voice rule + "Emit JSON only. Now."). No edits. No additions.
8. For each of the 5 cases:
   - Open `ars/skills/qc-preflight-agent/test-cases/case-NN-*/input.json`. Copy the **entire root object**.
   - User message = the JSON input object **only**. **No engine-stub fence** — QC Pre-flight reads no engine surface; everything it adjudicates (replicated_shots, rendered_shots, production_plan, cost_ledger, accumulated_qc_pre_flags, metadata) is already inside the input object. No prose, no markdown around the JSON.
   - Send. Capture the **raw JSON output only** (strip any accidental code fence — Hard Rule #1 forbids them, but verify). Save to `ars/skills/qc-preflight-agent/validation/llm-out/case-NN-output.json`.
   - Note token counts + wall-clock latency in the run-log (§8 template).
9. **Run validator** (single command, §5). Either **5/5 PASS → QC Pre-flight v1.0 LOCKED ceremony executable**, or capture failures for a Day 48 patch session.

---

## §1 Pre-flight checklist (13 items)

- [ ] **AI Video Gen v1.0 LOCK ceremony CLOSED.** Day 24 Items 8 + 11 ratified · Day 27 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #1.**
- [ ] **Style Replication v1.0 LOCK ceremony CLOSED.** Day 32 Items 6 + 8 + 11 ratified · Day 36 5/5 PASS · Notion row LOCKED · dashboard chip `live`. **HARD GATE #2.** (Both production-tier LOCKs must be CLOSED before QC Pre-flight — the terminal gate cannot LOCK ahead of the agents it gates.)
- [ ] **QC Pre-flight Day 44 LOCK CANDIDATE Items 6 + 8 + 11 ratified.** PRELIMINARY decisions #4 + #13 have explicit RATIFY/AMEND/DEFER verdicts. Cross-SPEC §3.9 n-tuple amendment carries operator signature (or is explicitly DEFERRED — see §6 note on the 6-tuple).
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key already configured.
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run. *(For QC Pre-flight these are functionally identical — no engine in either.)*
- [ ] **All 5 fixtures present** at `ars/skills/qc-preflight-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:** `mkdir -p "~/ars/skills/qc-preflight-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 45 LOCKED-as-drafted · re-verified Day 46 `validate.py`).
- [ ] **`input.schema.json` self-validates** ✓ (Day 45 · 5/5 fixtures green Day 46).
- [ ] **System-prompt + largest fixture footprint** = ~7.5 KB SKILL prompt + ~3.5 KB largest input (TC-05 drift, 3,546 B) = **~11 KB context window**. Trivial vs Opus 4.6 200 K context.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support).
- [ ] **No raw vendor credentials anywhere on screen.** QC Pre-flight references NO credentials (Hard Rule #2 — it calls no engine). If Opus emits a credential or composes an engine prompt in any response, abort — the agent has misunderstood its job.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object**. |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"SYSTEM PROMPT — v1.0" fence — identical across all 5 cases). |
| 3 | User message = `{input object}` only. **No fence, no stub, no prose.** QC Pre-flight reads no engine; the input carries everything it adjudicates. |
| 4 | Set temperature `0.2`, max tokens `8000`. Hit **Run**. |
| 5 | Wait for completion. Verify the response is a **single JSON object** with no markdown fences (Hard Rule #1 — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check: `metadata.agent_id == "qc-preflight-agent-v1.0"` AND `metadata.agent_version == "1.0"` AND `reel_ref.production_plan_id` echoes the input AND `human_review_required == true`. If not, halt — agent is hallucinating identifiers or breaking recommend-don't-approve. |

---

## §3 The 5 cases — expected branch + pass criteria

**The 5 fixtures exercise 4 of the 4 verdict values** (`pass` ×2, `fail` ×2, `hold` ×1) and **3 of the 9 LOCKED error codes live** (`entity_firewall_breach`, `format_spec_violation`, `drift_unresolved`). The remaining 6 codes + slot-11 catch-all are bound to the schema via the Day 46 `validate.py` adversarial guards, not re-exercised here (same discipline as Style Replication §9). `reshoot` is intentionally NOT in the live portfolio — it is Mode-A-exclusive and the 5 fixtures are Mode B/C; the schema's reshoot→production-coord-agent route guard is covered by the Day 46 adversarial accept/reject pair.

### TC-01 — `case-01-mode-b-pro-clean-pass` (Pro · Mode B · 5-shot · clean PASS + Mode B forensic cross-check)
- **Expected branch:** `successPreflightReport`. **Verdict:** `pass`. **route:** n/a (success carries `handoff_targets`).
- **Hard checks:**
  - `output_type == "successPreflightReport"`, `verdict == "pass"`.
  - `metadata.tier == "pro"`, `metadata.production_mode == "B"`, `metadata.lever_state == "lever-3"`.
  - `brand_voice_qc.points_total == 11` AND `points_passed == 11` AND `len(per_point) == 11`. Every `per_point[i].status == "pass"`, every `per_point[i].evidence` non-empty, `id`s are 1..11 in order. **A false-pass is structurally impossible** (schema-enforced: every status `pass`) — but assert it anyway, defense-in-depth.
  - `entity_firewall_pass_7.status == "pass"` AND `hits == 0` AND `tokens_scanned > 0`.
  - `format_spec_check.platform_variants_checked == 2` AND `aspect_ratio_violations == 0` AND `duration_violations == 0` AND `caption_burn_parity_violations == 0`.
  - `caption_spec_check.burn_in_firewall_status == "pass"` AND `parity_status == "pass"`.
  - `cost_ledger_check.status == "within_ceiling"` AND `tier_combined_ceiling_usd == 450` AND `cumulative_reel_usd <= 450` (fixture canon: $0.42).
  - `qc_pre_flags_adjudication.agents_reporting == 6` AND `floor_met_all == true` AND `negative_predicates == 0`.
  - `drift_reconciliation.unresolved_drift_count == 0`. (Rule #10: a `pass` is forbidden while this is > 0.)
  - **Mode B forensic:** `mode_b_chain_check` is an object with `passthrough_intact_bool == true` AND `negative_prompt_sha256` matching `^[a-f0-9]{64}$` (and equal to the input's `negative_prompt_sha256` — single hash survives the Style Replication passthrough).
  - `handoff_targets == ["localization", "publishing"]` (Step 10 success path).
  - top-level `qc_pre_flags[]` ≥ 4 entries, every element snake_case (`^[a-z][a-z0-9_]{0,63}$`).
  - `cost_incurred_usd <= 0.02` (self-cost ceiling, Hard Rule #2).
- **Lineage:** `metadata.parent_chain` is a 6-tuple: `[brief-…, script-…, storyboard-…, ai-video-gen-…, <uuid>, preflight-…]`. (Schema holds `minItems: 5, maxItems: 6`; the SKILL emits the 6th `preflight_report_id`. A 5-tuple is also accepted; a 4-tuple is rejected.)
- **Tamper-evidence:** `metadata.verdict_evidence_hash` matches `^[a-f0-9]{64}$`. *(The validator checks SHAPE, not value — Opus cannot deterministically reproduce the fixture's hash; the agent computes it honestly over its own evidence block.)*
- **Recommend-don't-approve:** top-level `human_review_required == true` AND `metadata.human_review_required == true`. Zero approval language (`approved`, `cleared to publish`, `published`) anywhere in any string.
- **Entity firewall + banned-vocab walk:** zero hits of the 10-entry canonical list (§6.5: `holdco group`, `4821`/`4821 main`/`main flagship`, `site-c-brand`/`6315`, `sln`/`salonb`/`shear & cuts`, `retail supply`, `principal`/`principal holdco`, `npox`/`community nonprofit`, `nonprofit leader a`/`nonprofit leader b`/`nonprofit leader c`, `partner brand`, `holdcogroup.com`) and zero banned-vocab (`babe`, `boss babe`, `girl boss`, `she-eo`, `mompreneur`) across every emitted string. (REINVENTED IS allowed — brand-as-pilot-customer per Cross-SPEC canon.)

### TC-02 — `case-02-mode-c-enterprise-clean-pass` (Enterprise · Mode C · clean PASS · mode-aware reporting)
- **Expected branch:** `successPreflightReport`. **Verdict:** `pass`.
- **Hard checks (delta vs TC-01):**
  - `metadata.tier == "enterprise"`, `metadata.production_mode == "C"`.
  - `format_spec_check.platform_variants_checked == 3`, all violation counts 0.
  - `cost_ledger_check.tier_combined_ceiling_usd == 870` AND `cumulative_reel_usd <= 870` (fixture canon: $0.57).
  - **`mode_b_chain_check == null`** (Mode C: AI Video Gen NOT invoked, no `rendered_shots`, no forensic cross-check). **This is the fixture's whole point** — the verdict is mode-AGNOSTIC (same `pass` shape as TC-01) but reporting is mode-AWARE (the Mode B-only field is correctly nulled). A regression that hard-required `rendered_shots` would silently fail every Mode C reel — the highest-margin path.
  - **Lineage position [3] == `"mode-c-direct"`** (no AI Video Gen stage in a Mode C chain).
  - All other TC-01 success checks apply (11/11 brand-voice, firewall hits 0, handoff_targets, recommend-don't-approve, verdict_evidence_hash shape).

### TC-03 — `case-03-entity-firewall-breach` → `errorEnvelope` `entity_firewall_breach` · **GATING FIXTURE**
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **route_back_to:** `style-replication-agent`.
- **This is the most important fixture in the portfolio.** The injected token `4821 Main` rides inside `replicated_shots[0].replication_notes` ("brand finish matched to 4821 Main reference grade") — a schema-valid free-text field. Six prior firewall passes missed it (an upstream bug); QC Pre-flight, the 7th and final pass, must catch it. **A v1.0 LOCK is BLOCKED if TC-03 does not catch the injected token.**
- **Hard checks:**
  - `output_type == "errorEnvelope"`, `verdict == "fail"`.
  - `failure_code == "entity_firewall_breach"`.
  - `failed_check_id == 2` (Step 2 / Check #2 = the 7th-pass firewall walk).
  - `route_back_to == "style-replication-agent"` (the leaking stage).
  - `attempts == 1` (a real reel defect is a valid verdict on first construction — NOT a self-QC regenerate loop).
  - `detail.leaking_upstream_stage == "style-replication-agent"`.
  - `detail.matched_firewall_entry == 2` (4821 main = entry #2 on the canonical list).
  - `detail.violation` names the token + the field it rode in (`replication_notes`). *(This is the ONE field where the banned token legitimately appears in the output — the breach report quoting the offending token for forensics. The §5 validator EXCLUDES `detail.violation` from its firewall walk; every OTHER string must be clean.)*
  - `detail.recovery_path` present (forensic-log + route-to-strip + re-run language).
  - `human_review_required == true` (top-level AND metadata) — even a clear breach is a recommendation, never an autonomous quarantine.
- **Negative checks:** NO `brand_voice_qc`, NO `handoff_targets`, NO `mode_b_chain_check` on the error branch (those are success-only fields).

### TC-04 — `case-04-format-spec-violation` → `errorEnvelope` `format_spec_violation`
- **Expected branch:** `errorEnvelope`. **Verdict:** `fail`. **route_back_to:** `style-replication-agent`.
- **Hard checks:**
  - `failure_code == "format_spec_violation"`, `failed_check_id == 4`, `attempts == 1`.
  - `route_back_to == "style-replication-agent"` (the agent that produces the deliverable aspect — NOT `production-coord-agent`; this is a Mode B render-side defect, not an unrecoverable live-footage source, so it is NOT a reshoot).
  - `detail.affected_platform == "instagram-feed"`.
  - `detail.format_spec_check.aspect_ratio_violations >= 1` (the 1:1 variant requested but every shot rendered 9:16 only).
  - `detail.format_spec_check.platform_variants_checked == 2` (coverage complete — no variant skipped; the violation is a real mismatch, not under-reporting).
  - `detail.recovery_path` offers BOTH a fix-it route AND a drop-the-variant route (advisory, not auto-executed — Decision #13: route-back automation depth is advisory in v1.0).
  - `human_review_required == true` (both).
- **Negative checks:** NO success-only fields; NO `handoff_targets`.

### TC-05 — `case-05-drift-unresolved` → `errorEnvelope` `drift_unresolved` · **THE SOFT-HOLD (4th verdict)**
- **Expected branch:** `errorEnvelope`. **Verdict:** `hold`. **route_back_to:** `null` (human review).
- **Hard checks:**
  - `failure_code == "drift_unresolved"`, `failed_check_id == 8` (Step 8 / Check #8 = drift reconciliation), `attempts == 1`.
  - `verdict == "hold"` — the fourth verdict value, distinct from pass/fail/reshoot.
  - **`route_back_to == null`** — schema `allOf` guard: a `hold` MUST carry `route_back_to: null` + `failure_code: drift_unresolved`. Human routing is recorded in `detail.routed_to`, not in `route_back_to`.
  - `detail.routed_to == "human-review"`.
  - `detail.affected_shot == "shot-003"`.
  - `detail.drift_reconciliation.unresolved_drift_count >= 1` AND `detail.drift_reconciliation.human_signoff_required == true`.
  - `detail.recovery_path` present (operator signs-off → re-run → resolves to pass; OR rejects → route to style-replication-agent).
  - `human_review_required == true` (both).
- **The discipline under test:** the agent may NEVER emit `pass` while `unresolved_drift_count > 0` (Rule #10). Faced with genuine ambiguity (real drift, no Lever-3 sign-off), it declines to render a machine verdict — NOT auto-failed, NOT auto-passed. This is recommend-don't-approve at its sharpest.
- **Negative checks:** NO success-only fields; NO `handoff_targets`; `route_back_to` is `null` (NOT a string).

### Cross-fixture invariants (apply to all 5)
- `metadata.agent_id == "qc-preflight-agent-v1.0"` on every output (success or error).
- `metadata.agent_version == "1.0"` on every output.
- `metadata.qc_gate_class == "pre_flight"` on every output.
- `metadata.runtime_environment_class == "staging"` for dry-run runs.
- `metadata.verdict_evidence_hash` matches `^[a-f0-9]{64}$` on every output (tamper-evident verdict; shape-checked, not value-checked).
- `metadata.parent_chain` is a well-formed 5- or 6-tuple (positions [0]=`brief-`, [1]=`script-`, [2]=`storyboard-`, [3]=`ai-video-gen-…`|`mode-c-direct`, [4]=UUID; optional [5]=`preflight-…`).
- `reel_ref.preflight_report_id` starts with `preflight-` on every output.
- top-level `human_review_required == true` AND `metadata.human_review_required == true` on every output (recommend-don't-approve, schema `const true`).
- Zero entity-firewall hits + zero banned-vocab (token-boundary, SPEC §6.5) across every emitted string, with two legitimate-naming exclusions: the success branch's `brand_voice_qc` subtree (points 7 & 11 evidence name the tokens they screen for) and TC-03's `detail.violation` (the breach report quotes the offending token for forensics). The 11/11 pass status is asserted independently.
- Zero approval language (`approved`, `cleared to publish`, `published`) anywhere.

---

## §4 Why there is NO engine-stub block (the QC Pre-flight difference)

Every prior LLM Test Runbook in the fleet (Day 11 Script, Day 19 Production Coord, Day 27 AI Video Gen, Day 36 Style Replication) appended a `<engine_dry_run_mode>` fence to the user message, because those agents dispatch generative engines and the dry-run fence replaces the engine surface with stubbed responses.

**QC Pre-flight dispatches NO engine** (Hard Rule #2 — its effective per-reel cost is $0.00–$0.02; "if you find yourself composing an engine prompt, you have misunderstood your job"). Everything the agent adjudicates is already inside the input object:

- `replicated_shots[]` — the production-tier deliverable (Style Replication output, any mode).
- `rendered_shots[]` + `negative_prompt_sha256` — Mode B forensic cross-check material (TC-01 only; TC-02/Mode C omits it).
- `production_plan.platform_variants[]` — the format-spec surface.
- `cost_ledger` — the cumulative-spend reconciliation surface (the agent is the first with total-spend visibility).
- `accumulated_qc_pre_flags{}` — the 6-agent floor-adjudication surface.
- `metadata` — tier / mode / parent_chain / lever_state.

There is nothing to stub. The user message is the **bare input object**. The agent reasons over it, runs the 11-step verdict loop + 11-point Brand Voice QC gate + 7th-pass firewall + cost ledger, and emits one of two branches. This is what makes it the cheapest gate in the fleet, and the only one where "live" and "dry-run" are functionally identical.

**The one optional engine-adjacent surface — native pHash/CLIP drift re-verify (~$0.001/shot) — is NOT exercised by any fixture.** TC-05 (drift) is a *carried, unsigned* drift that the agent defers to the human (hold); it does NOT contest the drift via re-verification. So even the sole micro-cost path stays dark across all 5 cases. **Total engine spend this runbook: $0.00.**

**Runtime-computed fields (hash, timestamps, latency):** `verdict_evidence_hash` is a SHA-256 the agent computes honestly over its own evidence block; `timestamps` + `latency_ms` are runtime telemetry. In a Workbench run these will NOT match the fixture's frozen values, and that is correct. The §5 validator checks `verdict_evidence_hash` for SHAPE (`^[a-f0-9]{64}$`) only, and does not assert timestamp/latency values. Do not flag a hash/timestamp mismatch against the fixture as a failure — only a malformed shape is a failure.

---

## §5 Post-run validator (paste-and-run)

After saving all 5 outputs to `validation/llm-out/case-NN-output.json`:

```bash
cd "~/ars/skills/qc-preflight-agent"

python3 << 'PYEOF'
import json, re, sys
from jsonschema import Draft202012Validator
from pathlib import Path

ROOT = Path(".")
OUT_SCHEMA = json.loads((ROOT / "schemas" / "output.schema.json").read_text())
v = Draft202012Validator(OUT_SCHEMA)

# 10-entry canonical entity firewall list (SPEC §6.5 — TOKEN-BOUNDARY, case-insensitive)
FIREWALL = ["holdco group","holdco group inc","hc","4821 main","4821","main flagship",
            "site-c-brand","6315","sln","retail supply","principal holdco","principal",
            "npox","community nonprofit","nonprofit leader a","nonprofit leader b","nonprofit leader c",
            "partner brand","holdcogroup.com"]
BANNED   = ["babe","boss babe","girl boss","girlboss","she-eo","mompreneur"]
APPROVAL = ["approved for publish","cleared to publish","published","approved"]

UUID_RE   = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)
SHA256_RE = re.compile(r"^[a-f0-9]{64}$")
SNAKE_RE  = re.compile(r"^[a-z][a-z0-9_]{0,63}$")

def word_hit(term, text):
    # token-boundary, case-insensitive (SPEC §6.5) — "hc" never matches inside "image"
    return re.search(r"(?<![a-z0-9])" + re.escape(term.lower()) + r"(?![a-z0-9])", text) is not None

EXPECT = {
  "case-01-mode-b-pro-clean-pass": {
    "branch": "successPreflightReport", "verdict": "pass",
    "tier": "pro", "mode": "B", "variants": 2, "ceiling": 450.0,
    "mode_b_chain": "object",
  },
  "case-02-mode-c-enterprise-clean-pass": {
    "branch": "successPreflightReport", "verdict": "pass",
    "tier": "enterprise", "mode": "C", "variants": 3, "ceiling": 870.0,
    "mode_b_chain": "null", "lineage_pos3": "mode-c-direct",
  },
  "case-03-entity-firewall-breach": {
    "branch": "errorEnvelope", "verdict": "fail",
    "failure_code": "entity_firewall_breach", "failed_check_id": 2,
    "route_back_to": "style-replication-agent", "attempts": 1,
    "leaking_stage": "style-replication-agent", "matched_entry": 2,
  },
  "case-04-format-spec-violation": {
    "branch": "errorEnvelope", "verdict": "fail",
    "failure_code": "format_spec_violation", "failed_check_id": 4,
    "route_back_to": "style-replication-agent", "attempts": 1,
    "affected_platform": "instagram-feed",
  },
  "case-05-drift-unresolved": {
    "branch": "errorEnvelope", "verdict": "hold",
    "failure_code": "drift_unresolved", "failed_check_id": 8,
    "route_back_to": None, "attempts": 1,
    "routed_to": "human-review", "affected_shot": "shot-003",
  },
}

def collect_strings(obj, acc):
    if isinstance(obj, str):
        acc.append(obj)
    elif isinstance(obj, dict):
        for k, val in obj.items():
            acc.append(k); collect_strings(val, acc)
    elif isinstance(obj, list):
        for item in obj: collect_strings(item, acc)

results = []
for case_id, exp in EXPECT.items():
    f = ROOT / "validation" / "llm-out" / f"{case_id}-output.json"
    if not f.exists():
        results.append((case_id, "MISSING", "no LLM output file")); continue
    try:
        out = json.loads(f.read_text())
    except Exception as e:
        results.append((case_id, "JSON_PARSE_ERR", str(e)[:160])); continue

    # 1. schema gate
    errs = list(v.iter_errors(out))
    if errs:
        results.append((case_id, "SCHEMA_FAIL", f"{len(errs)} errs · first: {errs[0].message[:150]}")); continue

    # 2. branch detection
    branch = out.get("output_type")
    if branch != exp["branch"]:
        results.append((case_id, "WRONG_BRANCH", f"got {branch!r}, expected {exp['branch']!r}")); continue

    fails = []
    meta = out.get("metadata", {}) or {}

    # ---- universal metadata + recommend-don't-approve ----
    if out.get("verdict") != exp["verdict"]:
        fails.append(f"verdict={out.get('verdict')!r}, expected {exp['verdict']!r}")
    if meta.get("agent_id") != "qc-preflight-agent-v1.0":
        fails.append(f"metadata.agent_id={meta.get('agent_id')!r}")
    if meta.get("agent_version") != "1.0":
        fails.append(f"metadata.agent_version={meta.get('agent_version')!r}")
    if meta.get("qc_gate_class") != "pre_flight":
        fails.append(f"metadata.qc_gate_class={meta.get('qc_gate_class')!r}")
    if out.get("human_review_required") is not True:
        fails.append(f"top-level human_review_required={out.get('human_review_required')!r}, expected true")
    if meta.get("human_review_required") is not True:
        fails.append(f"metadata.human_review_required={meta.get('human_review_required')!r}, expected true")
    veh = meta.get("verdict_evidence_hash")
    if not (isinstance(veh, str) and SHA256_RE.match(veh)):
        fails.append(f"metadata.verdict_evidence_hash bad shape: {veh!r}")

    # ---- parent_chain shape (5- or 6-tuple) ----
    pc = meta.get("parent_chain")
    if not (isinstance(pc, list) and len(pc) in (5, 6)):
        fails.append(f"parent_chain not a 5/6-tuple: {pc!r}")
    else:
        if not pc[0].startswith("brief-"):      fails.append(f"parent_chain[0]={pc[0]!r}")
        if not pc[1].startswith("script-"):     fails.append(f"parent_chain[1]={pc[1]!r}")
        if not pc[2].startswith("storyboard-"): fails.append(f"parent_chain[2]={pc[2]!r}")
        if not (pc[3].startswith("ai-video-gen-") or pc[3] == "mode-c-direct"):
            fails.append(f"parent_chain[3]={pc[3]!r}")
        if not UUID_RE.match(str(pc[4])):       fails.append(f"parent_chain[4] not a UUID: {pc[4]!r}")
        if len(pc) == 6 and not str(pc[5]).startswith("preflight-"):
            fails.append(f"parent_chain[5]={pc[5]!r}, expected preflight-…")
    if "lineage_pos3" in exp and isinstance(pc, list) and len(pc) >= 4 and pc[3] != exp["lineage_pos3"]:
        fails.append(f"parent_chain[3]={pc[3]!r}, expected {exp['lineage_pos3']!r}")

    # ---- reel_ref ----
    rr = out.get("reel_ref", {}) or {}
    if not str(rr.get("preflight_report_id","")).startswith("preflight-"):
        fails.append(f"reel_ref.preflight_report_id={rr.get('preflight_report_id')!r}")

    # ---- firewall / banned-vocab / approval walk (token-boundary; legit-naming fields excluded) ----
    # Exclusions for fields that LEGITIMATELY name entities — naming them IS the report doing its job:
    #   - success branch: brand_voice_qc (points 7 & 11 evidence describe the firewall / brand-safety
    #     check by naming the very tokens they screen for). The 11/11 pass status is asserted separately.
    #   - error branch: detail.violation (the breach report quotes the offending token for forensics).
    walk_obj = json.loads(json.dumps(out))  # deep copy
    if branch == "successPreflightReport":
        walk_obj.pop("brand_voice_qc", None)
    else:
        det = walk_obj.get("detail")
        if isinstance(det, dict) and "violation" in det:
            det.pop("violation")
    strings = []; collect_strings(walk_obj, strings)
    joined = "\n".join(strings).lower()
    for t in FIREWALL:
        if word_hit(t, joined): fails.append(f"entity_firewall_leak: {t!r}")
    for t in BANNED:
        if word_hit(t, joined): fails.append(f"banned_vocab_leak: {t!r}")
    for t in APPROVAL:
        if word_hit(t, joined): fails.append(f"approval_language_leak: {t!r}")

    if branch == "successPreflightReport":
        # tier / mode
        if meta.get("tier") != exp["tier"]:
            fails.append(f"metadata.tier={meta.get('tier')!r}, expected {exp['tier']!r}")
        if meta.get("production_mode") != exp["mode"]:
            fails.append(f"metadata.production_mode={meta.get('production_mode')!r}, expected {exp['mode']!r}")
        # 11-point brand-voice gate
        bv = out.get("brand_voice_qc", {}) or {}
        pp = bv.get("per_point", []) or []
        if bv.get("points_total") != 11: fails.append(f"brand_voice_qc.points_total={bv.get('points_total')}")
        if bv.get("points_passed") != 11: fails.append(f"brand_voice_qc.points_passed={bv.get('points_passed')}")
        if len(pp) != 11: fails.append(f"per_point len={len(pp)}, expected 11")
        for i, pt in enumerate(pp):
            if pt.get("status") != "pass":
                fails.append(f"per_point[{i}] id={pt.get('id')} status={pt.get('status')!r} (false-pass guard)")
            if not (pt.get("evidence") or "").strip():
                fails.append(f"per_point[{i}] empty evidence")
        # firewall counter
        efw = out.get("entity_firewall_pass_7", {}) or {}
        if efw.get("status") != "pass" or efw.get("hits") != 0:
            fails.append(f"entity_firewall_pass_7={efw!r} (need status pass, hits 0)")
        # format spec
        fs = out.get("format_spec_check", {}) or {}
        if fs.get("platform_variants_checked") != exp["variants"]:
            fails.append(f"format_spec_check.platform_variants_checked={fs.get('platform_variants_checked')}, expected {exp['variants']}")
        for k in ("aspect_ratio_violations","duration_violations","caption_burn_parity_violations"):
            if fs.get(k) != 0: fails.append(f"format_spec_check.{k}={fs.get(k)}, expected 0")
        # caption spec
        cs = out.get("caption_spec_check", {}) or {}
        if cs.get("burn_in_firewall_status") != "pass" or cs.get("parity_status") != "pass":
            fails.append(f"caption_spec_check={cs!r}")
        # cost ledger
        cl = out.get("cost_ledger_check", {}) or {}
        if cl.get("status") != "within_ceiling":
            fails.append(f"cost_ledger_check.status={cl.get('status')!r}")
        if cl.get("tier_combined_ceiling_usd") != exp["ceiling"]:
            fails.append(f"tier_combined_ceiling_usd={cl.get('tier_combined_ceiling_usd')}, expected {exp['ceiling']}")
        if (cl.get("cumulative_reel_usd") or 0) > exp["ceiling"]:
            fails.append(f"cumulative_reel_usd={cl.get('cumulative_reel_usd')} > ceiling {exp['ceiling']}")
        # qc_pre_flags adjudication
        qa = out.get("qc_pre_flags_adjudication", {}) or {}
        if qa.get("agents_reporting") != 6: fails.append(f"agents_reporting={qa.get('agents_reporting')}, expected 6")
        if qa.get("floor_met_all") is not True: fails.append(f"floor_met_all={qa.get('floor_met_all')!r}")
        if qa.get("negative_predicates") != 0: fails.append(f"negative_predicates={qa.get('negative_predicates')}")
        # drift
        dr = out.get("drift_reconciliation", {}) or {}
        if dr.get("unresolved_drift_count") != 0:
            fails.append(f"drift unresolved_drift_count={dr.get('unresolved_drift_count')}, expected 0 (Rule#10 forbids pass-over-drift)")
        # mode_b_chain_check
        mbc = out.get("mode_b_chain_check", "__absent__")
        if exp["mode_b_chain"] == "object":
            if not (isinstance(mbc, dict) and mbc.get("passthrough_intact_bool") is True
                    and SHA256_RE.match(str(mbc.get("negative_prompt_sha256","")))):
                fails.append(f"mode_b_chain_check object malformed: {mbc!r}")
        else:  # null
            if mbc is not None:
                fails.append(f"mode_b_chain_check={mbc!r}, expected null (Mode C)")
        # handoff_targets
        if out.get("handoff_targets") != ["localization","publishing"]:
            fails.append(f"handoff_targets={out.get('handoff_targets')!r}")
        # top-level qc_pre_flags >=4 snake_case
        qf = out.get("qc_pre_flags") or []
        if len(qf) < 4: fails.append(f"qc_pre_flags count={len(qf)} < 4")
        for j, fl in enumerate(qf):
            if not (isinstance(fl, str) and SNAKE_RE.match(fl)):
                fails.append(f"qc_pre_flags[{j}] not snake_case: {fl!r}")
        # self-cost ceiling
        if (out.get("cost_incurred_usd") or 0) > 0.02:
            fails.append(f"cost_incurred_usd={out.get('cost_incurred_usd')} > 0.02 self-cost ceiling")

    else:  # errorEnvelope
        if out.get("failure_code") != exp["failure_code"]:
            fails.append(f"failure_code={out.get('failure_code')!r}, expected {exp['failure_code']!r}")
        if out.get("failed_check_id") != exp["failed_check_id"]:
            fails.append(f"failed_check_id={out.get('failed_check_id')}, expected {exp['failed_check_id']}")
        if out.get("attempts") != exp["attempts"]:
            fails.append(f"attempts={out.get('attempts')}, expected {exp['attempts']}")
        # route_back_to (None for hold)
        if out.get("route_back_to") != exp["route_back_to"]:
            fails.append(f"route_back_to={out.get('route_back_to')!r}, expected {exp['route_back_to']!r}")
        detail = out.get("detail", {}) or {}
        if not (detail.get("recovery_path") or "").strip():
            fails.append("detail.recovery_path empty/absent")
        # per-case detail
        if "leaking_stage" in exp and detail.get("leaking_upstream_stage") != exp["leaking_stage"]:
            fails.append(f"detail.leaking_upstream_stage={detail.get('leaking_upstream_stage')!r}, expected {exp['leaking_stage']!r}")
        if "matched_entry" in exp and detail.get("matched_firewall_entry") != exp["matched_entry"]:
            fails.append(f"detail.matched_firewall_entry={detail.get('matched_firewall_entry')}, expected {exp['matched_entry']}")
        if "affected_platform" in exp and detail.get("affected_platform") != exp["affected_platform"]:
            fails.append(f"detail.affected_platform={detail.get('affected_platform')!r}, expected {exp['affected_platform']!r}")
        if exp["failure_code"] == "format_spec_violation":
            fsc = detail.get("format_spec_check", {}) or {}
            if (fsc.get("aspect_ratio_violations") or 0) < 1:
                fails.append(f"detail.format_spec_check.aspect_ratio_violations={fsc.get('aspect_ratio_violations')}, expected >=1")
        if exp["verdict"] == "hold":
            if detail.get("routed_to") != exp.get("routed_to"):
                fails.append(f"detail.routed_to={detail.get('routed_to')!r}, expected {exp.get('routed_to')!r}")
            dd = detail.get("drift_reconciliation", {}) or {}
            if (dd.get("unresolved_drift_count") or 0) < 1:
                fails.append(f"detail.drift_reconciliation.unresolved_drift_count={dd.get('unresolved_drift_count')}, expected >=1")
            if "affected_shot" in exp and detail.get("affected_shot") != exp["affected_shot"]:
                fails.append(f"detail.affected_shot={detail.get('affected_shot')!r}, expected {exp['affected_shot']!r}")
        # negative checks: no success-only fields on error branch
        for forbidden in ("brand_voice_qc","handoff_targets","mode_b_chain_check","entity_firewall_pass_7"):
            if forbidden in out:
                fails.append(f"success-only field {forbidden!r} present on error branch")

    results.append((case_id, "PASS" if not fails else "FAIL", "all checks green" if not fails else " || ".join(fails[:8])))

print()
print("=" * 88)
print("Day 47 LLM Test Runbook — QC Pre-flight Agent v1.0 — VALIDATOR RESULTS")
print("=" * 88)
pass_n = 0
for case_id, status, note in results:
    icon = "PASS " if status == "PASS" else "FAIL "
    print(f"  {icon} {case_id:40s} :: {status:14s} {note[:200]}")
    if status == "PASS": pass_n += 1
print("-" * 88)
print(f"  Aggregate: {pass_n}/{len(results)} PASS")
if pass_n == len(results):
    print("  >> QC Pre-flight v1.0 LOCK GATE = OPEN.")
    print("  >> HARD GATE: requires AI Video Gen v1.0 LOCK *and* Style Replication v1.0 LOCK CLOSED first.")
    print("  >> Ceremony: flip v1.0-LOCK-CANDIDATE-day-44 -> v1.0-LOCKED in SKILL.md frontmatter + Notion + dashboard chip.")
else:
    print(f"  >> QC Pre-flight v1.0 LOCK GATE = HELD. {len(results)-pass_n} failure(s) require patch.")
    print(f"  >> Patch protocol: SKILL.md system prompt ONLY (schemas LOCKED Day 45; no schema edits without a v1.0.x bump).")
print("=" * 88)
sys.exit(0 if pass_n == len(results) else 1)
PYEOF
```

Save the printed output: append ` > validation/llm-out/run-results-2026-06-05.txt 2>&1` to the bash command above, OR screenshot it.

---

## §6 Open Question #47 resolution — dry-run vs live

**Decision:** **dry-run mode is the v1.0 LOCK gate** — and for QC Pre-flight, dry-run and live are functionally identical.

**Why:**
- QC Pre-flight is the ONLY agent in the fleet that dispatches **no generative engine at all** (Hard Rule #2). There is no render call, no style-transfer call, no vendor API. "Live mode" for the production agents means real engine spend on non-deterministic outputs; for QC Pre-flight there is no such surface. The only engine-adjacent path — native pHash/CLIP drift re-verify at ~$0.001/shot — is exercised by ZERO of the 5 fixtures (TC-05 defers drift to the human rather than re-verifying it).
- v1.0 LOCK proves the agent's **reasoning + schema compliance + firewall coverage + 11-point gate adjudication + cost-ledger reconciliation + verdict-route correctness + recommend-don't-approve discipline**. None of these require any engine call. They require Opus 4.6 to consume the input payload and emit a schema-valid, contract-compliant verdict.
- Cost: dry-run = ~$3.50 in Opus tokens. There is no meaningfully different "live" number to compare against — the agent spends $0.00 of engine money in every mode. This is the cheapest LOCK gate in the fleet.

**The 6-tuple `parent_chain` (Decision #5 / Item 11 — DEFERRED, surfaced not advanced):** the schema holds `parent_chain` at `minItems: 5, maxItems: 6`. The SKILL emits the 6th `preflight_report_id` position; all 5 fixtures carry the 6-tuple; the schema accepts both. The Cross-SPEC §3.9 n-tuple amendment that flips the floor to exact-6 is **operator-only ratification (Item 11)** — Donna recommends RATIFY-AS-DRAFTED but does NOT advance it. The §5 validator accepts both 5- and 6-tuples by design, so this runbook does NOT depend on the amendment landing first. This is purely an operator decision, not a test-gate dependency.

---

## §7 Promotion rule LOCKED

5/5 PASS + **AI Video Gen v1.0 LOCK CLOSED** + **Style Replication v1.0 LOCK CLOSED** + Day 44 LOCK CANDIDATE Items 6 + 8 + 11 ratified → ceremony flips version tag `v1.0-LOCK-CANDIDATE-day-44` → `v1.0-LOCKED` in `skills/qc-preflight-agent/SKILL.md` frontmatter `status:` field AND the Notion ARS hub row AND the dashboard `agentic-reel-studio` QC Pre-flight chip `spec` (yellow) → `live` (green). The Day 47 evidence trail (5 LLM outputs + validator results + this runbook) is the canonical justification for the LOCK ceremony.

| Unlocked post-LOCK | Why |
|--------------------|-----|
| **The terminal gate goes LIVE** — every tier/mode reel now has a real pre-flight checkpoint before Localization/Publishing | QC Pre-flight is the 7th and last defense-in-depth firewall + the first universal-tier gate since Brief |
| **7th of 17 SKILL bundles confirmed LIVE** | Joins Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication — pipeline has 7 of 17 agents LOCKED at v1.0 |
| **Cross-SPEC §3.9 n-tuple amendment can land** (if Item 11 ratified) | QC Pre-flight is the agent that forces the 6-tuple (it appends `preflight_report_id`); its LOCK is the natural moment to flip the schema floor to exact-6 fleet-wide |
| **Recommend-don't-approve discipline proven end-to-end** | TC-05 hold + every branch's `human_review_required: const true` empirically demonstrate the gate never auto-approves a publish |
| **Agent #8 of 17 SPEC outline kickoff** | Donna recommendation at ceremony close — operator confirms the specific next-agent schedule |

---

## §8 Run-log template (fill in after each case)

Copy this block 5× into `validation/llm-out/run-log-2026-06-05.md`.

```
## Case: case-NN-<slug>

- **Run timestamp (UTC):** 2026-06-05THH:MM:SSZ
- **Mode:** dry-run | live   (functionally identical for QC Pre-flight — no engine)
- **Model:** claude-opus-4-6
- **Temperature:** 0.2
- **Max tokens:** 8000
- **Input tokens:** ____
- **Output tokens:** ____
- **Wall-clock seconds:** ____
- **Output file:** validation/llm-out/case-NN-<slug>-output.json
- **Output size (bytes):** ____
- **Branch emitted:** successPreflightReport | errorEnvelope
- **Verdict:** pass | fail | reshoot | hold
- **failure_code (if error):** ____
- **route_back_to:** ____
- **verdict_evidence_hash (64-hex shape OK?):** ____
- **parent_chain length (5 or 6):** ____
- **human_review_required (must be true):** ____
- **Validator result (from §5):** PASS | FAIL
- **If FAIL — first failure note:** ____________________
- **Spot-check notes (free-text ≤200 chars):** ____________________
```

---

## §9 Aggregate scoring sheet

| Case | Verdict expected | Branch expected | Verdict emitted | Validator | Notes |
|------|------------------|-----------------|-----------------|-----------|-------|
| TC-01 case-01-mode-b-pro-clean-pass | pass | successPreflightReport | _____ | _____ | _____ |
| TC-02 case-02-mode-c-enterprise-clean-pass | pass | successPreflightReport (mode_b_chain null) | _____ | _____ | _____ |
| TC-03 case-03-entity-firewall-breach | fail | errorEnvelope (entity_firewall_breach) **GATING** | _____ | _____ | _____ |
| TC-04 case-04-format-spec-violation | fail | errorEnvelope (format_spec_violation) | _____ | _____ | _____ |
| TC-05 case-05-drift-unresolved | hold | errorEnvelope (drift_unresolved) | _____ | _____ | _____ |

**Aggregate:** ___ / 5 PASS

**QC Pre-flight v1.0 LOCK gate decision (ceremony executable IF):**
- [ ] **5/5 PASS** AND
- [ ] **AI Video Gen v1.0 LOCK ceremony CLOSED first** (hard gate #1) AND
- [ ] **Style Replication v1.0 LOCK ceremony CLOSED first** (hard gate #2) AND
- [ ] **Day 44 LOCK CANDIDATE Items 6 + 8 + 11 ratified** AND
- [ ] **Validator output saved to `validation/llm-out/run-results-2026-06-05.txt`** AND
- [ ] **All 5 LLM output JSONs preserved in `validation/llm-out/`**

→ flip SKILL.md `status:` to `v1.0 LOCKED`. Mark Notion ARS hub row LOCKED. Update dashboard `agentic-reel-studio` QC Pre-flight chip → `live` (green). Schedule Agent #8 SPEC outline kickoff.

- [ ] **<5/5 PASS** → log failure(s) + patch the offending system-prompt clause(s) in SKILL.md (only — schemas LOCKED Day 45). Re-run failed cases Day 48. Do NOT promote until 5/5. **TC-03 is a special case: if the GATING fixture fails to catch the `4821 Main` token, the LOCK is hard-blocked regardless of the other four** — the agent's reason to exist did not fire.

---

## §10 Guardrails (do not skip — process integrity attestation)

- ✅ **No engine dispatch, in any mode.** QC Pre-flight calls no engine by design (Hard Rule #2). There is no live mode to misfire. If Opus composes an engine prompt or requests a credential in any response, abort — Rule #2 violation.
- ✅ **No credentials anywhere.** The agent references none. ZERO $ engine spend; ≤ $3.50 Opus tokens total.
- ✅ **No schema edits.** Day 45 schemas are LOCKED-as-drafted. Any drift between agent output and schema is an agent issue, not a schema issue.
- ✅ **No silent v1.0 promotion on partial PASS.** 4/5 PASS = LOCK held. The contract is 5/5 or nothing. TC-03 failing = hard-block.
- ✅ **No external comms triggered by this runbook.** Validator output is internal evidence. No client emails, no investor pings, no social posts.
- ✅ **No operator-impersonation.** This runbook does NOT close either production-tier LOCK ceremony, does NOT ratify Items 6/8/11, does NOT ratify PRELIMINARY decisions #4/#13, does NOT commit the Cross-SPEC §3.9 amendment, does NOT flip any version tag or dashboard chip. All of these are operator-only and remain PENDING until the operator acts.
- ✅ **No fake-advance.** No LLM Test Runbook executed by Donna — this document is the paste-and-run artifact for the operator's sit-down. The validator is schema + fixture-expectation checking, not an LLM run.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. The HC/NPOX tokens enumerated in §6.5 + the §5 validator FIREWALL list are the firewall's BLOCK-list (so the gate rejects them) — not a cross-entity reference. The `4821 Main` token in TC-03 is the gating fixture's catch surface. REINVENTED is the pilot brand inside the fixtures.
- ✅ **Rest Day honored** — this Day 47 build runs Friday Jun 5; the next Sunday (Jun 7) is docs-prep only.

---

## §11 Carry-over visibility block (Notion + dashboard + operator items)

**Operator-only action items (DO NOT advance silently):**

1. **Close AI Video Gen v1.0 LOCK ceremony** (HARD GATE #1 for QC Pre-flight LOCK):
   - Day 27 LLM Test 5/5 PASS verdict in (or re-run if pending)
   - Day 24 Items 8 + 11 ratified
   - Version tag flip `v1.0-LOCK-CANDIDATE-day-24` → `v1.0-LOCKED` + Notion + dashboard chip `live`

2. **Close Style Replication v1.0 LOCK ceremony** (HARD GATE #2 for QC Pre-flight LOCK):
   - Day 36 LLM Test 5/5 PASS verdict in (or run the Day 36 runbook — paste-and-run, ready)
   - Day 32 Items 6 + 8 + 11 ratified
   - Version tag flip `v1.0-LOCK-CANDIDATE-day-32` → `v1.0-LOCKED` + Notion + dashboard chip `live`
   - **Order note:** Day 32 §4 calendar orders AI Video Gen LOCK → Style Replication LOCK → QC Pre-flight LOCK. All three are pending.

3. **QC Pre-flight Day 44 LOCK CANDIDATE Items 6 + 8 + 11** (30–45 min · 3 independent actions, any order):
   - Item 6 — confirm inherited combined ceilings ($450 / $870 / ≤$40). Donna recommends RATIFY (schema enforces these as a 3-value enum).
   - Item 8 — walk the 14 critical decisions; explicit verdict on PRELIMINARY #4 + #13. Donna recommends RATIFY both.
   - Item 11 — Cross-SPEC §3.9 n-tuple amendment (the 6-tuple `parent_chain` forcing function). Donna recommends RATIFY-AS-DRAFTED. NOT a test-gate dependency (validator accepts 5- and 6-tuples).

4. **Day 47 main session — execute this runbook** (20–35 min). Opus Workbench paste-and-run for all 5 cases. Save outputs + run §5 validator + record PASS/FAIL aggregate.

5. **LOCK ceremony** — IF 5/5 PASS + both production-tier LOCKs CLOSED + Items 6/8/11 ratified → flip version tag + Notion + dashboard chip.

**Dashboard `agentic-reel-studio` updates queued for Day 47 close (Donna executes via `mcp__cowork__update_artifact` if the artifact exists):**
- "Today's Output" → "Day 47 QC Pre-flight v1.0 LLM Test Runbook authored (~12 sections · paste-and-run · no-engine gate)"
- QC Pre-flight chip stays `spec` (yellow) until the ceremony closes — chip flip is part of the LOCK ceremony, NOT this runbook.

---

## §12 Files produced by this runbook (post-run)

After the operator's Day 47 sit-down completes (regardless of pass/fail outcome):

- `validation/llm-out/case-NN-<slug>-output.json` × 5 — raw Opus output per case
- `validation/llm-out/run-log-2026-06-05.md` — run-log template filled in × 5
- `validation/llm-out/run-results-2026-06-05.txt` — captured §5 validator output
- (On 5/5 PASS + both production LOCKs closed + Items 6/8/11 ratified) ceremony: update `skills/qc-preflight-agent/SKILL.md` frontmatter `status:` field
- (On same) ceremony: update Notion ARS hub row → LOCKED
- (On same) ceremony: update dashboard `agentic-reel-studio` QC Pre-flight chip → `live` (green)

---

## Sources consulted in authoring this runbook

- `ars/skills/qc-preflight-agent/SKILL.md` (Day 46 — system prompt verbatim · 12 hard rules · 11-point gate · 11-step loop)
- `ars/skills/qc-preflight-agent/schemas/{input,output}.schema.json` (Day 45 LOCKED-as-drafted · META-SCHEMA VALID)
- `ars/skills/qc-preflight-agent/test-cases/case-NN-*/{scenario.md,input.json,expected_output.json}` × 5 (Day 46 fixture canon)
- `ars/skills/qc-preflight-agent/validate.py` (Day 46 — 34/34 harness; the §5 validator extends it to score live LLM output)
- `ars/skills/qc-preflight-agent/README.md` (Day 46 invocation guide)
- `ars/ARS-2026-06-02-Day-44-QC-Preflight-Agent-v1-LOCK-CANDIDATE.md` (Day 44 LOCK candidate · 14 decisions · Items 6/8/11)
- `ars/ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` (§6.5 canonical 10-entry firewall list · §7 system prompt source)
- `ars/ARS-2026-05-25-Day-36-Style-Replication-LLM-Test-Runbook.md` (structural pattern source — this runbook is the QC Pre-flight analog, minus the engine-stub block)
- `ars/build-log-2026-06-04.md` (Day 46 log — names the LLM Test Runbook as the next forward deliverable; lists the hard gates)

---

*Day 47 runbook authored ahead of the iMac sit-down so the operator can paste-and-run without re-deriving any step. QC Pre-flight is the cheapest LOCK gate in the fleet: it dispatches NO engine, so there is no engine-stub block and no live-vs-dry-run cost delta — total spend ≤ $3.50 Opus tokens, $0.00 engine. Dry-run is the v1.0 LOCK gate. 5/5 PASS + AI Video Gen LOCK closed + Style Replication LOCK closed + Items 6/8/11 ratified = QC Pre-flight v1.0 LOCKED ceremony executable. TC-03 is the gating fixture — if the 7th pass fails to catch the injected `4821 Main` token, the LOCK is hard-blocked regardless of the other four. Recommend-don't-approve discipline is schema-enforced (`human_review_required: const true` on every branch) and empirically proven by the TC-05 soft-hold. Entity boundary respected (Sequel Digital ARS; REINVENTED as pilot brand inside fixtures; HC/NPOX tokens are the firewall block-list). The 6-tuple parent_chain (Item 11) remains DEFERRED and is NOT a test-gate dependency — the validator accepts both 5- and 6-tuples. No operator-only action was advanced or impersonated.*
