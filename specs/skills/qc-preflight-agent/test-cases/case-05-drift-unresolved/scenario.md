# TC-05 — `drift_unresolved` (carried drift -> human-review soft-hold)

**Expected verdict:** `hold` · **branch:** `errorEnvelope` · **code:** `drift_unresolved` · **route_back_to:** `null` (human review)

A Mode B Pro reel where Style Replication flagged `shot-003` with `drift_warning_bool: true` / a
carried `style_drift_exceeded` signal, and there is **no Lever-3 human sign-off** on the carried
drift. QC Pre-flight does NOT auto-fail (a human may accept the drift) and does NOT auto-pass (the
drift is real and unsigned). It emits the **soft-hold** — the one non-binary outcome.

**Key invariants exercised**
- `verdict: "hold"` — the fourth verdict value, distinct from `pass`/`fail`/`reshoot`.
- The agent may NEVER emit `pass` while `unresolved_drift_count > 0` (Rule #10); self-QC Check #8 catches a forbidden auto-pass-over-drift before emission.
- Schema `allOf` guard: a `hold` verdict MUST carry `route_back_to: null` + `failure_code: drift_unresolved`. Human routing is recorded in `detail.routed_to`.
- This is the recommend-don't-approve discipline at its sharpest: faced with genuine ambiguity, the agent declines to render a machine verdict and defers to the operator.
