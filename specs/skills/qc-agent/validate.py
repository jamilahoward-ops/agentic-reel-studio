#!/usr/bin/env python3
"""
Full QC Agent — bundle validation harness (dry-run, $0, no engine, no render,
no compositing, no frame decode, no measured probe, no publish, no network, no LLM).

Validates:
  1. Both schemas compile under the JSON Schema Draft 2020-12 meta-schema.
  2. All 5 fixture input.json validate against input.schema.json.
  3. All 5 fixture expected_output.json validate against output.schema.json
     (TC-01/02 -> successQcReport; TC-03/04/05 -> errorEnvelope).
  4. Adversarial guards: the structural promises the SPEC makes are enforced by
     the schema — the TERMINAL adjudicator's zero-false-PASS const gates (every
     one of the §12.1 15-term AND-of-gates HARD terms const-pinned on the success
     branch, so a false-PASS is UNREPRESENTABLE), the RESTORED third verdict
     (pass | fail | reshoot — the enum split across the two branches), the LARGEST
     namespace in the fleet (12 named codes + slot = 15 strings, the two routed
     pairs NOT folded), the COMPUTED route_back_to (enum incl. null, not a per-code
     const), the exactly-11 per-point evidence array, the re-DERIVED firewall count
     (Check #6), the tri-anchor hash chain (the only pass verifying all THREE at
     once), mode_blind_confirm const, auto_published/qc_measured_probe_run const
     false, human_review_required const true, parent_chain held additively (input
     11-tuple / output 12-tuple), and the TC-01/TC-02 gate-convergence proof FIVE
     stages deep + the TC-05 GATING 13th-pass firewall catch.

The Full QC Agent calls NO generative engine, renders NO media, decodes NO frame,
measures NO pixel, and publishes NOTHING, so this harness is purely structural:
meta-schema + fixture conformance. $0 spent.

Run:  python3 validate.py     (requires jsonschema>=4.26, Draft 2020-12)
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
    ("case-01-mode-a-origin-pro-pass",         "successQcReport"),
    ("case-02-mode-c-enterprise-pass",         "successQcReport"),
    ("case-03-format-variant-mismatch-fail",   "errorEnvelope"),
    ("case-04-unresolved-upstream-flag-fail",  "errorEnvelope"),
    ("case-05-terminal-firewall-breach-fail",  "errorEnvelope"),
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

in01, out01 = fixtures["case-01-mode-a-origin-pro-pass"]        # pass
in02, out02 = fixtures["case-02-mode-c-enterprise-pass"]        # pass (convergence twin)
in03, out03 = fixtures["case-03-format-variant-mismatch-fail"]  # fail (format)
in04, out04 = fixtures["case-04-unresolved-upstream-flag-fail"] # fail (flag closure)
in05, out05 = fixtures["case-05-terminal-firewall-breach-fail"] # fail (firewall — GATING)

# ---------------------------------------------------------------- 4. false-PASS unrepresentable (success const gates)
print("\n== 4. Zero-false-PASS const gates — every §12.1 AND-term (schema must REJECT) ==")
# brand voice
bv = copy.deepcopy(out01); bv["qc_gate"]["brand_voice_11_point"]["points_passed"] = 10
reject("pass with brand_voice points_passed != 11", out_schema, bv)
bvt = copy.deepcopy(out01); bvt["qc_gate"]["brand_voice_11_point"]["points_total"] = 12
reject("pass with brand_voice points_total != 11", out_schema, bvt)
bvr = copy.deepcopy(out01); bvr["qc_gate"]["brand_voice_11_point"]["per_point_evidence"][3]["result"] = "fail"
reject("pass with a per_point_evidence row result 'fail'", out_schema, bvr)
bv10 = copy.deepcopy(out01)
bv10["qc_gate"]["brand_voice_11_point"]["per_point_evidence"] = bv10["qc_gate"]["brand_voice_11_point"]["per_point_evidence"][:10]
reject("pass with per_point_evidence != 11 rows (10)", out_schema, bv10)
bv12 = copy.deepcopy(out01)
extra = copy.deepcopy(bv12["qc_gate"]["brand_voice_11_point"]["per_point_evidence"][0]); extra["point_id"] = 11
bv12["qc_gate"]["brand_voice_11_point"]["per_point_evidence"].append(extra)
reject("pass with per_point_evidence != 11 rows (12)", out_schema, bv12)

# terminal firewall (13th pass — the re-derived count)
fh = copy.deepcopy(out01); fh["qc_gate"]["entity_firewall_pass_13"]["hits"] = 1
reject("pass with entity_firewall_pass_13.hits != 0 (re-derived const 0)", out_schema, fh)
fs = copy.deepcopy(out01); fs["qc_gate"]["entity_firewall_pass_13"]["status"] = "breach"
reject("pass with entity_firewall_pass_13.status 'breach'", out_schema, fs)

# format spec — all 5 booleans
for field in ["aspect_ok", "resolution_ok", "duration_in_band", "caption_burn_in_ok", "variants_match_promise"]:
    f = copy.deepcopy(out01); f["qc_gate"]["format_spec"][field] = False
    reject(f"pass with format_spec.{field}=false", out_schema, f)

# caption spec — both booleans
for field in ["parity_with_edl", "burn_in_text_firewall_clean"]:
    f = copy.deepcopy(out01); f["qc_gate"]["caption_spec"][field] = False
    reject(f"pass with caption_spec.{field}=false", out_schema, f)

# cost ledger closure
ci = copy.deepcopy(out01); ci["qc_gate"]["cost_ledger"]["in_envelope"] = False
reject("pass with cost_ledger.in_envelope=false", out_schema, ci)

# flag-surface closure (the terminal-gate step)
fa1 = copy.deepcopy(out01); fa1["flag_adjudication"]["agents_reporting"] = 11
reject("pass with flag_adjudication.agents_reporting != 12", out_schema, fa1)
fa2 = copy.deepcopy(out01); fa2["flag_adjudication"]["unresolved"] = 1
reject("pass with flag_adjudication.unresolved != 0", out_schema, fa2)
fa3 = copy.deepcopy(out01); fa3["flag_adjudication"]["surface_complete"] = False
reject("pass with flag_adjudication.surface_complete=false", out_schema, fa3)
fa4 = copy.deepcopy(out01); fa4["flag_adjudication"]["predicates_total"] = 40
reject("pass with predicates_total below the 48-floor minimum", out_schema, fa4)

# motion self-check consistency
msc = copy.deepcopy(out01); msc["motion_self_check_adjudication"]["self_check_consistent_with_gate"] = False
reject("pass with self_check_consistent_with_gate=false", out_schema, msc)

# tri-anchor evidence-hash chain
for field in ["motion_spec_evidence_hash_verified", "audio_spec_evidence_hash_verified",
              "edl_evidence_hash_verified", "chain_intact"]:
    f = copy.deepcopy(out01); f["evidence_hash_chain"][field] = False
    reject(f"pass with evidence_hash_chain.{field}=false", out_schema, f)

# recommend-don't-publish consts
ap = copy.deepcopy(out01); ap["publish_target"]["auto_published"] = True
reject("pass with publish_target.auto_published=true (forged-publish guard)", out_schema, ap)
apm = copy.deepcopy(out01); apm["metadata"]["auto_published"] = True
reject("pass with metadata.auto_published=true (forged-publish guard)", out_schema, apm)
pm = copy.deepcopy(out01); pm["publish_target"]["publish_mode"] = "automated"
reject("pass with publish_mode 'automated' (v1.1 reserved — not v1.0)", out_schema, pm)
mp = copy.deepcopy(out01); mp["qc_measured_probe_run"] = True
reject("pass with qc_measured_probe_run=true (no measured probe in v1.0)", out_schema, mp)
mpm = copy.deepcopy(out01); mpm["metadata"]["qc_measured_probe_run"] = True
reject("pass with metadata.qc_measured_probe_run=true", out_schema, mpm)
hr = copy.deepcopy(out01); hr["human_review_required"] = False
reject("pass with human_review_required=false (recommend-don't-publish)", out_schema, hr)
hrm = copy.deepcopy(out01); hrm["metadata"]["human_review_required"] = False
reject("pass with metadata.human_review_required=false", out_schema, hrm)

# mode-blind convergence break
mbr = copy.deepcopy(out01); mbr["mode_blind_confirm"]["production_mode_read"] = True
reject("pass with mode_blind_confirm.production_mode_read=true (convergence break)", out_schema, mbr)
mbc = copy.deepcopy(out01); mbc["mode_blind_confirm"]["consumed"] = "mode_a_v3_master"
reject("pass with mode_blind_confirm.consumed != 'mode_agnostic_v3_master' const", out_schema, mbc)

# route + handoff + report class
rb = copy.deepcopy(out01); rb["route_back_to"] = "motion-agent"
reject("pass with non-null route_back_to (a cleared reel routes forward)", out_schema, rb)
ht = copy.deepcopy(out01); ht["handoff_targets"] = ["publishing-agent"]
reject("pass with handoff_targets != ['localization-agent'] const", out_schema, ht)
rc = copy.deepcopy(out01); rc["metadata"]["qc_report_class"] = "terminal_preflight_fail"
reject("pass with qc_report_class 'terminal_preflight_fail' (branch/class mismatch)", out_schema, rc)
av = copy.deepcopy(out01); av["metadata"]["agent_version"] = "1.1"
reject("pass with metadata.agent_version != '1.0' const", out_schema, av)
ai = copy.deepcopy(out01); ai["metadata"]["agent_id"] = "motion-agent"
reject("pass with metadata.agent_id != 'qc-agent' const", out_schema, ai)

# ---------------------------------------------------------------- 4a. brand + URI type-system
print("\n== 4a. TYPE-SYSTEM invariants (brand anchor + platform-relative URIs) ==")
bid = copy.deepcopy(out01); bid["reel_ref"]["brand_id"] = "HOLDCO"
reject("reel_ref.brand_id != 'REINVENTED' const (entity firewall)", out_schema, bid)
pu = copy.deepcopy(out01); pu["publish_target"]["publish_queue_uri"] = "https://drive.google.com/reels/x"
reject("publish_queue_uri absolute URL (ars:// only — asset_uri_integrity)", out_schema, pu)
eh = copy.deepcopy(out01); eh["qc_report_evidence_hash"] = "NOTHEX"
reject("qc_report_evidence_hash not 64-hex", out_schema, eh)
ehc = copy.deepcopy(out01); ehc["qc_report_evidence_hash"] = "a" * 63
reject("qc_report_evidence_hash 63-hex (wrong length)", out_schema, ehc)
qf = copy.deepcopy(out01); qf["qc_pre_flags"] = ["ok_one", "ok_two", "ok_three"]
reject("qc_pre_flags below the >=4 floor (3)", out_schema, qf)
qfc = copy.deepcopy(out01); qfc["qc_pre_flags"] = ["Not_snake", "ok_two", "ok_three", "ok_four"]
reject("qc_pre_flags with a non-snake_case predicate", out_schema, qfc)
cost = copy.deepcopy(out01); cost["cost_incurred_usd"] = 0.75
reject("cost_incurred_usd above the 0.5 ceiling ($0 agent)", out_schema, cost)

# ---------------------------------------------------------------- 4b. the 3-verdict model (RESTORED reshoot)
print("\n== 4b. 3-verdict model (pass | fail | reshoot — the RESTORED third verdict) ==")
rev = copy.deepcopy(out01); rev["verdict"] = "fail"
reject("successQcReport with verdict 'fail' (branch/verdict mismatch)", out_schema, rev)
rev2 = copy.deepcopy(out01); rev2["verdict"] = "reshoot"
reject("successQcReport with verdict 'reshoot' (branch/verdict mismatch)", out_schema, rev2)
ewrong = copy.deepcopy(out03); ewrong["verdict"] = "pass"
reject("errorEnvelope with verdict 'pass' (branch/verdict mismatch)", out_schema, ewrong)
erv = copy.deepcopy(out03); erv["verdict"] = "revise"
reject("errorEnvelope verdict 'revise' (not a full-QC verdict)", out_schema, erv)
# reshoot IS representable on the error branch (the RESTORED third verdict)
rsh = copy.deepcopy(out03)
rsh["verdict"] = "reshoot"; rsh["failure_code"] = "qc_reshoot_required"
rsh["failed_check_id"] = 11; rsh["route_back_to"] = "production-coord-agent"
rsh["metadata"]["qc_report_class"] = "terminal_preflight_reshoot"
accept("errorEnvelope verdict 'reshoot' + qc_reshoot_required (the RESTORED third verdict)", out_schema, rsh)
rshc = copy.deepcopy(rsh); rshc["metadata"]["qc_report_class"] = "terminal_preflight_pass"
reject("reshoot with qc_report_class 'terminal_preflight_pass' (class/verdict mismatch)", out_schema, rshc)

# ---------------------------------------------------------------- 4c. namespace + computed routing
print("\n== 4c. 12-named + slot namespace (LARGEST in fleet) + COMPUTED route_back_to ==")
NAMED = ["upstream_motion_not_ready", "upstream_not_success", "evidence_hash_break",
         "master_unresolved", "asset_uri_integrity_failure", "brand_voice_gate_fail",
         "qc_firewall_breach", "format_spec_mismatch", "caption_spec_breach",
         "cost_ledger_overrun", "unresolved_upstream_flag", "qc_flag_surface_incomplete",
         "qc_reshoot_required", "qc_lineage_failure", "qc_agent_failed"]
for code in NAMED:
    c = copy.deepcopy(out03); c["failure_code"] = code
    # reshoot code needs matching verdict/class; keep others as fail
    if code == "qc_reshoot_required":
        c["verdict"] = "reshoot"; c["metadata"]["qc_report_class"] = "terminal_preflight_reshoot"
        c["route_back_to"] = "production-coord-agent"; c["failed_check_id"] = 11
    accept(f"errorEnvelope failure_code '{code}' representable (enum-present)", out_schema, c)
uc = copy.deepcopy(out03); uc["failure_code"] = "audio_firewall_breach"
reject("foreign failure_code 'audio_firewall_breach' (Sound's, not full QC's)", out_schema, uc)
uc2 = copy.deepcopy(out03); uc2["failure_code"] = "motion_firewall_breach"
reject("foreign failure_code 'motion_firewall_breach' (Motion's, not full QC's)", out_schema, uc2)
# the two routed pairs are DISTINCT strings, NOT folded (D8)
for pair_code in ("asset_uri_integrity_failure", "qc_flag_surface_incomplete"):
    c = copy.deepcopy(out03); c["failure_code"] = pair_code
    accept(f"routed-pair code '{pair_code}' enumerated distinctly (D8 not folded)", out_schema, c)
# route_back_to is COMPUTED: enum incl null; a foreign agent string rejected
rb_ok = copy.deepcopy(out03); rb_ok["route_back_to"] = "editor-agent"
accept("route_back_to 'editor-agent' (computed, in enum)", out_schema, rb_ok)
rb_null = copy.deepcopy(out03); rb_null["failure_code"] = "qc_lineage_failure"; rb_null["failed_check_id"] = 12; rb_null["route_back_to"] = None
accept("route_back_to null for qc_lineage_failure (forensic held)", out_schema, rb_null)
rb_bad = copy.deepcopy(out03); rb_bad["route_back_to"] = "localization-agent"
reject("route_back_to 'localization-agent' (not an upstream re-work target)", out_schema, rb_bad)
# failed_check_id bounds + attempts bounds
fci = copy.deepcopy(out03); fci["failed_check_id"] = 14
reject("failed_check_id 14 (out of the 1..13 range)", out_schema, fci)
att = copy.deepcopy(out03); att["attempts"] = 3
reject("attempts 3 (2-strike max)", out_schema, att)
slot = copy.deepcopy(out03)
slot["failure_code"] = "qc_agent_failed"; slot["failed_check_id"] = 13; slot["attempts"] = 2; slot["route_back_to"] = None
accept("valid slot qc_agent_failed (check 13, attempts 2, route null)", out_schema, slot)

# ---------------------------------------------------------------- 4d. parent_chain additive
print("\n== 4d. parent_chain held additively (output minItems 5 / maxItems 12; input maxItems 11) ==")
accept("output parent_chain 12-tuple (full-QC append)", out_schema, out01)
for n in (11, 10, 9, 8, 7, 6, 5):
    t = copy.deepcopy(out01); t["metadata"]["parent_chain"] = t["metadata"]["parent_chain"][:n]
    accept(f"output parent_chain {n}-tuple (held additively)", out_schema, t)
four = copy.deepcopy(out01); four["metadata"]["parent_chain"] = four["metadata"]["parent_chain"][:4]
reject("output parent_chain 4-tuple (below the additive floor)", out_schema, four)
thirteen = copy.deepcopy(out01)
thirteen["metadata"]["parent_chain"] = out01["metadata"]["parent_chain"] + [out01["reel_ref"]["qc_report_id"]]
reject("output parent_chain 13-tuple (above maxItems 12)", out_schema, thirteen)
# input inbound held at maxItems 11
accept("input parent_chain 11-tuple inbound (Motion chain)", in_schema, in01)
twelve_in = copy.deepcopy(in01)
twelve_in["metadata"]["parent_chain"] = twelve_in["metadata"]["parent_chain"] + [in01["metadata"]["parent_chain"][10]]
reject("input parent_chain 12-tuple (inbound maxItems 11)", in_schema, twelve_in)

# ---------------------------------------------------------------- 4e. input precondition guards
print("\n== 4e. Input guards (precondition is a runtime halt, NOT a schema reject) ==")
notready = copy.deepcopy(in01); notready["motion_spec"]["verdict"] = "fail"
reject("input motion_spec.verdict 'fail' (const motion_ready — runtime halt is upstream, but schema pins the gate)", in_schema, notready)
noterr = copy.deepcopy(in01); noterr["motion_spec"]["output_type"] = "errorEnvelope"
reject("input motion_spec.output_type 'errorEnvelope' (const successMotionSpec)", in_schema, noterr)
badfmt = copy.deepcopy(in01); badfmt["declared_format"]["platform_variants"] = []
reject("input declared_format.platform_variants empty (minItems 1)", in_schema, badfmt)
absuri = copy.deepcopy(in01); absuri["motion_spec"]["finish_target"]["v3_final_uri"] = "https://cdn.example/v3.mp4"
reject("input v3_final_uri absolute URL (ars:// only)", in_schema, absuri)
shortfloor = copy.deepcopy(in01); shortfloor["accumulated_qc_pre_flags"]["editor-agent"] = ["a_flag", "b_flag", "c_flag"]
reject("input an agent below the minItems-4 flag floor (3)", in_schema, shortfloor)
missingagent = copy.deepcopy(in01); del missingagent["accumulated_qc_pre_flags"]["sound-agent"]
reject("input missing a required upstream agent (sound-agent) in the flag surface", in_schema, missingagent)
badbrief = copy.deepcopy(in01); badbrief["brief_ref"]["brief_id"] = "not-a-brief-id"
reject("input malformed brief_id", in_schema, badbrief)
# production_mode is present-but-no-touch: a valid A/B/C value must ACCEPT
for m in ("A", "B", "C"):
    t = copy.deepcopy(in01); t["metadata"]["production_mode"] = m
    accept(f"input production_mode '{m}' accepted (present for lineage, never read)", in_schema, t)

# ---------------------------------------------------------------- 4f. gate-convergence proof
print("\n== 4f. TC-01/TC-02 mode-blind gate-convergence proof (FIVE stages deep) ==")
# Convergence compares the MODE-INVARIANT adjudication blocks. The two legitimately
# tier/census-varying surfaces are excluded per the §9 TC-02 spec ("byte-shape-identical
# downstream of the tier_richness_echo + cost-ledger blocks"): the cost_ledger envelope
# (tier-aware) and the firewall SCAN CENSUS (a data artifact of the richer text set — the
# verdict-bearing status+hits ARE compared). Everything the verdict logic touches is identical.
g1, g2 = out01["qc_gate"], out02["qc_gate"]
mode_invariant = (
    g1["brand_voice_11_point"] == g2["brand_voice_11_point"]
    and g1["format_spec"] == g2["format_spec"]
    and g1["caption_spec"] == g2["caption_spec"]
    and g1["entity_firewall_pass_13"]["status"] == g2["entity_firewall_pass_13"]["status"]
    and g1["entity_firewall_pass_13"]["hits"] == g2["entity_firewall_pass_13"]["hits"]
)
downstream = all(out01[k] == out02[k] for k in
           ["flag_adjudication", "motion_self_check_adjudication", "evidence_hash_chain",
            "mode_blind_confirm", "publish_target", "qc_measured_probe_run",
            "route_back_to", "handoff_targets"])
if mode_invariant and downstream and in01["metadata"]["production_mode"] != in02["metadata"]["production_mode"]:
    ok("TC-01 (Mode A) vs TC-02 (Mode C): mode-invariant gate-adjudication blocks identical despite different origin mode")
else:
    bad("TC-01/TC-02 convergence proof broken (gate paths differ or modes equal)")
if out01["mode_blind_confirm"]["production_mode_read"] is False and out02["mode_blind_confirm"]["production_mode_read"] is False:
    ok("both convergence fixtures attest production_mode_read:false")
else:
    bad("a convergence fixture failed the mode-blind self-attestation")
if out02["tier_richness_echo"]["tier"] == "enterprise" and out01["tier_richness_echo"]["tier"] == "pro" \
        and out02["qc_gate"]["cost_ledger"]["combined_envelope_usd"] != out01["qc_gate"]["cost_ledger"]["combined_envelope_usd"]:
    ok("the ONLY tier-aware divergence is the cost-ledger envelope (Pro 4.50 vs Enterprise 9.00) — every brand-gate rule identical")
else:
    bad("TC-02 does not isolate the cost-ledger envelope as the sole tier-aware surface")

# ---------------------------------------------------------------- 4g. TC-05 GATING firewall fixture
print("\n== 4g. TC-05 GATING fixture (13th-pass terminal firewall + self-check disagreement) ==")
blob = json.dumps(in05).lower()
if "4821 main" in blob and "principal holdco" in blob:
    ok("TC-05 input carries the injected banned tokens in the burned-in text")
else:
    bad("TC-05 input is missing an injected banned token")
d = out05.get("detail", {})
fw = d.get("entity_firewall_pass_13", {})
scd = d.get("self_check_disagreement", {})
if out05["failure_code"] == "qc_firewall_breach" and out05["failed_check_id"] == 6 \
        and out05["route_back_to"] == "motion-agent" \
        and fw.get("status") == "breach" and fw.get("hits") == 2 \
        and scd.get("motion_declared_banned_vocab_hits") == 0 and scd.get("qc_rederived_hits") == 2:
    ok("TC-05 = qc_firewall_breach (Check #6, hits 2, route motion) + self-check disagreement (declared 0 vs re-derived 2)")
else:
    bad("TC-05 does not encode the 13th-pass catch + the self-check disagreement provenance finding")
# TC-05 input motion_spec self-reported 0 (the finisher's clean claim the terminal gate overturns)
if in05["motion_spec"]["motion_self_check"]["banned_vocab_hits"] == 0:
    ok("TC-05 input Motion declared banned_vocab_hits:0 — the terminal gate re-derives and overturns it")
else:
    bad("TC-05 input Motion self-check is not the declared-0 the terminal gate must overturn")

# TC-03 completeness rule: all OTHER format sub-statuses explicitly computed (no short-circuit nulls)
sub = out03.get("detail", {}).get("format_sub_status", {})
if sub.get("variants_match_promise") is False and all(sub.get(k) is True for k in
        ("aspect_ok", "resolution_ok", "duration_in_band", "caption_burn_in_ok")):
    ok("TC-03 completeness rule: variants_match_promise false, all other format sub-statuses explicitly true")
else:
    bad("TC-03 does not honor the completeness rule (short-circuit nulls or missing sub-status)")

# TC-04 completeness-vs-closure: surface complete but a flag open
fadj = out04.get("detail", {})
if fadj.get("surface_complete") is True and fadj.get("unresolved") \
        and fadj["unresolved"][0]["agent_id"] == "editor-agent":
    ok("TC-04 accumulation-floor closure: surface_complete true, one editor-agent flag unresolved")
else:
    bad("TC-04 does not encode the complete-but-not-closed flag surface")

# ---------------------------------------------------------------- summary
print(f"\n=== RESULT: {PASS} passed, {FAIL} failed ===")
sys.exit(1 if FAIL else 0)
