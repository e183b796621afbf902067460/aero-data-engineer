FROM python:3.10-slim

USER root
RUN apt-get update && apt-get install -y git

ARG requirements=/code/requirements.txt

WORKDIR /code

ENV PYTHONPATH=${PYTHONPATH}:/code/app
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock
COPY ./app /code/app

RUN pip3 install poetry~=1.6.1
RUN poetry export -f requirements.txt > ${requirements}  --without-hashes --without linters,typing,tests
RUN pip3 install -r ${requirements}

# TODO RUN pip3 install -e "git+https://github.com/e183b796621afbf902067460/raffaelo.git#egg=raffaelo_uniswap_v3&subdirectory=_modules/raffaelo-uniswap-v3/"