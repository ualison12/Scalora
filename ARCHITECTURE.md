# Arquitetura do projeto

## Visão geral

Scalora é um monorepo de plataforma operacional composta por um backend modular, um frontend executivo e uma camada de infraestrutura para desenvolvimento e implantação. A arquitetura atual foi pensada para separar os domínios de negócio por módulos, permitindo evolução incremental sem acoplar demais os serviços.

## Objetivos de arquitetura

- separar claramente contexto de negócio e infraestrutura
- manter módulos por domínio, como CRM, financeiro, estoque, IA e plataforma
- facilitar a evolução para um modelo SaaS com múltiplos tenants
- reduzir acoplamento entre API, frontend e persistência

## Arquitetura geral

```text
Usuário / Browser
        |
        v
Frontend Next.js
        |
        v
API FastAPI
  |   |   |   |   |
  |   |   |   |   +-> Plataforma
  |   |   |   +-> IA
  |   |   +-> Estoque
  |   +-> Financeiro
  +-> CRM
        |
        v
PostgreSQL / SQLite
        |
        v
Redis (infraestrutura e evolução de cache/filas)
```

## Estrutura técnica

### Backend

O backend está localizado em apps/api e segue uma organização modular sob app/modules. Cada módulo é responsável por uma área específica do negócio e pode incluir:

- api: rotas FastAPI
- services: regras de negócio
- schemas: validação de entrada e saída
- models: entidades SQLAlchemy
- repositories: acesso à persistência
- tests: cobertura de comportamento relevante

### Frontend

O frontend está localizado em apps/web e tem como função oferecer uma visão operacional e executiva do sistema. A UI atual concentra-se em:

- painel executivo
- visão por módulos
- navegação administrativa
- cenários de IA e operações

## Pontos centrais do backend

Os arquivos principais do backend são:

- app/main.py: criação da aplicação FastAPI e middleware
- app/api/router.py: composição global das rotas
- app/core/config.py: configuração por ambiente
- app/core/security.py: helpers de autenticação e segurança
- app/database.py: modelos e integração de metadata compartilhada

## Módulos de domínio

### Autenticação e identidade

- login, refresh e logout
- gestão de usuários
- empresas e papéis
- controle de sessão e auditoria básica

### CRM

- leads
- contatos
- oportunidades
- estágios de vendas

### Financeiro

- contas a pagar e receber
- centros de custo
- boletos e fluxo de pagamentos
- relatórios e dashboards

### Estoque

- produtos
- categorias
- marcas
- fornecedores
- lotes
- movimentações

### IA

- provedores
- agentes
- prompts
- ferramentas
- automações
- memória
- chat
- summaries e analysis
- RAG

### Plataforma

- planos e assinaturas
- billing e webhooks
- SDK keys
- logs e backups
- deploy e administração

## Padrões de design

- separação entre camada de API, serviços e persistência
- utilização de rotas organizadas por módulo
- configuração por variáveis de ambiente
- tratamento de erros e logging centralizado no middleware
- abstração de regras de negócio em serviços para facilitar testes e extensão

## Considerações transversais

### Configuração

As configurações são carregadas por meio de um settings central, permitindo que a aplicação se adapte a diferentes ambientes sem alterar o código.

### Autenticação

A camada atual utiliza JWT e refresh tokens, além de hashing para senhas. Esse padrão é adequado para a fase atual de desenvolvimento e evolução.

### Observabilidade

A aplicação já possui logging básico de requests e um handler genérico para exceções. O próximo passo é evoluir para logs estruturados, tracing e alertas.

### Testes

A suíte backend contém testes para módulos principais, como CRM, finanças, estoque, IA, IAM e runtime.

## Estado de maturidade

A base do produto já está funcional e preparada para crescer. As prioridades de evolução são:

- reforço de autorização multi-tenant
- hardening de segurança e secrets
- maior cobertura de migrações e dados
- observabilidade operacional e monitoramento
- automação de deploy e operação

## Direção futura

A arquitetura atual é uma base sólida para uma plataforma empresarial mais completa, com foco em escalabilidade, governança e experiência operacional.
