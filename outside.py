import pygame
import playsound
import os
import sys
import time

# classes

class Button:
    def __init__(self, x, y, image_normal, image_hover, actions=None):
        self.x = x
        self.y = y
        self.image_normal = image_normal
        self.image_hover = image_hover
        self.rect = self.image_normal.get_rect()
        self.rect.topleft = (x, y)
        self.actions = actions if actions else []
        self.visible = True
        self.clicked = False  # Adicionando um atributo para rastrear os cliques

        self.show_text_function = None
        self.text_displayed = False

    def draw(self, screen):
        if self.visible:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.image_hover, (self.x, self.y))
            else:
                screen.blit(self.image_normal, (self.x, self.y))

    def check_click(self):
        if self.visible:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                for action in self.actions:
                    action()
                self.clicked = True  # Marcar o botão como clicado após a ação

    def reset_click(self):
        self.clicked = False

    def set_show_text_function(self, show_text_function):
        self.show_text_function = show_text_function

    def draw_text(self, screen):
        if self.clicked and self.show_text_function:
            self.show_text_function()
            self.clicked = False

    def hide(self):
        self.visible = False


# Função para exibir texto letra por letra em uma imagem
def show_text_on_image(screen, text):
    global balaoescuro
    font = pygame.font.Font(None, 40)
    image = pygame.image.load("img/balão_escuro.png")
    for i in range(len(text) + 1):
        text_surface = font.render(text[:i], True, (255, 255, 255))
        image.blit(text_surface, (40, 60))
        screen.blit(image, (100, 600))
        pygame.display.update()
        time.sleep(0.02)

    # Desaparecer depois de 3 segundos
    start_time = time.time()
    while time.time() - start_time < 3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def img(img):
    a = pygame.image.load(img).convert_alpha()
    return a


def img_cut(img, x, y):
    a = pygame.image.load(img).convert_alpha()
    a = pygame.transform.scale(a, (x, y))
    return a


pygame.init()
pygame.mixer.init()


# Configurações da tela
X = 1536
Y = 864
window = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Outside")

# imagens


# ----fundos----
divagar = img_cut("img/divagar.png", X, Y)
cre1 = img_cut("img/cred1.png", X, Y)
cre2 = img_cut("img/cred2.png", X, Y)
cre3 = img_cut("img/cred3.png", X, Y)
cre4 = img_cut("img/cred4.png", X, Y)
cre5 = img_cut("img/cred5.png", X, Y)
cre6 = img_cut("img/cred6.png", X, Y)
cre7 = img_cut("img/cred7.png", X, Y)
cre8 = img_cut("img/cred8.png", X, Y)
eye_box_tela = img_cut("img/caixa_lastroom_open_active.png", X, Y)
tela_do_pc = img_cut("img/fundo_do_pc.png", X, Y)
home = img_cut("img/fundo_inicial.png", X, Y)
credits_background = img_cut("img/fundo_dos_créditos.png", X, Y)
fundo_geral = img_cut("img/fundo.png", X, Y)
fundopuzzlegarrafa = img_cut("img/Fundo_puzzlegarrafa.png", X, Y)
fundosaladatv = img_cut("img/fundo_salaTv_water.png", X, Y)
fundosaladatvnowater = img_cut("img/fundo_salaTv_nowater.png", X, Y)
estanteampli = img_cut("img/Estanteampli.png", X, Y)
fundo_middlemenu = img_cut("img/FundinhoMiddleMenu.png", X, Y)
graucinza = img_cut("img/grau_cinza.png", 585.5, 216)
grauaberto = img_cut("img/grau_aberto.png", 300, 300)
telaquiz = img_cut("img/Telaquiz.png", X, Y)
sala_das_camas = img_cut("img/sala1_camas.png", X, Y)
Q1 = img_cut("img/Q1.png", X, Y)
Q2 = img_cut("img/Q2.png", X, Y)
Q3 = img_cut("img/Q3.png", X, Y)
puzzle1recado1 = img_cut("img/puzzle1_recado1.png", X, Y)
puzzlesenha = img_cut("img/puzzle_senha.png", X, Y)
sala2pt2 = img_cut("img/Sala2pt2.png", X, Y)
inventario_screen = img_cut("img/inventário.png", X, Y)

quiz_lastroom_inic = img_cut("img/Fundo_iniciar_lastdoor.png", 1600, 900)
quiz_lastroom = img_cut("img/Fundo_questions_lastdoor.png", 1600, 900)

lost_ld = img_cut("img/Youlost.png", 1600, 900)

tela_carta = img_cut("img/carta.jpg", X, Y)

porta_vermelho = img_cut("img/porta_vermei.png", X, Y)
porta_verde = img_cut("img/porta_abriu.png", X, Y)

# ----elementos_salas----

Q1_ld = img("img/Q1_lastdoor.png")
Q2_ld = img("img/Q2_lastdoor.png")

cama = img_cut("img/Cama.png", 440, 340)
escada = img_cut("img/escada.png", 169.33, 601.33)
estante = img_cut("img/estante.png", 491.667, 561.667)
armarioo = img_cut("img/armario.png", 734.44, 263.33)
buraco = img_cut("img/buraco.png", 728, 385)
garrafas = img_cut("img/garrafas.png", 450, 600)
pau = img_cut("img/pau.png", 130, 7)
chip = img_cut("img/chip.png", 120, 80)
chipampli = img_cut("img/chip.png", 540, 325.5)
pastaroxa, pastaroxapressed = img_cut("img/pastaroxa.png", 95, 205), img_cut("img/pastaroxapressed.png", 95, 205)
pastaverde, pastaverdepressed = img_cut("img/pastaverde.png", 95, 205), img_cut("img/pastaverdepressed.png", 95, 205)
pastaroxaampli = img_cut("img/pastaroxaampli.png", 618, 840)
pastaverdeampli = img_cut("img/Pastaverdeampli.png", 618, 840)
caixaampli = img("img/caixa.png")


caixalastroom = img("img/caixa_lastroom.png")
caixalastroomopen = img("img/caixa_lastroom_open_active.png")
caixalastroomnoactive = img("img/caixa_lastroom_open_notactive.png")
portaclosed = img_cut("img/porta_closed.png", 302, 476)
portalastroom = img_cut("img/porta_lastroom.png", 302, 476 )
portaopen = img_cut("img/porta_open.png", 302, 476)
grau1 = img("img/grau1.png")
grau2 = img("img/grau2.png")
grau3 = img("img/grau3.png")
grau4 = img("img/grau4.png")
chave = img_cut("img/chave.png", 150, 125)

bixinestrain = img_cut("img/bixinestranho.png", 604, 860)
kleitin = img_cut("img/fichinhadoKleitin.png", 604, 860)
dedin = img_cut("img/dedindocão.png", 604, 860)

pc = img_cut("img/pc.png", 613, 327)
x = img("img/x.png")
aviso = img("img/aviso_pc.png")
cancelar = img("img/cancelar.png")
esquecer = img("img/esquecer.png")

# ----Botões----

voltar_cred = img("img/voltarcred.png")
avante_cred = img("img/avantecred.png")
forpc = img("img/botao_pc.png")
iniciar = img("img/iniciar.png")
iniciar_pressionado = img("img/iniciar_pressionado.png")
creditos = img("img/créditos.png")
creditos_pressionado = img("img/créditos_pressionado.png")
sair = img("img/sair.png")
sair_pressionado = img("img/sair_pressionado.png")
back, back_pressed = img("img/pink_back.png"), img("img/yellow_back.png")
retomar = img("img/Menu_middle1.png")
retomarpressed = img("img/Menu_middle_pressed1.png")
inventario = img("img/Menu_middle2.png")
inventariopressed = img("img/Menu_middle_pressed2.png")
menuinicial = img("img/Menu_middle3.png")
menuinicialpressed = img("img/Menu_middle_pressed3.png")
armarioclosed = img_cut("img/armario_closed.png", X, Y)
armarioopen = img_cut("img/armario_open.png", X, Y)
caixa, caixapressed = img_cut("img/caixa.png", 190, 180), img_cut("img/caixapressed.png", 190, 180)
seta = img("img/seta.png")
setaesquerda, setaesquerdapressed = img_cut("img/seta_esquerda.png", 30, 50),  img_cut("img/seta_esquerda_pressed.png", 30, 50)
setaesquerdadoinventario, setaesquerdadoinventariopressionada = img("img/seta esquerda do inventário.png"), img("img/seta do inventário pressionada e esquerda.png")
setadireitadoinventario, setadireitadoinventariopressed = img("img/seta direita do inventário.png"), img("img/seta do inventário pressionada e direita.png")
setadireita, setadireitapressed = img_cut("img/seta cinza direita.png", 30, 50), img_cut("img/seta cinza direita pressionada.png", 30, 50)
tvligada = img_cut("img/tv_ligada.png", 437.5, 282.5)
hiddenbutton = img("img/hidden_button.png")
valvula = img_cut("img/Botão_valvula.png", 150, 150)
botaopc = img("img/botao_pc.png")
balaoescuro = img("img/balão_escuro.png")
ativado = img("img/ativado.png")
caixotes = img("img/caixotes.png")
abrir, abrirpressed = img("img/abrir.png"), img("img/abrir_pressed.png")
usar = img("img/usar.png")
usarpressed = img("img/usar_hover.png")
vai = img("img/vai.png")
K = img("img/K.png")
MDC = img_cut("img/MDC.png", X, Y)
C2H2 = img("img/C2H2.png")
C2H5OH = img("img/C2H5OH.png")
MgC12 = img("img/MgCl2.png")
C6H8O7 = img("img/C6H8O7.png")
SO2 = img("img/SO2.png")
HCl = img("img/HCl.png")
Na = img("img/Na.png")
Cl = img("img/Cl.png")
caixa_lastroom_png = img_cut("img/caixa_lastroom.png", 200, 200)
green_machine_png = img_cut("img/ativado.png", 600, 600)
red_machine_png = img_cut("img/desativado.png", 600, 600)

avante_darkgrey = img("img/avante_darkgrey.png")
avante_lightgrey = img("img/avante_lightgrey.png")
olho = img("img/botão_olho.png")

Op1q1_ld = img("img/Op1_q1_lastdoor.png")
Op2q1_ld = img("img/Op2_q1_lastdoor.png")
Op3q1_ld = img("img/Op3_q1_lastdoor.png")

Op1q2_ld = img("img/Op1_q2_lastdoor.png")
Op2q2_ld = img("img/Op2_q2_lastdoor.png")
Op3q2_ld = img("img/Op3_q2_lastdoor.png")

voltar_lastroom = img("img/voltar_lastroom.png")
voltar_lastroom_hover = img("img/voltar_pressed_lastroom.png")

#inventário

bixinededin = img_cut("img/bixinededin.png", 480, 480)
bixinekleitin = img_cut("img/bixinekleitin.png", 480, 480)
kleitinededin = img_cut("img/kleitinededin.png", 480, 480)
trêsjuntos = img_cut("img/trêsfichinhas.png", 480, 480)

# -----"Covalentes" -----

A, Apressed = img_cut("img/A.png", 116.2, 195), img_cut("img/A_pressed.png", 96.4, 173.2)
C, Cpressed = img_cut("img/C.png", 116.2, 195), img_cut("img/C_pressed.png", 96.4, 173.2)
E, Epressed = img_cut("img/E.png", 116.2, 195), img_cut("img/E_pressed.png", 96.4, 173.2)
L, Lpressed = img_cut("img/L.png", 116.2, 195), img_cut("img/L_pressed.png", 96.4, 173.2)
N, Npressed = img_cut("img/N.png", 116.2, 195), img_cut("img/N_pressed.png", 96.4, 173.2)
O, Opressed = img_cut("img/O.png", 116.2, 195), img_cut("img/O_pressed.png", 96.4, 173.2)
S, Spressed = img_cut("img/S.png", 116.2, 195), img_cut("img/S_pressed.png", 96.4, 173.2)
T, Tpressed = img_cut("img/T.png", 116.2, 195), img_cut("img/T_pressed.png", 96.4, 173.2)
V, Vpressed = img_cut("img/V.png", 116.2, 195), img_cut("img/V_pressed.png", 96.4, 173.2)

Comb_right = img_cut("img/Comb_right.png", X, Y)
Comb_wrong = img_cut("img/Comb_wrong.png", X, Y)

setacimaarm, setacimaarmpressed = img("img/seta_cima_armario.png"), img("img/seta_cima_arm_pressed.png")
setabaixoarm, setabaixoarmpressed = img("img/seta_baixo_armario.png"), img("img/seta_baixo_arm_pressed.png")

Ag_arm = img("img/Ag_arm.png")
Au_arm = img("img/Au_arm.png")
Br_arm = img("img/Br_arm.png")
C_arm = img("img/C_arm.png")
Ca_arm = img("img/Ca_arm.png")
Cl_arm = img("img/Cl_arm.png")
Ga_arm = img("img/Ga_arm.png")
H_arm = img("img/H_arm.png")
Hg_arm = img("img/Hg_arm.png")
O_arm = img("img/O_arm.png")

setaesquerdagrau, setaesquerdagraupressed = img("img/left_grau.png"), img("img/left_grau_pressed.png")
setadireitagrau, setadireitagraupressed = img("img/right_grau.png"), img("img/right_grau_pressed.png")
# variáveis
tela_atual = "main_menu"

rightcomb = False
comb = []

valv = []

water = False

Q1_lastd = False
Q2_lastd = False

roxo = False
verde = False
caixaestante = False
resposta = False
chave1 = False

fichetas = []
fichetas_checktotal = {'bixin', 'dedin', 'kleit'}
fichetas_check1 = {'bixin', 'dedin'}
fichetas_check2 = {'bixin', 'kleit'}
fichetas_check3 = {'kleit', 'dedin'}

area_invent = 1

counting_quiz_lastdoor = 0
counting_quiz_tv = 0

counting_firstseta_arm = 1
counting_secondseta_arm = 1

# Referente à máquina do olho
olho_on = False

grau = 1

portaaberta = False
cartão = False
cartão_catch = True

# defs

def fade():
    global window
    fade_surface = pygame.Surface((window.get_width(), window.get_height()))
    alpha = 0
    fade_surface.set_alpha(alpha)

    while alpha < 255:
        alpha += 10
        fade_surface.fill((7, 7, 7))  # Preenche com preto, mas pode ser outra cor
        fade_surface.set_alpha(alpha)
        window.blit(fade_surface, (0, 0))
        pygame.display.flip()

    # Lógica para mudar a tela aqui

    while alpha > 0:
        alpha -= 10
        fade_surface.fill((7, 7, 7))  # Preenche com preto, mas pode ser outra cor
        fade_surface.set_alpha(alpha)
        window.blit(fade_surface, (0, 0))
        pygame.display.flip()

def fade_tv():
    global window, water
    if water == True:
        fade_surface = pygame.Surface((window.get_width(), window.get_height()))
        alpha = 0
        fade_surface.set_alpha(alpha)

        while alpha < 255:
            alpha += 10
            fade_surface.fill((7, 7, 7))  # Preenche com preto, mas pode ser outra cor
            fade_surface.set_alpha(alpha)
            window.blit(fade_surface, (0, 0))
            pygame.display.flip()

        # Lógica para mudar a tela aqui

        while alpha > 0:
            alpha -= 10
            fade_surface.fill((7, 7, 7))  # Preenche com preto, mas pode ser outra cor
            fade_surface.set_alpha(alpha)
            window.blit(fade_surface, (0, 0))
            pygame.display.flip()
    else:
        pass

def fundo(img):
    window.blit(img, (0, 0))


def quita():
    pygame.quit()
    quit()


historyy = []

# -----tela ativa-----


def last_screen():
    global tela_atual, historyy
    tela_atual = historyy[-1]

def cred1():
    global tela_atual
    tela_atual = "cred1"


def cred2():
    global tela_atual
    tela_atual = "cred2"


def cred3():
    global tela_atual
    tela_atual = "cred3"


def cred4():
    global tela_atual
    tela_atual = "cred4"


def cred5():
    global tela_atual
    tela_atual = "cred5"


def cred6():
    global tela_atual
    tela_atual = "cred6"


def cred7():
    global tela_atual
    tela_atual = "cred7"


def cred8():
    global tela_atual
    tela_atual = "cred8"

lala = True


def balao_off():
    global lala
    lala = False


def balao_on():
    global lala
    if lala:
        for e in range(0, 10):
            if e < 9:
                window.blit(balaoescuro, (50, 600))


star_png = img("img/star.png")


def divagar_final():
    global tela_atual
    tela_atual = "divagar_final"


def divaga():
    global star
    star.set_show_text_function(
        lambda: show_text_on_image(window, "Me pergunto o que acontece depois daqui... "
                                           "Será algo pior..? "))
    star.draw_text(window)


star = Button(1000, 200, star_png, star_png, actions=[divaga])

def change_telas():
    global tela_atual, historyy, portaaberta
    if tela_atual == "camas":
        if rightcomb == False:
            tela_atual = "covalentes"
        elif rightcomb == True:
            tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "garrafonas":
        tela_atual = "saladatv"
        historyy.append(tela_atual)
    elif tela_atual == "garrafonas_ampliadas":
        tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "carta":
        tela_atual = "camas"
        historyy.append(tela_atual)
    elif tela_atual == "estante":
        tela_atual = "saladatv"
        historyy.append(tela_atual)
    elif tela_atual == "pc_tela_inicial":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "senha1":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "armario":
        tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "arm_open":
        tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "red_caixa":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "green_caixa":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "porta":
        if portaaberta == False:
            tela_atual = "saladatv"
        elif portaaberta == True:
            tela_atual = "saladatv_portaberta"

def change_telas_reverse():
    global tela_atual, historyy
    if tela_atual == "garrafonas":
        tela_atual = "camas"
        historyy.append(tela_atual)
    elif tela_atual == "saladatv":
        tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "camas":
        tela_atual = "carta"
        historyy.append(tela_atual)
    elif tela_atual == "saladatv":
        tela_atual = "estante"
        historyy.append(tela_atual)

def change_telas():
    global tela_atual, historyy, portaaberta
    if tela_atual == "camas":
        if rightcomb == False:
            tela_atual = "covalentes"
        elif rightcomb == True:
            tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "garrafonas":
        tela_atual = "saladatv"
        historyy.append(tela_atual)
    elif tela_atual == "garrafonas_ampliadas":
        tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "carta":
        tela_atual = "camas"
        historyy.append(tela_atual)
    elif tela_atual == "estante":
        tela_atual = "saladatv"
        historyy.append(tela_atual)
    elif tela_atual == "pc_tela_inicial":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "senha1":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "armario":
        tela_atual = "garrafonas"
        historyy.append(tela_atual)
    elif tela_atual == "red_caixa":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "green_caixa":
        tela_atual = "mesa"
        historyy.append(tela_atual)
    elif tela_atual == "porta":
        if portaaberta == False:
            tela_atual = "saladatv"
        elif portaaberta == True:
            tela_atual = "saladatv_portaberta"


def main_menu():
    global tela_atual, historyy, roxo, verde, water, caixaestante, Q1_lastd, Q2_lastd
    tela_atual = "main_menu"
    historyy.append(tela_atual)
    roxo = False
    verde = False
    caixaestante = False
    Q1_lastd = False
    Q2_lastd = False



def cred():
    global tela_atual
    tela_atual = "cred1"


def saladascamas():
    global tela_atual, historyy
    tela_atual = "camas"
    historyy.append(tela_atual)


def sala_da_senha1():
    global tela_atual, historyy
    tela_atual = "senha1"
    historyy.append(tela_atual)

def telaPC():
    global tela_atual, historyy
    tela_atual = "pc_tela_inicial"
    historyy.append(tela_atual)


def telaPCaviso():
    global tela_atual, historyy
    tela_atual = "pc_aviso"
    historyy.append(tela_atual)

def first():
    global comb
    a = 1
    comb.append(a)

def second():
    global comb
    a = 2
    comb.append(a)

def third():
    global comb
    a = 3
    comb.append(a)

def fourth():
    global comb
    a = 4
    comb.append(a)

def fifth():
    global comb
    a = 5
    comb.append(a)

def sixth():
    global comb
    a = 6
    comb.append(a)

def seventh():
    global comb
    a = 7
    comb.append(a)

def eighth():
    global comb
    a = 8
    comb.append(a)

def nineth():
    global comb
    a = 9
    comb.append(a)

def tenth():
    global comb
    a = 10
    comb.append(a)


def saladasgarrafonas():
    global tela_atual, historyy
    tela_atual = "garrafonas"
    historyy.append(tela_atual)

def garrafas_ampliadas():
    global tela_atual, historyy
    tela_atual = "garrafonas_ampliadas"
    historyy.append(tela_atual)

lala = True


def balao_off():
    global lala
    lala = False


def balao_on():
    global lala
    if lala:
        for e in range(0, 10):
            if e < 9:
                window.blit(balaoescuro, (50, 600))


def saladaTV():
    global tela_atual, historyy
    tela_atual = "saladatv"
    historyy.append(tela_atual)

# -----Sala da TV-----

def quiz_da_tv():
    global water, tela_atual, resposta, historyy
    if water == True:
        if resposta == False:
            tela_atual = "quiz_tv"
        elif resposta == True:
            tela_atual = "resposta_tv"
    elif water == False:
        pass
    historyy.append(tela_atual)

def counting_quizzin():
    global counting_quiz_tv
    counting_quiz_tv += 1

def reset_quizzin():
    global counting_quiz_tv
    counting_quiz_tv = 0

def change_perguntinha():
    global counting_quiz_tv, Q1, Q2, Q3
    if counting_quiz_tv == 1:
        window.blit(Q1, (0, 0))
    elif counting_quiz_tv == 2:
        window.blit(Q2, (0, 0))
    elif counting_quiz_tv == 3:
        window.blit(Q3, (0, 0))

def final_button_quiz_tv():
    global tela_atual, historyy
    tela_atual = "resposta_tv"
    historyy.append(tela_atual)


def opc_tv():
    global counting_quiz_tv, tela_atual, historyy
    if counting_quiz_tv == 1:
        tela_atual = "Op1_tv"
    elif counting_quiz_tv == 2:
        tela_atual = "Op2_tv"
    elif counting_quiz_tv == 3:
        tela_atual = "Op3_tv"
    historyy.append(tela_atual)

def respostaa():
    global resposta
    resposta = True


def estantee():
    global tela_atual, history
    tela_atual = "estante"
    history = "estante"

def PR():
    global roxo, tela_atual, historyy
    roxo = True
    tela_atual = "pastaroxa"
    historyy.append(tela_atual)

def PV():
    global verde, tela_atual, historyy
    verde = True
    tela_atual = "pastaverde"
    historyy.append(tela_atual)

def CE():
    global caixaestante, tela_atual, historyy
    caixaestante = True
    tela_atual = "caixa_fora"
    historyy.append(tela_atual)

def arq1():
    global tela_atual, roxo, verde, historyy
    if roxo == True:
        tela_atual = "arquivos_estante1"
    elif verde == True:
        tela_atual = "arquivos_estante2"
    historyy.append(tela_atual)
def return_estante():
    global caixaestante, verde, roxo, tela_atual, historyy
    caixaestante = False
    verde = False
    roxo = False
    tela_atual = "estante"
    historyy.append(tela_atual)


def mesa():
    global tela_atual, historyy
    tela_atual = "mesa"
    historyy.append(tela_atual)

def temperatura():
    global tela_atual, historyy
    tela_atual = "temp"
    historyy.append(tela_atual)

def add_temp():
    global grau
    grau += 1
    if grau == 5:
        grau = 1

def delete_temp():
    global grau
    grau -= 1
    if grau == 0:
        grau = 4

def carta():
    global tela_atual, history
    tela_atual = "carta"
    history = "carta"


def armario():
    global tela_atual, historyy
    tela_atual = "armario"
    historyy.append(tela_atual)



def escada_acima():
    global tela_atual, historyy, chave1
    if chave1 == False:
        escadinha.set_show_text_function(
            lambda: show_text_on_image(window, "Trancado"))
        escadinha.draw_text(window)
    elif chave1 == True:
        tela_atual = "escada_acima"
        historyy.append(tela_atual)


def middle_menu():
    global tela_atual
    tela_atual = "menu_middle"


def inventario_tela():
    global tela_atual
    tela_atual = "inventário"


def quiz_tv():
    global tela_atual
    tela_atual = "quiztv"


def qual_caixa():
    global tela_atual, machine_on
    if machine_on:
        tela_atual = "green_caixa"
    if not machine_on:
        tela_atual = "red_caixa"


def quiz_lastdoor():
    global tela_atual
    tela_atual = "quiz_lastdoor"


def quiz_lastdoor_text1():
    global tela_atual
    tela_atual = "questions_lastdoor1"


def quiz_lastdoor_text2():
    global tela_atual
    tela_atual = "questions_lastdoor2"


def quiz_lastdoor_op1():
    global tela_atual
    tela_atual = "op_lastdoor1"


def quiz_lastdoor_op2():
    global tela_atual
    tela_atual = "op_lastdoor2"


def lost_lastdoor():
    global tela_atual
    tela_atual = "You've_lost"

def abre():
    global tela_atual, area_invent, fichetas, cartão, portaaberta
    if area_invent == 1:
        if fichetas != []:
            tela_atual = "invent_arq"
    elif area_invent == 2:
        if cartão == False and portaaberta == False and historyy[-1] == "porta":
            cartão = True

def portafechabre():
    global tela_atual, historyy
    tela_atual = "porta"
    historyy.append(tela_atual)


#---combinações---

def first_val():
    global valv, fichetas
    if fichetas == []:
        valv1.set_show_text_function(
            lambda: show_text_on_image(window, "Não sei o que fazer aqui"))
        valv1.draw_text(window)
    else:
        a = 1
        valv.append(a)
        print(valv)
def second_val():
    global valv, fichetas
    if fichetas == []:
        valv2.set_show_text_function(lambda: show_text_on_image(window, "Não sei o que fazer aqui"))
        valv2.draw_text(window)
    else:
        a = 2
        valv.append(a)
        print(valv)
def third_val():
    global valv, fichetas
    if fichetas == []:
        valv3.set_show_text_function(lambda: show_text_on_image(window, "Não sei o que fazer aqui"))
        valv3.draw_text(window)
    else:
        a = 3
        valv.append(a)
        print(valv)

# -----contagens-----
def reset():
    global counting_quiz_lastdoor
    counting_quiz_lastdoor = 0


def quiz_lastdoor_count():
    global counting_quiz_lastdoor
    counting_quiz_lastdoor += 1

def count_invent():
    global area_invent
    area_invent +=1


def count_invent_reverse():
    global area_invent
    area_invent -= 1

def count_first_arm_plus():
    global counting_firstseta_arm, resposta
    if not resposta:
        setacima1.set_show_text_function(lambda: show_text_on_image(window, "Não sei a combinação"))
        setacima1.draw_text(window)
    else:
        counting_firstseta_arm += 1
        if counting_firstseta_arm == 11:
            counting_firstseta_arm = 1

def count_first_arm_minus():
    global counting_firstseta_arm, resposta
    if not resposta:
        setabaixo1.set_show_text_function(lambda: show_text_on_image(window, "Não sei a combinação"))
        setabaixo1.draw_text(window)
    else:
        counting_firstseta_arm -= 1
        if counting_firstseta_arm == 0:
            counting_firstseta_arm = 10

def count_second_arm_plus():
    global counting_secondseta_arm, resposta
    if not resposta:
        setacima2.set_show_text_function(lambda: show_text_on_image(window, "Não sei a combinação"))
        setacima2.draw_text(window)
    else:
        counting_secondseta_arm += 1
        if counting_secondseta_arm == 11:
            counting_secondseta_arm = 1

def count_second_arm_minus():
    global counting_secondseta_arm, resposta
    if not resposta:
        setabaixo2.set_show_text_function(lambda: show_text_on_image(window, "Não sei a combinação"))
        setabaixo2.draw_text(window)
    else:
        counting_secondseta_arm -= 1
        if counting_secondseta_arm == 0:
            counting_secondseta_arm = 10

def first_image():
    if counting_firstseta_arm == 7:
        window.blit(Ag_arm, (250, 400))
    elif counting_firstseta_arm == 9:
        window.blit(Au_arm, (250, 400))
    elif counting_firstseta_arm == 3:
        window.blit(Br_arm, (235, 390))
    elif counting_firstseta_arm == 4:
        window.blit(C_arm, (250, 400))
    elif counting_firstseta_arm == 1:
        window.blit(Ca_arm, (245, 400))
    elif counting_firstseta_arm == 6:
        window.blit(Cl_arm, (250, 400))
    elif counting_firstseta_arm == 2:
        window.blit(Ga_arm, (245, 400))
    elif counting_firstseta_arm == 8:
        window.blit(H_arm, (250, 400))
    elif counting_firstseta_arm == 5:
        window.blit(Hg_arm, (250, 400))
    elif counting_firstseta_arm == 10:
        window.blit(O_arm, (250, 400))

def second_image():
    if counting_secondseta_arm == 7:
        window.blit(Ag_arm, (450, 400))
    elif counting_secondseta_arm == 9:
        window.blit(Au_arm, (450, 400))
    elif counting_secondseta_arm == 3:
        window.blit(Br_arm, (435, 390))
    elif counting_secondseta_arm == 8:
        window.blit(C_arm, (450, 400))
    elif counting_secondseta_arm == 1:
        window.blit(Ca_arm, (445, 400))
    elif counting_secondseta_arm == 4:
        window.blit(Cl_arm, (450, 400))
    elif counting_secondseta_arm == 2:
        window.blit(Ga_arm, (445, 400))
    elif counting_secondseta_arm == 6:
        window.blit(H_arm, (450, 400))
    elif counting_secondseta_arm == 5:
        window.blit(Hg_arm, (450, 400))
    elif counting_secondseta_arm == 10:
        window.blit(O_arm, (450, 400))

def count_arm():
    global counting_firstseta_arm, counting_secondseta_arm, tela_atual, historyy
    if counting_firstseta_arm == 4 and counting_secondseta_arm == 10:
        tela_atual = "arm_open"
    else:
        pass


#-----somee-----

def on_button_click_kleitin():
    global fichetas
    kleitao.hide()
    a = "kleit"
    fichetas.append(a)
    print(fichetas)

def on_button_click_dedin():
    global fichetas
    dedinho.hide()
    a = "dedin"
    fichetas.append(a)
    print(fichetas)

def on_button_click_monstrin():
    global fichetas
    bixinfei.hide()
    a = "bixin"
    fichetas.append(a)
    print(fichetas)

def on_button_click_chip():
    global fichetas
    chipzin.hide()

#-----Variáveis-----

def agua():
    global water, valv
    if valv == [1, 3] or valv == [3, 1]:
        water = True
        counting_quiz_tv = 0
    elif len(valv) == 2:
        valv.clear()

#-----Sons-----

#pygame.mixer.music.load('Audio/trilhadapazduvidosa.mp3')
#pygame.mixer.music.set_volume(0.3)
#pygame.mixer.music.play(-1)


def trilhadastrevass():
    pygame.mixer.music.load('Audio/trilhasonoradastrevas.mp3')
    pygame.mixer.music.set_volume(40)
    pygame.mixer.music.play()


def ghost_breath():
    pygame.mixer.music.load('Audio/ghost_breath.mp3')
    pygame.mixer.music.set_volume(70)
    pygame.mixer.music.play()


def respostacertaa():
    pygame.mixer.music.load('Audio/respostacerta.mp3')
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play()


def respostaerradaa():
    pygame.mixer.music.load('Audio/respostaerrada.mp3')
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play()


def somdaaguaa():
    pygame.mixer.music.load('Audio/águadonegóciodeágua.mp3')
    pygame.mixer.music.set_volume(0.9)
    pygame.mixer.music.play()

def somdavalvulaa():
    pygame.mixer.music.load('Audio/respostacerta.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()


def somdoarmarioo():
    pygame.mixer.music.load('Audio/portadoarmarioabrida.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()


def coisodatemperaturaa():
    pygame.mixer.music.load('Audio/botãodatemp.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()


def somdacartaa():
    pygame.mixer.music.load('Audio/papel.mp3')
    pygame.mixer.music.set_volume(100)
    pygame.mixer.music.play()


def somdacaixadoburacoo():
    pygame.mixer.music.load('Audio/caixadoburaco.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()



def carttrue():
    global cartão_catch
    cartão_catch = True


# Botões

# -----main_menu-----

iniciar_jogo = Button(510, 190, iniciar, iniciar_pressionado, actions=[saladascamas, fade])
vai_pros_cred = Button(510, 390, creditos, creditos_pressionado, actions=[cred, fade])
fecha = Button(510, 590, sair, sair_pressionado, actions=[quita])

# ------ menu middle ------

main_menuu = Button(510, 190, menuinicial, menuinicialpressed, actions=[main_menu, fade])
retomar = Button(510, 390, retomar, retomarpressed, actions=[last_screen, fade])
inventory = Button(510, 590, inventario, inventariopressed, actions=[inventario_tela, fade])

# -----créditos-----

volcred1 = Button(300, 590, voltar_cred, voltar_cred, actions=[main_menu, fade])
volcred2 = Button(300, 590, voltar_cred, voltar_cred, actions=[cred1, fade])
volcred3 = Button(300, 590, voltar_cred, voltar_cred, actions=[cred2, fade])
volcred4 = Button(300, 590, voltar_cred, voltar_cred, actions=[cred3, fade])
volcred5 = Button(300, 590, voltar_cred, voltar_cred, actions=[cred4, fade])
volcred6 = Button(300, 590, voltar_cred, voltar_cred, actions=[cred5, fade])
volcred7 = Button(300, 590, voltar_cred, voltar_cred, actions=[cred6, fade])
volcred8 = Button(300, 590, voltar_cred, voltar_cred, actions=[cred7, fade])

avacred1 = Button(820, 590, avante_cred, avante_cred, actions=[cred2, fade])
avacred2 = Button(820, 590, avante_cred, avante_cred, actions=[cred3, fade])
avacred3 = Button(820, 590, avante_cred, avante_cred, actions=[cred4, fade])
avacred4 = Button(820, 590, avante_cred, avante_cred, actions=[cred5, fade])
avacred5 = Button(820, 590, avante_cred, avante_cred, actions=[cred6, fade])
avacred6 = Button(820, 590, avante_cred, avante_cred, actions=[cred7, fade])
avacred7 = Button(820, 590, avante_cred, avante_cred, actions=[cred8, fade])

# -----Inventário -----

seta_direita_invent = Button(1300, 370, setadireitadoinventario, setadireitadoinventariopressed, actions=[count_invent])
seta_esquerda_invent = Button(100, 370, setaesquerdadoinventario, setaesquerdadoinventariopressionada, actions=[count_invent_reverse])

abrek7 = Button(625, 700, abrir, abrirpressed, actions=[fade, abre])

# -----maps_general-----

left = Button(5, 400, setaesquerdapressed, setaesquerda, actions=[change_telas, fade])
right = Button(1500, 400, setadireitapressed, setadireita, actions=[change_telas_reverse, fade])

# -----sala_camas-----

cama_but = Button(980, 395, cama, cama, actions=[fade, carta, somdacartaa])

# ----- garrafonas -----

garrafonas = Button(50, 0, garrafas, garrafas, actions=[fade, garrafas_ampliadas])
arm = Button(765, 330, armarioo, armarioo, actions=[armario])
escadinha = Button(550, 0, escada, escada, actions=[escada_acima])

#armário

setacima1 = Button(305, 315, setacimaarm, setacimaarmpressed, actions=[count_first_arm_plus])
setacima2 = Button(495, 315, setacimaarm, setacimaarmpressed, actions=[count_second_arm_plus])
setabaixo1 = Button(305, 635, setabaixoarm, setabaixoarmpressed, actions=[count_first_arm_minus])
setabaixo2 = Button(495, 635, setabaixoarm, setabaixoarmpressed, actions=[count_second_arm_minus])

#garrafas_ampliadas

valv1 = Button(320, 450, valvula, valvula, actions=[first_val])
valv2 = Button(770, 450, valvula, valvula, actions=[second_val])
valv3 = Button(1200, 450, valvula, valvula, actions=[third_val])

# -----sala_estante-----

if water == False:
    tv = img_cut("img/tv_apagada.png", 437.5, 282.5)
elif water == True:
    tv = img_cut("img/tv_ligada.png", 437.5, 282.5)

estante_but = Button(1010, 50, estante, estante, actions=[estantee, fade])
porta_estante = Button(35, 95, portaclosed, portaclosed, actions=[fade, portafechabre])
Tv_estante = Button(325, 95, tv, tv, actions=[counting_quizzin, quiz_da_tv, fade_tv])


porta_estante_ab = Button(0, 105, portaopen, portaopen, actions=[fade, mesa])

porta_ld = Button(1200, 95, portalastroom, portalastroom, actions=[fade, saladaTV])

# -----side_estante-----
    #QUIZ
play = Button(450, 550, vai, vai, actions=[opc_tv, fade])

Op1Q1_tv = Button(150, 370, Na, Na, actions=[respostaerradaa, saladaTV, reset_quizzin, fade])
Op2Q1_tv = Button(600, 370, K, K, actions=[respostaerradaa, saladaTV, reset_quizzin, fade])
Op3Q1_tv = Button(1030, 370, Cl, Cl, actions=[respostacertaa, counting_quizzin, quiz_da_tv, fade])

Op1Q2_tv = Button(150, 370, HCl, HCl, actions=[respostaerradaa, saladaTV, reset_quizzin, fade])
Op2Q2_tv = Button(600, 370, C2H2,C2H2 , actions=[respostacertaa, counting_quizzin, quiz_da_tv, fade])
Op3Q2_tv = Button(1030, 370, SO2, SO2, actions=[respostaerradaa, saladaTV, reset_quizzin, fade])

Op1Q3_tv = Button(150, 370, C6H8O7, C6H8O7, actions=[respostaerradaa, saladaTV, reset_quizzin, fade])
Op2Q3_tv = Button(600, 370, C2H5OH, C2H5OH, actions=[respostaerradaa, saladaTV, reset_quizzin, fade])
Op3Q3_tv = Button(1030, 370, MgC12, MgC12, actions=[respostacertaa, counting_quizzin, final_button_quiz_tv, fade, respostaa])

voltar_tv = Button(640, 700, voltar_lastroom, voltar_lastroom_hover, actions=[saladaTV])

    #ESTANTE
caixinha = Button(730, 610, caixa, caixapressed, actions=[CE])
pastaroxa_but = Button(609, 114, pastaroxa, pastaroxapressed, actions=[PR])
pastaverde_but = Button(788, 114, pastaverde, pastaverdepressed, actions=[PV])
    #ampli
return_E = Button(5, 400, setaesquerdapressed, setaesquerda, actions=[return_estante])

#tela_atual = "pastaroxa"/"pastaverde"/"caixa_fora"

proxa = Button(430, 5, pastaroxaampli, pastaroxaampli, actions=[arq1, fade])
pverde = Button(430, 5, pastaverdeampli, pastaverdeampli, actions=[arq1, fade])

caixaa = Button(350, 100, caixaampli, caixaampli, actions=[])

    #Arqui
#tela_atual == "arquivos_estante1"

bixinfei = Button(150, 0, bixinestrain, bixinestrain, actions=[on_button_click_monstrin])
kleitao = Button(500, 0, kleitin, kleitin, actions=[on_button_click_kleitin])
dedinho = Button(800, 0, dedin, dedin, actions=[on_button_click_dedin])

voltar_arqui = Button(5, 400, setaesquerda, setaesquerdapressed, actions=[return_estante])


#-----quiz_lastdoor-----

avante_grey_1 = Button(1350, 700, avante_darkgrey, avante_lightgrey, actions=[fade, quiz_lastdoor_op1])
avante_grey_2 = Button(1350, 700, avante_darkgrey, avante_lightgrey, actions=[fade, quiz_lastdoor_op2])
olhinho = Button(400, 50, olho, olho, actions=[fade, quiz_lastdoor_text1])
voltaa = Button(1200, 100, voltar_lastroom, voltar_lastroom_hover, actions=[fade, quiz_lastdoor])

Op1_q1_ld = Button(200, 300, Op1q1_ld, Op1q1_ld, actions=[respostacertaa, fade, quiz_lastdoor_text2, quiz_lastdoor_count])
Op2_q1_ld = Button(600, 300, Op2q1_ld, Op2q1_ld, actions=[respostaerradaa, fade, reset, lost_lastdoor])
Op3_q1_ld = Button(1000, 300, Op3q1_ld, Op3q1_ld, actions=[respostaerradaa, fade, reset, lost_lastdoor])
Op1_q2_ld = Button(200, 300, Op1q2_ld, Op1q2_ld, actions=[respostaerradaa, fade, reset, lost_lastdoor])
Op2_q2_ld = Button(600, 300, Op2q2_ld, Op2q2_ld, actions=[respostaerradaa, fade, reset, lost_lastdoor])
Op3_q2_ld = Button(1000, 300, Op3q2_ld, Op3q2_ld, actions=[respostacertaa, fade, quiz_lastdoor_count])
##
Op1_q3_ld = Button(200, 300, Op1q2_ld, Op1q2_ld, actions=[respostaerradaa, fade ,reset, lost_lastdoor])
Op2_q3_ld = Button(600, 300, Op2q2_ld, Op2q2_ld, actions=[respostaerradaa, fade, reset, lost_lastdoor])
Op3_q3_ld = Button(1000, 300, Op3q2_ld, Op3q2_ld, actions=[respostacertaa, fade, quiz_lastdoor_count])


# -----"Covalentes" -----

Cbutton = Button(820, 320, C, Cpressed, actions=[first])
Obutton = Button(1080, 320, O, Opressed, actions=[second])
Vbutton = Button(690, 320, V, Vpressed, actions=[third])
Abutton = Button(1340, 320, A, Apressed, actions=[fourth])
Lbutton = Button(300, 320, L, Lpressed, actions=[fifth])
E1button = Button(950, 320, E, Epressed, actions=[sixth])
Nbutton = Button(560, 320, N, Npressed, actions=[seventh])
Tbutton = Button(430, 320, T, Tpressed, actions=[eighth])
E2button = Button(1210, 320, E, Epressed, actions=[nineth])
Sbutton = Button(170, 320, S, Spressed, actions=[tenth])

# ---- sala do pc ----

pc_button = Button(-36, 277, pc, pc, actions=[fade, sala_da_senha1])
temperatura_cinza = Button(550, 100, graucinza, graucinza, actions=[temperatura, fade])
ir_pra_caixa = Button(450, 400, caixa_lastroom_png, caixa_lastroom_png,
                      actions=[qual_caixa])

# eye box tela red machine


def red_machine_error():
    red_machine.set_show_text_function(
        lambda: show_text_on_image(window, "Isso deveria ligar...?"))
    red_machine.draw_text(window)


red_machine = Button(700, 150, red_machine_png, red_machine_png, actions=[red_machine_error])

# eye box green machine

green_machine = Button(700, 150, green_machine_png, green_machine_png, actions=[quiz_lastdoor])

# --- tela pc ---

x_button = Button(355, 508, x, x, actions=[telaPCaviso])
machine_on = False
# --- tela pc aviso ---


def def_machine_on():
    global machine_on
    machine_on = True


aviso = Button(400, 200, aviso, aviso, actions=None)
cancelar = Button(860, 635, cancelar, cancelar, actions=[def_machine_on, ghost_breath])
esquecer = Button(440, 635, esquecer, esquecer, actions=[telaPC])

#-----temp-----
leftgrau = Button(980, 443, setadireitagrau, setadireitagraupressed, actions=[delete_temp])
rightgrau = Button(1200, 443, setaesquerdagrau, setaesquerdagraupressed, actions=[add_temp])


#aaa sla

chipzin = Button(855, 475, chip, chip, actions=[carttrue,  on_button_click_chip])

#bulindo com drag and drop

#---invent---
image1 = img_cut("img/fichinhadoKleitin.png", 554,700)
image2 = img_cut("img/bixinestranho.png", 554, 700)
image3 = img_cut("img/dedindocão.png", 554, 700)
image4 = img_cut("img/resposta_garrafa.png", 554, 700)
image5 = img_cut("img/resposta_senhapc.png", 554, 700)

images1 = [image4, image5, image3]  # Lista de imagens para os três objetos
images2 = [image1, image2, image3]
current_images = [image1, image2, image3]  # Lista das imagens atuais para os três objetos

image_rects = [
    pygame.Rect(10, 10, image1.get_width(), image1.get_height()),  # Canto superior esquerdo
    pygame.Rect(X - image2.get_width() - 10, 10, image2.get_width(), image2.get_height()),  # Canto superior direito
    pygame.Rect(400, Y - image3.get_height() - 1, image3.get_width(), image3.get_height())  # Canto inferior esquerdo
]

dragging = [False, False, False]
offsets = [(0, 0) for _ in range(3)]

changing_image = [None, None, None, None, None]


image_chip = chipampli

image_rect_chip = image_chip.get_rect(topleft=(900, 600))

drop_area = pygame.Rect(710, 60, 350, 360)
dragging_chip = False
offset_x, offset_y = 0, 0

transparent_surface = pygame.Surface((image_rect_chip.width, image_rect_chip.height), pygame.SRCALPHA)

# bulindo com texto

text = [""]
TEXT_COLOR = (255, 255, 255)
font_size = 60
font_name = "arialblack"
font = pygame.font.SysFont(font_name, font_size)


def draw_text(text, font, color, x, y):
    for i, line in enumerate(text):
        img = font.render(line, True, color)
#        width = img.get_width()
        window.blit(img, (x, y + i * font_size))

# TELA FINAL BITCHES

star = Button(1000, 200, star_png, star_png, actions=[divaga])


# definir botões
botoes = {
    "main_menu": [iniciar_jogo, vai_pros_cred, fecha],
    "menu_middle": [main_menuu, retomar, inventory],
    "inventário": [seta_direita_invent, seta_esquerda_invent, abrek7],
    "camas": [left, cama_but],
    "senha1": [left],
    "covalentes": [Cbutton, Obutton, Vbutton, Abutton, Lbutton, E1button, Nbutton, Tbutton, E2button, Sbutton],
    "carta": [left],
    "garrafonas": [left, right, garrafonas, arm, escadinha],
    "armario": [left, setacima1, setacima2, setabaixo1, setabaixo2],
    "garrafonas_ampliadas": [left, valv1, valv2, valv3],
    "saladatv": [estante_but, right, Tv_estante, porta_estante],
    "saladatv_portaberta": [estante_but, right, Tv_estante, porta_estante_ab],
    "quiz_tv": [play],
    "Op1_tv": [Op1Q1_tv, Op2Q1_tv, Op3Q1_tv],
    "Op2_tv": [Op1Q2_tv, Op2Q2_tv, Op3Q2_tv],
    "Op3_tv": [Op1Q3_tv, Op2Q3_tv, Op3Q3_tv],
    "resposta_tv": [voltar_tv],
    "estante": [left, caixinha, pastaroxa_but, pastaverde_but],
    "pastaroxa": [proxa, return_E],
    "pastaverde": [pverde, return_E],
    "caixa_fora": [caixaa, return_E],
    "arquivos_estante1": [dedinho, bixinfei, voltar_arqui],
    "arquivos_estante2": [kleitao, voltar_arqui],
    "quiz_lastdoor": [olhinho],
    "questions_lastdoor1": [avante_grey_1],
    "questions_lastdoor2": [avante_grey_2],
    "op_lastdoor1": [Op1_q1_ld, Op2_q1_ld, Op3_q1_ld],
    "op_lastdoor2": [Op1_q2_ld, Op2_q2_ld, Op3_q2_ld],
    "You've_lost": [voltaa],
    "mesa": [pc_button, temperatura_cinza, ir_pra_caixa, porta_ld],
    "temp": [leftgrau, rightgrau],
    "pc_tela_inicial": [x_button, left],
    "pc_aviso": [aviso, cancelar, esquecer],
    "red_caixa": [red_machine, left],
    "green_caixa": [green_machine, left],
    "invent_arq": [],
    "porta": [left],
    "arm_open": [chipzin, left],
    "cred1": [volcred1, avacred1],
    "cred2": [volcred2, avacred2],
    "cred3": [volcred3, avacred3],
    "cred4": [volcred4, avacred4],
    "cred5": [volcred5, avacred5],
    "cred6": [volcred6, avacred6],
    "cred7": [volcred7, avacred7],
    "cred8": [volcred8],
    "divagar_final": [star]
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Verifique os cliques na tela atual
                for botao in botoes.get(tela_atual, []):
                    botao.check_click()

                if tela_atual == "invent_arq":
                    for i, img_rect in enumerate(image_rects):
                            if img_rect.collidepoint(event.pos):
                                dragging[i] = True
                                mouse_x, mouse_y = event.pos
                                offsets[i] = img_rect.x - mouse_x, img_rect.y - mouse_y
                                if current_images[i] in [image1, image2, image3]:
                                    changing_image = current_images[i]
                                elif current_images[i] in [image4, image2, image3]:
                                    changing_image = current_images[i]
                                elif current_images[i] in [image1, image2, image5]:
                                    changing_image = current_images[i]
                                elif current_images[i] in [image4, image2, image5]:
                                    changing_image = current_images[i]
                elif tela_atual == "porta":
                    if image_rect_chip.collidepoint(event.pos):
                        dragging_chip = True
                        offset_x = event.pos[0] - image_rect_chip.x
                        offset_y = event.pos[1] - image_rect_chip.y
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if tela_atual == "invent_arq":
                    for i, img_rect in enumerate(image_rects):
                        if dragging[i]:
                            dragging[i] = False
                            if changing_image == current_images[i]:
                                # Lógica para mudar a imagem específica
                                if changing_image == image1:
                                    current_images[i] = image4
                                    changing_image = image4
                                elif changing_image == image2:
                                    current_images[i] = image2
                                elif changing_image == image3:
                                    current_images[i] = image5
                                    changing_image = image5
                                elif current_images[i] == image4:
                                    current_images[i] = image1
                                    changing_image = image1
                                elif current_images[i] == image5:
                                    current_images[i] = image3
                                    changing_image = image3
                elif tela_atual == "porta":
                    dragging_chip = False
                    if drop_area.collidepoint(event.pos):
                        portaaberta = True
        elif event.type == pygame.MOUSEMOTION:
            if tela_atual == "invent_arq":
                for i, img_rect in enumerate(image_rects):
                    if dragging[i]:
                        mouse_x, mouse_y = event.pos
                        img_rect.x = mouse_x + offsets[i][0]
                        img_rect.y = mouse_y + offsets[i][1]
            elif tela_atual == "porta":
                if dragging_chip:
                    mouse_x, mouse_y = event.pos
                    image_rect_chip.x = mouse_x - offset_x
                    image_rect_chip.y = mouse_y - offset_y

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and tela_atual != "main_menu" and tela_atual != "menu_middle" and tela_atual != "créditos":
                tela_atual = "menu_middle"
        if event.type == pygame.TEXTINPUT and tela_atual == "senha1":
            text[-1] += event.text
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text[-1] = text[-1][:-1]
                if len(text[-1]) == 0 and len(text) > 1:
                    text = text[:-1]
            if event.key == pygame.K_RETURN and "Cadeia_de_Carbono" in text:
                text = [""]
                tela_atual = "pc_tela_inicial"

    # menus
    if tela_atual == "main_menu":
        window.fill((255, 255, 255))
        fundo(home)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "menu_middle":
        fundo(fundo_middlemenu)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred1":
        fundo(cre1)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred2":
        fundo(cre2)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred3":
        fundo(cre3)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred4":
        fundo(cre4)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred5":
        fundo(cre5)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred6":
        fundo(cre6)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred7":
        fundo(cre7)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "cred8":
        fundo(cre8)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "divagar_final":
        fundo(divagar)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "inventário":
        fundo(inventario_screen)
        if area_invent == 1:
            if set(fichetas) == fichetas_checktotal:
                window.blit(trêsjuntos, (530, 200))
            elif set(fichetas) == fichetas_check1:
                window.blit(bixinededin, (530, 200))
            elif set(fichetas) == fichetas_check2:
                window.blit(bixinekleitin, (530, 200))
            elif set(fichetas) == fichetas_check3:
                window.blit(kleitinededin, (530, 200))
        elif area_invent == 2:
            if cartão_catch == True:
                window.blit(chipampli, (500, 250))
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "invent_arq":
        window.fill("DimGrey")
        for i, img_rect in enumerate(image_rects):
            window.blit(current_images[i], img_rect)
    #salas
    elif tela_atual == "camas":
        fundo(sala_das_camas)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "pc_tela_inicial":
        fundo(tela_do_pc)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "pc_aviso":
        fundo(tela_do_pc)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "senha1":
        fundo(puzzlesenha)
        draw_text(text, font, TEXT_COLOR, 300, 450)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
            for event in pygame.event.get():
                if event.type == pygame.TEXTINPUT:
                    text[-1] += event.text
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        text[-1] = text[-1][:-1]
                        if len(text[-1]) == 0 and len(text) > 1:
                            text = text[:-1]
                    if event.key == pygame.K_RETURN and "Cadeia_de_Carbono" in text:
                        tela_atual = "pc_tela_inicial"
    elif tela_atual == "garrafonas":
        fundo(fundo_geral)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "armario":
        fundo(armarioclosed)
        first_image()
        second_image()
        count_arm()
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "arm_open":
        fundo(armarioopen)
        window.blit(O_arm, (450, 400))
        window.blit(C_arm, (250, 400))
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "garrafonas_ampliadas":
        fundo(fundopuzzlegarrafa)
        agua()
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "saladatv":
        fundo(fundosaladatvnowater)
        if water == True:
            fundo(fundosaladatv)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
        if water == True:
            window.blit(tvligada, (325, 95))

    elif tela_atual == "saladatv_portaberta":
        fundo(fundosaladatvnowater)
        if water == True:
            fundo(fundosaladatv)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
        if water == True:
            window.blit(tvligada, (325, 95))

    elif tela_atual == "porta":
        if portaaberta == False:
            fundo(porta_vermelho)
        elif portaaberta == True:
            fundo(porta_verde)
        if cartão == True:
            pygame.draw.rect(window, (125, 125, 125), drop_area, 2)
            window.blit(chipampli, image_rect_chip)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "mesa":
        fundo(fundo_geral)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "red_caixa":
        fundo(eye_box_tela)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "green_caixa":
        fundo(eye_box_tela)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "temp":
        window.fill((150, 147, 147))
        if grau == 1:
            window.blit(grau1, (150, 180))
        elif grau == 2:
            window.blit(grau2, (150, 180))
        elif grau == 3:
            window.blit(grau3, (150, 180))
        elif grau == 4:
            window.blit(grau4, (150, 180))
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    #sides: sala1
    elif tela_atual == "carta":
        fundo(tela_carta)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "covalentes":

        if rightcomb == False:
            fundo(Comb_wrong)
        elif rightcomb == True:
            fundo(Comb_right)
        if comb == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            rightcomb = True
            tela_atual = "garrafonas"
            historyy.append(tela_atual)
        elif comb != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and len(comb) == 10:
            comb.clear()
        else:
            pass

        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    #sides: sala3
    elif tela_atual == "estante":
        fundo(estanteampli)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "quiz_tv":
        fundo(telaquiz)
        change_perguntinha()
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "Op1_tv":
        fundo(telaquiz)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "Op2_tv":
        fundo(telaquiz)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "Op3_tv":
        fundo(telaquiz)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "resposta_tv":
        fundo(telaquiz)
        window.blit(MDC, (0, 0))
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "pastaroxa":
        fundo(estanteampli)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "pastaverde":
        fundo(estanteampli)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "caixa_fora":
        fundo(estanteampli)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "arquivos_estante1":
        window.fill("DimGray")
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "arquivos_estante2":
        window.fill("DimGray")
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    #quiz_lastdoor
    elif tela_atual == "quiz_lastdoor":
        fundo(quiz_lastroom_inic)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "questions_lastdoor1":
        fundo(quiz_lastroom)
        window.blit(Q1_ld, (70, 550))
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "questions_lastdoor2":
        fundo(quiz_lastroom)
        window.blit(Q2_ld, (70, 580))
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "op_lastdoor1":
        fundo(quiz_lastroom_inic)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "op_lastdoor2":
        fundo(quiz_lastroom_inic)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    elif tela_atual == "You've_lost":
        fundo(lost_ld)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    pygame.display.update()
