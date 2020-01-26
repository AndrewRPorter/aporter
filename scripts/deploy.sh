#!/bin/bash

docker-compose -f conf/docker-prod.yml pull
docker-compose -f conf/docker-prod.yml up