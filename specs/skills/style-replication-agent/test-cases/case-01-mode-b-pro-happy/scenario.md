# TC-01 — Mode B Pro Happy Path

**Branch:** successReplicatedShots / status=ready_for_qc

## Setup
- Tier: **Pro** ($50/reel ceiling)
- Mode: **B** (inheritor pass on AI Video Gen rendered_shots)
- 5 shots total: anchor (shot-001, Runway) + 4 inheritors (shot-002..005, Pika)
- Brand anchor cache HIT (anchor_id + anchor_sha256 + anchor_locked_date all match)

## Agent loop (expected)
- Step 1 schema valid ✓
- Step 2 anchor cache lookup → three-way bit equality PASS
- Step 3 Mode B branch: extract anchor_clip_embedding + anchor_phash + palette
- Step 4 negative-prompt-equivalent firewall payload composed + SHA-256 hashed
- Step 5 cost projection: 4 × $0.13 (Pika) + 5 × ~$0.004 (native) = ~$0.54; well under $50 × 1.10 = $55 ceiling
- Step 6 per-shot dispatch: Pika PRIMARY succeeds on all 4 inheritors (no fallback)
- Step 7 grade pass applied
- Step 8 Self-QC 12 checks: all PASS
- Step 10 literal_fingerprint_inherit full encoding emitted; replication_set_id UUID generated; 5-tuple parent_chain assembled
- Step 11 successReplicatedShots emitted with handoff_targets [edit-director, qc]

## Verification
- All 4 inheritor scores within drift threshold 0.85 (range 0.90-0.93)
- engine_fallback_used_bool=false on every shot
- mode_c_coverage_match_bool = null (correct for Mode B)
- 5-tuple parent_chain: [brief_id, script_id, storyboard_id, ai-video-gen-session, replication-uuid]
- Total cost $0.527 = 1.05% of $50 Pro ceiling (deep headroom)

## v1.0 LOCK gate signal
- 100% schema validity, 100% firewall catch, 0 retries, p95 wall-clock 4.5 min (under 8 min target)
- Lever 3 default: human review via QC handoff
- Demonstrates dominant-volume production path operating clean
