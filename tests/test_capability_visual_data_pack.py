from __future__ import annotations

import json
from pathlib import Path

from claimfirewall.claim_authority import load_claim_authority_policy, scan_paths


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "examples" / "showcase" / "ho-det-001-capability-visual-data-pack-v1.json"
PACK_MARKDOWN = ROOT / "examples" / "showcase" / "ho-det-001-capability-visual-data-pack-v1.md"
PACK_DOC = ROOT / "docs" / "showcase" / "HOXLINE_CAPABILITY_VISUAL_DATA_PACK_V1.md"
SCHEMA = ROOT / "schemas" / "capability-visual-data-pack-v1.schema.json"
POLICY = ROOT / "examples" / "policies" / "default-claim-authority-policy.yml"


REQUIRED_FIELDS = {
    "showcase_id",
    "artifact_id",
    "product",
    "category",
    "doctrine",
    "proof_ceiling",
    "public_safe",
    "human_review_required",
    "current_safe_claim",
    "executive_summary",
    "positive_capabilities",
    "loop_stage_statuses",
    "generated_outputs",
    "validation_metrics",
    "contract_metrics",
    "claim_authority_metrics",
    "authority_surfaces",
    "evidence_references",
    "visual_modules",
    "website_chart_data",
    "blocked_claims_collapsed",
    "remaining_gates",
    "non_claims",
}

REQUIRED_CAPABILITY_TEXT = {
    "Hoxline can run the canonical ProofOps loop for HO-DET-001.",
    "Hoxline can emit reviewer-readable JSON.",
    "Hoxline can emit reviewer-readable Markdown.",
    "Hoxline can verify the Gauntlet full-loop output contract.",
    "Hoxline can preserve the CONTROLLED_TEST_VALIDATED proof ceiling.",
    "Hoxline can map artifact state to allowed claim wording.",
    "Hoxline can map blocked claim families to safer wording and missing evidence.",
    "Hoxline can keep runtime and signal gated when evidence is missing.",
    "Hoxline can represent authority separation across the seven-repo system.",
    "Hoxline can show one artifact, one loop, one safe claim, and blocked stronger claims.",
}

REQUIRED_CHARTS = {
    "stage_status_distribution",
    "loop_stage_status_chart",
    "capability_maturity_chart",
    "authority_surface_chart",
    "generated_outputs_chart",
    "claim_decision_chart",
    "build_timeline",
}

REQUIRED_VISUAL_MODULES = {
    "mission_control_hero",
    "proofops_loop_orbit",
    "gauntlet_execution_console",
    "capability_maturity_visual",
    "authority_constellation",
    "evidence_pipeline_timeline",
    "claim_decision_matrix",
    "generated_outputs_wall",
    "reviewer_path_timeline",
    "still_gated_panel",
    "complexity_stats_rail",
}


def test_showcase_json_exists_and_parses() -> None:
    assert PACK.exists()
    assert PACK_MARKDOWN.exists()
    assert _pack()["showcase_id"] == "ho-det-001-capability-visual-data-pack-v1"


def test_required_fields_exist() -> None:
    assert REQUIRED_FIELDS <= set(_pack())


def test_positive_capabilities_include_required_capabilities() -> None:
    capabilities = {item["capability"] for item in _pack()["positive_capabilities"]}

    assert REQUIRED_CAPABILITY_TEXT <= capabilities


def test_loop_stage_statuses_has_11_stages() -> None:
    stages = _pack()["loop_stage_statuses"]

    assert len(stages) == 11
    assert [stage["order"] for stage in stages] == list(range(1, 12))


def test_runtime_and_signal_are_not_promoted() -> None:
    stages = {stage["stage"]: stage for stage in _pack()["loop_stage_statuses"]}

    assert stages["Runtime Candidate Ledger"]["status"] == "BLOCKED"
    assert stages["Signal Observation"]["status"] == "MISSING_EVIDENCE"
    assert stages["Runtime Candidate Ledger"]["status"] != "PASS"
    assert stages["Signal Observation"]["status"] != "PASS"


def test_public_safe_and_human_review_boundaries() -> None:
    pack = _pack()

    assert pack["public_safe"] is False
    assert pack["human_review_required"] is True


def test_website_chart_datasets_exist() -> None:
    chart_data = _pack()["website_chart_data"]

    assert REQUIRED_CHARTS <= set(chart_data)
    assert all(chart_data[name] for name in REQUIRED_CHARTS)


def test_visual_modules_exist() -> None:
    modules = {module["id"] for module in _pack()["visual_modules"]}

    assert REQUIRED_VISUAL_MODULES <= modules


def test_blocked_claims_are_collapsed_not_front_loaded() -> None:
    pack = _pack()
    keys = list(pack)

    assert keys.index("blocked_claims_collapsed") > keys.index("website_chart_data")
    assert keys.index("blocked_claims_collapsed") > keys.index("visual_modules")
    assert pack["blocked_claims_collapsed"]["blocked_count"] == 23


def test_schema_matches_showcase_json_constants() -> None:
    pack = _pack()
    schema = _schema()

    for field in ("artifact_id", "product", "category", "proof_ceiling", "public_safe", "human_review_required"):
        assert schema["properties"][field]["const"] == pack[field]
    assert set(schema["required"]) <= set(pack)


def test_schema_validates_showcase_json_when_jsonschema_is_available() -> None:
    try:
        import jsonschema
    except ModuleNotFoundError:
        return

    jsonschema.validate(_pack(), _schema())


def test_claim_firewall_allows_markdown_output() -> None:
    policy = load_claim_authority_policy(POLICY)
    report = scan_paths([PACK_MARKDOWN, PACK_DOC], policy, evidence_states=["controlled_test_validated"])

    assert report.allowed
    assert report.blocked_claims == ()


def _pack() -> dict[str, object]:
    with PACK.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _schema() -> dict[str, object]:
    with SCHEMA.open("r", encoding="utf-8") as handle:
        return json.load(handle)
