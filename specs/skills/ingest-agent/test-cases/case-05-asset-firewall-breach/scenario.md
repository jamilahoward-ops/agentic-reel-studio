# Case 05 — 8th-pass asset-layer firewall breach -> FAIL

**Verdict:** `fail` -> `errorEnvelope` (`asset_firewall_breach`)

A Pro-tier Mode B reel whose **content is fully clean** — all 7 prior content firewall passes would pass it. But the asset layer leaks: shot-002's filename is `sln_cuts_promo_take2.mp4` (entity token `sln`) and its sidecar caption metadata carries `holdcogroup.com`. Two hits. The forensic `detail` names both assets + the leaking upstream stage.

**Proves the agent's reason to exist (GATING fixture):** the 8th defense-in-depth pass scans the asset-layer surface — filenames, embedded media metadata, sidecar SRT/caption files — that no prior content pass ever inspected (Hard Rule #6). The banned tokens ride inside schema-valid `ars://` URIs and free-text fields, so the catch is a runtime adjudication, not a schema rejection.
