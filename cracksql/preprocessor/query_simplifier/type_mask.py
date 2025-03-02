from typing import Dict

from cracksql.preprocessor.query_simplifier.Tree import TreeNode
from cracksql.preprocessor.query_simplifier.normalize import father_value_list_compare


def mask_column(root_node: TreeNode, ori_node: TreeNode,
                src_dialect: str, tgt_dialect: str, index: int) -> tuple[Dict, int]:
    flag = False
    if src_dialect == 'oracle':
        if root_node.value == 'general_element':
            flag = True
    elif src_dialect == 'mysql':
        if root_node.value == 'fullColumnName' or (root_node.value == 'stringLiteral' and str(root_node).startswith('"')
                                                   and father_value_list_compare(ori_node,
                                                                                 ['constant', 'expressionAtom'])):
            flag = True
    elif src_dialect == 'pg':
        if root_node.value == 'columnref':
            flag = True
    else:
        raise ValueError("the type input of function mask_column is wrong")
    if flag:
        ori_str = str(root_node)
        root_node.value = f"column_{index}"
        root_node.is_terminal = True
        return {f"column_{index}": ori_str}, index + 1
    res = {}
    for i in range(len(root_node.children)):
        rep_map, index = mask_column(root_node.children[i], ori_node.children[i], src_dialect, tgt_dialect, index)
        if len(rep_map) > 0:
            res = {**res, **rep_map}
    return res, index


def mask_table(root_node: TreeNode, ori_node: TreeNode,
               src_dialect: str, tgt_dialect: str, index: int) -> tuple[Dict, int]:
    flag = False
    if src_dialect == 'oracle':
        if root_node.value == 'tableview_name':
            flag = True
    elif src_dialect == 'mysql':
        if root_node.value == "tableName":
            flag = True
    elif src_dialect == 'pg':
        if root_node.value == 'qualified_name' and father_value_list_compare(ori_node, ['relation_expr', 'table_ref']):
            flag = True
    else:
        raise ValueError("the type input of function mask_table is wrong")
    if flag:
        ori_str = str(root_node)
        root_node.value = f"table_{index}"
        root_node.is_terminal = True
        return {f"table_{index}": ori_str}, index + 1
    res = {}
    for i in range(len(root_node.children)):
        rep_map, index = mask_table(root_node.children[i], ori_node.children[i], src_dialect, tgt_dialect, index)
        if len(rep_map) > 0:
            res = {**res, **rep_map}
    return res, index


def mask_sub_query(root_node: TreeNode, ori_node: TreeNode,
                   src_dialect: str, tgt_dialect: str, index: int) -> tuple[Dict, int]:
    flag = False
    if src_dialect == 'oracle':
        if ((root_node.value == 'dml_table_expression_clause' and
             father_value_list_compare(root_node, ['table_ref_aux_internal', 'table_ref_aux'])) or
                (root_node.value == 'query_block' and not father_value_list_compare(ori_node,
                                                                                    ['subquery_basic_elements',
                                                                                     'subquery',
                                                                                     'select_only_statement',
                                                                                     'select_statement',
                                                                                     'data_manipulation_language_statements']))):
            flag = True
    elif src_dialect == 'mysql':
        if (root_node.value == 'selectStatement'
                and root_node.father is not None and (root_node.father.value == 'expressionAtom'
                                                      or root_node.father.value == 'predicate'
                                                      or root_node.father.value == 'tableSourceItem')):
            flag = True
    elif src_dialect == 'pg':
        if (root_node.value == 'select_with_parens' and root_node.father is not None
                and root_node.father.value == 'table_ref'):
            flag = True
    else:
        raise ValueError("the type input of function mask_sub_query is wrong")
    if flag:
        ori_str = str(root_node)
        root_node.value = f"subquery_{index}"
        root_node.is_terminal = True
        return {f"subquery_{index}": ori_str}, index + 1
    res = {}
    for i in range(len(root_node.children)):
        rep_map, index = mask_sub_query(root_node.children[i], ori_node.children[i], src_dialect, tgt_dialect, index)
        if len(rep_map) > 0:
            res = {**res, **rep_map}
    return res, index


def mask_type_node(root_node: TreeNode, src_dialect: str, tgt_dialect: str) -> tuple[str, Dict]:
    clone_node = root_node.clone()
    rep_sub_query_map, _ = mask_sub_query(clone_node, root_node, src_dialect, tgt_dialect, 0)
    rep_column_map, _ = mask_column(clone_node, root_node, src_dialect, tgt_dialect, 0)
    rep_table_map, _ = mask_table(clone_node, root_node, src_dialect, tgt_dialect, 0)
    return str(clone_node), {**rep_column_map, **rep_table_map, **rep_sub_query_map}
