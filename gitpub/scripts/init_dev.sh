#!/usr/bin/env bash

python3 manage.py makemigrations
python3 manage.py migrate

echo "** Starting application **"
python3 /gitpub/scripts/wait_db.py && python3 manage.py runserver 0.0.0.0:8080
