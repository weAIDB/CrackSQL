# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: dump_data
# @Author: xxxx
# @Time: 2024/10/2 10:12

import os
import re

os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # "-1"

import torch

import json
from tqdm import tqdm

from llama_index.retrievers.bm25 import BM25Retriever
from langchain_huggingface import HuggingFaceEmbeddings
from llama_index.core.node_parser import SimpleFileNodeParser

import sys

sys.path.append("/data/xxxx/index/sql_convertor/LLM4DB")

from CrackSQL.retriever.vector_db import VectorDB
from CrackSQL.retriever.retrieval_model import RetrievalModel, MultiEmbedding, CodeDescEmbedding

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_dict = {"all-MiniLM-L6-v2": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                                  "data/pretrained_model/all-MiniLM-L6-v2",
              "bge-large-en-v1.5": "/data/xxx/llm_model/bge-large-en-v1.5",
              "codebert-base": "/data/xxx/llm_model/codebert-base",
              "starencoder": "/data/xxx/llm_model/starencoder",

              "stella_en_400M_v5": "/data/xxx/llm_model/stella_en_400M_v5",
              "gte-large-en-v1.5": "/data/xxx/llm_model/gte-large-en-v1.5",

              "multi-embed": "",
              "cross-lingual": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/retriever/"
                               "exp_res/exp_res/model/rewrite_Train_25.pt"}

doc_dir = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/processed_document"

# keyword
dialect_load_keyword = {"pg": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                              "processed_document/pg/pg_keyword_ready.json",
                        "mysql": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                 "processed_document/mysql/mysql_keyword_ready.json",
                        "oracle": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                  "processed_document/oracle/oracle_19_keyword_ready.json"}

# data type
dialect_load_type = {"pg": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                           "processed_document/pg/pg_type_ready.json",
                     "mysql": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                              "processed_document/mysql/mysql_8_type_ready.json",
                     "oracle": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                               "processed_document/oracle/oracle_11_type_ready.json"}

# built-in function
dialect_load_function = {"pg": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                               "processed_document/pg/pg_1_function_ready_compensate.json",
                         "mysql": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                  "processed_document/mysql/mysql_function_ready.json",
                         "oracle": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                   "processed_document/oracle/oracle_11_function_ready.json"}


def get_keyword_text(db, item):
    if db == "postgres":
        item["KEYWORD"] = list()
        for field in ['Name']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])
        #     item["KEYWORD"] += f'{content}<sep>'
        # item["KEYWORD"] = re.sub(r'(<sep>)+', '<sep>', item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description', 'Demo']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    elif db == "mysql":
        item["KEYWORD"] = list()
        for field in ["Name"]:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description', 'Demo', 'Detail']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    elif db == "oracle":
        item["KEYWORD"] = list()
        for field in ["Name"]:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description', 'Demo']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(str(content))
        item["DESC"] = "<sep>".join(item["DESC"])

    return item["KEYWORD"], item["DESC"]


def get_type_text(db, item):
    if db == "postgres":
        item["KEYWORD"] = list()
        for field in ['Name']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description', 'Storage Size', 'Range',
                      'Low Value', 'High Value', 'Compensate']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    elif db == "mysql":
        item["KEYWORD"] = list()
        for field in ["Name"]:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description', 'Storage (Bytes)',
                      'Minimum Value Signed', 'Maximum Value Signed', 'Compensate']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    elif db == "oracle":
        item["KEYWORD"] = list()
        for field in ["Name"]:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    return item["KEYWORD"], item["DESC"]


def get_func_text(db, item):
    if db == "postgres":
        item["KEYWORD"] = list()
        for field in ["Name", 'Argument Type', 'Argument Type(s)',
                      'Aggregated Argument Type(s)',
                      'Direct Argument Type(s)', 'Return Type']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description', 'Example', 'Result',
                      'Example Query', 'Example Result',
                      'compensate']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    elif db == "mysql":
        item["KEYWORD"] = list()
        for field in ["Name"]:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description', 'Demo', 'Detail']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    elif db == "oracle":
        item["KEYWORD"] = list()
        for field in ["Name"]:
            content = item.get(field, "")
            if isinstance(content, list):
                item["KEYWORD"].extend(content)
            else:
                item["KEYWORD"].append(content)
        item["KEYWORD"] = "<sep>".join(item["KEYWORD"])

        item["DESC"] = list()
        for field in ['Description']:
            content = item.get(field, "")
            if isinstance(content, list):
                item["DESC"].extend(content)
            else:
                item["DESC"].append(content)
        item["DESC"] = "<sep>".join(item["DESC"])

    return item["KEYWORD"], item["DESC"]


def pre_db_docs(db, model_id, typ, data, is_dict=False):
    """
    ['Keyword', 'Src', 'Tree', 'Route', 'Description', 'Demo', 'Count']
    :param model_id:
    :param data:
    :param is_dict:
    :return:
    """
    if model_id == "BM25":
        from llama_index.core import Document
        docs = list()
        for item in data:
            if item["Dialect"] != db:
                continue

            if typ == "func":
                keyword, desc = get_func_text(db, item)
                docs.append(Document(text=desc,
                                     metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))
            elif typ == "keyword":
                keyword, desc = get_keyword_text(db, item)
                docs.append(Document(text=desc,
                                     metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))
            elif typ == "type":
                keyword, desc = get_type_text(db, item)
                docs.append(Document(text=desc,
                                     metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))
    else:
        from langchain_core.documents import Document
        docs = list()
        if is_dict:
            for item in data:
                if db == "pg":
                    db = "postgres"

                if item["Dialect"] != db:
                    continue

                if typ == "func":
                    keyword, desc = get_func_text(db, item)
                    docs.append(Document(page_content=f"{keyword}"
                                                      f"--separator--"
                                                      f"{desc}",
                                         metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))
                elif typ == "keyword":
                    keyword, desc = get_keyword_text(db, item)
                    docs.append(Document(page_content=f"{keyword}"
                                                      f"--separator--"
                                                      f"{desc}",
                                         metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))
                elif typ == "type":
                    keyword, desc = get_type_text(db, item)
                    docs.append(Document(page_content=f"{keyword}"
                                                      f"--separator--"
                                                      f"{desc}",
                                         metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))

        else:
            for item in data:
                if db == "pg":
                    db = "postgres"

                if item["Dialect"] != db:
                    continue

                if typ == "func":
                    keyword, desc = get_func_text(db, item)
                    docs.append(Document(page_content=desc,
                                         metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))
                elif typ == "keyword":
                    keyword, desc = get_keyword_text(db, item)
                    docs.append(Document(page_content=desc,
                                         metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))
                elif typ == "type":
                    keyword, desc = get_type_text(db, item)
                    docs.append(Document(page_content=desc,
                                         metadata={"KEYWORD": keyword, "DESC": desc, "ALL": str(item)}))

    docs_raw = data

    return docs, docs_raw


def data_to_db():
    top_k = 5
    batch_size = 64

    typ = "func"  # func, keyword, type
    data_load = f"/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                f"processed_document/three_dialects_{typ}_fine.json"
    with open(data_load, "r") as rf:
        data_temp = json.load(rf)

    data = list()
    if isinstance(data_temp, list):
        for item in data_temp:
            data.extend(item)
    elif isinstance(data_temp, dict):
        for item in data_temp.values():
            data.extend(item)

    db_list = ["mysql", "pg", "oracle"]
    model_list = list(model_dict.keys())
    for db in tqdm(db_list):
        for model in model_list:
            if model == "cross-lingual":
                is_dict = True
            else:
                is_dict = False

            # 1. prepare documents.
            docs, docs_raw = pre_db_docs(db, model, typ, data, is_dict=is_dict)

            # 2. build retriever
            retriever = RetrievalModel(model)

            # 3. build vector databases.
            if model == "BM25":
                db_id = "BM25"  # Chroma, BM25
            else:
                db_id = "Chroma"
                db_path = f"/data/xxxx/index/sql_convertor/LLM4DB/" \
                          f"LLM4DB/data/chroma_db/{db}_{typ}_{model}"

                if model == "multi-embed":
                    embed_func = MultiEmbedding()

                elif model == "cross-lingual":
                    embed_func = CodeDescEmbedding(input_sizes=(768, 384, 1024, 1024), hidden_size=512,
                                                   num_experts=2, num_heads=4, dropout=0.05).to(device)
                    embed_func = torch.nn.DataParallel(embed_func)

                    model_source = torch.load(model_dict[model], map_location=device)
                    embed_func.load_state_dict(model_source["model"])

                    embed_func = embed_func.module
                    embed_func.eval()

                else:
                    embed_func = HuggingFaceEmbeddings(model_name=model_dict[model])

            if db_id == "BM25":
                vector_db = VectorDB(db_id, embed_func=BM25Retriever)
                docs = SimpleFileNodeParser().get_nodes_from_documents(docs)
                vector_db.load_vector(docs, top_k=top_k)
            else:
                vector_db = VectorDB(db_id, db_path, embed_func)
                if not os.path.exists(db_path):
                    vector_db.load_vector(docs, batch_size=batch_size)
                vector_db.load_vector(docs, batch_size=batch_size)

if __name__ == "__main__":
    data_to_db()
