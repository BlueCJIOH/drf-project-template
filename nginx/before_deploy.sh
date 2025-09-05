#!/bin/bash

# Script to create Docker network 'nginx_network' and necessary volumes for 'develop' environment

# Define the environments
environments=("develop",)

# Define the network name
NETWORK_NAME="nginx_network"

# Function to create the Docker network if it doesn't exist
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

# Function to create a Docker volume if it doesn't exist
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

# Create the Docker network
create_network

echo "All necessary networks and volumes for 'develop' environments have been created or already exist."