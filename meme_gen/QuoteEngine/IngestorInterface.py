"""Contains an abstract class for ingestors."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract class for ingestors.

    Offers a common interface for all types of quote sources.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if this ingestor can ingest a file.

        :param path: the path of the file to ingest, e.g. './data/quote.csv'
        :return: true if this ingestor instance can ingest the file, else false
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a quote source file to a list of quotes.

        :param path: the path of the file to parse, e.g. './data/quote.csv'
        :return: a list of quotes, or an empty list
        """
        pass
