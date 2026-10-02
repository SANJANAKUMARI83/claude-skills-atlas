---
name: implementation-review
description: Review an implementation against its requirements, repository conventions, correctness risks, tests, and maintainability. Use before opening a pull request or when reviewing completed work.
---

# Implementation Review

Review completed work as if another engineer must maintain it.

## Process

1. Read the task or acceptance criteria.
2. Inspect the diff and changed files.
3. Trace changed behavior through callers and dependencies.
4. Check correctness, edge cases, error handling, and compatibility.
5. Compare the implementation with nearby repository conventions.
6. Inspect or add focused tests where practical.
7. Check documentation and user-facing behavior.
8. Separate blocking issues from suggestions.

## Review order

Prioritize:

1. Functional correctness
2. Security and data safety
3. Regression risk
4. Test coverage
5. Maintainability
6. Performance
7. Style

## Rules

- Do not praise code merely because it looks clean.
- Every finding should identify evidence, impact, and a concrete fix.
- Do not request speculative abstractions without a demonstrated need.
- If no blocking issue exists, explicitly say so.

## Output

Use:

- Verdict: ready / needs changes
- Blocking findings
- Non-blocking findings
- Missing tests
- Documentation gaps
- Suggested verification commands
