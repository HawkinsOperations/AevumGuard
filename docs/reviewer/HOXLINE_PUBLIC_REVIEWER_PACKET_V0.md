# Hoxline Public Reviewer Packet v0

This page explains how to read `examples/reviewer/hoxline-public-reviewer-packet-v0.json`.

## Purpose

The packet is a public-boundary current-state reviewer artifact. It is designed to be impressive because it is strict: it shows what exists, what is verified, what remains private, and which claims stay blocked.

It is not runtime proof, not signal proof, not public proof promotion, and not approval.

## Current State

* Product: Hoxline by HawkinsOperations.
* Doctrine: AI is not the authority. Evidence is.
* Public-safe status: `NOT_PUBLIC_SAFE`.
* Public proof published: `false`.
* Website rendering is proof: `false`.
* Green CI is approval: `false`.
* Human review required: `true`.
* Public proof ceiling: `CONTROLLED_TEST_VALIDATED`.
* Private reference ceiling: `PRIVATE_CONTROLLED_RUNTIME_PROOF`.

## Authority Surfaces

* `.github`: routing only.
* `hawkinsoperations-detections`: source truth.
* `hawkinsoperations-validation`: behavior truth.
* `hawkinsoperations-platform`: contracts and mechanics.
* `hawkinsoperations-proof`: claim authority.
* `hawkinsoperations-website`: rendering only.
* `hoxline`: product and control route.

## Detection Readout

HO-DET-001 has controlled validation evidence and remains under governed review. Private runtime reference digests are included only as hash references. Hash references are not public proof and do not make the route approved for public release claims.

HO-DET-011 and HO-DET-012 remain waiting on real operator input. Marker hits without governed execution IDs do not establish governed operator receipt evidence. The safe next step is a controlled operator run with an execution ID, sanitized Wazuh export, and operator attestation.

## Safe Claims

* HO-DET-001 has controlled validation evidence and remains under governed review.
* Hoxline controls how AI-assisted security work becomes tested, reviewed, blocked, or safe to claim.

## Blocked Claims

The packet does not claim runtime proven, signal observed, public-safe runtime proof, production ready, customer deployed, SOCaaS deployed, AI approved, analyst approved, final authorization, case closed, fleet-wide coverage, or public proof promotion.

## How To Inspect

Reviewers should inspect:

* `docs/reviewer/HOXLINE_REVIEWER_START_HERE.md`
* `docs/gauntlet/HO_DET_001_GAUNTLET_RUN.md`
* `examples/reviewer/hoxline-public-reviewer-packet-v0.json`
* `examples/reviewer/hoxline-public-reviewer-packet-v0.md`
* `schemas/public-reviewer-packet-v0.schema.json`

The verifier entrypoint is `hoxline reviewer verify`. It validates the packet against the schema and fail-closed public-boundary invariants.

## Promotion Boundary

No ledger append happened. No public proof was published. No schedule was enabled. No case was closed. No public-safe promotion happened.

Codex is labor. Evidence is authority. Raylee approves promotion.
