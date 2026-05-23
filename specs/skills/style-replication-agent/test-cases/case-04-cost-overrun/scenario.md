# TC-04 — Mode B Enterprise Cost Overrun

**Branch:** errorEnvelope / failure_code=cost_overrun

## Setup
- Tier: Enterprise · Mode: B · 8 shots (large reel)
- Pika availability degraded → 3 of 7 inheritors cascade to Runway fallback
- Cumulative spend breaches $120 × 1.10 = $132 hard ceiling on shot-006 dispatch

## Agent loop (expected)
- Step 1 schema valid (Enterprise + Mode B)
- Step 2 anchor cache HIT
- Step 5 cost projection: 7 × $0.13 Pika + native ~ $1 (under $132 ceiling, dispatch proceeds)
- Step 6 mid-dispatch reality: Pika fails first attempt on shots 002/003/004 → Runway fallback each time (engine_fallback_used_bool=true, cost ~$20-26 per Runway shot)
- Cumulative tracking: $134.15 at shot-006 entry — projection vs actual diverged
- Halt with cost_overrun on shot-006 BEFORE dispatching that engine job
- failed_check_id=7 (Cost ceiling enforcement)
- failed_shot_id=shot-006

## Verification
- status="blocked"
- 5 successful_shots[] preserved (Hard Rule #12 partial-work preservation)
- per_engine_overrun_attribution surfaces runway_style_reference=$60 as the cost driver
- recovery_path enumerates 3 operator-actionable mitigations
- Demonstrates fail-fast at projection (Step 7 reality vs Step 5 projection divergence)

## v1.0 LOCK gate signal
- Validates cost ceiling × 1.10 invariant (Hard Rule #7)
- Validates Hard Rule #12 partial-work preservation
- Validates per_engine_overrun_attribution telemetry (debugging surface for ops)
- Cost discipline: hard halt at $134.15 prevents runaway spend
