from board import Board
from piece import Zeton

class Game:
    
    def __init__(self):
        self.board = Board()
        self.turn = 1
        self.moves = []
        self.win = False

    def show(self):
        for row in range(8):
            rzad = " |"
            for column in range(8):
                if(self.board.board[row][column] == 0):
                    rzad += " 0 |"
                else:
                    literka = str(self.board.board[row][column])
                    if literka == "1":
                        rzad += " B |"
                    else:
                        rzad += " W |"
            print("-------------------------------------")
            print(row , rzad)
        print("-------------------------------------")
        print("   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")

    
    def play(self):
        while(self.win != True):
            self.show()
            pieces = self.board.move_list(self.turn)
            print("List of all pieces that can move at current moment:")
            self.show_moveavle_pieces(pieces)
            print("Select a piece in a format x y: ")
            x, y = input().split(" ")
            pionek = self.board.board[int(y)][int(x)]
            if pionek.color == self.turn:
                if self.board.can_move(pionek) == True:
                    moves = self.board.get_valid_moves(pionek)
                    print("Possible moves for picked piece:")
                    for move in moves:
                        print(move[1], " ", move[0])
                    print("Input dectination in a format x y: ")
                    x_move, y_move = input().split(" ")
                    ruch = [int(y_move), int(x_move)]
                    if ruch in moves:
                        self.board.move(pionek, ruch)
                        self.turn = self.turn*-1
                    else:
                        print("Invalid move")

    def show_moves(self):
        moves = self.board.get_valid_moves(self.board.board[2][2])
        for move in moves:
            print(move[0], " ", move[1])

    def show_moveavle_pieces(self, pieces):
        for piece in pieces:
            print(piece.x, " ", piece.y)