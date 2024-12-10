# Use the miniconda base image
FROM continuumio/miniconda3:24.9.2-0

WORKDIR /usr/src/app

# Copy the entire project directory (to access pyproject.toml)
COPY api_server /usr/src/app/api_server
COPY api_server/environment_20241209.yml /usr/src/app/api_server/environment_20241209.yml

# Create and activate the conda environment, and install dependencies
RUN conda env create -f /usr/src/app/api_server/environment_20241209.yml && \
    echo "source activate tomok_env" > ~/.bashrc && \
    /bin/bash -c "source /opt/conda/etc/profile.d/conda.sh && conda activate tomok_env" && \
    pip install .

# Make entrypoint.sh executable
RUN chmod +x /usr/src/app/api_server/entrypoint.sh

# Execute the needed applications with the necessary commands
ENTRYPOINT ["/bin/bash", "/usr/src/app/api_server/entrypoint.sh"]
