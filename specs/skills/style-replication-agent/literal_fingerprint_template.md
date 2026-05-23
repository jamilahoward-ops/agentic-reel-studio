# Literal Fingerprint Inherit Template — Style Replication Agent v1.0 (Day 34)

> **Role:** Style Replication's analog to AI Video Gen's `negative_prompt_template.md`. Documents the canonical composition rule for `literal_fingerprint_inherit` and the §16.5 decision #3 `anyOf` encoding that distinguishes Mode A partial encoding from Mode B + C full encoding.

---

## Why this exists

AI Video Gen ships every render dispatch with a SHA-256 of the composed negative prompt (Hard Rule #10 → schema-layer `const: true`). Style Replication is the **downstream half** of the same firewall: the brand-anchor immutable fingerprint passed downstream so **QC and the Loop agent can re-validate** without recomputing CLIP/pHash.

`literal_fingerprint_inherit` is the **read-side canon** of the same defense-in-depth pattern.

---

## Composition rule (Mode B + Mode C full encoding)

```
literal_fingerprint_inherit = {
  anchor_clip_embedding_uri:    ars://brand_anchor_cache/{BRAND_ID}/{anchor_id}.embeddings.bin
  anchor_phash_64bit:           0x[16-char lowercase hex of pHash]
  anchor_palette_lab_centroids: [[L*, a*, b*] × 5 — k=5 dominant CIELAB centroids]
  anchor_motion_grade_baseline: { contrast_target, saturation_target, lut_id }
}
```

All four components are derived from the brand-anchor cache lookup at **Step 2 of the 11-step process** (§7 system prompt) — before any per-shot dispatch. Cache miss on any of the four = halt with `anchor_unavailable`.

---

## Mode A partial encoding (§16.5 decision #3)

Mode A operates on a **raw shoot manifest** (operator + videographer assets). Raw shoot manifest fingerprinting differs from rendered_shots fingerprinting — specifically, `anchor_phash_64bit` is **not extracted** for raw shots because pHash on freshly captured ProRes/BRAW frames is **prone to capture-noise drift** that defeats the cache lookup invariant.

Mode A partial encoding **omits** `anchor_phash_64bit`. The schema enforces this via `not: required[anchor_phash_64bit]` on the `literalFingerprintInheritModeAPartial` `$def`.

```
literal_fingerprint_inherit (Mode A) = {
  anchor_clip_embedding_uri:    (present)
  anchor_phash_64bit:           (ABSENT — schema rejects if present)
  anchor_palette_lab_centroids: (present)
  anchor_motion_grade_baseline: (present)
}
```

---

## errorEnvelope branch

On the errorEnvelope branch, `literal_fingerprint_inherit` is `null`. The `anyOf` accepts three shapes:
1. Full (Mode B + C success branch)
2. Mode A partial (Mode A success branch)
3. null (errorEnvelope branch — agent halted before fingerprint resolved or after fingerprint resolved but before any inheritor shot succeeded)

---

## Enforcement chain (5 layers)

| Layer | What enforces | Failure mode |
|---|---|---|
| 1. Schema parse | `anyOf` on `literal_fingerprint_inherit` rejects unknown shapes | Caught at output validation (before downstream consumes) |
| 2. Anchor cache lookup (§7 Step 2) | Three-way bit equality: `anchor_id` + `anchor_sha256` + `anchor_locked_date` (Hard Rule #9) | `anchor_unavailable` errorEnvelope |
| 3. Composite inheritance_match_score (§7 Step 6) | `0.40 × s_clip + 0.30 × s_phash + 0.20 × s_palette + 0.10 × s_motion` per §12 (VERBATIM INHERIT from AI Video Gen Day 23 §12) | `style_drift_exceeded` if regenerate-then-still-fail (Decision #6 2-strike ceiling) |
| 4. QC pre-flag predicates (§7 Step 8) | `qc_pre_flags` snake_case predicates per Cross-SPEC §3.7 | `qc_pre_flags_format_violation` |
| 5. Downstream Loop agent (post-handoff) | Re-validates `literal_fingerprint_inherit` against the **same** brand-anchor cache to detect cache poisoning / version drift across Loop cycles | Loop agent halts; operator notified |

---

## What v1.0 does NOT cover

- **Real-time preview fingerprint inherit** (deferred to v1.0.1)
- **Multi-brand fingerprint federation** (deferred to v1.1+ — first Sequel Digital external client)
- **Per-engine drift attribution** within `literal_fingerprint_inherit` (current implementation rolls per-engine attribution into `per_engine_overrun_attribution` only on cost overrun, not on drift)
- **Anchor versioning beyond `anchor_version` major.minor** (no LoRA-style fine-tune chain; v1.1+)

These are documented as parked v1.0.1+ items in §15.

---

## Provenance

- Authored 2026-05-23 (Day 34 · Sat · Wk5D8/Wk6D1) — Sequel Digital ARS overnight build session
- SPEC source: Day 30 §6 (Self-QC) + Day 30 §7 (System Prompt) + Day 31 §12 (VERBATIM INHERIT from AI Video Gen Day 23 §12) + Day 31 §16 (Metadata Block) + Day 33 §16.5 decision #3 (Mode A partial encoding via `anyOf` + `not: required`)
- Mirror: AI Video Gen `negative_prompt_template.md` (read-side analog)
- No external comms. No render API. No engine credentials. No financial commitments.
