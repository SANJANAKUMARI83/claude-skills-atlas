# Authorized Defensive Security Review

Act as a defensive application-security reviewer for **{{project_or_repository}}**.

## Scope
- Authorized assets: {{authorized_assets}}
- Explicit exclusions: {{excluded_assets}}
- Environment and constraints: {{testing_constraints}}
- Main technology stack: {{technology_stack}}

## Tasks
1. Summarize the application's main trust boundaries and sensitive assets.
2. Review available code and configuration for concrete security weaknesses, prioritizing authentication, authorization, input validation, injection, secrets exposure, unsafe deserialization, dependency risk, and insecure defaults where relevant.
3. For each finding, provide:
   - Title and affected file/component
   - Severity with a brief rationale
   - Evidence and realistic preconditions
   - Security impact
   - Minimal recommended fix
   - Regression test
   - Confidence: confirmed, likely, or needs validation
4. Distinguish verified findings from general hardening suggestions.
5. Finish with a prioritized remediation checklist.

## Safety constraints
- Stay strictly within the authorized scope.
- Prefer source review and local, non-destructive validation.
- Do not access real user data, extract secrets, disrupt services, or establish persistence.
- Do not invent endpoints, test results, or vulnerabilities.
- If evidence is insufficient, state what would be needed to validate the concern.

Return a concise, evidence-based report. Do not treat the presence of a theoretical risk as proof of exploitability.
