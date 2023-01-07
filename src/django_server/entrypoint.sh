#!/bin/bash

cd django_server

python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

#python3 manage.py runserver 0.0.0.0:8000

# Launch WSGI server
gunicorn --bind 0.0.0.0:8000 django_server.wsgi:application
