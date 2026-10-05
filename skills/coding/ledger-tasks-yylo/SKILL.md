---
name: ledger-tasks-yylo
category: coding
tags: [task-management, kanban, cli, agents, workflow, tracking]
description: Track coding-agent work in a durable Git-backed task ledger (YYLO Ledger) so plans, status, and dependencies survive across sessions instead of living only in chat history.
---

# Ledger Tasks (YYLO)

## Purpose

Give a coding agent a persistent, queryable task store: planned work, status changes, dependencies, and history are recorded durably and read back on demand instead of being reconstructed from conversation memory.

## When to use

- Multi-session projects where task state must outlive a single conversation.
- Planning work that needs explicit dependencies (start B only after A) and blocked states.
- Any request for a kanban board, task list, or work ledger rather than a prose status update.
- The YYLO CLI is available (`npm install -g @yylo/cli`) and the project is initialized (a `.juno_task/` directory is present).

## Instructions

1. Run `yy ledger --help` first; the installed help is authoritative for the runtime.
2. Read before writing: `yy ledger record search --projection summary --limit 20 -f json` lists current tasks. Never guess record IDs.
3. Create tasks with `yy ledger create "{{task description}}" --status todo --tags {{project-tags}}`.
4. Move work forward with explicit status transitions (`backlog` → `todo` → `in_progress` → `done`) and record blockers with `--blocked-by {{task_id}}`.
5. Before reporting work as done, re-read the task record and check its acceptance notes. The ledger is the source of truth, not memory.
6. Prefer commands that return mutation receipts. Never hand-edit ledger store files or bypass the CLI.

## Inputs

- Short task descriptions, optional tags, desired status, and dependency task IDs.
- Record IDs (`task_...`) returned by earlier create or list calls.

## Outputs

- JSON task records containing IDs, status, tags, dependencies, and timestamps.
- Board-style summaries from `yy ledger list` (statuses, counts, ordering) suitable for quoting in replies.

## Example

```bash
yy ledger create "Add retry logic to uploader" --status todo --tags backend,reliability
# -> { "id": "{{task_id}}", "status": "todo", ... }

yy ledger update {{task_id}} --status in_progress
yy ledger update {{task_id}} --status done
yy ledger list --status todo,in_progress --limit 10
```

## Limitations

- Requires the YYLO CLI and an initialized project; without them, fall back to a plain checklist file the user nominates.
- Cross-project access is opt-in via registry configuration; the default scope is the current project only.
- Models tasks, dependencies, and typed records deliberately — not a replacement for issue trackers with rich UIs or permissions.

## Attribution

Adapted from the `ledger-tasks-yylo` skill in [yylo-dev/yylo-skills](https://github.com/yylo-dev/yylo-skills) (MIT).
