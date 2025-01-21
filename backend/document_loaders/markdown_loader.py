import markdown
import re
from .base import BaseLoader

class MarkdownLoader(BaseLoader):
    def load(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            md_text = f.read()
        html = markdown.markdown(md_text)
        text = re.sub(r'<[^>]+>', '', html)
        return text 