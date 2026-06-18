# Hoxline Gauntlet v1

Hoxline Gauntlet v1 is a laptop-runnable product-engine loop for one bounded artifact: `HO-DET-001`.

It covers:

AI-assisted security work -> Artifact Intake -> Evidence Graph -> Telemetry Contract Check -> Controlled Validation -> Runtime Candidate Ledger -> Signal Observation -> Human Review Gate -> ProofCard -> Claim Authority -> Safe Claim / Blocked Claim.

## Reviewer Commands

```powershell
python -B -m hoxline gauntlet verify --input examples/gauntlet/ho-det-001-gauntlet-run-v1.json --schema schemas/gauntlet-run-v1.schema.json
python -B -m hoxline gauntlet summarize --input examples/gauntlet/ho-det-001-gauntlet-run-v1.json
python -B -m hoxline claim-authority decide --input examples/gauntlet/ho-det-001-gauntlet-run-v1.json
python -B -m hoxline proofcard render --input examples/gauntlet/ho-det-001-gauntlet-run-v1.json
```

No server is required. No runtime collector is required.

## Source Routes

Downstream reviewers can use `examples/gauntlet/ho-det-001-gauntlet-v1-source-manifest.json` as the machine-readable route index for the v1 examples, schemas, reviewer docs, and CLI commands.

## Public-Safe Candidate Review v1

Gauntlet v1 now carries the merged platform/proof candidate-review state as Hoxline modeling only:

* `review_lane`: `PUBLIC_SAFE_CANDIDATE_REVIEW_V1`
* `review_version`: `v1`
* `privacy_review`, `stale_review`, `evidence_linkage_review`, `wording_approval`: `PENDING`
* `public_safe_status`: `NOT_PUBLIC_SAFE`
* `runtime_active`: `false`
* `signal_observed`: `false`
* `human_review_required`: `true`
* `proof_ceiling`: `CONTROLLED_TEST_VALIDATED`
* `proof_ceiling_meaning`: `CONTROLLED_VALIDATION_ONLY`

The platform reference is `hawkinsoperations-platform#64` at merge commit `c49a95e2b9f2e6b5fa118c03dfc68f8827981c82`. The proof reference is `hawkinsoperations-proof#82` at merge commit `68798e43855e34a15df06d9a2bc9d6ac71d6746d`. Hoxline stores those as references only; it does not take over platform ledger authority or proof authority.

## What It Proves

The command proves that the local Gauntlet v1 record preserves the product-loop shape, owner split, proof ceiling, missing evidence list, blocked claims, and next gate.

Allowed claim:

> HO-DET-001 has controlled validation evidence and remains under governed public-safe candidate review.

## What It Does Not Prove

It does not claim runtime truth, signal truth, public-safe approval, public-safe proof, customer deployment, SOCaaS deployment, production readiness, AI-approved disposition, analyst-approved disposition, final authorization, website rendering as proof, GitHub rendering as proof, green CI as approval, or case closure.

## Authority Split

* Source owner: `hawkinsoperations-detections`
* Validation owner: `hawkinsoperations-validation`
* Platform owner: `hawkinsoperations-platform`
* Proof owner: `hawkinsoperations-proof`
* Website owner: `hawkinsoperations-website`

The website boundary is rendering-only. The website may display approved records; it cannot authorize claims or create proof.

Proof ceiling: `CONTROLLED_TEST_VALIDATED`.

Public release safety is not asserted.
