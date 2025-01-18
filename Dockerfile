FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock /

RUN poetry config virtualenvs.create false \
    && poetry install

COPY . .

EXPOSE 8000
