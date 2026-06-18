from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from hoxline.cli import main
from hoxline.gauntlet import CANONICAL_LOOP, verify_gauntlet_run_v1


ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / "examples" / "gauntlet" / "ho-det-001-gauntlet-run-v1.json"
OVERCLAIM = ROOT / "examples" / "gauntlet" / "ho-det-001-gauntlet-run-v1-overclaim.json"
SCHEMA = ROOT / "schemas" / "gauntlet-run-v1.schema.json"
V0_RUN = ROOT / "examples" / "gauntlet" / "ho-det-001-full-loop-run-v0.json"
V0_SCHEMA = ROOT / "schemas" / "gauntlet-full-loop-run-v0.schema.json"


def test_gauntlet_v1_schema_and_example_are_valid() -> None:
    schema = _json(SCHEMA)
    run = _json(RUN)

    assert schema["$id"] == "https://hawkinsoperations.dev/hoxline/schemas/gauntlet-run-v1.schema.json"
    assert verify_gauntlet_run_v1(run, schema) == []
    assert [stage["stage"] for stage in run["loop_stages"]] == CANONICAL_LOOP
    assert run["review_lane"] == "PUBLIC_SAFE_CANDIDATE_REVIEW_V1"
    assert run["public_safe_status"] == "NOT_PUBLIC_SAFE"
    assert run["runtime_active"] is False
    assert run["signal_observed"] is False
    assert run["privacy_review"] == "PENDING"
    assert run["stale_review"] == "PENDING"
    assert run["evidence_linkage_review"] == "PENDING"
    assert run["wording_approval"] == "PENDING"
    assert run["proof_ceiling_meaning"] == "CONTROLLED_VALIDATION_ONLY"
    assert run["proof_packet_reference"]["packet_path"] == "proof/records/HO-DET-001-PUBLIC-SAFE-CANDIDATE-REVIEW-V1.md"
    assert run["platform_contract_reference"]["contract_path"] == "contracts/public-status-source-contract-v1.json"


def test_gauntlet_v1_cli_verify_passes_bounded_example(capsys) -> None:
    status = main(["gauntlet", "verify", "--input", str(RUN), "--schema", str(SCHEMA)])

    output = capsys.readouterr()
    assert status == 0
    assert "Hoxline Gauntlet verify: PASS" in output.out
    assert "proof_ceiling: CONTROLLED_TEST_VALIDATED" in output.out
    assert "public_safe_status: NOT_PUBLIC_SAFE" in output.out
    assert "runtime proof is not asserted" in output.out
    assert "next_gate: human_review_gate" in output.out


def test_gauntlet_v1_cli_verify_fails_overclaim_example(capsys) -> None:
    status = main(["gauntlet", "verify", "--input", str(OVERCLAIM), "--schema", str(SCHEMA)])

    output = capsys.readouterr()
    assert status == 1
    assert "allowed claim overstates proof boundary" in output.out
    assert "allowed_claims must contain the controlled-validation safe claim" in output.out


def test_candidate_review_cannot_promote_runtime_signal_or_public_safe() -> None:
    run = deepcopy(_json(RUN))
    run["runtime_active"] = True
    run["signal_observed"] = True
    run["public_safe_status"] = "PUBLIC_SAFE"

    errors = verify_gauntlet_run_v1(run, _json(SCHEMA))

    assert "runtime_active must remain false for candidate review" in errors
    assert "signal_observed must remain false for candidate review" in errors
    assert "public_safe_status must be NOT_PUBLIC_SAFE" in errors


def test_v0_gauntlet_verify_remains_compatible(capsys) -> None:
    status = main(["gauntlet", "verify", "--input", str(V0_RUN), "--schema", str(V0_SCHEMA)])

    output = capsys.readouterr()
    assert status == 0
    assert "Hoxline Gauntlet verify: PASS" in output.out


def test_runtime_or_signal_observed_without_evidence_fails() -> None:
    run = deepcopy(_json(RUN))
    run["runtime_candidate_ledger"]["observed"] = True
    run["signal_observation"]["observed"] = True

    errors = verify_gauntlet_run_v1(run, _json(SCHEMA))

    assert "runtime_candidate_ledger cannot be observed without evidence_refs" in errors
    assert "signal_observation cannot be observed without evidence_refs" in errors


def _json(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)
