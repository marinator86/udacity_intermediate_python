"""Check that an `MemeEngine` can be constructed and create a meme.

To run these tests from the project root, run:

    $ python3 -m unittest --verbose tests.test_memeengine

"""
import pathlib
import unittest
from MemeGenerator import MemeEngine


TESTS_ROOT = (pathlib.Path(__file__).parent).resolve()
TEST_IMAGE_FILE = TESTS_ROOT / 'xander_1.jpg'


class TestMemeengine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test_csv(self):
        # GIVEN
        # WHEN
        quote = MemeEngine("./out").make_meme(str(TEST_IMAGE_FILE), "text",
                                              "author", width=200)
        # THEN
        self.assertNotEqual(None, quote)


if __name__ == '__main__':
    unittest.main()
