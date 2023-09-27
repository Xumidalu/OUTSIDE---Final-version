import pygame
import os

pygame.init()

x, y = 1600, 900

WHITE = (255, 255, 255)

window = pygame.display.set_mode([x, y])
pygame.display.set_caption("PerfGens")

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


class Quizzz():
    def __init__(self):
        window.blit(telaquiz, (0, 0))
        window.blit(Q1, (0,0))
        window.blit(Q2, (0, 0))
        window.blit(Q3, (0,0))
        window.blit(MDC, (0,0))
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
                    pygame.quit()
                    quit()
            elif self.Q2 == True:
                if self.Hcl.check_click():
                    pygame.quit()
                    quit()
                elif self.SO2.check_click():
                    pygame.quit()
                    quit()
                elif self.C2H2.check_click():
                    self.Q2 = False
                    self.comc = True
                    self.Q3 = True
            elif self.Q3 == True:
                if self.MgCl2.check_click():
                    self.Q3 = False
                    self.resp = True
                elif self.C2H5OH.check_click() or self.C6H8O7.check_click():
                    pygame.quit()
                    quit()

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









quizuu = Quizzz()
tela_atual = "quiz"


run = True
while run:
    if tela_atual == "quiz":
        tela_atual = quizuu.handle_events()
        quizuu.update()

    pygame.display.flip()




