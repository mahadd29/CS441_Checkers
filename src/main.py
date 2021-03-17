
from mcts.mcts import mcts, mcts_root, MCTSNode, get_all_possible_moves
from minimax.minimax import minimax
from gui.window import GameWindow
from checkers.game import Game

from copy import deepcopy
import random

# Statistics gathering
import datetime
import time
import csv

import sys


def find_state(tree, board):
    for child in tree.children:
        if board.searcher.player_positions == child.board.searcher.player_positions:
            return child
    return None

def custom_move_function(game, move):
    if move not in get_all_possible_moves(game.board):
        raise ValueError('The provided move is not possible')

    game.board = game.board.create_new_board_from_move(move)
    game.moves.append(move)
    game.moves_since_last_capture = 0 if game.board.previous_move_was_capture else game.moves_since_last_capture + 1

def main():
    if len(sys.argv) == 3:
        mcts_policy = bool(sys.argv[1] == "ucb1")
        minimax_heuristic = bool(sys.argv[2] == "h1h2")
    else:
        print("usage: python main.py <random/ucb1> <h1h2/h1>")
        return
    
    filename = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    mcts_label = "mcts_ucb1_" if mcts_policy else "mcts_randompolicy_"
    minimax_label = "minimax_h1h2_" if minimax_heuristic else "minimax_h1_"
    csvfile = open(mcts_label + minimax_label + str(filename) + '.csv', 'w', newline='')
    fieldnames = ['per game:', 'minimax win (1/0)',	'mcts win (1/0)', 'total time (s)',	'number of moves', 'minimax avg time per move (s)', 'mcts avg time per move (s)', 'minimax pieces left', 'mcts pieces left' ]  
    header_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    header_writer.writeheader()
    csvfile.close()
    
    for _ in range(0, 20):
        with open(mcts_label + minimax_label + str(filename) + '.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            game_instance(writer, mcts_policy, minimax_heuristic)
        
def game_instance(csvlog_writer, mcts_policy, minimax_heuristic):

    game = Game()

    # Set a conservative consecutive noncapture move limit to speed up gameplay
    game.consecutive_noncapture_move_limit = 40

    window = GameWindow(800)
    mcts_root = MCTSNode(game.board, None, None)

    mcts_move_count = 0
    mcts_move_times = {}

    minimax_move_count = 0
    minimax_move_times = {}

    window.update(game.board)
    start_time = time.time()
    while not game.move_limit_reached() and len(get_all_possible_moves(game.board)) != 0:
        window.clock.tick(60)
        window.update(game.board)
        
        if game.whose_turn() == 1:
            mcts_move_start_time = time.time()
            (mcts_child, mcts_move) = mcts(mcts_root, mcts_policy)
            mcts_turn_time = time.time() - mcts_move_start_time
            mcts_move_times[mcts_move_count] = mcts_turn_time

            custom_move_function(game, mcts_move)
            mcts_root = mcts_child
            print("MCTS chooses node with " + str(mcts_child.t) + "/" + str(mcts_child.n) + " score in " + str(mcts_turn_time) + " sec")
            mcts_move_count += 1
        
        else:
            minimax_move_start_time = time.time()
            minimax_move = minimax(game, minimax_heuristic)
            minimax_turn_time = time.time() - minimax_move_start_time
            minimax_move_times[minimax_move_count] = minimax_turn_time

            custom_move_function(game, minimax_move)
            next_mcts_start = find_state(mcts_root, game.board)
            mcts_root = next_mcts_start if next_mcts_start != None else MCTSNode(game.board, None, None)
            print("Minimax chose a move in " + str(minimax_turn_time) + " sec")
            minimax_move_count += 1
    
    end_time = time.time()


    winner = game.get_winner()
    print("Game completed in " + str(mcts_move_count + minimax_move_count) + " moves. Winner is " + ("MCTS" if winner == 1 else "Minimax" if winner == 2 else "No one"))

    # statistics to be written to a csv file
    minimax_win = 1 if winner == 2 else 0
    mcts_win = 1 if winner == 1 else 0
    elapsed_time = end_time - start_time
    move_count = mcts_move_count + minimax_move_count
    mcts_remaining_pieces = len(game.board.searcher.player_pieces[1])
    minimax_remaining_pieces = len(game.board.searcher.player_pieces[2])
    # Average mcts move time
    mcts_average_move_time = 0
    for i in range(0, mcts_move_count):
        mcts_average_move_time += mcts_move_times[i]
    mcts_average_move_time /= mcts_move_count
    # Average minimax move time
    minimax_average_move_time = 0
    for i in range(0, minimax_move_count):
        minimax_average_move_time += minimax_move_times[i]
    minimax_average_move_time /= minimax_move_count
    csvlog_writer.writerow({'minimax win (1/0)': minimax_win, 'mcts win (1/0)': mcts_win, 'total time (s)': elapsed_time, 'number of moves': move_count, 'minimax avg time per move (s)': minimax_average_move_time, 'mcts avg time per move (s)': mcts_average_move_time, 'minimax pieces left': minimax_remaining_pieces, 'mcts pieces left': mcts_remaining_pieces})


    

if __name__ == "__main__":
    main()