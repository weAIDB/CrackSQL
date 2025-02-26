#!/bin/bash

pid=`ps -ef| grep "config/cracksql_gunicorn.conf wsgi_gunicorn:app"|grep -v grep|awk '{print $2}'|uniq`
if [[ -n "$pid" ]]
then
  echo "Stopping CrackSql process, PID: $pid"
  kill -9 $pid
else
  echo "CrackSql is not running!"
  exit -1
fi