from docx import Document
from .base import BaseLoader

class DocxLoader(BaseLoader):
    def load(self) -> str:
        doc = Document(self.file_path)
        return '\n'.join([para.text for para in doc.paragraphs]) 