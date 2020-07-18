import pygame

width_win = 750
height_win = 750
FPS = 60
run_app = True

pygame.init()
win = pygame.display.set_mode((width_win, height_win))

while run_app:
    pygame.time.wait(FPS)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run_app = False

    pygame.display.update()

pygame.quit()

