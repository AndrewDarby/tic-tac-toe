import unittest
from parameterized import parameterized
from common.board import Board

class BoardTest(unittest.TestCase):
    
    @parameterized.expand([
        (3,3),
        (4,4),
        (10,10),
    ])

    def test_board_size_value_equals_setting(self,size,expected):
        defaultsize = 3;
        board1 = Board(size);
        self.assertEqual(board1.size,expected)
        
    @parameterized.expand([
        (3, [['','',''],['','',''],['','','']]),
        (4, [['','','',''],['','','',''],['','','',''],['','','','']]),
    ])

    def test_board_grid_is_correct_size(self,size, expected):
        defaultsize = 3;
        board1 = Board(size);
        self.assertEqual(board1.grid,expected)
