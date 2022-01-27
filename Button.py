import pygame
import Appear

all_sprites = pygame.sprite.Group()

class Buttony(pygame.sprite.Sprite):
    imbel = Appear.load_image('кнопка_б.png')
    imch = Appear.load_image('кнопка_ч.png')

    def __init__(self, group=all_sprites):
        super().__init__(group)
        self.image = Buttony.imbel
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 487

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = self.imch
