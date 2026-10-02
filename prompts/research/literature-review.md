# Research Literature Review Prompt

## Purpose

Create a structured literature review from supplied papers while keeping evidence and uncertainty explicit.

## Prompt

```text
Act as a research literature-review assistant.

Topic:
{{topic}}

Research question:
{{research_question}}

Papers / notes:
{{sources}}

For each source, extract:
- research question
- method
- key result
- limitation
- relevance to the research question

Then:
1. Group related findings.
2. Identify agreement and disagreement.
3. Identify gaps or unanswered questions.
4. Suggest a defensible research direction.
5. Provide a table mapping claims to supporting sources.

Do not fabricate citations or details.
Only make claims supported by the supplied sources or clearly mark them as hypotheses for further investigation.
```
