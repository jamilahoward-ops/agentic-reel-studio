# AI Video Gen Agent — Negative Prompt Template Canon (v1.0)

**Source:** SPEC §6.5 firewall (10 entries) + §7 Hard Rule #5 no-buildings string + §7 Hard Rule #4 banned vocab pattern + §6 brand-anti-patterns
**Status:** v1.0 LOCKED — embedded in SKILL.md Hard Rule #10
**Composition step:** §7 Process Step 4 (compose once at session start, reuse across every render dispatch)
**Verification:** Hard Rule #10 + Self-QC Check #10 + schema-layer `negative_prompt_attached_bool: const true` (Day 25 LOCKED)

---

## Composition rule (Process Step 4 — verbatim)

Concatenate (in this order):
1. **Entity firewall** — 10 canonical entries from §6.5
2. **`brief.do_not_say`** — verbatim + first-order conjugates
3. **Brand-anti-patterns** — off-brand color palettes for REINVENTED v1.0 + off-tone visual descriptors
4. **No-buildings string** — verbatim from Hard Rule #5

ASSERT composed length `> 100` chars. Compute SHA-256 hash → `negative_prompt_sha256`. Bind once, reuse for every shot in Steps 5 + 6.

---

## Canonical template (v1.0 base — `do_not_say` token slot reserved)

```
<<<NEGATIVE PROMPT — NEVER RENDER THESE — ALWAYS EXCLUDE>>>

[ENTITY FIREWALL — 10 canonical entries · token-boundary case-insensitive]
holdco group, holdco group inc, hc,
4821 main, 4821, main flagship,
site-c-brand, 6315, 6315, 6315,
sln, sln group, sln cuts, sln shear, sln salon, overflow, shear & cuts,
retail supply, retail supply co,
principal holdco, principal,
npox, community nonprofit org,
nonprofit leader a, nonprofit leader b, nonprofit leader c,
partner brand,
holdcogroup.com

[BRIEF.DO_NOT_SAY — runtime injection per session]
{{ brief_do_not_say_csv }}
{{ brief_do_not_say_first_order_conjugates_csv }}

[BRAND-ANTI-PATTERNS — REINVENTED v1.0 off-brand visual canon]
muted earth tones, sterile corporate blue, pastel,
beige, taupe, cream, mauve,
cluttered, amateur, smartphone-shot, low-resolution,
shaky handheld, fluorescent overhead lighting,
generic stock-photo aesthetic, fisheye distortion,
oversaturated neon, over-processed HDR,
text watermark, vendor logo overlay, signature mark,
random subtitles, machine-translated captions, kawaii style

[NO-BUILDINGS STRING — Hard Rule #5 verbatim]
real-world buildings, identifiable architecture, recognizable landmarks, named skylines, registered structures

[NO-CREDENTIAL EXPOSURE — Hard Rule #8 reinforcement]
api keys, signed urls, presigned urls, raw credentials,
opaque handle ids visible in frame, terminal output, console logs

<<<END NEGATIVE PROMPT>>>
```

---

## Composition notes

- **Token order matters for some engines.** Runway / Pika / Luma honor list-order weights softly; HeyGen is largely indifferent to ordering. Composing in canonical order across the agent ensures byte-identical SHA-256 hashes for the same `brief.do_not_say` set.
- **Conjugation rule for `brief.do_not_say`:** verbatim + first-order conjugates (pluralization, gerund, past tense). Example: `do_not_say = ["cheap"]` → expand to `["cheap", "cheaper", "cheaply", "cheapest", "cheapened"]`. The conjugation is applied at composition time, not at engine dispatch time.
- **Empty `do_not_say` is allowed.** If `brief.do_not_say == []`, the `{{ brief_do_not_say_csv }}` slot collapses to nothing and the template still satisfies `length > 100 chars` from the firewall + brand-anti-pattern blocks alone.
- **Brand-anti-patterns are REINVENTED v1.0 hardcoded.** Multi-brand v1.1+ adds `{{ brand_anti_patterns_csv }}` runtime injection per `brief.brand_id`.

---

## SHA-256 verification rule

Every `rendered_shots[*].render_dispatch_log[*]` MUST carry:
- `negative_prompt_attached_bool: true` (schema enforces `const: true` — Day 25 LOCKED)
- `negative_prompt_sha256: "<64-hex>"` — SHA-256 hex digest of the **composed final string** (after `{{ brief_do_not_say_csv }}` substitution)

Self-QC Check #10 walks every dispatch log record. Any record missing either field, OR with `negative_prompt_attached_bool: false`, OR with `negative_prompt_sha256.length != 64` → halt with `negative_prompt_missing` errorEnvelope.

Optional re-verification (high-paranoia mode): recompute SHA-256 from the composed template and compare against logged value. Catches log tampering or accidental empty-string concatenation.

---

## Reference SHA-256 (empty `do_not_say` baseline)

Computed against the canonical template above with `{{ brief_do_not_say_csv }}` and `{{ brief_do_not_say_first_order_conjugates_csv }}` collapsed to empty strings:

```
ref_sha256_empty_do_not_say: "<computed at agent runtime per session — NOT pre-baked into v1.0 because brand_id may evolve brand-anti-patterns block in v1.1+>"
```

The hash is deterministic per session — same `brief.do_not_say` + same brand block = same SHA-256.

---

## Provenance

- Authored: 2026-05-15 (Fri · Day 26 · Wk4D6) — ARS overnight build session
- SPEC source: `ARS-2026-05-13-AI-Video-Gen-Agent-v1-Spec-LOCKED.md` §6.5 + §7 Hard Rule #5 + §7 Hard Rule #4 + §6 (brand-anti-patterns derived)
- Schema enforcement: `schemas/output.schema.json` `render_dispatch_log[*].negative_prompt_attached_bool: const: true` + `negative_prompt_sha256: pattern ^[a-f0-9]{64}$` (Day 25 LOCKED)
- Self-QC enforcement: SKILL.md Check #10
- Hard Rule enforcement: SKILL.md Hard Rule #10 (Process Step 4 + every dispatch in Steps 5–6)
- v1.1+ candidates: multi-brand `brand_anti_patterns` injection · per-brand SHA-256 baseline registry
- Lives at: `ars/skills/ai-video-gen-agent/negative_prompt_template.md` (mirror to `/outputs/ars/`)
- No external comms. No render API. No financial commitments.
