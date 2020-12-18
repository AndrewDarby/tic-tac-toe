"""
#Created 05/12/2020
@author: andrewdarby

represents playing board and records position of tiles on board
"""
from os import system, name

class Board():
    def __init__(self,size=0):
        #setup blank board of defined size
        if size == 0:
            self.input_size()
        else:
            self.size = size
        self.grid =[[' ' for i in range(self.size)] for j in range(self.size)]
        self.winner = ''
        
    def input_size(self):
        #ask for board size
        validinput = False
        while not validinput:
            boardsize = input("Enter size of board between 3 and 10 ")
            if boardsize.isdigit():
                if int(boardsize)>2 and int(boardsize)<11:
                    validinput = True
            print("You must enter a numeric value!")

        self.size = int(boardsize)
        
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

    def undo_move(self,coord,symbol):
        #place item on board, return true/false if suceed
        if (self.grid[coord[0]][coord[1]] == symbol):
            self.grid[coord[0]][coord[1]] = ' '
            return True
        return False
        
    def is_winner(self,record_winner):
        #check if game is won
        iswinner = False
        for i in range(self.size):
            # is all equal symbol for current row i
            if self.__is_winning_row(i):
                iswinner = True
                break
            if self.__is_winning_col(i):
                iswinner = True
                break
        # is forward diagonal equal or is reverse diagonal equal
        if self.__is_winning_diagonal_forward() or self.__is_winning_diagonal_reverse(): 
            iswinner = True
        if not record_winner:
            self.winner = '' #reset winner to be blank
        return iswinner
 
    def count_possible_winning_lines(self,mysymbol):
        possible_wins = 0
        for i in range(self.size):
            possible_wins += self.__possible_row(i,mysymbol)
            possible_wins += self.__possible_col(i,mysymbol)
        possible_wins += self.__possible_diagnonal_forward(mysymbol)
        possible_wins += self.__possible_diagnonal_reverse(mysymbol)
        return possible_wins
        
    def __possible_row(self,row_number,symbol):
        """
        check row has symbol or non empty
        """
        if all(x == symbol or x == ' ' for x in self.grid[row_number]): # all square in row grid[i] match symbol or blank
            if sum(x == symbol for x in self.grid[row_number]) > 0:
                return 1 
        return 0
  
    def __possible_col(self,col_number,symbol):
        """
        check col has symbol or non empty
        """
        if all(y[col_number] == symbol or y[col_number] == ' ' for y in self.grid): # all square in col grid match symbol or blank
            if sum(y[col_number] == symbol for y in self.grid) > 0:
                return 1 
        return 0
    
    def __possible_diagnonal_forward(self,symbol):
        """
        check diagonal forward has symbol or non empty
        """
        if all(self.grid[x][x] == ' ' or self.grid[x][x] == symbol for x in range(self.size)):  # all square in col grid match symbol or blank
            if sum(self.grid[x][x] == symbol for x in range(self.size)) > 0:
                return 1 
        return 0   
    
    def __possible_diagnonal_reverse(self,symbol):
        """
        check diagonal reverse has symbol or non empty
        """
        if all(self.grid[x][-1-x] == ' ' or self.grid[x][-1-x] == symbol for x in range(self.size)):  # all square in col grid match symbol or blank
            if sum(self.grid[x][-1-x] == symbol for x in range(self.size)) > 0:
                return 1 
        return 0                  
    
    def __is_winning_diagonal_forward(self):
        """
        check forward diagonal matches
        """
        if all(self.grid[0][0] == self.grid[x][x] and self.grid[0][0] != ' ' for x in range(self.size)): 
            self.winner = self.grid[0][0]
            return True 
        else:
            return False
 
    def __is_winning_diagonal_reverse(self):
        """
        check reverse diagonal matches
        """
        if all(self.grid[0][-1] == self.grid[x][-1-x] and self.grid[0][-1] != ' ' for x in range(self.size)): 
            self.winner = self.grid[0][-1]
            return True 
        else:
            return False
                      
    def __is_winning_row(self, row_number):
        """
        check all cols this row match and non empty
        """
        if all(x == self.grid[row_number][0] and x != ' ' for x in self.grid[row_number]): # all col x in this row grid[i] match
            self.winner = self.grid[row_number][0]
            return True 
        else:
            return False
        
        
    def __is_winning_col(self, col_number):
        """
        check all rows this col match and non empty
        """
        if all(self.grid[0][col_number] == y[col_number] and self.grid[0][col_number] != ' ' for y in self.grid): # every col i for each row y is equal
            self.winner = self.grid[0][col_number]
            return True 
        else:
            return False
              
    def is_game_over(self):
        #check if board is full. game complete it is a tie.
        total_squares = self.size ** 2
        blank_squares = 0
        for x in range(self.size):
            for y in range(self.size):
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