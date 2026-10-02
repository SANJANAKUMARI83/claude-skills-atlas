# Claude Code Task Breakdown Prompt

```text
I need to implement:

{{task}}

Before changing files:
1. Inspect the repository and identify the relevant files.
2. Explain the current implementation briefly.
3. Break the task into small verifiable steps.
4. Identify dependencies, risks, and edge cases.
5. Tell me what you need to confirm if an important requirement is ambiguous.

Do not start editing until the plan is clear.

After implementation:
- inspect the diff
- run relevant tests
- report what changed
- report exactly what was verified
```
