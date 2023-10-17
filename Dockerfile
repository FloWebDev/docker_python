FROM python:3.11

ARG UID
ARG GID

WORKDIR /usr/src/app

RUN pip install --no-cache-dir --upgrade pip wheel setuptools && \
    pip install --no-cache-dir requests numpy

RUN apt update && apt install -y apache2 apache2-utils libapache2-mod-wsgi-py3

COPY ./web.conf /etc/apache2/sites-available/web.conf

RUN a2enmod rewrite actions headers ssl wsgi
RUN a2ensite web.conf

# UID & GID
RUN usermod -u $UID www-data && groupmod -g $GID www-data
RUN chown -R www-data:www-data /var/www

CMD ["apache2ctl", "-D", "FOREGROUND"]