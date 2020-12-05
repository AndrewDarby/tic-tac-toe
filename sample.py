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

print("no loop")

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
"""
Class Board
    handles initialise array to store items on board
    print()
    place_item()
    is_winner()
    is_game_over()
Class Player
    request_input_choice(board)
    input_postion() - enter a2, etc
    isvalid_position() - based on size of board
    is_empty()
Class AIplayer - inherit from Player
    prompt_1_or_2player()
"""
"""
create_board(3)
next_player = 1
while not complete
    display_board()
    move_position = input_move(next_player)
    update_board
    if board_complete exit

"""