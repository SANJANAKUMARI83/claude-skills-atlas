# Plan → Implement → Verify

A reusable workflow for non-trivial coding tasks.

## Phase 1 — Understand

Inspect the repository, relevant files, existing tests, and conventions.

## Phase 2 — Plan

Write a short implementation plan containing affected files, behavior changes, risks, and verification.

## Phase 3 — Implement

Make the smallest coherent change that satisfies the requirement.

## Phase 4 — Verify

Inspect the diff, run focused tests, then broader checks when appropriate.

## Phase 5 — Report

Return:
- what changed
- files changed
- tests/checks run
- results
- unresolved risks

This workflow is deliberately conservative: exploration and verification are first-class steps.
