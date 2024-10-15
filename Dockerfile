#################################################
# MULTI STAGE DOCKER FILE
#################################################

#################################################
#  BASE ALPINE -latest-3.20.3
#  docker build . --target alpine --tag alpine/base  --no-cache 
#################################################
FROM alpine:3.20.3 AS alpine
    RUN  apk update \
    && apk upgrade \
    && apk add ca-certificates \
    && update-ca-certificates \
    && apk add --update coreutils && rm -rf /var/cache/apk/*   \ 
    && apk add --update tzdata curl unzip bash wget git libsodium \
    && apk add --no-cache nss libc6-compat vim nano mc \
    && rm -rf /var/cache/apk/*
#################################################
# BASE ALPINE-AR 
# docker build . --target alpine_ar -t alpine/ar  --no-cache
#################################################
FROM alpine AS alpine_ar
    RUN cp /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime
    RUN rm -r /usr/share/zoneinfo/Africa && \
        rm -r /usr/share/zoneinfo/Antarctica && \
        rm -r /usr/share/zoneinfo/Arctic && \
        rm -r /usr/share/zoneinfo/Asia && \
        rm -r /usr/share/zoneinfo/Atlantic && \
        rm -r /usr/share/zoneinfo/Australia && \
        rm -r /usr/share/zoneinfo/Europe  && \
        rm -r /usr/share/zoneinfo/Indian && \
        rm -r /usr/share/zoneinfo/Mexico && \
        rm -r /usr/share/zoneinfo/Pacific && \
        rm -r /usr/share/zoneinfo/Chile && \
        rm -r /usr/share/zoneinfo/Canada
#################################################
# BASE ALPINE - AR - DEV
# docker build . --target alpine_ar_dev -t alpine/ar_dev --no-cache
#################################################
FROM alpine_ar AS alpine_ar_dev
    RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    gcc mysql-dev make linux-headers musl-dev \
    libffi-dev \
    jpeg-dev  \ 
    openssl-dev \
    freetype-dev \
    bzip2-dev \
    zlib-dev
#################################################
# BASE ALPINE - AR - DEV - PYTHON 
# docker build . --target alpine_ar_dev_py -t alpine/ar_dev_py
#################################################
FROM alpine_ar_dev AS alpine_ar_dev_py
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && \
    apk add --no-cache --virtual .build-deps \ 
    && apk add python3 \
    && apk add py3-pip \
    && apk del .build-deps \
    && rm -rf /var/lib/apt/lists/*
#################################################
# BASE ALPINE - AR - DEV - PYTHON - ENV
# docker build . --target ar_dev_py_env -t ar_dev_py_env
#################################################
FROM alpine_ar_dev_py AS ar_dev_py_env
    ENV VIRTUAL_ENV=/opt/venv
    RUN python3 -m venv $VIRTUAL_ENV
    ENV PATH="$VIRTUAL_ENV/bin:$PATH"
    RUN python3 -m ensurepip --upgrade  
    RUN pip3 install --no-cache --upgrade pip setuptools wheel virtualenv
    RUN python3 -m pip install --upgrade mysql-connector-python 
    RUN python3 -m pip install --upgrade pika numpy BeautifulSoup4 pandas
    RUN python3 -m pip install --upgrade Pillow  requests 
    RUN python3 -m pip install --upgrade django-mysql
    #RUN python3 -m pip install --upgrade pyodbc pymssql pyodbc mysqlclient django_mysql
#################################################
# BASE ALPINE - AR - DEV - PYTHON - Django
# docker build . --target ar_dev_py_django -t ar_dev_py_django
#################################################
FROM ar_dev_py_env AS ar_dev_py_django
#
RUN adduser -D python
RUN mkdir -p /home/python/app && chown -R python:python /home/python/app
#
RUN python3 -m pip install --upgrade django djangorestframework djangorestframework-simplejwt
RUN python3 -m pip install --upgrade django-model-utils Markdown django-filter
RUN python3 -m pip install --upgrade django-ckeditor coreapi
RUN python3 -m pip freeze > /home/python/app/requirements.txt
#
WORKDIR /home/python/app
#USER python
#COPY --chown=python:python . . 
#
EXPOSE 8000
EXPOSE 9229
EXPOSE 9230
CMD tail -f /dev/null
#COPY --from=alpine_ar_dev_py /opt/venv /opt/venv
#################################################
#################################################
# BASE ALPINE - AR - DEV - PYTHON - RUNNER
# docker build . --target py_runner -t py_runner
#################################################
#################################################
#  BASE DEBIAN -latest
# docker build . --target debian -t debian/base
#################################################
FROM debian:trixie-slim AS debian
#################################################
# BASE DEBIAN - AR 
# docker build --target debian -t debian/ar
#################################################
FROM debian AS debian_ar
#
ENV TZ=America/Argentina/Buenos_Aires
ENV LANG=es_AR.UTF-8
ENV LC_ALL=es_AR.UTF-8
ENV LANGUAGE=es_AR.UTF-8
#################################################
#  BASE DEBIAN - AR - DEV
#################################################
