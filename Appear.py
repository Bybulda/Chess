import os
import pygame
import sys


screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

figures = ['пешка', 'ладья', 'конь', 'слон', 'королева', 'король']

positive = [(50, 187, 800, 105), (50, 787, 800, 105), (350, 387, 200, 100), (350, 587, 200, 100)]


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


def fonte(word, x, y, fint, color=(255, 235, 205)):
    text = fint.render(f'{word}', True, color)
    screen.blit(text, (x, y))


def sprit():
    xch, ych, yb = 50, 190, 790
    for el in positive:
        pygame.draw.rect(screen, (54, 48, 48),
                         el,
                         0, border_top_left_radius=25, border_top_right_radius=25,
                         border_bottom_left_radius=25, border_bottom_right_radius=25)
    for il in range(290, 691, 400):
        image = load_image(f"палка.png")
        screen.blit(image, (50, il))
    for i in figures:
        image1 = load_image(f"{i}.png")
        screen.blit(image1, (xch, ych))
        image2 = load_image(f"{i}_ч.png")
        screen.blit(image2, (xch, yb))
        xch += 140
    screen.blit(load_image('эмблема.png'), (400, 487))

