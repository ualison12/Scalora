# Banco de dados

## Visão geral

O modelo de dados do Scalora é relacional e foi pensado para suportar empresas, usuários, permissões e domínios operacionais como CRM, financeiro, estoque, IA e plataforma. A estrutura atual já organiza entidades principais e estabelece a base para expansão de regras e integrações.

## Motores suportados

- desenvolvimento e testes: SQLite
- ambiente orientado a produção: PostgreSQL

O repositório já inclui suporte a PostgreSQL via Docker Compose e uma configuração compatível com SQLAlchemy.

## Entidades principais

### Plataforma e identidade

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

### Estoque

- Product
- Category
- Brand
- Supplier
- Lot
- Movement

### Financeiro

- Payable
- Receivable
- CostCenter
- Boleto
- eventos e dados de cobrança

### IA

- AIProvider
- AIAgent
- PromptTemplate
- AITool
- AIAutomation
- AIMemory
- AIDocument

### Plataforma e operações

- Plan
- Subscription
- SDKKey
- AdminUser
- PlatformLog
- Backup
- Deployment
- Webhook

## Padrões de relacionamento

O modelo atual utiliza SQLAlchemy com relacionamentos explícitos onde há dependência estrutural. Os principais padrões observados são:

- usuários ligados a empresas
- refresh tokens e sessões associados a usuários
- auditoria ligada a ações de usuário e plataforma
- entidades de negócio referenciando a empresa ou usuário proprietário

## Estratégia de migrações

As migrações são gerenciadas com Alembic e armazenadas em apps/api/alembic. O fluxo recomendado é:

1. ajustar o modelo SQLAlchemy
2. gerar uma nova revisão do Alembic
3. revisar o diff da migração
4. aplicar em ambiente de desenvolvimento ou staging
5. validar rollback antes de produção

## Configuração

A conexão com o banco é controlada pela variável DATABASE_URL. Em desenvolvimento, o padrão é SQLite; em ambientes Docker ou produção, o projeto já está preparado para PostgreSQL.

## Boas práticas operacionais

- usar PostgreSQL em ambientes reais
- manter backups regulares das tabelas críticas
- adicionar índices para colunas de consulta frequente
- revisar chaves estrangeiras e cascatas conforme o volume crescer
- manter histórico de migrações versionado em repositório

## Estado atual

A camada de dados já suporta o conjunto atual de módulos e é suficiente para evolução incremental. As próximas melhorias devem incluir:

- mais restrições e integridade explícita
- índices para consultas de alto volume
- cobertura maior de migrações
- estratégia de particionamento para relatórios extensos

## Recomendações para produção

- separar ambientes por banco e credenciais
- evitar uso de dados de desenvolvimento em produção
- implementar políticas de retenção e backup
- revisar rotinas de manutenção e recuperação de falhas
