"""Contains an ingestor for all supported quote source files."""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """An ingestor for all supported file types.

    Encapsulates and employs all available specific ingestors.
    """

    allowed_extensions = ['csv', 'docx', 'pdf', 'txt']
    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a quote source file."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
