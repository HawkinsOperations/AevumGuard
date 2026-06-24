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


## Runtime Candidate Review Lane

ProofCard v1 can also represent a private runtime candidate review packet when platform evidence exists but public proof promotion is not approved.

This lane is for private reviewer routing only. It maps source ownership, telemetry contract, controlled validation, private runtime observation, sanitized packet verification, scheduled collector inclusion, claim ceiling, blocked claims, and the next human review gate without publishing raw evidence.

HO-DET-010 is the current bounded example for this lane:

* Source owner: `hawkinsoperations-detections`.
* Validation owner: `hawkinsoperations-validation`.
* Runtime and scheduled-collector mechanics owner: `hawkinsoperations-platform`.
* Telemetry contract: Windows Security EventChannel account and local-group management events.
* Runtime truth: private VM108-scoped signal evidence and verified private packet exist.
* Schedule truth: included in the standing private collector scope with HO-DET-009, HO-DET-011, and HO-DET-012.
* `public_safe_status`: `NOT_PUBLIC_SAFE`.
* `human_review_required`: `true`.
* `ai_disposition_authority`: `false`.

Allowed internal claim:

> HO-DET-010 has private VM108-scoped runtime signal evidence, a verified private packet, and standing private collector inclusion. It remains NOT_PUBLIC_SAFE pending governed review.

This lane does not publish execution IDs, raw Wazuh alerts, endpoint logs, command lines, generated credentials, private payloads, or packet contents. It does not create public promotion authority and does not raise any public claim ceiling.
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
