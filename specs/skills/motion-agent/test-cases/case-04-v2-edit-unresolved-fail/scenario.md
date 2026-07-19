# TC-04 — v2-edit handle does not resolve → FAIL + route to Sound

**Input:** A Sound-passed reel whose `audio_spec.finish_target.v2_edit_uri` is `null` (the audio-final cut handle does not resolve) and whose `asset_bundle.video` list is empty. The typography text still resolves from the EDL passthrough — only the picture handle is missing.

**Expected verdict:** `fail` (`errorEnvelope`).
**Expected code:** `v2_edit_unresolved` · `failed_check_id: 3` · `route_back_to: "sound-agent"`.

**Proves:** The SPLIT-code proof carried one stage deeper. `v2_edit_unresolved` routes to **Sound** (the `finish_target` block is where the v2-edit handle is minted) — the direct structural analog of Sound's `vo_track_missing`/`audio_asset_unresolved` split, except Motion's split routes to **two different agents** (the picture comes from Sound; the text comes from Editor), so the split is even more strongly justified (D8). `detail` names the unresolvable `v2_edit_uri` + the distinct recovery path. Verdict is `fail`, not `revise`.
