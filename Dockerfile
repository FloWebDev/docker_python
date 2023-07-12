FROM python:3.11

ARG UID
ARG GID

WORKDIR /usr/src/app

RUN pip install --no-cache-dir --upgrade pip wheel setuptools && \
    pip install --no-cache-dir requests beautifulsoup4 numpy matplotlib

# UID & GID
RUN groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python

USER python