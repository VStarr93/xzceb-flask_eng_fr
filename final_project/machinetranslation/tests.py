"""
This is a testing module.
"""

import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''
    This class will be used to test my translator application
    '''
    def test_english_to_french(self):
        '''
        This tests the english to french translator
        '''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNotNone(english_to_french('None'), 'Is None')

    def test_french_to_english(self):
        """
        This tests the french to english translator
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertIsNotNone(french_to_english('None'),"Is None")

if __name__ == '__main__':
    unittest.main()
