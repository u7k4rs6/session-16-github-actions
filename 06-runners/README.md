# 06: Runners

A runner is the machine that executes a GitHub Actions job.

## GitHub-hosted runners

GitHub provisions and removes the machine for each job. Examples include:

- `ubuntu-latest`
- `windows-latest`
- `macos-latest`

## Self-hosted runners

A self-hosted runner is managed by your organization. It can provide custom software or private network access, but it also requires patching, monitoring, and security controls.

Choose the smallest runner with the tools your job needs.
