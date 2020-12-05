"""
#Created 05/12/2020
@author: andrewdarby

represents player 
"""
class Player():
    def __init__(self):
        #setup player
        self.input_choice = ''
        self.input_coord = []
        pass
        
    #def take_turn():
        # prompt user for input and add item to board
    
    def input_position(self,boardsize):
        #request input position from player
        print("Position on board is given by letter for Col = a,b,. and digit for Row =1,2,...")
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
        self.input_coord = [ord(self.input_choice[0].lower())-96,  int(self.input_choice[1])]
            
    #def is_game_over():
        # cehck if board is full. game complete it is a tie.