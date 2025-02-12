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
    def __init__(self, 
                 model_name: str,
                 src_sql: str,
                 src_dialect: str, 
                 tgt_dialect: str,
                 tgt_db_config: dict,
                 embedding_config: dict,
                 vector_config: dict,
                 history_id: str = None,
                 out_type: str = "db",
                 retrieval_on: bool = True):
        """SQL方言转换器
        
        该类用于将一种SQL方言转换为另一种SQL方言,支持检索增强和历史记录功能。
        
        Args:
            model_name: 使用的LLM模型名称,如 'gpt-3.5-turbo'
            src_sql: 需要转换的源SQL语句
            src_dialect: 源SQL方言,如 'mysql' 
            tgt_dialect: 目标SQL方言,如 'postgresql'
            tgt_db_config: 目标数据库配置,字典格式包含:
                - host: 数据库主机地址
                - port: 端口号
                - user: 用户名
                - password: 密码
                - db_name: 数据库名
            embedding_config: 嵌入模型配置,字典格式包含:
                - src_model_name: 源方言嵌入模型名称
                - tgt_model_name: 目标方言嵌入模型名称
            vector_config: 向量数据库配置,字典格式包含:
                - src_collection_id: 源方言向量集合ID
                - tgt_collection_id: 目标方言向量集合ID
                - top_k: 检索时返回的最相似结果数量
            history_id: 历史记录ID,用于追踪转换过程
            out_type: 输出类型,支持:
                - "db": 结果保存到数据库
                - "file": 结果保存到文件
            retrieval_on: 是否启用检索增强功能
        """
        # 基础配置
        self.model_name = model_name
        self.src_sql = src_sql
        self.src_dialect = src_dialect 
        self.tgt_dialect = tgt_dialect

        # 目标数据库配置
        self.tgt_db_config = tgt_db_config
        
        # 嵌入模型相关配置
        self.src_embedding_model_name = embedding_config['src_model_name']  # 源方言嵌入模型
        self.tgt_embedding_model_name = embedding_config['tgt_model_name']  # 目标方言嵌入模型
        self.src_collection_id = vector_config['src_collection_id']      # 源方言向量集合
        self.tgt_collection_id = vector_config['tgt_collection_id']      # 目标方言向量集合
        self.top_k = vector_config['top_k']                             # 检索TOP-K结果数

        # 其他配置
        self.history_id = history_id  # 历史记录ID
        self.out_type = out_type      # 输出类型
        self.retrieval_on = retrieval_on  # 是否启用检索

        # 初始化核心组件
        self.translator = LLMTranslator(model_name)  # 初始化LLM翻译器
        self.vector_db = ChromaStore()              # 初始化向量数据库

    def local_rewrite(self, max_retry_time=2):
        """局部SQL改写方法
        
        该方法通过逐步定位和改写SQL片段来完成整个SQL的转换。支持重试机制和提升操作。
        
        Args:
            max_retry_time: 最大重试次数,默认为2次。超过后会触发提升操作。
            
        Returns:
            tuple: 包含以下元素:
                - str: 转换后的SQL语句。如果转换失败则返回错误信息。
                - list: 模型输出的历史记录列表。
                - list: 已处理的SQL片段列表。
                - list: 提升操作的历史记录列表。
                
        工作流程:
            1. 解析源SQL获取语法树和所有片段
            2. 规范化处理
            3. 循环处理每个定位到的片段:
                - 尝试直接转换
                - 如果失败则使用检索增强
                - 超过重试次数则进行提升操作
            4. 记录转换过程和结果
        """
        # 初始化结果列表
        model_ans_list, sql_ans_list = list(), list()
        used_pieces, lift_histories = list(), list()

        try:
            # 解析SQL获取语法树和片段
            root_node, all_pieces = self.get_sql_pieces()
            # 规范化处理
            normalize(root_node, self.src_dialect, self.tgt_dialect)
            self.src_sql = str(root_node)
        except ValueError as ve:
            # 解析失败处理
            traceback.print_exc()
            print(f"Antlr parse error: {self.src_sql}, translate cancelled, "
                  f"dialect: {self.src_dialect}\n{ve}", file=sys.stderr)
            return str(ve), model_ans_list, used_pieces, lift_histories

        # 如果没有找到可处理的片段,直接返回源SQL
        if len(all_pieces) == 0:
            return self.src_sql, ['Warning: No piece find'], used_pieces, lift_histories

        # 初始化转换状态
        now_sql = self.src_sql
        ori_piece, last_time_piece = None, None
        err_msg_list, err_info_list = list(), list()
        
        # 定位第一个需要处理的片段
        piece, assist_info = locate_node_piece(now_sql, self.src_dialect, self.tgt_dialect, 
                                             all_pieces, root_node, self.tgt_db_config['db_name'])
        
        # 如果没有定位到片段,使用模型判断
        if piece is None:
            history, sys_prompt, user_prompt = list(), None, None
            piece, assist_info, judge_raw = self.model_judge(root_node, all_pieces, self.src_sql, now_sql,
                                                           last_time_piece, history, sys_prompt, user_prompt)
            model_ans_list.append(judge_raw)

        # 主循环:处理每个定位到的片段
        while piece is not None:
            # 更新错误信息列表
            if assist_info not in err_msg_list:
                err_msg_list.append(assist_info)
                err_info_list = self.update_error_info_list(err_info_list, assist_info, piece)

            # 检查是否需要恢复到之前的状态
            back_flag = get_restore_piece_flag(assist_info, piece, last_time_piece, ori_piece)
            if back_flag:
                # 恢复到之前的状态
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
                # 保存当前片段作为原始状态
                ori_piece = piece
                err_msg_list, err_info_list = list(), list()

            node, tree_node = piece['Node'], piece['Tree']
            
            # 检查是否需要提升操作
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

            # 更新片段信息
            piece['Node'], piece['Tree'] = node, tree_node
            used_pieces.append({
                "piece": str(piece['Node']),
                "Keyword": piece['Keyword']
            })

            # 尝试转换当前片段
            if piece["Count"] == 0:
                try:
                    # 首次尝试使用sqlglot直接转换
                    ans_slice = sqlglot.transpile(str(piece['Node']), read=self.src_dialect, write=self.tgt_dialect)[0]
                    model_ans = {"role": "sqlglot", "content": ans_slice, "Action": "translate",
                               "Time": str(datetime.now())}
                except Exception as e:
                    # sqlglot转换失败,使用自定义转换方法
                    traceback.print_exc()
                    ans_slice, model_ans = self.rewrite_piece(piece, history=[], err_info_list=err_info_list)
            else:
                # 非首次尝试,直接使用自定义转换方法
                ans_slice, model_ans = self.rewrite_piece(piece, history=[], err_info_list=err_info_list)

            # 处理SELECT语句的特殊情况
            if 'select' in ans_slice.lower() and 'select' not in str(piece['Node']).lower():
                ans_slice = '(' + ans_slice + ')'

            # 创建新的树节点并更新语法树
            last_time_node = TreeNode(ans_slice, self.src_dialect, is_terminal=True, father=None,
                                    father_child_index=None, children=None, model_get=True)
            if piece['Node'] == root_node:
                root_node = last_time_node
            else:
                piece["Node"].father.replace_child(piece["Node"], last_time_node)
            
            # 更新片段列表
            all_pieces.remove(piece)
            new_piece = {
                "Node": last_time_node,
                "Tree": None,
                "Description": None,  # 设置为None,因为片段的具体含义未知
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

            # 记录转换结果
            model_ans["Translated SQL"] = now_sql
            model_ans_list.append(model_ans)

            # 定位下一个需要处理的片段
            piece, assist_info = locate_node_piece(now_sql, self.src_dialect,
                                                 self.tgt_dialect, all_pieces, root_node, self.tgt_db_config['db_name'])
            if piece is None:
                # 检查是否出现重复结果
                if now_sql in sql_ans_list:
                    return now_sql, model_ans_list, used_pieces, lift_histories

                # 使用模型判断是否需要继续处理
                piece, assist_info, judge_raw = self.handle_syntactic_correct_piece(self.src_sql, now_sql, root_node,
                                                                              all_pieces, last_time_piece,
                                                                              model_ans_list)
                model_ans_list.append(judge_raw)

            # 记录当前SQL结果
            if now_sql not in sql_ans_list:
                sql_ans_list.append(now_sql)

        return now_sql, model_ans_list, used_pieces, lift_histories

    def rewrite_piece(self, piece, history=list(), err_info_list=list()) -> [str, str]:
        """SQL片段重写方法
        
        Args:
            piece: SQL片段,可以是字典(包含Node节点)或字符串
            history: 历史转换记录列表
            err_info_list: 错误信息列表
        
        Returns:
            tuple: (转换后的SQL, 模型响应的完整信息)
        """
        # 处理输入SQL片段,支持字典或字符串格式
        if isinstance(piece, Dict):
            input_sql = str(piece['Node'])
        elif isinstance(piece, str):
            input_sql = piece

        # 构建错误示例提示
        example = str()
        for item in err_info_list:
            item['SQL Snippet'] = item['SQL Snippet'].strip('\n')
            example += f"-- ERROR: {item['Error']}\n{item['SQL Snippet']}\n\n"

        example = example.strip("\n")
        if len(example) != 0:
            # 将错误示例格式化到模板中
            example = EXAMPLE_PROMPT.format(example)

        hint = str()
        if self.retrieval_on:  # 如果启用检索增强
            if piece['Count'] == 0:  # 首次尝试
                # 使用基础转换提示模板
                sys_prompt = SYSTEM_PROMPT_SEG.format(
                    src_dialect=map_rep[self.src_dialect],
                    tgt_dialect=map_rep[self.tgt_dialect]
                ).strip("\n")
                user_prompt = USER_PROMPT_SEG.format(
                    src_dialect=map_rep[self.src_dialect],
                    tgt_dialect=map_rep[self.tgt_dialect],
                    sql=input_sql, 
                    hint=hint, 
                    example=example
                ).strip("\n")
            else:  # 非首次尝试,使用检索增强
                # 获取相似案例描述
                document = self.get_document_description(piece)
                # 使用检索增强提示模板
                sys_prompt = SYSTEM_PROMPT_RET.format(
                    src_dialect=map_rep[self.src_dialect],
                    tgt_dialect=map_rep[self.tgt_dialect]
                ).strip("\n")
                user_prompt = USER_PROMPT_RET.format(
                    src_dialect=map_rep[self.src_dialect],
                    tgt_dialect=map_rep[self.tgt_dialect],
                    sql=input_sql, 
                    hint=hint, 
                    example=example,
                    document=document
                ).strip("\n")
        else:  # 不启用检索增强
            # 使用普通转换提示模板
            sys_prompt = SYSTEM_PROMPT_NA.format(
                src_dialect=map_rep[self.src_dialect],
                tgt_dialect=map_rep[self.tgt_dialect]
            ).strip("\n")
            user_prompt = USER_PROMPT_NA.format(
                src_dialect=map_rep[self.src_dialect],
                tgt_dialect=map_rep[self.tgt_dialect],
                sql=input_sql, 
                example=example
            ).strip("\n")

        # 调用翻译器进行转换
        answer_raw = self.translator.trans_func(
            history, 
            sys_prompt, 
            user_prompt, 
            out_json=True
        )
        
        # 添加额外信息到响应中
        answer_raw["Action"] = "translate"  # 动作类型
        answer_raw["Time"] = str(datetime.now())  # 执行时间
        answer_raw["SYSTEM_PROMPT"] = sys_prompt  # 系统提示
        answer_raw["USER_PROMPT"] = user_prompt   # 用户提示
        
        return answer_raw["Answer"], answer_raw

    def get_sql_pieces(self):
        """获取SQL语句的所有片段
        
        该方法将SQL语句解析为语法树，并提取所有可处理的SQL片段。
        
        Returns:
            tuple: (根节点, 所有片段列表)
                - root_node: SQL语法树的根节点
                - all_pieces: 包含所有SQL片段的列表，每个片段是一个字典
        
        Raises:
            ValueError: 当SQL解析失败时抛出异常
        """
        # 使用ANTLR解析器解析SQL语句
        root_node, line, col, msg = parse_tree(self.src_sql, self.src_dialect)
        if root_node is None:
            # 解析失败时抛出异常
            raise ValueError(f"Parse error when executing ANTLR parser of {self.src_dialect}.\n"
                             f"The sql is {self.src_sql}")

        # 获取所有SQL片段
        all_pieces, root_node = get_all_piece(root_node, self.src_dialect)

        # 检查根节点是否已经在片段列表中
        flag = True
        for piece in all_pieces:
            if root_node == piece['Node']:
                flag = False
                break

        # 如果根节点不在片段列表中，创建根片段并添加到列表
        if flag:
            # 创建根片段字典
            root_piece = {
                "Node": root_node,          # 语法树节点
                "Tree": root_node,          # 完整语法树
                "Description": {            # 片段描述
                    "Type": "Keyword",
                    "Desc": "The whole SQL snippet above."
                },
                "Keyword": '',             # 关键字（根节点为空）
                "SubPieces": [piece for piece in all_pieces],  # 子片段列表
                "FatherPiece": None,       # 父片段（根节点无父片段）
                "Count": 0,                # 处理计数器
                'TrackPieces': []          # 追踪片段列表
            }

            # 更新所有没有父片段的片段，将其父片段设置为根片段
            for piece in all_pieces:
                if piece['FatherPiece'] is None:
                    piece['FatherPiece'] = root_piece
            
            # 将根片段添加到片段列表
            all_pieces.append(root_piece)

        return root_node, all_pieces

    def get_document_description(self, piece):
        """获取SQL片段的相关文档描述
        
        该方法通过向量检索获取与当前SQL片段相关的参考文档。
        
        Args:
            piece: SQL片段字典，包含关键字和描述信息
        
        Returns:
            str: JSON格式的文档描述
        """
        # 收集源SQL片段的关键字和描述
        src_key = [str(piece['Keyword'])]
        src_desc = [piece['Description']]
        # 收集子片段的关键字和描述
        for sub_piece in piece['SubPieces']:
            if sub_piece['Keyword'] is not None and sub_piece['Keyword'] not in src_key:
                src_key.append(sub_piece['Keyword'])
                src_desc.append(sub_piece['Description'])

        # 存储检索到的文档信息
        document = list()
        
        # 处理每个关键字和描述对
        for key, desc in zip(src_key, src_desc):
            # 跳过无效或根节点描述
            if desc is None or desc["Desc"] == "The whole SQL snippet above.":
                continue

            # 存储检索结果
            results = list()
            if self.model_name == "cross-lingual":
                # 跨语言模型：使用关键字和描述的组合进行检索
                emebddingstr = embedding_manager.get_embedding(
                    str(key) + '--separator--' + str(desc),
                    self.src_embedding_model_name
                )
                results.extend([ite[0] for ite in
                              self.vector_db.search_by_id(self.src_collection_id, emebddingstr, top_k=self.top_k)])
            else:
                # 普通模型：仅使用描述进行检索
                emebddingstr = embedding_manager.get_embedding(
                    desc["Desc"], 
                    self.tgt_embedding_model_name
                )
                results.extend([ite[0] for ite in
                              self.vector_db.search_by_id(self.tgt_collection_id, emebddingstr, top_k=self.top_k)])

            # 去重处理：确保每个关键字只出现一次
            results_key = set()
            results_pre = list()
            for ite in results:
                if ite.metadata["KEYWORD"] not in results_key:
                    results_key.add(ite.metadata["KEYWORD"])
                    results_pre.append(ite)

            # 处理目标关键字：移除多余的分隔符
            tgt_key = [re.sub(r'(<sep>)(\1){2,}', r'\1', ite.metadata["KEYWORD"]) for ite in results_pre]

            # 处理目标描述
            tgt_desc = list()
            for ite in results_pre:
                temp = list()
                try:
                    # 解析存储的元数据
                    detail = eval(ite.metadata["ALL"])
                    # 处理每个知识字段
                    for field in KNOWLEDGE_FIELD_LIST:
                        cont = detail.get(field, "")
                        # 处理列表类型的内容
                        if isinstance(cont, list):
                            cont = ";".join(cont).replace(";;", ";")
                        if cont != "":
                            # 特殊处理包含"Purpose"的内容
                            if "</eps> The Purpose" in cont:
                                parts = cont.split("</eps> The Purpose")
                                parts[0] = parts[0].split()[:chunk_size]
                                parts[1] = f"The Purpose{parts[1].strip()[:chunk_size]}"
                                temp.append(
                                    f" <{field}> : {' '.join([parts[0], parts[1]])}...")
                            else:
                                # 截断过长的内容
                                temp.append(
                                    f" <{field}> : {' '.join(cont.split()[:chunk_size])[:2 * chunk_size]}...")
                    tgt_desc.append(" <sep> ".join(temp))
                except Exception as e:
                    traceback.print_exc()

            # 构建文档描述
            document.append({
                # 源方言片段描述
                f"{map_rep[self.src_dialect]} snippet": (
                    f"`{key}`: {' '.join(desc['Desc'].split()[:chunk_size])[:2 * chunk_size]}..."
                ),
                # 目标方言片段描述
                f"{map_rep[self.tgt_dialect]} snippet": [
                    f"`{tk}`: {tdesc}" for tk, tdesc in zip(tgt_key, tgt_desc)
                ]
            })

        # 转换为格式化的JSON字符串
        document = json.dumps(document, indent=4)

        return document

    def update_error_info_list(self, err_info_list, assist_info, piece):
        """更新错误信息列表
        
        该方法根据不同的目标数据库方言处理错误信息，并更新错误信息列表。
        
        Args:
            err_info_list: 现有的错误信息列表
            assist_info: 辅助信息（错误消息）
            piece: SQL片段字典
        
        Returns:
            list: 更新后的错误信息列表
        """
        # Oracle数据库的特殊错误处理
        if self.tgt_dialect == "oracle":
            # 初始化错误信息前缀
            assist_info_pre = f"Some error occurs near the snippet:"
            
            try:
                # 处理Oracle特定错误
                # 跳过'ORA-00933'错误（SQL命令未正确结束），处理其他ERROR信息
                if 'ORA-00933: SQL command not properly ended' not in assist_info \
                        and 'ERROR' in assist_info:
                    # 定位ERROR关键字位置
                    err_pos = assist_info.index("ERROR")
                    # 添加错误位置后的信息
                    assist_info_pre += assist_info[err_pos:]
                    
                # 处理错误消息格式
                assist_info_pre = process_err_msg(assist_info_pre)
                
                # 添加到错误信息列表
                err_info_list.append({
                    "Error": assist_info_pre,           # 处理后的错误信息
                    "SQL Snippet": str(piece["Node"])   # 相关的SQL片段
                })
                
            except Exception as e:
                # 异常处理：记录异常并添加基础错误信息
                traceback.print_exc()
                assist_info_pre = process_err_msg(assist_info_pre)
                err_info_list.append({
                    "Error": assist_info_pre,
                    "SQL Snippet": str(piece["Node"])
                })
        else:
            # 非Oracle数据库的错误处理
            # 直接处理错误消息并添加到列表
            assist_info = process_err_msg(assist_info)
            err_info_list.append({
                "Error": assist_info,
                "SQL Snippet": str(piece["Node"])
            })

        return err_info_list

    def handle_syntactic_correct_piece(self, src_sql, now_sql, root_node, all_pieces, last_time_piece, model_ans_list):
        """处理语法正确的SQL片段
        
        该方法处理已经通过语法检查的SQL片段，判断是否需要进一步优化或修改。
        
        Args:
            src_sql: 原始SQL语句
            now_sql: 当前转换后的SQL语句
            root_node: SQL语法树的根节点
            all_pieces: 所有SQL片段列表
            last_time_piece: 上一次处理的片段
            model_ans_list: 模型回答历史列表
        
        Returns:
            tuple: (piece, assist_info, judge_raw)
                - piece: 需要进一步处理的SQL片段
                - assist_info: 辅助信息
                - judge_raw: 模型判断的原始输出
        """
        # 初始化历史记录和提示信息
        history, sys_prompt, user_prompt = list(), None, None
        
        # 如果存在模型回答历史
        if len(model_ans_list) > 0:
            # 查找最近一次包含系统提示的回答
            no = -1
            for i in range(len(model_ans_list) - 1, 0, -1):
                if "SYSTEM_PROMPT" in model_ans_list[i].keys():
                    no = i
                    break
                
            # 复制模型消息以避免修改原始数据
            model_message = copy.deepcopy(model_ans_list[no])

            # 移除动作标记
            model_message.pop("Action")
            
            # 提取系统提示和用户提示
            sys_prompt = None
            if "SYSTEM_PROMPT" in model_message.keys():
                sys_prompt = model_message.pop("SYSTEM_PROMPT")
                user_prompt = model_message.pop("USER_PROMPT")

            # 构建对话历史
            history.append({
                "role": "user", 
                "content": user_prompt
            })
            history.append(model_message)

            # 构建新的用户提示，用于反思和评估当前转换结果
            user_prompt = USER_PROMPT_REFLECT.format(
                src_dialect=map_rep[self.src_dialect],
                tgt_dialect=map_rep[self.tgt_dialect],
                src_sql=src_sql,
                tgt_sql=now_sql,
                snippet=f"`{str(last_time_piece['Node'])}`"
            ).strip("\n")

        # 调用模型进行判断
        piece, assist_info, judge_raw = self.model_judge(
            root_node,           # 语法树根节点
            all_pieces,          # 所有SQL片段
            src_sql,            # 源SQL
            now_sql,            # 当前SQL
            last_time_piece,    # 上一次处理的片段
            history,            # 对话历史
            sys_prompt,         # 系统提示
            user_prompt         # 用户提示
        )

        return piece, assist_info, judge_raw

    def model_judge(self, root_node, all_pieces, src_sql, now_sql, ans_slice, history=list(), sys_prompt=None,
                    user_prompt=None):
        """模型判断方法
        
        使用LLM模型判断SQL转换的质量，并识别需要进一步优化的片段。
        
        Args:
            root_node: SQL语法树的根节点
            all_pieces: 所有SQL片段列表
            src_sql: 源SQL语句
            now_sql: 当前转换后的SQL语句
            ans_slice: 上一次处理的片段
            history: 对话历史记录，默认为空列表
            sys_prompt: 系统提示，默认为None
            user_prompt: 用户提示，默认为None
        
        Returns:
            tuple: (piece, assist_info, answer_raw)
                - piece: 需要进一步处理的SQL片段
                - assist_info: 辅助信息
                - answer_raw: 模型的原始回答
        """
        # 确定要分析的片段
        if ans_slice is None:
            snippet = "all snippets"  # 分析所有片段
        else:
            snippet = f"`{str(ans_slice['Node'])}`"  # 分析特定片段

        # 如果没有提供系统提示，使用默认的判断提示模板
        if sys_prompt is None:
            sys_prompt = SYSTEM_PROMPT_JUDGE.format(
                src_dialect=self.src_dialect, 
                tgt_dialect=self.tgt_dialect
            ).strip("\n")
        
        # 如果没有提供用户提示，使用默认的判断提示模板
        if user_prompt is None:
            user_prompt = USER_PROMPT_JUDGE.format(
                src_dialect=self.src_dialect,
                tgt_dialect=self.tgt_dialect,
                src_sql=src_sql,
                tgt_sql=now_sql,
                snippet=snippet
            ).strip("\n")

        # 调用翻译器获取模型判断结果
        answer_raw = self.translator.trans_func(history, sys_prompt, user_prompt)
        
        # 使用正则表达式解析模型回答
        pattern = r'"SQL Snippet":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?),\s*"Confidence":\s*(.*?)\s'
        res = parse_llm_answer_v2(self.translator.model_name, answer_raw, pattern)
        snippet = res["Answer"]

        # 添加额外信息到回答中
        answer_raw["Action"] = "judge"  # 动作类型
        answer_raw["Time"] = str(datetime.now())  # 执行时间
        answer_raw["SYSTEM_PROMPT"] = sys_prompt  # 系统提示
        answer_raw["USER_PROMPT"] = user_prompt   # 用户提示

        # 初始化返回值
        piece, assist_info = None, None
        
        # 判断是否需要进一步处理
        # 当模型认为不需要修改或置信度低时，直接返回
        if "NONE" in snippet or "almost equivalent" in str(answer_raw) \
                or (isinstance(res['Confidence'], float) and res['Confidence'] < 0.8):
            return piece, assist_info, answer_raw

        # 构建辅助信息，包含需要检查的片段和模型的推理过程
        assist_info = f"The following snippet needs to be further examined: \n`{snippet}`\n" \
                      f"And some reflections about this translated snippet are: <reflection> {res['Reasoning']} </reflection>. " \
                      f"Note that these reflections might be incorrect, " \
                      f"so please carefully identify what is correct for the successful translation."

        # 在当前SQL中定位需要处理的片段
        column = now_sql.find(snippet)
        if column != -1:
            # 找到对应的语法树节点
            node, _ = TreeNode.locate_node(root_node, column, now_sql)
            # 在所有片段中找到对应的片段
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
