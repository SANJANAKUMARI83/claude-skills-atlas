# Safe Refactoring Prompt

```text
Refactor this codebase for {{goal}}.

Before editing:
1. Inspect the existing implementation and tests.
2. Identify behavior that must remain unchanged.
3. State the files you expect to modify.
4. Identify risks.

During editing:
- Prefer the smallest coherent change.
- Follow existing project conventions.
- Do not introduce a framework or abstraction without a concrete reason.
- Preserve public behavior unless a breaking change is explicitly requested.

After editing:
1. Review the diff.
2. Run relevant tests/checks.
3. Report exactly what changed and what was verified.
```
