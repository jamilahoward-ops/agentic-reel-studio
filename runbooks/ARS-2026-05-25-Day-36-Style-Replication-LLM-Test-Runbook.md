# Day 36 LLM Test Execution Runbook — Style Replication Agent v1.0

**Date authored:** 2026-05-25 (Mon · Day 36 · Wk6D2 · v1.0 LOCK gate)
**Audience:** Jamila — single 30–45 min sit-down at the iMac (paste-and-run discipline).
**Goal:** Run all 5 SKILL bundle fixtures through Opus 4.6 in **dry-run mode**, validate outputs against `schemas/output.schema.json`, declare Style Replication v1.0 **LOCKED** if 5/5 PASS — IF AND ONLY IF AI Video Gen v1.0 LOCK ceremony closes first (HARD GATE per Day 32 LOCK CANDIDATE §4 calendar).
**Estimated cost:** ≈ **$0.00 of engine spend** (dry-run · mock engine responses) · ~**$0.40–$0.90** Opus 4.6 inference per case × 5 ≈ **≤ $4.50 total LLM token spend**.
**Pre-validated:** Both schemas META-SCHEMA VALID (Day 33). 4 of 11+ checks inline-confirmed Day 34 (TC-01 input + TC-01 successReplicatedShots + TC-03 errorEnvelope + both schema headers). Full `validate.py` 11+/11+ stamp deferred to operator's fresh-process re-run choice (Day 36 Branch C optional).
**Mode default:** **dry-run** (Open Question #36 resolution — see §6 below). Operator can flip to **live** post-LOCK as a v1.0.1 confidence pass, ≤ $500 spend ceiling.
**Operator approval still required to begin:** Day 32 LOCK candidate Items 6 + 8 + 11 ratification AND Day 24 AI Video Gen LOCK candidate Items 8 + 11 ratification + Day 27 sit-down outcome (the AI Video Gen LOCK ceremony must close first — Style Replication LOCK is hard-gated).

---

## TL;DR (action sequence)

1. **Confirm AI Video Gen v1.0 LOCK ceremony has closed.** Items 8 + 11 ratified + Day 27 5/5 PASS verdict in + Notion row "ARS · AI Video Gen Agent v1.0 LOCK" marked LOCKED + dashboard chip flipped to `live`. If pending, stop and close that ceremony first. Style Replication LOCK Day 37 cannot proceed without it.
2. **Confirm Style Replication Day 32 LOCK candidate Items 6 + 8 + 11 are operator-ratified.** Item 6 = per-engine pricing spot-check (Pika + Runway pages). Item 8 = 15 critical decisions walk (4 PRELIMINARY items #2/#5/#7/#10 require explicit verdict). Item 11 = Cross-SPEC §3.9 amendment ratification (5-tuple parent_chain → n-tuple-as-lineage generalization).
3. **Optional:** Run `cd "~/ars/skills/style-replication-agent/" && python3 validate.py` in a fresh Python process for the canonical 11+/11+ checks PASS stamp. ~30 sec. Not gated — 4 of 11+ checks already confirmed inline Day 34.
4. **Open Claude Console** (Workbench): `https://console.anthropic.com/workbench`
5. **Model:** `claude-opus-4-6`. **Temperature:** `0.4`. **Max tokens:** `8000`. **Top-p:** default.
6. **System prompt:** open `ars/skills/style-replication-agent/SKILL.md`, locate the fenced block under §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)", paste **everything inside the fence** (13 hard rules + tier table + 11-step process + 12-check Self-QC + 6 errorEnvelope codes + output discipline + lever-state behavior + never-do list). No edits. No additions.
7. For each of the 5 cases:
   - Open `ars/skills/style-replication-agent/test-cases/case-NN-*/input.json`. Copy the entire root object.
   - In dry-run mode, append the **Engine Stub Block** (§4 below) inside a `<engine_dry_run_mode>` fence at the **end** of the user message. This primes Opus to behave as if pika_style_tokens / runway_style_reference / clip_native / phash_native / palette_native / grade_pass_native / coverage_envelope_native returned the stubbed responses. The agent's prompt body remains untouched; only the simulated engine surface changes.
   - User message = the JSON input object + the dry-run fence. No prose, no markdown around the JSON itself.
   - Send. Capture the **raw JSON output only** (strip any accidental code fence Opus emits — output discipline forbids them, but verify). Save to `ars/skills/style-replication-agent/validation/llm-out/case-NN-output.json`.
   - Note token counts + wall-clock latency in the run-log (template at end of this file).
8. **Run validator** (single command, §5 below). Either **5/5 PASS → Style Replication v1.0 LOCKED Day 37 ceremony executable**, or capture failures for Day 37 (Tue May 26) patch session.

---

## §1 Pre-flight checklist (13 items)

- [ ] **AI Video Gen v1.0 LOCK ceremony closed.** Items 8 + 11 ratified · Day 27 sit-down 5/5 PASS verdict in · Notion Action Tracker row marked LOCKED · dashboard chip flipped to `live`. **HARD GATE.** If pending, halt and close that ceremony first — Style Replication LOCK Day 37 is hard-gated on AI Video Gen LOCK first.
- [ ] **Style Replication Day 32 LOCK CANDIDATE Items 6 + 8 + 11 ratified.** All 4 PRELIMINARY items in §13 (#2/#5/#7/#10) have explicit RATIFY/AMEND/DEFER verdicts. Cross-SPEC §3.9 amendment (5-tuple parent_chain → n-tuple-as-lineage for all 17 agents) carries operator signature.
- [ ] **`validate.py` 11+/11+ checks PASS** — OR operator-declined-with-inline-subset-acceptance from Day 34 (4 of 11+ already inline-green: META-SCHEMA × 2 + TC-01 input + TC-01 success-branch + TC-03 errorEnvelope).
- [ ] **Claude Console open** at `https://console.anthropic.com/workbench`. API key in console (already configured).
- [ ] **Mode choice declared** on the run-log header (dry-run **OR** live). Default: dry-run.
- [ ] **All 5 fixtures present** at `ars/skills/style-replication-agent/test-cases/case-NN-*/input.json` (verify: `ls test-cases/case-*/input.json | wc -l` returns `5`).
- [ ] **Output folder ready:**
      `mkdir -p "~/ars/skills/style-replication-agent/validation/llm-out"`
- [ ] **`output.schema.json` self-validates** as Draft 2020-12 ✓ (Day 33 LOCKED · re-verified Day 34 inline).
- [ ] **`input.schema.json` self-validates** ✓ (Day 33 LOCKED · 5/5 smoke fixtures green Day 33).
- [ ] **System-prompt block + largest fixture footprint** = ~14.8 KB SKILL prompt + ~6.6 KB largest input (TC-04 Enterprise 7-shot) + ~2 KB dry-run fence = **~23 KB context window**. Trivial vs Opus 4.6 200 K context window.
- [ ] **`jsonschema` Python package available**: `python3 -c "import jsonschema; print(jsonschema.__version__)"` → ≥ 4.18 (Draft 2020-12 support).
- [ ] **No raw vendor credentials anywhere on screen.** `engine_quota_handles` values are opaque platform handles (`pika-token-opaque-handle-...`, `runway-style-ref-opaque-handle-...`). Hard Rule #5 — agent never sees real credentials.
- [ ] **Browser tabs closed** that are unrelated to console.anthropic.com (per user preference: close clutter).

---

## §2 Per-case execution checklist

For **each** of the 5 cases:

| Step | Action |
|------|--------|
| 1 | Open `test-cases/case-NN-*/input.json`. Copy the **entire root object** (NOT the file as wrapped JSON — the object itself). |
| 2 | Paste **system prompt** (verbatim from SKILL.md §"SYSTEM PROMPT — v1.0 (PASTE VERBATIM · DO NOT PARAPHRASE)" fence — identical across all 5 cases). |
| 3 | User message = `{input object}` then a newline then the dry-run engine-stub fence (`<engine_dry_run_mode>...</engine_dry_run_mode>` — §4 below). For live mode: omit the fence (Opus dispatches real engine calls via the orchestrator layer — DO NOT run live in this iMac console session; live mode requires the v1.0.1 orchestrator harness, not Workbench). |
| 4 | Set temperature `0.4`, max tokens `8000`. Hit **Run**. |
| 5 | Wait for completion. Verify response is a **single JSON object** with no markdown fences (output discipline — if violated, regenerate immediately). |
| 6 | Save the response (raw JSON, no wrapper, no preamble) to `validation/llm-out/case-NN-output.json`. |
| 7 | Note in run-log (§8 template): input tokens / output tokens / wall-clock seconds / temperature / model id / dry-run-or-live flag. |
| 8 | Spot-check: `metadata.agent_id == "style-replication-agent"` AND `metadata.agent_version starts with "v1.0"` AND `production_plan_id` echoes the input. If not, halt — agent is hallucinating identifiers. |

---

## §3 The 5 cases — expected branch + pass criteria

### TC-01 — `case-01-mode-b-pro-happy` (Pro · Mode B · 5-shot · single-engine Pika happy path)
- **Expected branch:** `successReplicatedShots` (top-level shape: `{ status: "ready_for_qc", replicated_shots[5], ... }`)
- **Hard checks:**
  - `tier == "Pro"`, `production_mode == "B"`, `lever == 3`.
  - `total_shots == 5`, `total_replicated_shots == 5`, `replicated_shots[]` length == 5.
  - `replicated_shots[0].shot_index == 1` AND `is_anchor_bool == true` AND `engine_id == "grade_pass_native"` AND `anchor_status == "anchor"` AND `inheritance_match_score_0_1 == 1.0`.
  - `replicated_shots[1..4]` (inheritor shots): `engine_id == "pika_style_tokens"` (Decision #5 PRIMARY) for all 4. `anchor_status == "inherit_pass"`. `inheritance_match_score_0_1 ≥ 0.85` (Drift threshold canon). `engine_fallback_used_bool == false` for all 4 (Pika single-pass, no Runway cascade). `retry_count == 0` for all 4.
  - Every `replicated_shots[*].asset_uri` matches `^ars://replicated_shots/REINVENTED/\d{4}-\d{2}-\d{2}/\d+/shot-\d{3}\.(mp4|mov|webm)$` (Hard Rule #8).
  - Every `replicated_shots[*].fingerprint_components` is an object with keys `{s_clip, s_phash, s_palette, s_motion}`, each in `[0,1]`.
  - `total_actual_usd ≤ $50 × 1.10 = $55` hard ceiling (Hard Rule #7 · Pro tier).
  - `literal_fingerprint_inherit` present and **fully encoded** (Mode B + C full encoding per Hard Rule #10) — includes `anchor_phash_64bit` (Mode A would omit this).
  - `metadata.parent_chain` is exactly a **5-tuple** (Hard Rule #13): `["brief-REINVENTED-2026-05-23-101", "script-REINVENTED-2026-05-23-101", "storyboard-REINVENTED-2026-05-23-101", "ai-video-gen-REINVENTED-2026-05-23-101", <replication_set_id starting with "replicationset-">]`.
  - `metadata.agent_id == "style-replication-agent"` AND `metadata.agent_version` starts with `"v1.0"`.
  - `handoff_targets[]` includes both `{agent: "edit-director", payload_ref: "replicated_shots"}` AND `{agent: "qc", payload_ref: "replicated_shots"}` (Step 11 minimum).
  - 12-check Self-QC results in `qc_pre_flags[]` (≥ 4 entries, every element snake_case per Cross-SPEC §3.7).
  - Zero error codes anywhere. Zero `errorEnvelope` block. `status == "ready_for_qc"` (NOT `"partial_with_warnings"`).
- **Banned-vocab check:** zero hits of `girl boss|girlboss|hustle culture|hustle|hustling|grind|grinding|boss babe|millionaire mindset` across every emitted string (case-insensitive, conjugates) (Hard Rule #1 inherited firewall from Brief Agent).
- **Entity firewall:** zero hits of `Holdco|Principal|NPOX|4821|6315|SLN|Retail Supply|Nonprofit Leader A|Nonprofit Leader B|Nonprofit Leader C|Partner Brand|holdcogroup\.com` anywhere in the output. (REINVENTED is the brand inside the fixtures — brand-as-pilot-customer per Cross-SPEC canon; REINVENTED IS allowed.)

### TC-02 — `case-02-mode-c-enterprise-happy` (Enterprise · Mode C · 3-shot · MARGIN DEMO)
- **Expected branch:** `successReplicatedShots` (Mode C hot-path · the agent's economic justification — see §3 deltas below)
- **Hard checks (delta vs TC-01):**
  - `tier == "Enterprise"`, `production_mode == "C"` (Mode C is Enterprise-ONLY at v1.0 per Hard Rule #2 + Decision #10).
  - `total_shots == 3`, `total_replicated_shots == 3`.
  - `replicated_shots[0].is_anchor_bool == true` AND `engine_id == "grade_pass_native"` AND `anchor_status == "anchor"` AND `inheritance_match_score_0_1 == 1.0` (anchor shot).
  - `replicated_shots[1..2]` (inheritor shots): `engine_id == "pika_style_tokens"` (Mode C hot-path uses Pika PRIMARY) for both. `inheritance_match_score_0_1 ≥ 0.85` for both. `engine_fallback_used_bool == false` for both.
  - **`total_actual_usd ≤ $55`** actual (Mode C Enterprise headroom check) — this represents **≥ 92% cost savings vs Mode B Enterprise equivalent** (~$692 baseline = the agent's economic margin demo).
  - `metadata.mode_c_coverage_match_bool == true` (Step 9 coverage envelope passed; agent did not fall back to Mode B equivalent re-render). If `false` → Hard Rule #2 + Decision #10 deems this a cost_overrun on the ceiling math; with `false` AND `total_actual_usd > $132` the branch flips to `errorEnvelope.failure_code == "cost_overrun"`.
  - `metadata.parent_chain` is exactly a 5-tuple. Position [3] (the AI Video Gen session id slot) MAY be the literal string `"mode-c-direct"` per Hard Rule #13 syntax (Mode C bypasses AI Video Gen upstream).
  - `literal_fingerprint_inherit` **fully encoded** (Mode C full encoding per Hard Rule #10).
  - All other TC-01 firewall + banned-vocab + asset_uri pattern + metadata.agent_id checks apply.

### TC-03 — `case-03-anchor-unavailable` → `errorEnvelope` `anchor_unavailable`
- **Expected branch:** `errorEnvelope`
- **Top-level shape:** `{ "status": "blocked", "errorEnvelope": { ... } }`.
- **Hard checks:**
  - `errorEnvelope.failure_code == "anchor_unavailable"`.
  - `errorEnvelope.failed_check_id == 9` (Hard Rule #9 three-way bit equality MISS — Self-QC Check #9 in 12-check list).
  - `errorEnvelope.attempts == 1` (Step 2 fail-fast halts before any dispatch — no retry; no inheritor cascade).
  - `errorEnvelope.detail.cache_lookup_result == "stale"` (or `"miss"` / `"version_drift"` — stale is fixture canon).
  - `errorEnvelope.detail.anchor_age_days == 128` AND `errorEnvelope.detail.anchor_freshness_max_days == 90` (the 128d-stale-vs-90d-ceiling diagnostic per Hard Rule #9).
  - `errorEnvelope.detail.spec_bug == false` (this is a cache state issue, not a SPEC bug).
  - **NO partial work emitted:** No `replicated_shots[]` array present. No top-level `total_replicated_shots > 0`. `errorEnvelope.successful_shots == []` empty array per Hard Rule #12 (partial-work preservation — nothing was preserved because nothing dispatched).
  - `recovery_path` guidance present with re-LOCK-anchor language.
- **Cost incurred check:** any cost telemetry indicates `0` or `0.00` (fail-fast Hard Rule #9 halts before Step 5 cost projection ever runs — agent halts at Step 2). Acceptable shapes: `cost_incurred_usd: 0`, OR `cost_incurred_usd: 0.0`, OR absence of cost telemetry block.
- **Banned-vocab + entity firewall walks** still apply (defense-in-depth across the errorEnvelope strings).

### TC-04 — `case-04-cost-overrun` → `errorEnvelope` `cost_overrun`
- **Expected branch:** `errorEnvelope`
- **Hard checks:**
  - `errorEnvelope.failure_code == "cost_overrun"`.
  - `errorEnvelope.failed_check_id == 7` (Self-QC Check #7 = cost ceiling enforcement).
  - `errorEnvelope.failed_shot_id == "shot-006"` (the dispatch that breached the ceiling).
  - `errorEnvelope.attempts == 1` (cost overrun detected once at actual spend true-up — no retry possible per Hard Rule #7).
  - `errorEnvelope.detail.tier_cost_ceiling_per_reel_usd == 120` (Enterprise).
  - `errorEnvelope.detail.hard_ceiling_with_buffer_usd == 132.0` (= $120 × 1.10).
  - `errorEnvelope.detail.actual_spent_at_halt_usd ≥ 132` (ceiling breach point — fixture canon: $134.15 ±$5 tolerance).
  - `errorEnvelope.detail.per_engine_actual_usd` is an object with at least `pika_style_tokens` + `runway_style_reference` keys, both > 0.
  - `errorEnvelope.detail.per_engine_overrun_attribution` is a non-empty object — must include `runway_style_reference` (the cost driver per fixture canon: 3 Pika→Runway fallback cascades at ~$60 overhead).
  - `errorEnvelope.detail.fallback_cascades >= 1` (cascade count surfaced for forensic review).
  - `errorEnvelope.detail.spec_bug == false`.
  - **`errorEnvelope.successful_shots[]` MUST contain exactly 5 preserved shots** (Hard Rule #12 partial-work preservation — fixture canon: shots 1+2+3+4+5 completed before halt on shot-006).
  - `recovery_path` guidance present with cost-attribution language (raise ceiling | reduce shots | investigate Pika availability).
- **Negative checks (Hard Rule #7 — overrun = halt before handoff):**
  - NO `handoff_targets[]` to edit-director or qc (top-level handoff_targets block absent OR empty array · partial-work preservation lives inside `errorEnvelope.successful_shots[]` for forensic Edit Director review, NOT in routable top-level payload).
  - Top-level `status == "blocked"`.

### TC-05 — `case-05-style-drift-exceeded` → `errorEnvelope` `style_drift_exceeded`
- **Expected branch:** `errorEnvelope` (after Decision #6 2-strike regenerate-then-still-fail)
- **Hard checks:**
  - `errorEnvelope.failure_code == "style_drift_exceeded"`.
  - `errorEnvelope.failed_check_id == 6` (Self-QC Check #6 = drift threshold per shot).
  - `errorEnvelope.failed_shot_id == "shot-003"` (the inheritor that drifted).
  - `errorEnvelope.attempts == 2` (Decision #6 2-strike ceiling reached: regenerate-then-still-fail).
  - `errorEnvelope.detail.drift_threshold == 0.85` (LOCKED canon).
  - `errorEnvelope.detail.shot_003_attempt_1_score < 0.85` AND `errorEnvelope.detail.shot_003_attempt_2_score < 0.85` (both attempts below floor — fixture canon: 0.71 and 0.74).
  - `errorEnvelope.detail.regenerate_strike_ceiling == 2` (Decision #6 LOCKED canon).
  - `errorEnvelope.detail.anchor_status == "inherit_fail_final"` (Hard Rule #6 mark).
  - `errorEnvelope.detail.engine_used == "pika_style_tokens"` (Decision #6 NO cascade to Runway — drift is a reasoning failure, not engine availability).
  - `errorEnvelope.detail.fallback_attempted == false` AND `errorEnvelope.detail.engine_fallback_used_bool == false` (Decision #6: drift fail does NOT cascade to fallback engine).
  - `errorEnvelope.detail.drift_components_attempt_2.s_motion ≤ 0.70` (diagnostic surface — below soft floor; fixture canon: 0.55).
  - `errorEnvelope.detail.spec_bug == false`.
  - **`errorEnvelope.successful_shots[]` MUST contain exactly 2 preserved shots** (Hard Rule #12 partial-work preservation — fixture canon: shots 1+2 succeeded; halt on shot-003 fail prevents shot-004+ attempts).
  - `recovery_path` guidance present (inspect upstream rendered_shots/shot-003 for prompt_seed noise | accept partial reel via Edit Director salvage).
- **Negative checks:**
  - NO `handoff_targets[]` to edit-director or qc on top level.
  - Top-level `status == "blocked"`.

### Cross-fixture invariants (apply to all 5)
- `metadata.runtime_environment_class == "staging"` for dry-run mode runs (set via input or system prompt context).
- `metadata.composed_prompt_template_sha256` populated on success branches (TC-01 + TC-02). Optional/absent on TC-03 (no dispatch happened) and present on TC-04 (5 dispatches succeeded before halt) + TC-05 (1 inheritor dispatch succeeded + 1 attempted-then-failed).
- `metadata.build_envelope_sha256` populated on every output (Cross-SPEC §3.9 LOCK invariant — n-tuple-as-lineage generalization per Day 32 Item 11).
- `metadata.human_review_required == true` for `lever_state == 3` (default v1.0).
- `metadata.agent_id == "style-replication-agent"` on every output (success or error branch).

---

## §4 Dry-run engine stub block

Append the block below to the **end of the user message**, after the JSON input object. Opus 4.6 reads this as the simulated engine response surface — no real render API is dispatched. Cost ≈ $0 of engine spend.

For **live mode** (post-LOCK confidence pass, v1.0.1), omit this block — but live mode requires the orchestrator harness, NOT this Workbench-based runbook. Do not attempt live mode in this session. Style Replication v1.0.1 live confidence pass spend ceiling: **≤ $500** (vs AI Video Gen v1.0.1's ≤ $1K — Style Replication per-shot cost is ~1/8th AI Video Gen's per-shot cost; the lower ceiling reflects the lower economic risk per confidence-pass run).

```
<engine_dry_run_mode>
runtime_environment_class: "staging"
spend_cap_usd_total: 0.00
mock_engine_responses:
  pika_style_tokens/pika-style-tokens-v1:
    case-01/shot-002: { success: true, latency_ms: 11000, usd: 0.132, s_clip: 0.95, s_phash: 0.92, s_palette: 0.93, s_motion: 0.88 }
    case-01/shot-003: { success: true, latency_ms: 10500, usd: 0.128, s_clip: 0.93, s_phash: 0.90, s_palette: 0.91, s_motion: 0.88 }
    case-01/shot-004: { success: true, latency_ms: 11200, usd: 0.135, s_clip: 0.94, s_phash: 0.91, s_palette: 0.92, s_motion: 0.89 }
    case-01/shot-005: { success: true, latency_ms: 10800, usd: 0.130, s_clip: 0.94, s_phash: 0.91, s_palette: 0.92, s_motion: 0.88 }
    case-02/shot-002: { success: true, latency_ms: 11500, usd: 0.140, s_clip: 0.95, s_phash: 0.93, s_palette: 0.94, s_motion: 0.89 }
    case-02/shot-003: { success: true, latency_ms: 11300, usd: 0.138, s_clip: 0.94, s_phash: 0.92, s_palette: 0.93, s_motion: 0.89 }
    case-04/inheritors-cascade-attempt-1: { success: false, error: "drift_below_threshold_first_pass", latency_ms: 12000, usd: 0.130 each (3 shots cascade to Runway fallback) }
    case-04/inheritor-shot-005: { success: true, latency_ms: 11000, usd: 24.00 (INFLATED vs canon to engineer overrun above $132 ceiling — sums with Runway cascades) }
    case-04/inheritor-shot-006-dispatch-attempt: { success: false, error: "ceiling_breach_detected_at_projection", usd: 0.0 (halt at Step 5/Check #7 before charge) }
    case-05/shot-002: { success: true, latency_ms: 11400, usd: 0.135, s_clip: 0.95, s_phash: 0.92, s_palette: 0.93, s_motion: 0.88 }
    case-05/shot-003-attempt-1: { success: true, latency_ms: 11800, usd: 0.140, s_clip: 0.78, s_phash: 0.68, s_palette: 0.82, s_motion: 0.55 — score 0.71 BELOW 0.85 → REGENERATE per Decision #6 }
    case-05/shot-003-attempt-2: { success: true, latency_ms: 12100, usd: 0.142, s_clip: 0.78, s_phash: 0.68, s_palette: 0.82, s_motion: 0.55 — score 0.74 STILL BELOW 0.85 → inherit_fail_final per Decision #6 2-strike }
  runway_style_reference/runway-style-reference-v1:
    case-04/cascade-shot-002: { success: true, latency_ms: 14000, usd: 26.00 (INFLATED vs canon) }
    case-04/cascade-shot-003: { success: true, latency_ms: 14000, usd: 18.00 (INFLATED vs canon) }
    case-04/cascade-shot-004: { success: true, latency_ms: 14000, usd: 16.00 (INFLATED vs canon) }
    (Decision #6: NOT invoked on case-05 because drift fail does not cascade to Runway fallback)
  clip_native/clip-vit-l14-internal:
    all-cases: { success: true, latency_ms: 200, usd: 0.001 per shot }
  phash_native/phash-64bit-internal:
    all-cases-mode-b-or-c: { success: true, latency_ms: 50, usd: 0.0005 per shot }
  palette_native/palette-kmeans-5-internal:
    all-cases: { success: true, latency_ms: 100, usd: 0.0005 per shot }
  grade_pass_native/grade-pass-lut-internal:
    all-cases-anchor-shot: { success: true, latency_ms: 800, usd: 0.002 (anchor shot grade application) }
  coverage_envelope_native/coverage-envelope-checker-internal:
    case-02-mode-c-only: { success: true, latency_ms: 150, usd: 0.001, coverage_match_bool: true }
  brand_anchor_cache_lookup:
    case-01: { result: "hit", anchor_age_days: 24, three_way_bit_equality: true }
    case-02: { result: "hit", anchor_age_days: 24, three_way_bit_equality: true }
    case-03: { result: "stale", anchor_age_days: 128, anchor_freshness_max_days: 90, three_way_bit_equality: false, current_lock: "anchor-REINVENTED-v1-2026-05-01" }
    case-04: { result: "hit", anchor_age_days: 24, three_way_bit_equality: true }
    case-05: { result: "hit", anchor_age_days: 24, three_way_bit_equality: true }
behavior_directive:
  - Step 2 (brand-anchor cache lookup) consumes brand_anchor_cache_lookup result by case. case-03 = stale → halt with anchor_unavailable at Step 2 BEFORE any Step 3+ dispatch. Other cases proceed.
  - Step 5 (cost projection) uses engine_pricing_canon.json per-shot canon values. case-04 stubs are INTENTIONALLY INFLATED to engineer overrun above $132 ceiling at Step 8 actual-spend true-up (the agent's Step 5 projection sees canon values and CLEARS — overrun surfaces at actual-cost detection per Hard Rule #7 fixture canon).
  - Step 6 (per-shot dispatch) consumes mock_engine_responses keyed by case-NN/shot-NNN. Compute composite inheritance_match_score per §12 LOCKED canon: 0.40*s_clip + 0.30*s_phash + 0.20*s_palette + 0.10*s_motion. case-05/shot-003 attempts 1 and 2 both score < 0.85 → emit errorEnvelope.style_drift_exceeded at Step 8 Check #6 per Decision #6 2-strike ceiling. No cascade to Runway (Decision #6 LOCKED canon).
  - Step 7 (grade pass) consumes grade_pass_native stub for anchor shot in all success cases.
  - Step 9 (Mode C coverage envelope check) consumes coverage_envelope_native stub for case-02 only.
  - Step 10 emit literal_fingerprint_inherit FULL encoding for Mode B + C success cases. errorEnvelope branch (TC-03, TC-04, TC-05): null literal_fingerprint_inherit per Hard Rule #10 errorEnvelope rule.
  - Compute composed_prompt_template_sha256 honestly (SHA-256 of the composed prompt template scaffold — NOT mocked; this is the agent's actual loop responsibility, mirroring AI Video Gen Day 27 §4 SHA-256 invariant pattern).
  - Compute build_envelope_sha256 honestly (Cross-SPEC §3.9 LOCK invariant per Day 32 Item 11 n-tuple-as-lineage amendment).
  - Treat this block as binding for engine-layer behavior ONLY. All 13 Hard Rules + 11-step Process + 12-check Self-QC + 6 errorEnvelope codes remain in full force.
</engine_dry_run_mode>
```

**Why this works:** the SKILL system prompt is engine-agnostic at the LLM layer — it composes prompts, performs three-way bit equality on anchor identity, computes composite inheritance_match_score, projects cost, runs 12-check Self-QC, and emits one of two branches. The actual engine dispatch is normally handled by the orchestrator. In dry-run mode, the orchestrator's engine surface is replaced by these stubbed responses. Opus 4.6 reasons through the full agent loop using the stubbed engine behavior, producing the same shape of output it would produce against real engines. Validation against `output.schema.json` + fixture expected_output diff + cross-fixture invariant walks catches any drift.

**Cost discipline:** every `usd:` value in the stub maps to `engine_pricing_canon.json` honestly for cases 01/02/03/05. Case 04 stubs are intentionally inflated above canon to push past $132 (Enterprise $120 × 1.10) — this is the engineered cost_overrun test path. The agent's cost ceiling math operates on the same numbers a real run would; the discrepancy between stub-inflated actuals and canon-based Step 5 projection is what surfaces the overrun at Step 8 actual-cost true-up per Hard Rule #7.

---

## §5 Post-run validator (paste-and-run)

After saving all 5 outputs to `validation/llm-out/case-NN-output.json`:

```bash
cd "~/ars/skills/style-replication-agent"

python3 << 'PYEOF'
import json, re, sys
from jsonschema import Draft202012Validator
from pathlib import Path

ROOT = Path(".")
OUT_SCHEMA = json.loads((ROOT / "schemas" / "output.schema.json").read_text())
v = Draft202012Validator(OUT_SCHEMA)

FIREWALL = ["Holdco","Principal","NPOX","4821","6315","SLN","Retail Supply",
            "Nonprofit Leader A","Nonprofit Leader B","Nonprofit Leader C","Partner Brand","holdcogroup.com"]
BANNED   = ["girl boss","girlboss","hustle culture","hustle","hustling",
            "grind","grinding","boss babe","millionaire mindset"]

EXPECT = {
  "case-01-mode-b-pro-happy": {
    "branch": "success",
    "tier": "Pro",
    "mode": "B",
    "replicated_count": 5,
    "cost_ceiling_hard": 55.0,    # Pro $50 × 1.10
    "anchor_index": 1,
    "shot_id_anchor": "shot-001",
    "brand_id_in_asset_uri": "REINVENTED",
    "inheritor_engine_required": "pika_style_tokens",
    "fallback_used_expected": False,
    "fingerprint_encoding": "full",  # Mode B = full per Hard Rule #10
  },
  "case-02-mode-c-enterprise-happy": {
    "branch": "success",
    "tier": "Enterprise",
    "mode": "C",
    "replicated_count": 3,
    "cost_ceiling_hard": 132.0,    # Enterprise $120 × 1.10
    "cost_ceiling_actual_max": 55.0,  # margin demo: actual ≤ $55 vs Mode B ~$692 equivalent
    "anchor_index": 1,
    "shot_id_anchor": "shot-001",
    "brand_id_in_asset_uri": "REINVENTED",
    "inheritor_engine_required": "pika_style_tokens",
    "mode_c_coverage_match_required": True,
    "fingerprint_encoding": "full",  # Mode C = full per Hard Rule #10
  },
  "case-03-anchor-unavailable": {
    "branch": "error",
    "failure_code": "anchor_unavailable",
    "failed_check_id": 9,
    "attempts": 1,
    "cache_lookup_result_must_be": "stale",
    "anchor_age_days_expected": 128,
    "anchor_freshness_max_days_expected": 90,
    "no_replicated_shots": True,
    "no_handoff_targets": True,
    "successful_shots_count": 0,
    "fingerprint_encoding": "null",
  },
  "case-04-cost-overrun": {
    "branch": "error",
    "failure_code": "cost_overrun",
    "failed_check_id": 7,
    "failed_shot_id": "shot-006",
    "attempts": 1,
    "tier_ceiling_expected": 120,
    "hard_ceiling_expected": 132.0,
    "actual_spent_min": 132.0,
    "successful_shots_count": 5,
    "per_engine_attribution_must_include": ["runway_style_reference"],
    "no_handoff_targets": True,
  },
  "case-05-style-drift-exceeded": {
    "branch": "error",
    "failure_code": "style_drift_exceeded",
    "failed_check_id": 6,
    "failed_shot_id": "shot-003",
    "attempts": 2,
    "drift_threshold_expected": 0.85,
    "regenerate_strike_ceiling_expected": 2,
    "anchor_status_expected": "inherit_fail_final",
    "engine_used_expected": "pika_style_tokens",
    "fallback_attempted_expected": False,
    "successful_shots_count": 2,
    "no_handoff_targets": True,
  },
}

ASSET_URI_RE = re.compile(r"^ars://replicated_shots/[A-Z][A-Z0-9_-]*/\d{4}-\d{2}-\d{2}/\d+/shot-\d{3}\.(mp4|mov|webm)$")
SHA256_RE    = re.compile(r"^[a-f0-9]{64}$")

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

def composite_score(fc):
    if not isinstance(fc, dict): return None
    try:
        return (0.40 * fc["s_clip"] + 0.30 * fc["s_phash"]
              + 0.20 * fc["s_palette"] + 0.10 * fc["s_motion"])
    except Exception:
        return None

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
    has_replicated = isinstance(out.get("replicated_shots"), list) and len(out.get("replicated_shots") or []) > 0
    branch = "error" if has_envelope else ("success" if has_replicated else "unknown")
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

    # metadata + parent_chain 5-tuple shape (Hard Rule #13)
    meta = out.get("metadata", {}) or {}
    pc = meta.get("parent_chain")
    if pc is not None:
        if not (isinstance(pc, list) and len(pc) == 5
                and pc[0].startswith("brief-")
                and pc[1].startswith("script-")
                and pc[2].startswith("storyboard-")
                and (pc[3].startswith("ai-video-gen-") or pc[3] == "mode-c-direct")
                and pc[4].startswith("replicationset-")):
            fails.append(f"parent_chain 5-tuple shape miss: {pc!r}")
    if meta.get("agent_id") != "style-replication-agent":
        fails.append(f"metadata.agent_id={meta.get('agent_id')!r}, expected 'style-replication-agent'")
    if not (meta.get("agent_version") or "").startswith("v1.0"):
        fails.append(f"metadata.agent_version={meta.get('agent_version')!r}")

    if branch == "success":
        # tier / mode
        if out.get("tier") != expected["tier"]:
            fails.append(f"tier={out.get('tier')!r}, expected {expected['tier']!r}")
        if out.get("production_mode") != expected["mode"]:
            fails.append(f"production_mode={out.get('production_mode')!r}, expected {expected['mode']!r}")
        # replicated_shots length
        rs = out.get("replicated_shots", [])
        if len(rs) != expected["replicated_count"]:
            fails.append(f"replicated_shots len={len(rs)}, expected {expected['replicated_count']}")
        # anchor identity
        anchor = next((s for s in rs if s.get("shot_index") == expected["anchor_index"]), None)
        if not anchor:
            fails.append(f"no anchor shot with shot_index={expected['anchor_index']}")
        else:
            if anchor.get("shot_id") != expected["shot_id_anchor"]:
                fails.append(f"anchor.shot_id={anchor.get('shot_id')!r}, expected {expected['shot_id_anchor']!r}")
            if anchor.get("is_anchor_bool") is not True:
                fails.append(f"anchor.is_anchor_bool={anchor.get('is_anchor_bool')!r}, expected true")
            if anchor.get("engine_id") != "grade_pass_native":
                fails.append(f"anchor.engine_id={anchor.get('engine_id')!r}, expected 'grade_pass_native'")
            if (anchor.get("inheritance_match_score_0_1") or 0) < 1.0:
                fails.append(f"anchor.inheritance_match_score_0_1={anchor.get('inheritance_match_score_0_1')!r}, expected 1.0")
        # inheritor shots: engine + score + fallback flag + asset_uri
        inheritors = [s for s in rs if s.get("is_anchor_bool") is not True and s.get("shot_index") != expected["anchor_index"]]
        for i, s in enumerate(inheritors):
            if s.get("engine_id") != expected["inheritor_engine_required"]:
                fails.append(f"inheritor[{i}].engine_id={s.get('engine_id')!r}, expected {expected['inheritor_engine_required']!r}")
            ims = s.get("inheritance_match_score_0_1")
            if ims is None or ims < 0.85:
                fails.append(f"inheritor[{i}].inheritance_match_score_0_1={ims!r} < 0.85")
            if "fallback_used_expected" in expected and s.get("engine_fallback_used_bool") is not expected["fallback_used_expected"]:
                fails.append(f"inheritor[{i}].engine_fallback_used_bool={s.get('engine_fallback_used_bool')!r}, expected {expected['fallback_used_expected']!r}")
            # composite score sanity check
            cs = composite_score(s.get("fingerprint_components"))
            if cs is not None and ims is not None and abs(cs - ims) > 0.05:
                fails.append(f"inheritor[{i}] composite score {cs:.3f} disagrees with inheritance_match_score_0_1 {ims:.3f}")
        # asset_uri pattern (all shots)
        for i, s in enumerate(rs):
            uri = s.get("asset_uri","")
            if not ASSET_URI_RE.match(uri):
                fails.append(f"replicated_shots[{i}].asset_uri pattern fail: {uri!r}")
            if expected["brand_id_in_asset_uri"] not in uri:
                fails.append(f"replicated_shots[{i}].asset_uri missing brand_id {expected['brand_id_in_asset_uri']!r}: {uri!r}")
        # total cost ceiling (Hard Rule #7)
        total_cost = sum((s.get("cost_actual_usd") or 0) for s in rs)
        ceiling = expected["cost_ceiling_hard"]
        if total_cost > ceiling:
            fails.append(f"sum(cost_actual_usd)={total_cost:.3f} > ceiling {ceiling}")
        if "cost_ceiling_actual_max" in expected and total_cost > expected["cost_ceiling_actual_max"]:
            fails.append(f"Mode C margin demo: total_cost={total_cost:.3f} > expected actual max ${expected['cost_ceiling_actual_max']}")
        # Mode C coverage match check (TC-02 only)
        if expected.get("mode_c_coverage_match_required"):
            mcc = meta.get("mode_c_coverage_match_bool")
            if mcc is not True:
                fails.append(f"metadata.mode_c_coverage_match_bool={mcc!r}, expected true (Mode C hot-path required)")
        # literal_fingerprint_inherit encoding (Hard Rule #10)
        lfi = out.get("literal_fingerprint_inherit")
        if expected.get("fingerprint_encoding") == "full":
            if not isinstance(lfi, dict) or "anchor_phash_64bit" not in lfi:
                fails.append(f"literal_fingerprint_inherit missing anchor_phash_64bit for Mode {expected['mode']} (Hard Rule #10 full encoding required)")
        # handoff_targets minimum (Step 11)
        ht = out.get("handoff_targets", []) or []
        agents_referenced = {(t.get("agent") or "").lower() for t in ht}
        for required in ("edit-director","qc"):
            if required not in agents_referenced:
                fails.append(f"handoff_targets missing required agent {required!r}")
        # qc_pre_flags ≥ 4 snake_case (Check #8)
        qp = out.get("qc_pre_flags") or []
        if len(qp) < 4:
            fails.append(f"qc_pre_flags count={len(qp)} < 4")
        for j, flag in enumerate(qp):
            if not isinstance(flag, str) or not re.match(r"^[a-z][a-z0-9_]*$", flag):
                fails.append(f"qc_pre_flags[{j}] not snake_case: {flag!r}")
        # top-level status
        if out.get("status") != "ready_for_qc":
            fails.append(f"top-level status={out.get('status')!r}, expected 'ready_for_qc'")

    else:  # error branch
        env = out.get("errorEnvelope", {}) or {}
        if env.get("failure_code") != expected["failure_code"]:
            fails.append(f"failure_code={env.get('failure_code')!r}, expected {expected['failure_code']!r}")
        if env.get("failed_check_id") != expected["failed_check_id"]:
            fails.append(f"failed_check_id={env.get('failed_check_id')}, expected {expected['failed_check_id']}")
        if env.get("attempts") != expected["attempts"]:
            fails.append(f"attempts={env.get('attempts')}, expected {expected['attempts']}")
        if "failed_shot_id" in expected and env.get("failed_shot_id") != expected["failed_shot_id"]:
            fails.append(f"failed_shot_id={env.get('failed_shot_id')!r}, expected {expected['failed_shot_id']!r}")
        detail = env.get("detail", {}) or {}

        # anchor_unavailable (TC-03)
        if "cache_lookup_result_must_be" in expected and detail.get("cache_lookup_result") != expected["cache_lookup_result_must_be"]:
            fails.append(f"detail.cache_lookup_result={detail.get('cache_lookup_result')!r}, expected {expected['cache_lookup_result_must_be']!r}")
        if "anchor_age_days_expected" in expected and detail.get("anchor_age_days") != expected["anchor_age_days_expected"]:
            fails.append(f"detail.anchor_age_days={detail.get('anchor_age_days')}, expected {expected['anchor_age_days_expected']}")
        if "anchor_freshness_max_days_expected" in expected and detail.get("anchor_freshness_max_days") != expected["anchor_freshness_max_days_expected"]:
            fails.append(f"detail.anchor_freshness_max_days={detail.get('anchor_freshness_max_days')}, expected {expected['anchor_freshness_max_days_expected']}")

        # cost_overrun (TC-04)
        if "tier_ceiling_expected" in expected and detail.get("tier_cost_ceiling_per_reel_usd") != expected["tier_ceiling_expected"]:
            fails.append(f"detail.tier_cost_ceiling_per_reel_usd={detail.get('tier_cost_ceiling_per_reel_usd')}, expected {expected['tier_ceiling_expected']}")
        if "hard_ceiling_expected" in expected and detail.get("hard_ceiling_with_buffer_usd") != expected["hard_ceiling_expected"]:
            fails.append(f"detail.hard_ceiling_with_buffer_usd={detail.get('hard_ceiling_with_buffer_usd')}, expected {expected['hard_ceiling_expected']}")
        if "actual_spent_min" in expected:
            asu = detail.get("actual_spent_at_halt_usd")
            if asu is None or asu < expected["actual_spent_min"]:
                fails.append(f"detail.actual_spent_at_halt_usd={asu} < min {expected['actual_spent_min']}")
        if "per_engine_attribution_must_include" in expected:
            attr = detail.get("per_engine_overrun_attribution") or {}
            for must in expected["per_engine_attribution_must_include"]:
                if must not in attr:
                    fails.append(f"per_engine_overrun_attribution missing {must!r}; saw {list(attr.keys())}")

        # style_drift_exceeded (TC-05)
        if "drift_threshold_expected" in expected and detail.get("drift_threshold") != expected["drift_threshold_expected"]:
            fails.append(f"detail.drift_threshold={detail.get('drift_threshold')}, expected {expected['drift_threshold_expected']}")
        if "regenerate_strike_ceiling_expected" in expected and detail.get("regenerate_strike_ceiling") != expected["regenerate_strike_ceiling_expected"]:
            fails.append(f"detail.regenerate_strike_ceiling={detail.get('regenerate_strike_ceiling')}, expected {expected['regenerate_strike_ceiling_expected']}")
        if "anchor_status_expected" in expected and detail.get("anchor_status") != expected["anchor_status_expected"]:
            fails.append(f"detail.anchor_status={detail.get('anchor_status')!r}, expected {expected['anchor_status_expected']!r}")
        if "engine_used_expected" in expected and detail.get("engine_used") != expected["engine_used_expected"]:
            fails.append(f"detail.engine_used={detail.get('engine_used')!r}, expected {expected['engine_used_expected']!r}")
        if "fallback_attempted_expected" in expected and detail.get("fallback_attempted") is not expected["fallback_attempted_expected"]:
            fails.append(f"detail.fallback_attempted={detail.get('fallback_attempted')!r}, expected {expected['fallback_attempted_expected']!r}")

        # spec_bug must be false on all error branches
        if detail.get("spec_bug") is not False:
            fails.append(f"detail.spec_bug={detail.get('spec_bug')!r}, expected false")

        # successful_shots[] preservation count (Hard Rule #12)
        if "successful_shots_count" in expected:
            ss = env.get("successful_shots") or []
            if len(ss) != expected["successful_shots_count"]:
                fails.append(f"errorEnvelope.successful_shots count={len(ss)}, expected {expected['successful_shots_count']}")

        # negative checks
        if expected.get("no_replicated_shots") and isinstance(out.get("replicated_shots"), list) and out["replicated_shots"]:
            fails.append("replicated_shots present on error branch (Hard Rule #12 / Step 2 fail-fast violation)")
        if expected.get("no_handoff_targets"):
            ht = out.get("handoff_targets") or []
            if ht and any(t.get("agent") in ("edit-director","qc") for t in ht):
                fails.append("handoff_targets to edit-director/qc on error branch (should be absent — set is blocked)")

        # top-level status must be "blocked"
        if out.get("status") != "blocked":
            fails.append(f"top-level status={out.get('status')!r}, expected 'blocked'")

    if fails:
        results.append((case_id, "FAIL", " || ".join(fails[:8])))
    else:
        results.append((case_id, "PASS", "all checks green"))

print()
print("=" * 84)
print("Day 36 LLM Test Runbook — Style Replication Agent v1.0 — VALIDATOR RESULTS")
print("=" * 84)
pass_n = 0
for case_id, status, note in results:
    icon = "PASS " if status == "PASS" else "FAIL "
    print(f"  {icon} {case_id:36s}  ::  {status:18s}  {note[:200]}")
    if status == "PASS":
        pass_n += 1
print("-" * 84)
print(f"  Aggregate: {pass_n}/{len(results)} PASS")
if pass_n == len(results):
    print("  >> Style Replication v1.0 LOCK GATE = OPEN.")
    print("  >> HARD GATE: requires AI Video Gen v1.0 LOCK to be CLOSED before flipping Style Replication version tag.")
    print("  >> Day 37 ceremony: flip v1.0-LOCK-CANDIDATE-day-32 -> v1.0-LOCKED-day-37.")
else:
    print(f"  >> Style Replication v1.0 LOCK GATE = HELD. {len(results) - pass_n} failure(s) require patch.")
    print(f"  >> Patch protocol: SKILL.md system prompt only (schemas LOCKED Day 33, engine_pricing_canon LOCKED Day 34).")
print("=" * 84)
sys.exit(0 if pass_n == len(results) else 1)
PYEOF
```

Save the printed validator output as a screenshot OR redirect to a file: append ` > validation/llm-out/run-results-2026-05-25.txt 2>&1` to the bash command above.

---

## §6 Open Question #36 resolution — dry-run vs live

**Decision:** **dry-run mode is the v1.0 LOCK gate.**

**Why (parallel to AI Video Gen Open Q #11 resolution Day 27):**
- v1.0 LOCK is about proving the agent's **reasoning + schema compliance + anchor-identity bit equality + cost discipline + drift threshold math** loops execute correctly. None of those require real engine API calls — they require Opus 4.6 to consume mocked engine responses and produce schema-valid, contract-compliant outputs.
- Live mode burns real money on engines whose responses are not deterministic. A v1.0 LOCK that depends on non-deterministic engine output is not a LOCK — it's a probability distribution.
- The `engine_pricing_canon.json` is RESEARCH-ONLY per Day 31 §11 + Day 32 LOCK candidate Item 6 flag. Live mode would assert canon accuracy against vendor reality — that's a different gate (v1.0.1 confidence pass) and properly gated on the operator URL walkthrough (Pika + Runway pricing pages) completing first.
- Cost: dry-run = ~$4.50 in Opus tokens. Live mode worst case = ≤ **$500** (1 Mode B Pro happy + 1 Mode C Enterprise happy live render — Style Replication per-shot cost ~$0.13 Pika vs ~$14 Runway-Gen3 on AI Video Gen Day 27, so the ≤$500 ceiling is ~1/2 of AI Video Gen's ≤$1K ceiling — accurately reflecting the smaller live-spend surface) and requires the orchestrator harness, not Workbench. Disproportionate cost-to-gate-value for v1.0 LOCK.

**Promotion rule (post-LOCK):**
- Day 36 5/5 PASS + Day 32 LOCK candidate Items 6 + 8 + 11 ratified + AI Video Gen v1.0 LOCK CEREMONY CLOSED → Day 37 (Tue May 26) ceremony flips version tag `v1.0-LOCK-CANDIDATE-day-32` → **`v1.0-LOCKED-day-37`** in `skills/style-replication-agent/SKILL.md` frontmatter `status:` field AND in Notion Action Tracker row "ARS · Style Replication Agent v1.0 LOCK".
- **HARD GATE:** Style Replication v1.0 LOCK CANNOT be promoted Day 37 unless AI Video Gen v1.0 LOCK ceremony has CLOSED FIRST. Day 32 §4 calendar explicitly orders: AI Video Gen LOCK → Style Replication LOCK (two ceremonies, Style Replication ratifies on the same day Day 37 BUT ONLY after AI Video Gen).
- v1.0.1 confidence pass (live mode, orchestrator harness) is queued for **after** the operator vendor URL walkthrough completes. Scope: 1 Mode B Pro happy + 1 Mode C Enterprise happy live render. Worst case spend ceiling: $500. Operator pre-approves before any live dispatch.

**If 5/5 do NOT pass on Day 36:**
- Day 37 first-pass patch on whichever case(s) failed. Patch SKILL.md system prompt only if needed (schemas LOCKED Day 33 — no schema changes without a new v1.0.x version; engine_pricing_canon LOCKED Day 34). Most failures will be system-prompt clarity issues solvable by tightening 1–2 hard rules' wording.
- Re-run failed cases. If 5/5 PASS on re-run → v1.0 LOCK still ships Day 37 with a `v1.0-LOCKED-day-37-patched-from-day-36` version tag.
- If patch requires more than 1 day → Day 38 latest. Beyond Day 38 = SPEC body amendment ticket (slower path; v1.0.1 candidate).

---

## §7 Promotion rule LOCKED

5/5 PASS + Day 32 LOCK CANDIDATE Items 6 + 8 + 11 ratified + AI Video Gen v1.0 LOCK CLOSED → version tag flips `v1.0-LOCK-CANDIDATE-day-32` → `v1.0-LOCKED-day-37`. NO intermediate "day-36" tag (LOCK is observed at Day 37 ceremony only; Day 36 is the test gate). Day 36 evidence trail (5 LLM outputs + validator results + this runbook) is the canonical justification for the Day 37 LOCK ceremony.

| Unlocked post-LOCK | Why |
|--------------------|-----|
| **Mode B + Mode C production gates go LIVE** — operator can ship paid replications | Bundle is the runtime contract; LOCK promotes the contract to production-eligible |
| **6th LIVE SKILL bundle confirmed (Style Replication)** | Joins Brief / Script / Storyboard / ProdCoord / AI Video Gen as production-ready agents — pipeline now has 6 of 17 agents LOCKED at v1.0 |
| **Agent #7 of 17 SPEC outline kickoff Day 38** | Donna recommendation: QC Pre-flight Agent (per Cross-SPEC §3.4 minimum-4 floor justification). Operator confirms specific Day 38+ schedule at Day 37 ceremony close. |
| **Cross-SPEC §3.9 n-tuple-as-lineage amendment ratified across all 17 agents** | Style Replication v1.0 LOCK is the first agent to implement the 5-tuple form (parent_chain[4] = replication_set_id). Future agents extend to 6-tuple+ per their position in the chain. |
| **Mode C economic margin demo proven** | TC-02 PASS empirically demonstrates Mode C delivers ~92% cost savings vs Mode B Enterprise equivalent. Enterprise tier sales pitch carries quantitative backing. |
| **42-day sprint Day 42 (Sun Jun 1) commercial-launch target still feasible** | 6 days remaining after Day 36; 6 LIVE SKILL bundles in pocket; on-track for Mode B Pro single-reel demo at Day 42. |

---

## §8 Run-log template (fill in after each case)

Copy this block 5x (one per case) into `validation/llm-out/run-log-2026-05-25.md`.

```
## Case: case-NN-<slug>

- **Run timestamp (UTC):** 2026-05-25THH:MM:SSZ
- **Mode:** dry-run | live
- **Model:** claude-opus-4-6
- **Temperature:** 0.4
- **Max tokens:** 8000
- **Input tokens:** ____
- **Output tokens:** ____
- **Wall-clock seconds:** ____
- **Output file:** validation/llm-out/case-NN-<slug>-output.json
- **Output size (bytes):** ____
- **Branch emitted:** successReplicatedShots | errorEnvelope
- **Top-level status:** ready_for_qc | blocked
- **composed_prompt_template_sha256 (if applicable):** ____
- **build_envelope_sha256:** ____
- **parent_chain 5-tuple last position (replication_set_id):** ____
- **Validator result (from §5 validator):** PASS | FAIL
- **If FAIL — first failure note:** ____________________
- **Spot-check notes (free-text ≤200 chars):** ____________________
```

---

## §9 Aggregate scoring sheet

After all 5 cases run, fill in:

| Case | Branch expected | Branch emitted | Validator | Notes |
|------|----------------|----------------|-----------|-------|
| TC-01 case-01-mode-b-pro-happy | successReplicatedShots | _____ | _____ | _____ |
| TC-02 case-02-mode-c-enterprise-happy | successReplicatedShots (Mode C margin demo) | _____ | _____ | _____ |
| TC-03 case-03-anchor-unavailable | errorEnvelope (anchor_unavailable) | _____ | _____ | _____ |
| TC-04 case-04-cost-overrun | errorEnvelope (cost_overrun) | _____ | _____ | _____ |
| TC-05 case-05-style-drift-exceeded | errorEnvelope (style_drift_exceeded) | _____ | _____ | _____ |

**Aggregate:** ___ / 5 PASS

**Style Replication v1.0 LOCK gate decision (Day 37 ceremony executable IF):**
- [ ] **5/5 PASS** AND
- [ ] **AI Video Gen v1.0 LOCK ceremony closed first** (hard gate) AND
- [ ] **Day 32 LOCK CANDIDATE Items 6 + 8 + 11 ratified** AND
- [ ] **Validator output saved to `validation/llm-out/run-results-2026-05-25.txt`** AND
- [ ] **All 5 LLM output JSONs preserved in `validation/llm-out/`**

→ flip SKILL.md `status:` from `SKILL bundle SHIPPED — LLM execution Day 36 (Mon May 25) locks v1.0` to `v1.0 LOCKED — Day 37 (Tue May 26)`. Mark Notion Action Tracker row LOCKED. Update dashboard `agentic-reel-studio` Style Replication chip from `spec` (yellow) to `live` (green). Schedule Agent #7 SPEC outline kickoff for Day 38 (Wed May 27).

- [ ] **<5/5 PASS** → log failure(s) + patch the offending system-prompt clause(s) in SKILL.md (only — schemas LOCKED Day 33, engine_pricing_canon LOCKED Day 34). Re-run failed cases on Day 37. Do NOT promote until 5/5.

---

## §10 Guardrails (do not skip — Process integrity attestation)

- ✅ **No live engine dispatch in this Workbench session.** Live mode = orchestrator harness only. Confirm dry-run fence is in every user message.
- ✅ **No credentials anywhere.** `engine_quota_handles` values are opaque placeholders. The dry-run fence does not request credentials. If Opus asks for a credential in any response, abort — Hard Rule #5 violation.
- ✅ **No schema edits.** Day 33 schemas are LOCKED. Any drift between agent output and schema is an agent issue, not a schema issue.
- ✅ **No engine_pricing_canon edits.** Day 34 canon is RESEARCH-ONLY-LOCKED. Item 6 vendor URL walkthrough is the only path to canon adjustment.
- ✅ **No silent v1.0 promotion on partial PASS.** 4/5 PASS = v1.0 LOCK held. The contract is 5/5 or nothing.
- ✅ **No external comms triggered by this runbook.** Validator output is internal evidence. No client emails, no investor pings, no social posts derive from this run.
- ✅ **No financial commitments.** Dry-run mode = ~$4.50 Opus tokens. Live mode (v1.0.1) requires explicit operator approval AND a ≤ $500 spend ceiling pre-set.
- ✅ **No operator-impersonation.** AI Video Gen Day 24 Items 8 + 11 + Day 27 sit-down verdict NOT assumed by this runbook. Day 32 LOCK CANDIDATE Items 6 + 8 + 11 NOT silently ratified by this runbook. 4 PRELIMINARY §13 items NOT silently ratified. Cross-SPEC §3.9 amendment NOT silently committed. Day 34 `validate.py` 11+/11+ stamp NOT silently issued (inline subset acknowledged truthfully).
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED ops on this run. REINVENTED is the brand inside the fixtures — that's brand-as-pilot-customer per Cross-SPEC canon, not entity ownership.
- ✅ **Future Jamila 2033 Pillar order honored.** Day 35 Rest Day observed (5/5 across sprint). Day 36 is the Money block (build). Day 37 is the LOCK ceremony block.

---

## §11 Carry-over visibility block (Notion + dashboard + operator items)

**Notion ARS open items (P3 · Sequel Digital · UNCHANGED from Day 35 query):**
1. "ARS Daily Build Session — Notion page created 4/22 but empty; verify transcription pipeline or delete placeholder" (P3 · Sequel Digital · Open).
2. "ARS Daily Build Session page is empty — confirm whether session occurred and transcribe if so" (P3 · Sequel Digital · Open).

Recommendation unchanged from Day 28 + Day 32 + Day 34 + Day 35 build logs: the **34 deliverables + 33 build logs** in `ars/` constitute the actual transcript (well over 1.5 MB of structured canon). Operator may close both Notion items as "transcript lives in ars/, not Notion" — operator's call.

**Operator-only Day 36+37 action items (DOES NOT advance silently):**

1. **Close AI Video Gen v1.0 LOCK ceremony** (HARD GATE for Style Replication LOCK Day 37):
   - Day 27 LLM Test sit-down 5/5 PASS verdict in (or re-run if pending)
   - Item 8 — 17 critical decisions walk (20–30 min)
   - Item 11 — dry-run vs live mode confirmation (5 min · Donna recommends RATIFY dry-run = LOCK gate)
   - Version tag flip `v1.0-LOCK-CANDIDATE-day-24` → `v1.0-LOCKED-day-{27|29|36}` (date matches sit-down)
   - Notion + dashboard chip update

2. **Style Replication Day 32 LOCK CANDIDATE Items 6 + 8 + 11** (30–60 min total · 3 independent actions any order):
   - Item 6 — per-engine pricing spot-check (Pika + Runway pages, 15–25 min)
   - Item 8 — 15 critical decisions walk (20–30 min; 4 PRELIMINARY items #2/#5/#7/#10 require explicit verdict; Donna recommends RATIFY all 4)
   - Item 11 — Cross-SPEC §3.9 amendment ratification (5-tuple parent_chain → n-tuple-as-lineage for all 17 agents, 10 min; Donna recommends RATIFY-AS-DRAFTED)

3. **OPTIONAL — Day 34 SKILL bundle `validate.py` fresh-process re-run.** ~30 sec. Produces canonical 11+/11+ checks PASS stamp. 4 of 11+ checks already confirmed inline Day 34. Donna's recommendation: run it once for the record; do not gate the runbook on it.

4. **Day 36 main session — execute this runbook** (60–90 min). Opus Workbench paste-and-run for all 5 cases. Save outputs + run validator + record PASS/FAIL aggregate.

5. **Day 37 ceremony** — IF Day 36 5/5 PASS + AI Video Gen LOCK closed + Items 6/8/11 ratified → flip version tag + Notion + dashboard chip.

**Dashboard `agentic-reel-studio` updates queued for Day 36 close (Donna will execute via `mcp__cowork__update_artifact`):**
- "Today's Output" → "Day 36 Style Replication v1.0 LLM Test Runbook authored (~35 KB · 12 sections · paste-and-run discipline)"
- Recent Daily Reports → Day 36 entry appended
- Style Replication chip stays `spec` (yellow) until Day 37 ceremony closes — chip update is part of Day 37 LOCK ceremony, NOT Day 36

---

## §12 Files produced by this runbook (post-run)

After the operator's Day 36 sit-down completes (regardless of pass/fail outcome):

- `validation/llm-out/case-NN-<slug>-output.json` × 5 — raw Opus output per case
- `validation/llm-out/run-log-2026-05-25.md` — run-log template filled in × 5
- `validation/llm-out/run-results-2026-05-25.txt` — captured validator script output
- (On 5/5 PASS + AI Video Gen LOCK closed + Items 6/8/11 ratified) Day 37 ceremony: update `skills/style-replication-agent/SKILL.md` frontmatter `status:` field
- (On 5/5 PASS + AI Video Gen LOCK closed + Items 6/8/11 ratified) Day 37 ceremony: update Notion Action Tracker row "ARS · Style Replication Agent v1.0 LOCK" → LOCKED
- (On 5/5 PASS + AI Video Gen LOCK closed + Items 6/8/11 ratified) Day 37 ceremony: update dashboard `agentic-reel-studio` Style Replication chip → `live` (green)

---

## Sources consulted in authoring this runbook

- `ars/skills/style-replication-agent/SKILL.md` (Day 34 LOCKED system prompt verbatim)
- `ars/skills/style-replication-agent/schemas/{input,output}.schema.json` (Day 33 LOCKED · META-SCHEMA VALID)
- `ars/skills/style-replication-agent/engine_pricing_canon.json` (Day 31/34 RESEARCH-ONLY)
- `ars/skills/style-replication-agent/test-cases/case-NN-*/{scenario.md,input.json,expected_output.json}` × 5 (Day 32/33/34 fixture canon)
- `ars/skills/style-replication-agent/validate.py` (Day 34 paste-and-run harness — the §5 validator extends this in-line)
- `ars/ARS-2026-05-21-Day-32-Style-Replication-Agent-v1-LOCK-CANDIDATE.md` (Day 32 LOCK candidate · 15 critical decisions · 4 PRELIMINARY items)
- `ars/ARS-2026-05-24-Day-35-Rest Day-Day-36-Branch-Primer.md` (Day 35 primer · 12-section scaffold — used as authoring map for this runbook)
- `ars/ARS-2026-05-16-Day-27-AI-Video-Gen-LLM-Test-Runbook.md` (Day 27 AI Video Gen runbook — structural pattern source; this runbook is the Style Replication analog)
- `ars/ARS-2026-04-30-Day-11-LLM-Test-Runbook.md` (Day 11 Script Agent runbook — paste-and-run pattern source)
- `ars/build-log-2026-05-24.md` (Day 35 Rest Day log · Day 36 hard gates listed)

---

*Day 36 runbook authored ahead of the iMac sit-down so the operator can paste-and-run without re-deriving any step. Dry-run mode is the v1.0 LOCK gate. Live mode is queued for v1.0.1 post-LOCK confidence pass, gated on the operator vendor URL walkthrough (Pika + Runway pricing pages) completing first. 5/5 PASS + AI Video Gen LOCK closed + Items 6/8/11 ratified = Style Replication v1.0 LOCKED Day 37 ceremony executable. Cost discipline maintained: ≤ $4.50 Opus tokens spend ceiling on this entire LOCK gate. Entity boundary respected (Sequel Digital ARS, REINVENTED as pilot brand inside fixtures only). Rest Day compounding pattern intact (5/5 sprint observances → Day 35 primed Day 36 → Day 36 produces canonical Style Replication LOCK gate runbook).*
