import pygame
import os

pygame.init()

x, y = 1600, 900

window = pygame.display.set_mode([x, y])
pygame.display.set_caption("PerfGens")

main_dir = os.path.dirname(__file__)
dir_img = os.path.join(main_dir, "cute_core")
home = pygame.image.load(os.path.join(dir_img, "fundo.png")).convert_alpha()
home = pygame.transform.scale(home, (1600, 900))

start_ = pygame.image.load(os.path.join(dir_img, "brown_start_button.png")).convert_alpha()
start_pressed = pygame.image.load(os.path.join(dir_img, "beige_start_button.png")).convert_alpha()

credits_ = pygame.image.load(os.path.join(dir_img, "brown_credits_button.png")).convert_alpha()
credits_pressed = pygame.image.load(os.path.join(dir_img, "beige_credits_button.png")).convert_alpha()

exit_ = pygame.image.load(os.path.join(dir_img, "brown_exit_button.png")).convert_alpha()
exit_pressed = pygame.image.load(os.path.join(dir_img, "beige_exit_button.png")).convert_alpha()

window.blit(home, (0, 0))


class Button:
    def __init__(self, x_axis, y_axis, image1, image2):
        self.image1 = image1
        self.image2 = image2
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.center = (x_axis, y_axis)
        self.pressed = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image2
        else:
            self.image = self.image1

        window.blit(self.image, (self.rect.x, self.rect.y))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True

        return False


class MainMenu:
    def __init__(self):
        window.blit(home, (0, 0))
        self.init_button = Button(380, 300, start_, start_pressed)
        self.cred_button = Button(380, 500, credits_, credits_pressed)
        self.exit_button = Button(380, 700, exit_, exit_pressed)

    def update(self):
        self.init_button.draw()
        self.cred_button.draw()
        self.exit_button.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.exit_button.check_click():
            pygame.quit()
            quit()

        if self.init_button.check_click():
            return "settings"  # Transição para a tela de configurações

        return "main_menu"  # Continua no menu principal


class SettingsScreen:
    def __init__(self):
        window.fill((210, 180, 140))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        window.fill((210, 180, 140))


settings_screen = SettingsScreen()
main_menu = MainMenu()
current_screen = "main_menu"

run = True
while run:
    if current_screen == "main_menu":
        current_screen = main_menu.handle_events()
        main_menu.update()
    elif current_screen == "settings":
        current_screen = settings_screen.handle_events()
        settings_screen.update()

    pygame.display.update()

pygame.quit()
