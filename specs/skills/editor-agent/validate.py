#!/usr/bin/env python3
"""
Editor Agent — bundle validation harness (dry-run, $0, no engine, no render, no network, no LLM).

Validates:
  1. Both schemas compile under the JSON Schema Draft 2020-12 meta-schema.
  2. All 5 fixture input.json validate against input.schema.json.
  3. All 5 fixture expected_output.json validate against output.schema.json
     (TC-01/02 -> successEdl; TC-03/04/05 -> errorEnvelope).
  4. Adversarial guards: the structural promises the SPEC makes are enforced by
     the schema — the FIRST fleet agent to DROP a predecessor verdict (two-verdict
     edl_ready | fail, NO revise), the zero-false-edl-ready const gates, the FOLDED
     route-back codes (asset_unresolved -> Ingest; plan_fidelity_breach -> Edit
     Director), the mode-blind const, render_dispatched const false + conform_mode
     const human_in_the_loop, recommend-don't-render const, slot-11 if/then,
     parent_chain held additively (9-tuple), and the TC-01/TC-02 mode-blind
     convergence proof (two stages deep).

The Editor Agent calls NO generative engine and renders NO media, so this harness
is purely structural: meta-schema + fixture conformance. $0 spent.

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
    ("case-01-mode-a-origin-pro-edl-ready",   "successEdl"),
    ("case-02-mode-c-enterprise-edl-ready",   "successEdl"),
    ("case-03-timecode-out-of-range-fail",    "errorEnvelope"),
    ("case-04-asset-unresolved-fail",         "errorEnvelope"),
    ("case-05-commit-firewall-breach-fail",   "errorEnvelope"),
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
in01, out01 = fixtures["case-01-mode-a-origin-pro-edl-ready"]   # edl_ready
in02, out02 = fixtures["case-02-mode-c-enterprise-edl-ready"]   # edl_ready
in03, out03 = fixtures["case-03-timecode-out-of-range-fail"]    # fail (timecode)
in04, out04 = fixtures["case-04-asset-unresolved-fail"]         # fail (asset)
in05, out05 = fixtures["case-05-commit-firewall-breach-fail"]   # fail (firewall)

# false-edl-ready: an edl_ready carrying a failing HARD conform bool must be rejected (const true)
fc = copy.deepcopy(out01); fc["conform_check"]["timeline_gap_free"] = False
reject("false-edl-ready (edl_ready with timeline_gap_free=false)", out_schema, fc)

# edl_ready with all_events_bounded=false must be rejected (const true)
fb = copy.deepcopy(out01); fb["conform_check"]["all_events_bounded_by_declared_duration"] = False
reject("edl_ready with all_events_bounded_by_declared_duration=false", out_schema, fb)

# edl_ready with a failing plan-fidelity bool must be rejected (const true)
ff = copy.deepcopy(out01); ff["plan_fidelity_check"]["caption_copy_byte_faithful"] = False
reject("edl_ready with caption_copy_byte_faithful=false", out_schema, ff)

# edl_ready with a 10th-pass firewall hit must be rejected (hits const 0)
fh = copy.deepcopy(out01); fh["edl_firewall_pass_10"]["hits"] = 1
reject("edl_ready with commit-time firewall hits>0", out_schema, fh)

# out-of-band total_timeline_ms must be rejected (45000..75000)
fdo = copy.deepcopy(out01); fdo["conform_check"]["total_timeline_ms"] = 90000
reject("edl_ready with total_timeline_ms out of the 45-75s band", out_schema, fdo)

# duration_in_band=false must be rejected (const true)
fd = copy.deepcopy(out01); fd["conform_check"]["duration_in_band"] = False
reject("edl_ready with duration_in_band=false", out_schema, fd)

# a caption event over 22 chars must be rejected
fcap = copy.deepcopy(out01); fcap["edl"]["caption_events"][0]["text"] = "this caption is far too long for the brand rule"
reject("caption event >22 chars", out_schema, fcap)

# a non-cut transition must be rejected (const cut)
ft = copy.deepcopy(out01); ft["edl"]["events"][0]["transition"] = "cross-dissolve"
reject("event transition != 'cut' const (hard-cuts-only at the EDL layer)", out_schema, ft)

# an all-caps / non-lowercase lower-third must be rejected (case const lowercase)
flc = copy.deepcopy(out01); flc["edl"]["lower_third_events"][0]["case"] = "uppercase"
reject("lower-third event case != lowercase", out_schema, flc)

# wrong end-card hold must be rejected (const 1500)
feh = copy.deepcopy(out01); feh["edl"]["end_card_event"]["hold_ms"] = 2000
reject("end_card_event.hold_ms != 1500 const", out_schema, feh)

# wrong format const must be rejected (frame_rate const 30)
ffr = copy.deepcopy(out01); ffr["edl"]["frame_rate"] = 24
reject("edl.frame_rate != 30 const", out_schema, ffr)

# wrong aspect const must be rejected (9:16)
fasp = copy.deepcopy(out01); fasp["edl"]["aspect"] = "16:9"
reject("edl.aspect != 9:16 const", out_schema, fasp)

# mode-blind violation: production_mode_read=true must be rejected (const false)
fmb = copy.deepcopy(out01); fmb["mode_blind_confirm"]["production_mode_read"] = True
reject("mode_blind_confirm.production_mode_read=true (convergence break)", out_schema, fmb)

# render_dispatched=true (root render_target) must be rejected (const false — forged-provenance guard)
frd = copy.deepcopy(out01); frd["render_target"]["render_dispatched"] = True
reject("render_target.render_dispatched=true (forged-provenance guard)", out_schema, frd)

# render_dispatched=true (metadata mirror) must be rejected (const false)
frd2 = copy.deepcopy(out01); frd2["metadata"]["render_dispatched"] = True
reject("metadata.render_dispatched=true (forged-provenance guard)", out_schema, frd2)

# conform_mode != human_in_the_loop must be rejected
fcm = copy.deepcopy(out01); fcm["render_target"]["conform_mode"] = "automated"
reject("render_target.conform_mode='automated' (v1.1 reserved — not v1.0)", out_schema, fcm)

# human_review_required:false must be rejected (recommend-don't-render)
fhr = copy.deepcopy(out01); fhr["human_review_required"] = False
reject("human_review_required:false on edl_ready", out_schema, fhr)

# a non-relative asset_uri in an event must be rejected (Hard Rule inherit)
fu = copy.deepcopy(out01); fu["edl"]["events"][0]["asset_uri"] = "https://cdn.example.com/shot-001.mp4"
reject("event with absolute (non-ars://) asset_uri", out_schema, fu)

# variants_conformed must be const 1 in v1.0
fvc = copy.deepcopy(out01); fvc["tier_richness_echo"]["variants_conformed"] = 2
reject("tier_richness_echo.variants_conformed != 1 (v1.0 primary-only)", out_schema, fvc)

# ---------------------------------------------------------------- 4b. the 2-verdict model
print("\n== 4b. 2-verdict model (edl_ready | fail — the FIRST fleet agent to DROP a predecessor verdict) ==")
# 'revise' is NOT a valid Editor verdict (the executor is deterministic — the defining divergence)
rev = copy.deepcopy(out01); rev["verdict"] = "revise"
reject("verdict 'revise' on success branch (Editor dropped Edit Director's third verdict)", out_schema, rev)
rev2 = copy.deepcopy(out03); rev2["verdict"] = "revise"
reject("verdict 'revise' on error branch (no third verdict anywhere)", out_schema, rev2)
# 'hold' / 'reshoot' are not Editor verdicts either
hold = copy.deepcopy(out03); hold["verdict"] = "hold"
reject("verdict 'hold' (not an Editor verdict)", out_schema, hold)
rs = copy.deepcopy(out03); rs["verdict"] = "reshoot"
reject("verdict 'reshoot' (not an Editor verdict)", out_schema, rs)
# the success branch verdict is pinned to edl_ready
vwrong = copy.deepcopy(out01); vwrong["verdict"] = "fail"
reject("successEdl with verdict 'fail' (branch/verdict mismatch)", out_schema, vwrong)

# ---------------------------------------------------------------- 4c. codes + folded routing
print("\n== 4c. errorEnvelope codes + FOLDED routing (route-back by destination, slot-11, halts) ==")
# asset_unresolved MUST route to ingest-agent (folded resolution code)
accept("asset_unresolved -> ingest-agent (folded: cut-asset/music-bed/voice-track)", out_schema, out04)
au_wrong = copy.deepcopy(out04); au_wrong["route_back_to"] = "edit-director-agent"
reject("asset_unresolved with wrong route (must be ingest-agent)", out_schema, au_wrong)

# the five edit-director-routed codes must route to edit-director-agent
accept("timecode_out_of_range -> edit-director-agent", out_schema, out03)
accept("edl_firewall_breach -> edit-director-agent", out_schema, out05)
tc_wrong = copy.deepcopy(out03); tc_wrong["route_back_to"] = "ingest-agent"
reject("timecode_out_of_range with wrong route (must be edit-director-agent)", out_schema, tc_wrong)
pf = copy.deepcopy(out03); pf["failure_code"] = "plan_fidelity_breach"
accept("plan_fidelity_breach -> edit-director-agent (folded: hash-tamper + copy deviation)", out_schema, pf)
pf_wrong = copy.deepcopy(pf); pf_wrong["route_back_to"] = "ingest-agent"
reject("plan_fidelity_breach with wrong route (must be edit-director-agent)", out_schema, pf_wrong)

# slot-11 editor_agent_failed: valid form (attempts 2, route null)
slot11 = copy.deepcopy(out03)
slot11["failure_code"] = "editor_agent_failed"; slot11["attempts"] = 2
slot11["route_back_to"] = None; slot11["failed_check_id"] = 11
accept("valid slot-11 editor_agent_failed (attempts 2, route null)", out_schema, slot11)
s11a = copy.deepcopy(slot11); s11a["attempts"] = 1
reject("editor_agent_failed with attempts=1 (if/then requires 2)", out_schema, s11a)
s11r = copy.deepcopy(slot11); s11r["attempts"] = 2; s11r["route_back_to"] = "ingest-agent"
reject("editor_agent_failed with non-null route_back_to", out_schema, s11r)

# the three halt codes must route null
for hc, cid in (("upstream_plan_not_ready", 1), ("upstream_not_success", 2), ("edl_lineage_failure", 10)):
    h = copy.deepcopy(out03); h["failure_code"] = hc; h["failed_check_id"] = cid; h["route_back_to"] = "ingest-agent"
    reject(f"{hc} with non-null route_back_to (precondition/forensic halt)", out_schema, h)
    hok = copy.deepcopy(out03); hok["failure_code"] = hc; hok["failed_check_id"] = cid; hok["route_back_to"] = None
    accept(f"{hc} with route null", out_schema, hok)

# a foreign failure_code must be rejected (an Edit Director code, not Editor's)
uc = copy.deepcopy(out03); uc["failure_code"] = "duration_envelope_breach"
reject("foreign failure_code 'duration_envelope_breach' (Edit Director's, not Editor's)", out_schema, uc)

# ---------------------------------------------------------------- 4d. parent_chain (9-tuple held additively)
print("\n== 4d. parent_chain held additively (output minItems 5, maxItems 9) ==")
nine = copy.deepcopy(out01)  # already a 9-tuple
accept("output parent_chain 9-tuple (Editor append)", out_schema, nine)
for n in (8, 7, 6, 5):
    t = copy.deepcopy(out01); t["metadata"]["parent_chain"] = t["metadata"]["parent_chain"][:n]
    accept(f"output parent_chain {n}-tuple (held additively)", out_schema, t)
four = copy.deepcopy(out01); four["metadata"]["parent_chain"] = four["metadata"]["parent_chain"][:4]
reject("output parent_chain 4-tuple (below the additive floor)", out_schema, four)
ten = copy.deepcopy(out01); ten["metadata"]["parent_chain"] = out01["metadata"]["parent_chain"] + [out01["reel_ref"]["edl_id"]]
reject("output parent_chain 10-tuple (above maxItems 9)", out_schema, ten)
# input held at maxItems 8
eight_in = copy.deepcopy(in01)
accept("input parent_chain 8-tuple inbound", in_schema, eight_in)
nine_in = copy.deepcopy(in01); nine_in["metadata"]["parent_chain"] = nine_in["metadata"]["parent_chain"] + [in01["metadata"]["parent_chain"][7]]
reject("input parent_chain 9-tuple (inbound maxItems 8)", in_schema, nine_in)

# ---------------------------------------------------------------- 4e. input guards
print("\n== 4e. Input guards (precondition is a runtime halt, NOT a schema reject) ==")
# a non-plan_ready plan with no sign-off is a VALID object (runtime halt upstream_plan_not_ready)
notready = copy.deepcopy(in01); notready["edit_plan"]["verdict"] = "revise"
accept("input revise plan (valid object — runtime halt upstream_plan_not_ready, not schema reject)", in_schema, notready)
# a consumed errorEnvelope plan is a VALID object (runtime halt upstream_not_success)
errin = copy.deepcopy(in01); errin["edit_plan"]["output_type"] = "errorEnvelope"
accept("input errorEnvelope plan (valid object — runtime halt upstream_not_success)", in_schema, errin)
# an absolute asset_uri in cut_order must be rejected (Hard Rule inherit)
absuri = copy.deepcopy(in01); absuri["edit_plan"]["cut_order"][0]["asset_uri"] = "https://cdn.example.com/x.mp4"
reject("input cut_order with absolute (non-ars://) asset_uri", in_schema, absuri)
# transitions must be the hard-cuts-only const
badtr = copy.deepcopy(in01); badtr["edit_plan"]["transitions"] = "cross-fade"
reject("input transitions != 'hard-cuts-only' const", in_schema, badtr)
# production_mode is REQUIRED present (carried for audit lineage even though never read)
nomode = copy.deepcopy(in01); del nomode["metadata"]["production_mode"]
reject("input missing production_mode (required-present for audit lineage)", in_schema, nomode)

# ---------------------------------------------------------------- 4f. convergence proof
print("\n== 4f. TC-01/TC-02 mode-blind convergence proof (two stages deep) ==")
_, o1 = fixtures["case-01-mode-a-origin-pro-edl-ready"]
_, o2 = fixtures["case-02-mode-c-enterprise-edl-ready"]
same = all(o1[k] == o2[k] for k in
           ["edl", "conform_check", "plan_fidelity_check", "edl_firewall_pass_10",
            "mode_blind_confirm", "render_target"])
if same and o1["metadata"]["production_mode"] != o2["metadata"]["production_mode"]:
    ok("TC-01 (Mode A) vs TC-02 (Mode C): conformed EDL byte-shape-identical despite different origin mode")
else:
    bad("TC-01/TC-02 convergence proof broken (conform paths differ or modes equal)")
if o1["mode_blind_confirm"]["production_mode_read"] is False and o2["mode_blind_confirm"]["production_mode_read"] is False:
    ok("both convergence fixtures attest production_mode_read:false")
else:
    bad("a convergence fixture failed the mode-blind self-attestation")

# ---------------------------------------------------------------- 4g. TC-05 gating fixture
print("\n== 4g. TC-05 gating fixture (10th-pass commit-time firewall) ==")
blob = json.dumps(in05)
if '"sln' in blob or 'sln ' in blob:
    ok("TC-05 input carries the injected banned token in the committed caption copy")
else:
    bad("TC-05 input is missing the injected banned token")
if out05["failure_code"] == "edl_firewall_breach" and out05["failed_check_id"] == 9 \
        and out05["route_back_to"] == "edit-director-agent" \
        and out05["detail"]["edl_firewall_pass_10"]["hits"] == 1:
    ok("TC-05 expected_output = edl_firewall_breach (Check #9, hits 1, route edit-director — the last line before pixels)")
else:
    bad("TC-05 expected_output does not encode the 10th-pass commit-time catch")

# ---------------------------------------------------------------- summary
print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
sys.exit(1 if FAIL else 0)
