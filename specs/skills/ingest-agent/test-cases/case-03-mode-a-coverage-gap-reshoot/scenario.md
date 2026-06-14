# Case 03 — Mode A coverage gap, ladder exhausted -> RESHOOT

**Verdict:** `reshoot` -> `errorEnvelope` (`missing_shot_coverage`)

A Starter-tier Mode A reel: live footage upload, 5 shots required. shot-004 has only take 1, whose declared duration fails the spec band; the take-substitution ladder is exhausted with no covering take. Coverage math is internally consistent (5 required, 4 covered, `coverage_complete:false`) — **no phantom coverage**. Routes to `production-coord-agent`.

**Proves:** `reshoot` is Mode-A-exclusive (Decision #3) — the schema `if/then` forces `route_back_to:production-coord-agent` + `failure_code:missing_shot_coverage` on any `reshoot`. AI output is re-genned (`fail`), live footage is re-shot (`reshoot`).
