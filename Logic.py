class Table:
    def __init__(self):
        self.moves = []
        self.color = -1
        self.boa = []
        self.x, self.y = 0, 0
        self.fig = ''
        self.eat = []

    def stay(self, a, spot):
        self.boa, self.x, self.y = a, spot[1], spot[0]
        self.fig = a[self.y][self.x].split('.')[0]
        if self.fig[-1] == 'ч':
            self.color, self.eat = 0, ['-', 'я', 'ь', 'н', 'а']
        elif self.fig[-1] != '-':
            self.color, self.eat = 1, ['-', 'ч']

    def pawn(self):
        if self.color == 1:
            if self.y > 0 and self.x > 0 and self.boa[self.y - 1][self.x - 1].split('.')[0][-1] == 'ч':
                self.moves.append([self.y - 1, self.x - 1])
            if self.y > 0 and self.x < 7 and self.boa[self.y - 1][self.x + 1].split('.')[0][-1] == 'ч':
                self.moves.append([self.y - 1, self.x + 1])
            if self.y > 0 and self.boa[self.y - 1][self.x] == '-':
                self.moves.append([self.y - 1, self.x])
            if self.y == 6:
                if self.boa[self.y - 1][self.x] == '-' and self.boa[self.y - 2][self.x] == '-':
                    self.moves.append([self.y - 2, self.x])
        elif self.color == 0:
            if self.y < 7 and self.x > 0 and self.boa[self.y + 1][self.x - 1].split('.')[0][-1] not in ['-', 'ч']:
                self.moves.append([self.y + 1, self.x - 1])
            if self.y < 7 and self.x < 7 and self.boa[self.y + 1][self.x + 1].split('.')[0][-1] not in ['-', 'ч']:
                self.moves.append([self.y + 1, self.x + 1])
            if self.y < 7 and self.boa[self.y + 1][self.x] == '-':
                self.moves.append([self.y + 1, self.x])
            if self.y == 1:
                if self.boa[self.y + 1][self.x] == '-' and self.boa[self.y + 2][self.x] == '-':
                    self.moves.append([self.y + 2, self.x])
        return self.moves

    def king(self):
        if self.color == 1:
            if self.y == 7 and self.boa[self.y][self.x + 3] == 'ладья.png':
                if all([self.boa[self.y][self.x + _] == '-' for _ in range(1, 3)]):
                    self.moves.append([self.y, self.x + 2])
        elif self.color == 0:
            if self.y == 0 and self.boa[self.y][self.x + 3] == 'ладья_ч.png':
                if all([self.boa[self.y][self.x + _] == '-' for _ in range(1, 3)]):
                    self.moves.append([self.y, self.x + 2])
        if self.y > 0 and self.x > 0 and self.boa[self.y - 1][self.x - 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y - 1, self.x - 1])
        if self.y > 0 and self.x < 7 and self.boa[self.y - 1][self.x + 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y - 1, self.x + 1])
        if self.y < 7 and self.x > 0 and self.boa[self.y + 1][self.x - 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y + 1, self.x - 1])
        if self.y < 7 and self.x < 7 and self.boa[self.y + 1][self.x + 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y + 1, self.x + 1])
        if self.x < 7 and self.boa[self.y][self.x + 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y, self.x + 1])
        if self.x > 0 and self.boa[self.y][self.x - 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y, self.x - 1])
        if self.y > 0 and self.boa[self.y - 1][self.x].split('.')[0][-1] in self.eat:
            self.moves.append([self.y - 1, self.x])
        if self.y < 7 and self.boa[self.y + 1][self.x].split('.')[0][-1] in self.eat:
            self.moves.append([self.y + 1, self.x])
        return self.moves

    def knight(self):
        if self.y > 1 and self.x > 0 and self.boa[self.y - 2][self.x - 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y - 2, self.x - 1])
        if self.y > 1 and self.x < 7 and self.boa[self.y - 2][self.x + 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y - 2, self.x + 1])
        if self.y < 6 and self.x > 0 and self.boa[self.y + 2][self.x - 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y + 2, self.x - 1])
        if self.y < 6 and self.x < 7 and self.boa[self.y + 2][self.x + 1].split('.')[0][-1] in self.eat:
            self.moves.append([self.y + 2, self.x + 1])
        if self.y > 0 and self.x > 1 and self.boa[self.y - 1][self.x - 2].split('.')[0][-1] in self.eat:
            self.moves.append([self.y - 1, self.x - 2])
        if self.y < 7 and self.x > 1 and self.boa[self.y + 1][self.x - 2].split('.')[0][-1] in self.eat:
            self.moves.append([self.y + 1, self.x - 2])
        if self.y > 0 and self.x < 6 and self.boa[self.y - 1][self.x + 2].split('.')[0][-1] in self.eat:
            self.moves.append([self.y - 1, self.x + 2])
        if self.y < 7 and self.x < 6 and self.boa[self.y + 1][self.x + 2].split('.')[0][-1] in self.eat:
            self.moves.append([self.y + 1, self.x + 2])
        return self.moves

    def rook(self):
        x = self.x
        y = self.y
        while x < 7:
            if self.boa[y][x + 1].split('.')[0][-1] in self.eat:
                self.moves.append([y, x + 1])
                if self.boa[y][x + 1].split('.')[0][-1] != '-':
                    break
                x += 1
            else:
                break
        x = self.x
        y = self.y
        while x > 0:
            if self.boa[y][x - 1].split('.')[0][-1] in self.eat:
                self.moves.append([y, x - 1])
                if self.boa[y][x - 1].split('.')[0][-1] != '-':
                    break
                x -= 1
            else:
                break
        x = self.x
        y = self.y
        while y < 7:
            if self.boa[y + 1][x].split('.')[0][-1] in self.eat:
                self.moves.append([y + 1, x])
                if self.boa[y + 1][x].split('.')[0][-1] != '-':
                    break
                y += 1
            else:
                break
        x = self.x
        y = self.y
        while y > 0:
            if self.boa[y - 1][x].split('.')[0][-1] in self.eat:
                self.moves.append([y - 1, x])
                if self.boa[y - 1][x].split('.')[0][-1] != '-':
                    break
                y -= 1
            else:
                break
        return self.moves

    def bishop(self):
        x = self.x
        y = self.y
        self.moves = []
        while x < 7 and y < 7:
            if self.boa[y + 1][x + 1].split('.')[0][-1] in self.eat:
                self.moves.append([y + 1, x + 1])
                if self.boa[y + 1][x + 1].split('.')[0][-1] != '-':
                    break
                x, y = x + 1, y + 1
            else:
                break
        x = self.x
        y = self.y
        while x > 0 and y > 0:
            if self.boa[y - 1][x - 1].split('.')[0][-1] in self.eat:
                self.moves.append([y - 1, x - 1])
                if self.boa[y - 1][x - 1].split('.')[0][-1] != '-':
                    break
                x, y = x - 1, y - 1
            else:
                break
        x = self.x
        y = self.y
        while y > 0 and x < 7:
            if self.boa[y - 1][x + 1].split('.')[0][-1] in self.eat:
                self.moves.append([y - 1, x + 1])
                if self.boa[y - 1][x + 1].split('.')[0][-1] != '-':
                    break
                x, y = x + 1, y - 1
            else:
                break
        x = self.x
        y = self.y
        while y < 7 and x > 0:
            if self.boa[y + 1][x - 1].split('.')[0][-1] in self.eat:
                self.moves.append([y + 1, x - 1])
                if self.boa[y + 1][x - 1].split('.')[0][-1] != '-':
                    break
                x, y = x - 1, y + 1
            else:
                break
        return self.moves

    def queen(self):
        self.moves = self.rook()
        self.moves += self.bishop()
        return self.moves
