import unittest
from parameterized import parameterized
from common.aiplayer import AIPlayer
from common.board import Board

class AIPlayerTest(unittest.TestCase):
    @parameterized.expand([
        ("X"),
        ("O"),
        ("@"),
        ("+"),
    ])       
    def test_validate_new_aiplayer_symbol_is_correct(self,character):
        aiplayer1 = AIPlayer(character)
        self.assertEqual(aiplayer1.symbol,character)
        
    @parameterized.expand([
        (3,[[[0,2],'X'],[[1,1],'O']],
        [[[0,0],0],[[0,1],0],[[1,0],0],[[1,2],0],[[2,0],0],[[2,1],0],[[2,2],0]]),
        (3,[[[0,1],'X'],[[1,1],'O'],[[1,2],'O']],
        [[[0,0],0],[[0,2],0],[[1,0],0],[[2,0],0],[[2,1],0],[[2,2],0]]),
    ])
    def test_create_array_next_steps_returns_correct_moves(self,size,moves, expected):
        aiplayer1 = AIPlayer()
        board1 = Board(size);
        for move in moves:
            board1.update_move(move[0],move[1])
        possiblesteps = aiplayer1.create_array_next_steps(board1)
        self.assertEqual(possiblesteps,expected)
        
    @parameterized.expand([
        (3,"X",[['O',' ',' '],[' ','X',' '],[' ',' ',' ']],
        [[[0,1],0],[[0,2],0],[[1,0],0],[[1,2],0],[[2,0],0],[[2,1],0],[[2,2],0]],
        [[[0,2],98],[[2,0],98],[[0,1],96],[[1,0],96],[[2,2],90],[[1,2],88],[[2,1],88]]),
        (3,"X",[['O','X','O'],[' ','X',' '],['O',' ','X']],
        [[[1,0],0],[[1,2],0],[[2,1],0]],
        [[[2,1],200],[[1,0],154],[[1,2],94]]),
    ])  
    def test_evaluate_possible_winning_paths_gives_correct_array(self,size,character,initial_grid,nextsteps,expected_list):
        """
        docstring
        """
        aiplayer1 = AIPlayer(character)
        board1 = Board(size);
        board1.grid = initial_grid
        sortedsteps = aiplayer1.evaluate_possible_winning_paths(board1,nextsteps)
        self.assertEqual(sortedsteps,expected_list)
    
    @parameterized.expand([
        (3,"X",[['O','X','O'],['X','X',' '],[' ','O',' ']],
        [[[1,2],0],[[2,0],0],[[2,2],0]],
        [[[1, 2], 200], [[2, 2], 102], [[2, 0], 92]]),
        (3,"X",[['O','X','O'],[' ','X',' '],['O',' ','X']],
        [[[1,0],0],[[1,2],0],[[2,1],0]],
        [[[2, 1], 200], [[1, 0], 154], [[1, 2], 94]]),
        (5,"X",[[' ',' ','X','O',' '],[' ','X','X','O',' '],[' ',' ','X','O',' '],[' ',' ',' ',' ','O'],[' ',' ','X','O',' ']],
        [[[0,0],0],[[0,1],0],[[0,4],0],[[1,0],0],[[1,4],0],[[2,0],0],[[2,4],0],
         [[3,0],0],[[3,1],0],[[3,2],0],[[3,3],0],[[4,0],0],[[4,1],0],[[4,4],0]],
        [[[3, 2], 200], [[3, 3], 146], [[3, 0], 88], [[0, 4], 86], [[1, 4], 86], [[2, 4], 86], [[3, 1], 86], 
         [[4, 4], 86], [[0, 0], 78], [[1, 0], 78], [[2, 0], 78], [[4, 0], 78], [[0, 1], 76], [[4, 1], 76]]),
        (6,"X",[[' ',' ','X','O',' ','O'],[' ','X','X','O','X','X'],[' ',' ','X','O',' ','X'],
            [' ',' ','X','O',' ','X'],[' ',' ',' ',' ','O','O'],[' ','X','X','O','X','X']],
        [[[0,0],0],[[0,1],0],[[0,4],0],[[1,0],0],[[2,0],0],[[2,1],0],[[2,4],0],
         [[3,0],0],[[3,1],0],[[3,4],0],[[4,0],0],[[4,1],0],[[4,2],0],[[4,3],0]],
        [[[4, 2], 200], [[4, 3], 154], [[4, 0], 96], [[4, 1], 94], [[0, 0], 86], [[1, 0], 86], [[2, 0], 86],
         [[3, 0], 86], [[0, 1], 84], [[0, 4], 84], [[2, 1], 84], [[2, 4], 84], [[3, 1], 84], [[3, 4], 84]]),
        (6,"X",[[' ',' ','X','O',' ','O'],[' ','X','X','X','X','X'],[' ',' ','X','O',' ','X'],
        [' ',' ','X','O',' ','X'],[' ',' ',' ',' ','O','O'],[' ','X','X','O','X','X']],
        [[[0,0],0],[[0,1],0],[[0,4],0],[[1,0],0],[[2,0],0],[[2,1],0],[[2,4],0],
         [[3,0],0],[[3,1],0],[[3,4],0],[[4,0],0],[[4,1],0],[[4,2],0],[[4,3],0]],
        [[[1, 0], 200], [[4, 2], 200], [[4, 0], 108], [[4, 1], 106], [[4, 3], 106], [[0, 0], 98], [[2, 0], 98], [[3, 0], 98], [[0, 1], 96], [[0, 4], 96], [[2, 1], 96], [[2, 4], 96], [[3, 1], 96], [[3, 4], 96]]),
    ])  
    def test_evaluate_possible_winning_paths_picks_winning_move(self,size,character,initial_grid,nextsteps,expected_list):
        """
        docstring
        """
        aiplayer1 = AIPlayer(character)
        board1 = Board(size);
        board1.grid = initial_grid
        sortedsteps = aiplayer1.evaluate_possible_winning_paths(board1,nextsteps)
        print(sortedsteps)
        self.assertEqual(sortedsteps,expected_list)