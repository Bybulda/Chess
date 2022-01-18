import Appear


variab = ['кнопка_б.png', 'кнопка_ч.png']
c = 1

class Button:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def update(self, x, y):
        global c
        if 300 >= x >= self.x and self.y <= y <= 587:
            im = Appear.load_image(variab[c])
            im.fill((54, 48, 48))
            Appear.screen.blit(im, (self.x, self.y))
            im = Appear.load_image(variab[c])
            Appear.screen.blit(im, (self.x, self.y))
            c = (c + 1) % 2

