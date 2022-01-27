import pygame
from copy import deepcopy
from Appear import sprit, fonte, load_image
import Config
import Button
import keyboard


poll = deepcopy(Config.pole)
positive = deepcopy(Config.positive)
start = 1
end = 0


def stater(x, y): return poll[x][y] != '-'


def cleaner():
    for i in range(8):
        for j in range(8):
            if poll[i][j] == '*':
                poll[i][j] = '-'


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.cl = 0

    def render(self, surface):
        for i in range(len(self.board)):
            fonte(8 - i % 8, 930, self.top + self.cell_size * i + 40, font, 'white')
            for j in range(len(self.board[i])):
                brdlt = 25 if i == 0 and j == 0 else -1
                brdrt = 25 if i == 0 and j == 7 else -1
                brdll = 25 if i == 7 and j == 0 else -1
                brdlr = 25 if i == 7 and j == 7 else -1
                cmd = (255, 235, 205) if i % 2 == 0 and j % 2 == 0 or j % 2 == 1 and i % 2 == 1 else (60, 170, 60)
                if i == 0:
                    fonte(chr(65 + j % 8), self.left + self.cell_size * j + 40, 110, font, 'white')
                pygame.draw.rect(surface, cmd,
                                 (self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size,
                                  self.cell_size),
                                 border_top_left_radius=brdlt, border_top_right_radius=brdrt,
                                 border_bottom_left_radius=brdll, border_bottom_right_radius=brdlr)

                if stater(i, j) and poll[i][j] != '*':
                    im = load_image(poll[i][j])
                    screen.blit(im, (self.left + self.cell_size * j, self.top + self.cell_size * i))
                elif poll[i][j] == '*':
                    pygame.draw.circle(screen, (179, 179, 0), (self.left + self.cell_size * j + 50,
                                                               self.top + self.cell_size * i + 50), 20)
        screen.blit(load_image('эмблема.png'), (400, 487))
        for el in positive:
            pygame.draw.rect(screen, (54, 48, 48),
                             el,
                             0, border_top_left_radius=25, border_top_right_radius=25,
                             border_bottom_left_radius=25, border_bottom_right_radius=25)
        for il in range(290, 691, 400):
            image = load_image(f"палка.png")
            screen.blit(image, (50, il))
        sprit()

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
        return rowi, coli

    def on_click(self, cell):
        x, y = cell
        z = ''
        if stater(x, y):
            if poll[x][y] == '*':
                poll[x][y] = poll[x+1][y]
                poll[x+1][y] = '-'
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keyboard.is_pressed('escape'):
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            Button.all_sprites.update(event)

    if not running:
        pygame.quit()
    else:
        if keyboard.is_pressed('space'):
            start = 0
        if start:
            screen.blit(load_image('меню_старт.png'), (0, 0))
            pygame.display.flip()
        else:
            screen.fill((64, 58, 58))
            board.render(screen)
            Button.all_sprites.draw(screen)
            pygame.display.flip()
