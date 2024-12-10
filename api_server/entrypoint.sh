#!/bin/bash
python /app/api_server/openapi_generator.py
python /app/api_server/app.py server.app_port=${PORT:-51032}
