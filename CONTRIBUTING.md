# Contributing

## Commit messages
Use [Conventional Commits](https://www.conventionalcommits.org/) format.

## Branching
Create feature branches from `main` and submit pull requests.

## Tests
Run `make test` before committing. Add tests for new features.

## Development
The project uses `uv` for dependency management. Create the environment with:

```bash
uv venv .venv
uv pip install -r requirements.uv.lock
```

Use Docker and Makefile commands for common tasks.

## Makefile commands
- `make build` – build images
- `make up` – start services
- `make migrate` – apply migrations
- `make loaddata` – load fixtures
- `make deploy` – build and run in detached mode
- `make down` – stop services
- `make clean` – remove containers and caches
