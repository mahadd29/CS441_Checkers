
from mcts.mcts import mcts, mcts_root, MCTSNode
from gui.window import GameWindow
from checkers.game import Game

from copy import deepcopy
import random
import time

def find_state(tree, board):
    for child in tree.children:
        if board.position_count == child.board.position_count and board.position_layout == child.board.position_layout:
            return child
    return None

def main():
    game = Game()

    window = GameWindow(800)

    mcts_root = MCTSNode(game.board, None, None)
    next_root = None

    move_count = 0
    window.update(game.board)
    while True:
        window.clock.tick(60)
        
        
        # MCTS is "player 1, white"
        if game.whose_turn() == 1:
            (node, move) = mcts(mcts_root)
            print(game.get_possible_moves())
            print(move)
            game.move(move)
            next_root = node
            window.update(game.board)
        
        # Random move chosen by opponent for now
        # Player 2 is black
        else:
            possible_moves = game.get_possible_moves()
            move = random.choice(possible_moves)
            game.move(move)
            mcts_root = find_state(next_root, game.board)
            time.sleep(0.25)
            window.update(game.board)
                
                

        move_count += 1

if __name__ == "__main__":
    main()