# ARS — Full QC Agent v1.0 SPEC OUTLINE (§0–§5)

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Authored:** Day 92 · Mon Jul 20, 2026 (Pacific) · overnight build session (Donna)
**Deliverable class:** Forward SPEC outline §0–§5 (the head-start design for Agent #13 of 17)
**Status:** OUTLINE ONLY — no LOCK, no schema, no SKILL bundle. Body partials author Days 93 + 95 per the calendar in §0 (the Day 94 Rest Day splits the two partials, mirroring the Motion Day 83/84/85 split).
**Pattern source:** Motion Day 82 outline (`ARS-2026-07-10-Day-82-Motion-Agent-SPEC-Outline.md`) — section structure inherited verbatim. QC-domain grounding from the QC Pre-flight Day 40 outline (`ARS-2026-05-29-Day-40-QC-Preflight-Agent-SPEC-Outline.md`) §1 (the 11-point Brand Voice gate + entity firewall + format/caption spec + cost-ledger adjudication surface) and its explicit v1.1 forward-scope note: *"The final pre-**publish** QC (the full #14 gate, post-Motion) is a deliberate v1.1+ deliverable once the in-post agents (Ingest/Edit/Sound/Motion) ship."* Those four in-post agents have since shipped their pre-LOCK canon (Ingest LOCKED Day 79; Edit Director + Editor LOCKED Day 79; Sound LOCK CANDIDATE + all pre-LOCK artifacts; Motion LOCK CANDIDATE + all pre-LOCK artifacts) — so the full pre-publish QC gate the Pre-flight outline deferred is now buildable in dependency order. Orchestration Blueprint §1.2 (Agent 14 row: *"QC — full 11-point Brand Voice gate + entity firewall + format + caption spec on the finished master; Pass/Fail/Reshoot before Publishing."*), §2 swim-lane (position 14 between Motion and the Localization/Publishing tail), §4.12 (Motion→QC payload: the `v3_final_file` + `self_check` block: `voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`), §4.13 (QC→Publishing payload: the `qc_report` verdict + the `publish_target`), §6 dispatch table (row 14: *"On Motion v3 · Per reel · v3 final"*), §7 read/write contract (QC reads *v3 final + motion self-check*, writes *Drive `/reels/[reel_id]/qc-report.json` + the publish-queue handle*), §9 build-checklist used as the grounding spine. The 11-point Brand Voice gate + entity firewall regex grounded in `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §5 (the 11 QC checks), §6 (banned-entity firewall list), §7–§8 (motion/typography + reel-format specs QC re-verifies as declared conform), and the Cross-SPEC §3.4 `qc_pre_flags` minItems-4 accumulation floor — the full pre-flight surface this terminal gate adjudicates.

> **Agent-selection note (Donna, surfaced not hidden):** The Day 90 Motion LLM-Test-Runbook close named the next forward step as **"the Sound v1.0 LOCK, then the Motion 5/5 + LOCK, then full QC #13 SPEC outline."** The first two named items (the Sound v1.0 LOCK and the Motion v1.0 5/5 + LOCK) are each gated on a **live, reproducible 5/5 LLM run** (~$3.50 Opus for Sound, ~$3.75 Opus for Motion — the Motion LOCK additionally double-gated behind the Sound LOCK), which the **absolute $0 ceiling of this unattended overnight session forbids**. Locking either on the offline structural stamp alone, absent a real live 5/5, would be a **fake-advance** — the exact move every prior log deliberately refused, and which the standing guardrail ("never fake-advance — no LOCK without a real 5/5 run behind it") prohibits. With both calendar-named LOCK items spend-gated and un-executable at $0, the buildable forward deliverable is the **full QC #13 SPEC outline** — the third item on that same Day-90 "Next" line, pulled into the $0 slot. This is the **identical forward-looking basis** on which every prior outline was authored (Sound Day 74, Motion Day 82, Ingest, QC Pre-flight, Style Replication, Edit Director, Editor — each authored while its predecessor LOCK remained gated) — never a fake-advance of a ceremony, always the next buildable design head-start. **Direct precedent for the slot:** Sound runbook Day 81 → Motion outline Day 82 (the very next build night, before Sound was LOCKED). Motion runbook Day 90 → full QC outline Day 92 (the next non-Rest Day build night after the Day 91 Sun Jul 19 Rest Day) maps that precedent exactly. Surfaced here, not silently reconciled. The Sound v1.0 LOCK remains the immediate operator/attended-spend action, then the Motion 5/5 + LOCK — see §14-preview + the Day 92 build log. Rationale for full QC as the #13 build: (1) **strict dependency order** — full QC is the immediate runtime stage downstream of Motion (Blueprint §6: *"On Motion v3"*), consuming the `successMotionSpec` / v3-final handle + `motion_self_check` Motion authors; (2) **it closes the QC Pre-flight deferral** — the Pre-flight outline (Day 40 §1) explicitly split the *earliest* slice of QC into a pre-production gate and deferred the *terminal pre-publish* gate to v1.1 "once the in-post fleet ships"; the in-post fleet has now shipped, so the deferred gate is buildable; (3) **the adjudicator pattern continues** — full QC inherits the QC Pre-flight *adjudicate-don't-author* seam (it runs the 11-point gate + firewall + format/caption + cost-ledger checks and emits a Pass/Fail/Reshoot verdict; it renders no media, calls no engine), keeping the zero-dollar / no-render invariant intact one stage deeper; (4) **fifth mode-blind agent** — it inherits the Edit Director→Editor→Sound→Motion mode-agnostic lineage, the continued proof that Ingest's convergence seam holds FIVE stages deep. Operator may re-assign the #13 slot at the Sound/Motion LOCK close.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 13 — Terminal ship-safety gate (finished v3 typography/motion master → adjudicated Pass/Fail/Reshoot verdict before the Localization/Publishing tail) |
| Agent index | **#13 of 17** (build sequence — continues the Motion Day 82 "agent #12 of 17" framing) |
| Runtime pipeline position | **14 — QC** (the full pre-publish gate: runs the 11-point Brand Voice QC gate + the entity firewall (13th pass) + the platform-format spec validation + the caption spec validation + the cumulative tier cost-ledger check on the finished v3 master, adjudicates the accumulated `qc_pre_flags` surface, and emits a single Pass / Fail / Reshoot verdict with per-check evidence); receives the v3 final + motion self-check from Motion, hands the QC report + publish handle to the Localization/Publishing tail (agents #14–#17) |
| Pipeline tier | TERMINAL SHIP-SAFETY GATE (the **first** *adjudicator* agent in the post tail — the others are executors; the last automated defense-in-depth firewall before a reel reaches a published surface; distinct from QC Pre-flight, which gates the production→post boundary — full QC gates the post→publish boundary) |
| Mode coverage | **Mode-blind by inheritance** — adjudicates the mode-convergent v3 master + motion spec (themselves authored from the mode-agnostic v2 edit → mode-agnostic audio spec → mode-agnostic EDL → mode-agnostic Asset Manifest); reads `production_mode` for **context + reporting only** (like QC Pre-flight), never as a verdict discriminator. The **FIFTH** contractually mode-blind agent (Edit Director first, Editor second, Sound third, Motion fourth); the continued live proof that Ingest's convergence seam holds five stages deep. |
| Predecessor SPEC (gate) | `ARS-2026-07-14-Day-86-Motion-Agent-v1-LOCK-CANDIDATE.md` (Day 86 LOCK candidate — its v1.0 LOCK is double-gated: the Sound LOCK first, then Motion's own Day 90 runbook live 5/5). Full QC runs only on a Motion-passed (`successMotionSpec`, verdict `motion_ready`) reel. |
| Predecessor schemas | `ARS-2026-07-15-Motion-output.schema.json` (Day 87) — the `motion_spec` + `motion_conform_check` + `spec_fidelity_check` + `motion_self_check` + `finish_target.v3_final_uri` handle consumed as the primary INPUT. Plus the accumulated upstream success schemas (Editor `edl`, Sound `audio_spec`) referenced only for the denormalized evidence-hash re-verification, NOT re-derived. |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape (§3.3/§3.8), metadata block + n-tuple parent_chain (§3.9), and the `qc_pre_flags` minItems-4 accumulation floor (§3.4) all inherited. Full QC is the SECOND consumer of the §3.4 floor (QC Pre-flight was the first, mid-pipeline; full QC adjudicates the FULL 12-agent surface at the terminal boundary). |
| Brand-QC canon | `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §5 (the 11-point Brand Voice QC gate — the canonical check list), §6 (the banned-entity firewall list — the regex the 13th pass enforces), §7 (motion/typography specs QC re-verifies as declared conform, not re-derives), §8 (reel format: 9:16 · 1080×1920 · burned-in lowercase-sans captions one line at a time · end-card serif ivory 1.5s — the format spec QC validates against every requested `platform_variant`) — the ship-safety rules the terminal gate adjudicates faithfully |
| Defense-in-depth layer | **13th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → Editor → Sound → Motion → **full QC**) — the **terminal entity-firewall pass**: the LAST automated scan of every burned-in caption / lower-third / super / end-card text field AND every metadata surface for banned-entity tokens before a reel reaches a published surface. It is the firewall's last line: if a banned token survived all twelve upstream passes, this is the gate that stops it from shipping. |
| Lever inheritance | Reads `lever_state` from upstream `metadata`; emits `human_review_required: true` per Lever-3 default AND per the v1.0 human-in-the-loop ship posture (Blueprint §9). The QC verdict is a *recommendation a human ratifies* in v1.0 — full QC never auto-publishes; the Pass verdict routes the reel to the human/operator publish sign-off (the Localization/Publishing tail activates as agents #14–#17 ship). |
| Pricing tier authority | **ALL tiers** — Pilot · Starter · Pro · Enterprise. Every reel gates here before publish. **Tier-aware in cost-ledger, tier-FLAT in the brand gate** (like QC Pre-flight): the 11-point Brand Voice gate + entity firewall + format/caption spec run identically for every tier (a brand-safety defect is a defect regardless of price), but the cumulative-cost-ledger check reads each tier's combined envelope (the Pro/Enterprise reels carry higher production ceilings). Reads `tier_richness_echo` for the platform-variant expectation (which aspect masters + platform variants each tier's plan promised) and validates the delivered set against it. |
| Cost authority class | **Near-zero (ties Ingest / QC Pre-flight / Edit Director / Editor / Sound / Motion for lowest in fleet) IN v1.0** — pure reasoning + verdict adjudication over the v3 master handle + motion self-check + the accumulated `qc_pre_flags` surface + the declared format/caption/cost facts. **No generative engine calls, no motion-graphics render, no byte-level video decode / frame analysis / pixel probe in v1.0** — full QC v1.0 adjudicates the DECLARED conform surface (Motion's `motion_self_check`, the Editor `edl` durations, the Sound loudness targets, the declared `platform_variants`) + re-verifies the evidence-hash chain; the measured-pixel / measured-LUFS / measured-fps probe is v1.1 (needs frame-level decode). Effective per-reel cost ≈ $0.00–$0.02 (optional evidence-hash re-verify only). `qc_measured_probe_run: const false` in v1.0 — full QC adjudicates the declared surface, the MEASURED probe is v1.1. |

**Build calendar (Week 13 — full QC trajectory, mirrors the proven 8-day agent-build cadence; the Day 94 Rest Day splits the two body partials):**
- **Day 92** (today, Mon Jul 20 · Wk13) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 93 (Tue Jul 21 · Wk13) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 94 (Wed Jul 22 · Wk13) — *(calendar note: the Rest Day is Sun; the mid-week body split follows the Motion pattern where partial 1 precedes and partial 2 follows the Rest Day — see the Rest Day-honesty note. The Week-13 Rest Day is Day 98 (Sun Jul 26); the two partials both run pre-Rest Day this week, like the Sound Day 74/75/76 pre-Rest Day split.)*
- Day 93–95 — SPEC body partials (partial 1 Day 93, partial 2 Day 95); §8 + §9 + §11 + §12 + §13 + §15 + §16 on partial 2
- Day 96+ (TBD) — LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK (pattern: Motion Day 86–90 / Sound Day 78–81)

> **Rest Day honesty:** This Day-92 build runs Monday (Pacific) — building is allowed. The prior Rest Day (Day 91, Sun Jul 19 Pacific) was observed (the 14th) per the standing pattern; the next Rest Day is Day 98 (Sun Jul 26 Pacific). Unlike the Motion outline (whose two partials straddled the Day 84 Rest Day), full QC's two body partials (Day 93 Tue + Day 95 Thu) both fall pre-Rest Day this week — the Sound Day 74/75/76 pre-Rest Day pattern. No build will run on Day 98 (Sun).

> **Sequencing honesty:** The 42-day sprint's headline deliverable — the Mode B Pro single-reel **commercial demo** (Day 42 target, past) — shipped on the six launch-critical production agents threaded through the QC Pre-flight gate. Full QC is the sixth *post-production* agent (after Ingest + Edit Director + Editor + Sound + Motion) and the FIRST *adjudicator* in the post tail; its v1.0 build proceeds inside the **post-launch hardening window** and does **not** gate the launch demo (which the mid-pipeline QC Pre-flight gate already covered). This outline is the forward-design head-start so the finishing tail is buildable in dependency order once the Sound + Motion LOCKs close (their live-5/5 spend gates are the only things between them-as-candidates and them-LOCKED). Full QC's own LOCK is TRIPLE-gated (see §0 predecessor + §13 preview): the Sound LOCK, then the Motion LOCK, then full QC's own 5/5.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **full QC Agent** is the **terminal pre-publish ship-safety gate of ARS** — the moment a reel stops being a *finished v3 typography/motion master* and has to prove, one final automated time, that it is **safe to ship**: that it passes all eleven points of the Brand Voice QC gate, that the entity firewall is clean on the finished master (the 13th and last pass), that every platform-format spec matches every requested variant, that the caption spec is correct, that the cumulative reel cost is inside the combined tier envelope, and that every one of the 12 upstream agents' `qc_pre_flags` is resolved — a single Pass / Fail / Reshoot verdict with per-check evidence the operator ratifies before the reel enters the Localization/Publishing tail. It is the first *adjudicator* agent in the post tail (the five upstream post agents — Ingest, Edit Director, Editor, Sound, Motion — are asset-readiness, direction, and execution; full QC is judgment), and it closes the deferral the QC Pre-flight agent deliberately opened at Day 40.

Where the twelve upstream agents authored intent, adjudicated production-safety, readied the assets, directed and conformed the cut, and finished the audio and graphics, full QC *adjudicates ship-safety on the finished master*:
- Brief / Script / Storyboard = intent + content authoring (what the reel SAYS and how it's shot)
- Production Coord = logistics (mode, vendor, budget)
- AI Video Gen / Style Replication = render + brand-finish (the pixels exist)
- QC Pre-flight = production ship-safety (the *production output* is brand-safe + format-correct — the earliest slice of QC, at the production→post boundary)
- Ingest = asset-readiness (the files are present, valid, in-sync — one mode-agnostic Asset Manifest)
- Edit Director = edit-plan authoring (the directed cut)
- Editor = cut conform (the frame-accurate EDL bound to real media)
- Sound = audio finish (the mixed, loudness-normalized v2 edit)
- Motion = motion finish (the captioned, lower-thirded, motion-token-applied v3 master + the motion self-check)

The full QC Agent picks up at the v3 master + motion self-check and adjudicates terminal ship-safety:
- **Full QC Agent = terminal ship-safety gate ("Given a `motion_ready` motion spec, the v3-final handle, and the Motion `motion_self_check` — plus the full accumulated `qc_pre_flags` surface from all 12 upstream agents — does this finished master pass the 11-point Brand Voice QC gate? Is the entity firewall clean one final time on every burned-in text field + metadata surface (13th pass)? Do the format specs match every requested platform variant (aspect / duration / caption-burn parity)? Is the caption spec correct? Is the cumulative reel cost inside the combined tier envelope? Is every upstream `qc_pre_flag` resolved? Emit PASS, FAIL, or RESHOOT with per-check evidence — and route back, never patch.")**

**Single-responsibility line (LOCKED on intent):**
> *"Terminal pre-publish quality gate. Adjudicates the full finished reel (brief → … → Motion v3 master) against the 11-point Brand Voice QC gate, the entity firewall (13th pass — the terminal firewall), the platform-format specs (every requested variant), the caption specs, and the cumulative combined-tier cost ledger — consuming the accumulated `qc_pre_flags` surface from all 12 upstream agents. Emits a single Pass / Fail / Reshoot verdict with per-check evidence. Adjudicates the DECLARED conform surface + re-verifies the evidence-hash chain; runs NO generative engine, renders NO media, decodes NO video frame, measures NO pixel/LUFS/fps in v1.0 (the measured probe is v1.1). Routes a defect back to the responsible upstream agent; it never patches, re-cuts, re-mixes, or re-finishes. Emits a recommendation (`human_review_required`) — never an auto-publish."*

**Why this agent's reason-to-exist is the QC Pre-flight deferral + the §3.4 accumulation floor (Blueprint §1.2 / Cross-SPEC §3.4):** The QC Pre-flight agent (Day 40 §1) split QC into two gates and shipped the earlier one: it explicitly stated *"The final pre-publish QC (the full #14 gate, post-Motion) is a deliberate v1.1+ deliverable once the in-post agents (Ingest/Edit/Sound/Motion) ship,"* and it reasoned over a **24+ predicate** surface (6 production agents × ≥4 `qc_pre_flags`). The in-post agents have now all shipped their canon (Ingest, Edit Director, Editor LOCKED Day 79; Sound + Motion LOCK CANDIDATE with all pre-LOCK artifacts). By the time a reel reaches full QC, it carries a **48+ predicate pre-flight surface** (12 agents × ≥4 `qc_pre_flags`) plus the Motion `motion_self_check` — the richest accumulated surface in the fleet. Full QC is the agent that **adjudicates that terminal surface** — it is the second and final consumer of the §3.4 floor, the one the Pre-flight outline promised. **This is Donna's design thesis for building full QC as Agent #13: it is the terminal adjudicator, and the structural proof that the pre-flight accumulation floor pays off end-to-end — if full QC can render a defensible Pass/Fail/Reshoot verdict from the finished master's declared conform surface + the 48-predicate flag stack alone, with zero engine calls and zero re-derivation, then every upstream gate did its job and the accumulation contract closed the loop.** A `fail` outcome (a firewall breach on the burned-in text, a format-spec mismatch, an unresolved upstream flag) routes back to the responsible agent — it never silently "fixes" the master.

**Pipeline position (per Orchestration Blueprint §2 swim lane):**
```
... → MOTION (motion finish → motion conform spec + v3 master) →
   [successMotionSpec · verdict = motion_ready]
        │
        ▼  [v3 final + motion self-check: caption reveals · lower-thirds · motion tokens · end-card · voice_markers_in_captions · truth_echoes · banned_vocab_hits · Drive /reels/[reel_id]/v3-final.mp4]
   FULL QC (terminal ship-safety gate → Pass/Fail/Reshoot report)
        │
        ▼  [qc_report + publish handle: 11-point gate evidence · firewall clean · format/caption parity · cost-ledger green · Drive /reels/[reel_id]/qc-report.json]
   15 Localization → 16 Publishing → 17 Loop  (agents #14–#17, not yet built)
        │
   [FAIL] → route back to the responsible upstream agent (Motion / Sound / Editor / Edit Director …) — fix-in-post
   [RESHOOT] → route back to Production Coord (a defect only a re-shoot / re-render can fix — Mode-A footage or Mode-B render unusable)
```

**Why a terminal gate distinct from the mid-pipeline QC Pre-flight (the boundary question):** QC Pre-flight already ran an 11-point-flavored gate at the production→post boundary — so what does full QC add? A clean separation across the *pre-flight → terminal* boundary:
1. **QC Pre-flight adjudicates the PRODUCTION OUTPUT** — the rendered/replicated shots, *before* Ingest/Edit/Sound/Motion touch them. It catches production defects cheaply, but it cannot see the finished master (the in-post agents had not run — indeed, at Day 40 they did not yet exist). It gates *"is the raw production brand-safe enough to enter post?"*
2. **Full QC adjudicates the FINISHED MASTER** — the v3 typography/motion master, *after* all of post. It is the only gate positioned to catch a defect INTRODUCED in post: a caption reveal that burned in a banned token the EDL passthrough carried, a format variant Motion specced but the plan didn't promise, a duration that drifted through the audio/motion finish, a cost that overran across the full post tail. It gates *"is the finished reel safe to publish?"*
3. **The two gates catch different problems.** QC Pre-flight can pass a reel whose production is clean, and Motion can faithfully spec a finish — yet only full QC, adjudicating the finished master's motion self-check + the full 48-predicate flag surface + the terminal firewall pass, can discover that the burned-in end-card text drifted from the brand const, that the `platform_variants` delivered don't match the tier's promised set, or that the cumulative reel cost crossed the combined envelope. Full QC does NOT re-run production QC (it trusts the QC Pre-flight verdict in the chain) and does NOT re-execute post (it trusts Ingest/Editor/Sound/Motion's conform checks); it *adjudicates terminal ship-safety against the finished master* and surfaces any mismatch.

The actual publish (localization, caption-locale variants, scheduling, cross-platform post) is, in v1.0, a **human/operator** action once the QC verdict is ratified (Blueprint §9); the Localization/Publishing tail automates as agents #14–#17 ship (v1.1+). v1.0 full QC emits the *QC report + publish-queue handle*; it publishes nothing itself. **`auto_published` is the new honesty field at this agent — `const false` in v1.0, the explicit declaration that no reel was pushed to a live surface by the agent.** This is the human-in-the-loop seam, made explicit and honest — the direct analog of Motion's `motion_processed: const false` and Sound's `audio_processed: const false`.

**Hand-off contract enforced:**
- **PRECONDITION:** Full QC reads the Motion `motion_spec.json`. If `output_type != "successMotionSpec"` OR `verdict not in {motion_ready}` → halt with `upstream_motion_not_ready`. Full QC never gates a reel whose motion finish did not pass Motion. A `fail` (errorEnvelope) motion spec → halt `upstream_not_success`.
- **INPUT contract:**
  - The Motion `successMotionSpec` — `motion_spec`, `motion_conform_check`, `spec_fidelity_check`, `motion_self_check` (`voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`), `finish_target.v3_final_uri`, `tier_richness_echo`, `mode_blind_confirm`, the `motion_spec_evidence_hash`.
  - The **accumulated `qc_pre_flags[]` surface** (all 12 upstream agents × ≥4 predicates — the 48+ predicate terminal surface) carried through `metadata`.
  - The **denormalized upstream chain** in `metadata.parent_chain` (11-tuple inbound from Motion, sextuply-deferred) — re-verified for evidence-hash integrity, not re-derived.
- **OUTPUT contract:** Emits `qc_report.json` per §3 (polymorphic: `successPreflightReport`-analog `successQcReport | errorEnvelope`). The Localization/Publishing tail reads the verdict + the publish handle without re-deriving QC.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| 11-point Brand Voice QC gate adjudication on the finished master (canonical from Brand Voice Intake §5 + Blueprint #14) | Per-platform aesthetic scoring (subjective creative QC) |
| Entity firewall — 13th (terminal) defense-in-depth pass over every burned-in text field + metadata surface | ML-based brand-likeness classifier (data-gated; needs the v1.0 production corpus) |
| Format-spec validation vs every `platform_variants[]` entry (aspect / duration / caption-burn parity) — DECLARED-conform | Measured-pixel / measured-fps / measured-resolution probe — needs frame-level decode (v1.1) |
| Caption-spec validation (burn-in text firewall + parity vs the EDL passthrough) | Measured-LUFS verification — Sound declared the target; the measured probe is v1.1 |
| Cumulative reel cost-ledger check vs the combined tier envelope (all upstream ceilings summed) | Auto-fix routing with patch generation (v1.0 only *routes*; does not patch) |
| `qc_pre_flags` adjudication across the FULL 12-agent chain (48+ predicate terminal surface) | Real-time human-in-the-loop review UI |
| Motion self-check adjudication (`voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`) per Blueprint §4.12 | Localization / caption-locale variant QC — activates when the Localization agent (#14) ships |
| Pass / Fail / Reshoot verdict with per-check evidence block | Reshoot-cost estimation + auto-rebook (ProdCoord round-trip automation) |
| Evidence-hash chain re-verification (motion / audio / edl hashes verify end-to-end) | Auto-publish / cross-platform scheduling — the Publishing agent (#16) owns it, v1.1 |
| 12-tuple parent_chain extension (inherits Motion 11-tuple + appends `qc_report_id`) | Multi-reel batch QC (v1.0 = one reel per invocation) |
| Terminal QC report construction (declarative per-check evidence JSON) + verdict recommendation | Publish-target rendering / encode dispatch (the actual publish compute) — v1.1 |

**Pricing tier table (full QC is universal-access; tier-FLAT in the brand gate, tier-AWARE in the cost ledger — defense-in-depth pass 13):**

| Tier | Reaches full QC? | full QC's own behavior | Cost | Gate note |
|------|-----------------|-----------------------|------|-----------|
| Pilot — Founding 5 | **YES** | 11-point gate + firewall + format/caption run identically; cost ledger reads the Pilot envelope | ~$0.00 | Pass/Fail/Reshoot on 9:16 primary |
| Starter — Operator | **YES** | Identical gate; cost ledger reads the Starter envelope | ~$0.00 | Pass/Fail/Reshoot on 9:16 primary |
| Pro — Studio | **YES** | Identical gate; cost ledger reads the higher Pro envelope; validates the richer promised variant set | ~$0.01–0.02 (optional hash re-verify) | validates 9:16 + flagged 1:1 parity |
| Enterprise — Agency | **YES** | Identical gate; cost ledger reads the Enterprise envelope; validates the richest promised variant set | ~$0.01–0.02 | validates the full promised platform-variant set |

Full QC adds **negligible** cost to every tier envelope in v1.0. Its economic value is **catch-cost avoidance at the last possible moment** — preventing a firewall breach, a format defect, a caption error, or a cost overrun from reaching a published surface (a brand-safety incident on a client's live account is the single most expensive failure the pipeline can produce; catching it here is the cheapest insurance).

---

## §2. Inputs

Full QC has **one canonical responsibility** (adjudicate terminal ship-safety) reached from **one** primary input shape — the mode-convergent finished master + motion self-check. Like QC Pre-flight (and the four post-tail executors), there is **no verdict-forking mode branch**: `production_mode` is read for context + reporting only. This is the fifth agent whose core logic is structurally mode-blind. (It reads `tier_richness_echo` for the platform-variant expectation and reads the tier envelope for the cost-ledger check — it does not fork the brand gate by tier.)

### §2.1 Precondition input — Motion motion-spec verdict (gate)

**Always read first.** The Motion `motion_spec.json`:
```json
{
  "output_type": "successMotionSpec",
  "verdict": "motion_ready",
  "reel_ref": { "motion_spec_id": "<uuid>", "audio_spec_id": "<uuid>" },
  "motion_spec": { "caption_reveals": [ /* ... */ ], "end_card": { /* brand const */ } },
  "motion_conform_check": { "all_markers_in_timeline": true, "motion_tokens_in_brand_set": true },
  "spec_fidelity_check": { "timeline_duration_matches_edl": true, "edl_evidence_hash_verified": true, "audio_spec_evidence_hash_verified": true },
  "motion_self_check": { "voice_markers_in_captions": 5, "truth_echoes": 2, "banned_vocab_hits": 0, "motion_tokens_applied": true },
  "finish_target": { "motion_processed": false, "finish_mode": "human_in_the_loop", "v3_final_uri": "ars://reels/.../v3-final.mp4" },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_v2_edit" },
  "human_review_required": true,
  "metadata": { /* 11-tuple parent_chain inbound, held additively; the accumulated qc_pre_flags surface */ }
}
```
**Hard validation:** `output_type == "successMotionSpec"` AND `verdict == "motion_ready"`. Otherwise → halt with `upstream_motion_not_ready`. A consumed `errorEnvelope` motion spec → halt `upstream_not_success`. Full QC does not gate a reel whose motion finish failed Motion, and does NOT auto-resolve a failed motion spec (the fix belongs upstream — full QC inherits the recommend-don't-override discipline, doubled: it is an adjudicator and NEVER patches).

### §2.2 Primary input — v3 master + motion self-check + accumulated flag surface (the finished reel to gate)

**Required input fields (preliminary — full schema on the Day 93/95 partials):**
```json
{
  "v3_final_uri": "ars://reels/.../v3-final.mp4",
  "motion_self_check": {
    "voice_markers_in_captions": 5,
    "truth_echoes": 2,
    "banned_vocab_hits": 0,
    "motion_tokens_applied": true
  },
  "declared_format": {
    "aspect": "9:16",
    "resolution": "1080x1920",
    "duration_ms": 62000,
    "caption_burn_in": true,
    "platform_variants": [ { "platform": "instagram", "aspect": "9:16" }, { "platform": "tiktok", "aspect": "9:16" } ]
  },
  "caption_passthrough": [ { "at_ms": 0, "text": "your calendar doesn't lie" } ],
  "cost_ledger": { "cumulative_usd": 0.00, "tier": "pro", "combined_envelope_usd": 4.50 },
  "evidence_hashes": { "motion_spec_evidence_hash": "<sha256>", "audio_spec_evidence_hash": "<sha256>", "edl_evidence_hash": "<sha256>" },
  "tier_richness_echo": { "tier": "pro", "platform_variants_promised": 2, "primary_aspect": "9:16" },
  "metadata": { /* Cross-SPEC §3.9 — tier, lever_state, brand_id, session_id, parent_chain (11-tuple inbound), the accumulated 48+ qc_pre_flags surface */ }
}
```

**Hard validations on primary input (defense-in-depth pass 13):**
1. Upstream `output_type` is `successMotionSpec`, NOT `errorEnvelope`. (errorEnvelope → `upstream_not_success`.)
2. `verdict == "motion_ready"`. Any other verdict → `upstream_motion_not_ready` (defensive — full QC cannot gate an unfinished master).
3. The `finish_target.v3_final_uri` resolves (the finished master handle exists), AND `motion_self_check.banned_vocab_hits == 0` is re-asserted at the gate (Motion declared it; full QC re-checks the passthrough text independently — the terminal firewall pass). v3 handle unresolvable → `master_unresolved`; a firewall hit on re-scan → `qc_firewall_breach`.
4. Every `platform_variants[]` entry's declared `aspect` / `duration` / `caption_burn_in` matches the tier's promised set (`tier_richness_echo.platform_variants_promised`) AND the brand format spec (§8: 9:16 / 1080×1920 / burned-in lowercase-sans). Mismatch → `format_spec_mismatch`.
5. `asset_uri`s / `v3_final_uri` remain platform-relative `ars://...` (Hard Rule #8 inherit — full QC echoes them into the publish handle; it must not introduce an absolute URL). Violation → `asset_uri_integrity_failure`.
6. `metadata.parent_chain` is a well-formed 11-tuple inbound (5→11-tuple accepted additively — see §3.3). Malformed → `qc_lineage_failure`.
7. Every one of the 12 upstream agents' `qc_pre_flags` is present (minItems-4 floor per agent) AND resolved (no flag left in an unresolved state). A missing agent's flags → `qc_flag_surface_incomplete`; an unresolved flag → `unresolved_upstream_flag`.

### §2.3 Adjudication-reference input — the 11-point Brand Voice gate + firewall + format spec (canon)

**Denormalized, read as the adjudication reference (not re-authored).** Full QC reads the Brand Voice Intake §5 (the 11 QC checks), §6 (the banned-entity firewall list), §7 (the motion/typography specs), and §8 (the reel-format spec) — used to run each of the 11 gate points against the finished master's declared conform surface, to re-scan the burned-in caption/lower-third/end-card passthrough text for banned tokens (the 13th terminal firewall pass), and to validate every `platform_variant` against the format spec. **Full QC consumes these as fixed canon facts — it adjudicates the master against them; it does NOT re-author the checks, does NOT re-derive the upstream conform (it trusts the Motion `motion_conform_check` + `spec_fidelity_check`, re-verifying only the evidence-hash chain), and does NOT decode the v3 video frame (no pixel read, no measured-format probe — declared surface + declared handle only, the same declared-spec posture as QC Pre-flight, Ingest, Edit Director, Editor, Sound, and Motion). The MEASURED probe is v1.1.**

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block: `tier`, `lever_state`, `brand_id`, `session_id`. Full QC reads `tier_richness_echo` for the platform-variant expectation (which masters + variants did this tier's plan promise? — it validates the delivered set against the promise) and reads the tier's combined cost envelope for the ledger check, and sets the report's `human_review_required: true` per Lever-3 default AND the v1.0 human-in-the-loop ship posture. It does **not** re-run cost derivation, asset validation, cut conform, creative direction, audio finish, or motion finish — those are QC Pre-flight's, Ingest's, Editor's, Edit Director's, Sound's, and Motion's authorities respectively; full QC *adjudicates* their passed verdicts and re-verifies the `motion_spec_evidence_hash` / `audio_spec_evidence_hash` / `edl_evidence_hash` chain end-to-end.

---

## §3. Outputs (skeleton)

Full QC emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 / QC Pre-flight Day 40 / Ingest Day 48 / Edit Director Day 58 / Editor Day 66 / Sound Day 74 / Motion Day 82 output pattern (`oneOf [success branch, errorEnvelope]`).

### §3.1 successQcReport branch (reel cleared to publish queue)

```json
{
  "output_type": "successQcReport",
  "verdict": "pass",
  "reel_ref": {
    "brand_id": "REINVENTED",
    "motion_spec_id": "<uuid>",
    "qc_report_id": "<uuid>"
  },
  "qc_gate": {
    "brand_voice_11_point": { "points_passed": 11, "points_total": 11, "per_point_evidence": [ /* 11 rows */ ] },
    "entity_firewall_pass_13": { "status": "pass", "text_fields_scanned": 7, "metadata_fields_scanned": 6, "hits": 0 },
    "format_spec": { "aspect_ok": true, "resolution_ok": true, "duration_in_band": true, "caption_burn_in_ok": true, "variants_match_promise": true },
    "caption_spec": { "burn_in_text_firewall_clean": true, "parity_with_edl": true },
    "cost_ledger": { "cumulative_usd": 0.00, "combined_envelope_usd": 4.50, "in_envelope": true }
  },
  "flag_adjudication": {
    "agents_reporting": 12,
    "predicates_total": 48,
    "unresolved": 0,
    "surface_complete": true
  },
  "motion_self_check_adjudication": {
    "voice_markers_in_captions": 5,
    "truth_echoes": 2,
    "banned_vocab_hits": 0,
    "motion_tokens_applied": true,
    "self_check_consistent_with_gate": true
  },
  "evidence_hash_chain": {
    "motion_spec_evidence_hash_verified": true,
    "audio_spec_evidence_hash_verified": true,
    "edl_evidence_hash_verified": true,
    "chain_intact": true
  },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_v3_master" },
  "publish_target": { "auto_published": false, "publish_mode": "human_in_the_loop", "publish_queue_uri": "ars://reels/.../qc-report.json (publish queue — pushed by the human/Publishing agent)" },
  "tier_richness_echo": { "tier": "pro", "platform_variants_promised": 2, "platform_variants_validated": 2, "primary_aspect": "9:16" },
  "handoff_targets": ["localization-agent"],
  "metadata": { /* Cross-SPEC §3.9 with QC additions per §3.3 — 12-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (reel not ship-safe)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "qc_firewall_breach",
  "failed_check_id": 8,
  "attempts": 1,
  "route_back_to": "motion-agent",
  "reel_ref": { "qc_report_id": "<uuid>" },
  "cost_incurred_usd": 0.00,
  "detail": {
    "violation": "a banned-entity token survived to the finished master's burned-in lower-third text — terminal firewall catch (13th pass)",
    "affected_fields": ["lower_third_events[1].text"],
    "recovery_path": "route back to Motion to re-spec the lower-third from a firewall-clean EDL passthrough; if the token is in the EDL source, escalate the route to Editor"
  },
  "metadata": { /* Cross-SPEC §3.9 — 12-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `pass` | 11-point gate green + firewall clean + format/caption parity + cost in-envelope + all 48 flags resolved + hash chain intact; cleared into the publish queue (held for human/Publishing-agent sign-off in v1.0) | `null` (forward to Localization/Publishing) | All gate + firewall + format + caption + ledger + flag + hash checks green |
| `fail` | The reel has a fixable defect (firewall hit, format mismatch, caption error, unresolved flag, hash break, cost overrun) that an upstream agent must fix in post | the responsible upstream agent (`motion-agent` for a finish-layer defect · `sound-agent` for an audio-finish gap · `editor-agent` for a timeline/typography-source defect · `edit-director-agent` for a plan defect) | A post-fixable defect |
| `reshoot` | The reel has a defect that NO in-post fix can resolve (unusable Mode-A footage / unusable Mode-B render surfaced only on the finished master) | `production-coord-agent` (a full production round-trip) | A production-level defect only a re-shoot / re-render can fix |

> **Defining divergence (surfaced):** Full QC carries **3 verdicts** (`pass | fail | reshoot`) — it deliberately RESTORES the third verdict the post-tail executors (Editor, Sound, Motion) each dropped. Those four are faithful executors with deterministic two-verdict postures (`ready | fail`); full QC is the fleet's terminal **adjudicator**, and the `reshoot` verdict is its defining authority — it is the ONLY post agent positioned to declare that a defect is un-fixable in post and must round-trip to production. This mirrors the QC Pre-flight three-verdict posture (`pass | fail | reshoot`) exactly — full QC is QC Pre-flight's terminal twin. It does NOT introduce a fourth `revise`/creative verdict: the creative judgment lives upstream at Edit Director, and by the time a reel reaches full QC the cut is locked, the audio finished, the graphics finished. Full QC either clears the master (`pass`), routes a fixable defect back (`fail`), or declares a production round-trip (`reshoot`). It never patches, re-cuts, re-mixes, or re-finishes — the adjudicate-don't-author discipline, at its terminal expression.

### §3.3 Metadata block additions (full QC-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **12-tuple** (inherits Motion's 11-tuple lineage + appends own `qc_report_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (RATIFIED Day 79). **Seventh forcing function**: the 12-tuple depends on the Motion 11-tuple LOCK (double-gated behind the Sound 10-tuple LOCK, itself spend-gated on the Day 81 runbook's live 5/5) behind the Editor 9-tuple LOCK (closed Day 79) behind the Edit Director 8-tuple, Ingest 7-tuple, QC 6-tuple (all closed Day 79). Encoded additively (`minItems: 5`, `prefixItems` positions 0–11, `maxItems: 12`, `items: false`) so it accepts the 5→12-tuple while rejecting a 4-tuple. The exact-N `minItems` flip to 12 is deferred to the same separately-validated hardening migration the Sound 10-tuple + Motion 11-tuple flips await. — see §5 + Open Questions.
- `qc_report_class` — enum (`terminal_preflight_pass` for a clean gate · `terminal_preflight_fail` · `terminal_preflight_reshoot`).
- `qc_report_evidence_hash` — SHA-256 over the `qc_gate` + `flag_adjudication` + `evidence_hash_chain` block (forensic, tamper-evident verdict).
- `auto_published` — `const false` in v1.0 (full QC adjudicates + queues; the human/Publishing agent pushes to the live surface. The direct analog of Motion's `motion_processed: const false`, Sound's `audio_processed: const false`, and Editor's `render_dispatched: const false` — the honest declaration that no reel was published by the agent). Flips to a real value only when the Publishing agent (#16) ships (v1.1).
- `publish_mode` — enum (`human_in_the_loop` for v1.0 · `automated` reserved for v1.1 Publishing agent). The explicit human-in-the-loop attestation.
- `qc_measured_probe_run` — `const false` in v1.0 (full QC adjudicates the DECLARED conform surface; the measured pixel/LUFS/fps probe is v1.1 — needs frame-level decode). The honest declaration that no frame was measured.
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.

### §3.4 errorEnvelope code namespace (target 8–10 LOCKED on Day 93/95 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `upstream_motion_not_ready` | Motion `verdict not in {motion_ready}` / not `successMotionSpec` | 1 | Halt — full QC never gates an unfinished master. |
| `upstream_not_success` | the consumed motion spec is `errorEnvelope` | 2 | Halt — cannot gate a failed motion-finish output. |
| `master_unresolved` | the `finish_target.v3_final_uri` (finished master) does not resolve | 3 | Hard FAIL — cannot gate a missing master; route back to Motion. |
| `format_spec_mismatch` | a `platform_variant` aspect/duration/caption-burn does not match the tier promise or the brand format spec (§8) | 4 | Hard FAIL — format parity enforced at the terminal gate; route to Motion (variant spec) or Editor (duration source). |
| `caption_spec_breach` | the burned-in caption text deviates from the EDL passthrough (parity break) or violates the one-line-at-a-time / lowercase-sans burn-in rule | 5 | Hard FAIL — caption parity enforced; route to Motion. |
| `brand_voice_gate_fail` | one or more of the 11 Brand Voice QC points fails on the finished master | 6 | Hard FAIL — the core gate; `detail` names the failing point(s); route to the responsible authoring agent. |
| `cost_ledger_overrun` | cumulative reel cost exceeds the combined tier envelope | 7 | Hard FAIL — the terminal cost check; route to Production Coord (envelope) for adjudication. |
| `qc_firewall_breach` | a banned-entity token appears in the finished master's burned-in text or metadata (13th, terminal pass) | 8 | Hard FAIL — the LAST firewall line before publish; forensic-log the field; route to Motion (finish layer) or Editor (EDL source). |
| `unresolved_upstream_flag` | one or more of the 48 accumulated `qc_pre_flags` is unresolved, OR an agent's flag surface is missing/below the minItems-4 floor (`qc_flag_surface_incomplete`) | 9 | Hard FAIL — the accumulation floor must close; `detail` names the agent + flag. |
| `evidence_hash_break` | the motion / audio / edl evidence-hash chain does not verify end-to-end | 10 | Hard FAIL — a tamper-evidence break; forensic; route to the agent whose hash broke. |
| `qc_reshoot_required` | a defect surfaced on the finished master that no in-post fix can resolve (unusable footage/render) | 11 | Hard FAIL → `reshoot` verdict; route to Production Coord — the full round-trip. |
| `qc_lineage_failure` | malformed parent_chain / broken n-tuple lineage | 12 | Forensic — audit-trail break. |
| `qc_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 93/95 LOCK:** 8–10 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping. (Preliminary list carries 11 named + lineage + catch-all; the §13 walk will confirm the routing granularity on `format_spec_mismatch` and `qc_firewall_breach` — Motion-first vs Editor-escalation — and the `qc_reshoot_required` → Production Coord round-trip, the terminal analog of QC Pre-flight's `reshoot`→ProdCoord route.)

---

## §4. Tier Constraints & Mode Coverage

**Per-tier gate access (full QC is universal-access; tier-FLAT in the brand gate, tier-AWARE in the cost ledger — restated for defense-in-depth pass 13):**

| Tier | Reaches full QC? | full QC's own gate behavior | Cost-ledger envelope read | Cost |
|------|-----------------|------------------------------|----------------------------|------|
| Pilot | **YES** | Identical 11-point gate + firewall + format/caption | Pilot combined envelope | ~$0.00 |
| Starter | **YES** | Identical 11-point gate + firewall + format/caption | Starter combined envelope | ~$0.00 |
| Pro | **YES** | Identical gate; validates richer promised variant set | Pro combined envelope | ~$0.01–0.02 |
| Enterprise | **YES** | Identical gate; validates richest promised variant set | Enterprise combined envelope | ~$0.01–0.02 |

**Why universal access + tier-FLAT brand gate (the same discipline as QC Pre-flight):** A brand-safety defect is a defect regardless of tier — an entity-firewall breach on a Pilot reel is exactly as unpublishable as on an Enterprise reel. The 11-point Brand Voice gate, the terminal firewall, and the format/caption spec run identically for every tier. The ONE tier-aware surface is the cost ledger: each tier carries a different combined production envelope (the summed AI Video Gen + Style Replication + post-tail ceilings), and full QC reads the correct envelope for the ledger check. **The finished master carries the tier envelope in its cost ledger; full QC validates against the correct one and applies the one brand gate for all.** This is the same tier-flat-gate / tier-aware-ledger discipline QC Pre-flight holds — the terminal adjudicator does not re-litigate the tier ladder for brand-safety, only for cost.

**No cost-derivation / no asset-validation / no cut-conform / no creative authority / no audio-finish / no motion-finish (the inherited discipline, sextupled):** Full QC does **NOT** re-derive the cost ledger (it reads the accumulated figure and checks it against the envelope — QC Pre-flight authored the derivation), re-validate assets (Ingest's authority), re-conform the cut (Editor's authority), re-direct the edit (Edit Director's authority), re-mix the audio (Sound's authority), OR re-finish the graphics (Motion's authority). It is six gates downstream of asset validation and one gate downstream of motion finish; re-executing any of them would be redundant and risk a double-fail on a reel already cleared through post. Full QC's authority is **terminal ship-safety adjudication** — the 11-point gate, the terminal firewall, the format/caption parity, the cost-ledger check, and the flag-surface + hash-chain closure, full stop.

**Mode coverage (mode-BLIND by inheritance — the convergence payoff, five stages deep):**

| Mode | What full QC sees | Mode-specific note |
|------|-------------------|--------------------|
| A (human footage origin) | The SAME mode-agnostic v3 master + motion self-check | Full QC reads `production_mode` for the report's context line only; the verdict logic never forks on it. |
| B (rendered + replicated origin) | The SAME mode-agnostic v3 master + motion self-check | Identical gate path. |
| C (replicated hot-path origin) | The SAME mode-agnostic v3 master + motion self-check | Identical gate path. |

**Mode-blind guarantee (the core §4 contract):** Full QC asserts `mode_blind_confirm.production_mode_read == false` in every output — a self-attestation that it adjudicated the finished master without forking the verdict on the origin mode (it may print the mode in the report's context block, but the Pass/Fail/Reshoot logic never reads it as a discriminator). This is the FIFTH machine-checkable proof that Ingest's mode-convergence seam holds — now five stages downstream, and at the TERMINAL gate. **Full QC is the fifth agent in the 17-agent fleet for which the mode columns of this table are identical; that identity, carried through the director (Edit Director) AND the timeline executor (Editor) AND the audio executor (Sound) AND the motion executor (Motion) AND now the terminal adjudicator (full QC), is the structural evidence that the entire post-production tail — from ingest to publish gate — is genuinely mode-agnostic end-to-end.** If full QC ever NEEDED to fork the verdict on mode to gate ship-safety, the convergence contract would be broken upstream. By construction it never does — the finished master is the same shape regardless of how the pixels were born.

---

## §5. Process Steps (System Prompt Skeleton — Day 93 §7 will LOCK)

The agent runs a **12-step gate loop** per invocation (extends the AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion 11-step process pattern by one — the terminal gate adds the flag-surface-closure step). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope. Unlike the executors, full QC runs ALL non-halting checks even after a soft flag (to produce a complete per-check evidence block), and only hard-halts on a precondition/lineage/hash break.

**Step 1 — Verify Motion precondition + parse input**
- Read the Motion `motion_spec.json`. Confirm `output_type == "successMotionSpec"` AND `verdict == "motion_ready"`. Otherwise → halt with `upstream_motion_not_ready`.
- Parse input JSON against `input.schema.json` (Day 93/95 LOCKED). There is NO mode branch — assert the v3 master + motion self-check is the mode-agnostic shape.
- Confirm the consumed motion spec is the success branch. Any `errorEnvelope` upstream → halt with `upstream_not_success`.

**Step 2 — Lineage integrity**
- Validate `metadata.parent_chain` is a well-formed 11-tuple inbound (5/6/7/8/9/10/11-tuple accepted additively under the ratified §3.9 amendment). Malformed → `qc_lineage_failure`.

**Step 3 — Evidence-hash chain re-verification**
- Re-verify the `motion_spec_evidence_hash`, `audio_spec_evidence_hash`, and `edl_evidence_hash` chain end-to-end (each hash re-computed over its source block and matched). Any break → `evidence_hash_break` (forensic; the terminal tamper check).

**Step 4 — Master resolution**
- Confirm `finish_target.v3_final_uri` resolves (the finished master handle exists). Unresolvable → `master_unresolved` (route to Motion).

**Step 5 — 11-point Brand Voice gate**
- Run each of the 11 Brand Voice QC points (Brand Voice Intake §5) against the finished master's declared conform surface + the motion self-check. Any point fails → record it; the gate hard-fails on any point → `brand_voice_gate_fail` with `detail` naming the failing point(s).

**Step 6 — Terminal entity firewall (13th pass)**
- Re-scan every burned-in caption / lower-third / super / end-card text field AND every metadata surface against the banned-entity list (Brand Voice Intake §6). Any hit → `qc_firewall_breach` (forensic-log the field; the LAST firewall line before publish). Independently re-derives `banned_vocab_hits`; a mismatch with Motion's declared `0` also flags.

**Step 7 — Format + caption spec parity**
- Validate every `platform_variants[]` entry's aspect/duration/caption-burn against the tier promise + the brand format spec (§8). Mismatch → `format_spec_mismatch`.
- Validate the burned-in caption text has parity with the EDL passthrough + obeys the one-line-at-a-time / lowercase-sans burn-in rule. Break → `caption_spec_breach`.

**Step 8 — Cumulative cost-ledger check**
- Read the accumulated `cost_ledger.cumulative_usd` and check it against the tier's `combined_envelope_usd`. Overrun → `cost_ledger_overrun` (route to Production Coord for envelope adjudication).

**Step 9 — Flag-surface closure (the terminal-gate step)**
- Confirm all 12 upstream agents' `qc_pre_flags` are present (minItems-4 floor per agent = 48+ predicate surface) AND resolved. A missing/short surface → `qc_flag_surface_incomplete`; an unresolved flag → `unresolved_upstream_flag`. This is the step the §3.4 accumulation floor was provisioned for.

**Step 10 — Motion self-check adjudication**
- Adjudicate the Motion `motion_self_check` (`voice_markers_in_captions` · `truth_echoes` · `banned_vocab_hits` · `motion_tokens_applied`) for consistency with the gate's independent findings. An inconsistency (e.g. Motion declared `banned_vocab_hits: 0` but Step 6 found a hit) escalates the firewall/gate fail.

**Step 11 — Verdict synthesis + reshoot determination**
- Synthesize the Pass/Fail/Reshoot verdict: `pass` iff every check green; `fail` for a post-fixable defect (route to the responsible upstream agent); `reshoot` iff a defect surfaced that no in-post fix can resolve (route to Production Coord). Emit per-check evidence for all 11 gate points + firewall + format + caption + ledger + flags + hashes.

**Step 12 — Mode-blind self-attestation + publish-queue handoff**
- Assert `mode_blind_confirm.production_mode_read == false`. On `pass`, write the `qc_report.json` + the publish-queue handle (`auto_published: false`, `publish_mode: human_in_the_loop`) to the Drive `/reels/[reel_id]/` publish queue; `handoff_targets: ["localization-agent"]` (holding-store default until the Localization agent #14 ships). Set `human_review_required: true`.

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 93 + 95)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 93 partial 1. Pattern source: QC Pre-flight §6 / Motion §6. Target 12–14 checks bipartite-covering the 8–10 errorEnvelope codes (one more than Motion's 10–12, reflecting the terminal gate's larger surface). Slot 11+ reserved for `qc_agent_failed` per Cross-SPEC §3.6 slot-naming canon. Checks span: precondition + motion-spec-evidence verify · lineage · evidence-hash-chain re-verify · master resolution · 11-point gate adjudication · terminal firewall (13th pass) · format-spec parity · caption-spec parity · cost-ledger closure · flag-surface closure (the 48-predicate check) · motion-self-check adjudication · mode-blind self-attestation.
- **§7 System Prompt v1.0** — Day 93 partial 1. Frame + hard rules + universal-tier-FLAT-gate / tier-aware-ledger table + 12-step gate loop verbatim from §5 + the Blueprint §4.13 qc-report/publish-handle target shape inlined + the 11-point Brand Voice gate (§5) + the banned-entity firewall list (§6) + the reel-format spec (§8) as the enforced adjudication surface. ~14–16 KB target (the largest system prompt in the fleet — the terminal gate carries the most checks). Hard Rules mirror QC Pre-flight with full-QC-specific tightening on "adjudicate-never-patch," "route-back-never-fix," and "recommend-never-auto-publish (auto_published const false)" discipline.
- **§8 Performance Targets** — Day 95 partial 2. 9 metric categories. Schema validity 100% / firewall catch 100% (a banned token must never survive the terminal pass) / 11-point-gate adjudication 100% / format-spec parity 100% / caption-spec parity 100% / flag-surface-closure 100% / evidence-hash-chain verify 100% / false-pass rate 0% target (a false pass ships a defect — the single most costly failure direction) / false-fail rate ≤ 6% (over-flagging a borderline reel to `fail`/`reshoot` is the acceptable failure direction — tighter than Motion's ≤8% because the terminal gate is the last line) / p50 latency 30s / p95 90s (the largest reasoning surface in the fleet — 11 points + firewall + format + caption + ledger + 48 flags) / zero engine + zero render + zero decode cost.
- **§9 Test Fixtures** — Day 95 partial 2. 5-fixture portfolio: TC-01 clean Mode-origin-A→motion-spec Pro `pass` (full 11-point gate green) · TC-02 Mode-origin-C Enterprise `pass` (proves mode-blind: byte-identical gate path to TC-01 despite different origin — the **mode-blind gate-convergence proof**, the full-QC analog of Motion's finish-convergence proof, FIVE stages deep) · TC-03 `format_spec_mismatch` → fail + route to Motion (a platform variant not matching the tier promise) · TC-04 `unresolved_upstream_flag` → fail + route to the responsible agent (an upstream `qc_pre_flag` left unresolved — the accumulation-floor catch, the check unique to the terminal gate) · TC-05 `qc_firewall_breach` (a banned token surviving to the finished master's burned-in text — the 13th terminal-pass last-line catch; GATING fixture). 5 of 8–10 codes exercised; remainder in schema-only fixtures. Optional probes: the `qc_reshoot_required`→ProdCoord round-trip (the `reshoot`-verdict fixture, unique to the adjudicator) + the `evidence_hash_break` forensic catch + the slot `qc_agent_failed` catch-all.
- **§10 Field Map** — Day 93 partial 1. ~26 rows · passthrough vs transform vs derived. motion-self-check→adjudication map + 11-point-gate→per-point-evidence map (derived) + firewall-scan→hit-record map + format-variant→parity-check map (transform) + cost-ledger→envelope-check map + flag-surface→closure map (the 48-predicate adjudication) + evidence-hash→chain-verify map + derived verdict/report map.
- **§11 Cost Model** — Day 95 partial 2. Zero engine + zero render + zero decode snapshot (gate reasoning + report authoring only; the optional evidence-hash re-verify is the only marginal cost, ~$0.01–0.02). Catch-cost-avoidance value model (economic justification = a brand-safety incident on a client's live surface is the single most expensive pipeline failure; the terminal gate is the last, cheapest insurance against it). Explicit note: the measured pixel/LUFS/fps probe lands in v1.1 (needs frame-level decode) — v1.0 is $0 by construction, adjudicating the declared surface + re-verifying the hash chain.
- **§12 Verdict Math** — Day 95 partial 2. PASS = (Motion precondition met) ∧ (lineage well-formed) ∧ (evidence-hash chain intact) ∧ (master resolved) ∧ (11-point gate all green) ∧ (terminal firewall clean) ∧ (format-spec parity) ∧ (caption-spec parity) ∧ (cost in-envelope) ∧ (all 48 flags resolved) ∧ (motion self-check consistent). Any single ∧-term false → `fail` per §3.2, UNLESS the defect is un-fixable in post → `reshoot` (the adjudicator's third verdict). The pass/fail split is deterministic; the fail-vs-reshoot determination is the one judgment slot (is the defect post-fixable or production-level?) — the terminal adjudicator's defining decision, mirroring QC Pre-flight's fail-vs-reshoot slot.
- **§13 Critical Decisions LOCKED** — Day 95 partial 2. Target 12–16 LOCKED decisions. Pre-scaffolded list:
  1. Gate-adjudication vs patch scope — v1.0 = adjudicate + route ONLY; full QC NEVER patches, re-cuts, re-mixes, or re-finishes. It emits a verdict + routes back. [LOCKED-as-drafted Day 92]
  2. Adjudicator, not executor — full QC reads the passed upstream verdicts + conform checks, re-verifying only the evidence-hash chain; it re-derives no upstream conform. [LOCKED-as-drafted Day 92]
  3. Three-verdict (RESTORE `reshoot`) — full QC is the terminal adjudicator; `pass | fail | reshoot`. The `reshoot` verdict (route to ProdCoord) is its defining authority — the only post agent that can declare a defect un-fixable in post. Mirrors QC Pre-flight. [LOCKED-as-drafted Day 92]
  4. Mode-blind by inheritance — no `production_mode` verdict fork; `mode_blind_confirm.production_mode_read: false` self-attested (the fifth mode-blind agent; mode read for the report context line only). [LOCKED-as-drafted Day 92]
  5. Motion-ready precondition — full QC runs only on a `successMotionSpec`/`motion_ready` reel; otherwise halts `upstream_motion_not_ready`. [LOCKED-as-drafted Day 92]
  6. Tier-FLAT brand gate / tier-AWARE cost ledger — all 4 tiers reach full QC; the 11-point gate + firewall + format/caption run identically; only the cost-ledger envelope is tier-read. [LOCKED-as-drafted Day 92]
  7. 12-tuple parent_chain — inherits Motion 11-tuple + appends `qc_report_id`; SEVENTH forcing function (depends on the Motion 11-tuple LOCK, double-gated behind the Sound 10-tuple LOCK, itself spend-gated on the Day 81 runbook 5/5; the §3.9 amendment is already RATIFIED Day 79). [DEFERRED — held additively at `minItems: 5`]
  8. errorEnvelope code count — 8–10 target; routing granularity on `format_spec_mismatch` / `qc_firewall_breach` (Motion-first vs Editor-escalation) + the `qc_reshoot_required`→ProdCoord route. [PRELIMINARY · operator amend Day 95]
  9. Self-QC check count — 12–14 (one more than Motion, reflecting the terminal surface). [PRELIMINARY · operator amend Day 95]
  10. False-PASS = ZERO tolerance — a firewall breach, format defect, caption error, unresolved flag, hash break, or cost overrun must NEVER survive to `pass`; the terminal gate's false-pass rate target is 0% (a false pass ships a brand-safety defect to a live client surface). [LOCKED-as-drafted Day 92]
  11. Terminal entity firewall (13th pass) — full QC re-scans every burned-in text field + metadata surface at the terminal boundary, the LAST firewall line before publish; independently re-derives `banned_vocab_hits` (does not trust Motion's declared count). [LOCKED-as-drafted Day 92]
  12. No engine, no render, no decode, no measured probe — NO generative engine, NO render, NO byte-level video decode, NO measured pixel/LUFS/fps probe in v1.0; declared conform surface + hash-chain re-verify only; `qc_measured_probe_run: const false`, `cost_incurred_usd ~$0.00–0.02`. [LOCKED-as-drafted Day 92]
  13. Flag-surface-closure = the terminal-gate step — full QC is the second + final consumer of the §3.4 minItems-4 accumulation floor; it adjudicates the full 48-predicate surface and hard-fails any unresolved/short flag. [LOCKED-as-drafted Day 92]
  14. Recommend-never-auto-publish — full QC emits a Pass verdict + a publish-queue handle; the human/Publishing agent pushes to the live surface. `auto_published: const false`. [LOCKED-as-drafted Day 92]
  15. Handoff to the Localization/Publishing tail — full QC hands the qc report + publish handle to the Drive publish queue (holding store) until the Localization agent #14 ships (Blueprint §4.13). [PRELIMINARY · operator amend Day 95]
  16. Triple-gated LOCK — full QC's own v1.0 LOCK sequences strictly AFTER the Sound LOCK, then the Motion LOCK, then its own 5/5 (the fleet's first TRIPLE-gate). [LOCKED-as-drafted Day 92]

- **§14 Calendar status updates** — Day 93 partial 1. Day 92 ✓ → trajectory populated.
- **§15 Change Log** — Day 95 partial 2. v1.0 lifecycle entries (outline-day-92 → body-day-93 → body-day-95 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 95 partial 2. Cross-SPEC §3.9 canonical fields + 7 full-QC additions (12-tuple parent_chain, qc_report_class, qc_report_evidence_hash, auto_published const false, publish_mode, qc_measured_probe_run const false, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `qc-agent` (kebab-case, matches the fleet pattern + Blueprint §4.12/§4.13 handoff target — distinct from `qc-preflight-agent`) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `qc_report_evidence_hash` SHA-256 over the qc_gate + flag_adjudication + evidence_hash_chain block; the motion/audio/edl evidence-hash chain re-verified end-to-end (inherits + terminally closes the Editor + Sound + Motion anchors) |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` (3-value) + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ **Full QC is the second + terminal CONSUMER of the floor** — it adjudicates the full 12-agent, 48+ predicate accumulated surface and hard-fails any unresolved/short flag (the closure the floor was provisioned for) |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-BLIND table — the fifth agent for which the mode columns are identical (the convergence payoff, five stages deep, at the terminal gate) |
| §3.6 Slot 11 naming canon | ✅ Reserved `qc_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Consumed shapes respected; full QC's own gate predicates snake_case |
| §3.8 Tier↔mode firewall (13th defense-in-depth) | ✅ Step 6 TERMINAL entity firewall (the LAST firewall line before publish) + §4 universal-tier-FLAT-gate / tier-aware-ledger table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 12-tuple, held additively. **Seventh forcing function** — gated on the Motion 11-tuple LOCK (double-gated behind the Sound 10-tuple LOCK, spend-gated on the Day 81 runbook 5/5); the §3.9 amendment itself is RATIFIED (Day 79). |
| §3.10 Cost ceiling authority | ✅ §4 explicitly DECLINES to re-derive cost (reads the accumulated figure + checks the envelope — QC Pre-flight's derivation), re-validate assets (Ingest's), re-conform the cut (Editor's), re-direct the edit (Edit Director's), re-mix the audio (Sound's), OR re-finish the graphics (Motion's) — no sextuple-enforcement; full QC is ~$0-cost in v1.0 |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 92 outline — 6 parked for operator amendment)

1. **Gate-adjudication-only vs partial-patch scope** — v1.0 adjudicates + routes back; it NEVER patches a defect. Confirm v1.0 stops at the verdict + route (no auto-fix, no patch generation — that is a deferred v1.1 auto-fix-routing feature the QC Pre-flight outline also deferred). *(Donna recommends: confirm adjudicate-and-route-only for v1.0 — the verdict + evidence block is the buildable, highest-leverage, $0 slice; auto-patch generation is a Week-4–5 feature that risks the terminal gate silently "fixing" a defect it should route back, exactly the override the adjudicate-don't-author boundary forbids.)*
2. **Three-verdict (restore `reshoot`)** — should full QC restore the `reshoot` verdict the post-tail executors dropped, mirroring QC Pre-flight? *(Donna recommends: restore three-verdict — full QC is the terminal adjudicator and the only post agent positioned to declare a defect un-fixable in post; without `reshoot`, an unusable-footage defect discovered on the finished master would have no correct route. `pass | fail | reshoot`, exactly QC Pre-flight's posture.)*
3. **12-tuple parent_chain** — seventh forcing function (depends on the Motion 11-tuple LOCK, double-gated behind the Sound 10-tuple LOCK, itself spend-gated on the Day 81 runbook 5/5; the §3.9 amendment is already RATIFIED Day 79). Full QC is the first 12-tuple consumer. *(Donna recommends: hold additively at `minItems: 5` until the Motion 11-tuple LOCKs; the exact-N flip to 12 folds into the same separately-validated hardening migration the Sound 10-tuple + Motion 11-tuple flips await.)*
4. **Measured probe vs declared-surface scope** — v1.0 adjudicates the DECLARED conform surface (Motion's self-check, the declared format/caption/cost) + re-verifies the hash chain; the measured pixel/LUFS/fps probe needs frame-level decode. Should the measured probe be in v1.0 or deferred? *(Donna recommends: defer the measured probe to v1.1 — frame-level decode is the same $-and-render surface the whole fleet defers to v1.1 automation; v1.0 adjudicating the declared surface + the hash chain is the buildable $0 slice, and Motion's self-check + the upstream conform checks already assert the declared facts. The measured probe is the belt-and-suspenders v1.1 layer.)*
5. **Handoff readiness** — full QC hands to the not-yet-built Localization agent (#14) → Publishing (#16). Should v1.0 emit the qc report + publish handle to a holding store (the Drive `/reels/[reel_id]/` publish queue, per Blueprint §7 I/O) until the Localization/Publishing tail ships, or assume direct handoff? *(Donna recommends: emit to the Drive publish queue in v1.0; direct agent-to-agent handoff activates when the Localization agent LOCKs — mirrors the Motion→finish-queue and Sound→finish-queue holding-store decisions.)*
6. **Firewall-count independence — trust vs re-derive Motion's `banned_vocab_hits`** — v1.0 re-scans the burned-in text independently (Step 6) rather than trusting Motion's declared `banned_vocab_hits: 0`; is an independent terminal re-derivation the right posture, or is trusting the upstream self-check sufficient? *(Donna recommends: ratify independent re-derivation for v1.0 — full QC is the LAST firewall line before a live client surface; the entire value of a terminal gate is that it does NOT trust the upstream self-report on the one check that ships brand-safety incidents. It re-scans, and flags any mismatch with the declared count as an escalation. This is the terminal gate's defining discipline.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (full QC trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 92 | Mon Jul 20 | **SPEC outline §0–§5** [SHIPPING NOW] | Motion Day 82 outline |
| 93 | Tue Jul 21 | SPEC body partial 1: §6 + §7 + §10 + §14 | Motion Day 83 / QC Pre-flight Day 41 |
| 95 | Thu Jul 23 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | Motion Day 85 / QC Pre-flight Day 43 |
| 96+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | Motion Day 86–90 / Sound Day 78–81 |
| 98 | Sun Jul 26 | **REST DAY** — no build (pre-stage next scaffold only) | Day 21/28/…/91 Rest Day compounding (15th) |

**Sprint context:** full QC is **Agent #13** — the sixth post-production agent and the FIRST *adjudicator* agent in the post tail, the 13th (terminal) defense-in-depth firewall and the **fifth contractually mode-blind agent** (the continued proof of Ingest's convergence seam, five stages deep). It is the terminal ship-safety gate — the last automated check before a reel reaches a published surface — and it closes the deferral QC Pre-flight deliberately opened at Day 40 ("the full #14 gate, post-Motion, built once the in-post fleet ships"). The in-post fleet has now shipped. In v1.0 it produces NO media and publishes NOTHING: it adjudicates the finished master's declared conform surface + the 48-predicate flag stack + the hash chain and emits a Pass/Fail/Reshoot verdict the human ratifies (measured probe + auto-publish deferred to v1.1), keeping the zero-dollar / no-render / no-decode / no-publish invariant intact. The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) shipped on the six production agents through the QC Pre-flight gate; full QC's v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the Motion, Sound, Ingest, QC Pre-flight, Style Replication, Edit Director, and Editor outlines were (while their predecessor LOCKs remained gated — full QC's LOCK here triple-gated behind the Sound + Motion LOCKs, both spend-gated on live 5/5 runs).

---

## Files produced today (Day 92)

- `ars/ARS-2026-07-20-Day-92-Full-QC-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-07-20.md` — Day 92 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 92)

- ✅ **No LLM dispatched.** No render API. No motion-graphics render. No engine credentials referenced. No vendor URLs walked. No media render, no byte-level video decode, no frame analysis, no measured pixel/LUFS/fps probe. (Full QC by design adjudicates a declared conform surface + re-verifies the evidence-hash chain in v1.0 — the measured probe is the Week 4–5 v1.1 scope.)
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no client/investor outreach. The end-of-run status digest to Jamila's Google Voice self-thread ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, no render compute, zero $ spent. (`jsonschema` 4.26.0 re-validation was a PyPI install with no vendor/engine surface, $0.)
- ✅ **No operator-impersonation.** Neither the Sound v1.0 LOCK nor the Motion v1.0 LOCK ceremony was performed — the Sound gate is a live, reproducible 5/5 run of the Day 81 runbook (~$3.50 Opus), and the Motion LOCK is double-gated (Sound LOCK first, then the Motion Day-90 runbook 5/5, ~$3.75 Opus); both are forbidden under the $0 unattended ceiling; locking either on the offline stamp alone would be a fake-advance (refused). Sound + Motion stay LOCK CANDIDATE. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED. The §3.9 amendment (ratified Day 79) NOT re-committed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. Full QC v1.0 LOCK will hard-gate itself on the upstream LOCKs (the Sound 10-tuple, then the Motion 11-tuple) being closed first — the fleet's first TRIPLE-gate.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched. Offline fleet regression sweep re-run: **434/434 (8 bundles), 0 drift.**
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 6 enumerates HC/NPOX tokens precisely so the agent can BLOCK them at the terminal gate — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Motion Day 82 outline structure inherited verbatim; QC-domain grounding from the QC Pre-flight Day 40 outline §1. Orchestration Blueprint §1.2 / §2 / §4.12 / §4.13 / §6 / §7 / §9 (Agent 14 QC definition) + Cross-SPEC §3 canon + Brand-Voice Intake §5–§8 used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-92 build runs Monday (Pacific); the prior Rest Day (Day 91, Sun Jul 19) was observed (14th). Next Rest Day: Day 98 (Sun Jul 26 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 92 ships clean. Day 93 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). Full QC is Agent #13 of 17 — the 13th (terminal) defense-in-depth firewall and the FIRST adjudicator agent in the post tail, the fifth contractually mode-blind agent and therefore the continued proof that Ingest's mode-convergence seam holds five stages deep. It is the terminal ship-safety gate — the last automated check before publish — and it closes the deferral QC Pre-flight opened at Day 40. In v1.0 it produces no media and publishes nothing, adjudicating the finished master's declared conform surface + the 48-predicate flag stack + the evidence-hash chain and emitting a Pass/Fail/Reshoot verdict the human ratifies (measured probe + auto-publish deferred to v1.1), keeping the zero-dollar / no-render / no-decode / no-publish invariant intact. Operator pickup: (1) the Sound v1.0 LOCK remains the immediate forward step — its gate is a live, reproducible 5/5 run of the Day 81 runbook (~$3.50 Opus) that the $0 overnight cannot execute; then the Motion 5/5 + LOCK (~$3.75 Opus, double-gated behind Sound); both runnable in Jamila's iMac sit-down OR an attended, spend-authorized Donna run under the standing authorization; the Motion 11-tuple is full QC's direct 12-tuple dependency; (2) review the §13 critical-decisions list — the §3.9 n-tuple amendment is already RATIFIED (Day 79), so full QC inherits n-tuple lineage cleanly (seventh forcing function, held additively until the Motion 11-tuple LOCKs); (3) confirm the Agent #13 = full QC selection (or re-assign the slot) at the Sound/Motion LOCK close. Neither the Sound nor the Motion v1.0 LOCK was performed tonight — locking on the offline stamp alone, absent the live 5/5s, would be a fake-advance; both stay in the spend-gated queue. Full QC's own LOCK is the fleet's first TRIPLE-gate: Sound LOCK → Motion LOCK → full QC 5/5.*
