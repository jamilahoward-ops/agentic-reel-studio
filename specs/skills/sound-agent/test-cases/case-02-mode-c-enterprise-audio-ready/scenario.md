# TC-02 — Mode-C Enterprise → `audio_ready` (the mode-blind finish-convergence proof)

**Branch:** `successAudioSpec` · **verdict:** `audio_ready` · **code:** `null`

The convergence twin of TC-01. A Mode-C (replicated hot-path) Enterprise reel produces a
**byte-shape-identical** `audio_spec` / `audio_conform_check` / `spec_fidelity_check` /
`audio_firewall_pass_11` / `mode_blind_confirm` / `finish_target` to the Mode-A Pro TC-01 —
despite a different origin `production_mode` (C vs A) and a different `parent_chain`
position-3 element (`mode-c-direct` vs the `productionplan-…` id).

This pair **IS** the mode-blind finish-convergence proof, now **three stages deep**: the
payoff Ingest's mode-convergence seam unlocked, carried through the director (Edit
Director), the timeline executor (Editor), AND now the audio finisher (Sound). Because
Sound never reads `production_mode`, the finish path cannot diverge on origin — the
`validate.py` convergence assertion checks the six finish blocks are equal while the modes
differ.
