# Case 02 — Mode-C-origin Enterprise reel → PLAN_READY (the mode-blind convergence proof)

**Verdict:** `plan_ready` → `successEditPlan` · **Code:** `null`

An Ingest-passed Enterprise reel whose Asset Manifest originated from Mode C (replicated hot-path): 8-shot bundle, full coverage, firewall-clean. The ONLY input differences from TC-01 are `metadata.production_mode: "C"` and the richer Enterprise envelope.

**Proves the convergence payoff Ingest unlocked** — the FIRST fleet test where the mode columns are behaviorally identical. The authored plan is byte-shape-identical to TC-01 downstream of the `tier_richness` block: `edit_plan`, `coverage_remap`, `structure_check`, `brand_edit_check`, `edit_plan_firewall_pass_9`, and `mode_blind_confirm` are produced by an IDENTICAL code path despite the different origin mode. `mode_blind_confirm.production_mode_read: false` (the agent never consulted the origin mode); no mode-conditional field leaks into the plan; `tier_richness` honors the Enterprise ceilings (≤12 cut beats, unlimited b-roll, 3 music swells, 5 variants flagged) while EVERY brand rule (hard-cuts-only, one-emotional-beat, end-card, internal-question CTA) is identical to the Pro path. The TC-01/TC-02 pair IS the convergence proof.
