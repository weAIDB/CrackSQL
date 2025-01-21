import json
from typing import Dict

from CrackSQL.preprocessor.query_simplifier.Tree import TreeNode
from CrackSQL.preprocessor.TreeParser.antlr_tree.antlr_tree_parser import parse_antlr
from CrackSQL.utils.tools import *
from CrackSQL.preprocessor.TreeParser.antlr_tree.antlr_tree_node import *
from CrackSQL.preprocessor.antlr_parser.parse_tree import parse_tree

"""
Used to generate a syntax tree for a given keyword
"""

map_to_stmt = {
    "pg": {
        "ABORT": ["transactionstmt"],
        "ALTER AGGREGATE": ["alterownerstmt"],
        "ALTER COLLATION": ["alterownerstmt"],
        "ALTER CONVERSION": ["alterownerstmt"],
        "ALTER DATABASE": ["alterownerstmt"],
        "ALTER DEFAULT PRIVILEGES": ["alterdefaultprivilegesstmt"],
        "ALTER DOMAIN": ["renamestmt"],
        "ALTER EVENT TRIGGER": ["renamestmt"],
        "ALTER EXTENSION": ["alterobjectschemastmt"],
        "ALTER FOREIGN DATA WRAPPER": [],
        "ALTER FOREIGN TABLE": [],
        "ALTER FUNCTION": [],
        "ALTER GROUP": [],
        "ALTER INDEX": [],
        "SELECT": "selectstmt",
    },
    "mysql": {

    }
}

banned_none_key_word = {
    "pg": {
        "unreserved_keyword",
        "plsql_unreserved_keyword",
        "reserved_keyword",
        "colid",
        "col_name_keyword"
    },
    "mysql": {

    }
}

dbg = (load_config())['dbg']

un_reach = -200

mask = "*******"


def make_trees_up_to_down(keywords: str, src: str, dialect: str):
    """
        According to the keywords in a keyword sequence, 
        the keyword subtree is constructed and generated

        You need to prevent non-keywords from having the same name as other keywords
    """
    antlr_lexer, antlr_parser = get_g4_path(dialect)
    rep2keyword, keyword2rep, node_map, grammar_rule_name = parse_antlr(antlr_lexer, antlr_parser)
    keywords_to_fit = keywords.split()
    global nodes
    nodes = []
    root_node = node_map[map_to_stmt[dialect][src]]
    focus_keywords = []
    for keyword in keywords_to_fit:
        if keyword in keyword2rep:
            assert keyword2rep[keyword] in node_map
            nodes.append(node_map[keyword2rep[keyword]])
            focus_keywords.append([keyword, keyword2rep[keyword]])

    """for each keyword find the path from root to it"""
    paths = {}
    for node in nodes:
        paths[node.value] = []
    visit = {}
    left, right, ans_ele = dfs(root_node, visit, 0, len(nodes), [], paths, dialect)
    if left < right:
        print('err in find ' + keywords)

    flag = True
    public_route = []
    k = 0
    while flag:
        fit_str = paths[nodes[0].value][k]
        for i in range(1, len(nodes)):
            if len(paths[nodes[i].value]) < k + 1 or paths[nodes[i].value][k] != fit_str:
                flag = False
        if flag:
            k = k + 1
    if k > 0:
        public_route = paths[nodes[0].value][:k - 1]
        for i in range(0, len(nodes)):
            paths[nodes[i].value] = paths[nodes[i].value][k - 1:]
            paths[nodes[i].value][len(paths[nodes[i].value]) - 1] = rep2keyword[
                paths[nodes[i].value][len(paths[nodes[i].value]) - 1]]
    if dbg:
        print('public_route:' + str(public_route))
        for key, value in paths.items():
            print(str(key) + " route:" + str(value))
    return focus_keywords, public_route, paths, rep2keyword, keyword2rep, grammar_rule_name


final_paths = []
nodes = []

path2idx = {}
all_paths = []
idx = 0


def path_clone(path: List[str]):
    res = []
    for path_str in path:
        res.append(path_str)
    return res


def make_trees_revised(keywords: str, src: str, dialect: str):
    """
        According to the keywords in a keyword sequence, 
        the keyword subtree is constructed and generated

        You need to prevent non-keywords from having the same name as other keywords
    """
    global final_paths
    final_paths = []
    global path2idx, idx, all_paths
    path2idx = {}
    idx = 0
    all_paths = []
    antlr_lexer, antlr_parser = get_g4_path(dialect)
    rep2keyword, keyword2rep, node_map, grammar_rule_name = parse_antlr(antlr_lexer, antlr_parser)
    keywords_to_fit = keywords.split()
    global nodes
    nodes = []
    root_node = node_map[map_to_stmt[dialect][src]]
    focus_keywords = []
    cnt_keyword = 0
    for keyword in keywords_to_fit:
        if keyword in keyword2rep:
            assert keyword2rep[keyword] in node_map
            nodes.append(node_map[keyword2rep[keyword]])
            focus_keywords.append([keyword, keyword2rep[keyword]])
            cnt_keyword = cnt_keyword + 1
        else:
            if len(nodes) > 0 and nodes[len(nodes) - 1] != mask:
                nodes.append(mask)
    if cnt_keyword == 0:
        return None, None, ''
        
    """for each keyword find the path from root to it"""
    visit = set()
    interval_dfs(root_node, visit, {}, {}, {},
                 [], banned_none_key_word[dialect])
    if len(final_paths) == 0:
        print('err in find ' + keywords)
        
    best_road_len = 1 << 20
    best_max_len = 1 << 20
    best_min_len = 1 << 20
    best_min_nodes = 1 << 20
    best_pub_road = []
    best_paths = []
    for paths in final_paths:
        flag = True
        public_route = []
        paths_print = []
        k = 0
        while flag and cnt_keyword > 1:
            fit_str = all_paths[paths[0]][k]
            for i in range(1, len(nodes)):
                if nodes[i] != mask and (len(all_paths[paths[i]]) < k + 1 or all_paths[paths[i]][k] != fit_str):
                    flag = False
            if flag:
                k = k + 1
        max_len = -1
        min_len = 1 << 20
        nodes_num = set()
        if k > 0:
            public_route = all_paths[paths[0]][:k - 1]
            for i in range(0, len(nodes)):
                if nodes[i] != mask:
                    path_print = path_clone(all_paths[paths[i]][k - 1:])
                    path_print[len(path_print) - 1] = rep2keyword[path_print[len(path_print) - 1]]
                    for node in path_print:
                        nodes_num.add(node)
                    paths_print.append(path_print)
                    max_len = max(max_len, len(path_print))
                    min_len = min(min_len, len(path_print))
                else:
                    paths_print.append([])
        else:
            for i in range(len(nodes)):
                if nodes[i] != mask:
                    path_print = path_clone(all_paths[paths[i]])
                    path_print[len(path_print) - 1] = rep2keyword[path_print[len(path_print) - 1]]
                    for node in path_print:
                        nodes_num.add(node)
                    paths_print.append(path_print)
                    max_len = max(max_len, len(path_print))
                    min_len = min(min_len, len(path_print))
                else:
                    paths_print.append([])
        if (len(nodes_num) < best_min_nodes
                or (len(nodes_num) == best_min_nodes and len(public_route) < best_road_len)
                or (len(nodes_num) == best_min_nodes and len(public_route) == best_road_len
                    and max_len < best_max_len)
                or (len(nodes_num) == best_min_nodes and len(public_route) == best_road_len
                    and max_len < best_max_len and min_len < best_min_len)):
            best_pub_road = public_route
            best_paths = paths_print
            best_road_len = len(public_route)
            best_max_len = max_len
            best_min_len = min_len
            best_min_nodes = len(nodes_num)
    return best_pub_road, best_paths, get_str_rep(best_pub_road, best_paths)

def get_str_rep(pub_road, paths):
    res_str = ''
    stack = []
    end_index = 0
    for path in paths:
        if len(path) == 0:
            continue
        index = 0
        while index < end_index and index < len(path):
            if stack[index] != path[index]:
                break
            else:
                index = index + 1
        for i in range(index, end_index):
            res_str = res_str + ')'
            stack.pop()
        end_index = index
        for i in range(index, len(path)):
            if i != len(path) - 1:
                res_str = res_str + ' (' + path[i]
                stack.append(path[i])
                end_index = end_index + 1
            else:
                res_str = res_str + " " + path[i]
    for i in range(end_index):
        res_str = res_str + ")"
    return res_str.strip()


def get_mark(node: AntlrRuleNode, left, right):
    return node.value + '_left' + str(left) + '_right' + str(right)


def roll_back(left, cur_node):
    i = left
    while i > 0:
        j = left - i + 1
        k = 0
        while k < i:
            if j + k == left:
                compare_word = cur_node.value
            else:
                compare_word = nodes[j + k]
            if compare_word == nodes[k].value:
                k = k + 1
            else:
                break
        if k == i:
            return i
        else:
            i = i - 1
    return i


def paths_clone(paths: List[int]):
    new_list = []
    for i in range(len(paths)):
        new_list.append(paths[i])
    return new_list


def paths_equal(paths1: List[int], paths2: List[int]) -> int:
    for i in range(len(paths1)):
        if paths1[i] > paths2[i]:
            return 1
        elif paths1[i] < paths2[i]:
            return -1
    return 0


def can_merge(left, index_left, right, index_right) -> bool:
    return left.right[index_left] == right.left[index_right] or (
            left.right[index_left] + 1 == right.left[index_right] and nodes[left.right[index_left]] == mask)


def print_paths(paths: List[int]):
    for i in range(len(paths)):
        if paths[i] != un_reach:
            print(str(i) + ":" + str(all_paths[paths[i]]))


class PosRes:
    # Used to indicate the range that can be covered by a prefix 
    # from the beginning of a non-terminal character to a certain position
    def __init__(self, length):
        self.left = []
        self.right = []
        self.paths = []
        self.length = length
        self.can_blank = False

    def check_correct(self):
        pass

    def add_new_keyword(self, pos: int, path_idx: int):
        self.left.append(pos)
        self.right.append(pos + 1)
        new_list = [un_reach for _ in range(self.length)]
        new_list[pos] = path_idx
        self.paths.append(new_list)
        self.check_correct()

    def add_new_interval(self, pos_res, index):
        self.left.append(pos_res.left[index])
        self.right.append(pos_res.right[index])
        self.paths.append(paths_clone(pos_res.paths[index]))
        self.check_correct()

    def add_merge(self, merge1, index1, merge2, index2):
        self.left.append(merge1.left[index1])
        self.right.append(merge2.right[index2])
        new_dict = [un_reach for _ in range(self.length)]
        for i in range(len(merge1.paths[index1])):
            if merge1.paths[index1][i] != un_reach:
                new_dict[i] = merge1.paths[index1][i]
        for i in range(len(merge2.paths[index2])):
            if merge2.paths[index2][i] != un_reach:
                new_dict[i] = merge2.paths[index2][i]
        self.paths.append(new_dict)
        self.check_correct()

    def is_empty(self) -> bool:
        return len(self.left) == 0

    def sort_left(self):
        if (len(self.left) != len(self.right)
                or len(self.right) != len(self.paths) or len(self.left) == 0):
            return
        items = list(zip(self.left, self.right, self.paths))

        def sort_key(item):
            left, right, path = item
            
            path_str = ''.join(map(str, path))
            return (left, right, path_str)

        items.sort(key=sort_key)
        self.left, self.right, self.paths = zip(*items)
        self.__dedup()
        self.check_correct()

    def __dedup(self):
        
        res_left = []
        res_right = []
        res_paths = []
        i = 0
        j = 1
        if not self.is_empty():
            res_left.append(self.left[0])
            res_right.append(self.right[0])
            res_paths.append(self.paths[0])
        while j < len(self.left) and i < len(self.left):
            
            while (j < len(self.left) and self.left[j] == res_left[i]
                   and self.right[j] == res_right[i] and paths_equal(self.paths[j], res_paths[i]) == 0):
                j = j + 1
            if j < len(self.left):
                res_left.append(self.left[j])
                res_right.append(self.right[j])
                res_paths.append(self.paths[j])
            i = i + 1
            j = j + 1
        self.left = res_left
        self.right = res_right
        self.paths = res_paths

    def sort_right(self):
        if len(self.left) != len(self.right) or len(self.right) != len(self.paths) or len(self.left) == 0:
            return
        items = list(zip(self.right, self.left, self.paths))

        def sort_key(item):
            left, right, path = item
            
            path_str = ''.join(map(str, path))
            return (left, right, path_str)

        items.sort(key=sort_key)
        self.right, self.left, self.paths = zip(*items)
        self.__dedup()
        self.check_correct()

    def is_equal(self, pos_res):
        
        if len(self.left) != len(pos_res.left):
            return False
        self.sort_left()
        pos_res.sort_left()
        for i in range(len(self.left)):
            if (self.left[i] != pos_res.left[i] or self.right[i] != pos_res.right[i]
                    or paths_equal(self.paths[i], pos_res.paths[i]) != 0):
                return False
        return True

    def add_empty(self):
        self.can_blank = True

    def __str__(self):
        res = ''
        if self.can_blank:
            res = 'blank_enable: '
        for i in range(len(self.left)):
            res = res + '[' + str(self.left[i]) + ', ' + str(self.right[i]) + '] ' + str(self.paths[i]) + " "
        return res

    def merge(self, pos_res):
        self.sort_left()
        pos_res.sort_left()
        i = 0
        j = 0
        res_left = []
        res_right = []
        res_paths = []
        while i < len(self.left) and j < len(pos_res.left):
            # find first in pos_res that bigger than self
            while (j < len(pos_res.left) and
                   ((self.left[i] > pos_res.left[j] or
                     (self.left[i] == pos_res.left[j]
                      and self.right[i] > pos_res.right[j]) or
                     (self.left[i] == pos_res.left[j]
                      and self.right[i] == pos_res.right[j])
                     and paths_equal(self.paths[i], pos_res.paths[j]) == 1))):
                res_left.append(pos_res.left[j])
                res_right.append(pos_res.right[j])
                res_paths.append(pos_res.paths[j])
                j = j + 1
            res_left.append(self.left[i])
            res_right.append(self.right[i])
            res_paths.append(self.paths[i])
            if j < len(pos_res.left) and self.left[i] == pos_res.left[j] and self.right[i] == pos_res.right[j]:
                j = j + 1
            i = i + 1
        if i < len(self.left):
            while i < len(self.left):
                res_left.append(self.left[i])
                res_right.append(self.right[i])
                res_paths.append(self.paths[i])
                i = i + 1
        if j < len(pos_res.left):
            while j < len(pos_res.left):
                res_left.append(pos_res.left[j])
                res_right.append(pos_res.right[j])
                res_paths.append(pos_res.paths[j])
                j = j + 1
        self.left = res_left
        self.right = res_right
        self.paths = res_paths
        self.check_correct()

    def rm_prefix_route(self, ori_path: List[str]):
        global idx, all_paths, path2idx
        new_pos_res = PosRes(self.length)
        new_pos_res.can_blank = self.can_blank
        for i in range(len(self.left)):
            new_pos_res.add_new_interval(self, i)
        new_paths = []
        for i in range(len(self.left)):
            new_path = [un_reach for _ in range(len(nodes))]
            for j in range(self.length):
                if self.paths[i][j] != un_reach:
                    path_tmp = all_paths[self.paths[i][j]]
                    tmp_path = path_tmp[len(ori_path):]
                    if tuple(tmp_path) in path2idx:
                        new_path[j] = path2idx[tuple(tmp_path)]
                    else:
                        all_paths.append(tmp_path)
                        path2idx[tuple(tmp_path)] = idx
                        new_path[j] = idx
                        idx = idx + 1
            new_paths.append(new_path)
        new_pos_res.paths = new_paths
        new_pos_res.check_correct()
        return new_pos_res

    def add_prefix_route(self, ori_path: List[str]):
        new_pos_res = PosRes(self.length)
        new_pos_res.can_blank = self.can_blank
        for i in range(len(self.left)):
            new_pos_res.add_new_interval(self, i)
        global idx, all_paths, path2idx
        new_paths = []
        for path in new_pos_res.paths:
            new_path = [un_reach for _ in range(len(nodes))]
            for i in range(len(nodes)):
                if path[i] == un_reach:
                    continue
                temp_path = ori_path + all_paths[path[i]]
                if tuple(temp_path) in path2idx:
                    new_path[i] = path2idx[tuple(temp_path)]
                else:
                    all_paths.append(temp_path)
                    path2idx[tuple(temp_path)] = idx
                    new_path[i] = idx
                    idx = idx + 1
            new_paths.append(new_path)
        new_pos_res.paths = new_paths
        new_pos_res.check_correct()
        return new_pos_res


def interval_dfs(node0: AntlrRuleNode, visit: set, prefix_word: Dict[str, PosRes], body_word: Dict[str, PosRes],
                 postfix_word: Dict[str, PosRes], cur_path: list, banned_words) -> tuple[PosRes, PosRes, PosRes]:
    """
        In consideration of the possibility that the partial prefix 
        to some non-keyword is complete, pass cur_pos_res
    """
    prefix = PosRes(len(nodes))
    body = PosRes(len(nodes))
    postfix = PosRes(len(nodes))
    can_empty = False
    global idx
    if node0.node_type == NodeType.KEYWORD:
        cur_path.append(node0.value)
        can_empty = False
        flag = False
        temp_idx = un_reach
        for i in range(len(nodes)):
            if nodes[i] == mask:
                continue
            if node0.link == nodes[i]:
                if not flag:
                    new_path = []
                    for node in cur_path:
                        new_path.append(node)
                    all_paths.append(new_path)
                    path2idx[tuple(new_path)] = idx
                    temp_idx = idx
                    idx = idx + 1
                    flag = True
                prefix.add_new_keyword(i, temp_idx)
                body.add_new_keyword(i, temp_idx)
                body.can_blank = False
                postfix.add_new_keyword(i, temp_idx)
                if dbg:
                    print('find ' + node0.value + " " + str(cur_path))
        cur_path.pop()
    elif node0.node_type == NodeType.NONE_KEYWORD or node0.node_type == NodeType.ROOT_NONE_KEYWORD:
        can_empty = True
        if node0.value in banned_words:
            return prefix, body, postfix
        cur_path.append(node0.value)
        if node0.value not in visit:
            visit.add(node0.value)
            node1 = node0 if node0.node_type == NodeType.ROOT_NONE_KEYWORD else node0.link
            flag = True
            body.can_blank = True
            for child in node1.children:
                child_prefix, child_body, child_postfix = interval_dfs(child, visit, prefix_word, body_word,
                                                                       postfix_word, cur_path, banned_words)
                can_empty = can_empty and child_body.can_blank
                check_fit(postfix, child_prefix)
                update_prefix(prefix, body, child_prefix, flag)
                update_body(body, child_body, flag)
                update_postfix(postfix, child_body, child_postfix)
                flag = False
            cur_path.pop()
            prefix_word[node0.value] = prefix.rm_prefix_route(cur_path)
            body_word[node0.value] = body.rm_prefix_route(cur_path)
            postfix_word[node0.value] = postfix.rm_prefix_route(cur_path)
        else:
            cur_path.pop()
            if node0.value in prefix_word:
                prefix = prefix_word[node0.value].add_prefix_route(cur_path)
                body = body_word[node0.value].add_prefix_route(cur_path)
                postfix = postfix_word[node0.value].add_prefix_route(cur_path)
            else:
                return prefix, body, postfix
    elif node0.node_type == NodeType.LITERAL:
        pass
    elif node0.node_type == NodeType.OR:
        can_empty = False
        for child in node0.children:
            child_prefix, child_body, child_postfix = (
                interval_dfs(child, visit, prefix_word, body_word, postfix_word, cur_path, banned_words))
            can_empty = can_empty or child_body.can_blank
            prefix.merge(child_prefix)
            body.merge(child_body)
            postfix.merge(child_postfix)
    else:
        # To calculate suffixes, you need to keep the body and postfix information for each child element
        assert node0.node_type == NodeType.SM_BRACKET or node0.node_type == NodeType.WORDS
        flag = True
        body.can_blank = True
        for child in node0.children:
            child_prefix, child_body, child_postfix = interval_dfs(child, visit, prefix_word, body_word,
                                                                   postfix_word, cur_path, banned_words)
            check_fit(postfix, child_prefix)
            update_prefix(prefix, body, child_prefix, flag)
            update_body(body, child_body, flag)
            update_postfix(postfix, child_body, child_postfix)
            flag = False
    if node0.repeat_type == RepeatType.QUES or node0.repeat_type == RepeatType.STAR:
        # Indicates that the value can be null
        can_empty = True
    if can_empty:
        body.add_empty()

    if dbg:
        print("VAL-----:" + node0.value)
        print(prefix)
        print(body)
        print(postfix)
    return prefix, body, postfix


def check_fit(postfix: PosRes, prefix: PosRes):
    postfix.sort_right()
    prefix.sort_left()
    if dbg:
        print("in_check_fit")
        print("~check")
        print(postfix)
        print(prefix)
    pre_len = 1 if nodes[0] == mask else 0
    post_len = len(nodes) - 1 if nodes[len(nodes) - 1] == mask else len(nodes)
    if pre_len == post_len - 1:
        for i in range(len(postfix.left)):
            if postfix.left[i] == pre_len and postfix.right[i] == pre_len + 1:
                res_path = [postfix.paths[i][0]]
                final_paths.append(res_path)
                if dbg:
                    print("find_way")
        for i in range(len(prefix.left)):
            if prefix.left[i] == pre_len and prefix.right[i] == pre_len + 1:
                res_path = [prefix.paths[i][0]]
                final_paths.append(res_path)
                if dbg:
                    print("find_way")
    else:
        for i in range(len(postfix.left)):
            for j in range(len(prefix.left)):
                if (postfix.left[i] <= pre_len and
                        can_merge(postfix, i, prefix, j) and prefix.right[j] >= post_len):
                    res_path = [un_reach for _ in range(len(nodes))]
                    for i1 in range(len(nodes)):
                        if postfix.paths[i][i1] != un_reach:
                            res_path[i1] = postfix.paths[i][i1]
                    for i2 in range(len(nodes)):
                        if prefix.paths[j][i2] != un_reach:
                            res_path[i2] = prefix.paths[j][i2]
                    final_paths.append(res_path)
                    if dbg:
                        print("find_way")
    if dbg:
        print("~endcheck")


def update_body(body: PosRes, child_body: PosRes, flag: bool):
    updated_body = PosRes(body.length)
    if dbg:
        print("enter---body")
        print(body)
        print(child_body)
    if body.can_blank or flag:
        # Add all of child_body
        for i in range(len(child_body.left)):
            updated_body.add_new_interval(child_body, i)
    else:
        for i in range(len(child_body.left)):
            if child_body.left[i] - 1 >= 0 and nodes[child_body.left[i] - 1] == mask:
                updated_body.add_new_interval(child_body, i)
    if child_body.can_blank:
        for i in range(len(body.left)):
            updated_body.add_new_interval(body, i)
    else:
        for i in range(len(body.left)):
            if body.right[i] < len(nodes) and nodes[body.right[i]] == mask:
                updated_body.add_new_interval(body, i)
    # Concatenate the front and back, adding only those that can be concatenated to updated_body
    if (body.can_blank or flag) and child_body.can_blank:
        updated_body.add_empty()
    for i in range(len(body.left)):
        for j in range(len(child_body.left)):
            if can_merge(body, i, child_body, j):
                updated_body.add_merge(body, i, child_body, j)
    updated_body.sort_left()
    body.left = updated_body.left
    body.right = updated_body.right
    body.paths = updated_body.paths
    body.can_blank = body.can_blank and child_body.can_blank
    if dbg:
        print(body)
        print("end---body")


def update_prefix(prefix: PosRes, body: PosRes, child_prefix: PosRes, flag: bool):
    if dbg:
        print("enter---prefix")
        print(prefix)
        print(body)
        print(child_prefix)
    if body.can_blank or flag:
        # Add all the information in child_prefix
        for i in range(len(child_prefix.left)):
            prefix.add_new_interval(child_prefix, i)
    else:
        for i in range(len(child_prefix.left)):
            # If left left is empty, then you can join
            if child_prefix.left[i] - 1 >= 0 and nodes[child_prefix.left[i] - 1] == mask:
                prefix.add_new_interval(child_prefix, i)
    for i in range(len(body.left)):
        for j in range(len(child_prefix.left)):
            if can_merge(body, i, child_prefix, j):
                prefix.add_merge(body, i, child_prefix, j)
    prefix.sort_left()
    if dbg:
        print(prefix)
        print("end---prefix")


def update_postfix(postfix: PosRes, child_body: PosRes, child_postfix: PosRes):
    if dbg:
        print("enter---postfix")
        print(postfix)
        print(child_body)
        print(child_postfix)
    updated_postfix = PosRes(postfix.length)
    if child_body.can_blank:
        # Clear the previous postfix
        for i in range(len(postfix.left)):
            updated_postfix.add_new_interval(postfix, i)
    else:
        for i in range(len(postfix.left)):
            if postfix.right[i] < len(nodes) and nodes[postfix.right[i]] == mask:
                updated_postfix.add_new_interval(postfix, i)
    for i in range(len(postfix.left)):
        for j in range(len(child_body.left)):
            if can_merge(postfix, i, child_body, j):
                updated_postfix.add_merge(postfix, i, child_body, j)
    for i in range(len(child_postfix.left)):
        updated_postfix.add_new_interval(child_postfix, i)
    postfix.left = updated_postfix.left
    postfix.right = updated_postfix.right
    postfix.paths = updated_postfix.paths
    postfix.sort_left()
    if dbg:
        print(postfix)
        print("end---postfix")


def dfs(node0: AntlrRuleNode, visit: Dict, left: int,
        right: int, cur_path: list, paths, dialect: str):
    ans_left = left
    ans_right = right
    ans_ele = None
    if left >= right:
        return left, right, ans_ele
    if node0.node_type == NodeType.KEYWORD:
        if node0.link == nodes[left]:
            ans_left = left + 1
            ans_right = right
            route_path = []
            for j in range(len(cur_path)):
                route_path.append(cur_path[j])
            route_path.append(node0.value)
            print('find: ' + str(route_path))
            paths[node0.value] = route_path
        else:
            
            ans_left = roll_back(left, node0)
            ans_right = right
    elif node0.node_type == NodeType.NONE_KEYWORD or node0.node_type == NodeType.ROOT_NONE_KEYWORD:
        if node0.value in banned_none_key_word[dialect]:
            return left, right, ans_ele
        mark = get_mark(node0, left, right)
        if visit.get(mark, -2) >= 0:
            return visit[mark], right, ans_ele
        elif visit.get(mark, -2) == -1:
            return left, right, ans_ele
        visit[mark] = -1
        node1 = node0 if node0.node_type == NodeType.ROOT_NONE_KEYWORD else node0.link
        cur_path.append(node1.value)
        for i in range(len(node1.children)):
            ans_left, ans_right, ans_path = dfs(node1.children[i], visit,
                                                ans_left, ans_right, cur_path, paths, dialect)
            if ans_ele is not None:
                break
        visit[mark] = ans_left
        cur_path.pop()
    elif node0.node_type == NodeType.LITERAL:
        return ans_left, ans_right, ans_ele
    elif node0.node_type == NodeType.OR:
        for i in range(len(node0.children)):
            left0, right0, ans_ele = dfs(node0.children[i], visit, left, right, cur_path, paths, dialect)
            if left0 >= ans_left and right0 <= ans_right:
                ans_left, ans_right = left0, right0
            if ans_ele is not None:
                break
    else:
        assert node0.node_type == NodeType.SM_BRACKET or node0.node_type == NodeType.WORDS
        for i in range(len(node0.children)):
            ans_left, ans_right, ans_ele = dfs(node0.children[i], visit, ans_left,
                                               ans_right, cur_path, paths, dialect)
            if ans_ele is not None:
                break
    if node0.repeat_type == RepeatType.QUES or node0.repeat_type == RepeatType.STAR:
        if ans_left < left:
            ans_left = left
        if ans_right > right:
            ans_right = right
    if (left == 0 and right == len(nodes) and ans_left >= ans_right and ans_ele is None
            and (node0.node_type == NodeType.KEYWORD
                 or node0.node_type == NodeType.ROOT_KEYWORD
                 or node0.node_type == NodeType.ROOT_NONE_KEYWORD
                 or node0.node_type == NodeType.NONE_KEYWORD)):
        ans_ele = node0
    return ans_left, ans_right, ans_ele


def get_str_tree(keyword: str, src: str, dialet: str):
    return "string_tree"


def is_terminal(keyword: str):
    if len(keyword) == 0 or len(keyword) == 1:
        return False
    for char in keyword:
        if 'A' <= char <= 'Z' or char == '_' or '0' <= char <= '9':
            continue
        return False
    return True


def is_special_locate_mark(str1):
    return str1 == '(' or str1 == ')' or str1 == '+' or str1 == '*' or str1 == ',' or str1 == '@'


def interval_tree_node_dfs(node0: TreeNode, visit: set, cur_path: list) -> tuple[PosRes, PosRes, PosRes]:
    prefix = PosRes(len(nodes))
    body = PosRes(len(nodes))
    postfix = PosRes(len(nodes))
    global idx
    if len(node0.children) == 0:
        if not is_terminal(node0.value) and not is_special_locate_mark(node0.value):
            body.add_empty()
            return prefix, body, postfix
        cur_path.append(node0.value)
        flag = False
        temp_idx = un_reach
        for i in range(len(nodes)):
            if nodes[i] == mask:
                continue
            if node0.value == nodes[i]:
                if not flag:
                    new_path = []
                    for node in cur_path:
                        new_path.append(node)
                    all_paths.append(new_path)
                    path2idx[tuple(new_path)] = idx
                    temp_idx = idx
                    idx = idx + 1
                    flag = True
                prefix.add_new_keyword(i, temp_idx)
                body.add_new_keyword(i, temp_idx)
                postfix.add_new_keyword(i, temp_idx)
                if dbg:
                    print('find ' + node0.value + " " + str(cur_path))
        cur_path.pop()
    else:
        flag = True
        cur_path.append(node0.value)
        for child in node0.children:
            child_prefix, child_body, child_postfix = interval_tree_node_dfs(child, visit, cur_path)
            check_fit(postfix, child_prefix)
            update_prefix(prefix, body, child_prefix, flag)
            update_body(body, child_body, flag)
            update_postfix(postfix, child_body, child_postfix)
            flag = False
        cur_path.pop()
    if dbg:
        print("VAL-----:" + node0.value)
        print(prefix)
        print(body)
        print(postfix)
    return prefix, body, postfix


def make_tree_gpt(keywords: str, description: str, dialect: str):
    global final_paths
    final_paths = []
    global path2idx, idx, all_paths
    path2idx = {}
    idx = 0
    all_paths = []
    keywords_to_fit = keywords.split()
    global nodes
    nodes = []
    cnt_keyword = 0
    for keyword in keywords_to_fit:
        if is_terminal(keyword) or is_special_locate_mark(keyword):
            nodes.append(keyword)
            cnt_keyword = cnt_keyword + 1
        else:
            if len(nodes) > 0 and nodes[len(nodes) - 1] != mask:
                nodes.append(mask)

    if cnt_keyword == 0:
        return '', ''
        
    """for each keyword find the path from root to it"""
    visit = set()
    example = give_example(keywords, description, dialect)
    try:
        example_json = json.loads(example[0])
    except Exception as e:
        print('parse error ' + keywords)
        return 'Parse error', 'example[0]'
    final_example = example_json['demo']
    tree_node, line, column, msg = parse_tree(final_example, dialect)
    if tree_node is None:
        print('parse error ' + keywords)
        return 'Parse error', final_example
    tree_node = TreeNode.make_g4_tree(tree_node, dialect)
    interval_tree_node_dfs(tree_node, visit, [])
    if len(final_paths) == 0:
        print('err in find ' + keywords)
        return 'Found error', final_example

    best_road_len = 1 << 20
    best_max_len = 1 << 20
    best_min_len = 1 << 20
    best_min_nodes = 1 << 20
    best_pub_road = []
    best_paths = []
    for paths in final_paths:
        flag = True
        public_route = []
        paths_print = []
        k = 0
        while flag and cnt_keyword > 1:
            fit_str = all_paths[paths[0]][k]
            for i in range(1, len(nodes)):
                if nodes[i] != mask and (len(all_paths[paths[i]]) < k + 1 or all_paths[paths[i]][k] != fit_str):
                    flag = False
            if flag:
                k = k + 1
        max_len = -1
        min_len = 1 << 20
        nodes_num = set()
        if k > 0:
            public_route = all_paths[paths[0]][:k - 1]
            for i in range(0, len(nodes)):
                if nodes[i] != mask:
                    path_print = path_clone(all_paths[paths[i]][k - 1:])
                    path_print[len(path_print) - 1] = path_print[len(path_print) - 1]
                    for node in path_print:
                        nodes_num.add(node)
                    paths_print.append(path_print)
                    max_len = max(max_len, len(path_print))
                    min_len = min(min_len, len(path_print))
                else:
                    paths_print.append([])
        else:
            for i in range(len(nodes)):
                if nodes[i] != mask:
                    path_print = path_clone(all_paths[paths[i]])
                    path_print[len(path_print) - 1] = path_print[len(path_print) - 1]
                    for node in path_print:
                        nodes_num.add(node)
                    paths_print.append(path_print)
                    max_len = max(max_len, len(path_print))
                    min_len = min(min_len, len(path_print))
                else:
                    paths_print.append([])
        if (len(nodes_num) < best_min_nodes
                or (len(nodes_num) == best_min_nodes and len(public_route) < best_road_len)
                or (len(nodes_num) == best_min_nodes and len(public_route) == best_road_len
                    and max_len < best_max_len)
                or (len(nodes_num) == best_min_nodes and len(public_route) == best_road_len
                    and max_len < best_max_len and min_len < best_min_len)):
            best_pub_road = public_route
            best_paths = paths_print
            best_road_len = len(public_route)
            best_max_len = max_len
            best_min_len = min_len
            best_min_nodes = len(nodes_num)
    if cnt_keyword == 1:
        best_paths[0] = best_paths[0][-2:]
    return get_str_rep(best_pub_road, best_paths), final_example


def make_tree_demo(keywords: str, dialect: str, example_demo):
    global final_paths
    final_paths = []
    global path2idx, idx, all_paths
    path2idx = {}
    idx = 0
    all_paths = []
    keywords_to_fit = keywords.split()
    global nodes
    nodes = []
    cnt_keyword = 0
    for keyword in keywords_to_fit:
        if is_terminal(keyword) or is_special_locate_mark(keyword):
            nodes.append(keyword)
            cnt_keyword = cnt_keyword + 1
        else:
            if len(nodes) > 0 and nodes[len(nodes) - 1] != mask:
                nodes.append(mask)

    if cnt_keyword == 0:
        return ''
        
    """for each keyword find the path from root to it"""
    visit = set()
    final_example = example_demo
    tree_node, line, column, msg = parse_tree(final_example, dialect)
    if tree_node is None:
        print('parse error ' + keywords)
        return 'Parse error'
    tree_node = TreeNode.make_g4_tree_by_node(tree_node, dialect)
    interval_tree_node_dfs(tree_node, visit, [])
    if len(final_paths) == 0:
        print('err in find ' + keywords)
        return 'Found error'

    best_road_len = 1 << 20
    best_max_len = 1 << 20
    best_min_len = 1 << 20
    best_min_nodes = 1 << 20
    best_pub_road = []
    best_paths = []
    for paths in final_paths:
        flag = True
        public_route = []
        paths_print = []
        k = 0
        while flag and cnt_keyword > 1:
            fit_str = all_paths[paths[0]][k]
            for i in range(1, len(nodes)):
                if nodes[i] != mask and (len(all_paths[paths[i]]) < k + 1 or all_paths[paths[i]][k] != fit_str):
                    flag = False
            if flag:
                k = k + 1
        max_len = -1
        min_len = 1 << 20
        nodes_num = set()
        if k > 0:
            public_route = all_paths[paths[0]][:k - 1]
            for i in range(0, len(nodes)):
                if nodes[i] != mask:
                    path_print = path_clone(all_paths[paths[i]][k - 1:])
                    path_print[len(path_print) - 1] = path_print[len(path_print) - 1]
                    for node in path_print:
                        nodes_num.add(node)
                    paths_print.append(path_print)
                    max_len = max(max_len, len(path_print))
                    min_len = min(min_len, len(path_print))
                else:
                    paths_print.append([])
        else:
            for i in range(len(nodes)):
                if nodes[i] != mask:
                    path_print = path_clone(all_paths[paths[i]])
                    path_print[len(path_print) - 1] = path_print[len(path_print) - 1]
                    for node in path_print:
                        nodes_num.add(node)
                    paths_print.append(path_print)
                    max_len = max(max_len, len(path_print))
                    min_len = min(min_len, len(path_print))
                else:
                    paths_print.append([])
        if (len(nodes_num) < best_min_nodes
                or (len(nodes_num) == best_min_nodes and len(public_route) < best_road_len)
                or (len(nodes_num) == best_min_nodes and len(public_route) == best_road_len
                    and max_len < best_max_len)
                or (len(nodes_num) == best_min_nodes and len(public_route) == best_road_len
                    and max_len < best_max_len and min_len < best_min_len)):
            best_pub_road = public_route
            best_paths = paths_print
            best_road_len = len(public_route)
            best_max_len = max_len
            best_min_len = min_len
            best_min_nodes = len(nodes_num)
    if cnt_keyword == 1:
        best_paths[0] = best_paths[0][-2:]
    return get_str_rep(best_pub_road, best_paths)


def make_tree(keyword: str, src, description, dialect):
    tree_rep, example = make_tree_gpt(keyword, description, dialect)
    return tree_rep, example


def give_example(keyword: str, description: str, dialect: str):
    user_prompt = (
        f"Assume you are an expert in providing examples for syntax fragments. "
        f"Below, I will give you a {dialect} SELECT syntax encapsulated in <code> label. "
        f"Your task is to provide a demo for this syntax with its description. "
        f"It's worth noting that this SQL syntax is just a fragment, "
        f"but you need to help complete it into a full executable SQL statement. "
        f"Remember, the demo should be as simple as possible, but you also need to ensure its correctness and "
        f"answer in format like this:"
        f"```json\n"
        f"{{\n"
        f"  \"demo\": \"demo of the syntax\"\n"
        f"}}\n"
        f"```\n"
        f"\n<code>\n{keyword}\n</code>\n"
        f"Here's the description you need:\n {description}"
    )
    return extract_json(remove_comments(send_request([], None, user_prompt)))
