"""Contains an ingestor for docx files."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """An ingestor for docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a docx file."""
        if not cls.can_ingest(path):
            raise Exception(f"cannot ingest {path}")

        cats = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            # print(f"line: {line}")
            parse = para.text.strip('\n\r').split(' - ')
            if len(parse) > 1:
                # print(f"sections: {parse}")
                new_cat = QuoteModel(parse[0][1:-1], parse[1].strip())
                # print(new_cat)
                cats.append(new_cat)
        return cats
