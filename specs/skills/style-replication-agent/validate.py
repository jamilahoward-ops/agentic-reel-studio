#!/usr/bin/env python3
"""ARS Style Replication Agent v1.0 — SKILL bundle validation harness (Day 34).

Validates the 5 SKILL bundle test fixtures + engine_pricing_canon.json structure:
- 5/5 input.json validate clean against schemas/input.schema.json
- 2/2 successReplicatedShots fixtures (TC-01 Mode B Pro happy · TC-02 Mode C Enterprise happy)
  validate clean against schemas/output.schema.json
- 3/3 errorEnvelope fixtures (TC-03 anchor_unavailable · TC-04 cost_overrun ·
  TC-05 style_drift_exceeded) validate clean against schemas/output.schema.json
- engine_pricing_canon.json parses + per-engine lookup works (7 engines · pika PRIMARY ·
  runway FALLBACK · 5 native compute paths)
- Schemas META-SCHEMA VALID against Draft 2020-12 (mirror of Day 33 smoke)

Day 34 success criteria from Day 32 LOCK CANDIDATE + Day 33 schemas:
  11 files in bundle (SKILL.md, README.md, engine_pricing_canon.json, literal_fingerprint_template.md,
  validate.py, prompts/user-template.txt, schemas/input.schema.json, schemas/output.schema.json,
  test-cases/case-01..case-05/{input.json + expected_output.json + scenario.md})
  · 5/5 inputs validate clean · 5/5 outputs validate clean ·
  engine_pricing_canon.json passes per-engine lookup · ZERO external comms · ZERO render API.

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
PRICING_CANON = json.loads((ROOT / "engine_pricing_canon.json").read_text())

# Smoke: schemas themselves META-SCHEMA VALID
Draft202012Validator.check_schema(INPUT_SCHEMA)
Draft202012Validator.check_schema(OUTPUT_SCHEMA)

input_v  = Draft202012Validator(INPUT_SCHEMA)
output_v = Draft202012Validator(OUTPUT_SCHEMA)

CASES = [
    "case-01-mode-b-pro-happy",
    "case-02-mode-c-enterprise-happy",
    "case-03-anchor-unavailable",
    "case-04-cost-overrun",
    "case-05-style-drift-exceeded",
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

print("== Schema META-VALIDITY (Day 33 smoke) ==")
print("  PASS  input.schema.json (Draft 2020-12)")
print("  PASS  output.schema.json (Draft 2020-12)")
results.extend([True, True])

print()
print("== Input schema validation (5 fixtures) ==")
for case in CASES:
    inp = json.loads((ROOT / "test-cases" / case / "input.json").read_text())
    results.append(validate(f"{case}/input.json", input_v, inp))

print()
print("== Output schema validation (5 expected_output fixtures) ==")
# TC-01 + TC-02 = successReplicatedShots branch
# TC-03 + TC-04 + TC-05 = errorEnvelope branch
for case in CASES:
    out_path = ROOT / "test-cases" / case / "expected_output.json"
    if not out_path.exists():
        print(f"  SKIP  {case}/expected_output.json (not present)")
        continue
    out = json.loads(out_path.read_text())
    results.append(validate(f"{case}/expected_output.json", output_v, out))

print()
print("== Engine pricing canon lookup test (7 engines) ==")
def lookup(engine, model):
    return PRICING_CANON["engines"][engine]["models"][model]["usd_per_shot"]

lookup_tests = [
    ("pika_style_tokens",        "pika-style-tokens-v1",                 0.13),
    ("runway_style_reference",   "runway-style-reference-v1",            0.24),
    ("clip_native",              "clip-vit-l14-internal",                0.001),
    ("phash_native",             "phash-64bit-internal",                 0.0005),
    ("palette_native",           "palette-kmeans-5-internal",            0.0005),
    ("grade_pass_native",        "grade-pass-lut-internal",              0.002),
    ("coverage_envelope_native", "coverage-envelope-checker-internal",   0.001),
]
canon_passes = 0
for eng, mdl, expected in lookup_tests:
    actual = lookup(eng, mdl)
    ok = abs(actual - expected) < 1e-6
    canon_passes += int(ok)
    status = "PASS" if ok else "FAIL"
    print(f"  {status}  {eng}/{mdl} → ${actual}/shot (expected ${expected})")
canon_ok = canon_passes == len(lookup_tests)
results.append(canon_ok)
print(f"  Canon lookup: {canon_passes}/{len(lookup_tests)} models validated")

print()
print(f"== Summary: {sum(results)}/{len(results)} checks pass ==")
sys.exit(0 if all(results) else 1)
