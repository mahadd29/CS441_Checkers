
from mcts.mcts import mcts_root, mcts, MCTSNode
from gui.window import GameWindow
from checkers.game import Game

#setup a board
game = Game()
print(game)

#initialize agents
#mcts(mcts_root)

window = GameWindow(800)



while True:
    window.clock.tick(60)
    window.update(game.board)