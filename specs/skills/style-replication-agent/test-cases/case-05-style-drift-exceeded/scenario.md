# TC-05 — Mode B Pro Style Drift Exceeded

**Branch:** errorEnvelope / failure_code=style_drift_exceeded

## Setup
- Tier: Pro · Mode: B · 4 shots
- shot-003 prompt_seed contained noise upstream → drifts away from anchor on both attempts
- Tests Decision #6 regenerate-then-still-fail 2-strike ceiling

## Agent loop (expected)
- Step 1 schema valid
- Step 2 anchor cache HIT
- Step 6 per-shot dispatch:
  - shot-002 → Pika → score 0.92 (pass)
  - shot-003 attempt 1 → Pika → score 0.71 (fail Check #6 drift threshold 0.85)
  - shot-003 attempt 2 (regenerate ONCE per Decision #6) → Pika → score 0.74 (still fail)
  - Mark inherit_fail_final, halt with style_drift_exceeded
- Do NOT cascade to Runway fallback (per LOCKED canon: drift is reasoning failure, not engine availability — Runway won't fix prompt-side noise)
- shot-004 NOT attempted (halt on shot-003)

## Verification
- status="blocked"
- attempts=2 (matches Decision #6 strike ceiling)
- successful_shots=[shot-001 anchor, shot-002 inheritor] preserved (Hard Rule #12)
- engine_fallback_used_bool=false (no Runway escalation on drift)
- drift_components_attempt_2.s_motion=0.55 surfaces the diagnostic
- recovery_path enumerates inspection path + Edit Director salvage

## v1.0 LOCK gate signal
- Validates Decision #6 2-strike ceiling (no third attempt under any circumstance)
- Validates Hard Rule #6 regenerate-then-still-fail hard halt
- Validates Hard Rule #12 partial-work preservation
- Validates drift_components surface (debugging granularity)
- Demonstrates the agent does NOT confuse drift (reasoning failure) with engine availability (fallback case)
