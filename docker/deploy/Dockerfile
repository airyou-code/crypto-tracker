FROM --platform=linux/amd64 python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # fix ImportError: failed to find libmagic
  && apt-get install -y libmagic-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # git is required for pip install from git repo
  && apt-get install -y git ssh \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && apt update && apt install -y curl

# Requirements are installed here to ensure they will be cached.
COPY ./webapp/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./docker/deploy/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/deploy/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app
COPY ./webapp /app

ENTRYPOINT ["/entrypoint"]
