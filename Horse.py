import pygame
from Appear import load_image


all_sprites = pygame.sprite.Group()


class Kon(pygame.sprite.Sprite):
    image = load_image("конь.png")
    im2 = load_image("конь_ч.png")

    def __init__(self, color, position, *group):
        super().__init__(*group)
        self.col = color
        self.image = Kon.image if self.col == "white" else Kon.im2
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def update(self):
        pass


for i in range(1050, 1551, 500):
    Kon('white', (i, 840), all_sprites)
    Kon('b', (i, 140), all_sprites)