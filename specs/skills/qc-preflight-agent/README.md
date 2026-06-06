# QC Pre-flight Agent — README (v1.0)

Human invocation guide for the **terminal pre-flight quality gate** — Agent #7 of 17 in the Agentic Reel Studio (ARS) pipeline, and the **7th and last defense-in-depth firewall**.

> **Built:** Thu Jun 4, 2026 (Day 46 · Wk7D3 · post-launch hardening window) · Sequel Digital — ARS
> **SPEC:** `ARS-2026-06-02-Day-44-QC-Preflight-Agent-v1-LOCK-CANDIDATE.md` (operator Items 6/8/11 pending)
> **Schemas:** Day 45 (Wed Jun 3) LOCKED-as-drafted + META-SCHEMA VALID (Draft 2020-12)
> **Bundle validation:** `validate.py` — 34/34 assertions green (meta-schema + 10 fixture validations + 14 adversarial guards)
> **v1.0 LOCK target:** post-launch hardening window — **HARD-GATED on AI Video Gen v1.0 LOCK + Style Replication v1.0 LOCK first**

---

## What this skill does

Reads the converged production-tier output — a `replicated_shots` payload from Style Replication
(primary, any mode) and optionally a `rendered_shots` payload from AI Video Gen (Mode B forensic
cross-check) — plus the denormalized upstream chain (`metadata.parent_chain`) and the per-stage
`qc_pre_flags[]` accumulated through the pipeline. It emits a single `preflight_report.json` carrying
a **Pass / Fail / Reshoot / Hold** verdict with per-check evidence.

Single-responsibility line: *"Terminal pre-flight quality gate. Adjudicate the full reel chain
against the 11-point Brand Voice QC gate, the entity firewall (7th pass), platform format specs,
caption specs, and the cumulative tier cost ledger. Emit a single Pass / Fail / Reshoot verdict with
per-check evidence. Calls NO generative engine."*

This is the **only agent that spends $0 at runtime** (reasoning-only; optional native pHash/CLIP
re-verify at ~$0.001/shot on contested drift only) and the **only agent with total-spend visibility**
across both production agents.

---

## Pipeline position

```
Trend Hunter → Strategy → Brief → Script → Storyboard → Production Coord → AI Video Gen → Style Replication → QC PRE-FLIGHT → Localization / Publishing → Loop
```

QC Pre-flight is the **terminal automated gate** and the **7th defense-in-depth firewall**: Brief
sets the entity firewall; Script, Storyboard, ProdCoord, AI Video Gen, and Style Replication each
re-validate it; QC Pre-flight is the **net** that catches whatever the six prior passes missed, and
adds the 11-point Brand Voice QC adjudication + the combined-reel cost-ledger reconciliation + the
tamper-evident verdict.

It is also the **first gate every tier traverses since Brief** — safety is not a tier feature. A
Pilot Mode A reel that leaks a banned token is the same brand-safety incident as a Enterprise-tier
Enterprise reel.

---

## When to invoke

- A Style Replication `successReplicatedShots` set is ready, in any mode (A / B / C).
- Mode B: AI Video Gen `rendered_shots` is also present for the forensic SHA-256 cross-check.
- The pipeline is about to hand a reel to Localization / Publishing — QC Pre-flight is the last stop.

**Do NOT invoke when:**
- Any consumed upstream branch is an `errorEnvelope` — QC Pre-flight halts at Step 1 with `upstream_not_success` (it cannot QC a failed input).
- You expect the agent to *fix* a defect — it adjudicates and routes; it does not patch (no engine).
- You expect a publish authorization — it **recommends**; the operator approves (Rule #12).

---

## Inputs (required envelope)

Validated by `schemas/input.schema.json`. Six required top-level fields:

| Field | Shape |
|-------|-------|
| `replicated_shots` | array (1–60) of `{shot_id, asset_uri (ars://…), qc_pre_flags[≥4], drift_warning_bool?, style_drift_exceeded?}` |
| `production_plan` | `{production_plan_id, platform_variants[1–12] of {platform, aspect_ratio, duration_s, caption_burn}}` |
| `brief_ref` | `{brief_id}` |
| `metadata` | `{tier, production_mode (A/B/C), parent_chain (5-tuple), session_id, lever_state, brand_id?}` |
| `cost_ledger` | `{ai_video_gen_actual_usd, style_replication_actual_usd, tier_combined_ceiling_usd ∈ {40,450,870}}` |
| `accumulated_qc_pre_flags` | object keyed by all 6 upstream agents, each ≥4 snake_case predicates |

Optional (Mode B forensic): `rendered_shots[]` + `negative_prompt_sha256`.

---

## Outputs (polymorphic)

Validated by `schemas/output.schema.json` — `oneOf [successPreflightReport | errorEnvelope]`.

- **`successPreflightReport`** (`verdict: "pass"`): the 13-term PASS conjunction held true. Carries
  `brand_voice_qc` (11/11), `entity_firewall_pass_7` (hits 0), `format_spec_check`, `caption_spec_check`,
  `cost_ledger_check` (within_ceiling), `qc_pre_flags_adjudication`, `drift_reconciliation` (0 unresolved),
  `mode_b_chain_check` (Mode B object / Mode A,C null), `handoff_targets: ["localization","publishing"]`,
  and a `verdict_evidence_hash`. **A false-pass is structurally impossible** — every `per_point.status`
  must be `pass`, every violation count `const 0`, schema-enforced.
- **`errorEnvelope`** (`verdict ∈ {fail, reshoot, hold}`): a `failure_code` from the 9 LOCKED codes +
  slot-11 catch-all, a `failed_check_id` (1–12), `route_back_to`, and an advisory `detail.recovery_path`.

`human_review_required` is `const true` on **both** branches (recommend-don't-approve, schema-enforced).

### Verdict → route map

| Verdict | route_back_to | Meaning |
|---------|---------------|---------|
| `pass` | `null` + handoff_targets | Cleared to advance to the human's publish decision. |
| `fail` | responsible upstream agent | Fixable without re-shooting. |
| `reshoot` | `production-coord-agent` (**Mode A only**) | Live source footage unusable. |
| `hold` | `null` (human review) | `drift_unresolved` soft-hold — NOT auto-failed, NOT auto-passed. |

---

## Test fixtures (`test-cases/`)

| Case | Verdict | Branch | Proves |
|------|---------|--------|--------|
| `case-01-mode-b-pro-clean-pass` | pass | success | dominant volume happy path + Mode B forensic cross-check |
| `case-02-mode-c-enterprise-clean-pass` | pass | success | mode-agnostic verdict, mode-aware reporting (`mode_b_chain_check: null`) |
| `case-03-entity-firewall-breach` | fail | error | **the 7th-pass catch — the agent's reason to exist (GATING fixture)** |
| `case-04-format-spec-violation` | fail | error | aspect mismatch → route to the responsible production agent |
| `case-05-drift-unresolved` | hold | error | the soft-hold 4th verdict; defers to the human |

The 3 codes exercised live are `entity_firewall_breach`, `format_spec_violation`, `drift_unresolved`.
The remaining 6 LOCKED codes + slot-11 are bound to the schema via `validate.py` adversarial guards
(same discipline as the Style Replication §9 portfolio).

---

## How to validate the bundle

```bash
cd skills/qc-preflight-agent
python3 validate.py      # 34/34 assertions; exit 0 = green; $0, no engine, no network
```

`validate.py` compiles both schemas under the Draft 2020-12 meta-schema, validates all 5
fixtures (input + expected_output) against the schemas, and runs 14 adversarial guards: false-pass
rejection, firewall-hits-on-pass rejection, unresolved-drift-on-pass rejection,
`human_review_required:false` rejection, hold/reshoot route guards, both folded codes rejected, the
`parent_chain` 6/5-tuple-accept-4-tuple-reject backward-compat, and the input floor/asset-uri/ceiling
guards.

---

## LOCK status & operator action items

QC Pre-flight v1.0 is a **LOCK CANDIDATE** (Day 44). This bundle is the Day 46 deliverable; it is
**LOCKED-as-drafted**, not LOCKED. The v1.0 LOCK ceremony is **OPERATOR-ONLY** and **hard-gated**:

1. **AI Video Gen v1.0 LOCK** — pending (hard-gates this LOCK).
2. **Style Replication v1.0 LOCK** — pending (hard-gates this LOCK).
3. **Day 36 Style Replication LLM Test Runbook** — 5/5 PASS unconfirmed (Style Replication LOCK gate).
4. **QC-local items** (independent): Item 6 inherited-ceiling confirm · Item 8 the 14-decision walk
   (#4/#13 PRELIMINARY) · Item 11 Cross-SPEC §3.9 amendment (the 6-tuple `parent_chain` forcing function).

Next forward deliverable after this bundle: the **LLM Test Runbook** (paste-and-run, operator-gated).

> **Hard constraints (CLAUDE.md + ARS attestation):** no generative engine, ever ($0 ceiling is
> forbidden-spend, not bounded-spend). Recommend-don't-approve — never "approved for publish."
> Sequel Digital entity only.
