import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"

from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.retrievers.bm25 import BM25Retriever

from retriever.dump_data import pre_db_docs

import torch
from tqdm import tqdm

import sys
import re
import json
import copy
import traceback
import sqlglot
from typing import Dict
from datetime import datetime

from langchain_huggingface import HuggingFaceEmbeddings

from preprocessor.antlr_parser.parse_tree import parse_tree
from preprocessor.query_simplifier.Tree import TreeNode, lift_node
from preprocessor.query_simplifier.rewrite import get_all_piece, reformat, \
    get_masked_slices, try_mark_tree_node, parse_llm_answer, get_all_tgt_used_piece
from preprocessor.query_simplifier.locate import locate_node_piece, replace_piece, get_func_name, \
    find_piece
from preprocessor.query_simplifier.normalize import normalize
from preprocessor.query_simplifier.type_mask import mask_type_node

from retriever.retrieval_model import RetrievalModel, CodeDescEmbedding
from retriever.vector_db import VectorDB
from translator.translate_prompt import SYSTEM_PROMPT_NA, USER_PROMPT_NA, \
    SYSTEM_PROMPT_SEG, USER_PROMPT_SEG, SYSTEM_PROMPT_MASK, USER_PROMPT_MASK, USER_ADVICE_MASK, \
    SYSTEM_PROMPT_RET, USER_PROMPT_RET, SYSTEM_PROMPT_DIR, USER_PROMPT_DIR, EXAMPLE_PROMPT
from translator.judge_prompt import SYSTEM_PROMPT_JUDGE, USER_PROMPT_JUDGE, USER_PROMPT_REFLECT
from translator.llm_translator import LLMTranslator
from utils.tools import get_proj_root_path, load_config, extract_json, parse_llm_answer_v2

chunk_size = 100
build_in_function_map = {}

config = load_config()
dbg = config['dbg']
use_test = config['use_test']
reflect_on = config['reflect_on']
slice_only = config['slice_only']
mask_on = config['mask_on']
locate_by_err = config['locate_by_err']

seg_on = config['seg_on']
retrieval_on = config['retrieval_on']

gpt_api_base = config['gpt_api_base']
gpt_api_key = config['gpt_api_key']
llama_3_1_api_base = config['llama3.1_api_base']
llama_3_2_api_base = config['llama3.2_api_base']

codellama_api_base = config['codellama_api_base']
codeqwen2_5_api_base = config['codeqwen2.5_api_base']
qwen2_5_api_base = config['qwen2.5_api_base']

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

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# https://huggingface.co/spaces/mteb/leaderboard

ret_bak_id = "bge-large-en-v1.5"

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


def init_model(model_id, ret_id, db_id, db_path, top_k, tgt_dialect=None):
    translator, retriever, vector_db = None, None, None
    retriever_bm25, vector_bm25 = None, None
    retriever_bak, vector_db_bak = None, None

    if "gpt-" in model_id:
        openai_conf = {"temperature": 0}
        api_base = gpt_api_base
        api_key = gpt_api_key

        translator = LLMTranslator(model_id, openai_conf)
        translator.load_model(api_base, api_key)

    elif model_id == "llama3.1":
        api_base = llama_3_1_api_base
        translator = LLMTranslator(model_id)
        translator.load_model(api_base)

    elif model_id == "llama3.2":
        api_base = llama_3_2_api_base
        translator = LLMTranslator(model_id)
        translator.load_model(api_base)

    elif model_id == "codellama":
        api_base = codellama_api_base
        translator = LLMTranslator(model_id)
        translator.load_model(api_base)

    elif model_id == "codeqwen2.5":
        api_base = codeqwen2_5_api_base
        translator = LLMTranslator(model_id)
        translator.load_model(api_base)

    elif model_id == "qwen2.5":
        api_base = qwen2_5_api_base
        translator = LLMTranslator(model_id)
        translator.load_model(api_base)

    if retrieval_on:
        retriever_bm25 = RetrievalModel("BM25")
        vector_bm25 = dict()
        for key in ["func", "keyword", "type"]:
            vector_bm25[key] = VectorDB("BM25", embed_func=BM25Retriever)
            data_load = f"./data/processed_document/three_dialects_{key}_fine.json"
            with open(data_load, "r") as rf:
                data_temp = json.load(rf)

            data = list()
            if isinstance(data_temp, list):
                for item in data_temp:
                    data.extend(item)
            elif isinstance(data_temp, dict):
                for item in data_temp.values():
                    data.extend(item)

            dialect = tgt_dialect
            if tgt_dialect == "pg":
                dialect = "postgres"

            docs_pre, _ = pre_db_docs(dialect, "BM25", key, data, is_dict=False)
            docs_pre = SimpleFileNodeParser().get_nodes_from_documents(docs_pre)
            vector_bm25[key].load_vector(docs_pre, top_k=top_k)

        retriever = RetrievalModel(ret_id)
        vector_db = dict()
        if ret_id != "BM25":
            if ret_id == "cross-lingual":
                embed_func = dict()
                for key in model_dict[ret_id].keys():
                    embed_func[key] = CodeDescEmbedding(input_sizes=(768, 384, 1024, 1024), hidden_size=512,
                                                        num_experts=2, num_heads=4, dropout=0.05).to(device)
                    embed_func[key] = torch.nn.DataParallel(embed_func[key])

                    model_source = torch.load(model_dict[ret_id][key], map_location=device)
                    embed_func[key].load_state_dict(model_source["model"])

                    embed_func[key] = embed_func[key].module
                    embed_func[key].eval()
            else:
                embed_func = HuggingFaceEmbeddings(model_name=model_dict[ret_id])

            for key in ["func", "keyword", "type"]:
                if isinstance(embed_func, dict):
                    vector_db[key] = VectorDB(db_id, db_path[key], embed_func[key])
                else:
                    vector_db[key] = VectorDB(db_id, db_path[key], embed_func)
        else:
            for key in ["func", "keyword", "type"]:
                vector_db[key] = VectorDB(db_id, embed_func=BM25Retriever)
                data_load = f"./data/processed_document/three_dialects_{key}_fine.json"
                with open(data_load, "r") as rf:
                    data_temp = json.load(rf)

                data = list()
                if isinstance(data_temp, list):
                    for item in data_temp:
                        data.extend(item)
                elif isinstance(data_temp, dict):
                    for item in data_temp.values():
                        data.extend(item)

                dialect = tgt_dialect
                if tgt_dialect == "pg":
                    dialect = "postgres"

                docs_pre, _ = pre_db_docs(dialect, ret_id, key, data, is_dict=False)
                docs_pre = SimpleFileNodeParser().get_nodes_from_documents(docs_pre)
                vector_db[key].load_vector(docs_pre, top_k=top_k)

        retriever_bak = RetrievalModel(ret_bak_id)
        vector_db_bak = dict()
        embed_func = HuggingFaceEmbeddings(model_name=model_dict[ret_bak_id])
        for key in ["func", "keyword", "type"]:
            vector_db_bak[key] = VectorDB("Chroma", f"./data/chroma_db/{tgt_dialect}_{key}_{ret_bak_id}", embed_func)
    else:
        return translator, None, None

    return translator, (retriever_bm25, retriever, retriever_bak), (vector_bm25, vector_db, vector_db_bak)


def direct_rewrite(translator, src_sql, src_dialect, tgt_dialect):
    model_ans_list = list()

    sys_prompt = None
    user_prompt = USER_PROMPT_DIR.format(src_dialect=map_rep[src_dialect],
                                         tgt_dialect=map_rep[tgt_dialect], sql=src_sql).strip("\n")

    answer_raw = translator.trans_func([], sys_prompt, user_prompt)
    pattern = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
    now_sql = parse_llm_answer(translator.model_id, answer_raw, pattern)

    answer_raw["Action"] = "translate"
    answer_raw["Time"] = str(datetime.now())
    answer_raw["SYSTEM_PROMPT"] = sys_prompt
    answer_raw["USER_PROMPT"] = user_prompt

    model_ans_list.append(answer_raw)

    return now_sql, model_ans_list


def direct_desc_rewrite(translator, retriever, vector_db, src_sql, src_dialect, tgt_dialect):
    hint, example = str(), str()

    src_sql = src_sql.strip(';')
    input_sql = src_sql

    try:
        root_node, line, col, msg = parse_tree(src_sql, src_dialect)
        if root_node is None:
            raise ValueError(f"Parse error when executing ANTLR parser of {src_dialect}.\n"
                             f"The sql is {src_sql}")
        all_pieces, root_node = get_all_piece(root_node, src_dialect)
        flag = True
        for piece in all_pieces:
            if root_node == piece['Node']:
                flag = False
                break
        if flag:
            root_piece = {
                "Node": root_node,
                "Tree": root_node,
                "Description": {"Type": "Keyword",
                                "Desc": "The whole SQL snippet above."},
                "Keyword": '',
                "SubPieces": [piece for piece in all_pieces],
                "FatherPiece": None,
                "Count": 0,
                'TrackPieces': []
            }
            for piece in all_pieces:
                if piece['FatherPiece'] is None:
                    piece['FatherPiece'] = root_piece
            all_pieces.append(root_piece)

        normalize(root_node, src_dialect, tgt_dialect)
        src_sql = str(root_node)
    except ValueError as ve:
        traceback.print_exc()
        print(f"Antlr parse error: {src_sql}, translate cancelled, "
              f"dialect: {src_dialect}\n{ve}", file=sys.stderr)
        return str(ve), [], [], []

    if len(all_pieces) == 0:
        return src_sql, ['Warning: No piece find'], [], []

    src_key, src_desc = list(), list()
    for piece in all_pieces:
        if piece['Keyword'] is not None and piece['Keyword'] not in src_key:
            src_key.append(str(piece['Keyword']))
            src_desc.append(piece['Description'])
        for sub_piece in piece['SubPieces']:
            if sub_piece['Keyword'] is not None and sub_piece['Keyword'] not in src_key:
                src_key.append(sub_piece['Keyword'])
                src_desc.append(sub_piece['Description'])

    document = list()
    for key, desc in zip(src_key, src_desc):
        if desc is None:
            continue

        if desc["Desc"] == "The whole SQL snippet above.":
            continue

        results = list()
        model_id = retriever[1].model_id
        if desc['Type'] == 'Keyword':
            continue

        elif desc['Type'] == 'Type':
            if model_id == "BM25":
                results.extend(
                    retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:top_k])

            else:
                if model_id == "cross-lingual":
                    results.extend(
                        [ite[0] for ite in retriever[1].retrieve(str(key) + '--separator--' + str(desc),
                                                                 vector_db[1][
                                                                     map_trans[desc["Type"]]].db,
                                                                 top_k=2)])
                else:
                    results.extend([ite[0] for ite in
                                    retriever[1].retrieve(str(desc),
                                                          vector_db[1][map_trans[desc["Type"]]].db,
                                                          top_k=2)])
            results.extend(retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:1])

        elif desc['Type'] == 'Function':
            if model_id == "BM25":
                results.extend(
                    retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:top_k])

            else:
                if model_id == "cross-lingual":
                    results.extend(
                        [ite[0] for ite in retriever[1].retrieve(str(key) + '--separator--' + str(desc),
                                                                 vector_db[1][
                                                                     map_trans[desc["Type"]]].db,
                                                                 top_k=2)])
                else:
                    results.extend([ite[0] for ite in
                                    retriever[1].retrieve(str(desc),
                                                          vector_db[1][map_trans[desc["Type"]]].db,
                                                          top_k=2)])
            results.extend([ite[0] for ite in
                            retriever[-1].retrieve(str(desc), vector_db[-1][map_trans[desc["Type"]]].db,
                                                   top_k=2)])
            results.extend(retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:1])

        results_key = set()
        results_pre = list()
        for ite in results[:top_k]:
            if ite.metadata["KEYWORD"] not in results_key:
                results_key.add(ite.metadata["KEYWORD"])
                results_pre.append(ite)

        tgt_key = [re.sub(r'(<sep>)(\1){2,}', r'\1', ite.metadata["KEYWORD"]) for ite in results_pre]

        tgt_desc = list()
        for ite in results_pre:
            temp = list()
            try:
                detail = eval(ite.metadata["ALL"])
                for field in ['Argument Type', 'Argument Type(s)',
                              'Aggregated Argument Type(s)',
                              'Direct Argument Type(s)', 'Return Type',
                              "Description", 'Example', 'Result',
                              'Example Query', 'Example Result', "Demo"]:
                    cont = detail.get(field, "")
                    if isinstance(cont, list):
                        cont = ";".join(cont).replace(";;", ";")
                    if cont != "":
                        if "</eps> The Purpose" in cont:
                            print(1)
                            parts = cont.split("</eps> The Purpose")
                            parts[0] = parts[0].split()[:chunk_size]
                            parts[1] = f"The Purpose{parts[1].strip()[:chunk_size]}"
                            print(parts)
                            temp.append(
                                f" <{field}> : {' '.join([parts[0], parts[1]])}...")
                        else:
                            temp.append(f" <{field}> : {' '.join(cont.split()[:chunk_size])[:2 * chunk_size]}...")
                tgt_desc.append(" <sep> ".join(temp))
            except Exception as e:
                traceback.print_exc()

        document.append(
            {
                f"{map_rep[src_dialect]} snippet": f"`{key}`: {' '.join(desc['Desc'].split()[:chunk_size])[:2 * chunk_size]}...",
                f"{map_rep[tgt_dialect]} snippet": [f"`{tk}`: {tdesc}" for tk, tdesc in
                                                    zip(tgt_key, tgt_desc)]})

    document = json.dumps(document, indent=4)

    sys_prompt = SYSTEM_PROMPT_RET.format(src_dialect=map_rep[src_dialect],
                                          tgt_dialect=map_rep[tgt_dialect]).strip("\n")

    user_prompt = USER_PROMPT_RET.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                         sql=input_sql, hint=hint, example=example, document=document).strip("\n")

    answer_raw = translator.trans_func([], sys_prompt, user_prompt)
    pattern = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?)'
    res = parse_llm_answer(translator.model_id, answer_raw, pattern)

    answer_raw["Action"] = "translate"
    answer_raw["Time"] = str(datetime.now())
    answer_raw["SYSTEM_PROMPT"] = sys_prompt
    answer_raw["USER_PROMPT"] = user_prompt
    return res, answer_raw


def local_rewrite(translator, retriever, vector_db, src_sql: str,
                  src_dialect, tgt_dialect, db_name, top_k,
                  sqlglot_try_time=0, max_retry_time=2):
    """
    List of
    {
        "Node": node,
        "Tree": function['Tree'],
        "Description": function['Description'],
        "Keyword": function['Keyword'],
        "SubPieces": sub-pieces,
        "FatherPieces": father-pieces
    }
    When want to use the representation of the node(the sql slice),
    just use TreeNode.gen_node_rep(node, src_dialect)
    """
    src_sql = src_sql.strip(';')
    try:
        root_node, line, col, msg = parse_tree(src_sql, src_dialect)
        if root_node is None:
            raise ValueError(f"Parse error when executing ANTLR parser of {src_dialect}.\n"
                             f"The sql is {src_sql}")
        all_pieces, root_node = get_all_piece(root_node, src_dialect)
        flag = True
        for piece in all_pieces:
            if root_node == piece['Node']:
                flag = False
                break
        if flag:
            root_piece = {
                "Node": root_node,
                "Tree": root_node,
                "Description": {"Type": "Keyword",
                                "Desc": "The whole SQL snippet above."},
                "Keyword": '',
                "SubPieces": [piece for piece in all_pieces],
                "FatherPiece": None,
                "Count": 0,
                'TrackPieces': []
            }
            for piece in all_pieces:
                if piece['FatherPiece'] is None:
                    piece['FatherPiece'] = root_piece
            all_pieces.append(root_piece)
        if slice_only:
            if mask_on:
                slices = []
                for piece in all_pieces:
                    new_sql, rep_map = mask_type_node(piece['Node'], src_dialect, tgt_dialect)
                    slices.append({
                        "ori_sql": str(piece['Node']),
                        "mask_sql": new_sql,
                        "rep_map": rep_map
                    })
                all_pieces = {
                    "src_sql": src_sql,
                    "src_dialect": src_dialect,
                    'slices': slices
                }
                return all_pieces, [], [], []
            rewrite_slices = {
                "src_sql": src_sql,
                "src_dialect": src_dialect,
                "slices": [
                    {
                        "Keyword": piece['Keyword'],
                        "str": str(piece['Node']),
                        "Desc": piece['Description']
                    } for piece in all_pieces
                ]
            }
            return rewrite_slices, [], [], []
        normalize(root_node, src_dialect, tgt_dialect)
        src_sql = str(root_node)
    except ValueError as ve:
        traceback.print_exc()
        print(f"Antlr parse error: {src_sql}, translate cancelled, "
              f"dialect: {src_dialect}\n{ve}", file=sys.stderr)
        # return "", []
        return str(ve), [], [], []

    if len(all_pieces) == 0:
        return src_sql, ['Warning: No piece find'], [], []

    used_pieces = []
    lift_histories = []

    now_sql = src_sql

    model_ans_list, sql_ans_list = list(), list()
    if locate_by_err:
        last_time_piece = None
        ori_piece = None

        err_msg_list, err_info_list = list(), list()
        piece, assist_info = locate_node_piece(now_sql, src_dialect,
                                               tgt_dialect, all_pieces, root_node, db_name)
        if piece is None:
            history, sys_prompt, user_prompt = list(), None, None
            if len(model_ans_list) > 0:
                no = -1
                for i in range(len(model_ans_list) - 1, 0, -1):
                    if "SYSTEM_PROMPT" in model_ans_list[i].keys():
                        no = i
                        break
                model_message = copy.deepcopy(model_ans_list[no])

                model_message.pop("Action")
                sys_prompt = None
                if "SYSTEM_PROMPT" in model_message.keys():
                    sys_prompt = model_message.pop("SYSTEM_PROMPT")
                    user_prompt = model_message.pop("USER_PROMPT")

                history.append({"role": "user", "content": user_prompt})
                history.append(model_message)

                user_prompt = USER_PROMPT_REFLECT.format(src_dialect=map_rep[src_dialect],
                                                         tgt_dialect=map_rep[tgt_dialect],
                                                         src_sql=src_sql, tgt_sql=now_sql,
                                                         snippet=f"`{str(last_time_piece['Node'])}`").strip("\n")

            piece, assist_info, judge_raw = model_judge(translator, map_rep[src_dialect], map_rep[tgt_dialect],
                                                        root_node, all_pieces, src_sql, now_sql,
                                                        last_time_piece, ori_piece, history, sys_prompt, user_prompt)
            model_ans_list.append(judge_raw)

        if piece is not None:
            err_msg_list.append(assist_info)
            if tgt_dialect == "oracle":
                try:
                    assist_info_pre = f"Some error occurs near the snippet:"
                    if 'ORA-00933: SQL command not properly ended' not in assist_info \
                            and 'ERROR' in assist_info:
                        err_pos = assist_info.index("ERROR")
                        assist_info_pre += assist_info[err_pos:]
                    err_info_list.append({"Error": assist_info_pre.replace("xxxx_BIRD.", "").replace("BIRD.",
                                                                                                    "").replace(
                        "pg_catalog.date_part(", "EXTRACT(").replace("Error while executing PostgreSQL query:", "").
                        replace(
                        "You have an error in your SQL syntax; check the manual that corresponds "
                        "to your MySQL server version for the right syntax to use near",
                        "Some error occurs near"),
                        "SQL Snippet": str(piece["Node"])})
                except Exception as e:
                    traceback.print_exc()
                    assist_info_pre = f"Some error occurs near the snippet:"
                    err_info_list.append({"Error": assist_info_pre.replace("xxxx_BIRD.", "").replace("BIRD.",
                                                                                                    "").replace(
                        "pg_catalog.date_part(", "EXTRACT(").replace("Error while executing PostgreSQL query:", "").
                        replace(
                        "You have an error in your SQL syntax; check the manual that corresponds "
                        "to your MySQL server version for the right syntax to use near",
                        "Some error occurs near"),
                        "SQL Snippet": str(piece["Node"])})
            else:
                err_info_list.append({"Error": assist_info.replace("xxxx_BIRD.", "").replace("BIRD.", "").replace(
                    "pg_catalog.date_part(", "EXTRACT(").replace("Error while executing PostgreSQL query:", "").
                                     replace("You have an error in your SQL syntax; check the manual that corresponds "
                                             "to your MySQL server version for the right syntax to use near",
                                             "Some error occurs near"),
                                      "SQL Snippet": str(piece["Node"])})

        while piece is not None:
            back_flag = False
            if assist_info is not None and assist_info.endswith("translate error"):
                match = re.search(r'Function\s+(\w+)\s+translate\s+error', assist_info)
                if match:
                    back_flag = True
                    func_name = match.group(1)
                    assert func_name.lower() == get_func_name(ori_piece['Keyword'])
                else:
                    assert False

            elif last_time_piece is not None and last_time_piece['Node'] == piece['Node']:
                back_flag = True

            if back_flag:
                replace_piece(last_time_piece, ori_piece)
                all_pieces.remove(last_time_piece)
                all_pieces.append(ori_piece)
                for sub_piece in ori_piece['SubPieces']:
                    all_pieces.append(sub_piece)
                piece = ori_piece
                piece['Count'] = piece['Count'] + 1
                if last_time_piece['Node'] == root_node:
                    root_node = ori_piece['Node']
                else:
                    piece["Node"].father.replace_child(last_time_piece['Node'], ori_piece['Node'])
            else:
                ori_piece = piece
                err_msg_list, err_info_list = list(), list()

            if piece is None:
                break

            node, tree_node = piece['Node'], piece['Tree']
            if piece['Count'] > max_retry_time:
                # use new strategy find upper node
                node = piece['Node']
                if node == root_node:
                    return 'Unsupport', model_ans_list, used_pieces, lift_histories
                pri_node_expr = str(node)
                terminate_flag = False
                while not terminate_flag:
                    assert node.father is not None
                    terminate_flag, node, tree_node, piece = lift_node(node, all_pieces, tree_node, piece)
                lift_node_expr = str(node)
                lift_histories.append({
                    "pre_expr": pri_node_expr,
                    "lift_expr": lift_node_expr
                })
                piece['Count'] = 0

            piece['Node'], piece['Tree'] = node, tree_node

            used_pieces.append({
                "piece": str(piece['Node']),
                "Keyword": piece['Keyword']
            })

            if piece["Count"] < sqlglot_try_time:
                src, tgt = src_dialect, tgt_dialect
                if src_dialect == "pg":
                    src = "postgres"
                if tgt_dialect == "pg":
                    tgt = "postgres"

                try:
                    ans_slice = sqlglot.transpile(str(piece['Node']), read=src, write=tgt)[0]
                    model_ans = {"role": "sqlglot", "content": ans_slice, "Action": "translate", "Time": str(datetime.now())}
                except Exception as e:
                    print(str(piece['Node']))
                    traceback.print_exc()
                    ans_slice, model_ans = rewrite_piece(ori_piece, piece, translator, retriever, vector_db,
                                                         src_dialect, tgt_dialect, top_k, sqlglot_try_time, err_info_list)
            else:
                ans_slice, model_ans = rewrite_piece(ori_piece, piece, translator, retriever, vector_db,
                                                     src_dialect, tgt_dialect, top_k, sqlglot_try_time, err_info_list)

            if 'select' in ans_slice.lower() and 'select' not in str(piece['Node']).lower():
                ans_slice = '(' + ans_slice + ')'

            last_time_node = TreeNode(ans_slice, src_dialect, is_terminal=True, father=None,
                                      father_child_index=None, children=None, model_get=True)
            if piece['Node'] == root_node:
                root_node = last_time_node
            else:
                piece["Node"].father.replace_child(piece["Node"], last_time_node)
            all_pieces.remove(piece)
            new_piece = {
                "Node": last_time_node,
                "Tree": None,
                "Description": None,  # set to none, for the exact meaning of the piece is not known
                "Keyword": piece['Keyword'],
                "SubPieces": [],
                "FatherPiece": piece['FatherPiece'],
                "Count": 0,
                "TrackPieces": []
            }
            all_pieces.append(new_piece)
            for sub_piece in piece['SubPieces']:
                all_pieces.remove(sub_piece)
            replace_piece(piece, new_piece)
            last_time_piece, ori_piece = new_piece, piece
            now_sql = str(root_node)

            model_ans["Translated SQL"] = now_sql
            model_ans_list.append(model_ans)

            piece, assist_info = locate_node_piece(now_sql, src_dialect,
                                                   tgt_dialect, all_pieces, root_node, db_name)
            if piece is None:
                if now_sql in sql_ans_list:
                    return now_sql, model_ans_list, used_pieces, lift_histories

                history, sys_prompt, user_prompt = list(), None, None
                if len(model_ans_list) > 0:
                    no = -1
                    for i in range(len(model_ans_list) - 1, 0, -1):
                        if "SYSTEM_PROMPT" in model_ans_list[i].keys():
                            no = i
                            break
                    model_message = copy.deepcopy(model_ans_list[no])

                    model_message.pop("Action")
                    sys_prompt = None
                    if "SYSTEM_PROMPT" in model_message.keys():
                        sys_prompt = model_message.pop("SYSTEM_PROMPT")
                        user_prompt = model_message.pop("USER_PROMPT")

                    history.append({"role": "user", "content": user_prompt})
                    history.append(model_message)

                    user_prompt = USER_PROMPT_REFLECT.format(src_dialect=map_rep[src_dialect],
                                                             tgt_dialect=map_rep[tgt_dialect],
                                                             src_sql=src_sql, tgt_sql=now_sql,
                                                             snippet=f"`{str(last_time_piece['Node'])}`").strip("\n")

                piece, assist_info, judge_raw = model_judge(translator, map_rep[src_dialect], map_rep[tgt_dialect],
                                                            root_node, all_pieces, src_sql, now_sql,
                                                            last_time_piece, ori_piece, history, sys_prompt,
                                                            user_prompt)
                model_ans_list.append(judge_raw)

            if piece is not None:
                if assist_info not in err_msg_list:
                    err_msg_list.append(assist_info)
                    if tgt_dialect == "oracle":
                        try:
                            assist_info_pre = f"Some error occurs near the snippet:"
                            if 'ORA-00933: SQL command not properly ended' not in assist_info \
                                    and 'ERROR' in assist_info:
                                err_pos = assist_info.index("ERROR")
                                assist_info_pre += assist_info[err_pos:]
                            err_info_list.append(
                                {"Error": assist_info_pre.replace("xxxx_BIRD.", "").replace("BIRD.", "").replace(
                                    "pg_catalog.date_part(", "EXTRACT(").replace(
                                    "Error while executing PostgreSQL query:", "").
                                    replace("You have an error in your SQL syntax; check the manual that corresponds "
                                            "to your MySQL server version for the right syntax to use near",
                                            "Some error occurs near"),
                                 "SQL Snippet": str(piece["Node"])})
                        except Exception as e:
                            traceback.print_exc()
                            assist_info_pre = f"Some error occurs near the snippet:"
                            err_info_list.append(
                                {"Error": assist_info_pre.replace("xxxx_BIRD.", "").replace("BIRD.", "").replace(
                                    "pg_catalog.date_part(", "EXTRACT(").replace(
                                    "Error while executing PostgreSQL query:", "").
                                    replace("You have an error in your SQL syntax; check the manual that corresponds "
                                            "to your MySQL server version for the right syntax to use near",
                                            "Some error occurs near"),
                                 "SQL Snippet": str(piece["Node"])})
                    else:
                        err_info_list.append({"Error": assist_info.replace("xxxx_BIRD.", "").replace("BIRD.",
                                                                                                    "").replace(
                            "pg_catalog.date_part(", "EXTRACT(").replace("Error while executing PostgreSQL query:", "").
                            replace(
                            "You have an error in your SQL syntax; check the manual that corresponds "
                            "to your MySQL server version for the right syntax to use near",
                            "Some error occurs near"),
                            "SQL Snippet": str(piece["Node"])})

            if now_sql not in sql_ans_list:
                sql_ans_list.append(now_sql)

        return now_sql, model_ans_list, used_pieces, lift_histories
    else:
        raise ValueError("Not Support without locate_by_err, please revise the Config.ini")


def rewrite_piece(ori_piece, piece, translator, retriever, vector_db,
                  src_dialect, tgt_dialect, top_k,
                  sqlglot_try_time=0, err_info_list=list()) -> [str, str]:
    if isinstance(piece, Dict):
        input_sql = str(piece['Node'])
    elif isinstance(piece, str):
        input_sql = piece
    
    example = str()
    for item in err_info_list:
        item['Error'] = item['Error'].replace("You have an error in your SQL syntax; "
                                              "check the manual that corresponds to your MySQL server "
                                              "version for the right syntax to use", "Syntax error").replace('\n', '')
        item['SQL Snippet'] = item['SQL Snippet'].strip('\n')
        example += f"-- ERROR: {item['Error']}\n{item['SQL Snippet']}\n\n"
    example = example.strip("\n")

    hint = str()
    if retrieval_on:
        if piece['Count'] == sqlglot_try_time:
            sys_prompt = SYSTEM_PROMPT_SEG.format(src_dialect=map_rep[src_dialect],
                                                  tgt_dialect=map_rep[tgt_dialect]).strip("\n")

            if len(example) != 0:
                example = EXAMPLE_PROMPT.format(example)

            if isinstance(ori_piece, Dict):
                src_sql = str(ori_piece["Node"])
            elif isinstance(ori_piece, str):
                src_sql = ori_piece

            user_prompt = USER_PROMPT_SEG.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                                 sql=input_sql, hint=hint, example=example).strip("\n")

        else:
            src_key = [str(piece['Keyword'])]
            src_desc = [piece['Description']]
            for sub_piece in piece['SubPieces']:
                if sub_piece['Keyword'] is not None and sub_piece['Keyword'] not in src_key:
                    src_key.append(sub_piece['Keyword'])
                    src_desc.append(sub_piece['Description'])

            document = list()
            for key, desc in zip(src_key, src_desc):
                if desc is None:
                    continue

                if desc["Desc"] == "The whole SQL snippet above.":
                    continue

                results = list()
                model_id = retriever[1].model_id
                if desc['Type'] == 'Keyword':
                    continue

                elif desc['Type'] == 'Type':
                    if model_id == "BM25":
                        results.extend(
                            retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:top_k])

                    else:
                        if model_id == "cross-lingual":
                            results.extend(
                                [ite[0] for ite in retriever[1].retrieve(str(key) + '--separator--' + str(desc),
                                                                         vector_db[1][
                                                                             map_trans[desc["Type"]]].db,
                                                                         top_k=2)])
                        else:
                            results.extend([ite[0] for ite in
                                            retriever[1].retrieve(str(desc),
                                                                  vector_db[1][map_trans[desc["Type"]]].db,
                                                                  top_k=2)])
                    results.extend(retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:1])

                elif desc['Type'] == 'Function':
                    if model_id == "BM25":
                        results.extend(
                            retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:top_k])

                    else:
                        if model_id == "cross-lingual":
                            results.extend(
                                [ite[0] for ite in retriever[1].retrieve(str(key) + '--separator--' + str(desc),
                                                                         vector_db[1][
                                                                             map_trans[desc["Type"]]].db,
                                                                         top_k=2)])
                        else:
                            results.extend([ite[0] for ite in
                                            retriever[1].retrieve(str(desc),
                                                                  vector_db[1][map_trans[desc["Type"]]].db,
                                                                  top_k=2)])
                    results.extend([ite[0] for ite in
                                    retriever[-1].retrieve(str(desc), vector_db[-1][map_trans[desc["Type"]]].db,
                                                           top_k=2)])
                    results.extend(retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:1])

                results_key = set()
                results_pre = list()
                for ite in results:
                    if ite.metadata["KEYWORD"] not in results_key:
                        results_key.add(ite.metadata["KEYWORD"])
                        results_pre.append(ite)

                tgt_key = [re.sub(r'(<sep>)(\1){2,}', r'\1', ite.metadata["KEYWORD"]) for ite in results_pre]

                tgt_desc = list()
                for ite in results_pre:
                    temp = list()
                    try:
                        detail = eval(ite.metadata["ALL"])
                        for field in ['Argument Type', 'Argument Type(s)',
                                      'Aggregated Argument Type(s)',
                                      'Direct Argument Type(s)', 'Return Type',
                                      "Description", 'Example', 'Result',
                                      'Example Query', 'Example Result', "Demo"]:
                            cont = detail.get(field, "")
                            if isinstance(cont, list):
                                cont = ";".join(cont).replace(";;", ";")
                            if cont != "":
                                if "</eps> The Purpose" in cont:
                                    print(1)
                                    parts = cont.split("</eps> The Purpose")
                                    parts[0] = parts[0].split()[:chunk_size]
                                    parts[1] = f"The Purpose{parts[1].strip()[:chunk_size]}"
                                    print(parts)
                                    temp.append(
                                        f" <{field}> : {' '.join([parts[0], parts[1]])}...")
                                else:
                                    temp.append(
                                        f" <{field}> : {' '.join(cont.split()[:chunk_size])[:2 * chunk_size]}...")
                        tgt_desc.append(" <sep> ".join(temp))
                    except Exception as e:
                        traceback.print_exc()

                document.append(
                    {
                        f"{map_rep[src_dialect]} snippet": f"`{key}`: {' '.join(desc['Desc'].split()[:chunk_size])[:2 * chunk_size]}...",
                        f"{map_rep[tgt_dialect]} snippet": [f"`{tk}`: {tdesc}" for tk, tdesc in
                                                            zip(tgt_key, tgt_desc)]})

            document = json.dumps(document, indent=4)

            sys_prompt = SYSTEM_PROMPT_RET.format(src_dialect=map_rep[src_dialect],
                                                  tgt_dialect=map_rep[tgt_dialect]).strip("\n")

            if len(example) != 0:
                example = EXAMPLE_PROMPT.format(example)

            if isinstance(ori_piece, Dict):
                src_sql = str(ori_piece["Node"])
            elif isinstance(ori_piece, str):
                src_sql = ori_piece

            user_prompt = USER_PROMPT_RET.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                                 sql=input_sql, hint=hint, example=example, document=document).strip(
                "\n")

    elif mask_on:
        mask_info = str()
        masked_sql, replace_map = mask_type_node(piece['Node'], src_dialect, tgt_dialect)
        new_dict = {k: str(v) for k, v in replace_map.items() if k.strip() != str(v)}
        for key in new_dict:
            mask_info = mask_info + f"- `{key}` denotes: `{new_dict[key]}`\n"
        sys_prompt = SYSTEM_PROMPT_MASK.format(src_dialect=map_rep[src_dialect],
                                               tgt_dialect=map_rep[tgt_dialect]).strip("\n")
        user_prompt = USER_PROMPT_MASK.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                              sql=masked_sql, mask_info=mask_info).strip("\n")

    elif seg_on:
        sys_prompt = SYSTEM_PROMPT_SEG.format(src_dialect=map_rep[src_dialect],
                                              tgt_dialect=map_rep[tgt_dialect]).strip("\n")

        if len(example) != 0:
            example = EXAMPLE_PROMPT.format(example)

        if isinstance(ori_piece, Dict):
            src_sql = str(ori_piece["Node"])
        elif isinstance(ori_piece, str):
            src_sql = ori_piece

        user_prompt = USER_PROMPT_SEG.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                             sql=input_sql, example=example).strip("\n")

    else:
        sys_prompt = SYSTEM_PROMPT_NA.format(src_dialect=map_rep[src_dialect],
                                             tgt_dialect=map_rep[tgt_dialect]).strip("\n")

        if len(example) != 0:
            example = EXAMPLE_PROMPT.format(example)

        user_prompt = USER_PROMPT_NA.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                            sql=input_sql, example=example).strip("\n")

    answer_raw = translator.trans_func([], sys_prompt, user_prompt)
    pattern = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?)'
    res = parse_llm_answer(translator.model_id, answer_raw, pattern)

    answer_raw["Action"] = "translate"
    answer_raw["Time"] = str(datetime.now())
    answer_raw["SYSTEM_PROMPT"] = sys_prompt
    answer_raw["USER_PROMPT"] = user_prompt
    return res, answer_raw


def model_judge(translator, src_dialect, tgt_dialect, root_node,
                all_pieces, src_sql, now_sql, ans_slice, ori_piece,
                history=list(), sys_prompt=None, user_prompt=None):
    if ans_slice is None:
        snippet = "all snippets"
    else:
        snippet = f"`{str(ans_slice['Node'])}`"

    if sys_prompt is None:
        sys_prompt = SYSTEM_PROMPT_JUDGE.format(src_dialect=src_dialect, tgt_dialect=tgt_dialect).strip("\n")
    if user_prompt is None:
        user_prompt = USER_PROMPT_JUDGE.format(src_dialect=src_dialect, tgt_dialect=tgt_dialect,
                                               src_sql=src_sql, tgt_sql=now_sql, snippet=snippet).strip("\n")
    answer_raw = translator.trans_func(history, sys_prompt, user_prompt)
    pattern = r'"SQL Snippet":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
    res = parse_llm_answer_v2(translator.model_id, answer_raw, pattern)
    snippet = res["Answer"]

    answer_raw["Action"] = "judge"
    answer_raw["Time"] = str(datetime.now())
    answer_raw["SYSTEM_PROMPT"] = sys_prompt
    answer_raw["USER_PROMPT"] = user_prompt

    piece, assist_info = None, None
    if "NONE" in snippet or "almost equivalent" in str(answer_raw) \
            or (isinstance(res['Confidence'], float) and res['Confidence'] < 0.8):
        return piece, assist_info, answer_raw

    assist_info = f"The following snippet needs to be further examined: \n`{snippet}`\n" \
                  f"And some reflections about this translated snippet are: <reflection> {res['Reasoning']} </reflection>. " \
                  f"Note that these reflections might be incorrect, " \
                  f"so please carefully identify what is correct for the successful translation."

    column = now_sql.find(snippet)
    if column != -1:
        node, _ = TreeNode.locate_node(root_node, column, now_sql)
        piece = find_piece(all_pieces, node)

    return piece, assist_info, answer_raw



def add_process(out_type, history_id, content, step_name, sql, role, is_success, error):
    
    if out_type == "file":
        # 添加到文件

        pass
    elif out_type == "db":
        # 添加到数据库 
        # 添加改写结果记录
        RewriteService.add_rewrite_process(
            history_id=history_id,
            content="SQL改写完成",
            step_name="改写结果",
            sql=rewritten_sql,
            role='assistant',
            is_success=True
        )

        pass
