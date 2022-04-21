import pygame
from const import SQUARE_SIZE, KING

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
        if self.king:
             pygame.draw.circle(window, KING, (self.x, self.y), radius/1.5)
            
    
    def move(self, row, col):
        self.row = row
        self.col = col
        if row == 0 or row == 7:
            print("elo")
            self.king = True
            print(self.king)
        self.piece_position()
