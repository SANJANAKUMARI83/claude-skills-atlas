# GitHub Agent Plugin

A portable GitHub workflow plugin for Claude Code.

It gives an agent a consistent workflow for working with GitHub through the official `gh` CLI: inspect repositories, read issues and PRs, review diffs, inspect GitHub Actions, create branches and commits, and open pull requests.

## Requirements

- Claude Code with plugin support
- Git
- GitHub CLI (`gh`)
- A GitHub account authenticated with `gh auth login`

The plugin does not contain credentials and never asks users to put tokens into project files.

## Install for development

From a clone of this repository:

```bash
claude --plugin-dir ./plugins/github-agent
```

Or install the plugin from a configured Claude Code marketplace.

## Use

The skill is available as:

```text
/github-agent:github
```

Examples:

```text
/github-agent:github inspect the current repository and summarize open PRs

/github-agent:github review PR #42, including the diff and CI status

/github-agent:github create a branch for the requested fix and open a PR
```

The plugin also provides a `github-operator` subagent for GitHub-focused tasks.

## Authentication

Run:

```bash
gh auth login
gh auth status
```

Authentication stays with the user's GitHub CLI configuration. The plugin never stores credentials.

## Design

The plugin is deliberately CLI-based rather than hard-coding a single GitHub account or token. That makes the workflow portable across users and repositories while leaving authorization under the user's GitHub account.

## Security

Review the plugin before installing it. GitHub operations can change external state. Destructive operations and permission changes require explicit user intent.

## License

MIT
