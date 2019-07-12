#!/bin/bash

cd aporter
exec gunicorn app.wsgi \
              --bind 0.0.0.0:8000 \
              --workers 4
