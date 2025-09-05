#!/bin/bash

# Ensure nginx network and shared named volumes for static/media exist.

set -euo pipefail

# Load env for naming (prefer local nginx/.env, then project root .env)
if [ -f ./.env ]; then
  set -a; source ./.env; set +a
fi
if [ -z "${PROJECT_NAME:-}" ] && [ -f ../.env ]; then
  # shellcheck disable=SC1091
  set -a; source ../.env; set +a
fi

ENVIRONMENT="${ENVIRONMENT:-develop}"
PROJECT_NAME="${PROJECT_NAME:-your_name}"

NETWORK_NAME="nginx_network"
VOLUME_STATIC_NAME="${PROJECT_NAME}-${ENVIRONMENT}_staticfiles"
VOLUME_MEDIA_NAME="${PROJECT_NAME}-${ENVIRONMENT}_media"

create_network() {
  echo "Checking if network '$NETWORK_NAME' exists..."
  if docker network ls --format '{{.Name}}' | grep -wq "$NETWORK_NAME"; then
    echo "Network '$NETWORK_NAME' already exists."
  else
    echo "Network '$NETWORK_NAME' not found. Creating..."
    docker network create "$NETWORK_NAME"
    if [ $? -eq 0 ]; then
      echo "Network '$NETWORK_NAME' successfully created."
    else
      echo "Error: Failed to create network '$NETWORK_NAME'." >&2
      exit 1
    fi
  fi
}

create_volume() {
  local volume_name="$1"
  echo "Checking if volume '$volume_name' exists..."
  if docker volume ls --format '{{.Name}}' | grep -wq "$volume_name"; then
    echo "Volume '$volume_name' already exists."
  else
    echo "Volume '$volume_name' not found. Creating..."
    docker volume create "$volume_name"
    if [ $? -eq 0 ]; then
      echo "Volume '$volume_name' successfully created."
    else
      echo "Error: Failed to create volume '$volume_name'." >&2
      exit 1
    fi
  fi
}

create_network
create_volume "$VOLUME_STATIC_NAME"
create_volume "$VOLUME_MEDIA_NAME"

echo "Ready. Network and volumes ensured:"
echo "  - network: $NETWORK_NAME"
echo "  - volume:  $VOLUME_STATIC_NAME"
echo "  - volume:  $VOLUME_MEDIA_NAME"
