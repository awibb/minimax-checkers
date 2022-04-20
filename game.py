from board import Board
from piece import Piece
from const import RED, WHITE

class Game:
    
    def __init__(self):
        self.board = Board()
        self.turn = RED
        self.moves = []
        self.win = False

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
            print(row , rzad)
        print("-------------------------------------")
        print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")

    
    def play(self, x,y):
        #debug
        self.show()
        print("Current Piece Location: ({},{})".format(x,y))
        pieces = self.board.move_list(self.turn)
        print("List of all pieces that can move at current moment:")
        self.show_moveavle_pieces(pieces)
        pionek = self.board.board[int(x)][int(y)]
        #if pionek.color == self.turn:
        if self.board.can_move(pionek) == True:
            moves = self.board.get_valid_moves(pionek)
            print("Possible moves for picked piece:")
            for move in moves:
                print(move[1], " ", move[0])
            print("Input dectination in a format x y: ")
            x_move, y_move = input().split(" ")
            ruch = [int(y_move), int(x_move)]
            if ruch in moves:
                self.board.move(pionek, int(y_move), int(x_move))
                if self.turn == RED:
                    self.turn = WHITE
                else:
                    self.turn = RED
            else:
                print("Invalid move")

    def show_moves(self):
        moves = self.board.get_valid_moves(self.board.board[2][2])
        for move in moves:
            print(move[0], " ", move[1])

    def show_moveavle_pieces(self, pieces):
        for piece in pieces:
            print(piece.col, " ", piece.row)