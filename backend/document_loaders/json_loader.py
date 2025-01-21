import json
from .base import BaseLoader

class JSONLoader(BaseLoader):
    """JSON文件加载器"""
    
    def load(self) -> str:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 将JSON数据转换为字符串形式
            if isinstance(data, (dict, list)):
                # 美化输出,便于后续处理
                return json.dumps(data, ensure_ascii=False, indent=2)
            else:
                return str(data)
                
        except json.JSONDecodeError as e:
            raise ValueError(f"无效的JSON文件: {str(e)}") 