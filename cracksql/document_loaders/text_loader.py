from cracksql.document_loaders.base import BaseLoader

class TextLoader(BaseLoader):
    def load(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read() 