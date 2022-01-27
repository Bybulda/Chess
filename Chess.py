import pygame
from copy import deepcopy
from Appear import sprit, fonte, load_image
import Button
import Config


n = 0
poll = deepcopy(Config.pole)
print(poll[6][0])


def stater(x, y): return poll[x][y] != '-'

def cleaner():
    for i in range(8):
        for j in range(8):
            if poll[i][j] == '*':
                poll[i][j] = '-'


all_sprites = pygame.sprite.Group()


class Buttony(pygame.sprite.Sprite):
    imbel = load_image('кнопка_б.png')
    imch = load_image('кнопка_ч.png')

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

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.cl = 0


    def render(self, surface, b=0):
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
                if i == 0:
                    fonte(self, strk[j], self.left + self.cell_size * j + 40, 110, font, 'white')
                if b == 0:
                    if i % 2 == 0 and j % 2 == 0 or j % 2 == 1 and i % 2 == 1:
                        pygame.draw.rect(surface, (255, 235, 205),
                                         (self.left + self.cell_size * j,
                                          self.top + self.cell_size * i,
                                          self.cell_size,
                                          self.cell_size),
                                         0, border_top_left_radius=brdlt, border_top_right_radius=brdrt,
                                         border_bottom_left_radius=brdll, border_bottom_right_radius=brdlr)
                    else:
                        pygame.draw.rect(surface, (60, 170, 60),
                                         (self.left + self.cell_size * j,
                                          self.top + self.cell_size * i,
                                          self.cell_size,
                                          self.cell_size),
                                         0, border_top_left_radius=brdlt, border_top_right_radius=brdrt,
                                         border_bottom_left_radius=brdll, border_bottom_right_radius=brdlr)
                    if stater(i, j) and poll[i][j] != '*':
                        im = load_image(poll[i][j])
                        screen.blit(im, (self.left + self.cell_size * j, self.top + self.cell_size * i))
                    elif poll[i][j] == '*':
                        pygame.draw.circle(screen, (179, 179, 0), (self.left + self.cell_size * j + 50,
                                                                   self.top + self.cell_size * i + 50), 20)
            positive = [(50, 187, 800, 105), (50, 787, 800, 105), (350, 387, 200, 100), (350, 587, 200, 100)]
            for el in positive:
                pygame.draw.rect(surface, (54, 48, 48),
                                 el,
                                 0, border_top_left_radius=25, border_top_right_radius=25,
                                 border_bottom_left_radius=25, border_bottom_right_radius=25)
            for il in range(290, 691, 400):
                image = load_image(f"палка.png")
                screen.blit(image, (50, il))
            sprit(self)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

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
        return (rowi, coli)

    def on_click(self, cell):
        x, y = cell
        z = ''
        if stater(x, y):
            cleaner()
            if poll[x][y] == 'пешка.png':
                poll[x-1][y], poll[x-2][y] = '*', '*'
                z = '*'
        print(x, y, z)

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
    clock.tick(60)
    f = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            f[0], f[1] = event.pos[0], event.pos[1]

    screen.fill((64, 58, 58))
    board.render(screen)
    all_sprites.draw(screen)
    all_sprites.update(*f)
    pygame.display.flip()

