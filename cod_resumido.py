import pygame
import os

# INICIANDO O JOGO & PREPARANDO O DIRETÓRIO DE IMAGENS

pygame.init()

x, y = 1600, 900

WHITE = (255, 255, 255)

window = pygame.display.set_mode([x, y])
pygame.display.set_caption("PerfGens")

main_dir = os.path.dirname(__file__)
dir_img = os.path.join(main_dir, "img")

pygame.mixer.music.load('dirty-phonk-music-141626.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

armariosound = pygame.mixer.music.load('armariosound.mp4')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
teladatemperaturasound = pygame.mixer.music.load('telatempsound.mp4')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)



click_sound = pygame.mixer.Sound('mouse-click-153941.mp3')

# FUNÇÕES PARA IMAGENS


def img_cut(img_name, in_x, in_y):
    a = pygame.image.load(os.path.join(dir_img, img_name)).convert_alpha()
    a = pygame.transform.scale(a, (in_x, in_y))
    return a


def img(img_name):
    a = pygame.image.load(os.path.join(dir_img, img_name)).convert_alpha()
    return a


# IMPORTES DE IMAGEM DE FUNDO
home = img_cut("fundo_inicial.png", 1600, 900)
sala_das_camas = img_cut("sala1_camas.png", 1600, 900)
credits_background = img_cut("fundo_dos_créditos.png", 1600, 900)
salaTV = img_cut("sala_da_tv.png", 1600, 900)
carta_funciona = img_cut("carta.jpg", 1600, 900)
sala2p1 = img_cut("sala2pt1.png", 1600, 900)
menu_middle = img_cut("FundinhoMiddleMenu.png", 1600, 900)
tela1_puzzle1 = img_cut("puzzle1_recado1.png", 1600, 900)  # ATÉ ENTÃO SEM USO
puzzle_garrafas = img_cut("fundo_puzzlegarrafa.png", 1600, 900)
inventory_screen = img_cut("caixotes.png", 1600, 900)
estanteR = img_cut("Estanteampli.png", 1600, 900)
sala2pt2 = img_cut("Sala2pt2.png", 1600, 900)
telaquiz = img_cut("Telaquiz.png", 1600, 900)
escada_acima = img_cut("escada_acima.png", 1600, 900)

# IMPORTES DE IMAGENS DE ELEMENTOS
start_, start_pressed = img("iniciar.png"), img("iniciar_pressionado.png")
credits_, credits_pressed = img("créditos.png"), img("créditos_pressionado.png")
exit_, exit_pressed = img("sair.png"), img("sair_pressionado.png")
back, back_pressed = img("pink_back.png"), img("yellow_back.png")
continuar, continuar_pressed = img("continuar.png"), img("continuar_amarelo.png")
avante, avante_hover = img("mini_continuar.png"), img("mini_continuar_hovering.png")
black_square = img("balão_escuro.png")
retomar, retomar_pressed = img("Menu_middle1.png"), img("Menu_middle_pressed1.png")
inventario, inventario_pressed = img("Menu_middle2.png"), img("Menu_middle_pressed2.png")
middleToMain, middleToMainHover = img("Menu_middle3.png"), img("Menu_middle_pressed3.png")
valvula = img_cut("Botão_valvula.png", 100, 100)
abrir, abrir_pressed = img("abrir.png"), img("abrir_pressed.png")
bixinestrain = img_cut("bixinestranho.png", 600, 800)
dedindocao = img_cut("dedindocão.png", 600, 800)
fichakleitin = img_cut("fichinhadoKleitin.png", 600, 800)
b = img_cut("bixinestranho.png", 180, 250)
d = img_cut("dedindocão.png", 180, 250)
k = img_cut("fichinhadoKleitin.png", 180, 250)
loucuras, loucurasBIG = img("importLoUcUrAs.png"), img_cut("importLoUcUrAs.png", 250, 205)
caixa = img_cut("caixa.png", 589, 471)
caixaR, caixapressedR = img_cut("caixa.png", 200, 200), img_cut("caixapressed.png", 200, 200)
pastaroxaR, pastaroxapressedR = img_cut("pastaroxa.png", 100, 215), img_cut("pastaroxapressed.png", 100, 215)
pastaroxaampli = img_cut("pastaroxaampli.png", 678, 900)
pastaverdeR, pastaverdepressedR = img_cut("pastaverde.png", 100, 215), img_cut("pastaverdepressed.png", 100, 215)
pastaverdeampli = img_cut("pastaverdeampli.png", 678, 900)
seta_preta_esquerda = img("seta esquerda do inventário.png")
seta_preta_esquerda_pressionada = img("seta do inventário pressionada e esquerda.png")
seta_preta_direita = img("seta direita do inventário.png")
seta_preta_direita_pressionada = img("seta do inventário pressionada e direita.png")

seta_preta_esquerda_mini = img_cut("seta esquerda do inventário.png", 40, 40)
seta_preta_esquerda_pressionada_mini = img_cut("seta do inventário pressionada e esquerda.png", 40, 40)
seta_preta_direita_mini = img_cut("seta direita do inventário.png", 40, 40)
seta_preta_direita_pressionada_mini = img_cut("seta do inventário pressionada e direita.png", 40, 40)

buraco = img("buraco.png")
hidden_button = img("hidden_button.png")
fatBox_open, fatBox_closed = img_cut("pão aberto.png", 450, 260), img_cut("pão fechado.png", 450, 260)
chip, chipBIG = img_cut("chip.png", 58, 40), img_cut("chip.png", 174, 120)
pau, pauBIG = img_cut("pau.png", 130, 7), img_cut("pau.png", 370, 20)
tv_on = img_cut("tv_ligada.png", 470, 300)
tv_off = img_cut("tv_apagada.png", 470, 300)

# IMPORTES DE IMAGENS DE ELEMENTOS / SETAS CINZA
seta, seta_pressed = img_cut("seta.png", 50, 50), img_cut("seta_pressed.png", 50, 50)
seta_left, seta_left_hover = img_cut("seta_esquerda.png", 100, 100), img_cut("seta_esquerda_pressed.png", 100, 100)
seta_right, seta_right_hover = img_cut("seta cinza direita.png", 100, 100), img_cut(
    "seta cinza direita pressionada.png", 100, 100)

# TEMPERATURAS
grau1 = img_cut("grau1.png", 700, 280)
grau2 = img_cut("grau2.png", 700, 280)
grau3 = img_cut("grau3.png", 700, 280)
grau4 = img_cut("grau4.png", 700, 280)
grau_aberto = img_cut("grau_aberto.png", 700, 280)
chave = img_cut("chave.png", 150, 125)

# QUIZ DE VARJÃO

inic, vaiii = img("Iniciar.png"), img("vai.png")


Q1, K, Na, Cl, Q2, Hcl, MgCl2 = img("Q1.png"), img("K.png"), img("Na.png"), img("Cl.png"), img("Q2.png"),\
                                img("HCl.png"), img("MgCl2.png")


SO2, C2H2, Q3, C2H5OH, C6H8O7, MDC = img("SO2.png"), img("C2H2.png"), img("Q3.png"), img("C2H5OH.png"),\
                                     img("C6H8O7.png"), img("MDC.png")


# OUTRAS VARIÁVEIS

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
texto8 = "LOUCUUURAS   guardado  no  inventário"
texto9 = "nada aqui"
texto10 = "Graveto adicionado ao seu inventário"
texto11 = "Chip adicionado ao seu inventário"
history = "sem telas recentes"

CINZA = (80, 80, 80)

inventory_lot_1 = "Vago"
inventory_lot_2 = "Vago"
inventory_lot_3 = "Vago"
inventory_lot_4 = "Vago"
inventory_lot_5 = "Vago"
inventory_lot_6 = "Vago"
inventory_lot_7 = "Vago"

pasta1 = False
pasta2 = False


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
        self.clicked = False

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
        global click_sound
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if not self.clicked:
                    if self.rect.collidepoint(mouse_pos):
                        click_sound.play()
                        self.clicked = True
                        return True
            else:
                self.clicked = False


class EscadaAcima:
    def __init__(self):
        window.blit(escada_acima, (0, 0))
        self.voltar = Button(100, 1000, seta_left, seta_left_hover)

    def update(self):
        window.blit(escada_acima, (0, 0))
        self.voltar.draw()

        if self.voltar.check_click():
            return "sala2p1"

        return "escada_acima"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if self.voltar.check_click():
            return "sala2p1"

        return "escada_acima"


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
        self.ir_pra_sala_esquerda = Button(100, 560, seta_left, seta_left_hover)
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
            self.hidden_button.bye_bye()
            self.buraco.draw()
        else:
            self.hidden_button.draw()
        if self.buraco.check_click():
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
            self.buraco.draw()
        else:
            self.hidden_button.draw()

        if self.buraco.check_click():
            self.contagem_do_black_square_pt2 += 1

        if self.contagem_do_black_square_pt2 != 0:
            window.blit(black_square, (100, 550))
            window.blit(self.recado2, (200, 645))
            self.varControle += 0.5
        if self.varControle > self.max_time:
            self.contagem_do_black_square_pt2 = 0
            self.varControle = 0


class Carta:
    def __init__(self):
        window.blit(carta_funciona, (0, 0))
        self.voltar = Button(100, 500, seta_left, seta_left_hover)

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
        self.ir_pra_sala_esquerda = Button(100, 560, seta_left, seta_left_hover)


class SalaDaTV:
    def __init__(self):
        window.blit(salaTV, (0, 0))
        self.ir_pra_sala_esquerda = Button(100, 560, seta_left, seta_left_hover)
        self.voltar_pra_garrafona1 = Button(1500, 560, seta_right, seta_right_hover)
        self.vai_pra_estante = Button(1000, 400, seta, seta_pressed)
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
                return "quiz"

        if self.vai_pra_estante.check_click():
            return "estante"
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
        self.vai_pra_estante.draw()
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
        window.blit(grau1, (300, 300))
        self.voltar_pra_tv = Button(1500, 560, seta_right, seta_right_hover)
        self.one = True
        self.two = False
        self.three = False
        self.four = False
        self.left = Button(1020, 270, seta_preta_esquerda_mini, seta_preta_esquerda_pressionada_mini)
        self.right = Button(1120, 270, seta_preta_direita_mini, seta_preta_direita_pressionada_mini)
        self.var1, self.var2, self.var3, self.var4, self.var5, self.var6 = 0, 0, 0, 0, 0, 0
        self.temperatura = 0
        self.text = str(self.temperatura)
        self.abrir_conte = 0
        self.abrir = False
        self.chave = Button(800, 236, chave, chave)
        self.show_chaves = False
        self.chave_cont = 0
        self.sou_lerda = 0
        self.suicide = 0

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

        if self.one and self.right.check_click():
            self.one = False
            self.two = True
            self.var1 = 0

        if self.two and self.right.check_click():
            self.two = False
            self.three = True
            self.var2 = 0

        if self.three and self.right.check_click():
            self.three = False
            self.four = True
            self.var3 = 0

        if self.four and self.left.check_click():
            self.four = False
            self.three = True
            self.var4 = 0

        if self.three and self.left.check_click():
            self.three = False
            self.two = True
            self.var5 = 0

        if self.two and self.left.check_click():
            self.two = False
            self.one = True
            self.var6 = 0

        if self.voltar_pra_tv.check_click():
            for e in range(1, 100000):
                if e == 99999:
                    return "salaTV"
                print(e)

        if self.one:
            self.temperatura = 0
        elif self.two:
            self.temperatura = 200
        elif self.three:
            self.temperatura = 900
        elif self.four:
            self.temperatura = 1500

        return "garrafa_pt_2"

    def update(self):
        global inventory_lot_7
        window.blit(sala2pt2, (0, 0))
        text = recadinhos(self.text, WHITE)
        window.blit(text, (300, 300))

        if self.one:
            self.temperatura = 0
        elif self.two:
            self.temperatura = 200
        elif self.three:
            self.temperatura = 900
        elif self.four:
            self.temperatura = 1500

        if self.one and self.right.check_click():
            self.var1 += 0.1
            if self.var1 > 8:
                self.one = False
                self.two = True
                self.var1 = 0

        if self.two and self.right.check_click():
            self.var2 += 0.1
            if self.var2 > 8:
                self.two = False
                self.three = True
                self.var2 = 0

        if self.three and self.right.check_click():
            self.var3 += 0.1
            if self.var3 > 8:
                self.three = False
                self.four = True
                self.var3 = 0

        if self.four and self.left.check_click():
            self.var4 += 0.1
            if self.var4 > 8:
                self.four = False
                self.three = True
                self.var4 = 0

        if self.three and self.left.check_click():
            self.var5 += 0.1
            if self.var5 > 8:
                self.three = False
                self.two = True
                self.var5 = 0

        if self.two and self.left.check_click():
            self.var6 += 0.1
            if self.var6 > 8:
                self.two = False
                self.one = True
                self.var6 = 0

        if self.one:
            window.blit(grau1, (525, 80))
        elif self.two:
            window.blit(grau2, (525, 80))
        elif self.three:
            window.blit(grau3, (525, 80))
        elif self.four:
            window.blit(grau4, (525, 80))
        self.voltar_pra_tv.draw()

        self.left.draw()
        self.right.draw()

        if self.left.check_click():
            teladatemperaturasound.play()
        if self.right.check_click():
            teladatemperaturasound.play()

        if self.four:
            self.abrir_conte += 0.2
            if self.abrir_conte > 10:
                self.abrir = True

        if self.abrir:
            window.blit(grau_aberto, (525, 80))
            self.show_chaves = True
            self.chave_cont += 0.5
            if self.chave.check_click() and self.chave_cont > 10:
                self.show_chaves = False
                self.sou_lerda += 1
                self.suicide += 1

            if self.suicide > 2:
                inventory_lot_7 = "chave_escada"

            if self.show_chaves and self.sou_lerda < 2:
                self.chave.draw()

        return "garrafa_pt_2"


class SaladasGarrafonas:
    def __init__(self):
        window.blit(sala2p1, (0, 0))
        self.escada = Button(680, 300, seta, seta_pressed)
        self.puzzlegarrafa = Button(380, 300, seta, seta_pressed)
        self.avante = Button(1350, 285, avante, avante_hover)
        self.loucuras = Button(1100, 336, loucuras, loucuras)
        self.ir_pra_sala_esquerda = Button(100, 560, seta_left, seta_left_hover)
        self.caixa = black_square
        self.texto = texto5
        self.texto2 = texto8
        self.texto10 = texto10
        self.texto11 = texto11
        self.recadin = recadinhos(self.texto, WHITE)
        self.recadin2 = recadinhos(self.texto2, WHITE)
        self.recadin3 = recadinhos(self.texto10, WHITE)
        self.recadin4 = recadinhos(self.texto11, WHITE)
        self.voltar_pra_sala_das_camas = Button(1500, 560, seta_right, seta_right_hover)
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
        global history, inventory_lot_7
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
        if self.pau.check_click():
            armariosound.play()


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
            if inventory_lot_7 == "Vago":
                self.msg = True
            elif inventory_lot_7 == "chave_escada":
                return "escada_acima"

        elif self.avante.check_click():
            self.msg = False
        elif self.puzzlegarrafa.check_click():
            return "puzzlegarrafa"

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
        global inventory_lot_1, inventory_lot_2, inventory_lot_3, inventory_lot_7
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
        self.puzzlegarrafa.draw()

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

        if not self.msg:
            pass

        self.escada.draw()
        self.ir_pra_sala_esquerda.draw()

        if self.msg:
            window.blit(self.caixa, (100, 100))
            window.blit(self.recadin, (200, 200))
            self.avante.draw()
        if self.voltar_pra_sala_das_camas.check_click():
            return "camas"
        elif self.escada.check_click():
            if inventory_lot_7 == "Vago":
                self.msg = True
            elif inventory_lot_7 == "chave_escada":
                return "escada_acima"
            print(inventory_lot_7)



        return "sala2p1"



class Estante:
    def __init__(self):
        window.blit(estanteR, (0, 0))
        window.blit(pastaroxaampli, (400, 10))
        window.blit(pastaverdeampli, (400, 10))
        window.blit(caixa, (500, 200))
        self.caixa = Button(840, 750, caixaR, caixapressedR)
        self.pastaroxa = Button(680, 225, pastaroxaR, pastaroxapressedR)
        self.pastaverde = Button(870, 225, pastaverdeR, pastaverdepressedR)
        self.volta = Button(300, 500, seta_left, seta_left_hover)
        self.abrir = Button(1500, 800, abrir, abrir_pressed)
        self.Ca = False
        self.Pr = False
        self.Pv = False
        self.princ = True

    def handle_events(self):
        global history, pasta1, pasta2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_estante"
                    return "menu_middle"

        if self.princ == True:
            if self.caixa.check_click():
                self.Ca = True
                self.princ = False
            if self.pastaroxa.check_click():
                self.Pr = True
                self.princ = False
            if self.pastaverde.check_click():
                self.Pv = True
                self.princ = False
        else:
            pass
        if self.volta.check_click():
            self.princ = True
            if self.Ca == True:
                self.Ca = False
            elif self.Pr == True:
                self.Pr = False
            elif self.Pv == True:
                self.Pv = False

        if self.abrir.check_click():
            if self.Ca == True:
                pass
            elif self.Pv == True or self.Pr == True:
                if self.Pv == True:
                    pasta1 = True
                    pasta2 = False
                elif self.Pr == True:
                    pasta2 = True
                    pasta1 = False
                return "arquivos"


        return "estante"


    def update(self):
        global pasta1, pasta2
        window.blit(estanteR, (0, 0))
        if self.princ == True:
            self.pastaroxa.draw()
            self.pastaverde.draw()
            self.caixa.draw()
        if self.Ca == True:
            window.blit(caixa, (500, 200))
            self.volta.draw()
            self.abrir.draw()
        elif self.Pr == True:
            window.blit(pastaroxaampli, (400, 10))
            self.volta.draw()
            self.abrir.draw()
        elif self.Pv == True:
            window.blit(pastaverdeampli, (400, 10))
            self.volta.draw()
            self.abrir.draw()


class Arquivos:
    def __init__(self):
        window.fill("DimGray")
        self.caixa = black_square
        self.bixinfei = Button(500, 450, bixinestrain, bixinestrain)
        self.dedindocao = Button(1100, 450, dedindocao, dedindocao)
        self.kleitin = Button(800, 450, fichakleitin, fichakleitin)
        self.voltar = Button(100, 500, seta_left, seta_left_hover)

    def handle_events(self):
        global pasta1, pasta2, history, inventory_lot_4, inventory_lot_5, inventory_lot_6
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_arquivo"
                    return "menu_middle"
        if pasta1:
            if self.kleitin.check_click():
                if inventory_lot_4 == "Vago":
                    inventory_lot_4 = "Ficha_Kleitinho"

        elif pasta2:
            if self.dedindocao.check_click():
                if inventory_lot_5 == "Vago":
                    inventory_lot_5 = "Ficha_dedinho"

            elif self.bixinfei.check_click():
                if inventory_lot_6 == "Vago":
                    inventory_lot_6 = "Ficha_bichinho"

        if self.voltar.check_click():
            return "estante"

        return "arquivos"

    def update(self):
        global pasta1, pasta2, inventory_lot_4, inventory_lot_5, inventory_lot_6
        window.fill("DimGray")
        self.voltar.draw()

    def update(self):
        global pasta1, pasta2, inventory_lot_4, inventory_lot_5, inventory_lot_6
        window.fill("DimGray")
        self.voltar.draw()
        if pasta1:
            if inventory_lot_4 != "Ficha_Kleitinho":
                self.kleitin.draw()
        elif pasta2:
            if inventory_lot_6 != "Ficha_bichinho":
                self.bixinfei.draw()
            if inventory_lot_5 != "Ficha_dedinho":
                self.dedindocao.draw()


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
        self.close_inventory = Button(100, 800, seta_left, seta_left_hover)
        self.loucuras = Button(230, 200, loucurasBIG, loucurasBIG)
        self.pau = Button(800, 200, pauBIG, pauBIG)
        self.chip = Button(1200, 200, chipBIG, chipBIG)
        self.ficha_kleitin = Button(230, 500, k, k)
        self.ficha_dedinho = Button(800, 500, d, d)
        self.ficha_bichinho = Button(1300, 500, b, b)
        self.texto = texto9
        self.recado = recadinhos(texto9, CINZA)
        self.chave = Button(250, 730, chave, chave)

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

        if inventory_lot_1 == "Vago":
            pass
        elif inventory_lot_1 == "Loucuras":
            self.loucuras.draw()

        if inventory_lot_2 == "Vago":
            pass
        elif inventory_lot_2 == "Pau":
            self.pau.draw()

        if inventory_lot_3 == "Vago":
            pass
        elif inventory_lot_3 == "Chip":
            self.chip.draw()

        if inventory_lot_4 == "Vago":
            pass
        elif inventory_lot_4 == "Ficha_Kleitinho":
            self.ficha_kleitin.draw()

        if inventory_lot_5 == "Vago":
            pass
        elif inventory_lot_5 == "Ficha_dedinho":
            self.ficha_dedinho.draw()

        if inventory_lot_6 == "Vago":
            pass
        elif inventory_lot_6 == "Ficha_bichinho":
            self.ficha_bichinho.draw()

        if inventory_lot_7 == "Vago":
            pass
        elif inventory_lot_7 == "chave_escada":
            self.chave.draw()


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
                    self.comc = True
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
        window.blit(telaquiz, (0, 0))
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


agua = False
ok_sequence = "Não"

class PuzzleGarrafas:
    def __init__(self):
        window.blit(puzzle_garrafas, (0, 0))
        self.valv1 = Button(425, 550, valvula, valvula)
        self.valv2 = Button(880, 550, valvula, valvula)
        self.valv3 = Button(1330, 550, valvula, valvula)
        self.first_condition = 0
        self.second_condition = 0

    def handle_events(self):
        global history, ok_sequence
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    history = "registrando_puzzle_garrafas"
                    return "menu_middle"


        if self.valv1.check_click():
            self.first_condition = 1

        if self.first_condition != 0 and self.valv2.check_click():
            self.first_condition = 0

        if self.first_condition != 0 and self.valv3.check_click():
            self.second_condition = 1

        if self.first_condition != 0 and self.second_condition != 0:
            ok_sequence = "ok_sequence"

            print(self.first_condition, self.second_condition)

        return "puzzlegarrafa"

    def update(self):
        global ok_sequence, agua

        window.blit(puzzle_garrafas, (0, 0))
        self.valv1.draw()
        self.valv2.draw()
        self.valv3.draw()
        if ok_sequence == "ok_sequence":
            window.blit(caixa, (500, 500))
        else:
            agua = False


class MiddleMenu:
    def __init__(self):
        global history
        window.blit(menu_middle, (0, 0))
        self.retomar = Button(790, 255, retomar, retomar_pressed)
        self.invent = Button(790, 455, inventario, inventario_pressed)
        self.menuinic = Button(790, 655, middleToMain, middleToMainHover)
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
            elif history == "registrando_puzzle_garrafas":
                return "puzzlegarrafa"

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


escada_pra_up = EscadaAcima()
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
garrafinas = PuzzleGarrafas()
arqui = Arquivos()
tela_atual = "main_menu"


run = True
while run:
    if tela_atual == "main_menu":
        tela_atual = main_menu.handle_events()
        main_menu.update()
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
    elif tela_atual == "puzzlegarrafa":
        tela_atual = garrafinas.handle_events()
        garrafinas.update()
    elif tela_atual == "arquivos":
        tela_atual = arqui.handle_events()
        arqui.update()
    elif tela_atual == "escada_acima":
        tela_atual = escada_pra_up.handle_events()
        escada_pra_up.update()
    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()