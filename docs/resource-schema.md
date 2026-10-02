# Resource Metadata Schema

Atlas resources use lightweight metadata so future catalogues and websites can index them.

Recommended frontmatter:

```yaml
---
name: code-review
title: Code Review
type: skill
domain: coding
difficulty: intermediate
tags: [review, debugging]
intended_use: Review source code for correctness and maintainability.
---
```

Required concepts are **name**, **type**, **domain**, **intended_use**, and the resource **path** (derived from Git).

Allowed types: skill, prompt, workflow, agent, template.

Keep metadata short, factual, and stable. Contributors may omit optional fields such as difficulty and tags.
