import logging
import re
import time

import func_timeout
from func_timeout import func_set_timeout

import paramiko
import pymysql
from pymysql.err import Error
import psycopg2
from psycopg2 import Error
import cx_Oracle

from utils.constants import oracle_locate_open

mysql_conn_map = {}
mysql_cursor_map = {}


def sql_execute(dialect: str, tgt_db_config: dict, sql: str):
    if dialect == 'pg':
        return pg_sql_execute(tgt_db_config, sql)
    elif dialect == 'mysql':
        return mysql_sql_execute(tgt_db_config, sql)
    elif dialect == 'oracle':
        return oracle_sql_execute(tgt_db_config, sql)
    else:
        raise ValueError(f"{dialect} is not supported")


def mysql_db_connect(db_config):
    dbname = db_config["db_name"]
    try:
        connection = pymysql.connect(database=db_config["db_name"],
                                     user=db_config["user"],
                                     password=db_config["password"],
                                     host=db_config["host"],
                                     port=db_config["port"])
        cursor = connection.cursor()
        mysql_conn_map[dbname] = connection
        mysql_cursor_map[dbname] = cursor
        if connection.open:
            return connection, cursor
    except Error as e:
        logging.error(f"Error while connecting to MySQL: {e}")


def mysql_sql_execute(db_config: dict, sql):
    db_name = db_config["db_name"]
    if db_name not in mysql_conn_map:
        mysql_db_connect(db_config)
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
        logging.info("MySQL connection is closed")


pg_conn_map = {}
pg_cursor_map = {}


def pg_db_connect(db_config):
    dbname = db_config["db_name"]
    try:
        connection = psycopg2.connect(database=db_config["db_name"],
                                      user=db_config["user"],
                                      password=db_config["password"],
                                      host=db_config["host"],
                                      port=db_config["port"])

        cursor = connection.cursor()

        pg_conn_map[dbname] = connection
        pg_cursor_map[dbname] = cursor
        if connection:
            return connection, cursor

    except (Exception, Error) as error:
        logging.error(f"Error while connecting to PostgreSQL: {error}")


def pg_sql_execute(db_config: dict, sql):
    db_name = db_config['db_name']
    if db_name not in pg_conn_map:
        pg_db_connect(db_config)
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
        logging.info("PostgreSQL connection is closed")


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


def oracle_db_connect(db_config):
    db_name = db_config["db_name"]  # db_config["user"]
    dsn = cx_Oracle.makedsn(db_config["host"], db_config["port"], service_name="your service")
    connection = cx_Oracle.connect(db_config["db_name"], db_config["password"], dsn)

    cursor = connection.cursor()

    oracle_cursor_map[db_name] = cursor
    oracle_conn_map[db_name] = connection
    return connection, cursor


def oracle_sql_execute(db_config: dict, sql, flag=False):
    db_name = db_config["db_name"]
    if db_name not in oracle_conn_map:
        oracle_db_connect(db_config)
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
            shell.send(f'sqlplus {db_config["db_name"]}/{db_config["password"]}@//'
                       f'{db_config["host"]}:{db_config["port"]}/your service\n')

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
        logging.info("Oracle connection is closed")
