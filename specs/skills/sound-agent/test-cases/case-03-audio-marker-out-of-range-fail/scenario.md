# TC-03 — `audio_marker_out_of_range` → `fail` (route Editor)

**Branch:** `errorEnvelope` · **verdict:** `fail` · **code:** `audio_marker_out_of_range` · **route:** `editor-agent`

A swell/SFX marker `at_ms` (90 000 ms) exceeds the EDL `total_timeline_ms` (60 000 ms).
A marker past the timeline is a timeline/EDL defect, so Sound FAILS the finish and routes
back to **Editor** to re-place the marker inside the conformed runtime. The `detail` names
the offending marker + the timeline bound. Soft-recoverable, never silently clamped
(Hard Rule #6 / Step 4 / Check #4).
