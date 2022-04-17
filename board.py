import pygame 
from const import BLACK,ROWS, SQUARE_SIZE, RED, COLS, WHITE
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()
    
    def draw_squares(self, window):
        #black background
        window.fill(BLACK)
        for row in range(ROWS):
            #draw a red square on every other iteration of the inner loop
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([0,0,0,0,0,0,0,0])
        
        order = True
        for i in range(3):
            for j in range(COLS):
                if j %  2 == order:
                    self.board[i][j] = Piece(i,j,WHITE)
            order = not order

        order = False
        for i in range(5,8):
            for j in range(COLS):
                if j %  2 == order:
                    self.board[i][j] = Piece(i,j,RED)
            order = not order

    
        
       
    
    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if(piece != 0):
                    piece.draw(window)

