#!/usr/bin/env python3
"""
Sound Agent — bundle validation harness (dry-run, $0, no engine, no DSP, no decode,
no LUFS measurement, no network, no LLM).

Validates:
  1. Both schemas compile under the JSON Schema Draft 2020-12 meta-schema.
  2. All 5 fixture input.json validate against input.schema.json.
  3. All 5 fixture expected_output.json validate against output.schema.json
     (TC-01/02 -> successAudioSpec; TC-03/04/05 -> errorEnvelope).
  4. Adversarial guards: the structural promises the SPEC makes are enforced by
     the schema — the SECOND fleet agent (after Editor) to carry only two verdicts
     (audio_ready | fail, NO revise), the zero-false-audio-ready const gates, the
     SPLIT Ingest-routed asset codes (vo_track_missing + audio_asset_unresolved kept
     SEPARATE — the deliberate opposite of Editor's single folded asset_unresolved),
     the FOLDED spec_fidelity_breach (route back to Editor), the mode-blind const,
     audio_processed const false + finish_mode const human_in_the_loop, recommend-
     don't-process const, slot-11 if/then, parent_chain held additively (10-tuple),
     and the TC-01/TC-02 mode-blind finish-convergence proof (THREE stages deep).

The Sound Agent calls NO generative engine, processes NO waveform, decodes NO audio,
and measures NO loudness, so this harness is purely structural: meta-schema + fixture
conformance. $0 spent.

Run:  python3 validate.py
Exit code 0 = all green.
"""
import json, os, sys, copy
from jsonschema import Draft202012Validator
from jsonschema.validators import validator_for

HERE = os.path.dirname(os.path.abspath(__file__))
SCH = os.path.join(HERE, "schemas")
TC = os.path.join(HERE, "test-cases")

PASS = 0
FAIL = 0

def ok(msg):
    global PASS; PASS += 1; print(f"  PASS  {msg}")

def bad(msg):
    global FAIL; FAIL += 1; print(f"  FAIL  {msg}")

def load(p):
    with open(p) as f:
        return json.load(f)

def is_valid(schema, inst):
    v = Draft202012Validator(schema)
    return next(iter(v.iter_errors(inst)), None) is None

def first_error(schema, inst):
    v = Draft202012Validator(schema)
    e = next(iter(v.iter_errors(inst)), None)
    return None if e is None else f"{list(e.path)}: {e.message}"

def reject(label, schema, inst):
    if is_valid(schema, inst):
        bad(f"{label} — schema ACCEPTED an instance it must reject")
    else:
        ok(f"{label} — rejected")

def accept(label, schema, inst):
    e = first_error(schema, inst)
    ok(f"{label} — accepted") if e is None else bad(f"{label} -> {e}")

# ---------------------------------------------------------------- 1. meta-schema
print("== 1. Schemas compile under Draft 2020-12 meta-schema ==")
in_schema = load(os.path.join(SCH, "input.schema.json"))
out_schema = load(os.path.join(SCH, "output.schema.json"))
for name, sch in (("input.schema.json", in_schema), ("output.schema.json", out_schema)):
    cls = validator_for(sch)
    try:
        cls.check_schema(sch)
        ok(f"{name} is a valid Draft 2020-12 schema ({cls.__name__})")
    except Exception as e:
        bad(f"{name} meta-schema error: {e}")

# ---------------------------------------------------------------- 2/3. fixtures
print("\n== 2/3. Fixture input + expected_output validation ==")
CASES = [
    ("case-01-mode-a-origin-pro-audio-ready",   "successAudioSpec"),
    ("case-02-mode-c-enterprise-audio-ready",   "successAudioSpec"),
    ("case-03-audio-marker-out-of-range-fail",  "errorEnvelope"),
    ("case-04-vo-track-missing-fail",           "errorEnvelope"),
    ("case-05-audio-firewall-breach-fail",      "errorEnvelope"),
]
fixtures = {}
for case, expect_branch in CASES:
    inp = load(os.path.join(TC, case, "input.json"))
    out = load(os.path.join(TC, case, "expected_output.json"))
    fixtures[case] = (inp, out)
    e = first_error(in_schema, inp)
    ok(f"{case}/input.json valid") if e is None else bad(f"{case}/input.json -> {e}")
    e = first_error(out_schema, out)
    ok(f"{case}/expected_output.json valid") if e is None else bad(f"{case}/expected_output.json -> {e}")
    if out.get("output_type") != expect_branch:
        bad(f"{case} expected branch {expect_branch}, got {out.get('output_type')}")
    else:
        ok(f"{case} -> {expect_branch} branch as expected")

# ---------------------------------------------------------------- 4. adversarial
print("\n== 4. Adversarial guards (schema must REJECT these) ==")
in01, out01 = fixtures["case-01-mode-a-origin-pro-audio-ready"]   # audio_ready
in02, out02 = fixtures["case-02-mode-c-enterprise-audio-ready"]   # audio_ready
in03, out03 = fixtures["case-03-audio-marker-out-of-range-fail"]  # fail (marker)
in04, out04 = fixtures["case-04-vo-track-missing-fail"]           # fail (vo track)
in05, out05 = fixtures["case-05-audio-firewall-breach-fail"]      # fail (firewall)

# false-audio-ready: an audio_ready carrying a failing HARD conform bool must be rejected (const true)
fc = copy.deepcopy(out01); fc["audio_conform_check"]["vo_track_resolved"] = False
reject("false-audio-ready (audio_ready with vo_track_resolved=false)", out_schema, fc)

fmb0 = copy.deepcopy(out01); fmb0["audio_conform_check"]["music_bed_resolved"] = False
reject("audio_ready with music_bed_resolved=false", out_schema, fmb0)

fmk = copy.deepcopy(out01); fmk["audio_conform_check"]["all_markers_in_timeline"] = False
reject("audio_ready with all_markers_in_timeline=false", out_schema, fmk)

flt = copy.deepcopy(out01); flt["audio_conform_check"]["loudness_target_in_spec"] = False
reject("audio_ready with loudness_target_in_spec=false", out_schema, flt)

# audio_ready with a failing spec-fidelity bool must be rejected (const true)
ff = copy.deepcopy(out01); ff["spec_fidelity_check"]["vo_transcript_byte_faithful"] = False
reject("audio_ready with vo_transcript_byte_faithful=false", out_schema, ff)

feh = copy.deepcopy(out01); feh["spec_fidelity_check"]["edl_evidence_hash_verified"] = False
reject("audio_ready with edl_evidence_hash_verified=false (tamper)", out_schema, feh)

# audio_ready with an 11th-pass firewall hit must be rejected (hits const 0)
fh = copy.deepcopy(out01); fh["audio_firewall_pass_11"]["hits"] = 1
reject("audio_ready with 11th-pass firewall hits>0", out_schema, fh)

fst = copy.deepcopy(out01); fst["audio_firewall_pass_11"]["status"] = "fail"
reject("audio_ready with firewall status='fail'", out_schema, fst)

# out-of-band total_timeline_ms must be rejected (45000..75000)
fdo = copy.deepcopy(out01); fdo["audio_conform_check"]["total_timeline_ms"] = 90000
reject("audio_ready with total_timeline_ms out of the 45-75s band", out_schema, fdo)

# duration_in_band=false must be rejected (const true)
fd = copy.deepcopy(out01); fd["audio_conform_check"]["duration_in_band"] = False
reject("audio_ready with duration_in_band=false", out_schema, fd)

# wrong loudness const must be rejected (primary const '-14 LUFS (IG/TT)')
fl = copy.deepcopy(out01); fl["audio_spec"]["loudness_target"]["primary"] = "-16 LUFS (YT)"
reject("audio_spec loudness primary != '-14 LUFS (IG/TT)' const", out_schema, fl)

# wrong true-peak const must be rejected (const -1.0)
ftp = copy.deepcopy(out01); ftp["audio_spec"]["loudness_target"]["true_peak_ceiling_dbtp"] = -2.0
reject("audio_spec true_peak_ceiling_dbtp != -1.0 const", out_schema, ftp)

# music bed not at t0 must be rejected (at_ms const 0)
fmb = copy.deepcopy(out01); fmb["audio_spec"]["music_bed"]["at_ms"] = 500
reject("audio_spec.music_bed.at_ms != 0 const (bed lays at t0)", out_schema, fmb)

# a non-relative asset_uri in the music bed must be rejected (Hard Rule inherit)
fu = copy.deepcopy(out01); fu["audio_spec"]["music_bed"]["asset_uri"] = "https://cdn.example.com/bed.mp3"
reject("music_bed with absolute (non-ars://) asset_uri", out_schema, fu)

# mode-blind violation: production_mode_read=true must be rejected (const false)
fmbr = copy.deepcopy(out01); fmbr["mode_blind_confirm"]["production_mode_read"] = True
reject("mode_blind_confirm.production_mode_read=true (convergence break)", out_schema, fmbr)

fcons = copy.deepcopy(out01); fcons["mode_blind_confirm"]["consumed"] = "mode_a_edl"
reject("mode_blind_confirm.consumed != 'mode_agnostic_edl' const", out_schema, fcons)

# audio_processed=true (root finish_target) must be rejected (const false — forged-provenance guard)
fap = copy.deepcopy(out01); fap["finish_target"]["audio_processed"] = True
reject("finish_target.audio_processed=true (forged-provenance guard)", out_schema, fap)

# audio_processed=true (metadata mirror) must be rejected (const false)
fap2 = copy.deepcopy(out01); fap2["metadata"]["audio_processed"] = True
reject("metadata.audio_processed=true (forged-provenance guard)", out_schema, fap2)

# finish_mode != human_in_the_loop must be rejected
ffm = copy.deepcopy(out01); ffm["finish_target"]["finish_mode"] = "automated"
reject("finish_target.finish_mode='automated' (v1.1 reserved — not v1.0)", out_schema, ffm)

# human_review_required:false must be rejected (recommend-don't-process)
fhr = copy.deepcopy(out01); fhr["human_review_required"] = False
reject("human_review_required:false on audio_ready", out_schema, fhr)

# loudness_variants_specced must be const 1 in v1.0
fvc = copy.deepcopy(out01); fvc["tier_richness_echo"]["loudness_variants_specced"] = 2
reject("tier_richness_echo.loudness_variants_specced != 1 (v1.0 primary master only)", out_schema, fvc)

# variant_masters must be empty in v1.0 (maxItems 0)
fvm = copy.deepcopy(out01); fvm["variant_masters"] = [{"target": "-16 LUFS (YT)"}]
reject("variant_masters non-empty (v1.0 maxItems 0)", out_schema, fvm)

# ---------------------------------------------------------------- 4b. the 2-verdict model
print("\n== 4b. 2-verdict model (audio_ready | fail — the SECOND fleet agent to carry only two verdicts) ==")
# 'revise' is NOT a valid Sound verdict (the executor is deterministic — inherits Editor's posture)
rev = copy.deepcopy(out01); rev["verdict"] = "revise"
reject("verdict 'revise' on success branch (Sound inherits Editor's two-verdict posture)", out_schema, rev)
rev2 = copy.deepcopy(out03); rev2["verdict"] = "revise"
reject("verdict 'revise' on error branch (no third verdict anywhere)", out_schema, rev2)
# 'hold' / 'reshoot' are not Sound verdicts either
hold = copy.deepcopy(out03); hold["verdict"] = "hold"
reject("verdict 'hold' (not a Sound verdict)", out_schema, hold)
# the success branch verdict is pinned to audio_ready
vwrong = copy.deepcopy(out01); vwrong["verdict"] = "fail"
reject("successAudioSpec with verdict 'fail' (branch/verdict mismatch)", out_schema, vwrong)
# the error branch verdict is pinned to fail
ewrong = copy.deepcopy(out03); ewrong["verdict"] = "audio_ready"
reject("errorEnvelope with verdict 'audio_ready' (branch/verdict mismatch)", out_schema, ewrong)

# ---------------------------------------------------------------- 4c. codes + SPLIT/folded routing
print("\n== 4c. errorEnvelope codes + SPLIT asset routing (route-back by destination, slot-11, halts) ==")
# vo_track_missing MUST route to ingest-agent (SPLIT code — VO side)
accept("vo_track_missing -> ingest-agent (SPLIT: the VO voice track)", out_schema, out04)
vt_wrong = copy.deepcopy(out04); vt_wrong["route_back_to"] = "editor-agent"
reject("vo_track_missing with wrong route (must be ingest-agent)", out_schema, vt_wrong)

# audio_asset_unresolved is the OTHER SPLIT code — also to ingest-agent (music-bed side)
aau = copy.deepcopy(out04); aau["failure_code"] = "audio_asset_unresolved"
accept("audio_asset_unresolved -> ingest-agent (SPLIT: the music bed — kept SEPARATE, D8)", out_schema, aau)
aau_wrong = copy.deepcopy(aau); aau_wrong["route_back_to"] = "editor-agent"
reject("audio_asset_unresolved with wrong route (must be ingest-agent)", out_schema, aau_wrong)

# the four editor-routed codes must route to editor-agent
accept("audio_marker_out_of_range -> editor-agent", out_schema, out03)
accept("audio_firewall_breach -> editor-agent", out_schema, out05)
mk_wrong = copy.deepcopy(out03); mk_wrong["route_back_to"] = "ingest-agent"
reject("audio_marker_out_of_range with wrong route (must be editor-agent)", out_schema, mk_wrong)
lt = copy.deepcopy(out03); lt["failure_code"] = "loudness_target_out_of_spec"
accept("loudness_target_out_of_spec -> editor-agent", out_schema, lt)
sf = copy.deepcopy(out03); sf["failure_code"] = "spec_fidelity_breach"
accept("spec_fidelity_breach -> editor-agent (FOLDED: hash-tamper + duration + mix/VO deviation)", out_schema, sf)
sf_wrong = copy.deepcopy(sf); sf_wrong["route_back_to"] = "ingest-agent"
reject("spec_fidelity_breach with wrong route (must be editor-agent)", out_schema, sf_wrong)

# slot-11 sound_agent_failed: valid form (attempts 2, route null)
slot11 = copy.deepcopy(out03)
slot11["failure_code"] = "sound_agent_failed"; slot11["attempts"] = 2
slot11["route_back_to"] = None; slot11["failed_check_id"] = 11
accept("valid slot-11 sound_agent_failed (attempts 2, route null)", out_schema, slot11)
s11a = copy.deepcopy(slot11); s11a["attempts"] = 1
reject("sound_agent_failed with attempts=1 (if/then requires 2)", out_schema, s11a)
s11r = copy.deepcopy(slot11); s11r["attempts"] = 2; s11r["route_back_to"] = "ingest-agent"
reject("sound_agent_failed with non-null route_back_to", out_schema, s11r)

# the three halt codes must route null
for hc, cid in (("upstream_edl_not_ready", 1), ("upstream_not_success", 2), ("audio_lineage_failure", 10)):
    h = copy.deepcopy(out03); h["failure_code"] = hc; h["failed_check_id"] = cid; h["route_back_to"] = "ingest-agent"
    reject(f"{hc} with non-null route_back_to (precondition/forensic halt)", out_schema, h)
    hok = copy.deepcopy(out03); hok["failure_code"] = hc; hok["failed_check_id"] = cid; hok["route_back_to"] = None
    accept(f"{hc} with route null", out_schema, hok)

# a foreign failure_code must be rejected (an Editor code, not Sound's)
uc = copy.deepcopy(out03); uc["failure_code"] = "edl_firewall_breach"
reject("foreign failure_code 'edl_firewall_breach' (Editor's, not Sound's)", out_schema, uc)

# ---------------------------------------------------------------- 4d. parent_chain (10-tuple held additively)
print("\n== 4d. parent_chain held additively (output minItems 5, maxItems 10) ==")
ten = copy.deepcopy(out01)  # already a 10-tuple
accept("output parent_chain 10-tuple (Sound append)", out_schema, ten)
for n in (9, 8, 7, 6, 5):
    t = copy.deepcopy(out01); t["metadata"]["parent_chain"] = t["metadata"]["parent_chain"][:n]
    accept(f"output parent_chain {n}-tuple (held additively)", out_schema, t)
four = copy.deepcopy(out01); four["metadata"]["parent_chain"] = four["metadata"]["parent_chain"][:4]
reject("output parent_chain 4-tuple (below the additive floor)", out_schema, four)
eleven = copy.deepcopy(out01)
eleven["metadata"]["parent_chain"] = out01["metadata"]["parent_chain"] + [out01["reel_ref"]["audio_spec_id"]]
reject("output parent_chain 11-tuple (above maxItems 10)", out_schema, eleven)
# input held at maxItems 9
nine_in = copy.deepcopy(in01)
accept("input parent_chain 9-tuple inbound", in_schema, nine_in)
ten_in = copy.deepcopy(in01)
ten_in["metadata"]["parent_chain"] = ten_in["metadata"]["parent_chain"] + [in01["metadata"]["parent_chain"][8]]
reject("input parent_chain 10-tuple (inbound maxItems 9)", in_schema, ten_in)

# ---------------------------------------------------------------- 4e. input guards
print("\n== 4e. Input guards (precondition is a runtime halt, NOT a schema reject) ==")
# a non-edl_ready EDL with no sign-off is a VALID object (runtime halt upstream_edl_not_ready)
notready = copy.deepcopy(in01); notready["edl"]["verdict"] = "fail"
accept("input fail-verdict EDL (valid object — runtime halt upstream_edl_not_ready, not schema reject)", in_schema, notready)
# a consumed errorEnvelope EDL is a VALID object (runtime halt upstream_not_success)
errin = copy.deepcopy(in01); errin["edl"]["output_type"] = "errorEnvelope"
accept("input errorEnvelope EDL (valid object — runtime halt upstream_not_success)", in_schema, errin)
# an absolute asset_uri in the music_event must be rejected (Hard Rule inherit)
absuri = copy.deepcopy(in01); absuri["edl"]["music_event"]["asset_uri"] = "https://cdn.example.com/x.mp3"
reject("input music_event with absolute (non-ars://) asset_uri", in_schema, absuri)
# a non-cut transition on an event must be rejected (const cut)
badtr = copy.deepcopy(in01); badtr["edl"]["events"][0]["transition"] = "cross-dissolve"
reject("input event transition != 'cut' const", in_schema, badtr)
# production_mode is REQUIRED present (carried for audit lineage even though never read)
nomode = copy.deepcopy(in01); del nomode["metadata"]["production_mode"]
reject("input missing production_mode (required-present for audit lineage)", in_schema, nomode)

# ---------------------------------------------------------------- 4f. convergence proof
print("\n== 4f. TC-01/TC-02 mode-blind finish-convergence proof (THREE stages deep) ==")
_, o1 = fixtures["case-01-mode-a-origin-pro-audio-ready"]
_, o2 = fixtures["case-02-mode-c-enterprise-audio-ready"]
same = all(o1[k] == o2[k] for k in
           ["audio_spec", "audio_conform_check", "spec_fidelity_check",
            "audio_firewall_pass_11", "mode_blind_confirm", "finish_target"])
if same and o1["metadata"]["production_mode"] != o2["metadata"]["production_mode"]:
    ok("TC-01 (Mode A) vs TC-02 (Mode C): finished audio_spec byte-shape-identical despite different origin mode")
else:
    bad("TC-01/TC-02 convergence proof broken (finish paths differ or modes equal)")
if o1["mode_blind_confirm"]["production_mode_read"] is False and o2["mode_blind_confirm"]["production_mode_read"] is False:
    ok("both convergence fixtures attest production_mode_read:false")
else:
    bad("a convergence fixture failed the mode-blind self-attestation")

# ---------------------------------------------------------------- 4g. TC-05 gating fixture
print("\n== 4g. TC-05 gating fixture (11th-pass audio-domain firewall) ==")
blob = json.dumps(in05).lower()
if "sln" in blob:
    ok("TC-05 input carries the injected banned token in the passthrough VO transcript")
else:
    bad("TC-05 input is missing the injected banned token")
if out05["failure_code"] == "audio_firewall_breach" and out05["failed_check_id"] == 8 \
        and out05["route_back_to"] == "editor-agent" \
        and out05["detail"]["audio_firewall_pass_11"]["hits"] == 1:
    ok("TC-05 expected_output = audio_firewall_breach (Check #8, hits 1, route editor — the last audio checkpoint before Motion)")
else:
    bad("TC-05 expected_output does not encode the 11th-pass audio-domain catch")

# ---------------------------------------------------------------- summary
print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
sys.exit(1 if FAIL else 0)
