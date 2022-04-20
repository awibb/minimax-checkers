from piece import Zeton

class Board:

    def __init__(self):
        self.board = []
        self.black_rem = 12
        self.white_rem = 12
        self.black_king = 0
        self.white_king = 0
        self.turn = 1
        self.create()

    def create(self):
        for row in range(8):
            self.board.append([])
            for column in range(8):
                if (column%2) == (row%2):
                    if row < 3:
                        self.board[row].append(Zeton(column, row, 1))
                    elif row > 4:
                        self.board[row].append(Zeton(column, row, -1))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def remove(self, pion, ruch):
        x_dec = (ruch[1]+pion.x)/2
        y_dec = (ruch[0]+pion.y)/2
        self.board[int(y_dec)][int(x_dec)] = 0
        if(pion.color == 1):
            self.white_rem -= 1
        else:
            self.black_rem -=1
        
    def get_max_attack_lenght(self, pion, ruch, path):
        new_piece = Zeton
        new_piece.x = ruch[1]
        new_piece.y = ruch[0]
        new_piece.color = pion.color
        new_piece.king = pion.king
        previous_location = [pion.y, pion.x]
        moves = self.get_valid_moves(new_piece)
        if new_piece.must_attack == True:
            for move in moves:
                reverse = [move, ruch]
                if reverse not in path:
                    forward = [ruch, move]
                    path.append(forward)
                    lenght = self.get_max_attack_lenght(pion, move, path)+1
                
        

    def move_list(self, turn):
        moving_pieces = []
        attack_pieces = []
        flag = False
        for j in range(8):
            for i in range(8):
                if type(self.board[j][i]) == Zeton:
                    if self.board[j][i].color == turn:
                        piece = self.board[j][i]
                        if self.can_move(piece):
                            moving_pieces.append(piece)
        for piec in moving_pieces:
            if piec.must_attack == True:
                attack_pieces.append(piec)                
                flag = True
        if flag == True:
            max_jumps = 1
            actual_pieces = []
            for piec in attack_pieces:
                moves = self.get_valid_moves(piec)
                if len(moves) > max_jumps:
                    actual_pieces = [piec]
                    max_jumps = placeholder
                elif len(moves) == max_jumps:
                    actual_pieces.append(piec)

            return actual_pieces

        return moving_pieces


    def move(self, pion, ruch):
        x = pion.x
        y = pion.y
        if pion.must_attack == True:
            self.remove(pion, ruch)
        pion.x = ruch[1]
        pion.y = ruch[0]
        self.board[y][x] = 0
        self.board[ruch[0]][ruch[1]] = pion
        if pion.y == 0 and pion.color == -1:
            pion.promote()
        elif pion.y == 7 and pion.color == 1:
            pion.promote()

    def can_move(self, pion):
        if len(self.get_valid_moves(pion)) == 0:
            return False
        return True

    def get_valid_moves(self, pion:Zeton, attack=False):
        normal_moves = []
        attack_moves = []
        x_pos = pion.x
        y_pos = pion.y
        if pion.color == 1 or pion.king == True:
            if y_pos<7:
                if x_pos<7:
                    if self.board[y_pos+1][x_pos+1] == 0:
                        move = [y_pos+1, x_pos+1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos+1][x_pos+1]) == Zeton:
                        if self.board[y_pos+1][x_pos+1].color == pion.color*-1 and x_pos<6 and y_pos<6 and self.board[y_pos+2][x_pos+2] == 0:
                            attack = True
                            move = [y_pos+2, x_pos+2]
                            attack_moves.append(move)
                if x_pos>0:
                    if self.board[y_pos+1][x_pos-1] == 0:
                        move = [y_pos+1, x_pos-1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos+1][x_pos-1]) == Zeton:
                        if self.board[y_pos+1][x_pos-1].color == pion.color*-1 and x_pos>1 and y_pos<6 and self.board[y_pos+2][x_pos-2] == 0:
                            attack = True
                            move = [y_pos+2, x_pos-2]
                            attack_moves.append(move)
            if x_pos>1 and y_pos>1:
                if type(self.board[y_pos-1][x_pos-1]) == Zeton:
                    if self.board[y_pos-1][x_pos-1].color == pion.color*-1  and self.board[y_pos-2][x_pos-2] == 0:
                        attack = True
                        move = [y_pos-2][x_pos-2]
                        attack_moves.append(move)

            if x_pos<6 and y_pos>1:
                if type(self.board[y_pos-1][x_pos+1]) == Zeton:
                    if self.board[y_pos-1][x_pos+1].color == pion.color*-1 and self.board[y_pos-2][x_pos+2] == 0:
                        attack = True
                        move = [y_pos-2][x_pos+2]
                        attack_moves.append(move)

        elif pion.color == -1 or pion.king == True:
            if y_pos > 0:
                if x_pos > 0:
                    if self.board[y_pos-1][x_pos-1] == 0:
                        move = [y_pos-1, x_pos-1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos-1][x_pos-1]) == Zeton:
                        if self.board[y_pos-1][x_pos-1].color == pion.color*-1 and x_pos>1 and y_pos>1:
                            if self.board[y_pos-2][x_pos-2] == 0:
                                attack = True
                                move = [y_pos-2, x_pos-2]
                                attack_moves.append(move)
                if x_pos < 7:
                    if self.board[y_pos-1][x_pos+1] == 0:
                        move = [y_pos-1, x_pos+1]
                        normal_moves.append(move)
                    elif type(self.board[y_pos-1][x_pos+1]) == Zeton:
                        if self.board[y_pos-1][x_pos+1].color == pion.color*-1 and x_pos<6 and y_pos>1:
                            if self.board[y_pos-2][x_pos+2] == 0:
                                attack = True
                                move = [y_pos-2, x_pos+2]
                                attack_moves.append(move)
            if y_pos<6:
                if x_pos>1:
                    if type(self.board[y_pos+1][x_pos-1]) == Zeton:
                        if self.board[y_pos+1][x_pos-1].color == pion.color*-1 and self.board[y_pos+2][x_pos-2] == 0:
                            attack = True
                            move = [y_pos+2][x_pos-2]
                            attack_moves.append(move)
                if x_pos<6:
                    if type(self.board[y_pos+1][x_pos+1]) == Zeton:
                        if self.board[y_pos+1][x_pos+1].color == pion.color*-1 and self.board[y_pos+2][x_pos+2] == 0:
                            attack = True
                            move = [y_pos+2][x_pos+2]
                            attack_moves.append(move)


        if attack == False:
            return normal_moves
        else:
            pion.must_attack = True
            return attack_moves
