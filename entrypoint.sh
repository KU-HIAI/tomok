#!/bin/bash

# conda 환경 활성화
source /opt/conda/etc/profile.d/conda.sh
conda activate tomok_env

# Extract arguments >> port, 라이브러리 파일 위치, ifc 파일 저장 위치
PORT=${PORT:-51080}
LIBRARY_PATH=${LIBRARY_PATH:-/usr/src/app/acc_server/library_files}
IFC_PATH=${IFC_PATH:-/usr/src/app/acc_server/uploads}
SPECIFICATION_DIR=${SPECIFICATION_DIR:-/usr/src/app/acc_server/openapi}
API_FILE=${API_FILE:-tomok-demo.yaml}

# Set environment variables for Docker mount paths
export LIBRARY_PATH
export IFC_PATH
export SPECIFICATION_DIR
export API_FILE

# Set environment variable for port
export PORT

export HYDRA_FULL_ERROR=1

# Run the acc_server script
python /usr/src/app/acc_server/app.py