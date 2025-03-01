import argparse
import configparser
import json
import logging
import os
import re
import sys
import traceback
from typing import List

import openai
import requests

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

    parser.add_argument("--exp_id", type=str, default="exp_id")
    parser.add_argument("--cache_dir", type=str, default="/data/")

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


def remove_comments(code):
    code = re.sub(r'//.*?\n', '\n', code)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    return code.strip()


def print_err(word: str):
    print(word, file=sys.stderr)


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


def parse_llm_answer(answer, pattern):
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
            return json_content_reflect
        else:
            return None
    except Exception as e:
        traceback.print_exc()
        return str(e)


def process_history_text(text, role, action):
    if role == "user" and action == "translate":
        # 1. input process
        input_sql_section = "The input SQL snippet is:"
        text = f"The current SQL snippet to be translated is:\n {text.split(input_sql_section)[-1]}"

        specification_section_start = "Below are specifications"
        specification_section_end = "specific SQL snippets in the input SQL snippet."
        text = f"{text.split(specification_section_start)[0]}{text.split(specification_section_end)[-1]}"
        text = text.replace("<< SPECIFICATION START >>", "").replace("<< SPECIFICATION END >>", "")
        text = text.replace("<< EXAMPLE START >>", "").replace("<< EXAMPLE END >>", "")
        text = text.replace("<reflection>", "`").replace("</reflection>", "`")

        # 2. output process
        output_section = "## OUTPUT FORMAT ##"
        text = text.split(output_section)[0]

    if role == "user" and action == "judge":
        # 1. input process
        text_prefix = text.split("This means they should return the same results with consistent data types")[0]
        text_suffix = text.split("## INPUT ##")[-1]
        text = f"{text_prefix}\n{text_suffix}"

        # 2. output process
        output_section = "## OUTPUT FORMAT ##"
        text = text.split(output_section)[0]

    if role == "assistant":
        if "```" not in text:
            text = f"```json\n{text}\n```"

    return text


def process_err_msg(msg):
    msg = msg.replace("xxxx_BIRD.", "").replace("BIRD.", "").replace(
        "pg_catalog.date_part(", "EXTRACT(").replace("Error while executing PostgreSQL query:", "").replace(
        "You have an error in your SQL syntax; check the manual that corresponds "
        "to your MySQL server version for the right syntax to use near",
        "Some error occurs near")

    return msg
