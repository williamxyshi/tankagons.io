import pygame
import os


class SpritesContainer:
    def __init__(self):
        self.background_sprite = pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets\\background.png'))
        self.tank_body_sprites = {'basic': pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets\\basetank.png'))}
        self.tank_turret_sprites = {'basic': pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets\\baseturret.png'))}
        self.bullet_sprites = {'bullet': pygame.image.load(os.path.join(os.path.dirname(__file__), 'assets\\bullet.png'))}

