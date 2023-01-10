FROM python:3.10.6-slim-buster

WORKDIR /app

RUN apt-get update -y && \
    apt-get install gcc libcurl4-openssl-dev libssl-dev curl gcc -y && \
    rm -rf /var/lib/apt/lists/*

COPY src/. /app/
COPY etc/pip/. /app/

RUN pip install pipenv && pipenv install --deploy --system
