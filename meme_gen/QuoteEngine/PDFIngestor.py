"""Contains an ingestor for pdf files."""
from typing import List
import subprocess
import random
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """An ingestor for pdf files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a pdf file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'

        if not os.path.exists('./tmp'):
            os.makedirs('./tmp')

        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        cats = []

        for line in file_ref.readlines():
            # print(f"line: {line}")
            parse = line.strip('\n\r').split(' - ')
            if len(parse) > 1:
                # print(f"sections: {parse}")
                new_cat = QuoteModel(parse[0][1:-1], parse[1].strip())
                # print(new_cat)
                cats.append(new_cat)

        file_ref.close()
        os.remove(tmp)
        return cats
