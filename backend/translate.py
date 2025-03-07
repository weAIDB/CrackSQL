import argparse
import asyncio
import copy
import json
import os
import re
import sys
import traceback
from datetime import datetime
from typing import Dict

import sqlglot
from tqdm import tqdm

from app_factory import create_app
from config.db_config import db_session_manager
from llm_model.embeddings import get_embeddings
from models import DatabaseConfig, KnowledgeBase
from preprocessor.antlr_parser.parse_tree import parse_tree
from preprocessor.query_simplifier.Tree import TreeNode, lift_node
from preprocessor.query_simplifier.locate import locate_node_piece, replace_piece, get_func_name, find_piece
from preprocessor.query_simplifier.normalize import normalize
from preprocessor.query_simplifier.rewrite import get_all_piece
from translator.judge_prompt import SYSTEM_PROMPT_JUDGE, USER_PROMPT_JUDGE, USER_PROMPT_REFLECT
from translator.llm_translator import LLMTranslator
from translator.translate_prompt import SYSTEM_PROMPT_NA, USER_PROMPT_NA, \
    SYSTEM_PROMPT_SEG, USER_PROMPT_SEG, SYSTEM_PROMPT_RET, USER_PROMPT_RET, EXAMPLE_PROMPT, JUDGE_INFO_PROMPT
from utils.constants import DIALECT_MAP, FAILED_TEMPLATE, CHUNK_SIZE, TRANSLATION_ANSWER_PATTERN, \
    JUDGE_ANSWER_PATTERN, DIALECT_LIST
from utils.tools import process_err_msg, process_history_text
from vector_store.chroma_store import ChromaStore


# rule translation


class Translator:
    def __init__(self,
                 model_name: str,
                 src_sql: str,
                 src_dialect: str,
                 tgt_dialect: str,
                 tgt_db_config: dict,
                 vector_config: dict,
                 retrieval_on: bool,
                 top_k: int,
                 history_id: str = None,
                 out_type: str = "file",
                 out_dir: str = None):
        """SQL dialect converter
        
        This class is used to convert one SQL dialect to another, supporting retrieval enhancement and history tracking.
        
        Args:
            model_name: The LLM model name used, such as 'gpt-3.5-turbo'
            src_sql: Source SQL statement to be converted
            src_dialect: Source SQL dialect, such as 'mysql'
            tgt_dialect: Target SQL dialect, such as 'postgresql'
            tgt_db_config: Target database configuration, dictionary format including:
                - host: Database host address
                - port: Port number
                - user: Username
                - password: Password
                - db_name: Database name
            vector_config: Vector database configuration, dictionary format including:
                - src_kb_name: Source dialect vector collection ID
                - tgt_kb_name: Target dialect vector collection ID
            retrieval_on: Whether to enable retrieval
            top_k: Number of most similar results to return during retrieval
            history_id: History record ID, used to track the conversion process
            out_type: Output type, supports:
                - "db": Results saved to database
                - "file": Results saved to file
            out_dir: Output Directory to dump result
        """
        # Basic configuration
        self.model_name = model_name
        self.src_sql = src_sql
        self.src_dialect = src_dialect
        self.tgt_dialect = tgt_dialect
        self.vector_config = vector_config
        self.tgt_db_config = tgt_db_config
        

        if self.src_dialect == "postgresql":
            self.src_dialect = "pg"
        if self.tgt_dialect == "postgresql":
            self.tgt_dialect = "pg"

        # Target database configuration
        self.tgt_db_config = tgt_db_config

        # Embedding model related configuration
        self.src_kb_name = vector_config['src_kb_name']  # Source dialect vector collection
        self.tgt_kb_name = vector_config['tgt_kb_name']  # Target dialect vector collection
        self.tgt_embedding_model_name = KnowledgeBase.query.filter_by(
            kb_name=vector_config['tgt_kb_name']).first().embedding_model_name

        self.retrieval_on = retrieval_on  # Whether to enable retrieval
        self.top_k = top_k  # Retrieval TOP-K results

        # Other configurations
        self.history_id = history_id  # History record ID
        self.out_type = out_type  # Output type
        self.out_dir = out_dir  # Output directory
        self.out_file = None
        if self.out_type is 'file':
            if not os.path.exists(self.out_dir):
                os.makedirs(self.out_dir)
            file_name = f"{self.src_dialect}_{self.tgt_dialect}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            self.out_file = os.path.join(self.out_dir, file_name)
            self.init_out_file()
        # Initialize core components
        self.translator = LLMTranslator(model_name)  # Initialize LLM translator
        self.vector_db = ChromaStore()  # Initialize vector database

    @db_session_manager
    def local_to_global_rewrite(self, max_retry_time=2):
        """Local SQL rewriting method
        
        This method completes the entire SQL conversion by gradually locating and rewriting SQL fragments. 
        Supports retry mechanism and lift operations.
        
        Args:
            max_retry_time: Maximum retry times, default is 2. Exceeding this will trigger lift operation.
            
        Returns:
            tuple: Contains the following elements:
                - str: Converted SQL statement. Returns error message if conversion fails.
                - list: Model output history records.
                - list: Processed SQL fragments.
                - list: Lift operation history records.
                
        Workflow:
            1. Parse source SQL to get syntax tree and all fragments
            2. Normalization processing
            3. Loop through each located fragment:
                - Try direct conversion
                - Use retrieval enhancement if fails
                - Perform lift operation if exceeds retry times
            4. Record conversion process and results
        """

        # Initialize result lists
        model_ans_list, sql_ans_list = list(), list()
        used_pieces, lift_histories = list(), list()

        try:
            # rule normalization
            # self.src_sql = self.rule_rewrite(self.src_sql, self.src_dialect, self.src_dialect)

            # Parse SQL to get syntax tree and fragments
            root_node, all_pieces = self.do_query_segmentation()
            # Normalization processing
            normalize(root_node, self.src_dialect, self.tgt_dialect)
            self.src_sql = str(root_node)
        except ValueError as ve:
            # Handle parsing failure
            traceback.print_exc()
            print(f"Antlr parse error: {self.src_sql}, translate cancelled, "
                  f"dialect: {self.src_dialect}\n{ve}", file=sys.stderr)
            return str(ve), model_ans_list, used_pieces, lift_histories

        # If no processable fragments found, return source SQL directly
        if len(all_pieces) == 0:
            return self.src_sql, ['Warning: No piece find'], used_pieces, lift_histories

        # rule translation
        # current_sql = self.rule_rewrite(self.src_sql, self.src_dialect, self.tgt_dialect)
        # piece, assist_info = locate_node_piece(current_sql, self.tgt_dialect, all_pieces,
        #                                        root_node, self.tgt_db_config)
        # if piece is None:
        #     return current_sql, model_ans_list, used_pieces, lift_histories

        # Initialize conversion state
        current_sql = self.src_sql
        ori_piece, last_time_piece = None, None
        err_msg_list, err_info_list = list(), list()

        # Locate first fragment to process
        piece, assist_info = locate_node_piece(current_sql, self.tgt_dialect, all_pieces,
                                               root_node, self.tgt_db_config, self.tgt_kb_name)

        # If no fragment located, use model judgment
        if piece is None:
            history, sys_prompt, user_prompt = list(), None, None
            piece, assist_info, judge_raw = self.model_judge(root_node, all_pieces, self.src_sql, current_sql,
                                                             last_time_piece, history, sys_prompt,
                                                             user_prompt)
            model_ans_list.append(judge_raw)

        # Main loop: process each located fragment
        while piece is not None:
            # Update error message list
            if assist_info not in err_msg_list:
                err_msg_list.append(assist_info)
                err_info_list = self.update_error_info_list(err_info_list, assist_info, piece)

            # Check if need to restore to previous state
            if last_time_piece is not None:
                back_flag = self.get_restore_piece_flag(assist_info, piece, last_time_piece, ori_piece)
                if back_flag:
                    # Restore to previous state
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
                    # Save current piece as original state
                    ori_piece = piece
                    err_msg_list, err_info_list = list(), list()

            node, tree_node = piece['Node'], piece['Tree']

            # Check if lift operation is needed
            if piece['Count'] > max_retry_time:
                node = piece['Node']
                if node == root_node:
                    return FAILED_TEMPLATE, model_ans_list, used_pieces, lift_histories

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

            # Update fragment information
            piece['Node'], piece['Tree'] = node, tree_node
            used_pieces.append({
                "piece": str(piece['Node']),
                "Keyword": piece['Keyword']
            })

            # # Try to convert current fragment
            # if piece["Count"] == 0:
            #     try:
            #         # First try using sqlglot for direct conversion
            #         ans_slice = self.rule_rewrite(str(piece['Node']), self.src_dialect, self.tgt_dialect)
            #         model_ans = {"role": "sqlglot", "content": ans_slice, "Action": "translate",
            #                      "Time": str(datetime.now())}
            #     except Exception as e:
            #         # If sqlglot conversion fails, use custom conversion method
            #         traceback.print_exc()
            #         ans_slice, model_ans = self.rewrite_piece(piece, history=[], err_info_list=err_info_list)
            # else:
            #     # For non-first attempts, directly use custom conversion method
            #     ans_slice, model_ans = self.rewrite_piece(piece, history=[], err_info_list=err_info_list)
            # For non-first attempts, directly use custom conversion method
            ans_slice, model_ans = self.rewrite_piece(piece, history=[], err_info_list=err_info_list)

            # Handle special case for SELECT statements
            if 'select' in ans_slice.lower() and 'select' not in str(piece['Node']).lower():
                ans_slice = '(' + ans_slice + ')'

            # Create new tree node and update syntax tree
            last_time_node = TreeNode(ans_slice, self.src_dialect, is_terminal=True, father=None,
                                      father_child_index=None, children=None, model_get=True)
            if piece['Node'] == root_node:
                root_node = last_time_node
            else:
                piece["Node"].father.replace_child(piece["Node"], last_time_node)

            # Update fragment list
            all_pieces.remove(piece)
            new_piece = {
                "Node": last_time_node,
                "Tree": None,
                "Description": None,  # Set to None as the specific meaning of the fragment is unknown
                "Keyword": piece['Keyword'],
                "SubPieces": [],
                "FatherPiece": piece['FatherPiece'],
                "Count": 0,
                "TrackPieces": [],
                "Type": None,
                "Detail": None
            }
            all_pieces.append(new_piece)
            for sub_piece in piece['SubPieces']:
                if sub_piece in all_pieces:
                    all_pieces.remove(sub_piece)
            replace_piece(piece, new_piece)
            last_time_piece, ori_piece = new_piece, piece
            current_sql = str(root_node)

            # Record conversion result
            model_ans["Translated SQL"] = current_sql
            model_ans_list.append(model_ans)

            # Locate next fragment to process
            piece, assist_info = locate_node_piece(current_sql, self.tgt_dialect, all_pieces,
                                                   root_node, self.tgt_db_config, self.tgt_kb_name)
            if piece is None:
                # Check for duplicate results
                if current_sql in sql_ans_list:
                    return current_sql, model_ans_list, used_pieces, lift_histories

                # Use model to judge if need to continue processing
                piece, assist_info, judge_raw = self.do_semantic_validation(self.src_sql, current_sql, root_node,
                                                                            all_pieces, last_time_piece, model_ans_list)

                model_ans_list.append(judge_raw)

            # Record current SQL result
            if current_sql not in sql_ans_list:
                sql_ans_list.append(current_sql)

        return current_sql, model_ans_list, used_pieces, lift_histories

    def rewrite_piece(self, piece, history=list(), err_info_list=list()) -> [str, str]:
        """SQL fragment rewriting method
        
        This method uses LLM to rewrite a SQL fragment from source dialect to target dialect.
        
        Args:
            piece: SQL fragment, can be dict (contains Node) or str
            history: History conversion record list
            err_info_list: Error information list
            
        Returns:
            tuple: (Converted SQL, Complete model response information)
        """
        # Process input SQL fragment, support dict or str format
        if isinstance(piece, Dict):
            input_sql = str(piece['Node'])
        elif isinstance(piece, str):
            input_sql = piece

        # Build error example prompt
        example = str()
        for item in err_info_list:
            item['SQL Snippet'] = item['SQL Snippet'].strip('\n')
            example += f"-- ERROR: {item['Error']}\n{item['SQL Snippet']}\n\n"

        example = example.strip("\n")
        if len(example) != 0:
            # Format error example into template
            example = EXAMPLE_PROMPT.format(example)

        hint = str()
        if self.retrieval_on:  # If retrieval enhancement is enabled
            # if piece['Count'] == 0:  # First attempt
            if False:  # First attempt
                # Use basic conversion prompt template
                sys_prompt = SYSTEM_PROMPT_SEG.format(
                    src_dialect=DIALECT_MAP[self.src_dialect],
                    tgt_dialect=DIALECT_MAP[self.tgt_dialect]
                ).strip("\n")
                user_prompt = USER_PROMPT_SEG.format(
                    src_dialect=DIALECT_MAP[self.src_dialect],
                    tgt_dialect=DIALECT_MAP[self.tgt_dialect],
                    sql=input_sql,
                    hint=hint,
                    example=example
                ).strip("\n")
            else:  # Not first attempt, use retrieval enhancement
                # Get similar case description
                document = self.get_document_description(piece)
                # Use retrieval enhanced prompt template
                sys_prompt = SYSTEM_PROMPT_RET.format(
                    src_dialect=DIALECT_MAP[self.src_dialect],
                    tgt_dialect=DIALECT_MAP[self.tgt_dialect]
                ).strip("\n")
                user_prompt = USER_PROMPT_RET.format(
                    src_dialect=DIALECT_MAP[self.src_dialect],
                    tgt_dialect=DIALECT_MAP[self.tgt_dialect],
                    sql=input_sql,
                    hint=hint,
                    example=example,
                    document=document
                ).strip("\n")
        else:  # Retrieval enhancement not enabled
            # Use normal conversion prompt template
            sys_prompt = SYSTEM_PROMPT_NA.format(
                src_dialect=DIALECT_MAP[self.src_dialect],
                tgt_dialect=DIALECT_MAP[self.tgt_dialect]
            ).strip("\n")
            user_prompt = USER_PROMPT_NA.format(
                src_dialect=DIALECT_MAP[self.src_dialect],
                tgt_dialect=DIALECT_MAP[self.tgt_dialect],
                sql=input_sql,
                example=example
            ).strip("\n")

        # Call translator for conversion
        self.add_process(content=process_history_text(user_prompt, role="user", action="translate"),
                         step_name="Rewrite result", sql=input_sql, role="user", is_success=True, error=None)
        answer_raw = self.translator.trans_func(
            history,
            sys_prompt,
            user_prompt
        )

        # Parse model answer using regex
        pattern = TRANSLATION_ANSWER_PATTERN
        res = self.translator.parse_llm_answer(answer_raw["content"], pattern)
        self.add_process(content=process_history_text(answer_raw["content"], role="assistant", action="translate"),
                         step_name="Rewrite result", sql=res["Answer"], role="assistant", is_success=True, error=None)

        answer_raw["Answer"] = res["Answer"]

        # Add extra information to response
        answer_raw["Action"] = "translate"  # Action type
        answer_raw["Time"] = str(datetime.now())  # Execution time
        answer_raw["SYSTEM_PROMPT"] = sys_prompt  # System prompt
        answer_raw["USER_PROMPT"] = user_prompt  # User prompt

        return answer_raw["Answer"], answer_raw

    def do_query_segmentation(self):
        """Get all segments of the SQL statement
        
        This method parses the SQL statement into a syntax tree and extracts all processable SQL segments.
        
        Returns:
            tuple: (root node, list of all segments)
                - root_node: Root node of the SQL syntax tree
                - all_pieces: List containing all SQL segments, each segment is a dictionary
        
        Raises:
            ValueError: Exception thrown when SQL parsing fails
        """
        # Use ANTLR parser to parse SQL statement
        root_node, line, col, msg = parse_tree(self.src_sql, self.src_dialect)
        if root_node is None:
            # Throw exception when parsing fails
            raise ValueError(f"Parse error when executing ANTLR parser of {self.src_dialect}.\n"
                             f"The sql is {self.src_sql}")

        # Get all SQL segments
        all_pieces, root_node = get_all_piece(root_node, self.src_kb_name, self.src_dialect)
        all_pieces = [piece for piece in all_pieces if piece["Type"] != "type"]

        # Check if root node is already in segment list
        flag = True
        for piece in all_pieces:
            if root_node == piece['Node']:
                flag = False
                break

        # If root node is not in segment list, create root segment and add to list
        if flag:
            # Create root segment dictionary
            root_piece = {
                "Node": root_node,  # Syntax tree node
                "Tree": root_node,  # Complete syntax tree
                "Description": "The whole SQL snippet above.",
                "Keyword": '',  # Keyword (empty for root node)
                "SubPieces": [piece for piece in all_pieces],  # List of sub-segments
                "FatherPiece": None,  # Parent segment (none for root node)
                "Count": 0,  # Processing counter
                'TrackPieces': [],  # Tracking segment list
                "Type": None,
                "Detail": None
            }

            # Update all segments without parent segment, set their parent to root segment
            for piece in all_pieces:
                if piece['FatherPiece'] is None:
                    piece['FatherPiece'] = root_piece

            # Add root segment to segment list
            all_pieces.append(root_piece)

        return root_node, all_pieces

    def get_restore_piece_flag(self, assist_info, piece, last_time_piece, ori_piece):
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

    def get_document_description(self, piece):
        """Get related document description for SQL segment
        
        This method retrieves reference documents related to current SQL segment through vector search.
        
        Args:
            piece: SQL segment dictionary containing keyword and description information
        
        Returns:
            str: Document description in JSON format
        """
        # Collect keywords and descriptions from source SQL segment
        src_key = [str(piece['Keyword'])]
        src_detail = [{"Description": piece['Description'], "Type": piece['Type'], "Detail": piece['Detail']}]
        # Collect keywords and descriptions from sub-segments
        for sub_piece in piece['SubPieces']:
            if sub_piece['Description'] is not None and sub_piece['Keyword'] is not None \
                    and sub_piece['Keyword'] not in src_key:
                src_key.append(sub_piece['Keyword'])
                src_detail.append({"Description": sub_piece['Description'],
                                   "Type": sub_piece['Type'],
                                   "Detail": sub_piece['Detail']})

        # Store retrieved document information
        document = list()

        # Process each keyword and description pair
        for key, detail in zip(src_key, src_detail):
            # desc = detail['Description']
            desc = f"{key}--separator--{detail['Detail']}{detail['Description']}"

            # Skip invalid or root node descriptions
            if desc is None or desc == "The whole SQL snippet above.":
                continue

            # Store search results
            results = list()
            if self.model_name == "cross-lingual":
                # Cross-lingual model: use combination of keyword and description for search
                query_embedding = asyncio.run(get_embeddings(
                    str(key) + '--separator--' + str(desc),
                    self.tgt_embedding_model_name
                ))
                results.extend([ite['content'] for ite in
                                self.vector_db.search(self.tgt_kb_name, query_embedding.tolist(),
                                                      content_type="function", top_k=self.top_k)])
            else:
                # Regular model: use only description for search
                query_embedding = asyncio.run(get_embeddings(
                    desc,
                    self.tgt_embedding_model_name
                ))
                topk_result = [ite for ite in
                               self.vector_db.search(self.tgt_kb_name, query_embedding.tolist(),
                                                     content_type=detail['Type'], top_k=self.top_k)]
                results.extend(topk_result)

            # Deduplication: ensure each keyword appears only once
            results_key, results_pre = set(), list()
            for ite in results:
                ite = eval(json.loads(ite["metadata"]['content']))
                if ite["keyword"] not in results_key:
                    results_key.add(ite["keyword"])
                    results_pre.append(f"{ite['description']}{ite['detail']}")
            # results_pre = results

            # Process target keywords: remove extra separators
            # tgt_key = [re.sub(r'(<sep>)(\1){2,}', r'\1', ite.metadata["KEYWORD"]) for ite in results_pre]
            # tgt_key = [re.sub(r'(<sep>)(\1){2,}', r'\1', ite) for ite in results_pre]
            tgt_key = results_key
            tgt_desc = results_pre

            # Build document description
            document.append({
                # Source dialect segment description
                f"{DIALECT_MAP[self.src_dialect]} snippet": (
                    f"`{key}`: {desc.split('--separator--')[-1][:CHUNK_SIZE]}..."
                ),
                # Target dialect segment description
                f"{DIALECT_MAP[self.tgt_dialect]} snippet": [
                    f"`{tk}`: {tdesc[:CHUNK_SIZE]}" for tk, tdesc in zip(tgt_key, tgt_desc)
                ]
            })

        # Convert to formatted JSON string
        document = json.dumps(document, indent=4)

        return document

    def update_error_info_list(self, err_info_list, assist_info, piece):
        """Update error information list
        
        This method processes error information according to different target database dialects and updates the error information list.
        
        Args:
            err_info_list: Existing error information list
            assist_info: Assistance information (error message)
            piece: SQL segment dictionary
        
        Returns:
            list: Updated error information list
        """
        # Special error handling for Oracle database
        if self.tgt_dialect == "oracle":
            # Initialize error information prefix
            assist_info_pre = f"Some error occurs near the snippet:"

            try:
                # Handle Oracle specific errors
                # Skip 'ORA-00933' error (SQL command not properly ended), handle other ERROR information
                if 'ORA-00933: SQL command not properly ended' not in assist_info \
                        and 'ERROR' in assist_info:
                    # Locate ERROR keyword position
                    err_pos = assist_info.index("ERROR")
                    # Add information after error position
                    assist_info_pre += assist_info[err_pos:]

                # Process error message format
                assist_info_pre = process_err_msg(assist_info_pre)

                # Add to error information list
                err_info_list.append({
                    "Error": assist_info_pre,  # Processed error information
                    "SQL Snippet": str(piece["Node"])  # Related SQL segment
                })

            except Exception as e:
                # Exception handling: log exception and add basic error information
                traceback.print_exc()
                assist_info_pre = process_err_msg(assist_info_pre)
                err_info_list.append({
                    "Error": assist_info_pre,
                    "SQL Snippet": str(piece["Node"])
                })
        else:
            # Error handling for non-Oracle databases
            # Directly process error message and add to list
            assist_info = process_err_msg(assist_info)
            err_info_list.append({
                "Error": assist_info,
                "SQL Snippet": str(piece["Node"])
            })

        return err_info_list

    def do_semantic_validation(self, src_sql, current_sql, root_node,
                               all_pieces, last_time_piece, model_ans_list):
        """Process syntactically correct SQL segments
        
        This method processes SQL segments that have passed syntax check, determining whether further optimization or modification is needed.
        
        Args:
            src_sql: Original SQL statement
            current_sql: Currently converted SQL statement
            root_node: Root node of SQL syntax tree
            all_pieces: List of all SQL segments
            last_time_piece: Last processed segment
            model_ans_list: Model answer history list
        
        Returns:
            tuple: (piece, assist_info, judge_raw)
                - piece: SQL segment that needs further processing
                - assist_info: Assistance information
                - judge_raw: Raw output of model judgment
        """
        # Initialize history and prompt information
        history, sys_prompt, user_prompt = list(), None, None

        # If model answer history exists
        if len(model_ans_list) > 0:
            # Find the most recent answer containing system prompt
            no = -1
            for i in range(len(model_ans_list) - 1, 0, -1):
                if "SYSTEM_PROMPT" in model_ans_list[i].keys():
                    no = i
                    break

            # Copy model message to avoid modifying original data
            model_message = copy.deepcopy(model_ans_list[no])

            # Remove action marker
            model_message.pop("Action")

            # Extract system prompt and user prompt
            sys_prompt = None
            if "SYSTEM_PROMPT" in model_message.keys():
                sys_prompt = model_message.pop("SYSTEM_PROMPT")
                user_prompt = model_message.pop("USER_PROMPT")

            # Build dialog history
            history.append({
                "role": "user",
                "content": user_prompt
            })
            history.append(model_message)

            # Build new user prompt for reflection and evaluation of current conversion result
            user_prompt = USER_PROMPT_REFLECT.format(
                src_dialect=DIALECT_MAP[self.src_dialect],
                tgt_dialect=DIALECT_MAP[self.tgt_dialect],
                src_sql=src_sql,
                tgt_sql=current_sql,
                snippet=f"`{str(last_time_piece['Node'])}`"
            ).strip("\n")

        # Call model for judgment
        piece, assist_info, judge_raw = self.model_judge(
            root_node,  # Root node of SQL syntax tree
            all_pieces,  # List of all SQL segments
            src_sql,  # Source SQL
            current_sql,  # Current SQL
            last_time_piece,  # Last processed segment
            history,  # Dialog history
            sys_prompt,  # System prompt
            user_prompt  # User prompt
        )

        return piece, assist_info, judge_raw

    def model_judge(self, root_node, all_pieces, src_sql, current_sql, ans_slice,
                    history=list(), sys_prompt=None, user_prompt=None):
        """Model judgment method
        
        Args:
            root_node: Root node of SQL syntax tree
            all_pieces: List of all SQL segments
            src_sql: Source SQL
            current_sql: Current SQL
            ans_slice: Answer slice
            history: Conversation history
            sys_prompt: System prompt
            user_prompt: User prompt
            
        Returns:
            Piece to be processed, assistance information, and judgment result
        """
        # Determine the fragment to analyze
        if ans_slice is None:
            snippet = "all snippets"  # Analyze all segments
        else:
            snippet = f"`{str(ans_slice['Node'])}`"  # Analyze specific segment

        # If system prompt is not provided, use default judgment prompt template
        if sys_prompt is None:
            sys_prompt = SYSTEM_PROMPT_JUDGE.format(
                src_dialect=self.src_dialect,
                tgt_dialect=self.tgt_dialect
            ).strip("\n")
        
        # If no user prompt provided, generate one
        if user_prompt is None:
            # Format user prompt
            user_prompt = USER_PROMPT_JUDGE.format(
                src_dialect=self.src_dialect,
                tgt_dialect=self.tgt_dialect,
                src_sql=src_sql,
                tgt_sql=current_sql,
                snippet=snippet
            ).strip("\n")

        # Call translator to get model judgment result
        self.add_process(content=process_history_text(user_prompt, role="user", action="judge"),
                         step_name="Rewrite result", sql=current_sql, role="user", is_success=True, error=None)

        answer_raw = self.translator.trans_func(history, sys_prompt, user_prompt)

        # Use regular expression to parse model answer
        pattern = JUDGE_ANSWER_PATTERN
        res = self.translator.parse_llm_answer(answer_raw["content"], pattern)
        self.add_process(content=process_history_text(answer_raw["content"], role="assistant", action="judge"),
                         step_name="Rewrite result", sql=res["Answer"], role="assistant", is_success=True, error=None)

        snippet = res["Answer"]

        # Add additional information to answer
        answer_raw["Action"] = "judge"  # Action type
        answer_raw["Time"] = str(datetime.now())  # Execution time
        answer_raw["SYSTEM_PROMPT"] = sys_prompt  # System prompt
        answer_raw["USER_PROMPT"] = user_prompt  # User prompt

        # Initialize return values
        piece, assist_info = None, None

        # Determine if further processing is needed
        # When the model believes no modification is needed or the confidence is low, return directly
        if "NONE" in snippet.upper() or "almost equivalent" in str(answer_raw) \
                or (isinstance(res['Confidence'], float) and res['Confidence'] < 0.8):
            return piece, assist_info, answer_raw

        # Build auxiliary information, including the fragment to check and the model's reasoning process
        assist_info = JUDGE_INFO_PROMPT.format(snippet=snippet, reasoning=res['Reasoning'])

        # Locate the fragment to process in the current SQL
        column = current_sql.find(snippet)
        if column != -1:
            # Find the corresponding syntax tree node
            node, _ = TreeNode.locate_node(root_node, column, current_sql)
            # Find the corresponding fragment in all segments
            piece = find_piece(all_pieces, node)

        return piece, assist_info, answer_raw

    def rule_rewrite(self, src_sql, src_dialect, tgt_dialect):
        try:
            if src_dialect == "postgresql":
                src_dialect = "postgres"
            if tgt_dialect == "postgresql":
                tgt_dialect = "postgres"
            tgt_sql = sqlglot.transpile(src_sql, read=src_dialect, write=tgt_dialect)[0]
            return tgt_sql

        except Exception as e:
            traceback.print_exc()
            return src_sql

    def direct_rewrite(self):
        translator = LLMTranslator(self.model_name)
        history, model_ans_list = list(), list()

        sys_prompt = SYSTEM_PROMPT_NA.format(
            src_dialect=DIALECT_MAP[self.src_dialect],
            tgt_dialect=DIALECT_MAP[self.tgt_dialect]
        ).strip("\n")
        user_prompt = USER_PROMPT_NA.format(src_dialect=DIALECT_MAP[self.src_dialect],
                                            tgt_dialect=DIALECT_MAP[self.tgt_dialect], sql=self.src_sql).strip("\n")

        answer = translator.trans_func(history, sys_prompt, user_prompt)
        current_sql = answer["Answer"]
        answer_raw = {}
        answer_raw["Action"] = "translate"
        answer_raw["Time"] = str(datetime.now())
        answer_raw["SYSTEM_PROMPT"] = sys_prompt
        answer_raw["USER_PROMPT"] = user_prompt

        model_ans_list.append(answer_raw)

        self.add_process(content="SQL rewrite completed", step_name="Rewrite result", sql=current_sql,
                         role="assistant", is_success=True, error=None)

        return current_sql, model_ans_list

    def init_out_file(self):
        res_data = {
            "info":                    {
                "src_dialect": self.src_dialect,
                "tgt_dialect": self.tgt_dialect,
                "src_sql": self.src_sql,
                "model_name": self.model_name,
                "vector_config": self.vector_config,
                "tgt_db_config": self.tgt_db_config,
            },
            "process_data": []
        }
        with open(self.out_file, "w") as wf:
            json.dump(res_data, wf, indent=4)

    def add_process(self, content, step_name, sql, role, is_success, error):
        if self.out_type == "file":
            # Add rewrite result record to file
            with open(self.out_file, "r") as rf:
                res_data = json.load(rf)
            res_data["process_data"].append({
                "role": role, "sql": sql, "content": content,
                "step_name": step_name, "is_success": is_success,
                "error": error
            })
            with open(self.out_file, "w") as wf:
                json.dump(res_data, wf, indent=4)

        elif self.out_type == "db":
            # Add rewrite result record to database
            from api.services.rewrite import RewriteService
            if self.history_id is not None:
                RewriteService.add_rewrite_process(
                    history_id=self.history_id,
                    content=content,
                    step_name=step_name,
                    sql=sql,
                    role=role,
                    is_success=is_success,
                    error=error
                )

    def update_rewrite_status(self, status, sql, error):
        """Update SQL rewrite status
        
        This method is used to update the status information of the SQL rewrite task in the database.
        
        Args:
            status: The status of the rewrite task
                Possible values include:
                - 'success': Rewrite successful
                - 'failed': Rewrite failed
                - 'processing': Processing
            sql: The rewritten SQL statement or intermediate result
            error: Error information (if any)
        
        Note:
            This method depends on the RewriteService service class to actually execute the database update operation.
        """
        # Import RewriteService service class
        from api.services.rewrite import RewriteService

        # Call the update method of the service class
        RewriteService.update_rewrite_status(
            history_id=self.history_id,  # History record ID
            status=status,  # Rewrite status
            sql=sql,  # SQL statement
            error=error  # Error information
        )


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='Run Local to Global Dialect Translation.')

    
    parser.add_argument('--src_dialect', type=str,
                        help='Source database dialect', choices=DIALECT_LIST)
    parser.add_argument('--tgt_dialect', type=str,
                        help='Target database dialect', choices=DIALECT_LIST)
    parser.add_argument('--src_sql', type=str,
                        help='Source SQL to be translated or file including multiple Source SQLs')

    parser.add_argument('--src_kb_name', type=str,
                        help='Source specification base or its file path')
    parser.add_argument('--tgt_kb_name', type=str,
                        help='Target specification base or its file path')

    parser.add_argument('--llm_model_name', type=str,
                        help='LLM for dialect translation')

    parser.add_argument('--retrieval_on', action='store_true',
                        help='Employ specification retrieval for dialect translation')
    parser.add_argument('--top_k', type=int, default=3,
                        help='Number of retrieved specification')
    parser.add_argument('--max_retry_time', type=int, default=2,
                        help='Maximal translation attempts for one segment')

    parser.add_argument('--out_dir', type=str,
                        help='Output directory to dump translation result')


    return parser.parse_args()



def main():
    args = parse_args()

    translated_sql_total, model_ans_list_total = list(), list()
    used_pieces_total, lift_histories_total = list(), list()

    app = create_app(config_name='PRODUCTION')
    with app.app_context():
        tgt_db = DatabaseConfig.query.get(1)

        tgt_db_config = {
            "host": tgt_db.host,
            "port": tgt_db.port,
            "user": tgt_db.username,
            "password": tgt_db.password,
            "db_name": tgt_db.database
        }
        vector_config = {
            "src_kb_name": args.src_kb_name,
            "tgt_kb_name": args.tgt_kb_name
        }

        if os.path.isfile(args.src_sql):
            with open(args.src_sql, "r") as rf:
                sql_list = rf.readlines()
        else:
            sql_list = [args.src_sql]

        for no, src_sql in tqdm(enumerate(sql_list)):
            translator = Translator(model_name=args.llm_model_name, src_sql=src_sql,
                                    src_dialect=args.src_dialect, tgt_dialect=args.tgt_dialect,
                                    tgt_db_config=tgt_db_config, vector_config=vector_config,
                                    history_id=None, out_type="file", out_dir=args.out_dir,
                                    retrieval_on=args.retrieval_on, top_k=args.top_k)

            translated_sql, model_ans_list, \
            used_pieces, lift_histories = translator.local_to_global_rewrite(max_retry_time=args.max_retry_time)

            translated_sql_total.append(translated_sql)
            with open(os.path.join(args.out_dir, "translated_sql_total.json"), "w") as wf:
                json.dump(translated_sql_total, wf, indent=4)

            model_ans_list_total.append(model_ans_list)
            with open(os.path.join(args.out_dir, "model_ans_list_total.json"), "w") as wf:
                json.dump(model_ans_list_total, wf, indent=4)

            used_pieces_total.append(used_pieces)
            with open(os.path.join(args.out_dir, "used_pieces_total.json"), "w") as wf:
                json.dump(used_pieces_total, wf, indent=4)

            lift_histories_total.append(lift_histories)
            with open(os.path.join(args.out_dir, "lift_histories_total.json"), "w") as wf:
                json.dump(lift_histories_total, wf, indent=4)

            print(f"The translated SQL is: {translated_sql}")
            print(model_ans_list)


if __name__ == "__main__":
    main()
