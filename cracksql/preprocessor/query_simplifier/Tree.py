import logging
import sys

from antlr4.tree.Tree import TerminalNodeImpl

from cracksql.utils.tools import self_split, remove_all_space
from cracksql.preprocessor.antlr_parser.parse_tree import get_parser

parser_map = {}


class TreeNode:
    def __init__(self, value: str, dialect: str, is_terminal: bool, father=None,
                 father_child_index=None, children=None, model_get=False):
        """
        Initialize a multi-tree node
        :param value: the node representation in the ANTLR grammar
        :param father_child_index: index in the child array of the parent node
        :param father: the parent node
        :param children: the child node list (empty list by default)
        """
        self.value = value.strip()
        self.children = children if children is not None else []
        self.child_link = {}
        self.father = father
        self.father_child_index = father_child_index
        self.link = None
        self.father_link = {}
        self.dialect = dialect
        self.is_terminal = is_terminal
        self.model_get = model_get

    def to_tree_rep(self):
        if len(self.children) != 0:
            res = '(' + self.value
            for child in self.children:
                res = res + " " + str(child.to_tree_rep())
            res = res + ")"
        else:
            return self.value
        return res

    def __str__(self):
        if self.value == '<EOF>':
            return ''
        res = ''
        flag = False
        flag_paren = True
        if self.is_terminal:
            res = self.value
            return res
        if self.dialect == 'mysql':
            if self.value in ['comparisonOperator', 'logicalOperator', 'bitOperator', 'multOperator', 'jsonOperator']:
                for child in self.children:
                    sub_str = str(child)
                    res = res + sub_str.strip()
                return res
            if (self.value == 'functionCall' and len(self.children) != 0
                    and (self.children[0].value == 'scalarFunctionName' or self.children[0].value == 'fullId')):
                flag_paren = False
            elif (self.value == 'specificFunction' or self.value == 'passwordFunctionClause' or
                  self.value == 'aggregateWindowedFunction' or self.value == 'nonAggregateWindowedFunction'):
                flag_paren = False
            if not flag_paren:
                for child in self.children:
                    if child.is_terminal and child.value == '(':
                        res = res + child.value
                        flag = True
                    else:
                        sub_str = str(child)
                        if sub_str.startswith('.') or res.endswith('.'):
                            flag = False
                        if sub_str != '':
                            if flag:
                                res = res + " " + sub_str.strip()
                            else:
                                res = res + sub_str
                                flag = True
                return res
        elif self.dialect == 'pg':
            if ((self.value == 'func_application' or self.value == 'func_expr_common_subexpr')
                    and len(self.children) != 0):
                flag_paren = False
            if not flag_paren:
                for child in self.children:
                    if child.is_terminal and child.value == '(':
                        res = res + child.value
                        flag = True
                    else:
                        sub_str = str(child)
                        if sub_str.startswith('.') or res.endswith('.'):
                            flag = False
                        if sub_str != '':
                            if flag:
                                res = res + " " + sub_str.strip()
                            else:
                                res = res + sub_str
                                flag = True
                return res
        elif self.dialect == 'oracle':
            if self.value in ['relational_operator']:
                for child in self.children:
                    sub_str = str(child)
                    res = res + sub_str.strip()
                return res
            if (self.value == 'string_function' or self.value == 'json_function'
                    or self.value == 'other_function' or self.value == 'numeric_function'):
                flag_paren = False
            if not flag_paren:
                for child in self.children:
                    if child.is_terminal and child.value == '(':
                        res = res + child.value
                        flag = True
                    else:
                        sub_str = str(child)
                        if sub_str.startswith('.') or res.endswith('.'):
                            flag = False
                        if sub_str != '':
                            if flag:
                                res = res + " " + sub_str.strip()
                            else:
                                res = res + sub_str
                                flag = True
                return res
            for child in self.children:
                sub_str = str(child)
                if sub_str.startswith('.'):
                    flag = False
                if sub_str != '':
                    if (flag and not res.endswith('.')
                            and not child.value == 'function_argument'
                            and not child.value == 'function_argument_analytic'
                            and not child.value == 'function_argument_modeling'):
                        res = res + " " + sub_str.strip()
                    else:
                        res = res + sub_str
                        flag = True
            return res
        for child in self.children:
            sub_str = str(child)
            if sub_str.startswith('.'):
                flag = False
            if sub_str != '':
                if flag and not res.endswith('.'):
                    res = res + " " + sub_str.strip()
                else:
                    res = res + sub_str
                    flag = True
        return res

    def add_child(self, node):
        self.children.append(node)
        node.father = self

    def replace_child(self, ori_child, new_child):
        i = 0
        while i < len(self.children):
            if self.children[i] == ori_child:
                self.children[i] = new_child
                new_child.father = self
                return
            i = i + 1
        assert False

    @staticmethod
    def make_g4_tree_by_node(antlr_node, dialect: str):
        if dialect in parser_map:
            parser = parser_map[dialect]
        else:
            parser = get_parser(dialect)
            parser_map[dialect] = parser
        if isinstance(antlr_node, TerminalNodeImpl):
            if antlr_node.getText() == '<EOF>':
                return None
            return TreeNode(antlr_node.getText(), dialect, True)
        else:
            if antlr_node.children is not None:
                node = TreeNode(parser.ruleNames[antlr_node.getRuleIndex()], dialect, False)
                for child in antlr_node.children:
                    child_node = TreeNode.make_g4_tree_by_node(child, dialect)
                    if child_node is not None:
                        node.add_child(child_node)
            else:
                return None
        return node

    @staticmethod
    def make_g4_tree(str_tree: str, dialect: str):
        node_stack = []
        used_words = self_split(str_tree)
        i = 0
        while i < len(used_words):
            if used_words[i][0] == '(':
                if len(used_words[i]) == 1:
                    cur_node = TreeNode(used_words[i], dialect, True, node_stack[len(node_stack) - 1],
                                        len(node_stack[len(node_stack) - 1].children))
                    node_stack[len(node_stack) - 1].add_child(cur_node)
                else:
                    node_name = used_words[i][1:]
                    if len(node_stack) == 0:
                        res = TreeNode(node_name, dialect, False)
                        node_stack.append(res)
                    else:
                        cur_node = TreeNode(node_name, dialect, False, node_stack[len(node_stack) - 1],
                                            len(node_stack[len(node_stack) - 1].children))
                        node_stack[len(node_stack) - 1].add_child(cur_node)
                        node_stack.append(cur_node)
            elif used_words[i][len(used_words[i]) - 1] == ')':
                if used_words[i][0] == ')':
                    cur_node = TreeNode(used_words[i][0], dialect, True, node_stack[len(node_stack) - 1],
                                        len(node_stack[len(node_stack) - 1].children))
                    node_stack[len(node_stack) - 1].add_child(cur_node)
                    cnt = len(used_words[i]) - 1
                else:
                    cnt = 0
                    final_index = len(used_words[i]) - 1
                    while used_words[i][final_index] == ')' and final_index > -1:
                        final_index = final_index - 1
                        cnt = cnt + 1
                    if final_index != -1:
                        final_index = final_index + 1
                        node_name = used_words[i][0: final_index]
                        cur_node = TreeNode(node_name, dialect, True, node_stack[len(node_stack) - 1],
                                            len(node_stack[len(node_stack) - 1].children))
                        node_stack[len(node_stack) - 1].add_child(cur_node)
                for j in range(cnt):
                    node_stack.pop()
            else:
                cur_node = TreeNode(used_words[i], dialect, True, node_stack[len(node_stack) - 1],
                                    len(node_stack[len(node_stack) - 1].children))
                node_stack[len(node_stack) - 1].add_child(cur_node)
            i = i + 1
        if len(node_stack) != 0:
            logging.error("error when parse to antlr Tree", file=sys.stderr)
        TreeNode.clean_node(res, res.dialect)
        return res

    @staticmethod
    def clean_node(root_node, dialect: str):
        for child in root_node.children:
            TreeNode.clean_node(child, dialect)
        i = len(root_node.children) - 1
        while i >= 0:
            if len(root_node.children[i].children) == 0 and not root_node.children[i].is_terminal:
                root_node.children.pop(i)
            i = i - 1

    @staticmethod
    def locate_node_exec(root_node, column: int, ori_sql: str, now_str: str):
        cur_str = now_str
        if len(root_node.children) != 0:
            for child in root_node.children:
                node, cur_str = TreeNode.locate_node_exec(child, column, ori_sql, cur_str)
                if node is not None:
                    return node, cur_str
            return None, cur_str
        elif not root_node.is_terminal:
            return None, now_str
        else:
            i = len(now_str)
            while ori_sql[i] == ' ':
                i = i + 1
            j, k = 0, 0
            while j < len(root_node.value):
                while (root_node.value[j] == ' '
                       or root_node.value[j] == '\n' or root_node.value[j] == '\t'):
                    j = j + 1
                while (ori_sql[i + k] == ' '
                       or ori_sql[i + k] == '\n' or ori_sql[i + k] == '\t'):
                    k = k + 1
                assert root_node.value[j] == ori_sql[i + k]
                j = j + 1
                k = k + 1
            if i <= column < i + j:
                return root_node, ori_sql[:i + j]
            else:
                return None, ori_sql[:i + j]

    def clone(self):
        new_node = TreeNode(self.value, self.dialect, self.is_terminal)
        new_node.model_get = self.model_get
        for child in self.children:
            new_node.add_child(child.clone())
        return new_node

    @staticmethod
    def locate_node(root_node, column: int, ori_sql: str):
        node_str = str(root_node)
        node_res = ''
        for split_piece in node_str.split():
            node_res = node_res + split_piece
        ori_res = ''
        for split_piece in ori_sql.split():
            ori_res = ori_res + split_piece
        assert ori_res == node_res
        return TreeNode.locate_node_exec(root_node, column, ori_sql, '')

    @staticmethod
    def no_space_loc(root_node, column: int, ori_sql: str, now_str: str):
        cur_str = now_str
        if len(root_node.children) != 0:
            for child in root_node.children:
                node, cur_str = TreeNode.no_space_loc(child, column, ori_sql, cur_str)
                if node is not None:
                    return node, cur_str
            return None, cur_str
        elif not root_node.is_terminal:
            return None, now_str
        else:
            i = len(now_str)
            j = 0
            node_value = remove_all_space(root_node.value)
            while j < len(node_value):
                assert node_value[j] == ori_sql[i + j]
                j = j + 1
            if i <= column < i + j:
                return root_node, ori_sql[:i + j]
            else:
                return None, ori_sql[:i + j]


def merge_tree(sub_tree_node: TreeNode, father_tree_node: TreeNode,
               rel_father_tree_node: TreeNode, start_index_i=0, start_index_j=-1):
    i = start_index_i
    j = start_index_j
    while i < len(rel_father_tree_node.children):
        if (j + 1 < len(father_tree_node.children) and
                rel_father_tree_node.children[i].value == father_tree_node.children[j + 1].value):
            j = j + 1
        if sub_tree_node.value == rel_father_tree_node.children[i].value:
            break
        i = i + 1
    if (j <= len(father_tree_node.children) - 1 and
            sub_tree_node.value == father_tree_node.children[j].value):
        i1 = 0
        j1 = -1
        for child in sub_tree_node.children:
            # child node also need to combine
            i1, j1 = merge_tree(child, father_tree_node.children[j],
                                rel_father_tree_node.children[i], i1, j1)
    else:
        father_tree_node.children.insert(j, sub_tree_node)
        sub_tree_node.father = father_tree_node
    return i + 1, j + 1


def lift_node(node, all_pieces, tree_node, piece):
    node = node.father
    flag = False
    terminate_flag = False
    for enum_piece in all_pieces:
        if node == enum_piece['Node']:
            enum_piece['TrackPieces'].append(piece)
            piece = enum_piece
            flag = True
            break
    if not flag:
        new_node = TreeNode(node.value, node.dialect, False)
        new_node.add_child(tree_node)
        tree_node = new_node
    else:
        if piece['Tree'] is None:
            return True, node, None, piece
        merge_tree(tree_node, piece['Tree'], node)
        tree_node = piece['Tree']
        terminate_flag = True
    if node.father is None or len(node.children) > 1:
        terminate_flag = True
    return terminate_flag, node, tree_node, piece
