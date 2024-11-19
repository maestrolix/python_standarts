#!/usr/bin/env bash
set -e
if [ -z "$API_LOG_LEVEL" ]; then
  API_LOG_LEVEL=info
fi
if [ -z "$API_PORT" ]; then
  API_PORT=5002
fi
GUNICORN_CMD_ARGS="--bind=0.0.0.0:${API_PORT}"
export GUNICORN_CMD_ARGS

entrypoint_await.sh
entrypoint_migrations.sh

gunicorn demo_project.composites.http_api:app