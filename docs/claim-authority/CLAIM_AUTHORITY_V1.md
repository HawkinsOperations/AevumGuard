# Claim Authority v1

Claim Authority v1 evaluates structured Gauntlet evidence state before allowing or blocking claims. It does not rely only on wording matches.

## Reviewer Command

```powershell
python -B -m hoxline claim-authority decide --input examples/gauntlet/ho-det-001-gauntlet-run-v1.json
```

## What It Allows

It allows the controlled-validation claim only when artifact intake is accepted, telemetry contract check passes, and controlled validation evidence exists.

Allowed claim:

> HO-DET-001 has controlled validation evidence and remains under governed public-safe candidate review.

## What It Blocks

It blocks stronger runtime, signal, production, customer, service, public-release, approval, authorization, and disposition wording when required structured evidence is missing.

For HO-DET-001 Public-Safe Candidate Review v1, it also preserves these blockers from the merged platform/proof boundary: runtime active, runtime proven, signal observed, public-safe approved, public-safe proof, production ready, production SOC, SOC deployed, SOCaaS deployed, customer deployed, customer validated, analyst approved, AI approved, autonomous approval, final human authorization, case closed, green CI as approval, website rendering as proof, and GitHub rendering as proof.

The promotion blockers remain `privacy_review_pending`, `stale_review_pending`, `evidence_linkage_review_pending`, `wording_approval_pending`, `human_review_required`, and `proof_ceiling_controlled_validation_only`.

## What It Does Not Prove

It does not claim runtime truth, signal truth, public-safe approval, public-safe proof, production readiness, customer deployment, SOCaaS deployment, AI-approved disposition, analyst-approved disposition, final authorization, website rendering as proof, GitHub rendering as proof, green CI as approval, or case closure.

## Authority Split

Source evidence belongs to `hawkinsoperations-detections`. Validation evidence belongs to `hawkinsoperations-validation`. Platform runtime and telemetry contract state belongs to `hawkinsoperations-platform`. ProofCard and claim decisions belong to `hawkinsoperations-proof`. Website rendering belongs to `hawkinsoperations-website`.

Proof ceiling: `CONTROLLED_TEST_VALIDATED`.

No server or runtime collector is required. Public release safety is not asserted.
