from io import StringIO 
import unittest
from unittest.mock import patch 
from modules.words import filter_words, display_list
        
class MyTesttwo(unittest.TestCase):
     def display_list_correct_value_to_stdout(self): 
        mylist= [0,1,2,3,4,5,6]
        expectedoutput = "[0, 1, 2, 3, 4, 5, 6]"
          
        with patch('sys.stdout', new = StringIO()) as fake_out: 
            display_list(mylist)
            self.assertEqual(fake_out.getvalue(), expectedoutput)