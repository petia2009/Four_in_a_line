import pygame

SPRITE_FOLDER = "sprites/game/"
BG_SPRITE = SPRITE_FOLDER + "bg.png"
RED_HOT_SPRITE = SPRITE_FOLDER + "f_player.png"
BLUE_HOT_SPRITE = SPRITE_FOLDER + "s_player.png"
PG_CELL_SIZE = 50
F_PLAYER = "red"
S_PLAYER = "blue"
NONE = "none"


class Game:
    def __init__(self, window, fps, pg_width, pg_height):
        self.win = window
        self.fps = fps
        self.pg_wdt = pg_width
        self.pg_hgh = pg_height
        self.bg = pygame.image.load(BG_SPRITE)
        self.f_player = pygame.image.load(RED_HOT_SPRITE)
        self.s_player = pygame.image.load(BLUE_HOT_SPRITE)
        self.run_game = True
        self.field = self.init_field(pg_height, pg_width)

    scene = 1

    pg_x = 75
    pg_y = 125
    move_x = 75
    move_y = 125
    move_wdt = 50
    move_hgh = 50

    selected_player = F_PLAYER
    is_move_selected = False
    move_cell_x = 0
    move_cell_y = 0
    selected_key = "none"

    def draw_bg(self):
        self.win.blit(self.bg, (0, 0))

    def draw_pg(self):
        row = 0
        column = 0
        while row < self.field.__len__():
            while column < self.field[row].__len__():
                self.draw_cell(self.pg_x, self.pg_y, self.field[row][column])
                self.pg_x = self.pg_x + PG_CELL_SIZE
                column += 1
            self.pg_y = self.pg_y + PG_CELL_SIZE

            self.pg_x = 75
            column = 0
            row += 1
        self.pg_y = 125

    def draw_cell(self, x, y, color):
        if color == NONE:
            pygame.draw.rect(self.win, (0, 0, 0), (x, y, PG_CELL_SIZE, PG_CELL_SIZE))
        elif color == F_PLAYER:
            pygame.draw.rect(self.win, (255, 0, 0), (x, y, PG_CELL_SIZE, PG_CELL_SIZE))
        elif color == S_PLAYER:
            pygame.draw.rect(self.win, (0, 0, 255), (x, y, PG_CELL_SIZE, PG_CELL_SIZE))
        else:
            pygame.draw.rect(self.win, (0, 0, 0), (x, y, PG_CELL_SIZE, PG_CELL_SIZE))
            self.win.blit(color, (x, y))

    def draw_player_move(self):
        sprite = self.f_player if self.selected_player == F_PLAYER else self.s_player
        self.win.blit(sprite, (
            self.move_x + PG_CELL_SIZE * self.move_cell_x,
            self.move_y + PG_CELL_SIZE * self.move_cell_y - self.move_hgh
        ))
        if self.move_cell_y < self.pg_hgh:
            self.move_cell_y += 1
        else:
            self.record_hot()
            self.change_move()

    def check_event(self):
        self.selected_key = "none"
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.scene = -1
                self.run_game = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.scene = 0
                    self.run_game = False
                if ev.key == pygame.K_RIGHT:
                    self.selected_key = "right"
                if ev.key == pygame.K_LEFT:
                    self.selected_key = "left"
                if ev.key == pygame.K_RETURN or ev.key == pygame.K_KP_ENTER:
                    self.is_move_selected = True

    def start(self):
        while self.run_game:
            self.check_event()

            self.draw_bg()
            self.draw_pg()
            if self.is_move_selected:
                self.draw_player_move()
            else:
                self.draw_hot_to_select()
                self.choose_column()
            pygame.display.update()
            pygame.time.wait(self.fps)
        return self.scene

    @staticmethod
    def init_field(size_x, size_y):
        field = [0] * size_x
        for row in range(0, size_x):
            field[row] = [0] * size_y
            for i in range(0, size_y):
                field[row][i] = NONE
        return field

    def choose_column(self):
        if self.selected_key == "right":
            if self.move_cell_x < self.field[0].__len__() - 1:
                self.move_cell_x += 1
            else:
                self.move_cell_x = 0
        if self.selected_key == "left":
            if self.move_cell_x > 0:
                self.move_cell_x -= 1
            else:
                self.move_cell_x = self.field[0].__len__() - 1

    def draw_hot_to_select(self):
        sprite = self.f_player if self.selected_player == F_PLAYER else self.s_player
        self.win.blit(sprite, (self.pg_x + self.move_cell_x * PG_CELL_SIZE, self.pg_x + 0 * PG_CELL_SIZE))

    def change_move(self):
        self.move_cell_y = 0
        if self.selected_player == F_PLAYER:
            self.is_move_selected = False
            self.selected_player = S_PLAYER
        elif self.selected_player == S_PLAYER:
            self.is_move_selected = False
            self.selected_player = F_PLAYER

    def record_hot(self):
        print(self.move_cell_x + 1)
        print(self.move_cell_y + 1)
        self.field[self.move_cell_y + 1 ][self.move_cell_x] = self.selected_player

