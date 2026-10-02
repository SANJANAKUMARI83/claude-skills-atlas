# Debugging Prompt

Copy and customize:

```text
Debug this {{language}} problem.

Goal:
{{expected_behavior}}

Code:
{{code}}

Observed behavior / error:
{{error}}

Constraints:
{{constraints}}

Work in this order:
1. Identify the exact failure.
2. Explain why it happens.
3. Distinguish syntax, runtime, logic, and environment issues.
4. Give the smallest correction that fixes the problem.
5. Explain how to verify the correction.
6. Mention any separate issues you notice, but do not mix them with the root cause.

Do not rewrite unrelated parts of the code.
Do not claim the code was executed unless it was actually executed.
```
