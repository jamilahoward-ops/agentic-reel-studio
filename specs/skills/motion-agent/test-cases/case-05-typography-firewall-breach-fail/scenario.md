# TC-05 — Typography-domain firewall breach → hard FAIL (12th-pass last visual-text checkpoint · GATING)

**Input:** A Sound-passed reel carrying TWO banned entity tokens that survived into the passthrough on-screen typography: `sln` in `caption_events[0].text` ("build on purpose with sln cuts.") and `holdco group` in `lower_third_events[0].text`. These are HC/NPOX firewall BLOCK-list tokens (§6.5, 11 entries) — not a cross-entity reference; ARS is Sequel Digital scope only.

**Expected verdict:** `fail` (`errorEnvelope`).
**Expected code:** `motion_firewall_breach` · `failed_check_id: 8` · `route_back_to: null` (forensic hold, not a re-work loop).

**Proves:** The 12th pass's existence proof — the LAST visual-text checkpoint before the master reaches full QC. Editor's 10th pass scanned the text as committed *data*; Sound's 11th scanned the *spoken* transcript; only Motion's 12th scans the text at the moment it becomes *pixels*. `detail.motion_firewall_pass_12 {status: "breach", passthrough_typography_fields_scanned: 4, hits: 2}`; `detail.leaking_fields` names BOTH offending typography fields + the rule each violated. **The single highest-stakes code in the namespace — a miss here is a banned entity token rendered into a published reel's frames, with no post-hoc fix. GATING: a runbook run that does not catch TC-05 fails the LOCK gate.**
