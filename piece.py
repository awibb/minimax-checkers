import pygame
from const import SQUARE_SIZE

class Piece:
    PADDING = 10
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x, self.y = 0,0
        self.king = False
        self.must_attack = False
        self.piece_position()
    
   
    def piece_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.piece_position()
