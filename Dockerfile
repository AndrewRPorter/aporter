FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www

ADD requirements.txt $CONTAINER_HOME
ADD app $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

RUN pip install --no-cache-dir -r $CONTAINER_HOME/requirements.txt