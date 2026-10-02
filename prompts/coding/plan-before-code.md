# Plan Before Code

Use this prompt when a coding task is large enough that implementation without a plan could create unnecessary rework.

~~~text
Before editing code:

1. Inspect the repository structure and relevant files.
2. Identify existing abstractions, tests, configuration, and conventions related to the task.
3. Restate the requested behavior and list assumptions.
4. Produce a short implementation plan with file-level changes.
5. Identify edge cases and regression risks.
6. Define the verification steps.

Do not modify files yet.

Wait for approval unless the user explicitly asked you to proceed autonomously.
~~~
