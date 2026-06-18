# ProofCard v1

ProofCard v1 is the reviewer-facing summary for a Gauntlet v1 run. It carries the artifact identity, owner split, proof ceiling, allowed claim, blocked claims, missing evidence, and next gate.

For HO-DET-001 it also carries the public-safe candidate-review lane from the merged platform/proof references:

* `review_lane`: `PUBLIC_SAFE_CANDIDATE_REVIEW_V1`
* Review gates: `privacy_review`, `stale_review`, `evidence_linkage_review`, and `wording_approval` all remain `PENDING`.
* `public_safe_status`: `NOT_PUBLIC_SAFE`
* `runtime_active`: `false`
* `signal_observed`: `false`
* `human_review_required`: `true`
* `proof_ceiling`: `CONTROLLED_TEST_VALIDATED`
* `proof_ceiling_meaning`: `CONTROLLED_VALIDATION_ONLY`

## Reviewer Command

```powershell
python -B -m hoxline proofcard render --input examples/gauntlet/ho-det-001-gauntlet-run-v1.json
```

## What It Proves

The rendered ProofCard shows that the Gauntlet record can emit deterministic review output from local JSON only.

## What It Does Not Prove

It does not claim runtime proof, signal proof, public-safe approval, public-safe proof, customer deployment, SOCaaS deployment, production readiness, AI approval, analyst approval, final authorization, website rendering as proof, GitHub rendering as proof, green CI as approval, or case closure.

## Boundaries

* Source owner: `hawkinsoperations-detections`
* Validation owner: `hawkinsoperations-validation`
* Platform owner: `hawkinsoperations-platform`
* Proof owner: `hawkinsoperations-proof`
* Website owner: `hawkinsoperations-website`

Proof ceiling: `CONTROLLED_TEST_VALIDATED`.

No server or runtime collector is required. The website is rendering-only and cannot authorize claims.
