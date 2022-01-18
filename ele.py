import pygame
from Appear import load_image


all_sprites = pygame.sprite.Group()


class Slon(pygame.sprite.Sprite):
    image = load_image("слон.png")
    im2 = load_image("слон_ч.png")

    def __init__(self, color, position, *group):
        super().__init__(*group)
        self.col = color
        self.image = Slon.image if self.col == "white" else Slon.im2
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        pass

for i in range(1150, 1451, 300):
    Slon('white', (i, 840), all_sprites)
    Slon('b', (i, 140), all_sprites)
