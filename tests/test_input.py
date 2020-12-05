from unittest import mock
import unittest
from modules.input import validate_position

class MyTest2(unittest.TestCase):
    def test_validate_position_returs_true(self):
        self.assertTrue(validate_position("a3"))
        self.assertTrue(validate_position("a1"))
        self.assertTrue(validate_position("A3"))
        self.assertTrue(validate_position("b2"))
        self.assertTrue(validate_position("c3"))

    def test_validate_position_returs_false(self):
        self.assertFalse(validate_position("33"))
        self.assertFalse(validate_position("3f"))
        self.assertFalse(validate_position("F3"))
        self.assertFalse(validate_position("Ff"))

    #def test_user_choice_returns_correct_data(self):
    #     user_input = [
    #         'c3',
    #     ]
    #     with patch('builtins.input', side_effect=user_input):
    #         boardposition = user_choice()
    #     self.assertEqual(boardposition, [3, 3])