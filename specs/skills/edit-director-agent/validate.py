#!/usr/bin/env python3
"""
Edit Director Agent — bundle validation harness (dry-run, $0, no engine, no render, no network, no LLM).

Validates:
  1. Both schemas compile under the JSON Schema Draft 2020-12 meta-schema.
  2. All 5 fixture input.json validate against input.schema.json.
  3. All 5 fixture expected_output.json validate against output.schema.json
     (TC-01/02 -> successEditPlan; TC-03/04/05 -> errorEnvelope).
  4. Adversarial guards: the structural promises the SPEC makes are enforced by
     the schema — the FIRST 3-verdict fleet agent (plan_ready | fail | revise),
     the zero-false-plan-ready const gates, the standalone duration code (NOT
     folded — opposite of Ingest), the mode-blind const, render_dispatched const
     false, recommend-don't-approve const, slot-11 if/then, parent_chain held
     additively (8-tuple), and the TC-01/TC-02 mode-blind convergence proof.

The Edit Director Agent calls NO generative engine and renders NO media, so this
harness is purely structural: meta-schema + fixture conformance. $0 spent.

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
    ("case-01-mode-a-origin-pro-plan-ready",   "successEditPlan"),
    ("case-02-mode-c-enterprise-plan-ready",   "successEditPlan"),
    ("case-03-coverage-gap-fail",              "errorEnvelope"),
    ("case-04-brand-edit-rule-conflict",       "errorEnvelope"),
    ("case-05-authored-text-firewall-breach",  "errorEnvelope"),
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
in01, out01 = fixtures["case-01-mode-a-origin-pro-plan-ready"]   # plan_ready
in02, out02 = fixtures["case-02-mode-c-enterprise-plan-ready"]   # plan_ready
in03, out03 = fixtures["case-03-coverage-gap-fail"]              # fail (coverage)
in04, out04 = fixtures["case-04-brand-edit-rule-conflict"]       # fail (brand)
in05, out05 = fixtures["case-05-authored-text-firewall-breach"]  # fail (firewall)

# false-plan-ready: a plan_ready carrying a failing HARD brand bool must be rejected (const true)
fp = copy.deepcopy(out01); fp["brand_edit_check"]["hard_cuts_only"] = False
reject("false-plan-ready (plan_ready with hard_cuts_only=false)", out_schema, fp)

# plan_ready with a 9th-pass firewall hit must be rejected (hits const 0)
fh = copy.deepcopy(out01); fh["edit_plan_firewall_pass_9"]["hits"] = 1
reject("plan_ready with authored-text firewall hits>0", out_schema, fh)

# plan_ready with a non-empty unmapped_beats must be rejected (const [])
fm = copy.deepcopy(out01); fm["coverage_remap"]["unmapped_beats"] = [4]
reject("plan_ready with non-empty unmapped_beats", out_schema, fm)

# plan_ready with duration_in_band=false must be rejected (const true)
fd = copy.deepcopy(out01); fd["structure_check"]["duration_in_band"] = False
reject("plan_ready with duration_in_band=false", out_schema, fd)

# out-of-band total_duration_ms must be rejected (45000..75000)
fdo = copy.deepcopy(out01); fdo["structure_check"]["total_duration_ms"] = 90000
reject("plan_ready with total_duration_ms out of the 45-75s band", out_schema, fdo)

# a caption line over 22 chars must be rejected
fc = copy.deepcopy(out01); fc["edit_plan"]["caption_lines"][0]["text"] = "this caption is way too long for the brand rule"
reject("caption line >22 chars", out_schema, fc)

# an all-caps / non-lowercase lower-third must be rejected (case const lowercase)
flc = copy.deepcopy(out01); flc["edit_plan"]["lower_thirds"][0]["case"] = "uppercase"
reject("lower-third case != lowercase", out_schema, flc)

# a fade in transitions must be rejected (const hard-cuts-only)
ft = copy.deepcopy(out01); ft["edit_plan"]["transitions"] = "cross-fade between beats"
reject("transitions != hard-cuts-only const", out_schema, ft)

# mode-blind violation: production_mode_read=true must be rejected (const false)
fmb = copy.deepcopy(out01); fmb["mode_blind_confirm"]["production_mode_read"] = True
reject("mode_blind_confirm.production_mode_read=true (convergence break)", out_schema, fmb)

# render_dispatched=true must be rejected (const false — forged-provenance guard)
frd = copy.deepcopy(out01); frd["metadata"]["render_dispatched"] = True
reject("render_dispatched=true (forged-provenance guard)", out_schema, frd)

# human_review_required:false must be rejected (recommend-don't-approve)
fhr = copy.deepcopy(out01); fhr["human_review_required"] = False
reject("human_review_required:false on plan_ready", out_schema, fhr)

# a non-relative asset_uri in a cut entry must be rejected (Hard Rule #8)
fu = copy.deepcopy(out01); fu["edit_plan"]["cut_order"][0]["asset_uri"] = "https://cdn.example.com/shot-001.mp4"
reject("cut_order with absolute (non-ars://) asset_uri", out_schema, fu)

# wrong end-card copy must be rejected (const)
fec = copy.deepcopy(out01); fec["edit_plan"]["end_card"]["line"] = "REINVENTED - build different."
reject("end_card.line != const brand copy", out_schema, fec)

# ---------------------------------------------------------------- 4b. the 3-verdict model
print("\n== 4b. 3-verdict model (plan_ready | fail | revise — the first fleet success-side third verdict) ==")
# a valid 'revise' (a soft brand bool may be false; revise_rationale required) must be accepted
rev = copy.deepcopy(out01)
rev["verdict"] = "revise"
rev["brand_edit_check"]["one_emotional_beat"] = False  # the soft-rule tension
rev["revise_rationale"] = {"soft_rule": "one_emotional_beat",
                           "tension": "a 4th body beat strengthens the cut but strains the one-emotional-beat rule"}
accept("valid 'revise' (soft bool false + revise_rationale + held for Lever-3)", out_schema, rev)

# 'revise' missing revise_rationale must be rejected (if/then allOf, Decision D10)
revx = copy.deepcopy(rev); del revx["revise_rationale"]
reject("'revise' verdict missing revise_rationale", out_schema, revx)

# a HARD brand bool may NOT be false even on 'revise' (only soft bools may)
revh = copy.deepcopy(rev); revh["brand_edit_check"]["hard_cuts_only"] = False
reject("'revise' with a HARD brand bool false (only soft bools may be false)", out_schema, revh)

# 'hold' is NOT a valid Edit Director verdict (the soft slot is 'revise' on the success branch)
hold = copy.deepcopy(out04); hold["verdict"] = "hold"
reject("verdict 'hold' (Edit Director's soft slot is 'revise', not 'hold')", out_schema, hold)

# 'reshoot' is NOT a valid Edit Director verdict (two gates downstream of live footage)
rs = copy.deepcopy(out04); rs["verdict"] = "reshoot"
reject("verdict 'reshoot' (no reshoot at the authoring layer)", out_schema, rs)

# ---------------------------------------------------------------- 4c. codes + routing
print("\n== 4c. errorEnvelope codes + routing (standalone duration code, slot-11, halts) ==")
# duration_envelope_breach is a STANDALONE valid code (NOT folded — the opposite of Ingest)
deb = copy.deepcopy(out04); deb["failure_code"] = "duration_envelope_breach"; deb["failed_check_id"] = 6
deb["route_back_to"] = "production-coord-agent"
accept("duration_envelope_breach STANDALONE (not folded — opposite of Ingest)", out_schema, deb)

# slot-11 edit_director_agent_failed: valid form (attempts 2, route null) accepted
slot11 = copy.deepcopy(out04)
slot11["failure_code"] = "edit_director_agent_failed"; slot11["attempts"] = 2
slot11["route_back_to"] = None; slot11["failed_check_id"] = 10
accept("valid slot-11 edit_director_agent_failed (attempts 2, route null)", out_schema, slot11)

# slot-11 with attempts=1 must be rejected (if/then requires attempts==2)
s11a = copy.deepcopy(slot11); s11a["attempts"] = 1
reject("edit_director_agent_failed with attempts=1", out_schema, s11a)

# slot-11 with a non-null route_back_to must be rejected (no upstream at fault)
s11r = copy.deepcopy(slot11); s11r["route_back_to"] = "ingest-agent"
reject("edit_director_agent_failed with non-null route_back_to", out_schema, s11r)

# plan_lineage_failure must route nowhere upstream (route_back_to null — forensic halt)
plf = copy.deepcopy(out03); plf["failure_code"] = "plan_lineage_failure"; plf["failed_check_id"] = 9
plf["route_back_to"] = "ingest-agent"
reject("plan_lineage_failure with non-null route_back_to (forensic halt)", out_schema, plf)

# upstream_ingest_not_passed must route null (precondition gate)
uin = copy.deepcopy(out03); uin["failure_code"] = "upstream_ingest_not_passed"; uin["failed_check_id"] = 1
reject("upstream_ingest_not_passed with non-null route_back_to (precondition halt)", out_schema, uin)

# an unknown failure_code must be rejected
uc = copy.deepcopy(out04); uc["failure_code"] = "asset_spec_violation"  # an Ingest code, not Edit Director's
reject("foreign failure_code 'asset_spec_violation' (not in Edit Director's namespace)", out_schema, uc)

# a valid coverage fail still accepted
accept("valid incomplete_shot_coverage -> ingest-agent", out_schema, out03)

# ---------------------------------------------------------------- 4d. parent_chain (8-tuple held additively)
print("\n== 4d. parent_chain held additively (output minItems 5, maxItems 8) ==")
eight = copy.deepcopy(out01)  # already an 8-tuple
accept("output parent_chain 8-tuple (Edit Director append)", out_schema, eight)
for n in (7, 6, 5):
    t = copy.deepcopy(out01); t["metadata"]["parent_chain"] = t["metadata"]["parent_chain"][:n]
    accept(f"output parent_chain {n}-tuple (held additively)", out_schema, t)
four = copy.deepcopy(out01); four["metadata"]["parent_chain"] = four["metadata"]["parent_chain"][:4]
reject("output parent_chain 4-tuple (below the additive floor)", out_schema, four)
# a 9-tuple must be rejected (maxItems 8)
nine = copy.deepcopy(out01); nine["metadata"]["parent_chain"] = out01["metadata"]["parent_chain"] + [out01["reel_ref"]["edit_plan_id"]]
reject("output parent_chain 9-tuple (above maxItems 8)", out_schema, nine)
# input held at maxItems 7
seven_in = copy.deepcopy(in01)
accept("input parent_chain 7-tuple inbound", in_schema, seven_in)
eight_in = copy.deepcopy(in01); eight_in["metadata"]["parent_chain"] = eight_in["metadata"]["parent_chain"] + [in01["metadata"]["parent_chain"][6]]
reject("input parent_chain 8-tuple (inbound maxItems 7)", in_schema, eight_in)

# ---------------------------------------------------------------- 4e. input guards
print("\n== 4e. Input guards (precondition is a runtime halt, NOT a schema reject) ==")
# a non-pass manifest with no sign-off is a VALID object (runtime halt upstream_ingest_not_passed, not a schema reject)
nonpass = copy.deepcopy(in01); nonpass["asset_manifest"]["verdict"] = "fail"
accept("input non-pass manifest (valid object — runtime halt, not schema reject)", in_schema, nonpass)
# a consumed errorEnvelope manifest is also a VALID object (runtime halt upstream_not_success)
errin = copy.deepcopy(in01); errin["asset_manifest"]["output_type"] = "errorEnvelope"
accept("input errorEnvelope manifest (valid object — runtime halt upstream_not_success)", in_schema, errin)
# an absolute asset_uri in raw_footage must be rejected (Hard Rule #8)
absuri = copy.deepcopy(in01); absuri["asset_manifest"]["asset_bundle"]["raw_footage"][0]["asset_uri"] = "https://cdn.example.com/x.mp4"
reject("input raw_footage with absolute (non-ars://) asset_uri", in_schema, absuri)
# production_mode is REQUIRED present (carried for audit lineage even though never read)
nomode = copy.deepcopy(in01); del nomode["metadata"]["production_mode"]
reject("input missing production_mode (required-present for audit lineage)", in_schema, nomode)

# ---------------------------------------------------------------- 4f. convergence proof
print("\n== 4f. TC-01/TC-02 mode-blind convergence proof ==")
_, o1 = fixtures["case-01-mode-a-origin-pro-plan-ready"]
_, o2 = fixtures["case-02-mode-c-enterprise-plan-ready"]
same = all(o1[k] == o2[k] for k in
           ["edit_plan", "coverage_remap", "structure_check", "brand_edit_check",
            "edit_plan_firewall_pass_9", "mode_blind_confirm"])
if same and o1["metadata"]["production_mode"] != o2["metadata"]["production_mode"]:
    ok("TC-01 (Mode A) vs TC-02 (Mode C): authored plan byte-shape-identical despite different origin mode")
else:
    bad("TC-01/TC-02 convergence proof broken (authoring paths differ or modes equal)")
# both attest mode-blindness
if o1["mode_blind_confirm"]["production_mode_read"] is False and o2["mode_blind_confirm"]["production_mode_read"] is False:
    ok("both convergence fixtures attest production_mode_read:false")
else:
    bad("a convergence fixture failed the mode-blind self-attestation")

# ---------------------------------------------------------------- 4g. TC-05 gating fixture
print("\n== 4g. TC-05 gating fixture (9th-pass authored-text firewall) ==")
blob = json.dumps(in05)
if "sln" in blob and "holdcogroup.com" in blob:
    ok("TC-05 input carries the injected banned tokens in the Script on_screen_text Edit Director authors from")
else:
    bad("TC-05 input is missing an injected banned token")
if out05["failure_code"] == "edit_plan_firewall_breach" and out05["failed_check_id"] == 4 \
        and out05["detail"]["edit_plan_firewall_pass_9"]["hits"] == 2 and out05["route_back_to"] is None:
    ok("TC-05 expected_output = edit_plan_firewall_breach (Check #4, hits 2, route null — leak is self-authored)")
else:
    bad("TC-05 expected_output does not encode the 9th-pass authored-text catch")

# ---------------------------------------------------------------- summary
print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
sys.exit(1 if FAIL else 0)
