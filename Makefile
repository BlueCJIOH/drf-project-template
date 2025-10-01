COMPOSE_FILE=docker-compose.yml

NO_CACHE ?= 0

ifneq ($(filter -nc,$(MAKECMDGOALS)),)
override NO_CACHE := 1
endif

ifeq ($(OS),Windows_NT)
  MKDIR = if not exist "$(1)" mkdir "$(1)"
else
  MKDIR = mkdir -p $(1)1
endif

BUILD_FLAGS :=
ifeq ($(NO_CACHE),1)
BUILD_FLAGS := --no-cache
endif

.PHONY: build up down migrate loaddata collectstatic deploy clean -nc

build:
	docker compose -f $(COMPOSE_FILE) build $(BUILD_FLAGS)

checkdirs:
	@echo "=================[Ensuring 'staticfiles' and 'media' directories exist locally...]================="
	@$(call MKDIR,src/core/staticfiles)
	@$(call MKDIR,src/media)
	@$(call MKDIR,src/static)
	@echo "Directories checked/created: staticfiles, media"

up:
	docker compose -f $(COMPOSE_FILE)  up -d

migrate:
	docker compose -f $(COMPOSE_FILE) run --remove-orphans --rm web uv run python src/manage.py migrate

loaddata:
	docker compose -f $(COMPOSE_FILE) run --remove-orphans --rm web sh -lc "uv run python src/manage.py loaddata src/core/fixtures/*"

collectstatic:
	docker compose -f $(COMPOSE_FILE) run --remove-orphans --rm web uv run python src/manage.py collectstatic --noinput

deploy: checkdirs build collectstatic migrate up loaddata

down:
	docker compose -f $(COMPOSE_FILE) down

clean:
	docker compose -f $(COMPOSE_FILE) down -v
	rm -rf __pycache__

# consume optional '-nc' goal passed after '--' so make does not error
-nc:
	@:
