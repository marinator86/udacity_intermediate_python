"""Contains an ingestor for csv files."""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """An ingestor for csv files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a csv file."""
        if not cls.can_ingest(path):
            raise Exception(f"cannot ingest {path}")

        cats = []
        df = pandas.read_csv(path, header=0)

        for i, row in df.iterrows():
            cats.append(QuoteModel(row['body'], row['author']))

        return cats
