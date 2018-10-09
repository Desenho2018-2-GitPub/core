#!/usr/bin/env bash

server_addr="0.0.0.0:8080"

sleep 2
echo "** Checking if migrations to do **"
python3 manage.py makemigrations
echo "** Migrating changes if existent **"
python3 manage.py migrate

echo "** Waiting for DB **"
python3 /gitpub/scripts/wait_db.py || exit 1

echo "Running server on $server_addr"
python3 manage.py runserver $server_addr