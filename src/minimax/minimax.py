# Minimax algorithm implementation file
# This file takes in a Game and finds the optimal move to make in a game of checkers
# CS 441: Group Project
# Authors: Dominique Moore, Alex Salazar

from checkers.game import Game
import copy

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

def min_value(game):
    if game.is_over():
        #return h1_total_pieces(game) + h2_kings_and_reg(game)
        ret = game.get_winner()
        if ret == 1:
            return ret, game
        elif ret == 2:
            return -1, game
        else:
            return 0, game

    beta = 100000
    best_move = None
   # game_copy = game
    for a in game.get_possible_moves():
        game_copy = copy.deepcopy(game)
        next_move = game_copy.move(a)
        compare, compare_move = max_value(next_move)
        if compare < beta:
            beta = compare
            best_move = compare_move
    return beta, best_move

# returns a utility value
def max_value(game):
    if game.is_over():
        #return h1_total_pieces(game) + h2_kings_and_reg(game)
        ret = game.get_winner()
        if ret == 1:
            return ret, game
        elif ret == 2:
            return -1, game
        else:
            return 0, game

    alpha = -100000
    best_move = None

    for a in game.get_possible_moves():
        print("working on " + str(a) + "in the following list:")
        print(game.get_possible_moves())
        game_copy = copy.deepcopy(game)
        next_move = game_copy.move(a)
        compare, compare_move = min_value(next_move)
        if compare > alpha:
            alpha = compare
            best_move = compare_move
    return alpha, best_move

def minimax(game):
    score, action = max_value(game)
    return action





if __name__ == "__main__":
    game1 = Game()
    
    next_move = minimax(game1)
    #game1.move(next_move)
        