
from mcts.mcts import mcts_root, mcts, MCTSNode
from checkers.game import Game

#setup a board
game = Game()
print(game)

#initialize agents
mcts(mcts_root)