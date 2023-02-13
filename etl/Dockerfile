FROM python:3.10-slim

WORKDIR /opt/dagster/app
ENV DAGSTER_HOME=/opt/dagster/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY workspace.yaml ./
COPY dagster.yaml ./
COPY aero ./aero
COPY framework ./framework
