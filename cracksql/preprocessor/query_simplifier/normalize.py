# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: normalize$
# @Author: xxxx
# @Time: 2024/10/6 22:19

from typing import List

from cracksql.preprocessor.antlr_parser.parse_tree import parse_tree
from cracksql.preprocessor.query_simplifier.Tree import TreeNode


def remove_as_mysql(root_node: TreeNode):
    remove_children = []
    if root_node.value in ['tableSourceItem', 'commonTableExpressions', 'selectElement']:
        for child in root_node.children:
            if child.is_terminal and child.value == 'AS':
                remove_children.append(child)
        for child in remove_children:
            root_node.children.remove(child)
    for child in root_node.children:
        if not child.is_terminal:
            remove_as_mysql(child)


def remove_as_pg(root_node: TreeNode):
    remove_children = []
    if root_node.value in ['target_el', 'table_alias_clause']:
        for child in root_node.children:
            if child.is_terminal and child.value == 'AS':
                remove_children.append(child)
        for child in remove_children:
            root_node.children.remove(child)
    for child in root_node.children:
        if not child.is_terminal:
            remove_as_pg(child)


def add_quote_mysql(root_node: TreeNode, quote_type: str):
    if father_value_list_compare(root_node, ['uid', 'tableSourceItem']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['uid', 'fullId']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['stringLiteral', 'constant']):
        add_quote_to_bot_node(root_node, quote_type)
    elif (father_value_list_compare(root_node, ['uid', 'fullColumnName']) and
          not (len(root_node.children) != 0 and root_node.children[0].value == 'scalarFunctionName')):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['uid', 'cteName', 'commonTableExpressions']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['qualified_name', 'relation_expr']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['uid', 'selectElement']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['dottedId', 'fullColumnName']):
        if root_node.is_terminal and not root_node.value == '.':
            assert root_node.value[0] == '.'
            src_str = root_node.value[1:]
            res = add_quote(src_str, quote_type)
            root_node.value = '.' + res
        elif root_node.is_terminal and root_node.value == '.':
            pass
        else:
            assert root_node.value == 'uid'
            add_quote_to_bot_node(root_node, quote_type)
    else:
        for child in root_node.children:
            add_quote_mysql(child, quote_type)


def remove_quote_mysql(root_node: TreeNode):
    if father_value_list_compare(root_node, ['uid', 'tableSourceItem']):
        rm_quote_to_bot_node(root_node, '`')
    elif father_value_list_compare(root_node, ['stringLiteral', 'constant']):
        rm_quote_to_bot_node(root_node, '`')
    elif father_value_list_compare(root_node, ['uid', 'fullId']):
        rm_quote_to_bot_node(root_node, '`')
    elif (father_value_list_compare(root_node, ['uid', 'fullColumnName'])
          and not (len(root_node.children) != 0 and root_node.children[0].value == 'scalarFunctionName')):
        rm_quote_to_bot_node(root_node, '`')
    elif father_value_list_compare(root_node, ['uid', 'cteName', 'commonTableExpressions']):
        rm_quote_to_bot_node(root_node, '`')
    elif father_value_list_compare(root_node, ['uid', 'selectElement']):
        rm_quote_to_bot_node(root_node, '`')
    elif father_value_list_compare(root_node, ['qualified_name', 'relation_expr']):
        rm_quote_to_bot_node(root_node, '`')
    elif father_value_list_compare(root_node, ['dottedId', 'fullColumnName']):
        if root_node.is_terminal and not root_node.value == '.':
            assert root_node.value[0] == '.'
            src_str = root_node.value[1:]
            res = rm_quote(src_str, '`')
            root_node.value = '.' + res
        elif root_node.is_terminal and root_node.value == '.':
            pass
        else:
            assert root_node.value == 'uid'
            rm_quote_to_bot_node(root_node, '`')
    else:
        for child in root_node.children:
            remove_quote_mysql(child)


def child_value_list_compare(root_node: TreeNode, child_list: List[str]) -> bool:
    now_child = root_node
    for child in child_list:
        if len(now_child.children) == 0:
            return False
        now_child = now_child.children[0]
        if isinstance(child, list):
            if now_child.value not in child:
                return False
        else:
            if now_child.value != child:
                return False
    return True


def add_quote_oracle(root_node: TreeNode, quote_type: str):
    if (father_value_list_compare(root_node, ['id_expression', 'general_element_part']) and
            not child_value_list_compare(root_node,
                                         ['non_reserved_keywords_pre12c', ['NULLIF', 'SYSDATE', "ROWNUM", "TRUNC"]])):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['regular_id', 'id_expression', 'identifier',
                                               'tableview_name', 'dml_table_expression_clause',
                                               'table_ref_aux_internal',
                                               'table_ref_aux', 'table_ref']) and not root_node.value == 'dual':
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node,
                                   ['id_expression', 'identifier', 'tableview_name']) and not child_value_list_compare(
            root_node, ['dual']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['id_expression', 'identifier', 'table_alias']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['id_expression', 'identifier', 'query_name']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['id_expression', 'identifier', 'column_alias']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['qualified_name', 'relation_expr']):
        add_quote_to_bot_node(root_node, quote_type)
    else:
        for child in root_node.children:
            add_quote_oracle(child, quote_type)


def father_value_list_compare(root_node: TreeNode, father_list: List[str]) -> bool:
    now_father = root_node.father
    for father in father_list:
        if isinstance(father, list):
            if now_father is None or now_father.value not in father:
                return False
        else:
            if now_father is None or now_father.value != father:
                return False
        now_father = now_father.father
    return True


def add_quote_pg(root_node: TreeNode, quote_type):
    if father_value_list_compare(root_node, ['colid', 'columnref']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['collabel', 'attr_name']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['collabel', 'target_el']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['table_alias']):
        add_quote_to_bot_node(root_node, quote_type)
    elif father_value_list_compare(root_node, ['qualified_name', 'relation_expr']):
        add_quote_to_bot_node(root_node, quote_type)
    else:
        for child in root_node.children:
            add_quote_pg(child, quote_type)


def remove_quote_pg(root_node: TreeNode):
    if father_value_list_compare(root_node, ['colid', 'columnref']):
        rm_quote_to_bot_node(root_node, '"')
    elif father_value_list_compare(root_node, ['collabel', 'attr_name']):
        rm_quote_to_bot_node(root_node, '"')
    elif father_value_list_compare(root_node, ['collabel', 'target_el']):
        rm_quote_to_bot_node(root_node, '"')
    elif father_value_list_compare(root_node, ['table_alias']):
        rm_quote_to_bot_node(root_node, '"')
    elif father_value_list_compare(root_node, ['qualified_name', 'relation_expr']):
        rm_quote_to_bot_node(root_node, '"')
    else:
        for child in root_node.children:
            remove_quote_pg(child)


def rm_quote_to_bot_node(root_node: TreeNode, quote_type: str):
    while not root_node.is_terminal:
        root_node = root_node.children[0]
    root_node.value = rm_quote(root_node.value, quote_type)


def rm_quote(src_str: str, quote_type: str) -> str:
    if src_str.startswith(quote_type):
        assert len(src_str) > 0
        src_str = src_str[1:]
    if src_str.endswith(quote_type):
        src_str = src_str[:-1]
    return src_str


def add_quote(src_str: str, quote_type: str) -> str:
    if src_str.startswith('\''):
        return src_str
    if quote_type == '\"':
        reverse_quote = '`'
    else:
        reverse_quote = '\"'
    res = ''
    if src_str.startswith(reverse_quote):
        assert len(src_str) > 0
        src_str = src_str[1:]
    if src_str.endswith(reverse_quote):
        src_str = src_str[:-1]
    if not src_str.startswith(quote_type):
        res = res + quote_type
    res = res + src_str
    if not src_str.endswith(quote_type):
        res = res + quote_type
    return res


def add_quote_to_bot_node(root_node: TreeNode, quote_type: str):
    while not root_node.is_terminal:
        root_node = root_node.children[0]
    root_node.value = add_quote(root_node.value, quote_type)


def normalize(root_node: TreeNode, src_dialect: str, tgt_dialect: str):
    if tgt_dialect == 'oracle':
        if src_dialect == 'mysql':
            remove_as_mysql(root_node)
            add_quote_mysql(root_node, '\"')
        elif src_dialect == 'pg':
            remove_as_pg(root_node)
            add_quote_pg(root_node, '\"')
        elif src_dialect == 'oracle':
            add_quote_oracle(root_node, '\"')
    elif tgt_dialect == 'mysql':
        if src_dialect == 'oracle':
            add_quote_oracle(root_node, '`')
        elif src_dialect == 'pg':
            add_quote_pg(root_node, '`')
        elif src_dialect == 'mysql':
            add_quote_mysql(root_node, '`')
    elif tgt_dialect == 'pg':
        if src_dialect == 'oracle':
            add_quote_oracle(root_node, '\"')
        elif src_dialect == 'mysql':
            add_quote_mysql(root_node, '\"')
        elif src_dialect == 'pg':
            add_quote_pg(root_node, '\"')


def normalize_sql(sql: str, src_dialect: str, tgt_dialect: str):
    tree_node, _, _, _ = parse_tree(sql, src_dialect)
    if tree_node is not None:
        node = TreeNode.make_g4_tree_by_node(tree_node, src_dialect)
        normalize(node, src_dialect, tgt_dialect)
        return node
    else:
        return None
