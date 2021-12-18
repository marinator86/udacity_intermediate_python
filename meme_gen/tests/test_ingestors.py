"""Check that an `Ingestor` can be constructed and parse its files.

To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_ingestors

"""
import pathlib
import math
import unittest

from QuoteEngine import QuoteModel
from QuoteEngine import CSVIngestor
from QuoteEngine import DocxIngestor
from QuoteEngine import PDFIngestor
from QuoteEngine import TextIngestor
from QuoteEngine import Ingestor

# Paths to the test data files.
TESTS_ROOT = (pathlib.Path(__file__).parent).resolve()
TEST_CSV_FILE = TESTS_ROOT / 'DogQuotesCSV.csv'
TEST_DOCX_FILE = TESTS_ROOT / 'DogQuotesDOCX.docx'
TEST_PDF_FILE = TESTS_ROOT / 'DogQuotesPDF.pdf'
TEST_TXT_FILE = TESTS_ROOT / 'DogQuotesTXT.txt'


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_csv(self):
        # GIVEN
        # WHEN
        quotes = CSVIngestor.parse(str(TEST_CSV_FILE))
        # THEN
        self.assertEqual(2, len(quotes))
        first = quotes[0]
        self.assertEqual("Chase the mailman", first.body)
        self.assertEqual("Skittle", first.author)
        second = quotes[1]
        self.assertEqual("When in doubt, go shoe-shopping", second.body)
        self.assertEqual("Mr. Paws", second.author)

    def test_pdf(self):
        # GIVEN
        # WHEN
        quotes = PDFIngestor.parse(str(TEST_PDF_FILE))
        # THEN
        self.assertEqual(3, len(quotes))
        first = quotes[0]
        self.assertEqual("Treat yo self", first.body)
        self.assertEqual("Fluffles", first.author)
        second = quotes[1]
        self.assertEqual("Life is like a box of treats", second.body)
        self.assertEqual("Forrest Pup", second.author)
        third = quotes[2]
        self.assertEqual("It's the size of the fight in the dog", third.body)
        self.assertEqual("Bark Twain", third.author)

    def test_docx(self):
        # GIVEN
        # WHEN
        quotes = DocxIngestor.parse(str(TEST_DOCX_FILE))
        # THEN
        self.assertEqual(4, len(quotes))
        first = quotes[0]
        self.assertEqual("Bark like no one’s listening", first.body)
        self.assertEqual("Rex", first.author)
        second = quotes[1]
        self.assertEqual("RAWRGWAWGGR", second.body)
        self.assertEqual("Chewy", second.author)
        third = quotes[2]
        self.assertEqual("Life is like peanut butter: crunchy", third.body)
        self.assertEqual("Peanut", third.author)
        fourth = quotes[3]
        self.assertEqual("Channel your inner husky", fourth.body)
        self.assertEqual("Tiny", fourth.author)

    def test_txt(self):
        # GIVEN
        # WHEN
        quotes = TextIngestor.parse(str(TEST_TXT_FILE))
        # THEN
        self.assertEqual(2, len(quotes))
        first = quotes[0]
        self.assertEqual("To bork or not to bork", first.body)
        self.assertEqual("Bork", first.author)
        second = quotes[1]
        self.assertEqual("He who smelt it...", second.body)
        self.assertEqual("Stinky", second.author)

    def test_ingestor(self):
        # GIVEN
        # WHEN
        quotes = Ingestor.parse(str(TEST_TXT_FILE))
        # THEN
        self.assertEqual(2, len(quotes))


if __name__ == '__main__':
    unittest.main()
