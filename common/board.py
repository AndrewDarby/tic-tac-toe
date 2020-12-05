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
    
    
    def update_move(self,coord,symbol):
        #place item on board, return true/false if suceed
        if (self.grid[coord[0]][coord[1]] == ' '):
            self.grid[coord[0]][coord[1]] = symbol
            return True
        return False

        
    def is_winner(self):
        #check if game is won
        # 
        for i in range(self.size):
            # is all equal symbol this row
            if all(x == self.grid[i][0] for x in self.grid[i]):
                self.winner = self.grid[i][0]
                return True
            # is diagonal equal forward
            # is diagonal equal reverse
        return True
        return False
        
    def is_game_over(self):
        #check if board is full. game complete it is a tie.
        total_squares = self.size ** 2
        print(f"total squares {total_squares}")
        blank_squares = 0
        for x in range(self.size):
            for y in range(self.size):
                print(f"[{x},{y}] = {self.grid[x][y]}")
                if self.grid[x][y] == ' ':
                    return False
                    break
        return True

     
    def __clear(): 
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else: 
            _ = system('clear') 