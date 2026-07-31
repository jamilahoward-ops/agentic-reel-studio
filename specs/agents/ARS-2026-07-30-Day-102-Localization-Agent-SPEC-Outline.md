# ARS — Localization Agent v1.0 SPEC OUTLINE (§0–§5)

**Entity:** Sequel Digital Solutions → Agentic Reel Studio
**Authored:** Day 102 · Thu Jul 30, 2026 (Pacific) · overnight build session (Donna)
**Deliverable class:** Forward SPEC outline §0–§5 (the head-start design for Agent #14 of 17 — the FIRST Distribution-stage agent)
**Status:** OUTLINE ONLY — no LOCK, no schema, no SKILL bundle. Body partials author Days 103 + 104 per the §0 calendar (both pre-Rest Day this week, the Sound Day 74/75/76 + full-QC Day 92/93/95 pre-Rest Day pattern; the Week-15 Rest Day is Day 105 · Sun Aug 2).
**Pattern source:** full QC Day 92 outline (`ARS-2026-07-20-Day-92-Full-QC-Agent-SPEC-Outline.md`) — section structure inherited verbatim. Executor-lineage grounding from the Motion Day 82 outline (`ARS-2026-07-10-Day-82-Motion-Agent-SPEC-Outline.md`) §1 (the finish-executor `*_processed: const false` declared-surface / no-render discipline) and the Editor Day 66 outline (the two-verdict executor posture + `render_dispatched: const false`). Orchestration Blueprint §1.5 (Agent 15 row: *"Localization — Optional. Generates caption variants for cross-platform (IG vs TT vs LI vs Shorts). Handles vertical-to-horizontal crops if needed."*), §2 swim-lane (position 15 between QC and Publishing, marked **optional**), §4.13 (QC→Lever Router→15 handoff: on `PASS` + Lever approval → 15 Localization), §4.14-adjacent (15→16 Publishing payload), §5 hard-blocker note (*"14 QC blocks 15/16"*) + soft-dependency note (*"15 Localization is optional — can skip for single-platform reels"*), §6 dispatch table (row 15: *"On Lever approval (if multi-platform variants needed) · Per reel · Approved final"*), §7 read/write contract (row 15: Localization reads *v3 final*, writes *Drive: platform variants folder*). Brand-format grounding from `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §6 (the banned-entity firewall list — re-invoked over any NET-NEW caption-variant text Localization authors) + §8 (the reel-format spec: 9:16 · 1080×1920 · burned-in lowercase-sans captions one line at a time · end-card serif ivory 1.5s — the master-format baseline each platform variant is derived FROM). Full QC handoff shape from the Day-96 full-QC LOCK candidate `publish_target` block (`auto_published: false` · `publish_mode: human_in_the_loop` · `publish_queue_uri` · `handoff_targets: ["localization-agent"]`) + `tier_richness_echo` (`platform_variants_promised` · `platform_variants_validated` · `primary_aspect`) — the promised-vs-delivered variant contract Localization fulfills.

> **Agent-selection note (Donna, surfaced not hidden):** The Day 101 full-QC LLM-Test-Runbook close named the forward build as **"the Sound v1.0 LOCK (live 5/5, ~$3.50 Opus) … then Motion LOCK, then full QC LOCK; then the Localization Agent #14 SPEC outline."** The three named LOCK items (Sound, then Motion, then full QC) are each gated on a **live, reproducible 5/5 LLM run** (~$3.50 / $3.75 / $4.25 Opus, in strict order — the fleet's first triple-gate), which the **absolute $0 ceiling of this unattended overnight session forbids**. Locking any of the three on the offline structural `validate.py` stamp alone, absent a real live 5/5, would be a **fake-advance** — the exact move every prior log deliberately refused, and which the standing guardrail ("never fake-advance — no LOCK without a real 5/5 run behind it") prohibits. With all three post-tail LOCK items spend-gated and un-executable at $0, the buildable forward deliverable is the **Localization #14 SPEC outline** — the fourth, explicitly named item on that same Day-101 "Next" line, pulled into the $0 slot. This is the **identical forward-looking basis** on which every prior outline was authored (Sound Day 74, Motion Day 82, full QC Day 92, Ingest, QC Pre-flight, Style Replication, Edit Director, Editor — each authored while its predecessor LOCK remained gated). **Direct precedent for the slot:** Sound runbook Day 81 → Motion outline Day 82 (the next build night, before Sound was LOCKED); Motion runbook Day 90 → full QC outline Day 92 (the next non-Rest Day build night after the Day 91 Rest Day). full QC runbook Day 101 → Localization outline Day 102 (the next build night) maps that precedent exactly. Surfaced here, not silently reconciled. The Sound v1.0 LOCK remains the immediate operator/attended-spend action, then Motion, then full QC — see §13-preview + the Day 102 build log. Rationale for Localization as the #14 build: (1) **strict dependency order** — Localization is the immediate runtime stage downstream of full QC (Blueprint §4.13: *"PASS + Lever approval → 15 Localization"*), consuming the `successQcReport` / `pass` verdict + the `publish_target` handle + the `tier_richness_echo` promised-variant contract full QC authors; (2) **it opens the Distribution stage** — the entire post-production tail (Ingest → Edit Director → Editor → Sound → Motion → full QC) is now built through its runbook; Localization is the FIRST agent of the two-agent Distribution stage (Blueprint §1.5), the bridge from the finished-and-cleared master to the published surface; (3) **the executor pattern resumes** — Localization inherits the Motion/Editor/Sound *author-a-declared-spec, render-nothing* seam (it authors the per-platform variant spec + crop spec and emits a two-branch verdict; it crops no pixel, re-encodes no frame, burns no caption, calls no engine), keeping the zero-dollar / no-render invariant intact one stage deeper; (4) **sixth mode-blind agent** — it inherits the Edit Director→Editor→Sound→Motion→full-QC mode-agnostic lineage, the continued proof that Ingest's convergence seam holds SIX stages deep, now at the Distribution boundary. Operator may re-assign the #14 slot at the Sound/Motion/full-QC LOCK close.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 15 — Distribution stage open (QC-cleared v3 master → per-platform variant + crop SPEC → publish-ready manifest for the Publishing agent) |
| Agent index | **#14 of 17** (build sequence — continues the full QC Day 92 "agent #13 of 17" framing) |
| Runtime pipeline position | **15 — Localization** (the OPTIONAL cross-platform variant author: given a full-QC-`pass` + human/Lever-approved v3 master, authors the per-platform caption-variant spec (IG / TikTok / LinkedIn / Shorts) + the vertical-to-horizontal / square crop spec for each requested platform beyond the primary, re-invokes the entity firewall over any NET-NEW caption-variant text it authors (the 14th, scoped defense-in-depth pass), and emits a single `variants_ready` (multi-platform) or `not_required` (single-platform pass-through) verdict + a platform-variant manifest; receives the QC report + publish handle from full QC, hands the variant manifest + the master handle to the Publishing agent (#16)) |
| Pipeline tier | **DISTRIBUTION EXECUTOR — the FIRST of two Distribution agents (Localization #14 → Publishing #16-runtime), and the FIRST OPTIONAL agent in the fleet.** Distinct from the post-production executors (Editor / Sound / Motion finish the master IN PLACE); Localization does not touch the cleared master — it authors *derivative* per-platform variant specs alongside it. Its optionality is a first-class contract property: for a single-platform reel it is a clean pass-through (`not_required`), forwarding the QC-cleared master straight to Publishing. |
| Mode coverage | **Mode-blind by inheritance** — authors variants from the mode-convergent v3 master + the full-QC `pass` verdict (themselves derived from the mode-agnostic v2 edit → mode-agnostic audio spec → mode-agnostic EDL → mode-agnostic Asset Manifest, and adjudicated by a mode-blind terminal gate); reads `production_mode` for **context + reporting only** (like full QC and the four executors), never as a variant-fork discriminator. The **SIXTH** contractually mode-blind agent (Edit Director first, Editor second, Sound third, Motion fourth, full QC fifth); the continued live proof that Ingest's convergence seam holds six stages deep, now at the Distribution boundary. |
| Predecessor SPEC (gate) | `ARS-2026-07-24-Day-96-Full-QC-Agent-v1-LOCK-CANDIDATE.md` (Day 96 LOCK candidate — its v1.0 LOCK is triple-gated: the Sound LOCK, then the Motion LOCK, then full QC's own Day 101 runbook live 5/5). Localization runs only on a full-QC-passed (`successQcReport`, verdict `pass`) + Lever/human-approved reel. |
| Predecessor schemas | `ARS-2026-07-25-QC-Agent-output.schema.json` (Day 97, full QC output) — the `successQcReport` (`verdict: pass` · `qc_gate` · `publish_target` {`auto_published: false` · `publish_mode` · `publish_queue_uri`} · `tier_richness_echo` {`platform_variants_promised` · `platform_variants_validated` · `primary_aspect`} · `mode_blind_confirm` · `qc_report_evidence_hash`) consumed as the primary INPUT. Plus the accumulated upstream success handles (the Motion `finish_target.v3_final_uri`) referenced only for the master handle + the denormalized evidence-hash re-verification, NOT re-derived. |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape (§3.3/§3.8), metadata block + n-tuple parent_chain (§3.9), and the `qc_pre_flags` minItems-4 accumulation floor (§3.4 — Localization appends its own ≥4 variant-flag predicates to the surface it forwards) all inherited. |
| Brand-format canon | `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md` §6 (the banned-entity firewall list — the regex Localization re-invokes over any NET-NEW caption-variant text it authors, the scoped 14th pass), §8 (the reel-format spec: 9:16 · 1080×1920 · burned-in lowercase-sans captions one line at a time · end-card serif ivory 1.5s — the master-format baseline every platform variant is derived FROM; a horizontal/square crop must preserve the caption-safe and end-card-safe regions) — the distribution rules the variant author honors faithfully |
| Defense-in-depth layer | **14th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → QC Pre-flight → Ingest → Edit Director → Editor → Sound → Motion → full QC → **Localization**) — a **SCOPED, ADDITIVE** pass: it does NOT re-scan the already-cleared master (full QC is the terminal firewall on the master — that claim stands); it scans ONLY the NET-NEW per-platform caption-variant / description text Localization itself authors, text that did not exist when full QC ran. The firewall guarantee therefore extends to derivative text without contradicting full QC's terminal-on-the-master authority. Any hit → the variant author never ships a banned token into a new platform caption. |
| Lever inheritance | Reads `lever_state` from upstream `metadata` AND the full-QC `publish_target` (which encodes the human/Lever approval that gates entry per Blueprint §4.13). Emits `human_review_required: true` per Lever-3 default AND per the v1.0 human-in-the-loop ship posture (Blueprint §9). Localization authors variant specs a human ratifies before Publishing pushes; it publishes nothing and renders nothing. |
| Pricing tier authority | **ALL tiers — but tier-GATED in scope (this is where "optional" bites).** Every reel passes THROUGH Localization, but most low-tier reels pass through as `not_required`. Localization reads `tier_richness_echo.platform_variants_promised`: Pilot / Starter typically promise a single primary 9:16 master → `not_required` pass-through; Pro promises 9:16 + a flagged 1:1 → authors the 1:1 crop + caption variant; Enterprise promises the richest cross-platform set → authors the full variant fan-out. **Tier-AWARE in the variant set, tier-FLAT in the firewall + crop-safety rules** (the banned-entity scan + the caption-safe/end-card-safe region preservation run identically for every authored variant regardless of tier). |
| Cost authority class | **Near-zero (ties Ingest / QC Pre-flight / Edit Director / Editor / Sound / Motion / full QC for lowest in fleet) IN v1.0** — pure reasoning + variant-spec + crop-spec authoring over the QC-cleared master handle + the promised-variant contract + the brand-format canon. **No generative engine calls, no pixel crop, no re-encode, no caption-locale burn, no byte-level video decode in v1.0** — Localization v1.0 authors the DECLARED variant spec (per-platform caption text + the crop rectangle geometry + the target format per platform) + re-verifies the inbound evidence-hash chain; the actual crop / re-encode / caption-burn render is v1.1 (needs frame-level encode). Effective per-reel cost ≈ $0.00–$0.02 (optional evidence-hash re-verify only). `variants_rendered: const false` in v1.0 — Localization authors the variant plan, the RENDER is v1.1. The direct analog of Motion's `motion_processed: const false`, Sound's `audio_processed: const false`, Editor's `render_dispatched: const false`, and full QC's `auto_published: const false`. |

**Build calendar (Week 15 — Localization trajectory, mirrors the proven 8-day agent-build cadence; both body partials fall pre-Rest Day this week):**
- **Day 102** (today, Thu Jul 30 · Wk15) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 103 (Fri Jul 31 · Wk15) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 104 (Sat Aug 1 · Wk15) — SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16
- **Day 105** (Sun Aug 2 · Wk15) — **REST DAY — no build** (16th observance; pre-stage the LOCK-candidate scaffold only)
- Day 106+ (Mon Aug 3, TBD) — LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK (pattern: full QC Day 96–101 / Motion Day 86–90 / Sound Day 78–81)

> **Rest Day honesty:** This Day-102 build runs Thursday (Pacific) — building is allowed. The prior Rest Day (Day 98, Sun Jul 26 Pacific) was observed (the 15th) per the standing pattern; the next Rest Day is Day 105 (Sun Aug 2 Pacific). Localization's two body partials (Day 103 Fri + Day 104 Sat) both fall pre-Rest Day this week — the Sound Day 74/75/76 + full-QC Day 92/93/95 pre-Rest Day pattern. No build will run on Day 105 (Sun).

> **Sequencing honesty:** The 42-day sprint's headline deliverable — the Mode B Pro single-reel **commercial demo** (Day 42 target, past) — shipped on the six launch-critical production agents threaded through the QC Pre-flight gate. Localization is the FIRST Distribution agent (after the full six-agent post-production tail: Ingest + Edit Director + Editor + Sound + Motion + full QC) and the FIRST *optional* agent in the fleet; its v1.0 build proceeds inside the **post-launch hardening window** and does **not** gate the launch demo (a single-platform Pro reel would pass Localization as `not_required`). This outline is the forward-design head-start so the Distribution stage is buildable in dependency order once the Sound + Motion + full-QC LOCKs close (their live-5/5 spend gates are the only things between them-as-candidates and them-LOCKED). Localization's own LOCK is QUADRUPLE-gated (see §0 predecessor + §13 preview): the Sound LOCK, then the Motion LOCK, then the full-QC LOCK, then Localization's own 5/5 — the fleet's first FOUR-gate.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Localization Agent** is the **first Distribution-stage agent of ARS** — the moment a reel stops being a *single QC-cleared 9:16 master* and, IF the plan asked for it, becomes a *set of per-platform variants ready to publish*: a caption-variant spec for each target surface (IG vs TikTok vs LinkedIn vs Shorts each carry different caption/description conventions), a crop spec for each aspect a platform needs (vertical → horizontal 16:9 or square 1:1, with the brand's caption-safe and end-card-safe regions preserved), and a platform-variant manifest the Publishing agent consumes to push each variant to its surface. It is an **executor** (like Editor, Sound, Motion — it authors a declared spec and renders nothing in v1.0), and it is the fleet's **first OPTIONAL agent**: for a single-platform reel it authors no variants and passes the cleared master straight to Publishing (`not_required`).

Where the thirteen upstream agents authored intent, adjudicated production-safety, readied the assets, directed and conformed the cut, finished the audio and graphics, and adjudicated terminal ship-safety, Localization *prepares the cleared master for cross-platform distribution*:
- Brief / Script / Storyboard = intent + content authoring (what the reel SAYS and how it's shot)
- Production Coord = logistics (mode, vendor, budget)
- AI Video Gen / Style Replication = render + brand-finish (the pixels exist)
- QC Pre-flight = production ship-safety (the *production output* is brand-safe + format-correct)
- Ingest = asset-readiness (the files are present, valid, in-sync — one mode-agnostic Asset Manifest)
- Edit Director = edit-plan authoring (the directed cut)
- Editor = cut conform (the frame-accurate EDL bound to real media)
- Sound = audio finish (the mixed, loudness-normalized v2 edit)
- Motion = motion finish (the captioned, lower-thirded, motion-token-applied v3 master + the motion self-check)
- full QC = terminal ship-safety adjudication (the Pass/Fail/Reshoot verdict + the publish handle)

The Localization Agent picks up at the QC-cleared v3 master + the publish handle and prepares distribution:
- **Localization Agent = cross-platform variant author ("Given a `successQcReport`/`pass` verdict, the human/Lever-approved v3-final handle, and the `tier_richness_echo` promised-variant contract — does this reel need per-platform variants? If the plan promised more than the single primary surface, author the per-platform caption-variant spec + the crop spec for each requested aspect (preserving the brand caption-safe + end-card-safe regions), re-scan any NET-NEW caption-variant text for banned tokens (the scoped 14th firewall pass), and emit `variants_ready` + a platform-variant manifest. If the plan promised only the single primary surface, emit `not_required` and pass the cleared master straight through. Author the DECLARED variant spec only — crop no pixel, re-encode no frame, burn no caption, call no engine in v1.0.")**

**Single-responsibility line (LOCKED on intent):**
> *"Optional cross-platform variant author. Given a full-QC-`pass`, human/Lever-approved v3 master + the promised-variant contract, authors the per-platform caption-variant spec + the aspect-crop spec (vertical→horizontal / square, brand caption-safe + end-card-safe regions preserved) for every requested platform beyond the primary, re-invoking the entity firewall over the NET-NEW variant text it authors (the scoped 14th pass). Emits `variants_ready` + a platform-variant manifest (multi-platform) OR `not_required` + a clean pass-through (single-platform). Authors the DECLARED variant spec only — crops NO pixel, re-encodes NO frame, burns NO caption, runs NO engine, renders NOTHING in v1.0 (the crop/encode render is v1.1). Emits a plan a human ratifies before Publishing pushes — never publishes, never renders."*

**Why this agent's reason-to-exist is the Distribution bridge + the promised-variant contract (Blueprint §1.5 / §4.13 / full-QC `tier_richness_echo`):** The full QC agent (Day 92 §3.1) closes its `successQcReport` with a `tier_richness_echo` block that records `platform_variants_promised` vs `platform_variants_validated` and a `handoff_targets: ["localization-agent"]` — it validated that the delivered variant SET matched the tier promise, but it authored no variants; it adjudicated the single master. Localization is the agent that **fulfills that promised-variant contract** — it reads the same `platform_variants_promised` figure full QC validated and, for each promised surface beyond the primary, authors the variant spec that makes the promise real. **This is Donna's design thesis for building Localization as Agent #14: it is the first Distribution agent, the bridge from a cleared single master to a publish-ready variant set, and the structural proof that optionality is a clean first-class contract — if Localization can emit a defensible `not_required` pass-through for a single-platform reel and a defensible `variants_ready` manifest for a multi-platform one, from the QC-cleared master + the promised-variant figure alone, with zero engine calls and zero render, then the Distribution stage is genuinely buildable at $0 and the optional-agent pattern is proven for the fleet.** A firewall hit on a NET-NEW caption variant, a crop that would clip the end-card-safe region, or a requested variant with no promised backing routes back to the responsible upstream agent or halts — it never ships a defective variant.

**Pipeline position (per Orchestration Blueprint §2 swim lane + §4.13 Lever router):**
```
... → FULL QC (terminal ship-safety gate → Pass/Fail/Reshoot report) →
   [successQcReport · verdict = pass · publish_target{auto_published:false, publish_mode:human_in_the_loop}]
        │
        ▼  [Lever Router: PASS + human/Lever approval → 15 Localization
             (Lever-3 100% review · Lever-2 sampled · Lever-1 auto)]
        │
        ▼  [v3 final + qc_report + tier_richness_echo{platform_variants_promised, primary_aspect}]
   LOCALIZATION (optional cross-platform variant author → variant manifest OR not_required pass-through)
        │
        ▼  [platform_variant_manifest + master handle: per-platform caption specs · crop specs (aspect + safe regions) · firewall-clean new text · Drive /reels/[reel_id]/variants/]
   16 PUBLISHING → 17/18 Learning Loop  (agents #15–#17 build order; Publishing = runtime 16, not yet built)
        │
   [FAIL] → route back to the responsible upstream agent (Motion for a caption-source defect · full QC for a promised-set mismatch)
   [not_required] → forward the cleared master to Publishing unchanged (single-platform pass-through)
```

**Why an executor distinct from the terminal adjudicator (the boundary question):** full QC just adjudicated ship-safety and cleared the master — so what does Localization add? A clean separation across the *adjudication → distribution-prep* boundary:
1. **full QC adjudicates ONE master** — the single 9:16 v3 master, emitting a Pass/Fail/Reshoot verdict. It renders nothing and authors no variants; it validated that the promised variant COUNT matched, not that the variants EXIST.
2. **Localization authors the variant SET** — it is the only agent positioned to turn the cleared single master into the per-platform variants the plan promised: the 16:9 crop for a LinkedIn/YouTube horizontal surface, the 1:1 crop for a feed post, the per-platform caption/description text. It gates *"does this reel need variants, and if so what is each one's spec?"*
3. **The two agents do different work.** full QC judges; Localization prepares. full QC can clear a master that promised three platform surfaces, but only Localization, reading the promised-variant contract, authors the two additional crop+caption specs that fulfill it — while re-invoking the firewall on the NET-NEW caption text those specs introduce (text full QC never saw). Localization does NOT re-adjudicate ship-safety (it trusts the full-QC `pass` in the chain) and does NOT re-scan the cleared master (full QC is terminal on the master); it *authors the derivative variant specs* and firewall-scans only what it newly writes.

The actual publish (encode dispatch, cross-platform push, scheduling, hashtag rotation, thumbnail pick, post-URL logging) is, in v1.0, the **Publishing agent's** job (runtime #16, not yet built) via Ayrshare (Blueprint §7); Localization emits the *variant manifest + the master handle*; it publishes nothing and renders nothing itself. **`variants_rendered` is the honesty field at this agent — `const false` in v1.0, the explicit declaration that no crop/encode/caption-burn was executed by the agent.** This is the human-in-the-loop + no-render seam, made explicit — the direct analog of Motion's `motion_processed: const false`, Sound's `audio_processed: const false`, Editor's `render_dispatched: const false`, and full QC's `auto_published: const false`.

**Hand-off contract enforced:**
- **PRECONDITION:** Localization reads the full QC `qc_report.json`. If `output_type != "successQcReport"` OR `verdict != "pass"` → halt with `upstream_qc_not_pass`. A `fail`/`reshoot`/`errorEnvelope` qc report → halt `upstream_not_success`. If the `publish_target` does not encode the human/Lever approval the Lever router requires (Blueprint §4.13) → halt `approval_not_granted`. Localization never authors variants for a reel that did not clear full QC and get approved.
- **INPUT contract:**
  - The full QC `successQcReport` — `verdict: pass`, `qc_gate`, `publish_target` (`auto_published: false` · `publish_mode` · `publish_queue_uri`), `tier_richness_echo` (`platform_variants_promised` · `platform_variants_validated` · `primary_aspect`), `mode_blind_confirm`, the `qc_report_evidence_hash`, the Motion `finish_target.v3_final_uri` (the master handle).
  - The **requested platform-variant set** (`platform_variants[]` from the Reel Plan / the tier promise) — the surfaces this reel is destined for.
  - The **denormalized upstream chain** in `metadata.parent_chain` (12-tuple inbound from full QC, seventuply-deferred) — re-verified for evidence-hash integrity, not re-derived.
- **OUTPUT contract:** Emits `localization_spec.json` per §3 (polymorphic: `successLocalizationSpec | errorEnvelope`, the success branch carrying the `variants_ready | not_required` sub-verdict). The Publishing agent reads the variant manifest + the master handle without re-deriving Localization.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| Optionality gate — `not_required` pass-through for a single-platform reel; `variants_ready` for a multi-platform reel (read from `platform_variants_promised`) | Automatic locale/language translation of caption text (needs a translation engine — v1.1) |
| Per-platform caption-variant SPEC authoring (IG / TikTok / LinkedIn / Shorts caption + description conventions) — DECLARED text | Sentiment/engagement-optimized caption rewriting (creative variant scoring — v1.1) |
| Aspect-crop SPEC authoring (9:16 → 16:9 / 1:1 crop rectangle geometry, brand caption-safe + end-card-safe regions preserved) — DECLARED geometry | The actual pixel crop / re-encode / caption-burn RENDER — needs frame-level encode (v1.1) |
| Scoped 14th firewall pass over NET-NEW caption-variant text (banned-entity re-scan) | Per-locale firewall lists (non-English banned-entity variants — data-gated, v1.1) |
| Crop-safety validation (a crop must not clip the caption-safe or end-card-safe region per Brand-Intake §8) — DECLARED-geometry check | Measured-pixel crop verification (frame decode + region measurement — v1.1) |
| Promised-variant fulfillment (author exactly the set `platform_variants_promised` counts; flag a mismatch) | Platform-specific thumbnail/cover-frame selection (the Publishing agent's §16 job — v1.1) |
| Firewall re-scan on new text + evidence-hash chain re-verification (inbound chain intact) | Auto-fix routing with variant patch generation (v1.0 only routes; does not patch) |
| Two-branch verdict (`variants_ready | not_required` success · `fail` error) with per-variant evidence | Hashtag rotation / caption-hashtag authoring (the Publishing agent's §16 job — v1.1) |
| 13-tuple parent_chain extension (inherits full QC 12-tuple + appends `localization_spec_id`) | Multi-reel batch localization (v1.0 = one reel per invocation) |
| Platform-variant manifest construction (declarative per-variant JSON) + the master handle passthrough | Publish-target encode dispatch / Ayrshare push (the Publishing agent owns it, v1.1) |

**Pricing tier table (Localization is universal-transit; tier-AWARE in the variant set, tier-FLAT in the firewall + crop-safety rules — the first optional agent):**

| Tier | Reaches Localization? | Localization's typical behavior | Cost | Note |
|------|----------------------|--------------------------------|------|------|
| Pilot — Founding 5 | **YES (transit)** | Usually `not_required` — single primary 9:16 master, no promised variants | ~$0.00 | Clean pass-through to Publishing |
| Starter — Operator | **YES (transit)** | Usually `not_required`; occasionally a single 1:1 if the plan flags it | ~$0.00 | Pass-through or one variant |
| Pro — Studio | **YES** | `variants_ready` — authors the 1:1 crop + caption variant (9:16 + flagged 1:1 promise) | ~$0.01–0.02 (optional hash re-verify) | 1–2 variants specced |
| Enterprise — Agency | **YES** | `variants_ready` — authors the full promised cross-platform fan-out (9:16 + 16:9 + 1:1 + per-platform captions) | ~$0.01–0.02 | Richest variant set |

Localization adds **negligible** cost to every tier envelope in v1.0. Its economic value is **cross-platform reach at the last mile** — turning one cleared master into every surface the plan promised, without a human hand-authoring each crop and caption, while guaranteeing no new caption text ships a banned token and no crop clips the brand-safe regions.

---

## §2. Inputs

Localization has **one canonical responsibility** (author cross-platform variants, or pass through) reached from **one** primary input shape — the QC-cleared master + the promised-variant contract. Like full QC and the four post-tail executors, there is **no verdict-forking mode branch**: `production_mode` is read for context + reporting only. This is the sixth agent whose core logic is structurally mode-blind. (It reads `tier_richness_echo.platform_variants_promised` for the optionality gate + the variant set — it does not fork the firewall or crop-safety rules by tier.)

### §2.1 Precondition input — full QC qc-report verdict (gate)

**Always read first.** The full QC `qc_report.json`:
```json
{
  "output_type": "successQcReport",
  "verdict": "pass",
  "reel_ref": { "motion_spec_id": "<uuid>", "qc_report_id": "<uuid>" },
  "qc_gate": { "brand_voice_11_point": { "points_passed": 11 }, "entity_firewall_pass_13": { "hits": 0 } },
  "publish_target": { "auto_published": false, "publish_mode": "human_in_the_loop", "publish_queue_uri": "ars://reels/.../qc-report.json" },
  "tier_richness_echo": { "tier": "pro", "platform_variants_promised": 2, "platform_variants_validated": 2, "primary_aspect": "9:16" },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_v3_master" },
  "handoff_targets": ["localization-agent"],
  "human_review_required": true,
  "metadata": { /* 12-tuple parent_chain inbound, held additively; the accumulated qc_pre_flags surface */ }
}
```
**Hard validation:** `output_type == "successQcReport"` AND `verdict == "pass"`. Otherwise → halt with `upstream_qc_not_pass`. A consumed `errorEnvelope` / `fail` / `reshoot` qc report → halt `upstream_not_success`. The `publish_target` must encode the human/Lever approval (Blueprint §4.13: PASS routes through the Lever router — Lever-3 100% review, Lever-2 sampled, Lever-1 auto — before Localization); absent it → halt `approval_not_granted`. Localization does not author variants for a reel that failed the terminal gate or that has not been approved, and NEVER re-adjudicates ship-safety (that authority is full QC's — Localization inherits the recommend-don't-override discipline: it is an executor and NEVER patches the master).

### §2.2 Primary input — v3 master + promised-variant contract (the reel to localize)

**Required input fields (preliminary — full schema on the Day 103/104 partials):**
```json
{
  "v3_final_uri": "ars://reels/.../v3-final.mp4",
  "primary_format": {
    "aspect": "9:16",
    "resolution": "1080x1920",
    "duration_ms": 62000,
    "caption_burn_in": true,
    "caption_safe_region": { "top_pct": 8, "bottom_pct": 18 },
    "end_card_safe_region": { "last_ms": 1500 }
  },
  "requested_platform_variants": [
    { "platform": "instagram_reels", "aspect": "9:16" },
    { "platform": "linkedin", "aspect": "1:1" }
  ],
  "tier_richness_echo": { "tier": "pro", "platform_variants_promised": 2, "primary_aspect": "9:16" },
  "caption_source": [ { "at_ms": 0, "text": "your calendar doesn't lie" } ],
  "evidence_hashes": { "qc_report_evidence_hash": "<sha256>", "motion_spec_evidence_hash": "<sha256>" },
  "metadata": { /* Cross-SPEC §3.9 — tier, lever_state, brand_id, session_id, parent_chain (12-tuple inbound), the accumulated qc_pre_flags surface */ }
}
```

**Hard validations on primary input (defense-in-depth pass 14 — scoped to net-new text):**
1. Upstream `output_type` is `successQcReport` with `verdict == "pass"`, NOT `errorEnvelope`/`fail`/`reshoot`. (Otherwise → `upstream_qc_not_pass` / `upstream_not_success`.)
2. The human/Lever approval is present in `publish_target`. Absent → `approval_not_granted`.
3. The `v3_final_uri` (cleared master) resolves. Unresolvable → `master_unresolved` (route back to Motion via full QC).
4. `requested_platform_variants[]` count reconciles with `tier_richness_echo.platform_variants_promised`. If the request asks for MORE surfaces than the tier promised → `variant_not_promised` (route to full QC / Production Coord — a scope mismatch the cleared master's promise doesn't back). If the request is the single primary only → take the `not_required` pass-through path (Step 5).
5. Every requested variant's target `aspect` is a supported crop of the `primary_format` (9:16 → 9:16 identity · 16:9 · 1:1 · 4:5), AND the declared crop rectangle preserves the `caption_safe_region` + `end_card_safe_region`. A crop that would clip either → `crop_safety_violation` (the brand-safe region rule).
6. Every NET-NEW caption-variant / description text Localization authors passes the entity-firewall re-scan (Brand-Intake §6). Any hit → `variant_firewall_breach` (the scoped 14th pass; forensic-log the field). The already-cleared master is NOT re-scanned (full QC is terminal on it).
7. `asset_uri`s / `v3_final_uri` remain platform-relative `ars://...` (Hard Rule #8 inherit — Localization echoes the master handle + writes each variant handle as `ars://...`; it must not introduce an absolute URL). Violation → `asset_uri_integrity_failure`.
8. `metadata.parent_chain` is a well-formed 12-tuple inbound (5→12-tuple accepted additively — see §3.3). Malformed → `localization_lineage_failure`.

### §2.3 Reference input — the brand-format spec + firewall list (canon)

**Denormalized, read as the authoring reference (not re-authored).** Localization reads the Brand Voice Intake §6 (the banned-entity firewall list — re-invoked over net-new variant text only) and §8 (the reel-format spec: 9:16 / 1080×1920 / burned-in lowercase-sans captions one line at a time / end-card serif ivory 1.5s — the master-format baseline each crop is derived FROM, and the caption-safe + end-card-safe regions each crop must preserve). **Localization consumes these as fixed canon facts — it authors variants that honor them; it does NOT re-author the format spec, does NOT re-scan the already-cleared master (full QC is terminal on it), and does NOT decode the v3 video frame (no pixel read, no measured crop probe — declared geometry + declared handle only, the same declared-spec posture as full QC, Motion, Sound, Editor, Ingest, and QC Pre-flight). The MEASURED crop probe is v1.1.**

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block + the full-QC `publish_target`: `tier`, `lever_state`, `brand_id`, `session_id`. Localization reads `tier_richness_echo.platform_variants_promised` for the optionality gate (single-platform → `not_required`; multi-platform → author the promised set) and the `primary_aspect` for the crop-derivation baseline, and sets the report's `human_review_required: true` per Lever-3 default AND the v1.0 human-in-the-loop ship posture. It does **not** re-run ship-safety adjudication, cost derivation, asset validation, cut conform, creative direction, audio finish, or motion finish — those are full QC's, QC Pre-flight's, Ingest's, Editor's, Edit Director's, Sound's, and Motion's authorities respectively; Localization *authors variants* over their cleared output and re-verifies the `qc_report_evidence_hash` / `motion_spec_evidence_hash` chain.

---

## §3. Outputs (skeleton)

Localization emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 / QC Pre-flight Day 40 / Ingest Day 48 / Edit Director Day 58 / Editor Day 66 / Sound Day 74 / Motion Day 82 / full QC Day 92 output pattern (`oneOf [success branch, errorEnvelope]`). The optionality lives as a `variants_ready | not_required` sub-verdict INSIDE the success branch — keeping the clean two-branch polymorphic shape.

### §3.1 successLocalizationSpec branch (variants authored OR pass-through)

```json
{
  "output_type": "successLocalizationSpec",
  "verdict": "variants_ready",
  "reel_ref": {
    "brand_id": "REINVENTED",
    "qc_report_id": "<uuid>",
    "localization_spec_id": "<uuid>"
  },
  "localization_scope": {
    "optional_agent": true,
    "platform_variants_promised": 2,
    "platform_variants_authored": 1,
    "primary_forwarded": true
  },
  "platform_variant_manifest": [
    {
      "platform": "linkedin",
      "aspect": "1:1",
      "crop_spec": { "source_aspect": "9:16", "target_aspect": "1:1", "crop_rect_pct": { "x": 0, "y": 22, "w": 100, "h": 56 }, "caption_safe_preserved": true, "end_card_safe_preserved": true },
      "caption_variant": { "text": "your calendar doesn't lie", "platform_convention": "linkedin_longform_ok", "firewall_scanned": true, "firewall_hits": 0 },
      "variant_uri": "ars://reels/.../variants/linkedin-1x1.mp4 (holding-store handle — render is v1.1)"
    }
  ],
  "primary_passthrough": { "v3_final_uri": "ars://reels/.../v3-final.mp4", "aspect": "9:16" },
  "variant_firewall": { "net_new_text_fields_scanned": 1, "hits": 0, "scope": "net_new_variant_text_only" },
  "crop_safety": { "all_crops_preserve_caption_safe": true, "all_crops_preserve_end_card_safe": true },
  "evidence_hash_chain": { "qc_report_evidence_hash_verified": true, "motion_spec_evidence_hash_verified": true, "chain_intact": true },
  "mode_blind_confirm": { "production_mode_read": false, "consumed": "mode_agnostic_v3_master" },
  "distribution_target": { "variants_rendered": false, "render_mode": "human_in_the_loop", "variants_queue_uri": "ars://reels/.../variants/ (publish queue — rendered + pushed by the human/Publishing agent)" },
  "tier_richness_echo": { "tier": "pro", "platform_variants_promised": 2, "platform_variants_authored": 1, "primary_aspect": "9:16" },
  "handoff_targets": ["publishing-agent"],
  "metadata": { /* Cross-SPEC §3.9 with Localization additions per §3.3 — 13-tuple parent_chain */ },
  "human_review_required": true
}
```

**The `not_required` pass-through (single-platform reel — the optional-agent skip path):**
```json
{
  "output_type": "successLocalizationSpec",
  "verdict": "not_required",
  "reel_ref": { "qc_report_id": "<uuid>", "localization_spec_id": "<uuid>" },
  "localization_scope": { "optional_agent": true, "platform_variants_promised": 1, "platform_variants_authored": 0, "primary_forwarded": true },
  "platform_variant_manifest": [],
  "primary_passthrough": { "v3_final_uri": "ars://reels/.../v3-final.mp4", "aspect": "9:16" },
  "variant_firewall": { "net_new_text_fields_scanned": 0, "hits": 0, "scope": "no_net_new_text" },
  "distribution_target": { "variants_rendered": false, "render_mode": "human_in_the_loop", "variants_queue_uri": "ars://reels/.../v3-final.mp4 (single-surface — forwarded unchanged)" },
  "handoff_targets": ["publishing-agent"],
  "metadata": { /* 13-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (variant cannot be safely authored)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "variant_firewall_breach",
  "failed_check_id": 6,
  "attempts": 1,
  "route_back_to": "motion-agent",
  "reel_ref": { "localization_spec_id": "<uuid>" },
  "cost_incurred_usd": 0.00,
  "detail": {
    "violation": "a banned-entity token appeared in a NET-NEW platform caption-variant field authored by Localization — scoped 14th-pass catch",
    "affected_fields": ["platform_variant_manifest[0].caption_variant.text"],
    "recovery_path": "route back to Motion to re-source the caption from a firewall-clean EDL passthrough; if the token is in the master's cleared caption source, escalate to full QC for re-adjudication (the master's own firewall pass would have missed it)"
  },
  "metadata": { /* Cross-SPEC §3.9 — 13-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `variants_ready` | Every promised variant authored; crops preserve the brand-safe regions; net-new text firewall-clean; hash chain intact; forwarded to the publish queue (held for human/Publishing-agent render + push in v1.0) | `null` (forward to Publishing) | Multi-platform reel, all variant + firewall + crop-safety checks green |
| `not_required` | Single-platform reel — no variants needed; the cleared master forwards unchanged (the optional-agent skip path) | `null` (forward to Publishing) | `platform_variants_promised == 1` (primary only) |
| `fail` | A variant cannot be safely authored (firewall hit on net-new text, a crop that clips a brand-safe region, a requested variant with no promised backing, a hash break) that an upstream agent must fix | the responsible upstream agent (`motion-agent` for a caption-source defect · `qc-agent`/`full QC` for a promised-set mismatch or a master-firewall miss · `production-coord-agent` for a scope/envelope mismatch) | A pre-render variant defect |

> **Defining divergence (surfaced):** Localization carries a **two-verdict success posture with an optional-skip sub-state** (`variants_ready | not_required` success · `fail` error) — it does NOT restore the `reshoot` verdict full QC holds. It is an **executor**, not an adjudicator: ship-safety was already judged one stage upstream (full QC), so there is no un-fixable-in-post determination left for Localization to make — a defect it finds is either a fixable upstream caption/crop-source issue (`fail` → route back) or nonexistent (`variants_ready`/`not_required`). The genuinely NEW contract property is `not_required`: Localization is the **fleet's first OPTIONAL agent**, and the `not_required` pass-through is its defining authority — the clean declaration that a single-platform reel needs no distribution variants and forwards unchanged. It never patches the master, never re-crops a rendered frame (it renders nothing), and never re-adjudicates ship-safety — the author-a-declared-variant-spec discipline, at the Distribution boundary.

### §3.3 Metadata block additions (Localization-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **13-tuple** (inherits full QC's 12-tuple lineage + appends own `localization_spec_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (RATIFIED Day 79). **Eighth forcing function**: the 13-tuple depends on the full QC 12-tuple LOCK (triple-gated behind the Motion 11-tuple LOCK behind the Sound 10-tuple LOCK, itself spend-gated on the Day 81 runbook's live 5/5) behind the Editor 9-tuple LOCK (closed Day 79) behind the Edit Director 8-tuple, Ingest 7-tuple, QC 6-tuple (all closed Day 79). Encoded additively (`minItems: 5`, `prefixItems` positions 0–12, `maxItems: 13`, `items: false`) so it accepts the 5→13-tuple while rejecting a 4-tuple. The exact-N `minItems` flip to 13 is deferred to the same separately-validated hardening migration the Sound 10-tuple + Motion 11-tuple + full-QC 12-tuple flips await. — see §5 + Open Questions.
- `localization_class` — enum (`variants_authored` for a multi-platform reel · `single_platform_passthrough` for `not_required` · `variant_fail`).
- `localization_spec_evidence_hash` — SHA-256 over the `platform_variant_manifest` + `variant_firewall` + `crop_safety` block (forensic, tamper-evident variant plan).
- `variants_rendered` — `const false` in v1.0 (Localization authors the variant plan; the human/Publishing agent renders the crop/encode + pushes. The direct analog of Motion's `motion_processed: const false`, Sound's `audio_processed: const false`, Editor's `render_dispatched: const false`, and full QC's `auto_published: const false` — the honest declaration that no crop/encode was executed by the agent). Flips to a real value only when the Publishing agent (#16) ships (v1.1).
- `render_mode` — enum (`human_in_the_loop` for v1.0 · `automated` reserved for v1.1 Publishing agent). The explicit human-in-the-loop attestation.
- `variant_firewall_scope` — `const "net_new_variant_text_only"` in v1.0 (the honest declaration that Localization's firewall pass covered ONLY the text it authored, NOT a re-scan of the full-QC-cleared master — the scoped 14th pass, not a second terminal pass).
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.

### §3.4 errorEnvelope code namespace (target 7–9 LOCKED on Day 103/104 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `upstream_qc_not_pass` | full QC `verdict != pass` / not `successQcReport` | 1 | Halt — Localization never localizes an uncleared reel. |
| `upstream_not_success` | the consumed qc report is `errorEnvelope`/`fail`/`reshoot` | 2 | Halt — cannot localize a failed-gate output. |
| `approval_not_granted` | the `publish_target` does not encode the human/Lever approval (Blueprint §4.13) | 3 | Halt — the Lever router must approve before Localization. |
| `master_unresolved` | the `v3_final_uri` (cleared master) does not resolve | 4 | Hard FAIL — cannot localize a missing master; route back to Motion (via full QC). |
| `variant_not_promised` | a requested platform variant exceeds `tier_richness_echo.platform_variants_promised` | 5 | Hard FAIL — scope mismatch; route to full QC / Production Coord (the promise doesn't back it). |
| `variant_firewall_breach` | a banned-entity token appears in a NET-NEW caption-variant / description field (the scoped 14th pass) | 6 | Hard FAIL — forensic-log the field; route to Motion (caption source) or escalate to full QC (a master-firewall miss). |
| `crop_safety_violation` | a declared crop rectangle would clip the caption-safe or end-card-safe region (Brand-Intake §8) | 7 | Hard FAIL — the brand-safe region rule; route to Motion (variant spec) — re-frame the crop. |
| `evidence_hash_break` | the qc-report / motion-spec evidence-hash chain does not verify end-to-end | 8 | Hard FAIL — a tamper-evidence break; forensic; route to the agent whose hash broke. |
| `asset_uri_integrity_failure` | a variant handle or the master handle is not a platform-relative `ars://...` URI | 9 | Hard FAIL — Hard Rule #8 inherit; no absolute URL may enter the manifest. |
| `localization_lineage_failure` | malformed parent_chain / broken n-tuple lineage | 10 | Forensic — audit-trail break. |
| `localization_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 103/104 LOCK:** 7–9 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping. (Preliminary list carries 9 named + lineage + catch-all; the §13 walk will confirm the routing granularity on `variant_firewall_breach` — Motion-first vs full-QC-escalation — and whether `variant_not_promised` routes to full QC or Production Coord.)

---

## §4. Tier Constraints & Mode Coverage

**Per-tier transit (Localization is universal-transit; tier-AWARE in the variant set, tier-FLAT in the firewall + crop-safety rules — restated for defense-in-depth pass 14):**

| Tier | Reaches Localization? | Typical scope behavior | Variant-set read | Cost |
|------|----------------------|------------------------|-------------------|------|
| Pilot | **YES (transit)** | Usually `not_required` (single primary 9:16) | Pilot promised set (typically 1) | ~$0.00 |
| Starter | **YES (transit)** | `not_required`, occasionally 1 flagged crop | Starter promised set | ~$0.00 |
| Pro | **YES** | `variants_ready` — 1–2 crops + caption variants | Pro promised set (9:16 + flagged 1:1) | ~$0.01–0.02 |
| Enterprise | **YES** | `variants_ready` — the full cross-platform fan-out | Enterprise promised set (richest) | ~$0.01–0.02 |

**Why universal transit + tier-AWARE scope + tier-FLAT safety (the optional-agent discipline):** Every reel passes THROUGH Localization (it is on the runtime path between full QC and Publishing), but the WORK it does is tier-scoped: a Pilot reel with a single promised surface exits as `not_required` in one step; an Enterprise reel with a promised cross-platform set exits with a full variant manifest. The ONE tier-flat surface pair is the firewall + crop-safety rules: the banned-entity re-scan on net-new text and the caption-safe/end-card-safe region preservation run identically for every authored variant regardless of tier (a firewall breach or a clipped end-card on a Pro variant is exactly as unpublishable as on an Enterprise variant). **The reel carries its promised-variant count in `tier_richness_echo`; Localization authors exactly that set (or none) and applies the one safety standard to all.** This is the distribution analog of full QC's tier-flat-gate / tier-aware-ledger discipline — the first Distribution agent does not re-litigate the tier ladder for safety, only for scope.

**No ship-safety re-adjudication / no cost-derivation / no asset-validation / no cut-conform / no creative authority / no audio-finish / no motion-finish / no render (the inherited discipline, septupled + render-abstained):** Localization does **NOT** re-adjudicate ship-safety (full QC's authority — it trusts the `pass`), re-derive the cost ledger (QC Pre-flight's), re-validate assets (Ingest's), re-conform the cut (Editor's), re-direct the edit (Edit Director's), re-mix the audio (Sound's), re-finish the graphics (Motion's), OR render/crop/re-encode any pixel (the v1.1 Publishing surface). It is seven gates downstream of asset validation and one gate downstream of the terminal adjudicator; re-executing any of them would be redundant. Localization's authority is **cross-platform variant authoring** — the per-platform caption spec, the crop spec (with brand-safe region preservation), the scoped net-new-text firewall pass, and the optionality gate, full stop.

**Mode coverage (mode-BLIND by inheritance — the convergence payoff, six stages deep):**

| Mode | What Localization sees | Mode-specific note |
|------|------------------------|--------------------|
| A (human footage origin) | The SAME mode-agnostic v3 master + full-QC `pass` | Localization reads `production_mode` for the report's context line only; the variant logic never forks on it. |
| B (rendered + replicated origin) | The SAME mode-agnostic v3 master + full-QC `pass` | Identical variant path. |
| C (replicated hot-path origin) | The SAME mode-agnostic v3 master + full-QC `pass` | Identical variant path. |

**Mode-blind guarantee (the core §4 contract):** Localization asserts `mode_blind_confirm.production_mode_read == false` in every output — a self-attestation that it authored the variants (or passed through) without forking on the origin mode (it may print the mode in the report's context block, but the crop/caption/firewall logic never reads it as a discriminator). This is the SIXTH machine-checkable proof that Ingest's mode-convergence seam holds — now six stages downstream, at the Distribution boundary. **Localization is the sixth agent in the 17-agent fleet for which the mode columns of this table are identical; that identity, carried through the director (Edit Director) AND the timeline executor (Editor) AND the audio executor (Sound) AND the motion executor (Motion) AND the terminal adjudicator (full QC) AND now the distribution author (Localization), is the structural evidence that the entire pipeline — from ingest to the publish-ready variant set — is genuinely mode-agnostic end-to-end.** If Localization ever NEEDED to fork the variant on mode, the convergence contract would be broken upstream. By construction it never does — the cleared master is the same shape regardless of how the pixels were born.

---

## §5. Process Steps (System Prompt Skeleton — Day 103 §7 will LOCK)

The agent runs an **11-step variant loop** per invocation (matches the AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion 11-step process pattern; one fewer than full QC's 12-step, reflecting the executor's narrower surface). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope. The `not_required` pass-through short-circuits after Step 5.

**Step 1 — Verify full-QC precondition + parse input**
- Read the full QC `qc_report.json`. Confirm `output_type == "successQcReport"` AND `verdict == "pass"`. Otherwise → halt with `upstream_qc_not_pass`.
- Confirm the `publish_target` encodes the human/Lever approval (Blueprint §4.13). Absent → halt `approval_not_granted`.
- Parse input JSON against `input.schema.json` (Day 103/104 LOCKED). There is NO mode branch — assert the v3 master is the mode-agnostic shape. Any `errorEnvelope`/`fail`/`reshoot` upstream → halt with `upstream_not_success`.

**Step 2 — Lineage integrity**
- Validate `metadata.parent_chain` is a well-formed 12-tuple inbound (5…12-tuple accepted additively under the ratified §3.9 amendment). Malformed → `localization_lineage_failure`.

**Step 3 — Evidence-hash chain re-verification**
- Re-verify the `qc_report_evidence_hash` + `motion_spec_evidence_hash` chain end-to-end (each hash re-computed over its source block and matched). Any break → `evidence_hash_break` (forensic).

**Step 4 — Master resolution**
- Confirm `v3_final_uri` resolves (the cleared master handle exists). Unresolvable → `master_unresolved` (route to Motion via full QC).

**Step 5 — Optionality gate (the optional-agent decision)**
- Read `tier_richness_echo.platform_variants_promised` + `requested_platform_variants[]`. If the promised set is the single primary surface only (`== 1`, matching `primary_aspect`) → emit `not_required` (primary forwarded unchanged) and short-circuit to Step 11. If a request exceeds the promised count → `variant_not_promised`. Otherwise proceed to author the promised set.

**Step 6 — Crop-spec authoring + brand-safe region preservation**
- For each requested variant aspect, author the crop-rectangle geometry deriving the target aspect from the `primary_aspect` (9:16 → 16:9 / 1:1 / 4:5). Validate the crop preserves the `caption_safe_region` + `end_card_safe_region` (Brand-Intake §8). A crop that clips either → `crop_safety_violation` (route to Motion — re-frame).

**Step 7 — Per-platform caption-variant authoring**
- For each target platform, author the caption/description-variant text per that platform's convention (IG / TikTok / LinkedIn / Shorts). Author from the cleared `caption_source` — do NOT introduce new claims (the creative authority is upstream); adapt formatting/length only.

**Step 8 — Scoped entity firewall (14th pass, net-new text only)**
- Re-scan ONLY the NET-NEW caption-variant / description text authored in Step 7 against the banned-entity list (Brand-Intake §6). Any hit → `variant_firewall_breach` (forensic-log the field). Do NOT re-scan the already-cleared master (full QC is terminal on it). Assert `variant_firewall_scope == "net_new_variant_text_only"`.

**Step 9 — Manifest assembly + promise reconciliation**
- Assemble the `platform_variant_manifest` (one entry per authored variant: platform, aspect, crop_spec, caption_variant, variant_uri holding handle) + the `primary_passthrough`. Reconcile `platform_variants_authored` against `platform_variants_promised`; a shortfall/overage → flag. Every variant handle must be `ars://...` → else `asset_uri_integrity_failure`.

**Step 10 — Verdict synthesis**
- Synthesize the verdict: `variants_ready` iff every promised variant authored + all crops safe + all net-new text firewall-clean + hash chain intact; `fail` for any pre-render defect (route to the responsible upstream agent). (The `not_required` verdict was set at Step 5.) Emit per-variant evidence for crop-safety + firewall + promise reconciliation.

**Step 11 — Mode-blind self-attestation + publish-queue handoff**
- Assert `mode_blind_confirm.production_mode_read == false`. On `variants_ready` / `not_required`, write the `localization_spec.json` + the variant manifest (`variants_rendered: false`, `render_mode: human_in_the_loop`) to the Drive `/reels/[reel_id]/variants/` publish queue; `handoff_targets: ["publishing-agent"]` (holding-store default until the Publishing agent #16 ships). Set `human_review_required: true`.

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 103 + 104)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 103 partial 1. Pattern source: full QC §6 / Motion §6. Target 11–13 checks bipartite-covering the 7–9 errorEnvelope codes. Slot 11+ reserved for `localization_agent_failed` per Cross-SPEC §3.6 slot-naming canon. Checks span: precondition + qc-report-evidence verify · approval-present · lineage · evidence-hash-chain re-verify · master resolution · optionality gate · crop-safety (region preservation) · per-platform caption authoring · scoped net-new firewall (14th pass) · manifest promise-reconciliation · mode-blind self-attestation.
- **§7 System Prompt v1.0** — Day 103 partial 1. Frame + hard rules + universal-transit / tier-aware-scope / tier-flat-safety table + 11-step variant loop verbatim from §5 + the Blueprint §7 variant-folder write target inlined + the banned-entity firewall list (§6, net-new scope) + the reel-format spec + caption-safe/end-card-safe regions (§8) as the authoring reference. ~12–14 KB target. Hard Rules mirror full QC / Motion with Localization-specific tightening on "author-never-render (variants_rendered const false)," "scoped-firewall-never-re-scan-the-master," and "optional-skip-is-a-clean-pass-through (not_required)" discipline.
- **§8 Performance Targets** — Day 104 partial 2. 9 metric categories. Schema validity 100% / net-new-text firewall catch 100% (a banned token must never enter a new platform caption) / crop-safety preservation 100% (no crop clips a brand-safe region) / optionality-gate correctness 100% (a single-platform reel must exit `not_required`, never spuriously author variants) / promise-reconciliation 100% / evidence-hash-chain verify 100% / false-`variants_ready` rate 0% target (shipping an unsafe variant is the costly direction) / false-`fail` rate ≤ 7% (over-flagging a borderline crop/caption to `fail` is the acceptable direction — looser than full QC's ≤6% because Localization is not the terminal safety line, full QC already cleared the master) / p50 latency 20s / p95 60s (a narrower reasoning surface than full QC) / zero engine + zero render + zero crop cost.
- **§9 Test Fixtures** — Day 104 partial 2. 5-fixture portfolio: TC-01 clean Mode-origin-A Pro `variants_ready` (a 1:1 crop + LinkedIn caption authored, all safe) · TC-02 Mode-origin-C Enterprise `variants_ready` (full cross-platform fan-out — proves mode-blind: byte-identical variant path to a Mode-A reel despite different origin, the **mode-blind variant-convergence proof**, SIX stages deep) · TC-03 Pilot `not_required` (single-platform pass-through — the optional-agent skip path, the fixture UNIQUE to the first optional agent) · TC-04 `crop_safety_violation` → fail + route to Motion (a 16:9 crop that clips the end-card-safe region) · TC-05 `variant_firewall_breach` (a banned token in a NET-NEW LinkedIn caption variant — the scoped 14th-pass catch; GATING fixture). 5 of 7–9 codes exercised; remainder in schema-only fixtures. Optional probes: the `variant_not_promised` scope-mismatch catch + the `approval_not_granted` halt + the `evidence_hash_break` forensic catch + the slot `localization_agent_failed` catch-all.
- **§10 Field Map** — Day 103 partial 1. ~24 rows · passthrough vs transform vs derived. qc-report→precondition map + promised-variant→optionality-gate map (derived) + primary-format→crop-geometry map (transform) + caption-source→per-platform-variant map (transform) + net-new-text→firewall-scan map + crop→safe-region-preservation map + manifest→promise-reconciliation map + derived verdict/manifest map + master→passthrough map.
- **§11 Cost Model** — Day 104 partial 2. Zero engine + zero render + zero crop snapshot (variant-spec + crop-geometry authoring only; the optional evidence-hash re-verify is the only marginal cost, ~$0.01–0.02). Reach value model (economic justification = cross-platform reach without a human hand-authoring each crop + caption, at $0 in v1.0). Explicit note: the actual crop/re-encode/caption-burn render lands in v1.1 (the Publishing surface) — v1.0 is $0 by construction, authoring the declared variant spec + re-verifying the hash chain.
- **§12 Verdict Math** — Day 104 partial 2. `variants_ready` = (full-QC precondition met) ∧ (approval present) ∧ (lineage well-formed) ∧ (evidence-hash chain intact) ∧ (master resolved) ∧ (promised set > primary) ∧ (every promised variant authored) ∧ (every crop preserves both brand-safe regions) ∧ (every net-new text field firewall-clean) ∧ (promise reconciled). `not_required` = the same preconditions ∧ (promised set == primary only). Any single ∧-term false (post-precondition) → `fail` per §3.2. The variants_ready/not_required split is deterministic on `platform_variants_promised`; there is no judgment slot (Localization is an executor — the one adjudication, is-the-defect-un-fixable, lives upstream at full QC).
- **§13 Critical Decisions LOCKED** — Day 104 partial 2. Target 11–14 LOCKED decisions. Pre-scaffolded list:
  1. Author-variant-spec-only vs render scope — v1.0 = author the declared variant + crop spec ONLY; Localization NEVER crops a pixel, re-encodes a frame, or burns a caption. It emits a manifest + routes. [LOCKED-as-drafted Day 102]
  2. Executor, not adjudicator — Localization reads the full-QC `pass` + the cleared master, re-verifying only the evidence-hash chain; it re-adjudicates no ship-safety, re-derives no upstream conform. [LOCKED-as-drafted Day 102]
  3. Two-verdict success + optional-skip sub-state (`variants_ready | not_required`) + `fail` — NO `reshoot` restore; Localization is an executor, ship-safety was judged upstream. The `not_required` pass-through is its defining authority (the first optional agent). [LOCKED-as-drafted Day 102]
  4. Mode-blind by inheritance — no `production_mode` variant fork; `mode_blind_confirm.production_mode_read: false` self-attested (the sixth mode-blind agent). [LOCKED-as-drafted Day 102]
  5. full-QC-pass + approval precondition — Localization runs only on a `successQcReport`/`pass` + Lever-approved reel; otherwise halts `upstream_qc_not_pass` / `approval_not_granted`. [LOCKED-as-drafted Day 102]
  6. Universal-transit / tier-aware-scope / tier-flat-safety — all 4 tiers transit Localization; the variant SET is tier-read (`platform_variants_promised`); the firewall + crop-safety rules run identically. [LOCKED-as-drafted Day 102]
  7. 13-tuple parent_chain — inherits full QC 12-tuple + appends `localization_spec_id`; EIGHTH forcing function (depends on the full-QC 12-tuple LOCK, triple-gated behind Motion 11-tuple behind Sound 10-tuple, spend-gated on the Day 81 runbook 5/5; the §3.9 amendment is already RATIFIED Day 79). [DEFERRED — held additively at `minItems: 5`]
  8. Scoped 14th firewall — Localization's firewall pass covers ONLY the NET-NEW caption-variant text it authors, NOT a re-scan of the cleared master (full QC is terminal on the master). `variant_firewall_scope: const "net_new_variant_text_only"`. [LOCKED-as-drafted Day 102]
  9. Crop-safety = brand-safe region preservation — every crop must preserve the caption-safe + end-card-safe regions (Brand-Intake §8); a clip → `crop_safety_violation`. [LOCKED-as-drafted Day 102]
  10. errorEnvelope code count — 7–9 target; routing granularity on `variant_firewall_breach` (Motion-first vs full-QC-escalation) + the `variant_not_promised` route (full QC vs ProdCoord). [PRELIMINARY · operator amend Day 104]
  11. Self-QC check count — 11–13 (one fewer than full QC, reflecting the narrower executor surface). [PRELIMINARY · operator amend Day 104]
  12. False-`variants_ready` = ZERO tolerance — an unsafe crop or a banned token in a new caption must NEVER survive to `variants_ready`; the target is 0% (a false variants_ready ships a defective variant to a live surface). [LOCKED-as-drafted Day 102]
  13. Author-never-render / recommend-never-publish — Localization emits a variant manifest + a holding-store handle; the human/Publishing agent renders the crop/encode + pushes. `variants_rendered: const false`. [LOCKED-as-drafted Day 102]
  14. Handoff to Publishing — Localization hands the variant manifest + the master handle to the Drive variants queue (holding store) until the Publishing agent #16 ships (Blueprint §7). [PRELIMINARY · operator amend Day 104]
  15. Quadruple-gated LOCK — Localization's own v1.0 LOCK sequences strictly AFTER the Sound LOCK, then the Motion LOCK, then the full-QC LOCK, then its own 5/5 (the fleet's first FOUR-gate). [LOCKED-as-drafted Day 102]

- **§14 Calendar status updates** — Day 103 partial 1. Day 102 ✓ → trajectory populated.
- **§15 Change Log** — Day 104 partial 2. v1.0 lifecycle entries (outline-day-102 → body-day-103 → body-day-104 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 104 partial 2. Cross-SPEC §3.9 canonical fields + 7 Localization additions (13-tuple parent_chain, localization_class, localization_spec_evidence_hash, variants_rendered const false, render_mode, variant_firewall_scope const, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `localization-agent` (kebab-case, matches the fleet pattern + Blueprint §4.13/§7 handoff target) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `localization_spec_evidence_hash` SHA-256 over the manifest + firewall + crop-safety block; the qc-report/motion-spec evidence-hash chain re-verified end-to-end (inherits the full QC + Motion anchors) |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion / full QC shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` (success sub-state) + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ Localization forwards the accumulated surface + appends its own ≥4 variant-flag predicates (crop-safety · net-new-firewall · promise-reconciliation · optionality) — the floor honored one stage deeper |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-BLIND table — the sixth agent for which the mode columns are identical (the convergence payoff, six stages deep, at the Distribution boundary) |
| §3.6 Slot 11 naming canon | ✅ Reserved `localization_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Consumed shapes respected; Localization's own variant predicates snake_case |
| §3.8 Tier↔mode firewall (14th defense-in-depth) | ✅ Step 8 SCOPED entity firewall (net-new caption-variant text only — does NOT contradict full QC's terminal-on-the-master claim) + §4 universal-transit / tier-aware-scope / tier-flat-safety table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 13-tuple, held additively. **Eighth forcing function** — gated on the full-QC 12-tuple LOCK (triple-gated behind Motion 11-tuple behind Sound 10-tuple, spend-gated on the Day 81 runbook 5/5); the §3.9 amendment itself is RATIFIED (Day 79). |
| §3.10 Cost ceiling authority | ✅ §4 explicitly DECLINES to re-adjudicate ship-safety (full QC's), re-derive cost (QC Pre-flight's), re-validate assets (Ingest's), re-conform the cut (Editor's), re-direct the edit (Edit Director's), re-mix the audio (Sound's), re-finish the graphics (Motion's), OR render any pixel (v1.1 Publishing) — no septuple-enforcement; Localization is ~$0-cost in v1.0 |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion / full-QC / Cross-SPEC / Brand-Intake references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 102 outline — 6 parked for operator amendment)

1. **Author-variant-spec-only vs partial-render scope** — v1.0 authors the declared variant + crop spec; it NEVER crops/re-encodes/burns. Confirm v1.0 stops at the manifest + route (no auto-render — that is the deferred v1.1 Publishing render surface). *(Donna recommends: confirm author-and-route-only for v1.0 — the variant manifest + crop geometry is the buildable, highest-leverage, $0 slice; the actual crop/encode render is the same $-and-render surface the whole fleet defers to v1.1 automation, and it belongs to the Publishing agent's compute path.)*
2. **Optional-skip verdict shape — `not_required` sub-state vs a distinct output_type** — should the single-platform pass-through be a `not_required` sub-verdict INSIDE `successLocalizationSpec` (keeping the clean two-branch oneOf), or a third top-level output_type? *(Donna recommends: `not_required` as a success sub-verdict — it preserves the fleet-wide two-branch `oneOf [success, errorEnvelope]` polymorphic shape every prior agent holds; a single-platform pass-through IS a success, just a zero-variant one. A third top-level branch would break the schema symmetry for no gain.)*
3. **13-tuple parent_chain** — eighth forcing function (depends on the full-QC 12-tuple LOCK, triple-gated behind Motion 11-tuple behind Sound 10-tuple, itself spend-gated on the Day 81 runbook 5/5; the §3.9 amendment is already RATIFIED Day 79). Localization is the first 13-tuple consumer. *(Donna recommends: hold additively at `minItems: 5` until the full-QC 12-tuple LOCKs; the exact-N flip to 13 folds into the same separately-validated hardening migration the Sound 10-tuple + Motion 11-tuple + full-QC 12-tuple flips await.)*
4. **Scoped firewall vs full re-scan** — v1.0 scans ONLY the net-new caption-variant text Localization authors, not the cleared master. Is the scoped 14th pass the right posture, or should Localization re-scan the whole master as a belt-and-suspenders? *(Donna recommends: scoped net-new-only — full QC is the ratified terminal firewall on the master (a LOCKED-on-intent claim); a second full re-scan would duplicate the terminal pass and muddy the "who owns the master firewall" boundary. Localization owns ONLY the text it introduces. This keeps the firewall-ownership chain clean and honest.)*
5. **Handoff readiness** — Localization hands to the not-yet-built Publishing agent (#16). Should v1.0 emit the variant manifest + master handle to a holding store (the Drive `/reels/[reel_id]/variants/` folder, per Blueprint §7), or assume direct handoff? *(Donna recommends: emit to the Drive variants queue in v1.0; direct agent-to-agent handoff activates when the Publishing agent LOCKs — mirrors the Motion→finish-queue, Sound→finish-queue, and full-QC→publish-queue holding-store decisions.)*
6. **Crop-derivation authority — declared geometry vs measured** — v1.0 authors the crop-rectangle geometry from the declared `primary_format` + declared safe regions (no frame decode); is declared-geometry the right posture, or does a safe crop need a measured frame probe? *(Donna recommends: declared-geometry for v1.0 — the measured crop probe is the same frame-decode surface the whole fleet defers to v1.1; the declared caption-safe + end-card-safe regions Motion/Brand-Intake specify are sufficient to author a safe crop rectangle. The measured verification is the v1.1 belt-and-suspenders layer, alongside the Publishing render.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (Localization trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 102 | Thu Jul 30 | **SPEC outline §0–§5** [SHIPPING NOW] | full QC Day 92 outline |
| 103 | Fri Jul 31 | SPEC body partial 1: §6 + §7 + §10 + §14 | full QC Day 93 / Motion Day 83 |
| 104 | Sat Aug 1 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | full QC Day 95 / Motion Day 85 |
| 105 | Sun Aug 2 | **REST DAY** — no build (pre-stage next scaffold only) | Day 21/28/…/98 Rest Day compounding (16th) |
| 106+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | full QC Day 96–101 / Motion Day 86–90 |

**Sprint context:** Localization is **Agent #14** — the FIRST Distribution-stage agent and the FIRST OPTIONAL agent in the fleet, the 14th (scoped, net-new-text) defense-in-depth firewall and the **sixth contractually mode-blind agent** (the continued proof of Ingest's convergence seam, six stages deep). It is the cross-platform variant author — the bridge from a single QC-cleared master to the publish-ready variant set the plan promised — and it opens the two-agent Distribution stage (Localization #14 → Publishing #16-runtime). In v1.0 it produces NO media and renders NOTHING: it authors the per-platform caption + crop spec (or passes a single-platform reel through as `not_required`), re-scans only the net-new text it writes, and emits a manifest the human ratifies (the crop/encode render deferred to v1.1 Publishing), keeping the zero-dollar / no-render invariant intact. The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) shipped on the six production agents through the QC Pre-flight gate; Localization's v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the full QC, Motion, Sound, Ingest, QC Pre-flight, Style Replication, Edit Director, and Editor outlines were (while their predecessor LOCKs remained gated — Localization's LOCK here quadruple-gated behind the Sound + Motion + full-QC LOCKs, all spend-gated on live 5/5 runs).

---

## Files produced today (Day 102)

- `ars/ARS-2026-07-30-Day-102-Localization-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-07-30.md` — Day 102 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 102)

- ✅ **No LLM dispatched.** No render API. No pixel crop, no re-encode, no caption-locale burn. No engine credentials referenced. No vendor URLs walked. No media render, no byte-level video decode, no measured crop probe. (Localization by design authors a declared variant + crop spec + re-verifies the evidence-hash chain in v1.0 — the crop/encode render is the Week 4–5 v1.1 Publishing scope.)
- ✅ **No external comms transacted.** No emails sent, no DMs, no social posts, no publish, no client/investor outreach. The end-of-run status digest to Jamila's Google Voice self-thread ([status number redacted]) is the only intended outbound, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, no render compute, zero $ spent. (`jsonschema` 4.26.0 re-validation is a PyPI install with no vendor/engine surface, $0.)
- ✅ **No operator-impersonation.** Neither the Sound v1.0 LOCK, the Motion v1.0 LOCK, nor the full-QC v1.0 LOCK ceremony was performed — the Sound gate is a live, reproducible 5/5 run of the Day 81 runbook (~$3.50 Opus); the Motion LOCK is double-gated (Sound LOCK first, then the Motion Day-90 runbook 5/5, ~$3.75 Opus); the full-QC LOCK is triple-gated (Sound → Motion → full-QC Day-101 runbook 5/5, ~$4.25 Opus); all three are forbidden under the $0 unattended ceiling; locking any on the offline stamp alone would be a fake-advance (refused). Sound + Motion + full QC stay LOCK CANDIDATE. No version tag flipped, no dashboard chip flipped, no Notion row marked LOCKED. The §3.9 amendment (ratified Day 79) NOT re-committed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. Localization v1.0 LOCK will hard-gate itself on the upstream LOCKs (Sound 10-tuple → Motion 11-tuple → full-QC 12-tuple) being closed first — the fleet's first QUADRUPLE-gate.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication / QC Pre-flight / Ingest / Edit Director / Editor / Sound / Motion / full-QC SPECs + schemas + SKILL bundles + Orchestration Blueprint + Cross-SPEC review + Brand-Voice Intake — every prior canon file untouched. Offline fleet regression sweep re-run: **557/557 (9 bundles), 0 drift.**
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + the brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 8 enumerates HC/NPOX tokens precisely so the agent can BLOCK them in net-new variant text — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** full QC Day 92 outline structure inherited verbatim; executor-lineage grounding from the Motion Day 82 + Editor Day 66 outlines. Orchestration Blueprint §1.5 / §2 / §4.13 / §5 / §6 / §7 (Agent 15 Localization definition) + Cross-SPEC §3 canon + Brand-Voice Intake §6 + §8 used as the grounding spine. No bespoke departures from canon.
- ✅ **Rest Day honored** — this Day-102 build runs Thursday (Pacific); the prior Rest Day (Day 98, Sun Jul 26) was observed (15th). Next Rest Day: Day 105 (Sun Aug 2 Pacific) — docs-prep / scaffold pre-stage only, no SPEC content.

---

*Day 102 ships clean. Day 103 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). Localization is Agent #14 of 17 — the FIRST Distribution agent and the FIRST OPTIONAL agent in the fleet, the 14th (scoped, net-new-text) defense-in-depth firewall and the sixth contractually mode-blind agent, the continued proof that Ingest's mode-convergence seam holds six stages deep. It is the cross-platform variant author — the bridge from a single QC-cleared master to the publish-ready variant set the plan promised — and it opens the two-agent Distribution stage. In v1.0 it produces no media and renders nothing, authoring the per-platform caption + crop spec (or passing a single-platform reel through as `not_required`), re-scanning only the net-new text it writes, and emitting a manifest the human ratifies (the crop/encode render deferred to v1.1 Publishing), keeping the zero-dollar / no-render invariant intact. Operator pickup: (1) the Sound v1.0 LOCK remains the immediate forward step — its gate is a live, reproducible 5/5 run of the Day 81 runbook (~$3.50 Opus) that the $0 overnight cannot execute; then the Motion 5/5 + LOCK (~$3.75 Opus, double-gated behind Sound); then the full-QC 5/5 + LOCK (~$4.25 Opus, triple-gated); all three runnable in Jamila's iMac sit-down OR an attended, spend-authorized Donna run under the standing authorization; the full-QC 12-tuple is Localization's direct 13-tuple dependency; (2) review the §13 critical-decisions list — the §3.9 n-tuple amendment is already RATIFIED (Day 79), so Localization inherits n-tuple lineage cleanly (eighth forcing function, held additively until the full-QC 12-tuple LOCKs); (3) confirm the Agent #14 = Localization selection (or re-assign the slot) at the Sound/Motion/full-QC LOCK close. None of the Sound, Motion, or full-QC v1.0 LOCKs was performed tonight — locking on the offline stamp alone, absent the live 5/5s, would be a fake-advance; all three stay in the spend-gated queue. Localization's own LOCK is the fleet's first QUADRUPLE-gate: Sound LOCK → Motion LOCK → full-QC LOCK → Localization 5/5.*
