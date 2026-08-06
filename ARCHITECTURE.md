# Architecture

## Overview

Scalora is a monorepo platform for operations, commerce, and AI-assisted workflows. The current implementation is organized around a FastAPI backend, a Next.js frontend, and a Docker-based runtime for local development and deployment.

## High-level structure

- Backend: Python 3.13+ with FastAPI, SQLAlchemy, Pydantic, and pytest
- Frontend: Next.js 15 with React 19 and TypeScript
- Data layer: PostgreSQL for production-oriented deployments and SQLite for local/test execution
- Runtime: Docker Compose with PostgreSQL, Redis, API, and web services

## Runtime topology

```text
Browser / Mobile Client
        |
        v
Next.js Web App
        |
        v
FastAPI API
  |      |      |
  |      |      +-> AI module
  |      |      +-> Platform module
  |      +-> Inventory module
  +-> CRM module
  +-> Finance module
        |
        v
PostgreSQL / SQLite
        |
        v
Redis (planned for caching and queues)
```

## Backend architecture

The backend follows a modular domain-driven layout under app/modules. Each module typically contains:

- api/routes: FastAPI routers
- services: business logic
- repositories: persistence access
- schemas: request/response validation
- models: SQLAlchemy entities
- tests: module-level verification

The central application entrypoints are:

- app/main.py: FastAPI application creation and middleware
- app/api/router.py: global router composition
- app/database.py: shared metadata and import registration
- app/core/config.py: environment-driven settings
- app/core/security.py: password hashing and JWT helpers

## Domain modules

### Authentication and users

- Login, logout, refresh token flows
- Company-scoped user access
- Session and audit logging support

### CRM

- Leads, contacts, stages, and deals

### Inventory

- Products, categories, brands, suppliers, lots, movements

### Finance

- Payables, receivables, cost centers, payments, dashboards, reports

### AI

- Providers, agents, prompts, tools, automations, memories, chat, summaries, analyses, RAG

### Platform

- Plans, subscriptions, billing events, webhooks, SDK keys, admin users, logs, backups, deployment metadata

## Frontend architecture

The web application is a thin UI layer over the API. Current pages include:

- Home dashboard
- Modules overview
- Admin operations
- AI module playground-style view

The frontend uses a component-based layout and CSS-driven cards, grids, and badges for the current dashboard experience.

## Cross-cutting concerns

### Configuration

Configuration comes from environment variables and the settings object in app/core/config.py. A sample environment file is maintained at the repository root.

### Authentication

The API currently supports JWT-based access tokens and refresh tokens with password hashing via bcrypt.

### Logging and errors

The application exposes a basic request logging middleware and exception handler. Production deployments should extend this with structured logs, correlation IDs, and external sinks.

### Testing

The backend test suite covers core services and module flows. The current suite is executed with pytest.

## Design principles

- Keep business logic in services
- Keep persistence concerns in repositories
- Encourage modular extension by domain
- Prefer explicit configuration and clear environment boundaries
- Keep API routes composable and consistent

## Current maturity

The codebase is now functional as a foundation platform, with modules operating together and a dashboard frontend available. The next improvement waves should focus on production hardening, multi-tenant authorization, stronger observability, and deployment automation.
