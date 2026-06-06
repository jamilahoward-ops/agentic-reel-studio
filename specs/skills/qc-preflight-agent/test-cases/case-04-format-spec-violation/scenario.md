# TC-04 — `format_spec_violation` (aspect mismatch -> fail + route)

**Expected verdict:** `fail` · **branch:** `errorEnvelope` · **code:** `format_spec_violation` · **route_back_to:** `style-replication-agent`

A Mode B Pro reel where `production_plan.platform_variants[1]` requests a 1:1 Instagram-feed crop,
but every `replicated_shots[*]` was produced at 9:16 only. The format spec check finds the missing
1:1 variant -> `fail`, routes back to the responsible production agent.

**Key invariants exercised**
- `format_spec_check.platform_variants_checked == len(platform_variants)` — coverage complete (no variant skipped); the violation is a real mismatch, not under-reporting.
- `route_back_to: "style-replication-agent"` (the agent that produces the deliverable aspect) — NOT `production-coord-agent`, because this is a Mode B render-side defect, not an unrecoverable live-footage source (Mode A reshoot).
- `recovery_path` offers BOTH a fix-it route and a drop-the-variant route — advisory, not auto-executed (Decision #13: route-back automation depth is advisory in v1.0).
