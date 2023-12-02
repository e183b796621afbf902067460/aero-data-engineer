FROM python:3.10-slim

USER root
RUN apt-get update && apt-get install -y git

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
# TODO RUN pip3 install -e "git+https://github.com/e183b796621afbf902067460/raffaelo.git#egg=raffaelo_uniswap_v3&subdirectory=_modules/raffaelo-uniswap-v3/"