FROM python:3.11-slim

WORKDIR /patient_backend

RUN apt-get update && apt-get install -y ca-certificates --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock MakeFile /patient_backend/

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /patient_backend
EXPOSE 8000
#CMD ["make", "run"]
CMD ["poetry", "run", "uvicorn", "patient_backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]