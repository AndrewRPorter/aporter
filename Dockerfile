FROM python:3.7-slim

ENV CONTAINER_HOME=/var/www

ADD . $CONTAINER_HOME
WORKDIR $CONTAINER_HOME

EXPOSE 8080

RUN pip install --no-cache-dir -r $CONTAINER_HOME/requirements.txt