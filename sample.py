from modules.words import filter_words, display_list
from modules.input import user_choice

mylist= [0,1,2,3,4,5,6]
display_list(mylist)

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]
# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
first_col = [row[1] for row in matrix]
print(first_col) # [1, 4, 7]

list = [0,0,0]
list2 = [0]*3
list3 =[5,3,4,6,1]
d = {'simple_key':'hello'}
# Grab 'hello'
print(f"1 {d['simple_key']}")
d = {'k1':{'k2':'hello'}}
print(f"2 {d['k1']['k2']}")
# Grab 'hello'
# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(f"3 {d['k1'][0]['nest_key'][1][0]}")
#Grab hello
# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(f"4 {d['k1'][2]['k2'][1]['tough'][2][0]}")
#Grab hello

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