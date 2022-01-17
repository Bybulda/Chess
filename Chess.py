import pygame
from Appear import sprit, fonte, load_image
import random
from PIL import Image, ImageFilter

all_sprites = pygame.sprite.Group()

'''for i in range(950, 1651, 100):
    sprite = pygame.sprite.Sprite()
    # определим его вид
    sprite.image = load_image("пешка.png")
    # и размеры
    sprite.rect = sprite.image.get_rect()
    # добавим спрайт в группу
    sprite.rect.x = i
    sprite.rect.y = 740
    all_sprites.add(sprite)'''


'''class Peshka(pygame.sprite.Sprite):
    image = load_image("пешка.png")

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        self.image = Peshka.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)'''


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.cl = 0
        self.figures = {'пешка': [(i, 740) for i in range(950, 1651, 100)], 'ладья': [(950, 840), (1650, 840)],
                        'конь': [(1050, 840), (1550, 840)], 'слон': [(1150, 840), (1450, 840)],
                        'королева': [(1250, 840)], 'король': [(1350, 840)]}

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        n = 8
        strk = 'ABCDEFGH'
        for i in range(len(self.board)):
            fonte(self, n, 930, self.top + self.cell_size * i + 40, font, 'white')
            n -= 1
            for j in range(len(self.board[i])):
                brdlt = 25 if i == 0 and j == 0 else -1
                brdrt = 25 if i == 0 and j == 7 else -1
                brdll = 25 if i == 7 and j == 0 else -1
                brdlr = 25 if i == 7 and j == 7 else -1
                if i % 2 == 0 and j % 2 == 0 or j % 2 == 1 and i % 2 == 1:
                    pygame.draw.rect(surface, (255, 235, 205),
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size,
                                      self.cell_size),
                                     0, border_top_left_radius=brdlt, border_top_right_radius=brdrt,
                                     border_bottom_left_radius=brdll, border_bottom_right_radius=brdlr)
                if i == 0:
                    fonte(self, strk[j], self.left + self.cell_size * j + 40, 110, font, 'white')
                if i % 2 == 1 and j % 2 == 0 or j % 2 == 1 and i % 2 == 0:
                    pygame.draw.rect(surface, (60, 170, 60),
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size,
                                      self.cell_size),
                                     0, border_top_left_radius=brdlt, border_top_right_radius=brdrt,
                                     border_bottom_left_radius=brdll, border_bottom_right_radius=brdlr)
            positive = [(50, 187, 800, 105), (50, 787, 800, 105), (350, 387, 200, 100), (350, 587, 200, 100)]
            # image = load_image(f"пелена.png")
            # screen.blit(image, (0, 0)
            image = load_image(f"кнопка_б.png")
            screen.blit(image, (250, 487))
            for el in positive:
                pygame.draw.rect(surface, (54, 48, 48),
                                 el,
                                 0, border_top_left_radius=25, border_top_right_radius=25,
                                 border_bottom_left_radius=25, border_bottom_right_radius=25)
            for il in range(290, 691, 400):
                image = load_image(f"палка.png")
                screen.blit(image, (50, il))
            sprit(self)

    def get_cell(self, mouse_pos):
        posx, posy = mouse_pos[0] - self.left, mouse_pos[1] - self.top
        if posx <= 0 or posy <= 0:
            return None
        if posx % self.cell_size == 0 or posy % self.cell_size == 0:
            return None
        if posx >= self.cell_size * self.width or posy >= self.cell_size * self.height:
            return None
        coli = posx // self.cell_size
        rowi = posy // self.cell_size
        return rowi, coli

    def on_click(self, cell):
        if cell:
            '''pygame.image.save(screen, "data\\screenshot.png")
            im = Image.open("data\\screenshot.png")
            im2 = im.filter(ImageFilter.GaussianBlur(radius=10))
            im2.save('data\\screenshot.png')
            im3 = load_image('screenshot.png')
            screen.blit(im3, (0, 0))
            pygame.display.flip()

            Peshka(all_sprites)
            all_sprites.draw(screen)
            all_sprites.update()'''


    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
board = Board(8, 8)
board.set_view(950, 140, 100)
running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
scetch = pygame.font.SysFont('arial', 20)

while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((64, 58, 58))
    board.render(screen)
    pygame.display.flip()
