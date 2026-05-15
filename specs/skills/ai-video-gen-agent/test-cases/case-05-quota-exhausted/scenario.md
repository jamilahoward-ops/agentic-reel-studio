# TC-05 — Inheritor cascade failure → `render_quota_exhausted`

**Tier:** Pro
**Mode:** B
**Total shots:** 3 (anchor + 2 inheritors)
**Engine assignments:** Runway Gen3 Alpha (anchor) · Pika (inheritor 1, fallback Luma) · Kling (inheritor 2, fallback Higgsfield)
**Expected branch:** `errorEnvelope`
**Expected failure_code:** `render_quota_exhausted`
**Expected failed_check_id:** 5 (Mode B coverage)
**Expected attempts:** 2 (Donna's outer self-QC — both inheritors burn 4 attempts each at the engine layer)

## Scenario

The anchor shot renders cleanly on Runway Gen3 Alpha — `render_status: "rendered"`. But every available inheritor engine has been quota-exhausted upstream by other concurrent reels (Pika rate-limited, Luma quota burned, Kling vendor outage, Higgsfield rate-limited). All inheritor renders fail across primary + fallback (4 attempts each).

Per Hard Rule #12 (retry policy):
- `shot-002` Pika: 2 attempts fail → fallback Luma: 2 attempts fail = `engine_failure_unrecoverable` for that shot
- `shot-003` Kling: 2 attempts fail → fallback Higgsfield: 2 attempts fail = `engine_failure_unrecoverable` for that shot

Per Hard Rule #12, inheritor failures are NOT individually fatal — agent continues. But Check #5 (Mode B coverage) detects that ALL inheritors failed across all engines → escalates to `render_quota_exhausted` (collective failure mode, distinct from `engine_failure_unrecoverable` which is per-shot).

Cost incurred: ~$198 (1 anchor + 8 burned inheritor attempts at varying engine prices).

The anchor `shot-001` did render successfully — but with 2 of 3 inheritors failed AND no engines remaining to retry, the set cannot be shipped. Operator absorbs the spent $198. The renders that DID complete are preserved in `detail{}` for forensic review (anchor render asset remains in object storage; orchestrator decides whether to re-queue with fresh quotas).

## Validates

- Inheritor failure cascade — distinct from anchor failure (TC-03)
- `render_quota_exhausted` distinct from `engine_failure_unrecoverable` (Decision #11 split)
- `failed_check_id: 5` (Check #5 Mode B coverage)
- `attempts: 2` (agent regenerated once at outer self-QC layer to confirm no recovery path)
- `failed_inheritor_shot_ids: [...]` in `detail{}`
- `engines_burned: [...]` in `detail{}` lists every engine touched
- `anchor_status: "rendered"` preserved in `detail{}` (operator knows the anchor asset exists for future re-queue)
- `cost_incurred_usd` honest accounting of spent capital

## Why this fixture exists

Tests the second-largest cost-protection invariant after anchor failure. When an entire vendor cohort has quota issues, the agent halts cleanly with a forensically rich errorEnvelope rather than emitting a partial-with-warnings set that downstream Edit can't actually use. The clean halt + cost honesty is the contract.
