# -*- coding: utf-8 -*-
# @Project: xxxx
# @Module: llm_translator
# @Author: xxxx
# @Time: 2024/9/2 22:51

import os
import json
import openai
import requests
import http.client


class LLMTranslator:
    def __init__(self, model_id, model_conf=None):
        self.model_id = model_id
        self.model_conf = model_conf

        self.model = None
        self.api_key = None
        self.tokenizer = None

        self.trans_func = None

    def load_model(self, api_base=None, api_key=None):
        if "gpt-" in self.model_id:
            # os.environ["OPENAI_API_BASE"] = api_base
            # os.environ["OPENAI_API_KEY"] = api_key
            #
            # openai.api_base = os.getenv("OPENAI_API_BASE")
            # self.model = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"),
            #                            base_url=os.getenv("OPENAI_API_BASE"))

            self.model = http.client.HTTPSConnection(api_base)
            self.api_key = api_key

            self.trans_func = self.openai_gpt

        elif self.model_id == "llama3.1":
            self.model = api_base
            self.trans_func = self.llama3

        elif self.model_id == "llama3.2":
            self.model = api_base
            self.trans_func = self.llama3

        elif self.model_id == "codellama":
            self.model = api_base
            self.trans_func = self.llama3

        elif self.model_id == "codeqwen2.5":
            self.model = api_base
            self.trans_func = self.llama3

        elif self.model_id == "qwen2.5":
            self.model = api_base
            self.trans_func = self.llama3

    def openai_gpt(self, history: [], sys_prompt, user_prompt):
        if sys_prompt is not None:
            messages = [{"role": "system", "content": sys_prompt}]
        else:
            messages = []
        for message in history:
            if 'choices' in message.keys():
                messages.append(message['choices'][0]['message'])
            else:
                messages.append(message)
        messages.append({"role": "user", "content": user_prompt})

        payload = json.dumps({
            "model": self.model_id,
            "messages": messages,
            "stream": False,
            **self.model_conf
        })
        headers = {
            "Authorization": self.api_key,
            "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
            "Content-Type": "application/json"
        }
        self.model.request("POST", "/v1/chat/completions", payload, headers)
        res = self.model.getresponse()
        data = res.read()

        return json.loads(data.decode("utf-8"))

    def openai_gpt_v1(self, history: [], sys_prompt, user_prompt):
        # https://platform.openai.com/docs/models
        if sys_prompt is not None:
            messages = [{"role": "system", "content": sys_prompt}]
        else:
            messages = []
        for message in history:
            messages.append(message)

        messages.append({"role": "user", "content": user_prompt})
        completion = self.model.chat.completions.create(
            model=self.model_id,
            messages=messages,
            **self.model_conf
        )
        # self.model.close()

        return completion.choices[0].message.content

    def llama3(self, history: [], sys_prompt, user_prompt):
        messages = list()
        if sys_prompt is not None:
            messages = [{"role": "system", "content": sys_prompt}]

        for message in history:
            messages.append(message)

        messages.append({"role": "user", "content": user_prompt})

        response = requests.request(method="POST", url=self.model,
                                    data=json.dumps({"messages": messages}))

        return json.loads(response.text)

    def llama3_2(self, history: [], sys_prompt, user_prompt):
        messages = list()
        if sys_prompt is not None:
            messages = [{"role": "system", "content": sys_prompt}]

        for message in history:
            messages.append(message)

        messages.append({"role": "user", "content": user_prompt})

        response = requests.request(method="POST", url=self.model,
                                    data=json.dumps({"messages": messages}))

        return response.text
