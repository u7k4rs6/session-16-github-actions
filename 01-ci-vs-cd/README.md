# 01: CI vs CD

## Continuous Integration

Continuous Integration (CI) means frequently merging small changes and automatically checking them with a build and tests.

Typical CI checks are:

1. Check out the code
2. Install dependencies
3. Run linting and tests
4. Report the result

## Continuous Delivery

Continuous Delivery keeps the application ready to release. A successful pipeline packages the application and makes it available for a controlled deployment.

## Continuous Deployment

Continuous Deployment automatically releases every change that passes the pipeline to a target environment.

```text
commit -> build -> test -> package -> deploy to staging -> approval -> production
```

CI validates the change. CD moves a validated change toward users.
