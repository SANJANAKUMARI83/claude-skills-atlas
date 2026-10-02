# Use Claude Skills Atlas in Your AI Agent

Claude Skills Atlas is a public library. You do not need access to the author's GitHub account to use it.

## Claude Code

```text
/plugin marketplace add cellrishi-code/claude-skills-atlas
/plugin install claude-skills-atlas@claude-skills-atlas
```

## Clone the library

```bash
git clone https://github.com/cellrishi-code/claude-skills-atlas.git
cd claude-skills-atlas
```

Choose resources from `skills/`, `prompts/`, `workflows/`, `agents/`, and `templates/`.

## Copy one skill

Copy a complete skill directory containing `SKILL.md` into the skills directory supported by your agent.

Example:

```text
skills/coding/code-review/SKILL.md
```

## Use a pre-made prompt

Open a prompt under `prompts/`, replace its `{{placeholders}}`, and paste it into your AI agent.

## Direct GitHub access

Skills: https://github.com/cellrishi-code/claude-skills-atlas/tree/main/skills

Prompts: https://github.com/cellrishi-code/claude-skills-atlas/tree/main/prompts

## Design principle

Skills are reusable behavior. Prompts are fast one-off instructions. Workflows are repeatable processes. Agents are specialized roles. Templates help contributors create new resources.

Resources should remain useful outside Claude Skills Atlas whenever possible.
