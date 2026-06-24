# Case 04 — Brand-edit rule conflict (a beat that only resolves with a fade) → hard FAIL

**Verdict:** `fail` → `errorEnvelope` · **Code:** `brand_edit_rule_conflict`

A Pro reel whose only coherent cut between beats 2 and 3 would require a cross-fade (the available shots cannot hard-cut cleanly without a jarring jump), and no alternate ordering avoids it. Every other gate is clean. The hard-cuts-only rule is NON-NEGOTIABLE (brand canon §7), so it cannot be silently overridden.

**Proves:** `failed_check_id: 7` (hard-rule branch); `detail.brand_edit_check.hard_cuts_only: false` with all other sub-statuses still explicitly computed (no short-circuit nulls); `detail` names the offending beat transition + the rule violated; verdict `fail` NOT `revise` (a HARD brand rule that cannot be satisfied is a hard fail — `revise` is reserved for SOFT-rule creative tension, not non-negotiable violations); `route_back_to: "production-coord-agent"` (the cut cannot be filled from current assets/intent — re-spec the shot coverage). The zero-tolerance brand-edit firewall's existence proof: a fade must NEVER survive to `plan_ready`.
