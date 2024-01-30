FROM python:3.11.7-slim-bookworm as builder

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev --no-root && rm -rf $POETRY_CACHE_DIR

FROM python:3.11.7-slim-bookworm as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]