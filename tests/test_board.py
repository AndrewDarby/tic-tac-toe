import unittest
from parameterized import parameterized
from common.board import Board

RECORD_THE_WINNER = True

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
        (3, [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]),
        (4, [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]),
    ])

    def test_board_grid_is_correct_size(self,size, expected):
        defaultsize = 3;
        board1 = Board(size);
        self.assertEqual(board1.grid,expected)
        
    @parameterized.expand([
        (3,[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[1,1]),
        (3,[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']],[2,1]),
    ])

    def test_board_grid_update_move_allowed(self,size,initial_grid, move):
        board1 = Board(size);
        board1.grid = initial_grid
        self.assertTrue(board1.update_move(move,"X"))
        
    @parameterized.expand([
        (3,[['X',' ',' '],[' ',' ',' '],[' ',' ',' ']],[0,0]),
        (3,[[' ',' ',' '],['X',' ',' '],[' ',' ',' ']],[1,0]),
        (4,[[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],['O','O',' ',' ']],[3,1]),
        (6,[[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ','X']],[5,5]),
    ])

    def test_board_grid_update_move_not_allowed(self,size,initial_grid, move):
        board1 = Board(size);
        board1.grid = initial_grid
        self.assertFalse(board1.update_move(move,"X"))

    @parameterized.expand([
        (3,[0,0],[['X',' ',' '],[' ',' ',' '],[' ',' ',' ']]),
        (3,[1,0],[[' ',' ',' '],['X',' ',' '],[' ',' ',' ']]),
        (4,[3,1],[[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ','X',' ',' ']]),
        (6,[5,5],[[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ','X']]),
    ])

    def test_board_grid_update_move_match_expected(self,size,move,expected_grid):
        board1 = Board(size);
        board1.update_move(move,"X")
        self.assertEqual(board1.grid,expected_grid)
        
    @parameterized.expand([
        (3,[['X','X','O'],['O','X','O'],['X','O','O']]),
        (4,[['X','X','O','O'],['O','X','O','X'],['X','O','O','X'],['X','O','O','X']]),
    ])

    def test_board_is_game_over_true(self,size,initial_grid):
        board1 = Board(size);
        board1.grid = initial_grid
        self.assertTrue(board1.is_game_over())
        
    @parameterized.expand([
        (3,[['X','X','O'],['O','X',' '],['X','O','O']]),
        (4,[['X','X','O',' '],['O','X','O','X'],['X','O','O','X'],['X','O','O','X']]),
    ])

    def test_board_is_game_over_false(self,size,initial_grid):
        board1 = Board(size);
        board1.grid = initial_grid
        self.assertFalse(board1.is_game_over())
        
    @parameterized.expand([
        (3,[['X','X','O'],['O','X',' '],['X','O','X']]),
        (3,[['X','X','X'],['O','X',' '],['O',' ','O']]),
        (3,[['X','X',' '],['O','X',' '],['O','X','O']]),
        (4,[['X',' ','O',' '],['O','X','O','X'],['X','O','X','X'],['X','O','O','X']]),
    ])

    def test_board_is_winner_true(self,size,initial_grid):
        board1 = Board(size);
        board1.grid = initial_grid
        self.assertTrue(board1.is_winner(RECORD_THE_WINNER))   
        
    @parameterized.expand([
        (3,[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]),
        (3,[[' ','X','X'],['O','X',' '],['O',' ','O']]),
        (3,[['X','X',' '],['O','O',' '],['O','X','O']]),
        (4,[['X',' ','O',' '],['O','O','O','X'],['X','O','X','X'],['X','O','O','X']]),
    ])

    def test_board_is_winner_false(self,size,initial_grid):
        board1 = Board(size);
        board1.grid = initial_grid
        self.assertFalse(board1.is_winner(RECORD_THE_WINNER))      
        
    @parameterized.expand([
        (3,[['X','X','O'],['O','X',' '],['X','O','X']],"X"),
        (3,[['X','X','X'],['O','X',' '],['O',' ','O']],"X"),
        (3,[['X','X',' '],['O','X',' '],['O','X','O']],"X"),
        (3,[['X','O','X'],['O','X',' '],['O',' ','X']],"X"),
        (3,[['X','X','O'],['O','O',' '],['O','X','O']],"O"),
        (4,[['X',' ','O',' '],['O','X','O','X'],['X','O','X','X'],['X','O','O','X']],"X"),
        (4,[['X',' ','O',' '],['O','O','O','O'],['X','O','X','X'],['X','O','O','X']],"O"),
    ])

    def test_board_is_winner_winningline_is_corect(self,size,initial_grid,winner):
        board1 = Board(size);
        board1.grid = initial_grid
        board1.is_winner(RECORD_THE_WINNER)
        self.assertEqual(board1.winner,winner) 
        
    @parameterized.expand([
        (3,[['X','X','O'],['O','X',' '],['X',' ',' ']],"X",3),
        (3,[['X','X','X'],['O','X',' '],['O',' ','O']],"O",1),
        (3,[['X','X',' '],['O','O',' '],[' ','X',' ']],"X",2),
        (3,[['O',' ',' '],['X','X',' '],[' ',' ',' ']],"X",3),
        (3,[['O',' ',' '],[' ','X',' '],['X',' ',' ']],"X",4),
        (3,[['O',' ',' '],[' ','X',' '],[' ','X',' ']],"X",4),
        (3,[['O',' ',' '],[' ','X',' '],[' ',' ','X']],"X",5),
        (4,[['O',' ','O',' '],[' ','X',' ',' '],[' ','X',' ',' '],['X',' ',' ',' ']],"X",5),
    ])
    def test_board_possible_win_returns_correct_number(self, size, initial_grid, symbol, expected):
        board1 = Board(size);
        board1.grid = initial_grid
        countpossiblewins = board1.count_possible_winning_lines(symbol)
        self.assertEqual(countpossiblewins,expected)    
        
