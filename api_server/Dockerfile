FROM tomok-base:latest

WORKDIR /app/api_server

COPY . /app/api_server

# Make entrypoint.sh executable
RUN chmod +x /app/api_server/entrypoint.sh

# Execute the needed applications with the necessary commands
ENTRYPOINT ["/bin/bash", "/app/api_server/entrypoint.sh"]