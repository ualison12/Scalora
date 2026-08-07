# API Reference

## Visão geral

A API do Scalora é construída com FastAPI e exposta sob o prefixo /api/v1. Ela centraliza o acesso às operações de autenticação, empresas, CRM, financeiro, estoque, IA e plataforma.

## Base URL

- desenvolvimento local: http://localhost:8000/api/v1
- ambiente Docker: http://localhost:8000/api/v1

## Documentação interativa

Quando a API estiver rodando, os endpoints abaixo estão disponíveis:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Autenticação

### POST /auth/login

Autentica um usuário e retorna um token de acesso.

### POST /auth/refresh

Emite um novo access token com base em um refresh token válido.

### POST /auth/logout

Revoga a sessão ou refresh token associado.

### GET /auth/me

Retorna informações do usuário autenticado no contexto atual.

## Endpoints por módulo

### Empresas

- rotas de empresas e contextos organizacionais
- suporte a estrutura baseada em company

### Usuários e permissões

- gestão de usuários
- papéis e permissões
- integração com o contexto da empresa

### CRM

- leads
- contatos
- deals
- stages
- dashboard de CRM

### Financeiro

- contas a pagar
- contas a receber
- centros de custo
- dashboards financeiros
- relatórios e fluxo de cobrança

### Estoque

- produtos
- categorias
- marcas
- fornecedores
- lotes
- movimentações
- dashboard de estoque

### IA

- provedores de IA
- agentes
- prompts
- ferramentas
- automações
- memória
- chat
- summaries e analysis
- RAG
- dashboard de IA

### Plataforma

- planos e assinaturas
- billing
- webhooks
- SDK
- administração
- logs
- backups
- deploy
- dashboard da plataforma

## Convenções de resposta

A API utiliza respostas JSON padrão do FastAPI. Erros e exceções são tratados pela camada de middleware e pelo handler global da aplicação.

## Exemplo de chamada

```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"secret"}'
```

## Observações de maturidade

A API atual está funcional para a base implementada e é adequada para desenvolvimento iterativo. Os próximos passos incluem:

- padronização de payloads de erro
- paginação e filtros consistentes
- rate limiting
- melhor contexto de autorização por tenant
- versionamento e documentação mais granular por recurso
