import pygame 
from const import BLACK,ROWS, SQUARE_SIZE, RED, COLS, WHITE, GREEN
from piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()
    

    def valid_move_position(self, col, row):
        #takes the row and col position of a value in the 2d board array and converts it to the position of that square on the ui
        return SQUARE_SIZE * col + SQUARE_SIZE // 2, SQUARE_SIZE * row + SQUARE_SIZE // 2


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
        #loops through the board and if the current index board[row][col] is a piece it will be drawn on the ui, if board[row][col] = 1 a green circle will be drawn in the position of board[row][col] on the ui
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if(piece != 0):
                    if piece == 1:
                        pygame.draw.circle(window, GREEN, (self.valid_move_position(col,row)), 15)
                    else:
                        piece.draw(window)

    def find_valid_move(self):
        #hard coded for a visualization but this needs to be implemented
        self.board[4][1] = 1
        self.board[4][3] = 1

    def clear_moves(self):
        #after the move has been processed the board needs to have all green circles removed from it which are represented in the board as 1's
         for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece == 1:
                    self.board[row][col] = 0


        
