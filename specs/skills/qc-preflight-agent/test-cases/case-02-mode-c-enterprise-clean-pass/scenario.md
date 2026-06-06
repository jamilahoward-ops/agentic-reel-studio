# TC-02 — Mode C Enterprise clean PASS

**Expected verdict:** `pass` · **branch:** `successPreflightReport` · **code:** none · **route_back_to:** null

Enterprise client (REINVENTED) Mode C hot-path reel — Style Replication produced grade-pass output
directly against the LOCKED anchor; AI Video Gen was NOT invoked, so there is **no `rendered_shots`
and no Mode B forensic cross-check** (`mode_b_chain_check` reports `null`). 3 `platform_variants`.
No carried drift. Cumulative cost $0.57 — well within the $870 Enterprise combined ceiling.

**Why this fixture matters:** it proves the gate is genuinely **mode-agnostic in verdict but
mode-aware in reporting** — the same PASS decision as TC-01, with the Mode B-only fields correctly
nulled. Without TC-02, a regression that hard-required `rendered_shots` would silently fail every
Mode C reel — the highest-margin path.

**Key invariants exercised**
- Mode-agnostic verdict logic produces the same PASS shape as TC-01 with `mode_b_chain_check: null`.
- `reshoot` (route to production-coord-agent) is unreachable in Mode C (Mode A-exclusive, Decision #14).
- `cost_ledger_check.tier_combined_ceiling_usd == 870`.
- Lineage position 3 = `mode-c-direct` (no AI Video Gen stage in the chain).
- All 12 self-QC checks PASS first attempt.
