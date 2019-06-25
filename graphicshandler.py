import pygame
from sprites import SpritesContainer

class GraphicsHandler:
	def __init__(self):
		self.sprites_container = SpritesContainer()

	def draw_tank_body(self, x :int, y :int, body_model :str ):
		self.screen.blit(self.sprites_container.tank_body_sprites[body_model],  (x, y))

