import psycopg2
import time
import os

pg_user = 'postgres'
pg_psw = 'postgres'
pg_db = 'postgres'
pg_host = 'db'


start = time.time()
success = False
param = "dbname='{}' user='{}' host='{}' password='{}'".format(
    pg_db, pg_user, pg_host, pg_psw)

while True:
    try:
        db = psycopg2.connect(param)
        success = True
        break
    except BaseException:
        print('No DB connection')
    end = time.time()
    if not success and end - start >= 15:
        print('ERROR: request timeout of 15 seconds')
        exit(1)
    time.sleep(1)
    print('Trying again')

print('Success on DB connection')
