"""Contains an ingestor for txt files."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """An ingestor for txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a txt file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        cats = []

        with open(path, 'r', encoding='utf-8-sig') as text_file:
            for line in text_file.readlines():
                # print(f"line: {line}")
                parse = line.strip('\n\r').split(' - ')
                if len(parse) > 1:
                    # print(f"sections: {parse}")
                    new_cat = QuoteModel(parse[0], parse[1].strip())
                    # print(new_cat)
                    cats.append(new_cat)

        return cats
