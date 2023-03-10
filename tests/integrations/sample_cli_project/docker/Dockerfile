FROM python:3.10.10-slim-buster

RUN apt-get update && \
    apt-get -y install g++ \
    && apt-get clean

WORKDIR /cli-app

COPY  models ./models
COPY  profiles ./profiles
COPY  snapshots ./snapshots
COPY  tests ./tests
COPY  dbt_project.yml ./dbt_project.yml

RUN pip install -U pip dbt-duckdb
