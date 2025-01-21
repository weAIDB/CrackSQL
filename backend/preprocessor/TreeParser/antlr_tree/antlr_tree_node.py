from enum import Enum


class NodeType(Enum):
    OR = 1
    KEYWORD = 2
    NONE_KEYWORD = 3
    WORDS = 4
    LITERAL = 5
    SM_BRACKET = 6
    BIG_BRACKET = 7
    ROOT_KEYWORD = 8
    ROOT_NONE_KEYWORD = 9


class RepeatType(Enum):
    """
        Used to mark repeatable cases, corresponding to non-repeatable, +,? , *
    """
    NONE = 0
    PLUS = 1
    QUES = 2
    STAR = 3


class AntlrRuleNode:
    def __init__(self, value: str, node_type: NodeType, repeat_type=RepeatType.NONE, father=None, children=None):
        """
        Initialize a multi-tree node
        :type: node type
        :param father: parent node
        :param children: child list (empty by default)
        """
        self.node_type = node_type
        self.repeat_type = repeat_type
        self.value = value
        self.children = children if children is not None else []
        self.child_link = {}
        self.father = father
        self.link = None
        self.father_link = {}
        self.father_set = set()

    def __str__(self):
        res_str = ''
        if self.node_type == NodeType.WORDS:
            for i in range(len(self.children)):
                res_str = res_str + ' ' + str(self.children[i])
            return res_str
        elif self.node_type == NodeType.SM_BRACKET:
            res_str = ' ( '
            for i in range(len(self.children)):
                res_str = res_str + ' ' + str(self.children[i])
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

    def link_to(self, node, root_node):
        self.link = node
        node.father_link.setdefault(root_node, []).append(self)
        root_node.child_link.setdefault(node, []).append(self)

    def add_father_set(self, node):
        self.father_set.add(node)

    def clear_child(self):
        self.children.clear()

    def get_derived_type(self):
        if self.node_type == NodeType.ROOT_KEYWORD:
            return NodeType.KEYWORD
        elif self.node_type == NodeType.ROOT_NONE_KEYWORD:
            return NodeType.NONE_KEYWORD
        else:
            return self.node_type
