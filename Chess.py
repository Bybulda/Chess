import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.cl = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, surface):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i % 2 == 0 and j % 2 == 0 or j % 2 == 1 and i % 2 == 1:
                    pygame.draw.rect(surface, (255, 235, 205),
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size,
                                      self.cell_size),
                                     0)
                elif i % 2 == 1 and j % 2 == 0 or j % 2 == 1 and i % 2 == 0:
                    pygame.draw.rect(surface, (60, 170, 60),
                                     (self.left + self.cell_size * j,
                                      self.top + self.cell_size * i,
                                      self.cell_size,
                                      self.cell_size),
                                     0)

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
        x, y = cell[0], cell[1]
        self.board[x][y] = 0 if self.board[x][y] else 1
        for xl in range(0, self.width):
            self.board[x][xl] = 0 if self.board[x][xl] else 1
        for yl in range(0, self.height):
            self.board[yl][y] = 0 if self.board[yl][y] else 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


pygame.init()
screen = pygame.display.set_mode((1400, 900), pygame.FULLSCREEN)
board = Board(8, 8)
board.set_view(400, 100, 100)
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
