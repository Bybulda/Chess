import Appear


variab = ['кнопка_б.png', 'кнопка_ч.png']
c = 0


class Button:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self, x, y):
        global c
        if 300 >= x >= self.x and self.y <= y <= 587:
            c = (c + 1) % 2
            im = Appear.load_image(variab[c])
            Appear.screen.blit(im, (self.x, self.y))
        else:
            im = Appear.load_image(variab[c])
            Appear.screen.blit(im, (self.x, self.y))
