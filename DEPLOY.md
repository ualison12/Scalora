# Deploy e operação

## Visão geral

O Scalora pode ser executado localmente com Docker Compose e também adaptado para ambientes mais próximos de produção, como máquinas virtuais, Kubernetes ou plataformas de containers gerenciadas.

## Ambiente local

### Pré-requisitos

- Docker e Docker Compose
- Python 3.13+
- Node.js 20+

### Subir a stack

```bash
docker compose up --build
```

Os serviços iniciados incluem:

- PostgreSQL na porta 5432
- Redis na porta 6379
- API na porta 8000
- frontend na porta 3000

## Variáveis de ambiente

A aplicação utiliza variáveis como:

- DATABASE_URL
- SECRET_KEY
- ALGORITHM
- ACCESS_TOKEN_EXPIRE_MINUTES
- APP_ENV
- APP_DEBUG

Essas configurações devem ser definidas de forma explícita em cada ambiente.

## Checklist para produção

- usar segredos fortes e rotacioná-los regularmente
- preferir PostgreSQL em vez de SQLite
- habilitar TLS e término de proxy reverso
- configurar backup e retenção
- implementar monitoramento e alertas
- evitar defaults de desenvolvimento em ambientes públicos

## Observações de containers

A configuração atual já inclui health checks para PostgreSQL e API. Para avançar para produção, recomenda-se:

- imagens separadas para produção
- execução sem privilégio root quando possível
- gerenciamento de segredos fora do repositório
- limites explícitos de CPU e memória

## Estratégia de rollout e rollback

- manter migrações versionadas em repositório
- aplicar migrações antes de publicar nova versão da API
- validar mudanças em staging antes de produção
- manter backups e artefatos para rollback

## Status atual

A infraestrutura atual é funcional para desenvolvimento local. A próxima evolução deve focar em automação de deployment, hardening operacional e observabilidade.
