# TC-01 — Pro Mode B happy path (3-shot single-engine)

**Tier:** Pro
**Mode:** B
**Total shots:** 3 (anchor + 2 inheritors)
**Engine:** Runway Gen3 Alpha (all shots)
**Expected branch:** `successRenderedShots`
**Expected error:** none

## Scenario

A Pro-tier REINVENTED reel: 45-second 3-shot Mode B render. Anchor on Runway Gen3 Alpha (15s), inheritor 1 on Runway Gen3 Alpha (12s), inheritor 2 on Runway Gen3 Alpha (18s). All renders complete on first attempt. No retries. No fallback engine activations.

Style consistency: anchor seed propagates via `literal_seed_inherit`. Inheritors hold canon (palette match 0.92 / 0.91 / 0.88 — all above 0.85 drift threshold).

Cost: $232 actual / $400 ceiling = 58% utilization (well within sweet-spot 55–85%).

## Validates

- 11-step process executes cleanly with no regen attempts
- Schema-layer enforcement of `negative_prompt_attached_bool: const true` honored on every dispatch log record
- Schema-layer enforcement of `asset_uri` `ars://renderset/...` pattern honored
- 4-tuple `parent_chain` extension at output (input had 3-tuple)
- 11 canonical metadata fields + 3 AI Video Gen-specific fields populated
- All 12 self-QC checks pass on first attempt
- `qc_pre_flags[]` ≥4 entries snake_case
- `handoff_targets[]` ≥2 entries (edit-director + qc) with resolvable `payload_ref`

## Why this fixture exists

Establishes the canonical "happy path" baseline for Pro tier. Every other fixture is a deviation from this shape. This fixture is the regression anchor — if a future SKILL bundle change breaks this, the change is rejected at LOCK gate.
