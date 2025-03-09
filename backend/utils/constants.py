# TODO: 优化掉，用户自己填

TOP_K = 1
CHUNK_SIZE = 250

RETRIEVAL_ON = True
MAX_RETRY_TIME = 2

MAX_TOKENS_DEFAULT = 8192
TEMPERATURE_DEFAULT = 0.0
FAILED_TEMPLATE = 'Cannot translate!'

TRANSLATION_ANSWER_PATTERN = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
JUDGE_ANSWER_PATTERN = r'"SQL Snippet":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'

DIALECT_LIST = ["pg", "mysql", "oracle"]
DIALECT_LIST_RULE = ["athena", "bigquery", "clickhouse", "databricks", "doris", "drill", "druid",
                     "duckdb", "dune", "hive", "materialize", "mysql", "oracle", "postgres",
                     "presto", "prql", "redshift", "risingwave", "snowflake", "spark", "spark2",
                     "sqlite", "starrocks", "tableau", "teradata", "trino", "tsql", "postgresql"]
DIALECT_MAP = {
    'pg': 'PostgreSQL 14.7',
    'mysql': "MySQL 8.4",
    'oracle': "Oracle 11g"
}

ORACLE_COMMAND_OPEN = False

TRANSLATION_RESULT_TEMP = r"""
The translated SQL is:
```sql
{translated_sql}
```
"""
