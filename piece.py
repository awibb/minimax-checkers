import pygame
from const import SQUARE_SIZE, GRAY

class Piece:
    PADDING = 15
    BORDER = 2
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x, self.y = 0,0
        self.piece_position()
    

    def piece_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)