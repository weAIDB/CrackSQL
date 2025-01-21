from abc import ABC, abstractmethod
import json
import re
from typing import Optional, Dict, Any, List
from config.logging_config import logger

class BaseProcessor(ABC):
    """LLM处理器基类"""
    
    def __init__(self, model_name: str):
        self.model_name = model_name
    
    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """系统提示词"""
        pass
        
    @property
    @abstractmethod
    def user_prompt_template(self) -> str:
        """用户提示词模板"""
        pass
    
    def _extract_json(self, text: str) -> Any:
        """从文本中提取JSON"""
        try:
            # 尝试直接解析
            return json.loads(text)
        except json.JSONDecodeError:
            # 尝试从文本中提取JSON字符串
            pattern = r'\{[\s\S]*\}|\[[\s\S]*\]'
            match = re.search(pattern, text)
            if match:
                try:
                    return json.loads(match.group())
                except json.JSONDecodeError:
                    pass
        return None
    
    @abstractmethod
    def _parse_response(self, response: str) -> Optional[Any]:
        """解析响应"""
        pass
        
    async def process(self, content: str, **kwargs) -> Optional[Any]:
        """处理内容"""
        try:
            from llm_model.llm_factory import get_llm
            
            # 获取LLM实例
            llm = get_llm(self.model_name)
            
            # 构建提示词
            prompt = self.user_prompt_template.format(content=content, **kwargs)
            
            # 调用LLM
            response = await llm.chat([
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ])
            
            # 解析响应
            result = self._parse_response(response)
            return result
            
        except Exception as e:
            logger.error(f"处理失败: {str(e)}")
            return None 