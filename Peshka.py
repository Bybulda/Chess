import pygame
from Appear import load_image


all_sprites = pygame.sprite.Group()


class Peshka(pygame.sprite.Sprite):
    image = load_image("пешка.png")
    im2 = load_image("пешка_ч.png")

    def __init__(self, color, position, *group):
        super().__init__(*group)
        self.col = color
        self.image = Peshka.image if self.col == "white" else Peshka.im2
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        pass


for i in range(950, 1651, 100):
    Peshka('white', (i, 740), all_sprites)
    Peshka('b', (i, 240), all_sprites)
