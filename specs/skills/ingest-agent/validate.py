#!/usr/bin/env python3
"""
Ingest Agent — bundle validation harness (dry-run, $0, no engine, no probe, no network).

Validates:
  1. Both schemas compile under the JSON Schema Draft 2020-12 meta-schema.
  2. All 5 fixture input.json validate against input.schema.json.
  3. All 5 fixture expected_output.json validate against output.schema.json
     (TC-01/02 -> successAssetManifest; TC-03/04/05 -> errorEnvelope).
  4. Adversarial guards: the structural promises the SPEC makes are enforced
     by the schema (false-pass impossible, verdict/route if-then guards, the
     folded code rejected, no `hold` verdict, recommend-don't-clear const,
     parent_chain backward-compat, input source/floor/uri guards).

The Ingest Agent calls NO generative engine and runs NO byte-level decode, so
this harness is purely structural: meta-schema + fixture conformance. $0 spent.

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
    ("case-01-mode-b-pro-clean-pass",        "successAssetManifest"),
    ("case-02-mode-c-enterprise-clean-pass", "successAssetManifest"),
    ("case-03-mode-a-coverage-gap-reshoot",  "errorEnvelope"),
    ("case-04-asset-spec-violation",         "errorEnvelope"),
    ("case-05-asset-firewall-breach",        "errorEnvelope"),
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
in01, out01 = fixtures["case-01-mode-b-pro-clean-pass"]   # pass branch
in03, out03 = fixtures["case-03-mode-a-coverage-gap-reshoot"]  # reshoot
in04, out04 = fixtures["case-04-asset-spec-violation"]    # fail
in05, out05 = fixtures["case-05-asset-firewall-breach"]   # fail (firewall)

# false-pass: a 'pass' carrying a failing spec_check boolean must be rejected
fp = copy.deepcopy(out01); fp["spec_check"]["aspect_ok"] = False
reject("false-pass (pass branch with spec_check.aspect_ok=false)", out_schema, fp)

# pass with firewall hits must be rejected
fh = copy.deepcopy(out01); fh["asset_firewall_pass_8"]["hits"] = 1
reject("pass branch with asset_firewall hits>0", out_schema, fh)

# pass with a non-empty missing_shots must be rejected
fm = copy.deepcopy(out01); fm["spec_check"]["missing_shots"] = ["shot-004"]
reject("pass branch with non-empty missing_shots", out_schema, fm)

# pass with coverage_complete=false must be rejected
fcc = copy.deepcopy(out01); fcc["coverage_check"]["coverage_complete"] = False
reject("pass branch with coverage_complete=false", out_schema, fcc)

# pass with byte_probe_performed=true must be rejected (declared-spec honesty contract)
bp = copy.deepcopy(out01); bp["metadata"]["byte_probe_performed"] = True
reject("byte_probe_performed=true (forged-provenance guard)", out_schema, bp)

# human_review_required:false must be rejected (recommend-don't-clear)
hr = copy.deepcopy(out01); hr["human_review_required"] = False
reject("human_review_required:false on pass branch", out_schema, hr)

# a non-relative asset_uri inside the manifest must be rejected
nr = copy.deepcopy(out01); nr["asset_bundle"]["raw_footage"][0]["asset_uri"] = "https://cdn.example.com/shot-001.mp4"
reject("manifest raw_footage with absolute (non-ars://) asset_uri", out_schema, nr)

# reshoot verdict NOT routed to production-coord-agent must be rejected (if/then)
rbad = copy.deepcopy(out03); rbad["route_back_to"] = "style-replication-agent"
reject("reshoot verdict not routed to production-coord-agent", out_schema, rbad)

# reshoot verdict with a non-coverage failure_code must be rejected (if/then)
rbad2 = copy.deepcopy(out03); rbad2["failure_code"] = "asset_spec_violation"
reject("reshoot verdict with failure_code != missing_shot_coverage", out_schema, rbad2)

# a valid reshoot must still be accepted
accept("valid reshoot -> production-coord-agent + missing_shot_coverage", out_schema, out03)

# slot-11 ingest_agent_failed: valid form (attempts 2, route null, verdict fail) accepted
slot11 = copy.deepcopy(out04)
slot11["failure_code"] = "ingest_agent_failed"; slot11["attempts"] = 2
slot11["route_back_to"] = None; slot11["verdict"] = "fail"
accept("valid slot-11 ingest_agent_failed (attempts 2, route null)", out_schema, slot11)

# slot-11 with attempts=1 must be rejected (if/then requires attempts==2)
s11a = copy.deepcopy(slot11); s11a["attempts"] = 1
reject("ingest_agent_failed with attempts=1", out_schema, s11a)

# slot-11 with a non-null route_back_to must be rejected (no upstream at fault)
s11r = copy.deepcopy(slot11); s11r["route_back_to"] = "style-replication-agent"
reject("ingest_agent_failed with non-null route_back_to", out_schema, s11r)

# the folded code must NOT be enumerated
fc = copy.deepcopy(out04); fc["failure_code"] = "duration_envelope_breach"
reject("folded code 'duration_envelope_breach' (must not be a valid failure_code)", out_schema, fc)

# 'hold' is NOT a valid Ingest verdict (deliberate divergence from QC Pre-flight)
hold = copy.deepcopy(out04); hold["verdict"] = "hold"
reject("verdict 'hold' (Ingest has no soft-hold — deterministic domain)", out_schema, hold)

# ---------------------------------------------------------------- 4b. parent_chain
print("\n== 4b. parent_chain backward-compat (held minItems 5, maxItems 7) ==")
seven = copy.deepcopy(out01)  # already a 7-tuple
accept("parent_chain 7-tuple (Ingest append)", out_schema, seven)
six = copy.deepcopy(out01); six["metadata"]["parent_chain"] = six["metadata"]["parent_chain"][:6]
accept("parent_chain 6-tuple (QC extension preview)", out_schema, six)
five = copy.deepcopy(out01); five["metadata"]["parent_chain"] = five["metadata"]["parent_chain"][:5]
accept("parent_chain 5-tuple (inbound canon)", out_schema, five)
four = copy.deepcopy(out01); four["metadata"]["parent_chain"] = four["metadata"]["parent_chain"][:4]
reject("parent_chain 4-tuple", out_schema, four)

# input parent_chain held at maxItems 6
sixin = copy.deepcopy(in01)  # already 6-tuple inbound
accept("input parent_chain 6-tuple inbound", in_schema, sixin)
seven_in = copy.deepcopy(in01); seven_in["metadata"]["parent_chain"] = seven_in["metadata"]["parent_chain"] + [seven_in["metadata"]["parent_chain"][4]]
reject("input parent_chain 7-tuple (inbound maxItems 6)", in_schema, seven_in)

# ---------------------------------------------------------------- 4c. input guards
print("\n== 4c. Input guards (polymorphic source + floor + uri) ==")
# both sources present must be rejected (oneOf)
both = copy.deepcopy(in01); both["footage_upload_manifest"] = {"clips": [{"shot_ref": "shot-001", "asset_uri": "ars://x/y.mp4", "take": 1}]}
reject("input with BOTH replicated_shots and footage_upload_manifest", in_schema, both)

# no source present must be rejected (oneOf)
none_src = copy.deepcopy(in01); del none_src["replicated_shots"]
reject("input with NO production source", in_schema, none_src)

# Mode A branch forbids rendered_shots
arend = copy.deepcopy(in03); arend["rendered_shots"] = [{"shot_ref": "shot-001"}]
reject("Mode A input carrying rendered_shots", in_schema, arend)

# <4 qc_pre_flags floor breach must be rejected
floor = copy.deepcopy(in01); floor["replicated_shots"][0]["qc_pre_flags"] = ["only_one_flag"]
reject("input with a <4 qc_pre_flags floor breach", in_schema, floor)

# absolute (non-ars://) asset_uri must be rejected
absuri = copy.deepcopy(in01); absuri["replicated_shots"][0]["asset_uri"] = "https://cdn.example.com/shot-001.mp4"
reject("input with absolute (non-ars://) asset_uri", in_schema, absuri)

# non-pass preflight with no sign-off is a VALID object (runtime halt, not schema reject)
nonpass = copy.deepcopy(in01); nonpass["preflight_report"]["verdict"] = "fail"
accept("input with non-pass preflight (valid object — runtime halt, not schema reject)", in_schema, nonpass)

# ---------------------------------------------------------------- 4d. gating fixture
print("\n== 4d. TC-05 gating fixture (8th-pass asset-layer firewall) ==")
blob = json.dumps(in05)
if "sln_cuts" in blob and "holdcogroup.com" in blob:
    ok("TC-05 input carries the injected asset-layer tokens (filename + sidecar metadata)")
else:
    bad("TC-05 input is missing an injected banned token")
if out05["failure_code"] == "asset_firewall_breach" and out05["route_back_to"] == "style-replication-agent":
    ok("TC-05 expected_output = asset_firewall_breach -> style-replication-agent")
else:
    bad("TC-05 expected_output does not encode the firewall catch")
# the convergence proof: TC-01 vs TC-02 asset_bundle + spec_check + coverage byte-shape identical
_, o1 = fixtures["case-01-mode-b-pro-clean-pass"]
_, o2 = fixtures["case-02-mode-c-enterprise-clean-pass"]
same = (o1["asset_bundle"] == o2["asset_bundle"] and o1["spec_check"] == o2["spec_check"]
        and o1["coverage_check"] == o2["coverage_check"])
ok("TC-01/TC-02 convergence: asset_bundle + spec_check + coverage byte-shape identical") if same \
    else bad("TC-01/TC-02 convergence proof broken (bundles differ)")

# ---------------------------------------------------------------- summary
print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
sys.exit(1 if FAIL else 0)
