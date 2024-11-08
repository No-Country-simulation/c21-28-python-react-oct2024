#################################################
# MULTI STAGE DOCKER FILE
#################################################

#################################################
#  BASE ALPINE -latest-3.20.3
#  docker build . --target alpine --tag alpine-base --no-cache 
#################################################
FROM alpine:3.20.3 AS alpine
    LABEL NAME="alpine"
    ############
    # DEFAULT  #
    ############
    RUN  apk update \
    && apk upgrade \
    && apk add ca-certificates \
    && update-ca-certificates \
    && apk add --update --no-cache coreutils && rm -rf /var/cache/apk/*   \ 
    && apk add --update --no-cache tzdata curl unzip zlib bash wget git libsodium \
    && apk add --update --no-cache nss libc6-compat vim nano mc grep gnupg \
    && apk add --update --no-cache pkgconfig gcompat libstdc++ \
    && apk add --update --no-cache autoconf automake libtool gpg freetds \
    && apk add --update --no-cache sqlite postgresql-client \ 
    && apk add --update --no-cache mariadb-connector-c make     
    ############
    # VS. CODE #
    ############
    RUN  apk update \
    && apk upgrade \
    && apk add --update --no-cache dropbear-scp \
    && apk add --update --no-cache dropbear-ssh \
    && apk add --update --no-cache zsh \
    && apk add --update --no-cache jq \
    && apk add --update --no-cache util-linux-misc \
    && apk add --update --no-cache procps   
    ############
    # MS-SQL
    ############
#arm64    
ENV architecture="amd64"
#Download the desired package(s)
RUN curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/msodbcsql18_18.0.1.1-1_$architecture.apk \
    && curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/mssql-tools18_18.0.1.1-1_$architecture.apk
#(Optional) Verify signature, if 'gpg' is missing install it using 'apk add gnupg':
RUN curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/msodbcsql18_18.0.1.1-1_$architecture.sig \
    && curl -O https://download.microsoft.com/download/b/9/f/b9f3cce4-3925-46d4-9f46-da08869c6486/mssql-tools18_18.0.1.1-1_$architecture.sig
# sig
RUN curl https://packages.microsoft.com/keys/microsoft.asc  | gpg --import - \
	&& gpg --verify msodbcsql18_18.0.1.1-1_$architecture.sig msodbcsql18_18.0.1.1-1_$architecture.apk \
	&& gpg --verify mssql-tools18_18.0.1.1-1_$architecture.sig mssql-tools18_18.0.1.1-1_$architecture.apk
#Install the package(s)
RUN apk add --allow-untrusted msodbcsql18_18.0.1.1-1_$architecture.apk \
	&& apk add --allow-untrusted mssql-tools18_18.0.1.1-1_$architecture.apk \
	&& rm -f msodbcsql18_18.0.1.1-1_$architecture.apk mssql-tools18_18.0.1.1-1_$architecture.apk    
#
RUN rm -rf /var/cache/apk/* \
    && apk cache clean    
# 
#COPY ./tools/shared/rarlinux-5.4.0.tar.gz ./
#
RUN wget http://www.rarlab.com/rar/rarlinux-5.4.0.tar.gz  && \
    tar -xzvf rarlinux-5.4.0.tar.gz && \
	cd rar && \
	make && \
	mv rar /usr/local/bin/rar
#rar_static    
#################################################
# BASE ALPINE-AR 
# docker build . --target alpine_ar -t alpine-ar  --no-cache
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
# docker build . --target alpine_ar_dev -t alpine_ar_dev --no-cache
#################################################
FROM alpine_ar AS alpine_ar_dev
#
RUN apk add --update --no-cache --virtual build-deps g++ unixodbc-dev \
    && apk add --update --no-cache gcc g++ make libc-dev linux-headers musl-dev \
    && apk add --update --no-cache libffi-dev py-cffi jpeg-dev openssl-dev \ 
    && apk add --update --no-cache freetype-dev bzip2-dev zlib-dev \
    && apk add --update --no-cache postgresql-dev postgresql-client \
    && apk add --update --no-cache mariadb-dev mariadb-connector-c-dev \
    && apk add --update --no-cache libxslt-dev gettext \
    && apk add --update --no-cache lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev 
    
    #apk del build-deps
#gcc musl-dev libffi-dev2 pkgconf
#apk del build-deps
#
RUN  rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apk/* \   
    && apk cache clean   
#################################################
# BASE ALPINE - AR - DEV - PYTHON 
# docker build . --target alpine_ar_dev_py -t alpine_ar_dev_py --no-cache
#################################################
FROM alpine_ar_dev AS alpine_ar_dev_py
#ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && \
    apk add --no-cache --virtual .build-deps \ 
    && apk add --update --no-cache python3-dev py3-pip \
    && ln -sf python3 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apk/* \   
    && apk cache clean
# 
#################################################
# BASE ALPINE - AR - DEV - PYTHON - ENV
# docker build . --target ar_dev_py_env -t ar_dev_py_env --no-cache
#################################################
FROM alpine_ar_dev_py AS ar_dev_py_env
    ENV VIRTUAL_ENV=/opt/venv
    RUN python3 -m venv $VIRTUAL_ENV
    ENV PATH="$VIRTUAL_ENV/bin:$PATH"
    RUN python3 -m ensurepip --upgrade  
    #virtualenv
    RUN pip3 install --no-cache --upgrade pip setuptools wheel 
    RUN python3 -m pip install --upgrade pika numpy BeautifulSoup4 pandas
    RUN python3 -m pip install --upgrade Pillow  requests 
    RUN python3 -m pip install --upgrade psycopg2-binary 
    RUN python3 -m pip install --upgrade PyMySQL PyMySQL[rsa] PyMySQL[ed25519]
    RUN python3 -m pip install --upgrade pyodbc mysql-connector-python
    RUN python3 -m pip install --upgrade mysqlclient SQLAlchemy
    #pip install "reactpy[fastapi,flask,sanic,starlette,tornado]"
# 
#################################################
# BASE ALPINE - AR - DEV - PYTHON - Django
# docker build . --target ar_dev_py_django -t ar_dev_py_django  --no-cache
#################################################
FROM ar_dev_py_env AS ar_dev_py_django
#
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN adduser -D python
RUN mkdir -p /home/python/app && chown -R python:python /home/python/app
#
RUN python3 -m pip install --upgrade django djangorestframework 
RUN python3 -m pip install --upgrade djangorestframework-simplejwt
RUN python3 -m pip install --upgrade django-model-utils Markdown django-filter
RUN python3 -m pip install --upgrade django-ckeditor coreapi
RUN python3 -m pip install --upgrade crispy-bootstrap5
RUN python3 -m pip install --upgrade django-crispy-forms
#pip install "reactpy[starlette]"
#RUN python3 -m pip install --upgrade pip install reactpy-django
#
RUN python3 -m pip freeze > /home/python/app/requirements.txt
#coreapi-cli
WORKDIR /home/python/app
USER python
#COPY --chown=python:python . . 
#
EXPOSE 8000
EXPOSE 9229
EXPOSE 9230
#CMD ["daphne", "backend.asgi:application", "-b", "0.0.0.0", "-p", $NUXT_PAGE_PORT]
CMD ["tail","-f","/dev/null"] 
#################################################
#################################################
# BASE ALPINE - AR - DEV - PYTHON - FastApi
# docker build . --target ar_dev_py_fastapi -t ar_dev_py_fastapi  --no-cache
#################################################
FROM ar_dev_py_env AS ar_dev_py_fastapi
#
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN adduser -D python
RUN mkdir -p /home/python/app && chown -R python:python /home/python/app
#
RUN python3 -m pip install --upgrade  "fastapi[all]" "uvicorn[standard]" 
RUN python3 -m pip install --upgrade  sqlmodel
RUN python3 -m pip install --upgrade  "pydantic[email,timezone]"
RUN python3 -m pip install --upgrade -U pytest copier
#https://medium.com/@kevinkoech265/a-guide-to-connecting-postgresql-and-pythons-fast-api-from-installation-to-integration-825f875f9f7d
#https://v2.chakra-ui.com/
#https://github.com/fastapi/full-stack-fastapi-template
#https://www.hackveda.in/articles/python-binary-decompilation.html
RUN python3 -m pip freeze > /home/python/app/requirements.txt
#
WORKDIR /home/python/app
USER python
#COPY --chown=python:python . . 
#
EXPOSE 8000
EXPOSE 9229
EXPOSE 9230
#CMD ["daphne", "backend.asgi:application", "-b", "0.0.0.0", "-p", $NUXT_PAGE_PORT]
CMD ["tail","-f","/dev/null"] 
#################################################
#  POSTGRESQL - BookWorm
#  docker build . --target postgres --tag postgres -t postgres --no-cache 
#################################################
FROM postgres:17.0-bookworm AS postgres 
EXPOSE 5432
#################################################
#  PGAdmin 4 
#  docker build . --target pgadmin4 --tag pgadmin4 -t pgadmin4 --no-cache 
#################################################
FROM dpage/pgadmin4 AS pgadmin4 
#################################################
#  BASE ALPINE - 20.18
#  docker build . --target nodev20 --tag node:v20 --no-cache 
#  docker save -o node20.tar  node:v20
#################################################
FROM node:20.18-alpine AS nodev20
WORKDIR /
RUN apk update && \
    apk add --no-cache --virtual .build-deps \
    && apk upgrade \
    && apk add ca-certificates \
    && update-ca-certificates \
    && apk add --update --no-cache make coreutils && rm -rf /var/cache/apk/*   \ 
    && apk add --update --no-cache tzdata curl unzip bash wget git libsodium \
    && apk add --update --no-cache nss libc6-compat vim nano mc \
    && rm -rf /var/cache/apk/* 
#
#COPY ./tools/shared/rarlinux-5.4.0.tar.gz ./
#RUN wget http://www.rarlab.com/rar/rarlinux-5.4.0.tar.gz  && \
# tar -xzvf rarlinux-5.4.0.tar.gz && \#
#	cd rar && \
#	make && \
#	mv rar /usr/local/bin/rar
#RUN rm -rf rarlinux-5.4.0.tar.gz rar
#
RUN mkdir -p /root/.aws/credentials && chmod +rw /root/.aws/credentials 
RUN mkdir -p /app/dist && chmod +rw /app/dist
#
COPY ./tools/front ./installer/tools
# 
RUN mkdir -p ./usr/local/lib/node_modules  && chmod +rw /usr/local/lib/node_modules
RUN chown -R root:$(whoami) /usr/local/lib/node_modules/
RUN chmod -R 775 /usr/local/lib/node_modules/
 
RUN npm install -g npm --unsafe-perm=true --allow-root
#RUN npm install -g nodemon --unsafe-perm=true --allow-root
#RUN npm install -g ts-node --unsafe-perm=true --allow-root
#RUN npm install -g tslib --unsafe-perm=true --allow-root
#RUN npm install -g @types/node --unsafe-perm=true --allow-root
#RUN npm install -g env-cmd --unsafe-perm=true --allow-root
WORKDIR /app
RUN npm install yarn
#RUN yarn create toolpad-app
#RUN yarn global add @types/react 
#RUN yarn global add @types/react-dom
#RUN yarn global add create-react-app
#EXPOSE 3000-3010
#EXPOSE 9229-9240
#CMD ["tail","-f","/dev/null"]
#################################################
#  BASE ALPINE - 20.18
#  docker build . --target radstudio --tag radstudio --no-cache 
#  docker save -o radstudio.tar radstudio
#################################################
FROM nodev20 AS radstudio
WORKDIR /app
EXPOSE 3002
EXPOSE 9231
CMD ["tail","-f","/dev/null"]
#################################################
#  BASE ALPINE - 20.18
#  docker build . --target front --tag front --no-cache 
#  docker save -o front.tar front
#################################################
FROM nodev20 AS front
WORKDIR /app
#RUN yarn add @toolpad/core 
#WORKDIR /app
#RUN yarn add @mui/material @mui/icons-material @emotion/react @emotion/styled
#WORKDIR /app
EXPOSE 3001
EXPOSE 9230
CMD ["tail","-f","/dev/null"]
