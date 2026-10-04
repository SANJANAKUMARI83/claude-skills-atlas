# Skill Quality Audit

Review the Claude skill at **{{skill_path_or_content}}** for clarity, usefulness, portability, and safety.

## Review checklist
1. **Purpose:** Is the skill's job specific and easy to understand?
2. **Trigger:** Does it explain when to use the skill and when not to?
3. **Workflow:** Are the instructions ordered, actionable, and free of unnecessary repetition?
4. **Inputs and outputs:** Are required inputs and expected deliverables explicit?
5. **Examples:** Is there a realistic example that demonstrates the intended behavior?
6. **Portability:** Does it avoid hard-coded personal context, machine-specific paths, and assumptions about unavailable tools?
7. **Safety:** Does it avoid requesting secrets, unsafe actions, or unauthorized access? Are important boundaries explicit?
8. **Evidence:** Does it distinguish facts, assumptions, and unverified claims?
9. **Maintainability:** Are names, links, and references clear and likely to remain valid?
10. **Atlas conventions:** Does it follow the repository's skill template and contribution guidance?

## Output format
- **Verdict:** ready, needs minor edits, or needs substantial revision
- **Strengths:** specific and observable
- **Findings:** quote or identify the relevant section, explain the issue, and suggest a concrete fix
- **Missing tests or examples:** list only useful additions
- **Priority edits:** order the changes by impact

Do not rewrite the entire skill unless asked. Do not invent defects or claim that a skill was tested when it was only inspected. Preserve the author's intent while recommending the smallest changes that improve quality.
