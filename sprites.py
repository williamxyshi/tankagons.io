import pygame
import os


class SpritesContainer:
    def __init__(self):
        self.tank_body_sprites = {'basic': pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets\\basetank.png'))}