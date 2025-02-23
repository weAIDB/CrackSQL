import json
import os
import sys
from glob import glob
from typing import List

from api.services.knowledge import get_json_items
from preprocessor.query_simplifier.Tree import TreeNode


# from utils.tools import load_config

# config = load_config()
# dbg = config['dbg']
# use_test = config['use_test']
# use_type = True


def load_json_keywords(kb_name: str, dialect: str):
    items = get_json_items(kb_name, all_item=True)
    keyword_table_json, function_table_json = list(), list()
    for item in items:
        item = json.loads(item.content)
        if item['tree'] == "Parse error" or item['tree'] == "Found error" or item['tree'] == "1":
            continue
        # print(item['tree'])
        item["tree"] = TreeNode.make_g4_tree(item['tree'], dialect)

        if item["type"] == "function":
            function_table_json.append(item)
        else:
            keyword_table_json.append(item)

    return keyword_table_json, function_table_json


def load_json_keywords_bak(kb_name: str, dialect: str):
    script_path = os.path.abspath(__file__)
    retrieve_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(script_path))),
                                 'data', 'processed_document', dialect)
    try:
        keyword_json_files = glob(os.path.join(retrieve_path, "*keyword_ready.json"))
        keywords_json = []
        for file_path in keyword_json_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                keywords_json = keywords_json + keyword_load_preprocess(json.loads(file.read()), dialect)
        print("keyword_load_preprocess", keywords_json)
    except Exception as e:
        raise e

    try:
        op_json_files = glob(os.path.join(retrieve_path, "*operator_ready.json"))
        for file_path in op_json_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                keywords_json = keywords_json + op_load_preprocess(json.loads(file.read()), dialect)
        print("op_load_preprocess", keywords_json)
    except Exception as e:
        raise e

    try:
        type_json_files = glob(os.path.join(retrieve_path, "*type_ready.json"))
        for file_path in type_json_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                keywords_json = keywords_json + type_load_preprocess(json.loads(file.read()), dialect)
        print("type_load_preprocess", keywords_json)
    except Exception as e:
        raise e

    # replace all the str_rep in the keyword_json to be the TreeNode
    # Unified as Keyword, Description, Tree
    try:
        functions_json_files = glob(os.path.join(retrieve_path, "*function_ready.json"))
        functions_json = []
        for file_path in functions_json_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                json_array = json.loads(file.read())
                functions_json = functions_json + func_load_preprocess(json_array, dialect)
        print("func_load_preprocess", keywords_json)
    except Exception as e:
        raise e
    return keywords_json, functions_json


def keyword_load_preprocess(json_array: List, dialect: str):
    if dialect == 'mysql':
        return mysql_keyword_process(json_array)
    elif dialect == 'pg':
        return pg_keyword_process(json_array)
    elif dialect == 'oracle':
        return oracle_keyword_process(json_array)
    else:
        raise ValueError(dialect + "keyword is not support yet")


def mysql_keyword_process(json_array: List):
    for keyword_list in json_array:
        new_tree_list = []
        for tree_rep in keyword_list["Tree"]:
            if tree_rep != 'Found error' and tree_rep != "Parse error":
                new_tree_list.append(TreeNode.make_g4_tree(tree_rep, 'mysql'))
            else:
                new_tree_list.append(tree_rep)

        keyword_list["Name"] = "; ".join(keyword_list["Keyword"][:3])

        keyword_list["KEYWORD"] = list()
        for field in ["Name"]:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["KEYWORD"].extend(content)
            else:
                keyword_list["KEYWORD"].append(str(content))
        keyword_list["KEYWORD"] = "<sep>".join(map(str, keyword_list["KEYWORD"]))

        keyword_list["DESC"] = list()
        for field in ['Description', 'Demo', 'Detail']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["DESC"].extend(content)
            else:
                keyword_list["DESC"].append(str(content))
        keyword_list["DESC"] = "<sep>".join(map(str, keyword_list["DESC"]))

        keyword_list["Tree"] = new_tree_list
        keyword_list['Description'] = {
            "Type": 'Keyword',
            "Desc": keyword_list['Description'],
            "KEYWORD": keyword_list["KEYWORD"],
            "DESC": keyword_list["DESC"]
        }

    return json_array


def pg_keyword_process(json_array: List):
    for keyword_list in json_array:
        new_tree_list = []
        for tree_rep in keyword_list["Tree"]:
            if tree_rep != 'Found error' and tree_rep != "Parse error":
                new_tree_list.append(TreeNode.make_g4_tree(tree_rep, 'pg'))
            else:
                new_tree_list.append(tree_rep)

        keyword_list["Name"] = "; ".join(keyword_list["Keyword"][:3])

        keyword_list["KEYWORD"] = list()
        for field in ['Name']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["KEYWORD"].extend(content)
            else:
                keyword_list["KEYWORD"].append(str(content))
        keyword_list["KEYWORD"] = "<sep>".join(map(str, keyword_list["KEYWORD"]))

        keyword_list["DESC"] = list()
        for field in ['Description', 'Demo']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["DESC"].extend(content)
            else:
                keyword_list["DESC"].append(str(content))
        keyword_list["DESC"] = "<sep>".join(map(str, keyword_list["DESC"]))

        keyword_list["Tree"] = new_tree_list
        keyword_list['Description'] = {
            "Type": 'Keyword',
            "Desc": keyword_list['Description'],
            "KEYWORD": keyword_list["KEYWORD"],
            "DESC": keyword_list["DESC"]
        }

    return json_array


def oracle_keyword_process(json_array: List):
    for keyword_list in json_array:
        new_tree_list = []
        if keyword_list["Tree"] is None:
            new_tree_list = ['Parse error' for _ in keyword_list['Keyword']]
        else:
            for tree_rep in keyword_list["Tree"]:
                if tree_rep != 'Found error' and tree_rep != "Parse error":
                    new_tree_list.append(TreeNode.make_g4_tree(tree_rep, 'oracle'))
                else:
                    new_tree_list.append(tree_rep)

        keyword_list["Name"] = "; ".join(keyword_list["Keyword"][:3])

        keyword_list["KEYWORD"] = list()
        for field in ["Name"]:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["KEYWORD"].extend(content)
            else:
                keyword_list["KEYWORD"].append(str(content))
        keyword_list["KEYWORD"] = "<sep>".join(map(str, keyword_list["KEYWORD"]))

        keyword_list["DESC"] = list()
        for field in ['Description', 'Demo']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["DESC"].extend(content)
            else:
                keyword_list["DESC"].append(str(content))
        keyword_list["DESC"] = "<sep>".join(map(str, keyword_list["DESC"]))

        keyword_list["Tree"] = new_tree_list
        keyword_list['Description'] = {
            "Type": 'Keyword',
            "Desc": keyword_list['Description'],
            "KEYWORD": keyword_list["KEYWORD"],
            "DESC": keyword_list["DESC"]
        }

    return json_array


def func_load_preprocess(json_array: List, dialect: str):
    if dialect == 'mysql':
        return mysql_func_process(json_array)
    elif dialect == 'pg':
        return pg_func_process(json_array)
    elif dialect == 'oracle':
        return oracle_func_process(json_array)
    else:
        raise ValueError(dialect + "function is not support yet")


def mysql_func_process(json_array: List):
    res = []
    for ele in json_array:
        desc = ele['Description'][0] + (f"\nThe detail about the {ele['Name']} is:\n "
                                        f"{ele['Detail']}")
        if len(ele['Demo']) != 0:
            desc = desc + f"\nThe example of the {ele['Name']} is:\n"
            for demo in ele['Demo']:
                desc = desc + demo + '\n'

        ele["KEYWORD"] = list()
        for field in ["Name"]:
            content = ele.get(field, "")
            if isinstance(content, list):
                ele["KEYWORD"].extend(content)
            else:
                ele["KEYWORD"].append(content)
        ele["KEYWORD"] = "<sep>".join(ele["KEYWORD"])

        ele["DESC"] = list()
        for field in ['Description', 'Demo', 'Detail']:
            content = ele.get(field, "")
            if isinstance(content, list):
                ele["DESC"].extend(content)
            else:
                ele["DESC"].append(content)
        ele["DESC"] = "<sep>".join(ele["DESC"])

        ans = {
            "Keyword": ele['Name'],
            "Tree": TreeNode.make_g4_tree(ele['Tree'], 'mysql'),
            "Description": {
                "Type": 'Function',
                "Desc": ele['Description'][0],
                "KEYWORD": ele["KEYWORD"],
                "DESC": ele["DESC"]
            },

        }
        res.append(ans)
    return res


def oracle_func_process(json_array: List):
    res = []
    for ele in json_array:
        if ele['Tree'] is None or ele['Tree'] == 'Parse error':
            continue

        ele["KEYWORD"] = list()
        for field in ["Name"]:
            content = ele.get(field, "")
            if isinstance(content, list):
                ele["KEYWORD"].extend(content)
            else:
                ele["KEYWORD"].append(content)
        ele["KEYWORD"] = "<sep>".join(ele["KEYWORD"])

        ele["DESC"] = list()
        for field in ['Description']:
            content = ele.get(field, "")
            if isinstance(content, list):
                ele["DESC"].extend(content)
            else:
                ele["DESC"].append(content)
        ele["DESC"] = "<sep>".join(ele["DESC"])

        ans = {
            "Keyword": ele['Name'],
            "Tree": TreeNode.make_g4_tree(ele['Tree'], 'oracle'),
            "Description": {
                "Type": 'Function',
                "Desc": ele['Description'],
                "KEYWORD": ele["KEYWORD"],
                "DESC": ele["DESC"]
            },

        }
        res.append(ans)
    return res


def pg_func_process(json_array: List):
    res = []
    for table in json_array:
        """
        "Function": "sha384(bytea)",
        "Return Type": "bytea",
        "Description": "SHA-384 hash",
        """
        i = 1
        while i < len(table):
            name = table[i]['Function']
            desc = ""
            if 'Return Type' in table[i]:
                desc = desc + "The return type of " + name + " is " + table[i]['Return Type'] + ". "
            if 'Description' in table[i]:
                desc = desc + "The description of " + name + " is \'" + table[i]['Description'] + "\'. "

            table[i]["Name"] = list(table[i].values())[0]

            KEYWORD = list()
            for field in ["Name", 'Argument Type', 'Argument Type(s)',
                          'Aggregated Argument Type(s)',
                          'Direct Argument Type(s)', 'Return Type']:
                content = table[i].get(field, "")
                if isinstance(content, list):
                    KEYWORD.extend(content)
                else:
                    KEYWORD.append(content)
            KEYWORD = "<sep>".join(KEYWORD)

            DESC = list()
            for field in ['Description', 'Example', 'Result',
                          'Example Query', 'Example Result',
                          'compensate']:
                content = table[i].get(field, "")
                if isinstance(content, list):
                    DESC.extend(content)
                else:
                    DESC.append(content)
            DESC = "<sep>".join(DESC)

            ans = {
                "Keyword": name,
                "Tree": TreeNode.make_g4_tree(table[i]['Tree'], 'pg'),
                "Description": {
                    "Type": 'Function',
                    "Desc": desc.strip(),
                    "KEYWORD": KEYWORD,
                    "DESC": DESC
                },

            }
            i = i + 1
            res.append(ans)
    return res


def type_load_preprocess(json_array: List, dialect: str):
    if dialect == 'mysql':
        return mysql_type_process(json_array)
    elif dialect == 'pg':
        return pg_type_process(json_array)
    elif dialect == 'oracle':
        return oracle_type_process(json_array)
    else:
        raise ValueError(dialect + "keyword is not support yet")


def mysql_type_process(json_array: List):
    res = []
    for keyword_list in json_array:
        new_tree_list = []

        for tree_rep in keyword_list["Tree"]:
            if tree_rep != 'Found error' and tree_rep != "Parse error":
                new_tree_list.append(TreeNode.make_g4_tree(tree_rep, 'mysql'))
            else:
                new_tree_list.append(tree_rep)

        desc = f"The description of {keyword_list['Type'][0]} are as follows:\n"
        for description in keyword_list['Description']:
            desc = desc + description + '\n'

        for key, value in keyword_list.items():
            if key not in ['Link', 'Type', 'Tree', 'Description', 'Compensate']:
                desc = desc + f"The {key} of {keyword_list['Type'][0]} is {value}. "

        keyword_list["Name"] = ";".join(keyword_list["Type"])

        keyword_list["KEYWORD"] = list()
        for field in ["Name"]:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["KEYWORD"].extend(content)
            else:
                keyword_list["KEYWORD"].append(content)
        keyword_list["KEYWORD"] = "<sep>".join(keyword_list["KEYWORD"])

        keyword_list["DESC"] = list()
        for field in ['Description', 'Storage (Bytes)',
                      'Minimum Value Signed', 'Maximum Value Signed', 'Compensate']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["DESC"].extend(content)
            else:
                keyword_list["DESC"].append(content)
        keyword_list["DESC"] = "<sep>".join(keyword_list["DESC"])

        ans = {
            "Keyword": keyword_list['Type'],
            "Tree": new_tree_list,
            "Description": {
                "Type": 'Type',
                "Desc": desc.strip(),
                "KEYWORD": keyword_list["KEYWORD"],
                "DESC": keyword_list["DESC"]
            },

        }
        res.append(ans)
    return res


def pg_type_process(json_array: List):
    res = []
    for keyword_list in json_array:
        new_tree_list = []

        for tree_rep in keyword_list["Tree"]:
            if tree_rep != 'Found error' and tree_rep != "Parse error":
                new_tree_list.append(TreeNode.make_g4_tree(tree_rep, 'mysql'))
            else:
                new_tree_list.append(tree_rep)

        desc = f"The description of {keyword_list['Type'][0]} are as follows:\n"
        for description in keyword_list['Description']:
            desc = desc + description + '\n'

        for key, value in keyword_list.items():
            if key not in ['Link', 'Type', 'Tree', 'Description', 'Compensate']:
                desc = desc + f"The {key} of {keyword_list['Type'][0]} is {value}. "

        keyword_list["Name"] = ";".join(keyword_list["Type"])

        keyword_list["KEYWORD"] = list()
        for field in ['Name']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["KEYWORD"].extend(content)
            else:
                keyword_list["KEYWORD"].append(content)
        keyword_list["KEYWORD"] = "<sep>".join(keyword_list["KEYWORD"])

        keyword_list["DESC"] = list()
        for field in ['Description', 'Storage Size', 'Range',
                      'Low Value', 'High Value', 'Compensate']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["DESC"].extend(content)
            else:
                keyword_list["DESC"].append(content)
        keyword_list["DESC"] = "<sep>".join(keyword_list["DESC"])

        ans = {
            "Keyword": keyword_list['Type'],
            "Tree": new_tree_list,
            "Description": {
                "Type": 'Type',
                "Desc": desc.strip(),
                "KEYWORD": keyword_list["KEYWORD"],
                "DESC": keyword_list["DESC"]
            },
        }
        res.append(ans)
    return res


def oracle_type_process(json_array: List):
    res = []
    for keyword_list in json_array:
        new_tree_list = []
        for tree_rep in keyword_list["Tree"]:
            if tree_rep != 'Found error' and tree_rep != "Parse error":
                new_tree_list.append(TreeNode.make_g4_tree(tree_rep, 'oracle'))
            else:
                new_tree_list.append(tree_rep)

        keyword_list["Name"] = keyword_list["Type"]

        keyword_list["KEYWORD"] = list()
        for field in ["Name"]:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["KEYWORD"].extend(content)
            else:
                keyword_list["KEYWORD"].append(content)
        keyword_list["KEYWORD"] = "<sep>".join(keyword_list["KEYWORD"])

        keyword_list["DESC"] = list()
        for field in ['Description']:
            content = keyword_list.get(field, "")
            if content == "":
                continue

            if isinstance(content, list):
                keyword_list["DESC"].extend(content)
            else:
                keyword_list["DESC"].append(content)
        keyword_list["DESC"] = "<sep>".join(keyword_list["DESC"])

        desc = f"The description of {keyword_list['Type']} are as follows:\n"
        desc = desc + keyword_list['Description'] + '\n'
        for key, value in keyword_list.items():
            if key not in ['Link', 'Type', 'Tree', 'Description', 'Compensate']:
                desc = desc + f"The {key} of {keyword_list['Type']} is {value}. "

        ans = {
            "Keyword": [keyword_list['Type']],
            "Tree": new_tree_list,
            "Description": {
                "Type": 'Type',
                "Desc": desc.strip(),
                "KEYWORD": keyword_list["KEYWORD"],
                "DESC": keyword_list["DESC"]
            },
        }
        res.append(ans)
    return res


def op_load_preprocess(json_array: List, dialect: str):
    if dialect == 'pg':
        return pg_op_loader(json_array)
    if dialect == 'mysql':
        return mysql_op_loader(json_array)
    else:
        print(f"{dialect}'s operator is not supported yet", file=sys.stderr)


def pg_op_loader(json_array: List):
    res = []
    for op in json_array:
        new_tree_list = [TreeNode.make_g4_tree(op['Tree'], 'pg')]

        desc = f"The description of {op['Operator']} are as follows:\n"
        desc = desc + op['Description'] + '\n'

        for key, value in op.items():
            if key not in ['Link', 'Operator', 'Tree', 'Description', 'Compensate']:
                desc = desc + f"The {key} of {op['Operator']} is {value}. "

        ans = {
            "Keyword": [op['Operator']],
            "Tree": new_tree_list,
            "Description": {
                "Type": 'Function',
                "Desc": desc.strip()
            }
        }
        res.append(ans)
    return res


def mysql_op_loader(json_array: List):
    res = []
    for op in json_array:
        new_tree_list = [TreeNode.make_g4_tree(op['Tree'], 'mysql')]

        desc = f"The description of {op['Operator']} are as follows:\n"
        desc = desc + op['Description'] + '\n'

        for key, value in op.items():
            if key not in ['Link', 'Operator', 'Tree', 'Description', 'Compensate']:
                desc = desc + f"The {key} of {op['Operator']} is {value}. "

        ans = {
            "Keyword": [op['Operator']],
            "Tree": new_tree_list,
            "Description": {
                "Type": 'Function',
                "Desc": desc.strip()
            }
        }
        res.append(ans)
    return res


if __name__ == "__main__":
    # mysql, pg, oracle
    src_dialect = "mysql"
    keyword_table_json, function_table_json = load_json_keywords_bak(src_dialect)

    src_dialect = "pg"
    keyword_table_json_pg, function_table_json_pg = load_json_keywords_bak(src_dialect)

    src_dialect = "oracle"
    keyword_table_json_oracle, function_table_json_oracle = load_json_keywords_bak(src_dialect)

    print(1)
