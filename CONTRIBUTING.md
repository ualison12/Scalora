# Contributing

## Welcome

Contributions to Scalora are welcome. The project is evolving quickly, so clear communication and small, testable changes are especially valuable.

## Development workflow

1. Create a branch from main.
2. Implement your change in a focused manner.
3. Add or update tests where relevant.
4. Run the relevant test suite.
5. Open a pull request with a clear summary and evidence.

## Local setup

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

## Coding standards

- Prefer explicit, readable Python and TypeScript.
- Keep business logic in services and persistence logic in repositories.
- Follow the existing module layout for new features.
- Add documentation for user-facing behavior and architectural decisions when relevant.

## Testing expectations

- Add tests for new behaviors and regressions.
- Prefer targeted unit tests for services and integration-style tests for routes when relevant.
- Verify the full backend test suite before opening a PR.

## Pull request checklist

- [ ] Feature or fix is described clearly
- [ ] Tests were added or updated
- [ ] Documentation was updated if needed
- [ ] No obvious security regression was introduced
- [ ] Relevant runtime checks were executed

## Communication

Use pull requests and issue discussions for implementation details, design questions, and rollout concerns.
