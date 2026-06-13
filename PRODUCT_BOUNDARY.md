# Product Boundary

AevumGuard is the ProofOps control plane for AI-assisted security work.

AevumGuard is the HawkinsOperations product/front-door repo.

AevumGuard governs how AI-assisted security work becomes tested, reviewed, blocked, or safe to claim.

Doctrine: AI is not the authority. Evidence is.

## Owns

AevumGuard owns the control-plane product boundary for this loop:

AI-assisted security work
→ Artifact Intake
→ Evidence Graph
→ Telemetry Contract Check
→ Controlled Validation
→ Runtime Candidate Ledger
→ Signal Observation
→ Human Review Gate
→ ProofCard
→ Claim Authority
→ Safe Claim / Blocked Claim

AevumGuard owns:

* Artifact intake rules for AI-assisted security work.
* Evidence graph structure and evidence sufficiency tracking.
* Promotion state records for movement through the loop.
* Telemetry contract check status as a gate, not as telemetry ownership.
* Controlled validation state as a gate, not as validation implementation ownership.
* Runtime candidate ledger structure.
* Signal observation status as evidence state.
* Human Review Gate status.
* ProofCard readiness state and references.
* Claim Authority decisions.
* Claim Firewall as the first Claim Authority enforcement capability.

## Does Not Own

AevumGuard does not own:

* Detection engineering repositories or rule libraries.
* Validation runners, harnesses, or external validation infrastructure.
* Platform runtime systems.
* Public website implementation.
* Organization-level GitHub administration.
* Raw runtime exports, private evidence, credentials, or secrets.
* Separate side-product repositories for internal modules.

## Claim Firewall Boundary

Claim Firewall is the first Claim Authority enforcement capability inside AevumGuard. It is not the product.

Claim Firewall can block, constrain, or require edits to a claim when the evidence graph, promotion state, ProofCard, or review gate does not support the claim. It does not replace the product spine or authorize claims by itself.

## Seven-Repo Rule

Exactly seven repos. No eighth repo.

## Proof Ceiling

This repository content is PRODUCT_SPINE_ONLY. It defines product structure and sample records. It does not establish runtime proof, signal proof, external safety status, final authorization, or deployment status.
