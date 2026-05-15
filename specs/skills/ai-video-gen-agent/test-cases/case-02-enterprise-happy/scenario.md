# TC-02 — Enterprise Mode B happy path (5-shot mixed-engines + HeyGen talent)

**Tier:** Enterprise
**Mode:** B
**Total shots:** 5 (anchor + 4 inheritors)
**Engines:** Runway Gen3 Alpha Turbo (anchor) · Pika 1.5 (inheritor 1, 5) · HeyGen v3 polish (inheritor 2, talent) · Kling 1.6 (inheritor 3)
**Expected branch:** `successRenderedShots`
**Expected error:** none

## Scenario

An Enterprise-tier REINVENTED reel: 90-second 5-shot Mode B render with HeyGen talent featured. Anchor on Runway Gen3 Alpha Turbo (Enterprise-only, 20s). Inheritors on Pika (12s, 18s), HeyGen v3 polish (25s talent direct-to-camera), Kling (15s establishing wide).

All renders complete on first attempt across 4 engines. No retries. No fallback activations. HeyGen talent_id is `jamila-howard-reinvented-v2` (v1.0 hardcoded — Check #9).

Style consistency: anchor seed propagates via `literal_seed_inherit`. Inheritors hold canon (palette match 0.92 / 0.88 / 0.87 / 0.86 — all above 0.85 drift threshold; one inheritor at the threshold edge).

Cost: $26.08 actual / $750 ceiling = 3.5% utilization (well below ceiling — Enterprise reel ran cheap due to HeyGen pricing efficiency).

## Validates

- Enterprise tier joint validation (`tier_cost_ceiling_usd: 750` enforced at schema layer)
- Multi-engine orchestration (4 distinct engines in one render set)
- HeyGen v3 polish Enterprise-only restriction honored (Pro tier would reject this model_id)
- `talent_id` conditional require on HeyGen shots (Process Step 5/6 + Check #9)
- `engine_telemetry_summary.per_engine` carries all 4 engines with 1.0 success rate
- 4-tuple `parent_chain` extension
- All 12 self-QC checks pass on first attempt across more complex 5-shot set

## Why this fixture exists

Establishes the canonical "Enterprise happy path" baseline. Tests multi-engine orchestration AND HeyGen talent authorization in a single fixture. The Pro fixture (TC-01) is single-engine; this is the multi-engine + talent-shot regression anchor.
