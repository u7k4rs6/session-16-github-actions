# 07: Secrets

Never commit passwords, API keys, tokens, or private certificates to Git.

Store sensitive values in the repository or environment **Settings > Secrets and variables > Actions**, then reference them with the `secrets` context.

```yaml
env:
  DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

The example workflow uses `DEMO_TOKEN` only if it has been configured. Missing secrets resolve to an empty value, so the demo does not expose or invent credentials.

Prefer environment-scoped secrets for deployment credentials and grant the workflow only the permissions it needs.
