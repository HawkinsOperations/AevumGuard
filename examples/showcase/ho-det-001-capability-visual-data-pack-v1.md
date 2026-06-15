# HO-DET-001 Capability Visual Data Pack v1

Product: Hoxline by HawkinsOperations

Category: ProofOps

Proof ceiling: CONTROLLED_TEST_VALIDATED

public_safe value: false

Human review required: true

## What Hoxline Can Verify Today

Hoxline can run the HO-DET-001 ProofOps loop, emit reviewer-readable JSON, emit reviewer-readable Markdown, verify the Gauntlet output contract, preserve the controlled-validation proof ceiling, map artifact state to allowed claim wording, map blocked claim families to safer wording and missing evidence, and keep runtime and signal gated when evidence is missing.

Safe claim:

> HO-DET-001 has controlled validation evidence from controlled positive and negative process-creation fixtures and remains under review.

## What Outputs Exist

- `examples/gauntlet/ho-det-001-full-loop-run-v0.json`
- `examples/gauntlet/ho-det-001-full-loop-run-v0.md`
- `schemas/gauntlet-full-loop-run-v0.schema.json`
- `examples/showcase/ho-det-001-capability-visual-data-pack-v1.json`
- `examples/showcase/ho-det-001-capability-visual-data-pack-v1.md`
- `schemas/capability-visual-data-pack-v1.schema.json`

This v1 pack is checked in as static JSON and Markdown. A future non-website
follow-up can add `python -B -m hoxline gauntlet showcase ...`; until then, the
website should consume the checked-in JSON data pack.

## What Passed

- Canonical loop stages: 11.
- Controlled validation positives: 7.
- Controlled validation negatives: 7.
- Matched positives: 7.
- Missed positives: 0.
- False-positive negatives: 0.
- Current test suite after this data pack: 53 passed.
- Claim Firewall allows the showcase Markdown.

## What The Website Can Safely Visualize

The website can render a mission-control hero, ProofOps loop, Gauntlet execution console, capability maturity visual, authority constellation, evidence pipeline timeline, claim decision matrix, generated outputs wall, reviewer path timeline, still-gated panel, and complexity stats rail.

Website rendering is not proof. Hoxline is not proof authority. Controlled validation proves controlled validation only.

## Chart Datasets

- `stage_status_distribution`
- `loop_stage_status_chart`
- `capability_maturity_chart`
- `authority_surface_chart`
- `generated_outputs_chart`
- `claim_decision_chart`
- `build_timeline`

## Visual Modules

- `mission_control_hero`
- `proofops_loop_orbit`
- `gauntlet_execution_console`
- `capability_maturity_visual`
- `authority_constellation`
- `evidence_pipeline_timeline`
- `claim_decision_matrix`
- `generated_outputs_wall`
- `reviewer_path_timeline`
- `still_gated_panel`
- `complexity_stats_rail`

## What Remains Gated

This data pack does not claim runtime-active status or runtime proven status. Runtime Candidate Ledger remains BLOCKED.

This data pack does not claim signal observed status. Signal Observation remains MISSING_EVIDENCE.

This data pack does not claim public-safe proof. public_safe remains false.

This data pack does not claim AI approval, analyst approval, final authorization, or case closure. human_review_required remains true.

This data pack does not claim production-ready status, SOCaaS-ready status, SOCaaS deployed status, customer deployed status, revenue, legal availability, trademark clearance, LLC formation, customer traction, or product-market fit.

## What Not To Claim

This data pack does not claim runtime, signal, public-safe proof, production, SOCaaS, customer deployment, AI approval, analyst approval, final authorization, legal availability, revenue, product-market fit, proof authority, or case closure.
