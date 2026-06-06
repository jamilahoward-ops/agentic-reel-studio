# TC-03 — `entity_firewall_breach` (the 7th-pass catch) · GATING FIXTURE

**Expected verdict:** `fail` · **branch:** `errorEnvelope` · **code:** `entity_firewall_breach` · **route_back_to:** `style-replication-agent`

A Mode B Pro reel where an upstream agent leaked a banned entity token. The
`style-replication-agent` `replication_notes` field contains `"brand finish matched to 4821 Main
reference grade"` — `4821 main` is entry #2 on the canonical firewall list. Six prior passes
missed it (an upstream bug). QC Pre-flight, the 7th and final pass, catches it.

**This is the most important fixture in the portfolio.** It is the proof that the agent's reason to
exist — being the net that catches what six prior passes missed — actually fires. A v1.0 LOCK is
BLOCKED if TC-03 does not catch the injected token.

**Key invariants exercised**
- Token-boundary, case-insensitive match — `4821 main` caught even mid-sentence in a free-text field.
- `failed_check_id: 2`, `failure_code: "entity_firewall_breach"`, `route_back_to: "style-replication-agent"` (the leaking stage, named in `detail.leaking_upstream_stage`).
- `human_review_required: true` — even a clear breach is a recommendation to the operator, never an autonomous quarantine.
- `attempts: 1` — a real reel defect is a valid verdict on first construction, not a self-QC regenerate loop.

> **Note:** the input is schema-valid (the firewall catch is a runtime adjudication, not a parse-time reject). The injected token rides inside `replication_notes`, an unconstrained free-text field on the consumed shot.
