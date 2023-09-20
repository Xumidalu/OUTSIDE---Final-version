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

black_square = pygame.image.load(os.path.join(dir_img, "balão_escuro.png")).convert_alpha()
avante = pygame.image.load(os.path.join(dir_img, "mini_continuar.png")).convert_alpha()
avante_hover = pygame.image.load(os.path.join(dir_img, "mini_continuar_hovering.png")).convert_alpha()
cartas = pygame.image.load(os.path.join(dir_img, "carta.jpg")).convert_alpha()
carta_funciona = pygame.transform.scale(cartas, (1600, 900))
# SETAS CINZA
seta = pygame.image.load(os.path.join(dir_img, "seta.png")).convert_alpha()
seta = pygame.transform.scale(seta, (50, 50))
seta_pressed = pygame.image.load(os.path.join(dir_img, "seta_pressed.png")).convert_alpha()
seta_pressed = pygame.transform.scale(seta_pressed, (50, 50))
seta_esquerda = pygame.image.load(os.path.join(dir_img, "seta_esquerda.png")).convert_alpha()
seta_esquerda = pygame.transform.scale(seta_esquerda, (100, 100))
seta_esquerda_pressed = pygame.image.load(os.path.join(dir_img, "seta_esquerda_pressed.png")).convert_alpha()
seta_esquerda_pressed = pygame.transform.scale(seta_esquerda_pressed, (100, 100))

seta_direita = pygame.image.load(os.path.join(dir_img, "seta cinza direita.png")).convert_alpha()
seta_direita = pygame.transform.scale(seta_direita, (100, 100))
seta_direita_pressed = pygame.image.load(os.path.join(dir_img, "seta cinza direita pressionada.png")).convert_alpha()
seta_direita_pressed = pygame.transform.scale(seta_direita_pressed, (100, 100))
#
salaa2p1 = pygame.image.load(os.path.join(dir_img, "sala2pt1.png")).convert_alpha()
sala2p1 = pygame.transform.scale(salaa2p1, (1600, 900))
sala2pt2 = pygame.image.load(os.path.join(dir_img, "Sala2pt2.png")).convert_alpha()
sala2pt2 = pygame.transform.scale(sala2pt2, (1600, 900))
menu_middleb = pygame.image.load(os.path.join(dir_img, "FundinhoMiddleMenu.png")).convert_alpha()
menu_middle = pygame.transform.scale(menu_middleb, (1600, 900))
retomar = pygame.image.load(os.path.join(dir_img, "Menu_middle1.png")).convert_alpha()
retomar_pressed = pygame.image.load(os.path.join(dir_img, "Menu_middle_pressed1.png")).convert_alpha()
inventario = pygame.image.load(os.path.join(dir_img, "Menu_middle2.png")).convert_alpha()
inventario_pressed = pygame.image.load(os.path.join(dir_img, "Menu_middle_pressed2.png")).convert_alpha()
Menu_princ_volt = pygame.image.load(os.path.join(dir_img, "Menu_middle3.png")).convert_alpha()
Menu_princ_volt_pressed = pygame.image.load(os.path.join(dir_img, "Menu_middle_pressed3.png")).convert_alpha()
tela1_puzzle1 = pygame.image.load(os.path.join(dir_img, "puzzle1_recado1.png")).convert_alpha()
tela1_puzzle1 = pygame.transform.scale(tela1_puzzle1, (1600, 900))
inventory_screen = pygame.image.load(os.path.join(dir_img, "inventário.png")).convert_alpha()
inventory_screen = pygame.transform.scale(inventory_screen, (1600, 900))
loucuras = pygame.image.load(os.path.join(dir_img, "importLoUcUrAs.png")).convert_alpha()
loucurasBIG = pygame.transform.scale(loucuras, (300, 300))
pontos = 0
fonte = pygame.font.SysFont("papyrus", 40, True)
contagem = f"pontos: {pontos}"
contagem_imprima = fonte.render(contagem, True, WHITE)
texto1 = "Onde eu estou...?"
texto2 = "isso é um hospital...? Como eu...?"
texto3 = "e onde estão as saídas..... certo, talvez eu esteja preso aqui..."
texto4 = "mas... talvez eu ache alguma pista?"
texto5 = "Não tenho a chave"
texto6 = "Ei... eu não sou maluco de por o braço aí...."
texto7 = "Ah, certo, eu sou"
texto8 = "Import   LOUCUUURAS   guardado  no  inventário"
texto9 = "nada aqui"
history = "sem telas recentes"
seta_preta_esquerda = pygame.image.load(os.path.join(dir_img, "seta esquerda do inventário.png")).convert_alpha()
seta_preta_esquerda_pressionada = pygame.image.load(
    os.path.join(dir_img, "seta do inventário pressionada e esquerda.png")).convert_alpha()
seta_preta_direita = pygame.image.load(os.path.join(dir_img, "seta direita do inventário.png")).convert_alpha()
seta_preta_direita_pressionada = pygame.image.load(
    os.path.join(dir_img, "seta do inventário pressionada e direita.png")).convert_alpha()
buraco = pygame.image.load(os.path.join(dir_img, "buraco.png")).convert_alpha()
hidden_button = pygame.image.load(os.path.join(dir_img, "hidden_button.png")).convert_alpha()
CINZA = (80, 80, 80)

inventory_lot_1 = "Vago"

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
        self.showing = True

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image = self.image2
        else:
            self.image = self.image1

        if self.showing:
            window.blit(self.image, (self.rect.x, self.rect.y))

    def bye_bye(self):
        self.showing = False

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
        self.varControle = 0
        self.more = True

    def update(self):
        window.blit(home, (0, 0))
        if self.more:
            self.varControle += 1
        self.init_button.draw()
        self.cred_button.draw()
        self.exit_button.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.init_button.check_click():
            return "camas"

        if self.exit_button.check_click():
            pygame.quit()
            quit()

        elif self.cred_button.check_click():
            return "ver_créditos"

        return "main_menu"


class IniciarJogo:
    def __init__(self):
        pass

    def handle_events(self):
        pass


class SalaDasCamas:
    def __init__(self):
        window.blit(sala_das_camas, (0, 0))
        window.blit(black_square, (100, 100))
        self.avante = Button(1350, 285, avante, avante_hover)
        self.ver_a_carta = Button(1200, 560, seta, seta_pressed)
        self.ir_pra_sala_esquerda = Button(100, 560, seta_esquerda, seta_esquerda_pressed)
        self.buraco = Button(728, 385, buraco, buraco)
        self.hidden_button = Button(730, 380, hidden_button, hidden_button)
        self.recado = recadinhos(texto1, WHITE)
        self.recado2 = recadinhos(texto6, WHITE)
        self.texto_atual = 1
        self.time_within_actions = 1000
        self.last_click = 0
        self.contagem_do_buraco = 0
        self.contagem_do_black_square_pt2 = 0
        self.showing = True
        self.completed_action = False
        self.max_time = 400
        self.varControle = 0

    def handle_events(self):
        global history
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_sala_das_camas"
                    return "menu_middle"

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
                elif self.texto_atual == 4:
                    self.recado = recadinhos(texto4, WHITE)
                    self.texto_atual = 5

        if self.ver_a_carta.check_click():
            return "carta"
        if self.ir_pra_sala_esquerda.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "sala2p1"
                print(e)

        # Só funciona com print
        # Mudar de lugar

        if self.hidden_button.check_click() and self.texto_atual > 4:
            self.contagem_do_buraco += 1
        if self.contagem_do_buraco > 110:
            self.buraco.draw()
        else:
            self.hidden_button.draw()
        if self.buraco.check_click() and self.contagem_do_buraco > 110:
            window.blit(black_square, (100, 550))
            window.blit(self.recado2, (200, 645))

        return "camas"

    def update(self):
        window.blit(sala_das_camas, (0, 0))
        if self.texto_atual <= 4:
            window.blit(black_square, (100, 100))
            window.blit(self.recado, (200, 200))
            self.avante.draw()
        elif self.texto_atual > 4:
            self.ver_a_carta.draw()
            self.ir_pra_sala_esquerda.draw()

        if self.hidden_button.check_click() and self.texto_atual > 4:
            self.hidden_button.bye_bye()
            self.contagem_do_buraco += 1
        if self.contagem_do_buraco > 110:
            self.buraco.draw()
        else:
            self.hidden_button.draw()
        if self.buraco.check_click():
            self.contagem_do_black_square_pt2 += 1

        if self.contagem_do_buraco > 110 and self.contagem_do_black_square_pt2 > 2:
            window.blit(black_square, (100, 550))
            window.blit(self.recado2, (200, 645))
            self.varControle += 0.5
        if self.varControle > self.max_time:
            self.contagem_do_black_square_pt2 = 0
            self.varControle = 0


class Carta:
    def __init__(self):
        window.blit(carta_funciona, (0, 0))
        self.voltar = Button(100, 500, seta_esquerda, seta_esquerda_pressed)

    def handle_events(self):
        global history
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_carta"
                    return "menu_middle"

        if self.voltar.check_click():
            return "camas"

        return "carta"

    def update(self):
        window.blit(carta_funciona, (0, 0))
        self.voltar.draw()


class PuzzleSalaUmParaDois:
    def __init__(self):
        window.blit(tela1_puzzle1, (0, 0))


class Sala_das_Garrafa_pt_2:
    def __init__(self):
        window.blit(sala2pt2, (0, 0))
        self.voltar_pra_pt1 = Button(1500, 560, seta_direita, seta_direita_pressed)

    def handle_events(self):
        global history
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_sala_das_garrafonas2"
                    return "menu_middle"

        if self.voltar_pra_pt1.check_click():
            return "camas"

        return "garrafa_pt_2"

    def update(self):
        window.blit(sala2pt2, (0, 0))
        self.voltar_pra_pt1.draw()



class SaladasGarrafonas:
    def __init__(self):
        window.blit(sala2p1, (0, 0))
        self.escada = Button(500, 500, seta, seta_pressed)
        self.avante = Button(1350, 285, avante, avante_hover)
        self.loucuras = Button(1100, 336, loucuras, loucuras)
        self.ir_pra_sala_esquerda = Button(100, 560, seta_esquerda, seta_esquerda_pressed)
        self.caixa = black_square
        self.texto = texto5
        self.texto2 = texto8
        self.recadin = recadinhos(self.texto, WHITE)
        self.recadin2 = recadinhos(self.texto2, WHITE)
        self.voltar_pra_sala_das_camas = Button(1500, 560, seta_direita, seta_direita_pressed)
        window.blit(self.caixa, (100, 100))
        window.blit(self.recadin, (200, 200))
        self.msg = False
        self.contagem_do_black_square_pt2 = 0
        self.varControle = 0
        self.max_time = 400
        self.show_potion = True

    def handle_events(self):
        global history
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_sala_das_garrafonas"
                    return "menu_middle"

        if self.voltar_pra_sala_das_camas.check_click():
            return "camas"
        if self.ir_pra_sala_esquerda.check_click():
            return "garrafa_pt_2"

        if self.escada.check_click():
            self.msg = True
        if self.avante.check_click():
            self.msg = False

        return "sala2p1"


    def update(self):
        global inventory_lot_1
        window.blit(sala2p1, (0, 0))
        self.voltar_pra_sala_das_camas.draw()
        self.ir_pra_sala_esquerda.draw()

        if self.show_potion:
            self.loucuras.draw()

        if self.loucuras.check_click():
            self.contagem_do_black_square_pt2 += 1
            self.show_potion = False
            inventory_lot_1 = "Loucuras"

        if self.contagem_do_black_square_pt2 > 2:
            window.blit(black_square, (100, 550))
            window.blit(self.recadin2, (200, 645))
            self.varControle += 0.5
        if self.varControle > self.max_time:
            self.contagem_do_black_square_pt2 = 0
            self.varControle = 0

        if self.msg == False:
            self.escada.draw()
        if self.msg == True:
            window.blit(self.caixa, (100, 100))
            window.blit(self.recadin, (200, 200))
            self.avante.draw()
        if self.voltar_pra_sala_das_camas.check_click():
            return "camas"
        else:
            return "sala2p1"


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


class Inventory:
    def __init__(self):
        global inventory_lot_1
        window.blit(inventory_screen, (0, 0))
        self.close_inventory = Button(100, 800, seta_esquerda, seta_esquerda_pressed)
        self.seta_esquerda = Button(250, 500, seta_preta_esquerda, seta_preta_esquerda_pressionada)
        self.seta_direita = Button(1350, 500, seta_preta_direita, seta_preta_direita_pressionada)
        self.loucuras = Button(800, 450, loucurasBIG, loucurasBIG)
        self.texto = texto9
        self.recado = recadinhos(texto9, CINZA)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if self.close_inventory.check_click():
            return "menu_middle"

        return "inventory"

    def update(self):
        global inventory_lot_1
        window.blit(inventory_screen, (0, 0))
        self.close_inventory.draw()
        self.seta_esquerda.draw()
        self.seta_direita.draw()
        if inventory_lot_1 == "Vago":
            window.blit(self.recado, (720, 420))
        elif inventory_lot_1 == "Loucuras":
            self.loucuras.draw()
        print(inventory_lot_1)



class MiddleMenu:
    def __init__(self):
        global history
        window.blit(menu_middle, (0, 0))
        self.retomar = Button(790, 255, retomar, retomar_pressed)
        self.invent = Button(790, 455, inventario, inventario_pressed)
        self.menuinic = Button(790, 655, Menu_princ_volt, Menu_princ_volt_pressed)
        self.varControle = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if self.retomar.check_click():
            print(history)
            if history == "registrando_sala_das_camas":
                return "camas"
            elif history == "registrando_sala_das_garrafonas":
                return "sala2p1"
            elif history == "registrando_carta":
                return "carta"
            elif history == "registrando_sala_das_garrafonas2":
                return "garrafa_pt_2"
        if self.invent.check_click():
            return "inventory"
        if self.menuinic.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "main_menu"

        return "menu_middle"

    def update(self):
        window.blit(menu_middle, (0, 0))
        self.retomar.draw()
        self.invent.draw()
        self.menuinic.draw()

inventory = Inventory()
beds_screen = SalaDasCamas()
credits_screen = Credits()
jogo_iniciado = IniciarJogo()
main_menu = MainMenu()
carta_screen = Carta()
sala2p1_screen = SaladasGarrafonas()
sala2pt2_screen = Sala_das_Garrafa_pt_2()
menuu_middle_screen = MiddleMenu()
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
    elif tela_atual == "carta":
        tela_atual = carta_screen.handle_events()
        carta_screen.update()
    elif tela_atual == "sala2p1":
        tela_atual = sala2p1_screen.handle_events()
        sala2p1_screen.update()
    elif tela_atual == "menu_middle":
        tela_atual = menuu_middle_screen.handle_events()
        menuu_middle_screen.update()
    elif tela_atual == "inventory":
        tela_atual = inventory.handle_events()
        inventory.update()
    elif tela_atual == "garrafa_pt_2":
        tela_atual = sala2pt2_screen.handle_events()
        sala2pt2_screen.update()

    pygame.display.update()

pygame.quit()
