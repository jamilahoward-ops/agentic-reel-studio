# TC-01 — Mode-A-origin Pro → `audio_ready`

**Branch:** `successAudioSpec` · **verdict:** `audio_ready` · **code:** `null`

The full faithful-finish happy path. A Mode-A (human-footage) Pro reel arrives with an
Editor `edl_ready` EDL (two hard-cut events, a music bed at t0 with two swell markers,
a two-line passthrough VO transcript) plus a resolved asset bundle (VO voice track +
music bed).

Sound authors ONE canonical `audio_spec`: the `-14 LUFS (IG/TT)` loudness target with a
`-1.0 dBTP` true-peak ceiling, the VO polish directives to the brand voice cadence, the
music-bed base level + duck envelope (duck moves over the VO spans, swell moves mapped
byte-position-faithful from the EDL `music_swell_map`), and the SFX accents placed on the
EDL swell markers — every marker inside the 60 000 ms timeline.

Proves: the `audio_conform_check` all-true, the 5 `spec_fidelity_check` booleans all-true,
the 11th-pass firewall census clean (`hits: 0`), the 10-tuple `parent_chain` additive
extension, `audio_processed: false` / `finish_mode: human_in_the_loop`, and
`mode_blind_confirm.production_mode_read: false`. An `audio_ready` = "ready for the human's
finish-into-v2 decision," never "mixed."
