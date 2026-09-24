# 05: Jobs and Steps

A workflow contains jobs. Each job runs on a runner and contains ordered steps.

Jobs run in parallel by default. Use `needs` when one job must finish before another starts.

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python -m pytest -q

  package:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - run: echo "Package after tests pass"
```

Use actions for reusable setup, and use `run` for shell commands specific to your project.
