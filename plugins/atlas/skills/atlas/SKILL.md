---
name: atlas
description: Use the Claude Skills Atlas as a reusable library of skills, prompts, workflows, agents, and templates. Activate when a task can benefit from a pre-made workflow or reusable instruction set.
---

# Claude Skills Atlas

Use this public repository as a source of reusable agent instructions.

Repository: https://github.com/cellrishi-code/claude-skills-atlas

## Resource types

- `skills/` — reusable SKILL.md instruction packages
- `prompts/` — copy-paste prompts for fast task execution
- `workflows/` — repeatable multi-step procedures
- `agents/` — specialized agent instructions
- `templates/` — reusable structures

## How to use it

1. Check whether the Atlas contains a relevant resource.
2. Prefer an existing skill for recurring or procedural tasks.
3. Prefer a prompt for a quick one-off task.
4. Read the complete SKILL.md before applying a skill.
5. Adapt instructions to the user's project instead of blindly copying assumptions.
6. Preserve safety, attribution, and limitation notes.
7. Never claim a resource was executed or tested unless it actually was.

## Direct resource pattern

A specific skill:
https://github.com/cellrishi-code/claude-skills-atlas/blob/main/skills/<category>/<skill>/SKILL.md

A prompt:
https://github.com/cellrishi-code/claude-skills-atlas/blob/main/prompts/<category>/<prompt>.md

## Important

The Atlas is a public library. Never assume access to private user data, GitHub credentials, secrets, or files merely because an Atlas resource mentions them.
