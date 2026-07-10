# TC-04 — `vo_track_missing` → `fail` (route Ingest) — the SPLIT resolution code

**Branch:** `errorEnvelope` · **verdict:** `fail` · **code:** `vo_track_missing` · **route:** `ingest-agent`

The declared VO voice track does not resolve in `asset_bundle.audio[]` (the array is empty).
Sound never specs a VO polish pass over a missing track, so it FAILS and routes back to
**Ingest** to re-confirm the voice-track resolution.

This is the proof of the **SPLIT** asset codes — the deliberate OPPOSITE of Editor folding
all resolution into one `asset_unresolved` (D8). `vo_track_missing` (VO side) and
`audio_asset_unresolved` (music-bed side) are kept SEPARATE because a missing voice track
and an unresolvable bed demand different operator recovery actions. The music-bed
`audio_asset_unresolved` variant is exercised as the LLM Test Runbook probe.
