# TC-03 — Caption reveal exceeds timeline → FAIL + route to Editor

**Input:** A Sound-passed reel whose second caption event lands at `at_ms: 90000` — past the 60000ms `total_timeline_ms`. A timeline/EDL defect: a reveal cannot be placed after the reel ends.

**Expected verdict:** `fail` (`errorEnvelope`).
**Expected code:** `motion_marker_out_of_range` · `failed_check_id: 4` · `route_back_to: "editor-agent"`.

**Proves:** The principal Editor route-back. The marker/timeline conform (Check #4) catches an over-range reveal and routes it back to the timeline owner (Editor) to re-place inside the 60000ms bound. `detail` names the offending marker (`90000`) + the timeline bound (`60000`) + the recovery path. Verdict is `fail` NOT `revise` (an over-range marker is a hard defect; Motion has no `revise` slot). `human_review_required: true`.
