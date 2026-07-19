#!/usr/bin/env python3
"""
Motion Agent — bundle validation harness (dry-run, $0, no engine, no render,
no compositing, no frame decode, no network, no LLM).

Validates:
  1. Both schemas compile under the JSON Schema Draft 2020-12 meta-schema.
  2. All 5 fixture input.json validate against input.schema.json.
  3. All 5 fixture expected_output.json validate against output.schema.json
     (TC-01/02 -> successMotionSpec; TC-03/04/05 -> errorEnvelope).
  4. Adversarial guards: the structural promises the SPEC makes are enforced by
     the schema — the THIRD fleet agent (after Editor + Sound) to carry only two
     verdicts (motion_ready | fail, NO revise), the zero-false-motion-ready const
     gates, the TWO TYPE-SYSTEM brand-policy encodings (the banned motion tokens
     are enum-excluded AND the all-caps lower-third is const false — both
     UNREPRESENTABLE), the SPLIT resolution codes routed to two different agents
     (v2_edit_unresolved -> Sound, text_asset_unresolved -> Editor), the SPLIT
     brand-policy codes (motion_token_out_of_spec vs typography_out_of_spec), the
     FOLDED spec_fidelity_breach (route Editor), the DUAL upstream-evidence-hash
     verify (the first agent to machine-verify TWO hashes), the mode-blind const,
     motion_processed const false + finish_mode const human_in_the_loop, recommend-
     don't-render const, slot-11 if/then, parent_chain held additively (11-tuple),
     and the TC-01/TC-02 mode-blind finish-convergence proof (FOUR stages deep).

The Motion Agent calls NO generative engine, renders NO graphics, composites NO
frame, and decodes NO video, so this harness is purely structural: meta-schema +
fixture conformance. $0 spent.

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
    ("case-01-mode-a-origin-pro-motion-ready",     "successMotionSpec"),
    ("case-02-mode-c-enterprise-motion-ready",     "successMotionSpec"),
    ("case-03-caption-reveal-out-of-range-fail",   "errorEnvelope"),
    ("case-04-v2-edit-unresolved-fail",            "errorEnvelope"),
    ("case-05-typography-firewall-breach-fail",    "errorEnvelope"),
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

in01, out01 = fixtures["case-01-mode-a-origin-pro-motion-ready"]     # motion_ready
in02, out02 = fixtures["case-02-mode-c-enterprise-motion-ready"]     # motion_ready
in03, out03 = fixtures["case-03-caption-reveal-out-of-range-fail"]   # fail (marker)
in04, out04 = fixtures["case-04-v2-edit-unresolved-fail"]            # fail (v2 edit)
in05, out05 = fixtures["case-05-typography-firewall-breach-fail"]    # fail (firewall)

# ---------------------------------------------------------------- 4. adversarial (const gates)
print("\n== 4. Adversarial guards — success-branch const gates (schema must REJECT) ==")
for field in ["v2_edit_resolved", "all_text_fields_resolved", "all_markers_in_timeline",
              "reveal_cadence_in_spec", "motion_tokens_in_brand_set", "duration_in_band"]:
    f = copy.deepcopy(out01); f["motion_conform_check"][field] = False
    reject(f"motion_ready with motion_conform_check.{field}=false", out_schema, f)

fdo = copy.deepcopy(out01); fdo["motion_conform_check"]["total_timeline_ms"] = 90000
reject("motion_ready with total_timeline_ms out of the 45-75s band", out_schema, fdo)

for field in ["caption_text_byte_faithful", "lower_third_text_byte_faithful",
              "end_card_matches_brand_const", "timeline_duration_matches_edl",
              "audio_spec_evidence_hash_verified", "edl_evidence_hash_verified"]:
    f = copy.deepcopy(out01); f["spec_fidelity_check"][field] = False
    reject(f"motion_ready with spec_fidelity_check.{field}=false", out_schema, f)

fh = copy.deepcopy(out01); fh["motion_firewall_pass_12"]["hits"] = 1
reject("motion_ready with 12th-pass firewall hits>0", out_schema, fh)
fst = copy.deepcopy(out01); fst["motion_firewall_pass_12"]["status"] = "breach"
reject("motion_ready with firewall status='breach'", out_schema, fst)
fbv = copy.deepcopy(out01); fbv["motion_self_check"]["banned_vocab_hits"] = 1
reject("motion_ready with motion_self_check.banned_vocab_hits!=0 (const 0)", out_schema, fbv)
fmt = copy.deepcopy(out01); fmt["motion_self_check"]["motion_tokens_applied"] = False
reject("motion_ready with motion_tokens_applied=false", out_schema, fmt)

# recommend-don't-render consts
fap = copy.deepcopy(out01); fap["finish_target"]["motion_processed"] = True
reject("finish_target.motion_processed=true (forged-provenance guard)", out_schema, fap)
fap2 = copy.deepcopy(out01); fap2["metadata"]["motion_processed"] = True
reject("metadata.motion_processed=true (forged-provenance guard)", out_schema, fap2)
ffm = copy.deepcopy(out01); ffm["finish_target"]["finish_mode"] = "automated"
reject("finish_target.finish_mode='automated' (v1.1 reserved — not v1.0)", out_schema, ffm)
fhr = copy.deepcopy(out01); fhr["human_review_required"] = False
reject("human_review_required:false on motion_ready", out_schema, fhr)

# mode-blind convergence break
fmbr = copy.deepcopy(out01); fmbr["mode_blind_confirm"]["production_mode_read"] = True
reject("mode_blind_confirm.production_mode_read=true (convergence break)", out_schema, fmbr)
fcons = copy.deepcopy(out01); fcons["mode_blind_confirm"]["consumed"] = "mode_a_v2_edit"
reject("mode_blind_confirm.consumed != 'mode_agnostic_v2_edit' const", out_schema, fcons)

# tier_richness_echo + variant_masters (v1.0 primary master only)
fvc = copy.deepcopy(out01); fvc["tier_richness_echo"]["aspect_variants_specced"] = 2
reject("tier_richness_echo.aspect_variants_specced != 1 (v1.0 primary master only)", out_schema, fvc)
fpa = copy.deepcopy(out01); fpa["tier_richness_echo"]["primary_aspect"] = "1:1"
reject("tier_richness_echo.primary_aspect != '9:16' const", out_schema, fpa)
fvm = copy.deepcopy(out01); fvm["variant_masters"] = [{"aspect": "1:1"}]
reject("variant_masters non-empty (v1.0 maxItems 0)", out_schema, fvm)

# ---------------------------------------------------------------- 4a. TYPE-SYSTEM brand policy
print("\n== 4a. TYPE-SYSTEM brand-policy encoding (the strongest in the fleet — 2 AND-terms unrepresentable) ==")
fwt = copy.deepcopy(out01); fwt["motion_spec"]["motion_tokens"]["applied"] = ["whip_pan"]
reject("motion_tokens.applied contains banned 'whip_pan' (enum-UNREPRESENTABLE)", out_schema, fwt)
for banned in ("shake", "meme_transition", "trending_transition"):
    f = copy.deepcopy(out01); f["motion_spec"]["motion_tokens"]["applied"] = ["static_hold", banned]
    reject(f"motion_tokens.applied contains banned '{banned}' (enum-UNREPRESENTABLE)", out_schema, f)
fov = copy.deepcopy(out01); fov["motion_spec"]["overlays"][0]["type"] = "whip_pan"
reject("overlay type 'whip_pan' (enum-UNREPRESENTABLE)", out_schema, fov)
fac = copy.deepcopy(out01); fac["motion_spec"]["lower_thirds"][0]["all_caps"] = True
reject("lower_thirds[*].all_caps=true — the all-caps screamer (const-false UNREPRESENTABLE)", out_schema, fac)
fls = copy.deepcopy(out01); fls["motion_spec"]["lower_thirds"][0]["style"] = "uppercase_serif_center"
reject("lower_thirds[*].style non-brand (const violation)", out_schema, fls)
fea = copy.deepcopy(out01); fea["motion_spec"]["motion_tokens"]["ease"] = "300ms bounce"
reject("motion_tokens.ease != '120ms ease-in-out' const", out_schema, fea)
fbp = copy.deepcopy(out01); fbp["motion_spec"]["motion_tokens"]["bounce_policy"] = "spring"
reject("motion_tokens.bounce_policy != 'zero_bounce' const", out_schema, fbp)
frv = copy.deepcopy(out01); frv["motion_spec"]["caption_reveals"][0]["ease"] = "linear_0ms"
reject("caption_reveals[*].ease != 'ease_in_out_120ms' const", out_schema, frv)
frr = copy.deepcopy(out01); frr["motion_spec"]["caption_reveals"][0]["reveal"] = "pop_in"
reject("caption_reveals[*].reveal != 'line_in' const", out_schema, frr)

# reveal_cadence consts
fol = copy.deepcopy(out01); fol["motion_spec"]["reveal_cadence"]["one_line_at_a_time"] = False
reject("reveal_cadence.one_line_at_a_time != true const", out_schema, fol)
fmr = copy.deepcopy(out01); fmr["motion_spec"]["reveal_cadence"]["max_reveals_per_8s"] = 2
reject("reveal_cadence.max_reveals_per_8s != 1 const", out_schema, fmr)
fbc = copy.deepcopy(out01); fbc["motion_spec"]["reveal_cadence"]["brand_cadence"] = "generic_v1"
reject("reveal_cadence.brand_cadence != 'reinvented_v3' const", out_schema, fbc)

# end-card brand consts (Brand-Voice Intake §8)
fet = copy.deepcopy(out01); fet["motion_spec"]["end_card"]["text"] = "REINVENTED - build on purpose."
reject("end_card.text ascii-hyphen drift (const requires em dash)", out_schema, fet)
fef = copy.deepcopy(out01); fef["motion_spec"]["end_card"]["font"] = "script"
reject("end_card.font != 'serif' const (script/decorative banned)", out_schema, fef)
feb = copy.deepcopy(out01); feb["motion_spec"]["end_card"]["bg"] = "black"
reject("end_card.bg != 'ivory' const", out_schema, feb)
feh = copy.deepcopy(out01); feh["motion_spec"]["end_card"]["hold_ms"] = 3000
reject("end_card.hold_ms != 1500 const", out_schema, feh)

# ---------------------------------------------------------------- 4b. the 2-verdict model
print("\n== 4b. 2-verdict model (motion_ready | fail — the THIRD fleet agent to carry only two verdicts) ==")
rev = copy.deepcopy(out01); rev["verdict"] = "revise"
reject("verdict 'revise' on success branch (Motion inherits Editor+Sound two-verdict posture)", out_schema, rev)
rev2 = copy.deepcopy(out03); rev2["verdict"] = "revise"
reject("verdict 'revise' on error branch (no third verdict anywhere)", out_schema, rev2)
hold = copy.deepcopy(out03); hold["verdict"] = "hold"
reject("verdict 'hold' (not a Motion verdict)", out_schema, hold)
vwrong = copy.deepcopy(out01); vwrong["verdict"] = "fail"
reject("successMotionSpec with verdict 'fail' (branch/verdict mismatch)", out_schema, vwrong)
ewrong = copy.deepcopy(out03); ewrong["verdict"] = "motion_ready"
reject("errorEnvelope with verdict 'motion_ready' (branch/verdict mismatch)", out_schema, ewrong)

# ---------------------------------------------------------------- 4c. codes + SPLIT/folded routing
print("\n== 4c. errorEnvelope codes + SPLIT dual-route + folded routing + slot-11 + halts ==")
# v2_edit_unresolved MUST route to sound-agent (SPLIT — the picture handle)
accept("v2_edit_unresolved -> sound-agent (SPLIT: the v2-edit handle)", out_schema, out04)
v2_wrong = copy.deepcopy(out04); v2_wrong["route_back_to"] = "editor-agent"
reject("v2_edit_unresolved with wrong route (must be sound-agent)", out_schema, v2_wrong)

# text_asset_unresolved is the OTHER SPLIT code — to editor-agent (the text)
tau = copy.deepcopy(out03); tau["failure_code"] = "text_asset_unresolved"; tau["failed_check_id"] = 3
accept("text_asset_unresolved -> editor-agent (SPLIT: the typography text — distinct route)", out_schema, tau)
tau_wrong = copy.deepcopy(tau); tau_wrong["route_back_to"] = "sound-agent"
reject("text_asset_unresolved with wrong route (must be editor-agent)", out_schema, tau_wrong)

# the editor-routed codes
accept("motion_marker_out_of_range -> editor-agent", out_schema, out03)
mk_wrong = copy.deepcopy(out03); mk_wrong["route_back_to"] = "sound-agent"
reject("motion_marker_out_of_range with wrong route (must be editor-agent)", out_schema, mk_wrong)
for code in ("motion_token_out_of_spec", "typography_out_of_spec", "spec_fidelity_breach"):
    c = copy.deepcopy(out03); c["failure_code"] = code
    accept(f"{code} -> editor-agent", out_schema, c)
    cw = copy.deepcopy(c); cw["route_back_to"] = "sound-agent"
    reject(f"{code} with wrong route (must be editor-agent)", out_schema, cw)

# slot-11 motion_agent_failed: valid form (attempts 2, route null)
slot11 = copy.deepcopy(out03)
slot11["failure_code"] = "motion_agent_failed"; slot11["attempts"] = 2
slot11["route_back_to"] = None; slot11["failed_check_id"] = 11
accept("valid slot-11 motion_agent_failed (attempts 2, route null)", out_schema, slot11)
s11a = copy.deepcopy(slot11); s11a["attempts"] = 1
reject("motion_agent_failed with attempts=1 (if/then requires 2)", out_schema, s11a)
s11r = copy.deepcopy(slot11); s11r["attempts"] = 2; s11r["route_back_to"] = "editor-agent"
reject("motion_agent_failed with non-null route_back_to", out_schema, s11r)

# the forensic/precondition halts must route null
for hc, cid in (("upstream_audio_not_ready", 1), ("upstream_not_success", 2),
                ("motion_firewall_breach", 8), ("motion_lineage_failure", 10)):
    h = copy.deepcopy(out03); h["failure_code"] = hc; h["failed_check_id"] = cid; h["route_back_to"] = "editor-agent"
    reject(f"{hc} with non-null route_back_to (precondition/forensic halt)", out_schema, h)
    hok = copy.deepcopy(out03); hok["failure_code"] = hc; hok["failed_check_id"] = cid; hok["route_back_to"] = None
    accept(f"{hc} with route null", out_schema, hok)

# a foreign failure_code must be rejected (a Sound code, not Motion's)
uc = copy.deepcopy(out03); uc["failure_code"] = "audio_firewall_breach"
reject("foreign failure_code 'audio_firewall_breach' (Sound's, not Motion's)", out_schema, uc)

# ---------------------------------------------------------------- 4d. parent_chain (11-tuple held additively)
print("\n== 4d. parent_chain held additively (output minItems 5, maxItems 11) ==")
eleven = copy.deepcopy(out01)  # already an 11-tuple
accept("output parent_chain 11-tuple (Motion append)", out_schema, eleven)
for n in (10, 9, 8, 7, 6, 5):
    t = copy.deepcopy(out01); t["metadata"]["parent_chain"] = t["metadata"]["parent_chain"][:n]
    accept(f"output parent_chain {n}-tuple (held additively)", out_schema, t)
four = copy.deepcopy(out01); four["metadata"]["parent_chain"] = four["metadata"]["parent_chain"][:4]
reject("output parent_chain 4-tuple (below the additive floor)", out_schema, four)
twelve = copy.deepcopy(out01)
twelve["metadata"]["parent_chain"] = out01["metadata"]["parent_chain"] + [out01["reel_ref"]["motion_spec_id"]]
reject("output parent_chain 12-tuple (above maxItems 11)", out_schema, twelve)
# input held at maxItems 10
ten_in = copy.deepcopy(in01)
accept("input parent_chain 10-tuple inbound", in_schema, ten_in)
eleven_in = copy.deepcopy(in01)
eleven_in["metadata"]["parent_chain"] = eleven_in["metadata"]["parent_chain"] + [in01["metadata"]["parent_chain"][9]]
reject("input parent_chain 11-tuple (inbound maxItems 10)", in_schema, eleven_in)

# ---------------------------------------------------------------- 4e. input guards
print("\n== 4e. Input guards (precondition is a runtime halt, NOT a schema reject) ==")
notready = copy.deepcopy(in01); notready["audio_spec"]["verdict"] = "fail"
accept("input fail-verdict audio_spec (valid object — runtime halt upstream_audio_not_ready)", in_schema, notready)
errin = copy.deepcopy(in01); errin["audio_spec"]["output_type"] = "errorEnvelope"
accept("input errorEnvelope audio_spec (valid object — runtime halt upstream_not_success)", in_schema, errin)
nullv2 = copy.deepcopy(in01); nullv2["audio_spec"]["finish_target"]["v2_edit_uri"] = None
accept("input null v2_edit_uri (valid object — runtime v2_edit_unresolved, not schema reject)", in_schema, nullv2)
badfr = copy.deepcopy(in01); badfr["edl"]["frame_rate"] = 24
reject("input edl.frame_rate != 30 (Brand-Voice §8 const)", in_schema, badfr)
nomode = copy.deepcopy(in01); del nomode["metadata"]["production_mode"]
reject("input missing production_mode (required-present for audit lineage)", in_schema, nomode)

# ---------------------------------------------------------------- 4f. convergence proof
print("\n== 4f. TC-01/TC-02 mode-blind finish-convergence proof (FOUR stages deep) ==")
_, o1 = fixtures["case-01-mode-a-origin-pro-motion-ready"]
_, o2 = fixtures["case-02-mode-c-enterprise-motion-ready"]
same = all(o1[k] == o2[k] for k in
           ["motion_spec", "motion_conform_check", "spec_fidelity_check",
            "motion_self_check", "motion_firewall_pass_12", "mode_blind_confirm", "finish_target"])
if same and o1["metadata"]["production_mode"] != o2["metadata"]["production_mode"]:
    ok("TC-01 (Mode A) vs TC-02 (Mode C): finished motion_spec byte-shape-identical despite different origin mode")
else:
    bad("TC-01/TC-02 convergence proof broken (finish paths differ or modes equal)")
if o1["mode_blind_confirm"]["production_mode_read"] is False and o2["mode_blind_confirm"]["production_mode_read"] is False:
    ok("both convergence fixtures attest production_mode_read:false")
else:
    bad("a convergence fixture failed the mode-blind self-attestation")
if o2["tier_richness_echo"]["aspect_variants_planned"] == 2 and o2["tier_richness_echo"]["aspect_variants_specced"] == 1:
    ok("TC-02 honors the Enterprise envelope (planned 2) while specced 1 (v1.0 primary master only)")
else:
    bad("TC-02 tier_richness_echo does not encode the Enterprise-planned / v1.0-specced split")

# ---------------------------------------------------------------- 4g. TC-05 gating fixture
print("\n== 4g. TC-05 gating fixture (12th-pass typography-domain firewall) ==")
blob = json.dumps(in05).lower()
if "sln" in blob and "holdco group" in blob:
    ok("TC-05 input carries the injected banned tokens in the passthrough typography")
else:
    bad("TC-05 input is missing an injected banned token")
if out05["failure_code"] == "motion_firewall_breach" and out05["failed_check_id"] == 8 \
        and out05["route_back_to"] is None \
        and out05["detail"]["motion_firewall_pass_12"]["hits"] == 2 \
        and out05["detail"]["motion_firewall_pass_12"]["status"] == "breach":
    ok("TC-05 expected_output = motion_firewall_breach (Check #8, hits 2, route null — the last visual-text checkpoint before full QC)")
else:
    bad("TC-05 expected_output does not encode the 12th-pass typography-domain catch")

# ---------------------------------------------------------------- summary
print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
sys.exit(1 if FAIL else 0)
