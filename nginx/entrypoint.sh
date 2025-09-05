#!/bin/bash

echo "Starting..."

echo "Running entrypoint script..." >> /var/log/nginx/entrypoint.log

envsubst '$ENVIRONMENT' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

reload_nginx() {
    while :; do
        sleep 6h
        nginx -s reload
    done
}

reload_nginx &

nginx -g "daemon off;"
