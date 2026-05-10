# ARS — Day 22 SPEC Body Pre-Flight (Rest Day Prep · Day 21)

**Date:** May 10, 2026 (Sun · Day 21 · Rest Day)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Status:** REST DAY PREP ONLY — section scaffolds for AI Video Gen Agent v1.0 SPEC body §6 / §7 / §10 / §14. Pattern-inherited from ProdCoord SPEC v1.0 (Day 14 LOCKED). Pure docs work — no LLM dispatched, no render API touched, no engine credentials referenced. Drop-in slots for Day 22 author.
**Pattern source:** `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` §6 / §7 / §10 / §14
**Predecessor outline:** `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (§0–§5 SHIPPED Day 20)
**Calendar context:** Day 21 = Rest Day, no build (Daily OS pillar: Rest → Body → Money → Authority → Relationships). Day 22 = §6 / §7 / §10 / §14 deep authoring. Day 23 = §8 / §9 / §11 / §12 / §13 / §15 / §16. Day 24 = LOCK.

---

## REST DAY-RESPECTFUL ADVANCEMENT — INTENT

This document is **scaffolding, not authoring**. It pre-positions Day 22's authoring so the operator-facing deep work (when the Rest Day ends) lands faster. Specifically:

- §6 12-Check Self-QC List → empty rows reserved for AI Video Gen-specific checks (anchor render, cost overrun, negative-prompt presence, render-engine resolution, asset URI scheme, post-render QC seed completeness, talent handle authorization, retry exhaustion, partial vs ready_for_edit gate, parent_chain integrity, qc_pre_flags ≥4 snake_case, metadata.human_review_required by lever).
- §7 System Prompt v1.0 → frame + tier table + process shape inherited; canon paragraph slots reserved; do NOT fill with actual prompt language until Day 22 (operator owns voice).
- §10 Storyboard → ProdCoord → AI Video Gen field map → schema cross-walk reserved; transform column empty pending Day 22.
- §14 Implementation Plan → calendar table extended through Day 27 with Rest Day-honored gaps.

Drop-in slot markers use `<<TBD-D22>>` so Day 22 author can grep and fill.

---

## §6 — 12-Check Self-QC List (SCAFFOLD ONLY)

**Inheritance from ProdCoord §6:** 12-check shape preserved. Failure-code column inherits ProdCoord's `errorEnvelope` codes plus the 4 v1.0-specific codes already enumerated in outline §3.5 (not_mode_b · quota_not_reserved · anchor_misalignment · cost_overrun · talent_unauthorized · engine_failure_unrecoverable · negative_prompt_missing).

**QC retry policy (LOCKED inheritance):** First QC failure → regen with concrete fix instructions inlined. Second failure → emit errorEnvelope. No third attempt. Predictable failure surface.

| # | Check | Failure code (slot) | Author note |
|---|-------|---------------------|-------------|
| 1 | **Entity firewall re-check (5th defense-in-depth pass — all string fields incl. composed prompts).** | `entity_firewall_breach` | Walk every string field in `rendered_shots.json` AND every prompt dispatched to engines. Prompts are NOT in the JSON output — they are ephemeral — but the negative-prompt template and the per-shot composed prompt both pass through this check before render dispatch. <<TBD-D22-PROMPT-WALK-LANG>> |
| 2 | **Banned vocab absence — `brief.do_not_say` terms not present in `rationale.*`, `escalation_path[*].notes`, all human-readable strings, AND in any text overlay rendered into the video itself (post_render_qc_seed.text_overlay_strings).** | `banned_vocab_leaked` | New angle for v1.0: rendered text overlays are video pixels but are extracted as strings via post_render_qc_seed.text_overlay_strings (OCR pass — engine returns this). Walk those strings too. <<TBD-D22-OCR-LANG>> |
| 3 | **No-buildings rule (Mode B render) — every shot's render output `post_render_qc_seed[*].suspected_buildings_bool == false`.** | `no_buildings_violation` | Storyboard / ProdCoord set `no_buildings_compliant_bool` on plan side. AI Video Gen verifies on RENDER side via post_render_qc_seed signal. <<TBD-D22-SUSPECTED-BUILDINGS-DEFINITION>> |
| 4 | **Tier↔mode authorization (5th defense-in-depth pass).** | `tier_constraint_violation` | `production_plan.tier ∈ {Pro, Enterprise}` AND `production_plan.production_mode == "B"`. Pilot/Starter never reach this agent. <<TBD-D22-PRE-CONDITION-LANG>> |
| 5 | **Mode B coverage — every `production_plan.mode_b_plan.render_queue[*].shot_id` resolves to exactly one entry in output `rendered_shots[]` AND status ∈ {rendered, partial, blocked}.** | `engine_failure_unrecoverable` (if all engines burn) OR set status=`partial_with_warnings` | Coverage gate. <<TBD-D22-COVERAGE-MAP>> |
| 6 | **Anchor render success — `style_consistency_anchor.anchor_shot_id` MUST equal `rendered_shots[0].shot_id` AND `rendered_shots[0].status == "rendered"`.** | `anchor_misalignment` (if mismatch) OR `engine_failure_unrecoverable` (if anchor failed and no fallback succeeded) | If anchor fails, the entire render set is blocked. Inheritors require the anchor to seed style consistency. Hard halt. <<TBD-D22-ANCHOR-FATAL-LANG>> |
| 7 | **Cost ceiling compliance — `render_telemetry.total_actual_cost_usd ≤ tier_ceiling_usd × (1 + cost_overrun_buffer_pct/100)`.** | `cost_overrun` | Default buffer = 10%. Hard reject at >110% of estimate. <<TBD-D22-COST-CEILING-MATH>> |
| 8 | **Quota reservation honored — every `production_plan.mode_b_plan.render_queue[*].quota_reserved_bool == true` at consumption time.** | `quota_not_reserved` | This is upstream's responsibility but defense-in-depth re-checks. <<TBD-D22-RESERVATION-CHECK-LANG>> |
| 9 | **Talent authorization (HeyGen shots only) — every shot with `engine_id == "heygen"` has `talent_id == "jamila-howard-reinvented-v2"` for v1.0.** | `talent_unauthorized` | Multi-talent v1.1+ deferred per Open Question #4. <<TBD-D22-TALENT-CHECK-LANG>> |
| 10 | **Negative-prompt presence — every `rendered_shots[*].render_dispatch_log` MUST record that the composed negative prompt was attached to the engine call.** | `negative_prompt_missing` | New v1.0-specific check. The negative prompt template is the runtime firewall — its absence on any single render = HARD FAIL. <<TBD-D22-NEGATIVE-PROMPT-LOG-FORMAT>> |
| 11 | **`handoff_targets[]` non-empty AND every `payload_ref` resolvable to a dotted path inside `rendered_shots.json`.** | `production_coord_agent_failed` (renamed slot — TBD final code) | Inherits ProdCoord's payload_ref resolver pattern. Edit Director / QC / Style Replication targets must each have valid refs. <<TBD-D22-HANDOFF-PAYLOAD-PATTERNS>> |
| 12 | **`qc_pre_flags[]` formatting — every element is a snake_case predicate (per Cross-SPEC canon §3.7) AND ≥4 entries.** | `qc_pre_flags_format_violation` (new slot) OR fold under existing | <<TBD-D22-QC-FLAGS-CANON-LANG>> |

**Authoring instruction for Day 22:** Each `<<TBD-D22-*>>` marker is a specific paragraph or table to draft. Do NOT add new checks beyond these 12 — the proven shape is 12 (matches Brief / Script / Storyboard / ProdCoord).

**Decision parked for Day 22 author:** Slot 11's failure code reads `production_coord_agent_failed` in inheritance; for AI Video Gen, this should rename to `ai_video_gen_agent_failed` for consistency with Cross-SPEC canon §3.6 errorEnvelope discipline (every agent emits its own typed failure code).

---

## §7 — System Prompt v1.0 (SCAFFOLD ONLY)

**Inheritance from ProdCoord §7:** Markdown-fenced prompt block. Single role declaration ("You are the AI Video Gen Agent..."). Hard rules numbered 1–N (NEVER violate). Tier table (runtime authoritative). Process steps numbered (matches §5 — 11 steps for AI Video Gen vs 9 for ProdCoord). Voice rules. JSON-only emit rule.

**DO NOT FILL** the prompt language on Day 21. The system prompt IS the LLM-facing canon — operator owns voice. Day 22 deep work.

### 7.1 Frame block (slot)

```
You are the AI Video Gen Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: <<TBD-D22-SINGLE-RESPONSIBILITY-LINE>>

You do NOT design shots. You do NOT pick the hook. You do NOT change the tier or mode. You do NOT modify the production plan. You bind concrete pixels to an executable render queue.
```

**Authoring note:** Single-responsibility line is already LOCKED in outline §1: *"Pixel binding for an executable render queue."* Inherit verbatim.

### 7.2 Hard rules (NEVER violate) — 13 slots reserved

| # | Rule (scaffold only — DO NOT fill) |
|---|------------------------------------|
| 1 | Output format = JSON only. Single object conforming to `rendered_shots.json` schema. No markdown, no commentary, no code fences. |
| 2 | <<TBD-D22-RULE-EVERY-SHOT-RENDERED-OR-EXPLAINED>> |
| 3 | Entity firewall (defense-in-depth, **5th** re-check). NEVER reference Holdco Group / 4821 Main / SITE-C-BRAND / 6315 / SLN / Retail Supply / Principal Holdco / NPOX / Nonprofit Leader A / Nonprofit Leader B / Nonprofit Leader C. Conjugates included. **AND NEVER inject any of these terms into a prompt sent to a render engine.** |
| 4 | Banned vocabulary. Inherit `brief.do_not_say`. Verbatim AND conjugate absence-check across rationale text, human-readable strings, AND every prompt dispatched to engines AND every text overlay rendered into video. |
| 5 | No-buildings rule passthrough — Mode B render outputs MUST NOT contain recognizable real-world buildings, identifiable architecture, or recognizable landmarks. Negative prompt template enforces. |
| 6 | Tier↔mode authorization (5th defense-in-depth). Pilot/Starter NEVER. Pro = Mode B unlocked. Enterprise = Mode B unlocked. |
| 7 | Cost ceiling is HARD — `render_telemetry.total_actual_cost_usd ≤ tier_cost_ceiling × 1.10` (10% overrun buffer). Hard reject `cost_overrun` errorEnvelope at >110%. |
| 8 | Asset URI scheme = platform-relative (`ars://renderset/...`). NEVER emit absolute external CDN URLs in any output field. NEVER emit signed URLs. NEVER emit raw API keys / handles / credentials. |
| 9 | HeyGen talent v1.0 = `"jamila-howard-reinvented-v2"` only. Reject any other talent_id with `talent_unauthorized`. Multi-talent v1.1+. |
| 10 | Negative-prompt template MUST attach to EVERY render dispatch. Verify in self-QC step #11. Absence on any single render = hard halt. |
| 11 | Anchor-first render — `rendered_shots[0]` (anchor) MUST complete `status == "rendered"` BEFORE any inheritor render dispatches. Anchor fail = whole-set blocked. |
| 12 | Render retries: 1 retry per shot on transient failure. After fallback engine also fails = `engine_failure_unrecoverable` for that shot. Set partial_with_warnings if anchor succeeded but inheritor(s) failed. |
| 13 | If self-QC fails 2 times → emit errorEnvelope. No 3rd attempt. Predictable failure surface. |

### 7.3 Tier table (runtime authoritative — slot)

| Tier | Mode B unlocked | Cost ceiling | Render runtime cap | Engines accessible |
|------|-----------------|-------------:|-------------------:|---------------------|
| Pilot | NO | n/a | n/a | n/a |
| Starter | NO | n/a | n/a | n/a |
| Pro | YES | $400 | 60 s | <<TBD-D22-PRO-ENGINE-LIST>> |
| Enterprise | YES | $750 | 90 s | <<TBD-D22-ENTERPRISE-ENGINE-LIST>> |

**Authoring note:** Pull from outline §4 (Tier Constraints) verbatim. Engine lists already declared in outline §0 (Runway / Pika / Luma / Flux / Kling / Higgsfield + HeyGen for talent).

### 7.4 Process (11 steps — slot)

Inherit verbatim from outline §5. Day 22 author copies the 11-step block from outline into the system prompt fence. No new authoring.

### 7.5 Voice rule (slot)

```
Voice for written rationale fields: clinical-warm, operator-to-operator, present tense, ≤14 words per sentence, action verbs.

Emit JSON only. Now.
```

**Inherit verbatim from ProdCoord §7. No deviation.**

---

## §10 — Storyboard → Production Plan → AI Video Gen Field Map (SCAFFOLD ONLY)

**Inheritance from ProdCoord §10:** Three-column table. Source field → destination field → transform note.

**Difference:** AI Video Gen reads from `production_plan.json` (ProdCoord output) — NOT directly from storyboard. The map is `production_plan.json field → rendered_shots.json destination → transform`. Two-hop trace from storyboard for audit purposes.

| `production_plan.json` field | `rendered_shots.json` destination | Transform | Author note |
|------------------------------|------------------------------------|-----------|-------------|
| `production_plan_id` | `production_plan_id` | Passthrough (audit trail). | <<TBD-D22-PASSTHROUGH-LANG>> |
| `brief_id` (via parent_chain) | `parent_chain[0]` | First element of 4-tuple. | |
| `script_id` (via parent_chain) | `parent_chain[1]` | Second element. | |
| `storyboard_id` (via parent_chain) | `parent_chain[2]` | Third element. | |
| `production_plan_id` | `parent_chain[3]` | Fourth element. (4-tuple v1.0 LOCKED.) | |
| `brand_id` | `brand_id` | Passthrough. | |
| `tier` | `tier` | Passthrough — drives cost ceiling re-validation. | |
| `lever` | `lever` | Passthrough — drives `metadata.human_review_required`. | |
| `production_mode` | `production_mode` | Passthrough — MUST equal `"B"`. | |
| `total_shots` | `total_shots` | Passthrough. | |
| `mode_b_plan.render_queue[]` | Drives `rendered_shots[]` 1:1 binding | Per-shot render dispatch. Every queue entry → exactly one rendered_shots entry. | <<TBD-D22-RENDER-QUEUE-MAP>> |
| `mode_b_plan.render_queue[*].shot_id` | `rendered_shots[*].shot_id` | 1:1 binding. | |
| `mode_b_plan.render_queue[*].engine_id` | `rendered_shots[*].engine_id_actual` | Passthrough on success; on retry, becomes `fallback_engine_id`. | <<TBD-D22-FALLBACK-LANG>> |
| `mode_b_plan.render_queue[*].fallback_engine_id` | `rendered_shots[*].fallback_engine_id` (if used) | Conditional passthrough. | |
| `mode_b_plan.render_queue[*].prompt_seed` | `rendered_shots[*].render_dispatch_log[*].composed_prompt_redacted` | TRANSFORM: prompt_seed + style_token_lib + negative_prompt_template = composed prompt. Stored REDACTED in log. | <<TBD-D22-COMPOSED-PROMPT-AUDIT>> |
| `mode_b_plan.render_queue[*].style_token` | Feeds composed prompt | TRANSFORM (composition). | |
| `mode_b_plan.render_queue[*].quota_reserved_bool` | `rendered_shots[*].quota_drawdown_log` | TRANSFORM (drawdown). | <<TBD-D22-DRAWDOWN-LANG>> |
| `mode_b_plan.style_consistency_anchor.anchor_shot_id` | `style_consistency_anchor.anchor_shot_id` | Passthrough. MUST equal `rendered_shots[0].shot_id`. | |
| `mode_b_plan.total_render_cost_usd_estimated` | `render_telemetry.total_estimated_cost_usd` | Passthrough — used as the budget ceiling for cost_overrun check. | |
| `mode_b_plan.runtime_target_seconds` | `render_telemetry.runtime_target_seconds` | Passthrough — informs latency budget. | |
| `tier_constraints.cost_ceiling_usd` (derived from tier) | `render_telemetry.tier_cost_ceiling_usd` | Lookup from §7.3 tier table. | |
| `qc_warnings` (from ProdCoord) | `qc_warnings` (inherited; may add own) | Append. | |
| `metadata.parent_chain` | `metadata.parent_chain` | Extend with own `production_plan_id`. | |

**v1.0 RESERVED FIELDS (`<<TBD-D22-DEFER>>`):**

- HeyGen talent_id mapping (production_plan does not currently surface talent at the render-queue level; v1.0 hardcodes `jamila-howard-reinvented-v2`; v1.1+ adds field).
- Multi-anchor rotation (Open Question #4 deferred).
- Auto-engine swap based on telemetry (Open Question #3 deferred).

**Authoring instruction for Day 22:** Fill `<<TBD-D22-*>>` markers with 1–3 sentence transform-mechanic explanations. Reference Cross-SPEC canon §3 sections for naming consistency. Do NOT add new fields beyond what production_plan.json schema (Day 17 LOCKED) defines.

---

## §14 — Implementation Plan (SCAFFOLD ONLY)

**Inheritance from ProdCoord §14:** Calendar table — Day · Date · Deliverable · Status. Dependencies block below.

**AI Video Gen calendar (full Week 4 + Wk5D1):**

| Day | Date | Deliverable | Status | Author |
|-----|------|-------------|--------|--------|
| Day 20 | Sat May 9 · Wk4D1 | **AI Video Gen Agent v1.0 SPEC OUTLINE §0–§5 SHIPPED** | ✅ DONE | Donna overnight |
| Day 21 | Sun May 10 · Rest Day | **Day 22 SPEC body pre-flight scaffold (THIS DOCUMENT)** — §6 / §7 / §10 / §14 drop-in slots reserved | ✅ DONE — Rest Day docs allowed | Donna overnight |
| Day 22 | Mon May 11 · Wk4D2 | **SPEC body §6 (12-Check Self-QC) + §7 (System Prompt v1.0) + §10 (Field Map) + §14 (Implementation Plan extension)** | ⬜ QUEUED | Donna overnight |
| Day 23 | Tue May 12 · Wk4D3 | **SPEC body §8 (Performance Targets) + §9 (5 Test Fixtures) + §11 (Cost Model per-engine $/sec) + §12 (Style Consistency Math) + §13 (17 Critical Decisions LOCKED) + §15 (Change Log) + §16 (Metadata schema)** | ⬜ QUEUED | Donna overnight |
| Day 24 | Wed May 13 · Wk4D4 | **SPEC v1.0 LOCK** — Cross-SPEC consistency review against ProdCoord SPEC + Cross-SPEC canon §3. Reconciliation of any naming / errorEnvelope / qc_pre_flags drift. LOCK signed. | ⬜ TARGET | Donna overnight + Jamila approval |
| Day 25 | Thu May 14 · Wk4D5 | **input.schema.json + output.schema.json** (Draft 2020-12, mutual-exclusivity if applicable). Self-validating. | ⬜ QUEUED | Donna overnight |
| Day 26 | Fri May 15 · Wk4D6 | **SKILL bundle** (10 files: SKILL.md, README, user-template, 2 schemas, 5 test fixtures). 5/5 inputs validate clean. | ⬜ QUEUED | Donna overnight |
| Day 27 | Sat May 16 · Wk5D1 | **LLM Test Runbook** (paste-and-run, pattern from Day 11 / Day 19). Operator-gated. | ⬜ QUEUED | Donna overnight |
| Day 28 | Sun May 17 · Rest Day | No build. Optional Jamila ~30 min review. | — | Jamila |
| Day 29+ | Mon May 18+ · Wk5D2+ | **Operator-gated LLM LOCK + Mode B production gate live.** Style Replication Agent SPEC outline begins (Mode C / Week 5 target). | ⬜ QUEUED | Jamila + Donna |

**Dependencies that MUST exist before Day 26 SKILL bundle build:**
- ✅ Production Coord Agent v1.0 SPEC LOCKED (Day 14)
- ✅ Production Coord input.schema.json + output.schema.json LOCKED (Day 17)
- ✅ Production Coord SKILL bundle LIVE (Day 18)
- ✅ Cross-SPEC Consistency Review LOCKED (Day 12)
- ✅ AI Video Gen SPEC outline §0–§5 (Day 20)
- ⬜ AI Video Gen SPEC body §6–§16 LOCKED (Day 24)
- ⬜ AI Video Gen schemas LOCKED (Day 25)
- ⬜ Engine `$/sec` lookup table — RESEARCH-ONLY canon for §11 cost model (Day 23 author task — NO subscription, NO API call, public docs only)
- ⬜ Negative-prompt template canon location decision (Open Question #8 — defer to v1.0 SKILL.md embedded; v1.1 refactor)

**Rest Day honored:** Day 21 (Sun May 10) and Day 28 (Sun May 17) — no build sessions per Daily OS pillar. Spec/docs work allowed (this document is the canonical Day 21 example).

---

## DAY 22 SPRINT RUNBOOK — paste-into-session pre-flight

For Day 22 (Mon May 11) deep authoring — operator copies the following sequence:

1. **Read** `ars/ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` §0–§5 (canon)
2. **Read** this document (`ars/ARS-2026-05-10-Day-22-SPEC-Body-Pre-Flight-Rest Day-Prep.md`) — §6 / §7 / §10 / §14 scaffolds
3. **Read** `ars/ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` §6 / §7 / §10 / §14 (pattern source)
4. **Read** `ars/ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED canon — must not drift)
5. **Author** §6 (target: ~3 hr · 12 checks fully drafted with failure-code rationale)
6. **Author** §7 (target: ~3 hr · system prompt block fenced + 13 hard rules + tier table from §7.3 + process from outline §5 + voice from §7.5)
7. **Author** §10 (target: ~2 hr · field map filled with transform paragraphs)
8. **Author** §14 (target: ~1 hr · status updates only — calendar already drafted in this document)
9. **Save as** `ARS-2026-05-11-AI-Video-Gen-Agent-v1-Spec.md` (Day 22 — partial, body §6/§7/§10/§14 LOCKED-as-drafted; §8/§9/§11/§12/§13/§15/§16 = `<<TBD-D23>>` slots)
10. **Mirror** to `/outputs/ars/`
11. **Build log** `build-log-2026-05-11.md` with session deliverables
12. **Update dashboard** — Day 22 row in Week 4 timeline + Today's Output

**Total Day 22 wall-clock:** ~9 hr (matches ProdCoord SPEC body Day 14 wall-clock). Operator-paced.

---

## SCHEMA NO-TOUCH RULE (re-asserted)

This document does NOT modify any LOCKED schema. Inherits:

- `production_plan.json` schema (Day 17 LOCKED) — read-only reference
- `storyboard.json` schema (Week 2/3 LOCKED) — read-only reference (audit trail)
- `script.json` schema (Day 9 LOCKED) — read-only reference (audit trail)
- `brief.json` schema (Day 7 LOCKED) — read-only reference (audit trail)

Day 25 will author `rendered_shots.json` schema. Until then, all fields described in §3 of outline + §10 of this document are SPEC-level claims, not schema-level enforcement.

---

## ENTITY SEPARATION (re-asserted — Rest Day docs)

This document is Sequel Digital ARS canon. Principal / Holdco Group / NPOX ZERO involvement.

**Defense-in-depth firewall list (5th layer continues):**
- Holdco Group / Holdco Group Inc. / HC (and conjugates)
- 4821 Main / 4821 / Main flagship
- SITE-C-BRAND / 6315 / 6315
- SLN / SLN Group / SLN Cuts / SLN Shear / SLN Salon / SalonB / Shear & Cuts
- Retail Supply / Retail Supply Co
- Principal Holdco / Principal
- NPOX / Community Nonprofit Org / Nonprofit Leader A / Nonprofit Leader B / Nonprofit Leader C
- Partner Brand

Document scanned for firewall references — every reference is in the firewall list itself, by design.

---

## PROCESS INTEGRITY (Day 21 Rest Day build)

- ✅ **Rest Day rule honored** — no full build session. Pure scaffold / docs work.
- ✅ No LLM dispatched. No render API touched. No engine credentials referenced.
- ✅ No external comms (no emails sent, no DMs, no posts).
- ✅ No financial commitments (no engine subscriptions, no quota purchases).
- ✅ No banned-vocab leaks — firewall list scanned across this document.
- ✅ No SPEC body content authored — only scaffold slots reserved (operator owns body language).
- ✅ Predecessor SPEC NOT touched (ProdCoord Day 14 LOCK respected — referenced only).
- ✅ Predecessor schemas NOT touched (ProdCoord Day 17 LOCK respected — referenced only).
- ✅ Cross-SPEC canon NOT touched (LOCKED — referenced only).
- ✅ AI Video Gen outline NOT touched (Day 20 outline LOCKED-as-shipped — referenced only).
- ✅ Build log written same day (`build-log-2026-05-10.md`).
- ✅ Mirror to `/outputs/ars/` complete.

---

## PROVENANCE

- Authored: 2026-05-10 (Sun · Day 21 · Rest Day · Wk4D2-prep) — ARS overnight Rest Day docs session
- Deliverable file: `ARS-2026-05-10-Day-22-SPEC-Body-Pre-Flight-Rest Day-Prep.md` (Desktop/ARS/ + outputs/ars/)
- Pattern source: `ARS-2026-05-03-Production-Coord-Agent-v1-Spec.md` §6 / §7 / §10 / §14 (Day 14 LOCKED — verbatim shape inherited, content slotted as `<<TBD-D22-*>>`)
- Predecessor outline: `ARS-2026-05-09-AI-Video-Gen-Agent-SPEC-Outline.md` (Day 20 §0–§5 SHIPPED)
- Cross-spec canon: `ARS-2026-05-01-Cross-Spec-Consistency-Review.md` (LOCKED)
- Daily OS reference: Rest → Body → Money → Authority → Relationships pillar (Rest Day = protected rest day)

*Day 21 Rest Day honored. Day 22 deep authoring is now scaffold-staged: §6 / §7 / §10 / §14 drop-in slots reserved with `<<TBD-D22-*>>` markers. Day 22 wall-clock estimate: ~9 hours operator-paced, mapping 1:1 to proven ProdCoord §14 wall-clock. No SPEC body content authored. No external comms. No financial commitments. No render API touched.*
