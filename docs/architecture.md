# Repository Architecture

Claude Skills Atlas separates reusable artifacts by type so contributors can find and reuse them quickly.

```text
skills/       Reusable SKILL.md instruction packages
prompts/      Copy-paste prompt templates
workflows/    Multi-step procedures
agents/       Specialized agent definitions
plugins/      Installable Claude Code plugins
templates/    Reusable documents, checklists, schemas, and structures
docs/         Project standards and architecture
.github/      Contribution and issue templates
```

## Design principles

### 1. Small and focused

Prefer one clear skill or prompt per file rather than a giant collection of unrelated instructions.

### 2. Discoverable

Use descriptive lowercase kebab-case names and place content under the most specific useful category.

### 3. Portable

Avoid private paths, personal context, secrets, account-specific identifiers, and assumptions that only work for one person.

### 4. Explicit

State inputs, outputs, assumptions, limitations, and examples whenever they matter.

### 5. Reviewable

A maintainer should be able to understand what changed and why from one pull request.

## Skill format

A skill should normally live in its own directory:

```text
skills/<category>/<skill-name>/SKILL.md
```

This mirrors common Claude skill packaging patterns while keeping the Atlas content domain-focused.

## Plugins

Plugins package reusable Claude Code components such as skills and agents into an installable unit. The repository includes `plugins/github-agent/`, a portable GitHub workflow plugin built around the user's authenticated `gh` CLI.
