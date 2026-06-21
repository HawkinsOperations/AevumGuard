from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from hoxline.cli import main
from hoxline.reviewer import compute_report_hash, verify_public_reviewer_packet


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "examples" / "reviewer" / "hoxline-public-reviewer-packet-v0.json"
PACKET_MARKDOWN = ROOT / "examples" / "reviewer" / "hoxline-public-reviewer-packet-v0.md"
SCHEMA = ROOT / "schemas" / "public-reviewer-packet-v0.schema.json"


def test_public_reviewer_packet_schema_validates_packet() -> None:
    errors = verify_public_reviewer_packet(_packet(), _schema())

    assert errors == []


def test_public_reviewer_packet_cli_passes_known_good(capsys) -> None:
    status = main(["reviewer", "verify", "--input", str(PACKET), "--schema", str(SCHEMA)])

    output = capsys.readouterr()
    assert status == 0
    assert "PASS" in output.out


def test_reviewer_packet_rejects_public_safe_status_true() -> None:
    packet = _packet()
    packet["public_safe_status"] = True
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("public_safe_status" in error for error in errors)


def test_reviewer_packet_rejects_public_proof_published_true() -> None:
    packet = _packet()
    packet["public_proof_published"] = True
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("public_proof_published" in error for error in errors)


def test_reviewer_packet_rejects_website_rendering_as_proof_true() -> None:
    packet = _packet()
    packet["website_rendering_is_proof"] = True
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("website_rendering_is_proof" in error for error in errors)


def test_reviewer_packet_rejects_green_ci_as_approval_true() -> None:
    packet = _packet()
    packet["green_ci_is_approval"] = True
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("green_ci_is_approval" in error for error in errors)


def test_reviewer_packet_rejects_human_review_not_required() -> None:
    packet = _packet()
    packet["human_review_required"] = False
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("human_review_required" in error for error in errors)


def test_reviewer_packet_rejects_operator_receipt_present_for_waiting_detections() -> None:
    packet = _packet()
    packet["detections"]["HO-DET-011"]["real_operator_receipt"] = "present"
    packet["detections"]["HO-DET-012"]["real_operator_receipt"] = "present"
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("HO-DET-011 field real_operator_receipt" in error for error in errors)
    assert any("HO-DET-012 field real_operator_receipt" in error for error in errors)


def test_reviewer_packet_rejects_blocked_claim_class_as_allowed() -> None:
    packet = _packet()
    packet["allowed_claims"].append("HO-DET-001 is runtime proven.")
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("allowed claim contains blocked claim class" in error for error in errors)


def test_reviewer_packet_rejects_stale_active_names() -> None:
    packet = _packet()
    packet["allowed_claims"].append("Hawk" + "line is ready for reviewers.")
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("stale product naming" in error for error in errors)


def test_reviewer_packet_rejects_aevumguard_outside_historical_notes() -> None:
    packet = _packet()
    packet["allowed_claims"].append("Aevum" + "Guard controls this route.")
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("prior product name is allowed only" in error for error in errors)


def test_reviewer_packet_rejects_raw_payload_keys() -> None:
    packet = _packet()
    packet["detections"]["HO-DET-011"]["raw_alert"] = "redacted"
    packet["report_hash"] = compute_report_hash(packet)

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("raw/private payload field" in error for error in errors)


def test_report_hash_is_deterministic() -> None:
    packet = _packet()

    assert compute_report_hash(packet) == packet["report_hash"]
    assert compute_report_hash(packet) == compute_report_hash(_packet())


def test_report_hash_mismatch_fails() -> None:
    packet = _packet()
    packet["report_hash"] = "0" * 64

    errors = verify_public_reviewer_packet(packet, _schema())

    assert any("report_hash mismatch" in error for error in errors)


def test_markdown_packet_contains_safe_and_blocked_claim_sections() -> None:
    text = PACKET_MARKDOWN.read_text(encoding="utf-8")

    assert "## Safe Claim" in text
    assert "## What Remains Blocked" in text
    assert "HO-DET-001 has controlled validation evidence and remains under governed review." in text
    assert "public-safe runtime proof" in text


def _packet() -> dict[str, object]:
    with PACKET.open("r", encoding="utf-8") as handle:
        return deepcopy(json.load(handle))


def _schema() -> dict[str, object]:
    with SCHEMA.open("r", encoding="utf-8") as handle:
        return json.load(handle)
