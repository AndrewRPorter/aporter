#!/bin/bash

source .env/bin/activate
gunicorn --bind localhost:5000 --reload "app.main:create_app()"
deactivate