# Research Claim Audit Prompt

```text
Audit the following research draft against the supplied sources.

Draft:
{{draft}}

Sources:
{{sources}}

For every important factual or scientific claim, create a table with:
- claim
- supporting source
- evidence found
- support level: direct / partial / contradicted / not established
- safer wording if needed

Rules:
- Do not invent citations.
- Do not infer experimental results that are absent from the source.
- Separate the source's statement from your interpretation.
- Flag numerical claims for explicit verification.
- Preserve uncertainty where the evidence is uncertain.
```
