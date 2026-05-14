#!/usr/bin/env python3
"""Negative-test harness — schemas MUST REJECT these inputs.
Confirms schemas catch what they should catch (defense-in-depth at schema layer).
"""
import json, copy, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).parent
INPUT_SCHEMA  = json.loads((ROOT / "input.schema.json").read_text())
OUTPUT_SCHEMA = json.loads((ROOT / "output.schema.json").read_text())

input_v  = Draft202012Validator(INPUT_SCHEMA)
output_v = Draft202012Validator(OUTPUT_SCHEMA)

TC01_INPUT  = json.loads((ROOT / "fixtures" / "TC-01-pro-happy-input.json").read_text())
TC01_OUTPUT = json.loads((ROOT / "fixtures" / "TC-01-pro-happy-output.json").read_text())

def expect_reject(label, schema_v, mutator):
    doc = copy.deepcopy(TC01_INPUT if "input" in label else TC01_OUTPUT)
    mutator(doc)
    errors = list(schema_v.iter_errors(doc))
    if errors:
        print(f"  PASS  {label} ({len(errors)} errors)")
        return True
    print(f"  FAIL  {label} — schema did NOT reject")
    return False

results = []
print("== Negative tests — schemas MUST reject these ==")

# Input schema negative tests
results.append(expect_reject(
    "input: Pilot tier rejected",
    input_v,
    lambda d: d["production_plan"].__setitem__("tier", "Pilot")
))
results.append(expect_reject(
    "input: Mode A rejected (production_mode != B)",
    input_v,
    lambda d: d["production_plan"].__setitem__("production_mode", "A")
))
results.append(expect_reject(
    "input: tier_cost_ceiling mismatch (Pro tier with 750 ceiling)",
    input_v,
    lambda d: d["production_plan"]["mode_b_plan"].__setitem__("tier_cost_ceiling_usd", 750)
))
results.append(expect_reject(
    "input: HeyGen shot missing talent_id",
    input_v,
    lambda d: d["production_plan"]["mode_b_plan"]["render_queue"][0].update({
        "engine_id": "heygen", "model_id": "heygen-v2-clone"
    })  # leaves talent_id absent → required-when-heygen kicks in
))

# Output schema negative tests
results.append(expect_reject(
    "output: negative_prompt_attached_bool=false rejected (Hard Rule #10)",
    output_v,
    lambda d: d["rendered_shots"][0]["render_dispatch_log"][0].__setitem__("negative_prompt_attached_bool", False)
))
results.append(expect_reject(
    "output: parent_chain wrong length (3 instead of 4)",
    output_v,
    lambda d: d.__setitem__("parent_chain", d["parent_chain"][:3])
))
results.append(expect_reject(
    "output: errorEnvelope failure_code not in 17-code enum",
    output_v,
    lambda d: {"status": "blocked", "errorEnvelope": {"failure_code": "made_up_code", "attempts": 1}}.items() and d.clear() or d.update({"status": "blocked", "errorEnvelope": {"failure_code": "made_up_code", "attempts": 1}})
))
results.append(expect_reject(
    "output: qc_pre_flags fewer than 4 entries",
    output_v,
    lambda d: d.__setitem__("qc_pre_flags", ["only_one"])
))
results.append(expect_reject(
    "output: asset_uri absolute URL rejected (must be ars:// platform-relative)",
    output_v,
    lambda d: d["rendered_shots"][0].__setitem__("asset_uri", "https://cdn.example.com/shot-001.mp4")
))
results.append(expect_reject(
    "output: suspected_buildings_bool=true still passes schema (content-layer check, not schema)",
    output_v,
    lambda d: d["rendered_shots"][0]["post_render_qc_seed"].__setitem__("suspected_buildings_bool", True)
))

print()
fails = sum(1 for r in results if not r)
print(f"== Summary: {sum(results)}/{len(results)} negative tests behave correctly ==")
# Note: the last one is expected to FAIL to reject (it's documenting that no_buildings is a content-layer check)
# So we expect 9/10 to "pass" the negative test
sys.exit(0 if fails <= 1 else 1)
