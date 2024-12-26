FROM tomok-base:latest

WORKDIR /app/acc_server

COPY . /app/acc_server

ENV HYDRA_FULL_ERROR=1

RUN chmod +x /app/acc_server/entrypoint.sh
RUN chmod +r /app/acc_server/openapi/tomok-demo.yaml
RUN chmod -R +r /app/acc_server/library_files/*

ENTRYPOINT ["/bin/bash", "/app/acc_server/entrypoint.sh"]