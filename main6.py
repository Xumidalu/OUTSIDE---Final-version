import pygame
import os

pygame.init()

x, y = 1600, 900

WHITE = (255, 255, 255)

window = pygame.display.set_mode([x, y])
pygame.display.set_caption("PerfGens")

main_dir = os.path.dirname(__file__)
dir_img = os.path.join(main_dir, "cute_core")
home = pygame.image.load(os.path.join(dir_img, "fundo_inicial.png")).convert_alpha()
home = pygame.transform.scale(home, (1600, 900))

start_ = pygame.image.load(os.path.join(dir_img, "iniciar.png")).convert_alpha()

start_pressed = pygame.image.load(os.path.join(dir_img, "iniciar_pressionado.png")).convert_alpha()


credits_ = pygame.image.load(os.path.join(dir_img, "créditos.png")).convert_alpha()

credits_pressed = pygame.image.load(os.path.join(dir_img, "créditos_pressionado.png")).convert_alpha()


exit_ = pygame.image.load(os.path.join(dir_img, "sair.png")).convert_alpha()

exit_pressed = pygame.image.load(os.path.join(dir_img, "sair_pressionado.png")).convert_alpha()


back = pygame.image.load(os.path.join(dir_img, "pink_back.png")).convert_alpha()
back_pressed = pygame.image.load(os.path.join(dir_img, "yellow_back.png")).convert_alpha()

continuar = pygame.image.load(os.path.join(dir_img, "continuar.png")).convert_alpha()
continuar_pressed = pygame.image.load(os.path.join(dir_img, "continuar_amarelo.png")).convert_alpha()

sala_das_camas = pygame.image.load(os.path.join(dir_img, "sala1_camas.png")).convert_alpha()
sala_das_camas = pygame.transform.scale(sala_das_camas, (1600, 900))

credits_background = pygame.image.load(os.path.join(dir_img, "fundo_dos_créditos.png")).convert_alpha()
credits_background = pygame.transform.scale(credits_background, (1600, 900))

idade_fundo = pygame.image.load(os.path.join(dir_img, "qual_a_sua_idade_fundo.png")).convert_alpha()
idade_fundo = pygame.transform.scale(idade_fundo, (1600, 900))

# BOTÕES DA TELA DE IDADE
var5_12 = pygame.image.load(os.path.join(dir_img, "5-12.png")).convert_alpha()
var5_12 = pygame.transform.scale(var5_12, (511, 144))
var5_12_press = pygame.image.load(os.path.join(dir_img, "5-12_press.png")).convert_alpha()
var5_12_press = pygame.transform.scale(var5_12_press, (511, 144))

var13_17 = pygame.image.load(os.path.join(dir_img, "13-17.png")).convert_alpha()
var13_17 = pygame.transform.scale(var13_17, (511, 144))
var13_17_press = pygame.image.load(os.path.join(dir_img, "13-17_press.png")).convert_alpha()
var13_17_press = pygame.transform.scale(var13_17_press, (511, 144))

var18_25 = pygame.image.load(os.path.join(dir_img, "18-25.png")).convert_alpha()
var18_25 = pygame.transform.scale(var18_25, (511, 144))
var18_25_press = pygame.image.load(os.path.join(dir_img, "18-25_press.png")).convert_alpha()
var18_25_press = pygame.transform.scale(var18_25_press, (511, 144))

var25 = pygame.image.load(os.path.join(dir_img, "25+.png")).convert_alpha()
var25 = pygame.transform.scale(var25, (511, 144))
var25_press = pygame.image.load(os.path.join(dir_img, "25+_press.png")).convert_alpha()
var25_press = pygame.transform.scale(var25_press, (511, 144))

black_square = pygame.image.load(os.path.join(dir_img, "balão_escuro.png")).convert_alpha()
avante = pygame.image.load(os.path.join(dir_img, "mini_continuar.png")).convert_alpha()
avante_hover = pygame.image.load(os.path.join(dir_img, "mini_continuar_hovering.png")).convert_alpha()

pontos = 0
fonte = pygame.font.SysFont("papyrus", 40, True)
contagem = f"pontos: {pontos}"
contagem_imprima = fonte.render(contagem, True, WHITE)

texto1 = "Onde eu estou...?"
texto2 = "isso é um hospital...? Como eu...?"
texto3 = "e onde estão as saídas..... certo, talvez eu esteja preso aqui..."
texto4 = "mas... talvez eu ache alguma pista?"


def recadinhos(var, color):
    return fonte.render(var, True, color)

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
        self.init_button = Button(790, 255, start_, start_pressed)
        self.cred_button = Button(790, 455, credits_, credits_pressed)
        self.exit_button = Button(790, 655, exit_, exit_pressed)

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
            return "camas"
        elif self.cred_button.check_click():
            return "ver_créditos"

        return "main_menu"


class IniciarJogo:
    def __init__(self):
        window.blit(idade_fundo, (0, 0))
        window.blit(contagem_imprima, (1300, 50))
        self.back_button = Button(1500, 800, back, back_pressed)
        self.age5_12 = Button(500, 450, var5_12, var5_12_press)
        self.age18_25 = Button(1100, 450, var18_25, var18_25_press)
        self.age13_17 = Button(500, 650, var13_17, var13_17_press)
        self.age25 = Button(1100, 650, var25, var25_press)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.back_button.check_click():
            return "camas"

        return "iniciar_jogo"

    def update(self):
        window.blit(idade_fundo, (0, 0))
        window.blit(contagem_imprima, (1300, 50))
        self.back_button.draw()
        self.age5_12.draw()
        self.age18_25.draw()
        self.age13_17.draw()
        self.age25.draw()


class SalaDasCamas:
    def __init__(self):
        window.blit(sala_das_camas, (0, 0))
        window.blit(black_square, (100, 100))
        self.avante = Button(1350, 285, avante, avante_hover)
        self.recado = recadinhos(texto1, WHITE)
        self.texto_atual = 1
        self.time_within_actions = 1000
        self.last_click = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        tempo_atual = pygame.time.get_ticks()

        if self.avante.check_click():
            if tempo_atual - self.last_click >= self.time_within_actions:
                self.last_click = tempo_atual
                if self.texto_atual == 1:
                    self.recado = recadinhos(texto2, WHITE)
                    self.texto_atual = 2
                elif self.texto_atual == 2:
                    self.recado = recadinhos(texto3, WHITE)
                    self.texto_atual = 3
                elif self.texto_atual == 3:
                    self.recado = recadinhos(texto4, WHITE)
                    self.texto_atual = 4

        return "camas"

    def update(self):
        window.blit(sala_das_camas, (0, 0))
        window.blit(black_square, (100, 100))
        self.avante.draw()
        window.blit(self.recado, (250, 150))


class Credits:
    def __init__(self):
        window.blit(credits_background, (0, 0))
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
        window.blit(credits_background, (0, 0))
        self.back_button.draw()


beds_screen = SalaDasCamas()
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
    elif tela_atual == "camas":
        tela_atual = beds_screen.handle_events()
        beds_screen.update()

    pygame.display.update()

pygame.quit()
