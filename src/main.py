
from mcts.mcts import mcts_root, mcts, MCTSNode
from gui.window import GameWindow
from checkers.game import Game

window = GameWindow(800)

game = Game()

while True:
    window.clock.tick(60)
    window.update(game.board)
