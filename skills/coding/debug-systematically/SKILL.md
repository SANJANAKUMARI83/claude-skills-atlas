---
name: debug-systematically
description: Diagnose software failures systematically instead of guessing. Use for bugs, failing tests, unexpected output, crashes, regressions, and inconsistent behavior.
---

# Debug Systematically

Treat debugging as evidence gathering and hypothesis elimination.

## Process

1. Reproduce the failure when possible.
2. Capture the exact error, input, environment, and expected behavior.
3. Minimize the failing case.
4. Trace backward from the observable failure to the earliest incorrect state.
5. Generate a small set of competing hypotheses.
6. Test the cheapest hypothesis that can distinguish them.
7. Apply the smallest correct fix.
8. Re-run the original reproduction and relevant regression tests.
9. Explain the root cause, not only the patch.

## Rules

- Never change multiple unrelated things before verifying the cause.
- Do not replace an error with silent fallback behavior unless intended.
- Preserve useful diagnostic information.
- Treat intermittent failures as evidence about timing, state, concurrency, caching, or environment.
- If the cause cannot be established, label it unresolved rather than guessing.

## Output

Return:

- Reproduction
- Observed vs expected behavior
- Root cause
- Minimal fix
- Verification
- Remaining uncertainty
