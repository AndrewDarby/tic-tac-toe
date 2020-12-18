from modules.words import filter_words, display_list

from datetime import datetime
from common.board import Board
from common.player import Player
from common.aiplayer import AIPlayer

RECORD_THE_WINNER = True

def game_setup():
    #ask for board size
    validinput = False
    print("Enter Number to select from following Options")
    print("1 - Two Player game")
    print("2 - One Player versus defensive AI")
    print("3 - One Player versus agressive AI")
    while not validinput:
        gameoption = input("Enter size of board between 3 and 10 ")
        if gameoption.isdigit():
            if int(gameoption)>0 and int(gameoption)<4:
                validinput = True
        print("Sorry - You must enter a numeric value!")
    return int(gameoption)

board1 = Board();
gameoption = game_setup()
if gameoption == 1:
    player1 = Player("X")
    player2 = Player("O")
elif gameoption == 2:
    player1 = Player("X")
    player2 = AIPlayer("O",2,-10)
else:
    player1 = Player("X")
    player2 = AIPlayer("O",4,-2)    
game_complete = False;
counter = 0
board1.print()
while not game_complete and not board1.is_winner(RECORD_THE_WINNER):
    player1.take_turn(board1) if (counter % 2) == 0 else player2.take_turn(board1)
    if(board1.is_game_over()):
        print("The game was a tie.")
        game_complete = True
    counter += 1
    board1.print()

if board1.winner != '':
    print(f"The winner was Player 1") if (player1.symbol) == board1.winner else print(f"The winner was Player 1")
    


