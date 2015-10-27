#!/bin/bash

mkdir -p /home/docker/code/pids

cd /home/docker/code
python3 manage.py migrate --noinput --fake-initial
python3 manage.py collectstatic --noinput

chown -R www-data:www-data /home/docker/code/
chmod -R u+rwX,go+rX /home/docker/code/

supervisord -n
