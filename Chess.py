import pygame
from copy import deepcopy
from Appear import sprit, fonte, load_image
import Config
import Button
import keyboard
import os
from datetime import timedelta
from PIL import Image, ImageFilter


end = 0
start = 1
timers = [0, 0]
eatw = [0, 0, 0, 0, 0, 0]
eatb = [0, 0, 0, 0, 0, 0]


def start_game(time):
    if time == 'short':
        timers[0], timers[1] = timedelta(minutes=5), timedelta(minutes=5)
    elif time == 'long':
        timers[0], timers[1] = timedelta(minutes=30), timedelta(minutes=30)
def draw_time():
    fonte(timers[0].__str__(), 375, 418, tim)
    fonte(timers[1].__str__(), 375, 618, tim)


def stater(x, y): return poll[x][y] != '-'


def ender():
    pygame.image.save(screen, "data\\screenshot.png")
    im = Image.open("data\\screenshot.png")
    im2 = im.filter(ImageFilter.GaussianBlur(radius=3))
    im2.save('data\\screenshot.png')
    screen.blit(load_image('screenshot.png'), (0, 0))
    screen.blit(load_image('финишное_меню.png'), (565, 246))


def get_menu_button(mouse_pos):
    x, y = mouse_pos
    if 1296 <= x <= 1716 and 739 <= y <= 943:
        return 'exit'
    elif 755 <= x <= 1175 and 739 <= y <= 943:
        return 'short'
    elif 213 <= x <= 633 and 739 <= y <= 943:
        return 'long'


def cleaner():
    for i in range(8):
        for j in range(8):
            if poll[i][j] == '*':
                poll[i][j] = '-'
            elif 'с_' in poll[i][j]:
                poll[i][j] = poll[i][j][2::]


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
            fonte(8 - i % 8, 930, self.top + self.cell_size * i + 40, font, (255, 235, 205))
            for j in range(len(self.board[i])):
                brdlt = 25 if i == 0 and j == 0 else -1
                brdrt = 25 if i == 0 and j == 7 else -1
                brdll = 25 if i == 7 and j == 0 else -1
                brdlr = 25 if i == 7 and j == 7 else -1
                cmd = (255, 235, 205) if i % 2 == 0 and j % 2 == 0 or j % 2 == 1 and i % 2 == 1 else (60, 170, 60)
                if i == 0:
                    fonte(chr(65 + j % 8), self.left + self.cell_size * j + 40, 110, font, (255, 235, 205))
                pygame.draw.rect(surface, cmd,
                                 (self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size,
                                  self.cell_size),
                                 border_top_left_radius=brdlt, border_top_right_radius=brdrt,
                                 border_bottom_left_radius=brdll, border_bottom_right_radius=brdlr)

                if stater(i, j) and poll[i][j] != '*':
                    im = load_image(poll[i][j])
                    screen.blit(im, (self.left + self.cell_size * j, self.top + self.cell_size * i))
                elif poll[i][j] == '*':
                    pygame.draw.circle(screen, (177, 231, 42), (self.left + self.cell_size * j + 50,
                                                                self.top + self.cell_size * i + 50), 20)
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
                if poll[x-1][y] != '-':
                    poll[x-1][y] = f'c_{poll[x-1][y]}'
                elif poll[x-2][y] != '-':
                    poll[x - 2][y] = f'с_{poll[x-2][y]}'
                else:
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
font = pygame.font.Font(os.path.join('data', 'Leto Text Sans Defect.otf'), 30)
numfig = pygame.font.Font(os.path.join('data', 'Leto Text Sans Defect.otf'), 20)
Menuf = pygame.font.Font(os.path.join('data', 'Leto Text Sans Defect.otf'), 60)
tim = pygame.font.Font(os.path.join('data', 'Leto Text Sans Defect.otf'), 40)


while running:
    clock.tick(10)
    MYTIMER1 = pygame.USEREVENT + 1
    MYTIMER2 = MYTIMER1 + 1
    if not running:
        pygame.quit()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keyboard.is_pressed('escape'):
                running = False
            if event.type == MYTIMER1:
                timers[0] -= timedelta(seconds=1)
            if event.type == MYTIMER2:
                timers[1] -= timedelta(seconds=1)
            if keyboard.is_pressed('alt') and end == 0 and start == 0:
                end = 1
                ender()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start:
                    if get_menu_button(event.pos) == 'exit':
                        running = False
                    elif get_menu_button(event.pos) == 'short':
                        start = 0
                        start_game('short')
                    elif get_menu_button(event.pos) == 'long':
                        start = 0
                        start_game('long')
                    poll = deepcopy(Config.pole)
                elif not start and not end:
                    Button.all_sprites.update(event)
                    cd = Button.button.get_hod()
                    if cd == 'b':
                        pygame.time.set_timer(MYTIMER2, 1000)
                        pygame.time.set_timer(MYTIMER1, 0)
                    elif cd == 'w':
                        pygame.time.set_timer(MYTIMER1, 1000)
                        pygame.time.set_timer(MYTIMER2, 0)
                    board.get_click(event.pos)
        if start:
            screen.blit(load_image('меню_старт.png'), (0, 0))
            fonte('LONG MATCH', 235, 820, Menuf)
            fonte('FAST MATCH', 780, 820, Menuf)
            fonte('EXIT GAME', 1350, 820, Menuf)
        elif end and not start:
            screen.blit(load_image('screenshot.png'), (0, 0))
            screen.blit(load_image('финишное_меню.png'), (565, 246))
        else:
            screen.fill((64, 58, 58))
            board.render(screen)
            Button.all_sprites.draw(screen)
            [fonte(eatw[i], 140 * (i + 1) - 25, 285, numfig) for i in range(6)]
            [fonte(eatb[i], 140 * (i + 1) - 25, 885, numfig) for i in range(6)]
            draw_time()
        pygame.display.flip()
