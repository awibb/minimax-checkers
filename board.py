from cmath import pi
from tkinter import W
import pygame
from const import BLACK, ROWS, SQUARE_SIZE, RED, COLS, WHITE, GREEN
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.turn = RED
        self.create_board()
        self.white_rem, self.red_rem = 12, 12
        self.prev_white_rem, self.prev_red_rem = self.white_rem, self.red_rem

    def set_x_y(self, x, y):
        self.prev_x = x
        self.prev_y = y

    def valid_move_position(self, col, row):
        # takes the row and col position of a value in the 2d board array and converts it to the position of that square on the ui
        return SQUARE_SIZE * col + SQUARE_SIZE // 2, SQUARE_SIZE * row + SQUARE_SIZE // 2

    def draw_squares(self, window):
        # black background
        window.fill(BLACK)
        for row in range(ROWS):
            # draw a red square on every other iteration of the inner loop
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, RED, (row*SQUARE_SIZE,
                                 col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0])

        order = True
        for i in range(3):
            for j in range(COLS):
                if j % 2 == order:
                    self.board[i][j] = Piece(i, j, WHITE)
            order = not order

        order = False
        for i in range(5, 8):
            for j in range(COLS):
                if j % 2 == order:
                    self.board[i][j] = Piece(i, j, RED)
            order = not order

    def draw(self, window):
        # loops through the board and if the current index board[row][col] is a piece it will be drawn on the ui, if board[row][col] = 1 a green circle will be drawn in the position of board[row][col] on the ui
        self.draw_squares(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if(piece != 0):
                    if piece == 1:
                        pygame.draw.circle(
                            window, GREEN, (self.valid_move_position(col, row)), 15)
                    else:
                        piece.draw(window)

    def get_valid_moves(self, piece: Piece, attack=False):
        normal_moves = []
        attack_moves = []
        x_pos = piece.col
        y_pos = piece.row
        print(piece.king)
        if piece.color == WHITE or piece.king == True:
            if y_pos < 7:
                if x_pos < 7:
                    if self.board[y_pos+1][x_pos+1] == 0:
                        move = [y_pos+1, x_pos+1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos+1][x_pos+1]) == Piece:
                        if x_pos < 6 and y_pos < 6:
                            if self.board[y_pos+1][x_pos+1].color == RED and self.board[y_pos+2][x_pos+2] == 0:
                                attack = True
                                move = [y_pos+2, x_pos+2]
                                attack_moves.append(move)
                if x_pos > 0:
                    if self.board[y_pos+1][x_pos-1] == 0:
                        move = [y_pos+1, x_pos-1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos+1][x_pos-1]) == Piece:
                        if x_pos > 1 and y_pos < 6 and self.board[y_pos+2][x_pos-2] == 0:
                            if self.board[y_pos+1][x_pos-1].color == RED and self.board[y_pos+2][x_pos-2] == 0:
                                attack = True
                                move = [y_pos+2, x_pos-2]
                                attack_moves.append(move)
            if x_pos > 1 and y_pos > 1:
                if type(self.board[y_pos-1][x_pos-1]) == Piece:
                    if self.board[y_pos-1][x_pos-1].color == RED and self.board[y_pos-2][x_pos-2] == 0:
                        attack = True
                        move = [y_pos-2, x_pos-2]
                        attack_moves.append(move)

            if x_pos < 6 and y_pos > 1:
                if type(self.board[y_pos-1][x_pos+1]) == Piece:
                    if self.board[y_pos-1][x_pos+1].color == RED and self.board[y_pos-2][x_pos+2] == 0:
                        attack = True
                        move = [y_pos-2, x_pos+2]
                        attack_moves.append(move)

        if piece.color == RED or piece.king == True:
            if y_pos > 0:
                if x_pos > 0:
                    if self.board[y_pos-1][x_pos-1] == 0:
                        move = [y_pos-1, x_pos-1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos-1][x_pos-1]) == Piece:
                        if self.board[y_pos-1][x_pos-1].color == WHITE and x_pos > 1 and y_pos > 1:
                            if self.board[y_pos-2][x_pos-2] == 0:
                                attack = True
                                move = [y_pos-2, x_pos-2]
                                attack_moves.append(move)
                if x_pos < 7:
                    if self.board[y_pos-1][x_pos+1] == 0:
                        move = [y_pos-1, x_pos+1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos-1][x_pos+1]) == Piece:
                        if self.board[y_pos-1][x_pos+1].color == WHITE and x_pos < 6 and y_pos > 1:
                            if self.board[y_pos-2][x_pos+2] == 0:
                                attack = True
                                move = [y_pos-2, x_pos+2]
                                attack_moves.append(move)
            if y_pos < 6:
                if x_pos > 1:
                    if type(self.board[y_pos+1][x_pos-1]) == Piece:
                        if self.board[y_pos+1][x_pos-1].color == WHITE and self.board[y_pos+2][x_pos-2] == 0:
                            attack = True
                            # IndexError: list index out of rang
                            move = [y_pos+2, x_pos-2]
                            attack_moves.append(move)
                if x_pos < 6:
                    if type(self.board[y_pos+1][x_pos+1]) == Piece:
                        if self.board[y_pos+1][x_pos+1].color == WHITE and self.board[y_pos+2][x_pos+2] == 0:
                            attack = True
                            move = [y_pos+2, x_pos+2]
                            attack_moves.append(move)

        if attack == False:
            return normal_moves
        else:
            piece.must_attack = True
            return attack_moves

    def clear_moves(self):
        # after the move has been processed the board needs to have all green circles removed from it which are represented in the board as 1's
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece == 1:
                    self.board[row][col] = 0

    def draw_moves(self, moves):
        for move in moves:
            if move[0] <= 7 and move[1] <= 7:
                if type(self.board[move[0]][move[1]]) and self.board[move[0]][move[1]] == 0:
                    self.board[move[0]][move[1]] = 1

    def remove(self, piece, row, col):
        dx = piece.row
        dy = piece.col
        dx = int((dx + row) // 2)
        dy = int((dy + col) // 2)
        self.board[int(dx)][int(dy)] = 0

        if(piece.color == RED):
            self.white_rem -= 1
        else:
            self.red_rem -= 1

    def move(self, piece, row, col):
        if piece.must_attack == True:
            self.remove(piece, row, col)
            piece.must_attack = False
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def can_move(self, piece):
        if len(self.get_valid_moves(piece)) == 0:
            return False
        return True

    def move_list(self, turn):
        moving_pieces = []
        attack_pieces = []
        flag = False
        for j in range(8):
            for i in range(8):
                if type(self.board[j][i]) == Piece:
                    if self.board[j][i].color == turn:
                        piece = self.board[j][i]
                        if self.can_move(piece):
                            moving_pieces.append(piece)
        for piec in moving_pieces:
            if piec.must_attack == True:
                attack_pieces.append(piec)
                flag = True
        if flag == True:
            return attack_pieces

        return moving_pieces
