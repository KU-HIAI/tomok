FROM python:3.11.5-slim-bookworm

WORKDIR /src

COPY pyproject.toml README.md /src/
COPY tomok /src/tomok

RUN pip install .