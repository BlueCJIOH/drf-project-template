#!/bin/sh
uv run python src/manage.py migrate
uv run python src/manage.py collectstatic --noinput
