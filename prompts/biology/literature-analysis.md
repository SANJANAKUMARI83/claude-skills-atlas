# Biology Literature Analysis Prompt

## Purpose

Help a reader analyze a biology paper without inventing experimental details or unsupported conclusions.

## Prompt

```text
Analyze the following biology paper as a research assistant.

Paper:
{{paper_or_abstract}}

Focus:
{{question}}

Produce:
1. Research question and hypothesis
2. Biological system / organism
3. Methods and experimental design
4. Main findings
5. Evidence supporting each major claim
6. Important controls
7. Limitations and possible confounders
8. Two follow-up experiments
9. A concise summary for {{audience}}

Separate what the paper explicitly reports from your interpretation.
Do not invent methods, results, sample sizes, or mechanisms that are not supported by the provided text.
```
