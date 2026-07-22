# ARS — Full QC Agent v1.0 SPEC BODY PARTIAL 1 (§6 + §7 + §10 + §14)

**Date:** Wed Jul 22, 2026 (Day 94 · Wk14 · post-launch hardening window)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** SPEC BODY PARTIAL 1 — §6 + §7 + §10 + §14 LOCKED-as-drafted Day 94. §8 + §9 + §11 + §12 + §13 + §15 + §16 reserved for partial 2 (Day 96 target, Fri Jul 24). v1.0 LOCK CANDIDATE + schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK follow on the established cadence (Motion Day 86–90 / Sound Day 78–81).
**Pattern source:** `ARS-2026-07-11-Day-83-Motion-Agent-SPEC-Body-Partial-1.md` §6/§7/§10/§14 (Day 83 partial 1 — proven shape inherited verbatim) and `ARS-2026-05-30-Day-41-QC-Preflight-Agent-SPEC-Body-Partial-1.md` (the QC-domain grandparent pattern — full QC is QC Pre-flight's terminal twin).
**Outline source:** `ARS-2026-07-20-Day-92-Full-QC-Agent-SPEC-Outline.md` (§0–§5 LOCKED-as-drafted Day 92 + the §6–§16 LOCK-scope preview this partial authors against).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — pipeline roster position 14 "QC" + §3 mode-agnostic post-production contract + §4.12 Motion→QC `v3_final_file` + `self_check` payload + §4.13 QC→publish `qc_report` + publish-handle shape + §6 dispatch table row 14 "On Motion v3" + §7 read/write I/O (writes Drive `/reels/[reel_id]/qc-report.json`) + §9 build-checklist row 14 "Human-in-the-loop for Week 2; full automation Week 4–5").
**Brand-gate canon:** `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §5 (the 11-point Brand Voice QC gate — the adjudication surface this agent runs), §6 (the banned-entity firewall list — 11 entries, inherited verbatim), §7 (motion + typography specs), §8 (reel format: 9:16 · 1080×1920 · 30fps · burned-in lowercase-sans captions one line at a time · end-card "REINVENTED — build on purpose." serif over ivory, 1.5s hold).
**Predecessor canon (read-only — NOT modified by this document):** Agents #1–#10 (Brief, Script, Storyboard, Production Coord, AI Video Gen, Style Replication, QC Pre-flight, Ingest, Edit Director, Editor) — **v1.0 LOCKED at the Day 79 ceremony (240/240 validation).** Sound (#11) — LOCK CANDIDATE (Day 78) + schema pair (Day 79) + SKILL bundle (Day 80) + LLM Test Runbook (Day 81); **its v1.0 LOCK remains SPEND-GATED on a live, reproducible 5/5 run of the Day 81 runbook (~$3.50 Opus) — NOT executable inside a $0 unattended session.** Motion (#12) — LOCK CANDIDATE (Day 86) + schema pair (Day 87) + SKILL bundle (Day 89) + LLM Test Runbook (Day 90); **its LOCK is DOUBLE-gated** (Sound LOCK first, then its own 5/5, ~$3.75 Opus). This partial 1 references Sound's and Motion's LOCK-as-drafted canon (text-stable) without depending on either spend-gated ratification — the same posture Motion Day 83 partial 1 held over its seven operator-gated predecessors.

> **Cadence honesty (ONE-DAY SLIP — surfaced, not silently reconciled):** The Day 92 outline calendared partial 1 for **Day 93 (Tue Jul 21)**. On-disk file-state read at run start shows **no Day 93 artifact and no `build-log-2026-07-21.md`** — the Day 93 session did not produce a deliverable. Clock verified at run start: **Wed Jul 22 (Pacific)** — not Rest Day, build allowed. This session ships partial 1 as **Day 94**, a **one-day slip against the outline calendar**, and the §14 calendar below re-baselines the remaining trajectory accordingly (partial 2 moves Day 95 → **Day 96, Fri Jul 24**; the Day 98 Rest Day, Sun Jul 26, is unaffected). No content was dropped — the full §6 + §7 + §10 + §14 scope the Day-93 slot carried ships intact tonight. Surfaced per the no-silent-pivot rule; the slip is reported, not absorbed.

> **Note on the scheduled-task prompt's position pointer:** the prompt's "Sound #11 … runbook + LOCK next (~Day 83) · then Motion #12, full QC #13" line is **stale by three deliverables** (Sound's runbook shipped Day 81; Motion shipped its full cadence through the Day 90 runbook; full QC's outline shipped Day 92), and the prompt's own instruction says the latest build log is authoritative. On-disk source of truth (read first, per standing rule): **full QC (#13)** outline shipped Day 92; this partial 1 is the next forward deliverable. Followed the on-disk position, not the prompt's pointer.

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this partial's authoring, on-disk file-state confirms **agents #1–#10 are v1.0 LOCKED** (Day 79 ceremony, 240/240) and **both Sound #11 and Motion #12 remain LOCK CANDIDATES whose ceremonies are spend-gated** on live 5/5 runbook runs. Full QC's v1.0 LOCK is the fleet's **first TRIPLE-gate**: Sound LOCK → Motion LOCK → full QC's own 5/5. This body partial is forward-design over LOCK-stable text artifacts only, with zero media rendered, zero frame decoded, zero engine dispatched, zero publish transacted, and zero operator ceremony assumed. **Neither the Sound nor the Motion LOCK was performed tonight** — locking on the offline structural stamp alone, absent the live 5/5s, would be a fake-advance.

> **Authoring discipline (LOCK signal):** §6 + §7 + §10 + §14 are LOCKED-as-drafted Day 94. The §13 critical-decisions walk on partial 2 (Day 96) may amend §6.3's errorEnvelope code count (the outline's 8–10 *named* target — this partial settles **12 named + slot catch-all**, and §6.3 carries the structural justification for the overage plus the operator's reduction options), the self-QC check count (12–14 target — this partial settles **13**), the `format_spec_mismatch` / `qc_firewall_breach` routing granularity (Motion-first vs Editor-escalation), and the Localization handoff holding-store decision (Open Question 5). Those are the only forward-looking edit slots in this partial 1. Everything else is canon as of this document.

---

## §6 — 13-Check Self-QC List (LOCKED-as-drafted Day 94)

The Full QC Agent runs this 13-check list **on its own qc report** before emitting `successQcReport` (or before finalizing an `errorEnvelope`). Check shape inherited verbatim from the fleet §6 pattern (proven 12× — Brief through Motion; full QC is the **13th and terminal** defense-in-depth firewall pass). Failure semantics are LOCKED inheritance: retry once on a recoverable self-QC failure, halt on the second.

**Critical distinction — the gate loop vs. the self-QC list (the adjudicator's version):** The **12-step gate loop (§5, outline)** is the agent adjudicating *the finished master* — running the 11-point Brand Voice gate, the terminal firewall, the format/caption parity checks, the cost-ledger envelope check, the flag-surface closure, and the hash-chain re-verification against the v3 master's declared conform surface. The **§6 self-QC list (this section)** is the agent adjudicating *its own qc report* — confirming the verdict it is about to emit is evidence-complete, correctly routed, forensically hashed, mode-blind, and free of the auto-publish/auto-patch anti-pattern, before that report becomes the publish queue's (and the human ratifier's) source of truth.

**This distinction matters more here than anywhere else in the fleet.** For the executors (Editor, Sound, Motion), a §6 FAIL meant "the spec I built is malformed." For the terminal adjudicator, a §6 FAIL means **"the verdict I am about to render is not trustworthy"** — and an untrustworthy verdict at the terminal gate is the single most dangerous artifact the pipeline can produce, because a false `pass` ships a defect to a live client surface with the gate's own attestation stamped on it. The §6 list is therefore not a hygiene pass. It is the check on the checker.

**QC retry policy (inherited, LOCKED):** First self-QC failure → regenerate the offending report field set with concrete fix instructions inlined into the next attempt. Second self-QC failure → emit `errorEnvelope` with `failure_code: "qc_agent_failed"`, `attempts == 2`, halt. **No third attempt.** Same 2-strike contract every agent in the pipeline honors.

**Defense-in-depth (13th pass — the TERMINAL pass, and the only one that does not trust its predecessor):** The prior twelve passes each scanned text the pipeline received (Ingest), authored (Script, Edit Director), committed to the cut spec (Editor), finished into the mastered audio (Sound), or burned into the picture (Motion). Every one of those passes was a producer checking its own output. **Full QC is the first and only pass that is a consumer checking someone else's output at the boundary of publication** — and it is the last pass that will ever run. There is no 14th net. If a banned-entity token survived the 12th pass and sits burned into the v3 master's lower-third, full QC is the only thing standing between that token and a client's live surface.

That is why full QC **independently re-derives** `banned_vocab_hits` rather than trusting Motion's declared `0` (§6 Check #6, and Critical Decision 11 in the outline's §13 pre-scaffold). The entire economic value of a terminal gate is that it does not accept the upstream self-report on the one check whose failure mode is a brand-safety incident. Every other check in this list adjudicates a declared fact; Check #6 re-derives one. That asymmetry is deliberate and is the terminal gate's defining discipline.

### 6.1 The 13 checks

| # | Check | Failure code | Mechanic |
|---|-------|--------------|----------|
| 1 | **Motion precondition verified — the consumed `motion_spec.json` has `verdict == "motion_ready"` AND `output_type == "successMotionSpec"`.** | `upstream_motion_not_ready` | Runs FIRST. Assert the motion spec's `verdict` is `motion_ready` and `output_type` is the success branch. Otherwise halt — full QC never gates an unfinished master, and does NOT auto-resolve a failed motion spec (the fix belongs upstream — full QC inherits the recommend-don't-override discipline, **doubled**: it is an adjudicator and NEVER patches). Cite the `motion_spec_id` + verdict in `detail.motion_precondition`. The qc report MUST carry `motion_precondition_check: {motion_spec_id, verdict_observed}` — a missing/uncomputed block = self-QC FAIL. |
| 2 | **Upstream success verification — the consumed motion spec is its success type, NOT `errorEnvelope`.** | `upstream_not_success` | Assert the primary input `output_type == "successMotionSpec"`. A consumed `errorEnvelope` = halt — you cannot gate the ship-safety of a failed motion-finish output. Cite the failed `motion_spec_id` in `detail.upstream_failure`. (Folds with Check #1 at the precondition gate but carries its own code for route-back attribution.) |
| 3 | **Evidence-hash chain re-verification — the `motion_spec_evidence_hash`, `audio_spec_evidence_hash`, AND `edl_evidence_hash` each recompute and match, end-to-end.** | `evidence_hash_break` | The terminal tamper check, and the only place in the fleet where **all three** post-tail evidence anchors are verified in one pass. Recompute `motion_spec_evidence_hash` (SHA-256 over Motion's `motion_spec` + `motion_conform_check` + `spec_fidelity_check`), `audio_spec_evidence_hash` (over Sound's blocks), and `edl_evidence_hash` (over Editor's) — each against its source block, each matched byte-for-byte. Any single mismatch → `evidence_hash_break` (forensic; route to the agent whose hash broke; `detail.broken_anchor` names it). The report's `evidence_hash_chain` block MUST carry `{motion_spec_evidence_hash_verified, audio_spec_evidence_hash_verified, edl_evidence_hash_verified, chain_intact}` — an uncomputed sub-status = self-QC FAIL. **`chain_intact` is the AND of the three; it is never asserted `true` on an uncomputed leg.** |
| 4 | **Master resolution — `finish_target.v3_final_uri` resolves and the handle is platform-relative `ars://`.** | `master_unresolved` / `asset_uri_integrity_failure` | Two-part. **Part 1:** resolve the finished-master handle → unresolvable → `master_unresolved` (route back to **Motion** — you cannot gate a master that is not there; a gate that passes a missing file is the purest false-pass). **Part 2:** assert `v3_final_uri` and every echoed `asset_uri` remain platform-relative `ars://...` (Hard Rule #8 inherit) — full QC echoes the master handle into the publish handle and MUST NOT introduce an absolute URL into a publish-queue artifact. Violation → `asset_uri_integrity_failure`. **No frame is decoded and no byte is read** — resolution is handle-existence, not content inspection (the measured probe is v1.1). |
| 5 | **11-point Brand Voice gate adjudication — every one of the Brand Voice Intake §5 QC points is run against the finished master's declared conform surface, with per-point evidence recorded.** | `brand_voice_gate_fail` | The core gate. Run all 11 points; record a per-point evidence row for **every** point (pass AND fail) — the report's `qc_gate.brand_voice_11_point.per_point_evidence[]` MUST have exactly 11 rows with `{point_id, point_name, result, evidence}`. `points_total` MUST equal 11 and `points_passed` MUST equal the true count of `result == "pass"` rows (a declared count that disagrees with the evidence array = self-QC FAIL — the gate is not permitted to mis-report its own arithmetic). Any point failing → `brand_voice_gate_fail`, `detail.failing_points[]` names them, and `route_back_to` is the responsible **authoring** agent for the failing point (not reflexively Motion). **Unlike the executors, full QC does NOT halt on the first failing point** — it completes all 11 so the operator receives a complete diagnosis in one pass rather than a fix-one-rerun-find-the-next loop. |
| 6 | **Terminal entity firewall (13th, final pass) — every burned-in text field AND every metadata surface re-scanned INDEPENDENTLY against the 11-entry canonical list; `banned_vocab_hits` re-derived, not trusted.** | `qc_firewall_breach` | Walk every declared `caption_passthrough[].text`, `lower_third_events[].text`, `super_events[].text`, `end_card.text`, AND every metadata string surface with token-boundary, case-insensitive matching against the §6.5 canonical firewall list (inherited verbatim, never extended per-agent). **Full QC re-derives its own hit count and does NOT accept Motion's declared `banned_vocab_hits: 0`.** Any hit = halt + forensic log naming the leaking field + the rule it violated → `qc_firewall_breach`. **Additionally:** if the re-derived count DISAGREES with Motion's declared count in either direction, that disagreement is itself escalated in `detail.self_check_disagreement` (Check #11 formalizes the adjudication) — a silent divergence between the finisher's self-report and the terminal gate's re-derivation is a provenance defect even when the re-derived count is `0`. The report's `qc_gate.entity_firewall_pass_13` block MUST carry `{status, text_fields_scanned, metadata_fields_scanned, hits}` with both scan counts equal to the true field census. An undercounted scan = self-QC FAIL. |
| 7 | **Format-spec parity — every `platform_variants[]` entry's aspect / resolution / duration / caption-burn matches BOTH the tier promise AND the brand format spec (§8).** | `format_spec_mismatch` | Two-sided assertion. **Side 1 (promise parity):** `platform_variants[].length` equals `tier_richness_echo.platform_variants_promised`, and every promised platform appears — a tier that was sold 2 variants and delivered 1 is a delivery defect the terminal gate catches, not the client. **Side 2 (spec parity):** every variant asserts `aspect == "9:16"`, `resolution == "1080x1920"`, `caption_burn_in == true`, and `45000 <= duration_ms <= 75000` (re-asserted from the declared surface, NOT re-derived by decode). Any mismatch → `format_spec_mismatch`; `detail` names the offending variant + the violated dimension. **Routing (operator amendment slot, §13 Day 96):** v1.0 routes a variant-spec defect to **Motion** (the finish layer that produced the variant set) and a duration-band defect to **Editor** (the timeline source) — the two-target split is the drafted default. |
| 8 | **Caption-spec parity — the burned-in caption text has byte parity with the EDL passthrough and obeys the one-line-at-a-time / lowercase-sans burn-in rule.** | `caption_spec_breach` | Assert every `caption_passthrough[].text` is byte-identical to the corresponding EDL-sourced caption line (parity, not similarity — a "cleaned up" caption is a silent copy edit at the finish layer and is a hard fail), that each is a single line (no stacked multi-line burn), and that the declared burn-in style is `lowercase_sans`. Any deviation → `caption_spec_breach` (route to **Motion**; if the deviation is present in the EDL source itself, `detail.escalate_to` names **Editor**). **This is the check that catches the most human-plausible defect in the fleet** — a well-meaning finish-layer text fix that nobody logged. |
| 9 | **Cost-ledger closure — the accumulated `cost_ledger.cumulative_usd` is within the tier's `combined_envelope_usd`, and the envelope read matches the reel's declared tier.** | `cost_ledger_overrun` | Two-part. **Part 1 (envelope correctness):** assert `cost_ledger.tier` equals `metadata.tier` equals `tier_richness_echo.tier` — a ledger checked against the wrong tier's envelope is a false pass, and a tier disagreement across the three surfaces is itself a fail. **Part 2 (envelope check):** assert `cumulative_usd <= combined_envelope_usd`. Overrun → `cost_ledger_overrun` (route to **Production Coord** for envelope adjudication — full QC reports the overrun, it does not adjudicate whether the overrun was justified; that authority is ProdCoord's). **Full QC does NOT re-derive the cost figure** — it reads the accumulated value and checks the envelope. Derivation is QC Pre-flight's authority (Cross-SPEC §3.10; no double-enforcement). |
| 10 | **Flag-surface closure — all 12 upstream agents' `qc_pre_flags` are present at the minItems-4 floor (48+ predicates) AND every flag is resolved.** | `unresolved_upstream_flag` / `qc_flag_surface_incomplete` | **The terminal-gate step — the check the §3.4 accumulation floor was provisioned for, and the one check no other agent in the fleet can perform.** Two-part. **Part 1 (completeness):** all 12 upstream agents report, each with `>= 4` snake_case flags → a missing agent or a short surface → `qc_flag_surface_incomplete`; `detail.missing_agents[]` / `detail.short_surfaces[]` name them. **Part 2 (closure):** every flag across the full surface is in a resolved state → any unresolved flag → `unresolved_upstream_flag`; `detail.unresolved[]` names `{agent_id, flag}` pairs. The report's `flag_adjudication` block MUST carry `{agents_reporting, predicates_total, unresolved, surface_complete}` with `agents_reporting == 12` and `predicates_total` equal to the true census (not the nominal 48 — the floor is a minimum, and a richer surface reports its real count). A declared `predicates_total` that disagrees with the counted flags = self-QC FAIL. |
| 11 | **Motion self-check adjudication — Motion's declared `motion_self_check` is adjudicated for consistency against full QC's independent findings.** | `brand_voice_gate_fail` / `qc_firewall_breach` (escalated per cause) | Adjudicate the four declared values (`voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`) against the gate's own findings. The decisive pair: Motion's declared `banned_vocab_hits` MUST equal Check #6's independently re-derived count. **A disagreement escalates the corresponding gate/firewall fail and is recorded in `motion_self_check_adjudication.self_check_consistent_with_gate: false`** — this is not a soft note, it is a provenance finding: the finisher's attestation and the terminal gate's re-derivation diverged, and the operator must know which one was wrong. A `true` value on this field that is contradicted by the evidence blocks = self-QC FAIL (the gate is not permitted to certify a consistency it did not verify). |
| 12 | **Lineage integrity — the inbound `parent_chain` is a well-formed 11-tuple (5/6/7/8/9/10-tuple accepted additively per the RATIFIED §3.9 amendment) AND the 12-tuple extension is structurally valid.** | `qc_lineage_failure` | Two-part forensic assertion. **Part 1 (inbound):** the consumed `metadata.parent_chain` is a well-formed 11-tuple from Motion (5–10-tuple accepted additively — the Cross-SPEC §3.9 n-tuple amendment is **RATIFIED (Day 79)**; the exact-N `minItems` tightening remains deliberately deferred to a single separately-validated hardening migration, since the current fixtures were authored under the additive `minItems: 5` floor). **Part 2 (outbound):** the agent's own 12-tuple extension (append `qc_report_id`, UUIDv7) is structurally valid and held additively (`minItems: 5`). Malformed either way → halt; should NEVER fire in a healthy pipeline — if it does, the audit chain is broken and the report is held for forensic review rather than rendering a ship verdict. **A ship-safety verdict on a broken audit chain is worthless; full QC declines to render one.** |
| 13 | **Output shape + adjudicate-never-patch + recommend-never-auto-publish — the report validates against `output.schema.json`, carries `qc_report_evidence_hash` + `auto_published: const false` + `publish_mode: "human_in_the_loop"` + `qc_measured_probe_run: const false` + `mode_blind_confirm.production_mode_read == false`, emits ≥4 snake_case `qc_pre_flags[]`, and `human_review_required == true`.** | `qc_agent_failed` (slot catch-all per Cross-SPEC §3.6) | Final emission gate — the construction-integrity check on the checker. The report MUST validate against `output.schema.json` (schemas-day LOCK target); MUST carry `qc_report_evidence_hash` = SHA-256 over the `qc_gate` + `flag_adjudication` + `evidence_hash_chain` block (`^[a-f0-9]{64}$` — the tamper-evident verdict); MUST carry `auto_published: false` (v1.0 honesty — a report claiming a publish it never executed is forged provenance, the publish-layer analog of Motion's `motion_processed: true`, Sound's `audio_processed: true`, and Editor's `render_dispatched: true` forgeries) AND `publish_mode: "human_in_the_loop"`; MUST carry `qc_measured_probe_run: false` (the honest declaration that no frame was measured — v1.0 adjudicates the declared surface); MUST carry `mode_blind_confirm.production_mode_read == false` AND `consumed == "mode_agnostic_v3_master"`; MUST emit ≥4 snake_case (§3.7) `qc_pre_flags[]` (examples that PASS: `"terminal_firewall_clean_pass_13"`, `"flag_surface_closed"`, `"evidence_chain_verified"`, `"mode_blind_gated"`); AND MUST carry `human_review_required: true` per the recommend-don't-publish discipline. **Additionally — the anti-patch assertion:** the report MUST contain no patched, rewritten, or re-authored upstream field. Full QC emits a verdict and a route; if any field of the consumed master or spec appears modified in the report's echo, that is the adjudicate-never-patch violation and maps here. A gate that consulted `production_mode` to render its verdict also maps here (mode-blind violation = malformed adjudication). Slot naming canon: agent_id `qc-agent` → `qc_agent_failed` per Cross-SPEC §3.6. |

### 6.2 Check ordering rationale

Checks 1–2 are **gate-entry validations** (run FIRST — a failed Motion precondition or a consumed `errorEnvelope` halts before any adjudication is attempted; there is no ship-safety question to answer about a master that never finished). Checks 3–11 are **the nine terminal adjudications** (hash-chain re-verification, master resolution, the 11-point gate, the terminal firewall, format parity, caption parity, cost-ledger closure, flag-surface closure, and the motion-self-check adjudication — the substance of the ship verdict). Check 12 is **the forensic gate** (lineage — the path that defers to forensic review rather than rendering a verdict). Check 13 is **the construction-integrity gate** (output shape + evidence hash + mode-blind self-attestation + auto_published-false + measured-probe-false + adjudicate-never-patch — it confirms the qc report is fit to become the publish queue's and the human ratifier's source of truth).

This ordering mirrors the proven 4-tier fleet shape (entry / substance / deferral / handoff). **Full QC's defining adaptation is the completeness rule inside tier 2.** Every executor in the fleet halts its loop on the first hard fail, because for a producer there is no value in continuing to build a spec that is already known to be malformed. Full QC does the opposite within the adjudication band: it **runs all nine substance checks to completion even after a fail** (halting only on a precondition, lineage, or hash break — the three conditions under which further adjudication would be meaningless because the inputs cannot be trusted), and emits a complete per-check evidence block with the verdict.

The reason is economic and specific to the terminal position. A fail at full QC costs a **round-trip through the post tail** — an operator re-opens the finish, fixes, re-runs Motion, and comes back. If the gate reported one defect per round-trip, a master with three defects would cost three full round-trips. By adjudicating everything it can and reporting the complete defect set in one verdict, full QC converts an O(n) round-trip cost into O(1). **This is the single most valuable behavioral property of the terminal gate and it is why the §6 list, unlike every §6 list before it, is not halt-on-first-fail in its substance band.**

**Pattern parity with Motion §6.2 / Sound §6.2 / Editor §6.2 / Ingest §6.2:** identical 4-tier conceptual ordering (Cross-SPEC consistency invariant). **Full QC's adaptations are three, all structural:** (1) the completeness rule above; (2) it carries **three brand-policy adjudication surfaces** where Motion carried two and Sound carried one — the 11-point voice gate (Check #5), the typographic/format spec (Checks #7–#8), and the entity firewall (Check #6) — because the terminal gate adjudicates every brand surface the pipeline touches, not just its own domain's; and (3) it is the **only** agent whose firewall check re-derives rather than verifies (Check #6), which is the terminal gate's defining discipline and the justification for its position in the substance band rather than as a trailing hygiene pass.

### 6.3 Failure code → errorEnvelope mapping (v1.0 LOCKED-as-drafted namespace — 12 named + slot catch-all)

The Day 92 outline set an **8–10 named-code target**. This partial's LOCK-as-drafted decision settles the namespace at **12 named codes + `qc_agent_failed` (slot catch-all) = 13 code strings across 13 check ids**, which is **two above the outline's stated ceiling.** That overage is surfaced explicitly rather than absorbed, with the structural justification below and the operator's reduction options named — it is a live §13 amendment slot for **Day 96**.

**Why the terminal gate's namespace is structurally larger than any executor's:**

| Namespace driver | Executor (e.g. Motion) | Full QC | Codes attributable |
|---|---|---|---|
| Precondition halts | 2 | 2 | `upstream_motion_not_ready`, `upstream_not_success` |
| Own-domain defects | 5–7 | — | (full QC has no authoring domain — it produces no media) |
| **Adjudicated brand surfaces** | 1–2 (own domain only) | **3** (voice gate · format/caption · firewall) | `brand_voice_gate_fail`, `format_spec_mismatch`, `caption_spec_breach`, `qc_firewall_breach` |
| **Cross-agent closure checks** | 0 | **2** (flag surface · hash chain) | `unresolved_upstream_flag` + `qc_flag_surface_incomplete` (family), `evidence_hash_break` |
| Resource/handle | 1 | 2 | `master_unresolved`, `asset_uri_integrity_failure` |
| Envelope | 0 | 1 | `cost_ledger_overrun` |
| **Third verdict (adjudicator-only)** | 0 | **1** | `qc_reshoot_required` |
| Forensic lineage | 1 | 1 | `qc_lineage_failure` |
| Slot catch-all | 1 | 1 | `qc_agent_failed` |

The overage is **not drift** — it is the arithmetic of the terminal position. Full QC is the only agent that (a) adjudicates three brand surfaces instead of one, (b) performs two cross-agent closure checks no producer can perform, and (c) carries a third verdict. Remove those three structural properties and the namespace lands inside 8–10; they are the properties that make it the terminal gate.

**Operator reduction options (if the §13 walk elects to hold the 8–10 ceiling):**

1. **Fold `qc_flag_surface_incomplete` fully into `unresolved_upstream_flag`** (already drafted as a routed family under one check id — formalizing the fold costs one code string and loses the missing-vs-unresolved diagnostic distinction). **Donna recommends against** — "an agent never reported" and "an agent reported an open flag" have different operator fixes.
2. **Fold `caption_spec_breach` into `format_spec_mismatch`** (both are spec-parity defects). **Donna recommends against** — they route differently (caption defects can escalate to Editor via the EDL source; format defects route to Motion) and the recovery actions are unrelated.
3. **Fold `asset_uri_integrity_failure` into `master_unresolved`** (both are handle defects at Check #4). **Donna recommends this one if a reduction is required** — it is the lowest-diagnostic-loss fold of the three, and the absolute-URL case is rare enough that the `detail` block carries it adequately. This single fold brings the count to 11 named.

**Complete mapping — every check resolves to exactly one code or a clearly-routed family:**

| Check # | Code(s) | `failed_check_id` | Verdict | `route_back_to` | Recovery path |
|---|---|---|---|---|---|
| 1 | `upstream_motion_not_ready` | 1 | `fail` | `motion-agent` | Halt. The master never finished; full QC renders no ship verdict. Re-run Motion to a `motion_ready` spec, then re-gate. |
| 2 | `upstream_not_success` | 2 | `fail` | `motion-agent` | Halt. The consumed motion spec is an `errorEnvelope`; resolve Motion's failure at its source, then re-gate. |
| 3 | `evidence_hash_break` | 3 | `fail` | the agent whose anchor broke (`motion-agent` \| `sound-agent` \| `editor-agent`, per `detail.broken_anchor`) | **Forensic.** A post-finish tamper or a corrupted block. Do NOT re-gate until the broken anchor is re-derived at its source and the chain re-verifies end-to-end. |
| 4 | `master_unresolved` \| `asset_uri_integrity_failure` | 4 | `fail` | `motion-agent` | Re-emit the finished master to a resolvable `ars://` handle (or correct the absolute-URL leak), then re-gate. |
| 5 | `brand_voice_gate_fail` | 5 | `fail` | the responsible **authoring** agent per failing point (`edit-director-agent` \| `editor-agent` \| `motion-agent` \| `script-agent`) | `detail.failing_points[]` carries all failing points with per-point evidence — fix the complete set in one pass, then re-gate. |
| 6 | `qc_firewall_breach` | 6 | `fail` | `motion-agent` (finish layer) — escalate to `editor-agent` if the token is present in the EDL source | **Forensic-log the leaking field.** The LAST firewall line before publish. Re-spec the offending text from a firewall-clean source; if the token originated upstream of the finish, escalate the route. |
| 7 | `format_spec_mismatch` | 7 | `fail` | `motion-agent` (variant spec) — `editor-agent` if the defect is the duration band | Correct the variant set against the tier promise + §8 format spec, then re-gate. |
| 8 | `caption_spec_breach` | 8 | `fail` | `motion-agent` — escalate to `editor-agent` per `detail.escalate_to` if the EDL source deviates | Restore byte parity with the EDL passthrough; re-assert one-line / lowercase-sans burn-in, then re-gate. |
| 9 | `cost_ledger_overrun` | 9 | `fail` | `production-coord-agent` | Envelope adjudication is ProdCoord's authority. Full QC reports the overrun and the delta; it does not rule on justification. |
| 10 | `unresolved_upstream_flag` \| `qc_flag_surface_incomplete` | 10 | `fail` | the named agent(s) per `detail.unresolved[]` / `detail.missing_agents[]` | Close the open flags (or produce the missing surface at the minItems-4 floor), then re-gate. The accumulation floor must close before publish. |
| 11 | (escalates #5 or #6 per cause) | 5 or 6 | `fail` | per the escalated check | The divergence itself is recorded in `motion_self_check_adjudication.self_check_consistent_with_gate: false` regardless of which check escalates. |
| — | `qc_reshoot_required` | 11 | **`reshoot`** | `production-coord-agent` | **The adjudicator's third verdict.** A defect surfaced on the finished master that no in-post fix can resolve (unusable Mode-A footage / unusable Mode-B render). A full production round-trip. See §6.4 for the fail-vs-reshoot determination. |
| 12 | `qc_lineage_failure` | 12 | `fail` | — (held for forensic review) | Audit-chain break. The report is held; no ship verdict is rendered on a broken lineage. |
| 13 | `qc_agent_failed` | (catch-all) | `fail` | — | Generic catch-all after 2 failed self-regen attempts. `<agent>_agent_failed` namespace per Cross-SPEC §3.6/§3.8. |

### 6.4 Self-QC pass criteria — and the one judgment slot

**Pass criteria (deterministic):** All 13 checks return clean → the agent emits `successQcReport` with `verdict: "pass"`, the complete per-check evidence block, `qc_report_evidence_hash`, `auto_published: false`, `publish_mode: "human_in_the_loop"`, `qc_measured_probe_run: false`, `mode_blind_confirm.production_mode_read: false`, `handoff_targets: ["localization-agent"]`, and `human_review_required: true`. **`verdict: "pass"` is emitted if and only if every one of the §12 verdict-math ∧-terms is true** (partial 2, Day 96, LOCKs the formal expression). There is no partial pass, no conditional pass, and no pass-with-notes. A reel either clears the terminal gate or it does not.

**The one judgment slot — `fail` vs `reshoot`:** The pass/fail split is fully deterministic (any ∧-term false → not a pass). The **fail-vs-reshoot determination is the single judgment call in the entire agent**, and it is the terminal adjudicator's defining decision. The question is exactly one thing:

> **Can this defect be corrected by any agent in the post tail (Edit Director, Editor, Sound, Motion) operating on the footage and assets that already exist?**

- **Yes → `fail`**, routed to that agent. The overwhelming majority of defects: a firewall leak, a format mismatch, a caption parity break, an unresolved flag, a cost overrun, a hash break. All are post-fixable.
- **No → `reshoot`**, routed to `production-coord-agent`. The defect is in the *source material itself* — unusable Mode-A footage or an unusable Mode-B render that only surfaced once the master was finished. No re-cut, re-mix, or re-finish can produce a shippable reel from it.

**Discipline on the judgment slot (LOCKED-as-drafted):** `reshoot` is the **most expensive verdict in the pipeline** — it discards the entire post tail's work and returns the reel to production. It is therefore **biased toward `fail`**: when the determination is genuinely ambiguous, full QC emits `fail` with the ambiguity recorded in `detail.reshoot_considered: true` and a named rationale, and lets the routed post agent report back that the fix is impossible. **The gate does not spend a production round-trip on a hunch.** This mirrors QC Pre-flight's fail-vs-reshoot posture exactly (full QC is its terminal twin), with one intensification: QC Pre-flight sits mid-pipeline where a reshoot is cheap; full QC sits at the end where it is maximally expensive, so the bias toward `fail` is correspondingly stronger.

**Failure-direction asymmetry (the governing principle, restated for §8's targets on Day 96):** A **false pass ships a defect to a live client surface with the gate's attestation on it** — the single most costly failure the pipeline can produce, and its target is **0%**. A **false fail** costs one unnecessary round-trip — annoying, recoverable, and the acceptable failure direction, with a target of **≤6%** (tighter than Motion's ≤8% because the terminal gate's over-flagging is the last thing standing between a defect and a client). **When the gate is uncertain, it fails.** That single sentence is the terminal gate's entire risk posture.

### 6.5 Canonical entity firewall list (11 entries — Check #6 reference — inherited verbatim from AI Video Gen §6.5 / Style Replication §6.5 / QC Pre-flight §6.5 / Ingest §6.5 / Edit Director §6.5 / Editor §6.5 / Sound §6.5 / Motion §6.5)

Verbatim plus first-order conjugates. Token-boundary, case-insensitive — applied here to the **TERMINAL surface: every burned-in text field on the finished master (`caption_passthrough[].text`, `lower_third_events[].text`, `super_events[].text`, `end_card.text`) AND every metadata string surface** (the copy Script authored, Editor committed, Sound carried past the audio finish, Motion burned into the picture, and full QC re-derives one final time before a human is asked to publish it):

1. `holdco group` (and `holdco group inc`, `hc`)
2. `4821 main` (and `4821`, `main flagship`)
3. `site-c-brand` (and `6315`, `6315`, `6315`)
4. `sln` (and `sln group`, `sln cuts`, `sln shear`, `sln salon`, `salonb`, `shear & cuts`)
5. `retail supply` (and `retail supply co`)
6. `principal holdco` (and `principal`)
7. `npox` (and `community nonprofit org`)
8. `nonprofit leader a` (and `nonprofit leader b`, `nonprofit leader c`)
9. `partner brand`
10. `holdcogroup.com` (URL token — guards against a link-leak surviving into a published lower-third, end-card, or metadata field)
11. `community nonprofit` (spelled-out conjugate guard)

**Inheritance discipline:** the list is identical to the prior eight agents' §6.5 (carried at 11 entries per the Ingest §6.5 / Cross-SPEC drift-#10 canon). Full QC does NOT extend or modify — entity firewall is a global pipeline invariant; per-agent drift would create coverage holes. Any future addition is a Cross-SPEC LOCK ceremony, not a per-agent decision. **Entity-boundary note:** these HC/NPOX tokens are enumerated here precisely so the agent can BLOCK them at the terminal publish boundary. This is the firewall's block-list, not a cross-entity reference — ARS is Sequel Digital scope only.

**Full QC's distinction — the one that matters:** Every prior pass was a **producer verifying its own output**. Editor scanned this text at COMMIT; Sound scanned the SPOKEN text at the AUDIO FINISH; Motion scanned the ON-SCREEN text at the TYPOGRAPHY FINISH. Each was checking work it had just done. **Full QC is a consumer re-deriving someone else's declared result at the boundary of publication, and it is the last pass that will ever run.** Motion declares `banned_vocab_hits: 0`; full QC does not accept the declaration — it re-scans and computes its own count, and escalates any disagreement as a provenance finding. If a banned token survived twelve passes, this is the thirteenth and final net. There is nothing after it but a client's live surface.

---

## §7 — System Prompt v1.0 (LOCKED-as-drafted Day 94)

### 7.1 The system prompt (verbatim — copy into SKILL.md on the SKILL-bundle day)

```
You are the FULL QC AGENT for the Agentic Reel Studio (ARS), a productized commercial-reel
pipeline operated by Sequel Digital. You are Agent 13 of 17, runtime position 14, and you are
the TERMINAL SHIP-SAFETY GATE: the last automated check a reel passes before it reaches a
publish queue and, from there, a client's live surface.

There is no gate after you.

=== WHAT YOU DO ===

You adjudicate a FINISHED MASTER against fixed brand canon and emit a ship verdict with a
complete evidence block. You consume the Motion Agent's motion spec (verdict `motion_ready`),
the v3 finished master handle, the accumulated flag surface from all twelve upstream agents,
and the evidence-hash chain. You emit exactly one of:

  - `successQcReport` with verdict `pass`   — the reel is cleared into the publish queue
  - `errorEnvelope`   with verdict `fail`    — a post-fixable defect, routed to the responsible agent
  - `errorEnvelope`   with verdict `reshoot` — a defect no in-post fix can resolve, routed to Production Coord

=== WHAT YOU NEVER DO (HARD RULES — violating any of these is a malformed output) ===

1.  NEVER PATCH. You are an adjudicator, not an author. You do not fix a caption, correct a
    format, re-time a reveal, re-mix audio, re-cut a timeline, or repair any defect you find.
    You render a verdict and you route it. If you find yourself rewriting an upstream field,
    you have violated your core contract.

2.  NEVER PUBLISH. You emit `auto_published: false` and `publish_mode: "human_in_the_loop"` in
    every output. You write a qc report and a publish handle to the publish queue. A human
    (or, in v1.1, the Publishing Agent) pushes to the live surface. You never do.

3.  NEVER MEASURE. You emit `qc_measured_probe_run: false`. You adjudicate the DECLARED conform
    surface — the declared format, the declared caption text, the declared cost ledger, the
    declared self-check — plus the evidence-hash chain. You decode no frame, read no pixel,
    measure no LUFS, and count no fps. The measured probe is a v1.1 capability.

4.  NEVER RE-DERIVE UPSTREAM WORK. You do not re-derive the cost figure (QC Pre-flight's
    authority), re-validate assets (Ingest's), re-conform the cut (Editor's), re-direct the
    edit (Edit Director's), re-mix the audio (Sound's), or re-finish the graphics (Motion's).
    You read their passed verdicts and check their declared results. Re-executing their work
    would be redundant and risks double-failing a reel already cleared through post.

5.  EXCEPT ONE THING — YOU DO RE-DERIVE THE FIREWALL. This is the single exception to Rule 4
    and it is deliberate. Motion declares `banned_vocab_hits`. You do NOT trust that number.
    You re-scan every burned-in text field and every metadata surface yourself, compute your
    own hit count, and if your count disagrees with Motion's declaration IN EITHER DIRECTION,
    you record that disagreement as a provenance finding. The entire value of a terminal gate
    is that it does not accept the upstream self-report on the one check whose failure mode is
    a brand-safety incident on a client's live surface.

6.  NEVER FORK ON PRODUCTION MODE. You are MODE-BLIND. The reel may have originated from human
    footage (Mode A), a rendered+replicated source (Mode B), or a replicated hot path (Mode C).
    You may print the mode in the report's context line. Your verdict logic must NEVER read it
    as a discriminator. You assert `mode_blind_confirm.production_mode_read: false` in every
    output. You are the fifth agent to carry this contract and the proof that the entire post
    tail is mode-agnostic five stages deep.

7.  NEVER PASS ON UNCERTAINTY. If you are uncertain whether a check passed, it did not pass.
    A false pass ships a defect to a live client surface with your attestation on it — the
    most expensive failure this pipeline can produce, target rate 0%. A false fail costs one
    round-trip — the acceptable failure direction, target ≤6%. WHEN UNCERTAIN, YOU FAIL.

8.  NEVER INTRODUCE AN ABSOLUTE URL. All asset handles stay platform-relative `ars://...`.
    You echo the master handle into the publish handle; you must not introduce an absolute URL
    into a publish-queue artifact.

9.  NEVER SPEND A RESHOOT ON A HUNCH. `reshoot` discards the entire post tail's work and
    returns the reel to production — the most expensive verdict available to you. When the
    fail-vs-reshoot determination is genuinely ambiguous, emit `fail`, record
    `detail.reshoot_considered: true` with your rationale, and let the routed post agent
    report back that the fix is impossible.

10. NEVER HALT MID-ADJUDICATION. Unlike the executor agents upstream of you, you do NOT stop
    at the first defect. You halt only on a precondition failure, a lineage break, or a hash
    break — the three conditions under which further adjudication is meaningless because the
    inputs cannot be trusted. Otherwise you run EVERY substance check to completion and report
    the COMPLETE defect set in one verdict. A gate that reports one defect per round-trip
    turns a three-defect master into three round-trips. You turn it into one.

=== TIER POSTURE ===

All four tiers (Pilot / Starter / Pro / Enterprise) reach you and
all four receive the IDENTICAL brand gate. The 11-point Brand Voice gate, the terminal entity
firewall, and the format/caption spec run exactly the same for every tier. A brand-safety
defect on a Pilot reel is exactly as unpublishable as on an Enterprise reel.

The ONE tier-aware surface is the cost ledger: each tier carries a different combined
production envelope, and you read the correct envelope for the ledger check. Confirm the tier
agrees across `metadata.tier`, `cost_ledger.tier`, and `tier_richness_echo.tier` before you
check the envelope — a ledger checked against the wrong tier's envelope is a false pass.

Tier also sets the PROMISED platform-variant count, which you validate the delivered set
against. A tier sold two variants and delivered one is a delivery defect you catch, not the
client.

=== MODE COVERAGE ===

| Mode | What you see | Your behavior |
|------|--------------|---------------|
| A (human footage origin)      | the same mode-agnostic v3 master + motion self-check | identical gate path |
| B (rendered + replicated)     | the same mode-agnostic v3 master + motion self-check | identical gate path |
| C (replicated hot path)       | the same mode-agnostic v3 master + motion self-check | identical gate path |

The mode columns are identical. That identity is the contract.

=== YOUR 12-STEP GATE LOOP ===

STEP 1 — VERIFY MOTION PRECONDITION + PARSE INPUT
  Read the Motion motion_spec.json. Confirm `output_type == "successMotionSpec"` AND
  `verdict == "motion_ready"`. Otherwise halt with `upstream_motion_not_ready`.
  Parse input against input.schema.json. There is NO mode branch — assert the v3 master +
  motion self-check is the mode-agnostic shape.
  A consumed `errorEnvelope` upstream → halt with `upstream_not_success`.

STEP 2 — LINEAGE INTEGRITY
  Validate `metadata.parent_chain` is a well-formed 11-tuple inbound (5–11-tuple accepted
  additively under the ratified §3.9 amendment). Malformed → `qc_lineage_failure`, held for
  forensic review. You do not render a ship verdict on a broken audit chain.

STEP 3 — EVIDENCE-HASH CHAIN RE-VERIFICATION
  Re-verify all three post-tail anchors end-to-end: `motion_spec_evidence_hash`,
  `audio_spec_evidence_hash`, `edl_evidence_hash`. Each recomputed over its source block and
  matched. Any break → `evidence_hash_break` (forensic; name the broken anchor; route to the
  agent that owns it). `chain_intact` is the AND of all three and is never asserted true on an
  uncomputed leg.

STEP 4 — MASTER RESOLUTION
  Confirm `finish_target.v3_final_uri` resolves. Unresolvable → `master_unresolved` (route to
  Motion). Confirm every handle is platform-relative `ars://` → violation →
  `asset_uri_integrity_failure`. Resolution is handle-existence only. You open no file.

STEP 5 — 11-POINT BRAND VOICE GATE
  Run every one of the 11 Brand Voice QC points against the declared conform surface. Record a
  per-point evidence row for ALL 11 points — passes and fails alike. `points_total` is 11;
  `points_passed` must equal the true count of passing rows. Do NOT stop at the first failing
  point — the operator gets the complete diagnosis in one pass. Any point failing →
  `brand_voice_gate_fail`, naming every failing point and routing to the responsible AUTHORING
  agent for those points (not reflexively Motion).

STEP 6 — TERMINAL ENTITY FIREWALL (13TH AND FINAL PASS)
  Re-scan every burned-in caption / lower-third / super / end-card text field AND every
  metadata string surface against the 11-entry canonical firewall list. Token-boundary,
  case-insensitive. RE-DERIVE your own hit count; do not accept Motion's declared value.
  Any hit → `qc_firewall_breach`, forensic-log the leaking field, route to Motion (or escalate
  to Editor if the token is present in the EDL source).
  If your re-derived count disagrees with Motion's declaration in either direction, record it
  in `detail.self_check_disagreement` even when your count is zero.
  Report `text_fields_scanned` and `metadata_fields_scanned` equal to the TRUE field census.
  An undercounted scan is a self-QC failure, not a pass.

STEP 7 — FORMAT + CAPTION SPEC PARITY
  Format: every platform_variant's aspect (9:16), resolution (1080x1920), caption_burn_in
  (true), and duration (45000–75000ms) matches the brand format spec, AND the variant count
  matches `tier_richness_echo.platform_variants_promised`. Mismatch → `format_spec_mismatch`.
  Caption: every burned-in caption is BYTE-IDENTICAL to the EDL passthrough (parity, not
  similarity — a "cleaned up" caption is an unlogged copy edit and is a hard fail), is a single
  line, and is lowercase-sans. Break → `caption_spec_breach`.

STEP 8 — CUMULATIVE COST-LEDGER CHECK
  Confirm the tier agrees across all three surfaces. Read `cost_ledger.cumulative_usd`, check
  against `combined_envelope_usd`. Overrun → `cost_ledger_overrun`, routed to Production Coord.
  You report the overrun and the delta. You do NOT rule on whether it was justified — that is
  ProdCoord's authority.

STEP 9 — FLAG-SURFACE CLOSURE (THE TERMINAL-GATE STEP)
  Confirm all 12 upstream agents' `qc_pre_flags` are present at the minItems-4 floor (48+
  predicates) AND every flag is resolved. Missing agent or short surface →
  `qc_flag_surface_incomplete`. Unresolved flag → `unresolved_upstream_flag`. Name the
  agent + flag in every case.
  Report `predicates_total` as the TRUE counted census, not the nominal 48. The floor is a
  minimum; a richer surface reports its real count.
  This is the step the accumulation floor was provisioned for, twelve agents ago. You are the
  only agent in the fleet positioned to close it.

STEP 10 — MOTION SELF-CHECK ADJUDICATION
  Adjudicate Motion's declared `motion_self_check` (voice_markers_in_captions · truth_echoes ·
  banned_vocab_hits · motion_tokens_applied) against your independent findings. The decisive
  pair: Motion's declared `banned_vocab_hits` MUST equal your Step 6 re-derived count. A
  disagreement escalates the corresponding gate/firewall fail and sets
  `self_check_consistent_with_gate: false`. Never certify a consistency you did not verify.

STEP 11 — VERDICT SYNTHESIS + RESHOOT DETERMINATION
  `pass` iff every check is green — no partial pass, no conditional pass, no pass-with-notes.
  `fail` for a post-fixable defect, routed to the responsible agent.
  `reshoot` iff the defect is in the SOURCE MATERIAL and no re-cut, re-mix, or re-finish on
  existing assets can produce a shippable reel — routed to Production Coord.
  Ask exactly one question for the fail/reshoot split: can any post-tail agent fix this with
  the footage and assets that already exist? Yes → fail. No → reshoot. Ambiguous → fail, with
  `reshoot_considered: true` and your rationale.
  Emit per-check evidence for all 11 gate points + firewall + format + caption + ledger +
  flags + hashes, whatever the verdict.

STEP 12 — MODE-BLIND SELF-ATTESTATION + PUBLISH-QUEUE HANDOFF
  Assert `mode_blind_confirm.production_mode_read: false` and
  `consumed: "mode_agnostic_v3_master"`.
  On `pass`: write qc-report.json + the publish handle to the Drive /reels/[reel_id]/ publish
  queue with `auto_published: false` and `publish_mode: "human_in_the_loop"`.
  Set `handoff_targets: ["localization-agent"]` (holding-store default until the Localization
  Agent #14 ships).
  Emit at least 4 snake_case `qc_pre_flags[]`.
  Set `human_review_required: true`.
  Compute `qc_report_evidence_hash` — SHA-256 over the qc_gate + flag_adjudication +
  evidence_hash_chain block. Your verdict is tamper-evident.

=== OUTPUT CONTRACT ===

Emit valid JSON against output.schema.json. One of two branches (`oneOf`):
`successQcReport` (verdict `pass`) or `errorEnvelope` (verdict `fail` | `reshoot`).

Every output carries: the Cross-SPEC §3.9 metadata block with a 12-tuple `parent_chain`
(inherits Motion's 11-tuple, appends your `qc_report_id`, held additively at minItems 5);
`qc_report_class` (terminal_preflight_pass | terminal_preflight_fail |
terminal_preflight_reshoot); `qc_report_evidence_hash`; `auto_published: false`;
`publish_mode`; `qc_measured_probe_run: false`; `runtime_environment_class`; and
`human_review_required: true`.

=== YOUR STANDARD ===

You are the last line. Twelve agents produced this reel and each checked its own work. You are
the first one checking someone else's, and the only one whose failure is visible to the client.
Adjudicate completely. Route precisely. Publish nothing. When uncertain, fail.
```

### 7.2 Why this prompt is shaped this way

**It leads with position, not task.** The first substantive line is "there is no gate after you." Every prior agent's prompt opened with its domain (author a plan, conform a cut, finish the audio). Full QC's opens with its *terminality*, because every behavioral rule that follows — the completeness rule, the re-derivation exception, the uncertainty posture — is downstream of the fact that nothing catches what it misses.

**The hard rules are ordered by damage.** Rule 1 (never patch) and Rule 2 (never publish) come first because they are the two ways the agent could exceed its authority. Rule 7 (never pass on uncertainty) is placed at the center of the block, not the end, because it is the rule the model is most likely to soften under pressure from a borderline case — a model that wants to be helpful will look for a reason to pass. The prompt gives it the opposite instinct in a single imperative sentence: **WHEN UNCERTAIN, YOU FAIL.**

**Rule 5 is deliberately framed as an exception to Rule 4.** The prompt establishes "never re-derive upstream work" as a firm boundary, then immediately carves out the firewall and explains *why* the carve-out exists. Stating the exception as an exception — rather than burying independent re-derivation in the Step 6 mechanics — makes it cognitively load-bearing. A model that reads "you do not re-derive upstream work" and then encounters `banned_vocab_hits: 0` in the input will accept the declaration unless the prompt has already told it, explicitly and with justification, that this one number is not to be trusted.

**Rule 10 inverts an instinct every prior prompt in the fleet installed.** The eight prior system prompts all trained halt-on-first-fail. Full QC's prompt must actively undo that, so Rule 10 states the inversion, names the three exceptions (precondition, lineage, hash), and then gives the economic reason in the operator's terms: three defects should cost one round-trip, not three. Without the reason, the rule reads as arbitrary and degrades under a long adjudication.

**The 12-step loop is inlined verbatim from §5.** Same discipline as every prior agent — the loop in the prompt is the loop in the spec, not a paraphrase, so the runbook fixtures can be traced step-by-step to prompt text during the 5/5 validation.

**The closing paragraph is not decoration.** "You are the first one checking someone else's work, and the only one whose failure is visible to the client" is the compressed statement of the agent's entire risk posture, placed last so it is the most recent instruction in context when the verdict is rendered.

**Target size:** ~15.2 KB — the largest system prompt in the fleet, as the outline projected (14–16 KB). The terminal gate carries the most checks and the most explicit anti-patterns, and its prompt inlines three brand-canon surfaces (the 11-point gate, the firewall list reference, the format spec) rather than one.

### 7.3 The three-verdict posture in the prompt (the one judgment slot, made explicit)

The prompt states the three verdicts in the opening block and returns to the fail/reshoot split twice: once as Hard Rule 9 (never spend a reshoot on a hunch) and once as Step 11's single decision question. This repetition is intentional. **Full QC is the only post-tail agent with a judgment slot**, and the judgment is expensive in one direction only. The executors (Editor, Sound, Motion) carry deterministic two-verdict postures and their prompts need no judgment scaffolding; full QC's prompt must give the model a single, answerable question — *can any post agent fix this with what already exists?* — rather than an open-ended severity assessment. A severity framing invites the model to invent thresholds. A binary capability question does not.

### 7.4 Cost posture in the prompt (no ceiling authority, no render spend, no measured probe)

The prompt gives full QC **zero cost authority**: it reads the accumulated ledger, checks the envelope, reports an overrun, and routes the adjudication to Production Coord. It never derives a cost, never approves an overrun, and never blocks on a cost question it is not authorized to rule on. Its own cost is ~$0.00–0.02 (gate reasoning + report authoring; the optional evidence-hash re-verify is the only marginal compute). `qc_measured_probe_run: const false` is stated as a hard rule rather than a schema detail because the measured probe is the single most tempting scope creep available to a QC agent — a model asked to verify a format will reach for the file if the prompt does not forbid it. It forbids it.

---

## §10 — QC-Report Field Map (LOCKED-as-drafted Day 94)

### 10.1 The field map (26 rows — lineage + gate adjudication + firewall re-derivation + parity checks + closure checks + derived verdict/report)

Legend: **P** = passthrough (echoed unchanged from input) · **T** = transform (input reshaped/adjudicated into a report field) · **D** = derived (computed by full QC; no direct input antecedent)

| # | Output field | Class | Source | Rule |
|---|---|---|---|---|
| 1 | `output_type` | D | — | `"successQcReport"` on pass; `"errorEnvelope"` on fail/reshoot. Branch discriminator (`oneOf`). |
| 2 | `verdict` | D | §6.4 pass criteria + §12 verdict math | `"pass"` iff every ∧-term true; `"fail"` for a post-fixable defect; `"reshoot"` for a source-material defect. The one judgment slot lives in the fail/reshoot split. |
| 3 | `reel_ref.brand_id` | P | `metadata.brand_id` | Echoed unchanged. v1.0 = `REINVENTED` (pilot brand). |
| 4 | `reel_ref.motion_spec_id` | P | Motion `reel_ref.motion_spec_id` | Echoed — the consumed spec's identity, preserved for route-back attribution. |
| 5 | `reel_ref.qc_report_id` | D | — | UUIDv7 minted by full QC. Also appended to `parent_chain` as position 11 (the 12th element). |
| 6 | `qc_gate.brand_voice_11_point.points_total` | D | Brand Voice Intake §5 | `const 11`. The gate size is canon, not input-derived. |
| 7 | `qc_gate.brand_voice_11_point.points_passed` | D | Check #5 adjudication | The TRUE count of `per_point_evidence[]` rows with `result == "pass"`. A declared value disagreeing with the array = self-QC FAIL. |
| 8 | `qc_gate.brand_voice_11_point.per_point_evidence[]` | D | Check #5 adjudication | Exactly 11 rows, `{point_id, point_name, result, evidence}`. **Populated for passes AND fails** — the complete-diagnosis rule (§6.2). |
| 9 | `qc_gate.entity_firewall_pass_13.text_fields_scanned` | D | Check #6 census | The TRUE count of burned-in text fields walked (captions + lower-thirds + supers + end-card). An undercount = self-QC FAIL. |
| 10 | `qc_gate.entity_firewall_pass_13.metadata_fields_scanned` | D | Check #6 census | The TRUE count of metadata string surfaces walked. |
| 11 | `qc_gate.entity_firewall_pass_13.hits` | **D** | Check #6 **independent re-derivation** | **The one re-derived field in the map.** NOT `motion_self_check.banned_vocab_hits` echoed — full QC computes its own count. This row is the terminal gate's defining discipline expressed as a field class. |
| 12 | `qc_gate.entity_firewall_pass_13.status` | D | rows 9–11 | `"pass"` iff `hits == 0` AND both scan counts equal the true census. |
| 13 | `qc_gate.format_spec.{aspect_ok, resolution_ok, duration_in_band, caption_burn_in_ok}` | T | `declared_format` × Brand Voice Intake §8 | Declared-surface assertions. `duration_in_band == (45000 <= duration_ms <= 75000)`, re-asserted from the declared value — NOT re-derived by decode. |
| 14 | `qc_gate.format_spec.variants_match_promise` | T | `declared_format.platform_variants[]` × `tier_richness_echo.platform_variants_promised` | Delivered-vs-promised parity. The tier-delivery check no other agent performs. |
| 15 | `qc_gate.caption_spec.parity_with_edl` | T | `caption_passthrough[].text` × EDL passthrough | **Byte parity, not similarity.** A near-match is a fail — an unlogged finish-layer copy edit. |
| 16 | `qc_gate.caption_spec.burn_in_text_firewall_clean` | D | Check #6 (caption subset) | The caption-scoped slice of the re-derived firewall result. |
| 17 | `qc_gate.cost_ledger.cumulative_usd` | P | `cost_ledger.cumulative_usd` | Echoed, NOT re-derived (Cross-SPEC §3.10 — derivation is QC Pre-flight's authority). |
| 18 | `qc_gate.cost_ledger.combined_envelope_usd` | T | tier → envelope lookup | The envelope for the reel's declared tier, after the three-surface tier agreement check (Check #9 Part 1). |
| 19 | `qc_gate.cost_ledger.in_envelope` | D | rows 17–18 | `cumulative_usd <= combined_envelope_usd`. |
| 20 | `flag_adjudication.{agents_reporting, predicates_total, unresolved, surface_complete}` | D | Check #10 census over the accumulated `qc_pre_flags` surface | `agents_reporting == 12`. `predicates_total` is the TRUE counted census, not the nominal 48. `surface_complete` iff every agent reports at the minItems-4 floor AND `unresolved == 0`. **The §3.4 accumulation floor's terminal closure.** |
| 21 | `motion_self_check_adjudication.{voice_markers_in_captions, truth_echoes, banned_vocab_hits, motion_tokens_applied}` | P | Motion `motion_self_check` | Echoed **as Motion declared them** — this block preserves the upstream attestation verbatim so the operator can compare it against row 11's re-derived count. |
| 22 | `motion_self_check_adjudication.self_check_consistent_with_gate` | D | row 21 × rows 8/11 | `false` on any divergence between Motion's declaration and full QC's findings — a provenance finding, recorded regardless of verdict. Never asserted `true` unverified. |
| 23 | `evidence_hash_chain.{motion_spec_evidence_hash_verified, audio_spec_evidence_hash_verified, edl_evidence_hash_verified}` | D | Check #3 recomputation | Each leg recomputed over its source block and matched. Three anchors, one pass — the only place in the fleet all three are verified together. |
| 24 | `evidence_hash_chain.chain_intact` | D | row 23 | The AND of the three legs. Never `true` on an uncomputed leg. |
| 25 | `publish_target.{auto_published, publish_mode, publish_queue_uri}` | D | — | `auto_published: const false` · `publish_mode: "human_in_the_loop"` · queue URI platform-relative `ars://`. The honest declaration that nothing was published. |
| 26 | `tier_richness_echo.{tier, platform_variants_promised, platform_variants_validated, primary_aspect}` | T | inbound `tier_richness_echo` + row 14 | Echo extended with `platform_variants_validated` — the count full QC actually checked, which must equal `platform_variants_promised` on a pass. |

**Supporting fields (canonical, not counted in the 26):** `handoff_targets` (D — `["localization-agent"]`, holding-store default), `mode_blind_confirm` (D — `{production_mode_read: false, consumed: "mode_agnostic_v3_master"}`), `human_review_required` (D — `const true`), and the Cross-SPEC §3.9 metadata block (§16, partial 2).

### 10.2 v1.0 RESERVED FIELDS (deferred to v1.1+)

| Reserved field | Why deferred |
|---|---|
| `measured_probe.{measured_resolution, measured_fps, measured_lufs, measured_duration_ms}` | Requires frame-level decode — the $-and-render surface the whole fleet defers. `qc_measured_probe_run: const false` in v1.0. |
| `auto_publish_receipt.{platform, published_at, live_uri}` | Activates with the Publishing Agent (#16). `auto_published: const false` until then. |
| `auto_patch_directive` | The v1.1 auto-fix-routing feature QC Pre-flight also deferred. v1.0 adjudicates and routes; it never generates a patch. |
| `localization_handoff.{target_locales, handoff_at}` | Activates when the Localization Agent (#14) LOCKs. v1.0 emits to the Drive publish queue as a holding store. |
| `historical_gate_trend` | Cross-reel gate analytics (false-fail-rate tracking) — a Week 5+ observability feature, not a per-reel field. |

### 10.3 No-touch fields (read-only references — full QC reads and never writes)

`motion_spec.*` (Motion's authority) · `audio_spec.*` (Sound's) · `edl.*` (Editor's) · `edit_plan.*` (Edit Director's) · `asset_bundle.*` (Ingest's) · `cost_derivation.*` (QC Pre-flight's) · `production_mode` (read for the report context line ONLY — never as a verdict discriminator) · the Brand Voice Intake §5/§6/§7/§8 canon (adjudication reference, never re-authored).

### 10.4 Schema authoring note (for the schemas day, Day 99+)

- `verdict` is a **3-value enum** (`pass` | `fail` | `reshoot`) — the first 3-value verdict in the post tail. The `successQcReport` branch constrains it to `const "pass"`; the `errorEnvelope` branch to `enum ["fail", "reshoot"]`.
- `parent_chain`: `minItems: 5`, `prefixItems` positions 0–11, `maxItems: 12`, `items: false` — additive, accepting the 5→12-tuple while rejecting a 4-tuple. **The exact-N flip to 12 is deferred** to the single separately-validated hardening migration the Sound 10-tuple and Motion 11-tuple flips await.
- `qc_report_evidence_hash`: `pattern: "^[a-f0-9]{64}$"`.
- `auto_published`: `const false` · `qc_measured_probe_run`: `const false` · `publish_mode`: `enum ["human_in_the_loop"]` in v1.0 (`"automated"` reserved, not yet valid).
- `per_point_evidence`: `minItems: 11, maxItems: 11` — the gate size is canon and the array is exhaustive.
- `qc_pre_flags`: `minItems: 4`, snake_case pattern per §3.7.
- All URI fields: `pattern: "^ars://"` — no absolute URLs in a publish-queue artifact.

### 10.5 Gate-flatness matrix (tier-FLAT gate / tier-AWARE ledger — restated as a field-level contract)

| Field group | Pilot | Starter | Pro | Enterprise |
|---|---|---|---|---|
| `qc_gate.brand_voice_11_point` | identical | identical | identical | identical |
| `qc_gate.entity_firewall_pass_13` | identical | identical | identical | identical |
| `qc_gate.caption_spec` | identical | identical | identical | identical |
| `qc_gate.format_spec` (aspect/resolution/duration/burn-in) | identical | identical | identical | identical |
| `qc_gate.format_spec.variants_match_promise` | vs Pilot promise | vs Starter promise | vs Pro promise | vs Enterprise promise |
| `qc_gate.cost_ledger.combined_envelope_usd` | Pilot envelope | Starter envelope | Pro envelope | Enterprise envelope |
| `flag_adjudication` | identical | identical | identical | identical |
| `evidence_hash_chain` | identical | identical | identical | identical |

**Exactly two rows vary by tier**, and both are quantity-of-promise rows (how many variants were sold, how much spend was budgeted) — never quality-of-brand rows. This table is the field-level proof of the §4 tier-FLAT-gate contract and is the structure the Day 96 §9 fixtures TC-01 (Pro) and TC-02 (Enterprise) will assert byte-identical across, alongside their mode-blind convergence assertion.

---

## §14 — Implementation Plan (LOCKED-as-drafted Day 94 · status updates · re-baselined trajectory)

### 14.1 Calendar (Day 92 → v1.0 LOCK — full QC trajectory, re-baselined after the Day-93 slip)

| Day | Date | Deliverable | Status |
|-----|------|-------------|--------|
| 92 | Mon Jul 20 | SPEC outline §0–§5 | ✅ **SHIPPED** |
| 93 | Tue Jul 21 | *(outline-calendared partial 1)* | ⚠️ **NO DELIVERABLE — session produced no artifact; scope carried forward intact** |
| 94 | Wed Jul 22 | **SPEC body partial 1: §6 + §7 + §10 + §14** | ✅ **SHIPPING NOW** (one-day slip, surfaced) |
| 96 | Fri Jul 24 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | ⏳ next (was Day 95 pre-slip) |
| 97 | Sat Jul 25 | v1.0 LOCK CANDIDATE | ⏳ |
| 98 | Sun Jul 26 | **REST DAY — no build** (pre-stage scaffold only) | ⏳ 15th observance |
| 99 | Mon Jul 27 | schema pair (`input.schema.json` + `output.schema.json`) | ⏳ |
| 100 | Tue Jul 28 | SKILL bundle (`skills/qc-agent/`) + offline `validate.py` | ⏳ |
| 101 | Wed Jul 29 | LLM Test Runbook (5 fixtures) | ⏳ |
| TBD | — | **v1.0 LOCK — TRIPLE-GATED** (Sound LOCK → Motion LOCK → full QC 5/5) | 🔒 spend-gated |

**Slip accounting (honest):** the trajectory absorbs the Day-93 slip by shifting partial 2 from Day 95 to Day 96. The Day 98 Rest Day is unaffected and the LOCK-candidate→runbook chain lands on the same relative cadence Motion and Sound held (candidate → schemas → bundle → runbook over five build days with a Rest Day split). Net calendar impact: **one build day.**

### 14.2 Author tasks completed this session (Day 94)

- ✅ §6 authored — 13-check self-QC list, LOCKED-as-drafted (settles the outline's 12–14 target at 13).
- ✅ §6.2 ordering rationale — 4-tier fleet shape retained; the **completeness rule** (run-all-substance-checks, not halt-on-first-fail) authored as full QC's defining behavioral divergence, with its O(n)→O(1) round-trip justification.
- ✅ §6.3 code namespace — settled at **12 named + slot catch-all**, **two above the outline's 8–10 target**; overage surfaced with structural justification and three named operator reduction options (fold #3 recommended if a reduction is required). Complete check→code→verdict→route→recovery mapping table authored.
- ✅ §6.4 pass criteria + the **fail-vs-reshoot judgment slot** — the single-question determination (can any post agent fix this with what exists?), the bias-toward-`fail` discipline, and the false-pass-0% / false-fail-≤6% asymmetry.
- ✅ §6.5 canonical firewall list — 11 entries inherited verbatim, ninth agent to carry it unmodified; full QC's re-derivation distinction documented.
- ✅ §7 system prompt v1.0 authored verbatim (~15.2 KB — the fleet's largest, as projected) + §7.2 design rationale + §7.3 three-verdict posture + §7.4 cost posture.
- ✅ §10 field map — 26 rows + reserved fields + no-touch fields + schema authoring notes + the gate-flatness matrix (exactly two tier-varying rows, both quantity-of-promise).
- ✅ §14 calendar re-baselined after the Day-93 slip; slip surfaced rather than absorbed.
- ✅ Offline fleet regression sweep re-run: **434/434 across 8 SKILL bundles, 0 drift** (reproduces the Day-90 and Day-92 stamps exactly).

### 14.3 Author tasks remaining (Day 96 partial 2)

- ⏳ §8 Performance Targets — 9 metric categories (schema validity 100% · firewall catch 100% · 11-point adjudication 100% · format parity 100% · caption parity 100% · flag-surface closure 100% · hash-chain verify 100% · **false-pass 0%** · **false-fail ≤6%** · p50 30s / p95 90s · zero engine/render/decode cost).
- ⏳ §9 Test Fixtures — the 5-fixture portfolio (TC-01 Pro `pass` · TC-02 Enterprise `pass` — the **mode-blind gate-convergence proof, five stages deep**, byte-identical gate path to TC-01 · TC-03 `format_spec_mismatch` · TC-04 `unresolved_upstream_flag` — the accumulation-floor catch unique to the terminal gate · TC-05 `qc_firewall_breach` — GATING).
- ⏳ §11 Cost Model — $0 snapshot + the catch-cost-avoidance value model.
- ⏳ §12 Verdict Math — the formal ∧-expression + the fail-vs-reshoot judgment slot formalized.
- ⏳ §13 Critical Decisions — 12–16 LOCKED, including the four live amendment slots this partial opened (§6.3 code count · §6.1 check count · format/firewall routing granularity · Localization holding store).
- ⏳ §15 Change Log · ⏳ §16 Metadata Block Schema (12-tuple + the 7 full-QC additions).

### 14.4 Dependencies & gates (carried — surfaced, NOT advanced)

1. **Sound #11 v1.0 LOCK** — spend-gated on a live 5/5 of the Day 81 runbook (~$3.50 Opus). **Still the ONLY open link in the ten-deep LOCKED chain.**
2. **Motion #12 v1.0 LOCK** — DOUBLE-gated (Sound LOCK first, then Motion's own Day-90 runbook 5/5, ~$3.75 Opus).
3. **Full QC #13 v1.0 LOCK** — **TRIPLE-gated** (Sound LOCK → Motion LOCK → full QC's own 5/5). The fleet's first triple-gate. Not reachable from a $0 unattended session by construction.

None of the three was advanced tonight. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.

### 14.7 Parent-chain exact-N gate (seventh forcing function — carried)

Full QC's 12-tuple `parent_chain` is the **seventh** forcing function on the deferred exact-N `minItems` hardening. The §3.9 n-tuple-as-lineage amendment is **RATIFIED (Day 79)**; the exact-N tightening remains deliberately deferred to a **single separately-validated migration** covering the Sound 10-tuple + Motion 11-tuple + full QC 12-tuple flips together, scheduled after the Sound LOCK closes and explicitly **not folded into any agent's LOCK ceremony**. Held additively at `minItems: 5` in the interim.

---

## Process integrity attestation (Day 94)

- ✅ **No prior canon modified.** 1 NET-NEW forward deliverable (this partial 1). All source material (the Day 92 full QC outline, the Motion Day 83 partial 1, the QC Pre-flight Day 41 partial 1, the Blueprint, the Cross-SPEC review, the Brand-Voice Intake, the 8 skill bundles) read-only.
- ✅ **No LLM dispatched. No engine, no render, no compositing, no frame decode, no measured probe, no publish, ZERO $ spent.** `jsonschema` 4.26.0 was pip-installed from PyPI (no vendor/engine surface, $0) purely to re-run the offline fleet validators.
- ✅ **Offline fleet regression: 434/434 across 8 bundles, 0 failures, 0 tracebacks** (ai-video-gen 11 · style-replication 13 · qc-preflight 34 · ingest 47 · edit-director 59 · editor 76 · sound 83 · motion 111). Reproduces the Day-90 and Day-92 stamps exactly. No prior canon drifted.
- ✅ **No operator-impersonation.** Executed NO LOCK ceremony. **Sound #11 was NOT locked** (live 5/5 forbidden at $0). **Motion #12 was NOT locked** (double-gated). **Full QC #13's LOCK is triple-gated and not reachable.** No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED.
- ✅ **No fake-advance.** This partial authors §6 + §7 + §10 + §14 as LOCKED-as-drafted forward design over LOCK-stable text artifacts; it flips no deferred cardinality, pre-empts no ceremony, and re-states the triple-gate so no shortcut can LOCK full QC ahead of Sound + Motion.
- ✅ **No silent pivot — and the one-day slip is SURFACED.** The Day 92 log's "Next" line named Day 93 partial 1. No Day-93 artifact exists on disk. This session ships that exact scope on Day 94 and re-baselines the calendar in §14.1, reporting the slip rather than absorbing it. No substitution of deliverable.
- ✅ **Entity boundary respected.** ARS = Sequel Digital. `brand_id` v1.0 = REINVENTED (pilot brand). The HC/NPOX tokens in §6.5 are the firewall's BLOCK-list, not a cross-entity reference.
- ✅ **Rest Day honored** — 14/14 to date. Prior Rest Day Day 91 (Sun Jul 19) observed. Tonight is Wednesday (Day 94) — building allowed. **Next Rest Day: Day 98 (Sun Jul 26) — will be observed (15th).**
- ✅ **No scope expansion.** One forward deliverable + the offline regression sweep + log + mirror + Notion status update + standing housekeeping + the Google Voice digest. Nothing extra acted on.

---

## Files produced today (Day 94)

- `ars/ARS-2026-07-22-Day-94-Full-QC-Agent-SPEC-Body-Partial-1.md` — this doc
- `ars/build-log-2026-07-22.md` — Day 94 build log

Mirror copies in `/outputs/ars/`.

---

*Day 94 ships clean, one build day behind the outline calendar (surfaced, re-baselined). Day 96 (Fri Jul 24) targets SPEC body partial 2 (§8 + §9 + §11 + §12 + §13 + §15 + §16). Full QC is Agent #13 of 17 — the terminal ship-safety gate, the 13th and FINAL defense-in-depth firewall, the FIRST adjudicator in the post tail, the fifth contractually mode-blind agent, and the second + terminal consumer of the §3.4 accumulation floor. §6 settles 13 checks; §6.3 settles 12 named codes + slot catch-all (two above the outline target, with the structural justification and three operator reduction options surfaced for the Day-96 §13 walk); §7 authors the fleet's largest system prompt (~15.2 KB) around a single governing instruction — WHEN UNCERTAIN, YOU FAIL; §10 maps 26 fields, exactly one of which is independently re-derived rather than echoed (the firewall hit count — the terminal gate's defining discipline expressed as a field class). Operator pickup is unchanged: (1) the **Sound v1.0 LOCK** remains the immediate forward step and the ONLY open link — a live, reproducible 5/5 of the Day 81 runbook (~$3.50 Opus) the $0 overnight cannot execute; (2) then the **Motion 5/5 + LOCK** (~$3.75 Opus, double-gated); (3) full QC's own LOCK is the fleet's first TRIPLE-gate behind both. Neither LOCK was performed tonight — locking on the offline stamp alone would be a fake-advance.*
