# TODO: 优化掉，用户自己填

TOP_K = 1
CHUNK_SIZE = 250

RETRIEVAL_ON = True
MAX_RETRY_TIME = 2
OUT_TYPE = "db"  # file, db

FAILED_TEMPLATE = 'Cannot translate!'

TRANSLATION_ANSWER_PATTERN = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
JUDGE_ANSWER_PATTERN = r'"SQL Snippet":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'

PARSER_LIST = ["pg", "mysql", "oracle"]

oracle_locate_open = False

DIALECT_MAP = {
    'pg': 'PostgreSQL 14.7',
    'mysql': "MySQL 8.4",
    'oracle': "Oracle 11g"
}
