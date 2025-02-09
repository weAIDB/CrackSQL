import re
import sys

import torch
import json
import copy
import traceback

import sqlglot
from typing import Dict
from datetime import datetime

from langchain_huggingface import HuggingFaceEmbeddings

from llama_index.core.node_parser import SimpleFileNodeParser
from llama_index.retrievers.bm25 import BM25Retriever

from CrackSQL.backend.utils.constants import KNOWLEDGE_FIELD_LIST, TRANSLATION_FORMAT, map_rep, model_dict, map_trans

from preprocessor.antlr_parser.parse_tree import parse_tree
from preprocessor.query_simplifier.Tree import TreeNode, lift_node
from preprocessor.query_simplifier.rewrite import get_all_piece
from preprocessor.query_simplifier.locate import locate_node_piece, replace_piece, get_func_name, find_piece
from preprocessor.query_simplifier.normalize import normalize

from retriever.dump_data import pre_db_docs
from retriever.retrieval_model import RetrievalModel, CodeDescEmbedding
from retriever.vector_db import VectorDB
from translator.translate_prompt import SYSTEM_PROMPT_NA, USER_PROMPT_NA, \
    SYSTEM_PROMPT_SEG, USER_PROMPT_SEG, SYSTEM_PROMPT_RET, USER_PROMPT_RET, USER_PROMPT_DIR, EXAMPLE_PROMPT
from translator.judge_prompt import SYSTEM_PROMPT_JUDGE, USER_PROMPT_JUDGE, USER_PROMPT_REFLECT
from translator.llm_translator import LLMTranslator
from utils.tools import load_config, parse_llm_answer, parse_llm_answer_v2, process_err_msg


# TODO(by zw): syn with config loader

chunk_size = 100
ret_bak_id = "bge-large-en-v1.5"
build_in_function_map = {}

config = load_config()
retrieval_on = config['retrieval_on']

gpt_api_base = config['gpt_api_base']
gpt_api_key = config['gpt_api_key']
llama_3_1_api_base = config['llama3.1_api_base']
llama_3_2_api_base = config['llama3.2_api_base']

codellama_api_base = config['codellama_api_base']
codeqwen2_5_api_base = config['codeqwen2.5_api_base']
qwen2_5_api_base = config['qwen2.5_api_base']

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def init_model(model_id, ret_id, db_id, db_path, top_k, tgt_dialect=None):
    translator, retriever, vector_db = None, None, None

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


def local_rewrite(translator, retriever, vector_db, src_sql,
                  src_dialect, tgt_dialect, db_name, top_k, max_retry_time=2):
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
    model_ans_list, sql_ans_list = list(), list()
    used_pieces, lift_histories = list(), list()
    try:
        root_node, all_pieces = get_sql_pieces(src_sql, src_dialect)
        normalize(root_node, src_dialect, tgt_dialect)
        src_sql = str(root_node)
    except ValueError as ve:
        traceback.print_exc()
        print(f"Antlr parse error: {src_sql}, translate cancelled, "
              f"dialect: {src_dialect}\n{ve}", file=sys.stderr)
        return str(ve), model_ans_list, used_pieces, lift_histories

    if len(all_pieces) == 0:
        return src_sql, ['Warning: No piece find'], used_pieces, lift_histories

    now_sql = src_sql
    ori_piece, last_time_piece = None, None
    err_msg_list, err_info_list = list(), list()
    piece, assist_info = locate_node_piece(now_sql, src_dialect,
                                           tgt_dialect, all_pieces, root_node, db_name)
    if piece is None:
        history, sys_prompt, user_prompt = list(), None, None
        piece, assist_info, judge_raw = model_judge(translator, map_rep[src_dialect], map_rep[tgt_dialect],
                                                    root_node, all_pieces, src_sql, now_sql,
                                                    last_time_piece, history, sys_prompt, user_prompt)
        model_ans_list.append(judge_raw)

    while piece is not None:
        if assist_info not in err_msg_list:
            err_msg_list.append(assist_info)
            err_info_list = update_error_info_list(err_info_list, assist_info, piece, tgt_dialect)

        back_flag = get_restore_piece_flag(assist_info, piece,
                                           last_time_piece, ori_piece)
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

        node, tree_node = piece['Node'], piece['Tree']
        # local-to-global lift operation
        if piece['Count'] > max_retry_time:
            node = piece['Node']
            if node == root_node:
                return 'Cannot translate!', model_ans_list, used_pieces, lift_histories
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

        if piece["Count"] == 0:
            try:
                ans_slice = sqlglot.transpile(str(piece['Node']), read=src_dialect, write=tgt_dialect)[0]
                model_ans = {"role": "sqlglot", "content": ans_slice, "Action": "translate",
                             "Time": str(datetime.now())}
            except Exception as e:
                traceback.print_exc()
                ans_slice, model_ans = rewrite_piece(piece, translator, retriever, vector_db,
                                                     src_dialect, tgt_dialect, top_k, [], err_info_list)
        else:
            ans_slice, model_ans = rewrite_piece(piece, translator, retriever, vector_db,
                                                 src_dialect, tgt_dialect, top_k, [], err_info_list)

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

            piece, assist_info, judge_raw = handle_syntactic_correct_piece(src_dialect, tgt_dialect, src_sql, now_sql,
                                                                           translator, root_node, all_pieces,
                                                                           last_time_piece, model_ans_list)

            model_ans_list.append(judge_raw)

        if now_sql not in sql_ans_list:
            sql_ans_list.append(now_sql)

    return now_sql, model_ans_list, used_pieces, lift_histories


def rewrite_piece(piece, translator, retriever, vector_db, src_dialect, tgt_dialect,
                  top_k, history=list(), err_info_list=list()) -> [str, str]:
    if isinstance(piece, Dict):
        input_sql = str(piece['Node'])
    elif isinstance(piece, str):
        input_sql = piece

    example = str()
    for item in err_info_list:
        item['SQL Snippet'] = item['SQL Snippet'].strip('\n')
        example += f"-- ERROR: {item['Error']}\n{item['SQL Snippet']}\n\n"

    example = example.strip("\n")
    if len(example) != 0:
        example = EXAMPLE_PROMPT.format(example)

    hint = str()
    if retrieval_on:
        if piece['Count'] == 0:
            sys_prompt = SYSTEM_PROMPT_SEG.format(src_dialect=map_rep[src_dialect],
                                                  tgt_dialect=map_rep[tgt_dialect]).strip("\n")
            user_prompt = USER_PROMPT_SEG.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                                 sql=input_sql, hint=hint, example=example).strip("\n")
        else:
            document = get_document_description(piece, retriever, vector_db, top_k, src_dialect, tgt_dialect)
            sys_prompt = SYSTEM_PROMPT_RET.format(src_dialect=map_rep[src_dialect],
                                                  tgt_dialect=map_rep[tgt_dialect]).strip("\n")
            user_prompt = USER_PROMPT_RET.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                                 sql=input_sql, hint=hint, example=example,
                                                 document=document).strip("\n")
    else:
        sys_prompt = SYSTEM_PROMPT_NA.format(src_dialect=map_rep[src_dialect],
                                             tgt_dialect=map_rep[tgt_dialect]).strip("\n")
        user_prompt = USER_PROMPT_NA.format(src_dialect=map_rep[src_dialect], tgt_dialect=map_rep[tgt_dialect],
                                            sql=input_sql, example=example).strip("\n")

    answer_raw = translator.trans_func(history, sys_prompt, user_prompt)

    res = parse_llm_answer(translator.model_id, answer_raw, TRANSLATION_FORMAT)

    answer_raw["Action"] = "translate"
    answer_raw["Time"] = str(datetime.now())
    answer_raw["SYSTEM_PROMPT"] = sys_prompt
    answer_raw["USER_PROMPT"] = user_prompt
    return res, answer_raw


def get_sql_pieces(src_sql, src_dialect):
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

    return root_node, all_pieces


def get_restore_piece_flag(assist_info, piece, last_time_piece, ori_piece):
    back_flag = False
    if assist_info is not None and assist_info.endswith("translate error"):
        match = re.search(r'Function\s+(\w+)\s+translate\s+error', assist_info)
        if match:
            back_flag = True
            func_name = match.group(1)
            assert func_name.lower() == get_func_name(ori_piece['Keyword'])
        else:
            raise Exception("Error occurs while parsing Function messages")

    elif last_time_piece is not None and last_time_piece['Node'] == piece['Node']:
        back_flag = True

    return back_flag


def get_document_description(piece, retriever, vector_db, top_k, src_dialect, tgt_dialect):
    src_key = [str(piece['Keyword'])]
    src_desc = [piece['Description']]
    for sub_piece in piece['SubPieces']:
        if sub_piece['Keyword'] is not None and sub_piece['Keyword'] not in src_key:
            src_key.append(sub_piece['Keyword'])
            src_desc.append(sub_piece['Description'])

    document = list()
    for key, desc in zip(src_key, src_desc):
        if desc is None or desc["Desc"] == "The whole SQL snippet above.":
            continue

        results = list()
        model_id = retriever[1].model_id
        if model_id == "cross-lingual":
            results.extend([ite[0] for ite in
                            retriever[1].retrieve(str(key) + '--separator--' + str(desc),
                                                  vector_db[1][map_trans[desc["Type"]]].db,
                                                  top_k=top_k)])
        else:
            results.extend([ite[0] for ite in
                            retriever[1].retrieve(str(desc),
                                                  vector_db[1][map_trans[desc["Type"]]].db,
                                                  top_k=top_k)])
        results.extend(retriever[0].retrieve(str(desc), vector_db[0][map_trans[desc["Type"]]].db)[:top_k])

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
                for field in KNOWLEDGE_FIELD_LIST:
                    cont = detail.get(field, "")
                    if isinstance(cont, list):
                        cont = ";".join(cont).replace(";;", ";")
                    if cont != "":
                        if "</eps> The Purpose" in cont:
                            parts = cont.split("</eps> The Purpose")
                            parts[0] = parts[0].split()[:chunk_size]
                            parts[1] = f"The Purpose{parts[1].strip()[:chunk_size]}"
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
                f"{map_rep[tgt_dialect]} snippet": [f"`{tk}`: {tdesc}" for tk, tdesc in zip(tgt_key, tgt_desc)]
            }
        )

    document = json.dumps(document, indent=4)

    return document


def update_error_info_list(err_info_list, assist_info, piece, tgt_dialect):
    if tgt_dialect == "oracle":
        assist_info_pre = f"Some error occurs near the snippet:"
        try:
            if 'ORA-00933: SQL command not properly ended' not in assist_info \
                    and 'ERROR' in assist_info:
                err_pos = assist_info.index("ERROR")
                assist_info_pre += assist_info[err_pos:]
            assist_info_pre = process_err_msg(assist_info_pre)
            err_info_list.append({"Error": assist_info_pre,
                                  "SQL Snippet": str(piece["Node"])})
        except Exception as e:
            traceback.print_exc()
            assist_info_pre = process_err_msg(assist_info_pre)
            err_info_list.append(
                {"Error": assist_info_pre,
                 "SQL Snippet": str(piece["Node"])})
    else:
        assist_info = process_err_msg(assist_info)
        err_info_list.append({"Error": assist_info,
                              "SQL Snippet": str(piece["Node"])})

    return err_info_list


def handle_syntactic_correct_piece(src_dialect, tgt_dialect, src_sql, now_sql, translator,
                                   root_node, all_pieces, last_time_piece, model_ans_list):
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
                                                last_time_piece, history, sys_prompt, user_prompt)

    return piece, assist_info, judge_raw


def model_judge(translator, src_dialect, tgt_dialect, root_node,
                all_pieces, src_sql, now_sql, ans_slice,
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


def direct_rewrite(translator, src_sql, src_dialect, tgt_dialect):
    history, model_ans_list = list(), list()

    sys_prompt = None
    user_prompt = USER_PROMPT_DIR.format(src_dialect=map_rep[src_dialect],
                                         tgt_dialect=map_rep[tgt_dialect], sql=src_sql).strip("\n")

    answer_raw = translator.trans_func(history, sys_prompt, user_prompt)
    pattern = r'"Answer":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
    now_sql = parse_llm_answer(translator.model_id, answer_raw, pattern)

    answer_raw["Action"] = "translate"
    answer_raw["Time"] = str(datetime.now())
    answer_raw["SYSTEM_PROMPT"] = sys_prompt
    answer_raw["USER_PROMPT"] = user_prompt

    model_ans_list.append(answer_raw)

    return now_sql, model_ans_list


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
