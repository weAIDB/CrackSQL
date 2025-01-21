from typing import List

from CrackSQL.preprocessor.TreeParser.bnf_tree.bnf_tree_node import *
from CrackSQL.utils.tools import self_split, split2wordlist


def parse_bnf(terms: List, node: BnfRuleNode, index: int, index_end: int) -> int:
    i = index
    cur_node = BnfRuleNode('keywords', NodeType.WORDS, RepeatType.NONE, node)
    last_node = None
    while i < index_end:
        temp_str = terms[i].strip()
        if len(temp_str) == 0:
            i = i + 1
            continue
        if temp_str == '{':
            node1 = BnfRuleNode('{}', NodeType.BIG_BRACKET, RepeatType.NONE, cur_node)
            cur_node.add_child(node1)
            left = 1
            temp_index = i + 1
            quote_flag = False
            while left > 0:
                if not quote_flag and terms[temp_index] == '{':
                    left = left + 1
                elif not quote_flag and terms[temp_index] == '}':
                    left = left - 1
                if terms[temp_index] == '\'':
                    quote_flag = not quote_flag
                temp_index = temp_index + 1
            parse_bnf(terms, node1, i + 1, temp_index - 1)
            i = temp_index
            last_node = node1
        elif temp_str == '(':
            node1 = BnfRuleNode('()', NodeType.SM_BRACKET, RepeatType.NONE, cur_node)
            cur_node.add_child(node1)
            left = 1
            temp_index = i + 1
            quote_flag = False
            while left > 0:
                if not quote_flag and terms[temp_index] == '(':
                    left = left + 1
                elif not quote_flag and terms[temp_index] == ')':
                    left = left - 1
                if terms[temp_index] == '\'':
                    quote_flag = not quote_flag
                temp_index = temp_index + 1
            parse_bnf(terms, node1, i + 1, temp_index - 1)
            i = temp_index
            last_node = node1
        elif temp_str == '[':
            node1 = BnfRuleNode('[]', NodeType.MID_BRACKET, RepeatType.NONE, cur_node)
            cur_node.add_child(node1)
            left = 1
            temp_index = i + 1
            quote_flag = False
            while left > 0:
                if not quote_flag and terms[temp_index] == '[':
                    left = left + 1
                elif not quote_flag and terms[temp_index] == ']':
                    left = left - 1
                if terms[temp_index] == '\'':
                    quote_flag = not quote_flag
                temp_index = temp_index + 1
            parse_bnf(terms, node1, i + 1, temp_index - 1)
            i = temp_index
            last_node = node1
        elif temp_str == '|':
            if node.node_type != NodeType.OR:
                if len(cur_node.children) != 0:
                    node.add_child(cur_node)
                    cur_node = BnfRuleNode('keywords', NodeType.WORDS, RepeatType.NONE, node)
                node1 = BnfRuleNode('or', NodeType.OR, RepeatType.NONE, node)
                for child_node in node.children:
                    node1.add_child(child_node)
                node.clear_child()
                node.add_child(node1)
                i = parse_bnf(terms, node1, i + 1, index_end)
            else:
                if len(cur_node.children) != 0:
                    node.add_child(cur_node)
                    cur_node = BnfRuleNode('keywords', NodeType.WORDS, RepeatType.NONE, node)
                i = i + 1
        
        else:
            node1 = BnfRuleNode(temp_str, NodeType.KEYWORD, RepeatType.NONE, node)
            cur_node.add_child(node1)
            last_node = node1
            i = i + 1

    if len(cur_node.children) != 0:
        node.add_child(cur_node)
    return i


def build_bnf_tree(keyword_str: str):
    root_node = BnfRuleNode('', NodeType.ROOT)
    word_list = split2wordlist(self_split(keyword_str))
    parse_bnf(word_list, root_node, 0, len(word_list))
    print(root_node)
    return root_node
