# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: main
# @Author: xxxx
# @Time: 2024/10/2 18:45

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

import json
import traceback

import sqlglot
from tqdm import tqdm

import sys
sys.path.append("..")

from CrackSQL.translate import init_model, local_rewrite, direct_rewrite, direct_desc_rewrite
from CrackSQL.utils.tools import get_proj_root_path, load_config

config = load_config()
seg_on = config['seg_on']
mask_on = config['mask_on']
retrieval_on = config['retrieval_on']


def main():
    top_k = 5
    max_retry_time = 2

    model_id = "gpt-4o"

    ret_id = "all-MiniLM-L6-v2"
    db_id = "Chroma"

    db_name = "xxxx_BIRD"
    db_path = {"func": f"your chroma db path for function",
                "keyword": f"your chroma db path for keyword",
                "type": f"your chroma db path for data type"}
    
    src_dialect, tgt_dialect = "pg", "mysql"
    translator, retriever, vector_db = init_model(model_id, ret_id, db_id, db_path, top_k, tgt_dialect)
    
    data_load = f"your data load path"
    
    with open(data_load, "r", encoding="utf-8") as file:
        json_pairs = json.loads(file.read())

    trans_res = list()
    for pair in tqdm(json_pairs):
        if src_dialect in pair.keys():
            src_sql = pair[src_dialect]
        else:
            src_sql = pair["src_sql"]

        tgt_sql = str()
        if tgt_dialect in pair.keys():
            tgt_sql = pair[tgt_dialect]
        
        try:
            trans_sql, resp_list = direct_rewrite(translator, src_sql, src_dialect, tgt_dialect)
            # trans_sql, resp_list, used_pieces, lift_histories = local_rewrite(translator, retriever, vector_db,
            #                                                                     src_sql, src_dialect, tgt_dialect,
            #                                                                     db_name=db_name, top_k=top_k,
            #                                                                     max_retry_time=max_retry_time)

            trans_res.append(
                {"src_sql": src_sql, "tgt_sql": tgt_sql,
                    "trans_sql": trans_sql, "response": resp_list})
        except Exception as e:
            traceback.print_exc()

        
        with open("./exp_res/example.json", "w") as file:
            json.dump(trans_res, file, indent=4)

if __name__ == "__main__":
    main()
