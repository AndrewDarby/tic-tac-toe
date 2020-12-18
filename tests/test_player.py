import unittest
from parameterized import parameterized
from common.board import Board
from common.player import Player

class PlayerTest(unittest.TestCase):
        
    def test_validate_new_player_coordiate_is_empty(self):
        player1 = Player()
        self.assertEqual(player1.input_grid_coord,[])
    
    @parameterized.expand([
        ("X"),
        ("O"),
        ("@"),
        ("+"),
    ])       
    def test_validate_new_player_symbol_is_correct(self,character):
        player1 = Player(character)
        self.assertEqual(player1.symbol,character)
    
    @parameterized.expand([
        ("a2",3),
        ("C3",3),
        ("d1",4),
        ("i9",9),
    ])
    def test_player_isvalid_position_returns_true(self,textposition,size):
        player1 = Player()
        self.assertTrue(player1.isvalid_position(textposition,size))

    @parameterized.expand([
        ("d2",3),
        ("C6",3),
        ("d10",4),
        ("p9",9),
    ])
    def test_player_isvalid_position_returns_false(self,textposition,size):
        player1 = Player()
        self.assertFalse(player1.isvalid_position(textposition,size))
        
    @parameterized.expand([
        ("d2",[3,1]),
        ("A1",[0,0]),
        ("e3",[4,2]),
        ("c7",[2,6]),
    ])
    def test_player_set_input_cord_returns_correct_value(self,textposition,coord):
        player1 = Player()
        player1.input_choice = textposition
        player1.set_input_coord()
        self.assertEqual(player1.input_grid_coord,coord)
    #def test_user_choice_returns_correct_data(self):
    #     user_input = [
    #         'c3',
    #     ]
    #     with patch('builtins.input', side_effect=user_input):
    #         boardposition = user_choice()
    #     self.assertEqual(boardposition, [3, 3])