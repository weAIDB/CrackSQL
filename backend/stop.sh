#!/bin/bash

pid=`ps -ef| grep "config/cracksql_gunicorn.conf wsgi_gunicorn:app"|grep -v grep|awk '{print $2}'|uniq`
if [[ -n "$pid" ]]
then
  echo "结束CrackSql进程, 进程PID为： $pid"
  kill -9 $pid
else
  echo "CrackSql未运行!"
  exit -1
fi