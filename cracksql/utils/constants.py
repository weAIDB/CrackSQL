# TODO: 优化掉，用户自己填

TOP_K = 1
CHUNK_SIZE = 250

RETRIEVAL_ON = True
MAX_RETRY_TIME = 2

FAILED_TEMPLATE = 'Cannot translate!'

TRANSLATION_ANSWER_PATTERN = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
JUDGE_ANSWER_PATTERN = r'"SQL Snippet":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'

DIALECT_LIST = ["pg", "mysql", "oracle"]
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
