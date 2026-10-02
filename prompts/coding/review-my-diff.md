# Review My Diff

Use this prompt before opening a pull request.

~~~text
Review my current changes against the original task.

Inspect:
- the complete diff
- relevant callers and dependencies
- existing tests
- repository conventions
- error handling and edge cases
- security-sensitive behavior
- documentation impact

Prioritize correctness and regression risk over style.

Return:
1. Blocking issues
2. Important non-blocking issues
3. Missing tests
4. Documentation gaps
5. Exact verification commands

Do not rewrite the code unless I ask. If you find no blocking issue, say so explicitly.
~~~
