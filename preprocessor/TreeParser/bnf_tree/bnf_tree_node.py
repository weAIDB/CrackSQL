from enum import Enum
from typing import List

from CrackSQL.utils.tools import only_lower_underscore


class NodeType(Enum):
    OR = 1
    KEYWORD = 2
    NONE_KEYWORD = 3
    WORDS = 4
    LITERAL = 5
    SM_BRACKET = 6
    MID_BRACKET = 7
    BIG_BRACKET = 8
    ROOT = 9


class RepeatType(Enum):
    NONE = 0
    PLUS = 1
    QUES = 2
    STAR = 3


class BnfRuleNode:
    def __init__(self, value: str, node_type: NodeType, repeat_type=RepeatType.NONE, father=None, children=None):
        """
        Initialize a multi-tree node
        :type: node type
        :param father: parent node
        :param children: child node list (empty by default)
        """
        self.node_type = node_type
        self.repeat_type = repeat_type
        self.value = value
        self.children = children if children is not None else []
        self.child_link = {}
        self.father = father
        self.link = None
        self.father_link = {}

    def __str__(self):
        res_str = ''
        if self.node_type == NodeType.WORDS:
            for i in range(len(self.children)):
                if i != 0:
                    res_str = res_str + " "
                res_str = res_str + str(self.children[i])
            return res_str
        elif self.node_type == NodeType.MID_BRACKET:
            res_str = ' [ '
            for i in range(len(self.children)):
                if i != 0:
                    res_str = res_str + " "
                res_str = res_str + str(self.children[i])
            return res_str + ' ]'
        elif self.node_type == NodeType.SM_BRACKET:
            res_str = ' ( '
            for i in range(len(self.children)):
                if i != 0:
                    res_str = res_str + " "
                res_str = res_str + str(self.children[i])
            return res_str + ' ) '
        res_str = self.value
        if len(self.children) != 0:
            res_str = res_str + ' { '
        for i in range(len(self.children)):
            if i != 0:
                if self.node_type == NodeType.OR:
                    res_str = res_str + ' | '
                else:
                    res_str = res_str + ' , '
            res_str = res_str + str(self.children[i])
        if len(self.children) != 0:
            res_str = res_str + ' } '
        return res_str

    def add_child(self, node):
        self.children.append(node)

    def clear_child(self):
        self.children.clear()

    def enumerate(self) -> List[str]:
        if self.node_type == NodeType.OR:
            ans = []
            for child in self.children:
                ans = ans + child.enumerate()
            return ans
        elif (self.node_type == NodeType.WORDS or self.node_type == NodeType.ROOT
              or self.node_type == NodeType.BIG_BRACKET or self.node_type == NodeType.MID_BRACKET):
            res = []
            flag = False
            last_idx = -1
            while not flag:
                flag = True
                ans = []
                for i in range(len(self.children)):
                    if self.children[i].node_type == NodeType.MID_BRACKET and i > last_idx and flag:
                        flag = False
                        last_idx = i
                        if len(ans) == 0:
                            ans = self.children[i].enumerate()
                        else:
                            temp_list = []
                            for child_str in self.children[i].enumerate():
                                if child_str == '...':
                                    continue
                                for ans_str in ans:
                                    temp_list.append(ans_str + " " + child_str)
                            ans = temp_list
                    elif self.children[i].node_type != NodeType.MID_BRACKET:
                        if len(ans) == 0:
                            ans = self.children[i].enumerate()
                        else:
                            temp_list = []
                            for child_str in self.children[i].enumerate():
                                if child_str == '...':
                                    continue
                                for ans_str in ans:
                                    temp_list.append(ans_str + " " + child_str)
                            ans = temp_list
                    else:
                        temp_list = []
                        for ans_str in ans:
                            if not ans_str.endswith('...'):
                                temp_list.append(ans_str + " ...")
                            else:
                                temp_list.append(ans_str)
                        ans = temp_list
                res = res + ans
            return res
        elif self.node_type == NodeType.KEYWORD:
            return [self.value]
        elif self.node_type == NodeType.LITERAL:
            return [self.value]

    def normal_enumerate(self) -> List[str]:
        if self.node_type == NodeType.OR:
            ans = []
            for child in self.children:
                ans = ans + child.normal_enumerate()
            return ans
        elif (self.node_type == NodeType.WORDS or self.node_type == NodeType.ROOT
              or self.node_type == NodeType.SM_BRACKET
              or self.node_type == NodeType.BIG_BRACKET or self.node_type == NodeType.MID_BRACKET):
            res = []
            flag = False
            last_idx = -1
            while not flag:
                flag = True
                ans = []
                for i in range(len(self.children)):
                    if self.children[i].node_type == NodeType.MID_BRACKET and i > last_idx and flag:
                        flag = False
                        last_idx = i
                        if len(ans) == 0:
                            ans = self.children[i].normal_enumerate()
                        else:
                            temp_list = []
                            for child_str in self.children[i].normal_enumerate():
                                for ans_str in ans:
                                    temp_list.append(ans_str + " " + child_str)
                            ans = temp_list
                    elif self.children[i].node_type != NodeType.MID_BRACKET:
                        if len(ans) == 0:
                            for child_str in self.children[i].normal_enumerate():
                                if self.children[i].node_type == NodeType.SM_BRACKET:
                                    ans.append(" ( " + child_str + " ) ")
                                else:
                                    ans.append(child_str)
                        else:
                            temp_list = []
                            if (self.children[i].node_type == NodeType.SM_BRACKET
                                    and len(self.children[i].normal_enumerate()) == 0):
                                for ans_str in ans:
                                    temp_list.append(ans_str + " ( ) ")
                            else:
                                for child_str in self.children[i].normal_enumerate():
                                    for ans_str in ans:
                                        if self.children[i].node_type == NodeType.SM_BRACKET:
                                            temp_list.append(ans_str + " ( " + child_str + " ) ")
                                        else:
                                            temp_list.append(ans_str + " " + child_str)
                            ans = temp_list
                    else:
                        temp_list = []
                        for ans_str in ans:
                            temp_list.append(ans_str)
                        ans = temp_list
                res = res + ans
            return BnfRuleNode.clear_List(res)
        elif self.node_type == NodeType.KEYWORD:
            return [self.value]
        elif self.node_type == NodeType.LITERAL:
            return [self.value]

    @staticmethod
    def clear_List(list_words: List[str]):
        res = set()
        for words in list_words:
            words_list = words.split()
            res_str = ""
            lower_flag = False
            for word in words_list:
                if lower_flag and only_lower_underscore(word.strip()):
                    continue
                res_str = res_str + word.strip() + " "
                lower_flag = only_lower_underscore(word.strip())
            if not res_str.strip() in res:
                res.add(res_str.strip())
        return list(res)
