import pygame
from sprites import SpritesContainer
width = 1440
height = 900

class GraphicsHandler:
	def __init__(self):
		self.sprites_container = SpritesContainer()
		self.screen = pygame.display.set_mode((width, height))

	def update_display(self, data):
		self.screen.fill((0, 0, 0))
		self.update_tank_body(data["tanks"])
		pygame.display.update()

	def draw_tank_body(self, x :int, y :int, body_model :str ):
		self.screen.blit(self.sprites_container.tank_body_sprites[body_model],  (x, y))

	def update_tank_body(self, data):
		for tank in data.values():
			self.draw_tank_body( tank.x, tank.y, tank.tank_body_model)