import pygame
from img_functions import img, img_cut
from button import Button
pygame.init()
x, y = 1600, 900
window = pygame.display.set_mode([x, y])
pygame.display.set_caption("PerfGens")

# elementos globais
voltar, voltar_h = img_cut("seta_esquerda.png", 100, 100), img_cut("seta_esquerda_pressed.png", 100, 100)
back_button = Button(1500, 800, voltar, voltar_h)
# tela inicial
home = img_cut("fundo_inicial.png", 1600, 900)
start_, start_pressed = img("iniciar.png"), img("iniciar_pressionado.png")
credits_, credits_pressed = img("créditos.png"), img("créditos_pressionado.png")
exit_, exit_pressed = img("sair.png"), img("sair_pressionado.png")
init_button = Button(790, 255, start_, start_pressed)
cred_button = Button(790, 455, credits_, credits_pressed)
exit_button = Button(790, 655, exit_, exit_pressed)
# salas das camas
camas = img_cut("cama_fundo.png", 1600, 900)
tapa = img("tapa_buraco.png")
cama0 = img("cama.png")
portal0 = img("portal.png")
tapa_buraco = Button(790, 250, tapa, tapa)
cama = Button(1200, 600, cama0, cama0)
portal = Button(790, 700, portal0, portal0)
# sala dos créditos
cred = img_cut("fundo_dos_créditos.png", 1600, 900)
# sala das camas de cabeça para baixo
camas2 = img_cut("cama_fundo_W.png", 1600, 900)
cama0_W = img("cama_W.png")
cama_W = Button(300, 300, cama0_W, cama0_W)
# carta
carta = img_cut("carta.jpg", 1600, 900)
# sala oculta
oculto = img_cut("oculto.png", 1600, 900)
homem0 = img("homem.png")
homem = Button(1100, 400, homem0, homem0)
oculta = pygame.mixer.Sound('trilhasonoradastrevas.mp3')
oculta.set_volume(0.5)
#
abc = 0
tela_atual = home
run = True
while run:
    window.blit(tela_atual, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    # variando
    if tela_atual == home:
        init_button.draw()
        cred_button.draw()
        exit_button.draw()
        if init_button.check_click():
            tela_atual = camas
        if cred_button.check_click():
            tela_atual = cred
        if exit_button.check_click():
            run = False
    if tela_atual == cred:
        back_button.draw()
        if back_button.check_click():
            tela_atual = home
    if tela_atual == camas:
        tapa_buraco.draw()
        cama.draw()
        back_button.draw()
        if back_button.check_click():
            tela_atual = home
        if cama.check_click():
            tela_atual = carta
        if tapa_buraco.check_click():
            tapa_buraco.bye_bye()
            for e in range(1, 10000):
                if e == 9999:
                    tela_atual = camas2
                print(e)

    if tela_atual == camas2:
        cama_W.draw()
        portal.draw()
        if portal.check_click():
            tela_atual = oculto

    if tela_atual == carta:
        back_button.draw()
        if back_button.check_click():
            tela_atual = camas
    if tela_atual == oculto:
        oculta.play()
        homem.draw()
        back_button.draw()
        if back_button.check_click():
            oculta.stop()
            tela_atual = camas
        if homem.check_click():
            pass

    pygame.display.update()
