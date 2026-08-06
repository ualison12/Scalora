# API Reference

## Overview

The Scalora API is implemented in FastAPI and is exposed under the base path /api/v1. It provides endpoints for authentication, company administration, CRM, finance, inventory, AI, and platform operations.

## Base URL

- Local development: http://localhost:8000/api/v1
- Docker Compose: http://localhost:8000/api/v1

## Authentication

### Login

- Endpoint: POST /auth/login
- Purpose: authenticate a user and return access and refresh tokens

### Refresh

- Endpoint: POST /auth/refresh
- Purpose: issue a new access token from a valid refresh token

### Logout

- Endpoint: POST /auth/logout
- Purpose: revoke a refresh token

### Current user

- Endpoint: GET /auth/me
- Purpose: return basic information for the current user context

## Core resource groups

### Companies

- CRUD endpoints for companies via the companies router

### Users and roles

- Manage users, roles, and permissions

### CRM

- Leads, contacts, deals, and stages

### Inventory

- Products, categories, brands, suppliers, lots, movements

### Finance

- Receivables, payables, cost centers, reports, dashboards, boletos, PIX-related flows

### AI

- Providers, agents, prompts, tools, automations, memory, chat, summaries, analyses, RAG

### Platform

- Plans, subscriptions, billing events, webhooks, SDK keys, admin operations, logs, backups, deployment metadata

## Response conventions

The API uses standard FastAPI JSON responses. Error responses are returned through FastAPI exception handling and the application middleware layer.

## OpenAPI documentation

Swagger UI and ReDoc are available through FastAPI’s built-in docs when the server is running:

- Swagger UI: /docs
- ReDoc: /redoc

## Example request

```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"secret"}'
```

## Notes

The current API is functional for the implemented modules and is suitable for iterative development. The next phase should focus on stronger authentication context, standardized error payloads, pagination, and rate limiting.
