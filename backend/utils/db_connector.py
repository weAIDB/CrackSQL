import re
import subprocess
import sys

import time

import func_timeout
from func_timeout import func_set_timeout

import paramiko
import pymysql
from pymysql.err import Error

import psycopg2
from psycopg2 import Error

import cx_Oracle

from utils.tools import load_config

mysql_conn_map = {}
mysql_cursor_map = {}

config = load_config()
oracle_locate_open = config['oracle_locate_open']


def sql_execute(dialect: str, db_name: str, sql: str):
    if dialect == 'pg':
        return pg_sql_execute(db_name, sql)
    elif dialect == 'mysql':
        return mysql_sql_execute(db_name, sql)
    elif dialect == 'oracle':
        return oracle_sql_execute(db_name, sql)
    else:
        raise ValueError(f"{dialect} is not supported")


def mysql_db_connect(dbname):
    try:
        connection = pymysql.connect(
            host='your host', 
            port='your port',  
            user='your name',  
            password='your password',
            database="your database"
        )
        cursor = connection.cursor()
        mysql_conn_map[dbname] = connection
        mysql_cursor_map[dbname] = cursor
        if connection.open:
            return connection, cursor
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")


def mysql_sql_execute(db_name: str, sql):
    if db_name not in mysql_conn_map:
        mysql_db_connect(db_name)
    connection = mysql_conn_map[db_name]
    cursor = mysql_cursor_map[db_name]
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        connection.commit()
        return True, rows
    except pymysql.Error as e:
        connection.rollback()
        return False, e.args[1]


def close_mysql_connnect(dbname: str):
    connection = mysql_conn_map[dbname]
    cursor = mysql_cursor_map[dbname]
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


pg_conn_map = {}
pg_cursor_map = {}


def pg_db_connect(dbname):
    try:
        connection = psycopg2.connect(database="your database",
                                      user="your name",
                                      password="your password",
                                      host="your host",
                                      port="your port")

        cursor = connection.cursor()

        pg_conn_map[dbname] = connection
        pg_cursor_map[dbname] = cursor
        if connection:
            return connection, cursor

    except (Exception, Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")


def pg_sql_execute(db_name: str, sql):
    if db_name not in pg_conn_map:
        pg_db_connect(db_name)
    connection = pg_conn_map[db_name]
    cursor = pg_cursor_map[db_name]
    try:
        cursor.execute(sql)
        if cursor.description:
            rows = cursor.fetchall()
        else:
            rows = None
        connection.commit()
        return True, rows
    except (Exception, Error) as error:
        connection.rollback()
        return False, f"Error while executing PostgreSQL query: {error}"


def close_pg_connect(db_name: str):
    connection = pg_conn_map[db_name]
    cursor = pg_cursor_map[db_name]
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


oracle_conn_map = {}
oracle_cursor_map = {}


@func_set_timeout(6)
def read_output(shell, prompt, timeout=15):
    start_time = time.time()

    output = str()
    while True:
        output += shell.recv(1024).decode('utf-8')

        # Check for the shell prompt to know when the command has finished
        if re.search(prompt, output):
            break

        # Check for timeout
        if time.time() - start_time > timeout:
            break

        time.sleep(0.1)  # Small delay to avoid busy waiting

    return output


def oracle_db_connect(db_name):
    dsn = cx_Oracle.makedsn("your host", "your port", service_name="your service")
    connection = cx_Oracle.connect("your database", "your password", dsn)

    cursor = connection.cursor()

    oracle_cursor_map[db_name] = cursor
    oracle_conn_map[db_name] = connection
    return connection, cursor


def oracle_sql_execute(db_name: str, sql, flag=False):
    if db_name not in oracle_conn_map:
        oracle_db_connect(db_name)
    connection = oracle_conn_map[db_name]
    cursor = oracle_cursor_map[db_name]
    try:
        cursor.execute(sql.strip(';'))
        rows = cursor.fetchall()
        connection.commit()
        return True, rows
    except (Exception, Error) as error:
        connection.rollback()
        if oracle_locate_open:
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("your host", username='your name', password='your password')

            shell = ssh.invoke_shell()
            shell.send(f'sqlplus xxxx/xxxx@//xxxx:xxxx/xxxx\n')

            time.sleep(2)

            try:
                read_output(shell, prompt="SQL>")

                shell.send(f"{sql.strip(';')};\n")

                output = read_output(shell, "SQL>")
                output = output.replace(f"{sql.strip(';')};\r\n", "").replace("\r\n\r\n\r\nSQL>", "")
            except func_timeout.exceptions.FunctionTimedOut as e:
                ssh.close()
                return False, f"Error occurs while executing the query: {error}"

            ssh.close()
            return False, output
        else:
            return False, f"Error occurs while executing the query: {error}"


def close_oracle_connect(db_name: str):
    connection = oracle_conn_map[db_name]
    cursor = oracle_cursor_map[db_name]
    if connection:
        cursor.close()
        connection.close()
        print("Oracle connection is closed")
