FROM python:3.12-slim

EXPOSE 8001
ENV PORT=8001

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

LABEL description="Caderneta de Dividas - Implantação"

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt && \
    apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
WORKDIR /code
COPY . /code

RUN useradd appuser && chown -R appuser /code
USER appuser