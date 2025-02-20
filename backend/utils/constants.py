# TODO: 优化掉，用户自己填

TOP_K = 1

FAILED_TEMPLATE = 'Cannot translate!'

TRANSLATION_FORMAT = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)'

map_parser = ["pg", "mysql", "sqlite", "oracle"]

KNOWLEDGE_FIELD_LIST = ['Argument Type', 'Argument Type(s)',
                        'Aggregated Argument Type(s)',
                        'Direct Argument Type(s)', 'Return Type',
                        "Description", 'Example', 'Result',
                        'Example Query', 'Example Result', "Demo"]

oracle_locate_open = False

map_rep = {
    'pg': 'PostgreSQL 14.7',
    'mysql': "MySQL 8.4",
    'oracle': "Oracle 11g"
}

map_trans = {
    "Function": "func",
    "Keyword": "keyword",
    "Type": "type"
}

# https://huggingface.co/spaces/mteb/leaderboard

model_dict = {"all-MiniLM-L6-v2": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                                  "data/pretrained_model/all-MiniLM-L6-v2",
              "bge-large-en-v1.5": "/data/xxxx/llm_model/bge-large-en-v1.5",
              "codebert-base": "/data/xxxx/llm_model/codebert-base",
              "starencoder": "/data/xxxx/llm_model/starencoder",

              "stella_en_400M_v5": "/data/xxxx/llm_model/stella_en_400M_v5",
              "gte-large-en-v1.5": "/data/xxxx/llm_model/gte-large-en-v1.5",

              "multi-embed": "",
              "cross-lingual": {
                  "func": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                          "retriever/exp_res/exp_func_v2/model/rewrite_func25.pt",
                  "keyword": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                             "retriever/exp_res/exp_keyword/model/rewrite_keyword20.pt",
                  "type": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                          "retriever/exp_res/exp_v2/model/rewrite_type_50.pt"}
              }
