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

salaTV = pygame.image.load(os.path.join(dir_img, "sala_da_tv.png")).convert_alpha()
salaTV = pygame.transform.scale(salaTV, (1600, 900))

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

estante = pygame.image.load("Estante/Estanteampli.png")
estanteR = pygame.transform.scale(estante, (1600, 900))
caixa = pygame.image.load("Estante/caixa.png")
caixaR = pygame.transform.scale(caixa,(200, 200))
caixapressed = pygame.image.load("Estante/caixapressed.png")
caixapressedR = pygame.transform.scale(caixapressed, (200, 200))
pastaroxa = pygame.image.load("Estante/pastaroxa.png")
pastaroxaR = pygame.transform.scale(pastaroxa, (100, 215))
pastaroxaampli = pygame.image.load("Estante/pastaroxaampli.png")
pastaroxapressed = pygame.image.load("Estante/pastaroxapressed.png")
pastaroxapressedR = pygame.transform.scale(pastaroxapressed, (100, 215))
pastaverde = pygame.image.load("Estante/pastaverde.png")
pastaverdeR = pygame.transform.scale(pastaverde, (100, 215))
pastaverdeampli = pygame.image.load("Estante/pastaverdeampli.png")
pastaverdepressed = pygame.image.load("Estante/pastaverdepressed.png")
pastaverdepressedR = pygame.transform.scale(pastaverdepressed, (100, 215))

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
texto10 = "Graveto adicionado ao seu inventário"
texto11 = "Chip adicionado ao seu inventário"
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

sala2pt2 = pygame.image.load(os.path.join(dir_img, "Sala2pt2.png")).convert_alpha()
sala2pt2 = pygame.transform.scale(sala2pt2, (1600, 900))

inventory_lot_1 = "Vago"
inventory_lot_2 = "Vago"
inventory_lot_3 = "Vago"

# TEMPERATURAS

grau1 = pygame.image.load(os.path.join(dir_img, "grau1.png")).convert_alpha()
grau1 = pygame.transform.scale(grau1, (124.4, 49.8))

grau2 = pygame.image.load(os.path.join(dir_img, "grau2.png")).convert_alpha()
grau2 = pygame.transform.scale(grau2, (124.4, 49.8))

grau3 = pygame.image.load(os.path.join(dir_img, "grau3.png")).convert_alpha()
grau3 = pygame.transform.scale(grau3, (124.4, 49.8))

grau4 = pygame.image.load(os.path.join(dir_img, "grau4.png")).convert_alpha()
grau4 = pygame.transform.scale(grau4, (124.4, 49.8))

# 26/09/2023

fatBox_open = pygame.image.load(os.path.join(dir_img, "pão aberto.png")).convert_alpha()
fatBox_open = pygame.transform.scale(fatBox_open, (450, 260))

fatBox_closed = pygame.image.load(os.path.join(dir_img, "pão fechado.png")).convert_alpha()
fatBox_closed = pygame.transform.scale(fatBox_closed, (450, 260))

chip = pygame.image.load(os.path.join(dir_img, "chip.png")).convert_alpha()
chip = pygame.transform.scale(chip, (58, 40))

chipBIG = pygame.transform.scale(chip, (174, 120))


pau = pygame.image.load(os.path.join(dir_img, "pau.png")).convert_alpha()
pau = pygame.transform.scale(pau, (130, 7))

pauBIG = pygame.transform.scale(pau, (390, 21))



telaquizza = pygame.image.load("quiz/Telaquiz.png")
telaquiz = pygame.transform.scale(telaquizza, (1600, 900))

inic = pygame.image.load("quiz/Iniciar.png")

vaiii = pygame.image.load("quiz/vai.png")

Q1 = pygame.image.load("quiz/Q1.png")

K = pygame.image.load("quiz/K.png")

Na = pygame.image.load("quiz/Na.png")

Cl =pygame.image.load("quiz/Cl.png")

Q2 = pygame.image.load("quiz/Q2.png")

Hcl = pygame.image.load("quiz/HCl.png")

SO2 = pygame.image.load("quiz/SO2.png")

C2H2 = pygame.image.load("quiz/C2H2.png")

Q3 = pygame.image.load("quiz/Q3.png")

C2H5OH = pygame.image.load("quiz/C2H5OH.png")

C6H8O7 = pygame.image.load("quiz/C6H8O7.png")

MgCl2 = pygame.image.load("quiz/MgCl2.png")

MDC = pygame.image.load("quiz/MDC.png")


tv_on = pygame.image.load(os.path.join(dir_img, "tv_ligada.png")).convert_alpha()
tv_on = pygame.transform.scale(tv_on, (470, 300))

tv_off = pygame.image.load(os.path.join(dir_img, "tv_apagada.png")).convert_alpha()
tv_off = pygame.transform.scale(tv_off, (470, 300))

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
        self.ir_pra_sala_esquerda = Button(100, 560, seta_esquerda, seta_esquerda_pressed)


class SalaDaTV:
    def __init__(self):
        window.blit(salaTV, (0, 0))
        self.ir_pra_sala_esquerda = Button(100, 560, seta_esquerda, seta_esquerda_pressed)
        self.voltar_pra_garrafona1 = Button(1500, 560, seta_direita, seta_direita_pressed)
        self.tv_off = Button(565, 210, tv_off, tv_off)
        self.tv_on = Button(565, 210, tv_on, tv_on)
        self.varControle = 0
        self.batata = True

    def handle_events(self):
        global history
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_sala_da_tv"
                    return "menu_middle"

            if self.batata:
                self.tv_off.draw()
            if not self.batata:
                self.tv_on.draw()

            if self.tv_off.check_click():
                self.batata = False
                for e in range(1, 100000):
                    if e == 99999:
                        return "quiz"
                    print(e)

        if self.ir_pra_sala_esquerda.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "garrafa_pt_2"
                print(e)
        elif self.voltar_pra_garrafona1.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "sala2p1"
                print(e)

        else:
            return "salaTV"

    def update(self):
        global inventory_lot_1
        window.blit(salaTV, (0, 0))
        if self.batata:
            self.tv_off.draw()
        if not self.batata:
            self.tv_on.draw()

        self.ir_pra_sala_esquerda.draw()
        self.voltar_pra_garrafona1.draw()
        if self.ir_pra_sala_esquerda.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "garrafa_pt_2"
                print(e)

        if self.tv_off.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "quiz"
                print(e)
            self.batata = False

        return "salaTV"


class Sala_das_Garrafa_pt_2:
    def __init__(self):
        window.blit(sala2pt2, (0, 0))
        self.voltar_pra_tv = Button(1500, 560, seta_direita, seta_direita_pressed)

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

        if self.voltar_pra_tv.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "salaTV"
                print(e)

        return "garrafa_pt_2"

    def update(self):
        window.blit(sala2pt2, (0, 0))
        self.voltar_pra_tv.draw()
        return "garrafa_pt_2"


class SaladasGarrafonas:
    def __init__(self):
        window.blit(sala2p1, (0, 0))
        self.escada = Button(680, 300, seta, seta_pressed)
        self.avante = Button(1350, 285, avante, avante_hover)
        self.loucuras = Button(1100, 336, loucuras, loucuras)
        self.ir_pra_sala_esquerda = Button(100, 560, seta_esquerda, seta_esquerda_pressed)
        self.caixa = black_square
        self.texto = texto5
        self.texto2 = texto8
        self.texto10 = texto10
        self.texto11 = texto11
        self.recadin = recadinhos(self.texto, WHITE)
        self.recadin2 = recadinhos(self.texto2, WHITE)
        self.recadin3 = recadinhos(self.texto10, WHITE)
        self.recadin4 = recadinhos(self.texto11, WHITE)
        self.voltar_pra_sala_das_camas = Button(1500, 560, seta_direita, seta_direita_pressed)
        window.blit(self.caixa, (100, 100))
        window.blit(self.recadin, (200, 200))
        self.msg = False
        self.contagem_do_black_square_pt2 = 0
        self.contagem_do_black_square_pt3 = 0
        self.contagem_do_black_square_pt4 = 0

        self.varControle = 0
        self.varControle2 = 0
        self.varControle3 = 0
        self.max_time = 400
        self.show_potion = True
        self.comoda_aberta = Button(1370, 495, fatBox_open, fatBox_open)
        self.comoda_fechada = Button(1370, 495, fatBox_closed, fatBox_closed)
        self.troca_comoda = False
        self.pau = Button(1350, 450, pau, pau)
        self.chip = Button(1250, 500, chip, chip)
        self.chip_e_pau_on = False
        self.pau_on = False
        self.chip_on = False


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

        if self.comoda_aberta.check_click():
            self.troca_comoda = True

        if not self.troca_comoda:
            self.comoda_fechada.draw()
        elif self.troca_comoda:
            self.comoda_aberta.draw()
            self.chip.draw()
            self.chip_on = True
            self.pau_on = True

        if self.pau_on:
            self.pau.draw()
        if self.chip_on:
            self.chip.draw()

        if self.troca_comoda:
            if self.pau.check_click():
                self.pau_on = False
                self.pau.bye_bye()
                self.contagem_do_black_square_pt3 += 1
            if self.chip.check_click():
                self.chip_on = False
                self.chip.bye_bye()
                self.contagem_do_black_square_pt4 += 1


        if self.escada.check_click():
            self.msg = True
        if self.avante.check_click():
            self.msg = False

        if self.ir_pra_sala_esquerda.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "salaTV"
                print(e)

        if self.voltar_pra_sala_das_camas.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "camas"
                print(e)

        return "sala2p1"


    def update(self):
        global inventory_lot_1, inventory_lot_2, inventory_lot_3
        window.blit(sala2p1, (0, 0))

        if self.comoda_aberta.check_click():
            self.troca_comoda = True

        if not self.troca_comoda:
            self.comoda_fechada.draw()
        elif self.troca_comoda:
            self.comoda_aberta.draw()
            self.chip.draw()
            self.chip_on = True
            self.pau_on = True

        if self.pau_on:
            self.pau.draw()
        if self.chip_on:
            self.chip.draw()

        if self.troca_comoda:
            if self.pau.check_click():
                self.pau_on = False
                self.contagem_do_black_square_pt3 += 1
                inventory_lot_2 = "Pau"
            if self.chip.check_click():
                self.chip_on = False
                self.contagem_do_black_square_pt4 += 1
                inventory_lot_3 = "Chip"

        self.voltar_pra_sala_das_camas.draw()

        if self.show_potion:
            self.loucuras.draw()

        if self.loucuras.check_click():
            self.contagem_do_black_square_pt2 += 1
            self.show_potion = False
            inventory_lot_1 = "Loucuras"

# BLACK_SQUARE DA POÇÃO
        if self.contagem_do_black_square_pt2 > 2:
            window.blit(black_square, (100, 550))
            window.blit(self.recadin2, (200, 645))
            self.varControle += 0.5
        if self.varControle > self.max_time:
            self.contagem_do_black_square_pt2 = 0
            self.varControle = 0

# BLACK_SQUARE DO PAU
        if self.contagem_do_black_square_pt3 > 2:
            window.blit(black_square, (100, 550))
            window.blit(self.recadin3, (200, 645))
            self.varControle2 += 0.5
        if self.varControle2 > self.max_time:
            self.contagem_do_black_square_pt3 = 0
            self.varControle2 = 0

# BLACK_SQUARE DO CHIP
        if self.contagem_do_black_square_pt4 > 2:
            window.blit(black_square, (100, 550))
            window.blit(self.recadin4, (200, 645))
            self.varControle3 += 0.5
        if self.varControle3 > self.max_time:
            self.contagem_do_black_square_pt4 = 0
            self.varControle3 = 0

        if self.msg == False:
            self.escada.draw()
            self.ir_pra_sala_esquerda.draw()

        if self.msg == True:
            window.blit(self.caixa, (100, 100))
            window.blit(self.recadin, (200, 200))
            self.avante.draw()
        if self.voltar_pra_sala_das_camas.check_click():
            return "camas"
        else:
            return "sala2p1"


class Estante:
    def __init__(self):
        window.blit(estanteR, (0, 0))
        window.blit(pastaroxaampli, (500, 100))
        window.blit(pastaverdeampli, (500, 100))
        window.blit(caixa, (500, 100))
        self.caixa = Button(840, 750, caixaR, caixapressedR)
        self.pastaroxa = Button(680, 225, pastaroxaR, pastaroxapressedR)
        self.pastaverde = Button(870, 225, pastaverdeR, pastaverdepressedR)
        self.volta = Button(300, 300, seta_esquerda, seta_esquerda_pressed)
        self.Ca = False
        self.Pr = False
        self.Pv = False
        self.princ = True

    def variables(self, name):
        self.Ca = False
        self.Pr = False
        self.Pv = False
        self.princ = True
        if name == True:
            self.Ca = False
            self.Pr = False
            self.Pv = False
            self.princ = False
        elif name == False:
            pass


    def handle_events(self):
        global history
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_estante"
                    return "menu_middle"

        if self.caixa.check_click():
            self.Ca = True
            self.princ = False
        if self.pastaroxa.check_click():
            self.Pr = True
            self.princ = False
        if self.pastaverde.check_click():
            self.Pv = True
            self.princ = False
        if self.volta.check_click():
            self.princ = True
            if self.Ca == True:
                self.Ca = False
            elif self.Pr == True:
                self.Pr = False
            elif self.Pv == True:
                self.Pv = False

        return "estante"

    def update(self):
        window.blit(estanteR, (0, 0))
        self.caixa.draw
        if self.princ == True:
            self.pastaroxa.draw()
            self.pastaverde.draw()
            self.caixa.draw()
        if self.Ca == True:
            window.blit(caixa, (500, 100))
            self.volta.draw()
        elif self.Pr == True:
            window.blit(pastaroxaampli, (500, 100))
            self.volta.draw()
        elif self.Pv == True:
            window.blit(pastaverdeampli, (500, 100))
            self.volta.draw()
        else:
            pass


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
        self.pau = Button(800, 450, pauBIG, pauBIG)
        self.chip = Button(800, 450, chipBIG, chipBIG)
        self.page1 = True
        self.page2 = False
        self.page3 = False
        self.varControl1 = 0
        self.varControl2 = 0
        self.varControl3 = 0
        self.varControl4 = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if self.close_inventory.check_click():
            return "menu_middle"

        return "inventory"

    def update(self):
        global inventory_lot_1, inventory_lot_2, inventory_lot_3
        window.blit(inventory_screen, (0, 0))
        self.close_inventory.draw()
        self.seta_esquerda.draw()
        self.seta_direita.draw()

        if self.seta_direita.check_click() and self.page1:
            self.varControl1 += 0.5
            if self.varControl1 > 8:
                self.page1 = False
                self.page2 = True
                self.varControl1 = 0

        if self.seta_direita.check_click() and self.page2:
            self.varControl2 += 0.5
            if self.varControl2 > 8:
                self.page2 = False
                self.page3 = True
                self.varControl2 = 0

        if self.seta_esquerda.check_click() and self.page3:
            self.varControl3 += 0.5
            if self.varControl3 > 8:
                self.page3 = False
                self.page2 = True

        if self.seta_esquerda.check_click() and self.page2:
            self.varControl4 += 0.5
            if self.varControl4 > 8:
                self.page2 = False
                self.page1 = True

        # Pag 1
        if self.page1:
            if inventory_lot_1 == "Vago":
                window.blit(self.recado, (720, 420))
            elif inventory_lot_1 == "Loucuras":
                self.loucuras.draw()

        # Pag 2
        if self.page2:
            if inventory_lot_2 == "Vago":
                window.blit(self.recado, (720, 420))
            elif inventory_lot_2 == "Pau":
                self.pau.draw()

        # Pag 3
        if self.page3:
            if inventory_lot_3 == "Vago":
                window.blit(self.recado, (720, 420))
            elif inventory_lot_3 == "Chip":
                self.chip.draw()


class Quizzz():
    def __init__(self):
        window.blit(telaquiz, (0, 0))
        window.blit(Q1, (0, 0))
        window.blit(Q2, (0, 0))
        window.blit(Q3, (0, 0))
        window.blit(MDC, (0, 0))
        self.Inic = Button(800, 500, inic, inic)
        self.vaai = Button(800, 600, vaiii, vaiii)
        self.K = Button(300, 200, K, K)
        self.Na = Button(1200, 500, Na, Na)
        self.Cl = Button(700, 700, Cl, Cl)
        self.Hcl = Button(1000, 500, Hcl, Hcl)
        self.SO2 = Button(600, 700, SO2, SO2)
        self.C2H2 = Button(300, 200, C2H2, C2H2)
        self.C2H5OH = Button(300, 400, C2H5OH, C2H5OH)
        self.C6H8O7 = Button(500, 800, C6H8O7, C6H8O7)
        self.MgCl2 = Button(1300, 100, MgCl2, MgCl2)
        self.inicio = True
        self.comc = False
        self.Q1 = False
        self.Q2 = False
        self.Q3 = False
        self.resp = False


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if self.Inic.check_click() and self.inicio == True:
            self.comc = True
            self.inicio = False
            self.Q1 = True
        if self.vaai.check_click() and self.comc == True:
            self.comc = False
        if self.comc == False:
            if self.Q1 == True:
                if self.Cl.check_click():
                    self.Q1 = False
                    self.Q2 = True
                    self.comc =True
                elif self.K.check_click() or self.Na.check_click():
                    return "salaTV"
            elif self.Q2 == True:
                if self.Hcl.check_click():
                    return "salaTV"
                elif self.SO2.check_click():
                    return "salaTV"
                elif self.C2H2.check_click():
                    self.Q2 = False
                    self.comc = True
                    self.Q3 = True
            elif self.Q3 == True:
                if self.MgCl2.check_click():
                    self.Q3 = False
                    self.resp = True
                elif self.C2H5OH.check_click() or self.C6H8O7.check_click():
                    return "salaTV"

        return "quiz"

    def update(self):
        window.blit(telaquiz, (0,0))
        if self.inicio == True:
            self.Inic.draw()
        elif self.comc == True:
            self.vaai.draw()
            if self.Q1 == True:
                window.blit(Q1, (0, 0))
            elif self.Q2 == True:
                window.blit(Q2, (0, 0))
            elif self.Q3 == True:
                window.blit(Q3, (0, 0))
        elif self.comc == False:
            if self.Q1 == True:
                self.K.draw()
                self.Na.draw()
                self.Cl.draw()
            elif self.Q2 == True:
                self.C2H2.draw()
                self.SO2.draw()
                self.Hcl.draw()
            elif self.Q3 == True:
                self.MgCl2.draw()
                self.C6H8O7.draw()
                self.C2H5OH.draw()

        if self.resp == True:
            window.blit(MDC, (0, 0))



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
            elif history == "registrando_estante":
                return "estante"
            elif history == "registrando_sala_da_tv":
                return "salaTV"
            elif history == "registrando_sala_das_garrafonas2":
                return "garrafa_pt_2"

        if self.invent.check_click():
            return "inventory"
        if self.menuinic.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "main_menu"
                print(e)

        return "menu_middle"

    def update(self):
        window.blit(menu_middle, (0, 0))
        self.retomar.draw()
        self.invent.draw()
        self.menuinic.draw()


quizuu = Quizzz()
sala2pt2_screen = Sala_das_Garrafa_pt_2()
sala_da_TV = SalaDaTV()
inventory = Inventory()
beds_screen = SalaDasCamas()
credits_screen = Credits()
jogo_iniciado = IniciarJogo()
main_menu = MainMenu()
carta_screen = Carta()
sala2p1_screen = SaladasGarrafonas()
menuu_middle_screen = MiddleMenu()
estante_screen = Estante()
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
    elif tela_atual == "estante":
        tela_atual = estante_screen.handle_events()
        estante_screen.update()
    elif tela_atual == "salaTV":
        tela_atual = sala_da_TV.handle_events()
        sala_da_TV.update()
    elif tela_atual == "garrafa_pt_2":
        tela_atual = sala2pt2_screen.handle_events()
        sala2pt2_screen.update()
    elif tela_atual == "quiz":
        tela_atual = quizuu.handle_events()
        quizuu.update()

    pygame.display.update()

pygame.quit()
