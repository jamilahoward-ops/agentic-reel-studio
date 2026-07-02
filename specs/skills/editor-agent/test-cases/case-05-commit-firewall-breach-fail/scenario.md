# Case 05 — Commit-time firewall breach → `fail` / `edl_firewall_breach` (GATING)

**Proves:** the 10th defense-in-depth pass — the last text checkpoint before pixels.

A banned-entity token (`sln`) has survived into a committed caption line (`"sln runs the studio"`). Editor authors no new copy — the string is Edit Director passthrough — but Editor is the agent that COMMITS that text to the executable cut spec, so its 10th-pass commit-time firewall re-scan is the final net before the copy is burned into pixels (Hard Rule #9 / Check #9).

**Expected verdict:** `fail`, `failure_code: edl_firewall_breach`, `failed_check_id: 9`, `route_back_to: edit-director-agent` (the committed copy is the plan's — the author owns the fix). `detail` forensically names the leaking committed field + the `hits: 1` firewall result. This is the **highest-stakes** code in the namespace: a leak here would be burned into the v1.mp4. GATING fixture.
