import pygame
from const import RED, SQUARE_SIZE, WHITE

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
        if row == 0 and self.color == RED:
            self.king = True
        elif row == 7 and self.color == WHITE:
            self.king = True
        self.piece_position()
