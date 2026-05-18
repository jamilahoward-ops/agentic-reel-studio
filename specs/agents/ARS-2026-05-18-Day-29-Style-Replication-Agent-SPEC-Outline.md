# ARS — Style Replication Agent v1.0 SPEC OUTLINE (§0–§5)

**Date:** Mon May 18, 2026 (Day 29 of 42 · Wk5D3)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** OUTLINE ONLY — §0–§5 drafted (purpose, scope, inputs, outputs skeleton, tier constraints, process). Full SPEC body §6–§16 + LOCK target Day 32 (Thu May 21). Schemas Day 33. SKILL bundle Day 34. LLM-test runbook Day 36. v1.0 LOCK Day 37 (Wk5 close).
**Pattern source:** `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (Day 20 outline — proven 17-section shape inherited verbatim; v1.0 LOCK-quality target).
**Pre-scaffold source:** `ARS-2026-05-17-Day-28-Rest Day-Day-29-Branch-Primer.md` (15 critical decisions pre-enumerated under Branch A · this doc resolves/expands each).
**Predecessor agent:** AI Video Gen Agent (consumes its `rendered_shots.json` output as anchor source — schemas LOCKED Day 25, SKILL bundle SHIPPED Day 26, v1.0 LOCK candidate ratification still operator-gated as of Day 29 start).
**Successor agents:** Edit Director (all modes), QC Agent (post-replication gate), and Mode C dedicated downstream TBD Week 5+.

> **AI Video Gen v1.0 LOCK status awareness (CRITICAL — do not silently advance):** As of this outline's authoring, the Day 24 LOCK candidate has 9/11 reviewer items autonomously verdicted PASS by Donna, but **Items 8 + 11 remain explicitly OPERATOR-ONLY**. The Day 27 LLM Test sit-down outcome is unconfirmed. This outline is therefore authored under the assumption that AI Video Gen v1.0 **will be** LOCKED but uses no production output from it; references are to LOCK-as-drafted SPEC + schema canon, both of which are LOCK-stable as text artifacts. Style Replication v1.0 LOCK on Day 37 will hard-gate itself on AI Video Gen v1.0 being LOCKED first. Forward-looking outline work does NOT constitute fake-advance.

---

## §0. Provenance & Build-Phase Position

| Field | Value |
|-------|-------|
| Build phase | Week 5 — Production layer extension (Mode C authorization gate) |
| Agent index | **#6 of 17** (per Orchestration Blueprint Day 5) |
| Pipeline tier | PRODUCTION (second of two — AI Video Gen + **Style Replication**) |
| Mode coverage | **Mode C primary** (style replication / hot path) · **Mode B passthrough** (inherits + passes through rendered anchors) · **Mode A passthrough** (user-provided footage style-graded) |
| Predecessor SPEC | `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` (Day 24 LOCK candidate — operator-gated) |
| Predecessor schemas | `skills/ai-video-gen-agent/schemas/output.schema.json` Day 25 LOCKED |
| Predecessor SKILL bundle | `skills/ai-video-gen-agent/` Day 26 SHIPPED (23 files · 11/11 validation PASS) |
| Cross-spec canon | `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED) — naming, errorEnvelope shape, qc_pre_flags format, 4-tuple parent_chain, metadata block all inherited |
| Defense-in-depth layer | **6th** firewall pass (Brief → Script → Storyboard → ProdCoord → AI Video Gen → **Style Replication**) |
| Lever inheritance | Reads `lever_state` from upstream `metadata` block; emits `human_review_required` per Lever 3 default until Day 60+ Lever-2 graduation gate |
| Pricing tier authority | **Pro tier (Mode B → C passthrough)** + **Enterprise tier (Mode A + B + C)** — Pilot/Starter NEVER reach this agent (same gating as AI Video Gen) |
| Cost authority class | **Lower than AI Video Gen** — Style Replication does NOT call render engines for net-new generation in Mode C hot path. Engine calls limited to: (a) style fingerprint extraction (CLIP / pHash compute, ~$0.001/shot), (b) Mode A user-clip style grade pass (Pika Style Tokens / Runway Style Reference, $0.10–$0.40/shot), (c) optional re-render on drift beyond tolerance (rare, Lever-3 only, requires human approval). |

**Build calendar (Week 5 close target):**
- **Day 29** (today, Mon May 18 · Wk5D3) — SPEC outline §0–§5 [SHIPPING NOW]
- Day 30 (Tue May 19 · Wk5D4) — SPEC body partial 1: §6 12-Check Self-QC + §7 System Prompt v1.0 frame + §10 Field Map scaffold
- Day 31 (Wed May 20 · Wk5D5) — SPEC body partial 2: §8 Performance Targets + §9 Test Fixtures + §11 Cost Model + §12 Style Consistency Math (inherits AI Video Gen §12 directly) + §13 Critical Decisions (target 12–15 LOCKED) + §15 Change Log + §16 Metadata Block
- Day 32 (Thu May 21 · Wk5D6) — Unified LOCK CANDIDATE (parallels Day 24 pattern · 11-item reviewer checklist)
- Day 33 (Fri May 22 · Wk5 close) — `input.schema.json` + `output.schema.json` (Draft 2020-12 · 4-tuple parent_chain extension · polymorphic output)
- Day 34 (Sat May 23 · Wk6D1 — Wk5 spillover) — SKILL bundle (~10–15 files · 5 test fixtures · 5/5 inputs validate clean)
- Day 35 (Sun May 24 · Wk6D2) — **REST DAY** (no build)
- Day 36 (Mon May 25 · Wk6D3) — LLM Test Runbook (paste-and-run · pattern from Day 11 / 19 / 27)
- Day 37 (Tue May 26 · Wk6D4) — v1.0 LOCK (Wk5 close target slipped by 1 day · operator-gated sit-down)

**Rest Day compounding pattern reuse:** Day 21 (Rest Day) pre-staged Day 22 scaffolds with 21 grep-able `<<TBD-D22-*>>` markers. Day 35 will pre-stage Day 36 LLM test runbook scaffold using identical pattern. Day 28 (just-past) similarly pre-staged Day 29 with the 15-decision scaffold — pattern validates.

---

## §1. Purpose & Position in Pipeline (LOCKED on intent)

The **Style Replication Agent** is the second production-tier agent in ARS. It is the **brand-aesthetic gate** of the pipeline — the moment a rendered shot or sourced clip stops being raw pixels and starts being recognizably *the brand*.

Production gates already passed:
- AI Video Gen Agent = render gate ("Did the pixels come out matching the brief, on-budget, with style consistency, with no firewall breach in the prompt?")

The Style Replication Agent picks up downstream:
- **Style Replication Agent = brand gate ("Are these pixels recognizably the brand's pixels? Does the palette match? Does the motion grade match? Does the brand finish layer apply consistently across the reel? If a viewer sees one shot, can they identify the brand without seeing a logo?")**

**Single-responsibility line (LOCKED):**
> *"Brand-aesthetic transfer onto rendered or sourced footage. Inherits anchor style from rendered_shots; applies consistent palette, motion grade, framing tokens, and brand finish layer across all inheritor shots without re-renders."*

**Why "without re-renders" matters:** Re-rendering is expensive ($0.20–$0.95/sec across engines per Day 23 §11 pricing canon). Style Replication's economic justification is that brand consistency can be achieved through **inheritance** + **grade pass** rather than **regeneration**. A reel with 5 shots at Enterprise tier ($165/shot ceiling per Day 22 §7 tier table) cannot afford to re-render the 4 inheritor shots if the anchor shot's brand aesthetic drifted. Style Replication enforces aesthetic consistency at ~5–10% of the cost of a re-render — that delta is the agent's reason for existence.

**Pipeline position (per Orchestration Blueprint §5):**
```
Trend Hunter → Strategy → Brief → Script → Storyboard → Production Coord →
   ├── (Mode A) Live shoot — human videographer + crew → Style Replication (style grade pass only)
   ├── (Mode B) AI Video Gen → Style Replication (anchor inherit + grade pass)
   └── (Mode C) Style Replication (hot path: pull from locked anchor cache + apply to new prompt — no AI Video Gen call)
→ Edit Director → Editor → Sound → Motion → QC → Localization → Publishing → Loop
```

**Why Mode C is the highest-margin mode in ARS:** Mode C bypasses both human shoot (Mode A cost driver) AND per-shot engine render (Mode B cost driver). At Enterprise tier, Mode C reduces production cost per reel from ~$612 (Mode B 5-shot envelope per Day 23 §9 TC-02) to ~$60–$120 (style fingerprint extraction + grade pass + QC). The agent must therefore enforce **a strict anchor-binding rule** — Mode C is permissible ONLY when a LOCKED brand anchor exists in cache + the new prompt does not request shots outside the anchor's coverage envelope. Otherwise, fall back to Mode B (which DOES call AI Video Gen).

**Hand-off contract enforced:**
- **INPUT contract:** Style Replication reads (depending on mode):
  - Mode B input: `rendered_shots.json` from AI Video Gen per Day 25 output.schema.json. Re-validates tier↔mode + entity firewall (defense-in-depth, **sixth time**). Halts with `not_replication_compatible` errorEnvelope if input branch is `errorEnvelope` not `successRenderedShots`.
  - Mode A input: User-provided footage URIs + `production_plan.json` `mode_a_plan` branch (ProdCoord canon). Re-validates user-footage entity-firewall pass (no banned-vocab in metadata, no buildings in frames per Hard Rule #8 inherit).
  - Mode C input: `production_plan.json` `mode_c_plan` branch (ProdCoord canon) + cached brand anchor reference (anchor_id pointing to LOCKED anchor in `brand_anchor_cache/`). Halts with `anchor_unavailable` if cache miss.
- **OUTPUT contract:** Emits `replicated_shots.json` per §3 of this spec (polymorphic: `successReplicatedShots` | `errorEnvelope`). Downstream production agents (Edit Director, QC, Localization) read this without re-deriving from upstream.

**v1.0 boundary (in-scope vs. deferred):**

| In-scope v1.0 | Deferred v1.1+ |
|---------------|----------------|
| 3-mode coverage (A grade pass, B inherit, C hot path) | Real-time style preview UI |
| Single brand anchor per reel | Multi-brand simultaneous inheritance (cross-brand reel — rare use case) |
| Style fingerprint: pHash + CLIP + palette (inherits Day 23 §12 canon directly) | Custom LoRA inheritance per brand (Sequel V1+ scale path; cost-heavy at v1.0 scale) |
| Drift threshold 0.85 (mirrors AI Video Gen Day 23 §12 default) | Per-engine drift threshold recalibration (parked Day 23 candidate) |
| 5 errorEnvelope codes minimum (target ~6–8 LOCKED Day 30) | Auto-anchor-switch on coverage envelope mismatch (Mode C escape hatch deferred) |
| Engine selection: Runway Style Reference (primary) + Pika Style Tokens (fallback) + native pHash/CLIP/palette compute (no engine call) | Third-party LUT import (DaVinci .cube file support — v1.2+ creative path) |
| Per-reel cost ceiling: Pro $50 / Enterprise $120 (proposed — operator amend Day 30) | Per-shot cost ceiling (current = per-reel envelope; per-shot ceiling deferred to v1.1) |
| Mode A grade-pass single-stage only | Multi-pass grade refinement (artistic iteration; v1.1+ enterprise creative tier) |
| Anchor identity check at runtime (anchor_id matches LOCKED anchor → SHA-256 verification) | Anchor versioning beyond v1.0 (anchor rev-management deferred) |
| Pilot/Starter tier NEVER reaches this agent (tier↔mode firewall fires upstream at Brief/Script/Storyboard) | Pilot tier Mode C unlock (sales-tier feature for future cohort; not v1.0 scope) |

**Pricing tier table (inherited from Day 6 Service Tier + Pricing Model · Day 22 §7 tier table mirror):**

| Tier | Mode Access | Style Replication Per-Reel Ceiling | Re-render fallback |
|------|-------------|-----------------------------------|-------------------|
| Pilot — Founding 5 | Mode A only | **N/A — does NOT reach this agent** | N/A |
| Starter — Operator | Mode A only | **N/A — does NOT reach this agent** | N/A |
| Pro — Studio | Mode A + B | **$50 per reel** | NOT permitted in v1.0 (cost gate) |
| Enterprise — Agency | Mode A + B + C | **$120 per reel** | Permitted with `human_review_required: true` Lever-3 only |

Tier ceilings reconciled with AI Video Gen Day 22 §7 ($400 Pro / $750 Enterprise) — Style Replication operates within the same per-reel envelope as the upstream renderer, NOT in addition to it. Combined Pro reel envelope: $400 (AI Video Gen) + $50 (Style Replication) = $450 hard ceiling. Enterprise: $750 + $120 = $870 hard ceiling. Both still inside the tier gross margin floor of 5× per Day 6 pricing canon.

---

## §2. Inputs

The Style Replication Agent has **three input branches** corresponding to the three production modes. Schema discriminator: `production_mode` field carried in upstream `metadata` block per Cross-SPEC §3.9.

### §2.1 Mode A input branch — user-source style grade

**When invoked:** Operator + videographer have delivered a `production_plan.json` with `production_mode == "A"` AND `mode_a_plan != null`. User-provided footage URIs (S3 / Drive / WeTransfer references) are listed in `mode_a_plan.source_clips[]`.

**Required input fields (preliminary — full schema Day 33):**
```json
{
  "production_plan": { /* full ProdCoord output, mode_a_plan branch active */ },
  "metadata": { /* Cross-SPEC §3.9 — production_mode, agent_id, parent_chain, session_id, etc. */ },
  "source_clips": [
    {
      "clip_id": "clip-001",
      "asset_uri": "ars://user-upload/REINVENTED/sess-2026-05-18-abc/clip-001.mp4",
      "duration_sec": 12.4,
      "resolution": "1080x1920",
      "shot_intent": "anchor",
      "qc_pre_flags": ["..."]
    }
  ],
  "brand_anchor_reference": { /* see §2.4 */ }
}
```

**Hard validations on Mode A input (defense-in-depth pass 6):**
1. `production_mode == "A"` AND `mode_a_plan != null`.
2. Every `source_clips[i].asset_uri` matches `ars://user-upload/{brand}/.../...` pattern (relative URI per Hard Rule #8 inherit).
3. `source_clips[].qc_pre_flags` contains ZERO banned-vocab tokens (entity firewall + no-buildings per Hard Rule #8 inherit).
4. At least one `source_clips[i].shot_intent == "anchor"` (style anchor for grade pass).
5. `brand_anchor_reference.anchor_id` resolves to a LOCKED brand anchor in cache (mandatory for Mode A grade pass to have a target aesthetic).

### §2.2 Mode B input branch — AI Video Gen passthrough + inherit

**When invoked:** Upstream AI Video Gen Agent has emitted a `successRenderedShots` payload. `production_mode == "B"` AND `successRenderedShots.rendered_shots[]` non-empty AND every shot's `render_status == "completed"`.

**Required input fields:**
```json
{
  "rendered_shots": [ /* AI Video Gen output.schema.json successRenderedShots branch */ ],
  "metadata": { /* Cross-SPEC §3.9 — inherits parent_chain from AI Video Gen (extends to 4-tuple this agent) */ },
  "anchor_shot_id": "shot-001",
  "brand_anchor_reference": { /* see §2.4 */ }
}
```

**Hard validations on Mode B input:**
1. Upstream branch is `successRenderedShots`, NOT `errorEnvelope`. (If errorEnvelope, halt with `not_replication_compatible`.)
2. `anchor_shot_id` resolves to a member of `rendered_shots[]` with `render_status == "completed"` AND `asset_uri` pattern valid.
3. Every `rendered_shots[i].negative_prompt_attached_bool == true` (Hard Rule #10 inherit verified at parse).
4. SHA-256 negative-prompt invariant: all rendered_shots share one `negative_prompt_sha256` value (forensic check — inherited canon from Day 22 §6 Check #10).
5. 4-tuple parent_chain extends correctly: input parent_chain is 4-tuple from AI Video Gen → this agent appends own production_plan_id reference to form 5-tuple? **DEFERRED to Day 30 §10 field map decision** — Cross-SPEC §3.9 currently specifies 4-tuple; Style Replication may extend or pass-through. Day 30 LOCK decision.

### §2.3 Mode C input branch — hot path / pure inherit (highest-margin path)

**When invoked:** `production_plan.json` has `production_mode == "C"` AND `mode_c_plan != null`. Mode C is unlocked ONLY at Enterprise tier per Day 6 pricing canon. No upstream AI Video Gen call has occurred for this reel.

**Required input fields:**
```json
{
  "production_plan": { /* mode_c_plan branch active */ },
  "metadata": { /* production_mode == "C" */ },
  "brand_anchor_reference": {
    "anchor_id": "anchor-REINVENTED-v2-locked-2026-05-15",
    "anchor_uri": "ars://brand_anchor_cache/REINVENTED/anchor-REINVENTED-v2-locked-2026-05-15.json",
    "anchor_locked_date": "2026-05-15",
    "anchor_sha256": "..."
  },
  "new_shot_prompts": [
    {
      "shot_id": "shot-001",
      "prompt_text": "Operator close-up at iMac, golden hour, brand-anchor inherited",
      "shot_intent": "hero",
      "qc_pre_flags": ["..."]
    }
  ]
}
```

**Hard validations on Mode C input (strictest — Mode C is highest-risk economically):**
1. `production_mode == "C"` AND `mode_c_plan != null`.
2. `brand_anchor_reference.anchor_id` resolves to LOCKED anchor in cache (Hard FAIL if cache miss → `anchor_unavailable` errorEnvelope).
3. `brand_anchor_reference.anchor_sha256` matches the cache's stored hash for that anchor (forensic anti-tamper).
4. `brand_anchor_reference.anchor_locked_date` is within 90 days of current run date (anchor freshness gate — anchors older than 90 days require explicit operator re-validation; deferred to Day 30 §13 critical decision).
5. Every `new_shot_prompts[i].prompt_text` passes the entity firewall + no-buildings + banned-vocab walk (same 11-point QC gate as Brand Voice Intake v1.0).
6. Tier validation: upstream `metadata.tier == "enterprise"` (Mode C is Enterprise-only at v1.0).
7. Coverage envelope check (Day 30 §13 critical decision): the prompts must request shots whose visual intent is *within* the anchor's coverage envelope (operator close-up, iMac scene, REINVENTED palette). Out-of-envelope prompts (e.g., "outdoor stadium establishing shot" when anchor is iMac workbench) → halt with `coverage_envelope_mismatch` errorEnvelope OR fall back to Mode B with explicit `human_review_required: true` flag.

### §2.4 brand_anchor_reference (shared across all 3 modes)

The `brand_anchor_reference` block is required for ALL three input modes. It points to a LOCKED brand anchor in `brand_anchor_cache/` — a directory of style fingerprints, palette extracts, motion grade tokens, and brand finish layer specs, one per LOCKED brand.

```json
{
  "anchor_id": "anchor-REINVENTED-v2-locked-2026-05-15",
  "anchor_uri": "ars://brand_anchor_cache/REINVENTED/anchor-REINVENTED-v2-locked-2026-05-15.json",
  "anchor_locked_date": "2026-05-15",
  "anchor_sha256": "...",
  "anchor_coverage_envelope": ["operator-portrait", "iMac-workbench", "golden-hour-indoor"],
  "anchor_lever_state": "lever-3-strict"
}
```

**v1.0 anchor cache scope:** REINVENTED (pilot customer per Cross-SPEC canon). One LOCKED anchor at v1.0 launch. Sequel Digital paid clients will each have one LOCKED anchor at onboarding (operator-controlled via Brand Voice Intake skill).

**Anchor LOCKED definition:** An anchor is "LOCKED" when (a) it has passed operator review via Brand Voice Intake skill v1.0, (b) all 4 style components (palette, motion grade, framing tokens, brand finish layer) have explicit human approval, (c) anchor_sha256 has been computed and stored, (d) anchor_locked_date is recorded. LOCKED anchors are read-only at this agent's runtime; modifications require a new anchor with a new anchor_id (versioning v1.0 baseline).

---

## §3. Outputs (skeleton)

The Style Replication Agent emits one of two polymorphic outputs per invocation. Mirrors AI Video Gen Day 25 output.schema.json pattern (oneOf [successRenderedShots, errorEnvelope]).

### §3.1 successReplicatedShots branch (happy path)

```json
{
  "output_type": "successReplicatedShots",
  "replicated_shots": [
    {
      "shot_id": "shot-001",
      "source_shot_id": "shot-001",
      "source_mode": "B",
      "asset_uri": "ars://replicated/REINVENTED/sess-.../shot-001-styled.mp4",
      "anchor_id_inherited": "anchor-REINVENTED-v2-locked-2026-05-15",
      "style_match_score": 0.91,
      "palette_delta_score": 0.94,
      "motion_grade_delta_score": 0.89,
      "brand_finish_layer_applied_bool": true,
      "drift_warning_bool": false,
      "cost_incurred_usd": 0.08,
      "engine_used": "native-clip-pHash-palette",
      "qc_pre_flags": [],
      "negative_prompt_attached_bool": true,
      "negative_prompt_sha256": "..."
    }
  ],
  "total_replication_cost_usd_actual": 0.40,
  "tier_cost_ceiling_usd": 50,
  "anchor_status": "inherited",
  "anchor_id": "anchor-REINVENTED-v2-locked-2026-05-15",
  "drift_summary": {
    "shots_within_tolerance": 5,
    "shots_with_drift_warning": 0,
    "shots_with_drift_failure": 0,
    "aggregate_style_match_score": 0.91
  },
  "engines_used": ["native-clip-pHash-palette"],
  "handoff_targets": ["edit-director", "qc-agent"],
  "metadata": { /* Cross-SPEC §3.9 with Style Replication additions per §3.3 */ }
}
```

### §3.2 errorEnvelope branch (failure path)

```json
{
  "output_type": "errorEnvelope",
  "failure_code": "anchor_unavailable",
  "failed_check_id": 1,
  "attempts": 1,
  "anchor_status": "missing",
  "anchor_id_requested": "anchor-REINVENTED-v2-locked-2026-05-15",
  "cost_incurred_usd": 0.01,
  "tier_cost_ceiling_usd": 50,
  "detail": {
    "cache_miss_reason": "anchor_uri does not resolve in brand_anchor_cache/",
    "cache_lookup_path_attempted": "ars://brand_anchor_cache/REINVENTED/anchor-REINVENTED-v2-locked-2026-05-15.json"
  },
  "metadata": { /* Cross-SPEC §3.9 */ },
  "human_review_required": true
}
```

### §3.3 Metadata block additions (Style Replication-specific)

Inherits all 11 Cross-SPEC §3.9 canonical fields PLUS extends with:
- `style_fingerprint_summary` — {pHash_method, clip_model_version, palette_extraction_method, drift_threshold_used}
- `anchor_cache_version` — string version identifier for the cache layer at runtime (e.g., "anchor_cache_v1.0")
- `runtime_environment_class` — enum (dev / staging / production) inherit from AI Video Gen §16

### §3.4 errorEnvelope code namespace (target 6–8 LOCKED Day 30)

Preliminary code list (operator amendment Day 30 §13 critical decisions walk):

| Code | Triggered by | failed_check_id | Notes |
|------|--------------|-----------------|-------|
| `anchor_unavailable` | brand_anchor_cache miss OR anchor_sha256 mismatch | 1 | Hard FAIL — cannot replicate without anchor |
| `style_drift_exceeded` | aggregate_style_match_score < 0.85 (drift threshold) | 2 | Soft warning in v1.0 (mirrors AI Video Gen Day 23 §12 default) — emits with `drift_warning_bool: true` per shot, halts only if aggregate < 0.70 (hard floor) |
| `palette_extraction_failure` | CLIP/pHash compute failed on source clip OR rendered_shot | 3 | Often engine-side failure (rare) |
| `motion_grade_mismatch` | Mode A clip motion grade outside anchor envelope by > 25% | 4 | User-source path failure mode |
| `brand_finish_layer_missing` | Anchor cache returned anchor without brand_finish_layer spec | 5 | LOCK-time anchor was incomplete — escalates to operator |
| `cost_overrun` | total_replication_cost_usd_actual > tier_cost_ceiling_usd | 6 | Hard FAIL — mirrors AI Video Gen Day 23 §13 Decision #15 |
| `coverage_envelope_mismatch` | Mode C prompts outside anchor coverage envelope | 7 | Mode C-specific — Day 30 §13 LOCK decision |
| `qc_pre_flags_format_violation` | qc_pre_flags array shape violates Cross-SPEC §3.7 | 8 | Defense-in-depth pass — same code as AI Video Gen §13 Decision #11 |
| `not_replication_compatible` | Upstream errorEnvelope passed as input (Mode B branch) | (reserved) | Day 30 LOCK decision: separate code OR alias to anchor_unavailable? |

**Target Day 30 LOCK:** 6–8 codes, each with trigger condition + failed_check_id + recovery path. Mirrors AI Video Gen 17-code shape but scoped tighter (Style Replication has narrower failure surface).

---

## §4. Tier Constraints & Mode Coverage

**Per-tier mode access (LOCKED upstream — restated for defense-in-depth pass 6):**

| Tier | Modes accessible | Reaches Style Replication? | Style Replication ceiling |
|------|------------------|---------------------------|--------------------------|
| Pilot | A | **NO** — Pilot does not unlock Mode B or C | N/A |
| Starter | A | **NO** | N/A |
| Pro | A, B | **YES** for Mode A grade pass + Mode B inherit | **$50/reel hard ceiling** |
| Enterprise | A, B, C | **YES** for all 3 modes | **$120/reel hard ceiling** |

**Cost ceiling rationale:**
- **Pro $50:** Mode A grade pass ($20–40 worst case across 8 shots) + Mode B inherit (mostly free, native compute ~$0.40) + 25% buffer.
- **Enterprise $120:** Mode A grade pass with finer LUT ($60 worst case) + Mode B inherit + Mode C hot path inherit (~$10) + Mode C optional re-render fallback ($30, Lever-3 gated only) + 25% buffer.

**Margin floor preserved:** Pro tier delivers 8 reels/mo at Pro-tier. Combined production envelope per reel = $450 (Mode B AI Video Gen $400 + Style Replication $50). Combined 8-reel monthly production cost ceiling = $3,600. Pro tier gross margin floor = 5× per Day 6 canon. Tier price Pro-tier / Cost $3,600 = 2.08× → **WARNING: at production cost ceiling, Pro tier is below 5× margin floor.** This is intentional — production cost ceilings are runtime upper bounds, not target averages. Target average production cost = $200–250/reel = 8 reels × $225 = $1,800/mo cost. Pro-tier / $1,800 = 4.17× — still below 5× floor. **Operator decision Day 30 §13 critical decision walk:** raise Pro production target average OR raise Pro tier price OR accept 4–5× actual margin at scale (vs 5× floor). Flagged for operator amendment.

**Enterprise check:** 30 reels/mo × $290 target average = $8,700/mo cost. Tier price Enterprise-tier. tier price / 8.7K = 1.72× → **FAIL margin floor.** Same flag as Pro. Day 30 §13 decision: production target average vs tier price reconciliation. Operator may raise Enterprise tier price to $20K to maintain 5× floor (parked Day 23 candidate from AI Video Gen SPEC).

**v1.0 enforcement choice (DEFAULT — operator can override Day 30):** Maintain $50/$120 hard ceilings at runtime regardless of margin math. Margin reconciliation is a pricing-tier conversation, not a runtime authority. Flag in Day 30 §13 critical decisions.

**Engine cost reality (preliminary — Day 31 §11 cost model authoring will LOCK):**

| Mode | Engine path | Per-shot cost estimate | Per-reel cost (avg) |
|------|-------------|----------------------|--------------------|
| A grade pass | Pika Style Tokens OR Runway Style Reference | $0.10–$0.40 | $0.80–$3.20 (8 shots) |
| B inherit | Native CLIP + pHash + palette extract (no engine call) | $0.001–$0.01 | $0.01–$0.08 (8 shots) |
| C hot path | Native compute + optional Pika Style Tokens on new prompts | $0.10–$0.30 | $0.50–$2.40 (8 shots) |
| C re-render fallback (Lever-3 only) | Runway Gen3 Alpha (≤2 shots) | $5.70/shot (6sec) | $11.40 (2 shots) |

Engine cost reality is **dramatically lower than AI Video Gen** because Style Replication does not call generative video models in the happy path — it calls *style transfer* models (Pika Style Tokens at $0.10/shot, Runway Style Reference at $0.40/shot) plus native CLIP/pHash/palette compute (essentially free per shot at ~$0.001).

---

## §5. Process Steps (System Prompt Skeleton — Day 30 §7 will LOCK)

The agent runs an 11-step loop per invocation (mirrors AI Video Gen Day 22 §7 11-step process — pattern source). Each step has a verifiable termination state; the loop halts on first hard FAIL.

**Step 1 — Parse input + detect mode branch**
- Parse input JSON against `input.schema.json` (Day 33 LOCKED).
- Detect `production_mode` (A / B / C) — branches into different Step-3 paths.
- Validate `brand_anchor_reference.anchor_id` resolves in cache. Hard FAIL → `anchor_unavailable`.
- Validate Cross-SPEC §3.7 qc_pre_flags shape on every input shot/clip. Hard FAIL → `qc_pre_flags_format_violation`.

**Step 2 — Defense-in-depth firewall pass (sixth time)**
- Walk every input shot/clip's qc_pre_flags + asset_uri + prompt_text (Mode C).
- Banned-vocab walk per Hard Rule #8 inherit (entity firewall + no-buildings).
- Hard FAIL → halt with the appropriate upstream-leaked code. (In v1.0, defense-in-depth pass 6 should NEVER fire — if it does, an upstream agent has a bug. Log forensic.)

**Step 3 — Mode-specific input prep**
- **Mode A path:** Pull source clips. Compute style fingerprint (CLIP + pHash + palette + motion grade extract) per clip. Compare to anchor fingerprint.
- **Mode B path:** Pull rendered_shots. Validate negative_prompt_sha256 invariant across shots (forensic Hard Rule #10 inherit). Compute style fingerprint per shot (same compute as Mode A).
- **Mode C path:** Pull mode_c_plan + new_shot_prompts. Verify coverage envelope match between prompts and anchor coverage envelope. Hard FAIL → `coverage_envelope_mismatch`.

**Step 4 — Anchor style fingerprint load**
- Load LOCKED anchor from cache (`brand_anchor_cache/{brand}/anchor-{anchor_id}.json`).
- Verify anchor_sha256 matches cache-stored hash. Hard FAIL → `anchor_unavailable`.
- Verify anchor_locked_date is within freshness window (90 days). Soft warning if outside.

**Step 5 — Style transfer / inheritance compute**
- **Mode A:** Dispatch grade pass via Pika Style Tokens (primary) or Runway Style Reference (fallback). Per shot, cost ~$0.10–$0.40. Negative prompt attached to every dispatch (Hard Rule #10 inherit — composed prompt template inherits from AI Video Gen Day 26 SKILL bundle `negative_prompt_template.md`).
- **Mode B:** Native CLIP + pHash + palette + motion grade compute per shot. Compare to anchor fingerprint. Compute drift score per shot. No engine call.
- **Mode C:** For each new_shot_prompt, dispatch Pika Style Tokens with anchor's style fingerprint embedded. Per shot, cost ~$0.10–$0.30. Negative prompt attached.

**Step 6 — Drift threshold check per shot**
- For each shot, compute `style_match_score = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette` (inherits AI Video Gen Day 23 §12 formula verbatim).
- If `style_match_score < 0.85` (drift threshold) → emit `drift_warning_bool: true` per shot but do NOT halt (soft warning in v1.0 per AI Video Gen Day 23 §13 Decision #4 inherit).
- If aggregate score across all shots < 0.70 (hard floor) → halt with `style_drift_exceeded` (failure cascade).

**Step 7 — Brand finish layer application**
- Apply anchor's `brand_finish_layer` spec to every shot. v1.0 = static finish (no per-shot variation). LUT, color grade, optional vignette per brand spec.
- Compute `brand_finish_layer_applied_bool` per shot. Hard FAIL on any shot's failure → `brand_finish_layer_missing` (anchor incompleteness escalates to operator).

**Step 8 — Cost ceiling check**
- Sum `cost_incurred_usd` across all shots in current invocation.
- Compare to `tier_cost_ceiling_usd` ($50 Pro / $120 Enterprise).
- Hard FAIL on overrun → `cost_overrun`. Per-shot attribution emitted in errorEnvelope detail block (mirrors AI Video Gen Day 25 schema pattern).

**Step 9 — Negative prompt SHA-256 invariant verification (Mode A & C only)**
- For every dispatched engine call this invocation, verify negative_prompt_sha256 is consistent (single hash across all calls).
- Mirror AI Video Gen §6 Check #10 — Hard Rule #10 enforcement chain. Hard FAIL → forensic log + `qc_pre_flags_format_violation` (re-uses code for negative-prompt-layer breach).

**Step 10 — Construct output payload**
- Build `successReplicatedShots` payload per §3.1.
- Compute `drift_summary` aggregates.
- Set `handoff_targets` array per pipeline canon (`["edit-director", "qc-agent"]` for happy path; `["qc-agent", "human-reviewer"]` if any drift warnings).
- Attach metadata block per §3.3.

**Step 11 — Emit + handoff**
- Validate output payload against `output.schema.json` (Day 33 LOCKED). Hard FAIL → forensic log + halt (output should always validate; failure here = agent bug).
- Emit JSON to stdout (paste-and-run runbook) OR persist to platform path per runtime environment.
- Mark `human_review_required: true` per Lever-3 default (until Day 60+ Lever-2 graduation gate).

**Anti-patterns Step 11 prevents (Lock-time discipline mirror from Day 22 §7):**
- No markdown fences around output JSON.
- No `print()` statements before output JSON block.
- No engine credentials referenced in output.
- No absolute URLs in any `asset_uri` field (Hard Rule #8 inherit).
- No empty `replicated_shots[]` array on success branch (if empty, must be errorEnvelope).

---

## §6–§16 LOCK SCOPE PREVIEW (authoring Days 30–32)

Reserved for SPEC body partial authoring on Days 30–31, then LOCK candidate Day 32. Outline references below are placeholders demonstrating the planned section coverage — actual section text drafted in subsequent days.

- **§6 12-Check Self-QC list** — Day 30 partial 1. Pattern source: AI Video Gen Day 22 §6 (12 checks bipartite-covering 17 errorEnvelope codes). Style Replication targets 10–12 checks bipartite-covering 6–8 errorEnvelope codes (narrower failure surface). Slot 11 of the check list reserved for `style_replication_agent_failed` per Cross-SPEC §3.6 slot naming canon.
- **§7 System Prompt v1.0** — Day 30 partial 1. Frame + 13 hard rules + tier table + 11-step process verbatim from §5 of this outline + voice rule inherit. ~10–12 KB target. Hard Rules 1–13 will mirror AI Video Gen §7 with Style Replication-specific tightening on Mode C anchor-binding discipline.
- **§8 Performance Targets** — Day 31 partial 2. 9 metric categories (mirrors AI Video Gen Day 23 §8). Schema validity 100% / firewall catch 100% / anchor success ≥ 98% (higher than AI Video Gen — Style Replication has fewer engine dependencies) / drift rate ≤ 10%/reel (tighter than AI Video Gen 15%/reel — Style Replication is dedicated to brand consistency) / cost variance ±10% / Pro p50 2 min / p95 5 min / Enterprise p50 4 min / p95 9 min (faster than AI Video Gen because no per-shot render) / retry rate ≤ 0.10/0.15 / fallback ≤ 4% shots.
- **§9 Test Fixtures** — Day 31 partial 2. 5 fixtures portfolio (TC-01 Mode B happy 8-shot inherit · TC-02 Mode C hot path 5-shot · TC-03 Mode A grade pass with drift warning · TC-04 anchor_unavailable failure · TC-05 cost_overrun failure). 5 of 6–8 error codes exercised; remaining 1–3 in schema-only fixtures Day 33.
- **§10 Field Map** — Day 30 partial 1. ~25 rows · passthrough vs transform vs derived columns. Pattern source: AI Video Gen Day 22 §10. Includes per-shot field map + reel-level aggregate field map.
- **§11 Cost Model** — Day 31 partial 2. Engine snapshot table (Pika Style Tokens $0.10/shot · Runway Style Reference $0.40/shot · native compute $0.001/shot). Per-tier cost discipline sweet spot (target 30–60% utilization of $50/$120 ceiling). Calibration windows (first 10 informational / 30 Lever-2 gate / 90 Lever-1 gate — mirror AI Video Gen Day 23 §8).
- **§12 Style Consistency Math** — Day 31 partial 2. **INHERITS Day 23 §12 formula directly:** `style_match_score = 0.40 × s_phash + 0.40 × s_clip + 0.20 × s_palette`. Drift threshold 0.85 default (soft warning in v1.0). Anchor identity check via SHA-256 (hash invariant across reel). Cross-SPEC §3.2 literal_seed_inherit precedent applies to Style Replication's anchor-binding rule.
- **§13 Critical Decisions LOCKED** — Day 31 partial 2. Target 12–15 LOCKED decisions, each: decision · rationale · alternative considered · revisit trigger. Pre-scaffolded list (Day 28 primer + this outline expansion):
  1. Style transfer engine selection — Pika Style Tokens primary + Runway Style Reference fallback + native compute for inheritance. [PRELIMINARY · operator amend Day 31]
  2. Style fingerprint storage format — pHash + CLIP + palette + motion grade (inherits Day 23 §12). [LOCKED-as-drafted Day 29]
  3. Drift threshold — 0.85 inherits from AI Video Gen. [LOCKED-as-drafted Day 29 · revisit Day 60+ if calibration shows Style Replication needs tighter threshold]
  4. Cost ceiling — Pro $50 / Enterprise $120. [PRELIMINARY · operator amend Day 31]
  5. Mode C hot path eligibility — Enterprise tier only + LOCKED anchor + coverage envelope match. [PRELIMINARY · operator amend Day 31]
  6. Brand finish layer authority — anchor-cached spec, applied at runtime. [LOCKED-as-drafted Day 29]
  7. Anchor binding rule — anchor_sha256 hash invariant; literal_seed_inherit precedent. [LOCKED-as-drafted Day 29]
  8. Failure mode coverage — 6–8 errorEnvelope codes (anchor_unavailable, style_drift_exceeded, palette_extraction_failure, motion_grade_mismatch, brand_finish_layer_missing, cost_overrun, coverage_envelope_mismatch, qc_pre_flags_format_violation, not_replication_compatible — target Day 30 reduces to 6–8). [PRELIMINARY · operator amend Day 30]
  9. QC pre-flight checks — 5–6 checks (anchor identity, drift score, palette delta, motion grade tolerance, brand finish presence, optional cost projection). [PRELIMINARY · operator amend Day 30]
  10. Schema strategy — reuse AI Video Gen output.schema.json shapes where possible; new file `style_replication_output.schema.json` only where shapes diverge (oneOf branch difference, successReplicatedShots branch shape, anchor reference block). [LOCKED-as-drafted Day 29]
  11. SKILL bundle authority — Style Replication gets its own SKILL bundle Day 34 (inherits ProdCoord Day 18 + AI Video Gen Day 26 10-file pattern + adds `brand_anchor_cache_template/` directory). [LOCKED-as-drafted Day 29]
  12. Telemetry additions — style_match_score, palette_delta_score, motion_grade_delta_score, brand_finish_layer_applied_bool. [LOCKED-as-drafted Day 29]
  13. Calibration windows — first 10 informational / 30 Lever-2 gate / 90 Lever-1 gate (mirror AI Video Gen). [LOCKED-as-drafted Day 29]
  14. v1.0 scope guardrail — DEFER: real-time style preview, multi-brand simultaneous inheritance, per-engine drift threshold, third-party LUT import, custom LoRA inheritance, multi-pass grade refinement, anchor versioning beyond v1.0. [LOCKED-as-drafted Day 29]
  15. 4-tuple parent_chain extension — pass-through (4-tuple stays 4-tuple) OR extend to 5-tuple (Style Replication appends own production_plan_id reference)? [DEFERRED Day 30 — Cross-SPEC §3.9 currently specifies 4-tuple; Style Replication may extend or pass-through.]

- **§14 Calendar status updates** — Day 30 partial 1. Day 29 ✓ → Day 36 LLM Runbook calendar populated.
- **§15 Change Log** — Day 31 partial 2. v1.0 lifecycle entries (outline-day-29 → scaffold-day-30 → body-day-30 → body-day-31 → LOCK-candidate-day-32 → schemas-day-33 → SKILL-day-34 → Rest Day-day-35 → LLM-runbook-day-36 → LOCKED-day-37). Parked candidates list.
- **§16 Metadata Block Schema** — Day 31 partial 2. 11 Cross-SPEC §3.9 canonical fields + 3 Style Replication additions (style_fingerprint_summary, anchor_cache_version, runtime_environment_class).

---

## Cross-SPEC §3 adherence (preliminary — full audit Day 32 LOCK)

| Cross-SPEC §3 dimension | Adherence status |
|-------------------------|------------------|
| §3.1 Agent naming canon | ✅ `style-replication-agent` (kebab-case, matches Brief / Script / Storyboard / ProdCoord / AI-Video-Gen pattern) |
| §3.2 literal_seed_inherit | ✅ Anchor-binding rule applies same precedent (anchor_sha256 hash invariant across reel) |
| §3.3 errorEnvelope shape | ✅ Mirrors ProdCoord Day 14 + AI Video Gen Day 25 shape (oneOf branch, failure_code, failed_check_id, attempts, detail, cost_incurred_usd, metadata, human_review_required) |
| §3.4 qc_pre_flags snake_case + minItems 4 | ✅ Enforced at Step 2 + schema-layer Day 33 |
| §3.5 Mode coverage matrix | ✅ §1 + §4 explicit 3-mode coverage (A grade pass + B inherit + C hot path) |
| §3.6 Slot 11 naming canon | ✅ Reserved `style_replication_agent_failed` for §6 check list Day 30 |
| §3.7 qc_pre_flags format | ✅ Inherits AI Video Gen Day 22 §6 Check enforcement (same Cross-SPEC source) |
| §3.8 Tier↔mode firewall (6th defense-in-depth) | ✅ Step 2 enforces; tier table §4 reconciles |
| §3.9 Metadata block canonical fields | ✅ §3.3 inherits 11 canonical + adds 3 Style Replication-specific |
| §3.10 Cost ceiling authority | ✅ §4 tier table + Step 8 enforcement. Margin reconciliation flagged Day 31 §13 critical decision. |
| §3.11 LOCK respect (no schema/SPEC edits after LOCK) | ✅ This outline does NOT modify AI Video Gen Day 22/23/24/25/26 canon — all references read-only. |

**No Cross-SPEC §3 violations identified at outline stage.** Full §3 self-audit will be embedded in Day 31 SPEC body partial 2.

---

## Open Questions (Day 29 outline — 6 parked for Day 30+ operator amendment)

1. **Pro vs Enterprise margin floor reconciliation** — at production ceiling envelope, Pro is 4.17× and Enterprise is 1.72× — both below 5× floor canon. Day 30 §13 decision: raise tier prices OR accept actual margin at scale OR raise target average production cost. *(Donna recommends: keep $50/$120 ceilings at runtime, treat margin reconciliation as pricing-tier conversation.)*
2. **Anchor freshness window** — 90 days proposed. Aggressive (60 days) or conservative (180 days)? Day 30 §13 decision.
3. **4-tuple parent_chain extension vs pass-through** — Style Replication appends own `production_plan_id` (5-tuple) OR passes 4-tuple through? Cross-SPEC §3.9 may need extension. Day 30 §10 field map LOCK decision.
4. **Mode C re-render fallback at Lever-3** — permitted with `human_review_required: true` flag, OR forbidden entirely in v1.0 (force Mode B if Mode C fails coverage)? Day 30 §13 decision.
5. **`not_replication_compatible` errorEnvelope code** — separate code OR alias to `anchor_unavailable`? Day 30 errorEnvelope namespace LOCK.
6. **Style transfer engine v1.0 primary** — Pika Style Tokens proposed primary based on cost ($0.10/shot vs Runway $0.40). Operator may prefer Runway for visual quality at Enterprise tier. Day 31 §11 cost model LOCK decision.

All 6 are non-blocking through Week 5 outline kickoff. Defaults proposed; operator can override Day 30 §13 critical decisions walk.

---

## v1.0 Build Calendar (full Style Replication trajectory)

| Day | Date | Deliverable | Pattern source |
|-----|------|-------------|----------------|
| 29 | Mon May 18 | **SPEC outline §0–§5** [SHIPPING NOW] | AI Video Gen Day 20 outline |
| 30 | Tue May 19 | SPEC body partial 1: §6 + §7 + §10 + §14 | AI Video Gen Day 22 |
| 31 | Wed May 20 | SPEC body partial 2: §8 + §9 + §11 + §12 + §13 + §15 + §16 | AI Video Gen Day 23 |
| 32 | Thu May 21 | Unified LOCK CANDIDATE (11-item reviewer checklist) | AI Video Gen Day 24 |
| 33 | Fri May 22 | `input.schema.json` + `output.schema.json` (Draft 2020-12) | AI Video Gen Day 25 |
| 34 | Sat May 23 | SKILL bundle (~10–15 files · 5 test fixtures · 5/5 inputs validate) | AI Video Gen Day 26 + ProdCoord Day 18 |
| 35 | Sun May 24 | **REST DAY** — no build (pre-stage Day 36 LLM runbook scaffold optional, per Day 21 / Day 28 pattern) | Day 21 / Day 28 Rest Day compounding |
| 36 | Mon May 25 | LLM Test Runbook (paste-and-run · 5 fixtures · dry-run engine stubs) | AI Video Gen Day 27 |
| 37 | Tue May 26 | **v1.0 LOCK** — operator-gated sit-down 30–45 min · 5/5 PASS gate | AI Video Gen Day 27+28 LOCK gate |

**Sprint context:** Day 37 v1.0 LOCK + Week 5 close = 5 of 6 weeks complete. Week 6 = commercial launch (landing page + first paid Sequel Digital pilot). Style Replication v1.0 LOCK is the last agent-build deliverable in the sprint — Week 6 is exclusively commercial / go-to-market.

---

## Files produced today (Day 29)

- `ars/ARS-2026-05-18-Day-29-Style-Replication-Agent-SPEC-Outline.md` — this doc (~30 KB target)
- `ars/build-log-2026-05-18.md` — Day 29 build log

Mirror copies in `/outputs/ars/`.

---

## Process integrity (Day 29)

- ✅ **No LLM dispatched.** No render API. No engine credentials referenced. No vendor URLs walked.
- ✅ **No external comms.** No emails sent, no DMs, no social posts, no investor outreach, no client outreach.
- ✅ **No financial commitments.** No subscriptions activated, no quota purchased, no engine API runs initiated.
- ✅ **No operator-impersonation.** Day 27 LLM Test sit-down outcome NOT assumed. Items 8 + 11 ratification NOT silently advanced. AI Video Gen v1.0 LOCK status remains CANDIDATE READY + BUNDLE BUILT + RUNBOOK AUTHORED until operator confirms.
- ✅ **No fake-advance.** This outline is forward-looking planning work, explicitly labeled OUTLINE ONLY. It contains zero net-new modifications to AI Video Gen v1.0 canon — all references read-only. Style Replication v1.0 LOCK on Day 37 will hard-gate itself on AI Video Gen v1.0 being LOCKED first.
- ✅ **All prior canon read-only.** Day 22 + Day 23 + Day 24 LOCK candidate + Day 25 schemas + Day 26 SKILL bundle + Day 27 runbook + Day 28 primer all untouched.
- ✅ **Entity boundary respected.** ARS is Sequel Digital. Zero cross-contamination with HC / NPOX / REINVENTED operations. REINVENTED inside fixtures + brand anchor cache remains brand-as-pilot-customer per Cross-SPEC canon.
- ✅ **Cross-SPEC §3 adherence preliminary audit complete.** 11 of 11 dimensions ✅ at outline stage. Full LOCK audit Day 32.
- ✅ **Pattern source acknowledged.** AI Video Gen Day 20 outline structure inherited verbatim. ProdCoord Day 12 outline structural map applied at meta-level. No bespoke departures from canon.

---

*Day 29 ships clean. Day 30 build session targets SPEC body partial 1 (§6 + §7 + §10 + §14). 8-day trajectory to v1.0 LOCK on Day 37 mapped + calibrated against AI Video Gen 8-day build precedent (Day 20 → Day 27 LOCK candidate). Operator pickup: review §13 critical decisions list at next available block; ratify or amend the 6 PRELIMINARY items so Day 30 partial 1 has LOCK-quality input.*
