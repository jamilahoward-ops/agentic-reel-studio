#!/usr/bin/env python3
"""ARS AI Video Gen Agent — Day 25 schema dry-run validation harness.
Validates 5 Day-23 test fixtures against input.schema.json + output.schema.json.
Happy paths (TC-01, TC-02) MUST validate clean against input schema.
TC-01 output MUST validate clean against output schema (successRenderedShots branch).
TC-03, TC-04, TC-05 output MUST validate clean against output schema (errorEnvelope branch).
"""
import json, sys, os
from pathlib import Path
from jsonschema import Draft202012Validator
from jsonschema.exceptions import best_match

ROOT = Path(__file__).parent
INPUT_SCHEMA  = json.loads((ROOT / "input.schema.json").read_text())
OUTPUT_SCHEMA = json.loads((ROOT / "output.schema.json").read_text())

input_v  = Draft202012Validator(INPUT_SCHEMA)
output_v = Draft202012Validator(OUTPUT_SCHEMA)

def validate(label, schema_v, doc, must_pass=True):
    errors = sorted(schema_v.iter_errors(doc), key=lambda e: e.path)
    if not errors and must_pass:
        print(f"  PASS  {label}")
        return True
    if not errors and not must_pass:
        print(f"  XFAIL {label} (expected failure but validated clean)")
        return False
    if errors and must_pass:
        print(f"  FAIL  {label}")
        for e in errors[:5]:
            path = "/".join(str(p) for p in e.absolute_path)
            print(f"        - path={path!r} :: {e.message[:240]}")
        return False
    # errors and not must_pass — expected
    print(f"  PASS  {label} (negative — got {len(errors)} expected errors)")
    return True

results = []

print("== Input schema validation (production_plan bundle) ==")
for fx in ["TC-01-pro-happy-input.json", "TC-02-enterprise-happy-input.json"]:
    doc = json.loads((ROOT / "fixtures" / fx).read_text())
    results.append(validate(fx, input_v, doc, must_pass=True))

print()
print("== Output schema validation (rendered_shots | errorEnvelope) ==")
for fx, must_pass in [
    ("TC-01-pro-happy-output.json", True),
    ("TC-03-anchor-failure-output.json", True),
    ("TC-04-cost-overrun-output.json", True),
    ("TC-05-quota-exhausted-output.json", True),
]:
    doc = json.loads((ROOT / "fixtures" / fx).read_text())
    results.append(validate(fx, output_v, doc, must_pass=must_pass))

print()
print(f"== Summary: {sum(results)}/{len(results)} fixtures validate clean ==")
sys.exit(0 if all(results) else 1)
