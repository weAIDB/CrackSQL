# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: pre_retriever_data
# @Author: xxxx
# @Time: 2024/9/17 13:31

import re
import os
import json
import traceback

import sqlglot

from translator.llm_translator import LLMTranslator
from translator.tool_prompt import USER_PROMPT_FUNC_EXAMPLE, USER_PROMPT_FUNC_NAME, USER_PROMPT_FUNC_COM
from utils.tools import load_config, parse_llm_answer

map_rep = {
    'postgres': 'PostgreSQL 14.7',
    'mysql': "MySQL 8.4",
    'oracle': "Oracle 11g"
}

# keyword
dialect_load_keyword = {"postgres": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                    "processed_document/pg/pg_keyword_ready.json",
                        "mysql": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                 "processed_document/mysql/mysql_keyword_ready.json",
                        "oracle": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                  "processed_document/oracle/oracle_11_keyword_ready.json"}

# data type
dialect_load_type = {"postgres": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                 "processed_document/pg/pg_type_ready.json",
                     "mysql": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                              "processed_document/mysql/mysql_8_type_ready.json",
                     "oracle": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                               "processed_document/oracle/oracle_11_type_ready.json"}

# built-in function
dialect_load_function = {"postgres": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                     "processed_document/pg/pg_14_function_ready.json",
                         "mysql": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                  "processed_document/mysql/mysql_function_ready.json",
                         "oracle": "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                                   "processed_document/oracle/oracle_11_function_ready.json"}

config = load_config()
gpt_api_base = config['gpt_api_base']
gpt_api_key = config['gpt_api_key']
llama_3_1_api_base = config['llama3.1_api_base']
llama_3_2_api_base = config['llama3.2_api_base']


def init_model(model_id):
    # https://platform.openai.com/docs/models/gpt-3-5-turbo
    if "gpt-" in model_id:  # gpt-4-turbo, gpt-4o, gpt-4o-mini
        openai_conf = {"temperature": 0}
        api_base = gpt_api_base
        api_key = gpt_api_key

        translator = LLMTranslator(model_id, openai_conf)
        translator.load_model(api_base, api_key)

    elif model_id == "llama3.1":
        api_base = llama_3_1_api_base
        translator = LLMTranslator(model_id)
        translator.load_model(api_base)

    elif model_id == "llama3.2":
        api_base = llama_3_2_api_base
        translator = LLMTranslator(model_id)
        translator.load_model(api_base)

    return translator


def pre_pg_func():
    """
    Merger compensate and ready
    :return:
    """
    ready_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                 "processed_document/pg/pg_14_function_ready.json"
    with open(ready_load, "r") as rf:
        ready = json.load(rf)

    compensate_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                      "processed_document/pg/pg_14_compensate_build_in_function.json"
    with open(compensate_load, "r") as rf:
        compensate = json.load(rf)

    ready_list = list()
    for item in ready:
        ready_list.extend(item[1:])

    for item in ready_list:
        name = list(item.values())[0]
        item["Name"] = name
        for temp in compensate:
            if name.replace(" ", "") == list(temp.values())[0].replace(" ", ""):
                item["compensate"] = temp["compensate"]
                break

    ready_save = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                 "processed_document/pg/pg_14_function_ready_compensate.json"
    with open(ready_save, "w") as wf:
        json.dump(ready_list, wf, indent=4)


def merge_files():
    file_path = "/data/xxxx/index/sql_convertor/data_resource/oracle11/Functions"

    func_list = list()
    for file in os.listdir(file_path):
        with open(f"{file_path}/{file}", "r") as rf:
            data = json.load(rf)

        desc = data["content"].split(" ", 1)[-1].split("<link>Previous")[0].replace("Syntax",
                                                                                    "The Syntax is: \n").replace(
            "Purpose", "\n The Purpose is: \n").replace("Examples", "\n The Examples is: \n")

        func_list.append({"Name": data["title"], "Link": data["url"], "Description": desc})

    file_save = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/processed_document/oracle/oracle_11_built-in-function.json"
    with open(file_save, "w") as wf:
        json.dump(func_list, wf, indent=2)


def count_share():
    # oracle: operator + some functions, pg: function description (paragraphs by keyword), mysql: keyword
    mysql_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/official_document/" \
                 "mysql/mysql_function/mysql_8.4_built-in-function.json"
    with open(mysql_load, "r") as rf:
        mysql = json.load(rf)
    mysql_func = [item["Name"] for item in mysql]

    pg_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
              "processed_document/pg/pg_14_function_ready.json"
    with open(pg_load, "r") as rf:
        pg = json.load(rf)
    pg_func = [list(item.values())[0] for item in pg]

    oracle_load = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                  "processed_document/oracle/oracle_11_built-in-function.json"
    with open(oracle_load, "r") as rf:
        oracle = json.load(rf)
    oracle_func = [item["Name"] for item in oracle]

    pg_mysql = set([item.split("(")[0].lower() for item in pg_func]).intersection(
        set([item.split("(")[0].lower() for item in mysql_func]))
    
    pg_oracle = set([item.split("(")[0].lower() for item in pg_func]).intersection(
        set([item.split("(")[0].lower() for item in oracle_func]))

    mysql_oracle = set([item.split("(")[0].lower() for item in mysql_func]).intersection(
        set([item.split("(")[0].lower() for item in oracle_func]))


def aug_data():
    class DataTransformation:
        def __init__(self, ):
            mysql_key = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/processed_document/mysql/mysql_keyword_ready.json"
            with open(mysql_key, "r") as rf:
                mysql_key = json.load(rf)

            pg_key = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/processed_document/pg/pg_keyword_ready.json"
            with open(pg_key, "r") as rf:
                pg_key = json.load(rf)

            oracle_key = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/processed_document/oracle/oracle_19_keyword_ready.json"
            with open(oracle_key, "r") as rf:
                oracle_key = json.load(rf)

    # import nltk
    # nltk.download('averaged_perceptron_tagger_eng')

    import nlpaug.augmenter.word as naw

    text = 'The quick brown fox jumps over the lazy dog .'
    text = "Return the average value of the argument"
    # text = "Return the arc tangent"

    # aug = naw.SynonymAug(aug_src='wordnet')
    aug = naw.SynonymAug(aug_src='ppdb',
                         model_path="/data/xxx/ppdb-2.0-tldr")
    augmented_text = aug.augment(text)

    print("Original:")
    print(text)
    print("Augmented Text:")
    print(augmented_text)


def pre_coarse_data():
    function_loads = ["/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                      "processed_document/pg/pg_14_function_ready_v2.json",
                      "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/official_document/"
                      "mysql/mysql_function/mysql_8.4_built-in-function.json",
                      "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/"
                      "processed_document/oracle/oracle_11_built-in-function.json"]

    all_data = dict()
    for function_load in function_loads:
        with open(function_load, "r") as rf:
            function_data = json.load(rf)

        for item in function_data:
            if "pg" in function_load:
                func = list(item.values())[0]
                func_pre = func.split("(")[0].lower()

                desc = str()
                if "Description" in item.keys():
                    desc += f"The Description is:\n{item['Description']}\n"
                if "Example" in item.keys():
                    desc += f"The Example is:\n{item['Example']}"

                if func_pre not in all_data.keys():
                    all_data[func_pre] = list()
                all_data[func_pre].append({"Dialect": "pg", "Function": func, "Description": desc})

                for dialect in ["mysql", "oracle"]:
                    try:
                        pg_other = sqlglot.transpile(func, read="postgres", write=dialect)
                        pg_other_pre = pg_other.split("(")[0].lower()
                        if pg_other.lower() != func.lower():
                            if pg_other_pre not in all_data.keys():
                                all_data[pg_other_pre] = list()
                            all_data[pg_other_pre].append({"Dialect": "pg", "Function": func, "Description": desc})
                    except:
                        traceback.print_exc()

            elif "mysql" in function_load:
                func = item["Name"]
                func_pre = func.split("(")[0].lower()

                desc = f"The Description is:\n{item['Description']}\n" \
                       f"The Detail is:\n{item['Detail']}"

                if func_pre not in all_data.keys():
                    all_data[func_pre] = list()
                all_data[func_pre].append({"Dialect": "mysql", "Function": func, "Description": desc})

                for dialect in ["postgres", "oracle"]:
                    try:
                        mysql_other = sqlglot.transpile(func, read="mysql", write=dialect)
                        mysql_other_pre = mysql_other.split("(")[0].lower()
                        if mysql_other.lower() != func.lower():
                            if mysql_other_pre not in all_data.keys():
                                all_data[mysql_other_pre] = list()
                            all_data[mysql_other_pre].append(
                                {"Dialect": "mysql", "Function": func, "Description": desc})
                    except:
                        traceback.print_exc()

            elif "oracle" in function_load:
                func = item["Name"]
                func_pre = func.split("(")[0].lower()

                desc = f"The Description is:\n{item['Description']}"

                if func_pre not in all_data.keys():
                    all_data[func_pre] = list()
                all_data[func_pre].append({"Dialect": "oracle", "Function": func, "Description": desc})

                for dialect in ["postgres", "mysql"]:
                    try:
                        oracle_other = sqlglot.transpile(func, read="oracle", write=dialect)
                        oracle_other_pre = oracle_other.split("(")[0].lower()
                        if oracle_other.lower() != func.lower():
                            if oracle_other_pre not in all_data.keys():
                                all_data[oracle_other_pre] = list()
                            all_data[oracle_other_pre].append(
                                {"Dialect": "oracle", "Function": func, "Description": desc})
                    except:
                        traceback.print_exc()

    data_save = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                "processed_document/three_dialects_built-in-function_coarse.json"
    with open(data_save, "w") as wf:
        json.dump(all_data, wf, indent=2)

    print(1)


def merge_lists(lists):
    lis = list()
    for ls in lists:
        ls = list(set([str(l) for l in ls]))
        lis.append(ls)
    lists = lis

    merged = []
    while lists:
        # Take the first list to merge
        current = lists.pop(0)
        to_merge = [current]

        # Find and merge all lists that share at least one common value
        for other in lists[:]:  # Create a copy of the list for safe iteration
            if set(current) & set(other):  # Check for common elements
                to_merge.append(other)
                lists.remove(other)

        # Merge all found lists into one
        current = set().union(*to_merge)
        merged.append(list(current))

    mer = list()
    for me in merged:
        me = [eval(m) for m in me]
        mer.append(me)
    merged = mer

    return merged


def pre_func_fine_data():
    databases = ["postgres", "mysql", "oracle"]

    all_data = dict()
    for db in databases:
        all_data[db] = dict()

        function_load = dialect_load_function[db]
        with open(function_load, "r") as rf:
            function_data = json.load(rf)

        info = set()
        for item in function_data:
            info = info.union(set(item.keys()))

        for item in function_data:
            key = item["Name"].split("(")[0].lower()
            if key not in all_data[db]:
                all_data[db][key] = list()
            item["Dialect"] = db
            all_data[db][key].append(item)

    all_mapping = dict()
    for db in databases:
        all_mapping[db] = dict()
        for key, value in all_data[db].items():
            all_mapping[db][key] = dict()
            for func in value:
                if db == "postgres" and ('Example' not in func.keys() or len(func['Example']) == 0):
                    continue

                if db == "mysql" and ('Demo' not in func.keys() or len(func['Demo']) == 0):
                    continue

                if db == "oracle" and 'Description' not in func.keys():
                    continue

                for d_temp in databases:
                    if d_temp == db or key in all_data[d_temp].keys():
                        continue

                    if db == "postgres":
                        src_sql = [func['Example']]

                    elif db == "mysql":
                        src_sql = list()
                        for demo in func['Demo']:
                            src_sql.extend(re.findall(r'mysql>\s*(.*?);', demo))

                    elif db == "oracle":
                        src_sql = list()
                        code = re.findall(r'<code>(.*?)</code>', func['Description'], re.DOTALL)
                        for item in code:
                            src_sql.extend([sql for sql in item.split(";") if "SELECT" in sql])

                    for sql in src_sql:
                        try:
                            func_name, func_temp_name = set(), set()

                            src_func_name_list = [f.lower() for f in re.findall(r'(\w+)\s*\(', sql)]
                            func_name.update(src_func_name_list)

                            tgt_sql = sqlglot.transpile(sql, read=db, write=d_temp)[0]
                            tgt_func_name_list = [f.lower() for f in re.findall(r'(\w+)\s*\(', tgt_sql)]
                            func_temp_name.update(tgt_func_name_list)

                            for temp in func_temp_name.difference(func_name):
                                if temp not in all_data[db].keys():
                                    if d_temp not in all_mapping[db][key].keys():
                                        all_mapping[db][key][d_temp] = set()

                                    if temp in all_data[d_temp].keys() and temp not in all_mapping[db][key][d_temp]:
                                        all_mapping[db][key][d_temp].add(temp)

                                        if d_temp in all_mapping.keys() and temp in all_mapping[d_temp].keys():
                                            if db not in all_mapping[d_temp][temp].keys():
                                                all_mapping[d_temp][temp][db] = set()
                                            all_mapping[d_temp][temp][db].add(key)

                        except Exception as e:
                            print(str(e))

    all_function = dict()
    for i in range(len(databases)):
        for key in all_data[databases[i]].keys():
            if isinstance(all_data[databases[i]][key], str):
                continue

            if key not in all_function.keys():
                all_function[key] = list()
            all_function[key].extend(all_data[databases[i]][key])

            db_temp = databases[i + 1:]
            for temp in db_temp:
                # if key not in all_function.keys():
                #     break

                if temp in all_mapping[databases[i]][key].keys() and \
                        len(all_mapping[databases[i]][key][temp]) > 0:
                    for func_temp in all_mapping[databases[i]][key][temp]:
                        all_function[key].extend(all_data[temp][func_temp])

    all_function = merge_lists(list(all_function.values()))

    data_save = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                "processed_document/three_dialects_func_fine.json"
    with open(data_save, "w") as wf:
        json.dump(all_function, wf, indent=2)


def pre_func_fine_data_model():
    model_id = "gpt-4o"  # llama3.1, llama3.2, gpt-3.5-turbo, gpt-4-turbo, gpt-4o, gpt-4o-mini
    translator = init_model(model_id)

    databases = ["postgres", "mysql", "oracle"]

    all_data = dict()
    for db in databases:
        all_data[db] = dict()

        function_load = dialect_load_function[db]
        with open(function_load, "r") as rf:
            function_data = json.load(rf)

        for item in function_data:
            key = item["Name"].split("(")[0].lower()
            if key not in all_data[db]:
                all_data[db][key] = list()
            item["Dialect"] = db
            all_data[db][key].append(item)

    all_mapping = dict()
    for db in databases:
        all_mapping[db] = dict()
        for key, value in all_data[db].items():
            all_mapping[db][key] = dict()

            for func in value:
                if db == "postgres":
                    user_prompt = USER_PROMPT_FUNC_COM.format(dialect=map_rep[db], function=func["Name"],
                                                              sql=func["Example"])
                    answer_raw = translator.trans_func([], None, user_prompt)
                    pattern = r'"Example SQL":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?)'
                    src_sql_model = parse_llm_answer(translator.model_id, answer_raw, pattern)

                    for d_temp in databases:
                        if d_temp == db:
                            continue

                        for src_sql in [func["Example"], src_sql_model]:
                            tgt_sql = sqlglot.transpile(src_sql, read=db, write=d_temp)[0]
                            user_prompt = USER_PROMPT_FUNC_NAME.format(src_dialect="Q1",
                                                                       tgt_dialect="Q2",
                                                                       src_sql=src_sql, tgt_sql=tgt_sql,
                                                                       function=func["Name"])
                            answer_raw = translator.trans_func([], None, user_prompt)
                            pattern = r'"Function":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?)'
                            func_name = parse_llm_answer(translator.model_id, answer_raw, pattern)

                            if func_name.split("(")[0].lower() in all_data[d_temp].keys():
                                # all_function
                                all_data[db][key].extend(all_data[d_temp][func_name.split("(")[0].lower()])

                            print(1)


                elif db == "oracle":
                    user_prompt = USER_PROMPT_FUNC_EXAMPLE.format(dialect=map_rep[db], function=func["Name"],
                                                                  description=func["Description"])
                    answer_raw = translator.trans_func([], None, user_prompt)
                    pattern = r'"Example SQL":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?)'
                    src_sql = parse_llm_answer(translator.model_id, answer_raw, pattern)

                    tgt_sql = sqlglot.transpile(func["Example"], read=db, write=d_temp)[0]

                    user_prompt = USER_PROMPT_FUNC_NAME.format(src_dialect=db, tgt_dialect=d_temp,
                                                               src_sql=src_sql, tgt_sql=tgt_sql, function="")
                    answer_raw = translator.trans_func([], None, user_prompt)
                    pattern = r'"Function":\s*(.*?)\s*,\s*"Reasoning":\s*(.*?)'
                    func_name = parse_llm_answer(translator.model_id, answer_raw, pattern)

    all_function = dict()
    for item in function_data:
        if "pg" in function_load:
            func = list(item.values())[0]
            func_pre = func.split("(")[0].lower()

            desc = str()
            if "Description" in item.keys():
                desc += f"The Description is:\n{item['Description']}\n"
            if "Example" in item.keys():
                desc += f"The Example is:\n{item['Example']}"

            if func_pre not in all_data.keys():
                all_data[func_pre] = list()
            all_data[func_pre].append({"Dialect": "pg", "Function": func, "Description": desc})

            for dialect in ["mysql", "oracle"]:
                try:
                    pg_other = sqlglot.transpile(func, read="postgres", write=dialect)
                    pg_other_pre = pg_other.split("(")[0].lower()
                    if pg_other.lower() != func.lower():
                        if pg_other_pre not in all_data.keys():
                            all_data[pg_other_pre] = list()
                        all_data[pg_other_pre].append({"Dialect": "pg", "Function": func, "Description": desc})
                except:
                    traceback.print_exc()

        elif "mysql" in function_load:
            func = item["Name"]
            func_pre = func.split("(")[0].lower()

            desc = f"The Description is:\n{item['Description']}\n" \
                   f"The Detail is:\n{item['Detail']}"

            if func_pre not in all_data.keys():
                all_data[func_pre] = list()
            all_data[func_pre].append({"Dialect": "mysql", "Function": func, "Description": desc})

            for dialect in ["postgres", "oracle"]:
                try:
                    mysql_other = sqlglot.transpile(func, read="mysql", write=dialect)
                    mysql_other_pre = mysql_other.split("(")[0].lower()
                    if mysql_other.lower() != func.lower():
                        if mysql_other_pre not in all_data.keys():
                            all_data[mysql_other_pre] = list()
                        all_data[mysql_other_pre].append(
                            {"Dialect": "mysql", "Function": func, "Description": desc})
                except:
                    traceback.print_exc()

        elif "oracle" in function_load:
            func = item["Name"]
            func_pre = func.split("(")[0].lower()

            desc = f"The Description is:\n{item['Description']}"

            if func_pre not in all_data.keys():
                all_data[func_pre] = list()
            all_data[func_pre].append({"Dialect": "oracle", "Function": func, "Description": desc})

            for dialect in ["postgres", "mysql"]:
                try:
                    oracle_other = sqlglot.transpile(func, read="oracle", write=dialect)
                    oracle_other_pre = oracle_other.split("(")[0].lower()
                    if oracle_other.lower() != func.lower():
                        if oracle_other_pre not in all_data.keys():
                            all_data[oracle_other_pre] = list()
                        all_data[oracle_other_pre].append(
                            {"Dialect": "oracle", "Function": func, "Description": desc})
                except:
                    traceback.print_exc()

    data_save = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                "processed_document/three_dialects_built-in-function_coarse.json"
    with open(data_save, "w") as wf:
        json.dump(all_data, wf, indent=2)

    print(1)


def pre_type_fine_data():
    databases = ["postgres", "mysql", "oracle"]

    all_type = dict()
    for db in databases:
        function_load = dialect_load_type[db]
        with open(function_load, "r") as rf:
            function_data = json.load(rf)

        info = set()
        for item in function_data:
            info = info.union(set(item.keys()))

        for item in function_data:
            if db == "postgres":
                item["Name"] = ";".join(item["Type"])
                key = item["Link"].split("#")[0].split("/")[-1].lower()
                if key not in all_type:
                    all_type[key] = list()
                item["Dialect"] = db
                all_type[key].append(item)
            elif db == "mysql":
                item["Name"] = ";".join(item["Type"])
                if "Links" in item.keys() and len(item["Links"]) > 0:
                    key = item["Links"][0].split("#")[0].split("/")[-1].lower()
                else:
                    key = item["Name"]
                if key not in all_type:
                    all_type[key] = list()
                item["Dialect"] = db
                all_type[key].append(item)
            elif db == "oracle":
                item["Name"] = item["Type"]
                key = item["Name"].lower()
                if key not in all_type:
                    all_type[key] = list()
                item["Dialect"] = db
                all_type[key].append(item)

    data_save = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                "processed_document/three_dialects_type_fine.json"
    with open(data_save, "w") as wf:
        json.dump(all_type, wf, indent=2)


def pre_keyword_fine_data():
    databases = ["postgres", "mysql", "oracle"]

    all_keyword = dict()
    for db in databases:
        function_load = dialect_load_keyword[db]
        with open(function_load, "r") as rf:
            function_data = json.load(rf)

        info = set()
        for item in function_data:
            info = info.union(set(item.keys()))

        for item in function_data:
            if db == "postgres":
                item["Name"] = ";".join(item["Keyword"])
                item["Dialect"] = db
                for no, key in enumerate(item["Keyword"]):
                    if key.lower().split(" ")[0] not in all_keyword:
                        all_keyword[key.lower().split(" ")[0]] = list()
                    all_keyword[key.lower().split(" ")[0]].append(item)
                    break

            elif db == "mysql":
                item["Name"] = ";".join(item["Keyword"])
                item["Dialect"] = db
                for no, key in enumerate(item["Keyword"]):
                    if key.lower().split(" ")[0] not in all_keyword:
                        all_keyword[key.lower().split(" ")[0]] = list()
                    all_keyword[key.lower().split(" ")[0]].append(item)
                    break

            elif db == "oracle":
                item["Name"] = ";".join(item["Keyword"])
                item["Dialect"] = db
                for no, key in enumerate(item["Keyword"]):
                    if key.lower().split(" ")[0] not in all_keyword:
                        all_keyword[key.lower().split(" ")[0]] = list()
                    all_keyword[key.lower().split(" ")[0]].append(item)
                    break

    data_save = "/data/xxxx/index/sql_convertor/LLM4DB/LLM4DB/data/" \
                "processed_document/three_dialects_keyword_fine.json"
    with open(data_save, "w") as wf:
        json.dump(all_keyword, wf, indent=2)


if __name__ == "__main__":
    pre_pg_func()
    # pre_coarse_data()

    # pre_func_fine_data()
    # pre_type_fine_data()
    # pre_keyword_fine_data()
