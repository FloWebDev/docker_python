# Docker Python

## Use Debian image instead of Alpine

Alpine image has too many troubles to install correctly some Python packages (missing dependencies and other undetected errors).

## Enable container to access to x11 socket of the host (for tkinter, matplotlib)

Include these two flag when doing the docker run (or equivalent in docker-compose.yml).

```
-v /tmp/.X11-unix:/tmp/.X11-unix
-e DISPLAY=unix$DISPLAY
```
And because the default settings of X11 only allows local users to print, we need to change this to all users.

```
$ sudo apt-get install x11-xserver-utils
$ xhost +
```

Source : https://stackoverflow.com/questions/49169055/docker-tkinter-tclerror-couldnt-connect-to-display/49229627#49229627

## Running Docker Containers as a Non-root User with a Custom UID / GID

Example:

```
ARG UID=1000
ARG GID=1000

RUN groupadd -g "${GID}" python \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python

USER python

# Everything after this point will run as the python user with a specific UID / GID
```

Source : https://nickjanetakis.com/blog/running-docker-containers-as-a-non-root-user-with-a-custom-uid-and-gid