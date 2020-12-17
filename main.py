from modules.words import filter_words, display_list

from common.board import Board
from common.player import Player
from common.aiplayer import AIPlayer

RECORD_THE_WINNER = True

board1 = Board(3);
player1 = Player("X")
player2 = AIPlayer("O")
game_complete = False;
counter = 0
board1.print()
while not game_complete and not board1.is_winner(RECORD_THE_WINNER):
    player1.take_turn(board1) if (counter % 2) == 0 else player2.take_turn(board1)
    if(board1.is_game_over()):
        print("The game was a tie")
        game_complete = True
    counter += 1
    board1.print()

if board1.winner != '':
    print(f"The winner was Player 1") if (player1.symbol) == board1.winner else print(f"The winner was Player 1")
