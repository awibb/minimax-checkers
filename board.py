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
            self.board.append([])
            for col in range(COLS):
                #default position of pieces using the standard checkers layout
                if col % 2 == ((row + 1) % 2):
                    #all pieces above row 3 will be white
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    #all pieces below row 4 will be red
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    #middle rows get 0's
                    else:
                        self.board[row].append(0)
                #alternating sqaures in rows 1-3 and 4-7 get a 0
                else:
                    self.board[row].append(0)
    
    def draw(self, window):
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if(piece != 0):
                    piece.draw(window)

