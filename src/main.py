
from mcts.mcts import mcts, mcts_root, MCTSNode, get_all_possible_moves
from gui.window import GameWindow
from checkers.game import Game

from copy import deepcopy
import random
import time

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
    game = Game()

    window = GameWindow(800)
    mcts_root = MCTSNode(game.board, None, None)
    move_count = 0

    window.update(game.board)
    while True:
        window.clock.tick(60)
        window.update(game.board)
        
        if game.move_limit_reached() or len(get_all_possible_moves(game.board)) == 0:
            break
        
        if game.whose_turn() == 1:
            (node, move) = mcts(mcts_root)
            print("MCTS chooses node with " + str(node.t) + "/" + str(node.n) + " score")
            custom_move_function(game, move)
            mcts_root = node
        
        else:
            possible_moves = get_all_possible_moves(game.board)
            move = random.choice(possible_moves)
            custom_move_function(game, move)
            time.sleep(0.25)
            next_mcts_start = find_state(mcts_root, game.board)
            mcts_root = next_mcts_start if next_mcts_start != None else MCTSNode(game.board, None, None)

        move_count += 1
    
    winner = game.get_winner()
    print("Game completed in " + str(move_count) + " moves. Winner is " + ("MCTS" if winner == 1 else "Minimax" if winner == 2 else "No one"))

if __name__ == "__main__":
    main()