import pygame
import os
import sys

pygame.init()
x,y = 1600, 900



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


#sons

trilhadapaz = pygame.mixer.music.load('trilhadapazduvidosa.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

armariosound = pygame.mixer.music.load('portadoarmarioabrida.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

coisodatemperatura = pygame.mixer.music.load('botãodatemp.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

caixadoburaco = pygame.mixer.music.load('caixadoburaco.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

somdacarta = pygame.mixer.music.load('papel.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

respostacerta = pygame.mixer.music.load('respostacerta.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

respostaerrada = pygame.mixer.music.load('respostaerrada.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

trilhadastrevas = pygame.mixer.music.load('trilhasonoradastrevas.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

somdavalvula = pygame.mixer.music.load('valvulasound.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

somdaagua = pygame.mixer.music.load('águadonegóciodeágua.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

click_sound = pygame.mixer.Sound('mouse-click-153941.mp3')


#----fundos----

home = img_cut("img/fundo_inicial.png", 1600, 900)
credits_background = img_cut("img/fundo_dos_créditos.png", 1600, 900)
fundopuzzlegarrafa = img_cut("img/Fundo_puzzlegarrafa.png", 1600, 900)
fundosaladatv = img_cut("img/fundo_salaTv_water.png")
fundosaladatvnowater = img_cut("img/fundo_salaTv_nowater.png")
estanteampli = img_cut("img/Estanteampli.png")
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
bixinestrain = img_cut("bixinestranho.png", 600, 800)
dedindocao = img_cut("dedindocão.png", 600, 800)
fichakleitin = img_cut("fichinhadoKleitin.png", 600, 800)
carta = img_cut("carta.jpg", 1600, 900)

#----elementos_salas----
escada = img_cut("img/escada.png", 680, 300)
estante = img_cut("img/estante.png", 1000, 400)
armario = img_cut("img/armario.png", 450, 260)
buraco = img_cut("img/buraco.png", 728, 385)
garrafas = img_cut("img/garrafas.png",380, 300 )
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
caixalastroomnoactive = img("img/caixa_lastroom_open_noactive.png")
portaclosed = img("img/porta_closed.png")
portalastroom = img("img/porta_lastroom.png")
portaopen = img("img/porta_open.png")
grau1 = img_cut("grau1.png", 700, 280)
grau2 = img_cut("grau2.png", 700, 280)
grau3 = img_cut("grau3.png", 700, 280)
grau4 = img_cut("grau4.png", 700, 280)
chave = img_cut("chave.png", 150, 125)

#----Botões----

forpc = img("img/botao_pc.png")
iniciar = img("img/iniciar.png")
iniciar_pressionado = img("img/iniciar_pressionado.png")
creditos = img("img/créditos.png")
creditos_pressionado = img("img/créditos_pressionado.png")
sair = img("img/sair.png")
sair_pressionado = img("img/sair_pressionado.png")
retomar = img("img/Menu_middle_1.png")
retomarpressed = img("img/Menu_middle_pressed1.png")
inventario = img("img/Menu_middle2.png")
inventariopressed = img("Menu_middle_pressed2.png")
menuinicial = img("img/Menu_middle_3")
menuinicialpressed = img("img/Menu_middle_pressed3")
armarioclosed = img("img/armario_closed.png")
armarioopen = img("img/armario_open.png")
caixa = img("img/caixa.png")
caixapressed = img("img/caixapressed.png")
seta = img("img/seta.png")
setaesquerda = img("img/seta_esquerda.png")
setaesquerdapressed = img("img/seta_esquerda_pressed.png")
setaesquerdadoinventario = img("img/seta esquerda do inventário.png")
setaesquerdadoinventariopressionada = img("img/seta do inventário pressionada e esquerda.png")
setadireitadoinventario = img("img/seta direita do inventário.png")
setadireitadoinventariopressed = img("img/seta do inventario pressionada e direita.png")
setadireita = img("setacinzadireita.png")
setadireitapressed = img("img/seta cinza direita pressionada.png")
tv = img("img/Tv.png")
tvligada = img("img/tv_ligada.png")
hiddenbutton = img("img/hidden_button.png")
valvula = img("img/Botão_valvula.png")
botaopc = img("img/botao_pc.png")
balaoescuro = img("img/balão_escuro.png")
ativado = img("img/ativado.png")
caixotes = img("img/caixotes.png")
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

#----Cenas_puzzles----



#----Quizzes----

#variaveis
tela_atual = "main_menu"



#defs

def fundo(img):
    window.blit(img, (0, 0))

def tela_inicial(img):
    global tela_atual
    tela_atual = "main_menu"


#Botões

Button(200, 300, )


running = True
while running:
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    pygame.display.update()







