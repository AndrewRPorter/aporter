#!/bin/bash

docker-compose -f conf/docker-prod.yml build
docker-compose -f conf/docker-prod.yml up -d