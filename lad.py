import pygame
from Appear import load_image


all_sprites = pygame.sprite.Group()


class Lad(pygame.sprite.Sprite):
    image = load_image("ладья.png")
    im2 = load_image("ладья_ч.png")

    def __init__(self, color, position, *group):
        super().__init__(*group)
        self.col = color
        self.image = Lad.image if self.col == "white" else Lad.im2
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        pass

for i in range(950, 1651, 700):
    Lad('white', (i, 840), all_sprites)
    Lad('b', (i, 140), all_sprites)
