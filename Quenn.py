import pygame
from Appear import load_image


all_sprites = pygame.sprite.Group()


class Quen(pygame.sprite.Sprite):
    image = load_image("королева.png")
    im2 = load_image("королева_ч.png")

    def __init__(self, color, position, *group):
        super().__init__(*group)
        self.col = color
        self.image = Quen.image if self.col == "white" else Quen.im2
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        pass


Quen('white', (1250, 840), all_sprites)
Quen('b', (1250, 140), all_sprites)