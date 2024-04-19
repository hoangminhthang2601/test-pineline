FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt

COPY ./requirements_dev.txt /tmp/requirements_dev.txt

COPY ./src/ailiver /app/ailiver

COPY ./tests/ /app/tests

WORKDIR /app

EXPOSE 8000

ARG DEV=false


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r /tmp/requirements_dev.txt ; \
    fi && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"

