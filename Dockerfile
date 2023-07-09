FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir requests beautifulsoup4
