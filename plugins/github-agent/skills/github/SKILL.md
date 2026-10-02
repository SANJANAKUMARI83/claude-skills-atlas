---
name: github
description: Use GitHub safely through the GitHub CLI (gh). Use when the user asks to inspect a GitHub repository, issue, pull request, branch, commit, workflow run, create or update GitHub content, or open a pull request.
---

# GitHub Agent

Use the GitHub CLI as the portable interface to GitHub. Do not ask the user to paste repository contents when the local checkout or authenticated `gh` CLI can provide them.

## Preconditions

1. Check that `gh` is installed:
   `gh --version`
2. Check authentication:
   `gh auth status`
3. If authentication is missing, tell the user to run `gh auth login`. Never ask for or store a personal access token in chat, files, prompts, or environment examples.
4. Prefer the current repository when the user is working inside a Git checkout. Otherwise require an explicit `OWNER/REPO` or GitHub URL.

## Read-only workflow

For repository inspection:
- `gh repo view OWNER/REPO --json nameWithOwner,description,defaultBranchRef,url`
- `gh api repos/OWNER/REPO/contents/PATH`
- `gh issue list --repo OWNER/REPO`
- `gh issue view NUMBER --repo OWNER/REPO`
- `gh pr list --repo OWNER/REPO`
- `gh pr view NUMBER --repo OWNER/REPO --comments`
- `gh pr diff NUMBER --repo OWNER/REPO`
- `gh run list --repo OWNER/REPO`
- `gh run view RUN_ID --repo OWNER/REPO --log-failed`

Use `--json` when structured data is useful. For large repositories, inspect targeted paths instead of dumping the entire tree.

## Git workflow

Before changing anything:
1. Inspect `git status --short --branch`.
2. Confirm the repository and current branch.
3. Read relevant files and existing contribution guidance.
4. Make the smallest change that satisfies the request.
5. Run the most relevant tests, lint, type checks, or build.
6. Review `git diff --check` and `git diff`.
7. Never commit secrets, tokens, `.env` files, credentials, or generated private data.

## Branches and commits

- Never rewrite `main` or another protected branch.
- Create a descriptive branch for changes:
  `git switch -c <type>/<short-description>`
- Prefer Conventional Commit messages, for example:
  `feat: add GitHub issue triage workflow`
- Before pushing, verify the remote:
  `git remote -v`
- Push the branch and set its upstream:
  `git push -u origin <branch>`

## Pull requests

When the user asks for a PR:
1. Push the branch.
2. Inspect the final diff.
3. Create the PR with:
   `gh pr create --base main --head <branch> --title "<title>" --body-file <file>`
4. Include:
   - Summary
   - Why the change is useful
   - Tests/checks run
   - Any limitations or follow-up work
5. Return the PR URL and state.

Do not claim that a PR is merged unless GitHub reports `MERGED`.

## Issues

For issue work:
- Search before creating duplicates: `gh issue list --search "keywords"`
- Create with `gh issue create` only after confirming the repository and request.
- When closing an issue, use the documented reason and summarize what resolved it.

## Reviews

For pull-request review:
1. Read the PR description and changed files.
2. Inspect the diff.
3. Check CI status.
4. Look for correctness, security, tests, compatibility, and maintainability.
5. Separate confirmed defects from suggestions.
6. Do not approve a PR merely because it looks plausible.

## Safety

GitHub actions can have real external effects. Treat these as confirmation points when the user did not explicitly request them:
- merging or closing a PR
- deleting branches, issues, releases, or repositories
- force-pushing
- changing repository permissions or secrets
- triggering deployments or production workflows

Never expose authentication tokens or private repository data in output.

## Output

For GitHub operations, report:
- repository
- branch/PR/issue affected
- files or resources changed
- checks performed
- links when available
- anything that still requires the user's action
