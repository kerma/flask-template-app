FROM python:3.7-alpine3.8

RUN set -ex \
    && apk add --no-cache --virtual .build-deps  \
        musl-dev \
        postgresql-dev \
        gcc

ARG pypi=https://pypi.org/simple
ADD requirements.txt /requirements.txt
ENV PIP_TRUSTED_HOST=localhost
RUN pip3 install -r requirements.txt -i $pypi

ADD . /code
WORKDIR /code
RUN pip3 install -e .

EXPOSE 8080
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "ftapp:create_app()"]
