from types import new_class
from board import Board
from piece import Piece
from const import RED, WHITE
from cmath import inf
from copy import deepcopy


class Game:

    def __init__(self):
        self.board = Board()
        self.turn = RED
        self.moves = []
        self.win = False
        self.prev_x = None
        self._prev_y = None
        self.counter = 0

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

    def minimax(self, state, depth, max_player, alpha, beta):
        copy_state = deepcopy(state)
        result = depth == 0 or self.win
        if result:
            return copy_state.evaluate()

        best_score = -inf if max_player else inf
        pieces = copy_state.move_list(
            WHITE) if max_player else copy_state.move_list(RED)
        for piece in pieces:
            moves = copy_state.get_valid_moves(piece)
            for m in moves:
                copy_state.move(piece, m[0], m[1])
                score = self.minimax(
                    copy_state, depth-1, False, alpha, beta) if max_player else self.minimax(copy_state, depth-1, True, alpha, beta)
                copy_state = deepcopy(state)
                best_score = max(score, best_score) if max_player else min(
                    score, best_score)
                if max_player:
                    alpha = max(alpha, best_score)
                    if alpha >= beta:
                        break
                elif max_player == False:
                    beta = min(best_score, beta)
                    if alpha >= beta:
                        break
                self.counter += 1

        return best_score

    def ai_move(self):
        best_move = None
        best_score = -inf
        board_copy = deepcopy(self.board)
        pieces = board_copy.move_list(WHITE)
        for piece in pieces:
            row, col = piece.row, piece.col
            moves = board_copy.get_valid_moves(piece)
            for m in moves:
                board_copy.move(piece, m[0], m[1])
                score = self.minimax(board_copy, 4, False, -inf, inf)
                board_copy = deepcopy(self.board)
                if score > best_score:
                    best_score = score
                    best_move = [row, col, m[0], m[1]]
        # doesn't make sense(row and col isnt a valid piece)
        # print(best_move)
        move_piece = self.board.board[best_move[0]][best_move[1]]

        # needs to be run for the attack flag to be true and remove pieces
        self.board.get_valid_moves(move_piece)
        self.board.move(move_piece, best_move[2], best_move[3])
        print("Possible states: ", self.counter)
        self.counter = 0

    def change_teams(self):
        if self.turn == RED:
            self.turn = WHITE
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
        self.change_teams()
