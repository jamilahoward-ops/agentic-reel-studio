# TC-01 — Clean Mode-A-origin Pro reel → MOTION_READY

**Input:** A Sound-passed (`audio_ready`) Pro reel from a Mode-A (human-footage) origin. A 2-caption / 1-lower-third typography set over a 60000ms timeline, the resolved v2-edit handle (`ars://reel/v2.mp4`), a clean 10-tuple inbound `parent_chain`, both upstream evidence hashes present.

**Expected verdict:** `motion_ready` (`successMotionSpec`).
**Expected code:** `null`.

**Proves:** The full faithful-finish happy path. Every deterministic gate green — the two upstream evidence hashes re-verify, the v2 edit + all typography text resolve, every reveal/overlay/lower-third/end-card marker sits inside the timeline, the reveal cadence and motion tokens are the brand consts, the end-card is the brand const, the 12th-pass typography firewall is clean (`hits: 0`). The emitted `motion_spec` carries the caption reveals (byte-faithful, `line_in` / `ease_in_out_120ms`), the brand `reveal_cadence`, the lowercase-sans lower-third (`all_caps: false`), the allowed motion tokens, a subtle-parallax overlay, and the serif-ivory end-card. `motion_processed: false` + `finish_mode: human_in_the_loop` + `human_review_required: true` (recommend-don't-render). `parent_chain` extended to an 11-tuple (append `motion_spec_id`, held additively). Handoff `["qc-agent"]`.
