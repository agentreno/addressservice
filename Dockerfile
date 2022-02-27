FROM python:3.9.2-slim-buster

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1.11 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  PATH="$PATH:/root/.local/bin"

WORKDIR /app

RUN pip install poetry

COPY ./addressservice ./addressservice
COPY poetry.lock pyproject.toml ./

RUN poetry install
RUN poetry run python addressservice/manage.py makemigrations cities_light
RUN poetry run python addressservice/manage.py migrate cities_light
RUN poetry run python addressservice/manage.py migrate

ENTRYPOINT ["poetry", "run", "python", "addressservice/manage.py", "runserver", "0.0.0.0:8000"]
