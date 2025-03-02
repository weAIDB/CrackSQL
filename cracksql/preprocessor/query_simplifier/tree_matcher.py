from cracksql.preprocessor.query_simplifier.Tree import *


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


def check_for_root_node(root_node: TreeNode, keyword_seq: str, keyword_tree_root: TreeNode, dialect):
    if root_node.value.lower() != keyword_tree_root.value.lower():
        return False
    return dual_dfs_on_tree(root_node, keyword_tree_root)
