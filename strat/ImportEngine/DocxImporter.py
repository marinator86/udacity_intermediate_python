from typing import List
import docx

from .ImportInterface import ImportInterface
from .Cat import Cat

class DocxImporter(ImportInterface):
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception(f"cannot ingest {path}")
        
        cats = []
        doc = docx.Document(path)
        
        for para in doc.paragraphs:
            if para.text is not "":
                p = para.text.split(',')
                cats.append(Cat(p[0], int(p[1]), bool(p[2])))
                
        return cats