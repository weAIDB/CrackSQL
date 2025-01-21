#!/usr/bin/env sh

# 启动FlaskAPP
nohup gunicorn -c config/cracksql_gunicorn.conf wsgi_gunicorn:app &
