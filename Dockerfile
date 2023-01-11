FROM python:3.11.1-bullseye
LABEL maintainer="Trevor Pierce"

ENV PYTHONUNBUFFERED 1

WORKDIR /student-data-api

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /student-data-api/app
COPY ./.flake8 /student-data-api

EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        fastapi-user

ENV PATH="/py/bin:$PATH"

USER fastapi-user
