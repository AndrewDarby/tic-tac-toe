from modules.words import filter_words, display_list
from modules.input import user_choice
from common.board import Board
from common.player import Player

mylist= [0,1,2,3,4,5,6]
display_list(mylist)

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
first_col = [row[1] for row in matrix]
print(first_col) # [1, 4, 7]

board1 = Board(3);
board1.print();
player1 = Player()
player1.input_position(board1.size)
print(player1.input_coord)


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