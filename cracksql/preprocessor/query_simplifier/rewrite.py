from typing import List, Dict

from cracksql.preprocessor.antlr_parser.parse_tree import parse_tree
from cracksql.preprocessor.query_simplifier.load_process import load_json_keywords
from cracksql.preprocessor.query_simplifier.locate import locate_by_segment
from cracksql.preprocessor.query_simplifier.tree_matcher import *
from cracksql.utils.tools import print_err

rewrite_keyword_map = {}
rewrite_function_map = {}


def function_rewrite(node: TreeNode, src_kb_name: str, src_dialect: str):
    # Considering the written format of function in the antlr grams, 
    # it is needed to check whether there are difference in Function call
    if src_dialect not in rewrite_keyword_map:
        keyword_table_json, function_table_json = load_json_keywords(src_kb_name, src_dialect)
        rewrite_keyword_map[src_dialect] = keyword_table_json
        rewrite_function_map[src_dialect] = function_table_json
    else:
        function_table_json = rewrite_function_map[src_dialect]
    for function in function_table_json:
        if function['tree'] is None:
            continue
        if check_for_root_node(node, function['keyword'], function['tree'], src_dialect):
            return {
                "Node": node,
                "Tree": function['tree'],
                "Description": function['description'],
                "Keyword": function['keyword'],
                "Type": function['type'],
                "Detail": function['detail']
            }
    return None


def keyword_rewrite(node: TreeNode, src_kb_name: str, src_dialect: str):
    # Considering the written format of function in the antlr grams, 
    # it is needed to check whether there are difference in Function call
    if src_dialect not in rewrite_keyword_map:
        keyword_table_json, function_table_json = load_json_keywords(src_kb_name, src_dialect)
        rewrite_keyword_map[src_dialect] = keyword_table_json
        rewrite_function_map[src_dialect] = function_table_json
    else:
        keyword_table_json = rewrite_keyword_map[src_dialect]
    to_pick_up_list = []
    cnt_flag = False
    for keyword_list in keyword_table_json:
        if keyword_list['tree'] is None:
            continue
        try:
            if keyword_list['tree'] == 'Found error' or keyword_list['tree'] == "Parse error":
                continue
        except Exception as e:
            print(str(e))
            print("keyword_list['tree']", keyword_list['tree'])
            print("keyword_list['keyword']", keyword_list['keyword'])
            raise NotImplementedError

        if check_for_root_node(node, keyword_list['keyword'], keyword_list['tree'], src_dialect):
            if 'Count' in keyword_list:
                cnt_flag = True
                to_pick_up_list.append({
                    "Tree": keyword_list['tree'],
                    "Description": keyword_list['description'],
                    "Keyword": keyword_list['keyword'],
                    "Count": keyword_list['Count'],
                    "Type": keyword_list['type'],
                    "Detail": keyword_list['detail']
                })
            else:
                to_pick_up_list.append({
                    "Tree": keyword_list['tree'],
                    "Description": keyword_list['description'],
                    "Keyword": keyword_list['keyword'],
                    "Type": keyword_list['type'],
                    "Detail": keyword_list['detail']
                })
    if cnt_flag:
        sorted(to_pick_up_list, key=lambda x: x["Count"], reverse=True)
    if len(to_pick_up_list) > 0:
        return {
            "Node": node,
            "Tree": to_pick_up_list[0]['Tree'],
            "Description": to_pick_up_list[0]['Description'],
            "Keyword": to_pick_up_list[0]['Keyword'],
            "Type": to_pick_up_list[0]['Type'],
            "Detail": keyword_list['detail']
        }
    return None


def slice_all(node: TreeNode, src_kb_name, src_dialect, only_func) -> List[Dict]:
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
    """
    res = []
    for i in range(len(node.children)):
        child_res = slice_all(node.children[i], src_kb_name, src_dialect, only_func)
        res = res + child_res
    global rewrite_keyword_map
    rewrite_dict = function_rewrite(node, src_kb_name, src_dialect)
    if rewrite_dict is not None:
        res.append(rewrite_dict)
    if not only_func:
        rewrite_dict = keyword_rewrite(node, src_kb_name, src_dialect)
        if rewrite_dict is not None:
            res.append(rewrite_dict)
    return res


def dfs_res(node: TreeNode, node2piece: Dict):
    sub_pieces = []
    for child in node.children:
        if child in node2piece and 'SubPieces' in node2piece[child]:
            sub_pieces = sub_pieces + node2piece[child]['SubPieces'] + [node2piece[child]]
        else:
            sub_pieces = sub_pieces + dfs_res(child, node2piece)
    if node in node2piece:
        node2piece[node]['SubPieces'] = sub_pieces
        return sub_pieces + [node2piece[node]]
    return sub_pieces


def search_upward(piece, node2piece: Dict):
    node = piece['Node']
    while True:
        node = node.father
        if node is None:
            return None
        if node in node2piece:
            return node2piece[node]


# directly slice all the pieces and then sort using the error info
def get_all_piece(tree_node: TreeNode, src_kb_name, src_dialect) -> tuple[List[Dict], TreeNode]:
    root_node = TreeNode.make_g4_tree_by_node(tree_node, src_dialect)
    res = slice_all(root_node, src_kb_name, src_dialect, False)
    node2piece = {}
    for piece in res:
        node2piece[piece['Node']] = piece
    for piece in res:
        if 'SubPieces' not in piece:
            dfs_res(piece['Node'], node2piece)
    for piece in res:
        piece['FatherPiece'] = search_upward(piece, node2piece)
        piece['Count'] = 0
        piece['TrackPieces'] = []
    return res, root_node


def get_all_model_ans_nodes(root_node: TreeNode) -> List[TreeNode]:
    res = []
    for child in root_node.children:
        res = res + get_all_model_ans_nodes(child)
    if root_node.model_get:
        res.append(root_node)
    return res


def get_all_tgt_used_piece(now_sql, tgt_dialect, src_root_node):
    if 'MySQL' in tgt_dialect:
        tgt_dialect = 'mysql'
    elif 'PostgreSQL' in tgt_dialect:
        tgt_dialect = 'pg'
    elif 'Oracle' in tgt_dialect:
        tgt_dialect = 'oracle'
    else:
        raise ValueError(f"{tgt_dialect} is not supported yet")
    try:
        tree_node, line, col, msg = parse_tree(now_sql, tgt_dialect)
        if tree_node is None:
            raise ValueError(f"Parse error when executing ANTLR parser of {tgt_dialect}.\n"
                             f"The sql is {now_sql}")
        tgt_all_pieces, root_node = get_all_piece(tree_node, tgt_dialect)
        model_answer_nodes = get_all_model_ans_nodes(src_root_node)
        pieces = []
        node2piece = {}
        for piece in tgt_all_pieces:
            node2piece[piece['Node']] = piece
        for model_answer_node in model_answer_nodes:
            pieces.append(
                locate_by_segment(now_sql, model_answer_node.value,
                                  tgt_all_pieces, node2piece, root_node)
            )
        return pieces
    except Exception as e:
        if (isinstance(e, ValueError)
                and str(e).startswith('Parse error when executing ANTLR parser of')):
            print_err("No desc can be provided because of Antlr Parse Error")
            return []
        else:
            raise e
