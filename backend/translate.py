import re
import sys

import torch
import json
import copy
import traceback
import sqlglot
from typing import Dict
from datetime import datetime
from models import RewriteStatus
from utils.constants import KNOWLEDGE_FIELD_LIST, map_rep
from preprocessor.antlr_parser.parse_tree import parse_tree
from preprocessor.query_simplifier.Tree import TreeNode, lift_node
from preprocessor.query_simplifier.rewrite import get_all_piece
from preprocessor.query_simplifier.locate import locate_node_piece, replace_piece, get_func_name, find_piece
from preprocessor.query_simplifier.normalize import normalize
from translator.translate_prompt import SYSTEM_PROMPT_NA, USER_PROMPT_NA, \
    SYSTEM_PROMPT_SEG, USER_PROMPT_SEG, SYSTEM_PROMPT_RET, USER_PROMPT_RET, USER_PROMPT_DIR, EXAMPLE_PROMPT
from translator.judge_prompt import SYSTEM_PROMPT_JUDGE, USER_PROMPT_JUDGE, USER_PROMPT_REFLECT
from translator.llm_translator import LLMTranslator
from llm_model.embeddings import embedding_manager
from vector_store.chroma_store import ChromaStore
from utils.tools import parse_llm_answer_v2, process_err_msg

chunk_size = 100


# def init_model(model_name, ret_id, db_id, db_path, top_k, tgt_dialect=None):
#     translator, retriever, vector_db = None, None, None

#     if retrieval_on:
#         retriever = RetrievalModel(ret_id)
#         vector_db = dict()
#         if ret_id == "cross-lingual":
#             embed_func = dict()
#         for key in model_dict[ret_id].keys():
#             embed_func[key] = CodeDescEmbedding(input_sizes=(768, 384, 1024, 1024), hidden_size=512,
#                                                 num_experts=2, num_heads=4, dropout=0.05).to(device)
#             embed_func[key] = torch.nn.DataParallel(embed_func[key])
#             model_source = torch.load(model_dict[ret_id][key], map_location=device)
#             embed_func[key].load_state_dict(model_source["model"])

#             embed_func[key] = embed_func[key].module
#             embed_func[key].eval()
#     else:
#         embed_func = HuggingFaceEmbeddings(model_name=model_dict[ret_id])

#     for key in ["func", "keyword", "type"]:
#         if isinstance(embed_func, dict):
#             vector_db[key] = VectorDB(db_id, db_path[key], embed_func[key])
#         else:
#             vector_db[key] = VectorDB(db_id, db_path[key], embed_func)

#         vector_db_bak = dict()
#         embed_func = HuggingFaceEmbeddings(model_name=model_dict[ret_bak_id])
#         for key in ["func", "keyword", "type"]:
#             vector_db_bak[key] = VectorDB("Chroma", f"./data/chroma_db/{tgt_dialect}_{key}_{ret_bak_id}", embed_func)
#     else:
#         return translator, None, None

#     return translator, retriever, vector_db


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


class Translate:
    def __init__(self, model_name, src_sql, src_dialect, tgt_dialect, tgt_db_host, tgt_db_port,
                 tgt_db_user, tgt_db_password, tgt_db_name, src_embedding_model_name, tgt_embedding_model_name,
                 src_collection_id, tgt_collection_id, top_k, history_id=None, out_type="db", retrieval_on=True):
        self.model_name = model_name
        self.src_collection_id = src_collection_id
        self.tgt_collection_id = tgt_collection_id
        self.src_sql = src_sql
        self.src_dialect = src_dialect
        self.tgt_dialect = tgt_dialect
        self.src_embedding_model_name = src_embedding_model_name
        self.tgt_embedding_model_name = tgt_embedding_model_name
        self.tgt_db_host = tgt_db_host
        self.tgt_db_port = tgt_db_port
        self.tgt_db_user = tgt_db_user
        self.tgt_db_password = tgt_db_password
        self.tgt_db_name = tgt_db_name
        self.top_k = top_k
        self.history_id = history_id
        self.out_type = out_type
        self.retrieval_on = retrieval_on
        self.translator = LLMTranslator(model_name)
        self.vector_db = ChromaStore()

    def local_rewrite(self, max_retry_time=2):

        model_ans_list, sql_ans_list = list(), list()
        used_pieces, lift_histories = list(), list()

        try:
            root_node, all_pieces = self.get_sql_pieces()
            normalize(root_node, self.src_dialect, self.tgt_dialect)
            self.src_sql = str(root_node)
        except ValueError as ve:
            traceback.print_exc()
            print(f"Antlr parse error: {self.src_sql}, translate cancelled, "
                  f"dialect: {self.src_dialect}\n{ve}", file=sys.stderr)
            return str(ve), model_ans_list, used_pieces, lift_histories

        if len(all_pieces) == 0:
            return self.src_sql, ['Warning: No piece find'], used_pieces, lift_histories

        now_sql = self.src_sql
        ori_piece, last_time_piece = None, None
        err_msg_list, err_info_list = list(), list()
        piece, assist_info = locate_node_piece(now_sql, self.src_dialect, self.tgt_dialect, all_pieces, root_node,
                                               self.tgt_db_name)
        if piece is None:
            history, sys_prompt, user_prompt = list(), None, None
            piece, assist_info, judge_raw = self.model_judge(root_node, all_pieces, self.src_sql, now_sql,
                                                             last_time_piece, history, sys_prompt, user_prompt)
            model_ans_list.append(judge_raw)

        while piece is not None:
            if assist_info not in err_msg_list:
                err_msg_list.append(assist_info)
                err_info_list = self.update_error_info_list(err_info_list, assist_info, piece)

            back_flag = get_restore_piece_flag(assist_info, piece, last_time_piece, ori_piece)
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
                    ans_slice = sqlglot.transpile(str(piece['Node']), read=self.src_dialect, write=self.tgt_dialect)[0]
                    model_ans = {"role": "sqlglot", "content": ans_slice, "Action": "translate",
                                 "Time": str(datetime.now())}
                except Exception as e:
                    traceback.print_exc()
                    ans_slice, model_ans = self.rewrite_piece(piece, history=[], err_info_list=err_info_list)
            else:
                ans_slice, model_ans = self.rewrite_piece(piece, history=[], err_info_list=err_info_list)

            if 'select' in ans_slice.lower() and 'select' not in str(piece['Node']).lower():
                ans_slice = '(' + ans_slice + ')'

            last_time_node = TreeNode(ans_slice, self.src_dialect, is_terminal=True, father=None,
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

            piece, assist_info = locate_node_piece(now_sql, self.src_dialect,
                                                   self.tgt_dialect, all_pieces, root_node, self.tgt_db_name)
            if piece is None:
                if now_sql in sql_ans_list:
                    return now_sql, model_ans_list, used_pieces, lift_histories

                piece, assist_info, judge_raw = self.handle_syntactic_correct_piece(src_sql, now_sql, root_node,
                                                                                    all_pieces, last_time_piece,
                                                                                    model_ans_list)

                model_ans_list.append(judge_raw)

            if now_sql not in sql_ans_list:
                sql_ans_list.append(now_sql)

        return now_sql, model_ans_list, used_pieces, lift_histories

    def rewrite_piece(self, piece, history=list(), err_info_list=list()) -> [str, str]:
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
        if self.retrieval_on:
            if piece['Count'] == 0:
                sys_prompt = SYSTEM_PROMPT_SEG.format(src_dialect=map_rep[self.src_dialect],
                                                      tgt_dialect=map_rep[self.tgt_dialect]).strip("\n")
                user_prompt = USER_PROMPT_SEG.format(src_dialect=map_rep[self.src_dialect],
                                                     tgt_dialect=map_rep[self.tgt_dialect],
                                                     sql=input_sql, hint=hint, example=example).strip("\n")
            else:
                document = self.get_document_description(piece)
                sys_prompt = SYSTEM_PROMPT_RET.format(src_dialect=map_rep[self.src_dialect],
                                                      tgt_dialect=map_rep[self.tgt_dialect]).strip("\n")
                user_prompt = USER_PROMPT_RET.format(src_dialect=map_rep[self.src_dialect],
                                                     tgt_dialect=map_rep[self.tgt_dialect],
                                                     sql=input_sql, hint=hint, example=example,
                                                     document=document).strip("\n")
        else:
            sys_prompt = SYSTEM_PROMPT_NA.format(src_dialect=map_rep[self.src_dialect],
                                                 tgt_dialect=map_rep[self.tgt_dialect]).strip("\n")
            user_prompt = USER_PROMPT_NA.format(src_dialect=map_rep[self.src_dialect],
                                                tgt_dialect=map_rep[self.tgt_dialect],
                                                sql=input_sql, example=example).strip("\n")

        answer_raw = self.translator.trans_func(history, sys_prompt, user_prompt, out_json=True)
        answer_raw["Action"] = "translate"
        answer_raw["Time"] = str(datetime.now())
        answer_raw["SYSTEM_PROMPT"] = sys_prompt
        answer_raw["USER_PROMPT"] = user_prompt
        return answer_raw["Answer"], answer_raw

    def get_sql_pieces(self):
        root_node, line, col, msg = parse_tree(self.src_sql, self.src_dialect)
        if root_node is None:
            raise ValueError(f"Parse error when executing ANTLR parser of {self.src_dialect}.\n"
                             f"The sql is {self.src_sql}")
        all_pieces, root_node = get_all_piece(root_node, self.src_dialect)
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

    def get_document_description(self, piece):
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
            if self.model_name == "cross-lingual":
                emebddingstr = embedding_manager.get_embedding(str(key) + '--separator--' + str(desc),
                                                               self.src_embedding_model_name)
                results.extend([ite[0] for ite in
                                self.vector_db.search_by_id(self.src_collection_id, emebddingstr, top_k=self.top_k)])
            else:
                emebddingstr = embedding_manager.get_embedding(desc["Desc"], self.tgt_embedding_model_name)
                results.extend([ite[0] for ite in
                                self.vector_db.search_by_id(self.tgt_collection_id, emebddingstr, top_k=self.top_k)])

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
                    f"{map_rep[self.src_dialect]} snippet": f"`{key}`: {' '.join(desc['Desc'].split()[:chunk_size])[:2 * chunk_size]}...",
                    f"{map_rep[self.tgt_dialect]} snippet": [f"`{tk}`: {tdesc}" for tk, tdesc in zip(tgt_key, tgt_desc)]
                }
            )

        document = json.dumps(document, indent=4)

        return document

    def update_error_info_list(self, err_info_list, assist_info, piece):
        if self.tgt_dialect == "oracle":
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

    def handle_syntactic_correct_piece(self, src_sql, now_sql, root_node, all_pieces, last_time_piece, model_ans_list):
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

            user_prompt = USER_PROMPT_REFLECT.format(src_dialect=map_rep[self.src_dialect],
                                                     tgt_dialect=map_rep[self.tgt_dialect],
                                                     src_sql=src_sql, tgt_sql=now_sql,
                                                     snippet=f"`{str(last_time_piece['Node'])}`").strip("\n")

        piece, assist_info, judge_raw = self.model_judge(root_node, all_pieces, src_sql, now_sql,
                                                         last_time_piece, history, sys_prompt, user_prompt)

        return piece, assist_info, judge_raw

    def model_judge(self, root_node, all_pieces, src_sql, now_sql, ans_slice, history=list(), sys_prompt=None,
                    user_prompt=None):
        if ans_slice is None:
            snippet = "all snippets"
        else:
            snippet = f"`{str(ans_slice['Node'])}`"

        if sys_prompt is None:
            sys_prompt = SYSTEM_PROMPT_JUDGE.format(src_dialect=self.src_dialect, tgt_dialect=self.tgt_dialect).strip(
                "\n")
        if user_prompt is None:
            user_prompt = USER_PROMPT_JUDGE.format(src_dialect=self.src_dialect, tgt_dialect=self.tgt_dialect,
                                                   src_sql=src_sql, tgt_sql=now_sql, snippet=snippet).strip("\n")
        answer_raw = self.translator.trans_func(history, sys_prompt, user_prompt)
        pattern = r'"SQL Snippet":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
        res = parse_llm_answer_v2(self.translator.model_name, answer_raw, pattern)
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

    def direct_rewrite(self):
        translator = LLMTranslator(self.model_name)
        history, model_ans_list = list(), list()

        sys_prompt = None
        user_prompt = USER_PROMPT_DIR.format(src_dialect=map_rep[self.src_dialect],
                                             tgt_dialect=map_rep[self.tgt_dialect], sql=self.src_sql).strip("\n")

        answer = translator.trans_func(history, sys_prompt, user_prompt, out_json=True)
        now_sql = answer["Answer"]
        answer_raw = {}
        answer_raw["Action"] = "translate"
        answer_raw["Time"] = str(datetime.now())
        answer_raw["SYSTEM_PROMPT"] = sys_prompt
        answer_raw["USER_PROMPT"] = user_prompt

        model_ans_list.append(answer_raw)

        self.add_process("SQL改写完成", "改写结果", now_sql, "assistant", True, None)

        return now_sql, model_ans_list

    def add_process(self, content, step_name, sql, role, is_success, error):
        if self.out_type == "file":
            # 添加到文件
            pass
        elif self.out_type == "db":
            # 添加到数据库 
            # 添加改写结果记录
            from api.services.rewrite import RewriteService
            RewriteService.add_rewrite_process(
                history_id=self.history_id,
                content=content,
                step_name=step_name,
                sql=sql,
                role=role,
                is_success=is_success,
                error=error
            )
            RewriteService.update_rewrite_status(
                history_id=self.history_id,
                status=RewriteStatus.SUCCESS if is_success else RewriteStatus.FAILED,
                sql=sql,
                error=error
            )
