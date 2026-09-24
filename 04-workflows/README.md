# 04: Workflows

A workflow is a YAML file that defines when automation runs and what it does.

Important parts:

- `name`: the workflow name shown in GitHub
- `on`: events that start the workflow
- `permissions`: the minimum token permissions
- `jobs`: one or more groups of steps
- `runs-on`: the runner image for a job
- `steps`: commands or reusable actions

Common triggers include `push`, `pull_request`, `workflow_dispatch`, and schedules with `cron`.

Keep workflows small and give each step a clear name so failures are easy to diagnose.
