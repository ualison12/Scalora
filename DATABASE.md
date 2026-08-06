# Database Guide

## Overview

Scalora uses a relational data model centered on companies, users, roles, and domain-specific entities for CRM, inventory, finance, AI, and platform operations.

## Supported database engines

- Development and tests: SQLite
- Production-oriented deployments: PostgreSQL

The repository includes PostgreSQL support in Docker Compose and SQLAlchemy configuration suitable for both engines.

## Core entities

### Core platform

- Company
- User
- Role
- Permission
- RefreshToken
- Session
- AuditLog

### CRM

- Lead
- Contact
- Deal
- Stage

### Inventory

- Product
- Category
- Brand
- Supplier
- Lot
- Movement

### Finance

- Payable
- Receivable
- Category
- CostCenter
- Boleto
- PIX transaction metadata
- BillingEvent

### AI

- AIProvider
- AIAgent
- PromptTemplate
- AITool
- AIAutomation
- AIMemory
- AIDocument

### Platform / operations

- Plan
- Subscription
- SDKKey
- AdminUser
- PlatformLog
- Backup
- Deployment
- Webhook

## Relationship patterns

The current model layer uses SQLAlchemy declarative models with relationships where needed, including:

- users belonging to a company
- refresh and session records linked to users
- audit logs for user and platform actions
- domain-specific references from inventory, finance, and platform modules to the owning company or user

## Migration strategy

The project includes Alembic support and migration files under apps/api/alembic. The recommended workflow is:

1. Update the SQLAlchemy models.
2. Create a new Alembic revision.
3. Review the generated migration.
4. Apply it in development or staging.
5. Validate rollback strategy before production.

## Configuration

Connection strings are provided via environment variables. The key variable is DATABASE_URL. The default development configuration is SQLite, while Docker Compose uses PostgreSQL.

## Operational guidance

- Use PostgreSQL for production-grade deployments.
- Keep backups for business-critical tables.
- Add indexes on high-volume lookup columns over time.
- Review foreign keys and cascade rules as the data model grows.
- Keep migration history versioned in source control.

## Current status

The database layer is functional and can support the current module set. Future work should focus on stronger constraints, indexes, partitioning strategy for large reporting datasets, and broader migration coverage.
