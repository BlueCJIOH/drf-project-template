# Project Template

This repository provides a DRF template configured to use the [uv](https://github.com/astral-sh/uv) package manager.

Useful for hackathons and project templates.

## Environment configuration

- Uses `.env` at repository root, loaded via `django-environ`.
- Example variables are in `.env.example` (copy to `.env`).

## Pre-commit hooks

- Configured in `.pre-commit-config.yaml` with `black`, `isort`, and `flake8`.
- Enable locally:
  1. `pip install pre-commit` (or add via your toolchain)
  2. `pre-commit install`
  3. Optionally run once on all files: `pre-commit run --all-files`

## Quick start

```bash
uv venv .venv
uv pip install -r requirements.uv.lock
cp .env.example .env
make deploy
```

The application is served through Docker. Common actions are encapsulated in the `Makefile`.

## Celery + Redis

- Services: `redis`, `default-worker`, `default-beat` are defined in `docker-compose.local.yml`.
- Beat schedules include a health `ping` every minute.