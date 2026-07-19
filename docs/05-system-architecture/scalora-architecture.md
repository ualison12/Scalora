# Scalora System Architecture

## Overview
Scalora is engineered using a modern, scalable, and highly available architecture organized as a Turbo monorepo. It ensures strict decoupling between individual microservices and frontend clients while sharing core utilities, configurations, and type definitions.

┌───────────────────┐
              │   Scalora Web     │
              │  (Next.js/React)  │
              └─────────┬─────────┘
                        │ (HTTPS / WSS)
                        ▼
              ┌───────────────────┐
              │    FastAPI API    │
              │     Gateway       │
              └────┬───────────┬──┘
                   │           │
    ┌──────────────▼───┐   ┌───▼──────────────┐
    │ PostgreSQL (Db)  │   │ Redis (Cache)    │
    └──────────────────┘   └───────────┬──────┘
                                       │
                                       ▼
                           ┌───────────────────┐
                           │  Celery Workers   │
                           │ (Background Jobs) │
                           └───────────────────┘



                           ## Stack Component Breakdown

### Monorepo Orchestration
- **Tooling:** Turborepo / pnpm Workspaces
- **Capabilities:** Fast caching, parallel execution, cross-package dependency resolution.

### Microservices & APIs
- **Core API Engine:** Python FastAPI
- **Key Characteristics:** Asynchronous request handling, built-in Pydantic data validation, OpenAPI specification auto-generation.

### Compute & Background Processing
- **Asynchronous Tasks:** Celery distributed task queue.
- **Message Broker:** Redis for real-time task queuing and low-latency key-value data caching.

### Persistence Layer
- **Relational Database:** PostgreSQL (Structured business logs, relational entity schemas, secure multi-tenant row isolation).