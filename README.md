# Session 16: GitHub Actions

This session introduces CI/CD concepts and GitHub Actions using a small Python calculator project.

## What you will learn

- How to structure a small Python project
- How to write tests with `pytest`
- How to create a GitHub Actions workflow
- How to run the same checks locally and in CI
- How workflows, jobs, steps, runners, and secrets fit together

## Lessons

| Folder | Topic |
| --- | --- |
| [`01-ci-vs-cd`](01-ci-vs-cd/) | Continuous integration vs continuous delivery and deployment |
| [`02-cicd-pipeline`](02-cicd-pipeline/) | Pipeline stages and promotion flow |
| [`03-github-actions`](03-github-actions/) | First GitHub Actions workflow |
| [`04-workflows`](04-workflows/) | Workflow triggers and structure |
| [`05-jobs-and-steps`](05-jobs-and-steps/) | Jobs, steps, dependencies, and outputs |
| [`06-runners`](06-runners/) | GitHub-hosted and self-hosted runners |
| [`07-secrets`](07-secrets/) | Secure values in workflows |

## Project structure

```text
session-16-github-actions/
├── .github/workflows/ci.yml
├── 01-ci-vs-cd/
├── 02-cicd-pipeline/
├── 03-github-actions/
├── 04-workflows/
├── 05-jobs-and-steps/
├── 06-runners/
├── 07-secrets/
├── app/
│   ├── __init__.py
│   └── calculator.py
├── tests/test_calculator.py
├── build.sh
├── requirements.txt
└── README.md
```

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pytest -q
python app/calculator.py
```

The calculator workflow runs automatically when changes are pushed or a pull request is opened against `main`. The lesson workflows under the numbered folders are examples. GitHub only executes workflow files from the repository-level `.github/workflows` directory.
