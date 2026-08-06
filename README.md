# Scalora

Scalora is a modular business operating system for companies that need CRM, finance, inventory, AI, and platform operations in a single product experience.

## Overview

The project is organized as a monorepo composed of:

- Backend API built with FastAPI and SQLAlchemy
- Web frontend built with Next.js and React
- Infrastructure and deployment assets through Docker Compose
- Domain modules for CRM, finance, inventory, AI, and platform operations

## Current capabilities

### Product areas

- Authentication and user management
- Company and role-based access structure
- CRM: leads, contacts, deals, and stages
- Inventory: products, categories, brands, suppliers, lots, movements
- Finance: payables, receivables, dashboards, reports, and payment-related flows
- AI: providers, agents, prompts, tools, automations, memory, analysis, summaries, and chat
- Platform: plans, subscriptions, billing events, webhooks, SDK keys, admin tools, logs, backups, and deployments

### User experience

- Executive dashboard with KPI cards and module overview
- Dark-themed UI layout
- Modular navigation for admin and AI scenarios

## Repository structure

```text
Scalora/
  apps/
    api/            # FastAPI backend
    web/            # Next.js frontend
  docs/            # Product, architecture, and design documentation
  docker-compose.yml
  AUDIT.md
  README.md
  ARCHITECTURE.md
  DATABASE.md
  API.md
  SECURITY.md
  DEPLOY.md
  CONTRIBUTING.md
  ROADMAP.md
  CHANGELOG.md
```

## Technology stack

### Backend

- Python 3.13+
- FastAPI
- SQLAlchemy
- Pydantic
- pytest

### Frontend

- Next.js 15
- React 19
- TypeScript

### Infrastructure

- Docker Compose
- PostgreSQL
- Redis
- Nginx (planned/operational groundwork)

## Getting started

### Backend

```bash
cd apps/api
pip install -r requirements.txt
python -m pytest -q
```

### Frontend

```bash
cd apps/web
npm install
npm run dev
```

### Full stack with Docker

```bash
docker compose up --build
```

## Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md)
- [DATABASE.md](DATABASE.md)
- [API.md](API.md)
- [SECURITY.md](SECURITY.md)
- [DEPLOY.md](DEPLOY.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [ROADMAP.md](ROADMAP.md)
- [CHANGELOG.md](CHANGELOG.md)

## Status

Scalora is currently in an early but functional foundation stage. The platform already includes modular backend services, a working API surface, the start of a web experience, and a documented roadmap for maturation into a production-ready system.

## License

See the repository license file for details.