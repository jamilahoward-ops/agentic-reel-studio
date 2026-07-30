# Full QC Agent — v1.0 (ARS Agent #13 of 17)

The **Full QC Agent** is the **first adjudicator agent** in the Agentic Reel Studio (ARS) post-production tail and the **terminal ship-safety gate** — the last automated check a reel passes before it reaches a publish queue and, from there, a client's live surface. **There is no gate after it.** It consumes the Motion Agent's finished-master motion spec (verdict `motion_ready`), the v3 finished master handle, the accumulated flag surface from all twelve upstream agents, and the tri-anchor evidence-hash chain, and emits **one ship verdict with a complete evidence block**: `pass` (cleared into the publish queue), `fail` (a post-fixable defect, routed to the responsible agent), or `reshoot` (a source-material defect no in-post fix can resolve, routed to Production Coord).

It calls **no generative engine, renders no media, decodes no frame, measures no pixel, and publishes nothing**. It adjudicates the DECLARED conform surface + re-verifies the hash chain, and re-derives exactly one thing (the firewall count). Its effective per-reel cost is **≈ $0.00–0.02** — the **seventh consecutive $0 agent**.

## What makes this agent distinctive

- **The first adjudicator — the first agent checking someone else's work.** The five upstream post agents (Ingest, Edit Director, Editor, Sound, Motion) are asset-readiness, direction, and execution; full QC is JUDGMENT. Twelve agents produced the reel and each checked its own work — full QC is the first checking another's, and the only one whose failure is visible to the client.
- **The 13th and TERMINAL defense-in-depth firewall — the ONLY pass that re-derives.** It re-scans every burned-in text field one final time before publish, computing its own hit count and **not trusting Motion's declared `banned_vocab_hits`**. Editor's 10th pass scanned committed text as *data*; Sound's 11th scanned the *spoken* transcript; Motion's 12th scanned the text as *pixels* and self-reported. Full QC re-derives that count and escalates any disagreement as a provenance finding — even when its own count is `0`. **A leak that survives here publishes with the gate's `pass` attestation on it, with no post-hoc fix.** (TC-05, GATING.)
- **The only agent to verify all THREE post-tail evidence hashes in one pass** — `motion_spec_evidence_hash` + `audio_spec_evidence_hash` + `edl_evidence_hash`; `chain_intact` is the AND of the three, never asserted true on an uncomputed leg.
- **The fifth contractually mode-blind agent.** It never reads `production_mode`; `mode_blind_confirm.production_mode_read: false` is the machine-checkable proof that Ingest's mode-convergence seam holds **five stages deep** (Edit Director → Editor → Sound → Motion → full QC — the TC-01/TC-02 gate-convergence proof). With full QC, the entire post-production tail is proven mode-agnostic from ingest to publish gate.
- **The second and final consumer of the §3.4 accumulation floor.** It reads the full 48-predicate flag surface and refuses to render a `pass` while any flag anywhere in the twelve-agent chain remains open — **the closure check no producer in the fleet can perform** (TC-04). The floor was provisioned across twelve agents specifically so this closure could exist.
- **RESTORES the third verdict — the terminal adjudicator's defining authority.** `pass | fail | reshoot`. Full QC is the only post agent positioned to declare a defect un-fixable in post. The pass/fail split is fully deterministic (any ∧-term false → not a pass); the fail-vs-reshoot determination is the single judgment call in the entire agent, isolated to non-pass routing so it can never produce a false pass. Mirrors QC Pre-flight exactly — full QC is its terminal twin.
- **The LARGEST error namespace in the fleet, by construction.** 12 named codes + slot — the arithmetic of the terminal position: three brand surfaces + two cross-agent closures + a third verdict. `route_back_to` is a computed field (three source-dependent route asymmetries), not a per-code const.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | The verbatim v1.0 system prompt (paste-into-the-LLM contract) + operator guide. |
| `schemas/input.schema.json` | Validates the input (Motion `motion_ready` precondition gate + mode-converged v3 master + tri-anchor evidence hashes + the 12-agent flag floor). |
| `schemas/output.schema.json` | Validates the polymorphic output (`successQcReport | errorEnvelope`, the 3-verdict model; false-PASS structurally unrepresentable). |
| `test-cases/` | 5 dry-run fixtures (`input.json` + `expected_output.json` + `scenario.md`). |
| `validate.py` | Offline dry-run harness — meta-schema + fixture conformance + adversarial guards + the false-PASS-unrepresentable proofs + the convergence proof. **$0, no engine, no render, no decode, no probe, no publish, no network, no LLM.** |

## Run the validator

```bash
cd qc-agent
python3 validate.py     # exit 0 = all green
```

Requires `jsonschema>=4.26` (Draft 2020-12). The harness is purely structural — it spends nothing.

## Test-case portfolio (5 fixtures)

| Case | Verdict | Code | Proves |
|------|---------|------|--------|
| 01 — Mode-A-origin Pro | `pass` | `null` | The full terminal-gate happy path. |
| 02 — Mode-C Enterprise | `pass` | `null` | **The mode-blind gate-convergence proof** — byte-shape-identical gate path to TC-01 despite a different origin mode (five stages deep). |
| 03 — Format variant mismatch | `fail` | `format_spec_mismatch` | A tier sold 2 variants delivered 1 → route to Motion — the delivery-promise gap only full QC reads. |
| 04 — Unresolved upstream flag | `fail` | `unresolved_upstream_flag` | An open flag on a complete surface → route to Editor — **the accumulation-floor closure catch NO other agent can perform**. |
| 05 — Terminal firewall breach | `fail` | `qc_firewall_breach` | **GATING** — the 13th-pass catch on the burned-in text, re-derived count (2) disagreeing with Motion's declared 0. |

The slot catch-all (`qc_agent_failed`), the `qc_flag_surface_incomplete` completeness variant, `caption_spec_breach`, `brand_voice_gate_fail`, `cost_ledger_overrun`, `master_unresolved`/`asset_uri_integrity_failure`, `evidence_hash_break`, and the `qc_reshoot_required` third verdict are exercised schema-only (via `validate.py`) and as named probes in the operator-run LLM Test Runbook, per the fleet's fixture-economy precedent. **`qc_reshoot_required` is the named adversarial runbook probe** — the reshoot verdict is definitionally hard to fixture from outside (it induces the fail-vs-reshoot judgment slot and asserts the bias-toward-`fail`).

## Pipeline position & dependencies

```
… → Editor (#10) → Sound (#11) → Motion (#12) → full QC (#13) → [Localization (#14) → Publishing (#16)] → …
```

Full QC consumes Motion's `successMotionSpec`/`motion_ready` as an absolute precondition and extends Motion's 11-tuple `parent_chain` to a 12-tuple (held additively, seventh-deferred — Decision D7). Its v1.0 LOCK is **hard-gated on the fleet's FIRST TRIPLE-gate**: the Sound v1.0 LOCK → the Motion v1.0 LOCK → full QC's own live 5/5, in order. Agents #1–#10 closed on the Day 79 ceremony; **Sound (#11) is the ONLY open ROOT link** (its LOCK is spend-gated on a live 5/5 run of the Day 81 runbook). The handoff target is `localization-agent` (Agent #14, not yet built) via the Drive `/reels/[reel_id]/` publish-queue holding store (D15).

## Status

**v1.0 LOCK CANDIDATE** (Day 96) — SPEC body §0–§16 complete, schemas authored (Day 97), this SKILL bundle authored (Day 100). Agents #1–#10 LOCKED on the Day 79 ceremony (240/240 real validation evidence); the Cross-SPEC §3.9 n-tuple amendment was ratified. Full QC stays at LOCK CANDIDATE until **(a) the Sound v1.0 LOCK closes, (b) the Motion v1.0 LOCK closes, and (c) full QC's own LLM Test Runbook is authored + run 5/5** — there is no 5/5 evidence to lock it on yet, and the harness does not manufacture one. Entity scope: **Sequel Digital only**. Pilot brand: **REINVENTED**.
