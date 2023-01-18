#!/bin/bash

python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

# Launch WSGI server
gunicorn --bind :8000 django_server.wsgi:application
