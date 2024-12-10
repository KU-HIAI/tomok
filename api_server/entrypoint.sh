#!/bin/bash

# conda 환경 활성화
source /opt/conda/etc/profile.d/conda.sh
conda activate tomok_env

PORT=${PORT:-51032}

export PORT

python /usr/src/app/api_server/openapi_generator.py
python /usr/src/app/api_server/app.py
