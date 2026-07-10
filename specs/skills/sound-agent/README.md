# Sound Agent — v1.0 (ARS Agent #11 of 17)

The **Sound Agent** is the second *executor* agent in the Agentic Reel Studio (ARS) post-production tail. It receives an Editor-passed, mode-agnostic Edit Decision List (the conformed cut) plus the resolved Ingest asset bundle, and authors **one canonical audio conform spec** — the loudness normalization target (`-14 LUFS (IG/TT)` primary, `-1.0 dBTP` true-peak ceiling), the VO polish directives (level, de-ess, breath-trim to the brand voice cadence), the music-bed base level + the ducking envelope under the VO (swell moves mapped byte-position-faithful from the EDL `music_swell_map`), and the SFX accents placed on the EDL's cut/swell markers — every marker bounded inside the declared timeline.

It calls **no generative engine, decodes no waveform, measures no loudness, and runs no audio DSP**. It authors an *audio spec*; in v1.0 the human finishes it into the v2.mp4 (Week 4–5 DSP automation is v1.1). Its effective per-reel cost is **~$0.00**.

## What makes this agent distinctive

- **The second executor agent — zero authorship.** Every audio-spec field is a faithful *transform* (the EDL's music event + swell markers → declared mix directives + duck moves), a byte-faithful *passthrough* (the VO transcript copied for the polish reference), or a computed *verification* (the conform/fidelity checks + firewall + evidence hash). NO net-new creative decision. A re-interpretation of the timeline is `spec_fidelity_breach`.
- **The 11th defense-in-depth firewall — the AUDIO-domain pass.** Sound authors no new copy (Script wrote it, Editor committed it), but it is the agent that FINISHES the spoken audio — so it re-scans every declared `vo_transcript[].text` one final time before the mix reaches Motion. **The last audio checkpoint before typography.** Editor's 10th pass scanned committed caption/lower-third/end-card TEXT; Sound scans the VO TRANSCRIPT — a distinct surface Editor's pass does not cover.
- **The third contractually mode-blind agent.** It never reads `production_mode`; `mode_blind_confirm.production_mode_read: false` is the machine-checkable proof that Ingest's mode-convergence seam holds **three stages deep** (Edit Director → Editor → Sound — the TC-01/TC-02 finish-convergence proof).
- **The second fleet agent to carry only two verdicts** — `audio_ready | fail`, NO `revise`. Sound is a fully-deterministic executor (an asset resolves or it doesn't; a marker is in the timeline or it isn't; the loudness target is the platform const or it isn't), so there is no subjective finish surface to hold to a human, and no third verdict. The soft creative call lives upstream at Edit Director.
- **The namespace SPLIT (D8) — the deliberate opposite of Editor.** `vo_track_missing` (the VO voice track) and `audio_asset_unresolved` (the music bed) are kept as SEPARATE codes because the two Ingest-routed asset gaps demand different operator recovery actions — whereas Editor folded all resolution into one `asset_unresolved`.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | The verbatim v1.0 system prompt (paste-into-the-LLM contract) + operator guide. |
| `schemas/input.schema.json` | Validates the input (Editor `edl_ready` precondition gate + mode-converged EDL + Ingest `asset_bundle` audio-resolution reference). |
| `schemas/output.schema.json` | Validates the polymorphic output (`successAudioSpec | errorEnvelope`, the 2-verdict model). |
| `test-cases/` | 5 dry-run fixtures (`input.json` + `expected_output.json` + `scenario.md`). |
| `validate.py` | Offline dry-run harness — meta-schema + fixture conformance + adversarial guards + the convergence proof. **$0, no engine, no DSP, no decode, no LUFS measurement, no network, no LLM.** |

## Run the validator

```bash
cd sound-agent
python3 validate.py     # exit 0 = all green
```

Requires `jsonschema>=4.26` (Draft 2020-12). The harness is purely structural — it spends nothing. Current status: **83 / 83 checks pass, 0 fail, $0.**

## Test-case portfolio (5 fixtures)

| Case | Verdict | Code | Proves |
|------|---------|------|--------|
| 01 — Mode-A-origin Pro | `audio_ready` | `null` | The full faithful-finish happy path. |
| 02 — Mode-C Enterprise | `audio_ready` | `null` | **The mode-blind finish-convergence proof** — byte-shape-identical finish path to TC-01 despite a different origin mode (three stages deep). |
| 03 — Audio marker out of range | `fail` | `audio_marker_out_of_range` | An SFX/duck marker over-runs the EDL timeline → route back to Editor to re-place it. |
| 04 — VO track missing | `fail` | `vo_track_missing` | The VO voice track does not resolve in the bundle → route back to Ingest (SPLIT resolution code). |
| 05 — Audio firewall breach | `fail` | `audio_firewall_breach` | **GATING** — the 11th-pass catch on the passthrough VO transcript, the last audio line before Motion. |

The slot-11 catch-all (`sound_agent_failed`), the music-bed `audio_asset_unresolved` SPLIT variant, the `spec_fidelity_breach` hash-tamper variant, and the deterministic single-assertion halts are exercised schema-only (via `validate.py`) and in the operator-run LLM Test Runbook's adversarial cases, per the fleet's fixture-economy precedent. **Fixture-economy divergence: there is NO `revise` verdict to exercise** (Sound's two-verdict posture).

## Pipeline position & dependencies

```
… → QC Pre-flight (#7) → Ingest (#8) → Edit Director (#9) → Editor (#10) → Sound (#11) → Motion (#12) → …
```

Sound consumes Editor's `successEdl`/`edl_ready` as an absolute precondition and extends Editor's 9-tuple `parent_chain` to a 10-tuple (held additively, quintuply-deferred — Decision D7). Its v1.0 LOCK is **hard-gated** on all six predecessor LOCK ceremonies closing first (AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → Editor) — those closed on the Day 79 ceremony. The handoff target is `motion-agent` (Agent #12, not yet built).

## Status

**v1.0 LOCK CANDIDATE** (Day 78) — SPEC body §0–§16 complete, schemas authored (Day 79), this SKILL bundle authored (Day 80). The six predecessor agents LOCKED on the Day 79 ceremony (240/240 real validation evidence) and the Cross-SPEC §3.9 n-tuple amendment was ratified. Sound stays at LOCK CANDIDATE until **its own LLM Test Runbook is authored + run 5/5** (the ~Day 83 slot) — there is no 5/5 evidence to lock it on yet, and the harness does not manufacture one. Entity scope: **Sequel Digital only**. Pilot brand: **REINVENTED**.
