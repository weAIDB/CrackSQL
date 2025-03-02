from abc import ABC, abstractmethod


class BaseLoader(ABC):
    """文档加载器基类"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self._content = None

    @property
    def content(self) -> str:
        """获取文档内容"""
        if self._content is None:
            self._content = self.load()
        return self._content

    @abstractmethod
    def load(self) -> str:
        """加载文档内容"""
        pass
