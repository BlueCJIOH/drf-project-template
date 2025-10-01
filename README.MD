# Project Template

This repository provides a DRF template configured to use the [uv](https://github.com/astral-sh/uv) package manager.

Useful for hackathons and project templates.

## How to add a new library

  - `uv add redis` — example for adding `redis` package

- How to recover `uv.lock` и `requirements.uv.lock`:
  1. Make lock file: `uv lock`
  2. Export dependencies to `requirements.uv.lock`: `uv export --format=requirements-txt -o requirements.uv.lock`

## Environment configuration

- Uses `.env` at repository root, loaded via `django-environ`.
- Example variables are in `.env.example` (copy to `.env`).

## Pre-commit hooks

- Configured in `.pre-commit-config.yaml` with `black`, `isort`, and `flake8`.
- Enable locally:
  1. `pip install pre-commit` (or add via your toolchain)
  2. `pre-commit install`
  3. Optionally run once on all files: `pre-commit run --all-files`

## Common Problems

```bash
warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance. 
If the cache and target directories are on different filesystems, hardlinking may not be supported.
If this is intentional, set export UV_LINK_MODE=copy or use --link-mode=copy to suppress this warning.
```

- Add `UV_LINK_MODE=copy` to Dockerfile.dev after `FROM python:3.12-slim AS builder`
- ENV UV_LINK_MODE=copy 

## Quick start

```bash
# via ssh
git clone git@github.com:ostrovok-hackathon-2025/venue.git
# or via https for read-only:
# git clone https://github.com/ostrovok-hackathon-2025/venue.git
cd venue
cp .env.example .env

# one-shot deploy if GNU Make is installed
make deploy
```
It can be deployed by manually as well
```bash
docker compose up --build -d
docker compose -f docker-compose.yml exec web uv run python src/manage.py collectstatic --noinput
docker compose -f docker-compose.yml exec uv run python src/manage.py migrate
docker compose -f docker-compose.yml exec web sh -lc "uv run python src/manage.py loaddata src/core/fixtures/*"

# create superuser
docker compose -f docker-compose.yml exec web uv run python src/manage.py createsuperuser
```

The application is served through Docker. Common actions are encapsulated in the `Makefile`.

## Structure

```text
project/                # DRF project template
├─ src/                 # Application source
│  ├─ core/             # Project core and global config
│  │  ├─ conf/          # Settings split by domain (api, auth, db, cache, etc.)
│  │  ├─ fixtures/      # Seed data for `loaddata`
│  │  └─ ...shared      # Shared modules (models, services, permissions, pagination, validators)
│  ├─ apps/             # Feature apps live here
│  │  ├─ a12n/          # Authentication endpoints and SimpleJWT integration
│  │  └─ healthz/       # Example app (health check)
│  │     └─ api/        # serializers, views
│  │     └─ urls.py     # urls for the app
│  └─ manage.py         # Django CLI entrypoint
├─ nginx/               # Nginx proxy + container setup
├─ Dockerfile.dev       # Dev container image
├─ docker-compose.local.yml # Local development docker-compose
├─ Makefile             # Common dev commands (deploy, up, clean)
├─ init.sh              # Bootstrap / setup script
├─ .env.example         # Example environment variables
├─ .pre-commit-config.yaml # Code quality hooks
├─ pyproject.toml       # Tooling config (formatters/linters/etc.)
└─ README.MD            # Project docs and getting started
```

Notes for new developers
- New app: create under `src/apps/<your_app>/` with optional `api/` for DRF.
- URLs: register app URLs in `src/core/urls.py`.
- Settings: keep domain-specific config in `src/core/conf/` and import via `src/core/settings.py`.
- Env vars: copy `.env.example` to `.env` and adjust as needed.
- Dev run: use `Makefile` targets or `docker-compose.local.yml` for local services.
- Fixtures: place JSON fixtures in `src/core/fixtures/` and load with `manage.py loaddata`.
