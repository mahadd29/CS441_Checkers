import pygame
from pygame import Rect
from checkers.board import Board
from checkers.board_searcher import BoardSearcher

class GameWindow:
    def __init__(self, resolution):
        pygame.init()
        pygame.font.init()
        self.window = pygame.display.set_mode((resolution, resolution))
        pygame.display.set_caption("Checkers")

        self.resolution = resolution
        self.clock = pygame.time.Clock()

        self.square_size = self.resolution/8
        self.piece_radius = (self.square_size / 2) - (0.2 * self.square_size)
        

    # Display the given state on the board
    def update(self, state):
        # Black checkers
        self.window.fill((0, 0, 0))
        
        #Red checkers
        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(self.window, (100, 0, 0), Rect(row * self.square_size, col *self.square_size, self.square_size, self.square_size))
        
        # Game pieces
        for piece in state.pieces:
            if piece.position == None:
                continue

            col = ((32-piece.position) % 4) * 2 * self.square_size + self.square_size/2 + ((((32 - piece.position) // 4) + 1)%2) * self.square_size
            row = ((32-piece.position) // 4)  * self.square_size + self.square_size/2 
            center = (col, row)
            color = (255, 255, 255)
            if piece.player != 1:
                color = (50, 50, 50)
            pygame.draw.circle(self.window, color, center, self.piece_radius)

        pygame.display.update()