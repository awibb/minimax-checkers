from board import Board
from piece import Piece
from const import RED, WHITE


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

    def change_teams(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def play(self, x, y):

        self.board.clear_moves()
        print("Current Piece Location: ({},{})".format(x, y))
        pieces = self.board.move_list(self.turn)
        piece = self.board.board[int(x)][int(y)]
        if self.board.can_move(piece) == True:
            moves = self.board.get_valid_moves(piece)
            print("Possible moves for picked piece:")
            for move in moves:
                print(move[1], " ", move[0])
            self.board.draw_moves(moves)
            self.prev_x = x
            self.prev_y = y
            self.board.prev_white_rem = self.board.white_rem
            self.board.prev_red_rem = self.board.red_rem

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

        if(prev_piece.must_attack == True and new_piece.must_attack == True):
            if(self.board.prev_white_rem != self.board.white_rem or self.board.prev_red_rem != self.board.red_rem):
                self._double = True
                prev_piece.must_attack = False

        self.change_teams()
        if(self._double):
            self.change_teams()
            self._double = None
