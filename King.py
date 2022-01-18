import pygame
from Appear import load_image


all_sprites = pygame.sprite.Group()


class King(pygame.sprite.Sprite):
    image = load_image("король.png")
    im2 = load_image("король_ч.png")

    def __init__(self, color, position, *group):
        super().__init__(*group)
        self.col = color
        self.image = King.image if self.col == "white" else King.im2
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]