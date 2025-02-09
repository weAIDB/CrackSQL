# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: locate$
# @Author: xxxx
# @Time: 2024/9/25 12:35

import os.path
import re
import sqlglot
import json
from typing import List, Dict

from preprocessor.antlr_parser.parse_tree import parse_tree
from preprocessor.query_simplifier.Tree import TreeNode
from utils.db_connector import sql_execute
from utils.tools import load_config, remove_all_space, print_err, get_proj_root_path, reformat_sql

pg_func_name = set()

config = load_config()
oracle_locate_open = config['oracle_locate_open']


def load_pg_func_name():
    global pg_func_name
    with open(os.path.join(get_proj_root_path(), "data", 'processed_document', 'pg',
                           'pg_1_function_ready.json'), 'r') as file:
        func_array = json.loads(file.read())
        for table in func_array:
            i = 1
            while i < len(table):
                name = table[i]['Function'][:table[i]['Function'].find('(')]
                pg_func_name.add(name.upper())
                i = i + 1


def locate_function(error_info: str, dialect: str, sql: str):
    if dialect == 'mysql':
        if error_info.find('check the manual that corresponds to your MySQL '
                           'server version for the right syntax to use near ') != -1:
            i = 0
            while i < len(error_info):
                if error_info[i:].startswith('check the manual that corresponds to your MySQL '
                                             'server version for the right syntax to use near '):
                    break
                i = i + 1
            i = i + len('check the manual that corresponds to your MySQL '
                        'server version for the right syntax to use near \'')
            j = i
            while j < len(error_info):
                if error_info[j:].startswith("' at line"):
                    break
                j = j + 1
            location = sql.find(error_info[i:j])
            if location == -1:
                raise ValueError("Format for the MySQL sql is needed for space may cause inconsistent")
        else:
            location = None
        pattern = r"Incorrect parameter count in the call to native function '(\w+)'"
        match = re.search(pattern, error_info)
        if match:
            return error_info, match.group(1), location
        else:
            pattern = r"FUNCTION \w+.(\w+) does not exist"
            match = re.search(pattern, error_info)
            if match:
                return error_info, match.group(1), location
            else:
                return error_info, None, location
    elif dialect == 'pg':
        pattern = r"function ([^() ]+)\(.*\) does not exist"
        match = re.search(pattern, error_info)
        err_lines = error_info.split('\n')
        if len(err_lines) > 2:
            pg_location = get_pg_location(err_lines[1], err_lines[2].find('^'), sql)
        else:
            pg_location = None
        if match:
            func_name = match.group(1).strip().upper()
            pg_func_map = {
                "PG_CATALOG.DATE_PART": "EXTRACT"
            }
            if func_name in pg_func_map:
                func_name = pg_func_map[func_name]
            assert err_lines[1].startswith('LINE 1: ')
            if len(pg_func_name) == 0:
                load_pg_func_name()

            return error_info, func_name, pg_location
        else:
            return error_info, None, pg_location
    elif dialect == 'oracle':
        if oracle_locate_open:
            i = 0
            error_lines = error_info.split('\n')
            flag = False
            for i in range(len(error_lines)):
                if error_lines[i].strip().startswith(sql):
                    flag = True
                    break
            msg = ''
            if flag:
                location = get_oracle_location(error_lines[i], error_lines[i + 1].find('*'), sql)
            else:
                pattern1 = r'Bind variable "(.*?)" not declared.'
                match = re.search(pattern1, error_info)
                if match:
                    location = sql.upper().find(match.group(1))
                else:
                    location = None
                if location == -1:
                    location = None
            for j in range(i, len(error_lines)):
                msg = msg + error_lines[j] + '\n'
            # if error_info.find('too many arguments for function') != -1:
            return msg, None, location
        else:
            return error_info, None, None


def find_piece(all_pieces: List[Dict], locate_node: TreeNode):
    # print("locate_node", locate_node)
    now_node = locate_node
    while True:
        for piece in all_pieces:
            if piece['Node'] == now_node:
                return piece
        if now_node.father is not None:
            now_node = now_node.father
        else:
            return None


def get_func_name(func: str):
    if func.find('(') != -1:
        return func[:func.find('(')]
    else:
        return func.lower()


def find_function(func_name, all_pieces, root_node, sql, location=None):
    if location is not None:
        ori_node, _ = TreeNode.locate_node(root_node, location, sql)
        while True:
            for piece in all_pieces:
                sql_slice = str(piece['Node'])
                if piece['Node'] == ori_node and func_name.lower() in sql_slice.lower():
                    return piece
            if ori_node.father is not None:
                ori_node = ori_node.father
            else:
                assert False
    else:
        for piece in all_pieces:
            if piece['Keyword'] is None:
                continue
            if func_name.lower() == get_func_name(piece['Keyword']):
                return piece
        # No piece was found with the false function
        res_piece = None
        min_len = 100000
        for piece in all_pieces:
            sql_slice = str(piece['Node'])
            if func_name.lower() in sql_slice.lower() and len(sql_slice) < min_len:
                res_piece = piece
                min_len = len(sql_slice)
        assert res_piece is not None
        return res_piece


def locate_node_piece(sql, src_dialect, tgt_dialect, all_pieces, root_node, db_name: str):
    flag, error_info = sql_execute(tgt_dialect, db_name, sql)
    if flag:
        return None, "no execute error"
    else:
        error_type, func_name, location = locate_function(error_info, tgt_dialect, sql)
        if func_name is not None:
            piece = find_function(func_name, all_pieces, root_node, sql, location)
            if piece is not None:
                error_type = re.sub(r'\s+', ' ', error_type)
                if "~~" in error_type and "LIKE" not in error_type:
                    error_type = error_type.replace("~~", "LIKE")
                if "~*" in error_type and "ILIKE" not in error_type:
                    error_type = error_type.replace("~*", "ILIKE")
                if "~" in error_type and "LIKE" not in error_type:
                    error_type = error_type.replace("~", "LIKE")
                return piece, error_type
            else:
                return None, f"Function {func_name} translate error"

        elif location is not None:
            node, _ = TreeNode.locate_node(root_node, location, sql)

            error_type = re.sub(r'\s+', ' ', error_type)
            if "~~" in error_type and "LIKE" not in error_type:
                error_type = error_type.replace("~~", "LIKE")
            if "~*" in error_type and "ILIKE" not in error_type:
                error_type = error_type.replace("~*", "ILIKE")
            if "~" in error_type and "LIKE" not in error_type:
                error_type = error_type.replace("~", "LIKE")

            return find_piece(all_pieces, node), error_type

        tree_node, line, column, msg = parse_tree(sql, tgt_dialect)
        if tree_node is not None:
            return None, "no parser error"

        node, _ = TreeNode.locate_node(root_node, column, sql)
        return find_piece(all_pieces, node), msg


def replace_piece(piece, new_piece):
    assert piece['FatherPiece'] == new_piece['FatherPiece']
    father_piece = piece['FatherPiece']
    while father_piece is not None:
        father_piece['SubPieces'].remove(piece)
        father_piece['SubPieces'].append(new_piece)
        for sub_piece in piece['SubPieces']:
            father_piece['SubPieces'].remove(sub_piece)
        for sub_piece in new_piece['SubPieces']:
            father_piece['SubPieces'].append(sub_piece)
        father_piece = father_piece['FatherPiece']


def get_pg_location(line_string: str, col: int, ori_sql: str):
    if line_string.startswith('LINE 1: ...'):
        sub_str = line_string[len('LINE 1: ...'):-3]
        if sub_str.endswith('...'):
            sub_str = sub_str[:-3]
        ori_loc = ori_sql.find(sub_str)
        return ori_loc + col - len('LINE 1: ...')
    elif line_string.startswith('LINE 1: '):
        sub_str = line_string[len('LINE 1: '):]
        ori_loc = ori_sql.find(sub_str)
        return ori_loc + col - len('LINE 1: ') + 1
    else:
        print(line_string)
        return None


def get_oracle_location(line_string: str, col: int, ori_sql: str):
    assert ori_sql[0] != ' ' and ori_sql[0] != '\n'
    i = 0
    while line_string[i] != ori_sql[0]:
        i = i + 1
    res = col - i
    return res


def find_all_subpiece(node, all_pieces, node2piece):
    res = []
    if node in node2piece:
        return node2piece[node]['SubPieces']
    else:
        for child in node.children:
            res = res + find_all_subpiece(child, all_pieces, node2piece)
            if child in node2piece:
                res.append(node2piece[node])
        return res


def find_piece_dfs(node: TreeNode, node_set: set, node2piece: Dict) -> List[Dict]:
    i = 0
    while i < len(node.children):
        if node.children[i] in node_set:
            break
        i = i + 1
    j = len(node.children) - 1
    while j >= 0:
        if node.children[j] in node_set:
            break
        j = j - 1
    if i == len(node.children):
        i = 0
    if j == -1:
        j = len(node.children) - 1
    t = i
    res = []
    while t <= j:
        res = res + find_piece_dfs(node.children[t], node_set, node2piece)
        t = t + 1
    if node in node2piece:
        res.append(node2piece[node])
    return res


def locate_by_segment(ori_sql: str, segment: str, all_pieces: List[Dict], node2piece: Dict, root_node: TreeNode):
    # remove_all_space and then locate
    # need to find the first father node and then have all the desc
    ori_sql_no_space = remove_all_space(ori_sql)
    segment_no_space = remove_all_space(segment)

    assert segment_no_space in ori_sql_no_space
    first_loc = ori_sql_no_space.find(segment_no_space)
    last_loc = first_loc + len(segment_no_space) - 1
    start_node, _ = TreeNode.no_space_loc(root_node, first_loc, ori_sql_no_space, '')
    end_node, _ = TreeNode.no_space_loc(root_node, last_loc, ori_sql_no_space, '')

    node_set = set()

    temp_node = start_node
    while temp_node is not None:
        node_set.add(temp_node)
        temp_node = temp_node.father
    temp_node = end_node
    while temp_node not in node_set:
        node_set.add(temp_node)
        temp_node = temp_node.father
        assert temp_node is not None

    return find_piece_dfs(temp_node, node_set, node2piece)
