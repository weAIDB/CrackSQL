#!/usr/bin/env sh

# Start FlaskAPP
nohup gunicorn -c config/cracksql_gunicorn.conf wsgi_gunicorn:app &
