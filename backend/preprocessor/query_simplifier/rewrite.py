import os.path

from preprocessor.query_simplifier.load_process import load_json_keywords
from preprocessor.query_simplifier.locate import locate_by_segment
from preprocessor.query_simplifier.tree_matcher import *

from utils.tools import *
from utils.db_connector import sql_execute


# config = load_config()
# dbg = config['dbg']
# use_test = config['use_test']
# reflect_on = config['reflect_on']
# slice_only = config['slice_only']
# mask_on = config['mask_on']
# locate_by_err = config['locate_by_err']

rewrite_keyword_map = {}
rewrite_function_map = {}

rewrite_pieces = []

# model = 'gpt-4o'


def function_rewrite(node: TreeNode, src_dialect: str):
    # Considering the written format of function in the antlr grams, 
    # it is needed to check whether there are difference in Function call
    if src_dialect not in rewrite_keyword_map:
        keyword_table_json, function_table_json = load_json_keywords(src_dialect)
        rewrite_keyword_map[src_dialect] = keyword_table_json
        rewrite_function_map[src_dialect] = function_table_json
    else:
        function_table_json = rewrite_function_map[src_dialect]
    for function in function_table_json:
        if function['Tree'] is None:
            continue
        if check_for_root_node(node, function['Keyword'], function['Tree'], src_dialect):
            return {
                "Node": node,
                "Tree": function['Tree'],
                "Description": function['Description'],
                "Keyword": function['Keyword']
            }
    return None


def keyword_rewrite(node: TreeNode, src_dialect: str):
    # Considering the written format of function in the antlr grams, 
    # it is needed to check whether there are difference in Function call
    if src_dialect not in rewrite_keyword_map:
        keyword_table_json, function_table_json = load_json_keywords(src_dialect)
        rewrite_keyword_map[src_dialect] = keyword_table_json
        rewrite_function_map[src_dialect] = function_table_json
    else:
        keyword_table_json = rewrite_keyword_map[src_dialect]
    to_pick_up_list = []
    cnt_flag = False
    for keyword_list in keyword_table_json:
        if keyword_list['Tree'] is None:
            continue

        for i in range(len(keyword_list['Keyword'])):
            try:
                if keyword_list['Tree'][i] == 'Found error' or keyword_list['Tree'][i] == "Parse error":
                    continue
            except Exception as e:
                print(str(e))
                print("keyword_list['Tree']", keyword_list['Tree'])
                print("keyword_list['Keyword']", keyword_list['Keyword'])
                raise NotImplementedError

            if check_for_root_node(node, keyword_list['Keyword'][i], keyword_list['Tree'][i], src_dialect):
                if 'Count' in keyword_list:
                    cnt_flag = True
                    to_pick_up_list.append({
                        "Tree": keyword_list['Tree'][i],
                        "Description": keyword_list['Description'],
                        "Keyword": keyword_list['Keyword'][i],
                        "Count": keyword_list['Count'][i]
                    })
                else:
                    to_pick_up_list.append({
                        "Tree": keyword_list['Tree'][i],
                        "Description": keyword_list['Description'],
                        "Keyword": keyword_list['Keyword'][i],
                    })
    if cnt_flag:
        sorted(to_pick_up_list, key=lambda x: x["Count"], reverse=True)
    if len(to_pick_up_list) > 0:
        return {
            "Node": node,
            "Tree": to_pick_up_list[0]['Tree'],
            "Description": to_pick_up_list[0]['Description'],
            "Keyword": to_pick_up_list[0]['Keyword']
        }
    return None


def verify_sql(sql: str, dialect: str, db_name: str) -> bool:
    # when change benchmark change here
    return sql_execute(dialect, db_name, sql)


def rewrite(sql, src_dialect, tgt_dialect):
    global rewrite_pieces
    rewrite_pieces = []
    if locate_by_err:
        now_sql = reformat(sql)
        tree_node, line, column, msg = parse_tree(now_sql, tgt_dialect)
        flag = False
        if slice_only:
            if tree_node is None:
                now_sql = rewrite_with_err(now_sql, line, column, msg, src_dialect, tgt_dialect)
                flag = True
        else:
            while tree_node is None:
                now_sql = rewrite_with_err(now_sql, line, column, msg, src_dialect, tgt_dialect)
                tree_node, line, column, msg = parse_tree(now_sql, tgt_dialect)
                flag = True
        verify_flag, _ = verify_sql(now_sql, tgt_dialect, 'tpch')
        if not flag and not verify_flag:
            tree_node, line, column, msg = parse_tree(now_sql, src_dialect)
            ans, flag = rewrite_tree_node(TreeNode.make_g4_tree_by_node(tree_node, src_dialect),
                                          src_dialect, tgt_dialect, True)
            return str(ans), rewrite_pieces
        return now_sql, rewrite_pieces
    else:
        sql_node, line, column, msg = parse_tree(sql, src_dialect)
        if sql_node is None:
            return f"parse error at line: {line}, column: {column}, message: {msg}"
        ans, flag = rewrite_tree_node(TreeNode.make_g4_tree_by_node(sql_node, src_dialect), src_dialect, tgt_dialect,
                                      False)
        return str(ans), rewrite_pieces


def rewrite_tree_node(node: TreeNode, src_dialect, tgt_dialect, only_func) -> (TreeNode, bool):
    flag = False
    for i in range(len(node.children)):
        node.children[i], flag_child = rewrite_tree_node(node.children[i], src_dialect, tgt_dialect, only_func)
        flag = flag or flag_child
    global rewrite_keyword_map
    rewrite_dict = function_rewrite(node, src_dialect)
    if rewrite_dict is not None:
        rewrite_sql = mask_rewrite(rewrite_dict['Node'], rewrite_dict['Tree'],
                                   rewrite_dict['Description'], src_dialect, tgt_dialect,
                                   rewrite_dict['Keyword'])
        return rewrite_sql, True
    if not only_func:
        rewrite_dict = keyword_rewrite(node, src_dialect)
        if rewrite_dict is not None:
            rewrite_sql = mask_rewrite(rewrite_dict['Node'], rewrite_dict['Tree'],
                                       rewrite_dict['Description'], src_dialect, tgt_dialect,
                                       rewrite_dict['Keyword'])
            return rewrite_sql, True
    return node, flag


def locate_tree_node(node: TreeNode, src_dialect, tgt_dialect, only_func):
    for i in range(len(node.children)):
        piece, description = locate_tree_node(node.children[i], src_dialect, tgt_dialect, only_func)
        if piece is None:
            return piece, description
    global rewrite_keyword_map
    rewrite_dict = function_rewrite(node, src_dialect)
    if rewrite_dict is not None:
        return (str(rewrite_dict['Node']),
                rewrite_dict['Description'])
    if not only_func:
        rewrite_dict = keyword_rewrite(node, src_dialect)
        if rewrite_dict is not None:
            return (str(rewrite_dict['Node']),
                    rewrite_dict['Description'])
    return None, None


def mask_rewrite(node: TreeNode, keyword_node: TreeNode,
                 description, src_dialect, tgt_dialect, keyword) -> TreeNode:
    flag, masked_sql, replace_map = try_mark_tree_node(node, keyword_node, {}, src_dialect)
    global rewrite_pieces
    assert flag is True
    if slice_only:
        rewrite_pieces.append({
            "keyword": keyword,
            "slice": masked_sql.strip()
        })
        return node
    res = ask_for_rewrite(masked_sql, description, src_dialect, tgt_dialect, keyword)
    new_root_node = TreeNode('', tgt_dialect, False)
    for split_strs in res.split():
        if split_strs in replace_map:
            new_root_node.add_child(replace_map[split_strs])
        else:
            new_root_node.add_child(TreeNode(split_strs, tgt_dialect, True))
    return new_root_node


def value_equal_check(node_value: str, keyword_value: str):
    return node_value.lower() == keyword_value.lower()


def try_mark_tree_node(node: TreeNode, keyword_node: TreeNode, index_map: Dict, src_dialect):
    masked_sql = ''
    i = 0
    flag = False
    replace_map = {}
    bit_mask = [-1 for _ in range(len(node.children))]
    if len(node.children) == 0:
        if len(keyword_node.children) != 0 or not value_equal_check(node.value, keyword_node.value):
            return False, masked_sql, replace_map
        else:
            return True, node.value, replace_map
    while i < len(node.children) and len(keyword_node.children) > 0:
        if not value_equal_check(node.children[i].value, keyword_node.children[0].value):
            i = i + 1
            continue
        j = 0
        k = 0
        temp_list = []
        temp_replace_map = {}
        sub_sql_list = []
        while i + k < len(node.children) and j < len(keyword_node.children):
            flag1, masked_sql_t, replace_map_t = (
                try_mark_tree_node(node.children[i + k], keyword_node.children[j], index_map, src_dialect))
            if flag1:
                temp_list.append(i + k)
                temp_replace_map = {**temp_replace_map, **replace_map_t}
                j = j + 1
                sub_sql_list.append(masked_sql_t)
            if j == len(keyword_node.children):
                for m in range(len(temp_list)):
                    bit_mask[temp_list[m]] = sub_sql_list[m]
                replace_map = {**temp_replace_map, **replace_map}
                i = i + k
                flag = True
                break
            k = k + 1
        i = i + 1
    global mask_on
    if not mask_on:
        return flag, index_map, reformat(str(node)), replace_map
    for i in range(len(bit_mask)):
        if bit_mask[i] == -1:
            if node.children[i].is_terminal:
                if masked_sql != '':
                    masked_sql = masked_sql + ' '
                masked_sql = masked_sql + node.children[i].value
                replace_map[node.children[i].value] = node.children[i]
            elif len(node.children[i].children) == 0:
                continue
            else:
                if map_expr(node.children[i].value, src_dialect) in index_map:
                    index = index_map[map_expr(node.children[i].value, src_dialect)]
                    index_map[map_expr(node.children[i].value, src_dialect)] = index + 1
                    if masked_sql != '':
                        masked_sql = masked_sql + ' '
                    masked_sql = masked_sql + map_expr(node.children[i].value, src_dialect) + "_" + str(index)
                    replace_map[node.children[i].value + "_" + str(index)] = node.children[i]
                else:
                    index_map[map_expr(node.children[i].value, src_dialect)] = 0
                    if masked_sql != '':
                        masked_sql = masked_sql + ' '
                    masked_sql = masked_sql + map_expr(node.children[i].value, src_dialect)
                    replace_map[node.children[i].value] = node.children[i]
        elif bit_mask[i] != '':
            if masked_sql != '':
                masked_sql = masked_sql + ' '
            masked_sql = masked_sql + bit_mask[i]
    return flag, masked_sql, replace_map


map_name_rep = {}


def map_expr(name: str, dialect: str):
    if dialect not in map_name_rep:
        with open(os.path.join(get_proj_root_path(),
                               'preprocessor', 'query_simplifier',
                               'name_standardize', dialect + '_map.json'), 'r') as map_file:
            json_map = json.load(map_file)
            map_name_rep[dialect] = json_map
    else:
        json_map = map_name_rep[dialect]
    if name in json_map:
        return json_map[name]['name']
    else:
        return name


def ask_for_rewrite(masked_sql: str, description: str, src_dialect: str, tgt_dialect: str, keyword: str):
    map_rep = {
        'pg': 'PostgreSQL',
        'mysql': "MySQL"
    }
    description = description.replace('</CodeLiteral>', "\"")
    description = description.replace('<CodeLiteral>', "\"")
    description = description.replace('</Code>', "\"")
    description = description.replace('<Code>', "\"")
    src_dialect = map_rep[src_dialect]
    tgt_dialect = map_rep[tgt_dialect]
    sys_prompt = ("You are an expert in translating SQL queries between different dialects, "
                  "such as PostgreSQL and MySQL.")
    
    user_prompt = (
        f"Please translate the following SQL expression from {src_dialect} to {tgt_dialect}.\n\n"
        f"Key details:\n"
        f"- The SQL query uses lowercase wildcards (e.g., `expression_1`, `table_1`). "
        f"You may use these wildcards in your response.\n"
        f"- Focus on translating the uppercase keywords to ensure compatibility with {tgt_dialect}.\n"
        f"- Avoid including schema details for tables in the translation unless absolutely necessary.\n\n"
        f"Please proceed step by step:\n"
        f"1. Assess whether the SQL can be translated with adjustments, "
        f"even if significant, and provide the translated version with those adjustments.\n"
        f"2. If you conclude that the translation is 'Unsupported', "
        f"reflect on whether any alternative approaches or workarounds "
        f"could enable a translation that maintains logical equivalence.\n"
        f"3. Only respond with 'Unsupported' if, after careful reflection, "
        f"you determine that a translation is truly impossible in {tgt_dialect}.\n\n"
        f"4. If your translation includes schema information for the tables, please reconsider "
        f"whether there are alternative approaches that allow for the translation without using schema details. "
        f"Provide this alternative version instead, if possible."
        f"The SQL query is:\n\n{masked_sql}\n\n"
        f"Response format:\n"
        f"```json\n"
        f"{{\n"
        f"\t\"Ans\": \"<Translated SQL or 'Unsupported'>\",\n"
        f"\t\"Unsupported\": true if the query cannot be translated, false otherwise,\n"
        f"\t\"Explanation\": "
        f"\"A brief explanation of the translation, including any significant adjustments made, "
        f"the reflection process, or why it's unsupported.\"\n"
        f"}}\n"
        f"```\n"
    )

    if dbg:
        return masked_sql
    else:
        global model
        ans = send_request([], sys_prompt, user_prompt, model=model)
        try:
            json_content = json.loads(extract_json(ans)[0])
            if "Unsupported" in json_content and json_content["Unsupported"]:
                if reflect_on:
                    assert "Explanation" in json_content
                    explanation = json_content['Explanation']

                    reflect_prompt = (
                        f"Please translate the following SQL expression from {src_dialect} to {tgt_dialect}.\n\n"
                        f"Key details:\n"
                        f"- The SQL query uses lowercase wildcards (e.g., `expression_1`, `table_1`). "
                        f"You may use these wildcards in your response.\n"
                        f"- Focus on translating the uppercase keywords to ensure compatibility with {tgt_dialect}.\n\n"
                        f"- Avoid including schema details for tables in the translation "
                        f"unless absolutely necessary.\n\n"
                        f"Please proceed step by step:\n"
                        f"1. Assess whether the SQL can be translated to {tgt_dialect}. "
                        f"Return the translated version, making minor adjustments if necessary.\n"
                        f"2. If significant adjustments are required, provide the translated version "
                        f"along with an explanation of the changes.\n"
                        f"3. Only respond with 'Unsupported' if, after careful consideration, you determine that "
                        f"a translation is truly impossible in {tgt_dialect}, "
                        f"and no workaround can maintain logical equivalence.\n\n"
                        f"4. If your translation includes schema information for the tables, please reconsider "
                        f"whether there are alternative approaches that allow "
                        f"for the translation without using schema details. "
                        f"Provide this alternative version instead, if possible."
                        f"The SQL query is:\n\n{masked_sql}\n\n"
                        f"Response format:\n"
                        f"```json\n"
                        f"{{\n"
                        f"\t\"Ans\": \"<Translated SQL or 'Unsupported'>\",\n"
                        f"\t\"Unsupported\": true if the query cannot be translated, false otherwise,\n"
                        f"\t\"Explanation\": \"A brief explanation of the translation, including any adjustments made, "
                        f"or why it's unsupported.\"\n"
                        f"}}\n"
                        f"```\n"
                        f"Here are some insights for your reference: {explanation}"
                    )

                    ans_reflect = send_request([], sys_prompt, reflect_prompt, model=model)
                    json_content_reflect = json.loads(extract_json(ans_reflect)[0])
                    if "Unsupported" in json_content_reflect and json_content_reflect["Unsupported"]:
                        res = "Unsupported"
                    else:
                        assert "Ans" in json_content_reflect
                        res = json_content_reflect["Ans"]
                        explanation = json_content_reflect["Explanation"]
                else:
                    res = "Unsupported"
                    explanation = json_content["Explanation"]
            else:
                assert "Ans" in json_content
                res = json_content["Ans"]
                explanation = json_content["Explanation"]
            rewrite_pieces.append({
                "keyword": keyword,
                "slice": masked_sql.strip(),
                "rewrite_piece": res,
                "explanation": explanation
            })
            return res
        except Exception as e:
            return ans


def reformat(sql):
    res = self_split(sql)
    ans = ''
    for word in res:
        if word != '':
            ans = ans + word + " "
    return ans.strip()


def get_masked_slices(piece: Dict, src_dialect):
    ori_sql = str(piece['Node'])
    flag, masked_sql, replace_map = try_mark_tree_node(piece['Node'], piece['Tree'], {}, src_dialect)
    rep_replace_map = {}
    for key, value in replace_map.items():
        rep_replace_map[key] = str(value)
    return {
        "ori_sql": ori_sql,
        "masked_sql": reformat(masked_sql),
        'keyword': piece['Keyword'],
        "replace_map": rep_replace_map
    }


def rewrite_with_err(sql, tgt_line, tgt_col, tgt_msg, src_dialect, tgt_dialect) -> str:
    tree_node, line, column, msg = parse_tree(sql, src_dialect)
    assert sql is not None
    root_node = TreeNode.make_g4_tree_by_node(tree_node, src_dialect)
    node, now_str = TreeNode.locate_node(root_node, tgt_col, sql)
    while node.father is not None and len(node.father.children) == 1:
        node = node.father
    times = 1
    while times > 0 and node.father is not None:
        node = node.father
        times = times - 1
    ans, flag = rewrite_tree_node(node, src_dialect, tgt_dialect, False)
    step = 1
    while not flag:
        for i in range(step):
            node = node.father
        ans, flag = rewrite_tree_node(node, src_dialect, tgt_dialect, False)
    if node.father is not None:
        node.father.replace_child(node, ans)
        return str(root_node)
    else:
        return str(ans)


def locate_with_err(sql, tgt_line, tgt_col, tgt_msg, src_dialect, tgt_dialect):
    tree_node, line, column, msg = parse_tree(sql, src_dialect)
    assert sql is not None
    root_node = TreeNode.make_g4_tree_by_node(tree_node, src_dialect)
    node, now_str = TreeNode.locate_node(root_node, tgt_col, sql)
    while node.father is not None and len(node.father.children) == 1:
        node = node.father
    times = 1
    while times > 0 and node.father is not None:
        node = node.father
        times = times - 1
    piece, desc = locate_tree_node(node, src_dialect, tgt_dialect, False)
    step = 1
    while desc is None:
        for i in range(step):
            node = node.father
            if node.father is None:
                break
        piece, desc = locate_tree_node(node, src_dialect, tgt_dialect, False)
    return piece, desc


def locate_error(sql, src_dialect, tgt_dialect):
    global rewrite_pieces
    rewrite_pieces = []
    if locate_by_err:
        now_sql = reformat(sql)
        tree_node, line, column, msg = parse_tree(now_sql, tgt_dialect)
        if tree_node is None:
            piece, desc = locate_with_err(now_sql, line, column, msg, src_dialect, tgt_dialect)
            if piece is not None:
                return piece, desc
        verify_flag, _ = verify_sql(now_sql, tgt_dialect, 'tpch')
        if not verify_flag:
            tree_node, line, column, msg = parse_tree(now_sql, src_dialect)
            piece, desc = locate_tree_node(TreeNode.make_g4_tree_by_node(tree_node, src_dialect),
                                           src_dialect, tgt_dialect, True)
            return piece, desc
        return None, None
    else:
        raise ValueError("must execute in locate_by_err mode")


def slice_all(node: TreeNode, src_dialect, only_func) -> List[Dict]:
    """
    List of
    {
        "Node": node,
        "Tree": function['Tree'],
        "Description": function['Description'],
        "Keyword": function['Keyword'],
        "SubPieces": sub-pieces,
        "FatherPieces": father-pieces
    }
    """
    res = []
    for i in range(len(node.children)):
        child_res = slice_all(node.children[i], src_dialect, only_func)
        res = res + child_res
    global rewrite_keyword_map
    rewrite_dict = function_rewrite(node, src_dialect)
    if rewrite_dict is not None:
        res.append(rewrite_dict)
    if not only_func:
        rewrite_dict = keyword_rewrite(node, src_dialect)
        if rewrite_dict is not None:
            res.append(rewrite_dict)
    return res


def dfs_res(node: TreeNode, node2piece: Dict):
    sub_pieces = []
    for child in node.children:
        if child in node2piece and 'SubPieces' in node2piece[child]:
            sub_pieces = sub_pieces + node2piece[child]['SubPieces'] + [node2piece[child]]
        else:
            sub_pieces = sub_pieces + dfs_res(child, node2piece)
    if node in node2piece:
        node2piece[node]['SubPieces'] = sub_pieces
        return sub_pieces + [node2piece[node]]
    return sub_pieces


# directly slice all the pieces and then sort using the error info
def get_all_piece(tree_node: TreeNode, src_dialect) -> tuple[List[Dict], TreeNode]:
    root_node = TreeNode.make_g4_tree_by_node(tree_node, src_dialect)
    res = slice_all(root_node, src_dialect, False)
    node2piece = {}
    for piece in res:
        node2piece[piece['Node']] = piece
    for piece in res:
        if 'SubPieces' not in piece:
            dfs_res(piece['Node'], node2piece)
    for piece in res:
        piece['FatherPiece'] = search_upward(piece, node2piece)
        piece['Count'] = 0
        piece['TrackPieces'] = []
    return res, root_node


def get_all_model_ans_nodes(root_node: TreeNode) -> List[TreeNode]:
    res = []
    for child in root_node.children:
        res = res + get_all_model_ans_nodes(child)
    if root_node.model_get:
        res.append(root_node)
    return res


def get_all_tgt_used_piece(now_sql, tgt_dialect, src_root_node):
    if 'MySQL' in tgt_dialect:
        tgt_dialect = 'mysql'
    elif 'PostgreSQL' in tgt_dialect:
        tgt_dialect = 'pg'
    elif 'Oracle' in tgt_dialect:
        tgt_dialect = 'oracle'
    else:
        raise ValueError(f"{tgt_dialect} is not supported yet")
    try:
        tree_node, line, col, msg = parse_tree(now_sql, tgt_dialect)
        if tree_node is None:
            raise ValueError(f"Parse error when executing ANTLR parser of {tgt_dialect}.\n"
                             f"The sql is {now_sql}")
        tgt_all_pieces, root_node = get_all_piece(tree_node, tgt_dialect)
        model_answer_nodes = get_all_model_ans_nodes(src_root_node)
        pieces = []
        node2piece = {}
        for piece in tgt_all_pieces:
            node2piece[piece['Node']] = piece
        for model_answer_node in model_answer_nodes:
            pieces.append(
                locate_by_segment(now_sql, model_answer_node.value,
                                  tgt_all_pieces, node2piece, root_node)
            )
        return pieces
    except Exception as e:
        if (isinstance(e, ValueError)
                and str(e).startswith('Parse error when executing ANTLR parser of')):
            print_err("No desc can be provided because of Antlr Parse Error")
            return []
        else:
            raise e


def search_upward(piece, node2piece: Dict):
    node = piece['Node']
    while True:
        node = node.father
        if node is None:
            return None
        if node in node2piece:
            return node2piece[node]
