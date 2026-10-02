---
name: codebase-understanding
description: Build a reliable mental model of an unfamiliar repository before making changes. Use when entering a new codebase, investigating architecture, or when the user asks where a feature belongs.
---

# Codebase Understanding

Build understanding before proposing edits. Prefer evidence from the repository over assumptions.

## Process

1. Identify entry points, package/build files, configuration, tests, and documentation.
2. Map the relevant directory structure.
3. Trace the execution path for the requested feature or bug.
4. Identify important data models, interfaces, dependencies, and integration boundaries.
5. Search for existing implementations before proposing new ones.
6. Record constraints, conventions, and likely regression points.
7. Summarize the model in a compact form before changing code.

## Rules

- Read targeted files before broad exploration.
- Do not invent architecture that is not supported by repository evidence.
- Prefer existing abstractions over introducing parallel ones.
- Distinguish observed facts from hypotheses.
- If the change crosses multiple layers, state the dependency order.

## Output

Return:

- Repository map
- Relevant execution/data flow
- Existing patterns to reuse
- Constraints and risks
- Proposed change locations
- Verification plan
