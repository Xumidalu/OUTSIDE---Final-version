import pygame
import os

main_dir = os.path.dirname(__file__)
dir_img = os.path.join(main_dir, "img")


def img_cut(img_name, in_x, in_y):
    a = pygame.image.load(os.path.join(dir_img, img_name)).convert_alpha()
    a = pygame.transform.scale(a, (in_x, in_y))
    return a


def img(img_name):
    a = pygame.image.load(os.path.join(dir_img, img_name)).convert_alpha()
    return a