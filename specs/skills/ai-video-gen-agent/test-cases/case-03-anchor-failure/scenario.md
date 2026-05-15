# TC-03 — Anchor failure → `engine_failure_unrecoverable`

**Tier:** Pro
**Mode:** B
**Total shots:** 3 (anchor + 2 inheritors)
**Engine assignments:** Runway Gen3 Alpha (anchor + all inheritors) · Pika 1.5 (fallback)
**Expected branch:** `errorEnvelope`
**Expected failure_code:** `engine_failure_unrecoverable`
**Expected failed_check_id:** 6 (anchor render success)
**Expected attempts:** 4 (primary attempt 1 → primary attempt 2 → fallback attempt 1 → fallback attempt 2)

## Scenario

The anchor shot's `prompt_seed` is unusually demanding — "anchor: complex hero shot with intricate motion blur dynamics" — which triggers Runway Gen3 Alpha to repeatedly return a degraded/corrupted output OR an explicit failure response.

Process Step 5 attempts:
1. **Runway Gen3 Alpha attempt 1** — fail (engine returns rendering error or degraded quality below acceptance threshold)
2. **Runway Gen3 Alpha attempt 2 (retry)** — fail (same error)
3. **Pika 1.5 (fallback) attempt 1** — fail (different engine, same difficult prompt)
4. **Pika 1.5 (fallback) attempt 2 (retry)** — fail

After 4 burned attempts, the anchor is unrecoverable. Per Hard Rule #11 (anchor-first sequencing), the agent halts the entire render set. Inheritors (`shot-002`, `shot-003`) are NEVER dispatched — operator avoids the cost of N inheritor renders that would all drift without an anchor reference.

Cost incurred: ~$45 (4 attempts × ~$11 average per attempt at 15s anchor duration).

## Validates

- Anchor-first render sequencing (Hard Rule #11) — inheritors never dispatch
- Retry policy (Hard Rule #12) — exactly 1+1 across primary + fallback (max 4 attempts/shot)
- `engine_failure_unrecoverable` errorEnvelope shape with `anchor_shot_id` + `engines_burned` + `cost_incurred_usd` in `detail{}`
- `failed_check_id: 6` (Check #6 anchor render success)
- `attempts: 4` (cost-disciplined ceiling)
- `status: "blocked"` at top level
- No partial set emitted — anchor failure is fatal (vs inheritor failure which would emit `partial_with_warnings`)

## Why this fixture exists

Tests the most expensive failure mode the agent can prevent. The cost discipline of "anchor fail = whole set blocked" prevents the operator from paying for 2 inheritor renders that would each render from a non-existent style anchor. This is the single most important cost-protection invariant in v1.0.
