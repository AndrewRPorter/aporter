FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www
WORKDIR $CONTAINER_HOME

ADD requirements.txt .

RUN mkdir app
ADD app $CONTAINER_HOME/app

RUN pip install --no-cache-dir -r requirements.txt