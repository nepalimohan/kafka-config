#!/bin/bash
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec supervisord -c /app/supervisord.conf
