from typing import Optional
from .base import BaseProcessor

class SummaryProcessor(BaseProcessor):
    """摘要生成处理器"""
    
    @property
    def system_prompt(self) -> str:
        return """你是一个深度文本分析专家和摘要生成专家，你的任务是：
        1、需要从给定文本中提取关键信息并生成摘要。
        2、摘要能够覆盖文本的所有信息，包括但不限于文本的主题、细节、隐含意义和可能的扩展思考。
        3、摘要的字数不少于文本的80%。
        4、输出为JSON格式，需要符合JSON标准，能够直接使用Python的json.loads进行解析。"""
    
    @property
    def user_prompt_template(self) -> str:
        return """请根据以下文本生成摘要，必须返回严格的JSON格式。
        文本内容：{content}
        要求：
        1. 返回格式必须是: {{"summary": "摘要内容"}}
        2. 不要包含任何其他字段
        3. 不要在JSON中包含任何注释或说明
        4. 确保返回的是合法的JSON格式
        """
    
    def _parse_response(self, response: str) -> Optional[str]:
        try:
            result = self._extract_json(response)
            if isinstance(result, dict):
                return result.get('summary')
            return None
        except Exception as e:
            logger.error(f"摘要解析失败: {str(e)}")
            return None 