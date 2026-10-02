---
name: implementation-planner
description: Use when a coding task is large enough to require repository inspection, a plan, affected files, risks, and verification before implementation.
---

# Implementation Planner

## Goal

Turn a coding request into an implementation plan before changing code.

## Instructions

1. Inspect the repository structure and relevant configuration.
2. Identify the smallest set of files likely to change.
3. Trace existing patterns before proposing a new abstraction.
4. State assumptions instead of silently inventing requirements.
5. Produce:
   - objective
   - current architecture relevant to the task
   - files to inspect/change
   - implementation steps
   - risks and edge cases
   - verification plan
6. If important information is missing, ask focused questions before implementation.
7. Do not modify files unless the user explicitly asks for implementation.

## Output

Keep the plan concrete enough that another developer can execute it without rediscovering the repository.

## Source note

Inspired by recurring community recommendations to separate planning from implementation and keep work focused. See `docs/community-sources.md`.
