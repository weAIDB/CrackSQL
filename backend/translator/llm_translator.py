import json
import asyncio
from llm_model.llm_manager import llm_manager


class LLMTranslator:
    def __init__(self, model_name, model_conf=None):
        self.model_name = model_name
        self.model_conf = model_conf
        self.model = llm_manager.get_model(self.model_name, self.model_conf)
        self.trans_func = self.chat

    def chat(self, history: [], sys_prompt, user_prompt, out_json=False):
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

        # 使用 asyncio.run() 运行异步调用
        response = asyncio.run(self.model.chat(messages))

        # if out_json:
        #     # return self._extract_json(response)
        #     response_parsed = parse_llm_answer_v2(self.model_name, response, TRANSLATION_FORMAT)

        return response

    def _extract_json(self, response: str):
        """从AI回答中提取JSON内容
        
        Args:
            response: AI返回的原始响应
            
        Returns:
            Any: 解析后的JSON对象
            
        Raises:
            ValueError: JSON解析失败
        """
        try:
            # 先尝试直接解析JSON
            try:
                result = json.loads(response)
            except json.JSONDecodeError:
                try:
                    response = response.replace("“", '"').replace("”", '"')
                    result = json.loads(response)
                except json.JSONDecodeError:
                    # JSON解析失败,尝试使用正则匹配
                    import re
                    pattern = r'```json\s*({[\s\S]*?})\s*```|({[\s\S]*})'
                    match = re.search(pattern, response)

                    if not match:
                        raise ValueError("未找到有效的JSON内容")

                    # 获取第一个非None的组
                    json_str = next(group for group in match.groups() if group is not None)
                    result = json.loads(json_str)
            return result

        except Exception as e:
            raise ValueError(f"JSON解析失败: {str(e)}")
