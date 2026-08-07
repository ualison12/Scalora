# Contribuindo com o Scalora

## Boas-vindas

Contribuições são bem-vindas. Como o projeto está em crescimento, mudanças pequenas, bem testadas e bem descritas têm maior valor do que alterações amplas e difusas.

## Fluxo de desenvolvimento

1. criar uma branch a partir da branch principal
2. implementar a mudança de forma focada
3. adicionar ou atualizar testes quando aplicável
4. executar a suíte relevante
5. abrir um pull request com resumo claro e evidências

## Configuração local

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
npm run build
```

### Docker

```bash
docker compose up --build
```

## Padrões de código

- preferir Python e TypeScript claros e explícitos
- manter lógica de negócio em services
- manter persistência e acesso a dados em camadas apropriadas
- seguir a estrutura modular existente para novos recursos
- documentar mudanças que alterem arquitetura, fluxo ou comportamento do usuário

## Expectativas de teste

- adicionar testes para novos comportamentos e regressões
- preferir testes unitários para regras de negócio e testes de integração para rotas quando pertinente
- validar a suíte backend antes de abrir PR

## Checklist de pull request

- [ ] a mudança está descrita com clareza
- [ ] testes foram adicionados ou atualizados
- [ ] documentação foi atualizada quando necessário
- [ ] não foi introduzido um regressão evidente de segurança
- [ ] os checks relevantes foram executados

## Comunicação

Use pull requests e discussões de issues para detalhes de implementação, decisões de design e questões de rollout.
