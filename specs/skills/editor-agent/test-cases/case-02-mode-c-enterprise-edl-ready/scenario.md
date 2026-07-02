# Case 02 — Mode-C Enterprise → `edl_ready` (the mode-blind convergence proof)

**Proves:** Ingest's mode-convergence seam holds **two stages deep** — the byte-shape-identical conform path despite a different origin mode.

The convergence twin of Case 01. The footage here originated in **Mode C** (replicated hot-path — `parent_chain[3] == "mode-c-direct"`), the tier is **Enterprise**, and yet Editor conforms it through the **identical executor logic** and emits a byte-shape-identical `edl` / `conform_check` / `plan_fidelity_check` / `edl_firewall_pass_10` / `mode_blind_confirm` block. Only the audit-lineage fields differ (`production_mode`, `tier`).

**Expected verdict:** `edl_ready`, with `mode_blind_confirm.production_mode_read: false`. The conform never branched on origin mode — the machine-checkable proof that Editor (the executor) carries mode-blindness after Edit Director (the director) carried it, so the post-production tail is mode-agnostic end-to-end.
