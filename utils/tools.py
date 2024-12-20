import json
import re
import sys
import traceback

from typing import List
import os
import openai
import configparser
import requests

import logging
import argparse

import sqlglot

tf_step = 0
summary_writer = None


def set_logger(log_file):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

    # log to file
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    # log to console
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)


def add_summary_value(key, value, step=None):
    if step is None:
        summary_writer.add_scalar(key, value, tf_step)
    else:
        summary_writer.add_scalar(key, value, step)


def get_parser():
    parser = argparse.ArgumentParser(
        description="A Cross-lingual Embedding Model.")

    parser.add_argument("--exp_id", type=str, default="exp_func_v2")
    parser.add_argument("--cache_dir", type=str, default="/data/huggingface")

    parser.add_argument("--epoch", type=int, default=50)
    parser.add_argument("--lr", type=float, default=0.001)

    parser.add_argument("--data_load", type=str,
                        default="")
    parser.add_argument("--model_load", type=str,
                        default="")
    parser.add_argument("--data_save", type=str,
                        default="./exp_res/{}/data/{}_data.pt")

    parser.add_argument("--seed", type=int, default=666)
    parser.add_argument("--runlog", type=str,
                        default="./exp_res/{}/exp_runtime.log")
    parser.add_argument("--logdir", type=str,
                        default="./exp_res/{}/logdir/")

    parser.add_argument("--model_save_gap", type=int, default=1)
    parser.add_argument("--model_save", type=str,
                        default="./exp_res/{}/model/rewrite_{}.pt")

    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--dropout", type=float, default=0.5)

    return parser


def self_split(str1: str) -> List[str]:
    """
    """
    res = []
    str0 = ''
    flag = False
    i = 0
    while i < len(str1):
        if str1[i] == '\'':
            flag = not flag
            str0 = str0 + str1[i]
        elif not flag and (str1[i] == ' ' or str1[i] == '\n'):
            if str0 != '':
                res.append(str0)
            str0 = ''
        else:
            if str1[i] == '\\':
                str0 = str0 + str1[i]
                i = i + 1
            str0 = str0 + str1[i]
        i = i + 1
    if str0 != '':
        res.append(str0)
    return res


def get_g4_path(dialect: str):
    return (os.path.join(get_proj_root_path(), 'data', "revised_g4doc", dialect, 'lexer'),
            os.path.join(get_proj_root_path(), 'data', "revised_g4doc", dialect, 'parser'))


def send_request(history: [], sys_prompt, prompt, model="gpt-4-turbo"):
    if sys_prompt is not None:
        messages = [{"role": "system", "content": sys_prompt}]
    else:
        messages = []
    for message in history:
        messages.append(message)
    messages.append({"role": "user", "content": prompt})

    flag = False
    if flag:
        os.environ["OPENAI_API_BASE"] = "your api base for GPT"
        os.environ["OPENAI_API_KEY"] = "your api key for GPT"

        openai.api_base = os.getenv('OPENAI_API_BASE')
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'),
                               base_url=os.getenv('OPENAI_API_BASE'))

        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=1
        )

        client.close()
        return completion.choices[0].message.content
    else:
        url = "your api base for GPT"
        payload = {
            "model": model,
            "messages": messages
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-your api key for GPT",
            "content-type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response_dict = json.loads(response.text)
        return response_dict['choices'][0]['message']['content']


async def async_send_request(history: [], sys_prompt, prompt):
    os.environ["OPENAI_API_BASE"] = "your api base for GPT"
    os.environ["OPENAI_API_KEY"] = "your api key for GPT"

    openai.api_base = os.getenv('OPENAI_API_BASE')
    async_client = openai.AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'),
                                      base_url=os.getenv('OPENAI_API_BASE'))

    messages = [{"role": "system", "content": sys_prompt}]
    for message in history:
        messages.append(message)
    messages.append({"role": "user", "content": prompt})
    completion = await async_client.chat.completions.create(
        model="gpt-4-turbo",
        messages=messages,
        temperature=1
    )
    await async_client.close()
    return completion.choices[0].message.content


def split2wordlist(terms) -> List[str]:
    """
    """
    res = []
    for term in terms:
        i = 0
        cur_str = ''
        flag = 0
        while i < len(term):
            if 'a' <= term[i] <= 'z' or 'A' <= term[i] <= 'Z' or term[i] == '_' or '0' <= term[i] <= '9':
                if flag != 0 and cur_str != '':
                    res.append(cur_str)
                    cur_str = ''
                flag = 0
                cur_str = cur_str + term[i]
            elif term[i] == "'":
                if flag != 1 and cur_str != '':
                    res.append(cur_str)
                    cur_str = ''
                flag = 1
                cur_str = cur_str + term[i]
                i = i + 1
                while term[i] != "'":
                    if term[i] == '\\':
                        i = i + 1
                    cur_str = cur_str + term[i]
                    i = i + 1
                res.append(cur_str + "'")
                cur_str = ''
            elif (term[i] == '(' or term[i] == ')' or term[i] == '*' or term[i] == '[' or term[i] == ']'
                  or term[i] == '+' or term[i] == '|' or term[i] == '?' or term[i] == '=' or term[i] == ','):
                if cur_str != '':
                    res.append(cur_str)
                    cur_str = ''
                flag = 2
                res.append(term[i])
            elif term[i] == '.':
                if flag != 3 and cur_str != '':
                    res.append(cur_str)
                    cur_str = ''
                flag = 3
                cur_str = cur_str + term[i]
            else:
                if flag != 4 and cur_str != '':
                    res.append(cur_str)
                    cur_str = ''
                flag = 4
                cur_str = cur_str + term[i]
            i = i + 1
        if cur_str != '':
            res.append(cur_str)
    return res

def extract_json(bnf: str) -> List[str]:
    matches = re.findall(r'```json(.*?)```', bnf, re.DOTALL)
    return [match.strip() for match in matches]


def remove_quotes(s):
    """
    """
    quotes = ['"', "'"]
    while s and s[0] in quotes and s[0] == s[-1]:
        s = s[1:-1]
    return s


def remove_comments(code):
    code = re.sub(r'//.*?\n', '\n', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code.strip()


def is_non_terminal(word: str) -> bool:
    for i in range(len(word)):
        if word[i] == '_' or ('z' >= word[i] >= 'a'):
            continue
        else:
            return False
    return True


def print_err(word: str):
    print(word, file=sys.stderr)


def get_lexer_parser(dialect: str):
    directory_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                  'data', 'revised_g4doc', dialect)
    return os.path.join(directory_path, 'lexer'), os.path.join(directory_path, 'parser')


def get_proj_root_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config(config_file=None):
    if config_file is None:
        config_file = os.path.join(get_proj_root_path(), 'Config.ini')
    config = configparser.ConfigParser()
    config.read(config_file)
    return {
        'dbg': config.getboolean("MODE", 'dbg'),
        'use_test': config.getboolean("MODE", 'use_test'),
        'reflect_on': config.getboolean("MODE", 'reflection_on'),
        'mask_on': config.getboolean("MODE", 'mask_on'),
        "min_mask_len": config.getint("MODE", 'min_mask_len'),
        'slice_only': config.getboolean("MODE", 'slice_only'),
        'locate_by_err': config.getboolean("MODE", 'locate_by_err'),
        'oracle_locate_open': config.getboolean("MODE", 'oracle_locate_open'),

        'seg_on': config.getboolean("MODE", 'seg_on'),
        'retrieval_on': config.getboolean("MODE", 'retrieval_on'),

        "gpt_api_base": config.get("API", 'gpt_api_base'),
        "gpt_api_key": config.get("API", 'gpt_api_key'),
        "llama3.1_api_base": config.get("API", 'llama3.1_api_base'),
        "llama3.2_api_base": config.get("API", 'llama3.2_api_base'),

        "codellama_api_base": config.get("API", 'codellama_api_base'),
        "codeqwen2.5_api_base": config.get("API", 'codeqwen2.5_api_base'),
        "qwen2.5_api_base": config.get("API", 'qwen2.5_api_base'),
    }


def only_lower_underscore(word: str):
    for i in range(len(word)):
        if (word[i] > 'z' or word[i] < 'a') and word[i] != '_':
            return False
    return True


def remove_all_space(ori_str: str):
    res = ''
    for ori_sql_slice in ori_str.split():
        res = res + ori_sql_slice
    return res


def only_lower_under_score_digit(word: str):
    for i in range(len(word)):
        if not ('z' >= word[i] >= 'a' or '9' >= word[i] >= '0') and word[i] != '_':
            return False
    return True


def parse_llm_answer(model_id, answer_raw, pattern):
    if "gpt-" in model_id:
        answer = answer_raw['choices'][0]['message']['content']
    elif "llama" in model_id:
        answer = answer_raw['content']
    elif "qwen" in model_id:
        answer = answer_raw['content']

    try:
        match = re.search(pattern, answer, re.DOTALL)
        if match:
            answer_ori = match.group(1)
            if answer_ori[0] == '"':
                answer_ori = answer_ori[1:]
            if answer_ori[-1] == '"':
                answer_ori = answer_ori[:-1]
            answer_extract = answer_ori.replace('\\\"', '\"')
            reasoning = match.group(2).strip('"').replace('\\\"', '\"')
            json_content_reflect = {
                "Answer": answer_extract,
                "Reasoning": reasoning
            }
            res = json_content_reflect["Answer"]
        else:
            res = "Answer not returned in the given format!"

        return res
    except Exception as e:
        traceback.print_exc()
        return str(e)


def parse_llm_answer_v2(model_id, answer_raw, pattern):
    if "gpt-" in model_id:
        answer = answer_raw['choices'][0]['message']['content']
    elif "llama" in model_id:
        answer = answer_raw['content']
    elif "qwen" in model_id:
        answer = answer_raw['content']

    try:
        match = re.search(pattern, answer, re.DOTALL)
        if match:
            answer_extract = match.group(1).strip('"').replace('\\\"', '\"')
            reasoning = match.group(2).strip('"').replace('\\\"', '\"')
            confidence = match.group(3).strip('"').replace('\\\"', '\"')
            try:
                confidence = eval(confidence)
            except Exception as e:
                confidence = 0.8
                traceback.print_exc()

            json_content_reflect = {
                "Answer": answer_extract,
                "Reasoning": reasoning,
                "Confidence": confidence
            }
            res = json_content_reflect
        else:
            res = {"Answer": "Answer not returned in the given format!",
                   "Reasoning": "Error occurs!",
                   "Confidence": 0}

        return res
    except Exception as e:
        traceback.print_exc()
        return {"Answer": str(e), "Reasoning": "Error occurs!", "Confidence": 0}


def reformat_sql(ori_sql: str):
    new_sql = sqlglot.parse_one(ori_sql).sql()
    i = 0
    j = 0
    res = ''
    while i < len(ori_sql):
        if ori_sql[i] == ' ' or ori_sql[i] == '\t' or ori_sql[i] == '\n':
            i = i + 1
        if new_sql[j] == ' ' or new_sql[j] == '\n' or new_sql[j] == '\t':
            res = res + ' '
            j = j + 1
        i2 = i
        while i2 < len(ori_sql) and ori_sql[i2] != ' ' and ori_sql[i2] != '\t' and ori_sql[i2] != '\n':
            i2 = i2 + 1
        j2 = j
        while j2 < len(new_sql) and new_sql[j2] != ' ' and new_sql[j2] != '\t' and ori_sql[j2] != '\n':
            j2 = j2 + 1
        if new_sql[j: j2].startswith(ori_sql[i: i2]):
            res = res + ori_sql[i: i2]
            j = j + len(ori_sql[i: i2])
        else:
            res = res + " " + ori_sql[i: i2] + " "
        i = i2 + 1
    final_res = ''
    for split_slice in res.strip().split():
        final_res = final_res + split_slice + " "
    return final_res.strip()
