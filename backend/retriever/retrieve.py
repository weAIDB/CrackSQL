# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: retriever_model
# @Author: xxxx
# @Time: 2024/9/1 19:13

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # "-1"

import torch

import json
from tqdm import tqdm

from sentence_transformers import SentenceTransformer

# from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.retrievers.bm25 import BM25Retriever

import sys
sys.path.append(".")

from CrackSQL.retriever.vector_db import VectorDB
from CrackSQL.retriever.retrieval_model import RetrievalModel, MultiEmbedding, CodeDescEmbedding, HuggingBackboneV2

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"  # "-1"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# https://huggingface.co/spaces/mteb/leaderboard

model_dict = {
    "all-MiniLM-L6-v2": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/"
                        "data/pretrained_model/all-MiniLM-L6-v2",
    "bge-large-en-v1.5": "/data/xxx/llm_model/bge-large-en-v1.5",
    "codebert-base": "/data/xxx/llm_model/codebert-base",
    "starencoder": "/data/xxx/llm_model/starencoder",

    "stella_en_1.5B_v5": "/data/xxx/llm_model/stella_en_1.5B_v5",
    "stella_en_400M_v5": "/data/xxx/llm_model/stella_en_400M_v5",
    "gte-large-en-v1.5": "/data/xxx/llm_model/gte-large-en-v1.5",

    "multi-embed": "",
    "cross-lingual": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/retriever/"
                     "exp_res/exp_pre/model/rewrite_Train_25.pt"
}

dialect_load = {"pg": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                      "official_document/pg/pg_14_built-in-function.json",
                "mysql": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                         "official_document/mysql/mysql_function/mysql_8.4_built-in-function.json",
                "oracle": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                          "processed_document/oracle/oracle_11_built-in-function.json"}


def pre_short_docs(model_id, data_load, is_dict=False):
    with open(data_load, "r") as rf:
        data = json.load(rf)

    if "mysql_8.4_built-in-function" in data_load:
        if model_id == "BM25":
            from llama_index.core import Document
            docs = [Document(text=f"{item['Description']}. {item['Detail']}",
                             metadata={"Function": item["Name"],
                                       "Link": item["Link"]}) for item in data]
        else:
            from langchain_core.documents import Document
            if is_dict:
                docs = [Document(page_content=f"{item['Name']}"
                                              f"--separator--"
                                              f"{item['Description']}. {item['Detail']}",
                                 metadata={"Function": item["Name"],
                                           "Link": item["Link"]}) for item in data]
            else:
                docs = [Document(page_content=f"{item['Description']}. {item['Detail']}",
                                 metadata={"Function": item["Name"],
                                           "Link": item["Link"]}) for item in data]

        docs_raw = data

    elif "pg_14_built-in-function" in data_load:
        docs, docs_raw = list(), list()
        for table in data:
            header = table[0]
            if header[0] not in ["Operator", "Function", "Name"]:
                continue

            for row in table[1:]:
                if len(row) != len(header):
                    continue

                if model_id == "BM25":
                    from llama_index.core import Document
                    docs.append(Document(text=" ".join([f"{row[h]}" for h in header[1:]]),
                                         metadata={header[0]: row[header[0]]}))
                else:
                    from langchain_core.documents import Document
                    if is_dict:
                        docs.append(Document(page_content=f"{row[header[0]]}"
                                                          f"--separator--"
                                                          f"{' '.join([row[h] for h in header[1:]])}",
                                             metadata={header[0]: row[header[0]]}))
                    else:
                        docs.append(Document(page_content=" ".join([f"{row[h]}" for h in header[1:]]),
                                             metadata={header[0]: row[header[0]]}))

                docs_raw.append(row)

    elif "oracle_11_built-in-function" in data_load:
        if model_id == "BM25":
            from llama_index.core import Document
            docs = [Document(text=item["Description"],
                             metadata={"Function": item["Name"],
                                       "Link": item["Link"]}) for item in data]
        else:
            from langchain_core.documents import Document
            if is_dict:
                docs = [Document(page_content=f"{item['Name']}"
                                              f"--separator--"
                                              f"{item['Description']}",
                                 metadata={"Function": item["Name"],
                                           "Link": item["Link"]}) for item in data]
            else:
                docs = [Document(page_content=item["Description"],
                                 metadata={"Function": item["Name"],
                                           "Link": item["Link"]}) for item in data]

        docs_raw = data

    return docs, docs_raw


def pre_long_docs(data_load, long_conf=dict(chunk_size=500,
                                            chunk_overlap=200,
                                            length_function=len)):
    with open(data_load, "r") as rf:
        data = json.load(rf)

    text_splitter = RecursiveCharacterTextSplitter(**long_conf)

    docs = text_splitter.split_text(data)

    return docs


def eval_retriever(model, data_load, retriever,
                   vector_db, top_k, data_save, is_dict):
    docs, docs_raw = pre_short_docs(model, data_load, is_dict=is_dict)

    result_list = list()
    for query in tqdm(docs_raw):
        query_str = "; ".join([f"{item[0]}: {item[1]}" for item in list(query.items())[1:]])
        if retriever.model_id == "BM25":
            results = retriever.retrieve(query_str, vector_db, top_k)
            results_li = [{"page_content": res.text,
                           "metadata": res.metadata,
                           "score": res.score} for res in results]
        else:
            if is_dict:
                query_str = f"{list(query.values())[0]}--separator--{query_str}"
            results = retriever.retrieve(query_str, vector_db, top_k)
            results_li = [{"page_content": res[0].page_content,
                           "metadata": res[0].metadata,
                           "score": res[1]} for res in results]

        result_list.append({"query": query, "results": results_li})

    with open(data_save, "w") as wf:
        json.dump(result_list, wf, indent=2)


def main():
    top_k = 5
    batch_size = 64

    trans_list = [("pg", "mysql"), ("mysql", "pg"), ("pg", "oracle"),
                  ("oracle", "pg"), ("mysql", "oracle"), ("oracle", "mysql")]
    model_list = list(model_dict.keys())
    for src, tgt in trans_list:
        for model in model_list:
            if model == "cross-lingual":
                is_dict = True
            else:
                is_dict = False

            # 1. prepare documents.
            data_load = dialect_load[tgt]
            docs, docs_raw = pre_short_docs(model, data_load, is_dict=is_dict)

            # 2. build retriever
            retriever = RetrievalModel(model)

            # 3. build vector databases.
            if model == "BM25":
                db_id = "BM25"  # Chroma, BM25
            else:
                db_id = "Chroma"
                db_path = f"/data/xxxx/index/sql_convertor/data_resource/chroma_db/{tgt}_built_in_{model}"

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
                    model_kwargs = {'trust_remote_code': True}
                    embed_func = HuggingFaceEmbeddings(model_name=model_dict[model],
                                                       model_kwargs=model_kwargs)

            if db_id == "BM25":
                vector_db = VectorDB(db_id, embed_func=BM25Retriever)
                docs = SimpleFileNodeParser().get_nodes_from_documents(docs)
                vector_db.load_vector(docs, top_k=top_k)
            else:
                vector_db = VectorDB(db_id, db_path, embed_func)
                vector_db.load_vector(docs, batch_size=batch_size)
                # vector_db.db.get(include=["embeddings", "metadatas", "documents"])

            # 4. get results
            data_load = dialect_load[src]
            data_save = f"/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/" \
                        f"retriever/rag_res/{src}_{tgt}_short_{model}_res.json"

            eval_retriever(model, data_load, retriever,
                           vector_db.db, top_k, data_save, is_dict)


if __name__ == "__main__":
    main()
