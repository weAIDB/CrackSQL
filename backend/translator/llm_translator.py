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
from llm_model.llm_manager import LLMManager

class LLMTranslator:
    def __init__(self, model_name, model_conf=None):
        self.model_name = model_name
        self.model_conf = model_conf
        self.llm_manager = LLMManager()
        self.model = self.llm_manager.get_model(self.model_name, self.model_conf)
        self.trans_func = self.chat


    def chat(self, history: [], sys_prompt, user_prompt):
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

        response = self.model.chat(messages)
        return json.loads(response)

