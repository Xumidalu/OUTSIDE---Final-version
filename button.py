import pygame
pygame.init()
x, y = 1600, 900
window = pygame.display.set_mode([x, y])

click_sound = pygame.mixer.Sound('mouse-click-153941.mp3')


class Button:
    def __init__(self, x_axis, y_axis, image1, image2):
        self.image1 = image1
        self.image2 = image2
        self.image = image1
        self.rect = self.image.get_rect()
        self.rect.center = (x_axis, y_axis)
        self.showing = True
        self.varControle = 0

    def draw(self):
        if self.showing:
            self.varControle += 1
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.image = self.image2
            else:
                self.image = self.image1

            window.blit(self.image, (self.rect.x, self.rect.y))

    def bye_bye(self):
        self.showing = False

    def check_click(self):
        if self.showing:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] and self.varControle > 100:
                    click_sound.play()
                    self.varControle = 0
                    return True

