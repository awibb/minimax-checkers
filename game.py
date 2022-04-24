from board import Board
from piece import Piece
from const import RED, WHITE
import random


class Game:

    def __init__(self):
        self.board = Board()
        self.turn = RED
        self.moves = []
        self.win = False
        self.prev_x = None
        self._prev_y = None
        self._double = None

    def show(self):
        for row in range(8):
            rzad = " |"
            for column in range(8):
                if(self.board.board[row][column] == 0):
                    rzad += " 0 |"
                elif type(self.board.board[row][column]) == Piece:
                    literka = str(self.board.board[row][column].color)
                    if self.board.board[row][column].color == (255, 255, 255):
                        rzad += " W |"
                    else:
                        rzad += " R |"
            print("-------------------------------------")
            print(row, rzad)
        print("-------------------------------------")
        print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")

    def ai_move(self):
        pieces = self.board.move_list(WHITE)
        piece = random.choice(pieces)
        moves = self.board.get_valid_moves(piece)
        move = random.choice(moves)
        self.board.move(piece, move[0], move[1])
        self.change_teams()

    def change_teams(self):
        if self.turn == RED:
            self.turn = WHITE
            self.ai_move()
        else:
            self.turn = RED

    def play(self, x, y):
        self.board.clear_moves()
        print("Current Piece Location: ({},{})".format(x, y))
        pionek = self.board.board[int(x)][int(y)]
        if self.board.can_move(pionek) == True:
            moves = self.board.get_valid_moves(pionek)
            self.board.draw_moves(moves)
            self.prev_x = x
            self.prev_y = y
            self.board.prev_white_rem = self.board.white_rem
            self.board.prev_red_rem = self.board.red_rem
            print("King: ", pionek.king)

    def show_moves(self):
        moves = self.board.get_valid_moves(self.board.board[2][2])
        for move in moves:
            print(move[0], " ", move[1])

    def show_moveavle_pieces(self, pieces):
        for piece in pieces:
            print(piece.col, " ", piece.row)

    def process_move(self, row, col):
        self.board.clear_moves()
        prev_piece = self.board.board[self.prev_x][self.prev_y]
        self.board.move(prev_piece, int(row), int(col))
        new_piece = self.board.board[row][col]
        if type(new_piece) == Piece:
            new_piece.must_attack = False
            m = self.board.get_valid_moves(new_piece)

        # print("Old White Score: ", self.board.prev_white_rem)
        # print("New White Score: ", self.board.white_rem)
        # print()
        # print("Old Red Score: ", self.board.prev_red_rem)
        # print("New Red Score: ", self.board.red_rem)

        print(self.board.prev_white_rem == self.board.white_rem)
        print(self.board.prev_red_rem == self.board.red_rem)

        if(prev_piece.must_attack == True and new_piece.must_attack == True):
            if(self.board.prev_white_rem != self.board.white_rem or self.board.prev_red_rem != self.board.red_rem):
                print("DOUBLE!")
                self._double = True
                prev_piece.must_attack = False

        self.change_teams()
        if(self._double):
            self.change_teams()
            self._double = None
