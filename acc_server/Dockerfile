# Use the miniconda base image
FROM continuumio/miniconda3:24.9.2-0

WORKDIR /usr/src/app/acc_server

# Copy the environment.yml and other necessary files
COPY acc_server/environment.yml /usr/src/app/acc_server/environment.yml
COPY pyproject.toml /usr/src/app/pyproject.toml
COPY README.md /usr/src/app/README.md
COPY acc_server /usr/src/app/acc_server

# Create and activate the conda environment, and install dependencies
RUN conda env create -f /usr/src/app/acc_server/environment.yml && \
    echo "source activate tomok_env" > ~/.bashrc && \
    /bin/bash -c "source /opt/conda/etc/profile.d/conda.sh && conda activate tomok_env"

# Make entrypoint.sh executable
RUN chmod +x /usr/src/app/acc_server/entrypoint.sh

# Execute the needed applications with the necessary commands
ENTRYPOINT ["/bin/bash", "/usr/src/app/acc_server/entrypoint.sh"]