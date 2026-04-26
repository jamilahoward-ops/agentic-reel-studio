# ARS — Brief Agent v1.0 SPEC

**Date:** April 26, 2026 (Sunday — Day 7 · Rest Day build session = SPEC ONLY, no code)
**Owner:** Jamila Howard (Sequel Digital — ARS productized build)
**Build phase:** Week 2 pre-stage. Monday Apr 27 = build against this spec.
**Status:** v1.0 LOCKED for Monday execution. Implementation = fill-in-the-blanks.

---

## §1. Purpose & Position in Pipeline

The **Brief Agent** is the second agent in the ARS pre-production stage and the **first content-generating agent** in the pipeline. It converts a topic + brand context into a structured, executable creative brief that downstream agents (Script, Storyboard, Production Coord) can act on without further human interpretation.

**Pipeline position (per Orchestration Blueprint §5):**
```
Trend Hunter → Strategy → BRIEF AGENT → Script → Storyboard → Production Coord → ...
```

**Why the Brief Agent matters:** Every downstream failure in ARS traces back to a weak brief. If the brief is wrong, the script is wrong, the storyboard is wrong, the reel is wrong. The Brief Agent is the **integrity gate** for the entire production line — it is where ARS spends the most prompt-engineering budget.

**Hand-off contract enforced:** The Brief Agent's output is the canonical `brief.json` per Orchestration Blueprint §5.3 schema. No improvisation downstream.

---

## §2. Inputs (Full Schema)

The Brief Agent consumes **three required inputs** and **two optional inputs**.

### 2.1 Required inputs

| Field | Source | Type | Required |
|-------|--------|------|----------|
| `brand_voice_intake` | Brand Voice Intake JSON (per `ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md`) | object | YES |
| `topic_signal` | Trend Hunter or manual seed (string + reason) | object | YES |
| `tier_context` | Pricing tier of the client (Pilot / Starter / Pro / Enterprise) | enum | YES |

### 2.2 Optional inputs

| Field | Source | Type | Required |
|-------|--------|------|----------|
| `prior_briefs` | Last 5 briefs for this brand (memory loop) | array | NO |
| `manual_override` | Jamila or operator forcing a specific angle | string | NO |

### 2.3 Input JSON schema (canonical)

```json
{
  "brand_id": "REINVENTED",
  "brand_voice_intake": { /* full Brand Voice Intake object */ },
  "topic_signal": {
    "topic": "Why operators burn out at 7-figure revenue",
    "reason": "Trend Hunter flagged 4 viral posts in last 48h on operator burnout; community DM volume up 31% week-over-week",
    "source": "trend_hunter | manual",
    "confidence": 0.78,
    "competing_angles": [
      "boundary work as productivity",
      "delegation as self-respect",
      "the cost of being needed"
    ]
  },
  "tier_context": "Pilot",
  "prior_briefs": [ /* up to 5 most recent brief.json objects, oldest first */ ],
  "manual_override": null,
  "lever_state": 3,
  "session_id": "ars-2026-04-27-001"
}
```

### 2.4 Input validation rules

- `brand_voice_intake` must include all 11 required sections (entity firewall, voice attributes, do-say/don't-say lists, etc.). If any section missing → REJECT input, return error to orchestrator.
- `topic_signal.confidence` < 0.5 → flag for human review BEFORE running brief.
- `tier_context` must be one of `["Pilot", "Starter", "Pro", "Enterprise"]`. Else REJECT.
- `prior_briefs` length capped at 5. If > 5, take most recent 5.
- All inputs sanitized for prompt injection markers (`<|im_start|>`, jailbreak phrases, HC/Principal/NPOX cross-entity leaks per firewall).

---

## §3. Outputs (Full Schema — `brief.json`)

The Brief Agent produces a **single canonical output**: a JSON object that conforms to Orchestration Blueprint §5.3.

### 3.1 Output JSON schema

```json
{
  "brief_id": "brief-REINVENTED-2026-04-27-001",
  "brand_id": "REINVENTED",
  "tier": "Pilot",
  "lever": 3,
  "production_mode": "A",
  "created_at": "2026-04-27T16:00:00Z",
  "session_id": "ars-2026-04-27-001",
  "title_working": "The 7-Figure Burnout Trap",
  "hook": {
    "first_3_seconds": "You hit seven figures and now you can't sleep. That's not success — that's a warning sign.",
    "alt_hooks": [
      "Seven figures, six hours of sleep, five red flags you ignored.",
      "If your business needs you 24/7 to survive, you don't own a business — you own a job."
    ],
    "delivery": "direct-to-camera | voiceover-over-broll",
    "tone": "honest-without-pity"
  },
  "core_promise": "By second 30, viewer understands why scaling without systems creates a trap, not freedom.",
  "audience": {
    "primary": "Female operators, 35–50, $500K–$5M revenue, founder-dependent business",
    "psychographic_pain": "Exhausted, identity-fused-with-business, secretly resents own success",
    "language_register": "operator-to-operator (peer, not guru)"
  },
  "structure": {
    "format": "monologue | listicle | story | data-reveal | duet-style",
    "selected": "story",
    "beats": [
      { "second": "0–3", "beat": "Hook — 7-figure burnout reframe", "purpose": "stop scroll" },
      { "second": "3–10", "beat": "Personal proof point — 'I was there'", "purpose": "credibility" },
      { "second": "10–25", "beat": "The 3-trap reveal — needed-ness, no-systems, identity-fusion", "purpose": "value delivery" },
      { "second": "25–35", "beat": "The reframe — burnout = system failure, not personal failure", "purpose": "shift" },
      { "second": "35–45", "beat": "Specific tactic — first 30 min of the day rule", "purpose": "actionable" },
      { "second": "45–55", "beat": "Tagline / signature line", "purpose": "memorable close" }
    ],
    "duration_target_seconds": 55,
    "duration_min": 45,
    "duration_max": 75
  },
  "messaging_pillars_used": ["operator-truth-telling", "systems-over-effort", "identity-vs-business-separation"],
  "do_say": [
    "operator", "system", "you built this", "trap", "reframe"
  ],
  "do_not_say": [
    "girlboss", "hustle", "grind", "boss babe", "millionaire mindset", "8-figure", "luxury", "elevate"
  ],
  "visual_direction": {
    "setting": "neutral interior, soft window light, no clutter — operator-credible",
    "wardrobe": "REINVENTED visual canon — earth tones, structured silhouette, no pattern noise",
    "color_palette": ["#1a1033", "#d4b996", "#ffffff"],
    "shot_list_hint": [
      "Medium wide, hands visible, 5–7 sec — for credibility opener",
      "Tight medium for reframe beat — 3–4 sec",
      "Cutaway B-roll of journal/coffee/laptop for tactic — 2 sec each x 3"
    ],
    "no_buildings_rule": "Per CLAUDE.md HC Visual Brand Rule — no AI-generated buildings. REINVENTED brand has its own ban: no aspirational lifestyle stock."
  },
  "audio_direction": {
    "voice": "REINVENTED operator-direct register",
    "music_mood": "low-tempo, minor-key cello pad, NO trending TikTok beats for this tier",
    "sfx_use": "minimal — 1 transition swoosh max",
    "captions": "REINVENTED brand kit captions: brand purple #6a3093, white text, bottom-third"
  },
  "cta": {
    "type": "soft | hard | none",
    "selected": "soft",
    "copy": "If this hit — the REINVENTED waitlist is open. Link in bio.",
    "placement": "voiceover at 50–55s + on-screen end card"
  },
  "platform_targets": [
    { "platform": "Instagram Reels", "aspect": "9:16", "first_frame_text": "7-FIGURE BURNOUT" },
    { "platform": "TikTok", "aspect": "9:16", "first_frame_text": "7-FIGURE BURNOUT" },
    { "platform": "LinkedIn", "aspect": "9:16 (cropped to 1:1)", "first_frame_text": "Read what 7-figure operators won't say" }
  ],
  "qc_pre_flags": [
    "Verify no HC / Principal / NPOX / 4821 / 6315 reference",
    "Verify no banned hustle-culture vocabulary",
    "Verify operator register, not guru register"
  ],
  "rationale": {
    "why_this_topic": "Trend Hunter signal + brand pain alignment + waitlist is open",
    "why_this_format": "Story format outperforms monologue 2.4x for REINVENTED's audience per prior_briefs analytics",
    "why_this_hook": "Reframe-style hook beats listicle hook in the 35–50 demo per A/B data from REINVENTED Q1 reels"
  },
  "downstream_dependencies": {
    "script_agent": "consume this brief.json directly — produce 55-second script",
    "storyboard_agent": "use shot_list_hint + duration beats to draft 6-shot storyboard",
    "production_coord_agent": "use visual_direction + audio_direction + platform_targets to assemble shoot list (Mode A) or AI-gen prompt (Mode B)"
  },
  "metadata": {
    "agent_version": "brief-agent-v1.0",
    "model_used": "claude-opus-4-6",
    "prompt_template_id": "brief-agent-v1.0-prompt",
    "tokens_in": 0,
    "tokens_out": 0,
    "latency_ms": 0,
    "qc_score_predicted": 0.0,
    "human_review_required": true
  }
}
```

### 3.2 Output validation (before handoff to Script Agent)

The orchestrator runs THIS brief through 8 hard checks. ANY failure = re-run brief.

1. ✅ All required schema fields present
2. ✅ `do_not_say` list contains the 8 banned hustle terms (verbatim from Brand Voice Intake §6.2)
3. ✅ No HC / Principal / NPOX references anywhere in object (entity firewall)
4. ✅ `duration_target_seconds` between `duration_min` and `duration_max`
5. ✅ Beats sum to ≥95% of duration target (no silent gaps)
6. ✅ At least 2 alt_hooks present (script can A/B)
7. ✅ Visual direction includes "no_buildings_rule" acknowledgment
8. ✅ At least 3 messaging_pillars_used selected from Brand Voice Intake §3 canon

---

## §4. Decision Logic / Process Steps

The Brief Agent runs **9 sequential steps** internally. No skipping.

### Step 1 — Validate inputs
- Confirm all required fields present
- Confirm Brand Voice Intake has 11 sections
- Confirm tier_context is valid enum
- If invalid → HALT, return `{ "error": "input_validation_failed", "reason": "..." }`

### Step 2 — Load brand context
- Parse Brand Voice Intake JSON
- Extract: voice attributes, do-say/don't-say lists, audience definitions, messaging pillars, entity firewall list
- Build internal `brand_context` working object

### Step 3 — Analyze topic signal
- Score topic against brand pillars (0–1 confidence each pillar)
- Identify which 2–3 pillars THIS topic activates
- If topic activates 0 pillars → flag `topic_drift_warning: true` (still produces brief, but rationale logs concern)

### Step 4 — Tier-aware constraint loading
- Pilot tier → 8 reels/mo, Mode A only, 55-sec target, 1 brand context
- Starter tier → same as Pilot
- Pro tier → 16 reels/mo, Mode A+B, 45–90 sec range, 1 brand
- Enterprise tier → 30 reels/mo, A+B+C, full duration range, up to 3 brands
- Apply duration + format flexibility per tier

### Step 5 — Format selection
- Choose ONE of: monologue, listicle, story, data-reveal, duet-style
- Decision rules:
  - If topic = pain/identity → story (default for REINVENTED)
  - If topic = how-to / tactical → listicle
  - If topic = data/trend → data-reveal
  - If topic = response to public take → duet-style
  - If topic = thought leadership → monologue
- If `prior_briefs` exists, weight against last 5 formats to avoid repetition (cap any single format at 3 of last 5)

### Step 6 — Hook generation
- Generate 1 primary + 2 alternates
- Each hook follows REINVENTED hook framework: reframe / contrarian / personal-proof
- Hook validation: must be ≤ 15 words, must contain at least one banned-by-default-but-allowed-here trigger word OR a number, must not start with "Are you" or "Have you ever"

### Step 7 — Beat structure
- Build beats array per duration target
- Each beat must declare: second range, beat description, purpose
- Total beats: 5–7 (sweet spot per REINVENTED data)
- First beat ALWAYS = hook (0–3 sec)
- Last beat ALWAYS = signature/CTA close

### Step 8 — Visual + Audio direction
- Pull visual canon from Brand Voice Intake §8
- Apply tier production mode (A/B/C) constraints
- Enforce `no_buildings_rule` (per CLAUDE.md and REINVENTED brand canon)
- Specify shot list hints (not exhaustive — Storyboard Agent fills in)

### Step 9 — Self-QC + emit
- Run output through 8-check validation list (§3.2)
- If 1+ checks fail → re-attempt up to 2x with adjusted prompt, then escalate
- If all pass → emit `brief.json` with `human_review_required: true` (Lever 3 default)
- Log to memory loop for future `prior_briefs` reference

---

## §5. Prompt Template (LLM-Ready)

The Brief Agent is a Claude skill. The user-facing message is the input JSON; the system prompt is the canon below.

### 5.1 System prompt (v1.0 — LOCKED)

```
You are the Brief Agent for Agentic Reel Studio (ARS), a productized service under Sequel Digital that produces high-output short-form video content for elite operators.

Your single job: convert a topic + brand context into a structured creative brief that downstream agents (Script, Storyboard, Production Coord) can execute without further human interpretation.

## Hard rules (NEVER violate)

1. **Output format = JSON only.** No markdown, no commentary, no explanation. Single JSON object conforming to schema.
2. **Entity firewall.** This brief is for the brand specified in `brand_id`. NEVER reference Holdco Group (HC), 4821 Main, SITE-C-BRAND, SLN, Retail Supply, Principal Holdco, NPOX, or Nonprofit Leader A in ANY field. If the topic signal accidentally drifts toward these, REJECT the topic and return `{"error": "entity_firewall_breach", "topic": "..."}`.
3. **Banned vocabulary.** Honor the `do_not_say` list from Brand Voice Intake. NEVER use those terms verbatim or as conjugates.
4. **No buildings rule.** If visual direction implies a location, specify "interior, neutral" or "shot in REINVENTED home studio." NEVER specify aspirational external buildings.
5. **Duration discipline.** `duration_target_seconds` must be inside `duration_min`–`duration_max`. Beats must sum to ≥95% of target.
6. **Tier honoring.** A Pilot tier brief CANNOT specify Mode B/C. A Starter brief CANNOT specify Mode B/C. Mode A only for those tiers.
7. **Memory respect.** If `prior_briefs` provided, do not repeat the same format more than 3 of the last 5 briefs. Diversify.
8. **Self-QC before emit.** Run the 8-check list internally. If anything fails, regenerate that section once. If still failing, emit with `human_review_required: true` and add a `qc_warnings` field flagging the issue.

## Process (run in order)

1. Validate inputs.
2. Load brand context.
3. Analyze topic signal vs brand pillars.
4. Apply tier constraints.
5. Select format.
6. Generate hook (1 primary + 2 alt).
7. Build beats.
8. Direct visual + audio.
9. Self-QC + emit JSON.

## Voice for the brief itself (meta)

Write the brief in operator voice — clinical, direct, no fluff. The brief is read by other agents AND by Jamila. She wants to scan it in 90 seconds and trust it.

Output the canonical brief.json. Nothing else.
```

### 5.2 User prompt template

```
INPUT:
{input_json}

Generate the brief.json per system prompt rules. Output JSON only.
```

### 5.3 Stop conditions

- Output exceeds 5KB → regenerate, condense
- Output is not valid JSON → regenerate up to 2x, then HALT
- Output contains `<|` or `</im_` markers → reject as prompt injection, regenerate fresh
- Output references banned entity → entity firewall breach, HALT and log

---

## §6. Failure Modes / Guardrails

### 6.1 Identified failure modes (10)

| # | Failure | Likelihood | Mitigation |
|---|---------|------------|------------|
| 1 | LLM produces non-JSON output | Medium | Regenerate with explicit "JSON ONLY" reminder |
| 2 | Output references HC / Principal / NPOX | Low (firewall) | Hard reject + log; do not pass to Script Agent |
| 3 | Output uses banned hustle vocabulary | Medium | Output check vs do_not_say list; regenerate if found |
| 4 | Format repeats last 3 briefs | Medium | prior_briefs analysis in Step 5 |
| 5 | Duration math doesn't add up | Low | §3.2 check 5 + 4 |
| 6 | Topic drift from brand pillars | Medium | topic_drift_warning flag, human review |
| 7 | Hook is too long (>15 words) | Low | Step 6 validation |
| 8 | Hook starts with "Are you / Have you ever" (banned opener) | Medium | Step 6 validation |
| 9 | Brief calls Mode B/C on Pilot/Starter tier | Low | Step 4 tier constraint check |
| 10 | Visual direction implies aspirational building | Low | no_buildings_rule explicit + check |

### 6.2 Escalation path

- 1 failure on first attempt → silent regeneration
- 2 failures on retry → emit with `human_review_required: true` + `qc_warnings` array
- 3+ failures → HALT, return `{"error": "brief_agent_failed", "attempts": 3, "last_warnings": [...]}` to orchestrator
- Orchestrator surfaces error to Jamila (or operator) for manual brief authoring

### 6.3 Lever 3 default behavior

At Lever 3 (start state — first 30 reels), `human_review_required` is ALWAYS `true` regardless of QC pass. Jamila approves every brief before Script Agent runs.

At Lever 2 (after 30 reels, sampled approval), `human_review_required` is `true` for 1-in-5 briefs (random) plus all briefs with any QC warning.

At Lever 1 (after 90 reels, full autonomy), `human_review_required` is only `true` if QC warnings present OR `topic_drift_warning: true`.

---

## §7. Test Cases (5 sample inputs + expected outputs)

### Test Case 1 — REINVENTED · Pilot · Story format

**Input:**
- brand_id: REINVENTED
- topic_signal.topic: "Why operators burn out at 7-figure revenue"
- topic_signal.confidence: 0.78
- tier_context: Pilot
- prior_briefs: empty

**Expected output highlights:**
- format: "story"
- duration_target_seconds: 55
- production_mode: "A"
- messaging_pillars_used: includes "operator-truth-telling"
- do_not_say includes "girlboss", "hustle", "grind"
- human_review_required: true (Lever 3)

### Test Case 2 — REINVENTED · Starter · Listicle format

**Input:**
- brand_id: REINVENTED
- topic_signal.topic: "5 systems every $1M operator should automate"
- topic_signal.confidence: 0.85
- tier_context: Starter
- prior_briefs: 3 prior story-formats (forces format diversification)

**Expected:**
- format: "listicle" (because 3/5 prior were story → listicle wins)
- structure.beats: 7 beats (intro + 5 list items + close)
- duration_target_seconds: 60–70

### Test Case 3 — Entity firewall breach test

**Input:**
- brand_id: REINVENTED
- topic_signal.topic: "How Holdco Group is changing barbershops" (bait)

**Expected:**
- ERROR: `{"error": "entity_firewall_breach", "topic": "Holdco Group is OFF-LIMITS for REINVENTED brand"}`
- HALT before any generation

### Test Case 4 — Tier mismatch / Mode B on Pilot

**Input:**
- brand_id: REINVENTED
- topic_signal.topic: "AI-generated reel of operator's daily routine"
- topic_signal.competing_angles: ["fully AI animated"]
- tier_context: Pilot

**Expected:**
- production_mode: "A" (forced by tier constraint)
- rationale.why_this_format: notes that AI-generated angle was rejected because Pilot tier locks Mode A only
- Suggests alternative live-action treatment of same topic

### Test Case 5 — Low-confidence topic

**Input:**
- brand_id: REINVENTED
- topic_signal.topic: "Random meme template trending on TikTok"
- topic_signal.confidence: 0.34
- tier_context: Starter

**Expected:**
- topic_drift_warning: true
- human_review_required: true (regardless of Lever)
- qc_warnings: ["topic_signal.confidence below 0.5 threshold — consider rejecting topic and re-running Trend Hunter"]
- Brief still generated (operator can override warning)

---

## §8. Performance Targets

### 8.1 v1.0 targets (Week 2 build)

| Metric | Target | Hard Floor |
|--------|--------|------------|
| Latency (avg) | <90s | <300s |
| Token cost (input + output, Opus 4.6) | <$0.30/brief | <$0.80/brief |
| Schema validity rate | 100% | 95% |
| Entity firewall catch rate | 100% | 100% (zero tolerance) |
| Banned vocab catch rate | 100% | 99% |
| Lever 3 approval rate (Jamila accepts as-is) | >70% | >50% |
| Format diversity (no format >60% of last 10 briefs) | Yes | Yes |

### 8.2 v1.1 targets (after first 30 reels — Week 4–5)

| Metric | Target |
|--------|--------|
| Lever 3 approval rate | >85% |
| Latency (avg) | <60s |
| Token cost | <$0.20/brief |
| Brief → final reel "no rework needed" rate | >80% |

### 8.3 Tracking / instrumentation

Every brief emission logs:
- `tokens_in`, `tokens_out`, `latency_ms`
- `qc_score_predicted` (self-rated confidence 0–1)
- `human_decision` (approved as-is | minor edit | major edit | rejected) — captured post-Jamila review
- All four metrics feed the Margin Watchdog (Week 5 build) and the v1.1 prompt-engineering iteration.

---

## §9. Implementation Notes (Monday Build Plan)

### 9.1 Format = Claude skill

Build as a Claude skill with this structure:

```
/Sequel Digital/ARS/skills/brief-agent/
  SKILL.md           ← system prompt + process rules + io schema
  prompts/
    user-template.txt  ← user message template
  schemas/
    input.schema.json   ← input validation (jsonschema)
    output.schema.json  ← output validation (jsonschema)
  test-cases/
    case-01-reinvented-pilot-story.json
    case-02-reinvented-starter-listicle.json
    case-03-entity-firewall-breach.json
    case-04-tier-mismatch-mode-b-pilot.json
    case-05-low-confidence-topic.json
  README.md          ← human-readable brief: how to invoke + expected behavior
```

### 9.2 Monday Apr 27 build sequence (estimated 4 hours)

1. **Hour 1** — Stand up skill folder structure. Drop SKILL.md from §5.1 of this spec.
2. **Hour 2** — Build input + output JSON schemas (jsonschema format). Validate with sample REINVENTED Brand Voice Intake.
3. **Hour 3** — Run test cases 1–5. Log outputs. Compare against expected.
4. **Hour 4** — Iterate prompt for any test case failures. Lock v1.0 if all 5 pass.

### 9.3 Dependencies that must exist BEFORE build

- ✅ Brand Voice Intake JSON for REINVENTED (`ARS-2026-04-23-Brand-Voice-Intake-REINVENTED.md`) — DONE
- ✅ Orchestration Blueprint with §5 schema canon (`ARS-2026-04-24-Agent-Orchestration-Blueprint.md`) — DONE
- ✅ Pricing Model with tier rules (`ARS-2026-04-25-Service-Tier-Pricing-Model.md`) — DONE
- ✅ This spec — DONE (4/26)
- ⬜ Trend Hunter agent — NOT YET BUILT (Week 3 target)
- ⬜ Strategy agent — NOT YET BUILT (Week 3)

**Critical dependency note:** Brief Agent v1.0 can be tested WITHOUT Trend Hunter live by feeding manual topic_signal objects (per test cases). This is the correct Week 2 sequence — build Brief Agent against mock inputs, then wire to Trend Hunter in Week 3.

### 9.4 Storage / outputs

All briefs emitted by the agent get saved to:
```
/Sequel Digital/ARS/briefs/{brand_id}/{brief_id}.json
```

Plus a copy logged to Notion ARS Hub database (when Notion ARS database exists — part of Week 3 build).

---

## §10. v1.0 → v2.0 Evolution Path

### v1.0 (Week 2 build) — what's locked
- Single-brand briefs (REINVENTED only)
- 5 format options
- 9-step process
- 8-point QC
- Manual topic feed acceptable (Trend Hunter optional)

### v1.1 (Week 3–4) — additions
- Multi-brand brief (Brief Agent receives `brand_id` and loads correct Brand Voice Intake)
- Live Trend Hunter integration
- Prior_briefs memory wired (last 5 actual briefs in DB)
- Latency optimization (token reduction in prompt)

### v1.2 (Week 5) — additions
- Margin Watchdog instrumentation
- A/B testing of hooks (Brief Agent emits 2 candidate briefs at Pro+ tier; Script Agent picks winner based on prior data)
- Lever 2 sampling automation

### v2.0 (post-launch, ~Week 8–10) — additions
- Cross-brand learning (what works for REINVENTED informs Sequel Digital client briefs WITHOUT entity bleed)
- Predictive QC scoring (model self-rates brief and Jamila's likely approval before emit)
- Cost-to-deliver auto-tuning (Margin Watchdog tells Brief Agent which formats are cheap to produce)

---

## §11. Integration with Brand Voice Intake + Orchestration Blueprint

### 11.1 Brand Voice Intake → Brief Agent

The Brief Agent **reads** these sections from Brand Voice Intake:
- §1 brand_id
- §2 voice_attributes (tone, register, energy)
- §3 messaging_pillars (top 5)
- §4 audience_definition (primary + psychographic)
- §5 do_say / hook_seeds
- §6 do_not_say (banned vocabulary)
- §7 entity_firewall (off-limits cross-references)
- §8 visual_canon
- §9 audio_canon
- §10 cta_library
- §11 platform_targets

Every section is **required** input. Missing section → reject input.

### 11.2 Brief Agent → Script Agent (handoff)

Per Orchestration Blueprint §5.4, the handoff contract is:
- Script Agent receives: full `brief.json`
- Script Agent does NOT consume Brand Voice Intake directly (Brief Agent is the abstraction layer)
- Script Agent produces `script.json` per §5.4 schema
- If Script Agent encounters fields it doesn't understand → returns `{"error": "brief_schema_mismatch", "field": "..."}` to orchestrator → orchestrator re-runs Brief Agent

### 11.3 Brief Agent ↔ Storyboard Agent

Storyboard Agent reads `brief.json.visual_direction` + `brief.json.structure.beats` to build 6-shot storyboard. Brief Agent's `shot_list_hint` is advisory only — Storyboard Agent has authority to expand.

### 11.4 Brief Agent ↔ QC Agent (Week 4 integration)

When QC Agent goes live (Week 4), final-reel QC outputs feed back to Brief Agent's memory loop. If a brief consistently produces reels that fail QC, the Brief Agent's prompt is flagged for revision in next prompt-engineering pass.

---

## §12. Acceptance Criteria

This spec is "build-ready" if and only if:

- [x] Schema for `brief.json` is fully specified (§3.1)
- [x] Input schema is fully specified (§2.3)
- [x] System prompt is locked, no TODOs (§5.1)
- [x] All 9 process steps documented (§4)
- [x] All 10 failure modes catalogued + mitigated (§6.1)
- [x] At least 5 test cases written with inputs + expected outputs (§7)
- [x] v1.0 performance targets defined (§8.1)
- [x] Implementation file structure mapped (§9.1)
- [x] Build time estimate provided (§9.2)
- [x] v1.0 → v2.0 evolution path mapped (§10)
- [x] Upstream/downstream integration documented (§11)

**ALL 11 criteria met. Spec is LOCKED for Monday build.**

---

## §13. Rest Day note (transparency)

This spec was authored on Sunday Apr 26 — Day 7. Per Daily OS Rest Day rule, no code/skill build was executed. Spec drafting is documentation work, not build work — Rest Day-compatible per Future Jamila 2033 framework. Monday Apr 27 = first build session executes against this spec.

---

*ARS Brief Agent v1.0 SPEC*
*Author: Sequel Digital ARS overnight build session*
*Locked: April 26, 2026 (Sunday)*
*Next action: Monday Apr 27 — execute §9.2 build sequence*
*Spec lives at: `ars/ARS-2026-04-26-Brief-Agent-v1-Spec.md`*
*Mirror: `/outputs/ars/ARS-2026-04-26-Brief-Agent-v1-Spec.md`*
