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
# b_init_pink = pygame.transform.scale(b_init_pink, (600, 150))
start_pressed = pygame.image.load(os.path.join(dir_img, "beige_start_button.png")).convert_alpha()
# b_init_lilac = pygame.transform.scale(b_init_lilac, (600, 150))

credits_ = pygame.image.load(os.path.join(dir_img, "brown_credits_button.png")).convert_alpha()
# b_cred_pink = pygame.transform.scale(b_cred_pink, (600, 150))
credits_pressed = pygame.image.load(os.path.join(dir_img, "beige_credits_button.png")).convert_alpha()
# b_cred_lilac = pygame.transform.scale(b_cred_lilac, (600, 150))

exit_ = pygame.image.load(os.path.join(dir_img, "brown_exit_button.png")).convert_alpha()
# b_cont_pink = pygame.transform.scale(b_cont_pink, (600, 150))
exit_pressed = pygame.image.load(os.path.join(dir_img, "beige_exit_button.png")).convert_alpha()
# b_cont_lilac = pygame.transform.scale(b_cont_lilac, (600, 150))


window.blit(home, (0, 0))


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

    def bye_bye(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True

        return False


init_button = Button(380, 300, start_, start_pressed)
cred_button = Button(380, 500, credits_, credits_pressed)
exit_button = Button(380, 700, exit_, exit_pressed)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    bye = exit_button.bye_bye()
    if bye:
        run = False

    init_button.draw()
    cred_button.draw()
    exit_button.draw()

    pygame.display.update()
