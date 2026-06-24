# Case 05 — Authored-text firewall breach (banned token in a lower-third Edit Director WROTE) → hard FAIL

**Verdict:** `fail` → `errorEnvelope` · **Code:** `edit_plan_firewall_breach` · **GATING fixture (9th-pass new surface)**

A Mode-B-origin reel, all upstream content fully clean (Ingest's 8th pass passed it; all 8 prior passes would pass it) — but during caption/lower-third authoring the agent composes a lower-third reading `built for operators like sln` (firewall entry #4 token in the copy Edit Director itself WROTE) and a second reading `see holdcogroup.com` (entry #10 URL token).

**Proves:** `failed_check_id: 4`; `detail.edit_plan_firewall_pass_9 {status: breach, authored_text_fields_scanned: N, hits: 2}` with the census matching the true authored-field count (every lower-third + caption line + the end-card); forensic `detail` names BOTH leaking AUTHORED fields + the rule each violated; `route_back_to: null` (no upstream is at fault — the leak is in Edit Director's own authorship). The catch occurs on a surface NO content pass and NO prior firewall pass could see — this is the 9th pass's existence proof, the FIRST firewall over self-authored text. The single highest-stakes code in the namespace — a leak here would be burned into a published cut.
