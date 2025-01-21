import pdfplumber
from .base import BaseLoader

class PDFLoader(BaseLoader):
    def load(self) -> str:
        text = ""
        with pdfplumber.open(self.file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ''
        return text 