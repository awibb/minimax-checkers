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
            rzad = "|"
            for column in range(8):
                if(self.board.board[7-row][column] == 0):
                    rzad += " 0 |"
                else:
                    literka = str(self.board.board[7-row][column])
                    if literka == "1":
                        rzad += " 1 |"
                    else:
                        rzad += "-1 |"
            print("----------------------------------")
            print(rzad)
        print("----------------------------------\n")

    
    def play(self):
        while(self.win != True):
            self.show()
            print("Select a piece in a format x y: ")
            x, y = input().split(" ")
            pionek = self.board.board[int(y)-1][int(x)-1]
            if self.board.can_move(pionek) == True:
                moves = self.board.get_valid_moves(pionek)
                print("Input dectination in a format x y: ")
                x_move, y_move = input().split(" ")
                ruch = [int(y_move)-1, int(x_move)-1]
                for move in moves:
                    print(move)
                if ruch in moves:
                    self.board.move(pionek, ruch)
                else:
                    print("Invalid move")

    def show_moves(self):
        moves = self.board.get_valid_moves(self.board.board[2][2])
        for move in moves:
            print(move[0], " ", move[1])