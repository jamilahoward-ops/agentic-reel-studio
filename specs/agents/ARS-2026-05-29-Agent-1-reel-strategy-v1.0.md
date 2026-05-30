# Agent #1 — reel-strategy (v1.0 · finalized)

> Exported from Notion (finalized 2026-05-29). Phase 1 core agent of the live REINVENTED pipeline; covers the Strategy role in the
> orchestration blueprint and writes rows into the `ARS · Reel Pipeline` Notion database.

*Phase 1 core agent · Finalized May 29, 2026 from Day-1 draft · Status: ready to run*

## Purpose

The Head of Content. Decides what the next reel should be about, why it matters now, and what success looks like. Wakes on schedule or on demand, scans inputs, drops a brief into the pipeline.

## Inputs

1. **Brand intake** (voice DNA + do-not-do) — the Brand Intake Hub (locked voice + visual system)
2. **Trend Queue** (top brand-relevant trends) — `ARS · Trend Queue` database
3. **Reel Pipeline** (what's posted / coming — dedupe) — `ARS · Reel Pipeline` database
4. Manual overrides ("make one about X")

## Output — creates a Reel Pipeline row

Stage = Idea → Brief. Fields: Reel (topic), brand_id, Hook, Format, Goal, KPI Target, Trend Source, Lever = Lever 3, Approval = Pending.

## Logic

1. Pull top 5 queued trends + recent performers + calendar gaps.
2. Score each candidate 0–10 on: brand fit, timeliness, differentiation, effort/ROI.
3. Highest combined score wins (ties → freshness + KPI alignment).
4. Write the structured brief into a new Reel Pipeline row.

## Guardrails

- Never picks a topic posted in the last 14 days.
- Auto-rejects anything hitting the do-not-do filter.
- If brand-voice confidence < 70%, pause and ask.
- Every row defaults to **Lever 3** — nothing publishes without human approval.

## Hands off to

→ **brief** (expands the pick into a full creative brief).
