import pygame
from game.game import Game
from menu.menu import Menu


run_app = True
width_window = 750
height_window = 750
scene = 0
fps = 60
playground_width = 12
playground_height = 11

pygame.init()
win = pygame.display.set_mode((width_window, height_window))

while run_app:
    if scene == 0:
        menu = Menu(win, fps)
        scene = menu.draw()
    elif scene == 1:
        game = Game(win, fps, playground_width, playground_height)
        scene = game.start()
    elif scene == -1:
        run_app = False

