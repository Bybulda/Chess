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
        print(self.fig, self.color)

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


pole = [['ладья_ч.png', 'конь_ч.png', 'слон_ч.png', 'королева_ч.png', 'король_ч.png', 'слон_ч.png', 'конь_ч.png', 'ладья_ч.png'],
        ['пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png', 'пешка_ч.png'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png', 'пешка.png'],
        ['ладья.png', 'конь.png', 'слон.png', 'королева.png', 'король.png', 'слон.png', 'конь.png', 'ладья.png']]

b = [7, 0]
figure, can_moves, proof = Table(), [], pole[b[0]][b[1]].split('.')[0]
figure.stay(pole, b)
if proof == 'пешка' or proof == 'пешка_ч':
    can_moves = figure.pawn()
elif proof == 'король' or proof == 'король_ч':
    can_moves = figure.king()
elif proof == 'конь' or proof == 'конь_ч':
    can_moves = figure.knight()
elif proof == 'ладья' or proof == 'ладья_ч':
    can_moves = figure.rook()
print(can_moves)
if len(can_moves) != 0:
    for i in can_moves:
        if pole[i[0]][i[1]] != '-':
            pole[i[0]][i[1]] = 'с_' + pole[i[0]][i[1]]
        else:
            pole[i[0]][i[1]] = '*'
for i in pole:
    print(i)
