import os
from typing import Optional
from .base import BaseLoader
from .markdown_loader import MarkdownLoader
from .docx_loader import DocxLoader
from .text_loader import TextLoader
from .json_loader import JSONLoader

class LoaderFactory:
    """文档加载器工厂"""
    
    _loaders = {
        '.json': JSONLoader
    }
    
    @classmethod
    def get_loader(cls, file_path: str) -> Optional[BaseLoader]:
        """获取对应的加载器"""
        ext = os.path.splitext(file_path)[1].lower()
        loader_class = cls._loaders.get(ext)
        
        if not loader_class:
            raise ValueError(f"不支持的文件类型: {ext}")
            
        return loader_class(file_path) 