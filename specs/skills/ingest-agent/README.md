# Ingest Agent — README (v1.0)

Human invocation guide for the **post-production gateway** — Agent #8 of 17 in the Agentic Reel Studio (ARS) pipeline, the **first post-production agent**, the **8th defense-in-depth firewall** (the first to scan the asset layer), and the **mode-convergence seam**.

> **Built:** Sat Jun 13, 2026 (Day 55 · Wk8 · post-launch hardening window) · Sequel Digital — ARS
> **SPEC:** `ARS-2026-06-11-Day-53-Ingest-Agent-v1-LOCK-CANDIDATE.md` (operator Items 6/8/11 pending)
> **Schemas:** Day 54 (Fri Jun 12) LOCKED-as-drafted + META-SCHEMA VALID (Draft 2020-12)
> **Bundle validation:** `validate.py` — 47/47 assertions green (meta-schema + 10 fixture validations + adversarial guards)
> **v1.0 LOCK target:** post-launch hardening window — **HARD-GATED on AI Video Gen + Style Replication + QC Pre-flight v1.0 LOCKs first**

---

## What this skill does

Receives the QC-passed production output, validates each asset against the production-plan technical spec **at the declared-metadata level** (no byte-level decode), confirms full storyboard-shot coverage, runs the **8th defense-in-depth firewall pass** over the asset layer (filenames, embedded media metadata, sidecar caption/SRT files), and emits a single canonical **`asset_manifest.json`** carrying a **Pass / Fail-fixable / Reshoot** verdict with per-asset evidence.

Single-responsibility line: *"Post-production gateway. Receive the QC-passed production output, validate each asset against the production-plan spec at the declared-metadata level, confirm full shot coverage, run the 8th firewall pass over the asset layer, and emit a single canonical Asset Manifest with a Pass / Fail / Reshoot verdict. Calls NO generative engine and performs NO byte-level decode."*

Two things make this agent distinctive: it is the **mode-convergence seam** — whatever production mode enters (A live footage, B replicated+rendered, C replicated), it emits **one manifest shape**, and from it onward the entire in-post fleet is mode-blind. And it is the **only agent with NO native-compute option at all** — its effective per-reel cost is structurally **$0.00** ($0 engine + $0 byte-probe), tying QC Pre-flight for the cheapest agent in the 17-agent fleet.

---

## Pipeline position

```
… → AI Video Gen → Style Replication → QC Pre-flight → INGEST → Edit Director → … → Loop
                                          (gate)        (gateway)  (Agent #9, not yet built)
```

Ingest sits immediately downstream of the QC Pre-flight gate and immediately upstream of Edit Director (Agent #9). It is the **8th defense-in-depth firewall**: the seven prior passes scanned reel *content*; Ingest is the first and only pass to scan the **asset layer** — filenames, embedded media metadata, sidecar files — a surface no content pass can see.

It is also **universal-tier**: every reel, every mode, every tier traverses it at ~$0. A Pilot Mode A reel with a missing shot file is the same edit-blocking defect as a Enterprise reel — the gateway opens for everyone, identically.

---

## When to invoke

- A QC Pre-flight `preflight_report` came back `verdict: "pass"` (or a Lever-3 sign-off is attached) and a production-tier asset set is ready.
- Mode A: a videographer `footage_upload_manifest` is ready for the take-substitution + coverage gateway.
- Mode B/C: a Style Replication `replicated_shots` set is ready (Mode B adds the AI Video Gen `rendered_shots` forensic cross-ref).
- The pipeline is about to hand assets to Edit Director — Ingest is the convergence gateway that makes that handoff mode-blind.

**Do NOT invoke when:**
- The `preflight_report` verdict is not `pass` and no Lever-3 sign-off is attached — Ingest halts at Step 1 with `upstream_qc_not_passed` (it never ingests an unvetted reel).
- Any consumed upstream branch is an `errorEnvelope` — Ingest halts with `upstream_not_success` (it cannot ingest a failed input).
- You expect the agent to *fix* a defect — it adjudicates and routes; it does not patch, transcode, or conform (no engine).
- You expect a clear-to-edit authorization — it **recommends**; the operator clears (Rule #12).

---

## Inputs (required envelope)

Validated by `schemas/input.schema.json`. Five required top-level fields + the polymorphic production source:

| Field | Shape |
|-------|-------|
| `preflight_report` | `{preflight_report_id, verdict (pass/fail/reshoot/hold), lever3_signoff?}` — the QC precondition gate (read FIRST) |
| `production_plan` | `{production_plan_id, platform_variants[1–12] of {platform, aspect_ratio, duration_s, caption_burn}, assets_pulled?, music_bed?}` |
| `storyboard_ref` | `{storyboard_id, total_shots (1–60)}` — the coverage basis |
| `brief_ref` | `{brief_id}` |
| `metadata` | `{tier, production_mode (A/B/C), parent_chain (6-tuple, held), session_id, lever_state, brand_id?}` |

**Polymorphic source** (top-level `oneOf`, keyed by `production_mode`):
- **Mode B/C** → `replicated_shots[]` present (Mode B may also carry `rendered_shots[]` for the forensic cross-ref). `footage_upload_manifest` forbidden.
- **Mode A** → `footage_upload_manifest` present (`{clips[] with takes, audio[], music_bed?}`). `replicated_shots` AND `rendered_shots` forbidden.

---

## Outputs (polymorphic)

Validated by `schemas/output.schema.json` — `oneOf [successAssetManifest | errorEnvelope]`.

- **`successAssetManifest`** (`verdict: "pass"`): the AND-of-8-gates held true. Carries the canonical `asset_bundle` (the editor's mode-agnostic pull list), `mode_convergence`, `qc_precondition_check`, `asset_uri_integrity` (`non_relative/dangling: 0`), `asset_firewall_pass_8` (`hits: 0`), `spec_check` (all booleans `true`, `missing_shots: []`), `coverage_check` (`coverage_complete: true`), `handoff_targets: [edit-director-agent]`, and a `manifest_evidence_hash`. **A false-pass is structurally impossible** — every gate term is schema-pinned `const`.
- **`errorEnvelope`** (`verdict ∈ {fail, reshoot}`): a `failure_code` from the 8 LOCKED codes + slot-11 catch-all, a `failed_check_id` (1–11), `attempts` (1–2), `route_back_to`, and an advisory `detail.recovery_path`.

`human_review_required` is `const true` on **both** branches (recommend-don't-clear, schema-enforced). `byte_probe_performed` is `const false` (declared-spec honesty contract).

### Verdict → route map

| Verdict | route_back_to | Meaning |
|---------|---------------|---------|
| `pass` | — + `handoff_targets: [edit-director-agent]` | Ready to advance to the operator's clear-to-edit decision. |
| `fail` | producing agent or `re-upload` | Fixable without re-shooting. |
| `reshoot` | `production-coord-agent` (**Mode A only**) | Live footage unusable, take-ladder exhausted. |
| `fail` (`ingest_agent_failed`) | `null` | Slot-11 self-QC exhaustion (attempts 2). |

There is **no `hold`** — Ingest's domain is deterministic (deliberate divergence from QC Pre-flight).

---

## Test fixtures (`test-cases/`)

| Case | Verdict | Branch | Proves |
|------|---------|--------|--------|
| `case-01-mode-b-pro-clean-pass` | pass | success | dominant-volume happy path + Mode B forensic source |
| `case-02-mode-c-enterprise-clean-pass` | pass | success | **the mode-convergence proof** — bundle byte-shape identical to case-01 |
| `case-03-mode-a-coverage-gap-reshoot` | reshoot | error | the Mode-A-exclusive `reshoot` verdict (`if/then` route guard) |
| `case-04-asset-spec-violation` | fail | error | declared-spec mismatch → route to the producing agent |
| `case-05-asset-firewall-breach` | fail | error | **the 8th-pass asset-layer catch — the agent's reason to exist (GATING fixture)** |

Five of the 8 codes are exercised behaviorally. The 3 unexercised codes (`upstream_qc_not_passed`, `upstream_not_success`, `manifest_lineage_failure`) are deterministic single-assertion entry/forensic halts covered schema-only; slot-11 `ingest_agent_failed` is covered by the `validate.py` adversarial guards (same fixture-economy discipline the Style Replication + QC Pre-flight portfolios ratified).

---

## How to validate the bundle

```bash
cd skills/ingest-agent
python3 validate.py      # 47/47 assertions; exit 0 = green; $0, no engine, no probe, no network
```

`validate.py` compiles both schemas under the Draft 2020-12 meta-schema, validates all 5 fixtures (input + expected_output), and runs the adversarial guards: false-pass rejection (failing `spec_check` / firewall hits / non-empty `missing_shots` / `coverage_complete:false` on a pass), `byte_probe_performed:true` rejection, `human_review_required:false` rejection, the `reshoot`/slot-11 `if/then` route guards, the folded `duration_envelope_breach` code rejected, `hold` rejected, the `parent_chain` 7/6/5-tuple-accept-4-tuple-reject backward-compat, the polymorphic-source `oneOf` guards, the qc_pre_flags floor + `ars://` URI guards, and the TC-01/TC-02 convergence proof.

---

## LOCK status & operator action items

Ingest v1.0 is a **LOCK CANDIDATE** (Day 53). This bundle is the Day 55 deliverable; it is **LOCKED-as-drafted**, not LOCKED. The v1.0 LOCK ceremony is **OPERATOR-ONLY** and **hard-gated**:

1. **AI Video Gen v1.0 LOCK** — pending (chain head; hard-gates this LOCK).
2. **Style Replication v1.0 LOCK** — pending (Day 36 runbook 5/5 unconfirmed).
3. **QC Pre-flight v1.0 LOCK** — pending (Day 47 runbook 5/5 unconfirmed) — **Ingest's direct dependency** (precondition gate + the 6-tuple the 7-tuple extends).
4. **Ingest-local items** (independent, any can move first): Item 6 cost-model confirm (the lightest in fleet history — no vendor URLs, no ceilings owned) · Item 8 the 15-decision walk (D15 PRELIMINARY → Notion holding store; D6 doubly-deferred) · Item 11 Cross-SPEC §3.9 amendment (the 7-tuple forcing function — now doubly load-bearing with QC's 6-tuple).

Next forward deliverable after this bundle: the **LLM Test Runbook** (paste-and-run, operator-gated · Day 57+). Day 56 (Sun Jun 14) is the Rest Day — docs-prep only, no SPEC content.

> **Hard constraints (CLAUDE.md + ARS attestation):** no generative engine and no byte-level decode, ever ($0 ceiling is forbidden-spend, not bounded-spend). Recommend-don't-clear — never "cleared for edit." No cost re-litigation. False-pass tolerance ZERO. Sequel Digital entity only.
