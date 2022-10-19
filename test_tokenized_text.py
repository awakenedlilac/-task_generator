# pylint: skip-file
"""
Checks the first lab text preprocessing functions
"""

import unittest
from tasks_gen import TextProcessor

class TokenizeTest(unittest.TestCase):
    """
    Tests tokenize function
    """
    @classmethod
    def setUpClass(cls):
        cls.text_processor = TextProcessor()

    def test_tokenized_text_ideal(self):
        """
        Ideal tokenize scenario
        """
        expected = [['Я был в магазине', ' Купил все продукты', '']]
        actual = self.text_processor.tokenized_text('Я был в магазине. Купил все продукты.')
        self.assertEqual(expected, actual)

    def test_tokenize_several_texts(self):
        """
        tokenizes several texts by #
        """
        self.text_processor = TextProcessor()
        expected = [['Я был в магазине', ''], ['Купил все продукты', '']]
        actual = self.text_processor.tokenized_text("""#\nЯ был в магазине.\n#\nКупил все продукты.""")
        self.assertEqual(expected, actual)

    def test_tokenize_bad_input(self):
        """
        Tokenize bad input argument scenario
        """
        bad_inputs = [[], {}, (), None, 9, 9.34, True]
        expected = None
        for bad_input in bad_inputs:
            actual = self.text_processor.tokenized_text(bad_input)
            self.assertEqual(expected, actual)
