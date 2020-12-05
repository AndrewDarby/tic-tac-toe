"""
#Created 05/12/2020
@author: andrewdarby

represents playing board and records position of tiles on board
"""
from os import system, name

class Board():
    def __init__(self,size=3):
        #setup blank board of defined size
        self.grid =[[' ' for i in range(size)] for j in range(size)]
        self.size = size
        
    def print(self):
        # output contents of board to screen
        self.__clear
        for i in range(self.size):
            print(' |', end='')
            for j in range(self.size):
                print(f"  {self.grid[i][j]}  |", end='') 
            print()
            print(f" {'-'*self.size*6}-")
    
    
    #def place_item():
    #     #place item on board, return true/false if suceed
        
    # def is_winner():
    #     # check if game is won
        
    # def is_game_over():
    #     # cehck if board is full. game complete it is a tie.
    # define our clear function
     
    def __clear(): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 