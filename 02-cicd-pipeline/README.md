# 02: CI/CD Pipeline

A pipeline is a repeatable sequence of automated checks and delivery steps.

```text
Source
  |
  v
Build -> Test -> Security scan -> Package -> Deploy staging -> Verify -> Deploy production
```

## Good pipeline properties

- Fast feedback early in the pipeline
- Reproducible commands and pinned dependencies
- No secrets committed to the repository
- An approval or protected environment before production
- Logs and a clear failure status

The calculator project uses the first part of this pipeline. Its GitHub Actions job installs `requirements.txt` and runs the test suite.
