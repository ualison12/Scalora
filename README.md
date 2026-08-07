# Scalora

Scalora é uma plataforma modular de operações empresariais construída para unir CRM, finanças, estoque, IA e operações de plataforma em uma experiência única. O projeto está estruturado como um monorepo com backend em FastAPI, frontend em Next.js e infraestrutura baseada em Docker.

## Visão geral

A versão atual do repositório já entrega uma base funcional para desenvolvimento e validação de cenários reais de negócios. O ecossistema inclui:

- API backend organizada por módulos de domínio
- Frontend executivo com visão consolidada de KPIs e módulos
- Infraestrutura local para API, banco de dados e interface web
- Estrutura preparada para expansão em produto SaaS e operações multi-tenant

## Status atual

O projeto encontra-se em estágio inicial, porém com uma base sólida para evolução. Os principais blocos já estão presentes:

- autenticação e gestão de usuários
- estrutura de empresas e papéis
- módulos de CRM, finanças, estoque e IA
- painel executivo no frontend
- rotas de API organizadas por domínio
- ambiente Docker para desenvolvimento local

## Arquitetura resumida

O repositório está organizado em:

- apps/api: backend FastAPI, modelos, serviços, rotas e testes
- apps/web: frontend Next.js com interface de dashboard e módulos
- docs: documentação de produto, arquitetura, banco, API e decisões
- infrastructure: Dockerfiles e configuração de implantação
- docker-compose.yml: ambiente local completo com PostgreSQL, Redis, API e web

## Stack tecnológica

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

### Infraestrutura

- Docker Compose
- PostgreSQL
- Redis
- Nginx como base para evolução de deployment

## Estrutura do repositório

```text
Scalora/
  apps/
    api/
    web/
  docs/
  infrastructure/
  docker-compose.yml
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

## Módulos principais

### CRM

Gerenciamento de leads, contatos, oportunidades e etapas de vendas.

### Financeiro

Fluxos de contas a pagar, contas a receber, centros de custo, relatórios e dashboards.

### Estoque

Produtos, categorias, marcas, fornecedores, lotes e movimentações.

### IA

Provedores, agentes, prompts, ferramentas, automações, memória, chat, resumos e análises.

### Plataforma

Planos, assinaturas, eventos de billing, webhooks, SDK, logs, backups e deploy.

## Como executar localmente

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

### Stack completo com Docker

```bash
docker compose up --build
```

A aplicação ficará disponível em:

- API: http://localhost:8000
- Frontend: http://localhost:3000
- PostgreSQL: localhost:5432
- Redis: localhost:6379

## Documentação

- [ARCHITECTURE.md](ARCHITECTURE.md)
- [DATABASE.md](DATABASE.md)
- [API.md](API.md)
- [SECURITY.md](SECURITY.md)
- [DEPLOY.md](DEPLOY.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [ROADMAP.md](ROADMAP.md)
- [CHANGELOG.md](CHANGELOG.md)

## Princípios de desenvolvimento

- manter lógica de negócio em serviços
- organizar modelos e persistência por domínio
- priorizar modularidade e extensibilidade
- manter configuração e ambientes explícitos
- documentar mudanças importantes de arquitetura e fluxo

## Licença

Consulte o arquivo de licença do repositório para informações completas.