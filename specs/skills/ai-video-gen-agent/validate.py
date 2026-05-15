#!/usr/bin/env python3
"""ARS AI Video Gen Agent v1.0 — SKILL bundle validation harness (Day 26).

Validates the 5 SKILL bundle test fixtures + vendor_pricing_canon.json structure:
- 5/5 input.json validate clean against schemas/input.schema.json
- 1/1 successRenderedShots fixture (TC-01) validates clean against schemas/output.schema.json
- 1/1 successRenderedShots fixture (TC-02) validates clean against schemas/output.schema.json
- 3/3 errorEnvelope fixtures (TC-03/04/05) validate clean against schemas/output.schema.json (errorEnvelope branch)
- vendor_pricing_canon.json parses + per-engine lookup works (e.g., runway → runway-gen3-alpha → usd_per_sec: 0.95)

Day 26 success criteria from build log Day 25:
  10 files in bundle · 5/5 inputs validate clean · 4 expected_output fixtures validate clean ·
  vendor_pricing_canon.json passes per-engine lookup.

Usage:
  python3 validate.py
"""
import json, sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("ERROR: jsonschema not installed. Run: pip install jsonschema")
    sys.exit(2)

ROOT = Path(__file__).parent
INPUT_SCHEMA  = json.loads((ROOT / "schemas" / "input.schema.json").read_text())
OUTPUT_SCHEMA = json.loads((ROOT / "schemas" / "output.schema.json").read_text())
PRICING_CANON = json.loads((ROOT / "vendor_pricing_canon.json").read_text())

input_v  = Draft202012Validator(INPUT_SCHEMA)
output_v = Draft202012Validator(OUTPUT_SCHEMA)

CASES = [
    "case-01-pro-happy",
    "case-02-enterprise-happy",
    "case-03-anchor-failure",
    "case-04-cost-overrun",
    "case-05-quota-exhausted",
]

results = []

def validate(label, schema_v, doc):
    errors = sorted(schema_v.iter_errors(doc), key=lambda e: list(e.path))
    if not errors:
        print(f"  PASS  {label}")
        return True
    print(f"  FAIL  {label}")
    for e in errors[:5]:
        path = "/".join(str(p) for p in e.absolute_path)
        print(f"        - path={path!r} :: {e.message[:240]}")
    return False

print("== Input schema validation (5 fixtures) ==")
for case in CASES:
    inp = json.loads((ROOT / "test-cases" / case / "input.json").read_text())
    results.append(validate(f"{case}/input.json", input_v, inp))

print()
print("== Output schema validation (4 expected_output fixtures) ==")
# TC-01 + TC-02 = successRenderedShots branch
# TC-03 + TC-04 + TC-05 = errorEnvelope branch
for case in CASES:
    out_path = ROOT / "test-cases" / case / "expected_output.json"
    if not out_path.exists():
        print(f"  SKIP  {case}/expected_output.json (not present)")
        continue
    out = json.loads(out_path.read_text())
    results.append(validate(f"{case}/expected_output.json", output_v, out))

print()
print("== Vendor pricing canon lookup test ==")
def lookup(engine, model):
    return PRICING_CANON["engines"][engine]["models"][model]["usd_per_sec"]

lookup_tests = [
    ("runway", "runway-gen3-alpha", 0.95),
    ("runway", "runway-gen3-alpha-turbo", 0.45),
    ("pika",   "pika-1.5", 0.30),
    ("luma",   "luma-dream-machine", 0.35),
    ("flux",   "flux-1.1", 0.20),
    ("kling",  "kling-1.6", 0.40),
    ("higgsfield", "higgsfield-v1", 0.50),
    ("heygen", "heygen-v2-clone", 0.042),
    ("heygen", "heygen-v3-polish", 0.083),
]
canon_passes = 0
for eng, mdl, expected in lookup_tests:
    actual = lookup(eng, mdl)
    ok = abs(actual - expected) < 1e-6
    canon_passes += int(ok)
    status = "PASS" if ok else "FAIL"
    print(f"  {status}  {eng}/{mdl} → ${actual}/sec (expected ${expected})")
canon_ok = canon_passes == len(lookup_tests)
results.append(canon_ok)
print(f"  Canon lookup: {canon_passes}/{len(lookup_tests)} models validated")

print()
print(f"== Summary: {sum(results)}/{len(results)} checks pass ==")
sys.exit(0 if all(results) else 1)
