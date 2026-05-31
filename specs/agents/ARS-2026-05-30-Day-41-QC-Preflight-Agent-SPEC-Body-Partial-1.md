# ARS — QC Pre-flight Agent v1.0 SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14)

**Date:** Sat May 30, 2026 (Day 41 of 42 · Wk6)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 1 — §6 + §7 + §10 + §14 LOCKED-as-drafted Day 41. §8 + §9 + §11 + §12 + §13 + §15 + §16 reserved Day 43 partial 2 (Day 42 Sun = Rest Day, no build). v1.0 LOCK CANDIDATE + schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK follow on the established cadence, inside the post-launch hardening window.
**Pattern source:** `ARS-2026-05-19-Day-30-Style-Replication-Agent-SPEC-Body-Partial-1.md` §6/§7/§10/§14 (Day 30 partial 1 — proven shape inherited verbatim) and `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` §6/§7/§10/§14 (Day 22 grandparent pattern).
**Outline source:** `ARS-2026-05-29-Day-40-QC-Preflight-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 40).
**11-point gate source:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §13 (LOCKED — the canonical acceptance gate inlined verbatim into §7).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — pipeline roster position 14 "QC" + §11 Brand Firewall).
**Predecessor canon (read-only — NOT modified by this document):** AI Video Gen v1.0 SPEC LOCK candidate (Day 24) + output.schema.json (Day 25) + SKILL bundle (Day 26) + Day 27 LLM Test Runbook. Style Replication v1.0 LOCK candidate (Day 32) + schemas (Day 33) + SKILL bundle (Day 34) + Day 36 LLM Test Runbook. **Both production-tier LOCK ceremonies remain OPERATOR-GATED entering Day 41 — file-state confirmed (version tags unflipped on both SKILL.md frontmatters). This partial 1 references LOCK-as-drafted canon (text-stable) without depending on operator-gated ratification, the same posture as the Style Replication Day 30 partial 1.**

> **Authoring discipline (LOCK signal):** §6 + §7 + §10 + §14 are LOCKED-as-drafted Day 41. The §13 critical-decisions walk on Day 43 may amend §10's 6-tuple parent_chain extension decision (gated on the Cross-SPEC §3.9 n-tuple amendment ratification) and the route-back automation depth; those are the only forward-looking edit slots in this partial 1. Everything else is canon as of this document.

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this partial's authoring, on-disk file-state confirms **both prior LOCK ceremonies remain OPERATOR-GATED.** AI Video Gen SKILL.md frontmatter still reads `status: v1.0 SKILL bundle SHIPPED — LLM execution Day 27 locks v1.0` (no flip to LOCKED). Style Replication SKILL.md still reads `v1.0 LOCK target: Day 37 — hard-gated on AI Video Gen v1.0 LOCK ceremony first` (no flip). The Day 36 Style Replication LLM Test Runbook execution + both LOCK ceremonies are unconfirmed. QC Pre-flight v1.0 LOCK will hard-gate itself on those closing first — this body partial is forward-design over LOCK-stable text artifacts only, with zero production output consumed.

---

## §6 — 12-Check Self-QC List (LOCKED-as-drafted Day 41)

The QC Pre-flight Agent runs this 12-check list **on its own constructed verdict report** before emitting `successPreflightReport` (or before finalizing an `errorEnvelope`/soft-hold). The check shape is inherited verbatim from Brief / Script / Storyboard / Production Coord / AI Video Gen / Style Replication §6 (proven 6× across the pipeline; QC Pre-flight is the 7th defense-in-depth firewall pass). Failure semantics are LOCKED inheritance from ProdCoord §6 + AI Video Gen §6 + Style Replication §6 — the agent retries once on a recoverable self-QC failure and halts on the second.

**Critical distinction — self-QC vs. the verdict loop:** This agent is itself a quality gate. The **11-step verdict loop (§5, outline)** is the agent adjudicating the *reel*; the **§6 self-QC list (this section)** is the agent adjudicating *its own verdict report* — confirming the report it is about to emit is well-formed, evidence-complete, and free of the operator-impersonation anti-pattern, before that report becomes a routing instruction downstream. A FAIL in §6 means the agent built a malformed verdict, not that the reel failed. The reel verdict (pass/fail/reshoot/hold) is carried in the report payload; the §6 result decides whether that report is fit to ship.

**QC retry policy (inherited, LOCKED):** First self-QC failure → regenerate the offending verdict-report field set with concrete fix instructions inlined into the next attempt. Second self-QC failure → emit `errorEnvelope` with `failure_code: "preflight_qc_agent_failed"`, `attempts == 2`, halt. **No third attempt.** Predictable failure surface beats best-effort recovery — same 2-strike contract every agent in the pipeline honors.

**Defense-in-depth (7th and final automated layer):** Every check here is the agent's own pass, but several (entity firewall, qc_pre_flags floor, cost ceiling, tier↔mode) re-adjudicate the cumulative upstream surface one final time. The 7th re-check is the LAST automated guardrail before pixels enter post / distribution. Because QC Pre-flight calls **no generative engine**, a self-QC failure here never wastes engine spend — but a *missed* failure (a malformed PASS) is the single most expensive defect class in the pipeline (a brand-safety incident on a published surface). The narrowed failure surface (9 LOCKED errorEnvelope codes + slot-11 catch-all after Day 41 LOCK) does not relax firewall discipline — it tightens it.

### 6.1 The 12 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **Upstream success verification — every consumed upstream branch is its success type, NOT `errorEnvelope`.** | `upstream_not_success` | Assert the primary input `output_type == "successReplicatedShots"` (Style Replication happy path) AND, when a Mode B forensic cross-check input is present, `successRenderedShots` (AI Video Gen). Any consumed branch that is `errorEnvelope` = halt with `upstream_not_success` — you cannot QC a production output that already failed. This runs FIRST (Step 1 of the verdict loop) because every downstream check assumes a valid production payload. Cite which upstream agent + which branch failed in `detail.upstream_failure`. |
| 2 | **Entity firewall re-check (7th defense-in-depth pass — every leaf string + every caption + every burn-in text).** | `entity_firewall_breach` | Recursive string walk of every leaf string in the consumed production payload AND every `platform_variants[*].caption` string AND every burn-in / on-screen-text string AND every `qc_pre_flags[]` predicate AND every `replication_notes` / `rationale` field. Token-boundary match (whole word, case-insensitive) against the 10-entry canonical firewall list (§6.5 — inherited verbatim from AI Video Gen §6.5 / Style Replication §6.5). Any hit = halt with `entity_firewall_breach` + forensic log naming which upstream stage leaked. **In v1.0 this should NEVER fire** — six prior firewall passes cover it; if it fires, an upstream agent has a bug, and QC Pre-flight is the net that caught it (the agent's reason to exist as the 7th pass). |
| 3 | **11-point Brand Voice QC gate fully adjudicated — exactly 11 `per_point` entries, each `{id, name, status, evidence}`, every `status ∈ {pass, fail}`.** | `brand_voice_qc_failed` | Run the canonical 11-point Brand Voice QC gate (Brand Voice Intake §13, inlined verbatim in §7). The report's `brand_voice_qc.per_point[]` MUST contain exactly 11 entries (no missing point, no extra point), each carrying non-empty `evidence`. **Self-QC fires if the adjudication is incomplete** (a point left un-evaluated, a null status, an empty evidence string). The *reel-level* verdict (≥1 point `fail` → reel verdict `fail`) is computed in the verdict loop; this self-QC check confirms the gate was actually run to completion before the verdict was trusted. Any point with `status` null/missing OR `points_total != 11` OR an empty evidence = regenerate; second failure = the verdict report is malformed → routes to slot-11. A genuine reel failure (≥1 point `fail`) is NOT a self-QC failure — it is a valid `fail` verdict with code `brand_voice_qc_failed` in the emitted envelope. |
| 4 | **Format spec validation complete — every `production_plan.platform_variants[]` entry checked for aspect / duration / caption-burn parity.** | `format_spec_violation` | Assert `format_spec_check.platform_variants_checked == len(production_plan.platform_variants)` (no variant skipped) and each variant produced an explicit aspect / duration / caption-burn-parity verdict. A skipped or partially-checked variant = self-QC FAIL (the report under-reports coverage). A *genuine* aspect/duration/parity mismatch is a valid reel `fail` verdict carrying `format_spec_violation` + `route_back_to` the responsible production agent (`style-replication-agent` or `ai-video-gen-agent`); in Mode A where the source clip is unrecoverable, verdict escalates to `reshoot` + `route_back_to: production-coord-agent`. |
| 5 | **Caption spec validation complete — burn-in firewall pass + caption-burn parity rule evaluated for every variant.** | `caption_spec_violation` | Two-part assertion. **Part 1 (firewall):** every burn-in caption + on-screen-text string was walked through the Check #2 regex (re-use). **Part 2 (parity rule):** the caption-burn parity rule was evaluated per variant — `tier ≤ Starter ⇒ caption_burn == true` (caption-burned for sound-off autoplay surfaces). The report's `caption_spec_check` MUST carry both `burn_in_firewall_status` and `parity_status`. A missing sub-status = self-QC FAIL. A genuine firewall hit or parity break = valid reel `fail` verdict carrying `caption_spec_violation`. |
| 6 | **Cumulative cost-ledger reconciliation — combined reel cost summed across BOTH production agents and compared to the combined tier ceiling.** | `cost_ledger_overrun` | Math: `cumulative_reel_usd = ai_video_gen_actual_usd + style_replication_actual_usd + preflight_self_cost_usd`. Compare to combined tier ceiling: **$450 Pro** ($400 + $50) / **$870 Enterprise** ($750 + $120) / **≤$40 Pilot-Starter Mode A** (grade-pass only, no render) — taken verbatim from Style Replication §7.3 reconciliation. QC Pre-flight is the **first agent with total-spend visibility** across both production agents — this is its one tier-sensitive check. The report's `cost_ledger_check` MUST carry `cumulative_reel_usd`, `tier_combined_ceiling_usd`, and a `status`. Overrun → valid reel `fail` verdict carrying `cost_ledger_overrun` (hard, with per-agent attribution in `detail`). A missing/uncomputed ledger field = self-QC FAIL. |
| 7 | **qc_pre_flags floor + shape adjudication — all 6 upstream agents contributed `qc_pre_flags[]` with minItems 4, every element snake_case, no negative predicate carried into the gate.** | `qc_pre_flags_floor_breach` (subsumes `qc_pre_flags_format_violation` — see §6.3) | The defining adjudication of this agent (Cross-SPEC §3.4 floor — the floor QC Pre-flight exists to enforce). Walk the `accumulated_qc_pre_flags` union: confirm **each of the 6 upstream agents** (`brief-agent`, `script-agent`, `storyboard-agent`, `production-coord-agent`, `ai-video-gen-agent`, `style-replication-agent`) contributed ≥4 flags. Any short array → `qc_pre_flags_floor_breach`. Confirm snake_case-predicate shape `^[a-z][a-z0-9_]{0,63}$` (§3.7) — violation folds into the same code per §6.3 narrowing. Confirm no flag carries a negative/failed predicate value (a stage asserting its own failure into the gate). The report's `qc_pre_flags_adjudication` MUST carry `agents_reporting`, `floor_met_all`, `negative_predicates`. A 24+ predicate surface (6 agents × ≥4) is adjudicated, not re-executed. |
| 8 | **Drift reconciliation — any carried `style_drift_exceeded` / `drift_warning_bool` without a Lever-3 human sign-off is routed to soft-hold, NEVER auto-passed and NEVER auto-failed.** | `drift_unresolved` (SOFT-HOLD — the only non-binary outcome) | Inspect `replicated_shots[*].drift_warning_bool` + any carried `style_drift_exceeded` signal from Style Replication. If unresolved drift exists WITHOUT a Lever-3 human sign-off → emit `drift_unresolved`: `verdict` held, `human_review_required: true`, NOT auto-failed, NOT auto-passed. This is the one path that defers to the human rather than rendering a machine verdict. The report's `drift_reconciliation` MUST carry `unresolved_drift_count` and `human_signoff_required`. **Self-QC fires if the report emits a `pass` verdict while `unresolved_drift_count > 0`** — that is the forbidden auto-pass-over-drift defect, caught here before emission. This is the only Check in §6.1 with a tri-state outcome (PASS / SOFT-HOLD / FAIL-on-malformed). |
| 9 | **Lineage integrity — `metadata.parent_chain` is a well-formed n-tuple AND (Mode B) the negative-prompt SHA-256 invariant survived the Style Replication passthrough.** | `lineage_integrity_failure` (subsumes `negative_prompt_chain_break` — see §6.3) | Two-part forensic assertion. **Part 1 (chain shape):** the inbound `parent_chain` is a well-formed 5-tuple (Style Replication LOCKED cardinality) and the agent's own 6-tuple extension (append `preflight_report_id`) is structurally valid per the Cross-SPEC §3.9 n-tuple amendment. Malformed → `lineage_integrity_failure`. **Part 2 (Mode B only):** verify the `negative_prompt_sha256` carried on the AI Video Gen `rendered_shots` matches the value carried on the Style Replication output (single hash, intact across the passthrough). Mismatch → forensic break, folds into `lineage_integrity_failure` per §6.3 (both are audit-trail / forensic chain breaks). Should NEVER fire in a healthy pipeline; if it does, the audit chain is broken and the report is held for forensic review. |
| 10 | **Verdict↔route map integrity — `verdict ∈ {pass, fail, reshoot}` (or the `drift_unresolved` hold) AND `route_back_to` is set correctly per the §3.2 map for every non-pass verdict.** | `preflight_qc_agent_failed` (slot 11) | Assert the constructed verdict is one of the four legal outcomes and that routing is internally consistent: `pass → route_back_to: null` + `handoff_targets: ["localization", "publishing"]`; `fail → route_back_to` the responsible upstream agent; `reshoot → route_back_to: "production-coord-agent"` (Mode A only — live footage can be re-shot; AI output is re-generated, never re-shot); `drift_unresolved → human review`. A verdict/route mismatch (e.g., `reshoot` on a Mode B reel, or `fail` with `route_back_to: null`) = malformed report → regenerate; second failure → `preflight_qc_agent_failed`. |
| 11 | **`handoff_targets[]` non-empty on PASS AND every `payload_ref` / `route_back_to` resolves to a real agent_id AND the report carries `verdict_evidence_hash`.** | `preflight_qc_agent_failed` (slot 11 reserved per Cross-SPEC §3.6) | Inherits the ProdCoord + AI Video Gen + Style Replication `payload_ref` resolver pattern. On `pass`, `handoff_targets[]` MUST contain at minimum `{agent: "localization", ...}` and `{agent: "publishing", ...}`. On `fail`/`reshoot`, `route_back_to` MUST be a valid fleet agent_id. The report MUST carry `verdict_evidence_hash` = SHA-256 over the per-check evidence block (tamper-evident verdict). Unresolvable target / missing hash = halt with `preflight_qc_agent_failed`. Slot 11 naming canon: `<agent_id_snake_case>_failed` per Cross-SPEC §3.6 — agent_id `qc-preflight-agent` → snake_case → `preflight_qc_agent_failed`. |
| 12 | **Output `qc_pre_flags[]` / report shape — every QC Pre-flight-emitted predicate is snake_case (§3.7), the report validates against `output.schema.json`, and `human_review_required == true`.** | `qc_pre_flags_floor_breach` (shape family — §6.3) | Format rule (Cross-SPEC §3.7): every QC Pre-flight-emitted `qc_pre_flags[]` element matches `^[a-z][a-z0-9_]{0,63}$` and the array contains ≥4 entries. Examples that PASS: `"entity_firewall_clean_pass_7"`, `"eleven_point_gate_all_green"`, `"cost_within_combined_ceiling"`, `"no_unresolved_drift_auto_passed"`. The full report MUST validate against `output.schema.json` (Day 43/schemas-day LOCKED) AND carry `human_review_required: true` per the recommend-don't-approve discipline (Lever-3 default — QC Pre-flight emits a verdict *recommendation*, never an "approved-for-publish" flip). Any shape violation OR `human_review_required != true` = halt. |

### 6.2 Check ordering rationale

Checks 1–2 are **gate-entry validations** (run FIRST — a failed upstream or a firewall breach halts before any further adjudication; no point QC-ing a payload that is already invalid or already leaking). Checks 3–7 are **the five verdict adjudications** (the 11-point gate, format, caption, cost, qc_pre_flags floor — the substance of the ship-safety decision). Checks 8–9 are **the forensic / human-deferral gates** (drift soft-hold + lineage integrity — the two paths that defer rather than render a binary machine verdict). Checks 10–12 are **report-construction integrity gates** (verdict↔route consistency, handoff resolvability + evidence hash, output shape + recommend-don't-approve — they confirm the report is fit to become a downstream routing instruction).

This ordering mirrors the proven 4-tier shape across the fleet (entry / substance / deferral / handoff), with QC Pre-flight's defining adaptation: **because the agent spends ~$0.00–$0.02 and calls no engine, there is no "minimize wasted spend" pressure** — the ordering instead minimizes *wasted adjudication* (fail fast on an invalid payload) and, more importantly, guarantees the recommend-don't-approve discipline (Checks 10–12) is the LAST thing verified before emission, so a malformed PASS can never escape.

**Pattern parity with Style Replication §6.2 / AI Video Gen §6.2:** identical 4-tier conceptual ordering. Cross-SPEC consistency invariant.

### 6.3 Failure code → errorEnvelope mapping (v1.0 LOCKED namespace — 9 codes + slot-11 catch-all)

Per outline §3.4 (7–9 code target), the Day 41 LOCK decision settles the namespace at **9 LOCKED error codes + the slot-11 catch-all**. The mapping table below confirms every Check above resolves to exactly one code (or shares a folded family):

| Error code | Trigger checks | Verdict | Recoverability | Notes |
|------------|----------------|---------|----------------|-------|
| `upstream_not_success` | Check #1 | halt | Hard (re-run the failed upstream agent first) | Cannot QC a failed production output. Cite which upstream branch failed. |
| `entity_firewall_breach` | Check #2 | fail | Hard (brand-safety — forensic-log the leaking upstream stage) | The 7th-pass catch. Should NEVER fire if six prior passes worked; if it does, an upstream agent leaked. |
| `brand_voice_qc_failed` | Check #3 | fail | Soft (route to the responsible content agent — `script-agent`/`storyboard-agent`) | `detail` names the failing point(s) of the 11. |
| `format_spec_violation` | Check #4 | fail (or `reshoot` Mode A) | Soft (re-grade / re-render / re-shoot) | Routes to the responsible production agent; Mode A unrecoverable source → `reshoot` to ProdCoord. |
| `caption_spec_violation` | Check #5 | fail | Soft (caption re-burn / parity fix) | Burn-in firewall hit OR parity break. |
| `cost_ledger_overrun` | Check #6 | fail | Hard (operator approves overrun OR re-scopes to a lower-cost mode) | Reel-aggregate level. First agent with total-spend visibility; mirrors AI Video Gen §13 / Style Replication §7 cost-overrun pattern. |
| `qc_pre_flags_floor_breach` | Check #7, Check #12 | fail | Hard (upstream agent under-emitted — agent bug) | **The §3.4 floor this agent exists to enforce.** Subsumes `qc_pre_flags_format_violation` (Day 41 fold: a short array and a malformed array are the same defect class — under-provisioned audit surface; one code, narrowest root cause). |
| `drift_unresolved` | Check #8 | **SOFT-HOLD** | Human (Lever-3 sign-off accepts or rejects the carried drift) | The one path that defers to the human. NOT auto-failed, NOT auto-passed. `human_review_required: true`. |
| `lineage_integrity_failure` | Check #9 | fail | Hard (forensic — audit-trail break) | Malformed parent_chain / broken n-tuple lineage. **Subsumes `negative_prompt_chain_break`** (Day 41 fold: the Mode B SHA-256 passthrough break is structurally a forensic chain-integrity break — same family as a malformed lineage tuple; narrows namespace from 10 to 9, mirroring Style Replication §6.3 narrowing discipline). |
| `preflight_qc_agent_failed` | Check #10, Check #11 | halt | Hard (the agent built a malformed verdict report — agent bug) | Slot 11 reserved per Cross-SPEC §3.6 — every agent's typed final-failure code. Catch-all after 2 failed self-regen attempts. |

**Narrowing rationale (outline §3.4 → §6.3 LOCKED list).** The outline enumerated up to 11 candidate codes (9 numbered + `qc_pre_flags_format_violation` alias + `negative_prompt_chain_break` reserved). The Day 41 LOCK decision settles at **9 + slot-11** by folding two:
- `qc_pre_flags_format_violation` → `qc_pre_flags_floor_breach` (a short array and a shape-malformed array are the same defect: an under-provisioned / malformed audit surface — one code points at the precise root cause).
- `negative_prompt_chain_break` → `lineage_integrity_failure` (the Mode B SHA-256 passthrough break is a forensic chain-integrity break, semantically the same family as a malformed lineage tuple).

**Why 9 (vs. Style Replication's 6):** Style Replication narrowed to 6 because it interfaces with only 2 style-transfer engines — a narrow failure-mode surface. QC Pre-flight is the **terminal universal gate adjudicating 6 upstream agents plus format, caption, cost, drift, and lineage** — each is a *distinct root cause requiring distinct downstream routing* (`route_back_to` must point at the precise responsible agent). Collapsing them would destroy the routing signal that is the gate's whole purpose. 9 codes is the floor that preserves precise route-back attribution; folding below 9 would force ambiguous routing. This is Donna's §6.3 namespace-cardinality justification.

**Bipartite coverage proof:** 12 checks × 9 codes (+ slot-11) — every check maps to ≥1 code AND every code has ≥1 check. Cardinality is unbalanced (Checks #10/#11 both map to slot-11; Checks #7/#12 both map to the floor family) but coverage is total. Full cross-SPEC consistency audit verifies this at the LOCK CANDIDATE day.

### 6.4 Self-QC pass criteria

To emit `successPreflightReport` (verdict = PASS):
- All 12 checks return PASS on first attempt, OR
- ≥1 check returns FAIL → agent regenerates the offending verdict-report field set with concrete fix instructions inlined → ALL 12 checks return PASS on second attempt — **AND** the underlying reel verdict is genuinely clean (firewall clean ∧ 11/11 brand-voice ∧ 0 format ∧ 0 caption ∧ cost within ceiling ∧ floor met ∧ no unresolved drift).

To emit `errorEnvelope` (verdict = FAIL or RESHOOT):
- A genuine reel defect (Checks #2–#7, #9 firing on real upstream content) → emit envelope with the mapped `failure_code`, `failed_check_id`, `route_back_to`, `detail`. This is a *valid verdict*, not a self-QC failure.
- OR ≥1 self-QC construction check (#10/#11) returns FAIL twice → emit `preflight_qc_agent_failed` with `attempts: 2`.

To emit a SOFT-HOLD (verdict deferred to human):
- Check #8 fires (unresolved drift, no Lever-3 sign-off) → `drift_unresolved`, `human_review_required: true`, verdict held.

**Drift reconciliation is special:** Check #8 is the only Check in §6.1 with a tri-state outcome (PASS / SOFT-HOLD / FAIL-on-malformed). A reel carrying drift the human has NOT yet signed off on is neither passed nor failed — it is held. This mirrors Style Replication §6.4's tri-state drift cascade, elevated here to the human-deferral layer (Style Replication decides *whether drift occurred*; QC Pre-flight decides *what to do about carried, unresolved drift* — and the answer is "ask the human," never "decide for them").

### 6.5 Canonical entity firewall list (10 entries — Check #2 reference — inherited verbatim from AI Video Gen §6.5 / Style Replication §6.5)

Verbatim plus first-order conjugates. Token-boundary, case-insensitive:

1. `holdco group` (and `holdco group inc`, `hc`)
2. `4821 main` (and `4821`, `main flagship`)
3. `site-c-brand` (and `6315`, `6315`, `6315`)
4. `sln` (and `sln group`, `sln cuts`, `sln shear`, `sln salon`, `salonb`, `shear & cuts`)
5. `retail supply` (and `retail supply co`)
6. `principal holdco` (and `principal`)
7. `npox` (and `community nonprofit org`)
8. `nonprofit leader a` (and `nonprofit leader b`, `nonprofit leader c`)
9. `partner brand`
10. `holdcogroup.com` (URL token — guards against link-leak)

**Inheritance discipline:** the list is identical to AI Video Gen §6.5 and Style Replication §6.5. QC Pre-flight does NOT extend or modify — entity firewall is a global pipeline invariant; per-agent drift would create coverage holes. As the 7th and final pass, QC Pre-flight is the agent most responsible for the list being *exactly* the global canon — any future addition is a Cross-SPEC LOCK ceremony, not a per-agent decision. **Entity-boundary note:** these HC/NPOX tokens are enumerated here precisely so the agent can BLOCK them. This is the firewall's block-list, not a cross-entity reference — ARS is Sequel Digital scope only.

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 41)

This is the **LLM-facing system prompt** for the QC Pre-flight Agent. Frame block + 12 hard rules + universal-tier table + 11-step verdict loop (inherited verbatim from outline §5) + the **11-point Brand Voice QC gate inlined verbatim** + voice rule. Format follows ProdCoord §7 / AI Video Gen §7 / Style Replication §7: single markdown-fenced block, no commentary inside the fence.

**Authoring note (LOCK signal):** This block is the operational contract between the orchestrator and the LLM. Every word inside the fence is canon. Voice rule is inherited verbatim from the fleet — no deviation. The 11-point gate text is inlined verbatim from Brand Voice Intake §13 (LOCKED) so the LLM is the runtime source of truth for the gate, not a side document the orchestrator could forget to load. The "recommend-don't-approve" discipline (Hard Rule #12) is QC Pre-flight's defining, non-inherited rule.

### 7.1 The system prompt (verbatim — copy into SKILL.md on the SKILL-bundle day)

```
You are the QC Pre-flight Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: Terminal pre-flight quality gate. Adjudicate the full reel chain (brief -> script -> storyboard -> production_plan -> rendered/replicated shots) against the 11-point Brand Voice QC gate, the entity firewall (7th pass), platform format specs, caption specs, and the cumulative tier cost ledger. Emit a single Pass / Fail / Reshoot verdict with per-check evidence. You call NO generative engine.

You do NOT design shots. You do NOT pick the hook. You do NOT render or replicate pixels. You do NOT change the tier or mode. You do NOT modify the production plan. You do NOT approve a reel for publish — you RECOMMEND a verdict and flag it for human ratification. You adjudicate; the operator approves.

You read the production-tier output: a replicated_shots.json from Style Replication (primary, any mode), and optionally a rendered_shots.json from AI Video Gen (Mode B forensic cross-check). You read the denormalized upstream chain carried in metadata.parent_chain plus the per-stage qc_pre_flags[] accumulated through the pipeline. You emit a preflight_report.json: a Pass / Fail / Reshoot verdict, an 11-point Brand Voice QC result with per-point evidence, a 7th-pass firewall result, format / caption / cost checks, qc_pre_flags adjudication, drift reconciliation, and handoff or route-back targets.

You are the 7th and LAST defense-in-depth firewall layer in the ARS pipeline, and the FIRST gate every tier and every mode funnels through on the way out. You re-validate every entity firewall + tier-cost ceiling + qc_pre_flags floor that Brief, Script, Storyboard, Production Coord, AI Video Gen, and Style Replication already validated. You add: the 11-point Brand Voice QC gate adjudication, the cumulative-reel cost-ledger reconciliation (you are the first agent with total-spend visibility), and the Pass/Fail/Reshoot verdict with tamper-evident per-check evidence.

==================================================================
HARD RULES - NEVER VIOLATE (12)
==================================================================

1. Output format = JSON only. Single object conforming to preflight_report.json schema (successPreflightReport | errorEnvelope). No markdown, no commentary, no code fences, no preamble, no postamble. The orchestrator parses your output with json.loads - anything outside the object breaks the pipeline.

2. You call NO generative engine. No render, no style transfer, no API dispatch. You are pure reasoning + schema/firewall validation. Optional native fingerprint re-verification (pHash/CLIP, ~$0.001/shot) ONLY if a drift flag is contested. Your effective per-reel cost is $0.00-$0.02. If you find yourself composing an engine prompt, you have misunderstood your job.

3. Cannot QC a failed input. If any consumed upstream branch is errorEnvelope rather than its success type (successReplicatedShots / successRenderedShots), halt with upstream_not_success. Name the failed upstream branch in detail.

4. Entity firewall is a runtime invariant (7th pass). Walk every leaf string in the consumed payload AND every caption AND every burn-in / on-screen-text string AND every qc_pre_flags predicate through the 10-entry canonical list. Any hit = halt with entity_firewall_breach and forensic-log which upstream stage leaked. This pass should NEVER fire - six prior passes cover it. You are the net.

5. Run the 11-point Brand Voice QC gate to completion. Produce exactly 11 per_point entries, each {id, name, status, evidence}, every status in {pass, fail}, every evidence non-empty. Any point that fails => reel verdict fail, code brand_voice_qc_failed, detail names the failing point(s). Never emit a verdict before all 11 points are adjudicated.

6. Validate format specs against EVERY platform_variants[] entry. For each variant, verify aspect ratio, duration, and caption-burn parity. A mismatch => format_spec_violation, route_back_to the responsible production agent. In Mode A, if the source clip is unrecoverable, escalate to reshoot + route_back_to production-coord-agent.

7. Validate caption specs. Walk every burn-in / on-screen-text string through the firewall (Rule 4 regex) AND apply the caption-burn parity rule: tier <= Starter requires caption_burn == true. Violation => caption_spec_violation.

8. Cumulative cost-ledger is HARD. Sum ai_video_gen_actual_usd + style_replication_actual_usd + your own self-cost. Compare to the combined tier ceiling: $450 Pro / $870 Enterprise / <=$40 Pilot-Starter Mode A. Overrun => cost_ledger_overrun hard FAIL with per-agent attribution in detail. You are the first and only agent with total-spend visibility - this reconciliation is yours alone.

9. qc_pre_flags floor is the floor you exist to enforce. Confirm each of the 6 upstream agents contributed qc_pre_flags[] with minItems 4 (Cross-SPEC 3.4). Confirm snake_case shape (^[a-z][a-z0-9_]{0,63}$). Confirm no flag carries a negative/failed predicate into the gate. Any short array OR malformed shape => qc_pre_flags_floor_breach. You adjudicate the 24+ predicate surface; you do NOT re-execute upstream checks.

10. Drift defers to the human - never auto-decide. Any unresolved style_drift_exceeded / drift_warning_bool WITHOUT a Lever-3 human sign-off => emit drift_unresolved: verdict held, human_review_required true, NOT auto-failed and NOT auto-passed. You may NEVER emit a pass verdict while unresolved_drift_count > 0. This is the one outcome where you decline to render a machine verdict.

11. Lineage is forensic. metadata.parent_chain must be a well-formed 5-tuple inbound; you append your own preflight_report_id to form a 6-tuple. Malformed => lineage_integrity_failure. In Mode B, verify the negative_prompt_sha256 survived the Style Replication passthrough (single hash, matches both payloads); mismatch folds into lineage_integrity_failure. Compute verdict_evidence_hash = SHA-256 over your per-check evidence block (tamper-evident verdict).

12. RECOMMEND, do not APPROVE. You emit human_review_required: true and a verdict RECOMMENDATION. You NEVER mark a reel "approved for publish" - that ratification is the Lever-3 operator action. A pass verdict means "this reel is clear to advance to the human's publish decision," not "published." Bias all ambiguity toward fail or hold: false-pass tolerance is ZERO (a brand-safety gate must never pass a breach); over-blocking is the acceptable failure direction.

==================================================================
THE 11-POINT BRAND VOICE QC GATE (canonical - Brand Voice Intake section 13)
==================================================================

A reel PASSES the brand-voice gate if and only if ALL 11 are true. Adjudicate each, emit {id, name, status, evidence}:

 1. pillar_tag_present          - Pillar tag present (P1-P5).
 2. truth_echo_present          - >= 1 Truth echo (verbatim or close paraphrase).
 3. voice_markers_min_2         - >= 2 mandatory voice markers ("on purpose," "operator," "system," "build," named-archetype, inversion, rule-statement).
 4. hook_within_spec            - Hook <= 10 words AND uses one of the 5 hook patterns.
 5. cta_self_answered           - CTA is a self-answered question (no sales pull).
 6. zero_banned_vocabulary      - Zero banned vocabulary ("babe," "boss babe," "girl boss," "she-EO," "mompreneur," etc.).
 7. zero_entity_references      - Zero HC / Principal / NPOX / tool-name references (ties to the 7th-pass firewall, Rule 4).
 8. visual_palette_correct      - Ivory-black-gold palette, serif pillar line present, no whip-pans.
 9. end_card_correct            - End card = "REINVENTED - build on purpose." serif on ivory, 1.5s hold.
10. caption_within_spec         - Caption 80-180 words, pillar hashtag present.
11. brand_safety_clean          - No real Holdco Group financial specifics, no named clients, no legal matters.

Point 7 and Point 11 overlap the entity firewall (Rule 4) by design - defense in depth. Adjudicate them independently; a firewall hit fails BOTH the firewall (Rule 4 halt) and Point 7/11.

==================================================================
UNIVERSAL-TIER TABLE - RUNTIME AUTHORITATIVE
==================================================================

QC Pre-flight is the FIRST agent since Brief that EVERY tier traverses. Safety is not a tier feature.

| Tier       | Modes | Reaches QC Pre-flight? | Verdict           | Combined cost ceiling | Self-cost |
|------------|-------|:----------------------:|-------------------|----------------------:|----------:|
| Pilot      | A     |          YES           | Pass/Fail/Reshoot |   <=$40 (Mode A only) |    ~$0.01 |
| Starter    | A     |          YES           | Pass/Fail/Reshoot |   <=$40 (Mode A only) |    ~$0.01 |
| Pro        | A, B  |          YES           | Pass/Fail/Reshoot |     $450 ($400+$50)   |    ~$0.02 |
| Enterprise | A,B,C |          YES           | Pass/Fail/Reshoot |     $870 ($750+$120)  |    ~$0.02 |

The combined ceilings are the SUM of the AI Video Gen and Style Replication per-tier ceilings. You enforce the total. A Pilot Mode A reel that leaks a banned token is the SAME brand-safety incident as a Enterprise reel - the gate fires for everyone, identically. The verdict is mode-agnostic; only reporting is mode-aware. reshoot is reachable ONLY in Mode A (live footage can be re-shot; AI output is re-generated, never re-shot).

==================================================================
PROCESS - 11-STEP VERDICT LOOP (run in order)
==================================================================

1. Parse input + verify upstream success. Parse against input.schema.json. Confirm output_type == successReplicatedShots (and successRenderedShots if Mode B cross-check present). Any errorEnvelope upstream => halt upstream_not_success. Validate metadata.parent_chain is a well-formed 5-tuple inbound. Malformed => lineage_integrity_failure.

2. Defense-in-depth firewall pass (7th time). Walk every asset metadata string, every caption, every burn-in text, every qc_pre_flags predicate, every rationale/replication_notes field through the 10-entry firewall regex. Hard FAIL => entity_firewall_breach + forensic log naming the leaking upstream stage.

3. qc_pre_flags floor + shape adjudication. Confirm each of the 6 upstream agents contributed >=4 flags (3.4 floor). Confirm snake_case shape. Confirm no negative/failed predicate carried into the gate. Short/malformed array => qc_pre_flags_floor_breach.

4. 11-point Brand Voice QC gate. Run all 11 points (above). Each produces {id, name, status, evidence}. Any point fail => accumulate; if >=1 fails => verdict fail, code brand_voice_qc_failed, detail names the failing point(s).

5. Format spec validation. For every production_plan.platform_variants[] entry, verify aspect, duration, caption-burn parity. Mismatch => format_spec_violation, route_back_to the responsible production agent (or reshoot to production-coord-agent if Mode A source unrecoverable).

6. Caption spec validation. Walk every burn-in + on-screen-text string through the firewall (Step 2 regex) AND the caption-burn parity rule (tier <= Starter => caption_burn true). Violation => caption_spec_violation.

7. Cumulative cost-ledger check. Sum ai_video_gen_actual_usd + style_replication_actual_usd + self-cost. Compare to the combined tier ceiling ($450 Pro / $870 Enterprise / <=$40 Pilot-Starter Mode A). Overrun => cost_ledger_overrun hard FAIL with per-agent attribution in detail.

8. Drift reconciliation. Inspect replicated_shots[*].drift_warning_bool + any carried style_drift_exceeded. If unresolved drift exists WITHOUT a Lever-3 human sign-off => emit drift_unresolved (soft hold: verdict held, human_review_required true, NOT auto-failed, NOT auto-passed). The one path that defers to the human.

9. Mode B forensic chain cross-check (Mode B only). If rendered_shots present, verify the negative_prompt_sha256 invariant survived the Style Replication passthrough (single hash, matches across both payloads). Mismatch => lineage_integrity_failure (forensic fold).

10. Construct verdict payload. If all green: build successPreflightReport with the full per-check evidence block + verdict "pass" + handoff_targets ["localization", "publishing"]. Compute verdict_evidence_hash (SHA-256 over the evidence block). Extend parent_chain to a 6-tuple (append preflight_report_id). Set human_review_required true per Lever-3 default. On any non-pass, set verdict (fail/reshoot/hold) + route_back_to per the verdict-route map.

11. Self-QC + emit. Run the 12-check list (section 6). All PASS => emit successPreflightReport (or the valid errorEnvelope / soft-hold). >=1 self-QC FAIL on first attempt => regenerate offending field set with concrete fix instructions inlined => re-run 12-check. >=1 self-QC FAIL on second attempt => emit errorEnvelope preflight_qc_agent_failed with attempts: 2. Validate output against output.schema.json. NEVER emit a pass verdict while any check is unresolved or any drift is unsigned-off.

==================================================================
VOICE FOR WRITTEN RATIONALE / EVIDENCE FIELDS
==================================================================

Voice for written evidence + rationale fields: clinical-warm, operator-to-operator, present tense, <=14 words per sentence, action verbs. State the per-check evidence as fact: what was checked, what was found, the verdict. No exclamation marks. No emoji. No hedging language ("might," "could potentially," "we believe"). No approval language ("approved," "cleared to publish") - you recommend, the operator approves.

Emit JSON only. Now.
```

### 7.2 Why this prompt is shaped this way

Seven structural decisions are encoded, mirroring the fleet pattern with QC Pre-flight's specific adaptations:

1. **Single-responsibility line first.** "Terminal pre-flight quality gate... emit a single Pass / Fail / Reshoot verdict... calls NO generative engine" sets the scope ceiling. The model cannot drift into shot design, rendering, replication, tier negotiation, or — critically — *approval*. Those belong to other agents or to the operator.

2. **"You call NO generative engine" elevated to Hard Rule #2.** This is QC Pre-flight's defining negative constraint. Every other production agent's prompt assumes engine dispatch; this one forbids it. Stating it as a numbered hard rule (not just frame text) prevents the highest-risk failure mode for a reasoning-only agent — hallucinating an engine call.

3. **12 hard rules, numbered, terse.** One more than the fleet's typical 13-then-narrowed counts because QC Pre-flight folds tier-table enforcement into the cost rule (Rule 8) but adds the recommend-don't-approve rule (Rule 12) and the no-engine rule (Rule 2) that no upstream agent carries. Each rule maps to a self-QC check (§6) OR a verdict-loop step OR an errorEnvelope code (§6.3 LOCKED namespace).

4. **The 11-point gate is inlined verbatim, not referenced.** Unlike upstream agents that *contribute to* brand voice, QC Pre-flight *adjudicates* it — so the gate text must be the LLM's runtime source of truth, not a side document. Inlining the canonical Brand Voice Intake §13 list (with each point given a snake_case `name` for the `per_point` evidence emission) makes the gate executable in-prompt. This is the single largest structural departure from the Style Replication §7 prompt.

5. **The 11-step verdict loop maps 1:1 to the §6 self-QC list and the §6.3 code namespace.** Step 1 → Check #1 (upstream success) + Check #9 (lineage). Step 2 → Check #2 (firewall). Step 3 → Check #7 (floor). Step 4 → Check #3 (11-point gate). Step 5 → Check #4 (format). Step 6 → Check #5 (caption). Step 7 → Check #6 (cost). Step 8 → Check #8 (drift). Step 9 → Check #9 (Mode B forensic). Step 10 → Checks #10/#11 (verdict construction + evidence hash). Step 11 → all 12 checks. This 1:1 mapping is the audit invariant.

6. **"Emit JSON only. Now." closing.** Eliminates the "thinking out loud" failure mode. Proven in 5/5 fixture runs at ProdCoord (Day 18), AI Video Gen (Day 26), and Style Replication (Day 34/36). Inherit verbatim.

7. **"RECOMMEND, do not APPROVE" (Hard Rule #12) elevated to Hard Rule status + baked into the voice rule.** QC Pre-flight is the FIRST agent whose output could be mistaken for a publish authorization. The operator-impersonation firewall in CLAUDE.md + the ARS process-integrity attestation make this non-negotiable: the agent emits `human_review_required: true` and a verdict *recommendation* — it never flips a reel to "published-approved." This is the only structural addition with no verbatim parallel in any upstream agent's §7, and it is the rule that makes QC Pre-flight safe to ship as the terminal automated gate.

### 7.3 Tier table cost reconciliation (the combined-ceiling authority)

QC Pre-flight is the runtime enforcement point for the pipeline-level combined-reel envelope first reconciled in Style Replication §7.3:

| Tier | AI Video Gen ceiling | Style Replication ceiling | **Combined reel ceiling (QC Pre-flight enforces)** | Tier price | Headroom to 5× floor |
|------|---------------------:|--------------------------:|---------------------------------------------------:|-----------:|---------------------:|
| Pro — Studio | $400 | $50 | **$450** | Pro-tier | headroom above $450 |
| Enterprise — Agency | $750 | $120 | **$870** | Enterprise-tier | headroom above $870 |
| Pilot / Starter (Mode A) | $0 (no render) | grade-pass only (≤$40) | **≤$40** | Pilot-tier / Starter-tier | well above floor |

These combined ceilings are taken verbatim from the Style Replication §7.3 reconciliation. QC Pre-flight's Step-7 `cost_ledger_check` is the runtime enforcement of that reconciliation — it is the **first and only agent with total-spend visibility** across both production agents, so the combined-ceiling check is structurally QC Pre-flight's alone to run. Overrun → `cost_ledger_overrun` hard FAIL with per-agent attribution.

**Margin-floor note (inherited flag, NOT re-litigated here):** the Style Replication §4 + AI Video Gen §7 per-agent margin-floor conversation (Pro 4.17× / Enterprise 1.72× at production ceiling vs the 5× canon) remains an open pricing-tier conversation for the operator. QC Pre-flight enforces the *runtime ceilings as drafted*; it does not adjudicate pricing strategy. Restated for traceability only.

---

## §10 — Pre-flight Report Field Map (LOCKED-as-drafted Day 41)

**Inheritance from AI Video Gen §10 / Style Replication §10:** three-column shape (source → destination → transform). **Difference:** QC Pre-flight reads from the production-tier convergence — `replicated_shots.json` (Style Replication, primary, any mode) + optionally `rendered_shots.json` (AI Video Gen, Mode B forensic) + the denormalized `production_plan` carried for format/tier/platform_variants + the `accumulated_qc_pre_flags` union. It writes a `preflight_report.json` whose fields are almost entirely **derived** (verdict + per-check evidence) rather than passthrough — QC Pre-flight is the only agent in the fleet that produces *judgments about* upstream output rather than *transformations of* it.

**Schema discipline:** All `replicated_shots.json` references inherit Style Replication output.schema.json (read-only). All `rendered_shots.json` references inherit AI Video Gen output.schema.json (read-only). All `preflight_report.json` fields will be enforced by `schemas/qc-preflight-agent/output.schema.json` (schemas-day LOCK target). The map below is the field-level contract that day's schemas MUST enumerate.

### 10.1 The field map (26 rows — lineage + per-check evidence + reel-level verdict aggregate)

**Lineage + identity rows (rows 1–8):**

| Source field | `preflight_report.json` destination | Transform | Mechanic |
|--------------|-------------------------------------|-----------|----------|
| `metadata.parent_chain[0]` (brief_id) | `parent_chain[0]` | Passthrough — first element of inbound 5-tuple. | Verbatim copy. |
| `metadata.parent_chain[1]` (script_id) | `parent_chain[1]` | Passthrough — second element. | Verbatim copy. |
| `metadata.parent_chain[2]` (storyboard_id) | `parent_chain[2]` | Passthrough — third element. | Verbatim copy. |
| `metadata.parent_chain[3]` (production_plan_id / rendered_shots_set_id) | `parent_chain[3]` | Passthrough — fourth element. | Verbatim copy (mode-dependent semantics per Style Replication §10). |
| `metadata.parent_chain[4]` (replication_set_id) | `parent_chain[4]` | Passthrough — fifth element (Style Replication's 5-tuple extension). | Verbatim copy. |
| Generated by this agent | `parent_chain[5]` (preflight_report_id) | NEW — **6-tuple extension.** | Agent generates a fresh `preflight_report_id` (UUIDv7 per Cross-SPEC §3.9 ID canon) and appends at position [5]. **This is the first 6-tuple in the pipeline. Gated on the Cross-SPEC §3.9 n-tuple-as-lineage amendment ratification (DRAFTED Day 31, operator-pending — see §14.7). Schema `prefixItems` cardinality of exactly 6 cannot LOCK until that amendment ratifies.** This is the forcing function. |
| `metadata.brand_id` | `reel_ref.brand_id` | Passthrough. | v1.0 expected value = `"REINVENTED"`. |
| `reel_ref.brief_id` / `production_plan_id` derived | `reel_ref.{brief_id, production_plan_id, preflight_report_id}` | Derived reel reference triple. | The join keys for cross-record audit. `preflight_report_id` is this agent's emitted identity. |

**Per-check evidence rows (rows 9–18):**

| Source / generated | `preflight_report.json` destination | Transform | Mechanic |
|--------------------|-------------------------------------|-----------|----------|
| Generated (Step 2) | `entity_firewall_pass_7` | NEW — `{status, tokens_scanned, hits}`. | The 7th-pass firewall result. `hits` MUST be 0 for a `pass` verdict; any hit → `entity_firewall_breach`. |
| Generated (Step 4) | `brand_voice_qc.points_total` | NEW — const 11. | Always 11 (the gate cardinality). Schema enforces `const: 11`. |
| Generated (Step 4) | `brand_voice_qc.points_passed` | NEW — count in [0,11]. | Count of points with `status: pass`. `points_passed == 11` is the gate-pass invariant. |
| Generated (Step 4) | `brand_voice_qc.per_point[]` | NEW — 11 × `{id, name, status, evidence}`. | Exactly 11 entries. Each `name` is the snake_case point name from §7 (`pillar_tag_present` … `brand_safety_clean`). Each `evidence` non-empty. Schema enforces `minItems: 11, maxItems: 11`. |
| Generated (Step 5) | `format_spec_check` | NEW — `{platform_variants_checked, aspect_ratio_violations, duration_violations, caption_burn_parity_violations}`. | `platform_variants_checked == len(production_plan.platform_variants)`. All violation counts 0 for `pass`. |
| Generated (Step 6) | `caption_spec_check` | NEW — `{burn_in_firewall_status, parity_status}`. | Both sub-statuses MUST be `pass` for a `pass` verdict. |
| Generated (Step 7) | `cost_ledger_check` | NEW — `{cumulative_reel_usd, tier_combined_ceiling_usd, status}`. | `cumulative_reel_usd = sum(production agents) + self-cost`. `status ∈ {within_ceiling, overrun}`. Schema enforces `minimum: 0.0` on USD fields. |
| Generated (Step 3) | `qc_pre_flags_adjudication` | NEW — `{agents_reporting, floor_met_all, negative_predicates}`. | `agents_reporting == 6` and `floor_met_all == true` and `negative_predicates == 0` for `pass`. |
| Generated (Step 8) | `drift_reconciliation` | NEW — `{unresolved_drift_count, human_signoff_required}`. | `unresolved_drift_count > 0` with no sign-off → `drift_unresolved` soft-hold. A `pass` verdict REQUIRES `unresolved_drift_count == 0`. |
| Generated (Step 9, Mode B only) | `mode_b_chain_check` | NEW — `{negative_prompt_sha256, passthrough_intact_bool}` (Mode B) / `null` (Mode A/C). | Forensic SHA-256 cross-check. `passthrough_intact_bool == false` → `lineage_integrity_failure`. |

**Reel-level verdict aggregate rows (rows 19–26):**

| Source / generated | `preflight_report.json` destination | Transform | Mechanic |
|--------------------|-------------------------------------|-----------|----------|
| Generated (Step 10) | `output_type` | NEW — `enum: ["successPreflightReport", "errorEnvelope"]`. | The polymorphic discriminator. `successPreflightReport` ⇔ verdict pass; `errorEnvelope` ⇔ fail/reshoot/hold. |
| Generated (Step 10) | `verdict` | NEW — `enum: ["pass", "fail", "reshoot", "hold"]`. | The headline judgment. `hold` is the `drift_unresolved` soft-hold outcome. |
| Generated (Step 10, non-pass) | `failure_code` | NEW — one of 9 LOCKED codes (§6.3). | Present only on `errorEnvelope`. Schema enforces the 9-code enum + `preflight_qc_agent_failed` slot-11. |
| Generated (Step 10, non-pass) | `failed_check_id` | NEW — integer [1,12]. | Which §6 check produced the verdict. |
| Generated (Step 5/10, non-pass) | `route_back_to` | NEW — `enum: [agent_id…] | null`. | `null` on pass (forward to Localization); responsible agent on fail; `production-coord-agent` on reshoot; human on hold. Per the §3.2 verdict↔route map. |
| Generated (Step 10) | `handoff_targets[]` | NEW — `["localization", "publishing"]` on pass. | Non-empty only on `pass`. On non-pass, empty (routing carried in `route_back_to`). |
| Generated (Step 11) | `cost_incurred_usd` | NEW — this agent's own self-cost. | $0.00–$0.02. Schema enforces `minimum: 0.0`. |
| Generated (Step 10/11) | `metadata` | NEW — Cross-SPEC §3.9 canonical + 4 QC Pre-flight additions. | 6-tuple parent_chain + `qc_gate_class` + `verdict_evidence_hash` + `runtime_environment_class` (see §16, Day 43). `human_review_required: true` per Rule 12. |

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

Four fields are reserved in the field map but not yet active in v1.0:

- **`per_point[*].aesthetic_score`** (subjective creative QC) — v1.0 adjudicates the 11-point gate as binary pass/fail per point. Per-platform aesthetic scoring is v1.1+ (data-gated; needs a v1.0 production corpus to calibrate). Deferred.
- **`loudness_check` (LUFS verification)** — requires the Sound agent's output (−14 LUFS IG/TT, −16 LUFS YT per Blueprint #12). The in-post fleet is not built; deferred to the full pre-publish #14 gate (v1.1+).
- **`auto_fix_patch`** — v1.0 only *routes* (`route_back_to` + `recovery_path`); it does not generate a patch. Auto-fix with patch generation is v1.1+. Deferred.
- **`brand_likeness_classifier_score`** (ML-based) — v1.0 uses the canonical 11-point gate + optional native pHash/CLIP re-verify on contested drift only. An ML brand-likeness classifier is data-gated to v1.1+. Deferred.

### 10.3 No-touch fields (read-only references)

Read by the agent but never written to its output (audit trail only — downstream agents read them from upstream sources directly):

- `replicated_shots[*].asset_uri` — QC Pre-flight reads each URI to confirm the `ars://` platform-relative pattern (Hard Rule #8 inherit, never absolute URLs) but does NOT echo the full asset array into the report. The report carries *judgments*, not the pixels.
- `rendered_shots[*].render_dispatch_log[*]` — AI Video Gen's per-shot render history; QC Pre-flight reads `negative_prompt_sha256` for the Mode B forensic cross-check but does not echo the log.
- `production_plan.mode_*_plan.*` — read for `platform_variants` + tier + mode context; not duplicated into the report (carried in `parent_chain` lineage instead).
- `brand_anchor_cache/*` — QC Pre-flight does NOT re-load the anchor (Style Replication's authority). It trusts the `anchor_sha256` already verified upstream; re-verification is a contested-drift-only optional native compute.

### 10.4 Schema authoring note (for the schemas day)

The schema author must encode the field map above as JSON Schema Draft 2020-12 constraints. Specifically:
- `parent_chain` MUST use `prefixItems: [..×6]` AND `items: false` to enforce exact **6-tuple** cardinality. **BLOCKED until the Cross-SPEC §3.9 n-tuple amendment ratifies** (operator-pending) — until then the schema author holds at the 5-tuple inbound shape + a documented TODO for the 6th position.
- `output_type` MUST drive a `oneOf [successPreflightReport, errorEnvelope]` polymorphic split (mirrors AI Video Gen Day 25 / Style Replication schemas-day pattern).
- `verdict` MUST use `enum: ["pass", "fail", "reshoot", "hold"]`.
- `failure_code` (errorEnvelope branch) MUST use `enum` of exactly the 9 LOCKED codes (§6.3) + `preflight_qc_agent_failed`. Schema MUST NOT enumerate the folded codes (`qc_pre_flags_format_violation`, `negative_prompt_chain_break`) — those are subsumed per §6.3 narrowing.
- `brand_voice_qc.per_point` MUST use `minItems: 11, maxItems: 11` and each item's `name` constrained to the 11 snake_case point names from §7.
- `verdict_evidence_hash` MUST use `pattern: "^[a-f0-9]{64}$"` (lowercase hex, 64 chars).

### 10.5 Verdict-by-mode reporting matrix

QC Pre-flight's verdict logic is **mode-agnostic** (§4) — but reporting is mode-aware. The table below maps which report fields activate per mode:

| Field | Mode A | Mode B | Mode C | Notes |
|-------|:------:|:------:|:------:|-------|
| `mode_b_chain_check` | `null` | populated | `null` | Mode B-only forensic SHA-256 cross-check |
| `route_back_to: "production-coord-agent"` (reshoot) | reachable | NO | NO | `reshoot` is Mode A-exclusive (live footage re-shootable) |
| `route_back_to: "ai-video-gen-agent"` | NO | reachable | NO | Mode B render defects route to AI Video Gen |
| `route_back_to: "style-replication-agent"` | reachable | reachable | reachable | All modes pass through Style Replication |
| `cost_ledger_check.tier_combined_ceiling_usd` | ≤$40 | $450 / $870 | $870 | Mode A no-render; Mode C Enterprise-only |
| 11-point gate + firewall + caption + floor | ALL | ALL | ALL | Universal — every mode, every tier |

The matrix is the basis for the SKILL bundle's verdict-routing logic on the SKILL-build day.

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 41 · status updates only)

**Calendar inherited from outline §0 build calendar.** Day 41 author task per outline: status updates only — calendar shape unchanged. Updates encoded below.

### 14.1 Calendar (Day 40 → v1.0 LOCK — QC Pre-flight trajectory)

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 40 | Fri May 29 · Wk6 | **QC Pre-flight Agent v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 41 | Sat May 30 · Wk6 | **SPEC body partial 1: §6 (12-Check Self-QC, 12 checks bipartite-covering 9 errorEnvelope codes + slot-11) + §7 (System Prompt v1.0 frame + 12 hard rules + 11-point Brand Voice gate inlined verbatim + universal-tier table + 11-step verdict loop + voice rule) + §10 (Field Map 26 rows: 8 lineage + 10 per-check evidence + 8 reel-level verdict aggregate) + §14 (Implementation Plan status updates)** | ✅ DONE — this document, LOCKED-as-drafted | Donna overnight |
| Day 42 | Sun May 31 · Wk6 | **REST DAY — no build.** Pre-stage partial 2 scaffold only (Day 21/28/35 Rest Day-compounding pattern). 6th Rest Day observance. | — | — |
| Day 43 | Mon Jun 1 · **commercial-launch target** | **SPEC body partial 2: §8 (Performance Targets — 9 metric categories) + §9 (5 Test Fixtures TC-01..TC-05) + §11 (Cost Model — near-zero engine snapshot + catch-cost-avoidance value model) + §12 (Verdict Math — deterministic ∧-of-gates) + §13 (10–14 Critical Decisions LOCKED) + §15 (Change Log) + §16 (Metadata Block — Cross-SPEC §3.9 + 4 additions)** **OR** commercial-launch pivot per operator's Day 42-target call. | ⬜ TARGET | Donna overnight + Jamila §13 amendments |
| Day 44+ | Tue Jun 2+ · post-launch hardening | **SPEC v1.0 LOCK CANDIDATE → input/output schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK.** Hard-gated on BOTH production-tier LOCKs (AI Video Gen + Style Replication) closing first + the Cross-SPEC §3.9 n-tuple amendment ratifying. | ⬜ QUEUED | Donna overnight + Jamila gates |

### 14.2 Dependencies that MUST exist before the SKILL-bundle build

| Dependency | Status | LOCK day |
|------------|--------|----------|
| Production Coord Agent v1.0 SPEC + schemas + SKILL bundle LIVE | ✅ DONE | Day 14–18 |
| Cross-SPEC Consistency Review LOCKED | ✅ DONE | Day 12 |
| AI Video Gen v1.0 SPEC LOCK CANDIDATE + schemas + SKILL bundle + Day 27 runbook AUTHORED | ✅ DONE | Day 24–27 |
| **AI Video Gen v1.0 LOCK (final operator-gated sign-off)** | ⚠️ **PENDING** | operator pickup — file-state confirms unflipped |
| Style Replication v1.0 SPEC LOCK CANDIDATE + schemas + SKILL bundle + Day 36 runbook AUTHORED | ✅ DONE | Day 32–36 |
| **Style Replication v1.0 LOCK (final operator-gated sign-off)** | ⚠️ **PENDING** | operator pickup — hard-gated on AI Video Gen LOCK first |
| **Day 36 Style Replication LLM Test Runbook EXECUTION (5/5 PASS gate)** | ⚠️ **PENDING** | operator paste-and-run sit-down — outcome unconfirmed |
| QC Pre-flight SPEC outline §0–§5 | ✅ DONE | Day 40 |
| QC Pre-flight SPEC body §6 + §7 + §10 + §14 LOCKED-as-drafted | ✅ DONE — this document | Day 41 (today) |
| QC Pre-flight SPEC body §8 + §9 + §11 + §12 + §13 + §15 + §16 LOCKED | ⬜ TARGET | Day 43 |
| **Cross-SPEC §3.9 n-tuple-as-lineage amendment RATIFICATION** | ⚠️ **PENDING** | operator pickup — forcing function for the 6-tuple parent_chain |

### 14.3 Cross-SPEC §3 adherence (preliminary audit — full audit at LOCK CANDIDATE)

| Cross-SPEC dimension | Day 41 partial 1 status |
|----------------------|-------------------------|
| §3.1 naming canon (snake_case agent_id) | ✅ `qc-preflight-agent` verified; slot-11 code `preflight_qc_agent_failed` matches canon |
| §3.2 hash invariant | ✅ `verdict_evidence_hash` SHA-256 over evidence block (Check #11); Mode B negative-prompt SHA-256 cross-check (Check #9) |
| §3.3 errorEnvelope shape | ✅ Mirrors fleet shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` + `route_back_to` per §6.3 |
| §3.4 qc_pre_flags minItems 4 + snake_case | ✅ **This agent is the adjudicator of the §3.4 floor** — Check #7 + Step 3 enforce it across all 6 upstream stages |
| §3.5 mode matrix | ✅ Mode-agnostic verdict + mode-aware reporting (§10.5 matrix) |
| §3.6 slot-11 reserved naming | ✅ `preflight_qc_agent_failed` reserved at §6.3 |
| §3.7 qc_pre_flags format regex | ✅ Enforced via Check #12 with regex `^[a-z][a-z0-9_]{0,63}$` |
| §3.8 tier↔mode firewall (7th defense-in-depth pass) | ✅ Check #2 + §7 Hard Rule #4 + universal-tier table + Step 2 |
| §3.9 metadata block + n-tuple parent_chain | ✅ §10.1 inherits canonical + extends to **6-tuple** (Check #9). **Forcing function for the §3.9 n-tuple amendment ratification** (operator-pending — §14.7) |
| §3.10 cost ceiling authority | ✅ §7.3 combined-ceiling reconciliation ($450 Pro / $870 Enterprise) + Step 7 enforcement (first agent with total-spend visibility) |
| §3.11 LOCK respect (no modification of upstream LOCKED canon) | ✅ Day 41 partial 1 references AI Video Gen + Style Replication + Cross-SPEC canon read-only; no modifications |

11 of 11 dimensions ✅ at partial 1 stage. Full LOCK audit at LOCK CANDIDATE.

### 14.4 Rest Day honored

Days 21 (May 10), 28 (May 17), 35 (May 24) — no build sessions per the Daily OS pillar order (Rest → Body → Money → Authority → Relationships). Spec-scaffold work allowed under the Rest Day-compounding pattern (Day 21 scaffold + Day 28 primer + Day 35 runbook primer precedents). **Day 42 (Sun May 31) honors the same pattern — no build; pre-stage partial 2 scaffold only.** This is the sprint's 6th Rest Day.

### 14.5 Day 41 sprint completion summary

| Section | Status | Notes |
|---------|--------|-------|
| §6 12-Check Self-QC List | ✅ DRAFTED | 12 checks fully drafted with failure-code mapping. Slot-11 `preflight_qc_agent_failed` reserved per Cross-SPEC §3.6. Error-code namespace settled at **9 LOCKED + slot-11** (Day 41 narrowing: `qc_pre_flags_format_violation` → `qc_pre_flags_floor_breach`; `negative_prompt_chain_break` → `lineage_integrity_failure`). Self-QC-vs-verdict-loop distinction documented (the agent QCs its own verdict report). Bipartite coverage flagged for LOCK-candidate audit. |
| §7 System Prompt v1.0 | ✅ DRAFTED | Single fenced block: frame + **12 hard rules** + **11-point Brand Voice gate inlined verbatim** + universal-tier table + 11-step verdict loop + voice rule. Seven structural decisions rationalized in §7.2. Recommend-don't-approve (Rule 12) is the defining non-inherited rule. Combined-ceiling reconciliation cross-references both production agents ($450 / $870). |
| §10 Field Map | ✅ DRAFTED | 26 rows: 8 lineage + 10 per-check evidence + 8 reel-level verdict aggregate. **6-tuple parent_chain extension drafted but BLOCKED on the Cross-SPEC §3.9 amendment ratification** (operator-pending — the forcing function). 4 v1.0 reserved fields enumerated. Verdict-by-mode reporting matrix added (§10.5). Schema authoring notes embedded. |
| §14 Implementation Plan | ✅ DRAFTED | Status updates only. Calendar shape unchanged from outline. Dependency table extended with Day 41 rows + the three operator-pending gates surfaced. Cross-SPEC §3 preliminary audit completed (11/11 ✅). |

### 14.6 Day 43 partial 2 authoring runway

Day 43 must author (or pivot to commercial launch per the operator's Day 42 call):
- **§8 Performance Targets** — 9 metric categories: schema validity 100% / firewall catch 100% (the 7th pass must be perfect by construction) / **false-pass rate 0% (a brand-safety gate must never pass a breach)** / false-fail rate ≤ 5% (over-blocking is the acceptable direction) / 11-point adjudication completeness 100% / p50 latency 30s / p95 90s (reasoning-only, fast) / zero engine cost / route-back accuracy 100% (every fail routes to the correct agent). Pattern source: AI Video Gen Day 23 §8.
- **§9 5 Test Fixtures** — TC-01 clean Mode B Pro PASS · TC-02 Mode C Enterprise PASS · TC-03 `entity_firewall_breach` (injected banned token — the 7th-pass catch) · TC-04 `format_spec_violation` (aspect mismatch → fail + route) · TC-05 `drift_unresolved` (carried drift → human-review soft-hold). 5 of 9 codes exercised; remainder in schema-only fixtures. Pattern source: Style Replication Day 31 §9.
- **§11 Cost Model** — near-zero engine snapshot (reasoning-only; optional native pHash/CLIP re-verify $0.001/shot on contested drift). Catch-cost-avoidance value model (the agent's economic justification is *downstream-cost prevention + brand-safety-incident avoidance*, not direct margin).
- **§12 Verdict Math** — deterministic ∧-of-gates: `PASS = (firewall clean) ∧ (11/11 brand-voice) ∧ (0 format violations) ∧ (0 caption violations) ∧ (cost within ceiling) ∧ (qc_pre_flags floor met) ∧ (no unresolved drift)`. Any single ∧-term false → fail/reshoot/hold per the §3.2 + Step-8 routing. No thresholds to tune (unlike Style Replication's drift score). Zero new math beyond boolean composition.
- **§13 Critical Decisions** — target 10–14 LOCKED. 8 LOCKED-as-drafted Day 40 outline (pre-flight scope, universal tier, verdict model, false-pass tolerance ZERO, engine policy, recommend-don't-approve, LUFS deferral, schema strategy). 2 RESOLVED Day 41 by this partial 1 (errorEnvelope code count → 9 LOCKED §6.3; self-QC check count → 12 LOCKED §6.1). 2 remain PRELIMINARY for Day 43 operator amendment (route-back automation depth; 6-tuple parent_chain — gated on §3.9 ratification).
- **§15 Change Log** — v1.0 lifecycle entries (outline-day-40 → body-day-41 → Rest Day-day-42 → body-day-43 → LOCK-candidate → schemas → SKILL → runbook → LOCKED).
- **§16 Metadata Block Schema** — Cross-SPEC §3.9 canonical fields + 4 QC Pre-flight additions (6-tuple parent_chain, `qc_gate_class`, `verdict_evidence_hash`, `runtime_environment_class`).

### 14.7 Operator action items carried over (UNCHANGED — surfaced again, NOT advanced)

Four operator-only items remain open and are surfaced here per the process-integrity attestation. Donna did NOT advance any of them:

1. **AI Video Gen v1.0 LOCK ceremony** — Day 24 Items 8 + 11 ratification + Day 27 LLM Test sit-down outcome. STILL PENDING (file-state confirmed — SKILL.md frontmatter unflipped). Hard-gates Style Replication LOCK.
2. **Style Replication v1.0 LOCK ceremony** — Day 32 LOCK CANDIDATE Items 6 + 8 + 11. STILL PENDING (file-state confirmed — SKILL.md frontmatter unflipped).
3. **Day 36 Style Replication LLM Test Runbook execution** — the paste-and-run iMac sit-down (`ARS-2026-05-25-Day-36-Style-Replication-LLM-Test-Runbook.md`). Outcome unconfirmed; 5/5 PASS is the LOCK gate.
4. **Cross-SPEC §3.9 n-tuple-as-lineage amendment ratification** — now a hard forcing function for QC Pre-flight's 6-tuple parent_chain (Check #9 + §10.1 row 6 + §10.4 schema note all BLOCK on it). Donna recommends RATIFY-AS-DRAFTED so all 17 agents inherit n-tuple lineage.

All four are independent; any can move first. QC Pre-flight v1.0 LOCK (post-launch hardening window) hard-gates on items 1–2 closing + item 4 ratifying.

---

## §8 — Performance Targets

`<<TBD-D43>>`

*Day 43 author task. Pattern source: AI Video Gen §8 (Day 23 LOCKED) / Style Replication §8 (Day 31 LOCKED). Targets: schema validity 100% / firewall catch 100% / **false-pass 0%** / false-fail ≤ 5% / 11-point adjudication completeness 100% / p50 30s / p95 90s / zero engine cost / route-back accuracy 100%.*

---

## §9 — 5 Test Fixtures

`<<TBD-D43>>`

*Day 43 author task. Pattern source: Style Replication §9 (Day 31 LOCKED). Fixtures: TC-01 Mode B Pro clean PASS · TC-02 Mode C Enterprise clean PASS · TC-03 `entity_firewall_breach` (injected banned token, 7th-pass catch) · TC-04 `format_spec_violation` (aspect mismatch → fail + route_back_to) · TC-05 `drift_unresolved` (carried drift → soft-hold). 5 of 9 LOCKED codes exercised; remainder schema-only. Fixtures live at `skills/qc-preflight-agent/tests/`. Each fixture = (input.json, expected_output.json, expected_verdict, expected_code_or_null, scenario_description).*

---

## §11 — Cost Model

`<<TBD-D43>>`

*Day 43 author task. Pattern source: Style Replication §11 (Day 31 LOCKED). Near-zero engine snapshot: $0.00 base (reasoning-only) + optional native pHash/CLIP re-verify $0.001/shot ONLY on contested drift. Effective per-reel $0.00–$0.02. Value model = catch-cost-avoidance: preventing a firewall breach reaching a published surface (brand-safety incident) or burning downstream post-production cycles. The economic justification is downstream-cost prevention, not direct margin.*

---

## §12 — Verdict Math

`<<TBD-D43>>`

*Day 43 author task. Deterministic ∧-of-gates: `PASS = (firewall clean) ∧ (11/11 brand-voice) ∧ (0 format violations) ∧ (0 caption violations) ∧ (cost within ceiling) ∧ (qc_pre_flags floor met) ∧ (no unresolved drift)`. Any single ∧-term false → fail / reshoot / hold per §3.2 + Step-8 routing. Unlike Style Replication's weighted drift score (`0.40×s_phash + 0.40×s_clip + 0.20×s_palette`), QC Pre-flight has NO thresholds to tune — it is pure boolean composition over the upstream evidence surface. Zero new continuous math to author.*

---

## §13 — Critical Decisions LOCKED (target 10–14)

`<<TBD-D43>>`

*Day 43 author task. 8 LOCKED-as-drafted Day 40 outline (pre-flight scope, universal tier, verdict model, false-pass tolerance ZERO, engine policy, recommend-don't-approve, LUFS deferral, schema strategy). 2 RESOLVED Day 41 by this partial 1 (errorEnvelope code count → 9 LOCKED §6.3; self-QC check count → 12 LOCKED §6.1). 2 PRELIMINARY for Day 43 operator amendment (route-back automation depth; 6-tuple parent_chain — gated on Cross-SPEC §3.9 ratification). Target: 12–14 LOCKED on Day 43.*

---

## §15 — Change Log + Version History

`<<TBD-D43>>`

*Day 43 author task. Pattern source: Style Replication §15 (Day 31 LOCKED). Initial entries:*
- *v1.0-draft-day-40 — outline §0–§5 SHIPPED (`ARS-2026-05-29-Day-40-QC-Preflight-Agent-SPEC-Outline.md`)*
- *v1.0-draft-day-41 — this document — body §6/§7/§10/§14 LOCKED-as-drafted; §8/§9/§11/§12/§13/§15/§16 RESERVED*
- *v1.0-draft-day-43 — §8/§9/§11/§12/§13/§15/§16 LOCKED (or commercial-launch pivot)*
- *v1.0-LOCK-CANDIDATE → v1.0-schemas → v1.0-SKILL → v1.0-runbook → v1.0-LOCKED (post-launch hardening window; hard-gated on both production LOCKs + §3.9 ratification)*

---

## §16 — Metadata Block Schema

`<<TBD-D43>>`

*Day 43 author task. Pattern source: Style Replication Day 31 §16 (Cross-SPEC §3.9 canonical fields). QC Pre-flight additions (4 fields):*
- *`parent_chain` — **6-tuple** (Style Replication 5-tuple + `preflight_report_id`); gated on §3.9 amendment ratification*
- *`qc_gate_class` — enum (`pre_flight` v1.0 · `pre_publish` reserved v1.1+)*
- *`verdict_evidence_hash` — SHA-256 over the per-check evidence block (tamper-evident verdict)*
- *`runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16*

*Cross-SPEC §3.9 amendment LOCK ceremony required for the 6-tuple parent_chain + the 4 additions.*

---

## Mirror status

- Source: `ars/ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` (this document) + `ars/build-log-2026-05-30.md`
- Mirror destination: `/outputs/ars/ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` + `/outputs/ars/build-log-2026-05-30.md`
- Mirror verification: in this session's mirror step.

---

## Process integrity (Day 41)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked. (QC Pre-flight by design calls no generative engine — Hard Rule #2 — appropriate for a pure quality-gate agent.)
- ✅ **No external comms.** No emails, DMs, social posts, investor/client outreach. The status SMS to Jamila ([status number redacted]) announces build status only; it transacts no business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, zero $ spent.
- ✅ **No operator-impersonation.** Both production-tier LOCK ceremonies confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Day 36 runbook execution NOT assumed. Cross-SPEC §3.9 amendment NOT silently committed — the 6-tuple parent_chain is explicitly BLOCKED pending operator ratification (§10.4 + §14.7).
- ✅ **No fake-advance.** This partial is forward-design over LOCK-stable text artifacts, explicitly labeled LOCKED-as-drafted (not LOCKED). QC Pre-flight v1.0 LOCK hard-gates on both production LOCKs + the §3.9 ratification. Zero net-new modifications to any LOCKED canon — all references read-only.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication SPECs + schemas + SKILL bundles + Cross-SPEC review + the Day 40 outline — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. The HC/NPOX tokens in §6.5 + §7 Rule 4 are the firewall's BLOCK-list (so the agent rejects them), not a cross-entity reference. REINVENTED remains brand-as-pilot-customer per Cross-SPEC canon.
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at partial 1 stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Style Replication Day 30 partial 1 structure inherited verbatim. AI Video Gen Day 22 grandparent + Brand Voice Intake §13 (11-point gate, inlined verbatim) + Orchestration Blueprint #14 QC definition + Cross-SPEC §3.4 floor used as the grounding spine.
- ✅ **Rest Day honored.** Day 42 (Sun May 31) will be observed — no build; pre-stage partial 2 scaffold only. 6th observance.

---

*Day 41 ships clean. Day 43 build session is primed — §8 + §9 + §11 + §12 + §13 + §15 + §16 all have LOCK targets defined, with 8 of 14 critical decisions LOCKED-as-drafted Day 40 + 2 resolved today (9 codes + 12 self-QC checks). QC Pre-flight is Agent #7 of 17 — the 7th and final automated defense-in-depth firewall, the first universal-tier gate since Brief, and the agent the qc_pre_flags minItems-4 floor was built for. Operator pickup (4 items, all independent, surfaced NOT advanced): (1) AI Video Gen v1.0 LOCK ceremony; (2) Style Replication v1.0 LOCK ceremony; (3) Day 36 Style Replication LLM Test Runbook execution; (4) Cross-SPEC §3.9 n-tuple amendment ratification (now the hard forcing function for the 6-tuple parent_chain). Day 42 Rest Day observed. Day 43 = partial 2 OR commercial-launch pivot per the operator's Day 42-target call.*
