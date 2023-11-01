import pygame
import os
import sys


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

    def draw(self, screen):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.image_hover, (self.x, self.y))
        else:
            screen.blit(self.image_normal, (self.x, self.y))

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            for action in self.actions:
                action()


def img(img):
    a = pygame.image.load(img).convert_alpha()
    return a


def img_cut(img, x, y):
    a = pygame.image.load(img).convert_alpha()
    a = pygame.transform.scale(a, (x, y))
    return a


pygame.init()

# Configurações da tela
window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Outside")

# sons

# sons


# imagens


# ----fundos----

home = img_cut("img/fundo_inicial.png", 1600, 900)
credits_background = img_cut("img/fundo_dos_créditos.png", 1600, 900)
fundo_geral = img_cut("img/fundo.png", 1600, 900)
fundopuzzlegarrafa = img_cut("img/Fundo_puzzlegarrafa.png", 1600, 900)
fundosaladatv = img_cut("img/fundo_salaTv_water.png", 1600, 900)
fundosaladatvnowater = img_cut("img/fundo_salaTv_nowater.png", 1600, 900)
estanteampli = img_cut("img/Estanteampli.png", 1600, 900)
fundo_middlemenu = img_cut("img/FundinhoMiddleMenu.png", 1600, 900)
graucinza = img_cut("img/grau_cinza.png", 300, 300)
grauaberto = img_cut("img/grau_aberto.png", 300, 300)
telaquiz = img_cut("img/Telaquiz.png", 1600, 900)
sala_das_camas = img_cut("img/sala1_camas.png", 1600, 900)
Q1 = img_cut("img/Q1.png", 1600, 900)
Q2 = img_cut("img/Q2.png", 1600, 900)
Q3 = img_cut("img/Q3.png", 1600, 900)
puzzle1recado1 = img_cut("img/puzzle1_recado1.png", 1600, 900)
puzzlesenha = img_cut("img/puzzle_senha.png", 1600, 900)
sala2pt2 = img_cut("img/Sala2pt2.png", 1600, 900)

quiz_lastroom_inic = img_cut("img/Fundo_iniciar_lastdoor.png", 1600, 900)
quiz_lastroom = img_cut("img/Fundo_questions_lastdoor.png", 1600, 900)

lost_ld = img_cut("img/Youlost.png", 1600, 900)

tela_carta = img_cut("img/carta.jpg", 1600, 900)

# ----elementos_salas----

Q1_ld = img("img/Q1_lastdoor.png")
Q2_ld = img("img/Q2_lastdoor.png")

# ----Botões----


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
armarioclosed = img("img/armario_closed.png")
armarioopen = img("img/armario_open.png")
caixa = img("img/caixa.png")
caixapressed = img("img/caixapressed.png")
seta = img("img/seta.png")
setaesquerda, setaesquerdapressed = img_cut("img/seta_esquerda.png", 100, 100),  img_cut("img/seta_esquerda_pressed.png", 100, 100)
setaesquerdadoinventario = img("img/seta esquerda do inventário.png")
setaesquerdadoinventariopressionada = img("img/seta do inventário pressionada e esquerda.png")
setadireitadoinventario = img("img/seta direita do inventário.png")
setadireitadoinventariopressed = img("img/seta do inventário pressionada e direita.png")
setadireita = img("img/seta cinza direita.png")
setadireitapressed = img("img/seta cinza direita pressionada.png")
tv = img("img/Tv.png")
tvligada = img("img/tv_ligada.png")
hiddenbutton = img("img/hidden_button.png")
valvula = img("img/Botão_valvula.png")
botaopc = img("img/botao_pc.png")
balaoescuro = img("img/balão_escuro.png")
ativado = img("img/ativado.png")
caixotes = img("img/caixotes.png")
abrir = img("img/abrir.png")
abrirpressed = img("img/abrir_pressed.png")
usar = img("img/usar.png")
usarpressed = img("img/usar_hover.png")
vai = img("img/vai.png")
K = img("img/K.png")
MDC = img("img/MDC.png")
C2H2 = img("img/C2H2.png")
C2H5OH = img("img/C2H5OH.png")
MgC12 = img("img/MgCl2.png")
C6H8O7 = img("img/C6H8O7.png")
SO2 = img("img/SO2.png")
HCl = img("img/HCl.png")
Na = img("img/Na.png")
Cl = img("img/Cl.png")

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

# ----elementos_salas----

cama = img_cut("img/Cama.png", 455, 340)
escada = img_cut("img/escada.png", 680, 300)
estante = img_cut("img/estante.png", 1000, 400)
armario = img_cut("img/armario.png", 450, 260)
buraco = img_cut("img/buraco.png", 728, 385)
garrafas = img_cut("img/garrafas.png", 380, 300)
pau = img_cut("img/pau.png", 130, 7)
chip = img_cut("img/chip.png", 58, 40)
pastaroxa = img_cut("img/pastaroxa.png", 100, 215)
pastaroxaampli = img_cut("img/pastaroxaampli.png", 678, 900)
pastaroxapressed = img_cut("img/pastaroxapressed.png", 100, 215)
pastaverde = img_cut("img/pastaverde.png", 100, 215)
pastaverdeampli = img_cut("img/Pastaverdeampli.png", 678, 900)
pastaverdepressed = img_cut("img/pastaverdepressed.png", 100, 215)
caixalastroom = img("img/caixa_lastroom.png")
caixalastroomopen = img("img/caixa_lastroom_open_active.png")
caixalastroomnoactive = img("img/caixa_lastroom_open_notactive.png")
portaclosed = img("img/porta_closed.png")
portalastroom = img("img/porta_lastroom.png")
portaopen = img("img/porta_open.png")
grau1 = img_cut("img/grau1.png", 700, 280)
grau2 = img_cut("img/grau2.png", 700, 280)
grau3 = img_cut("img/grau3.png", 700, 280)
grau4 = img_cut("img/grau4.png", 700, 280)
chave = img_cut("img/chave.png", 150, 125)

# ----Cenas_puzzles----


# ----Quizzes----


# variáveis
tela_atual = "main_menu"

water = False

Q1_lastd = False
Q2_lastd = False

counting_quiz_lastdoor = 0


# defs

def fundo(img):
    window.blit(img, (0, 0))


def quit():
    global running
    pygame.quit()
    quit()
    running = False


# -----tela ativa-----

def go_left():
    global tela_atual
    if tela_atual == "camas":
        tela_atual = "garrafonas"
    elif tela_atual == "garrafonas":
        tela_atual = "saladatv"
    elif tela_atual == "saladatv":
        tela_atual = "mesa"


def go_right():
    global tela_atual
    if tela_atual == "garrafonas":
        tela_atual = "camas"
    elif tela_atual == "saladatv":
        tela_atual = "garrafonas"
    elif tela_atual == "mesa":
        tela_atual = "saladatv"


def main_menu():
    global tela_atual
    tela_atual = "main_menu"


def cred():
    global tela_atual
    tela_atual = "créditos"


def saladascamas():
    global tela_atual
    tela_atual = "camas"


def saladasgarrafonas():
    global tela_atual
    tela_atual = "garrafonas"


def saladaTV():
    global tela_atual
    tela_atual = "saladatv"


def estante():
    global tela_atual
    tela_atual = "estante"


def mesa():
    global tela_atual
    tela_atual = "mesa"


def carta():
    global tela_atual
    tela_atual = "carta"


def valvula():
    global tela_atual
    tela_atual = "valvula"


def armario():
    global tela_atual
    tela_atual = "armario"


def escada_acima():
    global tela_atual
    tela_atual = "escada_acima"


def middle_menu():
    global tela_atual
    tela_atual = "menu_middle"


def inventario():
    global tela_atual
    tela_atual = "inventário"


def quiz_tv():
    global tela_atual
    tela_atual = "quiztv"


def caixa_lastdoor():
    global tela_atual
    tela_atual = "caixa"


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


# -----contagens-----
def reset():
    global counting_quiz_lastdoor
    counting_quiz_lastdoor = 0


def quiz_lastdoor_count():
    global counting_quiz_lastdoor
    counting_quiz_lastdoor += 1
    print(counting_quiz_lastdoor)

#-----Variáveis-----

def agua():
    global water
    if water == False:
        water = True
    elif water == True:
        water = False

# Botões

#-----main_menu-----

iniciar_jogo = Button(530, 190, iniciar, iniciar_pressionado, actions=[saladascamas])
vai_pros_cred = Button(530, 390, creditos, creditos_pressionado, actions=[cred])
fecha = Button(530, 590, sair, sair_pressionado, actions=[quit])

#-----créditos-----

pink_back_button = Button(1500, 800, back, back_pressed, actions=[main_menu])

# -----maps_general-----

left = Button(110, 500, setaesquerdapressed, setaesquerda, actions=[go_left])

#-----sala_camas-----

cama = Button(1050, 430, cama, cama, actions=[carta])

#-----quiz_lastdoor-----

avante_grey_1 = Button(1350, 700, avante_darkgrey, avante_lightgrey, actions=[quiz_lastdoor_op1])

avante_grey_2 = Button(1350, 700, avante_darkgrey, avante_lightgrey, actions=[quiz_lastdoor_op2])

olhinho = Button(400, 50, olho, olho, actions=[quiz_lastdoor_text1])

Op1_q1_ld = Button(200, 300, Op1q1_ld, Op1q1_ld, actions=[quiz_lastdoor_text2, quiz_lastdoor_count])
Op2_q1_ld = Button(600, 300, Op2q1_ld, Op2q1_ld, actions=[reset, lost_lastdoor])
Op3_q1_ld = Button(1000, 300, Op3q1_ld, Op3q1_ld, actions=[reset, lost_lastdoor])

Op1_q2_ld = Button(200, 300, Op1q2_ld, Op1q2_ld, actions=[reset, lost_lastdoor])
Op2_q2_ld = Button(600, 300, Op2q2_ld, Op2q2_ld, actions=[reset, lost_lastdoor])
Op3_q2_ld = Button(1000, 300, Op3q2_ld, Op3q2_ld, actions=[quiz_lastdoor_count, quit])

voltaa = Button(1200, 100, voltar_lastroom, voltar_lastroom_hover, actions=[quiz_lastdoor])

# definir botões
botoes = {
    "main_menu": [iniciar_jogo, vai_pros_cred, fecha],
    "créditos":  [pink_back_button],
    "camas": [left, cama],
    "garrafonas": [left],
    "saladatv": [left],
    "quiz_lastdoor": [olhinho],
    "questions_lastdoor1": [avante_grey_1],
    "questions_lastdoor2": [avante_grey_2],
    "op_lastdoor1": [Op1_q1_ld, Op2_q1_ld, Op3_q1_ld],
    "op_lastdoor2": [Op1_q2_ld, Op2_q2_ld, Op3_q2_ld],
    "You've_lost": [voltaa]
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Verifique os cliques na tela atual
                for botao in botoes.get(tela_atual, []):
                    botao.check_click()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and tela_atual != "main menu" and tela_atual != "menu_middle" and tela_atual != "créditos":
                tela_atual = "menu_middle"

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
    elif tela_atual == "créditos":
        fundo(credits_background)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    #salas
    elif tela_atual == "camas":
        fundo(sala_das_camas)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "garrafonas":
        fundo(fundo_geral)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "saladatv":
        if water == False:
            fundo(fundosaladatvnowater)
        elif water == True:
            fundo(fundosaladatv)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)
    elif tela_atual == "mesa":
        fundo(sala2pt2)
        for botao in botoes.get(tela_atual, []):
            botao.draw(window)

    #sides: sala1
    elif tela_atual == "carta":
        fundo(tela_carta)

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
