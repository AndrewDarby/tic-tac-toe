import unittest
from modules.words import filter_words, display_list
from modules.input import validate_position

class MyTest(unittest.TestCase):
    def test_filter_words_returns_correct_output(self):
        l = ['hello','are','cat','dog','ham','hi','go','to','heart']
        self.assertEqual(filter_words(l,'h'), ['hello','ham','hi','heart'])

