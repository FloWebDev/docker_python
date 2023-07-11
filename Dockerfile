FROM python:3.11

WORKDIR /usr/src/app

RUN pip install --no-cache-dir --upgrade pip wheel setuptools && \
    pip install --no-cache-dir requests beautifulsoup4 numpy matplotlib
