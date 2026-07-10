# TC-05 — `audio_firewall_breach` → `fail` (route Editor) — GATING

**Branch:** `errorEnvelope` · **verdict:** `fail` · **code:** `audio_firewall_breach` · **route:** `editor-agent`

**The 11th-pass audio-domain existence proof — the GATING fixture.** A banned-entity token
(`sln cuts`) is present in the passthrough `vo_transcript[0].text`. The copy was otherwise
clean through Editor's 10th commit-time pass (which scans committed caption / lower-third /
end-card TEXT) — but the **VO transcript is a distinct surface Editor's pass does not
cover**. Sound's 11th pass is the last net between the spoken word and the mastered audio:
it re-scans every declared `vo_transcript[].text` through the 11-entry canonical firewall
regex and catches the leak **before the audio is mastered**.

`detail` names the leaking VO-transcript field + the banned token + the failing firewall
census (`hits: 1`). Routes to **Editor** (the committed-copy surface is Editor's). These
HC/NPOX tokens are the firewall's BLOCK-list, not a cross-entity reference — ARS is Sequel
Digital scope only.
