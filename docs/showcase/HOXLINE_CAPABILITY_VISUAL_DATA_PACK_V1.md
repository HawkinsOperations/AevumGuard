# Hoxline Capability Visual Data Pack v1

Status: WEBSITE_READY_DATA_LAYER_V1

Product surface: Hoxline by HawkinsOperations

Proof ceiling: CONTROLLED_TEST_VALIDATED

public_safe value: false

Human review required: true

## What Hoxline Can Verify Today

Hoxline can run the canonical ProofOps loop for HO-DET-001, emit reviewer-readable JSON and Markdown, verify the Gauntlet full-loop output contract, preserve the CONTROLLED_TEST_VALIDATED proof ceiling, map artifact state to allowed claim wording, map blocked claim families to safer wording and missing evidence, and keep runtime and signal gated when evidence is missing.

The current safe claim is:

> HO-DET-001 has controlled validation evidence under stated scope and remains bounded by its proof ceiling.

## What Outputs Exist

- `examples/gauntlet/ho-det-001-full-loop-run-v0.json`
- `examples/gauntlet/ho-det-001-full-loop-run-v0.md`
- `schemas/gauntlet-full-loop-run-v0.schema.json`
- `examples/showcase/ho-det-001-capability-visual-data-pack-v1.json`
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
- Output contract tests after PR #12: 8.
- Current test suite after this data pack: 53 passed.

## What The Website Can Safely Visualize

The website can safely visualize the mission-control hero, ProofOps loop, Gauntlet execution console, capability maturity chart, authority surface map, evidence path timeline, generated outputs wall, claim decision matrix, remaining gates panel, and complexity stats rail from the JSON data pack.

Website rendering is not proof. Hoxline is not proof authority. Controlled validation proves controlled validation only.

## What Remains Gated

Runtime Candidate Ledger remains BLOCKED. This data pack does not claim runtime-active status or runtime proven status.

Signal Observation remains MISSING_EVIDENCE. This data pack does not claim signal observed status.

public_safe remains false. This data pack does not claim public-safe proof.

human_review_required remains true. This data pack does not claim AI approval, analyst approval, final authorization, or case closure.

Business and legal surfaces remain gated. This data pack does not claim production-ready status, SOCaaS-ready status, SOCaaS deployed status, customer deployed status, revenue, legal availability, trademark clearance, LLC formation, customer traction, or product-market fit.

## Chart Datasets

- `stage_status_distribution`
- `loop_stage_status_chart`
- `capability_maturity_chart`
- `authority_surface_chart`
- `generated_outputs_chart`
- `claim_decision_chart`
- `build_timeline`

## Visual Modules To Build

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

## What Not To Claim

This data pack does not claim runtime, signal, public-safe proof, production, SOCaaS, customer deployment, AI approval, analyst approval, final authorization, legal availability, revenue, product-market fit, proof authority, or case closure.
