import os
import json

from api.services.knowledge import get_json_items
from preprocessor.query_simplifier.Tree import TreeNode


def load_json_keywords(kb_name: str, dialect: str):
    if os.path.isfile(kb_name):
        with open(kb_name, "r") as rf:
            items = json.load(rf)
    else:
        items = get_json_items(kb_name, all_item=True)

    keyword_table_json, function_table_json = list(), list()
    for item in items:
        if not os.path.isfile(kb_name):
            item = json.loads(item.content)
        if item['tree'] == "Parse error" or item['tree'] == "Found error":
            continue
        item["tree"] = TreeNode.make_g4_tree(item['tree'], dialect)

        if item["type"] == "function":
            function_table_json.append(item)
        else:
            keyword_table_json.append(item)

    return keyword_table_json, function_table_json
