import pygame
import os

width_window = 750
height_window = 750
FPS = 60
run_app = True

pygame.init()
win = pygame.display.set_mode((width_window, height_window))

bg = pygame.image.load("../sprites/bg.jpg")
play_button = pygame.image.load("../sprites/play_button.png")
play_button_focus = pygame.image.load("../sprites/play_button_focus.png")
exit_button = pygame.image.load("../sprites/exit_button.png")
exit_button_focus = pygame.image.load("../sprites/exit_button_focus.png")

button_select = 1
play = False
exit = False
play_focus = True
exit_focus = False

def button_play(focus):
    if focus:
        win.blit(play_button_focus, (100, 150))
    elif focus == False:
        win.blit(play_button, (100, 150))

def button_exit(focus):
    if focus:
        win.blit(exit_button_focus, (100, 300))
    elif focus == False:
        win.blit(exit_button, (100, 300))

while run_app:
    pygame.time.wait(FPS)

    if button_select == 1:
        play = True
        exit = False
        play_focus = True
        exit_focus = False
    elif button_select == 2:
        play = False
        exit = True
        play_focus = False
        exit_focus = True
    elif button_select <= 1:
        button_select = 2
    elif button_select >= 2:
        button_select = 1
    else:
        print("АААААААААААААААААААА ОШИБКААААААААААААААААААААААААААААА")

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run_app = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_DOWN:
                button_select += 1
            if ev.key == pygame.K_UP:
                button_select -= 1
            if ev.key == pygame.K_KP_ENTER or ev.key == pygame.K_RETURN:
                if play:
                    os.system("python ../game/game.py")
                    run_app = False
                if exit:
                    run_app = False

    win.blit(bg, (0, 0))
    button_play(play_focus)
    button_exit(exit_focus)

    pygame.display.update()
pygame.quit()