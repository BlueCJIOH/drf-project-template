# ODIN Backend Template

This repository provides a Django + DRF template configured to use the [uv](https://github.com/astral-sh/uv) package manager.

## Quick start

```bash
uv venv .venv
uv pip install -r requirements.uv.lock
cp .env.example .env
make up
```

The application is served through Docker. Common actions are encapsulated in the `Makefile`.
