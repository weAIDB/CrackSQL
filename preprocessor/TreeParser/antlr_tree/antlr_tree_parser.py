import re
from typing import List

from CrackSQL.preprocessor.TreeParser.antlr_tree.antlr_tree_node import *
from CrackSQL.utils.tools import self_split, split2wordlist


def is_terminal_word(g4_str: str):
    """
    Only care about keywords.
    Only words match with xxx : "xxx" will be considered
    """
    i = 0
    while i < len(g4_str):
        if g4_str[i] == ':':
            break
        i = i + 1
    repre = g4_str[i + 1:-1].strip()
    quote_flag = 0
    for i in range(0, len(repre)):
        if repre[i].isspace():
            continue
        if quote_flag == 0 and repre[i] != '\'':
            return False
        elif repre[i] == '\'':
            quote_flag = 1 - quote_flag
    return True


def split_name_repre(g4_str: str):
    i = 0
    while i < len(g4_str):
        if g4_str[i] == ':':
            break
        i = i + 1
    name = g4_str[0: i]
    repre = g4_str[i + 1:]
    names = name.split()
    if names[0] == 'fragment':
        name = names[1]
    return name.strip(), repre.strip()


def parse_g4(terms: List, node: AntlrRuleNode, node_map: dict[str, AntlrRuleNode], index: int, index_end: int,
             root_node: AntlrRuleNode):
    i = index
    cur_node = AntlrRuleNode('keywords', NodeType.WORDS, RepeatType.NONE, node)
    last_node = None
    while i < index_end:
        temp_str = terms[i]
        if len(temp_str) == 0:
            i = i + 1
            continue
        if temp_str == '(':
            node1 = AntlrRuleNode('()', NodeType.SM_BRACKET, RepeatType.NONE, cur_node)
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
            parse_g4(terms, node1, node_map, i + 1, temp_index - 1, root_node)
            i = temp_index
            last_node = node1
        elif temp_str == '|':
            if node.node_type != NodeType.OR:
                if len(cur_node.children) != 0:
                    node.add_child(cur_node)
                    cur_node = AntlrRuleNode('keywords', NodeType.WORDS, RepeatType.NONE, node)
                node1 = AntlrRuleNode('or', NodeType.OR, RepeatType.NONE, node)
                for child_node in node.children:
                    node1.add_child(child_node)
                node.clear_child()
                node.add_child(node1)
                i = parse_g4(terms, node1, node_map, i + 1, index_end, root_node)
            else:
                if len(cur_node.children) != 0:
                    node.add_child(cur_node)
                    cur_node = AntlrRuleNode('keywords', NodeType.WORDS, RepeatType.NONE, node)
                i = i + 1
        elif temp_str == '[':
            reg_str = ''
            while terms[i] != ']':
                reg_str = reg_str + terms[i]
                i = i + 1
                continue
            node1 = AntlrRuleNode(reg_str + ']', NodeType.LITERAL, RepeatType.NONE, node)
            last_node = node1
            cur_node.add_child(node1)
            i = i + 1
        elif temp_str == '*' or temp_str == '+' or temp_str == '?':
            if last_node is not None:
                if temp_str == '*':
                    last_node.repeat_type = RepeatType.STAR
                elif temp_str == '+':
                    last_node.repeat_type = RepeatType.PLUS
                elif temp_str == '?':
                    last_node.repeat_type = RepeatType.QUES
            i = i + 1
        elif temp_str[0] == '\'':
            node1 = AntlrRuleNode(temp_str, NodeType.LITERAL, RepeatType.NONE, node)
            last_node = node1
            i = i + 1
            cur_node.add_child(node1)
        elif is_rule_name(temp_str):
            if i + 1 < len(terms) and terms[i + 1] == '=':
                i = i + 2
                continue
            else:
                if temp_str in node_map:
                    link_node = node_map[temp_str]
                    if not link_node.value == root_node.value:
                        link_node.add_father_set(root_node)
                    node1 = AntlrRuleNode(link_node.value, link_node.get_derived_type(), RepeatType.NONE, node)
                    cur_node.add_child(node1)
                    node1.link_to(link_node, root_node)
                    last_node = node1
                i = i + 1
        else:
            i = i + 1
    if len(cur_node.children) != 0:
        node.add_child(cur_node)
    return i


def is_rule_name(str1: str):
    for i in range(len(str1)):
        if 'a' <= str1[i] <= 'z' or 'A' <= str1[i] <= 'Z' or str1[i] == '_' or '0' <= str1[i] <= '9':
            continue
        return False
    return True


def merge_repr(rep) -> str:
    res = ''
    quote_flag = False
    for i in range(len(rep)):
        if rep[i] == '\'':
            quote_flag = not quote_flag
        elif quote_flag:
            res = res + rep[i]
    return res


def extract_g4_from_file(gram_path):
    with open(gram_path, 'r') as file:
        content = file.read()
    content = re.sub(r'//.*?(?=\n|$)', '', content)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    content = re.sub(r'#\s*[a-z_A-Z0-9\s]*(?=\n|$)', '', content)
    res = []
    str0 = ''
    flag = False
    i = 0
    while i < len(content):
        if not flag and content[i] == ';':
            res.append(str0)
            str0 = ''
            i = i + 1
            continue
        if content[i] == '\'':
            flag = not flag
        elif flag and content[i] == '\\':
            str0 = str0 + content[i]
            i = i + 1
        str0 = str0 + content[i]
        i = i + 1
    return res


def parse_antlr(lexer_path, parser_path):
    import os
    lexer_g4s = extract_g4_from_file(lexer_path)
    parser_g4s = extract_g4_from_file(parser_path)

    node_map = {}
    keyword2rep = {}
    rep2keyword = {}
    grammar_rule_name = set()
    name_rep_pairs = []
    for g4_str in lexer_g4s:
        used_str = g4_str.strip()
        name, repr = split_name_repre(used_str)
        name_rep_pairs.append([name, repr])
        rule_node = AntlrRuleNode(name, NodeType.ROOT_KEYWORD, RepeatType.NONE)
        node_map[name] = rule_node
        keyword2rep[merge_repr(used_str)] = name
        rep2keyword[name] = merge_repr(used_str)
    for g4_str in parser_g4s:
        used_str = g4_str.strip()
        name, repr = split_name_repre(used_str)
        name_rep_pairs.append([name, repr])
        rule_node = AntlrRuleNode(name, NodeType.ROOT_NONE_KEYWORD, RepeatType.NONE)
        node_map[name] = rule_node
        grammar_rule_name.add(name)

    for name_rep_pair in name_rep_pairs:
        name = name_rep_pair[0]
        rep = name_rep_pair[1]
        all_words = split2wordlist(self_split(rep))
        parse_g4(all_words, node_map[name], node_map, 0, len(all_words), node_map[name])

    return rep2keyword, keyword2rep, node_map, grammar_rule_name
