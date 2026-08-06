# Security Guide

## Overview

Scalora includes foundational security mechanisms for authentication, password hashing, and environment-based configuration. The current implementation should be considered a baseline rather than a complete production security posture.

## Current protections

- Password hashing with bcrypt
- JWT-based access token issuance
- Refresh token records and basic session tracking
- Environment-based configuration for secret values
- Basic CORS support and request logging middleware

## Important gaps to address

- Strong secret management for production
- Multi-tenant authorization enforcement
- Rate limiting and abuse protection
- Structured audit events for sensitive actions
- TLS termination and secure headers in deployed environments
- Regular rotation of credentials and tokens

## Recommended practices

- Never commit secrets or real credentials.
- Use environment variables or a secret manager in production.
- Restrict CORS origins explicitly.
- Enforce least-privilege access for admin and platform operations.
- Keep dependencies updated and review package changes regularly.

## Incident handling

If an incident is suspected:

1. Rotate access and refresh secrets.
2. Revoke or invalidate active sessions and tokens where possible.
3. Review audit logs and recent activity.
4. Limit access temporarily if needed.
5. Document the incident and follow-up actions.

## Current status

The security layer is functional for development and early-stage deployment. Production readiness requires stronger hardening around authentication context, secrets, and operational monitoring.
