import json
import os.path

from CrackSQL.preprocessor.antlr_parser.parse_tree import parse_tree
from CrackSQL.utils.tools import get_proj_root_path


def mark_mysql_tree(tree_rep: str, func_name: str):
    reps = tree_rep.split()
    i = 0
    while i < len(reps):
        if reps[i] == '(functionCall':
            i = i + 1
            break
        i = i + 1
    ans = '(functionCall'
    j = 0
    while i < len(reps):
        if reps[i][0] == '(' and len(reps[i]) != 1:
            j = j + 1
            ans = ans + " " + reps[i]
        else:
            if reps[i].lower().find(func_name.lower()) == -1:
                t = -1
                while reps[t] == ')':
                    t = t - 1
                assert t + j == -1
            ans = ans + " " + reps[i]
            break
        i = i + 1
    ans = ans + " ( ))"
    return ans


def make_mysql_function_tree():
    with open(os.path.join(get_proj_root_path(),
                           'data', 'processed_document',
                           'mysql', 'mysql_8.4_built-in-function.json')) as file:
        json_array = json.loads(file.read())
    mysql_res = []
    todo_res = []
    for ele in json_array:
        desc = ele['Description'],
        link = ele['Link'],
        detail = ele['Detail']
        names = ele['Name'].split(',')
        for name in names:
            if '()' in name and (name[-1] == ')' and name[-2] == '('):
                name1 = name[:-2].strip()
                sql = 'SELECT ' + name1 + '(1);'
                tree_rep = parse_tree(sql, 'mysql')
                if tree_rep is None or '(functionCall' not in tree_rep:
                    todo_res.append({
                        'Name': name,
                        'Description': desc,
                        'Link': link,
                        'Detail': detail
                    })
                else:
                    mysql_res.append({
                        'Name': name1,
                        'Tree': mark_mysql_tree(tree_rep, name1),
                        'Description': desc,
                        'Link': link,
                        'Detail': detail
                    })
            else:
                todo_res.append({
                    'Name': name,
                    'Description': desc,
                    'Link': link,
                    'Detail': detail
                })
    with open('mysql_function_ready.json', 'w') as file:
        json.dump(mysql_res, file, indent=4)
    with open('mysql_function_todo.json', 'w') as file:
        json.dump(todo_res, file, indent=4)


def mark_pg_tree(tree_rep: str, func_name: str, bracket_flag):
    # func_application
    # func_expr_common_subexpr
    if 'func_application' in tree_rep:
        reps = tree_rep.split()
        i = 0
        while i < len(reps):
            if reps[i] == '(func_application':
                i = i + 1
                break
            i = i + 1
        ans = '(func_application'
    elif 'func_expr_common_subexpr' in tree_rep:
        reps = tree_rep.split()
        i = 0
        while i < len(reps):
            if reps[i] == '(func_expr_common_subexpr':
                i = i + 1
                break
            i = i + 1
        ans = '(func_expr_common_subexpr'
    else:
        return None
    j = 0
    while i < len(reps):
        if reps[i][0] == '(' and len(reps[i]) != 1:
            j = j + 1
            ans = ans + " " + reps[i]
        else:
            if reps[i].lower().find(func_name.lower()) == 0:
                ans = ans + " " + func_name.lower()
                for k in range(j):
                    ans = ans + ')'
            break
        i = i + 1
    if bracket_flag:
        ans = ans + " ( ))"
    else:
        ans = ans + ")"
    print(tree_rep)
    print(ans)
    return ans


def make_pg_func_tree():
    with open(os.path.join(get_proj_root_path(),
                           'data', 'processed_document',
                           'pg', 'pg_14_built-in-function.json')) as file:
        json_array = json.loads(file.read())
    pg_func_res = []
    todo_func_res = []
    set1 = set()
    for table in json_array:
        table_res = []
        table_todo_res = []
        table_res.append(table[0])
        table_todo_res.append(table[0])
        table_header = table[0]
        set1.add(table_header[0])
        todo_flag = False
        res_flag = False
        if table_header[0] == 'Function':
            i = 1
            while i < len(table):
                name = table[i]['Function']
                print(name)
                temp_func = {}
                for j in range(len(table_header)):
                    if table_header[j] in table[i]:
                        temp_func[table_header[j]] = table[i][table_header[j]]
                flag = True
                if name.count('(') == 0:
                    sql = 'SELECT ' + name.strip() + ';'
                    tree_rep = parse_tree(sql, 'pg')
                    if tree_rep is None:
                        flag = False
                    else:
                        tree_rep = mark_pg_tree(tree_rep, name, False)
                        if tree_rep is not None:
                            temp_func['Tree'] = tree_rep
                        else:
                            flag = False
                elif "()" in name:
                    name0 = name[0:name.find('(')]
                    sql = 'SELECT ' + name0.strip() + '();'
                    tree_rep = parse_tree(sql, 'pg')
                    if tree_rep is None:
                        flag = False
                    else:
                        tree_rep = mark_pg_tree(tree_rep, name0, True)
                        if tree_rep is not None:
                            temp_func['Tree'] = tree_rep
                        else:
                            flag = False
                else:
                    name0 = name[0:name.find('(')]
                    sql = 'SELECT ' + name0.strip() + '(1);'
                    tree_rep = parse_tree(sql, 'pg')
                    if tree_rep is None:
                        flag = False
                    else:
                        tree_rep1 = mark_pg_tree(tree_rep, name0, True)
                        if tree_rep1 is not None:
                            temp_func['Tree'] = tree_rep1
                        else:
                            flag = False
                if not flag:
                    table_todo_res.append(temp_func)
                else:
                    table_res.append(temp_func)
                todo_flag = todo_flag or (not flag)
                res_flag = res_flag or flag
                i = i + 1
            if todo_flag:
                todo_func_res.append(table_todo_res)
            if res_flag:
                pg_func_res.append(table_res)
        else:
            table_res = table
            todo_func_res.append(table_res)
    with open('pg_14_function_ready.json', 'w') as file:
        json.dump(pg_func_res, file, indent=4)
    with open('pg_14_function_todo.json', 'w') as file:
        json.dump(todo_func_res, file, indent=4)
    print(set1)


make_pg_func_tree()
