#!/usr/bin/env bash

python3 manage.py makemigrations
python3 manage.py migrate

echo "** Waiting for DB **"
python3 /gitpub/scripts/wait_db.py || exit 1

echo "Django App starting..."
python3 manage.py runserver 0.0.0.0:8080