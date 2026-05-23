# TC-03 — Mode C Anchor Unavailable

**Branch:** errorEnvelope / failure_code=anchor_unavailable

## Setup
- Tier: Enterprise · Mode: C
- brand_anchor_reference references DEPRECATED anchor (v0.9, locked 2026-01-15 = 128 days old)
- Default freshness ceiling 90 days → STALE
- Current cache holds anchor-REINVENTED-v1-2026-05-01

## Agent loop (expected)
- Step 1 schema valid (Enterprise + Mode C joint validation satisfied)
- Step 2 anchor cache lookup → three-way bit equality FAIL (anchor_id + anchor_sha256 reference deprecated record)
- Halt with anchor_unavailable BEFORE any dispatch (cost incurred: $0)
- failed_check_id=9 (Anchor identity three-way bit equality)

## Verification
- status="blocked" (const enforced)
- successful_shots=[] (no inheritor reached dispatch)
- recovery_path includes operator-actionable next step (re-LOCK current anchor)
- attempts=1 (single anchor lookup attempt; no regenerate scoped to anchor lookup)
- No partial_replicated_shots (Hard Rule #12 — nothing to preserve)

## v1.0 LOCK gate signal
- Demonstrates fail-fast behavior on stale anchor
- Validates Hard Rule #9 (three-way bit equality) hard halt
- Validates §6.3 6-code namespace (anchor_unavailable as canonical code)
- Cost discipline: $0 spent on doomed dispatch
