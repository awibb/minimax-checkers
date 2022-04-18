
class Zeton:

    def __init__(self, x1, y1, player):
        self.x = x1
        self.y = y1
        self.color = player
        self.king = False
        self.must_attack = False

    def move(self, xf, yf):
        self.x = xf 
        self.y = yf

    def promote(self):
        self.king = True

    def __repr__(self):
        return str(self.color)