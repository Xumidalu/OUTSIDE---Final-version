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

back = pygame.image.load(os.path.join(dir_img, "back.png")).convert_alpha()
back_pressed = pygame.image.load(os.path.join(dir_img, "blue_back.png")).convert_alpha()



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
        window.blit(home, (0, 0))
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
            return "iniciar_jogo"
        elif self.cred_button.check_click():
            return "ver_créditos"

        return "main_menu"


class IniciarJogo:
    def __init__(self):
        window.fill((210, 180, 140))
        self.back_button = Button(1500, 800, back, back_pressed)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.back_button.check_click():
            return "main_menu"

        return "iniciar_jogo"

    def update(self):
        window.fill((210, 180, 140))
        self.back_button.draw()


class Credits:
    def __init__(self):
        window.fill((47, 79, 79))
        self.back_button = Button(1500, 800, back, back_pressed)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.back_button.check_click():
            return "main_menu"

        return "ver_créditos"

    def update(self):
        window.fill((47, 79, 79))
        self.back_button.draw()


credits_screen = Credits()
jogo_iniciado = IniciarJogo()
main_menu = MainMenu()
tela_atual = "main_menu"

run = True
while run:
    if tela_atual == "main_menu":
        tela_atual = main_menu.handle_events()
        main_menu.update()
    elif tela_atual == "iniciar_jogo":
        tela_atual = jogo_iniciado.handle_events()
        jogo_iniciado.update()
    elif tela_atual == "ver_créditos":
        tela_atual = credits_screen.handle_events()
        credits_screen.update()

    pygame.display.update()

pygame.quit()
