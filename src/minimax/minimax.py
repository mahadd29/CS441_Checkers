# Minimax algorithm implementation file
# This file takes in a Game and finds the optimal move to make in a game of checkers
# CS 441: Group Project
# Authors: Dominique Moore, Alex Salazar

from checkers.game import Game
import copy
import numpy as np

# minimax(s) =
# {
#    Utility(s)                                         if Terminal-Test(s)
#    max{a in set of Actions(s)} Minimax(Result(s,a))   if Player(s) = MAX
#    min{a in set of Actions(s)} Minimax(Result(s,a))   if Player(s) = MIN
# }

# state plays full game from current state to find next optimal move
# state class
#   is either a max node or min node
#   calculate the minimax decision for current state
#   transition to next state base on minimax decision

# function minimax-decision(state) returns an action
#   return argMax{a in set of Actions(s)} Min-Value(Result(state,a))

# function Max-Value(state) returns a utility value
#   if Terminal-Test(state) then return Utility(state)
#   v = -inf
#   for each x in Actions(state) do:
#       v = Max(v,Min-Value(Result(s,x)))
#   return v

# function Min-Value(state) returns a utility value
#   if Terminal-Test(state) then return Utility(state)
#   v = inf
#   for each x in Actions(state) do:
#       v = Min(v,Max-Value(Result(s,x)))
#   return v

# Result(s,x) is the new state, s, after taking action, x.

# function Utility(state) returns a float value
#   Ratio of total number of pieces for player 1 over player 2 (check for zero)
#       if either are zero then a terminal state has been reached
#       if number of pieces for player two is 0, then return a really high value
#   Ratio of the sum of kings + sum of normal pieces of both players     kings = 3, normal piece = 1
#   return (Total pieces P1/Total pieces P2) + (number of kings for P1 + number of normal pieces for P1)/(number of kings for P2 + number of normal pieces for P2)

# function Terminal-Test(state) returns True or False
#   return game.is_over()

MAX_DEPTH = 1

def h1_total_pieces(game_board):
   p1_count = p2_count = 0.0
   p1_pieces = game_board.board.searcher.get_pieces_by_player(1)
   p2_pieces = game_board.board.searcher.get_pieces_by_player(2)
   for p1, p2 in zip(p1_pieces, p2_pieces):
       if not p1.captured:
            p1_count = p1_count + 1.0
       if not p2.captured:
            p2_count = p2_count + 1.0
   if p2_count < 1.0:
       return p1_count
   return (p1_count/p2_count)

def h2_kings_and_reg(game_board):
   p1_points = p2_points = 0.0
   p1_pieces = game_board.board.searcher.get_pieces_by_player(1)
   p2_pieces = game_board.board.searcher.get_pieces_by_player(2)
   for p1, p2 in zip(p1_pieces, p2_pieces):
       if not p1.captured:
           if p1.king:
               p1_points = p1_points + 5.0
           else: p1_points = p1_points + 3.0
       if not p2.captured:
           if p2.king:
               p2_points = p2_points + 5.0
           else: p2_points = p2_points + 3.0
   if p2_points < 1.0:
       return p1_points
   return (p1_points/p2_points)

def min_value(game, depth):
    if game.is_over():
        #return h1_total_pieces(game) + h2_kings_and_reg(game)
        ret = game.get_winner()
        #print("game winner: "+ str(ret))
        if ret == 1:
            return ret+9
        elif ret == 2:
            return -1
        else:
            return 0
    if depth == MAX_DEPTH:
        return (h1_total_pieces(game) + h2_kings_and_reg(game))

    beta = 100000
    #chosen_move = None
    
    all_moves = game.get_possible_moves()
    for a in reversed(all_moves):
        #print("working on " + str(a) + "in the following list:")
        #print(game.get_possible_moves())
        game_copy = copy.deepcopy(game)
        next_move = game_copy.move(a)
        compare = max_value(next_move, depth+1)
        if compare < beta:
            beta = compare
            #chosen_move = next_move
    return beta

# returns a utility value
def max_value(game, depth):
    if game.is_over():
        #return h1_total_pieces(game) + h2_kings_and_reg(game)
        ret = game.get_winner()
        #print("game winner: "+ str(ret))
        if ret == 1:
            return ret+9
        elif ret == 2:
            return -1
        else:
            return 0
    if depth == MAX_DEPTH:
        return (h1_total_pieces(game) + h2_kings_and_reg(game))

    alpha = -100000
    #chosen_move = None
    
    all_moves = game.get_possible_moves()
    for a in reversed(all_moves):
        #print("working on " + str(a) + "in the following list:")
        #print(game.get_possible_moves())
        game_copy = copy.deepcopy(game)
        next_move = game_copy.move(a)
        compare = min_value(next_move, depth+1)
        if compare > alpha:                    
            alpha = compare
            #chosen_move = next_move
    return alpha

def minimax(game):
    max_score = -10000
    move = None
    for a in game.get_possible_moves():
        game_copy = copy.deepcopy(game)
        next_move = game_copy.move(a)
        compare = max_value(next_move,0)
        if compare > max_score:
            max_score = compare
            move = a
    return move
def board_mapping(p):
    if p == 1: return 0, 1
    if p == 2: return 0, 3
    if p == 3: return 0, 5
    if p == 4: return 0, 7
    
    if p == 5: return 1, 0
    if p == 6: return 1, 2
    if p == 7: return 1, 4
    if p == 8: return 1, 6
    
    if p == 9: return 2, 1
    if p == 10: return 2, 3
    if p == 11: return 2, 5
    if p == 12: return 2, 7
    
    if p == 13: return 3, 0
    if p == 14: return 3, 2
    if p == 15: return 3, 4
    if p == 16: return 3, 6
    
    if p == 17: return 4, 1
    if p == 18: return 4, 3
    if p == 19: return 4, 5
    if p == 20: return 4, 7
    
    if p == 21: return 5, 0
    if p == 22: return 5, 2
    if p == 23: return 5, 4
    if p == 24: return 5, 6
    
    if p == 25: return 6, 1
    if p == 26: return 6, 3
    if p == 27: return 6, 5
    if p == 28: return 6, 7
    
    if p == 29: return 7, 0
    if p == 30: return 7, 2
    if p == 31: return 7, 4
    if p == 32: return 7, 6
    
    
    
def display(game):
    board = np.zeros(64).astype(int)
    board = board.reshape(8,8)
    for piece in game.board.pieces:
        if not piece.captured:
            x, y = board_mapping(piece.position)
            if piece.player == 1:
                if piece.king:
                    board[x][y] = 10
                else: board[x][y] = 1
            elif piece.king:
                board[x][y] = 20
            else: board[x][y] = 2
    print(board)
    
def display_move(game, move):
    origin_x, origin_y = board_mapping(move[0]) 
    dest_x, dest_y = board_mapping(move[1]) 
    
    board = np.zeros(64).astype(int)
    board = board.reshape(8,8)
    for piece in game.board.pieces:
        if not piece.captured:
            x, y = board_mapping(piece.position)
            if piece.player == 1:
                if piece.king:
                    board[x][y] = 10
                else: board[x][y] = 1
            elif piece.king:
                board[x][y] = 20
            else: board[x][y] = 2
    
    for row in range(8):
            if row == origin_x:
                print(board[row], end=" ")
                print("<--From Posistion: " + str(origin_y))    
            elif row == dest_x:
                print(board[row], end=" ")
                print("<--To Position: " + str(dest_y))
            else: print(board[row])


if __name__ == "__main__":
    game1 = Game()
    display_move(game1,[1, 5])
  
    while(not game1.is_over()):
        next_move = minimax(game1)
        print("Taking move: " + str(next_move))
        game1.move(next_move)
        display(game1)
    
    print("game winner: "+ str(game1.get_winner()))
        