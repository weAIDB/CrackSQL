import re
import asyncio
import traceback

from llm_model.llm_manager import llm_manager


class LLMTranslator:
    def __init__(self, model_name, model_conf=None):
        self.model_name = model_name
        self.model_conf = model_conf
        self.model = llm_manager.get_model(self.model_name, self.model_conf)
        self.trans_func = self.chat
        if not self.model:
            raise ValueError(f"Model {self.model_name} not found")

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

        # 直接调用模型的chat方法
        response = self.model.chat(messages)

        return response

    def parse_llm_answer(self, answer, pattern):
        try:
            match = re.search(pattern, answer, re.DOTALL)
            if match:
                answer_extract = match.group(1).strip('"').replace('\\\"', '\"')
                reasoning = match.group(2).strip('"').replace('\\\"', '\"')
                confidence = match.group(3).strip('"').replace('\\\"', '\"')
                try:
                    confidence = eval(confidence)
                except Exception as e:
                    confidence = 0.01
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
