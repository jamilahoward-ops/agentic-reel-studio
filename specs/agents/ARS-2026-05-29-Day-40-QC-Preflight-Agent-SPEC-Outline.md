# ARS — QC Pre-flight Agent v1.0 SPEC OUTLINE (§0–§5)

**Date:** Fri May 29, 2026 (Day 40 of 42 · Week 6)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** OUTLINE ONLY — §0–§5 drafted (purpose, scope, inputs, outputs skeleton, tier constraints, process). Full SPEC body §6–§16 + LOCK candidate target on the subsequent build days. Schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK to follow on the established 8-day agent-build cadence.
**Pattern source:** `ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` (Day 29 outline — proven 17-section shape inherited verbatim) and `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (Day 22 outline grandparent pattern). v1.0 LOCK-quality target.
**Canon source:** `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED — naming map, errorEnvelope shape, qc_pre_flags minItems-4 floor, metadata block, n-tuple-as-lineage parent_chain all inherited).
**Orchestration source:** `ARS-2026-04-24-Agent-Orchestration-Blueprint.md` (Day 5 LOCKED — pipeline roster position 14 "QC" + 11-point Brand Voice QC gate definition).
**Predecessor agents (all built):** Brief (#1) · Script (#2) · Storyboard (#3) · Production Coord (#4) · AI Video Gen (#5) · Style Replication (#6). QC Pre-flight consumes the convergence of the production tier (rendered_shots from AI Video Gen Mode B + replicated_shots from Style Replication Modes A/B/C).
**Successor agents:** Localization (#15 pipeline) · Publishing (#16 pipeline) · and the in-post fleet (Ingest / Edit Director / Editor / Sound / Motion — not yet built). v1.0 QC Pre-flight gates the **production → post boundary**; the final pre-publish QC touchpoint is a separate v1.1+ build.

> **LOCK-state awareness (CRITICAL — do not silently advance):** As of this outline's authoring, on-disk file-state confirms **both prior LOCK ceremonies remain OPERATOR-GATED.** AI Video Gen SKILL.md frontmatter still reads `status: v1.0 SKILL bundle SHIPPED — LLM execution Day 27 locks v1.0` (no version-tag flip to LOCKED). Style Replication SKILL.md still reads `v1.0 LOCK target: Day 37 — hard-gated on AI Video Gen v1.0 LOCK ceremony first` (no flip). The Day 36 LLM Test Runbook execution + the AI Video Gen and Style Replication LOCK ceremonies are unconfirmed. This outline is therefore authored under the same posture as the Day 29 Style Replication outline (which was written while AI Video Gen LOCK was operator-gated): it references LOCK-stable **text artifacts** (the SPECs + schemas as drafted) and uses **no production output** from either agent. Forward-looking outline work does NOT constitute fake-advance and does NOT impersonate the operator. The two pending LOCK ceremonies are surfaced as carried-over operator action items in §5 and in tonight's build log.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 6 — Quality gate layer (production → post boundary pre-flight) |
| Agent index | **#7 of 17** (build sequence — per Orchestration Blueprint Day 5 roster + Style Replication SKILL.md "agent #6 of 17" confirmation) |
| Runtime pipeline position | **14 — QC** (the Brand Voice QC gate); v1.0 scope is the **pre-flight** variant gating the production-tier output before it enters post-production |
| Pipeline tier | QUALITY GATE (first and only QC-tier agent built in the sprint) |
| Mode coverage | **Mode-agnostic** — adjudicates Mode A (graded user footage), Mode B (rendered + replicated), Mode C (replicated hot-path) output without branching its core verdict logic |
| Predecessor SPEC (production) | `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` (Day 24 LOCK candidate — operator-gated) + Style Replication Day 32 LOCK CANDIDATE (operator-gated) |
| Predecessor schemas | `skills/ai-video-gen-agent/schemas/output.schema.json` (Day 25) + `skills/style-replication-agent/schemas/output.schema.json` (Day 33) — both consumed as INPUT branches |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape, qc_pre_flags minItems-4 floor, metadata block, parent_chain lineage all inherited |
| Defense-in-depth layer | **7th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → Style Replication → **QC Pre-flight**) — the LAST automated firewall before distribution |
| Lever inheritance | Reads `lever_state` from upstream `metadata` block; emits `human_review_required` per Lever 3 default until Day 60+ Lever-2 graduation gate. **As the terminal gate, QC Pre-flight is the natural Lever-3 sit-down surface** — its Pass/Fail/Reshoot verdict is what the human ratifies. |
| Pricing tier authority | **ALL tiers** — Pilot · Starter · Pro · Enterprise. QC Pre-flight is the **first agent since Brief that every tier traverses** (Mode A Pilot reels skip AI Video Gen + Style Replication's Mode B/C paths, but still require a pre-flight QC gate). Universal gate. |
| Cost authority class | **LOWEST of any agent** — pure reasoning + schema/firewall validation. No generative engine calls. Optional native re-verification of brand-finish fingerprints (pHash/CLIP, ~$0.001/shot) only if a drift flag is contested. Effective per-reel cost ≈ $0.00–$0.02. |

**Build calendar (Week 6 — QC Pre-flight trajectory, mirrors the proven 8-day agent-build cadence):**
- **Day 40** (today, Fri May 29 · Wk6) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 41 (Sat May 30 · Wk6) — SPEC body partial 1: §6 Self-QC checklist + §7 System Prompt v1.0 frame + §10 Field Map scaffold + §14 calendar
- Day 42 (Sun May 31 · Wk6) — **REST DAY** (no build; pre-stage scaffold only, per Day 21/28/35 Rest Day-compounding pattern)
- Day 43 (Mon Jun 1 · commercial-launch target day) — SPEC body partial 2 + LOCK candidate path **OR** commercial-launch pivot per operator's Day 42-target call. *(Note: the canon commercial-launch target is Mon Jun 1; QC Pre-flight v1.0 LOCK lands inside the post-launch hardening window, not gating launch itself — see §5 sequencing note.)*

> **Sequencing honesty:** The 42-day sprint's headline deliverable is the **Mode B Pro single-reel commercial demo at Day 42**, threaded through the 6 built agents. QC Pre-flight is Agent #7 — it **extends** the fleet past the launch-critical six. Its v1.0 build proceeds in parallel with / just after launch; it does **not** block the Day 42 demo. This outline is the forward-design head-start so the gate is LOCK-ready early in the post-launch hardening phase.

**Rest Day compounding pattern reuse:** Day 42 (Sun May 31) is the sprint's 6th Rest Day. Per the canonical pattern (Day 7 Brief LOCK · Day 14 ProdCoord SPEC body · Day 21 scaffold prep · Day 28 Style Replication branch primer · Day 35 Style Replication runbook primer), Day 42 Rest Day pre-stages the next build day's scaffold without advancing build canon.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **QC Pre-flight Agent** is the **quality gate** of ARS — the moment a reel stops being "produced" and has to prove it is **safe to ship**. It is the seventh and final automated defense-in-depth firewall pass, and the first gate every tier and every mode funnels through on the way out.

Gates already passed upstream:
- Brief / Script / Storyboard = intent + content gates (entity firewall set + re-validated 3×)
- Production Coord = logistics gate (mode routing + vendor + budget envelope)
- AI Video Gen = render gate ("Did the pixels come out matching the brief, on-budget, no firewall breach in the prompt?")
- Style Replication = brand gate ("Are these pixels recognizably the brand's pixels?")

The QC Pre-flight Agent picks up at the convergence point:
- **QC Pre-flight Agent = ship-safety gate ("Does this reel pass the 11-point Brand Voice QC gate? Is the entity firewall clean one final time? Do the format specs match every requested platform variant? Is the caption spec correct? Is the cumulative reel cost inside the tier envelope? Is every upstream `qc_pre_flag` resolved? PASS, FAIL, or RESHOOT?")**

**Single-responsibility line (LOCKED):**
> *"Terminal pre-flight quality gate. Adjudicates the full reel chain (brief → script → storyboard → production_plan → rendered/replicated shots) against the 11-point Brand Voice QC gate, the entity firewall (7th pass), platform format specs, caption specs, and the cumulative tier cost ledger. Emits a single Pass / Fail / Reshoot verdict with per-check evidence. Calls no generative engine."*

**Why this agent's reason-to-exist is the qc_pre_flags minItems-4 floor (Cross-SPEC §3.4):** Every upstream agent has been required, since the Cross-SPEC LOCK, to emit `qc_pre_flags[]` with **minItems 4** — a structured, snake_case, machine-parseable set of pre-flight assertions per stage. That floor existed *for this agent*. Brief asserts its pre-flight predicates, Script adds its own, Storyboard, ProdCoord, AI Video Gen, and Style Replication each stack ≥4 more. By the time a reel reaches QC Pre-flight, it carries a **24+ predicate pre-flight surface** (6 agents × ≥4). QC Pre-flight is the agent that **adjudicates that accumulated surface** — it is the consumer the floor was provisioned for. Without QC Pre-flight, the qc_pre_flags floor is a write-only audit field; with it, the floor becomes an executable go/no-go contract. **This is Donna's §3.4 minimum-4 floor justification for building QC Pre-flight as Agent #7.**

**Pipeline position (per Orchestration Blueprint §2 swim lane):**
```
... → Production Coord →
   ├── (Mode A) Live shoot → Style Replication (grade pass) ┐
   ├── (Mode B) AI Video Gen → Style Replication (inherit)  ├─► QC PRE-FLIGHT (ship-safety gate)
   └── (Mode C) Style Replication (hot path)                ┘        │
                                                                     ▼
                                              [PASS] → Localization → Publishing → Loop
                                              [FAIL] → route back to the responsible agent (fix-in-post)
                                              [RESHOOT] → route back to Production Coord (Mode A footage unusable)
```

**Why a PRE-flight gate (and not only the final QC):** The Orchestration Blueprint defines a single "14 QC" agent running the 11-point Brand Voice gate before publishing. v1.0 splits the earliest, highest-leverage slice of that responsibility into a **pre-flight** gate at the production → post boundary, for three reasons:
1. **Fail cheap.** Catching an entity-firewall breach or format mismatch *before* Ingest/Edit/Sound/Motion spend cycles (and before the in-post agents even exist) is the cheapest possible catch point.
2. **The in-post fleet is not built yet.** v1.0 cannot gate post-production it can't see. Gating the production output it *can* see (rendered_shots + replicated_shots) is the buildable, shippable slice.
3. **It is the natural Lever-3 sit-down.** The human's "is this brand-correct?" judgment belongs at the production → post handoff. QC Pre-flight produces exactly the artifact (a Pass/Fail/Reshoot report with per-check evidence) the operator ratifies.

The final pre-**publish** QC (the full #14 gate, post-Motion) is a deliberate **v1.1+** deliverable once the in-post agents (Ingest/Edit/Sound/Motion) ship.

**Hand-off contract enforced:**
- **INPUT contract:** QC Pre-flight reads the production-tier output (polymorphic):
  - From **Style Replication**: `replicated_shots.json` (`successReplicatedShots | errorEnvelope`) — the primary input for Modes A/B/C that pass through Style Replication.
  - From **AI Video Gen** (Mode B where Style Replication is a pure passthrough, or for forensic cross-check): `rendered_shots.json` (`successRenderedShots | errorEnvelope`).
  - Plus the **denormalized upstream chain** carried in `metadata.parent_chain` + the per-stage `qc_pre_flags[]` accumulated through the pipeline.
  - Halts with `upstream_not_success` errorEnvelope if any consumed upstream branch is `errorEnvelope` rather than its success branch.
- **OUTPUT contract:** Emits `preflight_report.json` per §3 (polymorphic: `successPreflightReport` | `errorEnvelope`). Downstream agents (Localization, Publishing) read the verdict without re-deriving QC from upstream.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| 11-point Brand Voice QC gate adjudication (canonical from Brand Voice Intake v1.0 + Blueprint #14) | Per-platform aesthetic scoring (subjective creative QC) |
| Entity firewall — 7th defense-in-depth pass (canonical regex from Cross-SPEC §3 drift #10) | ML-based brand-likeness classifier (data-gated; needs v1.0 production corpus) |
| Format spec validation vs every `platform_variants[]` entry (aspect / duration / caption-burn parity) | Loudness (LUFS) verification — requires the Sound agent's output (not built); deferred |
| Caption spec validation (burn-in text firewall + parity) | Auto-fix routing with patch generation (v1.0 only *routes*; does not patch) |
| Cumulative reel cost-ledger check vs combined tier envelope (AI Video Gen + Style Replication ceilings) | Real-time human-in-the-loop review UI |
| qc_pre_flags adjudication across the full 6-agent chain (24+ predicate surface) | Final pre-publish QC (full #14 gate, post-Motion) — built once in-post fleet ships |
| Pass / Fail / Reshoot verdict with per-check evidence block | Reshoot-cost estimation + auto-rebook (ProdCoord round-trip automation) |
| 6-tuple parent_chain extension (inherits Style Replication 5-tuple + appends `preflight_report_id` ref) | Multi-reel batch pre-flight (v1.0 = one reel per invocation) |
| Optional native brand-finish fingerprint re-verification (pHash/CLIP, contested-drift only) | Per-shot frame-level visual QC (frame extraction + classifier) |

**Pricing tier table (QC Pre-flight is universal — restated for defense-in-depth pass 7):**

| Tier | Reaches QC Pre-flight? | QC Pre-flight cost ceiling | Verdict authority |
|------|------------------------|----------------------------|-------------------|
| Pilot — Founding 5 | **YES** (Mode A reels still gate here) | ~$0.01 (reasoning only) | Pass/Fail/Reshoot |
| Starter — Operator | **YES** | ~$0.01 | Pass/Fail/Reshoot |
| Pro — Studio | **YES** | ~$0.02 (optional fingerprint re-verify) | Pass/Fail/Reshoot |
| Enterprise — Agency | **YES** | ~$0.02 | Pass/Fail/Reshoot |

QC Pre-flight adds **negligible** cost to every tier envelope. Its economic value is **catch-cost avoidance** — preventing a firewall breach or format defect from reaching a published surface (brand-safety incident) or from burning downstream post-production cycles.

---

## §2. Inputs

QC Pre-flight has **one canonical input branch** (the production-tier output) with a polymorphic predecessor shape. Unlike Style Replication's three mode branches, QC Pre-flight is mode-agnostic — `production_mode` is read for context and reporting, but the core verdict logic does not fork on it. Schema discriminator for the *predecessor success/error shape* is the upstream `output_type` field; mode is carried in `metadata.production_mode` per Cross-SPEC §3.9.

### §2.1 Primary input — production-tier output (replicated_shots, preferred)

**When invoked:** Style Replication has emitted a `replicated_shots.json` (any mode). This is the canonical happy-path input — Style Replication is the last production-tier agent and its output is the brand-final pixel set.

**Required input fields (preliminary — full schema on the Day 41/43 partials):**
```json
{
  "replicated_shots": [ /* Style Replication output.schema.json successReplicatedShots branch */ ],
  "production_plan": { /* denormalized ProdCoord output for format-spec + tier + platform_variants */ },
  "brief_ref": { "brief_id": "brief-REINVENTED-2026-05-29-001" },
  "metadata": { /* Cross-SPEC §3.9 — production_mode, agent_id chain, parent_chain (5-tuple inbound), session_id, lever_state, accumulated qc_pre_flags surface */ },
  "cost_ledger": {
    "ai_video_gen_actual_usd": 0.00,
    "style_replication_actual_usd": 0.40,
    "tier_combined_ceiling_usd": 450
  }
}
```

**Hard validations on primary input (defense-in-depth pass 7):**
1. Upstream `output_type == "successReplicatedShots"`, NOT `errorEnvelope`. (If errorEnvelope → halt with `upstream_not_success`.)
2. Every `replicated_shots[i].asset_uri` matches the platform-relative `ars://...` pattern (Hard Rule #8 inherit — **no absolute URLs**).
3. Every `replicated_shots[i].qc_pre_flags[]` satisfies the Cross-SPEC §3.4 minItems-4 floor AND is snake_case-predicate-shaped (§3.7). Shape violation → `qc_pre_flags_format_violation`.
4. `metadata.parent_chain` is a valid 5-tuple inbound (lineage integrity — see §3.3). Malformed → `lineage_integrity_failure`.
5. `replicated_shots[i].drift_warning_bool` flags are reconciled: any unresolved `style_drift_exceeded` carried forward without a Lever-3 human sign-off → `drift_unresolved` (held for review, not auto-passed).
6. `production_plan.platform_variants[]` is present and non-empty (format spec target set).

### §2.2 Secondary / cross-check input — AI Video Gen rendered_shots (Mode B forensic)

**When invoked:** For Mode B reels, QC Pre-flight may additionally read the upstream `rendered_shots.json` to forensically verify the negative-prompt SHA-256 invariant survived the Style Replication passthrough (Hard Rule #10 chain integrity). This is a **cross-check**, not a separate verdict path.

**Required input fields:**
```json
{
  "rendered_shots": [ /* AI Video Gen output.schema.json successRenderedShots branch */ ],
  "negative_prompt_sha256": "..."
}
```

**Hard validations (Mode B only):**
1. `successRenderedShots.rendered_shots[]` shares one `negative_prompt_sha256` value (forensic invariant — Day 22 §6 Check #10 inherit).
2. That SHA-256 matches the `negative_prompt_sha256` carried on the Style Replication output (chain integrity across the passthrough). Mismatch → `negative_prompt_chain_break` (forensic — should never fire in a healthy pipeline).

### §2.3 Accumulated qc_pre_flags surface (consumed across all inputs)

The defining input of this agent. QC Pre-flight walks the **union** of `qc_pre_flags[]` arrays accumulated through the chain:

```json
{
  "accumulated_qc_pre_flags": {
    "brief-agent":            ["no_banned_vocabulary", "hook_within_3s", "tier_mode_authorized", "no_buildings_declared"],
    "script-agent":           ["hook_verbatim_from_brief", "duration_within_band", "do_not_say_absent", "cta_block_present"],
    "storyboard-agent":       ["shot_count_within_tier", "audio_pillar_voice_present", "no_buildings_per_shot", "platform_variants_complete"],
    "production-coord-agent":  ["mode_routed", "vendor_assigned", "budget_envelope_set", "qc_pre_flags_propagated"],
    "ai-video-gen-agent":     ["negative_prompt_attached", "render_status_completed", "cost_within_ceiling", "firewall_prompt_clean"],
    "style-replication-agent": ["anchor_identity_verified", "drift_within_tolerance", "brand_finish_applied", "cost_within_ceiling"]
  }
}
```

**v1.0 adjudication rule:** Every agent must have contributed **≥4** flags (the §3.4 floor). A short array (<4 from any stage) is itself a defect → `qc_pre_flags_floor_breach`. QC Pre-flight does NOT re-execute upstream checks; it **adjudicates the assertions** — confirming the floor is met, the shapes are valid, and no flag carries a negative/failed predicate value into the gate.

### §2.4 Lever + tier context (shared)

Inherited from the upstream `metadata` block: `tier`, `lever_state`, `production_mode`, `brand_id`, `session_id`. QC Pre-flight re-validates the tier↔mode authorization one final time (7th pass) and sets the verdict's `human_review_required` per Lever-3 default.

---

## §3. Outputs (skeleton)

QC Pre-flight emits one of two polymorphic outputs per invocation. Mirrors the AI Video Gen Day 25 / Style Replication Day 33 output pattern (oneOf [success branch, errorEnvelope]).

### §3.1 successPreflightReport branch (verdict = PASS)

```json
{
  "output_type": "successPreflightReport",
  "verdict": "pass",
  "reel_ref": {
    "brief_id": "brief-REINVENTED-2026-05-29-001",
    "production_plan_id": "productionplan-REINVENTED-2026-05-29-001",
    "preflight_report_id": "preflight-REINVENTED-2026-05-29-001"
  },
  "brand_voice_qc": {
    "points_total": 11,
    "points_passed": 11,
    "per_point": [ { "id": 1, "name": "entity_firewall_clean", "status": "pass", "evidence": "0 banned tokens across all asset metadata + captions" } /* ... 11 entries */ ]
  },
  "entity_firewall_pass_7": { "status": "pass", "tokens_scanned": 1840, "hits": 0 },
  "format_spec_check": {
    "platform_variants_checked": 3,
    "aspect_ratio_violations": 0,
    "duration_violations": 0,
    "caption_burn_parity_violations": 0
  },
  "caption_spec_check": { "burn_in_firewall_status": "pass", "parity_status": "pass" },
  "cost_ledger_check": {
    "cumulative_reel_usd": 0.40,
    "tier_combined_ceiling_usd": 450,
    "status": "within_ceiling"
  },
  "qc_pre_flags_adjudication": { "agents_reporting": 6, "floor_met_all": true, "negative_predicates": 0 },
  "drift_reconciliation": { "unresolved_drift_count": 0, "human_signoff_required": false },
  "handoff_targets": ["localization", "publishing"],
  "metadata": { /* Cross-SPEC §3.9 with QC Pre-flight additions per §3.3 — 6-tuple parent_chain */ },
  "human_review_required": true
}
```

### §3.2 errorEnvelope branch (verdict = FAIL or RESHOOT)

```json
{
  "output_type": "errorEnvelope",
  "verdict": "fail",
  "failure_code": "format_spec_violation",
  "failed_check_id": 3,
  "attempts": 1,
  "route_back_to": "style-replication-agent",
  "reel_ref": { "preflight_report_id": "preflight-REINVENTED-2026-05-29-001" },
  "cost_incurred_usd": 0.01,
  "detail": {
    "violation": "platform_variants[1] requested aspect 1:1 but replicated_shots[*] rendered at 9:16 only",
    "affected_platform": "instagram-feed",
    "recovery_path": "re-run Style Replication grade pass with 1:1 crop token OR drop the 1:1 variant from platform_variants"
  },
  "metadata": { /* Cross-SPEC §3.9 — 6-tuple parent_chain */ },
  "human_review_required": true
}
```

**Verdict ↔ route mapping (LOCKED on intent):**

| Verdict | Meaning | `route_back_to` | When |
|---------|---------|-----------------|------|
| `pass` | Cleared into post / distribution | `null` (forward to Localization) | All checks green |
| `fail` | Fixable without re-shooting | the responsible upstream agent (e.g., `style-replication-agent`, `ai-video-gen-agent`, `script-agent`) | Format/caption/cost/firewall defect fixable in production or post |
| `reshoot` | Mode A source footage unusable | `production-coord-agent` | Mode A grade pass cannot rescue an out-of-spec source clip |

### §3.3 Metadata block additions (QC Pre-flight-specific)

Inherits all Cross-SPEC §3.9 canonical fields (agent_id, agent_version, model_used, prompt_template_id, tokens_in/out, latency_ms, qc_score_predicted, human_review_required, iteration_count) PLUS extends with:
- `parent_chain` — **6-tuple** (inherits Style Replication's 5-tuple lineage + appends own `preflight_report_id` reference). Per the **Cross-SPEC §3.9 n-tuple-as-lineage amendment** (DRAFTED Day 31 §16.3; **ratification still operator-pending** — see §5). QC Pre-flight is the first concrete 6-tuple consumer and a forcing function for that amendment's ratification.
- `qc_gate_class` — enum (`pre_flight` for v1.0 · `pre_publish` reserved for v1.1+).
- `verdict_evidence_hash` — SHA-256 over the per-check evidence block (forensic, tamper-evident verdict).
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16.

### §3.4 errorEnvelope code namespace (target 7–9 LOCKED on Day 41/43 partial)

Preliminary code list (operator amendment on the §13 critical-decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `entity_firewall_breach` | banned-entity token in any asset metadata / caption / burn-in (7th pass) | 1 | Hard FAIL — brand-safety. Should never fire if 6 upstream passes worked; if it does, forensic-log which upstream agent leaked. |
| `brand_voice_qc_failed` | ≥1 of the 11 Brand Voice QC points fails | 2 | Verdict = fail; `detail` names the failing point(s). |
| `format_spec_violation` | aspect / duration / caption-burn parity mismatch vs a `platform_variants[]` entry | 3 | Verdict = fail; routes to the responsible production agent. |
| `caption_spec_violation` | burn-in text firewall hit OR caption parity break | 4 | Verdict = fail. |
| `cost_ledger_overrun` | cumulative reel cost > combined tier ceiling | 5 | Hard FAIL — mirrors AI Video Gen §13 / Style Replication §3.4 cost-overrun pattern, at the reel-aggregate level. |
| `upstream_not_success` | a consumed upstream branch is `errorEnvelope` | 6 | Halt — cannot QC a failed production output. |
| `drift_unresolved` | `style_drift_exceeded`/`drift_warning` carried forward without Lever-3 sign-off | 7 | Held for human review (not auto-failed, not auto-passed). |
| `qc_pre_flags_floor_breach` | any upstream stage contributed <4 qc_pre_flags (§3.4 floor) | 8 | Defense-in-depth — the floor this agent exists to enforce. |
| `lineage_integrity_failure` | malformed parent_chain / broken n-tuple lineage | 9 | Forensic — audit-trail break. |
| `qc_pre_flags_format_violation` | qc_pre_flags array shape violates §3.7 | (alias 8) | Same family as floor breach. |
| `negative_prompt_chain_break` | Mode B SHA-256 invariant broke across Style Replication passthrough | (reserved) | Forensic — Day 41 LOCK decision: distinct code OR alias to entity_firewall family. |
| `preflight_qc_agent_failed` | generic catch-all after 2 failed self-regen attempts (Slot-11 canon §3.6) | (catch-all) | `<agent>_agent_failed` namespace per Cross-SPEC §3.8. |

**Target Day 41/43 LOCK:** 7–9 codes, each with trigger condition + failed_check_id + recovery path + route_back_to mapping.

---

## §4. Tier Constraints & Mode Coverage

**Per-tier gate access (QC Pre-flight is universal — restated for defense-in-depth pass 7):**

| Tier | Modes accessible | Reaches QC Pre-flight? | Verdict | Cost |
|------|------------------|------------------------|---------|------|
| Pilot | A | **YES** | Pass/Fail/Reshoot | ~$0.01 |
| Starter | A | **YES** | Pass/Fail/Reshoot | ~$0.01 |
| Pro | A, B | **YES** | Pass/Fail/Reshoot | ~$0.02 |
| Enterprise | A, B, C | **YES** | Pass/Fail/Reshoot | ~$0.02 |

**Why universal access (vs Style Replication's Pro/Enterprise gating):** Style Replication's Mode B/C paths are tier-gated because they are *production capabilities* sold by tier. QC Pre-flight is a *safety gate* — brand safety is not a tier feature. A Pilot Mode A reel that leaks a banned entity token is the same brand-safety incident as a Enterprise reel. The gate fires for everyone.

**Cumulative cost-ledger authority (the one tier-sensitive check QC Pre-flight runs):**

QC Pre-flight is where the **combined** reel cost is finally reconciled against the **combined** tier ceiling — the first agent with visibility into the *total* spend across both production agents:

| Tier | AI Video Gen ceiling | Style Replication ceiling | **Combined reel ceiling (QC Pre-flight enforces)** |
|------|----------------------|---------------------------|----------------------------------------------------|
| Pro | $400 | $50 | **$450** |
| Enterprise | $750 | $120 | **$870** |
| Pilot / Starter (Mode A) | $0 (no render) | grade-pass only (≤$40) | **≤$40** |

These combined ceilings are taken directly from the Style Replication §1 reconciliation ("Combined Pro reel envelope: $400 + $50 = $450 hard ceiling. Enterprise: $750 + $120 = $870"). QC Pre-flight's `cost_ledger_check` is the runtime enforcement of that reconciliation. Overrun → `cost_ledger_overrun` hard FAIL.

**Margin-floor note (inherited flag, NOT re-litigated here):** The Style Replication §4 + AI Video Gen §7 margin-floor reconciliation (Pro 4.17× / Enterprise 1.72× at production ceiling vs 5× floor canon) remains an **open pricing-tier conversation** flagged for the operator. QC Pre-flight enforces the *runtime ceilings as drafted*; it does not adjudicate pricing strategy. Restated for traceability only.

**Mode coverage (mode-agnostic verdict, mode-aware reporting):**

| Mode | What QC Pre-flight checks | Mode-specific note |
|------|---------------------------|--------------------|
| A (graded user footage) | Full 11-point gate + format + caption + firewall; `reshoot` route available if source clip is unrecoverable | Only mode where `reshoot` verdict is reachable (live footage can be re-shot; AI output is re-generated, not re-shot) |
| B (rendered + replicated) | Full gate + §2.2 negative-prompt SHA-256 chain cross-check | Forensic chain-integrity cross-check active |
| C (replicated hot-path) | Full gate + anchor-identity confirmation carried from Style Replication | Highest-margin mode; tightest brand-finish scrutiny |

---

## §5. Process Steps (System Prompt Skeleton — Day 41 §7 will LOCK)

The agent runs an **11-step verdict loop** per invocation (mirrors the AI Video Gen / Style Replication 11-step process pattern). Each step has a verifiable termination state; the loop halts on first hard FAIL and emits the corresponding errorEnvelope, EXCEPT the soft-hold `drift_unresolved` path which routes to human review rather than failing outright.

**Step 1 — Parse input + verify upstream success**
- Parse input JSON against `input.schema.json` (Day 41/43 LOCKED).
- Confirm upstream `output_type == "successReplicatedShots"` (and `successRenderedShots` if Mode B cross-check present). Any `errorEnvelope` upstream → halt with `upstream_not_success`.
- Validate `metadata.parent_chain` is a well-formed 5-tuple inbound. Malformed → `lineage_integrity_failure`.

**Step 2 — Defense-in-depth firewall pass (seventh time)**
- Walk every asset's metadata, every caption string, every burn-in text, every `qc_pre_flags` predicate, every `replication_notes` field with the canonical entity-firewall regex (Cross-SPEC §3 drift #10): `Holdco | Principal | NPOX | 4821 | 6315 | SLN | Retail Supply | Nonprofit Leader A | Community Nonprofit | Nonprofit Leader B | Nonprofit Leader C`.
- Hard FAIL → `entity_firewall_breach` + forensic log naming which upstream stage leaked (in v1.0 this should NEVER fire — six prior passes cover it; if it fires, an upstream agent has a bug).

**Step 3 — qc_pre_flags floor + shape adjudication**
- Confirm each of the 6 upstream agents contributed `qc_pre_flags[]` with **minItems 4** (Cross-SPEC §3.4 floor). Any short array → `qc_pre_flags_floor_breach`.
- Confirm snake_case-predicate shape (§3.7). Violation → `qc_pre_flags_format_violation`.
- Confirm no flag carries a negative/failed predicate value into the gate (a stage asserting its own failure). Negative predicate → route to the appropriate code.

**Step 4 — 11-point Brand Voice QC gate**
- Run the canonical 11-point Brand Voice QC gate (from Brand Voice Intake v1.0 + Blueprint #14). Each point produces `{id, name, status, evidence}`.
- Any point `fail` → accumulate; if ≥1 fails → verdict `fail`, code `brand_voice_qc_failed`, `detail` names the failing point(s).

**Step 5 — Format spec validation**
- For every `production_plan.platform_variants[]` entry, verify the replicated/rendered shots satisfy aspect, duration, and caption-burn parity.
- Mismatch → `format_spec_violation`, `route_back_to` the responsible production agent.

**Step 6 — Caption spec validation**
- Walk every burn-in caption + on-screen-text string through the firewall (re-uses Step 2 regex) AND the caption-burn parity rule (tier ≤ Starter ⇒ caption_burn true).
- Violation → `caption_spec_violation`.

**Step 7 — Cumulative cost-ledger check**
- Sum `ai_video_gen_actual_usd + style_replication_actual_usd` (+ any QC Pre-flight self-cost).
- Compare to the combined tier ceiling ($450 Pro / $870 Enterprise / ≤$40 Pilot-Starter Mode A).
- Overrun → `cost_ledger_overrun` hard FAIL with per-agent attribution in `detail`.

**Step 8 — Drift reconciliation**
- Inspect `replicated_shots[*].drift_warning_bool` + any carried `style_drift_exceeded` signal from Style Replication.
- If unresolved drift exists WITHOUT a Lever-3 human sign-off → emit `drift_unresolved` (soft hold: `verdict` held, `human_review_required: true`, NOT auto-failed, NOT auto-passed). This is the one path that defers to the human rather than rendering a machine verdict.

**Step 9 — Mode B forensic chain cross-check (Mode B only)**
- If `rendered_shots` present, verify the negative-prompt SHA-256 invariant survived the Style Replication passthrough (single hash, matches across both payloads).
- Mismatch → `negative_prompt_chain_break` (forensic).

**Step 10 — Construct verdict payload**
- If all green: build `successPreflightReport` per §3.1 with the full per-check evidence block + `verdict: "pass"` + `handoff_targets: ["localization", "publishing"]`.
- Compute `verdict_evidence_hash` (SHA-256 over the evidence block — tamper-evident).
- Extend `parent_chain` to a **6-tuple** (append `preflight_report_id`).
- Set `human_review_required: true` per Lever-3 default.

**Step 11 — Emit + handoff**
- Validate output payload against `output.schema.json` (Day 41/43 LOCKED). Hard FAIL → forensic log + halt (output should always validate; failure here = agent bug).
- Emit JSON to stdout (paste-and-run runbook) OR persist to platform path per runtime environment.
- On `fail` / `reshoot`, set `route_back_to` per the §3.2 verdict↔route map so the Orchestrator can re-enter the pipeline at the correct agent.

**Anti-patterns Step 11 prevents (Lock-time discipline mirror from AI Video Gen / Style Replication §11):**
- No markdown fences around output JSON.
- No `print()` statements before the output JSON block.
- No engine credentials referenced (QC Pre-flight calls no engine anyway).
- No absolute URLs in any `asset_uri` echoed into the report (Hard Rule #8 inherit).
- No `pass` verdict emitted while any check is unresolved (must be `fail`, `reshoot`, or the `drift_unresolved` soft-hold).
- **No operator-impersonation:** QC Pre-flight emits `human_review_required: true` and a verdict *recommendation*; it does NOT mark a reel "approved for publish" — that ratification is the Lever-3 operator action.

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 41 + 43)

Reserved for SPEC body partial authoring. Outline references below are placeholders demonstrating planned section coverage — actual section text drafted in subsequent days.

- **§6 Self-QC checklist** — Day 41 partial 1. Pattern source: AI Video Gen §6 / Style Replication §6. Target 10–12 checks bipartite-covering the 7–9 errorEnvelope codes. Slot 11 reserved for `preflight_qc_agent_failed` per Cross-SPEC §3.6 slot-naming canon.
- **§7 System Prompt v1.0** — Day 41 partial 1. Frame + hard rules + universal-tier table + 11-step verdict loop verbatim from §5 + the 11-point Brand Voice QC gate text inlined. ~11–13 KB target. Hard Rules mirror AI Video Gen / Style Replication with QC Pre-flight-specific tightening on the "recommend-don't-approve" Lever-3 discipline.
- **§8 Performance Targets** — Day 43 partial 2. 9 metric categories. Schema validity 100% / firewall catch 100% (the 7th pass must be perfect by construction) / false-pass rate 0% target (a brand-safety gate must never pass a breach) / false-fail rate ≤ 5% (over-blocking is the acceptable failure direction) / p50 latency 30s / p95 90s (reasoning-only, fast) / zero engine cost.
- **§9 Test Fixtures** — Day 43 partial 2. 5-fixture portfolio: TC-01 clean Mode B Pro PASS · TC-02 Mode C Enterprise PASS · TC-03 `entity_firewall_breach` (injected banned token — the 7th-pass catch) · TC-04 `format_spec_violation` (aspect mismatch → fail + route) · TC-05 `drift_unresolved` (carried drift → human-review soft-hold). 5 of 7–9 codes exercised; remainder in schema-only fixtures.
- **§10 Field Map** — Day 41 partial 1. ~25 rows · passthrough vs transform vs derived. Per-check evidence map + reel-level verdict aggregate map.
- **§11 Cost Model** — Day 43 partial 2. Near-zero engine snapshot (reasoning-only; optional native pHash/CLIP re-verify $0.001/shot). Catch-cost-avoidance value model (the agent's economic justification is downstream-cost prevention, not direct margin).
- **§12 Verdict Math** — Day 43 partial 2. PASS = (firewall clean) ∧ (11/11 brand-voice) ∧ (0 format violations) ∧ (0 caption violations) ∧ (cost within ceiling) ∧ (qc_pre_flags floor met) ∧ (no unresolved drift). Any single ∧-term false → fail/reshoot/hold per the §3.2 + Step-8 routing. Deterministic, no thresholds to tune (unlike Style Replication's drift score).
- **§13 Critical Decisions LOCKED** — Day 43 partial 2. Target 10–14 LOCKED decisions. Pre-scaffolded list:
  1. Pre-flight vs pre-publish scope — v1.0 = pre-flight (production → post boundary) ONLY; full #14 pre-publish gate deferred to v1.1 once in-post fleet ships. [LOCKED-as-drafted Day 40]
  2. Universal tier access — all 4 tiers traverse QC Pre-flight (safety is not a tier feature). [LOCKED-as-drafted Day 40]
  3. Verdict model — Pass / Fail / Reshoot, with `drift_unresolved` soft-hold as a 4th human-deferred outcome. [LOCKED-as-drafted Day 40]
  4. Route-back map — fail→responsible agent, reshoot→ProdCoord, drift→human. [PRELIMINARY · operator amend Day 43]
  5. 6-tuple parent_chain — inherits Style Replication 5-tuple + appends `preflight_report_id`; depends on Cross-SPEC §3.9 n-tuple amendment ratification. [DEFERRED — gated on operator ratifying §3.9 amendment]
  6. errorEnvelope code count — 7–9 target. [PRELIMINARY · operator amend Day 43]
  7. Self-QC check count — 10–12. [PRELIMINARY · operator amend Day 43]
  8. False-pass tolerance — ZERO (a brand-safety gate must never pass a breach); bias all ambiguity toward fail/hold. [LOCKED-as-drafted Day 40]
  9. Engine policy — NO generative engine calls; optional native pHash/CLIP re-verify only on contested drift. [LOCKED-as-drafted Day 40]
  10. Recommend-don't-approve — QC Pre-flight emits `human_review_required: true` + verdict recommendation; never flips a reel to "published-approved" (Lever-3 operator action). [LOCKED-as-drafted Day 40]
  11. LUFS / loudness check — DEFERRED to v1.1 (requires Sound agent output, not built). [LOCKED-as-drafted Day 40]
  12. Schema strategy — new `preflight_report` output schema; reuse Cross-SPEC errorEnvelope + metadata shapes. [LOCKED-as-drafted Day 40]
- **§14 Calendar status updates** — Day 41 partial 1. Day 40 ✓ → trajectory populated.
- **§15 Change Log** — Day 43 partial 2. v1.0 lifecycle entries (outline-day-40 → body-day-41 → Rest Day-day-42 → body-day-43 → LOCK-candidate → schemas → SKILL → runbook → LOCKED). Parked candidates list.
- **§16 Metadata Block Schema** — Day 43 partial 2. Cross-SPEC §3.9 canonical fields + 4 QC Pre-flight additions (6-tuple parent_chain, qc_gate_class, verdict_evidence_hash, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit at LOCK candidate)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `qc-preflight-agent` (kebab-case, matches the fleet pattern) |
| §3.2 literal_seed_inherit / hash invariant | ✅ `verdict_evidence_hash` SHA-256 over evidence block; Mode B negative-prompt SHA-256 chain cross-check |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord / AI Video Gen / Style Replication shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) + adds `verdict` + `route_back_to` |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ **This agent is the adjudicator of the §3.4 floor** — Step 3 enforces it across all 6 upstream stages |
| §3.5 Mode coverage matrix | ✅ §4 explicit mode-agnostic verdict + mode-aware reporting (A/B/C) |
| §3.6 Slot 11 naming canon | ✅ Reserved `preflight_qc_agent_failed` for §6 check list |
| §3.7 qc_pre_flags format | ✅ Step 3 shape adjudication |
| §3.8 Tier↔mode firewall (7th defense-in-depth) | ✅ Step 2 + §4 universal-tier table |
| §3.9 Metadata block + n-tuple parent_chain | ✅ §3.3 inherits canonical + extends to 6-tuple. **Forcing function for the §3.9 n-tuple amendment ratification** (operator-pending). |
| §3.10 Cost ceiling authority | ✅ §4 combined-ceiling reconciliation + Step 7 enforcement (first agent with total-spend visibility) |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify any LOCKED canon — all AI Video Gen / Style Replication / Cross-SPEC references read-only |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit embedded in the LOCK candidate.

---

## Open Questions (Day 40 outline — 6 parked for operator amendment)

1. **Pre-flight vs full #14 QC scope** — v1.0 gates production → post boundary only. Confirm the full pre-publish #14 gate is a v1.1 deliverable (built after the in-post fleet ships). *(Donna recommends: confirm pre-flight-only for v1.0 — it is the buildable, highest-leverage slice.)*
2. **`drift_unresolved` soft-hold semantics** — is a carried drift warning a hold-for-human (Donna's draft) OR an outright fail? *(Donna recommends: soft-hold — auto-failing brand-finish drift is too aggressive when a human may accept it.)*
3. **6-tuple parent_chain** — depends on the Cross-SPEC §3.9 n-tuple-as-lineage amendment, which is **DRAFTED but still operator-unratified** (carried from Style Replication Day 32 Item 11). QC Pre-flight is the first 6-tuple consumer — its build is the forcing function. *(Donna recommends: RATIFY the §3.9 amendment AS-DRAFTED so all 17 agents inherit n-tuple lineage.)*
4. **Route-back automation depth** — v1.0 emits `route_back_to` + `recovery_path` (advisory). Should the Orchestrator auto-re-enter, or hold for operator dispatch? *(Donna recommends: advisory in v1.0; auto-re-entry is a v1.1 Orchestrator feature.)*
5. **False-pass tolerance** — confirm ZERO false-pass policy (bias all ambiguity to fail/hold). *(Donna recommends: ratify zero-false-pass — over-blocking is the safe failure direction for a brand-safety gate.)*
6. **Reshoot verdict scope** — confined to Mode A (live footage) only, since AI output is re-generated not re-shot? *(Donna recommends: yes — `reshoot` is Mode A-exclusive; Mode B/C defects route as `fail` to the production agent.)*

All 6 are non-blocking through the outline kickoff. Defaults proposed; operator can override on the §13 critical-decisions walk.

---

## v1.0 Build Calendar (full QC Pre-flight trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 40 | Fri May 29 | **SPEC outline §0–§5** [SHIPPING NOW] | Style Replication Day 29 outline |
| 41 | Sat May 30 | SPEC body partial 1: §6 + §7 + §10 + §14 | Style Replication Day 30 |
| 42 | Sun May 31 | **REST DAY** — no build (pre-stage partial 2 scaffold only) | Day 21/28/35 Rest Day compounding |
| 43 | Mon Jun 1 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 **OR** commercial-launch pivot per operator | Style Replication Day 31 |
| 44+ | TBD | LOCK candidate → schemas → SKILL bundle → LLM-test runbook → v1.0 LOCK | Style Replication Day 32–37 |

**Sprint context:** QC Pre-flight is **Agent #7** — it extends the fleet past the six launch-critical agents. The 42-day sprint's headline deliverable (Mode B Pro single-reel commercial demo) ships on the six built agents; QC Pre-flight v1.0 LOCK lands in the **post-launch hardening window**. This outline is the forward-design head-start, authored on the same forward-looking basis the Style Replication outline was (while prior LOCK ceremonies were operator-gated).

---

## Files produced today (Day 40)

- `ars/ARS-2026-05-29-Day-40-QC-Preflight-Agent-SPEC-Outline.md` — this doc
- `ars/build-log-2026-05-29.md` — Day 40 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 40)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked. (QC Pre-flight by design calls no generative engine — appropriate for a pure quality-gate agent.)
- ✅ **No external comms.** No emails sent, no DMs, no social posts, no investor/client outreach. The morning SMS handoff to Jamila (Google Voice [status number redacted]) is the only outbound, per CLAUDE.md — it announces status, it does not transact business.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine runs, zero $ spent.
- ✅ **No operator-impersonation.** AI Video Gen Day 24 Items 8 + 11 + Day 27 sit-down verdict NOT assumed. Style Replication Day 32 Items 6 + 8 + 11 NOT silently ratified. Both LOCK ceremonies confirmed STILL-PENDING via on-disk file-state (version tags unflipped). Cross-SPEC §3.9 amendment NOT silently committed. Day 36 LLM Test Runbook execution NOT assumed.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. Zero net-new modifications to any LOCKED canon — all references read-only. QC Pre-flight v1.0 LOCK will hard-gate itself on the production-tier agents' LOCKs being closed first.
- ✅ **All prior canon read-only.** Brief / Script / Storyboard / ProdCoord / AI Video Gen / Style Replication SPECs + schemas + SKILL bundles + Day 35 primer + Day 36 runbook — every prior canon file untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon. (Note: the entity-firewall regex in §5 Step 2 enumerates HC/NPOX tokens precisely so the agent can BLOCK them — this is the firewall's block-list, not a cross-entity reference.)
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit at LOCK candidate.
- ✅ **Pattern source acknowledged.** Style Replication Day 29 outline structure inherited verbatim. AI Video Gen Day 22 outline + Orchestration Blueprint #14 QC definition + Cross-SPEC §3.4 floor used as the grounding spine. No bespoke departures from canon.

---

*Day 40 ships clean. Day 41 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). QC Pre-flight is Agent #7 of 17 — the 7th defense-in-depth firewall and the first universal-tier gate since Brief. It is the agent the qc_pre_flags minItems-4 floor was built for. Operator pickup: (1) the two production-tier LOCK ceremonies (AI Video Gen + Style Replication) remain pending and gate QC Pre-flight's eventual v1.0 LOCK; (2) review the §13 critical-decisions list + ratify the Cross-SPEC §3.9 n-tuple amendment so the 6-tuple parent_chain is canon.*
