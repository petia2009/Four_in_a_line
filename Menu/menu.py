import pygame


class Menu:
    def __init__(self, window, fps):
        self.window = window
        self.fps = fps

    fps = 60
    run_menu = True
    scene = 0

    sprite_folder = "sprites/menu/"
    bg = pygame.image.load(sprite_folder + "bg.jpg")
    play_button = pygame.image.load(sprite_folder + "play_button.png")
    play_button_focus = pygame.image.load(sprite_folder + "play_button_focus.png")
    exit_button = pygame.image.load(sprite_folder + "exit_button.png")
    exit_button_focus = pygame.image.load(sprite_folder + "exit_button_focus.png")

    button_select = 1
    play = False
    exit = False
    play_focus = False
    exit_focus = False

    def draw_button_play(self, focus):
        if focus:
            self.window.blit(self.play_button_focus, (100, 150))
        elif focus == False:
            self.window.blit(self.play_button, (100, 150))

    def draw_button_exit(self, focus):
        if focus:
            self.window.blit(self.exit_button_focus, (100, 300))
        elif focus == False:
            self.window.blit(self.exit_button, (100, 300))

    def draw(self):
        while self.run_menu:
            pygame.time.wait(self.fps)

            if self.button_select == 1:
                self.play = True
                self.exit = False
                self.play_focus = True
                self.exit_focus = False
            elif self.button_select == 2:
                self.play = False
                self.exit = True
                self.play_focus = False
                self.exit_focus = True
            elif self.button_select <= 1:
                self.button_select = 2
            elif self.button_select >= 2:
                self.button_select = 1
            else:
                print("qwertyuiopasdfghjklzxcvbnm")

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.run_all_app = False
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_DOWN:
                        self.button_select += 1
                    if ev.key == pygame.K_UP:
                        self.button_select -= 1
                    if ev.key == pygame.K_KP_ENTER or ev.key == pygame.K_RETURN:
                        if self.play:
                            self.scene = 1
                            self.run_menu = False
                        if self.exit:
                            self.scene = -1
                            self.run_menu = False

            self.window.blit(self.bg, (0, 0))
            self.draw_button_play(self.play_focus)
            self.draw_button_exit(self.exit_focus)

            pygame.display.update()

        return self.scene

