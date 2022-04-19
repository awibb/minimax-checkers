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
        print(y_dec, x_dec)
        self.board[int(y_dec)-1][int(x_dec)-1] = 0
        if(pion.color == 1):
            self.white_rem -= 1
        else:
            self.black_rem -=1
        
    def get_attack_sequence(self, pion, ruch, sequence, koniec):
        self.board[pion.y][pion.x] = 0
        pion.x = ruch[1]
        pion.y = ruch[0]
        moves = self.get_valid_moves(pion, True)
        if moves.size() == 0:
            pion.must_attack = False
            return koniec.append(sequence)
        else:
            for move in moves:
                sekwencja = sequence
                sekwencja.append(move)
                pionek = pion
                self.get_attack_sequence(pionek, move, sekwencja, koniec)


    def move(self, pion, ruch):
        x = pion.x
        y = pion.y
        pion.x = ruch[1]
        pion.y = ruch[0]
        if pion.must_attack == True:
            self.remove(pion, ruch)
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
            if self.board[y_pos+1][x_pos+1] == 0:
                move = [y_pos+1, x_pos+1]
                normal_moves.append(move)
            elif type(self.board[y_pos+1][x_pos+1]) == Zeton:
                if self.board[y_pos+1][x_pos+1].color == pion.color*-1 and x_pos<6 and y_pos<6 and self.board[y_pos+2][x_pos+2] == 0:
                    attack = True
                    move = [y_pos+2, x_pos+2]
                    attack_moves.append(move)
            if self.board[y_pos+1][x_pos-1] == 0:
                move = [y_pos+1, x_pos-1]
                normal_moves.append(move)
            elif type(self.board[y_pos+1][x_pos-1]) == Zeton:
                if self.board[y_pos+1][x_pos-1].color == pion.color*-1 and x_pos>1 and y_pos<6 and self.board[y_pos-1][x_pos+2] == 0:
                    attack = True
                    move = [y_pos+2, x_pos-2]
                    attack_moves.append(move)
            if type(self.board[y_pos-1][x_pos-1]) == Zeton:
                if self.board[y_pos-1][x_pos-1].color == pion.color*-1 and x_pos>1 and y_pos>1 and self.board[y_pos-2][x_pos-2] == 0:
                    attack = True
                    move = [y_pos-2][x_pos-2]
                    attack_moves.append(move)

            if type(self.board[y_pos-1][x_pos+1]) == Zeton: 
                if self.board[y_pos-1][x_pos+1] == pion.color*-1 and x_pos<6 and y_pos>1 and self.board[y_pos-2][x_pos+2] == 0:
                    attack = True
                    move = [y_pos-2][x_pos+2]
                    attack_moves.append(move)

        elif pion.color == -1 or pion.king == True:
            if self.board[y_pos-1][x_pos-1] == 0:
                move = [y_pos-1, x_pos-1]
                normal_moves.append(move)
            elif type(self.board[y_pos-1][x_pos-1]) == Zeton:
                if self.board[y_pos-1][x_pos-1].color == pion.color*-1 and x_pos>1 and y_pos>1 and self.board[y_pos-2][x_pos-2] == 0:
                    attack = True
                    move = [y_pos-2, x_pos-2]
                    attack_moves.append(move)
            if self.board[y_pos-1][x_pos+1] == 0:
                move = [y_pos-1, x_pos+1]
                normal_moves.append(move)
            elif type(self.board[y_pos-1][x_pos+1]) == Zeton:
                if self.board[y_pos-1][x_pos+1].color == pion.color*-1 and x_pos<6 and y_pos>1 and self.board[y_pos-2][x_pos+2] == 0:
                    attack = True
                    move = [y_pos-2, x_pos+2]
                    attack_moves.append(move)
            if type(self.board[y_pos+1][x_pos-1]) == Zeton:
                if self.board[y_pos+1][x_pos-1] == pion.color*-1 and x_pos>1 and y_pos<6 and self.board[y_pos+2][x_pos-2] == 0:
                    attack = True
                    move = [y_pos+2][x_pos-2]
                    attack_moves.append(move)

            if type(self.board[y_pos+1][x_pos+1]) == Zeton:
                if self.board[y_pos+1][x_pos+1] == pion.color*-1 and x_pos<6 and y_pos<6 and self.board[y_pos+2][x_pos+2] == 0:
                    attack = True
                    move = [y_pos+2][x_pos+2]
                    attack_moves.append(move)


        if attack == False:
            return normal_moves
        else:
            pion.must_attack = True
            return attack_moves
