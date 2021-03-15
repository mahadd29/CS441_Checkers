
from mcts.mcts import mcts_root, mcts, MCTSNode
from gui.window import GameWindow
from checkers.game import Game

window = GameWindow(800)

while True:
    window.clock.tick(60)
    window.update(game.board)
