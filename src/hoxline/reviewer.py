from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
from typing import Any


SCHEMA_VERSION = "hoxline-public-reviewer-packet-v0"
SCHEMA_ID = "https://hawkinsoperations.dev/hoxline/schemas/public-reviewer-packet-v0.schema.json"
PRODUCT = "Hoxline by HawkinsOperations"
DOCTRINE = "AI is not the authority. Evidence is."
PUBLIC_SAFE_STATUS = "NOT_PUBLIC_SAFE"
PROOF_CEILING_PUBLIC = "CONTROLLED_TEST_VALIDATED"
PROOF_CEILING_PRIVATE_REFERENCE = "PRIVATE_CONTROLLED_RUNTIME_PROOF"
SAFE_CLAIM = "HO-DET-001 has controlled validation evidence and remains under governed review."

CANONICAL_LOOP = [
    "AI-assisted security work",
    "Artifact Intake",
    "Evidence Graph",
    "Telemetry Contract Check",
    "Controlled Validation",
    "Runtime Candidate Ledger",
    "Signal Observation",
    "Human Review Gate",
    "ProofCard",
    "Claim Authority",
    "Safe Claim / Blocked Claim",
]

REQUIRED_AUTHORITY_SURFACES = {
    ".github": "routing only",
    "detections": "source truth",
    "validation": "behavior truth",
    "platform": "contracts/mechanics",
    "proof": "claim authority",
    "website": "rendering only",
    "hoxline": "product/control route",
}

REQUIRED_TOP_LEVEL_FIELDS = {
    "$schema",
    "schema_version",
    "generated_at_utc",
    "product",
    "doctrine",
    "public_safe_status",
    "public_proof_published",
    "website_rendering_is_proof",
    "green_ci_is_approval",
    "human_review_required",
    "proof_ceiling_public",
    "proof_ceiling_private_reference",
    "authority_surfaces",
    "detections",
    "product_loop",
    "allowed_claims",
    "blocked_claims",
    "missing_evidence",
    "reviewer_paths",
    "validation_commands",
    "report_hash",
}

BLOCKED_ALLOWED_CLAIM_PATTERNS = [
    r"\bruntime[- ]proven\b",
    r"\bruntime\s+proof\b",
    r"\bsignal\s+observed\b",
    r"\bproduction[- ]ready\b",
    r"\bcustomer\s+deployed\b",
    r"\bcustomer\s+validated\b",
    r"\bSOCaaS[- ]ready\b",
    r"\bSOCaaS\s+deployed\b",
    r"\bSOCaaS\s+available\b",
    r"\bautonomous\s+SOC\b",
    r"\bfleet-wide\s+coverage\b",
    r"\bpublic-safe\s+runtime\s+proof\b",
    r"\bpublic\s+runtime\s+proof\b",
    r"\bpublic\s+signal\s+proof\b",
    r"\bAI[- ]approved\b",
    r"\banalyst[- ]approved\b",
    r"\bfinal\s+(human\s+)?authorization\b",
    r"\bcase[- ]closed\b",
    r"\bcase\s+closure\b",
]

REQUIRED_BLOCKED_CLAIMS = [
    "runtime proven",
    "signal observed",
    "public-safe runtime proof",
    "production ready",
    "customer deployed",
    "SOCaaS deployed",
    "AI approved",
    "analyst approved",
    "final authorization",
    "case closed",
    "fleet-wide coverage",
    "public proof promotion",
]

BANNED_PAYLOAD_KEYS = {
    "alert",
    "alerts",
    "raw_alert",
    "raw_alerts",
    "raw_wazuh_alert",
    "raw_wazuh_alerts",
    "raw_payload",
    "raw_payloads",
    "payload",
    "payloads",
    "private_payload",
    "private_payloads",
    "private_route_dump",
    "private_route_dumps",
    "private_route_contents",
    "route_dump",
    "route_dumps",
    "secret",
    "secrets",
    "token",
    "tokens",
    "credential",
    "credentials",
    "command_line",
    "command_lines",
}

STALE_NAME_PATTERNS = [
    re.compile(r"\bHawk" + r"line\b", re.IGNORECASE),
    re.compile(r"\bHox\s+" + r"Line\b", re.IGNORECASE),
    re.compile(r"\bAvant" + r"Guard\b", re.IGNORECASE),
]
PRIOR_NAME_PATTERN = re.compile(r"\bAevum" + r"Guard\b", re.IGNORECASE)


class ReviewerPacketError(ValueError):
    """Raised when a reviewer packet cannot be loaded."""


def verify_public_reviewer_packet_file(input_path: Path, schema_path: Path) -> list[str]:
    schema = _load_json(schema_path)
    packet = _load_json(input_path)
    return verify_public_reviewer_packet(packet, schema)


def verify_public_reviewer_packet(packet: dict[str, Any], schema: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    if schema is not None:
        _validate_schema(schema, errors)
    _validate_top_level(packet, errors)
    _validate_authority_surfaces(packet, errors)
    _validate_detections(packet, errors)
    _validate_claim_boundaries(packet, errors)
    _validate_payload_boundary(packet, errors)
    _validate_stale_names(packet, errors)
    _validate_report_hash(packet, errors)
    return errors


def compute_report_hash(packet: dict[str, Any]) -> str:
    canonical = deepcopy(packet)
    canonical.pop("report_hash", None)
    encoded = json.dumps(canonical, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return sha256(encoded).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ReviewerPacketError(f"input must be a JSON object: {path}")
    return data


def _validate_schema(schema: dict[str, Any], errors: list[str]) -> None:
    if schema.get("$id") != SCHEMA_ID:
        errors.append(f"schema $id must be {SCHEMA_ID}")
    if schema.get("title") != "Hoxline Public Reviewer Packet v0":
        errors.append("schema title must be Hoxline Public Reviewer Packet v0")
    required = schema.get("required")
    if not isinstance(required, list):
        errors.append("schema required must be a list")
        return
    missing = sorted(REQUIRED_TOP_LEVEL_FIELDS - set(required))
    if missing:
        errors.append(f"schema required missing fields: {', '.join(missing)}")


def _validate_top_level(packet: dict[str, Any], errors: list[str]) -> None:
    missing = sorted(REQUIRED_TOP_LEVEL_FIELDS - set(packet))
    if missing:
        errors.append(f"packet missing required fields: {', '.join(missing)}")

    expected = {
        "schema_version": SCHEMA_VERSION,
        "product": PRODUCT,
        "doctrine": DOCTRINE,
        "public_safe_status": PUBLIC_SAFE_STATUS,
        "public_proof_published": False,
        "website_rendering_is_proof": False,
        "green_ci_is_approval": False,
        "human_review_required": True,
        "proof_ceiling_public": PROOF_CEILING_PUBLIC,
        "proof_ceiling_private_reference": PROOF_CEILING_PRIVATE_REFERENCE,
    }
    for field, value in expected.items():
        if packet.get(field) != value:
            errors.append(f"field {field} must be {value!r}")

    if packet.get("product_loop") != CANONICAL_LOOP:
        errors.append("product_loop must match the canonical Hoxline loop")

    for field in ("allowed_claims", "blocked_claims", "missing_evidence", "reviewer_paths", "validation_commands"):
        if not isinstance(packet.get(field), list) or not packet.get(field):
            errors.append(f"{field} must be a non-empty list")


def _validate_authority_surfaces(packet: dict[str, Any], errors: list[str]) -> None:
    surfaces = packet.get("authority_surfaces")
    if surfaces != REQUIRED_AUTHORITY_SURFACES:
        errors.append("authority_surfaces must preserve the seven-surface public boundary")


def _validate_detections(packet: dict[str, Any], errors: list[str]) -> None:
    detections = packet.get("detections")
    if not isinstance(detections, dict):
        errors.append("detections must be an object")
        return

    required_ids = {"HO-DET-001", "HO-DET-011", "HO-DET-012"}
    missing_ids = sorted(required_ids - set(detections))
    if missing_ids:
        errors.append(f"detections missing required ids: {', '.join(missing_ids)}")
        return

    ho_det_001 = detections.get("HO-DET-001")
    if not isinstance(ho_det_001, dict):
        errors.append("HO-DET-001 must be an object")
    else:
        expected = {
            "public_state": PROOF_CEILING_PUBLIC,
            "public_safe": False,
            "private_runtime_reference_available": True,
            "private_runtime_reference_public_boundary": "HASH_REFERENCE_ONLY_NOT_PUBLIC_PROOF",
            "canonical_private_packet_digest": "589e4220b73cc26115629281f29fe34c17950e539454881734802392729ec2f9",
            "historical_noncanonical_packet_digest": "78100a2e72b5ca5f1866f4bfba48d3b48dc0512eef8620d0eed1fe3c854cc891",
            "safe_public_claim": SAFE_CLAIM,
        }
        for field, value in expected.items():
            if ho_det_001.get(field) != value:
                errors.append(f"HO-DET-001 field {field} must be {value!r}")

    for detection_id in ("HO-DET-011", "HO-DET-012"):
        item = detections.get(detection_id)
        if not isinstance(item, dict):
            errors.append(f"{detection_id} must be an object")
            continue
        expected = {
            "public_state": "WAITING_FOR_REAL_OPERATOR_INPUT",
            "fixture_private_runtime_path": True,
            "real_operator_receipt": "missing",
            "remote_wazuh_discovery_result": "marker_hits_without_governed_execution_id",
            "public_safe": False,
        }
        for field, value in expected.items():
            if item.get(field) != value:
                errors.append(f"{detection_id} field {field} must be {value!r}")


def _validate_claim_boundaries(packet: dict[str, Any], errors: list[str]) -> None:
    allowed_claims = packet.get("allowed_claims")
    if isinstance(allowed_claims, list):
        if SAFE_CLAIM not in allowed_claims:
            errors.append("allowed_claims must contain the safe HO-DET-001 controlled-validation claim")
        for claim in allowed_claims:
            if not isinstance(claim, str):
                errors.append("allowed_claims must contain only strings")
                continue
            for pattern in BLOCKED_ALLOWED_CLAIM_PATTERNS:
                if re.search(pattern, claim, flags=re.IGNORECASE):
                    errors.append(f"allowed claim contains blocked claim class: {claim}")
                    break

    blocked_claims = packet.get("blocked_claims")
    if isinstance(blocked_claims, list):
        observed = {claim for claim in blocked_claims if isinstance(claim, str)}
        missing = [claim for claim in REQUIRED_BLOCKED_CLAIMS if claim not in observed]
        if missing:
            errors.append(f"blocked_claims missing required claim classes: {', '.join(missing)}")


def _validate_payload_boundary(packet: dict[str, Any], errors: list[str]) -> None:
    for path, key, _value in _walk(packet):
        lowered_key = key.lower()
        if lowered_key in BANNED_PAYLOAD_KEYS:
            errors.append(f"raw/private payload field is not allowed: {path}")


def _validate_stale_names(packet: dict[str, Any], errors: list[str]) -> None:
    for path, _key, value in _walk(packet):
        if not isinstance(value, str):
            continue
        for pattern in STALE_NAME_PATTERNS:
            if pattern.search(value):
                errors.append(f"stale product naming is not allowed outside historical compatibility notes: {path}")
        if PRIOR_NAME_PATTERN.search(value) and not _is_historical_compatibility_note(path, value):
            errors.append(f"prior product name is allowed only in historical compatibility notes: {path}")


def _is_historical_compatibility_note(path: str, value: str) -> bool:
    lowered_path = path.lower()
    lowered_value = value.lower()
    return "historical_compatibility" in lowered_path and "prior working name" in lowered_value and "current product" in lowered_value


def _validate_report_hash(packet: dict[str, Any], errors: list[str]) -> None:
    observed = packet.get("report_hash")
    if not isinstance(observed, str) or not re.fullmatch(r"[0-9a-f]{64}", observed):
        errors.append("report_hash must be a lowercase SHA-256 hex digest")
        return
    expected = compute_report_hash(packet)
    if observed != expected:
        errors.append(f"report_hash mismatch: expected {expected}")


def _walk(value: Any, path: str = "$") -> list[tuple[str, str, Any]]:
    items: list[tuple[str, str, Any]] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            items.append((child_path, str(key), child))
            items.extend(_walk(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            child_path = f"{path}[{index}]"
            items.append((child_path, str(index), child))
            items.extend(_walk(child, child_path))
    return items
