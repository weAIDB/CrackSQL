import os
from glob import glob

from doc_process.make_tree import *
from preprocessor.query_simplifier.Tree import *
from preprocessor.antlr_parser.parse_tree import parse_tree

dbg = (load_config())['dbg']


def tree_matcher(src_sql: str, dialect: str):
    script_path = os.path.abspath(__file__)
    retrieve_path = os.path.join(os.path.dirname(os.path.dirname(script_path)), 'RetrievalSource', dialect)
    json_files = glob(os.path.join(retrieve_path, "*.json"))
    for file_path in json_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            keywords_json = json.loads(file.read())
            for keyword_unit in keywords_json:
                for i in range(keyword_unit['Keyword']):
                    keyword_seq = keyword_unit['Keyword'][i]
                    tree_keyword = keyword_unit['Tree'][i]
                    check_keyword(src_sql, keyword_seq, tree_keyword, dialect)


def is_valid_string(s: str) -> bool:
    return all((char == '(' or char == ')' or char == '_'
                or 'A' <= char <= 'Z' or '0' <= char <= '0') for char in s)


def check_keyword(src_sql, keyword_seq: str, keyword_tree_rep: str, dialect: str):
    src_sql_tree_node, line, column, msg = parse_tree(src_sql, dialect)
    if src_sql_tree_node is None:
        return f"parse error at line: {line}, column: {column}, message: {msg}"
    if filter_by_string(keyword_seq, src_sql):
        ans_nodes = filter_on_tree(TreeNode.make_g4_tree_by_node(src_sql_tree_node, dialect),
                                   TreeNode.make_g4_tree(keyword_tree_rep, dialect))
        ans_str = [str(node) for node in ans_nodes]
        return ans_nodes, ans_str


def check_for_root_node(root_node: TreeNode, keyword_seq: str, keyword_tree_root: TreeNode, dialect):
    if root_node.value.lower() != keyword_tree_root.value.lower():
        return False
    return dual_dfs_on_tree(root_node, keyword_tree_root)


def filter_on_tree(src_sql_tree_node: TreeNode, keyword_tree_node: TreeNode):
    return dfs_on_tree(src_sql_tree_node, keyword_tree_node)


def dfs_on_tree(src_sql_tree_node: TreeNode, keyword_tree_node: TreeNode) -> List[TreeNode]:
    res = []
    if src_sql_tree_node.value == keyword_tree_node.value:
        if dual_dfs_on_tree(src_sql_tree_node, keyword_tree_node):
            res.append(src_sql_tree_node)
    for child in src_sql_tree_node.children:
        res = res + dfs_on_tree(child, keyword_tree_node)
    return res


def dual_dfs_on_tree(src_sql_tree_node: TreeNode, keyword_tree_node: TreeNode):
    i = 0
    j = 0
    while i < len(src_sql_tree_node.children) and j < len(keyword_tree_node.children):
        if (src_sql_tree_node.children[i].value.lower() == keyword_tree_node.children[j].value.lower()
                and dual_dfs_on_tree(src_sql_tree_node.children[i], keyword_tree_node.children[j])):
            j = j + 1
        i = i + 1
    if j == len(keyword_tree_node.children):
        return True
    else:
        return False


def filter_by_string(keywords: str, src_sql):
    """use string to check whether the src_sql can contain the keywords_seq first"""
    source_words = keywords.split()
    last_position = -1
    for word in source_words:
        if not is_valid_string(word):
            continue
        position = src_sql.find(word, last_position + 1)
        if position == -1 or position <= last_position:
            return False
        last_position = position
    return True


def check_path(node: TreeNode, path, index: int):
    if dbg:
        print('--')
        print(node.value)
        print(path[index])
        print('--')
    if node.value != path[index]:
        return False
    elif index > len(path) - 1 or (index == len(path) - 1 and node.value == path[index]):
        return True
    else:
        for child in node.children:
            if check_path(child, path, index + 1):
                return True
        return False
