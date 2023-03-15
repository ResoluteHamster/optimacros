ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION:-3.10.10}-slim-bullseye

ENV POETRY_VERSION=1.4.0
RUN pip install "poetry==$POETRY_VERSION" && poetry config virtualenvs.create false

ENV TZ=Europe/Moscow
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_NO_CACHE_DIR=off
ENV PYTHONDONTWRITEBYTECODE=on
ENV PYTHONFAULTHANDLER=on
ENV PYTHONUNBUFFERED=on

COPY . /opt/optimacros
WORKDIR /opt/optimacros

# Dependencies
ARG RUN_LEVEL=production
ENV RUN_LEVEL=${RUN_LEVEL}
WORKDIR /opt/optimacros
COPY pyproject.toml poetry.loc[k] /opt/optimacros/
RUN poetry install $(if [ "${RUN_LEVEL}" = "production" ]; then echo "--no-dev"; fi ) --no-interaction --no-ansi -vvv
RUN pip install gunicorn


CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:80", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.main:app"]

