# Deployment Guide

## Overview

Scalora can be run locally with Docker Compose and can also be adapted to a production deployment model on a VM, Kubernetes, or a managed container platform.

## Local development

### Prerequisites

- Docker and Docker Compose
- Python 3.13+
- Node.js 20+

### Start the stack

```bash
docker compose up --build
```

This starts:

- PostgreSQL on port 5432
- Redis on port 6379
- API on port 8000
- Web app on port 3000

## Environment variables

The application expects variables such as:

- DATABASE_URL
- SECRET_KEY
- ALGORITHM
- ACCESS_TOKEN_EXPIRE_MINUTES
- APP_ENV
- APP_DEBUG

Refer to the repository root environment example for defaults and placeholders.

## Production checklist

- Use strong secrets and rotate them regularly.
- Run PostgreSQL instead of SQLite.
- Enable TLS and reverse proxy termination.
- Configure backups and retention policies.
- Add monitoring and alerting for API uptime and error rate.
- Avoid using development defaults in production.

## Container notes

The current Docker Compose setup includes health checks for PostgreSQL and the API container. Additional hardening should include:

- dedicated production images
- non-root container execution where possible
- separate secrets management
- explicit resource limits

## Rollout and rollback

- Keep migrations in source control.
- Apply database migrations before rolling out new API versions.
- Test deployment changes in staging first.
- Maintain versioned backup artifacts for rollback readiness.

## Current status

The deployment stack is operational for local development and can be extended for staging or production use. The next improvements should focus on production hardening and automated release pipelines.
