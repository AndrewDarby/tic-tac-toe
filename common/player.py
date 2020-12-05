"""
#Created 05/12/2020
@author: andrewdarby

represents player 
"""
class Player():
    def __init__(self,X_or_O = "X"):
        #setup player
        self.input_choice = ''
        self.input_grid_coord = []
        self.symbol = X_or_O
        pass
        
    def take_turn(self,board):
        # prompt user for input and add item to board
        print(f"Position your {self.symbol} on board. giving letter for Col = a,b,. and digit for Row =1,2,...")
        
        valid_turn = False
        while not valid_turn:
            self.input_position(board.size)
            self.set_input_cord()
            valid_turn = (board.update_move(self.input_grid_coord,self.symbol))
    
    def input_position(self,boardsize):
        #request input position from player
        
        validinput = False
        position = ""
        while not validinput:
            position = input("Enter position on board; e.g. A1, B3")
            validinput = self.isvalid_position(position,boardsize)
            if not validinput:
                print("First characher must be alpabetic,A,B,C, second char must be numeric digit")

        self.input_choice = position
        
    def isvalid_position(self,position,boardsize):
        # check if chosen position is valid, based on size of board
        maxchar = 97 + boardsize -1
        return len(position) == 2 and position[1].isdigit() and (int(position[1]) <= boardsize) and ord(position[0].lower()) >=97 and ord(position[0].lower()) <=maxchar
        
    def set_input_cord(self):
        self.input_grid_coord = [ord(self.input_choice[0].lower())-97,  int(self.input_choice[1])-1]
            
    #def is_game_over():
        # cehck if board is full. game complete it is a tie.