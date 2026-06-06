#!/usr/bin/env python3
"""
QC Pre-flight Agent — bundle validation harness (dry-run, $0, no engine).

Validates:
  1. Both schemas compile under the JSON Schema Draft 2020-12 meta-schema.
  2. All 5 fixture input.json validate against input.schema.json.
  3. All 5 fixture expected_output.json validate against output.schema.json
     (TC-01/02 -> successPreflightReport; TC-03/04/05 -> errorEnvelope).
  4. Adversarial guards: the structural promises the SPEC makes are enforced
     by the schema (false-pass impossible, hold/reshoot route guards, folded
     codes rejected, recommend-don't-approve const, parent_chain backward-compat).

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
    ("case-01-mode-b-pro-clean-pass",        "successPreflightReport"),
    ("case-02-mode-c-enterprise-clean-pass", "successPreflightReport"),
    ("case-03-entity-firewall-breach",       "errorEnvelope"),
    ("case-04-format-spec-violation",        "errorEnvelope"),
    ("case-05-drift-unresolved",             "errorEnvelope"),
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
in01, out01 = fixtures["case-01-mode-b-pro-clean-pass"]
in03, out03 = fixtures["case-03-entity-firewall-breach"]
in05, out05 = fixtures["case-05-drift-unresolved"]

def reject(label, schema, inst):
    if is_valid(schema, inst):
        bad(f"{label} — schema ACCEPTED an instance it must reject")
    else:
        ok(f"{label} — rejected")

def accept(label, schema, inst):
    e = first_error(schema, inst)
    ok(f"{label} — accepted") if e is None else bad(f"{label} -> {e}")

# false-pass: a 'pass' carrying a failing brand-voice point must be rejected
fp = copy.deepcopy(out01); fp["brand_voice_qc"]["per_point"][5]["status"] = "fail"
reject("false-pass (pass branch with a failing brand-voice point)", out_schema, fp)

# pass with firewall hits must be rejected
fh = copy.deepcopy(out01); fh["entity_firewall_pass_7"]["hits"] = 1
reject("pass branch with entity_firewall hits>0", out_schema, fh)

# pass with unresolved drift must be rejected
fd = copy.deepcopy(out01); fd["drift_reconciliation"]["unresolved_drift_count"] = 1
reject("pass branch with unresolved_drift_count>0", out_schema, fd)

# human_review_required:false must be rejected (recommend-don't-approve)
hr = copy.deepcopy(out01); hr["human_review_required"] = False
reject("human_review_required:false on pass branch", out_schema, hr)

# hold verdict with a non-null route_back_to must be rejected
hbad = copy.deepcopy(out05); hbad["route_back_to"] = "style-replication-agent"
reject("hold verdict with non-null route_back_to", out_schema, hbad)

# reshoot verdict NOT routed to production-coord-agent must be rejected
rbad = copy.deepcopy(out03); rbad["verdict"] = "reshoot"; rbad["route_back_to"] = "style-replication-agent"; rbad["failure_code"] = "format_spec_violation"
reject("reshoot verdict not routed to production-coord-agent", out_schema, rbad)

# a valid reshoot (Mode A) must be accepted
rgood = copy.deepcopy(out03); rgood["verdict"] = "reshoot"; rgood["route_back_to"] = "production-coord-agent"; rgood["failure_code"] = "format_spec_violation"; rgood["metadata"]["production_mode"] = "A"
accept("valid reshoot -> production-coord-agent", out_schema, rgood)

# folded codes must NOT be enumerated
for folded in ("qc_pre_flags_format_violation", "negative_prompt_chain_break"):
    fc = copy.deepcopy(out03); fc["failure_code"] = folded
    reject(f"folded code '{folded}' (must not be a valid failure_code)", out_schema, fc)

# parent_chain backward-compat: 6-tuple accepted, 5-tuple accepted, 4-tuple rejected
print("\n== 4b. parent_chain backward-compat (held minItems 5, maxItems 6) ==")
six = copy.deepcopy(out01)   # already 6-tuple
accept("parent_chain 6-tuple", out_schema, six)
five = copy.deepcopy(out01); five["metadata"]["parent_chain"] = five["metadata"]["parent_chain"][:5]
accept("parent_chain 5-tuple (inbound canon)", out_schema, five)
four = copy.deepcopy(out01); four["metadata"]["parent_chain"] = four["metadata"]["parent_chain"][:4]
reject("parent_chain 4-tuple", out_schema, four)

# input adversarial: a <4 qc_pre_flags floor breach + an absolute asset_uri must be rejected
print("\n== 4c. Input guards ==")
floor = copy.deepcopy(in01); floor["accumulated_qc_pre_flags"]["brief-agent"] = ["only_one_flag"]
reject("input with a <4 qc_pre_flags floor breach", in_schema, floor)
absuri = copy.deepcopy(in01); absuri["replicated_shots"][0]["asset_uri"] = "https://cdn.example.com/shot-001.mp4"
reject("input with absolute (non-ars://) asset_uri", in_schema, absuri)
badceil = copy.deepcopy(in01); badceil["cost_ledger"]["tier_combined_ceiling_usd"] = 500
reject("input with non-canonical combined ceiling (500)", in_schema, badceil)

# TC-03 gating: the injected banned token rides in a schema-valid free-text field
print("\n== 4d. TC-03 gating fixture ==")
if "4821 Main" in json.dumps(in03):
    ok("TC-03 input carries the injected '4821 Main' token (runtime 7th-pass catch surface)")
else:
    bad("TC-03 input is missing the injected banned token")
if out03["failure_code"] == "entity_firewall_breach" and out03["route_back_to"] == "style-replication-agent":
    ok("TC-03 expected_output = entity_firewall_breach -> style-replication-agent")
else:
    bad("TC-03 expected_output does not encode the firewall catch")

# ---------------------------------------------------------------- summary
print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
sys.exit(1 if FAIL else 0)
