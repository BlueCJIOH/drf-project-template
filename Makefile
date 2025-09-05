COMPOSE_FILE=docker-compose.local.yml

.PHONY: build up down migrate loaddata deploy clean

build:
	docker compose -f $(COMPOSE_FILE) build

up:
	docker compose -f $(COMPOSE_FILE) up

migrate:
	docker compose -f $(COMPOSE_FILE) run --rm web uv run python src/manage.py migrate

loaddata:
	docker compose -f $(COMPOSE_FILE) run --rm web uv run python src/manage.py loaddata $(file)

deploy:
	docker compose -f $(COMPOSE_FILE) up -d --build

down:
	docker compose -f $(COMPOSE_FILE) down

clean:
	docker compose -f $(COMPOSE_FILE) down -v
	rm -rf __pycache__ .venv
