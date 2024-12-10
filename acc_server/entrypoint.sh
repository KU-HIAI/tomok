#!/bin/bash

# Extract arguments >> port, 라이브러리 파일 위치, ifc 파일 저장 위치
PORT=${PORT:-51080}
LIBRARY_PATH=${LIBRARY_PATH:-/app/acc_server/library_files}
IFC_PATH=${IFC_PATH:-/app/acc_server/uploads}
SPECIFICATION_DIR=${SPECIFICATION_DIR:-/app/acc_server/openapi}
API_FILE=${API_FILE:-tomok-demo.yaml}
OPENAPI_URL=${OPENAPI_URL:-https://tomokapi.hiai.kr/v1.0/openapi.json}

# Set environment variables for Docker mount paths
export LIBRARY_PATH
export IFC_PATH
export SPECIFICATION_DIR
export API_FILE

# Set environment variable for port
export PORT

export OPENAPI_URL

export HYDRA_FULL_ERROR=1

# Run the acc_server script
python /app/acc_server/app.py server.app_port=${PORT}