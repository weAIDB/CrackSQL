import json


def remove_redundant_paren(target_str: str) -> str:
    terms = target_str.split()
    res = ""
    left_paren = 0
    for term in terms:
        if term == '(':
            res = res + " ( "
            left_paren = left_paren + 1
        elif term == ')' and left_paren > 0:
            res = res + " ) "
            left_paren = left_paren - 1
        elif term != ")":
            res = res + " " + term + " "
        else:
            print("clean")
    return res


def remake_paren(target_str: str):
    terms = target_str.split()
    res = ""
    i = 0
    while i < len(terms):
        if terms[i] == '(':
            if terms[i + 1] != ')':
                res = res + " (" + terms[i + 1] + " "
                i = i + 1
            else:
                res = res + " ( "
        else:
            res = res + " " + terms[i] + " "
        i = i + 1
    return res


def all_r_bracket(term):
    for char in term:
        if char != ')':
            return False
    return True


def remake_r_paren(target_str: str):
    terms = target_str.split()
    res = ""
    i = 0
    while i < len(terms):
        if terms[i] == ')':
            if terms[i - 1] == '(':
                res = res + " ) "
            else:
                res = res + ")"
        elif all_r_bracket(terms[i]):
            res = res + terms[i]
        else:
            res = res + " " + terms[i]
        i = i + 1
    return res


def clean_paren(file_path: str):
    """
    used to clean the redundant paren of the tree representation
    """
    res = []
    with open(file_path, 'r') as file:
        keyword_table = json.loads(file.read())

        for keyword in keyword_table:
            new_tree = []
            for tree in keyword["Tree"]:
                new_tree.append(remove_redundant_paren(tree))
            res.append({
                "Keyword": keyword["Keyword"],
                "Src": keyword["Src"],
                "Tree": new_tree,
                "Route": keyword["Route"],
                "Description": keyword["Description"],
                "Demo": keyword["Demo"]
            })
    with open(file_path + "backup", 'w') as file:
        json.dump(res, file, indent=4)


def paren_remake(file_path: str):
    """
    used to make ( and keyword name together
    """
    res = []
    with open(file_path, 'r') as file:
        keyword_table = json.loads(file.read())

        for keyword in keyword_table:
            new_tree = []
            for tree in keyword["Tree"]:
                new_tree.append(remake_paren(tree))
            res.append({
                "Keyword": keyword["Keyword"],
                "Src": keyword["Src"],
                "Tree": new_tree,
                "Route": keyword["Route"],
                "Description": keyword["Description"],
                "Demo": keyword["Demo"]
            })
    with open(file_path + "backup", 'w') as file:
        json.dump(res, file, indent=4)


def paren_r_remake(file_path: str):
    """
    used to make ( and keyword name together
    """
    res = []
    with open(file_path, 'r') as file:
        keyword_table = json.loads(file.read())

        for keyword in keyword_table:
            new_tree = []
            for tree in keyword["Tree"]:
                new_tree.append(remake_r_paren(tree))
            res.append({
                "Keyword": keyword["Keyword"],
                "Src": keyword["Src"],
                "Tree": new_tree,
                "Route": keyword["Route"],
                "Description": keyword["Description"],
                "Demo": keyword["Demo"]
            })
    with open(file_path + "1", 'w') as file:
        json.dump(res, file, indent=4)


def remake(file_path: str):
    """
    used to make ( and keyword name together
    """
    res = []
    with open(file_path, 'r') as file:
        keyword_table = json.loads(file.read())

        for keyword in keyword_table:
            new_tree = []
            for tree in keyword["Tree"]:
                new_tree.append(remake_r_paren(remake_paren(remove_redundant_paren(tree))))
            res.append({
                "Keyword": keyword["Keyword"],
                "Src": keyword["Src"],
                "Tree": new_tree,
                "Route": keyword["Route"],
                "Description": keyword["Description"],
                "Demo": keyword["Demo"]
            })
    with open(file_path + "1", 'w') as file:
        json.dump(res, file, indent=4)
