# TC-04 — Cost overrun → `cost_overrun`

**Tier:** Enterprise
**Mode:** B
**Total shots:** 5 (anchor + 4 inheritors)
**Engine assignments:** Runway Gen3 Alpha (anchor 30s) · Pika · HeyGen v3 polish (talent) · Kling · Flux
**Expected branch:** `errorEnvelope`
**Expected failure_code:** `cost_overrun`
**Expected failed_check_id:** 7 (cost ceiling compliance)
**Expected attempts:** 1

## Scenario

An Enterprise-tier reel where renders complete successfully but actual costs blow past the hard ceiling.

ProdCoord estimated $750 (=Enterprise ceiling). At runtime, actual costs run higher than the per-engine snapshot due to:
- Anchor at 30s on Runway Gen3 Alpha = $28.50 (estimate vs actual close)
- Multiple engine retries (transient 5xx surfaces) — retry costs accumulate
- HeyGen v3 polish per-second slightly higher than canon snapshot
- Aggregate per-engine overrun attribution: Runway +$42, Pika +$18, HeyGen +$15, Kling +$12, Flux +$5

Total actual: **$852** vs hard ceiling **$825** (= $750 × 1.10 default buffer) → **excess: $27 (3.3% over hard ceiling)**.

Per Hard Rule #7 ("cost ceiling is HARD; no exceptions for almost made it"), Process Step 8 telemetry true-up triggers `cost_overrun` errorEnvelope. Renders are NOT routed to Edit Director — operator absorbs the spent $852 but downstream cost is prevented (no Edit / QC compute spent on an over-budget set).

## Validates

- Cost ceiling enforcement (Hard Rule #7) — `total_render_cost_usd_actual > tier_cost_ceiling_usd × 1.10` triggers halt
- Default `cost_overrun_buffer_pct: 10` produces $825 hard ceiling for Enterprise
- `per_engine_overrun_attribution{}` in `detail{}` (operator can identify which engine drove the overrun for next iteration)
- `failed_check_id: 7` (Check #7)
- `excess_usd: 27` and `excess_pct: 13.6` (relative to estimate, not ceiling) in `detail{}`
- `attempts: 1` (cost overrun is detected once at telemetry true-up — no retry possible)

## Why this fixture exists

Tests the hardest cost discipline rule. Even $1 over the hard ceiling = halt. This fixture proves the agent does NOT ship over-budget renders even when all renders technically succeeded. The cost ceiling is the operator's CFO lens; this is where it gets enforced.
