# Edit Director Agent — v1.0 (ARS Agent #9 of 17)

The **Edit Director Agent** is the first creative-AUTHORING agent in the Agentic Reel Studio (ARS) post-production tail. It receives an Ingest-passed, mode-agnostic Asset Manifest plus the denormalized Script beat map and Storyboard shot vocabulary, and authors **one canonical Edit Plan** — cut order, pacing, captions, lower-thirds, music-bed swell map, transition policy, and the mandatory end-card — honoring the REINVENTED brand-edit ruleset and the 45–75s structure.

It calls **no generative engine and renders no media**. It authors a *plan*; the Editor (position 11) executes the cut. Its effective per-reel cost is **~$0.00**.

## What makes this agent distinctive

- **The 9th defense-in-depth firewall** — the FIRST pass to scan text the pipeline *authors itself* (lower-third copy, caption strings, the end-card line), a surface no prior content pass owned.
- **The first contractually mode-blind agent** — it never reads `production_mode`; `mode_blind_confirm.production_mode_read: false` is the live, machine-checkable proof that Ingest's mode-convergence seam holds end-to-end (the TC-01/TC-02 convergence proof).
- **The first 3-verdict fleet agent** — `plan_ready | fail | revise`, where `revise` is a success-branch payload that surfaces a soft brand-rule creative tension to a human (Lever-3) rather than silently overriding a rule or dropping a stronger cut.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | The verbatim v1.0 system prompt (paste-into-the-LLM contract) + operator guide. |
| `schemas/input.schema.json` | Validates the input (Ingest precondition gate + mode-converged Asset Manifest + denormalized creative intent). |
| `schemas/output.schema.json` | Validates the polymorphic output (`successEditPlan | errorEnvelope`, the 3-verdict model). |
| `test-cases/` | 5 dry-run fixtures (`input.json` + `expected_output.json` + `scenario.md`). |
| `validate.py` | Offline dry-run harness — meta-schema + fixture conformance + adversarial guards + the convergence proof. **$0, no engine, no render, no network, no LLM.** |

## Run the validator

```bash
cd edit-director-agent
python3 validate.py     # exit 0 = all green (59/59 assertions)
```

Requires `jsonschema>=4.26` (Draft 2020-12). The harness is purely structural — it spends nothing.

## Test-case portfolio (5 fixtures)

| Case | Verdict | Code | Proves |
|------|---------|------|--------|
| 01 — Mode-A-origin Pro | `plan_ready` | `null` | The full authored plan happy path. |
| 02 — Mode-C Enterprise | `plan_ready` | `null` | **The mode-blind convergence proof** — byte-shape-identical authoring path to TC-01 despite a different origin mode. |
| 03 — Coverage gap | `fail` | `incomplete_shot_coverage` | The defensive coverage re-confirm → route back to Ingest (can't cut over a hole). |
| 04 — Brand-edit conflict | `fail` | `brand_edit_rule_conflict` | A fade can never survive to `plan_ready` (hard FAIL, **not** `revise`). |
| 05 — Authored-text firewall breach | `fail` | `edit_plan_firewall_breach` | **GATING** — the 9th-pass catch on copy Edit Director itself wrote. |

The `revise` verdict and the slot-11 catch-all (`edit_director_agent_failed`) are exercised schema-only (via `validate.py`) and in the operator-run LLM Test Runbook's adversarial case, per the fleet's fixture-economy precedent.

## Pipeline position & dependencies

```
… → AI Video Gen (#5) → Style Replication (#6) → QC Pre-flight (#7) → Ingest (#8) → Edit Director (#9) → Editor (#10) → …
```

Edit Director consumes Ingest's `successAssetManifest`/`pass` as an absolute precondition and extends Ingest's 7-tuple `parent_chain` to an 8-tuple (held additively, triply-deferred — Decision D6). Its v1.0 LOCK is **hard-gated** on all four predecessor LOCK ceremonies closing first (AI Video Gen → Style Replication → QC Pre-flight → Ingest). The logical handoff target is `editor-agent` (Agent #10, not yet built); the physical v1.0 destination is the Notion Edit Plan holding store until Editor LOCKs (Decision D15, operator-pending).

## Status

**v1.0 LOCK CANDIDATE** (Day 61) — SPEC body §0–§16 complete, schemas authored (Day 62), this SKILL bundle authored (Day 64). Awaiting the operator LOCK ceremony, which is hard-gated on the four predecessor LOCKs + the Cross-SPEC §3.9 n-tuple amendment ratification. Entity scope: **Sequel Digital only**. Pilot brand: **REINVENTED**.
