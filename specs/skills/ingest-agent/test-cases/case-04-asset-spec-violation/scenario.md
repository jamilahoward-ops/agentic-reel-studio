# Case 04 — declared-spec mismatch -> FAIL

**Verdict:** `fail` -> `errorEnvelope` (`asset_spec_violation`)

A Pro-tier Mode B reel. shot-003's declared aspect is 16:9 against a 9:16 plan target. The mismatch is a **fixable** defect — re-replicate the shot, no re-shoot. Routes to `style-replication-agent`. Verdict is `fail`, NOT `reshoot` (Mode B AI output is re-genned). All other sub-checks were still computed — no short-circuit nulls.

**Proves:** spec adjudication at the DECLARED level (`byte_probe_performed:false`); the fail-route to the responsible producing agent; the duration-envelope fold lives in this same code family (`detail.subtype`, Decision #14).
