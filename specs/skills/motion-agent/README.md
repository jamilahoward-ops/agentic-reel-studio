# Motion Agent — v1.0 (ARS Agent #12 of 17)

The **Motion Agent** is the third *executor* agent in the Agentic Reel Studio (ARS) post-production tail and the **final finisher before full QC**. It receives a Sound-passed, mode-agnostic audio spec (the finished-audio cut) plus the EDL typography source (the on-screen caption / lower-third / end-card text), and authors **one canonical motion conform spec** — the caption reveal timings (one line at a time, one reveal per 8s max, 120ms ease-in-out), the lower-third and super placements (lowercase sans, left-aligned, subtle underline, never all-caps), the subtle-parallax and overlay directives (bounded by the allowed brand token set), the motion-token application map (`120ms ease-in-out`, `zero_bounce`), and the end-card hold (`REINVENTED — build on purpose.` serif over ivory, 1.5s) — every marker bounded inside the declared timeline.

It calls **no generative engine, renders no graphics, burns in no text, and decodes no video frame**. It authors a *motion spec*; in v1.0 the human finishes it into the v3-final.mp4 (Week 4–5 render automation is v1.1). Its effective per-reel cost is **~$0.00**.

## What makes this agent distinctive

- **The third executor agent — zero authorship.** Every motion-spec field is a faithful *transform* (the EDL's caption/lower-third/end-card events → reveal timings + placements + token map), a byte-faithful *passthrough* (the typography text + lineage + timeline), or a computed *verification* (the conform/fidelity/self-check blocks + the firewall + the dual evidence hash). NO net-new creative decision. A re-interpretation of the timeline or the copy is `spec_fidelity_breach`. This is the last domain where an agent could have been tempted to "write a better caption," and deliberately isn't.
- **The 12th defense-in-depth firewall — the TYPOGRAPHY-domain pass.** Motion authors no new copy, but it is the agent that turns written text into PIXELS — so it re-scans every declared caption / lower-third / end-card string one final time before the master reaches full QC. **The last visual-text checkpoint in the pipeline.** Editor's 10th pass scanned committed text as *data*; Sound's 11th scanned the *spoken* transcript; Motion's 12th scans the text at the moment it becomes *picture* — a distinct surface neither prior pass covers. A leak that survives here is burned into the delivered frame, with no post-hoc fix.
- **The fourth contractually mode-blind agent.** It never reads `production_mode`; `mode_blind_confirm.production_mode_read: false` is the machine-checkable proof that Ingest's mode-convergence seam holds **four stages deep** (Edit Director → Editor → Sound → Motion — the TC-01/TC-02 finish-convergence proof). With Motion, the entire post-production tail is proven mode-agnostic end to end.
- **The third fleet agent to carry only two verdicts** — `motion_ready | fail`, NO `revise`. Motion is a fully-deterministic executor (a token is in the allowed set or it isn't; a lower-third is lowercase-sans or it's an all-caps screamer; two reveals are 8s apart or they collide; the end-card is the brand const or it isn't), so there is no subjective finish surface and no third verdict. The soft creative call lives three stages upstream at Edit Director.
- **The strongest brand-policy encoding in the fleet — TWO type-system invariants.** The banned motion tokens (`whip_pan`/`shake`/`meme_transition`/`trending_transition`) are `enum`-excluded and the all-caps lower-third is `all_caps: const false` — a spec that violates either **cannot serialize**. Two §12 AND-of-gate terms are enforced in the type layer, not just the composition.
- **The dual-route SPLIT (D8) — one code larger than Sound, and the split routes to two agents.** `v2_edit_unresolved` (the picture handle → **Sound**) and `text_asset_unresolved` (the typography text → **Editor**) are separate codes routed to two different owners; and `motion_token_out_of_spec` vs `typography_out_of_spec` are separate because the motion domain carries two distinct brand-policy surfaces where audio carried one.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | The verbatim v1.0 system prompt (paste-into-the-LLM contract) + operator guide. |
| `schemas/input.schema.json` | Validates the input (Sound `audio_ready` precondition gate + mode-converged EDL typography source + Sound `v2_edit_uri` finish reference). |
| `schemas/output.schema.json` | Validates the polymorphic output (`successMotionSpec | errorEnvelope`, the 2-verdict model). |
| `test-cases/` | 5 dry-run fixtures (`input.json` + `expected_output.json` + `scenario.md`). |
| `validate.py` | Offline dry-run harness — meta-schema + fixture conformance + adversarial guards + the convergence proof. **$0, no engine, no render, no compositing, no frame decode, no network, no LLM.** |

## Run the validator

```bash
cd motion-agent
python3 validate.py     # exit 0 = all green
```

Requires `jsonschema>=4.26` (Draft 2020-12). The harness is purely structural — it spends nothing. Current status: **111 / 111 checks pass, 0 fail, $0.**

## Test-case portfolio (5 fixtures)

| Case | Verdict | Code | Proves |
|------|---------|------|--------|
| 01 — Mode-A-origin Pro | `motion_ready` | `null` | The full faithful-finish happy path. |
| 02 — Mode-C Enterprise | `motion_ready` | `null` | **The mode-blind finish-convergence proof** — byte-shape-identical finish path to TC-01 despite a different origin mode (four stages deep). |
| 03 — Caption reveal out of range | `fail` | `motion_marker_out_of_range` | A caption reveal over-runs the EDL timeline → route back to Editor to re-place it. |
| 04 — v2-edit unresolved | `fail` | `v2_edit_unresolved` | The audio-final cut handle does not resolve → route back to Sound (SPLIT resolution code — distinct route). |
| 05 — Typography firewall breach | `fail` | `motion_firewall_breach` | **GATING** — the 12th-pass catch on the passthrough on-screen typography, the last visual-text line before the master. |

The slot-11 catch-all (`motion_agent_failed`), the `text_asset_unresolved` SPLIT-to-Editor variant, the `motion_token_out_of_spec` / `typography_out_of_spec` type-layer negatives, the `spec_fidelity_breach` dual-hash-tamper variant, and the deterministic single-assertion halts are exercised schema-only (via `validate.py`) and in the operator-run LLM Test Runbook's adversarial cases, per the fleet's fixture-economy precedent. **Fixture-economy divergence: two brand-policy codes are type-layer-enforced** (their primary test is a schema-negative, not a behavioral run — the banned tokens and the all-caps screamer are unrepresentable).

## Pipeline position & dependencies

```
… → Ingest (#8) → Edit Director (#9) → Editor (#10) → Sound (#11) → Motion (#12) → full QC (#13) → …
```

Motion consumes Sound's `successAudioSpec`/`audio_ready` as an absolute precondition and extends Sound's 10-tuple `parent_chain` to an 11-tuple (held additively, sextuply-deferred — Decision D7). Its v1.0 LOCK is **hard-gated** on all predecessor LOCK ceremonies closing first (AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → Editor → Sound). Agents #1–#10 closed on the Day 79 ceremony; **Sound (#11) is the ONLY open link** (its LOCK is spend-gated on a live 5/5 run of the Day 81 runbook). The handoff target is `qc-agent` (Agent #13, not yet built).

## Status

**v1.0 LOCK CANDIDATE** (Day 86) — SPEC body §0–§16 complete, schemas authored (Day 87), this SKILL bundle authored (Day 89). Agents #1–#10 LOCKED on the Day 79 ceremony (240/240 real validation evidence) and the Cross-SPEC §3.9 n-tuple amendment was ratified. Motion stays at LOCK CANDIDATE until **(a) the Sound v1.0 LOCK closes** (Sound's own gate — a live 5/5 run) **and (b) Motion's own LLM Test Runbook is authored + run 5/5** — there is no 5/5 evidence to lock it on yet, and the harness does not manufacture one. Entity scope: **Sequel Digital only**. Pilot brand: **REINVENTED**.
