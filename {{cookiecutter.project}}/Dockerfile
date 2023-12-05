FROM python:3.10-slim

USER root
RUN apt-get update -y && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

WORKDIR /code

ENV PYTHONPATH=${PYTHONPATH}:/code/app
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock
COPY ./app /code/app

RUN pip3 install poetry~=1.7.1
RUN poetry install --no-root

RUN pip3 install -e "git+https://github.com/e183b796621afbf902067460/raffaelo.git#egg=raffaelo_quickswap_v3&subdirectory=_modules/raffaelo-quickswap-v3/" --config-settings editable_mode=strict
RUN pip3 install -e "git+https://github.com/e183b796621afbf902067460/raffaelo.git#egg=raffaelo_uniswap_v3&subdirectory=_modules/raffaelo-uniswap-v3/" --config-settings editable_mode=strict
