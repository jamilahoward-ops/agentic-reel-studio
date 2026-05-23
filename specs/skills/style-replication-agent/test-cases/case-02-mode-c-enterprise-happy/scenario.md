# TC-02 — Mode C Enterprise Happy Path · MARGIN DEMO -92%

**Branch:** successReplicatedShots / status=ready_for_qc

## Setup
- Tier: **Enterprise** ($120/reel ceiling)
- Mode: **C** (Enterprise hot-path direct from ProdCoord; no AI Video Gen upstream)
- 3 shots total: anchor + 2 hot-path inheritors
- mode_c_directive.coverage_envelope_tolerance_pct = 12 (default)

## Agent loop (expected)
- Step 1 schema valid; tier=Enterprise (Decision #10 satisfied)
- Step 2 anchor cache HIT (three-way bit equality)
- Step 3 Mode C branch: validate envelope tolerance against anchor envelope
- Step 4 firewall payload + SHA-256
- Step 5 cost projection: 2 × $0.13 (Pika) + 3 × ~$0.005 (native) + 3 × $0.001 (envelope check) = ~$55 (within Enterprise $120 × 1.10 = $132 ceiling)
- Step 6 per-shot dispatch: Pika succeeds on both inheritors (no fallback)
- Step 7 grade pass applied (cinematic finish intent)
- Step 8 Self-QC 12 checks: all PASS
- Step 9 Mode C envelope check PASS → mode_c_coverage_match_bool=true
- Step 10 literal_fingerprint_inherit FULL encoding; replication_set_id UUID; 5-tuple parent_chain with "mode-c-direct" at position [3]
- Step 11 successReplicatedShots emitted

## The Margin Story
- Mode C actual cost: **$55.00**
- Mode B equivalent re-render envelope (~$692 — 3 shots × Runway anchor $15 + 2 inheritors × HeyGen polish + native pipeline)
- **Δ = -$637/reel · -92% cost**
- This is the agent's economic justification at scale. Without Mode C, Lever 1 graduation (post-90 reels) does not pencil.

## v1.0 LOCK gate signal
- mode_c_coverage_match_bool=true (not null) — only Mode C output
- "mode-c-direct" literal in parent_chain position [3]
- per_engine_dispatched.coverage_envelope_native=3 (Mode C only engine)
- self_qc_failed_check_id=null (clean run)
