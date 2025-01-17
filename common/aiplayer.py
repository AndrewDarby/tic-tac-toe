from common.board import Board
from common.player import Player
import random

DONOT_RECORD_THE_WINNER = False

class AIPlayer(Player):
    
    def __init__(self,X_or_O,heuristic_factor_self,heuristic_factor_opponent):
    #setup aiplayer
        self.heuristic_factor_self = heuristic_factor_self
        self.heuristic_factor_opponent = heuristic_factor_opponent
        super().__init__(X_or_O)
        
    
    def take_turn(self,board):
        #create array of possible moves, based on empty slots
        possiblemoves = self.create_array_next_steps(board)
        #play square with highest score
        order_of_moves = self.order_possible_possible_moves_by_score(board,possiblemoves)
        topscore = order_of_moves[0][1]
        selected_moves = list(filter(lambda x: x[1] == topscore,order_of_moves))
        selected_move = order_of_moves[random.randint(0,len(selected_moves)-1)][0]
        valid_turn = (board.update_move(selected_move,self.symbol))
        if (valid_turn): 
            print(f"AI played the move {selected_move}")
        else:
            print(f"Warning {selected_move} by AI is not valid.")    
        
    def create_array_next_steps(self,board):
        """
        return array with co-ordinates for empty squares
        """
        nextSteps = []
        for i in range(board.size):
            for j in range(board.size):
                if board.grid[i][j] == ' ':
                    nextSteps.append([[i,j],0])
        return nextSteps
        
    def order_possible_possible_moves_by_score(self,board,nextmoves):
        """
        record winning_paths_heuristics - sort by possible winning lines score
        """
        oponentsymbol = ("O" if self.symbol == "X" else "X")
            
        nextSteps = []
        symbols = [self.symbol, oponentsymbol]
        for i in range(len(nextmoves)):
            heuristicscore = 100
            move = nextmoves[i][0]
            board.update_move(move, self.symbol)
            if board.is_winner(DONOT_RECORD_THE_WINNER) : #if winning move for me, score= -200
                heuristicscore += 100
            else: 
                heuristicscore += (self.heuristic_factor_self * board.count_possible_winning_lines(self.symbol)) 
                heuristicscore += (self.heuristic_factor_opponent * board.count_possible_winning_lines(oponentsymbol))
            board.undo_move(move, self.symbol)
            
            board.update_move(move, oponentsymbol)
            if board.is_winner(DONOT_RECORD_THE_WINNER) : #if winning move opponent, top move score -100
                heuristicscore += 50
            board.undo_move(move, oponentsymbol)
            nextmoves[i][1] = heuristicscore
        return sorted(nextmoves, key=lambda k: k[1], reverse=True)
    
        
               