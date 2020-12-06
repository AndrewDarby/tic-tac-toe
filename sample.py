from modules.words import filter_words, display_list

from common.board import Board
from common.player import Player

board1 = Board(3);
player1 = Player("X")
player2 = Player("O")
game_complete = False;
counter = 0
print(f"iswinner: {board1.is_winner()}")
while not game_complete and not board1.is_winner():
    board1.print()
    player1.take_turn(board1) if (counter % 2) == 0 else player2.take_turn(board1)
    if(board1.is_game_over()):
        print("The game was a tie")
        game_complete = True
    counter += 1

if board1.winner != '':
    print(f"The winner was Player 1") if (player1.symbol) == board1.winner else print(f"The winner was Player 1")

#print(user_choice())
# Assign s as a string
# Create a new list
# list1 = [1,2,3]
# # Append
# list1.append('append me!')
# # Show
# print(list1) # [1, 2, 3, 'append me!']
# # Assign the popped element, remember default popped index is -1
# popped_item = list1.pop()
# print(popped_item) # append me!

#print(list1) # [2, 3, 'append me!']
