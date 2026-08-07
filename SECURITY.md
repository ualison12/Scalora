# Segurança

## Visão geral

O Scalora já incorpora mecanismos básicos de segurança para autenticação, gerenciamento de credenciais e configuração por ambiente. A implementação atual representa uma base funcional para desenvolvimento e validação, mas ainda precisa de reforços antes de ser considerada totalmente adequada para produção.

## Proteções atuais

- hash de senhas com bcrypt
- emissão de JWT para autenticação
- refresh tokens e rastreamento básico de sessão
- configuração por variáveis de ambiente
- controle inicial de CORS e logging de requests

## Áreas prioritárias de hardening

- gestão forte de secrets em produção
- autorização explícita por tenant e contexto de empresa
- rate limiting e proteção contra abuso
- auditoria estruturada para ações sensíveis
- TLS, headers de segurança e proteção de edge em ambientes públicos
- rotação regular de credenciais e tokens

## Práticas recomendadas

- nunca publicar senhas, tokens ou chaves reais em repositório
- usar variáveis de ambiente ou gerenciadores de segredos em produção
- limitar origens permitidas no CORS
- aplicar princípio de menor privilégio para operações administrativas
- manter dependências atualizadas e revisar mudanças de segurança regularmente

## Resposta a incidentes

Se houver suspeita de incidente:

1. rotacionar secrets de acesso e refresh
2. invalidar sessões e tokens ativos quando possível
3. revisar logs e atividade recente
4. restringir temporariamente o acesso
5. documentar a ocorrência e os próximos passos

## Status atual

A camada de segurança já está funcional para desenvolvimento e ambientes iniciais. Para uma adoção mais robusta, o próximo ciclo deve reforçar autenticação contextual, gerenciamento seguro de segredos e observabilidade de segurança.
