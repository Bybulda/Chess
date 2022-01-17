import os
import pygame
import sys


screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def fonte(self, word, x, y, fint, color):
    text = fint.render(f'{word}', True, color)
    screen.blit(text, (x, y))

def sprit(self):
    xch, ych, yb = 50, 190, 790
    # for i in sorted(self.figures.keys()):
    for i in self.figures.keys():
        image1 = load_image(f"{i}.png")
        screen.blit(image1, (xch, ych))
        image2 = load_image(f"{i}_ч.png")
        screen.blit(image2, (xch, yb))
        xch += 140
        for j in self.figures[i]:
            image = load_image(f"{i}.png")
            screen.blit(image, j)
            image = load_image(f"{i}_ч.png")
            screen.blit(image, (j[0], 140 if j[1] == 840 else 240))